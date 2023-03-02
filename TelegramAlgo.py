import os
import sys
#import time
#import string
import math
import re
import csv
import asyncio
#import datetime as dt
import pandas as pd
#import numpy as np
import os.path
import telepot 
import datetime
#from datetime import datetime, timedelta, time
from datetime import timedelta, time
from telethon.sync import TelegramClient
#from telethon import functions, types, events, utils
from telethon import events, utils
#from telethon.tl.custom import Button
from kiteconnect import KiteConnect
#from tabulate import tabulate 
from time import sleep
from os import path
#from numpy import random
pd.options.mode.chained_assignment = None
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

global PrimeQueue
global MyPrimeQueuePL
global startProcessMyQueue
global ForceExit
global ForceExitACTIVE
global ForceExitPENDING
global ForceExitACTIVEQueue
global ForceExitPENDINGQueue
global OkToForceExit
global ScalpBANKNIFTY
global SendMorningMessage

global LastCallHour
global LastCallMin

global TakeProfitPcent
global StopLossPcent
global MinTakeProfit
global MinStopLoss
global TradeStartHour
global TradeStartMinute
global TradeStartSecond
global NoNewEntryHour
global NoNewEntryMinute
global TradeCloseHour
global TradeCloseMinute
global IamTestingNow
global CheckTradeCloseHour
global SendMesageToTelegram
global PlaySafeStopLossPcentChk
global PlaySafeStopLossTrailLow
global PlaySafeStopLossTrailHigh
global MaxBudget
global MaxLotSize
global TestStepInc
global TestStepIncVal
global TestStepDec
global TestStepDecVal
global TakeProfitLoopPcent
global StopLossLoopPcent
global MaxEntryCutOff
global settings_df
global DefMinTime
global DefMaxTime
global DefTakeProfitPcent
global DefStopLossPcent
global DefMinEntryPriceRange
global DefMaxEntryPriceRange
global DefFixTakeProfitPcent
global DefFixStopLossPcent
global SingleSLPLLow
global SingleSLPLHigh
global SingleSLPLLowT
global SingleSLPLHighT
global SingleSLPLLowS
global SingleSLPLHighS
global SingleSLPLLowQ
global SingleSLPLHighQ
global SingleSLPLLowL
global SingleSLPLHighL
global SelectedSLPLLow
global SelectedSLPLHigh

global SingleSLPLHighTime
global SingleSLPLLowTime
global SingleSLPLHighTimeT
global SingleSLPLLowTimeT
global SingleSLPLHighTimeS
global SingleSLPLLowTimeS
global SingleSLPLHighTimeQ
global SingleSLPLLowTimeQ
global SingleSLPLHighTimeL
global SingleSLPLLowTimeL
global SelectedSLPLLowTime
global SelectedSLPLHighTime
global TempPLQueuePrev
global DoHedgeTrade
global TestStepIncStop
global TestStepDecStop
global Msg1
global TmpMsg1
global Msg2
global TmpMsg2
global Msg3
global TmpMsg3
global Msg4
global TmpMsg4
    
def act(x):
    return x+10

def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.datetime.now().time(): # you can add here any additional variable to break loop if necessary
        sleep(10)# you can change 1 sec interval to any other
    return action
    
    
#Set Default Values
TakeProfitPcent = 0.05 #this will increase upto 27.5% at 2.5% interval
StopLossPcent = 0.05

LastCallHour = 0
LastCallMin = 0

DefTakeProfitPcent = 0.15
DefStopLossPcent = 0.15
DefFixTakeProfitPcent = 0.15
DefFixStopLossPcent = 0.125

MinTakeProfit = 5
MinStopLoss = 5
MaxEntryCutOff = 10
TakeProfitLoopPcent = 0.025
StopLossLoopPcent = 0.025

SingleSLPLLow = 0
SingleSLPLHigh = 0
SingleSLPLLowT = 0
SingleSLPLHighT = 0
SingleSLPLLowS = 0
SingleSLPLHighS = 0
SingleSLPLLowQ = 0
SingleSLPLHighQ = 0
SingleSLPLLowL = 0
SingleSLPLHighL = 0
SelectedSLPLLow = 0
SelectedSLPLHigh = 0

IamTestingNow = False
WaitUntilMorining = True
RunFromMobile = True
SendMesageToTelegram = True

if IamTestingNow == True:
    now = datetime.datetime.now()
    now_plus = now + timedelta(minutes = 10)
    now_plus_str = datetime.datetime.strftime(now_plus, "%H:%M")
    ScriptWaitTime = '00:01'
    ScriptCloseTime = now_plus_str
    TradeStartHour = 0
    TradeStartMinute = 1
    TradeStartSecond = 5
    NoNewEntryHour = now_plus.hour
    NoNewEntryMinute = now_plus.minute
    TradeCloseHour = now_plus.hour
    TradeCloseMinute = now_plus.minute
    CheckTradeCloseHour = False
    PlaySafeStopLossPcentChk = 0.15
    PlaySafeStopLossTrailLow = 5
    PlaySafeStopLossTrailHigh = 20
    MaxBudget = 15000
    MaxLotSize = 50
    TestStepInc = True
    TestStepIncVal = 0.2
    TestStepIncStop = 300
    TestStepDecStop = 300
    TestStepDec = False
    TestStepDecVal = 0.2
    ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
    #ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
    DefMinTime = datetime.datetime.strptime(ThisDate+' 00:02:05.1', '%Y%m%d %H:%M:%S.%f')
    DefMaxTime = datetime.datetime.strptime(ThisDate+' 23:59:59.1', '%Y%m%d %H:%M:%S.%f')
    DefMinEntryPriceRange = 10
    DefMaxEntryPriceRange = 1000
    DoHedgeTrade = False
else:
    ScriptWaitTime = '09:00'
    ScriptCloseTime = '15:10'
    TradeStartHour = 9
    TradeStartMinute = 15
    TradeStartSecond = 1
    NoNewEntryHour = 15
    NoNewEntryMinute = 0
    TradeCloseHour = 15
    TradeCloseMinute = 10
    CheckTradeCloseHour = True
    PlaySafeStopLossPcentChk = 0.15
    PlaySafeStopLossTrailLow = 5
    PlaySafeStopLossTrailHigh = 20
    MaxBudget = 15000
    MaxLotSize = 50
    TestStepInc = False
    TestStepIncVal = 1
    TestStepIncStop = 6
    TestStepDecStop = 6
    TestStepDec = False
    TestStepDecVal = 1
    ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
    DefMinTime = datetime.datetime.strptime(ThisDate+' 09:15:00.1', '%Y%m%d %H:%M:%S.%f')
    DefMaxTime = datetime.datetime.strptime(ThisDate+' 15:00:00.1', '%Y%m%d %H:%M:%S.%f')
    DefMinEntryPriceRange = 10
    DefMaxEntryPriceRange = 4000
    DoHedgeTrade = False

if RunFromMobile == True:
    userSelf = 434371522 #+919916557445
    user = 434371522 #+918919460830
else:
    userSelf = 468457704 #+919916557445
    user = 434371522 #+918919460830

ForceExit = False
ForceExitACTIVE = False
ForceExitPENDING = False
ForceExitACTIVEQueue = False
ForceExitPENDINGQueue = False
OkToForceExit = False
startProcessMyQueue = 0

    

if WaitUntilMorining == True:
    startTime = time(*(map(int, ScriptWaitTime.split(':'))))
    endTime = time(*(map(int, ScriptCloseTime.split(':'))))
    print(startTime, datetime.datetime.now())
    if  datetime.datetime.now().time() > endTime:
        print('Waiting untill midnight', datetime.datetime.now())
        wait_start('23:59', lambda: act(100))
        print('Waiting untill pass mid night', datetime.datetime.now())
        sleep(120)
    print('Waiting untill morning', datetime.datetime.now())
    wait_start(ScriptWaitTime, lambda: act(100))

print('Starting now', datetime.datetime.now())


HolidayDates = pd.read_csv("HolidayDates.csv")
Today = datetime.datetime.now().date().strftime('%Y-%m-%d')
WeekNo = datetime.datetime.now().date().weekday()
IsTodayHoliday = pd.DataFrame()
IsTodayHoliday = HolidayDates[(HolidayDates['HolidayDate'] == Today)]
if len(IsTodayHoliday)>0 and IamTestingNow == False:
    print('Today Holiday')
    sys.exit()
elif WeekNo >= 5 and IamTestingNow == False:
    print('Today Weekend')
    sys.exit()
else:
    print('Today TradingDay')

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#get dump of all NSE instruments
HolidayDates = pd.read_csv("HolidayDates.csv")
fut_df = pd.read_csv("BNF_Instruments.csv")
nfo_df = pd.read_csv("NSE_Instruments.csv")
settings_df = pd.read_csv("TAG_Mapping.csv")
ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
#MyPrimeQueueCsv = 'MyPrimeQueue' + ThisDate + '_5.csv'
MyPrimeQueueLoadBackCsv = 'MyPrimeQueueLoadBack' + ThisDate + '_5.csv'
MyPrimeQueuePLCsv = 'MyPrimeQueuePL' + ThisDate + '_5.csv'

#Get or Create Queue DataFrame
if path.exists(MyPrimeQueueLoadBackCsv):
    PrimeQueue = pd.read_csv(MyPrimeQueueLoadBackCsv) 
else:
    PrimeQueue = pd.DataFrame(columns = ['tag', 'symbol', 'entry_price', 'entry_price2', 'spotprice', 'buy_price', 
        'high', 'low', 'ltp', 'inv_amount', 'quantity', 'logtime', 'ordertime', 
        'SL1', 'SLsell_price', 'SLP&L', 'SLP&LA', 'SLhigh', 'SLlow', 'SLltp', 'SLtime', 'SLMsg', 
        'T1', 'T1sell_price', 'T1P&L', 'T1P&LA', 'T1high', 'T1low', 'T1ltp', 'T1time', 'T1Msg', 
        'T2', 'T2sell_price', 'T2P&L', 'T2P&LA', 'T2high', 'T2low', 'T2ltp', 'T2time', 'T2Msg', 
        'T3', 'T3sell_price', 'T3P&L', 'T3P&LA', 'T3high', 'T3low', 'T3ltp', 'T3time', 'T3Msg', 
        'order_number', 'order_type', 'buy_sell', 'senderid', 'token', 'IndexEntry', 'IndexName', 
        'ChannelChk', 'ScriptRunMode', 'trailstoploss', 'PrintTime', 'CutOffCheck1', 'CutOffCheck2'])
    #PrimeQueue = pd.DataFrame(columns = ['symbol','entry_price','spotprice','buy_price','ltp','high','low','order_type', 'buy_sell', 'quantity', 'senderid', 'token', 'tag', 'order_number', 'logtime','ordertime','sell_price1','P&L1','stoploss1','takeprofit1','exitorder1','sell_price2','P&L2','stoploss2','takeprofit2','exitorder2','sell_price3','P&L3','stoploss3','takeprofit3','exitorder3','sell_price4','P&L4','stoploss4','takeprofit4','exitorder4','sell_price5','P&L5','stoploss5','takeprofit5','exitorder5','sell_price6','P&L6','stoploss6','takeprofit6','exitorder6','sell_price7','P&L7','stoploss7','takeprofit7','exitorder7','sell_price8','P&L8','stoploss8','takeprofit8','exitorder8','sell_price9','P&L9','stoploss9','takeprofit9','exitorder9','sell_price10','P&L10','stoploss10','takeprofit10','exitorder10', 'ScriptRunMode',  'trailstoploss',  'ChannelChk',  'PriceRangeChk',  'TimeRangeChk','maxentryprice','maxentrytime','PrintTime','maxtimedif', 'maxbuypriceDiff'])

if path.exists(MyPrimeQueuePLCsv):
    MyPrimeQueuePL = pd.read_csv(MyPrimeQueuePLCsv) 
else:
    #PrimeQueue = pd.DataFrame(columns = ['symbol','entry_price','spotprice','buy_price','order_type', 'buy_sell', 'quantity', 'stoploss1','takeprofit1','ltp','high','low','senderid', 'token', 'tag', 'order_number', 'logtime','ordertime','exitorder1'])
    MyPrimeQueuePL = pd.DataFrame()

TempPLQueuePrev = pd.DataFrame()

def StoreMyPrimeQueue():
    global PrimeQueue
    PrimeQueue['PrintTime'] = datetime.datetime.now()
    PrimeQueue.to_csv(MyPrimeQueueLoadBackCsv,  encoding='utf-8',index=False, na_rep='')
    #content2=tabulate(PrimeQueue, headers = 'keys', tablefmt = 'tsv', showindex=False)
    #text_file=open(MyPrimeQueueCsv,"w")
    #text_file.write(content2)
    #text_file.close()

def placeMarketOrder(symbol,buy_sell,quantity, tagtext,senderid):    
    # Place an intraday market order on NSE
    if buy_sell == "BUY":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "SELL":
        t_type=kite.TRANSACTION_TYPE_SELL
    #print('Print tagtext', tagtext)
    quantity = int(quantity)
    try:
        if False:
            print('==================================== TRY WITH NAME', tagtext)
            Order_ID = kite.place_order(tradingsymbol=symbol,
                            exchange=kite.EXCHANGE_NFO,
                            transaction_type=t_type,
                            quantity=quantity,
                            order_type=kite.ORDER_TYPE_MARKET,
                            product=kite.PRODUCT_MIS,
                            variety=kite.VARIETY_REGULAR)
            print(Order_ID)
    except:
        True
        if False:
            try:
                print('==================================== TRY WITH ID', senderid)
                Order_ID = kite.place_order(tradingsymbol=symbol,
                            exchange=kite.EXCHANGE_NFO,
                            transaction_type=t_type,
                            quantity=quantity,
                            order_type=kite.ORDER_TYPE_MARKET,
                            product=kite.PRODUCT_MIS,
                            variety=kite.VARIETY_REGULAR,
                            tag=senderid)
                print(Order_ID)
            except:
                try:
                    print('==================================== TRY BLANK')
                    Order_ID = kite.place_order(tradingsymbol=symbol,
                                exchange=kite.EXCHANGE_NFO,
                                transaction_type=t_type,
                                quantity=quantity,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_MIS,
                                variety=kite.VARIETY_REGULAR)
                    print(Order_ID)
                except:
                    True
 
def instrumentLookup(instrument_df,symbol):
    """Looks up instrument token for a given script from instrument dump"""
    try:
        ins_token = instrument_df[instrument_df.tradingsymbol==symbol].instrument_token.values[0]
        ins_lot = instrument_df[instrument_df.tradingsymbol==symbol].lot_size.values[0]
        return ins_token, ins_lot
    except:
        return -1, -1

def settingsLookup(senderid):
    global settings_df
    global DefTakeProfitPcent
    global DefStopLossPcent
    try:
        minentryprice = settings_df[settings_df.senderid==senderid].minentryprice.values[0]
        maxentryprice = settings_df[settings_df.senderid==senderid].maxentryprice.values[0]
        stoploss = settings_df[settings_df.senderid==senderid].stoploss.values[0]
        takeprofit = settings_df[settings_df.senderid==senderid].takeprofit.values[0]
        minentryprice1 = settings_df[settings_df.senderid==senderid].minentryprice1.values[0]
        maxentryprice1 = settings_df[settings_df.senderid==senderid].maxentryprice1.values[0]
        stoploss1 = settings_df[settings_df.senderid==senderid].stoploss1.values[0]
        takeprofit1 = settings_df[settings_df.senderid==senderid].takeprofit1.values[0]
        
        maxcutoff = settings_df[settings_df.senderid==senderid].maxcutoff.values[0]
        maxquantity = settings_df[settings_df.senderid==senderid].maxquantity.values[0]
        trailstoploss = settings_df[settings_df.senderid==senderid].trailstoploss.values[0]
        minentrytimex = settings_df[settings_df.senderid==senderid].minentrytime.values[0]
        maxentrytimex = settings_df[settings_df.senderid==senderid].maxentrytime.values[0]
        
        maxtimedif = settings_df[settings_df.senderid==senderid].maxtimedif.values[0]
        maxbuypriceDiff = settings_df[settings_df.senderid==senderid].maxbuypricediff.values[0]
        
        tag = settings_df[settings_df.senderid==senderid].tag.values[0]
        ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
        minentrytime = datetime.datetime.strptime(ThisDate+' '+minentrytimex, '%Y%m%d %H:%M:%S.%f')
        maxentrytime = datetime.datetime.strptime(ThisDate+' '+maxentrytimex, '%Y%m%d %H:%M:%S.%f')
    except:
        minentryprice = DefMinEntryPriceRange
        maxentryprice = DefMaxEntryPriceRange
        stoploss = DefStopLossPcent
        takeprofit = DefTakeProfitPcent
        minentryprice1 = 0
        maxentryprice1 = 0
        maxtimedif = 10000
        maxbuypriceDiff = 10000
        
        stoploss1 = 0
        takeprofit1 = 0
        maxcutoff = 1
        maxquantity = 25
        trailstoploss = 'Yes'
        minentrytime = DefMinTime
        maxentrytime = DefMaxTime
        tag = senderid

    return tag, minentryprice, maxentryprice, stoploss, takeprofit, minentryprice1, maxentryprice1, stoploss1, takeprofit1, maxcutoff, maxquantity, trailstoploss, minentrytime, maxentrytime, maxtimedif, maxbuypriceDiff
    
def TargetLookup(senderid):
    global settings_df
    DayName = datetime.datetime.now().strftime("%a")
    try:
        TargetLevel = settings_df[settings_df.senderid==senderid][DayName].values[0]
    except Exception as e:
        print('TargetLookup Error', str(e))
        TargetLevel = 'T3'
    return TargetLevel
    
def sender_id_Lookup(senderid):
    global settings_df
    try:
        tag = settings_df[settings_df.senderid==senderid].tag.values[0]
    except:
        tag = senderid

    return tag

 
def CheckLTPandPlaceOrder(PrimeQueueEntry, ltp):
    global ForceExit
    global ForceExitACTIVEQueue
    global ForceExitPENDINGQueue
    global TradeStartHour
    global TradeStartMinute
    global TradeStartSecond
    global NoNewEntryHour
    global NoNewEntryMinute
    global TradeCloseHour
    global TradeCloseMinute
    global CheckTradeCloseHour
    global TestStepInc
    global TestStepIncVal    
    global TestStepDec    
    global TestStepDecVal
    global MaxEntryCutOff
    global TradeStartHour
    global TradeStartMinute
    
    OrderIsPlaced = ''
    Mn = datetime.datetime.now().minute
    Hr = datetime.datetime.now().hour
    Sc = datetime.datetime.now().second

    if Hr < TradeStartHour:
        return OrderIsPlaced
    if Hr == TradeStartHour:
        if Mn <TradeStartMinute or (Mn == TradeStartMinute and Sc < TradeStartSecond):
            return OrderIsPlaced
    
    token = int(PrimeQueueEntry['token'])
    order_number = PrimeQueueEntry['order_number']
    entryPrice = float(PrimeQueueEntry['entry_price'])
    ScriptRunMode  = PrimeQueueEntry['ScriptRunMode']
    trailstoploss  = PrimeQueueEntry['trailstoploss']
    CurQuantity = PrimeQueueEntry['quantity']
    
    if str(order_number) == '' or pd.isna(order_number):
        order_number = 0
        order_numberTxt = '1'
    else:
        order_number = int(order_number)
        order_numberTxt = str(order_number)
    
    #ltag =   PrimeQueueEntry['tag']
    takeProfit = float(PrimeQueueEntry['takeprofit'+order_numberTxt])
    SL = float(PrimeQueueEntry['stoploss'+order_numberTxt])
    price = ltp[str(token)]['last_price']
    
    if order_number == 0:
        if  TestStepInc == True:
            TestStepIncVal = TestStepIncVal
            price = round(price + TestStepIncVal,2)
        if  TestStepDec == True:
            
            TestStepDecVal = TestStepDecVal
            price = round((price + TestStepIncVal) - TestStepDecVal,2)
        if PrimeQueueEntry['buy_sell'] == 'BUY':
            MaxEntryPrice = entryPrice + (entryPrice * MaxEntryCutOff)
            MinEntryPrice = entryPrice - 1 
        else:
            MaxEntryPrice = entryPrice - (entryPrice  * MaxEntryCutOff)
            MinEntryPrice = entryPrice + 1
        
        print(datetime.now(), '========== ENTRY CHECK ', ScriptRunMode, PrimeQueueEntry['tag'])
        print(PrimeQueueEntry['symbol'], 'CurQuantity', CurQuantity,'spotprice', PrimeQueueEntry['spotprice'], 'EP: ', entryPrice, 'LTP: ', price, 'Min: ', MinEntryPrice, 'Max: ', MaxEntryPrice, 'Tme:', PrimeQueueEntry['logtime'])

        if CheckTradeCloseHour == True:
            if Hr >= NoNewEntryHour and Mn > NoNewEntryMinute:
                SkipEntry = True
            else:
                SkipEntry = False
        else:
            SkipEntry = False
        if Hr > TradeCloseHour or (Hr == TradeCloseHour and Mn >= TradeCloseMinute):
            SkipEntry = True

        if ((PrimeQueueEntry['buy_sell'] == 'BUY' and price >= MinEntryPrice and  price <= MaxEntryPrice) \
                or (PrimeQueueEntry['buy_sell'] == 'SELL' and price >= MaxEntryPrice and  price <= MinEntryPrice)) and SkipEntry == False:
            if ScriptRunMode == "SelectedSL":
                placeMarketOrder(PrimeQueueEntry['symbol'],PrimeQueueEntry['buy_sell'],PrimeQueueEntry['quantity'],PrimeQueueEntry['tag'],PrimeQueueEntry['senderid'])
            OrderIsPlaced = 'YesOrderIsPlaced'
            print(OrderIsPlaced, 'in CHK')

        elif (PrimeQueueEntry['buy_sell'] == 'BUY' and price  > MaxEntryPrice) \
                or (PrimeQueueEntry['buy_sell'] == 'SELL' and price < MaxEntryPrice) \
                or ForceExit == True or  SkipEntry == True or ForceExitPENDINGQueue == True:
            OrderIsPlaced = "NoSkipEntry"
    else:
        buy_price = PrimeQueueEntry['buy_price']
        lot_size = PrimeQueueEntry['quantity']
        high_price = PrimeQueueEntry['high']
        low_price = PrimeQueueEntry['low']
        if high_price == 0:
            high_price = price
        if low_price == 0:
            low_price = price
        if TestStepInc == True or TestStepDec == True:
            #if ScriptRunMode == 'SingleSL' or ScriptRunMode == 'SingleSLStd':
            if ScriptRunMode == 'SingleSL' or TestStepInc == True:
                if TestStepIncVal >= 20:
                    TestStepInc = False
                    TestStepDec = True
                    price = price + TestStepIncVal
                    #TestStepIncVal = 1
                    #TestStepDecVal = 1
            else:
                if order_number >=4:
                    TestStepInc = False
                    TestStepDec = True
                    price = price + TestStepIncVal

            if  TestStepInc == True:
                TestStepIncVal = TestStepIncVal
                price = round(price + TestStepIncVal,2)

            if  TestStepDec == True:
                TestStepDecVal = TestStepDecVal
                price = round((price + TestStepIncVal) - TestStepDecVal,2)
        if PrimeQueueEntry['buy_sell'] == 'SELL':
            Buy_Sell = 'BUY'
            if trailstoploss == 'Yes1':
                CurrentPriceDiff = buy_price - low_price
                if CurrentPriceDiff >= SL:
                    MyStopLoss = math.floor(low_price +SL)
                    MyTakeProfit = math.floor(buy_price - takeProfit) - (takeProfit * 0.15)
                else:
                    MyStopLoss = math.floor(buy_price +SL)
                    MyTakeProfit = math.floor(buy_price - takeProfit) - (takeProfit * 0.15)
            else:
                MyStopLoss = math.floor(buy_price +SL)
                MyTakeProfit = math.floor(buy_price - takeProfit) - (takeProfit * 0.15)
        else:
            Buy_Sell = 'SELL'
            if trailstoploss == 'Yes1':
                CurrentPriceDiff = high_price - buy_price
                if CurrentPriceDiff >= SL:
                    MyStopLoss = math.floor(high_price -SL)
                    MyTakeProfit = math.floor(buy_price + takeProfit) - (takeProfit * 0.15)
                else:
                    MyStopLoss = math.floor(buy_price - SL)
                    MyTakeProfit = math.floor(buy_price + takeProfit) - (takeProfit * 0.15)
            else:
                MyStopLoss = math.floor(buy_price - SL)
                MyTakeProfit = math.floor(buy_price + takeProfit) - (takeProfit * 0.15)
        if Hr > TradeCloseHour or (Hr == TradeCloseHour and Mn >= TradeCloseMinute):
            ForceExit = True
        #print('buy_price',buy_price, 'high_price', high_price, 'CurrentPriceDiff', CurrentPriceDiff, 'SL',SL, 'MyStopLoss',MyStopLoss,'MyTakeProfit',MyTakeProfit)
        
        #NetDifference = round(((((price) - buy_price) * lot_size) - (lot_size * 2)),2)
        IvestmentValue = lot_size * buy_price
        Brokerage = 40
        TransactionCharges = IvestmentValue * 0.00159
        GST = (Brokerage + TransactionCharges) * 0.18
        AdditionalCharges = Brokerage + TransactionCharges + GST + 10
        NetDifference = round((((price - buy_price) * lot_size) - (AdditionalCharges)),0)

        GainPcent = (NetDifference / IvestmentValue)
        print(datetime.now(), '========== EXIT CHECK - Level ', order_number, ScriptRunMode, PrimeQueueEntry['tag'])
        print(PrimeQueueEntry['symbol'], 'CurQuantity', CurQuantity, 'SP', PrimeQueueEntry['spotprice'], 'EP: ', entryPrice, 'BP: ', buy_price, 'H: ', high_price,'L: ',low_price, 'SL: ', MyStopLoss, 'PT: ', MyTakeProfit,'LTP: ', price, 'M2M: ', NetDifference)
        
        BuyExitCheck = (Buy_Sell== 'BUY' and price >= MyStopLoss and  price <= MyTakeProfit)
        SellExitCheck = (Buy_Sell== 'SELL' and (price <= MyStopLoss or price >= MyTakeProfit))
        SelectedSLCheck = ((NetDifference >= 2000 or NetDifference < -1500) and ScriptRunMode == "SelectedSL") 
        SingleSLCheck = ((NetDifference >= 10000 or NetDifference < -2500) and ScriptRunMode == "SingleSL")
        GainPcentCheck = (GainPcent < -0.1) or (GainPcent >= 0.08)

        if BuyExitCheck or SellExitCheck or SelectedSLCheck or SingleSLCheck or GainPcentCheck or ForceExitACTIVEQueue == True or ForceExit == True:
            if ScriptRunMode == "SelectedSL":
                placeMarketOrder(PrimeQueueEntry['symbol'],Buy_Sell,PrimeQueueEntry['quantity'],PrimeQueueEntry['tag'],PrimeQueueEntry['senderid'])
            OrderIsPlaced = 'YesOrderIsPlaced'
            print(OrderIsPlaced, 'in CHK')

    return OrderIsPlaced

