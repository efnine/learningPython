import fix_yahoo_finance as yf
import pandas as pd
import datetime
#import Tkinter
#import tkinter
#from tkFileDialog import askopenfilename
import time
import sys #used to identify python version
import getpass #used to get PC username

### Lets define where files will get saved to ####
username = getpass.getuser()
read_file_path = "C:/Users/" + username + "/Documents/Sync/FUND-ADMINISTRATION/YahooDownloader/YahooDownloaderApp/"
download_file_path = "C:\\Users\\" + username + "\\Documents\\Sync\\FUND-ADMINISTRATION\\YahooDownloader\\YahooDownloaderApp\\yfDownloads\\"

def fetchTickers():
    print("\n")
    print("Hi there, please select csv file containing Yahoo tickers ")
    print("you'd like me to read-in:")
    print("\n")
    time.sleep(2)
    
    # I'd like the app to work for both Py 2 and 3
    if sys.version_info[0] < 3:
        import Tkinter # not pythonic to import in middle of function, but in this case it makes sense
        from tkFileDialog import askopenfilename
        root = Tkinter.Tk() ; root.withdraw()
    else:
        import tkinter # not pythonic to import in middle of function, but in this case it makes sense
        from tkinter.filedialog import askopenfilename
        root = tkinter.Tk() ; root.withdraw()

    while True:
        try:
            csv_filename = askopenfilename(parent=root)
            df = pd.read_csv(csv_filename, header=None)
            ticker_list = list(df.values.T.flatten())
            
            for ticker in ticker_list:
                try:
                    fetchYahooStockData(ticker)
                    print("\n")
                    print(ticker + " has been downloaded")
                except (RuntimeError, TypeError, NameError):
                    print(ticker + " Doesn't look right")
                    pass
                
            print("\n"*2)
            print("I've downloded the following tickers: ")
            for ticker in ticker_list:
                print(ticker)
            print("\nGood bye")
            break
        except ValueError:
            print("That file is not a csv, try again.")
            #fetchTickers()
        except IOError:
            print("\nGood Bye.")
            break
                    
            
def fetchYahooStockData(yahoo_ticker):
    """
    (follow promt) -> csv with yahoo tickers in it
    
    Function retrieves data from Yahoo and writes the data into a csv file.
    It assumes the data should range from 1999-01-01 to yesterday.
    
    >>> fetchYahooData("RY.TO","YahooOutput-RY.csv")
    """
    csv_filename = "yf-" + yahoo_ticker + ".csv"
    start_date = "1979-01-01" # can be wtc date you'd like yyyy-mm-dd
#     start_date = "2017-12-29" # can be wtc date you'd like yyyy-mm-dd
    end_date = datetime.datetime.now()
    # Call Yahoo
    yahoo_data = yf.download(yahoo_ticker, start=start_date, end=end_date)
    # Turn call into csv file
    yahoo_data.to_csv(download_file_path + csv_filename)


# def tickerToCSV(List_of_tickers):
#     ticker_list = []
#     for i in range(len(List_of_tickers)):
#         ticker_list.append(List_of_tickers[i])
#         df = pd.DataFrame(ticker_list)
#         df.to_csv("YahooTickerList.csv",index=None,header=False)

#### Lets download a list of ticker lists ###
# def batchFetchTickers():
#     yahooTickerLists = ["xfnTickerList.csv","xegTickerList.csv", 
#                         "xlfTickerList.csv", "qqqTickerList.csv",
#                         "denTickerList.csv","canSectorsTickerList.csv",
#                         "usaSectorsTickerList.csv"]
#     
#     print("\nDownloading the following ticker lists:")
#     print(yahooTickerLists)
#     time.sleep(1)
#     
#     for tickerList in yahooTickerLists:
#         print("****************************************")
#         print("Downloading " + tickerList)
#         print("****************************************")
#         csv_filename = tickerList
#         full_path = read_file_path + csv_filename
#         df = pd.read_csv(full_path, header=None)
#         ticker_list = list(df.values.T.flatten())
# 
#         
#         for ticker in ticker_list:
#             try:
#                 fetchYahooStockData(ticker)
#                 print("\n")
#                 print(ticker + " has been downloaded")
#             except:
#                 print("\n")
#                 print(ticker + " failed to be downloaded")
#         
#         print("\n")
#         print("_________________________________________")
#         print("I've downloded the following tickers: ")
#         print(ticker_list)
#         print("_________________________________________")
        

fetchTickers()
    

        