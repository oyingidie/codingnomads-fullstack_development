# 0. Which of the following strings is the longest?
#       - longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
#       - longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
#       - longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
#       - strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
#
# 1. Use the len() function to find out.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

# is the longest string in German?
if len(longest_german_word) > len(longest_hungarian_word) \
and len(longest_german_word) > len(longest_finnish_word) \
and len(longest_german_word) > len(strong_password):
    print("The longest string is in German with", len(longest_german_word), "characters.")

# is the longest string in Hungarian?
elif len(longest_hungarian_word) > len(longest_german_word) \
and len(longest_hungarian_word) > len(longest_finnish_word) \
and len(longest_hungarian_word) > len(strong_password):
    print("The longest string is in Hungarian with", len(longest_hungarian_word), "characters.")

# is the longest string in Finnish?
elif len(longest_finnish_word) > len(longest_german_word) \
and len(longest_finnish_word) > len(longest_hungarian_word) \
and len(longest_finnish_word) > len(strong_password):
    print("The longest string is in Finnish with", len(longest_finnish_word), "characters.")

# is the longest string the password?
else:
    print("The longest string is the strong password with", len(strong_password), "characters.")