async def ProcessMyQueue():
    global startProcessMyQueue
    global PrimeQueue
    global ForceExit
    global ForceExitACTIVE
    global ForceExitPENDING
    global ForceExitACTIVEQueue
    global ForceExitPENDINGQueue
    global OkToForceExit
    global PlaySafeStopLoss
    global PlaySafeStopLossPcentChk
    global PlaySafeStopLossTrailLow
    global PlaySafeStopLossTrailHigh
    global TestStepInc
    global TestStepIncVal    
    global TestStepDec    
    global TestStepDecVal
    global TradeStartHour
    global TradeStartMinute
    global TradeStartSecond
    global TestStepIncStop
    global TestStepDecStop
    print('StartedProcessMyQueue')
    WhileLoopCounter = 0
    LoopCounter = 0
    CurrentOrderStatus = ''
    while True:
        try:
            if len(PrimeQueue) ==0:
                print('waiting for orders', datetime.datetime.now())
                await asyncio.sleep(1)

                Mn = datetime.datetime.now().minute
                Hr = datetime.datetime.now().hour
                if Hr > TradeCloseHour or (Hr == TradeCloseHour and Mn >= TradeCloseMinute):
                    print('exiting now')
                    bot.sendMessage(userSelf, 'EXIT')

                if ForceExit == True:
                    OkToForceExit = True
                    bot.sendMessage(userSelf, 'ForceExitNow')
                    await asyncio.sleep(20)
            else:
                PendingPrimeQueue = pd.DataFrame()
                PendingPrimeQueue = PrimeQueue[(PrimeQueue['order_number'] !=11)]

                if len(PendingPrimeQueue) ==0:
                    print('waiting fresh orders', datetime.datetime.now(), ForceExit)
                    #print("saving csv")
                    UpdateCSV = StoreMyPrimeQueue()

                    Mn = datetime.datetime.now().minute
                    Hr = datetime.datetime.now().hour
                    if Hr > TradeCloseHour or (Hr == TradeCloseHour and Mn >= TradeCloseMinute):
                        print('exiting now')
                        bot.sendMessage(userSelf, 'EXIT')

                    await asyncio.sleep(1)
                    if ForceExit == True:
                        print(1)
                        await asyncio.sleep(60)
                        PrintTxt = FetchPrintMsg()
                        print(PrintTxt)
                        if PrintTxt != '' and SendMesageToTelegram == True:
                            await client.send_message(ScalpBANKNIFTY, PrintTxt)
                        print(2)
                        try:
                            PrintTxt = FetchPrintMsgSELL()
                            print(PrintTxt)
                            if PrintTxt != '' and SendMesageToTelegram == True and False:
                                await client.send_message(ScalpBANKNIFTY, PrintTxt)
                        except Exception as e:
                            print(str(e))
                        try:
                            PrintTxt = FetchPrintMsgSafe()
                            print(PrintTxt)
                            if PrintTxt != '' and SendMesageToTelegram == True and False:
                                await client.send_message(ScalpBANKNIFTY, PrintTxt)
                        except Exception as e:
                            print(str(e))
                        try:
                            PrintTxt = FetchPrintMsgSafe2()
                            print(PrintTxt)
                            if PrintTxt != '' and SendMesageToTelegram == True and False:
                                await client.send_message(ScalpBANKNIFTY, PrintTxt)
                        except Exception as e:
                            print(str(e))

                            
                        print(3)
                        OkToForceExit = True
                        UpdateCSV = StoreMyPrimeQueue()
                        bot.sendMessage(userSelf, 'ForceExitNow')
                        await asyncio.sleep(20)

                else:
                    
                    Mn = datetime.datetime.now().minute
                    Hr = datetime.datetime.now().hour
                    Sc = datetime.datetime.now().second
                
                    ProcessMyQueueList = False
                    if Hr > TradeStartHour:
                        ProcessMyQueueList = True
                    elif Hr == TradeStartHour:
                        if Mn > TradeStartMinute or (Mn == TradeStartMinute and Sc >TradeStartSecond):
                            ProcessMyQueueList = True

                    #Check if time
                    if ProcessMyQueueList == False:
                        UpdateCSV = StoreMyPrimeQueue()
                        await asyncio.sleep(1)
                        print('waiting for entry time', datetime.datetime.now())
                    else:
                        #sleep(1)
                        print('########################################################### ProcessMyQueue', datetime.datetime.now())

                        Tokens = PendingPrimeQueue.token.unique()
                        #ltp = kite.ltp(Tokens)
                        ltp = kite.quote(Tokens)
                        #await asyncio.sleep(5)
                        if ForceExitACTIVE == True:
                            ForceExitACTIVEQueue = True
                            print('2ForceExitACTIVEQueue',ForceExitACTIVEQueue)
                        if ForceExitPENDING == True:
                            ForceExitPENDINGQueue = True
                            print('2ForceExitPENDINGQueue',ForceExitPENDINGQueue)
                        MsgToPrint = ''
                        MsgTesting = ''
                        MsgMKT = ''
                        MsgMKT_Skip = ''
                        MsgMKT_FINAL = ''
                        MsgMKT_FINAL2 = ''
                        MsgMKT_FINAL3 = ''
                        MsgMKT_Safe = ''
                        MsgMKT_Safe2 = ''
                        MsgMKT_SELL = ''
                        LoopCounter = LoopCounter + 1
                        #await asyncio.sleep(0.5)
                        if LoopCounter >3:
                            await asyncio.sleep(0.1)
                            LoopCounter = 0
                        for i in range(0, len(PendingPrimeQueue)):
                            TempLoopNum = 1
                            GrossM2M = 0
                            CurrentOrderStatus = 'BlankStatus'
                            lot_size = PendingPrimeQueue.iloc[i]['quantity']
                            spotprice = float(PendingPrimeQueue.iloc[i]['spotprice'])
                            ltime = PendingPrimeQueue.iloc[i]['logtime']
                            order_number = PendingPrimeQueue.iloc[i]['order_number']
                            order_type = PendingPrimeQueue.iloc[i]['order_type']
                            token = int(PendingPrimeQueue.iloc[i]['token'])
                            cHigh = float(PendingPrimeQueue.iloc[i]['high'])
                            cLow = float(PendingPrimeQueue.iloc[i]['low'])
                            symbol = PendingPrimeQueue.iloc[i]['symbol']
                            tag = PendingPrimeQueue.iloc[i]['tag']
                            ScriptRunMode  = PendingPrimeQueue.iloc[i]['ScriptRunMode']
                            trailstoploss  = PendingPrimeQueue.iloc[i]['trailstoploss']
                            ordertime = PendingPrimeQueue.iloc[i]['ordertime']
                            IndexEntry = PendingPrimeQueue.iloc[i]['IndexEntry']
                            IndexName = PendingPrimeQueue.iloc[i]['IndexEntry']
                            entry_price = float(PendingPrimeQueue.iloc[i]['entry_price'])
                            entry_price2 = float(PendingPrimeQueue.iloc[i]['entry_price2'])
                            
                            buy_sell = PendingPrimeQueue.iloc[i]['buy_sell']
                            buy_price = float(PendingPrimeQueue.iloc[i]['buy_price'])
                            T1 = float(PendingPrimeQueue.iloc[i]['T1'])
                            T2 = float(PendingPrimeQueue.iloc[i]['T2'])
                            T3 = float(PendingPrimeQueue.iloc[i]['T3'])
                            SL = float(PendingPrimeQueue.iloc[i]['SL1'])
                            CutOffCheck1 = float(PendingPrimeQueue.iloc[i]['CutOffCheck1'])
                            CutOffCheck2 = float(PendingPrimeQueue.iloc[i]['CutOffCheck2'])
                            T1sell_price = float(PendingPrimeQueue.iloc[i]['T1sell_price'])
                            T2sell_price = float(PendingPrimeQueue.iloc[i]['T2sell_price'])
                            T3sell_price = float(PendingPrimeQueue.iloc[i]['T3sell_price'])
                            SLsell_price = float(PendingPrimeQueue.iloc[i]['SLsell_price'])
                            
                            
                            T1Msg = PendingPrimeQueue.iloc[i]['T1Msg']
                            T2Msg = PendingPrimeQueue.iloc[i]['T2Msg']
                            T3Msg = PendingPrimeQueue.iloc[i]['T3Msg']
                            SLMsg = PendingPrimeQueue.iloc[i]['SLMsg']
                            
                            if T1Msg != 'No':
                                T1Msg = 'Yes'
                            if T2Msg != 'No':
                                T2Msg = 'Yes'
                            if T3Msg != 'No':
                                T3Msg = 'Yes'
                            if SLMsg != 'No':
                                SLMsg = 'Yes'

                            price = ltp[str(token)]['last_price']
                            lastDay_price = ltp[str(token)]['ohlc']['close']

                            price = round(price,2)
                            if price != lastDay_price -1 or buy_price > 0:
                                #print('TestStepInc', TestStepInc, 'TestStepIncVal', TestStepIncVal, 'TestStepDec', TestStepDec)
                                if IamTestingNow == True:
                                    if TestStepIncVal >= 6:
                                        TestStepInc = False
                                        TestStepDec = True
       
                                    if TestStepInc == True:
                                        TestStepIncVal= TestStepIncVal + 0.25
                                        price = round(price + TestStepIncVal,2)
        
                                    if  TestStepDec == True:
                                        TestStepDecVal = TestStepDecVal + 0.25
                                        if TestStepDecVal <= 12:
                                            price = round((price + TestStepIncVal) - TestStepDecVal,2)
                                        else:
                                            price = round((price + TestStepIncVal) + TestStepDecVal,2)
                                try:


                                    PrimeQueue.loc[PrimeQueue.logtime==ltime, 'ltp'] = price
                                    if (buy_sell == 'BUY' and (price > cHigh or cHigh == 0)) or (buy_sell == 'SELL' and (price > cHigh or cHigh == 0) and (buy_price > 0 or order_type == 'EXIT_SAFE' or order_type == 'EXIT_SAFE2')):
                                        PrimeQueue.loc[PrimeQueue.logtime==ltime, 'high'] = price
                                        cHigh = price
                                    if (buy_sell == 'SELL' and (price < cLow or cLow == 0) and buy_price > 0) or (buy_sell == 'BUY' and (price < cLow or cLow == 0) and (buy_price > 0 or order_type == 'EXIT_SAFE' or order_type == 'EXIT_SAFE2')):
                                        PrimeQueue.loc[PrimeQueue.logtime==ltime, 'low'] = price
                                        cLow = price
                                except Exception as e:
                                    print('failed to update ltp')
                                    print(str(e))

                                try:
                                    #print(spotprice, price, entry_price)
                                    if spotprice == 0:
                                        if buy_sell  == 'BUY':
                                            if price > entry_price:
                                                if price >= 300:
                                                    entry_price = price + 2
                                                elif price >= 70:
                                                    entry_price = price + 1.5
                                                else:
                                                    entry_price = price + 1.25
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'entry_price'] = entry_price
                                                PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'entry_price'] = entry_price

                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'entry_price2'] = 0
                                                PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'entry_price2'] = 0

                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'spotprice'] = price
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'spotprice'] = price
                                            xT = round(entry_price * 0.1,2)
                                            if xT < 10:
                                                xT = 10
                                            eTarget = round(entry_price + xT,2)
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1'] = eTarget
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'T1'] = eTarget
                                        else:
                                            if price < entry_price:
                                                if price >= 300:
                                                    entry_price = price - 2
                                                elif price >= 70:
                                                    entry_price = price - 1.5
                                                else:
                                                    entry_price = price - 1.25
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'entry_price'] = entry_price
                                                PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'entry_price'] = entry_price

                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'entry_price2'] = 0
                                                PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'entry_price2'] = 0

                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'spotprice'] = price
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'spotprice'] = price
                                            xT = round(entry_price * 0.1,2)
                                            if xT < 10:
                                                xT = 10
                                            eTarget = round(entry_price - xT,2)
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1'] = eTarget
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'T1'] = eTarget
                                except:
                                    print('failed to spotprice')


                                if trailstoploss == 'Yes' and order_number > 0 and False:
                                    
                                    CurrentPriceDiff = cHigh - buy_price
                                    CurrentPriceDiffPCent = round(CurrentPriceDiff / buy_price,2)
                                    #BaseLimitVal1 = round(buy_price * 0.01,2)
                                    BaseLimitVal2 = round(buy_price * 0.02,2)

                                    if symbol.startswith('BANK'):
                                        if BaseLimitVal2 < 6:
                                            LimitVal = BaseLimitVal2
                                        else:
                                            LimitVal = 6
                                    else:
                                        if BaseLimitVal2 < 3:
                                            LimitVal = BaseLimitVal2
                                        else:
                                            LimitVal = 3
                                    if LimitVal < 0.5:
                                        LimitVal = 0.5
                                    if CurrentPriceDiff >=LimitVal or (CurrentPriceDiffPCent > 0.01 and GrossM2M > 100):
                                        NewStopLoss = round((cHigh - LimitVal),2)
                                        if NewStopLoss < SL:
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SL1'] = NewStopLoss
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'SL1'] = NewStopLoss
                                            #print('NewStopLoss', NewStopLoss, 'eStopLoss', eStopLoss)
                                    elif GainPcent > 0.01:
                                        NewStopLoss = round(buy_price * 0.95,2)
                                        if NewStopLoss < 2:
                                            NewStopLoss = 2
                                        if NewStopLoss < SL:
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SL1'] = NewStopLoss
                                            PendingPrimeQueue.loc[PendingPrimeQueue.logtime==ltime, 'SL1'] = NewStopLoss
                                            #print('NewStopLoss', NewStopLoss, 'eStopLoss', eStopLoss)
                                #print(1)
                                if  ScriptRunMode == 'ToChannel':
                                    EndOfTradeHour = False
                                    if Hr > TradeCloseHour or (Hr == TradeCloseHour and Mn >= (TradeCloseMinute)):
                                        EndOfTradeHour = True
                                        PrimeQueue.loc[PrimeQueue.logtime==ltime, 'order_number'] = 11 
                                    
                                    GrossM2M = 0
                                    T1_Exit_Condition = False
                                    SL_Exit_Condition = False
                                    if buy_price == 0:
                                        Entry_Condition = False

                                        if order_type == 'EXIT_SAFE':
                                            if spotprice > 0:
                                                if spotprice > entry_price:
                                                    EntryPoint = spotprice
                                                else:
                                                    EntryPoint = entry_price
                                            else:
                                                EntryPoint = entry_price

                                            if IndexName == "BANKNIFTY":
                                                MaxPointsToEnter = EntryPoint + 6
                                            else:
                                                MaxPointsToEnter = EntryPoint + 4

                                            if SLsell_price == 0 and price >= entry_price and cLow < (entry_price - 4) and cHigh <= MaxPointsToEnter and cHigh < T1 - 3:
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'inv_amount'] = lot_size * price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'low'] = price

                                        elif order_type == 'EXIT_SAFE2':

                                            MaxPointsToEnter = entry_price + (int(T1 - entry_price) * 0.8)

                                            if SLsell_price == 0 and price >= entry_price and cLow < (entry_price - 4) and cHigh < MaxPointsToEnter :
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'inv_amount'] = lot_size * price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'low'] = price
                                        elif 'FINAL' in order_type:
                                            if buy_sell == 'BUY' and price >= entry_price:
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'inv_amount'] = lot_size * price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'low'] = price
                                            if buy_sell == 'SELL' and price <= entry_price:
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'high'] = price

                                        else:
                                            if buy_sell == 'BUY' and price >= entry_price:
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'inv_amount'] = lot_size * price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'low'] = price
                                            if buy_sell == 'SELL' and price <= entry_price:
                                                Entry_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'high'] = price

                                        if Entry_Condition == True:
                                            buy_price = price
                                            cLow = price

                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'buy_price'] = price
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'order_number'] = 1
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
                                            
                                            if (T1 < (price * 1.04) or  T1 < (price + 6)) and 'TESTING' in order_type:
                                                xT = price * 0.05
                                                if xT < 6:
                                                    xT = 6
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1'] = round(price + (xT * 1),2)
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2'] = round(price + (xT * 2),2)
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3'] = round(price + (xT * 3),2)
                                                T1 = round(buy_price + (xT * 1),2)
                                                T2 = round(buy_price + (xT * 2),2)
                                                T3 = round(buy_price + (xT * 3),2)

                                    elif buy_price > 0 :
                                        
                                        


                                        IvestmentValue = lot_size * buy_price
                                        Brokerage = 40
                                        TransactionCharges = IvestmentValue * 0.00159
                                        GST = (Brokerage + TransactionCharges) * 0.18
                                        AdditionalCharges = Brokerage + TransactionCharges + GST
                                        
                                        sell_price = 0
                                        if SLsell_price > 0 or  T1sell_price > 0:
                                            if SLsell_price > 0:
                                                sell_price = SLsell_price
                                            if T1sell_price > 0:
                                                sell_price = T1sell_price
                                            if T2sell_price > 0:
                                                sell_price = T2sell_price
                                            if T3sell_price > 0:
                                                sell_price = T3sell_price
                                        else:
                                            sell_price = price

                                        if buy_sell == 'BUY':
                                            GrossM2M = round((((sell_price - buy_price) * lot_size) - (AdditionalCharges)),0)
                                        else:
                                            GrossM2M = round((((buy_price - sell_price) * lot_size) - (AdditionalCharges)),0)
                                                
                                        #print('buy_price',buy_price,'sell_price',sell_price,'price',price,'AdditionalCharges',AdditionalCharges,'GrossM2M',GrossM2M)
                                        DateTimeObject = datetime.datetime.strptime(str(ordertime), '%Y-%m-%d %H:%M:%S.%f')
                                        OrdTime = DateTimeObject
                                        NowTime = datetime.datetime.now()

                                        if (((NowTime - OrdTime) >= datetime.timedelta(seconds=60 * 1)) and  CutOffCheck1 == 0) or \
                                            (((NowTime - OrdTime) >= datetime.timedelta(seconds=60 * 3)) and  CutOffCheck2 == 0):

                                            if CutOffCheck1 == 0:
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'CutOffCheck1'] = GrossM2M
                                            if CutOffCheck2 == 0:
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'CutOffCheck2'] = GrossM2M

                                        if order_type == 'FINAL':

                                            if trailstoploss == 'T3':
                                                Target = T3
                                            elif trailstoploss == 'T2':
                                                Target = T2
                                            elif trailstoploss == 'T1':
                                                Target = T1

                                            if buy_sell == 'SELL':
                                                xStopLoss = SL
                                            elif SL < 50:
                                                xStopLoss = SL - 2
                                            else:
                                                xStopLoss = SL - 5
                                        
                                            if (SLMsg == 'No' and T1Msg == 'No' and (GrossM2M > 0)) and \
                                                ((buy_sell == 'BUY' and (cHigh >= Target) and T1 > 0) or \
                                                (buy_sell == 'SELL' and (cLow <= Target) and cLow > 0) or (EndOfTradeHour == True )):
                                                
                                                T1_Exit_Condition = True
                                            
                                            if (SLMsg == 'No' and T1Msg == 'No' and buy_price > 0 and GrossM2M < 0 and T1sell_price == 0) and \
                                                ((buy_sell == 'BUY' and cLow < xStopLoss) or \
                                                (buy_sell == 'SELL' and cHigh > xStopLoss ) or (EndOfTradeHour == True )):

                                                SL_Exit_Condition = True
                                        elif order_type == 'FINAL2':

                                            if trailstoploss == 'T3':
                                                Target = T3
                                            elif trailstoploss == 'T2':
                                                Target = T2
                                            elif trailstoploss == 'T1':
                                                Target = T1

                                            if buy_sell == 'SELL':
                                                xStopLoss = SL
                                            elif SL < 50:
                                                xStopLoss = SL - 2
                                            else:
                                                xStopLoss = SL - 5

                                            TrailExitNow = False
                                            if cHigh > (T2 + ((T3-T2)*0.6)) and price <= T2:
                                                TrailExitNow = True
                                            elif cHigh > T2 and price <= T1:
                                                TrailExitNow = True
                                            elif cHigh > T1 and price <= buy_price:
                                                TrailExitNow = True


                                            if (SLMsg == 'No' and T1Msg == 'No' and (GrossM2M > 0 or TrailExitNow)) and \
                                                ((buy_sell == 'BUY' and ((cHigh >= Target) or TrailExitNow) and T1 > 0) or \
                                                (buy_sell == 'SELL' and (cLow <= Target) and cLow > 0) or (EndOfTradeHour == True )):
                                                
                                                T1_Exit_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&L'] = 0
                                            if (SLMsg == 'No' and T1Msg == 'No' and buy_price > 0 and GrossM2M < 0 and T1sell_price == 0) and \
                                                ((buy_sell == 'BUY' and cLow < xStopLoss) or \
                                                (buy_sell == 'SELL' and cHigh > xStopLoss ) or (EndOfTradeHour == True )):

                                                SL_Exit_Condition = True

                                        elif order_type == 'FINAL3':

                                            if trailstoploss == 'T3':
                                                Target = T3 * 10
                                            elif trailstoploss == 'T2':
                                                Target = T2 * 10
                                            elif trailstoploss == 'T1':
                                                Target = T1 * 10

                                            if buy_sell == 'SELL':
                                                xStopLoss = SL
                                            elif SL < 50:
                                                xStopLoss = SL - 2
                                            else:
                                                xStopLoss = SL - 5

                                            CurPoints = 0
                                            if buy_sell == 'BUY':
                                                CurPoints = int(price - buy_price)
                                            elif buy_sell == 'SELL':
                                                CurPoints = int(buy_price - price)

                                            tDiff = T2 - T1

                                            TrailExitNow = False
                                            if cHigh > (buy_price + tDiff) and price <= (cHigh - tDiff):
                                                TrailExitNow = True


                                            if (SLMsg == 'No' and T1Msg == 'No' and (GrossM2M > 0 or TrailExitNow)) and \
                                                ((buy_sell == 'BUY' and ((cHigh >= Target) or TrailExitNow) and T1 > 0) or \
                                                (buy_sell == 'SELL' and (cLow <= Target) and cLow > 0) or (EndOfTradeHour == True )):
                                                
                                                T1_Exit_Condition = True
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&L'] = 0
                                            if (SLMsg == 'No' and T1Msg == 'No' and buy_price > 0 and GrossM2M < 0 and T1sell_price == 0) and \
                                                ((buy_sell == 'BUY' and cLow < xStopLoss) or \
                                                (buy_sell == 'SELL' and cHigh > xStopLoss ) or (EndOfTradeHour == True )):

                                                SL_Exit_Condition = True

                                        elif order_type == 'EXIT_SAFE':
                                            if SLsell_price == 0 and  T1sell_price == 0:
                                                CurrentPoints = round(price - buy_price,0)
                                                MaxPoints = round(cHigh - buy_price,0)
                                                MinPoints = round(cLow - buy_price,0)
                                                if IndexName == "BANKNIFTY":
                                                    DrowDown = -12
                                                    DrowUp = 8
                                                    if MaxPoints > 50:
                                                        TrailExit = 10
                                                    else:
                                                        TrailExit = 6
                                                else:
                                                    DrowDown = -8
                                                    DrowUp = 5
                                                    if MaxPoints > 20:
                                                        TrailExit = 6
                                                    else:
                                                        TrailExit = 4

                                                if EndOfTradeHour == True or cHigh >= T1 or cLow < SL or CurrentPoints <= DrowDown or (MaxPoints > DrowUp and CurrentPoints < (MaxPoints - TrailExit)):
                                                    if GrossM2M >= 0:
                                                        T1_Exit_Condition = True
                                                    if GrossM2M < 0:
                                                        SL_Exit_Condition = True
                                            elif SLsell_price > 0 and SLMsg == 'No':
                                                SL_Exit_Condition = True
                                            elif T1sell_price > 0 and T1Msg == 'No':
                                                T1_Exit_Condition = True
                                        elif order_type == 'EXIT_SAFE2':
                                            if SLsell_price == 0 and  T1sell_price == 0:

                                                if EndOfTradeHour == True or cHigh >= T1 or cLow < SL:
                                                    if GrossM2M >= 0:
                                                        T1_Exit_Condition = True
                                                    if GrossM2M < 0:
                                                        SL_Exit_Condition = True
                                            elif SLsell_price > 0 and SLMsg == 'No':
                                                SL_Exit_Condition = True
                                            elif T1sell_price > 0 and T1Msg == 'No':
                                                T1_Exit_Condition = True

                                        else:

                                            if buy_sell == 'SELL':
                                                xStopLoss = SL
                                            elif SL < 50:
                                                xStopLoss = SL - 2
                                            else:
                                                xStopLoss = SL - 5

                                            if (T1Msg == 'No' and GrossM2M > 0) and \
                                                ((buy_sell == 'BUY' and (cHigh >= T1 or price >= T1) and T1 > 0) or \
                                                (buy_sell == 'SELL' and (cLow <= T1 or price <= T1) and cLow > 0) or (EndOfTradeHour == True )):
                                                
                                                T1_Exit_Condition = True
                                            
                                            if (SLMsg == 'No' and buy_price > 0 and GrossM2M < 0 and T1sell_price == 0) and \
                                                ((buy_sell == 'BUY' and cLow < xStopLoss) or \
                                                (buy_sell == 'SELL' and cHigh > SL ) or (EndOfTradeHour == True )):

                                                SL_Exit_Condition = True
                                            
                                    #print(3)
                                    MsgToPrint = MsgToPrint + '\n' + tag.ljust(20)[0:20] + ' ' + IndexEntry + '\tSP: ' + str(spotprice).ljust(6)  +' EP: ' + str(entry_price).ljust(6) +' BP: ' + str(buy_price).ljust(10) + 'SL: ' + str(SL).ljust(6) + ' (' + SLMsg + ')\tT1: ' + \
                                    str(T1).ljust(6)  + ' (' + T1Msg.ljust(3) + ')\tT2: ' + str(T2).ljust(6)  + ' (' + T2Msg.ljust(3) + ')\tT3: ' + str(T3).ljust(6) + ' (' + T3Msg.ljust(3) + ')\tLTP: ' + \
                                    str(price).ljust(10) + 'cHigh: ' + str(cHigh).ljust(10) + 'cLow: ' + str(cLow).ljust(10) + 'M2M: ' + str(GrossM2M).ljust(10) + 'Qt: ' + str(lot_size).ljust(4) + 'TG: ' + str(trailstoploss)
                                    #print(4)
                                    if buy_sell == 'SELL' or order_type == 'EXIT_SAFE':
                                        xStopLoss = SL
                                    elif SL < 50:
                                        xStopLoss = SL - 2
                                    else:
                                        xStopLoss = SL - 5
                                    MsgToChannel = ''
                                    #print(MsgToPrint)
                                    #print(5)
                                    DateTimeObject = datetime.datetime.strptime(str(ltime), '%Y-%m-%d %H:%M:%S.%f')
                                    DateTimeStr = str(datetime.datetime.strftime(DateTimeObject, '%H:%M'))
                                    #lMn = DateTimeObject.minute
                                    #lHr = DateTimeObject.hour

                                    #Mn = datetime.datetime.now().minute
                                    #Hr = datetime.datetime.now().hour

                                    NowTime = datetime.datetime.now()

                                    #SendMessageToChannel = True
                                    SendMessageToChannel = False
                                    #if Hr > lHr or (Hr == lHr and Mn > (lMn + 1)):
                                    if (NowTime - DateTimeObject) > datetime.timedelta(seconds=60 * 2):
                                        SendMessageToChannel = True
                                    
                                    if T1Msg == 'No' and SLMsg == 'No' and EndOfTradeHour == True and False:
                                        if price >= entry_price2 and entry_price2 > 0:
                                            MsgToChannel = 'EXIT IN PROFIT ZONE ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                        elif price >= ((entry_price+xStopLoss) / 2) :
                                            MsgToChannel = 'EXIT AT CTC ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                        else:
                                            MsgToChannel = 'EXIT AT CMP ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                        
                                    TrigerMsg = 'LTP: ' + str(price) + ' cHigh: ' + str(cHigh) + ' cLow: ' + str(cLow)
                                    #print('T1Msg',T1Msg, T1, cHigh, price, 'T1sell_price', T1sell_price)
                                    #print(6)                                    done till here
                                    
                                    if  T1_Exit_Condition == True:
                                        MsgToPrint = MsgToPrint + '\n' + 'T1 hit'
                                        #print('T1 hit')
                                        if T1sell_price == 0:
                                            MsgToPrint = MsgToPrint + '\n' + 'T1 update'
                                            #print('T1 update')
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1P&L'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1P&LA'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1sell_price'] = price
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1ltp'] = price
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1high'] = cHigh
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1low'] = cLow
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1time'] = datetime.datetime.now()
                                            if order_type == 'FINAL' or order_type == 'FINAL2':
                                                T1Msg = TrigerMsg
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1Msg'] = TrigerMsg
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2Msg'] = TrigerMsg
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3Msg'] = TrigerMsg
                                            UpdateCSV = StoreMyPrimeQueue()
                                        if (SendMessageToChannel == True and order_type == 'MKT'and T1Msg == 'No') or (order_type != 'MKT'and T1Msg == 'No'):
                                            T1Msg = TrigerMsg
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1Msg'] = TrigerMsg
                                            UpdateCSV = StoreMyPrimeQueue()
                                            if cHigh >= T1:
                                                MsgToChannel = 'TARGET1 HIT ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                            else:
                                                True
                                                #MsgToChannel = 'Exit AT CMP' + IndexEntry  + ' (' + DateTimeStr + ')'
                                    if 'FINAL' not in order_type:
                                        if (T2Msg == 'No' and GrossM2M > 0) and \
                                            ((buy_sell == 'BUY' and (cHigh >= T2 or price >= T2) and T2 > 0) or \
                                            (buy_sell == 'SELL' and (cLow <= T2 or price <= T2) and cLow > 0)):
                                            MsgToPrint = MsgToPrint + '\n' + 'T2 hit'
                                            #print('T2 hit')
                                            if T2sell_price == 0:
                                                MsgToPrint = MsgToPrint + '\n' + 'T2 update'
                                                #print('T2 update')
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2P&L'] = GrossM2M
                                                if buy_sell == 'BUY' :
                                                    PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2P&LA'] = round((((price - buy_price) * lot_size) - (AdditionalCharges)),0)
                                                else:
                                                    PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2P&LA'] = round((((buy_price - price) * lot_size) - (AdditionalCharges)),0)
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2sell_price'] = price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2ltp'] = price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2high'] = cHigh
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2low'] = cLow
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2time'] = datetime.datetime.now()
                                                UpdateCSV = StoreMyPrimeQueue()
                                            if (SendMessageToChannel == True and order_type == 'MKT'and T1Msg == 'Yes') or (order_type != 'MKT'and T1Msg == 'Yes'):
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T2Msg'] = TrigerMsg
                                                MsgToChannel = 'TARGET2 HIT ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                                UpdateCSV = StoreMyPrimeQueue()
                                    
                                    if 'FINAL' not in order_type:
                                        if (T3Msg == 'No' and GrossM2M > 0) and \
                                            ((buy_sell == 'BUY' and cHigh >= T3 and T3 > 0) or \
                                            (buy_sell == 'SELL' and (cLow <= T3 or price <= T3) and cLow > 0)):
                                            MsgToPrint = MsgToPrint + '\n' + 'T3 hit'
                                            #print('T3 hit')
                                            if T3sell_price == 0:
                                                MsgToPrint = MsgToPrint + '\n' + 'T3 update'
                                                #print('T3 update')
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3P&L'] = GrossM2M
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3P&LA'] = GrossM2M
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3sell_price'] = price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3ltp'] = price
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3high'] = cHigh
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3low'] = cLow
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3time'] = datetime.datetime.now()
                                                UpdateCSV = StoreMyPrimeQueue()
                                            if (SendMessageToChannel == True and order_type == 'MKT'and T2Msg == 'Yes') or (order_type != 'MKT'and T2Msg == 'Yes'):
                                                PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T3Msg'] = TrigerMsg
                                                MsgToChannel = 'TARGET3 HIT ' + IndexEntry  + ' (' + DateTimeStr + ')'
                                                UpdateCSV = StoreMyPrimeQueue()
                                    #print(7)
                                    if SL_Exit_Condition == True:

                                        MsgToPrint = MsgToPrint + '\n' + 'SL hit'
                                        #print('SL hit')
                                        if SLsell_price == 0:
                                            MsgToPrint = MsgToPrint + '\n' + 'SL update'
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&L'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&LA'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1P&L'] = 0
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLsell_price'] = price
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLltp'] = price
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLhigh'] = cHigh
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLlow'] = cLow
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLtime'] = datetime.datetime.now()
                                            #if SendMessageToChannel == True  and SLMsg == 'No':
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLMsg'] = TrigerMsg
                                            if cLow < xStopLoss:
                                                MsgToChannel = 'SL HIT ' + IndexEntry + ' (' + DateTimeStr + ')'
                                            else:
                                                True
                                                #MsgToChannel = 'Exit AT CMP ' + IndexEntry + ' (' + DateTimeStr + ')'
                                            UpdateCSV = StoreMyPrimeQueue()
                                    #print(8)
                                    if SLMsg == 'No' and T1Msg == 'No' and T1sell_price == 0 and SLsell_price == 0:
                                        if GrossM2M > 0:
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1P&L'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&L'] = 0
                                        else:
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'SLP&L'] = GrossM2M
                                            PrimeQueue.loc[PrimeQueue.logtime==ltime, 'T1P&L'] = 0

                                    if MsgToChannel != '' and order_type == 'MKT' and SendMessageToChannel == True and SendMesageToTelegram == True:
                                        
                                        await client.send_message(ScalpBANKNIFTY, MsgToChannel)

                                    
                                    if order_type == 'TESTING':
                                        MsgTesting = MsgTesting + MsgToPrint
                                    elif order_type == 'MKT':
                                        MsgMKT = MsgMKT + MsgToPrint 
                                    elif order_type == 'MKT_Skip':
                                        MsgMKT_Skip = MsgMKT_Skip + MsgToPrint
                                    elif order_type == 'FINAL':
                                        MsgMKT_FINAL = MsgMKT_FINAL + MsgToPrint
                                    elif order_type == 'FINAL2':
                                        MsgMKT_FINAL2 = MsgMKT_FINAL2 + MsgToPrint
                                    elif order_type == 'FINAL3':
                                        MsgMKT_FINAL3 = MsgMKT_FINAL3 + MsgToPrint
                                    elif order_type == 'EXIT_SAFE':
                                        MsgMKT_Safe = MsgMKT_Safe + MsgToPrint
                                    elif order_type == 'EXIT_SAFE2':
                                        MsgMKT_Safe2 = MsgMKT_Safe2 + MsgToPrint
                                    elif 'SELL' in order_type:
                                        MsgMKT_SELL= MsgMKT_SELL + MsgToPrint
                                    MsgToPrint = ''
                        
                        if len(MsgMKT_Safe) > 10:
                            print('=========    Exit SAFE   ==========')
                            print(MsgMKT_Safe)
                        if len(MsgMKT_Safe2) > 10:
                            print('=========    Exit SAFE2   ==========')
                            print(MsgMKT_Safe2)
                        if len(MsgMKT_SELL) > 10:
                            print('=========    TO SELL      ==========')
                            print(MsgMKT_SELL)
                        if len(MsgTesting) > 10:
                            print('=========    ORIGINAL     ==========')
                            print(MsgTesting)
                        if len(MsgMKT) > 10:
                            print('=========    TO CHANNEL   ==========')
                            print(MsgMKT)
                        if len(MsgMKT_Skip) > 10:
                            print('=========    TO SKIP      ==========')
                            print(MsgMKT_Skip)
                        if len(MsgMKT_FINAL) > 10:
                            print('=========    FINAL      ==========')
                            print(MsgMKT_FINAL)
                        if len(MsgMKT_FINAL2) > 10:
                            print('=========    FINAL2      ==========')
                            print(MsgMKT_FINAL2)
                        if len(MsgMKT_FINAL3) > 10:
                            print('=========    FINAL3      ==========')
                            print(MsgMKT_FINAL3)
                        
                        #print(9)

                        if ForceExitACTIVEQueue == True:
                            ForceExitACTIVE = False
                            ForceExitACTIVEQueue = False
                            print('3ForceExitACTIVEQueue',ForceExitACTIVEQueue)
                            UpdateCSV = StoreMyPrimeQueue()
                        if ForceExitPENDINGQueue == True:
                            ForceExitPENDING = False
                            ForceExitPENDINGQueue = False
                            print('3ForceExitPENDINGQueue',ForceExitPENDINGQueue)
                            UpdateCSV = StoreMyPrimeQueue()
                        WhileLoopCounter = WhileLoopCounter + 1
                        #await asyncio.sleep(0.5)
                        if WhileLoopCounter >=3:
                            #print("saving csv")
                            UpdateCSV = StoreMyPrimeQueue()
                            WhileLoopCounter = 0
                        #print(10)
                #await asyncio.sleep(2)
        except Exception as e:
            print(str(e))
            #print(CurrentOrderStatus, 'error loop')
            await asyncio.sleep(5)
            #startProcessMyQueue = 0
            #RandRunQueue = KickStartProcessMyQueue()
            print('========================================================')
            #print('========================================================')
            #print('loop again')
            #print('========================================================')
            #print('========================================================')
            #await asyncio.sleep(1)
    

