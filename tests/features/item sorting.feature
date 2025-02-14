# Created by amien at 14/02/2025
Feature: Automation practice items sorting

  Scenario: Sorting items
    Given User opens automation practice website
    And User searches for dress in product search bar
    And product results are displayed
    When User sorts displayed results by in stock param
    Then Products are sorted by in stock param