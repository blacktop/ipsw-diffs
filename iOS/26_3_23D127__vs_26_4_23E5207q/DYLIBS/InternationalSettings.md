## InternationalSettings

> `/System/Library/AccessibilityBundles/InternationalSettings.axbundle/InternationalSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x984
+3005.16.0.0.0
+  __TEXT.__text: 0xa0c
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0xe4
   __TEXT.__cstring: 0x1cd

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86E072C9-6179-31E2-BBF3-5870B715B403
+  UUID: B6329831-49B4-3D13-81AF-7535F5B70FAA
   Functions: 21
   Symbols:   160
   CStrings:  89
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ ___60+[AXInternationalSettingsGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___60+[AXInternationalSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___60+[AXInternationalSettingsGlue accessibilityInitializeBundle]_block_invoke_4 : 112 -> 120
~ +[ISInternationalViewControllerAccessibility _accessibilityPerformValidations:] : 176 -> 188
~ -[ISInternationalViewControllerAccessibility updateCell:forPreferredLanguageAtIndex:] : 284 -> 300
~ -[ISInternationalViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 564 -> 572
~ ___78-[ISInternationalViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke : 116 -> 124
~ -[ISLanguageViewControllerAccessibility tableView:cellForRowAtIndexPath:] : 216 -> 240
~ -[RegionFormatSampleViewAccessibility setTextForRegionExample:] : 516 -> 568

```