def KickStartProcessMyQueue():
    global startProcessMyQueue
    print("===================================")
    if startProcessMyQueue == 0:
        print('Int startProcessMyQueue', startProcessMyQueue)
        startProcessMyQueue = 1
        r2123 =  asyncio.create_task(ProcessMyQueue())
        print('end startProcessMyQueue', startProcessMyQueue)
        
def GetStockDate(d, weekday):
    
    days_ahead = weekday - d.weekday()
    days_ahead2 = (weekday - d.weekday()) + 7
    if days_ahead < 0: # Target day already happened this week
        days_ahead += 7
        days_ahead2 += 7
    
    next_thursday = d + timedelta(days_ahead)
    next_to_next_thursday = d + timedelta(days_ahead2)
    Yr = str(int(next_thursday.year) - 2000)
    M1 = next_thursday.strftime("%y%m")
    M2 = next_to_next_thursday.strftime("%y%m")
    if int(M2) > int(M1):
        StockDate = Yr + next_thursday.strftime("%b").upper()
    else:
        Mn = int(next_thursday.month)
        dt = next_thursday.strftime("%d")
        
        if Mn >= 10:
            m = next_thursday.strftime("%b")[0:1]
        else:
            m = str(Mn)
        StockDate = (Yr + m + dt)
    return StockDate

def cleanup_title(raw_text):
    ## remove all non-ascii
    raw_text = raw_text.upper()
    raw_text = raw_text.replace('𝐏𝐀𝐈𝐃', 'PAID')
    raw_text = raw_text.replace('🇪', 'E')
    raw_text = raw_text.replace('🇦', 'A')
    raw_text = raw_text.replace('🇬', 'G')
    raw_text = raw_text.replace('🇱', 'L')
    raw_text = raw_text.replace('🇸', 'S')
    raw_text = raw_text.replace('™', '')
    raw_text = raw_text.replace('Bᴀɴᴋɴɪғᴛʏ_W_Exᴘɪʀʏ', 'BNF_W_EXPIRY')

    raw_text = raw_text.replace('𝐀𝐋𝐋', 'ALL')
    text = ""
    for c in raw_text:
        if ((ord(c) == 32) or (ord(c) == 46) or (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90)):
            text += c
        else:
            text += ' '
    text = text.replace(' . ', ' ')
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    
    return text
    

