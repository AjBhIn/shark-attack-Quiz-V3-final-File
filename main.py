# Importing take place here
import pygame as pg
import sys
import race_track as rt
import white_board as wt
import question_answers as qs
from datetime import datetime as dt
import scene as sc
import tracker as ds

class Game:
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

        # Telll the loop function if it is time for the next question as well stores te value for the next question number
        self.moving_to_next = False
        self.question_number = 0
        self.total_question_len = qs.num_questions_answers - 2
        self.current_time = 0
        self.button_pressed_time = 0
        self.next_ques_in = 2
        self.updates_ques_num = 0
        self.wrong_question_num = 0

        # Adding shark
        self.shark = sc.Shark("shark.png", (120, 305))
        sc.shark_sprite.add(self.shark)

        #Adding water
        self.water = sc.Scene("WATER.png", (1008, 347))
        sc.scene_sprities.add(self.water)
        
        # Adding island
        self.island = sc.Scene("island.png", (1042, 347))
        sc.scene_sprities.add(self.island)

        # Distance covered
        self.distance = 1000
        self.var = f"Away from Shore {self.distance}m"

        # "Question on" texts
        self.question_on = 1 + len(qs.answer_check)
        self.question_on_text = f"Question {self.question_on}/{len(qs.class_question_list)}"

        # Display
            # Colors
        self.correct_answer_color = (247, 255, 247)
        self.wrong_answer_color = (255, 107, 107)
        self.display_text_color = self.correct_answer_color
        self.display_string = "Finished"
        self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
        self.display_text_placement = (self.display_string_x, 368)
        self.display_background = pg.image.load("display.png").convert_alpha()
        self.display_background_rect = self.display_background.get_rect(center = (int(self.window.get_width()/2), 368))

        self.evn = pg.USEREVENT + 1
        pg.time.set_timer(self.evn, 2000)

    def looper(self):
        while True:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if self.question_number < (len(qs.class_question_list) - 1): # Minusing 2 from the original list of question to keep it below the last question:
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
                                if int(self.time.total_seconds()) > self.next_ques_in:
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

                            # Updating the question number
                            self.question_on = len(qs.answer_check) + 1

                            # Display update
                            self.display_string = "NONE"
                            self.display_text_color = self.correct_answer_color
                            self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                            self.display_text_placement = (self.display_string_x, 368)
    
                else:
                    self.question_number = self.question_number
                    qs.question_ans_num = self.question_number

                if events.type == self.evn:
                    self.distance -= 100
                    self.var = f"Away from Shore {self.distance}m"

            # Updating question number
            self.question_on_text = f"Question {self.question_on}/{len(qs.class_question_list)}"
                        
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
            sc.scene_sprities.draw(self.window)
            sc.scene_sprities.draw(self.window)

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
            
            if button_pressed_1 == True or button_pressed_2 == True or button_pressed_3 == True or button_pressed_4 == True:
                self.button_pressed_time = dt.now()
                if qs.answer_check[len(qs.answer_check) - 1] == False:
                    self.display_string = "Wrong"
                    self.display_text_color = self.wrong_answer_color
                    self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                    self.display_text_placement = (self.display_string_x, 368)
                else:
                    self.display_string = "Correct"
                    self.display_text_color = self.correct_answer_color
                    self.display_string_x = int(self.window.get_width()/2) - int(ds.jura_medium.size(self.display_string)[0]/2)
                    self.display_text_placement = (self.display_string_x, 368)


            # Putting a custom cursor
            pg.mouse.set_cursor(self.cursor)

            # Updating the game
            pg.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    game = Game()
    game.looper()

# Q3,(2x + 3x) = 10, x = 2,x = 5,x = 1,x = 2.5, x = 2
# Q4,What is School Speed Zone ?,40,50 ,20 ,30,40
# Q5,New Zealand Captical ?,Welligton,Auckland,Waikto,Christchurch,Welligton
# Q6,Formula for Power ?,P = W/t,P = A/F,W = Fd,v = d/t,P = W/t