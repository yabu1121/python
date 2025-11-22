todo_list = []


def display_only(t_list):
  for index, item in enumerate(t_list):
      task_state = "✅" if item["done"] == True else "未"
      print(f"{index + 1} : {item["task"]} {task_state}")


def display_menu():
  print("\n TODO-APP")
  print("1: todoを追加")
  print("2: todoを表示")
  print("3: todoを完了")
  print("4: todoを削除")
  print("0: アプリを終了")
  print("-----------")


def add_todo(t_list):
  task = input("追加したいタスクを入力してください。\n")
  t_list.append({"task": task, "done": False})
  print("タスクを追加しました。")


def display_todo(t_list):
  if len(t_list) == 0:
    print("taskがありません")
  else:
    display_only(t_list)
    print("todoリストを出力しました。")


def complete_todo(t_list):
  if not t_list:
    print("完了できるタスクがありません。")
    return
  
  display_only(t_list)

  try:
    complete_number_index = int(input("何番が終わりましたか？\n"))
    complete_number_index = complete_number_index - 1
    if t_list[complete_number_index]["done"] == False:
      t_list[complete_number_index]["done"] = True
    else:
      print("すでに完了しています\n")
  except ValueError:
    print("無効な入力:番号を数字で入力してください")


def delete_todo(t_list):
  display_only(t_list)
  print("どのタスクを削除しますか\n")
  delete_task_index = int(input("番号で教えてください。"))
  delete_task_index = delete_task_index - 1
  print(f"{t_list[delete_task_index]["task"]}を削除しました。")
  t_list.pop(delete_task_index)


def end_todo():
  print("todoアプリを終了します。")


def main():
  global todo_list
  while(True):
    display_menu()
    user_choice = input("0-4で選択してください\n")
    if user_choice == '1':
      add_todo(todo_list)
    elif user_choice == '2':
      display_todo(todo_list)
    elif user_choice == '3':
      complete_todo(todo_list)
    elif user_choice == '4':
      delete_todo(todo_list)
    elif user_choice == '0':
      end_todo()
      break
    else:
      print("無効な入力です。終了したい場合は0を入力してください。") 


if __name__ == "__main__":
    main()