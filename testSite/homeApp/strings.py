# -*- coding: utf-8 -*-
#strings variables
hebrew = "he"
english = "en"

#translation variables
hebrewHome = "בית"
englishHome = "home"

# context variables
home = "home"
enNavBarCon = {
    home : englishHome
}
heNavBarCon = {
    home : hebrewHome
}


def navbarStrings(language):
    if(language == english):
        return enNavBarCon
    if(language == hebrew):
        return heNavBarCon
    return enNavBarCon