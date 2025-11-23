#import convertors
#print(f"convertors.kg_to_lbs(10): {convertors.kg_to_lbs(10)}")

from modules.convertors import kg_to_lbs
from ecommerce.shipping import calc_shipping

print(f"kg_to_lbs(10): {kg_to_lbs(10)}")
calc_shipping()
