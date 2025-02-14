# Created by amien at 12/02/2025
Feature: Shopping flow feature

  Background:
    Given User opens automation practice website
    And User chooses to sign in
    And User fills login fields with users REGISTERED_USER credentials
    And Clicks sign in button
    And User is logged in

  Scenario: Test shopping
    When User searches for dress in product search bar
    And product results are displayed
    And User sorts displayed results by in stock param
    And User is able to add product to basket
    And User can proceed with product to checkout
    And User proceeds to checkout on address page
    And Ticks terms of service checkbox
    And User goes to payment page with proceed to checkout button
    Then User is able to finalise shopping with bank wire payment
    And Order complete success message is displayed