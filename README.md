# psp-website
This is the repository for the code that will run on an AWS instance for my local chapter of Phi Sigma Pi.

## Changelog

### Version 1

Version 1 is live at (http://pspvt.com), and the following features were implemented.
 - Homepage including a calendar & announcements list
 - Calendar view with just the calendar
 - Events on the calendar that can be clicked to view that event's page
 - Announcements view with all announcements sorted from most recent to oldest
 - Events view, which shows all events sorted from furthest in the future to oldest in the past
 - Admin view which logs admin users in
 - 6 admin controls
   - Create Event
   - Edit Event
   - Create Announcement
   - Edit Announcement
   - Create User
   - Edit User
- Also implemented an admin user logout action in order to test views between admin and non-admin users.

#### Features to Come
 - Attendance Manager for events
 - Points Manager for events
 - Better UI (particularly for admin controls)
 - Social Media Links
 - Support for several devices (i.e., Mac, iPad, mobile, etc.)

---

## About
This website requires the following functionality to meet the fraternity's needs.
1. Frat Calendar
2. Upcoming Events Board
3. Social Media links
4. Page for each event on the calendar.
5. Ability to mark attendance (before and after)
6. Announcements
7. Unified points tracking
8. Login Capability
9. Polls (Marissa's request)

## Breakdown

Content will be organized into **events**; each event will have its own page accessible via a URL.
Each event will include a time, location, short description, and attendance. An event page can include whatever content the event creator wants. Any admin user can edit an event's page. There is no ownership of content created on this website.
Events will support the Markdown language for formatting text.


Attendance before an event happens will be an area for brothers to mark if they are coming, potentially coming, or not coming.
Attendance after an event will allow admins (exec & others) to mark who attended. 

The Calendar will be on the home page and will resemble a smaller version of the canvas calendar. Events will be scheduled on their specific days and will have their time listed alongside the event name for easy viewing. 
When events are created, they will be automatically added to the calendar.
Clicking an event's label in the calendar opens a small pop-up with key details about the event.

The Events board will be similar to the calendar but will just be a list of events in chronological order. The calendar can occasionally be hard to read, but it will look similar to the "Agenda" view on Canvas.

The Announcements section will display recent announcements compiled by admins. There will be a page for Admins to send announcements.

