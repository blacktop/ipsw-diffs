## ActivitySharing

> `/System/Library/AccessibilityBundles/ActivitySharing.axbundle/ActivitySharing`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x434
-  __TEXT.__auth_stubs: 0xf0
+1001.12.0.0.0
+  __TEXT.__text: 0x454
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x70
   __TEXT.__objc_classname: 0x57

   __TEXT.__objc_methname: 0x2f4
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__auth_got: 0x70
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x120

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2007D259-26E8-38B5-9A02-B7F61E73FBA7
+  UUID: AC53E977-AD01-3977-80D2-89699D196DAB
   Functions: 13
-  Symbols:   78
+  Symbols:   76
   CStrings:  53
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[ASFriendAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[ASFriendAccessibility _accessibilityLoadAccessibilityInformation] : 340 -> 348
~ ___54+[AXActivitySharingGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___54+[AXActivitySharingGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ _accessibilityLocalizedString : 160 -> 168

```
