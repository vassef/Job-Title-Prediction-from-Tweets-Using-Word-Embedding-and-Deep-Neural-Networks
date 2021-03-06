# instruction to install twint
# install git
# pip3 install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
# instruction to install emojis
# pip3 install emojis

import pandas as pd
import emot
import emojis
import twint
import nest_asyncio

Emojie = ['๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐คฃ', '๐', '๐', '๐', '๐', '๐', '๐', '๐ฅฐ', '๐', '๐คฉ', '๐',
          '๐',
          'โบ๏ธ', '๐', '๐', '\U0001f972', '๐', '๐', '๐', '๐คช', '๐', '๐ค', '๐ค', '๐คญ', '๐คซ', '๐ค', '๐ค', '๐คจ', '๐',
          '๐', '๐ถ', '๐', '๐', '๐', '๐ฌ', '๐คฅ', '๐', '๐', '๐ช', '๐คค', '๐ด', '๐ท', '๐ค', '๐ค', '๐คข', '๐คฎ', '๐คง',
          '๐ฅต',
          '๐ฅถ', '๐ฅด', '๐ต', '๐คฏ', '๐ค ', '๐ฅณ', '\U0001f978', '๐', '๐ค', '๐ง', '๐', '๐', '๐', 'โน๏ธ', '๐ฎ', '๐ฏ', '๐ฒ',
          '๐ณ', '๐ฅบ', '๐ฆ', '๐ง', '๐จ', '๐ฐ', '๐ฅ', '๐ข', '๐ญ', '๐ฑ', '๐', '๐ฃ', '๐', '๐', '๐ฉ', '๐ซ', '๐ฅฑ', '๐ค',
          '๐ก',
          '๐ก', '๐ ', '๐คฌ', '๐', '๐ฟ', '๐', 'โ ๏ธ', '๐ฉ', '๐ฉ', '๐ฉ', '๐คก', '๐น', '๐บ', '๐ป', '๐ฝ', '๐พ', '๐ค', '๐บ',
          '๐ธ',
          '๐น', '๐ป', '๐ผ', '๐ฝ', '๐', '๐ฟ', '๐พ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐',
          '๐',
          '๐', 'โฃ๏ธ', '๐', 'โค๏ธ', '๐งก', '๐', '๐', '๐', '๐', '๐ค', '๐ค', '๐ค', '๐ฏ', '๐ข', '๐ฅ', '๐ฅ', '๐ซ', '๐ฆ',
          '๐จ',
          '๐ณ๏ธ', '๐ฃ', '๐ฌ', '๐๏ธ\u200d๐จ๏ธ', '๐จ๏ธ', '๐ฏ๏ธ', '๐ญ', '๐ค', '๐', '๐ค', '๐๏ธ', 'โ', 'โ', '๐', '๐',
          '\U0001f90c', '๐ค', 'โ๏ธ', '๐ค', '๐ค', '๐ค', '๐ค', '๐', '๐', '๐', '๐', '๐', '๐', 'โ๏ธ', '๐', '๐', '๐',
          '๐', 'โ', 'โ', '๐', '๐', '๐', '๐ค', '๐ค', '๐', '๐', '๐', '๐คฒ', '๐ค', '๐', 'โ๏ธ', '๐', '๐คณ', '๐ช',
          '๐ฆพ',
          '๐ฆฟ', '๐ฆต', '๐ฆถ', '๐', '๐ฆป', '๐', '๐ง ', '\U0001fac0', '\U0001fac1', '๐ฆท', '๐ฆด', '๐', '๐๏ธ', '๐', '๐',
          '๐ถ',
          '๐ง', '๐ฆ', '๐ง', '๐ง', '๐ฑ', '๐จ', '๐ง', '๐จ\u200d๐ฆฐ', '๐จ\u200d๐ฆฑ', '๐จ\u200d๐ฆณ', '๐จ\u200d๐ฆฒ', '๐ฉ',
          '๐ฉ\u200d๐ฆฐ', '๐ง\u200d๐ฆฐ', '๐ฉ\u200d๐ฆฑ', '๐ง\u200d๐ฆฑ', '๐ฉ\u200d๐ฆณ', '๐ง\u200d๐ฆณ', '๐ฉ\u200d๐ฆฒ',
          '๐ง\u200d๐ฆฒ',
          '๐ฑ\u200dโ๏ธ', '๐ฑ\u200dโ๏ธ', '๐ฑ\u200dโ๏ธ', '๐ง', '๐ด', '๐ต', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐',
          '๐\u200dโ๏ธ',
          '๐\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ',
          '๐', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐ง',
          '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐คฆ', '๐คฆ\u200dโ๏ธ', '๐คฆ\u200dโ๏ธ', '๐คท',
          '๐คท\u200dโ๏ธ', '๐คท\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐จ\u200dโ๏ธ', '๐ฉ\u200dโ๏ธ', '๐ง\u200d๐', '๐จ\u200d๐',
          '๐ฉ\u200d๐',
          '๐ง\u200d๐ซ', '๐จ\u200d๐ซ', '๐ฉ\u200d๐ซ', '๐ง\u200dโ๏ธ', '๐จ\u200dโ๏ธ', '๐ฉ\u200dโ๏ธ', '๐ง\u200d๐พ',
          '๐จ\u200d๐พ',
          '๐ฉ\u200d๐พ', '๐ง\u200d๐ณ', '๐จ\u200d๐ณ', '๐ฉ\u200d๐ณ', '๐ง\u200d๐ง', '๐จ\u200d๐ง', '๐ฉ\u200d๐ง',
          '๐ง\u200d๐ญ',
          '๐จ\u200d๐ญ', '๐ฉ\u200d๐ญ', '๐ง\u200d๐ผ', '๐จ\u200d๐ผ', '๐ฉ\u200d๐ผ', '๐ง\u200d๐ฌ', '๐จ\u200d๐ฌ',
          '๐ฉ\u200d๐ฌ',
          '๐ง\u200d๐ป', '๐จ\u200d๐ป', '๐ฉ\u200d๐ป', '๐ง\u200d๐ค', '๐จ\u200d๐ค', '๐ฉ\u200d๐ค', '๐ง\u200d๐จ',
          '๐จ\u200d๐จ',
          '๐ฉ\u200d๐จ', '๐ง\u200dโ๏ธ', '๐จ\u200dโ๏ธ', '๐ฉ\u200dโ๏ธ', '๐ง\u200d๐', '๐จ\u200d๐', '๐ฉ\u200d๐',
          '๐ง\u200d๐',
          '๐จ\u200d๐', '๐ฉ\u200d๐', '๐ฎ', '๐ฎ', '๐ฎ\u200dโ๏ธ', '๐ฎ\u200dโ๏ธ', '๐ต๏ธ', '๐ต๏ธ\u200dโ๏ธ', '๐ต๏ธ\u200dโ๏ธ', '๐',
          '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '\U0001f977', '๐ท', '๐ท\u200dโ๏ธ', '๐ท\u200dโ๏ธ', '๐คด', '๐ธ', '๐ณ', '๐ณ\u200dโ๏ธ',
          '๐ณ\u200dโ๏ธ', '๐ฒ', '๐ง', '๐คต', '๐คต\u200dโ๏ธ', '๐คต\u200dโ๏ธ', '๐ฐ', '๐ฐ\u200dโ๏ธ', '๐ฐ\u200dโ๏ธ', '๐ฐ\u200dโ๏ธ',
          '๐คฐ',
          '๐คฑ', '๐ฉ\u200d๐ผ', '๐จ\u200d๐ผ', '๐ง\u200d๐ผ', '๐ผ', '๐', '๐คถ', '๐ง\u200d๐', '๐ฆธ', '๐ฆธ\u200dโ๏ธ',
          '๐ฆธ\u200dโ๏ธ',
          '๐ฆน', '๐ฆน\u200dโ๏ธ', '๐ฆน\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง',
          '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง',
          '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐',
          '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐ถ', '๐ถ\u200dโ๏ธ', '๐ถ\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง',
          '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง\u200d๐ฆฏ', '๐จ\u200d๐ฆฏ', '๐ฉ\u200d๐ฆฏ', '๐ง\u200d๐ฆผ', '๐จ\u200d๐ฆผ',
          '๐ฉ\u200d๐ฆผ',
          '๐ง\u200d๐ฆฝ', '๐จ\u200d๐ฆฝ', '๐ฉ\u200d๐ฆฝ', '๐', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐', '๐', '๐บ', '๐ด๏ธ',
          '๐ฏ',
          '๐ฏ\u200dโ๏ธ', '๐ฏ\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐คบ', '๐',
          'โท๏ธ',
          '๐', '๐๏ธ', '๐๏ธ\u200dโ๏ธ', '๐๏ธ\u200dโ๏ธ', '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', '๐ฃ', '๐ฃ\u200dโ๏ธ', '๐ฃ\u200dโ๏ธ',
          '๐', '๐\u200dโ๏ธ', '๐\u200dโ๏ธ', 'โน๏ธ', 'โน๏ธ\u200dโ๏ธ', 'โน๏ธ\u200dโ๏ธ', 'โน๏ธ\u200dโ๏ธ', 'โน๏ธ\u200dโ๏ธ', '๐๏ธ',
          '๐๏ธ\u200dโ๏ธ', '๐๏ธ\u200dโ๏ธ', '๐ด', '๐ด\u200dโ๏ธ', '๐ด\u200dโ๏ธ', '๐ต', '๐ต\u200dโ๏ธ', '๐ต\u200dโ๏ธ', '๐คธ',
          '๐คธ\u200dโ๏ธ', '๐คธ\u200dโ๏ธ', '๐คผ', '๐คผ\u200dโ๏ธ', '๐คผ\u200dโ๏ธ', '๐คฝ', '๐คฝ\u200dโ๏ธ', '๐คฝ\u200dโ๏ธ', '๐คพ',
          '๐คพ\u200dโ๏ธ', '๐คพ\u200dโ๏ธ', '๐คน', '๐คน\u200dโ๏ธ', '๐คน\u200dโ๏ธ', '๐ง', '๐ง\u200dโ๏ธ', '๐ง\u200dโ๏ธ', '๐', '๐',
          '๐ง\u200d๐ค\u200d๐ง', '๐ญ', '๐ซ', '๐ฌ', '๐', '๐ฉ\u200dโค๏ธ\u200d๐\u200d๐จ', '๐จ\u200dโค๏ธ\u200d๐\u200d๐จ',
          '๐ฉ\u200dโค๏ธ\u200d๐\u200d๐ฉ', '๐', '๐ฉ\u200dโค๏ธ\u200d๐จ', '๐จ\u200dโค๏ธ\u200d๐จ', '๐ฉ\u200dโค๏ธ\u200d๐ฉ', '๐ช',
          '๐จ\u200d๐ฉ\u200d๐ฆ', '๐จ\u200d๐ฉ\u200d๐ง', '๐จ\u200d๐ฉ\u200d๐ง\u200d๐ฆ', '๐จ\u200d๐ฉ\u200d๐ฆ\u200d๐ฆ',
          '๐จ\u200d๐ฉ\u200d๐ง\u200d๐ง', '๐จ\u200d๐จ\u200d๐ฆ', '๐จ\u200d๐จ\u200d๐ง', '๐จ\u200d๐จ\u200d๐ง\u200d๐ฆ',
          '๐จ\u200d๐จ\u200d๐ฆ\u200d๐ฆ', '๐จ\u200d๐จ\u200d๐ง\u200d๐ง', '๐ฉ\u200d๐ฉ\u200d๐ฆ', '๐ฉ\u200d๐ฉ\u200d๐ง',
          '๐ฉ\u200d๐ฉ\u200d๐ง\u200d๐ฆ', '๐ฉ\u200d๐ฉ\u200d๐ฆ\u200d๐ฆ', '๐ฉ\u200d๐ฉ\u200d๐ง\u200d๐ง', '๐จ\u200d๐ฆ',
          '๐จ\u200d๐ฆ\u200d๐ฆ', '๐จ\u200d๐ง', '๐จ\u200d๐ง\u200d๐ฆ', '๐จ\u200d๐ง\u200d๐ง', '๐ฉ\u200d๐ฆ',
          '๐ฉ\u200d๐ฆ\u200d๐ฆ', '๐ฉ\u200d๐ง', '๐ฉ\u200d๐ง\u200d๐ฆ', '๐ฉ\u200d๐ง\u200d๐ง', '๐ฃ๏ธ', '๐ค', '๐ฅ',
          '\U0001fac2',
          '๐ฃ', '๐ต', '๐', '๐ฆ', '๐ฆง', '๐ถ', '๐', '๐ฆฎ', '๐\u200d๐ฆบ', '๐ฉ', '๐บ', '๐ฆ', '๐ฆ', '๐ฑ', '๐', '๐\u200dโฌ',
          '๐ฆ', '๐ฏ', '๐', '๐', '๐ด', '๐', '๐ฆ', '๐ฆ', '๐ฆ', '\U0001f9ac', '๐ฎ', '๐', '๐', '๐', '๐ท', '๐', '๐',
          '๐ฝ', '๐', '๐', '๐', '๐ช', '๐ซ', '๐ฆ', '๐ฆ', '๐', '\U0001f9a3', '๐ฆ', '๐ฆ', '๐ญ', '๐', '๐', '๐น', '๐ฐ',
          '๐', '๐ฟ๏ธ', '\U0001f9ab', '๐ฆ', '๐ฆ', '๐ป', '๐ป\u200dโ๏ธ', '๐จ', '๐ผ', '๐ฆฅ', '๐ฆฆ', '๐ฆจ', '๐ฆ', '๐ฆก', '๐พ',
          '๐พ',
          '๐ฆ', '๐', '๐', '๐ฃ', '๐ค', '๐ฅ', '๐ฆ', '๐ง', '๐๏ธ', '๐ฆ', '๐ฆ', '๐ฆข', '๐ฆ', '\U0001f9a4', '\U0001fab6',
          '๐ฆฉ',
          '๐ฆ', '๐ฆ', '๐ธ', '๐', '๐ข', '๐ฆ', '๐', '๐ฒ', '๐', '๐ฆ', '๐ฆ', '๐ณ', '๐', '๐ฌ', '๐ฌ', '\U0001f9ad', '๐',
          '๐ ', '๐ก', '๐ฆ', '๐', '๐', '๐', '๐ฆ', '๐', '๐', '๐', '๐', '\U0001fab2', '๐', '๐ฆ', '\U0001fab3',
          '๐ท๏ธ',
          '๐ธ๏ธ', '๐ฆ', '๐ฆ', '\U0001fab0', '\U0001fab1', '๐ฆ ', '๐', '๐ธ', '๐ฎ', '๐ต๏ธ', '๐น', '๐ฅ', '๐บ', '๐ป', '๐ผ',
          '๐ท',
          '๐ฑ', '\U0001fab4', '๐ฒ', '๐ณ', '๐ด', '๐ต', '๐พ', '๐ฟ', 'โ๏ธ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐',
          '๐', '๐', '๐', '๐', '๐', '๐ฅญ', '๐', '๐', '๐', '๐', '๐', '๐', '\U0001fad0', '๐ฅ', '๐',
          '\U0001fad2',
          '๐ฅฅ', '๐ฅ', '๐', '๐ฅ', '๐ฅ', '๐ฝ', '๐ถ๏ธ', '\U0001fad1', '๐ฅ', '๐ฅฌ', '๐ฅฆ', '๐ง', '๐ง', '๐', '๐ฅ', '๐ฐ', '๐',
          '๐ฅ', '๐ฅ', '\U0001fad3', '๐ฅจ', '๐ฅฏ', '๐ฅ', '๐ง', '๐ง', '๐', '๐', '๐ฅฉ', '๐ฅ', '๐', '๐', '๐', '๐ญ', '๐ฅช',
          '๐ฎ', '๐ฏ', '\U0001fad4', '๐ฅ', '๐ง', '๐ฅ', '๐ณ', '๐ฅ', '๐ฒ', '\U0001fad5', '๐ฅฃ', '๐ฅ', '๐ฟ', '๐ง', '๐ง',
          '๐ฅซ',
          '๐ฑ', '๐', '๐', '๐', '๐', '๐', '๐', '๐ ', '๐ข', '๐ฃ', '๐ค', '๐ฅ', '๐ฅฎ', '๐ก', '๐ฅ', '๐ฅ ', '๐ฅก', '๐ฆ',
          '๐ฆ',
          '๐ฆ', '๐ฆ', '๐ฆช', '๐ฆ', '๐ง', '๐จ', '๐ฉ', '๐ช', '๐', '๐ฐ', '๐ง', '๐ฅง', '๐ซ', '๐ฌ', '๐ญ', '๐ฎ', '๐ฏ', '๐ผ',
          '๐ฅ',
          'โ', '\U0001fad6', '๐ต', '๐ถ', '๐พ', '๐ท', '๐ธ', '๐น', '๐บ', '๐ป', '๐ฅ', '๐ฅ', '๐ฅค', '\U0001f9cb', '๐ง', '๐ง',
          '๐ง', '๐ฅข', '๐ฝ๏ธ', '๐ด', '๐ฅ', '๐ช', '๐ช', '๐บ', '๐', '๐', '๐', '๐', '๐บ๏ธ', '๐พ', '๐งญ', '๐๏ธ', 'โฐ๏ธ', '๐',
          '๐ป', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐งฑ', '\U0001faa8', '\U0001fab5', '\U0001f6d6',
          '๐๏ธ', '๐๏ธ', '๐ ', '๐ก', '๐ข', '๐ฃ', '๐ค', '๐ฅ', '๐ฆ', '๐จ', '๐ฉ', '๐ช', '๐ซ', '๐ฌ', '๐ญ', '๐ฏ', '๐ฐ', '๐',
          '๐ผ', '๐ฝ', 'โช', '๐', '๐', '๐', 'โฉ๏ธ', '๐', 'โฒ', 'โบ', '๐', '๐', '๐๏ธ', '๐', '๐', '๐', '๐', '๐',
          'โจ๏ธ',
          '๐ ', '๐ก', '๐ข', '๐', '๐ช', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐',
          '๐',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '\U0001f6fb', '๐', '๐', '๐', '๐๏ธ',
          '๐๏ธ', '๐ต', '๐ฆฝ', '๐ฆผ', '๐บ', '๐ฒ', '๐ด', '๐น', '\U0001f6fc', '๐', '๐ฃ๏ธ', '๐ค๏ธ', '๐ข๏ธ', 'โฝ', '๐จ', '๐ฅ',
          '๐ฆ',
          '๐', '๐ง', 'โ', 'โต', 'โต', '๐ถ', '๐ค', '๐ณ๏ธ', 'โด๏ธ', '๐ฅ๏ธ', '๐ข', 'โ๏ธ', '๐ฉ๏ธ', '๐ซ', '๐ฌ', '๐ช', '๐บ', '๐',
          '๐',
          '๐ ', '๐ก', '๐ฐ๏ธ', '๐', '๐ธ', '๐๏ธ', '๐งณ', 'โ', 'โณ', 'โ', 'โฐ', 'โฑ๏ธ', 'โฒ๏ธ', '๐ฐ๏ธ', '๐', '๐ง', '๐', '๐',
          '๐',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐ ', '๐', '๐ก', '๐', '๐ข', '๐', '๐ฃ', '๐', '๐ค', '๐', '๐ฅ', '๐',
          '๐ฆ',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐ก๏ธ', 'โ๏ธ', '๐', '๐', '๐ช',
          'โญ',
          '๐', '๐ ', '๐', 'โ๏ธ', 'โ', 'โ๏ธ', '๐ค๏ธ', '๐ฅ๏ธ', '๐ฆ๏ธ', '๐ง๏ธ', '๐จ๏ธ', '๐ฉ๏ธ', '๐ช๏ธ', '๐ซ๏ธ', '๐ฌ๏ธ', '๐', '๐',
          '๐', 'โ๏ธ', 'โ', 'โฑ๏ธ', 'โก', 'โ๏ธ', 'โ๏ธ', 'โ', 'โ๏ธ', '๐ฅ', '๐ง', '๐', '๐', '๐', '๐', '๐', '๐งจ', 'โจ', '๐',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐งง', '๐', '๐', '๐๏ธ', '๐๏ธ', '๐ซ', '๐๏ธ', '๐', '๐', '๐ฅ',
          '๐ฅ', '๐ฅ', 'โฝ', 'โพ', '๐ฅ', '๐', '๐', '๐', '๐', '๐พ', '๐ฅ', '๐ณ', '๐', '๐', '๐', '๐ฅ', '๐', '๐ธ',
          '๐ฅ',
          '๐ฅ', '๐ฅ', 'โณ', 'โธ๏ธ', '๐ฃ', '๐คฟ', '๐ฝ', '๐ฟ', '๐ท', '๐ฅ', '๐ฏ', '๐ช', '๐ช', '๐ฑ', '๐ฎ', '\U0001fa84', '๐งฟ',
          '๐ฎ',
          '๐น๏ธ', '๐ฐ', '๐ฒ', '๐งฉ', '๐งธ', '\U0001fa85', '\U0001fa86', 'โ ๏ธ', 'โฅ๏ธ', 'โฆ๏ธ', 'โฃ๏ธ', 'โ๏ธ', '๐', '๐', '๐ด',
          '๐ญ',
          '๐ผ๏ธ', '๐จ', '๐งต', '\U0001faa1', '๐งถ', '\U0001faa2', '๐', '๐ถ๏ธ', '๐ฅฝ', '๐ฅผ', '๐ฆบ', '๐', '๐', '๐', '๐',
          '๐งฃ',
          '๐งค', '๐งฅ', '๐งฆ', '๐', '๐', '๐ฅป', '๐ฉฑ', '๐ฉฒ', '๐ฉณ', '๐', '๐', '๐', '๐', '๐', '๐๏ธ', '๐', '\U0001fa74',
          '๐', '๐', '๐', '๐ฅพ', '๐ฅฟ', '๐ ', '๐ก', '๐ฉฐ', '๐ข', '๐', '๐', '๐ฉ', '๐', '๐งข', '\U0001fa96', 'โ๏ธ', '๐ฟ',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐ข', '๐ฃ', '๐ฏ', '๐', '๐', '๐ผ', '๐ต', '๐ถ', '๐๏ธ', '๐๏ธ', '๐๏ธ',
          '๐ค', '๐ง', '๐ป', '๐ท', '\U0001fa97', '๐ธ', '๐น', '๐บ', '๐ป', '๐ช', '๐ฅ', '\U0001fa98', '๐ฑ', '๐ฒ', 'โ๏ธ',
          'โ๏ธ',
          '๐', '๐', '๐ ', '๐', '๐', '๐ป', '๐ฅ๏ธ', '๐จ๏ธ', 'โจ๏ธ', '๐ฑ๏ธ', '๐ฒ๏ธ', '๐ฝ', '๐พ', '๐ฟ', '๐', '๐งฎ', '๐ฅ',
          '๐๏ธ',
          '๐ฝ๏ธ', '๐ฌ', '๐บ', '๐ท', '๐ธ', '๐น', '๐ผ', '๐', '๐', '๐ฏ๏ธ', '๐ก', '๐ฆ', '๐ฎ', '๐ฎ', '๐ช', '๐', '๐', '๐',
          '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐ฐ', '๐๏ธ', '๐', '๐', '๐ท๏ธ', '๐ฐ',
          '\U0001fa99',
          '๐ด', '๐ต', '๐ถ', '๐ท', '๐ธ', '๐ณ', '๐งพ', '๐น', 'โ๏ธ', 'โ๏ธ', '๐ง', '๐จ', '๐ฉ', '๐ค', '๐ฅ', '๐ฆ', '๐ซ', '๐ช',
          '๐ฌ',
          '๐ญ', '๐ฎ', '๐ณ๏ธ', 'โ๏ธ', 'โ๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐', '๐', '๐ผ', '๐', '๐', '๐๏ธ', '๐', '๐',
          '๐๏ธ',
          '๐๏ธ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐๏ธ', '๐', '๐', 'โ๏ธ', '๐๏ธ', '๐๏ธ', '๐๏ธ', '๐',
          '๐',
          '๐', '๐', '๐', '๐๏ธ', '๐จ', '๐ช', 'โ๏ธ', 'โ๏ธ', '๐ ๏ธ', '๐ก๏ธ', 'โ๏ธ', '๐ซ', '\U0001fa83', '๐น', '๐ก๏ธ',
          '\U0001fa9a', '๐ง', '\U0001fa9b', '๐ฉ', 'โ๏ธ', '๐๏ธ', 'โ๏ธ', '๐ฆฏ', '๐', 'โ๏ธ', '\U0001fa9d', '๐งฐ', '๐งฒ',
          '\U0001fa9c', 'โ๏ธ', '๐งช', '๐งซ', '๐งฌ', '๐ฌ', '๐ญ', '๐ก', '๐', '๐ฉธ', '๐', '๐ฉน', '๐ฉบ', '๐ช', '\U0001f6d7',
          '\U0001fa9e', '\U0001fa9f', '๐๏ธ', '๐๏ธ', '๐ช', '๐ฝ', '\U0001faa0', '๐ฟ', '๐', '\U0001faa4', '๐ช', '๐งด',
          '๐งท',
          '๐งน', '๐งบ', '๐งป', '\U0001faa3', '๐งผ', '\U0001faa5', '๐งฝ', '๐งฏ', '๐', '๐ฌ', 'โฐ๏ธ', '\U0001faa6', 'โฑ๏ธ', '๐ฟ',
          '\U0001faa7', '๐ง', '๐ฎ', '๐ฐ', 'โฟ', '๐น', '๐บ', '๐ป', '๐ผ', '๐พ', '๐', '๐', '๐', '๐', 'โ ๏ธ', '๐ธ', 'โ',
          '๐ซ',
          '๐ณ', '๐ญ', '๐ฏ', '๐ฑ', '๐ท', '๐ต', '๐', 'โข๏ธ', 'โฃ๏ธ', 'โฌ๏ธ', 'โ๏ธ', 'โก๏ธ', 'โ๏ธ', 'โฌ๏ธ', 'โ๏ธ', 'โฌ๏ธ', 'โ๏ธ', 'โ๏ธ',
          'โ๏ธ',
          'โฉ๏ธ', 'โช๏ธ', 'โคด๏ธ', 'โคต๏ธ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', 'โ๏ธ', '๐๏ธ', 'โก๏ธ', 'โธ๏ธ', 'โฏ๏ธ', 'โ๏ธ',
          'โฆ๏ธ',
          'โช๏ธ', 'โฎ๏ธ', '๐', '๐ฏ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', 'โ', '๐', '๐', '๐',
          'โถ๏ธ',
          'โฉ', 'โญ๏ธ', 'โฏ๏ธ', 'โ๏ธ', 'โช', 'โฎ๏ธ', '๐ผ', 'โซ', '๐ฝ', 'โฌ', 'โธ๏ธ', 'โน๏ธ', 'โบ๏ธ', 'โ๏ธ', '๐ฆ', '๐', '๐', '๐ถ', '๐ณ',
          '๐ด', 'โ๏ธ', 'โ๏ธ', 'โง๏ธ', 'โ๏ธ', 'โ', 'โ', 'โ', 'โพ๏ธ', 'โผ๏ธ', 'โ๏ธ', 'โ', 'โ', 'โ', 'โ', 'โ', 'ใฐ๏ธ', '๐ฑ', '๐ฒ',
          'โ๏ธ',
          'โป๏ธ', 'โ๏ธ', '๐ฑ', '๐', '๐ฐ', 'โญ', 'โ', 'โ๏ธ', 'โ๏ธ', 'โ', 'โ', 'โฐ', 'โฟ', 'ใฝ๏ธ', 'โณ๏ธ', 'โด๏ธ', 'โ๏ธ', 'ยฉ๏ธ', 'ยฎ๏ธ',
          'โข๏ธ',
          '#๏ธโฃ', '*๏ธโฃ', '0๏ธโฃ', '1๏ธโฃ', '2๏ธโฃ', '3๏ธโฃ', '4๏ธโฃ', '5๏ธโฃ', '6๏ธโฃ', '7๏ธโฃ', '8๏ธโฃ', '9๏ธโฃ', '๐', '๐ ', '๐ก', '๐ข',
          '๐ฃ',
          '๐ค', '๐ฐ๏ธ', '๐', '๐ฑ๏ธ', '๐', '๐', '๐', 'โน๏ธ', '๐', 'โ๏ธ', '๐', '๐', '๐พ๏ธ', '๐', '๐ฟ๏ธ', '๐', '๐',
          '๐',
          '๐', '๐๏ธ', '๐ท๏ธ', '๐ถ', '๐ฏ', '๐', '๐น', '๐', '๐ฒ', '๐', '๐ธ', '๐ด', '๐ณ', 'ใ๏ธ', 'ใ๏ธ', '๐บ', '๐ต', '๐ด',
          '๐ ', '๐ก', '๐ข', '๐ต', '๐ฃ', '๐ค', 'โซ', 'โช', '๐ฅ', '๐ง', '๐จ', '๐ฉ', '๐ฆ', '๐ช', '๐ซ', 'โฌ', 'โฌ', 'โผ๏ธ', 'โป๏ธ',
          'โพ',
          'โฝ', 'โช๏ธ', 'โซ๏ธ', '๐ถ', '๐ท', '๐ธ', '๐น', '๐บ', '๐ป', '๐ ', '๐', '๐ณ', '๐ฒ', '๐', '๐ฉ', '๐', '๐ด', '๐ณ๏ธ',
          '๐ณ๏ธ\u200d๐', '๐ณ๏ธ\u200dโง๏ธ', '๐ด\u200dโ ๏ธ', '๐ฆ๐จ', '๐ฆ๐ฉ', '๐ฆ๐ช', '๐ฆ๐ซ', '๐ฆ๐ฌ', '๐ฆ๐ฎ', '๐ฆ๐ฑ', '๐ฆ๐ฒ',
          '๐ฆ๐ด', '๐ฆ๐ถ', '๐ฆ๐ท', '๐ฆ๐ธ', '๐ฆ๐น', '๐ฆ๐บ', '๐ฆ๐ผ', '๐ฆ๐ฝ', '๐ฆ๐ฟ', '๐ง๐ฆ', '๐ง๐ง', '๐ง๐ฉ', '๐ง๐ช',
          '๐ง๐ซ',
          '๐ง๐ฌ', '๐ง๐ญ', '๐ง๐ฎ', '๐ง๐ฏ', '๐ง๐ฑ', '๐ง๐ฒ', '๐ง๐ณ', '๐ง๐ด', '๐ง๐ถ', '๐ง๐ท', '๐ง๐ธ', '๐ง๐น', '๐ง๐ป',
          '๐ง๐ผ',
          '๐ง๐พ', '๐ง๐ฟ', '๐จ๐ฆ', '๐จ๐จ', '๐จ๐ฉ', '๐จ๐ซ', '๐จ๐ฌ', '๐จ๐ญ', '๐จ๐ฎ', '๐จ๐ฐ', '๐จ๐ฑ', '๐จ๐ฒ', '๐จ๐ณ',
          '๐จ๐ด',
          '๐จ๐ต', '๐จ๐ท', '๐จ๐บ', '๐จ๐ป', '๐จ๐ผ', '๐จ๐ฝ', '๐จ๐พ', '๐จ๐ฟ', '๐ฉ๐ช', '๐ฉ๐ฌ', '๐ฉ๐ฏ', '๐ฉ๐ฐ', '๐ฉ๐ฒ',
          '๐ฉ๐ด',
          '๐ฉ๐ฟ', '๐ช๐ฆ', '๐ช๐จ', '๐ช๐ช', '๐ช๐ฌ', '๐ช๐ญ', '๐ช๐ท', '๐ช๐ธ', '๐ช๐น', '๐ช๐บ', '๐ช๐บ', '๐ซ๐ฎ', '๐ซ๐ฏ',
          '๐ซ๐ฐ',
          '๐ซ๐ฒ', '๐ซ๐ด', '๐ซ๐ท', '๐ฌ๐ฆ', '๐ฌ๐ง', '๐ฌ๐ง', '๐ฌ๐ฉ', '๐ฌ๐ช', '๐ฌ๐ซ', '๐ฌ๐ฌ', '๐ฌ๐ญ', '๐ฌ๐ฎ', '๐ฌ๐ฑ',
          '๐ฌ๐ฒ',
          '๐ฌ๐ณ', '๐ฌ๐ต', '๐ฌ๐ถ', '๐ฌ๐ท', '๐ฌ๐ธ', '๐ฌ๐น', '๐ฌ๐บ', '๐ฌ๐ผ', '๐ฌ๐พ', '๐ญ๐ฐ', '๐ญ๐ฒ', '๐ญ๐ณ', '๐ญ๐ท',
          '๐ญ๐น',
          '๐ญ๐บ', '๐ฎ๐จ', '๐ฎ๐ฉ', '๐ฎ๐ช', '๐ฎ๐ฑ', '๐ฎ๐ฒ', '๐ฎ๐ณ', '๐ฎ๐ด', '๐ฎ๐ถ', '๐ฎ๐ท', '๐ฎ๐ธ', '๐ฎ๐น', '๐ฏ๐ช',
          '๐ฏ๐ฒ',
          '๐ฏ๐ด', '๐ฏ๐ต', '๐ฐ๐ช', '๐ฐ๐ฌ', '๐ฐ๐ญ', '๐ฐ๐ฎ', '๐ฐ๐ฒ', '๐ฐ๐ณ', '๐ฐ๐ต', '๐ฐ๐ท', '๐ฐ๐ผ', '๐ฐ๐พ', '๐ฐ๐ฟ',
          '๐ฑ๐ฆ',
          '๐ฑ๐ง', '๐ฑ๐จ', '๐ฑ๐ฎ', '๐ฑ๐ฐ', '๐ฑ๐ท', '๐ฑ๐ธ', '๐ฑ๐น', '๐ฑ๐บ', '๐ฑ๐ป', '๐ฑ๐พ', '๐ฒ๐ฆ', '๐ฒ๐จ', '๐ฒ๐ฉ',
          '๐ฒ๐ช',
          '๐ฒ๐ซ', '๐ฒ๐ฌ', '๐ฒ๐ญ', '๐ฒ๐ฐ', '๐ฒ๐ฑ', '๐ฒ๐ฒ', '๐ฒ๐ณ', '๐ฒ๐ด', '๐ฒ๐ต', '๐ฒ๐ถ', '๐ฒ๐ท', '๐ฒ๐ธ', '๐ฒ๐น',
          '๐ฒ๐บ',
          '๐ฒ๐ป', '๐ฒ๐ผ', '๐ฒ๐ฝ', '๐ฒ๐พ', '๐ฒ๐ฟ', '๐ณ๐ฆ', '๐ณ๐จ', '๐ณ๐ช', '๐ณ๐ซ', '๐ณ๐ฌ', '๐ณ๐ฎ', '๐ณ๐ฑ', '๐ณ๐ด',
          '๐ณ๐ต',
          '๐ณ๐ท', '๐ณ๐บ', '๐ณ๐ฟ', '๐ด๐ฒ', '๐ต๐ฆ', '๐ต๐ช', '๐ต๐ซ', '๐ต๐ฌ', '๐ต๐ญ', '๐ต๐ฐ', '๐ต๐ฑ', '๐ต๐ฒ', '๐ต๐ณ',
          '๐ต๐ท',
          '๐ต๐ธ', '๐ต๐น', '๐ต๐ผ', '๐ต๐พ', '๐ถ๐ฆ', '๐ท๐ช', '๐ท๐ด', '๐ท๐ธ', '๐ท๐บ', '๐ท๐ผ', '๐ธ๐ฆ', '๐ธ๐ง', '๐ธ๐จ',
          '๐ธ๐ฉ',
          '๐ธ๐ช', '๐ธ๐ฌ', '๐ธ๐ญ', '๐ธ๐ฎ', '๐ธ๐ฏ', '๐ธ๐ฐ', '๐ธ๐ฑ', '๐ธ๐ฒ', '๐ธ๐ณ', '๐ธ๐ด', '๐ธ๐ท', '๐ธ๐ธ', '๐ธ๐น',
          '๐ธ๐ป',
          '๐ธ๐ฝ', '๐ธ๐พ', '๐ธ๐ฟ', '๐น๐ฆ', '๐น๐จ', '๐น๐ฉ', '๐น๐ซ', '๐น๐ฌ', '๐น๐ญ', '๐น๐ฏ', '๐น๐ฐ', '๐น๐ฑ', '๐น๐ฒ',
          '๐น๐ณ',
          '๐น๐ด', '๐น๐ท', '๐น๐น', '๐น๐ป', '๐น๐ผ', '๐น๐ฟ', '๐บ๐ฆ', '๐บ๐ฌ', '๐บ๐ฒ', '๐บ๐ณ', '๐บ๐ธ', '๐บ๐พ', '๐บ๐ฟ',
          '๐ป๐ฆ',
          '๐ป๐จ', '๐ป๐ช', '๐ป๐ฌ', '๐ป๐ฎ', '๐ป๐ณ', '๐ป๐บ', '๐ผ๐ซ', '๐ผ๐ธ', '๐ฝ๐ฐ', '๐พ๐ช', '๐พ๐น', '๐ฟ๐ฆ', '๐ฟ๐ฒ',
          '๐ฟ๐ผ',
          '๐ด\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f',
          '๐ด\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f',
          '๐ด\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f']


def return_tweet(emojie_lst):
    data = []
    for i, emo in enumerate(emojie_lst):
        try:
            tweets = []
            c = twint.Config()
            c.Images = True
            c.Search = emo
            c.Min_likes = 50000
            c.Store_object = True
            c.Store_object_tweets_list = tweets
            twint.run.Search(c)
            data.extend(tweets)
        except:
            print('The Error arise from index :{}\nRun the code again by changing return_tweet(search[{}:]) '.format(i,
                                                                                                                     i))
            break
        print("in progress...\nindex number -> {}".format(i))
    return data


Tweets = return_tweet(Emojie)
# creating a dataframe
df = pd.concat(
    [pd.Series(Tweets).apply(lambda x: x.username), pd.Series(Tweets).apply(lambda x: x.name)],
    axis=1)
df.columns = ['username', 'name']
# English only
df = df[pd.Series(Tweets).apply(lambda x: x.lang) == 'en'].reset_index()
df = df.drop('index', axis=1)
df = df.sample(frac=1).reset_index()
df = df.drop('index', axis=1)
# writing to an excel file
df.to_excel('twitter_Emojis.xlsx', sheet_name='sheet_1', index=False)
