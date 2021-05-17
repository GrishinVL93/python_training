Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <address> , <lastname> , <company> , <homephone> , <mobilephone> , <workphone> , <secondaryphone> , <email> , <email2> , <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added new contact

  Examples:
  | firstname | middlename | address | lastname | company | homephone | mobilephone | workphone | secondaryphone | email       | email2     | email3     |
  | FN1       | MN1        | Ad1     | LN1      | Comp1   | 834329403 | 38437239    | 324348    | 3248283        | fdsf@mds.ru | sf@mds.ru  | fd@mds.ru  |
  | FN2       | MN2        | Ad2     | LN2      | Cm2     | 234848    | 759944      | 2344324   | 2433444        | fddAAmds.ru | dsf3@jd.ri | sdfsdf@m.r |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <middlename>, <address> , <lastname> , <company> , <homephone> , <mobilephone> , <workphone> , <secondaryphone> , <email> , <email2> , <email3>
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list with the modified contact

  Examples:
  | firstname | middlename | address | lastname | company | homephone | mobilephone | workphone | secondaryphone | email  | email2  | email3  |
  | UpdFN     | UpdMN      | UpdAd   | UpdLN    | UpdCom  | UpdHP     | UpdMP       | UpdWP     | UpdSP          | UpdEm1 | UpdEm2  | UpdEm3  |
