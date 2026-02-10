class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        freq = {}
        for i in range(len(hand)):
            if hand[i] in freq:
                freq[hand[i]] += 1
            else:
                freq[hand[i]] = 1
        
        hand.sort()

        for card in hand:
            if freq[card] == 0:
                continue

            for next_card in range(card, card + groupSize):
                if freq.get(next_card, 0) == 0:
                    return False
                freq[next_card] -= 1
                
            
        return True
        


        