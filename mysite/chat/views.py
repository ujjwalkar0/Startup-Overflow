from django.shortcuts import render
from rest_framework import APIView
from chat.models import *
from django.contrib.auth.models import User

class MessagesView(APIView):
	def create_group(self, request, group_name, owner):
		gr = GroupName.objects.create(
			name=group_name,
			owner=User.objects.filter(username=request.user)
		)
		for i in request.data["members"]:
			gr.member.set(i)
	
	def rename_group(self, request, group_id, group_name):
		gr = GroupName.objects.get(id=group_id)
		gr.name = group_name
	
	def delete_group(self,request, group_id):
		gr = GroupName.objects.get(id=group_id)
		gr.delete()
	
	def send_msg(self, request):
		pass