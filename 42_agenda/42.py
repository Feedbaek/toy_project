# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    42.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: minskim2 <minskim2@student.42seoul.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/26 17:30:03 by minskim2          #+#    #+#              #
#    Updated: 2021/09/26 19:48:58 by minskim2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyautogui
import time

while 1:
	pyautogui.click(x=600,y=400)
	time.sleep(0.1)
	pyautogui.doubleClick(x=650,y=450)
	time.sleep(0.1)
