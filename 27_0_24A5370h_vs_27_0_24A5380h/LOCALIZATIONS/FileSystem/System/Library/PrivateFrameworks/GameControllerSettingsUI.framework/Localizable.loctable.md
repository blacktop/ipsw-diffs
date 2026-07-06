## GameControllerSettingsUI

> `FileSystem/System/Library/PrivateFrameworks/GameControllerSettingsUI.framework/Localizable.loctable`

```diff

 en.CONTROLLER_FORGET_CONFIRMATION_DESCRIPTION = "Are you sure you want to erase settings for this controller? Your profiles will not be erased."
 en.CONTROLLER_FORGET_ELLIPSIS = "Erase Controller Settings…"
 en.CONTROLLER_HOME_BUTTON_ACTION_TITLE = "Press Home Button to Open"
-en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT = "%@ apps"
+en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT.NSStringLocalizedFormatKey = "%#@apps@"
+en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT.apps.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT.apps.NSStringFormatValueTypeKey = "d"
+en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT.apps.one = "1 app"
+en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_COUNT.apps.other = "%d apps"
 en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_DISCLAIMER = "Home button overrides allow apps to respond to home button presses, while preventing the home button from opening the Game Overlay or Games."
 en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_EDIT = "Edit…"
 en.CONTROLLER_HOME_BUTTON_EXEMPTIONS_EMPTY = "No Home Button Overrides"

```
