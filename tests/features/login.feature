# Created by amien at 12/02/2025
Feature: Automation practice login
  # Enter feature description here

  Scenario: Login to shop
    Given User opens automation practice website
    When User chooses to sign in
    And User fills login fields with users REGISTERED_USER credentials
    And Clicks sign in button
    Then User is logged in