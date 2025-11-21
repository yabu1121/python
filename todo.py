todo_list = []

def display_menu():
  print("\n TODO-APP")
  print("1: todoを追加")
  print("2: todoを表示")
  print("3: todoを完了")
  print("4: todoを削除")
  print("0: アプリを終了")
  print("-----------")

def add_todo():
  print("add")
  choice()

def display_todo():
  print("display")
  choice()

def complete_todo():
  print("complete")
  choice()
  
def delete_todo():
  print("delete")
  choice()

def end_todo():
  print("end")
  choice()

def choice():
  choice = input("0-4で選択してください")
  if choice == '1':
    add_todo()
  elif choice == '2':
    display_todo()
  elif choice == '3':
    complete_todo()
  elif choice == '4':
    delete_todo()
  elif choice == '0':
    end_todo()
  else:
    print("無効な入力です。終了したい場合は0を入力してください。")
    choice() 


def main():
  display_menu()
  choice()

if __name__ == "__main__":
    main()