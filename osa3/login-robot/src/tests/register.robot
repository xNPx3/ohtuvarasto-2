*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  uusi  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  Username must be unique

Register With Too Short Username And Valid Password
    Input Credentials  k  salasana123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle 123  salasana123
    Output Should Contain  Username must consist only of characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  uusi  sala
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  uusi  salasana
    Output Should Contain  Password must not consist only of letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command