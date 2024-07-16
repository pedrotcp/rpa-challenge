# (Pedro Araujo) RPA Challenge - Fresh News 2.0
                             ________   ________   ________                                            
                            |\   __  \ |\   __  \ |\   __  \                                           
                            \ \  \|\  \\ \  \|\  \\ \  \|\  \                                          
                             \ \   _  _\\ \   ____\\ \   __  \                                         
                              \ \  \\  \|\ \  \___| \ \  \ \  \                                        
                               \ \__\\ _\ \ \__\     \ \__\ \__\                                       
                                \|__|\|__| \|__|      \|__|\|__|                                       
     ________   ___  ___   ________   ___        ___        _______    ________    ________   _______      
    |\   ____\ |\  \|\  \ |\   __  \ |\  \      |\  \      |\  ___ \  |\   ___  \ |\   ____\ |\  ___ \     
    \ \  \___| \ \  \\\  \\ \  \|\  \\ \  \     \ \  \     \ \   __/| \ \  \\ \  \\ \  \___| \ \   __/|    
     \ \  \     \ \   __  \\ \   __  \\ \  \     \ \  \     \ \  \_|/__\ \  \\ \  \\ \  \  ___\ \  \_|/__  
      \ \  \____ \ \  \ \  \\ \  \ \  \\ \  \____ \ \  \____ \ \  \_|\ \\ \  \\ \  \\ \  \|\  \\ \  \_|\ \ 
       \ \_______\\ \__\ \__\\ \__\ \__\\ \_______\\ \_______\\ \_______\\ \__\\ \__\\ \_______\\ \_______\
        \|_______| \|__|\|__| \|__|\|__| \|_______| \|_______| \|_______| \|__| \|__| \|_______| \|_______|
<hr>
This is the repository for a fictional automation company called Araujo Automation, created for the Fresh News 2.0 RPA Challenge

<p align="center">
  <img src="https://github.com/pedrotcp/rpa-challenge/blob/main/docs/A2.png?raw=true" />
</p>
<hr>
This robot extracts news from a news website and writes it to an excel file.

It is written in Python, and uses Robocorp's Python RPA framework.  

The news source chosen for it was Los Angeles Times. However there is a base class called BaseNewsSource, which you can extend and use to implement other news sources more easily. 

## Installation

To install this project, first install the Robocorp VSCode extension, login to your robocorp account, and optionally, set up the integration with Github so you always have the most recent version of your robot automatically deployed to your cloud.

```bash
  command -param1
  cd my-project
```


## Documents

The PDD (Process Definition Document) can be found inside the docs directory. It contains, among other things, a high level description of the process as is, and to-be.

The FAR (Financial Analysis Report) can also be found inside the same directory, and contains a brief description of the project costs and savings. 

## TO-DOs
# Optimize the logic for the maximum number of months (check with the user) ;
# Maintain execution of next Work Item in queue even if an error is thrown in the current one;
# Check if the month parameter should be considered whole or partial i.e. "Last 2 months" should fall in any day of the 2nd month going back, or the first day of that month?    
# Create fallback strategies, i.e., if robot cannot paginate via WebElements, maybe try via URL (if parameter is present)
# Try to identify sources that implement captchas that prevent scraping and maybe use proxy/change webdriver (I.e. use Edge or Firefox)


## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)



## Author

- [@pedrotcp](https://www.github.com/pedrotcp)
  [Linkedin](https://www.linkedin.com/in/pedroharaujo/)