def cleanup_text(raw_text):
    ## remove all non-ascii
    #print(raw_text)
    raw_text = raw_text.upper()
    raw_text = re.sub(r'\s+', ' ', raw_text)
    raw_text = raw_text.replace('BUY :-', 'BUY ABOVE')
    raw_text = raw_text.replace('𝗕𝗨𝗬', 'BUY')
    raw_text = raw_text.replace('𝗕𝗔𝗡𝗞', 'BANK')
    raw_text = raw_text.replace('𝗡𝗜𝗙𝗧𝗬', 'NIFTY')
    raw_text = raw_text.replace('Bᴀɴᴋɴɪғᴛʏ_W_Exᴘɪʀʏ', 'BNF_W_EXPIRY')
    for k in range(30,50):
        raw_text = raw_text.replace('BANKNIFTY '+ str(int(k)) + ',', 'BANKNIFTY BUY '+ str(int(k)))
    #print(raw_text)
    text = ""

    for c in raw_text:
        if ((ord(c) == 32) or (ord(c) == 46) or (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90)):
            text += c
        elif ord(c) == 64: #and ('ABOVE' not in raw_text and 'NEAR' not in raw_text and 'ABV' not in raw_text):
            text += 'ABOVE'
        else:
            text += ' '
    #print(text)
    
    OrignalCleanText = text
    if 'ACHIEVED' not in text and 'TARGET HIT' not in text and 'TARGETS HIT' not in text and text.startswith("PAID") == False:
        text = re.sub(r'\s+', ' ', text)
        text = text.replace('RISKY', ' ')
        text = text.replace('LOOKS', ' ')
        text = text.replace('GOOD', ' ')
        text = text.replace('ONLY', ' ')
        text = text.replace('SELL.', 'SELL')
        text = text.replace('BUY.', 'BUY')
        text = text.replace('PUT', 'PE')
        text = text.replace('PE.', 'PE ')
        text = text.replace(' CE', 'CE')
        text = text.replace(' PE', 'PE')
        text = text.replace('EXPIRY', ' ')
        text = text.replace('@', ' @ ')
        text = text.replace('NEAR', ' NEAR ')
        text = text.replace('BUY BANKNIFTY', ' BANKNIFTY BUY ')
        text = text.replace('ABOVE ABOVE', ' ABOVE ')
        text = text.replace('ABOVEABOVE', ' ABOVE ')
        text = text.replace('ABOVE', ' ABOVE ')
        text = text.replace('ABOVE CMP', ' ABOVE ')
        text = text.replace('ABV', ' ABV ')
        text = text.replace('CMP', ' CMP ')
        text = text.replace('TGT', ' TARGET ')
        text = text.replace('AT PRICE', 'ABOVE')
        text = text.replace('TG ', ' TARGET ')
        text = text.replace('PRICE', ' ABOVE ')
        text = text.replace('ADD MORE AT', ' ')
        text = text.replace('AT ABOVE', 'ABOVE')
        
        for number in range(1, 32):
            for k in range(2,0,-1):
                text = text.replace(str(number).zfill(k) + 'ST', ' ')
                text = text.replace(str(number).zfill(k) + 'ND', ' ')
                text = text.replace(str(number).zfill(k) + 'RD', ' ')
                text = text.replace(str(number).zfill(k) + 'TH', ' ')
            
        for m in range(1,13):
            m_Short = datetime.date(1900, m, 1).strftime('%b').upper()
            m_Full = datetime.date(1900, m, 1).strftime('%B').upper()
            
            text = text.replace(m_Full, ' ')
            text = text.replace(" "+m_Short+" ", ' ')
            
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = text.replace('@ @', '@')
        text = text.replace('@@', '@')

        #print("CleanText = ", text)

        #print(text)
        raw_OrderMsg = text
        raw_OrderMsg = raw_OrderMsg.replace('SL PAID', 'SL 0')
        
        raw_OrderMsg = raw_OrderMsg.replace('TARGET OPEN', ' ')
        #if "TARGET" not in raw_OrderMsg:
        #   raw_OrderMsg = raw_OrderMsg + " TARGET 0 SL 0"
        
        raw_OrderMsg = raw_OrderMsg.replace('BANK NIFTY', 'BANKNIFTY')

        list_ = ['@', 'AT' , 'ABOVE' , 'ABV', 'CMP']
        if all(word not in raw_OrderMsg for word in list_):
            if 'PE BUY' in raw_OrderMsg:
                raw_OrderMsg = raw_OrderMsg.replace("PE BUY", "PE BUY ABOVE")
            elif 'CE BUY' in raw_OrderMsg:
                raw_OrderMsg = raw_OrderMsg.replace("CE BUY", "CE BUY ABOVE")
            else:
                raw_OrderMsg = raw_OrderMsg.replace("CE ", "CE ABOVE ")
                raw_OrderMsg = raw_OrderMsg.replace("PE ", "PE ABOVE ")
        
        if 'HEDGE' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('HEDGE','')
            raw_OrderMsg = "HEDGE " + raw_OrderMsg
        if 'CE BUY AB' in raw_OrderMsg and 'BANKNIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('CE BUY AB','CE AB')
            raw_OrderMsg = raw_OrderMsg.replace('BANKNIFTY','BANKNIFTY BUY ')
        elif 'PE BUY AB' in raw_OrderMsg and 'BANKNIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('PE BUY AB','PE AB')
            raw_OrderMsg = raw_OrderMsg.replace('BANKNIFTY','BANKNIFTY BUY ')
        elif 'CE BUY AB' in raw_OrderMsg and 'NIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('CE BUY AB','CE AB')
            raw_OrderMsg = raw_OrderMsg.replace('NIFTY','NIFTY BUY ')
        elif 'PE BUY AB' in raw_OrderMsg and 'NIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('PE BUY AB','PE AB')
            raw_OrderMsg = raw_OrderMsg.replace('NIFTY','NIFTY BUY ')
        elif 'CE BUY AB' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('CE BUY AB','CE AB')
            raw_OrderMsg = "BUY " + raw_OrderMsg
        elif 'PE BUY AB' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('PE BUY AB','PE AB')
            raw_OrderMsg = "BUY " + raw_OrderMsg
        elif 'BUY' not in raw_OrderMsg and 'BANKNIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('BANKNIFTY','BANKNIFTY BUY ')
        elif 'BUY' not in raw_OrderMsg and 'NIFTY' in raw_OrderMsg:
            raw_OrderMsg = raw_OrderMsg.replace('NIFTY','NIFTY BUY ')

        raw_OrderMsg = raw_OrderMsg.replace('BUY NIFTY','NIFTY BUY')
        raw_OrderMsg = raw_OrderMsg.replace('BUY BANKNIFTY','BANKNIFTY BUY')
        raw_OrderMsg = raw_OrderMsg.replace('  ',' ')
        raw_OrderMsg = raw_OrderMsg.replace('  ',' ')
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = raw_OrderMsg

    #print(text)
    return text, OrignalCleanText

