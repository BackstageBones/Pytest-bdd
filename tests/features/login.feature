# Created by amien at 12/02/2025
Feature: Automation practice login
  # Enter feature description here

  Scenario: Login to shop
    Given User opens automationpractice website
    When User chooses to login
    And User fills login fields with users <user> credentials
    And Clicks sign in button
    Then User is logged in