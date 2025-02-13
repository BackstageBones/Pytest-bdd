# Created by amien at 12/02/2025
Feature: Automation practice user registration

  Scenario: Register new user
    Given User opens automation practice website
    When User chooses to sign in
    And Selects option to register as new user by filling e-mail field with user REGISTRATION_USER data
    And User fills registration form with personal data
    Then User is successfully registered