
# 0. Write the necessary code to display the following message to the console:
#        Time for co-co-co-ding.
#
# SCENARIO: Use an operator and f-string formatting to create this output
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

word_0 = "time"
word_1 = "for"
word_2 = "coding"
character_0 = " "
character_1 = "-"
character_2 = "."

special_word = (word_2[:2] + character_1) * 3
message = word_0 + character_0 + word_1 + character_0 + special_word + word_2[-4:] + character_2
