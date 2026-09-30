## Settings-Assistant

> `/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x630
-  __TEXT.__auth_stubs: 0xc0
+3005.16.0.0.0
+  __TEXT.__text: 0x688
+  __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__cstring: 0x1b1
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x68
+  __AUTH_CONST.__auth_got: 0x60
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6156C788-6026-33C3-A099-6FEE04A7989E
+  UUID: 3A894B1F-6508-30DF-B3F3-7AB3514DB590
   Functions: 22
-  Symbols:   119
+  Symbols:   118
   CStrings:  79
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ -[ACSettingsSliderViewAccessibility accessibilityLabel] : 168 -> 188
~ -[ACSettingsSliderViewAccessibility accessibilityValue] : 84 -> 92
~ -[ACSettingsSliderViewAccessibility accessibilityDecrement] : 72 -> 76
~ -[ACSettingsSliderViewAccessibility accessibilityIncrement] : 72 -> 76
~ -[ACSettingsSliderViewAccessibility accessibilityTraits] : 64 -> 68
~ -[ACSettingsSwitchViewAccessibility accessibilityLabel] : 84 -> 92
~ -[ACSettingsSwitchViewAccessibility accessibilityValue] : 144 -> 156
~ -[ACSettingsSwitchViewAccessibility accessibilityActivationPoint] : 80 -> 84
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke : 164 -> 172
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 224 -> 228
~ ___49+[SiriSettingsGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ _accessibilityLocalizedString : 176 -> 184

```
