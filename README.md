# salary-scraping
This repository is part of my research project on how different retirement savings plans offered by the same employer may crowd out each other. 

A quick example here is that suppose your employer offers two retirement savings plan: a 401(k) plan and a 403(b) plan. My research wants to see how do your participation and contribution decisions on the 403(b) plan changes if your employer forces you to contribute more to the 401(k) plan. 

Maybe some of you may say, of course I will just reduce my contribution to the 403(b) plan if I'm forced to contribute more to the 401(k) plan. The problems in the real world are:
* You may or may not paying attention to your 401(k) plan. A large portion of people would just don't pay any attention 
* Even if you do pay attention to the 401(k), you may choose not to change anything on the 403(b) plan side because maybe some investment offered in 403(b) plan outperform everything in the 401(k) plan. 

I have data of workers in a large non-profit employer. The problem is that salaries are collapsed into bins by data provider and I'd like to web scrap salary for the employer in a given year and later on use the actual salary data to randomly draw annual earnings from appropriate bins so that I can use imputed salary in my analysis later on.  
