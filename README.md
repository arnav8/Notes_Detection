# Notes_Detection

To solve this problem of detecting notes in an audio file, I went throught the documentation of [Aubio](https://aubio.org/), which contains tons of fucntions that we can use. Using, the aubio python package I came up with this [script](https://github.com/arnav8/Notes_Detection/blob/main/aubio_notes.py) that outputs the notes of an audio along with the timestamps. 

### [aubio_notes.py](https://github.com/arnav8/Notes_Detection/blob/main/aubio_notes.py):
* Using Fast Fourier transform and the ``` notes ``` function of the aubio package, i desgined this script that outputs a series of timeframe and detected note at that timeframe. 
* The performace of the script is depicted in the table below, and it misrecognises only two notes in the audio clip. Test Audio was the [Happy Birthday song](https://www.youtube.com/watch?v=GL3fe5dzeyQ&t=19s).

   Time (sec) | Predicted Note  | Actual Note|\
5.921088  ------>  A#5		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <-----Audio Starts------>\
6.954376  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\
7.244626  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\
7.401361  ------>  D4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D4\
7.749660  ------>  C5           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C5\
8.121179  ------>  F3           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F3\
8.492698  ------>  E4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E4\
9.444717  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\         
9.723356  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\
9.851066  ------>  D4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D4\
10.199365  ------>  C5			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C5\
10.895964  ------>  C3			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3 (MISMATCH)\
11.279093  ------>  F4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F4\
12.149841  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4
12.480726  ------>  C4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\
13.246984  ------>  D4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4 (MISMATCH)\
13.328254  ------>  C5			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C4\
13.839093  ------>  A4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A4\
14.309297  ------>  F4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F4\
14.686621  ------>  E4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E4\
15.092971  ------>  D4		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	D4\
16.068209  ------>  A#4			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A#4\
16.312018  ------>  A#4		    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A#4\
16.491973  ------>  A4		    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A4\
16.851882  ------>  F4          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F4\
17.159546  ------>  G4          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4\
17.531066  ------>  F4          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F4\
18.947483  ------>  C#3			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <-----Audio Ends------>\


### [Note Recognition In Python - Method 2](https://medium.com/@ianvonseggern/note-recognition-in-python-c2020d0dae24):
* Lastly, I also came across this [Medium article](https://medium.com/@ianvonseggern/note-recognition-in-python-c2020d0dae24), which tries to solve the same problem. The Code and implemenation for the same came be found [here](https://github.com/ianvonseggern1/note-prediction).
* Results of this approach are as follows:\
Actual Notes\
['E', 'F#', 'G#', 'A', 'E', 'A', 'A', 'B', 'C#', 'D', 'A', 'D', 'D', 'C#', 'B', 'A', 'E', 'A', 'A', 'G#', 'F#', 'E', 'B', 'B', 'E', 'F#', 'E', 'B', 'D#', 'B', 'A', 'G#', 'F#', 'E', 'B', 'E', 'B', 'E', 'B', 'E', 'B', 'E', 'B', 'E']\
Predicted Notes\
['E', 'F#', 'G#', 'A', 'A', 'A', 'B', 'C#', 'D', 'A', 'D', 'C#', 'B', 'A', 'E', 'A', 'A', 'G#', 'F#', 'E', 'B', 'B', 'E', 'F#', 'E', 'B', 'D#', 'B', 'A', 'G#', 'F#', 'E', 'B', 'B', 'B', 'B', 'E', 'B', 'E', 'B']\
Levenshtein distance: 5/44 
