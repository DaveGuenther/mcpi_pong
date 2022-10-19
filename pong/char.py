
class Char:
    
    data={'1':
          [
              [9,1,1,9,9],
              [1,9,1,9,9],
              [9,9,1,9,9],
              [9,9,1,9,9],
              [9,9,1,9,9],
              [9,9,1,9,9],
              [9,9,1,9,9],
              [9,9,1,9,9],
              [1,1,1,1,1]
          ],
          '2':
          [
              [9,1,1,1,9],
              [1,9,9,9,1],
              [9,9,9,9,1],
              [9,9,9,9,1],
              [9,9,9,1,9],
              [9,9,1,9,9],
              [9,1,9,9,9],
              [1,9,9,9,9],
              [1,9,9,9,9],
              [1,1,9,9,9]
          ],
          '3':
          [
              [9,1,1,1,9],
              [1,9,9,9,1],
              [9,9,9,9,1],
              [9,9,9,9,1],
              [9,9,1,1,9],
              [9,9,9,1,9],
              [9,9,9,9,1],
              [9,9,9,9,1],
              [1,9,9,9,1],
              [9,1,1,1,9]
          ]
         }
       
    
    def put_char(character, x=4, y=10, transparent=False):
        """
        
        :param character: (single character string)  This is the character that will be printed on the screen
        :param x: (int) This is the x position on the display for the top left corner of the character
        :param y: (int) this is the y position on the display for the top left corner of the character
        
        """
        #:param center(x, y):  (tuple) This is the screen coordinates of the center of the character to be displayed
        #:param scale=1: (float) 1 is unity scale.  <1 is smaller and >1 is bigger
        #:param rot: (float) degrees to rotate CCW
    
        
        char_array = self.data[character]
        
        