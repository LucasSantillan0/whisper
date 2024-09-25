
from config.BootstrapApp import bootstrapApplication
from tasks.Conversation import runConversation


if __name__ == "__main__":
  bootstrapApplication(tasks=[runConversation])