
 pallet_id = []
 pallet_count = 0

 getpr = "BNT-007"
 pallet_present = True
 partinstation = True

 def check_pallet_in_db():
     global pallet_count  # Declare pallet_count as global to modify it within the function
     if partinstation and getpr not in pallet_id:
         pallet_id.append(getpr)
         pallet_count += 1
         return "Pallet registered."

     elif partinstation and getpr in pallet_id:
         return "Pallet already in the database."

 if partinstation:
     result = check_pallet_in_db()
     print(result)
     print(f"Total pallets on the line: {pallet_count}")





