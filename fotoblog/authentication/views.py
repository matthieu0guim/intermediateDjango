from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.views.generic import View
from . import forms

