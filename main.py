from pytube import YouTube

def run():
    def Dowload(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print('There has been an error in downloading this video')
        print('This dowload has completed :)')

    Dowload(input('Put your youtube link here: '))



if __name__=='__main__':
    run()