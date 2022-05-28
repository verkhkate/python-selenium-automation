Feature: WINDOWS HANDLING

Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon Terms & Conditions page
 When Store original window
 And Click on Amazon Privacy Notice link
 And Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And Close Amazon Privacy Notice window
 And Return to Amazon Terms & Conditions window
