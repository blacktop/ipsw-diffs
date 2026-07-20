## SpringBoard

> `FileSystem/System/Library/AccessibilityBundles/SpringBoard.axbundle/Accessibility.loctable`

```diff

 en.page.management.showing = "Homescreen Page Hiding"
 en.parallax.effect.button.for.wallpaper = "Parallax Effect"
 en.passcode.entry = "Passcode field"
-en.passcode.values.entered = "%1$d of %2$d entered"
+en.passcode.values.entered.NSStringLocalizedFormatKey = "%#@valuesentered1@ of %#@valuesentered2@"
+en.passcode.values.entered.valuesentered1.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.passcode.values.entered.valuesentered1.NSStringFormatValueTypeKey = "d"
+en.passcode.values.entered.valuesentered1.one = "%d"
+en.passcode.values.entered.valuesentered1.other = "%d"
+en.passcode.values.entered.valuesentered2.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.passcode.values.entered.valuesentered2.NSStringFormatValueTypeKey = "d"
+en.passcode.values.entered.valuesentered2.one = "%d value entered"
+en.passcode.values.entered.valuesentered2.other = "%d values entered"
 en.pause.button = "Pause"
 en.people.picker.hint = "Double-tap to communicate with %@. Buttons will appear to the right."
 en.people.picker.items.collapsed = "Contact buttons hidden"

```
