Feature: Testing tax computation

Scenario Outline: Calculate the tax amount for 2020-21
   Given a <salary>
    when I calculate tax
    then it should get the tax as <tax>

 Examples: Consumer Electronics
   | salary | tax |
   | 2000000 | 325000   |
