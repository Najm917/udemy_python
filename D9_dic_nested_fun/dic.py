programing_dict={
  "function":"a function is methoth that is create a particular task and want to use many time using function name",
  "bug":"bug is part of programing this is show where is error"
}

# print(programing_dict["bug"])

# all key access through loop

for key in programing_dict:
  print(key)
  
# nested dic

countrys_state={
  "India":
    ["Bihar","Up","Jharkhand","West-Bangal"],
  "USA":
    ["New York","California","Texas"],
  "UK":
    ["London","Manchester","Liverpool"]
  }

print(countrys_state["India"][0:2])

nest_list=["a","b",["c","d"]]
print(nest_list[2][0])


travel_vlog={
  "India":{
    "cities":["Bihar","Up","Jharkhand","West-Bangal"],
    "total_visits":10
  },
  "USA":{
    "cities":["New York","California","Texas"],
    "total_visits":5
  },
  "UK":{
    "cities":["London","Manchester","Liverpool"],
    "total_visits":3
  }
}

print(travel_vlog["USA"]["cities"][0])