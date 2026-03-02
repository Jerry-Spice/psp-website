import calendar
import datetime
import markdown
from flask import Flask, redirect, render_template, request, session, Blueprint, current_app
from html_to_markdown import convert

from DataTypes.Announcement import Announcement
from DataTypes.Event import Event

from Managers.ConfigManager import ConfigManager