# Importing take place here
import pygame as pg
import sys
import white_board as wt
import question_answers as qs
from datetime import datetime as dt
import scene as sc
import tracker as ds
import ending as ed
import exit as ex

class Game:

    def Next_question(self):
        if self.question_number < self.question_len_main: # Minusing 1 from the original list of question to keep it below the last question:
            if self.moving_to_next:
                # Checking if it is time to move to next question
                self.current_time = dt.now()
                self.time = (self.current_time - self.button_pressed_time)
                if int(self.time.total_seconds()) > self.next_ques_in:
                    pass
                else:
                    while True:
                        self.current_time = dt.now()
                        self.time = (self.current_time - self.button_pressed_time)
                        if self.time.total_seconds() > self.next_ques_in:
                            break

                if int(self.time.total_seconds()) > self.next_ques_in:
                    qs.class_question_list[self.question_number].next_question()
                    qs.class_answer_list[self.question_number][0].next_ans()
                    qs.class_answer_list[self.question_number][1].next_ans()
                    qs.class_answer_list[self.question_number][2].next_ans()
                    qs.class_answer_list[self.question_number][3].next_ans()
                    qs.button_states[0] = False
                    qs.button_states[1] = False
                    qs.button_states[2] = False
                    qs.button_states[3] = False
                    self.question_number += 1
                    self.updates_ques_num = self.question_number
                    qs.question_spirit.add(qs.class_question_list[self.question_number])
                    qs.answers_spirit.add(qs.class_answer_list[self.question_number])
                    qs.question_ans_num = self.question_number
                    self.moving_to_next = False

                    # Updating the dashboard
                    self.question_on_text = f"Mistakes {qs.answer_check.count(False)}/{self.num_shark_moves - 1}"
                    self.var = f"Away from Shore {self.distance}m"

        else:
            self.question_number = self.question_number
            qs.question_ans_num = self.question_number
            if self.shark_x_position_new == self.swimmer_x_position_new:
                pass
            elif self.swimmer_x_position_new >= int(self.water_width - 20):
                pass
            else:
                self.in_middle = True

    def Shark_collied(self):
        if pg.sprite.spritecollide(sc.swimmer_sprite.sprite, sc.shark_sprite, False):
            ed.dead_sprite.add(self.blood_scene)
            ed.ending_string_sprit.add(self.failed_string)
            ex.exit_bt_sprite.add(self.exit_button)
            if self.question_number < 3:
                ex.exit_message_sprite.add(self.exit_message_3)
            else:
                ex.exit_message_sprite.add(self.exit_message_2)

            # Updatig the position of the finishing scene
            self.dead_image_y += 1
            if self.dead_image_y >= 0:
                self.dead_image_y = 0
            else:
                pass

            self.question_on_text = f"Mistakes {qs.answer_check.count(False)}/{self.num_shark_moves - 1}"
            # Reseting
            self.question_len_main = (len(qs.class_question_list) - 3)
            qs.answers_spirit.empty()
            qs.question_spirit.empty()
            qs.line_spirit.empty()

            # Putting finsihed text on the display
            self.display_string = "Finished"
            self.display_text_color = self.correct_answer_color
            self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
            self.display_text_placement = (self.display_string_x, 368)

            self.distance = "Unknown"
            self.var = f"Away from Shore {self.distance}m"

    def Island_collied(self):
        if pg.sprite.spritecollide(sc.swimmer_sprite.sprite, sc.island_sprities, False):
                # Adding the instance to game (not displaying them yet)
                ed.ending_string_sprit.add(self.passed_string)
                ed.ending_string_sprit.add(self.passed_description)
                ed.ending_score_sprit.add(self.passed_rate)
                ex.exit_message_sprite.add(self.exit_message_1)
                ex.exit_bt_sprite.add(self.exit_button)

                # This statements will make sure to run code only onces
                if self.collied_island:
                    self.finished_game_in = int(pg.time.get_ticks() // 1000)
                    self.passed_rate_text = f"{self.finished_game_in}s"

                    # Putting finsihed text on the display
                    self.display_string = "Finished"
                    self.display_text_color = self.correct_answer_color
                    self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                    self.display_text_placement = (self.display_string_x, 368)

                    # Reseting
                    self.question_len_main = (len(qs.class_question_list) - 2)
                    qs.answers_spirit.empty()
                    qs.question_spirit.empty()
                    qs.line_spirit.empty()

                    self.collied_island = False

                self.var = f"Away from Shore {self.distance}m"

    def Main_stage(self):
        for events in pg.event.get():
                if events.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if events.type == self.next_que_event:
                    if self.moving_to_next:
                        if self.display_string == "Wrong":
                            if self.shark_x_position_new >= self.shark_x_position:
                                self.Next_question()
                        elif self.display_string == "Correct":
                            if self.swimmer_x_position_new >= self.swimmer_x_position:
                                self.Next_question()
                    
        # Putting colours on the window
        self.window.fill(self.window_bg)
        self.current_time = pg.time.get_ticks()

        # Putting the white board on the screen
        self.window.blit(wt.main_board.surface, (0, 347))
        wt.main_board.surface.blit(wt.display_board.surface, (0, 40))

        # Dashboard
        self.distance_text = ds.Dashboard(self.window, (22, 368), ds.jura_regular, self.var)
        self.question_num_text = ds.Dashboard(self.window, (900, 368), ds.jura_regular, self.question_on_text)
        self.window.blit(self.display_background, self.display_background_rect)
        self.display_text = ds.Dashboard(self.window, self.display_text_placement, ds.jura_medium, self.display_string, self.display_text_color )

        # Scene
        sc.shark_sprite.draw(self.window)
        sc.swimmer_sprite.draw(self.window)
        sc.ocean_sprities.draw(self.window)
        sc.island_sprities.draw(self.window)

        # Finishing the text
        ed.dead_sprite.draw(self.window)
        ed.ending_string_sprit.draw(self.window)
        ed.ending_score_sprit.draw(self.window)

        # Exit screen draw
        ex.exit_bt_sprite.draw(self.window)
        ex.exit_message_sprite.draw(self.window)
        ex.exit_bt_sprite.update()

        # Putting the results
        self.score = qs.answer_check.count(True)
        self.passed_rate_text = f"{self.finished_game_in}s"
        
        # Updating finishing text and Finishing scene
        ed.ending_score_sprit.update(self.passed_rate_text)
        ed.dead_sprite.update(self.dead_image_y)

        # Scenes update
        sc.ocean_sprities.update()
        sc.island_sprities.update()

        # Putting the questions on the screen
        qs.question_spirit.draw(self.window)
        qs.class_question_list[self.question_number].update()
        qs.line_spirit.draw(self.window)

        # Putting the options on the screen
        qs.answers_spirit.draw(self.window)
        button_pressed_1 = qs.class_answer_list[self.question_number][0].update()
        button_pressed_2 = qs.class_answer_list[self.question_number][1].update()
        button_pressed_3 = qs.class_answer_list[self.question_number][2].update()
        button_pressed_4 = qs.class_answer_list[self.question_number][3].update()

        if True in qs.button_states:
            self.moving_to_next = True
            # Telling the computer put an event for the computer can detect an even easily in the event section
            pg.event.post(pg.event.Event(self.next_que_event))

        if button_pressed_1 == True or button_pressed_2 == True or button_pressed_3 == True or button_pressed_4 == True:
            self.button_pressed_time = dt.now()
            if qs.answer_check[len(qs.answer_check) - 1] == False:
                self.display_string = "Wrong"
                self.display_text_color = self.wrong_answer_color
                self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                self.display_text_placement = (self.display_string_x, 368)
                # Also moves the shark
                self.shark_x_position += self.displacement

            elif qs.answer_check[len(qs.answer_check) - 1] == True:
                self.display_string = "Correct"
                self.display_text_color = self.correct_answer_color
                self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                self.display_text_placement = (self.display_string_x, 368)
                # Also moves the swimmer
                self.swimmer_x_position += self.displacement

                # Updating the distance
                self.distance -= self.displacement
                if self.distance < 10:
                    self.distance = 0
                else:
                    pass
            else:
                pass

        sc.shark_sprite.update(self.shark_x_position_new)
        if self.shark_x_position_new < self.shark_x_position:
            self.shark_x_position_new += int(self.shark_steps)
            self.shark_steps += int(0.9)
        
        sc.swimmer_sprite.update(self.swimmer_x_position_new)
        if self.swimmer_x_position_new < self.swimmer_x_position:
            self.swimmer_x_position_new += int(self.swimmer_steps)
            self.swimmer_steps += int(0.1)

        if self.in_middle:
            sc.shark_sprite.update(self.shark_x_position_new)
            if self.shark_x_position_new < self.swimmer_x_position_new:
                self.shark_x_position_new += int(self.shark_steps)
                self.shark_steps += int(0.9)
            
        # Putting a custom cursor
        pg.mouse.set_cursor(self.cursor)

        # Updating the game
        pg.display.update()

    def __init__(self):
        # Settings for the window
        self.WIDTH = 1042
        self.HEIGHT = 697
        self.FPS = 90

        # Starting pygame
        pg.init()

        # Setting up the window
        self.window = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("QUIZ RACE")
        self.ICON_IMAGE = pg.image.load("icon.png")
        pg.display.set_icon(self.ICON_IMAGE)
        self.clock = pg.time.Clock()

        # Colours for the window
        self.window_bg = (247, 247, 247)

        # Custom cursor
        self.image_of_cursor = pg.image.load("cursor (1).png") # image of the cursor
        self.image_of_cursor_rotate = pg.transform.rotozoom(self.image_of_cursor, 30, 1)  # rotating the image
        self.cursor = pg.cursors.Cursor((11, 12), self.image_of_cursor_rotate) # putting the image in cursor widget

        # Tell the loop function if it is time for the next question as well stores te value for the next question number
        self.moving_to_next = False
        self.question_number = 0
        self.question_len_main = (len(qs.class_question_list) - 1)
        self.total_question_len = qs.num_questions_answers - 2
        self.current_time = 0
        self.button_pressed_time = 0
        self.next_ques_in = 2
        self.updates_ques_num = 0
        self.wrong_question_num = 0

        # Settings movement for shark and player
        self.water_width = 940
        self.total_questions = qs.actual_que_num_v2
        self.num_shark_moves = 2
        self.in_middle = False

        # The Equation for dividing the arean in interger
        self.displacement = int(self.water_width/(self.total_questions + self.num_shark_moves))

        # Adding shark
        self.shark_x_position = self.displacement
        self.shark_x_position_new = self.displacement
        self.shark_steps = 1
        self.shark = sc.Shark("shark.png", (self.shark_x_position, 305))
        sc.shark_sprite.add(self.shark)

        # Adding swimmer
        self.swimmer_x_position = self.displacement * (self.num_shark_moves + 1)
        self.swimmer_x_position_new = self.displacement * (self.num_shark_moves + 1)
        self.swimmer_steps = 1
        self.swimmer = sc.Swimmer("swim.png", (self.swimmer_x_position, 305))
        sc.swimmer_sprite.add(self.swimmer)

        #Adding water
        self.ocean = sc.Ocean("WATER.png", (1008, 347))
        sc.ocean_sprities.add(self.ocean)
        
        # Adding island
        self.collied_island = True
        self.island = sc.Island("island.png", (1042, 347))
        sc.island_sprities.add(self.island)

        # Distance covered
        self.distance = self.water_width - self.swimmer_x_position
        self.var = f"Away from Shore {self.distance}m"

        # Mistakes texts
        self.question_on_text = f"Mistakes {0}/{self.num_shark_moves - 1}"

        # Ending Text
        # Instance of class
        self.finished_game_in = 0
        self.passed_rate_text = f"{self.finished_game_in}s"
        self.failed_string =  ed.Endingtext("YOU DIED", 1042, 165)
        self.passed_string =  ed.Endingtext("JAWS ESCAPED", 1042, 155)
        self.passed_description =  ed.Endingtext("You Have Escaped the Jaws in", 1042, 210, 18)
        self.passed_rate =  ed.Scoretext(self.passed_rate_text, 1042, 245, 35)

        # Ending scene images and instances
        self.dead_image_y = -200
        self.blood_scene = ed.Deadscene("dead image.png", (0, self.dead_image_y))

        # Displayed.
            # Colors
        self.correct_answer_color = (247, 255, 247)
        self.wrong_answer_color = (255, 107, 107)
        self.display_text_color = self.correct_answer_color
        self.display_string = "Finished"
        self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
        self.display_text_placement = (self.display_string_x, 368)
        self.display_background = pg.image.load("display.png").convert_alpha()
        self.display_background_rect = self.display_background.get_rect(center = (int(self.window.get_width()/2), 368))

        # Exit Screen
        self.exit_button  =  ex.Exitbutton(int(self.window.get_width()/2))
        self.exit_message_1 = ex.Exitmessage("You have escaped the Jaws.", "Well Done!", "nerd.png")
        self.exit_message_2 = ex.Exitmessage("Could not escape the Island.", "Try Again!", "crying.png")
        self.exit_message_3 = ex.Exitmessage("Hmmmmmmmmmmmmmmmmmmmmmmm", "Try Again!", "angry.png")

        # User event to for moving to Next Question
        self.next_que_event = pg.USEREVENT + 1

    def looper(self):
        while True:
            self.Main_stage()
            self.Shark_collied()
            self.Island_collied()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    game = Game()
    game.looper()

# Q3,(2x + 3x) = 10, x = 2,x = 5,x = 1,x = 2.5, x = 2
# Q4,What is School Speed Zone ?,40,50 ,20 ,30,40
# Q5,New Zealand Captical ?,Welligton,Auckland,Waikto,Christchurch,Welligton
# Q6,Formula for Power ?,P = W/t,P = A/F,W = Fd,v = d/t,P = W/t