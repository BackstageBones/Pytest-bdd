# Created by amien at 12/02/2025
Feature: Automation practice product sorting
  # Enter feature description here
  Background:
    Given User opens automation practice website
    When User searches for dress in product search bar
    And product results are displayed
    And User sorts displayed results by in stock param


  Scenario: Search for items and sort them
    Then Products are sorted by in stock param

  Scenario: Test shopping
    Then User is able to add product to basket
    And User can proceed with product to checkout