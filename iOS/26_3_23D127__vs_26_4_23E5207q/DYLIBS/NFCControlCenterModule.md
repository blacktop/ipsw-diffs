## NFCControlCenterModule

> `/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x834
-  __TEXT.__auth_stubs: 0x150
+3005.16.0.0.0
+  __TEXT.__text: 0x880
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0xd8
   __TEXT.__cstring: 0x222
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FF484C5-77A8-38F4-8C4D-6B7E6F3363DC
+  UUID: 3E713475-4975-35E6-A9F1-F231B10BEEA4
   Functions: 22
-  Symbols:   136
+  Symbols:   135
   CStrings:  98
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___61+[AXNFCControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 128 -> 136
~ _accessibilityLocalizedString : 160 -> 168
~ -[NFCCWrappedLabelAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[NFCCWrappedLabelAccessibility accessibilityLabel] : 84 -> 92
~ -[NFCCWrappedLabelAccessibility accessibilityTraits] : 64 -> 68
~ +[NFCCContentViewControllerAccessibility _accessibilityPerformValidations:] : 276 -> 284
~ -[NFCCContentViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 368 -> 372
~ ___84-[NFCCContentViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 252 -> 272
~ -[NFCCContentViewControllerAccessibility _setModuleState:animated:] : 180 -> 184

```
