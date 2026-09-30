## AppleAccountSettings

> `/System/Library/AccessibilityBundles/AppleAccountSettings.axbundle/AppleAccountSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x7b8
-  __TEXT.__auth_stubs: 0x1d0
+3005.16.0.0.0
+  __TEXT.__text: 0x7bc
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0xb8
   __TEXT.__cstring: 0x2bd
   __TEXT.__unwind_info: 0x98

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C87738A-798B-366F-AF13-0D8D90BF590C
+  UUID: ACCF7C3F-A54F-34B0-BEEE-6EACA6C1F26A
   Functions: 19
-  Symbols:   131
+  Symbols:   126
   CStrings:  75
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x6
- _objc_retain_x7
Functions:
~ _accessibilityLocalizedString : 156 -> 164
~ ___59+[AXAppleAccountSettingsGlue accessibilityInitializeBundle]_block_invoke : 104 -> 108
~ ___59+[AXAppleAccountSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___59+[AXAppleAccountSettingsGlue accessibilityInitializeBundle]_block_invoke_5 : 92 -> 100
~ +[AAUIAppleAccountHeaderViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[AAUIAppleAccountHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 308
~ +[AAUserNotificationAccessibility _accessibilityPerformValidations:] : 216 -> 224
~ +[AAUserNotificationAccessibility showUserNotificationWithTitle:message:cancelButtonTitle:otherButtonTitle:withCompletionBlock:] : 212 -> 196
~ +[AAUserNotificationAccessibility showUserNotificationWithTitle:message:textFieldTitle:cancelButtonTitle:otherButtonTitle:completion:] : 232 -> 212
~ +[AAUserNotificationAccessibility showUserNotificationWithTitle:message:secureTextFieldTitle:cancelButtonTitle:otherButtonTitle:completion:] : 232 -> 212

```
