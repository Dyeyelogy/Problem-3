while True:
    con_name = input("\nConsumer Name: ")
    con_id = input("Consumer ID: ")
    con_cat = input("Consumer Category (Residential/Commercial): ")
    con_add = input("Consumer Address: ")
    pres_read = float(input("Present Reading: "))
    prev_read = float(input("Previous Reading: "))
    car = float(input("Current Amount Rate: "))
    duedate = str(input("Due Date: "))

    cmu = pres_read - prev_read
    amountdue = cmu * car
    ocr = amountdue * 0.23
    oc = cmu * ocr
    netbill = amountdue + oc

    print("\nConsumer Name: ", con_name)
    print("Consumer ID: ", con_id)
    print("Consumer Category: ", con_cat)
    print("Consumer Address: ", con_add)
    print("CMU: ", cmu)
    print("Net Bill: ", netbill)
    print("Other Charges: ", oc)
    print("Amount Due: ", amountdue)
    repeat = input("Do you want to repeat the transaction? (yes/no): ")
    if repeat == "no":
        break
    elif repeat == "yes":
        continue
