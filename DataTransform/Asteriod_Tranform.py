# Normalize dates and times to a consistent format.
# Create time-based aggregations, such as the number of asteroids close to Earth per month.


#Create a function which can help time zone to IST
# I can take three parameter 1 is d--ate second and third will be from TZ to to TZ


from DataIngestion import Asteriod_Ingestion
#for now i am importing the JSON result but going forward it need to get from database
import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, '/home/mayank/Desktop/Project/DE/NASA/DataIngestion')

result = Asteriod_Ingestion.asteroid()

# res = result['near_earth_objects']
# r = (res["2023-12-01"])
# print(r[0]['name'])

try:
    near_earth_objects = result['near_earth_objects']
    count = 0

    # Iterate over each object in the list
    for day in near_earth_objects:
        # 'day' may contain additional information, so iterate over the objects for each day
        for obj in near_earth_objects[day]:
            # Access the 'name' field within each object
            name = obj.get('name', False)  # Use get() to handle the case where 'name' is not present
            close_approach_data = obj.get('close_approach_data')

            # Uncomment the lines below if you want to access the 'close_approach_date'
            # close_approach_date = close_approach_data[0].get('close_approach_date') if close_approach_data else None
            # print("Close Approach Date:", close_approach_date)

            count += 1
            # Print the name
            # print("Name:", name)
            # for x in close_approach_data:
            #     print(x.get('close_approach_date'))

    print("Total Count:", count)

except KeyError as e:
    print(f"KeyError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



# for obj in res:
#     for x in obj:
#         print(x)