async def ProcessMyText(raw_OrderMsg, name, sender_id):
    
    global PrimeQueue
    global MaxBudget
    global MaxLotSize
    global TakeProfitPcent
    global StopLossPcent
    global MinTakeProfit
    global MinStopLoss
    global TakeProfitLoopPcent
    global StopLossLoopPcent
    global ScriptRunMode
    global TradeStartHour
    global TradeStartMinute
    global TradeStartSecond
    global DoHedgeTrade
    
    global LastCallHour
    global LastCallMin

    RandRunQueue = KickStartProcessMyQueue()
    raw_OrderMsg = re.sub(r'\(.*\)', '', raw_OrderMsg)

    #Man_R1 = r"(BUY|SELL)\s?[0-9]*\s([A-Z0-9CEPE]*)\s[@|AT|ABOVE|ABV|CMP]*\s([0-9.]*)[-0-9.,\s]*([TARGET|TGT|PT]*)\s+([0-9.]*)[-0-9.,\s]*(SL)*\s([0-9.]*)[-0-9.,\s]*([TARGET|TGT|PT]*)\s+([0-9.]*)"
    RegExEntry = "(BUY|SELL)\s?[0-9]*\s([A-Z0-9CEPE]*)\s[@|AT|ABOVE|NEAR|ABV|CMP]*\s([0-9.]*)[\s]?([0-9.]*)"
    RegExPT = "(TARGET|TGT|PT)\s+([0-9.]*)[\s]?([0-9.]*)[\s]?([0-9.]*)"
    RegExSL = "\s(SL)\s([0-9.]*)"
    
    #generic_re = re.compile("(%s)" % (Man_R1)).findall(raw_OrderMsg)
    
    generic_re_EntryMaster = re.compile("(%s)" % (RegExEntry)).findall(raw_OrderMsg)
    generic_re_PT = re.compile("(%s)" % (RegExPT)).findall(raw_OrderMsg)
    generic_re_SL = re.compile("(%s)" % (RegExSL)).findall(raw_OrderMsg)
    
    ind = 0
    #lot_size = 25
    print(raw_OrderMsg)
    print(generic_re_EntryMaster)
    print(generic_re_PT)
    print(generic_re_SL)
    ReMatchCount = len(generic_re_EntryMaster)
    if "HEDG" in raw_OrderMsg and ReMatchCount > 1: 
        HEDGE = True
    else:
        HEDGE = False
    BNF = False
    NFT = False
    FIN = False
    if "BANKNIFTY" in raw_OrderMsg:
        BNF = True
    if BNF == False:
        if "NIFTY" in raw_OrderMsg:
            NFT = True
    if BNF == False and NFT == False:
        if "FINNIFTY" in raw_OrderMsg:
            FIN = True
    raw_OrderMsgPrint = raw_OrderMsg

    try:
        for generic_re_Entry in generic_re_EntryMaster:
            print(0)
            
            tag= sender_id_Lookup(sender_id)
            TargetLevel = TargetLookup(sender_id)
            print(1)
            if tag == sender_id:
                if name == '':
                    name = sender_id 
            else:
                name = tag

            if name == '':
                name = sender_id 
            EntryType = generic_re_Entry[1]
            StockCode = generic_re_Entry[2]
            xE1 = float(generic_re_Entry[3])
            xE2 = 0
            if generic_re_Entry[4] != '':
                xE2 = float(generic_re_Entry[4])
                pDiffVal = abs(xE1 - xE2)
                if pDiffVal > 20:
                    xE2 = xE1 + 20

            if xE2 == 0:
                xE2 = xE1
            ePrice = 0
            ePrice2 = 0
            print(2)
            if xE1 > xE2:
                ePrice = xE2
                ePrice2 = xE1
                ePriceMax = xE1
            else:
                ePrice = xE1
                ePrice2 = xE2
                ePriceMax = xE2
                
            eTarget = 0
            eTarget2 = 0
            eTarget3 = 0
            eTargetTxt = ""
            if generic_re_PT != []:
                eTargetTxt = generic_re_PT[0][1]
                
                if generic_re_PT[0][2] != '':
                    eTarget = float(generic_re_PT[0][2])
                if generic_re_PT[0][3] != '':
                    eTarget2 = float(generic_re_PT[0][3])
                if generic_re_PT[0][4] != '':
                    eTarget3 = float(generic_re_PT[0][4])
            print(3)
            eStopLossTxt = ""
            eStopLoss = 0
            if generic_re_SL != []:
                print(generic_re_SL[0][1])
                eStopLossTxt = generic_re_SL[0][1]
                if generic_re_SL[0][2] != '':
                    eStopLoss = float(generic_re_SL[0][2])
            

            if eTarget == 0 or eTarget < ePriceMax:
                xTargetTemp = round(ePriceMax * 0.1,0)
                if xTargetTemp < 10: 
                    xTargetTemp  = 10
                eTarget = ePriceMax + xTargetTemp
                eTarget2 = ePriceMax + (xTargetTemp * 2)
                eTarget3 = ePriceMax + (xTargetTemp * 3)
            if eTarget > 100:
                xTargetTemp = round(ePriceMax * 0.1,0)
                if xTargetTemp < 10: 
                    xTargetTemp  = 10
                #eTarget3 = eTarget
                eTarget = ePriceMax + (xTargetTemp * 1)
                eTarget2 = ePriceMax + (xTargetTemp * 2)
                eTarget3 = ePriceMax + (xTargetTemp * 3)

            if eStopLoss == 0:
                if ePrice > 40:
                    xStopLossTemp = round(ePriceMax * 0.1,0)
                    if xStopLossTemp < 20: 
                        xStopLossTemp  = 20
                    eStopLoss = ePrice - xStopLossTemp
            
            #print('Profit:', eTarget, eStopLoss)
            
            #print('Profit:', eTarget, eStopLoss)
            #print(StockCode)
            print(4)
            if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                StockCode = TodayCodeBNF + StockCode
            elif FIN == True and "FINNIFTY" not in StockCode:
                StockCode = TodayCodeFIN + StockCode
            elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                StockCode = TodayCodeNFT + StockCode
            if "BANKNIFTY" in StockCode:
                IndexName = 'BANKNIFTY'
                IndexEntry1 = StockCode.replace(TodayCodeBNF,"")
            elif  "NIFTY" in StockCode:
                IndexName = 'NIFTY'
                IndexEntry1 = StockCode.replace(TodayCodeNFT,"")
            elif "FIN" in StockCode:
                IndexName = 'FINNIFTY'
                IndexEntry1 = StockCode.replace(TodayCodeFIN,"")
            #print(StockCode)
            #token, lot_size = instrumentLookup(fut_df,StockCode)
            token, lot_size = instrumentLookup(nfo_df,StockCode)
            print(5)
            print(token, lot_size, StockCode)
            ltp = kite.quote(token)
            print(ltp)
            price = ltp[str(token)]['last_price']
            print(token, lot_size, StockCode, price)
            
            pDiff = price - ePrice
            print(pDiff,ePrice)
            pDiffP = round(pDiff / ePrice,3)

            #print('ePrice: ', ePrice, ' CMP: ', price, ' pDiff: ', pDiff)

            EntryTypeChanged = False
            ChangeTypeSuccess = True
            if EntryType == 'SELL' and (StockCode.endswith("PE") or StockCode.endswith("CE")):
                ChangeTypeSuccess = False
                EntryType = 'BUY'
                if  StockCode.endswith("PE"):
                    StockCode = StockCode[:-2] + 'CE'
                if  StockCode.endswith("CE"):
                    StockCode = StockCode[:-2] + 'PE'
                ChangeTypeSuccess = True
                EntryTypeChanged = True
            if ChangeTypeSuccess == False:
                return raw_OrderMsg
            
            if EntryTypeChanged == True:
                token, lot_size = instrumentLookup(nfo_df,StockCode)
                ltp = kite.quote(token)
                price = ltp[str(token)]['last_price']
                print(token, lot_size, StockCode, price)

                
                if pDiff > 20:
                    ePrice = round(price + (price * pDiffP),2)
                else:
                    ePrice = price
                print('ePrice: ', ePrice, ' CMP: ', price, ' pDiff: ', pDiff, ' pDiffP: ', pDiffP, ' diffVal: ', price * pDiffP)
                
            
            Mn = datetime.datetime.now().minute
            Hr = datetime.datetime.now().hour
            Sc = datetime.datetime.now().second
            #print('aaaa')
            spotpriceTmp = 0
            if Hr > TradeStartHour:
                spotpriceTmp = price
            elif Hr == TradeStartHour:
                if Mn > TradeStartMinute or (Mn == TradeStartMinute and Sc > TradeStartSecond):
                    spotpriceTmp = price
            
            
            #tag, minentryprice, maxentryprice, stoploss, takeprofit, minentryprice1, maxentryprice1, stoploss1, takeprofit1, maxcutoff, maxquantity, trailstoploss, minentrytime, maxentrytime, maxtimedif, maxbuypriceDiff = settingsLookup(sender_id)

            ChannelChk = 'Shortlisted'
            trailstoploss = 'No'
            print(name)
            if name == 'BASIC' and False:
                ScriptRunMode = 'SelectedSL'
            else:
                ScriptRunMode = 'SingleSL'
            ScriptRunMode = 'ToChannel'
            #if name == "PAID ALL":
            #    ScriptRunMode = "SingleSL"
            #order_type = 'MKT'
            order_type = 'TESTING'

            if HEDGE == True:
                order_type = 'TESTING_HEDGE'
                #ePrice = spotpriceTmp
                #entryQty = math.floor(10000 / spotpriceTmp / lot_size) * lot_size
                #if entryQty == 0:
                #    entryQty = lot_size
                #if entryQty == 25 and ((spotpriceTmp * lot_size) < 7000):
                #    entryQty = 50
                #elif entryQty > 10000:
                #    entryQty = math.floor(10000 / lot_size) * lot_size
            else:
                True
                '''if ePrice > spotpriceTmp:
                    ePriceForQTY = ePrice
                else:
                    ePriceForQTY = spotpriceTmp
                if name == 'BASIC':
                    entryQty = math.floor(25000 / ePriceForQTY / lot_size) * lot_size
                else:
                    entryQty = math.floor(50000 / ePriceForQTY / lot_size) * lot_size
                
                #if entryQty > 400:
                    #entryQty = math.floor(400 / lot_size) * lot_size
                if entryQty == 0 or spotpriceTmp == 0:
                    entryQty = lot_size
                if entryQty == 25:
                    entryQty = 50'''
            
            entryQty = lot_size * 2

            if spotpriceTmp > 0 and False:
                if spotpriceTmp >= ePrice:
                    if ePrice >= 300:
                        ePrice = spotpriceTmp + 2
                    elif ePrice >= 70:
                        ePrice = spotpriceTmp + 1.5
                    else:
                        ePrice = spotpriceTmp + 1.25
            
            print('StockCode', StockCode, 'price:', ePrice,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty)
            TmpEP = 0
            TmpSP = 0
            ThisIsNewEntryPrimary = True
            ToChannelQueue = pd.DataFrame()
            ToChannelQueue = PrimeQueue[(PrimeQueue['ScriptRunMode'] != 'ToChannel')]
            if len(ToChannelQueue) > 0:
                ToChannelQueueTOpen = pd.DataFrame()
                ToChannelQueueTOpen = ToChannelQueue[(ToChannelQueue['order_number'] !=11)]
                if len(ToChannelQueueTOpen) > 0:
                    ToChannelQueueOpenEntry = pd.DataFrame()
                    ToChannelQueueOpenEntry = ToChannelQueueTOpen[(ToChannelQueueTOpen['symbol'] == StockCode)]
                    if len(ToChannelQueueOpenEntry) > 0:
                        for i in range(0, len(ToChannelQueueOpenEntry)):
                            Curentry_price = ToChannelQueueOpenEntry.iloc[i]['entry_price']
                            Curspotprice = ToChannelQueueOpenEntry.iloc[i]['spotprice']
                            if Curentry_price > TmpEP:
                                TmpEP = Curentry_price
                            if Curspotprice > TmpSP:
                                TmpSP = Curspotprice
                        if TmpSP > TmpEP:
                            PriceToCheck = TmpSP
                        else:
                            PriceToCheck = TmpEP

                        if spotpriceTmp > ePrice:
                            CurPriceToCheck = spotpriceTmp
                        else:
                            CurPriceToCheck = ePrice
                        if CurPriceToCheck >= (PriceToCheck * 1.1):
                            ThisIsNewEntryPrimary = True
                        else:
                            ThisIsNewEntryPrimary = False


            print('===========      First Order  FixTarget-SelectedSL  =================')
            ltime = datetime.datetime.now()
            
            PriceDiff = round(spotpriceTmp / ePrice,2)
            if (PriceDiff >= 0.8 and PriceDiff <= 1.2) == False:
                eStopLossPcent = eStopLoss / price
                eStopLossDif = price - eStopLoss
                if eStopLossPcent > 0.2 and eStopLossDif > 30:
                    eStopLoss = int(price * 0.9)

            eTarget = round(eTarget,2)
            eTarget2 = round(eTarget2,2)
            eTarget3 = round(eTarget3,2)
            eStopLoss = round(eStopLoss,2)
            try:
                TipBy = str(name) + '_O'
            except:
                TipBy = str(sender_id) + '_O'
            #print('Profit:', eTarget, eStopLoss)
            TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
            TempEntryQueue = TempEntryQueue.append({'symbol': StockCode,
                                                    'buy_sell': EntryType,
                                                    'spotprice': spotpriceTmp,
                                                    'entry_price': ePrice,
                                                    'entry_price2': ePrice2,
                                                    'quantity': entryQty,
                                                    'order_type': order_type,
                                                    'logtime': ltime,
                                                    'ordertime':'',
                                                    'buy_price':0,
                                                    'inv_amount':0,
                                                    'ltp':0,
                                                    'high':0,
                                                    'low':0,
                                                    'T1': eTarget,
                                                    'T1Msg':'No',
                                                    'T1ltp':0,
                                                    'T1high':0,
                                                    'T1low':0,
                                                    'T1P&L':0,
                                                    'T1P&LA':0,
                                                    'T1time':'',
                                                    'T1sell_price':0,
                                                    'T2': eTarget2,
                                                    'T2Msg':'No',
                                                    'T2ltp':0,
                                                    'T2high':0,
                                                    'T2low':0,
                                                    'T2P&L':0,
                                                    'T2P&LA':0,
                                                    'T2time':'',
                                                    'T2sell_price':0,
                                                    'T3': eTarget3,
                                                    'T3Msg':'No',
                                                    'T3ltp':0,
                                                    'T3high':0,
                                                    'T3low':0,
                                                    'T3P&L':0,
                                                    'T3P&LA':0,
                                                    'T3time':'',
                                                    'T3sell_price':0,
                                                    'SL1': eStopLoss,
                                                    'SLMsg':'No',
                                                    'SLltp':0,
                                                    'SLhigh':0,
                                                    'SLlow':0,
                                                    'SLP&L':0,
                                                    'SLP&LA':0,
                                                    'SLtime':'',
                                                    'SLsell_price':0,
                                                    'IndexName': IndexName,
                                                    'IndexEntry': IndexEntry1,
                                                    'trailstoploss': 'No',
                                                    'ScriptRunMode': ScriptRunMode,
                                                    'ChannelChk': ChannelChk,
                                                    'tag': TipBy,
                                                    'order_number': '',
                                                    'senderid':sender_id,
                                                    'CutOffCheck1': 0,
                                                    'CutOffCheck2': 0,
                                                    'token':token
                                                    }, ignore_index=True)



            #CurrentOrderStatus = CheckLTPandPlaceOrder(TempEntryQueue.iloc[0], ltp)
            #print('thats here 5', CurrentOrderStatus)
            #if CurrentOrderStatus == 'YesOrderIsPlaced':
            if spotpriceTmp >= ePrice:
                inv_amount = entryQty * price
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'buy_price'] = price
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'low'] = price
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'high'] = price
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ltp'] = price
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'inv_amount'] = inv_amount
            
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 1
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
            #elif CurrentOrderStatus == 'NoSkipEntry':
            #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 11
            #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = 'Skipped'

            PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
            
            UpdateCSV = StoreMyPrimeQueue()
            CurrentOrderStatus = ''

            FinalOrderMsg = (EntryType, StockCode, "ABOVE", ePrice, "Target", eTarget, "StopLoss", eStopLoss)
            raw_OrderMsgPrint = FinalOrderMsg
        
    except Exception as e:
        print('Error 0', str(e))     
    ind += 1

    #==========================================================================================================
    #====================================  TO CHANNEL      ====================================================
    #==========================================================================================================
    #==========================================================================================================
    
    #This for Telegram
    #if len(generic_re_EntryMaster) == 1 and ThisIsNewEntryPrimary == True:
    try:
        if len(generic_re_EntryMaster) == 1:
            print('try this is new entry')
            Mn = datetime.datetime.now().minute
            Hr = datetime.datetime.now().hour
            Sc = datetime.datetime.now().second


            IsAnyPositionOpen = False
            ToChannelQueue = pd.DataFrame()
            ToChannelQueue = PrimeQueue[(PrimeQueue['order_type'] == 'MKT')]
            if len(ToChannelQueue) > 0:
                ToChannelQueueTOpen = pd.DataFrame()
                ToChannelQueueTOpen = ToChannelQueue[(ToChannelQueue['T2Msg'] == 'No')]
                if len(ToChannelQueueTOpen) > 0:
                    ToChannelQueueSOpen = pd.DataFrame()
                    ToChannelQueueSOpen = ToChannelQueueTOpen[(ToChannelQueueTOpen['SLMsg'] == 'No')]
                    if len(ToChannelQueueSOpen) > 0:
                        IsAnyPositionOpen = True

            NextCallTime = datetime.time(LastCallHour,LastCallMin + 5,1,1)
            TradeStartTime = datetime.time(TradeStartHour,TradeStartMinute + 1,1,1)
            CurrentTime = datetime.datetime.now().time()

            SelectedList = ['BANK NIFTY SURE SHOT','EAGLE ZERO HERO','HERO ZERO HNI CALLS','NIFTY_EXPONENTIAl','ONE CALL','BNF 5000 DAILY']

            def FindMatch(sName):
                for ChannelName in SelectedList:
                    if ChannelName.upper() == name.upper():
                        return True
                return False
            if FindMatch(name):
                order_type = 'MKT'
            elif  (((CurrentTime >= TradeStartTime and (CurrentTime >= NextCallTime or IsAnyPositionOpen == False))) and price <= 600):
                LastCallHour = Hr
                if Mn >54:
                    LastCallMin = 54
                else:
                    LastCallMin = Mn
                order_type = 'MKT'
            else:
                order_type = 'MKT_Skip'
            ltime = datetime.datetime.now()
            for generic_re_Entry in generic_re_EntryMaster:
                #print(1)
                
                #name = str(name) + '_H' 
                EntryType = generic_re_Entry[1]
                StockCode = generic_re_Entry[2]
                ePrice = float(generic_re_Entry[3])

                #print(StockCode)
                if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                    StockCode = TodayCodeBNF + StockCode
                elif FIN == True and "FINNIFTY" not in StockCode:
                    StockCode = TodayCodeFIN + StockCode
                elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                    StockCode = TodayCodeNFT + StockCode
                
                token1, lot_size1 = instrumentLookup(nfo_df,StockCode)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                AwaitDiff = 0
                if price1 < ePrice and abs(ePrice - price1) >= 3:
                    AwaitEntry = True
                    AwaitDiff = (ePrice - price1) / price1
                    AwaitDiff = AwaitDiff * 1.1

                else:
                    AwaitEntry = False
                if StockCode.endswith("CE"):
                    IndexType1 = "CE"
                    IndexType2 = "PE"
                else:
                    IndexType1 = "PE"
                    IndexType2 = "CE"
                

                IndexEntryCode2 = ''
                if "BANKNIFTY" in StockCode:
                    IndexName = 'BANKNIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeBNF,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY BANK').get('NSE:NIFTY BANK').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100) + 100
                    if IndexEntry1 >= CurrentIndexRange:
                        IndexEntry1 = IndexEntry1 - 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                        #    IndexEntry1 = CurrentIndexRange + 200
                    else:
                        IndexEntry1 = IndexEntry1 + 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                         #   IndexEntry1 = CurrentIndexRange - 200

                    IndexEntryCode1 = TodayCodeBNF + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif FIN == True and False:
                    IndexEntry1 = int(StockCode.replace(TodayCodeFIN,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY FIN SERVICE').get('NSE:NIFTY FIN SERVICE').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexEntry1 >= CurrentIndexRange:
                        IndexEntry1 = IndexEntry1 - 50
                    else:
                        IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeFIN + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif  "NIFTY" in StockCode:
                    IndexName = 'NIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeNFT,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY 50').get('NSE:NIFTY 50').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexEntry1 >= CurrentIndexRange:
                        IndexEntry1 = IndexEntry1 - 50
                    else:
                        IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeNFT + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)

                #print(StockCode)
                #token, lot_size = instrumentLookup(fut_df,StockCode)
                token1, lot_size1 = instrumentLookup(nfo_df,IndexEntryCode1)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                price1 = round(price1,2)
                EntryPrice1 = price1
                if AwaitEntry == True:
                    EntryLevel1 = round(price1 * AwaitDiff,2)
                    if EntryLevel1 < 1:
                        EntryLevel1 = 1
                    EntryPrice1 = int(price1 + EntryLevel1)
                if price1 >= 10 or EntryPrice1 > 10:
                    if AwaitEntry == True:
                        EntryLevel1 = round(price1 * AwaitDiff,2)
                        if EntryLevel1 < 4:
                            EntryLevel1 = 4
                        EntryPrice1 = int(round(((price1 + EntryLevel1) / 5),0)* 5)
                        #EntryPrice1 = int(price1 + EntryLevel1)
                        entry_price2 = 0
                        CurTarget = round(EntryPrice1 * 0.05,0)
                        if CurTarget < 6:
                            CurTarget = 5
                        elif CurTarget < 12:
                            CurTarget =10
                        elif CurTarget < 22:
                            CurTarget =15
                        else:
                            CurTarget = 20
                        
                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    else:
                        EntryLevel1 = round(price1 * 0.06,2)
                        EntryLevel2 = round(price1 * 0.03,2)

                        if EntryLevel1 > 10:
                            EntryLevel1 = 10
                        elif EntryLevel1 < 4:
                            EntryLevel1 = 4
                        if EntryLevel2 > 5:
                            EntryLevel2 = 5
                        elif EntryLevel2 < 2:
                            EntryLevel2 = 2
                        EntryPrice1 = int(((price1 - EntryLevel1) / 10))* 10
                        entry_price2 = int(((price1 - EntryLevel2) / 10))* 10

                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int((price1 + EntryLevel1) / 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1 - 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1)

                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        if entry_price2 < 1:
                            entry_price2 = 1
                        CurTarget = round(EntryPrice1 * 0.1,0)
                        if CurTarget < 7:
                            CurTarget = 5
                        elif CurTarget < 12:
                            CurTarget =10
                        elif CurTarget < 17:
                            CurTarget =15
                        else:
                            CurTarget = 20
                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    

                    if T1 < price1:
                        T1 = int(entry_price2 + (CurTarget * 1))
                        T2 = int(entry_price2 + (CurTarget * 2))
                        T3 = int(entry_price2 + (CurTarget * 3))

                    if T1 < price1:
                        T1 = int(price1 + (CurTarget * 0.5))
                        T2 = int(price1 + (CurTarget * 1))
                        T3 = int(price1 + (CurTarget * 1.5))

                    T1 = round(T1,2)
                    T2 = round(T2,2)
                    T3 = round(T3,2)

                    if AwaitEntry == True:
                        if abs(price1 - T1) < 5:
                            T1 += 5
                        if abs(T1 - T2) < 5:
                            T2 += 5
                        if abs(T2 - T3) < 5:
                            T3 += 5
                    else:
                        if abs(price1 - T1) < 5:
                            T1 += 5
                        if abs(T1 - T2) < 5:
                            T2 += 5
                        if abs(T2 - T3) < 5:
                            T3 += 5

                    CurSL = round(EntryPrice1 * 0.1,0)
                    SL = int(EntryPrice1 - (CurSL * 1))
                    if CurSL < 10:
                        CurSL = int(EntryPrice1 + (CurTarget * 1))
                    if EntryPrice1 < 25:
                        SL = 0
                    if AwaitEntry == True:
                        TradeMsg = 'I AM BUYING ' + IndexName + ' ' + str(IndexEntry1) + IndexType1 + '\nENTRY ABOVE: ' + str(EntryPrice1) + '' + '\nTGT: ' + str(T1) + '/' + str(T2) + '/' + str(T3)  + ' \nSL: ' + str(SL)
                    else:
                        TradeMsg = 'I AM BUYING ' + IndexName + ' ' + str(IndexEntry1) + IndexType1 + '\nENTRY AT: ' + str(EntryPrice1) + ' - ' + str(entry_price2) + '' + ' \nTGT: ' + str(T1) + '/' + str(T2) + '/' + str(T3) + ' \nSL: ' + str(SL)
                    

                    """print(ePriceForQTY)
                                                                    ePrice1 = price1
                                                                    entryQty1 = math.floor(50000 / ePriceForQTY / lot_size1) * lot_size1
                                                                    if entryQty1 < 150:
                                                                        entryQty1 = 150
                                                                    elif entryQty1 > 1000:
                                                                        entryQty1 = math.floor(1000 / lot_size1) * lot_size1"""
                    entryQty1 = lot_size1 * 2
                    inv_amount = entryQty1 * ePriceForQTY
                    #print('StockCode', IndexEntryCode1, 'price:', ePrice1,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty1)
                    
                    ThisIsNewEntry = True
                    ToChannelQueue = pd.DataFrame()
                    ToChannelQueue = PrimeQueue[(PrimeQueue['order_type'] == 'MKT')]
                    if len(ToChannelQueue) > 0:
                        ToChannelQueueTOpen = pd.DataFrame()
                        ToChannelQueueTOpen = ToChannelQueue[(ToChannelQueue['T1Msg'] == 'No')]
                        if len(ToChannelQueueTOpen) > 0:
                            ToChannelQueueSOpen = pd.DataFrame()
                            ToChannelQueueSOpen = ToChannelQueueTOpen[(ToChannelQueueTOpen['SLMsg'] == 'No')]
                            if len(ToChannelQueueSOpen) > 0:
                                ToChannelQueueOpenEntry = pd.DataFrame()
                                ToChannelQueueOpenEntry = ToChannelQueueSOpen[(ToChannelQueueSOpen['symbol'] == IndexEntryCode1)]
                                if len(ToChannelQueueOpenEntry) > 0:
                                    ThisIsNewEntry = False

                    entry_price_diference = abs(EntryPrice1 - price1)

                    if ThisIsNewEntry == False or entry_price_diference > 40:
                        order_type = 'MKT_Skip'
                    if True:
                        try:
                            TipBy = str(name) + '_H'
                        except:
                            TipBy = str(sender_id) + '_H'
                        #print('Profit:', eTarget, eStopLoss)
                        TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
                        TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode1,
                                                                'buy_sell': 'BUY',
                                                                'spotprice': price1,
                                                                'entry_price': EntryPrice1,
                                                                'entry_price2': entry_price2,
                                                                'quantity': entryQty1,
                                                                'order_type': order_type,
                                                                'logtime': ltime,
                                                                'ordertime':'',
                                                                'buy_price':0,
                                                                'inv_amount':inv_amount,
                                                                'ltp':0,
                                                                'high':0,
                                                                'low':0,
                                                                'T1': T1,
                                                                'T1Msg':'No',
                                                                'T1ltp':0,
                                                                'T1high':0,
                                                                'T1low':0,
                                                                'T1P&L':0,
                                                                'T1P&LA':0,
                                                                'T1time':'',
                                                                'T1sell_price':0,
                                                                'T2': T2,
                                                                'T2Msg':'No',
                                                                'T2ltp':0,
                                                                'T2high':0,
                                                                'T2low':0,
                                                                'T2P&L':0,
                                                                'T2P&LA':0,
                                                                'T2time':'',
                                                                'T2sell_price':0,
                                                                'T3': T3,
                                                                'T3Msg':'No',
                                                                'T3ltp':0,
                                                                'T3high':0,
                                                                'T3low':0,
                                                                'T3P&L':0,
                                                                'T3P&LA':0,
                                                                'T3time':'',
                                                                'T3sell_price':0,
                                                                'SL1': SL,
                                                                'SLMsg':'No',
                                                                'SLltp':0,
                                                                'SLhigh':0,
                                                                'SLlow':0,
                                                                'SLP&L':0,
                                                                'SLP&LA':0,
                                                                'SLtime':'',
                                                                'SLsell_price':0,
                                                                'IndexName': IndexName,
                                                                'IndexEntry': str(IndexEntry1) + IndexType1,
                                                                'trailstoploss': 'No',
                                                                'ScriptRunMode': ScriptRunMode,
                                                                'ChannelChk': ChannelChk,
                                                                'tag': TipBy,
                                                                'order_number': '',
                                                                'senderid':sender_id,
                                                                'CutOffCheck1': 0,
                                                                'CutOffCheck2': 0,
                                                                'token':token1
                                                                }, ignore_index=True)
                        
                        try:
                            if "T" in TargetLevel:      
                                #==========================================================================================================
                                #==================================DAILY Target Check======================================================
                                #==========================================================================================================
                                #==========================================================================================================
                                ltime2 = datetime.datetime.now()
                                print(TargetLevel,ltime2)
                                TestingEntryQueue = TempEntryQueue.copy()
                                if price1 >= EntryPrice1 - 1:
                                    entry_price = price1 + 1
                                else:
                                    entry_price = EntryPrice1
                                TestingEntryQueue.loc[TestingEntryQueue.logtime==ltime, 'entry_price'] = entry_price
                                TestingEntryQueue.loc[TestingEntryQueue.logtime==ltime, 'trailstoploss'] = TargetLevel
                                TestingEntryQueue.loc[TestingEntryQueue.logtime==ltime, 'order_type'] = 'FINAL'
                                TestingEntryQueue.loc[TestingEntryQueue.logtime==ltime, 'tag'] = str(name) + '_F'
                                TestingEntryQueue.loc[TestingEntryQueue.logtime==ltime, 'logtime'] = ltime2


                                ltime3 = datetime.datetime.now()
                                print(TargetLevel,ltime3)
                                TestingEntryQueue2 = TestingEntryQueue.copy()
                                TestingEntryQueue2.loc[TestingEntryQueue2.logtime==ltime2, 'order_type'] = 'FINAL2'
                                TestingEntryQueue2.loc[TestingEntryQueue2.logtime==ltime2, 'tag'] = str(name) + '_F2'
                                TestingEntryQueue2.loc[TestingEntryQueue2.logtime==ltime2, 'logtime'] = ltime3

                                ltime4 = datetime.datetime.now()
                                print(TargetLevel,ltime4)
                                TestingEntryQueue3 = TestingEntryQueue.copy()
                                TestingEntryQueue3.loc[TestingEntryQueue3.logtime==ltime2, 'order_type'] = 'FINAL3'
                                TestingEntryQueue3.loc[TestingEntryQueue3.logtime==ltime2, 'tag'] = str(name) + '_F3'
                                TestingEntryQueue3.loc[TestingEntryQueue3.logtime==ltime2, 'logtime'] = ltime4
                        except Exception as e:
                            print('Error to add FINAL entries', str(e))

                        if price1 >= EntryPrice1:
                            inv_amount = entryQty1 * price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'buy_price'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'low'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'high'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ltp'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'inv_amount'] = inv_amount
                        
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
                        #elif CurrentOrderStatus == 'NoSkipEntry':
                        #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 11
                        #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = 'Skipped'

                        
                        PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
                        if TargetLevel != 'NA':
                            PrimeQueue = PrimeQueue.append(TestingEntryQueue.iloc[0])
                            PrimeQueue = PrimeQueue.append(TestingEntryQueue2.iloc[0])
                            PrimeQueue = PrimeQueue.append(TestingEntryQueue3.iloc[0])
                        UpdateCSV = StoreMyPrimeQueue()
                        CurrentOrderStatus = ''
                        if order_type == 'MKT' and SendMesageToTelegram == True:
                            await client.send_message(ScalpBANKNIFTY, TradeMsg)
                        print('StockCode', IndexEntryCode1, 'price:', price1,',EntryPrice1: ', EntryPrice1, ', entry_price2:',entry_price2, 'T1', T1, 'SL', SL)
                        
                        #print('===========      First Order  FixTarget-SingleStockSL HEDGE 1  =================')
        
    except Exception as e:
        print('Error 1', str(e))            
    #==========================================================================================================
    #==================================EXIT_SAFE===============================================================
    #==========================================================================================================
    #==========================================================================================================
    
    #This for Telegram
    #if len(generic_re_EntryMaster) == 1 and ThisIsNewEntryPrimary == True:
    try:
        if len(generic_re_EntryMaster) == 1 and False:
            print('try this is new EXIT_SAFE entry')
            Mn = datetime.datetime.now().minute
            Hr = datetime.datetime.now().hour
            Sc = datetime.datetime.now().second

            order_type = 'EXIT_SAFE'
            ltime = datetime.datetime.now()
            for generic_re_Entry in generic_re_EntryMaster:
                #print(1)
                
                #name = str(name) + '_H' 
                EntryType = generic_re_Entry[1]
                StockCode = generic_re_Entry[2]
                ePrice = float(generic_re_Entry[3])

                #print(StockCode)
                if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                    StockCode = TodayCodeBNF + StockCode
                elif FIN == True and "FINNIFTY" not in StockCode:
                    StockCode = TodayCodeFIN + StockCode
                elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                    StockCode = TodayCodeNFT + StockCode
                
                token1, lot_size1 = instrumentLookup(nfo_df,StockCode)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                AwaitDiff = 0
                if price1 < ePrice and abs(ePrice - price1) >= 3:
                    AwaitEntry = True
                    AwaitDiff = (ePrice - price1) / price1
                    AwaitDiff = AwaitDiff * 1.1

                else:
                    AwaitEntry = False
                if StockCode.endswith("CE"):
                    IndexType1 = "CE"
                    IndexType2 = "PE"
                else:
                    IndexType1 = "PE"
                    IndexType2 = "CE"
                

                IndexEntryCode2 = ''
                if "BANKNIFTY" in StockCode:
                    IndexName = 'BANKNIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeBNF,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY BANK').get('NSE:NIFTY BANK').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100) + 100
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 100
                    else:
                        IndexEntry1 = CurrentIndexRange + 100
                    
                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                        #    IndexEntry1 = CurrentIndexRange + 200
                    #else:
                        #IndexEntry1 = IndexEntry1 + 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                         #   IndexEntry1 = CurrentIndexRange - 200

                    IndexEntryCode1 = TodayCodeBNF + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif FIN == True and False:
                    IndexEntry1 = int(StockCode.replace(TodayCodeFIN,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY FIN SERVICE').get('NSE:NIFTY FIN SERVICE').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 50
                    else:
                        IndexEntry1 = CurrentIndexRange + 50

                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 50
                    #else:
                        #IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeFIN + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif  "NIFTY" in StockCode:
                    IndexName = 'NIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeNFT,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY 50').get('NSE:NIFTY 50').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 50
                    else:
                        IndexEntry1 = CurrentIndexRange + 50
                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 50
                    #else:
                        #IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeNFT + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)

                #print(StockCode)
                #token, lot_size = instrumentLookup(fut_df,StockCode)
                token1, lot_size1 = instrumentLookup(nfo_df,IndexEntryCode1)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                price1 = round(price1,2)
                EntryPrice1 = price1
                if AwaitEntry == True:
                    EntryLevel1 = round(price1 * AwaitDiff,2)
                    if EntryLevel1 < 1:
                        EntryLevel1 = 1
                    EntryPrice1 = int(price1 + EntryLevel1)
                if price1 >= 10 or EntryPrice1 > 10:
                    if AwaitEntry == True:
                        EntryLevel1 = round(price1 * AwaitDiff,2)
                        if EntryLevel1 < 4:
                            EntryLevel1 = 4
                        EntryPrice1 = int(round(((price1 + EntryLevel1) / 5),0)* 5)
                        #EntryPrice1 = int(price1 + EntryLevel1)
                        entry_price2 = 0
                        CurTarget = round(EntryPrice1 * 0.2,0)
                        if CurTarget < 5:
                            CurTarget = 5
                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    else:
                        EntryLevel1 = round(price1 * 0.04,2)
                        EntryLevel2 = round(price1 * 0.02,2)

                        if EntryLevel1 > 10:
                            EntryLevel1 = 10
                        elif EntryLevel1 < 4:
                            EntryLevel1 = 4
                        if EntryLevel2 > 5:
                            EntryLevel2 = 5
                        elif EntryLevel2 < 2:
                            EntryLevel2 = 2
                        EntryPrice1 = int(((price1 - EntryLevel1) / 5))* 5
                        entry_price2 = int(((price1 - EntryLevel2) / 5))* 5

                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int((price1 + EntryLevel1) / 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1 - 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1)

                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        if entry_price2 < 1:
                            entry_price2 = 1
                        
                        CurTarget = round(EntryPrice1 * 0.2,0)
                        if CurTarget < 5:
                            CurTarget = 5

                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    

                    if T1 < price1:
                        T1 = int(entry_price2 + (CurTarget * 1))
                        T2 = int(entry_price2 + (CurTarget * 2))
                        T3 = int(entry_price2 + (CurTarget * 3))

                    if T1 < price1:
                        T1 = int(price1 + (CurTarget * 1))
                        T2 = int(price1 + (CurTarget * 2))
                        T3 = int(price1 + (CurTarget * 3))

                    T1 = round(T1,2)
                    T2 = round(T2,2)
                    T3 = round(T3,2)

                    if abs(price1 - T1) < 5:
                        T1 += 5
                    if abs(T1 - T2) < 5:
                        T2 = T1 + 5
                    if abs(T2 - T3) < 5:
                        T3 = T2 + 5

                    CurSL = round(EntryPrice1 * 0.1,0)
                    SL = int(EntryPrice1 - (CurSL * 1))
                    if CurSL < 10:
                        CurSL = int(EntryPrice1 + (CurTarget * 1))
                    if EntryPrice1 < 25:
                        SL = 0
                    
                    entryQty1 = lot_size1 * 2
                    inv_amount = entryQty1 * ePriceForQTY
                    #print('StockCode', IndexEntryCode1, 'price:', ePrice1,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty1)
                    

                    if True:
                        try:
                            TipBy = str(name) + '_E'
                        except:
                            TipBy = str(sender_id) + '_E'
                        #print('Profit:', eTarget, eStopLoss)
                        TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
                        TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode1,
                                                                'buy_sell': 'BUY',
                                                                'spotprice': price1,
                                                                'entry_price': EntryPrice1,
                                                                'entry_price2': 0,
                                                                'quantity': entryQty1,
                                                                'order_type': order_type,
                                                                'logtime': ltime,
                                                                'ordertime':'',
                                                                'buy_price':0,
                                                                'inv_amount':inv_amount,
                                                                'ltp':0,
                                                                'high':0,
                                                                'low':0,
                                                                'T1': T1,
                                                                'T1Msg':'No',
                                                                'T1ltp':0,
                                                                'T1high':0,
                                                                'T1low':0,
                                                                'T1P&L':0,
                                                                'T1P&LA':0,
                                                                'T1time':'',
                                                                'T1sell_price':0,
                                                                'T2': T2,
                                                                'T2Msg':'No',
                                                                'T2ltp':0,
                                                                'T2high':0,
                                                                'T2low':0,
                                                                'T2P&L':0,
                                                                'T2P&LA':0,
                                                                'T2time':'',
                                                                'T2sell_price':0,
                                                                'T3': T3,
                                                                'T3Msg':'No',
                                                                'T3ltp':0,
                                                                'T3high':0,
                                                                'T3low':0,
                                                                'T3P&L':0,
                                                                'T3P&LA':0,
                                                                'T3time':'',
                                                                'T3sell_price':0,
                                                                'SL1': SL,
                                                                'SLMsg':'No',
                                                                'SLltp':0,
                                                                'SLhigh':0,
                                                                'SLlow':0,
                                                                'SLP&L':0,
                                                                'SLP&LA':0,
                                                                'SLtime':'',
                                                                'SLsell_price':0,
                                                                'IndexName': IndexName,
                                                                'IndexEntry': str(IndexEntry1) + IndexType1,
                                                                'trailstoploss': 'No',
                                                                'ScriptRunMode': ScriptRunMode,
                                                                'ChannelChk': ChannelChk,
                                                                'tag': TipBy,
                                                                'order_number': '',
                                                                'senderid':sender_id,
                                                                'CutOffCheck1': 0,
                                                                'CutOffCheck2': 0,
                                                                'token':token1
                                                                }, ignore_index=True)

                        
                        PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
                        
                        UpdateCSV = StoreMyPrimeQueue()
                        print('StockCode', IndexEntryCode1, 'price:', price1,',EntryPrice1: ', EntryPrice1, ', entry_price2:',entry_price2, 'T1', T1, 'SL', SL)
                        
                        #print('===========      First Order  FixTarget-SingleStockSL HEDGE 1  =================')
                        
    except Exception as e:
        print('Error 2', str(e))              
    #==========================================================================================================
    #==================================EXIT_SAFE2===============================================================
    #==========================================================================================================
    #==========================================================================================================
    
    #This for Telegram
    #if len(generic_re_EntryMaster) == 1 and ThisIsNewEntryPrimary == True:
    try:
        if len(generic_re_EntryMaster) == 1 and False:
            print('try this is new EXIT_SAFE2 entry')
            Mn = datetime.datetime.now().minute
            Hr = datetime.datetime.now().hour
            Sc = datetime.datetime.now().second

            order_type = 'EXIT_SAFE2'
            ltime = datetime.datetime.now()
            for generic_re_Entry in generic_re_EntryMaster:
                #print(1)
                
                #name = str(name) + '_H' 
                EntryType = generic_re_Entry[1]
                StockCode = generic_re_Entry[2]
                ePrice = float(generic_re_Entry[3])

                #print(StockCode)
                if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                    StockCode = TodayCodeBNF + StockCode
                elif FIN == True and "FINNIFTY" not in StockCode:
                    StockCode = TodayCodeFIN + StockCode
                elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                    StockCode = TodayCodeNFT + StockCode
                
                token1, lot_size1 = instrumentLookup(nfo_df,StockCode)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                AwaitDiff = 0
                if price1 < ePrice and abs(ePrice - price1) >= 3:
                    AwaitEntry = True
                    AwaitDiff = (ePrice - price1) / price1
                    AwaitDiff = AwaitDiff * 1.1

                else:
                    AwaitEntry = False
                if StockCode.endswith("CE"):
                    IndexType1 = "CE"
                    IndexType2 = "PE"
                else:
                    IndexType1 = "PE"
                    IndexType2 = "CE"
                

                IndexEntryCode2 = ''
                if "BANKNIFTY" in StockCode:
                    IndexName = 'BANKNIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeBNF,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY BANK').get('NSE:NIFTY BANK').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100) + 100
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 100
                    else:
                        IndexEntry1 = CurrentIndexRange + 100
                    
                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                        #    IndexEntry1 = CurrentIndexRange + 200
                    #else:
                        #IndexEntry1 = IndexEntry1 + 100
                        #IndexDiff = abs(CurrentIndexRange - IndexEntry1)
                        #if IndexDiff > 400:
                         #   IndexEntry1 = CurrentIndexRange - 200

                    IndexEntryCode1 = TodayCodeBNF + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif FIN == True and False:
                    IndexEntry1 = int(StockCode.replace(TodayCodeFIN,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY FIN SERVICE').get('NSE:NIFTY FIN SERVICE').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 50
                    else:
                        IndexEntry1 = CurrentIndexRange + 50

                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 50
                    #else:
                        #IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeFIN + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif  "NIFTY" in StockCode:
                    IndexName = 'NIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeNFT,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY 50').get('NSE:NIFTY 50').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    if IndexType1 == 'CE':
                        IndexEntry1 = CurrentIndexRange - 50
                    else:
                        IndexEntry1 = CurrentIndexRange + 50
                    #if IndexEntry1 >= CurrentIndexRange:
                        #IndexEntry1 = IndexEntry1 - 50
                    #else:
                        #IndexEntry1 = IndexEntry1 + 50

                    IndexEntryCode1 = TodayCodeNFT + str(IndexEntry1) + IndexType1
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)

                #print(StockCode)
                #token, lot_size = instrumentLookup(fut_df,StockCode)
                token1, lot_size1 = instrumentLookup(nfo_df,IndexEntryCode1)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                price1 = round(price1,2)
                EntryPrice1 = price1
                if AwaitEntry == True:
                    EntryLevel1 = round(price1 * AwaitDiff,2)
                    if EntryLevel1 < 1:
                        EntryLevel1 = 1
                    EntryPrice1 = int(price1 + EntryLevel1)
                if price1 >= 10 or EntryPrice1 > 10:
                    if AwaitEntry == True:
                        EntryLevel1 = round(price1 * AwaitDiff,2)
                        if EntryLevel1 < 4:
                            EntryLevel1 = 4
                        EntryPrice1 = int(round(((price1 + EntryLevel1) / 5),0)* 5)
                        #EntryPrice1 = int(price1 + EntryLevel1)
                        entry_price2 = 0
                        CurTarget = round(EntryPrice1 * 0.05,0)
                        if CurTarget < 5:
                            CurTarget = 5
                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    else:
                        EntryLevel1 = round(price1 * 0.04,2)
                        EntryLevel2 = round(price1 * 0.02,2)

                        if EntryLevel1 > 10:
                            EntryLevel1 = 10
                        elif EntryLevel1 < 4:
                            EntryLevel1 = 4
                        if EntryLevel2 > 5:
                            EntryLevel2 = 5
                        elif EntryLevel2 < 2:
                            EntryLevel2 = 2
                        EntryPrice1 = int(((price1 - EntryLevel1) / 5))* 5
                        entry_price2 = int(((price1 - EntryLevel2) / 5))* 5

                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int((price1 + EntryLevel1) / 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1 - 2)
                        if entry_price2 <= EntryPrice1: 
                            entry_price2 = int(price1)

                        ePriceForQTY = EntryPrice1
                        if EntryPrice1 <= 1:
                            EntryPrice1 = 0
                            ePriceForQTY = price1
                        
                        if entry_price2 < 1:
                            entry_price2 = 1
                        
                        CurTarget = round(EntryPrice1 * 0.1,0)
                        if CurTarget < 5:
                            CurTarget = 5
                        if CurTarget > 30:
                            CurTarget = 30

                        T1 = int(EntryPrice1 + (CurTarget * 1))
                        T2 = int(EntryPrice1 + (CurTarget * 2))
                        T3 = int(EntryPrice1 + (CurTarget * 3))
                    

                    if T1 < price1:
                        T1 = int(entry_price2 + (CurTarget * 1))
                        T2 = int(entry_price2 + (CurTarget * 2))
                        T3 = int(entry_price2 + (CurTarget * 3))

                    if T1 < price1:
                        T1 = int(price1 + (CurTarget * 1))
                        T2 = int(price1 + (CurTarget * 2))
                        T3 = int(price1 + (CurTarget * 3))

                    T1 = round(T1,2)
                    T2 = round(T2,2)
                    T3 = round(T3,2)

                    if abs(price1 - T1) < 5:
                        T1 += 5
                    if abs(T1 - T2) < 5:
                        T2 = T1 + 5
                    if abs(T2 - T3) < 5:
                        T3 = T2 + 5

                    CurSL = round(EntryPrice1 * 0.1,0)

                    if CurSL > 15:
                        CurSL = 15
                    elif CurSL < 5:
                        CurSL = 5

                    SL = int(EntryPrice1 - (CurSL * 1))

                    if EntryPrice1 < 6:
                        SL = 1
                    elif EntryPrice1 < 15:
                        SL = 10
                    
                    entryQty1 = lot_size1 * 2
                    inv_amount = entryQty1 * ePriceForQTY
                    #print('StockCode', IndexEntryCode1, 'price:', ePrice1,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty1)
                    

                    if True:
                        try:
                            TipBy = str(name) + '_E2'
                        except:
                            TipBy = str(sender_id) + '_E2'
                        #print('Profit:', eTarget, eStopLoss)
                        TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
                        TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode1,
                                                                'buy_sell': 'BUY',
                                                                'spotprice': price1,
                                                                'entry_price': EntryPrice1,
                                                                'entry_price2': 0,
                                                                'quantity': entryQty1,
                                                                'order_type': order_type,
                                                                'logtime': ltime,
                                                                'ordertime':'',
                                                                'buy_price':0,
                                                                'inv_amount':inv_amount,
                                                                'ltp':0,
                                                                'high':0,
                                                                'low':0,
                                                                'T1': T1,
                                                                'T1Msg':'No',
                                                                'T1ltp':0,
                                                                'T1high':0,
                                                                'T1low':0,
                                                                'T1P&L':0,
                                                                'T1P&LA':0,
                                                                'T1time':'',
                                                                'T1sell_price':0,
                                                                'T2': T2,
                                                                'T2Msg':'No',
                                                                'T2ltp':0,
                                                                'T2high':0,
                                                                'T2low':0,
                                                                'T2P&L':0,
                                                                'T2P&LA':0,
                                                                'T2time':'',
                                                                'T2sell_price':0,
                                                                'T3': T3,
                                                                'T3Msg':'No',
                                                                'T3ltp':0,
                                                                'T3high':0,
                                                                'T3low':0,
                                                                'T3P&L':0,
                                                                'T3P&LA':0,
                                                                'T3time':'',
                                                                'T3sell_price':0,
                                                                'SL1': SL,
                                                                'SLMsg':'No',
                                                                'SLltp':0,
                                                                'SLhigh':0,
                                                                'SLlow':0,
                                                                'SLP&L':0,
                                                                'SLP&LA':0,
                                                                'SLtime':'',
                                                                'SLsell_price':0,
                                                                'IndexName': IndexName,
                                                                'IndexEntry': str(IndexEntry1) + IndexType1,
                                                                'trailstoploss': 'No',
                                                                'ScriptRunMode': ScriptRunMode,
                                                                'ChannelChk': ChannelChk,
                                                                'tag': TipBy,
                                                                'order_number': '',
                                                                'senderid':sender_id,
                                                                'CutOffCheck1': 0,
                                                                'CutOffCheck2': 0,
                                                                'token':token1
                                                                }, ignore_index=True)

                        
                        PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
                        
                        UpdateCSV = StoreMyPrimeQueue()
                        print('StockCode', IndexEntryCode1, 'price:', price1,',EntryPrice1: ', EntryPrice1, ', entry_price2:',entry_price2, 'T1', T1, 'SL', SL)
                        
                        #print('===========      First Order  FixTarget-SingleStockSL HEDGE 1  =================')
                        
    except Exception as e:
        print('Error 2', str(e))      
    #this if for SELL entry
    #if len(generic_re_EntryMaster) == 1 and ThisIsNewEntryPrimary == True:
    try:
        if len(generic_re_EntryMaster) == 1 and False:
            print('try this is new entry of SELL')
            Mn = datetime.datetime.now().minute
            Hr = datetime.datetime.now().hour
            Sc = datetime.datetime.now().second

            order_type = 'MKT_SELL'

            try:
                TipBy = str(name) + '_SELL'
            except:
                TipBy = str(sender_id) + '_SELL'

            ltime = datetime.datetime.now()
            for generic_re_Entry in generic_re_EntryMaster:
                #print(1)
                
                #name = str(name) + '_H' 
                EntryType = generic_re_Entry[1]
                StockCode = generic_re_Entry[2]
                ePrice = float(generic_re_Entry[3])

                #print(StockCode)
                if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                    StockCode = TodayCodeBNF + StockCode
                elif FIN == True and "FINNIFTY" not in StockCode:
                    StockCode = TodayCodeFIN + StockCode
                elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                    StockCode = TodayCodeNFT + StockCode
                
                token1, lot_size1 = instrumentLookup(nfo_df,StockCode)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']
                AwaitDiff = 0
                if price1 < ePrice and abs(ePrice - price1) >= 3:
                    AwaitEntry = True
                    AwaitDiff = (price1 - ePrice) / ePrice
                    AwaitDiff = AwaitDiff * 1.1
                else:
                    AwaitEntry = False

                if StockCode.endswith("CE"):
                    IndexType1 = "CE"
                    IndexType2 = "PE"
                else:
                    IndexType1 = "PE"
                    IndexType2 = "CE"
                

                IndexEntryCode2 = ''
                if "BANKNIFTY" in StockCode:
                    IndexName = 'BANKNIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeBNF,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY BANK').get('NSE:NIFTY BANK').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100)
                    IndexDiff = CurrentIndexRange - IndexEntry1
                    IndexDiff = IndexDiff -100 if IndexDiff > 400 else IndexDiff
                    IndexDiff = IndexDiff +100 if IndexDiff < -400 else IndexDiff
                    IndexDiff = 600 if IndexDiff > 600 else IndexDiff
                    IndexDiff = -600 if IndexDiff < -600 else IndexDiff
                    NewIndexEntry = CurrentIndexRange + IndexDiff
                    IndexEntryCode1 = TodayCodeBNF + str(NewIndexEntry) + IndexType2
                    StrikeLevels = abs(IndexDiff / 100)
                    if IndexType2 == "CE":
                        StartPcent = 15.25 / 100
                        AddPcent = (0.33 /100) * StrikeLevels
                    else:
                        StartPcent = 14.5 / 100
                        AddPcent = (0.22 /100) * StrikeLevels

                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif FIN == True and False:
                    IndexEntry1 = int(StockCode.replace(TodayCodeFIN,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY FIN SERVICE').get('NSE:NIFTY FIN SERVICE').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    IndexDiff = CurrentIndexRange - IndexEntry1
                    IndexDiff = IndexDiff -50 if IndexDiff > 200 else IndexDiff
                    IndexDiff = IndexDiff +50 if IndexDiff < -200 else IndexDiff
                    IndexDiff = 300 if IndexDiff > 300 else IndexDiff
                    IndexDiff = -300 if IndexDiff < -300 else IndexDiff
                    NewIndexEntry = CurrentIndexRange + IndexDiff
                    IndexEntryCode1 = TodayCodeFIN + str(NewIndexEntry) + IndexType2
                    StrikeLevels = abs(IndexDiff / 50)
                    if IndexType2 == "CE":
                        StartPcent = 12 / 100
                        AddPcent = (0.33 /100) * StrikeLevels
                    else:
                        StartPcent = 11.8 / 100
                        AddPcent = (0.25 /100) * StrikeLevels
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
                elif  "NIFTY" in StockCode:
                    IndexName = 'NIFTY'
                    IndexEntry1 = int(StockCode.replace(TodayCodeNFT,"").replace("CE","").replace("PE",""))
                    IndexPrice = int(kite.quote('NSE:NIFTY 50').get('NSE:NIFTY 50').get('last_price'))
                    CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                    IndexDiff = CurrentIndexRange - IndexEntry1
                    IndexDiff = IndexDiff -50 if IndexDiff > 200 else IndexDiff
                    IndexDiff = IndexDiff +50 if IndexDiff < -200 else IndexDiff
                    IndexDiff = 300 if IndexDiff > 300 else IndexDiff
                    IndexDiff = -300 if IndexDiff < -300 else IndexDiff
                    NewIndexEntry = CurrentIndexRange + IndexDiff
                    IndexEntryCode1 = TodayCodeNFT + str(NewIndexEntry) + IndexType2
                    StrikeLevels = abs(IndexDiff / 50)
                    if IndexType2 == "CE":
                        StartPcent = 12 / 100
                        AddPcent = (0.33 /100) * StrikeLevels
                    else:
                        StartPcent = 11.8 / 100
                        AddPcent = (0.25 /100) * StrikeLevels
                    #print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)

                if (IndexType2 == "CE" and IndexDiff >= 0) or \
                    (IndexType2 == "PE" and IndexDiff < 0):
                    MarginPcent = StartPcent - AddPcent
                else:
                    MarginPcent = StartPcent + AddPcent

                #print(StockCode)
                #token, lot_size = instrumentLookup(fut_df,StockCode)
                token1, lot_size1 = instrumentLookup(nfo_df,IndexEntryCode1)
                #print(token, lot_size, StockCode)
                ltp1 = kite.quote(token1)
                price1 = ltp1[str(token1)]['last_price']

                price1 = round(price1,2)
                EntryPrice1 = price1
                if AwaitEntry == True:
                    EntryLevel1 = round(price1 * AwaitDiff,2)
                    if EntryLevel1 > -3:
                        EntryLevel1 = -3
                    EntryPrice1 = int(price1 + EntryLevel1)

                
                if EntryPrice1 < 50:
                    order_type = 'MKT_SELL_SKIP'
                
                if EntryPrice1 >= 20:
                    EntryLevel1 = 0
                    if AwaitEntry == True:
                        EntryLevel1 = round(price1 * AwaitDiff,2)
                        if EntryLevel1 > -2:
                            EntryLevel1 = -2
                    else:
                        if price1 > 250:
                            EntryLevel1 = round(price1 * -0.01,2)
                            if EntryLevel1 > -3:
                                EntryLevel1 = -3
                            elif EntryLevel1 > -1:
                                EntryLevel1 = -1

                    EntryPrice1 = int(round(((price1 + EntryLevel1) / 3),0)* 3)
                    #EntryPrice1 = int(price1 + EntryLevel1)
                    entry_price2 = 0
                    CurTarget = round(EntryPrice1 * 0.1,0)
                    if CurTarget > 20:
                        CurTarget = 20
                    elif CurTarget > 15:
                        CurTarget =15
                    elif CurTarget > 10:
                        CurTarget = 10
                    else:
                        CurTarget = 10
                    
                    T1 = int(EntryPrice1 - (CurTarget * 1))
                    T2 = int(EntryPrice1 - (CurTarget * 2))
                    T3 = int(EntryPrice1 - (CurTarget * 3))
                    
                    T1 = 1 if T1 < 1 else T1
                    T2 = 1 if T2 < 1 else T2
                    T3 = 1 if T3 < 1 else T3

                    CurSL = round(EntryPrice1 * 0.15,0)

                    if CurSL < 15:
                        CurSL = 15

                    SL = int(EntryPrice1 + (CurSL * 1))
                    if SL < 5:
                        SL = 5
                    entryQty1 = lot_size1 * 1
                    inv_amount = ((NewIndexEntry + EntryPrice1) * entryQty1) * MarginPcent
                    #print('StockCode', IndexEntryCode1, 'price:', EntryPrice1,',eTarget: ', T1, ', eStopLoss:',SL, 'Qty', entryQty1)
                    

                    if True:
                        #print('Profit:', eTarget, eStopLoss)
                        TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
                        TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode1,
                                                                'buy_sell': 'SELL',
                                                                'spotprice': price1,
                                                                'entry_price': EntryPrice1,
                                                                'entry_price2': entry_price2,
                                                                'quantity': entryQty1,
                                                                'order_type': order_type,
                                                                'logtime': ltime,
                                                                'ordertime':'',
                                                                'buy_price':0,
                                                                'inv_amount':inv_amount,
                                                                'ltp':0,
                                                                'high':0,
                                                                'low':0,
                                                                'T1': T1,
                                                                'T1Msg':'No',
                                                                'T1ltp':0,
                                                                'T1high':0,
                                                                'T1low':0,
                                                                'T1P&L':0,
                                                                'T1P&LA':0,
                                                                'T1time':'',
                                                                'T1sell_price':0,
                                                                'T2': T2,
                                                                'T2Msg':'No',
                                                                'T2ltp':0,
                                                                'T2high':0,
                                                                'T2low':0,
                                                                'T2P&L':0,
                                                                'T2P&LA':0,
                                                                'T2time':'',
                                                                'T2sell_price':0,
                                                                'T3': T3,
                                                                'T3Msg':'No',
                                                                'T3ltp':0,
                                                                'T3high':0,
                                                                'T3low':0,
                                                                'T3P&L':0,
                                                                'T3P&LA':0,
                                                                'T3time':'',
                                                                'T3sell_price':0,
                                                                'SL1': SL,
                                                                'SLMsg':'No',
                                                                'SLltp':0,
                                                                'SLhigh':0,
                                                                'SLlow':0,
                                                                'SLP&L':0,
                                                                'SLP&LA':0,
                                                                'SLtime':'',
                                                                'SLsell_price':0,
                                                                'IndexName': IndexName,
                                                                'IndexEntry': str(NewIndexEntry) + IndexType2,
                                                                'trailstoploss': 'No',
                                                                'ScriptRunMode': ScriptRunMode,
                                                                'ChannelChk': ChannelChk,
                                                                'tag': TipBy,
                                                                'order_number': '',
                                                                'senderid':sender_id,
                                                                'CutOffCheck1': 0,
                                                                'CutOffCheck2': 0,
                                                                'token':token1
                                                                }, ignore_index=True)

                        if price1 <= EntryPrice1:
                            #inv_amount = entryQty1 * price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'buy_price'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'low'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'high'] = price1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ltp'] = price1
                            #TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'inv_amount'] = inv_amount
                        
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 1
                            TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
                        #elif CurrentOrderStatus == 'NoSkipEntry':
                        #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 11
                        #    TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = 'Skipped'

                        
                        PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
                        
                        UpdateCSV = StoreMyPrimeQueue()
                        CurrentOrderStatus = ''
                        print('StockCode', IndexEntryCode1, 'price:', price1,',EntryPrice1: ', EntryPrice1, ', entry_price2:',entry_price2, 'T1', T1, 'SL', SL)
                        
                        #print('===========      First Order  FixTarget-SingleStockSL HEDGE 1  =================')
                        
        
    except Exception as e:
        print('Error 3', str(e)) 


    if len(generic_re_EntryMaster) == 1 and DoHedgeTrade == True and False:
        for generic_re_Entry in generic_re_EntryMaster:
            #print(1)
            
            tag= sender_id_Lookup(sender_id)

            if tag == sender_id:
                if name == '':
                    name = sender_id 
            else:
                name = tag

            if name == '':
                name = sender_id 
            
            name = str(name) + '_H' 
            EntryType = generic_re_Entry[1]
            StockCode = generic_re_Entry[2]
            ePrice = float(generic_re_Entry[3])
            
            #print(StockCode)
            if (BNF == True and "BANKNIFTY" not in StockCode) or StockCode.startswith("3") or StockCode.startswith("4"):
                StockCode = TodayCodeBNF + StockCode
            elif FIN == True and "FINNIFTY" not in StockCode:
                StockCode = TodayCodeFIN + StockCode
            elif (NFT == True and "NIFTY" not in StockCode) or StockCode.startswith("1"):
                StockCode = TodayCodeNFT + StockCode
            
            if StockCode.endswith("CE"):
                IndexType1 = "CE"
                IndexType2 = "PE"
            else:
                IndexType1 = "PE"
                IndexType2 = "CE"
                
            if BNF == True:
                IndexEntry1 = int(StockCode.replace(TodayCodeBNF,"").replace("CE","").replace("PE",""))
                IndexPrice = int(kite.quote('NSE:NIFTY BANK').get('NSE:NIFTY BANK').get('last_price'))
                CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100) + 100
                if IndexEntry1 > CurrentIndexRange:
                    IndexDiff = IndexEntry1 - CurrentIndexRange
                    IndexEntry2 = CurrentIndexRange - IndexDiff
                else:
                    IndexDiff =  CurrentIndexRange - IndexEntry1
                    IndexEntry2 = CurrentIndexRange + IndexDiff

                IndexEntryCode1 = TodayCodeBNF + str(IndexEntry1) + IndexType1
                IndexEntryCode2 = TodayCodeBNF + str(IndexEntry2) + IndexType2
                print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
            if FIN == True:
                IndexEntry1 = int(StockCode.replace(TodayCodeFIN,"").replace("CE","").replace("PE",""))
                IndexPrice = int(kite.quote('NSE:NIFTY FIN SERVICE').get('NSE:NIFTY BANK').get('last_price'))
                CurrentIndexRange = (IndexPrice + (100 - 1)) - ((IndexPrice + (100 - 1)) % 100)
                print(CurrentIndexRange)

                if IndexEntry1 > CurrentIndexRange:
                    IndexDiff = IndexEntry1 - CurrentIndexRange
                    IndexEntry2 = CurrentIndexRange - IndexDiff
                else:
                    IndexDiff =  CurrentIndexRange - IndexEntry1
                    IndexEntry2 = CurrentIndexRange + IndexDiff

                IndexEntryCode1 = TodayCodeFIN + str(IndexEntry1) + IndexType1
                IndexEntryCode2 = TodayCodeFIN + str(IndexEntry2) + IndexType2
                print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)
            if NFT == True:
                IndexEntry1 = int(StockCode.replace(TodayCodeNFT,"").replace("CE","").replace("PE",""))
                IndexPrice = int(kite.quote('NSE:NIFTY 50').get('NSE:NIFTY 50').get('last_price'))
                CurrentIndexRange = (IndexPrice + (50 - 1)) - ((IndexPrice + (50 - 1)) % 50)
                print(CurrentIndexRange)

                if IndexEntry1 > CurrentIndexRange:
                    IndexDiff = IndexEntry1 - CurrentIndexRange
                    IndexEntry2 = CurrentIndexRange - IndexDiff
                else:
                    IndexDiff =  CurrentIndexRange - IndexEntry1
                    IndexEntry2 = CurrentIndexRange + IndexDiff

                IndexEntryCode1 = TodayCodeNFT + str(IndexEntry1) + IndexType1
                IndexEntryCode2 = TodayCodeNFT + str(IndexEntry2) + IndexType2
                print(IndexEntryCode1, CurrentIndexRange, IndexEntryCode2)

            #print(StockCode)
            #token, lot_size = instrumentLookup(fut_df,StockCode)
            token1, lot_size1 = instrumentLookup(nfo_df,IndexEntryCode1)
            token2, lot_size2 = instrumentLookup(nfo_df,IndexEntryCode2)
            #print(token, lot_size, StockCode)
            ltp1 = kite.quote(token1)
            price1 = ltp1[str(token1)]['last_price']
            price1 = price1
            ltp2 = kite.quote(token2)
            price2 = ltp2[str(token2)]['last_price']
            price2 = price2
            if price1 > price2:
                ePriceForQTY = price1
            else:
                ePriceForQTY = price2

            tag, minentryprice, maxentryprice, stoploss, takeprofit, minentryprice1, maxentryprice1, stoploss1, takeprofit1, maxcutoff, maxquantity, trailstoploss, minentrytime, maxentrytime, maxtimedif, maxbuypriceDiff = settingsLookup(sender_id)

            ScriptRunMode = 'SingleStockSL'
            ChannelChk = 'Shortlisted'
            order_type = 'HEDGE'
            eStopLoss = 12
            eTarget = 200
            
            ePrice1 = price1
            entryQty1 = math.floor(5000 / ePriceForQTY / lot_size1) * lot_size1
            if entryQty1 == 0:
                entryQty1 = lot_size1
            elif entryQty1 > 10000:
                entryQty1 = math.floor(10000 / lot_size1) * lot_size1
        

            print('StockCode', IndexEntryCode1, 'price:', ePrice1,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty1)
            
            print('===========      First Order  FixTarget-SingleStockSL HEDGE 1  =================')
            ltime = datetime.datetime.now()
            
            #print('Profit:', eTarget, eStopLoss)
            TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
            TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode1,
                                                    'buy_sell': 'BUY',
                                                    'spotprice': ePrice1,
                                                    'order_type': order_type,
                                                    'quantity': entryQty1,
                                                    'entry_price': ePrice1 + 2,
                                                    'stoploss1': eStopLoss,
                                                    'takeprofit1': eTarget,
                                                    'trailstoploss': 'Yes',
                                                    'ScriptRunMode': ScriptRunMode,
                                                    'ChannelChk': ChannelChk,
                                                    'ltp':0,
                                                    'high':0,
                                                    'low':0,
                                                    'inv_amount':0,
                                                    'buy_price':0,
                                                    'sell_price1':0,
                                                    'tag': name,
                                                    'order_number': '',
                                                    'logtime': ltime,
                                                    'ordertime':'',
                                                    'exitorder1':'',
                                                    'senderid':sender_id,
                                                    'CutOffCheck1': 0,
                                                    'CutOffCheck2': 0,
                                                    'token':token1
                                                    }, ignore_index=True)

            
            CurrentOrderStatus = CheckLTPandPlaceOrder(TempEntryQueue.iloc[0], ltp1)
            print('thats here 5', CurrentOrderStatus)
            if CurrentOrderStatus == 'YesOrderIsPlaced':
                inv_amount = entryQty1 * ePrice1
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'buy_price'] = ePrice1
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'inv_amount'] = inv_amount
            
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 1
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
            elif CurrentOrderStatus == 'NoSkipEntry':
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 11
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = 'Skipped'

            PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
            
            UpdateCSV = StoreMyPrimeQueue()
            CurrentOrderStatus = ''


            ePrice2 = price2
            entryQty2 = math.floor(5000 / ePriceForQTY / lot_size2) * lot_size2
            if entryQty2 == 0:
                entryQty2 = lot_size2
            elif entryQty2 > 10000:
                entryQty2 = math.floor(10000 / lot_size2) * lot_size2
        

            print('StockCode', IndexEntryCode2, 'price:', ePrice2,',eTarget: ', eTarget, ', eStopLoss:',eStopLoss, 'Qty', entryQty2)
            
            print('===========      First Order  FixTarget-SingleStockSL HEDGE 2  =================')
            ltime2 = datetime.datetime.now()
            
            #print('Profit:', eTarget, eStopLoss)
            TempEntryQueue = pd.DataFrame(columns=PrimeQueue.columns)
            TempEntryQueue = TempEntryQueue.append({'symbol': IndexEntryCode2,
                                                    'buy_sell': 'BUY',
                                                    'spotprice': ePrice2,
                                                    'order_type': order_type,
                                                    'quantity': entryQty2,
                                                    'entry_price': ePrice2 + 3,
                                                    'stoploss1': eStopLoss,
                                                    'takeprofit1': eTarget,
                                                    'trailstoploss': 'Yes',
                                                    'ScriptRunMode': ScriptRunMode,
                                                    'ChannelChk': ChannelChk,
                                                    'ltp':0,
                                                    'high':0,
                                                    'low':0,
                                                    'inv_amount':0,
                                                    'buy_price':0,
                                                    'sell_price1':0,
                                                    'tag': name,
                                                    'order_number': '',
                                                    'logtime': ltime2,
                                                    'ordertime':'',
                                                    'exitorder1':'',
                                                    'senderid':sender_id,
                                                    'CutOffCheck1': 0,
                                                    'CutOffCheck2': 0,
                                                    'token':token2
                                                    }, ignore_index=True)

            
            CurrentOrderStatus = CheckLTPandPlaceOrder(TempEntryQueue.iloc[0], ltp2)
            print('thats here 5', CurrentOrderStatus)
            if CurrentOrderStatus == 'YesOrderIsPlaced':
                inv_amount = entryQty2 * ePrice2
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'buy_price'] = ePrice2
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'inv_amount'] = inv_amount
            
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 1
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = datetime.datetime.now()
            elif CurrentOrderStatus == 'NoSkipEntry':
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'order_number'] = 11
                TempEntryQueue.loc[TempEntryQueue.logtime==ltime, 'ordertime'] = 'Skipped'

            PrimeQueue = PrimeQueue.append(TempEntryQueue.iloc[0])
            
            UpdateCSV = StoreMyPrimeQueue()
            CurrentOrderStatus = ''

    return raw_OrderMsgPrint

