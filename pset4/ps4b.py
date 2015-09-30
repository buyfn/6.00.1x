from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None

    # For each word in the wordList
    for word in wordList:
        #print word

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            wordScore = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if wordScore > bestScore:

                # Update your best score, and best word accordingly
                bestScore = wordScore
                bestWord = word


    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0

    while calculateHandlen(hand) > 0:
        print "\nCurrent hand: ",
        displayHand(hand)

        computerWord = compChooseWord(hand, wordList, n)
        if computerWord is None:
          break
        else:
          wordScore = getWordScore(computerWord, n)
          totalScore += wordScore

          print "'" + computerWord + "'" + " earned " + str(wordScore) + " points. Total: " + str(totalScore) + " points."
          hand = updateHand(hand, computerWord)

    print "Total score: " + str(totalScore) + " points."

    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    def playPlayersHand(hand, player):
      if player == "c":
        return compPlayHand(hand, wordList, HAND_SIZE)
      else:
        return playHand(hand, wordList, HAND_SIZE)

    lastHand = {}

    # while game goes on:
    while True:
      handSelection = ""
      playerSelection = ""

      # get input from user to deal new hand, play previous hand or exit game
      handSelection = raw_input("\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ")
      # if "n":
      if handSelection == "n":
        # deal new hand
        lastHand = dealHand(HAND_SIZE)
        # ask user to choose player
        while playerSelection not in ["u", "c"]:
          playerSelection = raw_input("\nEnter u to have yourself play, c to have the computer play: ")
          if playerSelection not in ["u", "c"]:
            print "Invalid input"
        # playPlayersHand
        playPlayersHand(lastHand, playerSelection)

      # if "r":
      elif handSelection == "r":
        # if it's not first game:
        if len(lastHand) != 0:
          # ask user to choose player
          while playerSelection not in ["u", "c"]:
            playerSelection = raw_input("\nEnter u to have yourself play, c to have the computer play: ")
            if playerSelection not in ["u", "c"]:
              print "Invalid input"
          # playPlayersHand
          playPlayersHand(lastHand, playerSelection)
        else:
          print "You have not played a hand yet."

      elif handSelection == "e":
        break

      else:
        print "Invalid input"

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #compPlayHand(testHands[3], wordList, HAND_SIZE)
    playGame(wordList)


