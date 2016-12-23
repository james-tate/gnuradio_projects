# gnuradio_projects

gnuradio projects I use mainly for testing and learning

If you would like to run any of the projects, the top_block.py can be run independently in each project. The .grc of file 
in the project folder can be opened and modified in gnuradio-companion.

gnuradio blocks used:
----------------------
  gr-osmosdr  
  gr-qtgui // If you get an error "ImportError: cannot import name qtgui" install libqwt-dev then rebuild gnuradio. (for pybombs -> "pybombs rebuild gnuradio")  
  gr-wxgui  

projects
-----------------------
hackrf_fm_radio: a fm radio tuner with gui fft, compatible with osmosdr source. Based on [SDR with HackRF, Lesson 1](https://greatscottgadgets.com/sdr/1/)
