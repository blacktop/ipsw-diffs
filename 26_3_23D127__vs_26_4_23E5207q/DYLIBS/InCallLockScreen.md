## InCallLockScreen

> `/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x410
+3005.16.0.0.0
+  __TEXT.__text: 0x434
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__cstring: 0x1b4

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D7C501C-61FE-3C64-94F4-E451C84F464D
+  UUID: 61277813-8850-3CBE-9410-02A886196708
   Functions: 13
   Symbols:   86
   CStrings:  68
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXInCallLockScreenGlue accessibilityInitializeBundle] : 100 -> 104
~ ___55+[AXInCallLockScreenGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ +[PHCallParticipantsViewAccessibility _accessibilityPerformValidations:] : 308 -> 316
~ -[PHCallParticipantsViewAccessibility updateParticipantsAnimated:] : 280 -> 292
~ -[PHCallParticipantsViewAccessibility isAccessibilityElement] : 104 -> 108
~ -[PHCallParticipantsViewAccessibility _accessibilityIsDisplayedInBanner] : 76 -> 80

```
