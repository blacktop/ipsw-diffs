## SIMSetupUIService

> `/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5e4
-  __TEXT.__auth_stubs: 0x110
+3005.16.0.0.0
+  __TEXT.__text: 0x618
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0xdc
   __TEXT.__cstring: 0x16b
   __TEXT.__unwind_info: 0x90

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x90
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C58F50D-D679-3BC8-B515-777FD874FDC4
+  UUID: A10E5262-0407-384A-ADC1-282B171421F0
   Functions: 18
-  Symbols:   113
+  Symbols:   111
   CStrings:  70
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXSIMSetupUIServiceGlue accessibilityInitializeBundle] : 148 -> 152
~ ___56+[AXSIMSetupUIServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___56+[AXSIMSetupUIServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 92 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[TSSIMUnlockDetailViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[TSSIMUnlockDetailViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ -[TSSIMUnlockDetailViewAccessibility initWithActionType:actionSubtype:] : 96 -> 92
~ +[TSSIMUnlockEntryViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[TSSIMUnlockEntryViewAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[TSSIMUnlockEntryViewAccessibility initWithActionType:actionSubtype:] : 96 -> 92
~ -[TSSIMUnlockEntryViewAccessibility _configureDetailLabelText] : 144 -> 152

```
