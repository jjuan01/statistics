data = []

def get_data(singleData):
  data.append(singleData)
  print(data)


if __name__ == '__main__':

  print("sample data")
  singleData = input()
  get_data(singleData)