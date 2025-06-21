from django.db import models

# Create your models here.
# chat model
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    volunteer_id = models.ForeignKey('volunteers.Volunteer', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField( default=False)
    def __str__(self):
        return f"Chat {self.chat_id}"

# chat message model
class ChatMessage(models.Model):
    ChatMessage_id = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    sender_id = models.PositiveIntegerField()
    message_text = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    def __str__(self):
        return f" ChatMessage{self.ChatMessage_id}"
