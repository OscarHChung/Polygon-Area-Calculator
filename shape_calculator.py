class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, wid):
    self.width = wid
  
  def set_height(self, h):
    self.height = h
  
  def get_area(self):
    return (self.width * self.height)
  
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = "Too big for picture."
    if (self.width > 50) or (self.height > 50):
      return "Too big for picture."
    else:
      picture = self.height * ((self.width * "*") + "\n")
    
    return picture
  
  def get_amount_inside(self, shape):
    if (shape.width > self.width) or (shape.height > self.height):
      return 0
    else:
      return int(self.width / shape.width) * int(self.height / shape.height)


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)
  
  def __repr__(self):
    return f"Square(side={self.width})"
  
  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side
  
  def set_height(self, new_side):
    self.set_side(new_side)

  def set_width(self, new_side):
    self.set_side(new_side)
