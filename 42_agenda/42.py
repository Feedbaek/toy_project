# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    42.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: minskim2 <minskim2@student.42seoul.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/26 17:30:03 by minskim2          #+#    #+#              #
#    Updated: 2021/09/27 22:28:47 by minskim2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyautogui
import keyboard
import time

while 1:
		position = pyautogui.position()
		if keyboard.is_pressed('enter'):
				print(position)
				time.sleep(0.2)
