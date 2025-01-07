available_items=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_items=['mushrooms','french fries','extra cheese']
for requested_item in requested_items:
    if requested_item in available_items:
        print(f"Adding {requested_item}.")
    else:   #   MULTIPLE LISTS
        print(f"Sorry,we don't have {requested_item}.")    
print("\nFinished making my pizza!")        