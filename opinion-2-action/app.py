# Take feedbacks from users and generate action to address them

import csv
from os import write
from openai import OpenAI

def generate_executive_summary(feedbacks):
  """
  Generates an executive summary based on user feedback about an event.

  Args:
    feedbacks (list): A list of users' feedback about the event.

  Returns:
    str: The generated executive summary.

  Raises:
    Exception: If an error occurs during the generation process.
  """
  client = OpenAI()

  messages = [
    {
      "role": "system",
      "content": "You are a world class opinion analyser bot that can analyse a users opinion and can generate actions from it.\n\nYou are given a list of users and their opinions about an event.\n\nGenerate an executive summary that contains a report of users based on whether they felt good, okay or bad about the event and generate actions to address the concerns from users. Also include the overall percentage of users who gave the different feedback about the event and generate a pulse of how the users felt about the event and highlight the best and worst feedback."
    },
    {
      "role": "user",
      "content": feedbacks
    },
  ]

  try:
    completion = client.chat.completions.create(model="gpt-4", messages=messages)

    return completion.choices[0].message.content
  except Exception as e:
    print(f"An error occurred: {e}")
    return None


def get_formatted_feedbacks(file_path):
  """
  Reads a CSV file containing user feedbacks and returns formatted feedbacks.

  Args:
    file_path (str): The path to the CSV file.

  Returns:
    str: The formatted feedbacks.

  """
  feedbacks = ''
  lines = 0

  with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # ignore the header
    next(csvreader)

    # Read and print each row of the CSV
    for row in csvreader:
      lines += 1
      feedbacks += row[0] + ': ' + row[1] + '\n'

  print(f"Read {lines} feedbacks from {file_path}.")

  return feedbacks


def write_summary(summary):
  """
  Writes the generated summary to a text file.

  Args:
    summary (str): The generated summary.

  """
  with open('opinion-2-action/output/summary.txt', 'w') as f:
    f.write(summary)
    f.close()


def main():
  """
  This is the main function that is invoked when the program is called.
  """
  input_file = 'opinion-2-action/input/opinions.csv'
  print(f"Reading opinions from {input_file}...")
  feedbacks = get_formatted_feedbacks(input_file)

  print("Generating executive summary using Open AI...")
  summary = generate_executive_summary(feedbacks)
  print('Summary Generated.')

  print("Writing summary to opinion-2-action/output/summary.txt...")
  write_summary(summary)

  print("Done.")


if __name__ == "__main__":
  main()
