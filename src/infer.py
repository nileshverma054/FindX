from evaluate import infer
from create_hist import Embeddings
import cv2
import time

depth = 15
d_type = 'd1'
q_img = "database/images/3159.jpg"

if __name__ == '__main__':
  obj = Embeddings()
  q_hist = obj.make_hist(q_img)
  i_img = cv2.imread(q_img)
  cv2.imshow('Query',i_img)
  results = infer(q_hist, depth=depth, d_type=d_type)
  
  for index,result in enumerate(results):
    print(index,result['img'],result['dis'])
    r = cv2.imread(result['img'])
    cv2.imshow("Results",r)
    cv2.waitKey(0)

