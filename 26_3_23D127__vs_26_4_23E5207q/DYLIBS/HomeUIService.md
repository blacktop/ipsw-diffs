## HomeUIService

> `/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xd04
-  __TEXT.__auth_stubs: 0x160
+3005.16.0.0.0
+  __TEXT.__text: 0xd84
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__cstring: 0x301
   __TEXT.__unwind_info: 0xb8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B371548B-873C-3011-8681-1D4E2A2E8E62
+  UUID: 5A9EBBC4-0D52-3614-97E4-23A3E820F3D8
   Functions: 34
-  Symbols:   196
+  Symbols:   194
   CStrings:  133
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ -[HSPCDetectedViewControllerAccessibility viewWillAppear:] : 168 -> 176
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___52+[AXHomeUIServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 132 -> 140
~ _accessibilityLocalizedString : 148 -> 156
~ +[HSPCCameraScanViewControllerAccessibility _accessibilityPerformValidations:] : 268 -> 276
~ -[HSPCCameraScanViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 272 -> 296
~ -[HSPCCameraScanViewControllerAccessibility _handleSetupCode:] : 172 -> 180
~ +[HSPCPasscodeEntryViewAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[HSPCPasscodeEntryViewAccessibility accessibilityTraits] : 188 -> 192
~ -[HSPCPasscodeEntryViewAccessibility accessibilityValue] : 240 -> 248
~ -[HSPCPasscodeEntryViewAccessibility insertText:] : 340 -> 352
~ ___49-[HSPCPasscodeEntryViewAccessibility insertText:]_block_invoke : 100 -> 104
~ -[HSPCPasscodeEntryViewAccessibility deleteBackward] : 188 -> 196
~ +[HSSetupTroubleshootingTipCellAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[HSSetupTroubleshootingTipCellAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108

```