def FetchPrintMsg():
    print(12345)
    PrimeQueueTmpA = pd.read_csv(MyPrimeQueueLoadBackCsv)
    PrimeQueueTmp = PrimeQueueTmpA[(PrimeQueueTmpA['order_type'] =='MKT')]

    MyPrimeQueuePL = pd.read_csv(MyPrimeQueuePLCsv)
    PrimeQueueTmp2 = MyPrimeQueuePL[(MyPrimeQueuePL['7ScriptMode'] == "ToChannel")]

    TotalNFTPoints = 0
    TotalBNFPoints = 0
    EntryCounter = 0
    ProftCounter = 0
    LossCounter = 0
    InvestmentLocked = 0
    ConsvVal = 0
    if len(PrimeQueueTmp2) > 0:
        InvestmentLocked = int(PrimeQueueTmp2['5MaxInv'].max())

    print(7890,len(PrimeQueueTmp))
    PrintTxt = 'TODAY PERFORMANCE\n\n'
    for i in range(0, len(PrimeQueueTmp)):
        
        lot_size = int(PrimeQueueTmp.iloc[i]['quantity'])
        entry_price1 = float(PrimeQueueTmp.iloc[i]['entry_price'])
        entry_price2 = float(PrimeQueueTmp.iloc[i]['entry_price2'])
        cHigh = float(PrimeQueueTmp.iloc[i]['high'])
        cLow = float(PrimeQueueTmp.iloc[i]['low'])
        ltp = float(PrimeQueueTmp.iloc[i]['ltp'])
        IndexEntry = PrimeQueueTmp.iloc[i]['IndexEntry']
        IndexName = PrimeQueueTmp.iloc[i]['IndexName']
        buy_price = float(PrimeQueueTmp.iloc[i]['buy_price'])
        
        if entry_price2 > entry_price1:
            entry_price = entry_price2
        else:
            entry_price = entry_price1

        T1 = float(PrimeQueueTmp.iloc[i]['T1'])
        T2 = float(PrimeQueueTmp.iloc[i]['T2'])
        T3 = float(PrimeQueueTmp.iloc[i]['T3'])
        SL = float(PrimeQueueTmp.iloc[i]['SL1'])
        SLMsg = PrimeQueueTmp.iloc[i]['SLMsg']
        
        TargetHit = False
        SlHit = False
        if buy_price > 0:
            EntryCounter += 1
            ConsvExitAt = ltp
            if cHigh >= T1:
                TargetHit = True
                TG = "T1"
                ConsvExitAt = T1
                if cHigh >= T2:
                    TG = "T2"
                if cHigh >= T3:
                    TG = "T3"
            if SLMsg != 'No':
                SlHit = True
                ConsvExitAt = SL
                
            #print(TG, TargetHit, SlHit)
            ProfitPoints = round(cHigh - entry_price,0)
            CurConsvVal = round(ConsvExitAt - entry_price,0) * lot_size
            ConsvVal += CurConsvVal
            #print('ProfitPoints',ProfitPoints,'ConsvVal',ConsvVal,'CurConsvVal',CurConsvVal,'entry_price',entry_price,'ConsvExitAt',ConsvExitAt,'lot_size',lot_size)
            if ProfitPoints > 10:
                ProfitPoints = round(ProfitPoints/5,0) * 5
            else:
                ProfitPoints = 10
            LossPoints  = round(SL - entry_price,0)
            NutralPoints = round(round(ltp - entry_price,0)/5,0) * 5
            if SlHit == True:
                PrintTxt += IndexEntry + ' : ' + str(int(LossPoints)) + ' POINTS (SL HIT)\n'
                if IndexName == 'NIFTY':
                    TotalNFTPoints += LossPoints
                else:
                    TotalBNFPoints += LossPoints
                LossCounter += 1
            if TargetHit == True:
                PrintTxt += IndexEntry + ' : ' + str(int(ProfitPoints)) + ' POINTS (' + TG + ' HIT)\n'
                if IndexName == 'NIFTY':
                    TotalNFTPoints += ProfitPoints
                else:
                    TotalBNFPoints += ProfitPoints
                ProftCounter += 1
            if TargetHit == False and SlHit == False :
                
                NProfitPoints = round(round(cHigh - entry_price,0)/5,0) * 5
                if NProfitPoints >= 5:
                    PrintTxt += IndexEntry + ' : ' + str(int(NProfitPoints)) +' POINTS (T1 NOT HIT)\n'
                    if IndexName == 'NIFTY':
                        TotalNFTPoints += NProfitPoints
                    else:
                        TotalBNFPoints += NProfitPoints
                    ProftCounter += 1
                elif NutralPoints > -5:
                    PrintTxt += IndexEntry + ' : 0 POINTS (AT CTC)\n'
                else:
                    PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) +' POINTS (LOSS)\n'
                    if IndexName == 'NIFTY':
                        TotalNFTPoints += NutralPoints
                    else:
                        TotalBNFPoints += NutralPoints
                    LossCounter += 1
            #print(TotalBNFPoints,TotalNFTPoints)

    NFTValue = 0 
    BNFValue = 0
    print('ConsvVal',ConsvVal)
    if EntryCounter > 0:
        NetConsvVal = ConsvVal - (EntryCounter * 75)
    if TotalNFTPoints != 0:
        NFTValue = TotalNFTPoints * 100
    print(NFTValue)
    if TotalBNFPoints != 0:
        BNFValue = TotalBNFPoints * 50
    print(BNFValue)
    TotalVal = NFTValue + BNFValue
    if NFTValue != 0 or  BNFValue != 0 or  EntryCounter != 0:
        #PrintTxt += '\nSuccess Ratio: ' + str(int(round(int((ProftCounter/(ProftCounter+LossCounter)) * 100)/5,0)*5)) + '%\n\n'
        PrintTxt += '\nNet Result @ Max Points: ' + str(int(TotalVal)) + '/- (@ 2LOTS) \n'
        if BNFValue != 0:
            PrintTxt += 'BANKNIFTY 50 * ' + str(int(TotalBNFPoints)) +' = ' + str(int(BNFValue)) + '\n'
        if NFTValue != 0:
            PrintTxt += 'NIFTY 100 * ' + str(int(TotalNFTPoints)) +' = ' + str(int(NFTValue)) + ')\n\n'

        PrintTxt += 'Net Result @ Safe: ' + str(int(NetConsvVal)) + ' [After Brokerage]\n'
        PrintTxt += 'MaxInvestmentLocked @ Safe: ' + str(InvestmentLocked) + '\n'
        PrintTxt += 'Profitability @ Safe: '+ str(round((NetConsvVal / InvestmentLocked) *100,2)) + ' %\n\n'
        PrintTxt += '@Safe ==> EXIT on T1 and NO second entry after SL is hit'
        return PrintTxt
    else:
        return ''
    

