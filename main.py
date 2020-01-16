import pickle
import os
import pandas as pd
import tkinter as tk
from tkinter import *

# file_path = os.path.join('model_files','model_70.sav')
# loaded_model = pickle.load(open(file_path, 'rb'))
#
# user_input = [
#     {
#         'LIST_PRICE': 100000,
#         'ISFEATURED': 0,
#         'ISRENTGUARANTEED': 1,
#         'NEIGHBORHOODSCORE': 4,
#         'COMPUTEDLEVEREDCASHONCASH': 0.09,
#         'COMPUTEDTOTALRETURN': 1000,
#         'EST_REPAIR_COST': 2000,
#         'PERC': 20
#     }
# ]
# user_input = pd.DataFrame(user_input)
# result = loaded_model.predict_expectation(user_input).values[0, 0]
#
# print(result)


class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.master.title("Welcome use RoofStock Pricing Kit")

        self.LIST_PRICE = StringVar()
        self.EST_PRICE = StringVar()
        self.ISFEATURED = StringVar()
        self.ISRENTGUARANTEED = StringVar()
        self.NEIGHBORHOODSCORE = StringVar()
        self.COMPUTEDLEVEREDCASHONCASH = StringVar()
        self.COMPUTEDTOTALRETURN = StringVar()
        self.EST_REPAIR_COST = StringVar()
        self.WATITIME = StringVar()
        #self.PERC = StringVar()

        self.top_frame = Frame(self.master)
        self.down_frame = LabelFrame(self.master, text='Result')

        self.top_frame.grid()
        self.down_frame.grid()

        self.offer_prob_70 = StringVar()
        self.offer_prob_75 = StringVar()
        self.offer_prob_80 = StringVar()
        self.offer_prob_85 = StringVar()
        self.offer_prob_90 = StringVar()
        self.offer_prob_95 = StringVar()

        self.median_time_70 = StringVar()
        self.median_time_75 = StringVar()
        self.median_time_80 = StringVar()
        self.median_time_85 = StringVar()
        self.median_time_90 = StringVar()
        self.median_time_95 = StringVar()

        self.expected_time_70 = StringVar()
        self.expected_time_75 = StringVar()
        self.expected_time_80 = StringVar()
        self.expected_time_85 = StringVar()
        self.expected_time_90 = StringVar()
        self.expected_time_95 = StringVar()

        self.create_top(self.top_frame)
        self.create_down(self.down_frame)
        self.load_models()

    def create_top(self, local_frame):
        self.top_left_frame = LabelFrame(local_frame, text='User Input:')
        self.top_right_frame = LabelFrame(local_frame, text='Control:')
        self.top_left_frame.grid(row=0, column=0)
        self.top_right_frame.grid(row=0, column=1)

        input_Label_list_price = Label(self.top_left_frame, text='List Price')
        input_Label_est_price = Label(self.top_left_frame, text='EST Value')
        input_Label_is_featured = Label(self.top_left_frame,text='Is Featured')
        input_Label_rent_guaranteed = Label(self.top_left_frame,text='Rent Guaranteed')
        input_Label_neighborhood_score = Label(self.top_left_frame,text='Neighborhood Score')
        input_Label_cash_on_cash = Label(self.top_left_frame,text='Cash on Cash Return')
        input_Label_total_return = Label(self.top_left_frame,text='Total Return')
        input_Label_est_repair_cost = Label(self.top_left_frame,text='EST Repair Cost')
        input_Label_waiting_time = Label(self.top_left_frame,text='Acceptable Waiting Time (Days)')

        input_Label_list_price.grid(column=0,row=0)
        input_Label_est_price.grid(column=0,row=1)
        input_Label_is_featured.grid(column=0,row=2)
        input_Label_rent_guaranteed.grid(column=0,row=3)
        input_Label_neighborhood_score.grid(column=0,row=4)
        input_Label_cash_on_cash.grid(column=0,row=5)
        input_Label_total_return.grid(column=0,row=6)
        input_Label_est_repair_cost.grid(column=0,row=7)
        input_Label_waiting_time.grid(column=0,row=8)

        self.entry_LIST_PRICE = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.LIST_PRICE)
        self.entry_EST_PRICE = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.EST_PRICE)
        self.entry_ISFEATURED = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.ISFEATURED)
        self.entry_ISRENTGUARANTEED = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.ISRENTGUARANTEED)
        self.entry_NEIGHBORHOODSCORE = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.NEIGHBORHOODSCORE)
        self.entry_COMPUTEDLEVEREDCASHONCASH = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.COMPUTEDLEVEREDCASHONCASH)
        self.entry_COMPUTEDTOTALRETURN = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.COMPUTEDTOTALRETURN)
        self.entry_EST_REPAIR_COST = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.EST_REPAIR_COST)
        self.entry_WATITIME = Entry(self.top_left_frame, width= 15,justify = 'right', textvariable=self.WATITIME)

        self.entry_LIST_PRICE.grid(sticky = (W),column=1,row=0)
        self.entry_EST_PRICE.grid(sticky = (W),column=1,row=1)
        self.entry_ISFEATURED.grid(sticky = (W),column=1,row=2)
        self.entry_ISRENTGUARANTEED.grid(sticky = (W),column=1,row=3)
        self.entry_NEIGHBORHOODSCORE.grid(sticky = (W),column=1,row=4)
        self.entry_COMPUTEDLEVEREDCASHONCASH.grid(sticky = (W),column=1,row=5)
        self.entry_COMPUTEDTOTALRETURN.grid(sticky = (W),column=1,row=6)
        self.entry_EST_REPAIR_COST.grid(sticky = (W),column=1,row=7)
        self.entry_WATITIME.grid(sticky = (W),column=1,row=8)

        self.run_btn = Button(self.top_right_frame,text='Get Estimation')
        self.run_btn['command'] = self.get_result

        self.reset_btn = Button(self.top_right_frame, text='Reset Program')
        self.reset_btn['command'] = self.reset_input

        self.quit_btn = Button(self.top_right_frame, text='Quit')
        self.quit_btn['command']=self.master.quit

        self.run_btn.grid(row=0)
        self.reset_btn.grid(row=1)
        self.quit_btn.grid(row=2)


    def create_down(self, local_frame):
        label_good_offer_bar = Label(local_frame,text='Good Offer %')
        label_good_offer_prob = Label(local_frame,text='Probability [Get Offer Within Waiting Time]')
        label_survival_median = Label(local_frame,text='Expected Waiting Time [Median]')
        label_expection = Label(local_frame,text='Expected Waiting Time')

        label_good_offer_bar.grid(row=0,column=0)
        label_good_offer_prob.grid(row=0,column=1)
        label_survival_median.grid(row=0,column=2)
        label_expection.grid(row=0,column=3)

        label_good_offer_70 = Label(local_frame, text='70 %')
        label_good_offer_75 = Label(local_frame, text='75 %')
        label_good_offer_80 = Label(local_frame, text='80 %')
        label_good_offer_85 = Label(local_frame, text='85 %')
        label_good_offer_90 = Label(local_frame, text='90 %')
        label_good_offer_95 = Label(local_frame, text='95 %')

        label_good_offer_70.grid(column=0,row=1,sticky=W)
        label_good_offer_75.grid(column=0,row=2,sticky=W)
        label_good_offer_80.grid(column=0,row=3,sticky=W)
        label_good_offer_85.grid(column=0,row=4,sticky=W)
        label_good_offer_90.grid(column=0,row=5,sticky=W)
        label_good_offer_95.grid(column=0,row=6,sticky=W)

        Entry(local_frame,textvariable=self.offer_prob_70).grid(row=1,column=1)
        Entry(local_frame,textvariable=self.offer_prob_75).grid(row=2,column=1)
        Entry(local_frame,textvariable=self.offer_prob_80).grid(row=3,column=1)
        Entry(local_frame,textvariable=self.offer_prob_85).grid(row=4,column=1)
        Entry(local_frame,textvariable=self.offer_prob_90).grid(row=5,column=1)
        Entry(local_frame,textvariable=self.offer_prob_95).grid(row=6,column=1)

        Entry(local_frame,textvariable=self.median_time_70).grid(row=1,column=2)
        Entry(local_frame,textvariable=self.median_time_75).grid(row=2,column=2)
        Entry(local_frame,textvariable=self.median_time_80).grid(row=3,column=2)
        Entry(local_frame,textvariable=self.median_time_85).grid(row=4,column=2)
        Entry(local_frame,textvariable=self.median_time_90).grid(row=5,column=2)
        Entry(local_frame,textvariable=self.median_time_95).grid(row=6,column=2)

        Entry(local_frame,textvariable=self.expected_time_70).grid(row=1,column=3)
        Entry(local_frame,textvariable=self.expected_time_75).grid(row=2,column=3)
        Entry(local_frame,textvariable=self.expected_time_80).grid(row=3,column=3)
        Entry(local_frame,textvariable=self.expected_time_85).grid(row=4,column=3)
        Entry(local_frame,textvariable=self.expected_time_90).grid(row=5,column=3)
        Entry(local_frame,textvariable=self.expected_time_95).grid(row=6,column=3)

    def load_models(self):
        file_path_70 = os.path.join('model_files', 'model_70.sav')
        file_path_75 = os.path.join('model_files', 'model_75.sav')
        file_path_80 = os.path.join('model_files', 'model_80.sav')
        file_path_85 = os.path.join('model_files', 'model_85.sav')
        file_path_90 = os.path.join('model_files', 'model_90.sav')
        file_path_95 = os.path.join('model_files', 'model_95.sav')

        self.cph_70 = pickle.load(open(file_path_70, 'rb'))
        self.cph_75 = pickle.load(open(file_path_75, 'rb'))
        self.cph_80 = pickle.load(open(file_path_80, 'rb'))
        self.cph_85 = pickle.load(open(file_path_85, 'rb'))
        self.cph_90 = pickle.load(open(file_path_90, 'rb'))
        self.cph_95 = pickle.load(open(file_path_95, 'rb'))

        # user_input = [
        #     {
        #         'LIST_PRICE': 100000,
        #         'ISFEATURED': 0,
        #         'ISRENTGUARANTEED': 1,
        #         'NEIGHBORHOODSCORE': 4,
        #         'COMPUTEDLEVEREDCASHONCASH': 0.09,
        #         'COMPUTEDTOTALRETURN': 1000,
        #         'EST_REPAIR_COST': 2000,
        #         'PERC': 20
        #     }
        # ]
        # user_input = pd.DataFrame(user_input)
        # result = self.cph_75.predict_expectation(user_input).values[0, 0]
        #
        # print(result)

    def reset_input(self):
        self.LIST_PRICE.set('')
        self.EST_PRICE.set('')
        self.ISFEATURED.set('')
        self.ISRENTGUARANTEED.set('')
        self.NEIGHBORHOODSCORE.set('')
        self.COMPUTEDLEVEREDCASHONCASH.set('')
        self.COMPUTEDTOTALRETURN.set('')
        self.EST_REPAIR_COST.set('')
        self.WATITIME.set('')

    def get_result(self):
        user_input_list = []
        #list_price = self.LIST_PRICE.get()
        user_input_dict = {
            'LIST_PRICE': float(self.LIST_PRICE.get()),
            'ISFEATURED': bool(self.ISFEATURED.get()),
            'ISRENTGUARANTEED': bool(self.ISRENTGUARANTEED.get()),
            'NEIGHBORHOODSCORE': float(self.NEIGHBORHOODSCORE.get()),
            'COMPUTEDLEVEREDCASHONCASH': float(self.COMPUTEDLEVEREDCASHONCASH.get()),
            'COMPUTEDTOTALRETURN': float(self.COMPUTEDTOTALRETURN.get()),
            'EST_REPAIR_COST': float(self.EST_REPAIR_COST.get()),
            'PERC': (float(self.LIST_PRICE.get())/float(self.EST_PRICE.get()) - 1) * 100
        }

        user_input_list.append(user_input_dict)
        user_input_pd = pd.DataFrame(user_input_list)
        waiting_time = int(self.WATITIME.get())

        self.offer_prob_70.set(str((1-self.cph_70.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))
        self.offer_prob_75.set(str((1-self.cph_75.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))
        self.offer_prob_80.set(str((1-self.cph_80.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))
        self.offer_prob_85.set(str((1-self.cph_85.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))
        self.offer_prob_90.set(str((1-self.cph_90.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))
        self.offer_prob_95.set(str((1-self.cph_95.predict_survival_function(user_input_pd,waiting_time).values[0, 0])*100))

        self.median_time_70.set(str(self.cph_70.predict_median(user_input_pd)))
        self.median_time_75.set(str(self.cph_75.predict_median(user_input_pd)))
        self.median_time_80.set(str(self.cph_80.predict_median(user_input_pd)))
        self.median_time_85.set(str(self.cph_85.predict_median(user_input_pd)))
        self.median_time_90.set(str(self.cph_90.predict_median(user_input_pd)))
        self.median_time_95.set(str(self.cph_95.predict_median(user_input_pd)))

        self.expected_time_70.set(str(self.cph_70.predict_expectation(user_input_pd).values[0, 0]))
        self.expected_time_75.set(str(self.cph_75.predict_expectation(user_input_pd).values[0, 0]))
        self.expected_time_80.set(str(self.cph_80.predict_expectation(user_input_pd).values[0, 0]))
        self.expected_time_85.set(str(self.cph_85.predict_expectation(user_input_pd).values[0, 0]))
        self.expected_time_90.set(str(self.cph_90.predict_expectation(user_input_pd).values[0, 0]))
        self.expected_time_95.set(str(self.cph_95.predict_expectation(user_input_pd).values[0, 0]))

root = tk.Tk()
app = Application(master=root)
app.mainloop()