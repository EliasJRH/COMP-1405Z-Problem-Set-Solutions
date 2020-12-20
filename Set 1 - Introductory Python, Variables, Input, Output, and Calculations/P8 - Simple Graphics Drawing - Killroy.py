from SimpleGraphics import *

setWidth(3)
#Middle line that Killroy is looking over
line(100,300,178,300)
line(256,300,386,300)
line(430,300,570,300)
line(646,300,700,300)
#Head
arc(300,175,225,250,180,-180)
#Nose curver
arc(386,325,45,65,0,-180)
#Eyes
ellipse(385,250,4,4)
ellipse(430,250,4,4)
#Nose lines
line(389,280,385,360)
line(429,280,432,360)
#left hand
arc(180,280,76,35,180,-180)
arc(180,260,20,70,180,180)
arc(200,260,18,75,180,180)
arc(218,260,18,73,180,180)
arc(236,260,20,70,180,180)
#right hand
arc(570,280,76,35,180,-180)
arc(570,260,20,70,180,180)
arc(590,260,18,75,180,180)
arc(608,260,18,73,180,180)
arc(626,260,20,70,180,180)
#text
text(550,170, "Killroy")
text(549,185,"Was")
text(550,200,"Here")