def FetchPrintMsgSELL():
    print(12345)
    PrimeQueueTmpA = pd.read_csv(MyPrimeQueueLoadBackCsv)
    PrimeQueueTmp = PrimeQueueTmpA[(PrimeQueueTmpA['order_type'].str.contains("SELL"))]
    MyPrimeQueuePL = pd.read_csv(MyPrimeQueuePLCsv)
    PrimeQueueTmp2 = MyPrimeQueuePL[(MyPrimeQueuePL['7ScriptMode'].str.contains("SELL"))]

    TotalNFTPoints = 0
    TotalBNFPoints = 0
    EntryCounter = 0
    ProftCounter = 0
    LossCounter = 0
    InvestmentLocked = 0
    NFTCounter = 0
    BNFCounter=0
    NFTConsvPoints = 0
    BNFConsvPoints = 0

    if len(PrimeQueueTmp2) > 0:
        InvestmentLocked = int(PrimeQueueTmp2['5MaxInv'].max())


    print(7890,len(PrimeQueueTmp))
    PrintTxt = 'RESULT OF NEW OPTION SELLING STRATEGY [UNDER TEST]\n\n'
    for i in range(0, len(PrimeQueueTmp)):
        lot_size = int(PrimeQueueTmp.iloc[i]['quantity'])
        entry_price1 = float(PrimeQueueTmp.iloc[i]['entry_price'])
        entry_price2 = float(PrimeQueueTmp.iloc[i]['entry_price2'])
        cHigh = float(PrimeQueueTmp.iloc[i]['high'])
        cLow = float(PrimeQueueTmp.iloc[i]['low'])
        ltp = float(PrimeQueueTmp.iloc[i]['ltp'])
        IndexEntry = PrimeQueueTmp.iloc[i]['IndexEntry']
        IndexName = PrimeQueueTmp.iloc[i]['IndexName']
        buy_price = float(PrimeQueueTmp.iloc[i]['buy_price'])
        
        if entry_price2 > entry_price1:
            entry_price = entry_price2
        else:
            entry_price = entry_price1

        T1 = float(PrimeQueueTmp.iloc[i]['T1'])
        T2 = float(PrimeQueueTmp.iloc[i]['T2'])
        T3 = float(PrimeQueueTmp.iloc[i]['T3'])
        SL = float(PrimeQueueTmp.iloc[i]['SL1'])
        SLMsg = PrimeQueueTmp.iloc[i]['SLMsg']
        T1sell_price = float(PrimeQueueTmp.iloc[i]['T1sell_price'])
        T2sell_price = float(PrimeQueueTmp.iloc[i]['T2sell_price'])
        T3sell_price = float(PrimeQueueTmp.iloc[i]['T3sell_price'])
        SLsell_price = float(PrimeQueueTmp.iloc[i]['SLsell_price'])
        #print(buy_price,T1sell_price, T2sell_price,T2sell_price,SLsell_price)
        TargetHit = False
        SlHit = False
        Tsell_price = 0
        ProfitPoints = 0
        LossPoints = 0
        PP = 0
        if buy_price > 0:
            EntryCounter += 1
            #if T1sell_price > 0:
            #    EP = T1sell_price
            #if SLsell_price > 0:
            #    EP = SLsell_price

            if cLow <= T1:
                ConsvPoints = round(buy_price - T1sell_price,0)
                TargetHit = True
                TG = "T1"
                Tsell_price = T1sell_price
                if cLow <= T2:
                    TG = "T2"
                    Tsell_price = T2sell_price
                if cLow <= T3:
                    TG = "T3"
                    Tsell_price = T3sell_price
                ProfitPoints = round(buy_price - Tsell_price,0)
                PP = (ProfitPoints * lot_size) - 75
            if cHigh >=  SL and SLsell_price > 0:
                SlHit = True
                ConsvPoints = round(buy_price - SLsell_price,0)
                LossPoints  = round(buy_price - SLsell_price,0)
            #print(TG, TargetHit, SlHit)
            
            

            #print('ProfitPoints',ProfitPoints,'ConsvVal',ConsvVal,'CurConsvVal',CurConsvVal,'buy_price',buy_price,'ConsvExitAt',ConsvExitAt,'lot_size',lot_size)
            NutralPoints = round(buy_price - ltp,0)
            PMS = ''
            if SlHit == True:
                PrintTxt += IndexEntry + ' : ' + str(int(LossPoints)) + ' (SL HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = LossPoints
                PMS = '   (SL HIT)'
            if TargetHit == True and Tsell_price > 0:
                PrintTxt += IndexEntry + ' : ' + str(int(ProfitPoints)) + ' POINTS (' + TG + ' HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = ProfitPoints
                if PMS == '':
                    PMS = '   (' + TG + ' HIT)'
            elif NutralPoints > 0 and Tsell_price == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (T1 NOT HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (T1 NOT HIT)'
            elif NutralPoints < 0 and SlHit == False:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (LOSS - SL NOT HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (LOSS - SL NOT HIT)'
            elif NutralPoints == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (NO MOVEMENT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (NO MOVEMENT)'
            
            
            '''print('IndexEntry'.ljust(10)+ IndexEntry.ljust(10) + 'BP:'.ljust(6) + str(int(buy_price)).ljust(6) + \
                    'EP'.ljust(6) + str(int(EP)).ljust(6) + \
                    'Lo'.ljust(6) + str(int(cLow)).ljust(6) + \
                    'Hi'.ljust(6) + str(int(cHigh)).ljust(6) + \
                    'LT'.ljust(6) + str(int(ltp)).ljust(6) + \
                    'PP'.ljust(6) + str(int(ConsvPoints)).ljust(6) + \
                    'PFT'.ljust(6) + str(int((ConsvPoints * lot_size)-75)).ljust(6) + \
                    'MP'.ljust(6) + str(int((PP))).ljust(6) + PMS)'''

            if IndexName == 'NIFTY':
                TotalNFTPoints += CurrentEntryPoints
                NFTCounter += 1
                if SlHit == True:
                    NFTConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    NFTConsvPoints += ConsvPoints
                else:
                    NFTConsvPoints += NutralPoints
                nft_lot_size = lot_size
            else:
                TotalBNFPoints += CurrentEntryPoints
                BNFCounter += 1
                if SlHit == True:
                    BNFConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    BNFConsvPoints += ConsvPoints
                else:
                    BNFConsvPoints += NutralPoints
                bnf_lot_size = lot_size
            #print(TotalBNFPoints,TotalNFTPoints)

    NFTValue = 0 
    BNFValue = 0
    NFTConsvValue = 0
    BNNFConsvValue = 0
    if NFTCounter > 0:
        NFTValue = (TotalNFTPoints * nft_lot_size) - (NFTCounter * 75)
        NFTConsvValue = (NFTConsvPoints * nft_lot_size) - (NFTCounter * 75)
    print(NFTValue)
    if BNFCounter > 0:
        BNFValue = (TotalBNFPoints * bnf_lot_size) - (BNFCounter * 75)
        BNNFConsvValue = (BNFConsvPoints * bnf_lot_size) - (BNFCounter * 75)
    print(BNFValue)
    TotalVal = NFTValue + BNFValue
    TotalConsvVal = NFTConsvValue + BNNFConsvValue
    if NFTValue != 0 or  BNFValue != 0:
        #PrintTxt += '\nSuccess Ratio: ' + str(int(round(int((ProftCounter/(ProftCounter+LossCounter)) * 100)/5,0)*5)) + '%\n\n'
        PrintTxt += '\nNet Result: @ Max Points # ' + str(int(TotalVal)) + ', @ Safe '+ ' # ' + str(int(TotalConsvVal))  + ' [After Brokerage]\n'
        if BNFValue != 0:
            PrintTxt += ('BANKNIFTY ' + str(bnf_lot_size))+ ' @ Max Points '      + str(int(TotalBNFPoints)) + ' # ' + str(int(BNFValue)) + ', @ Safe # ' + str(int(BNNFConsvValue)) + '\n'
        if NFTValue != 0:
            PrintTxt += ('NIFTY ' + str(nft_lot_size)) + ' @ Max Points '      + str(int(TotalNFTPoints))+ ' # ' + str(int(NFTValue))+ ', @ Safe # ' + str(int(NFTConsvValue)) + '\n\n'
        
        
        PrintTxt += 'MaxInvestmentLocked @ Safe: ' + str(InvestmentLocked)+ '\n'
        PrintTxt += 'Profitability @ Safe: ' + str(round((TotalConsvVal / InvestmentLocked) *100,2)) + ' %\n\n'
        PrintTxt += '@Safe ==> EXIT on T1 and NO second entry after SL is hit'
        return PrintTxt
    else:
        return ''
    

def FetchPrintMsgSafe():
    print(12345)
    PrimeQueueTmpA = pd.read_csv(MyPrimeQueueLoadBackCsv)
    PrimeQueueTmp = PrimeQueueTmpA[(PrimeQueueTmpA['order_type'] =='EXIT_SAFE')]
    MyPrimeQueuePL = pd.read_csv(MyPrimeQueuePLCsv)
    PrimeQueueTmp2 = MyPrimeQueuePL[(MyPrimeQueuePL['7ScriptMode'] == "ToChannelSafe")]

    TotalNFTPoints = 0
    TotalBNFPoints = 0
    EntryCounter = 0
    ProftCounter = 0
    LossCounter = 0
    InvestmentLocked = 0
    NFTCounter = 0
    BNFCounter=0
    NFTConsvPoints = 0
    BNFConsvPoints = 0

    if len(PrimeQueueTmp2) > 0:
        InvestmentLocked = int(PrimeQueueTmp2['5MaxInv'].max())


    print(7890,len(PrimeQueueTmp))
    PrintTxt = 'RESULT OF NEW SAFE EXIT [UNDER TEST]\n\n'
    for i in range(0, len(PrimeQueueTmp)):
        lot_size = int(PrimeQueueTmp.iloc[i]['quantity'])
        entry_price1 = float(PrimeQueueTmp.iloc[i]['entry_price'])
        cHigh = float(PrimeQueueTmp.iloc[i]['high'])
        cLow = float(PrimeQueueTmp.iloc[i]['low'])
        ltp = float(PrimeQueueTmp.iloc[i]['ltp'])
        IndexEntry = PrimeQueueTmp.iloc[i]['IndexEntry']
        IndexName = PrimeQueueTmp.iloc[i]['IndexName']
        buy_price = float(PrimeQueueTmp.iloc[i]['buy_price'])
        
        entry_price = entry_price1

        T1 = float(PrimeQueueTmp.iloc[i]['T1'])
        T2 = float(PrimeQueueTmp.iloc[i]['T2'])
        T3 = float(PrimeQueueTmp.iloc[i]['T3'])
        SL = float(PrimeQueueTmp.iloc[i]['SL1'])
        SLMsg = PrimeQueueTmp.iloc[i]['SLMsg']
        T1sell_price = float(PrimeQueueTmp.iloc[i]['T1sell_price'])
        T2sell_price = float(PrimeQueueTmp.iloc[i]['T2sell_price'])
        T3sell_price = float(PrimeQueueTmp.iloc[i]['T3sell_price'])
        SLsell_price = float(PrimeQueueTmp.iloc[i]['SLsell_price'])
        #print(buy_price,T1sell_price, T2sell_price,T2sell_price,SLsell_price)
        TargetHit = False
        SlHit = False
        Tsell_price = 0
        ProfitPoints = 0
        LossPoints = 0
        PP = 0
        if buy_price > 0:
            EntryCounter += 1
            #if T1sell_price > 0:
            #    EP = T1sell_price
            #if SLsell_price > 0:
            #    EP = SLsell_price

            if T1sell_price > 0:
                ConsvPoints = round(T1sell_price - buy_price,0)
                TargetHit = True
                TG = "T1"
                Tsell_price = T1sell_price
                if T2sell_price > 0:
                    TG = "T2"
                    Tsell_price = T2sell_price
                if T3sell_price > 0:
                    TG = "T3"
                    Tsell_price = T3sell_price
                ProfitPoints = round(Tsell_price - buy_price,0)
                PP = (ProfitPoints * lot_size) - 75
            if SLsell_price > 0:
                SlHit = True
                ConsvPoints = round(SLsell_price - buy_price,0)
                LossPoints  = round(SLsell_price - buy_price,0)
            #print(TG, TargetHit, SlHit)
            
            

            #print('ProfitPoints',ProfitPoints,'ConsvVal',ConsvVal,'CurConsvVal',CurConsvVal,'buy_price',buy_price,'ConsvExitAt',ConsvExitAt,'lot_size',lot_size)
            NutralPoints = round(buy_price - ltp,0)
            PMS = ''
            if SlHit == True:
                PrintTxt += IndexEntry + ' : ' + str(int(LossPoints)) + ' (SL HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = LossPoints
                PMS = '   (SL HIT)'
            if TargetHit == True and Tsell_price > 0:
                PrintTxt += IndexEntry + ' : ' + str(int(ProfitPoints)) + ' POINTS (' + TG + ' HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = ProfitPoints
                if PMS == '':
                    PMS = '   (' + TG + ' HIT)'
            elif NutralPoints > 0 and Tsell_price == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (T1 NOT HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (T1 NOT HIT)'
            elif NutralPoints < 0 and SlHit == False:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (LOSS - SL NOT HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (LOSS - SL NOT HIT)'
            elif NutralPoints == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (NO MOVEMENT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (NO MOVEMENT)'
            
            
            '''print('IndexEntry'.ljust(10)+ IndexEntry.ljust(10) + 'BP:'.ljust(6) + str(int(buy_price)).ljust(6) + \
                    'EP'.ljust(6) + str(int(EP)).ljust(6) + \
                    'Lo'.ljust(6) + str(int(cLow)).ljust(6) + \
                    'Hi'.ljust(6) + str(int(cHigh)).ljust(6) + \
                    'LT'.ljust(6) + str(int(ltp)).ljust(6) + \
                    'PP'.ljust(6) + str(int(ConsvPoints)).ljust(6) + \
                    'PFT'.ljust(6) + str(int((ConsvPoints * lot_size)-75)).ljust(6) + \
                    'MP'.ljust(6) + str(int((PP))).ljust(6) + PMS)'''

            if IndexName == 'NIFTY':
                TotalNFTPoints += CurrentEntryPoints
                NFTCounter += 1
                if SlHit == True:
                    NFTConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    NFTConsvPoints += ConsvPoints
                else:
                    NFTConsvPoints += NutralPoints
                nft_lot_size = lot_size
            else:
                TotalBNFPoints += CurrentEntryPoints
                BNFCounter += 1
                if SlHit == True:
                    BNFConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    BNFConsvPoints += ConsvPoints
                else:
                    BNFConsvPoints += NutralPoints
                bnf_lot_size = lot_size
            #print(TotalBNFPoints,TotalNFTPoints)

    NFTValue = 0 
    BNFValue = 0
    NFTConsvValue = 0
    BNNFConsvValue = 0
    if NFTCounter > 0:
        NFTValue = (TotalNFTPoints * nft_lot_size) - (NFTCounter * 75)
        NFTConsvValue = (NFTConsvPoints * nft_lot_size) - (NFTCounter * 75)
    print(NFTValue)
    if BNFCounter > 0:
        BNFValue = (TotalBNFPoints * bnf_lot_size) - (BNFCounter * 75)
        BNNFConsvValue = (BNFConsvPoints * bnf_lot_size) - (BNFCounter * 75)
    print(BNFValue)
    TotalVal = NFTValue + BNFValue
    TotalConsvVal = NFTConsvValue + BNNFConsvValue
    if NFTValue != 0 or  BNFValue != 0:
        #PrintTxt += '\nSuccess Ratio: ' + str(int(round(int((ProftCounter/(ProftCounter+LossCounter)) * 100)/5,0)*5)) + '%\n\n'
        PrintTxt += '\nNet Result: @ Max Points # ' + str(int(TotalVal)) + ', @ Safe '+ ' # ' + str(int(TotalConsvVal))  + ' [After Brokerage]\n'
        if BNFValue != 0:
            PrintTxt += ('BANKNIFTY ' + str(bnf_lot_size))+ ' @ Max Points '      + str(int(TotalBNFPoints)) + ' # ' + str(int(BNFValue)) + ', @ Safe # ' + str(int(BNNFConsvValue)) + '\n'
        if NFTValue != 0:
            PrintTxt += ('NIFTY ' + str(nft_lot_size)) + ' @ Max Points '      + str(int(TotalNFTPoints))+ ' # ' + str(int(NFTValue))+ ', @ Safe # ' + str(int(NFTConsvValue)) + '\n\n'
        
        
        PrintTxt += 'MaxInvestmentLocked @ Safe: ' + str(InvestmentLocked)+ '\n'
        PrintTxt += 'Profitability @ Safe: ' + str(round((TotalConsvVal / InvestmentLocked) *100,2)) + ' %\n\n'
        PrintTxt += '@Safe ==> ENTRY on point and EXIT on T1 and NO second entry after SL is hit'
        return PrintTxt
    else:
        return ''
    

def FetchPrintMsgSafe2():
    print(12345)
    PrimeQueueTmpA = pd.read_csv(MyPrimeQueueLoadBackCsv)
    PrimeQueueTmp = PrimeQueueTmpA[(PrimeQueueTmpA['order_type'] =='EXIT_SAFE2')]
    MyPrimeQueuePL = pd.read_csv(MyPrimeQueuePLCsv)
    PrimeQueueTmp2 = MyPrimeQueuePL[(MyPrimeQueuePL['7ScriptMode'] == "ToChannelSafe2")]


    TotalNFTPoints = 0
    TotalBNFPoints = 0
    EntryCounter = 0
    ProftCounter = 0
    LossCounter = 0
    InvestmentLocked = 0
    NFTCounter = 0
    BNFCounter=0
    NFTConsvPoints = 0
    BNFConsvPoints = 0

    if len(PrimeQueueTmp2) > 0:
        InvestmentLocked = int(PrimeQueueTmp2['5MaxInv'].max())


    print(7890,len(PrimeQueueTmp))
    PrintTxt = 'RESULT OF NEW SAFE EXIT2 [UNDER TEST]\n\n'
    for i in range(0, len(PrimeQueueTmp)):
        lot_size = int(PrimeQueueTmp.iloc[i]['quantity'])
        entry_price1 = float(PrimeQueueTmp.iloc[i]['entry_price'])
        cHigh = float(PrimeQueueTmp.iloc[i]['high'])
        cLow = float(PrimeQueueTmp.iloc[i]['low'])
        ltp = float(PrimeQueueTmp.iloc[i]['ltp'])
        IndexEntry = PrimeQueueTmp.iloc[i]['IndexEntry']
        IndexName = PrimeQueueTmp.iloc[i]['IndexName']
        buy_price = float(PrimeQueueTmp.iloc[i]['buy_price'])
        
        entry_price = entry_price1

        T1 = float(PrimeQueueTmp.iloc[i]['T1'])
        T2 = float(PrimeQueueTmp.iloc[i]['T2'])
        T3 = float(PrimeQueueTmp.iloc[i]['T3'])
        SL = float(PrimeQueueTmp.iloc[i]['SL1'])
        SLMsg = PrimeQueueTmp.iloc[i]['SLMsg']
        T1sell_price = float(PrimeQueueTmp.iloc[i]['T1sell_price'])
        T2sell_price = float(PrimeQueueTmp.iloc[i]['T2sell_price'])
        T3sell_price = float(PrimeQueueTmp.iloc[i]['T3sell_price'])
        SLsell_price = float(PrimeQueueTmp.iloc[i]['SLsell_price'])
        #print(buy_price,T1sell_price, T2sell_price,T2sell_price,SLsell_price)
        TargetHit = False
        SlHit = False
        Tsell_price = 0
        ProfitPoints = 0
        LossPoints = 0
        PP = 0
        if buy_price > 0:
            EntryCounter += 1
            #if T1sell_price > 0:
            #    EP = T1sell_price
            #if SLsell_price > 0:
            #    EP = SLsell_price

            if T1sell_price > 0:
                ConsvPoints = round(T1sell_price - buy_price,0)
                TargetHit = True
                TG = "T1"
                Tsell_price = T1sell_price
                if T2sell_price > 0:
                    TG = "T2"
                    Tsell_price = T2sell_price
                if T3sell_price > 0:
                    TG = "T3"
                    Tsell_price = T3sell_price
                ProfitPoints = round(Tsell_price - buy_price,0)
                PP = (ProfitPoints * lot_size) - 75
            if SLsell_price > 0:
                SlHit = True
                ConsvPoints = round(SLsell_price - buy_price,0)
                LossPoints  = round(SLsell_price - buy_price,0)
            #print(TG, TargetHit, SlHit)
            
            

            #print('ProfitPoints',ProfitPoints,'ConsvVal',ConsvVal,'CurConsvVal',CurConsvVal,'buy_price',buy_price,'ConsvExitAt',ConsvExitAt,'lot_size',lot_size)
            NutralPoints = round(buy_price - ltp,0)
            PMS = ''
            if SlHit == True:
                PrintTxt += IndexEntry + ' : ' + str(int(LossPoints)) + ' (SL HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = LossPoints
                PMS = '   (SL HIT)'
            if TargetHit == True and Tsell_price > 0:
                PrintTxt += IndexEntry + ' : ' + str(int(ProfitPoints)) + ' POINTS (' + TG + ' HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = ProfitPoints
                if PMS == '':
                    PMS = '   (' + TG + ' HIT)'
            elif NutralPoints > 0 and Tsell_price == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (T1 NOT HIT)\n'
                ProftCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (T1 NOT HIT)'
            elif NutralPoints < 0 and SlHit == False:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (LOSS - SL NOT HIT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (LOSS - SL NOT HIT)'
            elif NutralPoints == 0:
                PrintTxt += IndexEntry + ' : ' + str(int(NutralPoints)) + ' POINTS (NO MOVEMENT)\n'
                LossCounter += 1
                CurrentEntryPoints = NutralPoints
                if PMS == '':
                    PMS = '   (NO MOVEMENT)'
            
            
            '''print('IndexEntry'.ljust(10)+ IndexEntry.ljust(10) + 'BP:'.ljust(6) + str(int(buy_price)).ljust(6) + \
                    'EP'.ljust(6) + str(int(EP)).ljust(6) + \
                    'Lo'.ljust(6) + str(int(cLow)).ljust(6) + \
                    'Hi'.ljust(6) + str(int(cHigh)).ljust(6) + \
                    'LT'.ljust(6) + str(int(ltp)).ljust(6) + \
                    'PP'.ljust(6) + str(int(ConsvPoints)).ljust(6) + \
                    'PFT'.ljust(6) + str(int((ConsvPoints * lot_size)-75)).ljust(6) + \
                    'MP'.ljust(6) + str(int((PP))).ljust(6) + PMS)'''

            if IndexName == 'NIFTY':
                TotalNFTPoints += CurrentEntryPoints
                NFTCounter += 1
                if SlHit == True:
                    NFTConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    NFTConsvPoints += ConsvPoints
                else:
                    NFTConsvPoints += NutralPoints
                nft_lot_size = lot_size
            else:
                TotalBNFPoints += CurrentEntryPoints
                BNFCounter += 1
                if SlHit == True:
                    BNFConsvPoints += LossPoints
                elif TargetHit == True and SlHit == False:
                    BNFConsvPoints += ConsvPoints
                else:
                    BNFConsvPoints += NutralPoints
                bnf_lot_size = lot_size
            #print(TotalBNFPoints,TotalNFTPoints)

    NFTValue = 0 
    BNFValue = 0
    NFTConsvValue = 0
    BNNFConsvValue = 0
    if NFTCounter > 0:
        NFTValue = (TotalNFTPoints * nft_lot_size) - (NFTCounter * 75)
        NFTConsvValue = (NFTConsvPoints * nft_lot_size) - (NFTCounter * 75)
    print(NFTValue)
    if BNFCounter > 0:
        BNFValue = (TotalBNFPoints * bnf_lot_size) - (BNFCounter * 75)
        BNNFConsvValue = (BNFConsvPoints * bnf_lot_size) - (BNFCounter * 75)
    print(BNFValue)
    TotalVal = NFTValue + BNFValue
    TotalConsvVal = NFTConsvValue + BNNFConsvValue
    if NFTValue != 0 or  BNFValue != 0:
        #PrintTxt += '\nSuccess Ratio: ' + str(int(round(int((ProftCounter/(ProftCounter+LossCounter)) * 100)/5,0)*5)) + '%\n\n'
        PrintTxt += '\nNet Result: @ Max Points # ' + str(int(TotalVal)) + ', @ Safe '+ ' # ' + str(int(TotalConsvVal))  + ' [After Brokerage]\n'
        if BNFValue != 0:
            PrintTxt += ('BANKNIFTY ' + str(bnf_lot_size))+ ' @ Max Points '      + str(int(TotalBNFPoints)) + ' # ' + str(int(BNFValue)) + ', @ Safe # ' + str(int(BNNFConsvValue)) + '\n'
        if NFTValue != 0:
            PrintTxt += ('NIFTY ' + str(nft_lot_size)) + ' @ Max Points '      + str(int(TotalNFTPoints))+ ' # ' + str(int(NFTValue))+ ', @ Safe # ' + str(int(NFTConsvValue)) + '\n\n'
        
        
        PrintTxt += 'MaxInvestmentLocked @ Safe: ' + str(InvestmentLocked)+ '\n'
        PrintTxt += 'Profitability @ Safe: ' + str(round((TotalConsvVal / InvestmentLocked) *100,2)) + ' %\n\n'
        PrintTxt += '@Safe ==> ENTRY on point and EXIT on T1 and NO second entry after SL is hit'
        return PrintTxt
    else:
        return ''
    
#async def BaseSetup():
StockDate = GetStockDate(datetime.datetime.now().date(), 3) # 0 = Monday, 1=Tuesday, 2=Wednesday...
if StockDate == '21819':
    StockDate = '21818'
if StockDate == '21N04':
    StockDate = '21N03'

print(StockDate)
TodayCodeBNF = "BANKNIFTY" + StockDate
TodayCodeNFT = "NIFTY" + StockDate
TodayCodeFIN = "FINNIFTY" + StockDate

session = os.environ.get('TG_SESSION', 'printer')
api_id = 1472332
api_hash = '1e98c905f7f49cf78f1067aa98da3ab8'

telegram_token = '668903696:AAHWiDtntw6jrBX5s1VOnmTY0LE3ll2wUuQ'

bot = telepot.Bot(telegram_token)

client = TelegramClient(session, api_id, api_hash).start()
client.start()


if IamTestingNow == True:
    destination_channel_username='TestPing_bot'
else:
    destination_channel_username='ScalpBANKNIFTY'


entity=client.get_entity(destination_channel_username)
ScalpBANKNIFTY = entity.id


ThisDate = datetime.datetime.now().date().strftime('%Y%m%d')
fileName = 'TelethonData' + ThisDate + '_5.csv'


if path.exists(fileName):
    SendMorningMessage = False
    print('DONT Send MESSAGE to TG')

else:
    print('START Send MESSAGE to TG')
    SendMorningMessage = True
    Msg1 = 'Good Morning Scalpers \nWish you good day $$$'
    Msg2 = 'DISCLAIMER: KIND ATTENTION \n\n ALL UPDATES AND POSTS IN THIS CHANNEL ARE ONLY FOR KNOWLEDGE AND RESEARCH PURPOSE. ALL VIEWS PRESENTED HERE ARE NON-ADVISORY. ' + \
            'I AM NOT SEBI REGISTERED AND NOT RESPONSIBLE FOR ANY DIRECT OR INDIRECT PROFIT OR LOSS. ' + \
            'EQUITY INVESTMENTS ARE SUBJECT TO 100% MARKET RISK. PLEASE TALK TO YOUR FINANCIAL ADVISOR BEFORE TAKING ANY POSITIONS, NO RIGHTS/CLAIMS.'
    Msg3 = 'KIND ATTENTION: \n\n$$ BANKNIFTY and NIFTY OPTIONS are HIGHLY VOLATILE and SUBJECT TO 100% MARKET RISK\n\n'
    Msg3 = Msg3 + '$$ MESSAGE TO REMIND MYSELF EVERYDAY\n\n'
    Msg3 = Msg3 + '$$ I wait and enter only in given range, and follow strict Stop Loss and Target.\n\n'
    Msg3 = Msg3 + '$$ I DO NOT trade if entry levels missed and do not over trade once SL or Target hit.\n\n'
    Msg3 = Msg3 + '$$ I DO NOT buy if price is falling, wait for it to bounce back.\n\n'
    Msg3 = Msg3 + '$$ I Avoid trading once I earn 2K or 2% of your capital, DONT LOSE THE PROFITS!\n\n'
    Msg3 = Msg3 + '$$$$$$$$$$$$$$$$$$$$$$$$$\n\n'
    Msg4 = ''
    TmpMsg1 = ''
    TmpMsg2 = ''
    TmpMsg3 = ''
    TmpMsg4 = ''

file = open(fileName, 'a')
writer = csv.writer(file)


if path.exists(fileName) == False:
    writer.writerow(['MsgID','MsgFromID','MsgDate','MsgFwd','MsgReply','MsgBot','MsgSender','MsgTxt','MsgOrder','MsgSenderID','nowStart','nowEnd','CleanTxt'])


#destination_channel_username='PythonTestChannel1'
#entity=client.get_entity(destination_channel_username)

#with client:
#    await client.send_message('me', 'Hello to myself!')

bot.sendMessage(userSelf, 'StartProcess')


# `pattern` is a regex, see https://docs.python.org/3/library/re.html
# Use https://regexone.com/ if you want a more interactive way of learning.
#
# "(?i)" makes it case-insensitive, and | separates "options".
#@client.on(events.NewMessage(pattern=r'(?i).*\b(hello|hi)\b'))
@client.on(events.NewMessage())


#async def main():
#    await asyncio.gather(BaseSetup(), ProcessMyQueue())

async def handler(event):
    global ForceExit
    global ForceExitACTIVE
    global ForceExitPENDING

    global OkToForceExit
    global TradeStartHour
    global TradeStartMinute
    global TradeStartSecond
    global NoNewEntryHour 
    global NoNewEntryMinute
    global TestStepIncVal
    global TestStepInc
    global TestStepDec
    global TestStepDecVal
    global SendMorningMessage

    global Msg1
    global TmpMsg1
    global Msg2
    global TmpMsg2
    global Msg3
    global TmpMsg3
    global Msg4
    global TmpMsg4
    '''
    async for dialog in client.iter_dialogs():
        #print(dialog)
        print(dialog.id, ',', dialog.title)
    '''
    if SendMorningMessage == True and SendMesageToTelegram == True:
        if Msg1 != '':
            TmpMsg1 = Msg1
            Msg1 = ''
            print('Send MESSAGE to TG')
            await client.send_message(ScalpBANKNIFTY, TmpMsg1)
        sleep(3)
        if Msg2 != '':
            TmpMsg2 = Msg2
            Msg2 = ''
            print('Send MESSAGE to TG')
            await client.send_message(ScalpBANKNIFTY, TmpMsg2)
        sleep(3)
        if Msg3 != '':
            TmpMsg3 = Msg3
            Msg3 = ''
            print('Send MESSAGE to TG')
            await client.send_message(ScalpBANKNIFTY, TmpMsg3)
        sleep(3)
        if Msg4 != '':
            TmpMsg4 = Msg4
            Msg4 = ''
            print('Send MESSAGE to TG')
            await client.send_message(ScalpBANKNIFTY, TmpMsg4)
        SendMorningMessage = False

    if SendMorningMessage == False:
        

        nowStart = datetime.datetime.now()
        sender = await event.get_sender()
        try:
            sender_id = sender.id
        except:
            sender_id = 0
        if (sender_id == 468457704 or sender_id == 668903696  or sender_id == 434371522 ):
            if event.text.upper() == "EXIT":
                ForceExit = True
                print('1ForceExit',ForceExit)
            if event.text.upper() == "ACTIVE":
                ForceExitACTIVE = True
                print('1ForceExitACTIVE',ForceExitACTIVE)
            if event.text.upper() == "PENDING":
                ForceExitPENDING = True
                print('1ForceExitPENDING',ForceExitPENDING)

        if (sender_id == 668903696  or sender_id == 434371522 ) and event.text.upper() == "FORCEEXITNOW":
            if OkToForceExit == True:
                print('============ Terminating the script =========')
                sys.exit()
        name = utils.get_display_name(sender)
        OrigText = event.text.upper()
        CleanTxt, OrignalCleanText = cleanup_text(OrigText)
        OrderText = ""
        MsgFwd = "False"
        MsgReply = "False"
        MsgBot = "False"    
        if event.fwd_from:
            print('Skip FWD Msg')
            MsgFwd = "True"
        elif event.reply_to_msg_id:
            print('Skip Reply Msg')
            MsgReply = "True"
        elif event.via_bot_id:
            print('Skip Bot Msg')
            MsgBot = "True"
        else:
            if ((sender_id == 468457704 or sender_id == 668903696  or sender_id == 434371522) and (("SELL" in OrigText) or ("BUY" in OrigText))) or ("SELL" not in OrigText) and (sender_id != ScalpBANKNIFTY):
                SenderCleanName = cleanup_title(name)
                try:
                    OrderText = await ProcessMyText(CleanTxt, SenderCleanName, sender_id)
                except Exception as e:
                    print('ProcessMyText Error',str(e))
                    OrderText = str(e)
                print(name, ': ', OrderText)
        
        nowEnd = datetime.datetime.now()
        MsgID = event.id 
        MsgFromID = event.from_id
        MsgDate = event.date
        MsgSenderID = sender    
        MsgSender = name
        MsgTxt = OrignalCleanText
        MsgOrder = OrderText
        writer.writerow([MsgID,MsgFromID,MsgDate,MsgFwd,MsgReply,MsgBot,MsgSender,MsgTxt,MsgOrder,MsgSenderID,nowStart,nowEnd,CleanTxt])
        print(nowEnd)

    
try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()

