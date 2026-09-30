## HeadphoneProxService

> `/System/Library/AccessibilityBundles/HeadphoneProxService.axbundle/HeadphoneProxService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xba4
-  __TEXT.__auth_stubs: 0x1a0
+3005.16.0.0.0
+  __TEXT.__text: 0xc3c
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__cstring: 0x292
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x3f0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9F64A35-6E1E-3FB3-9BF7-B158B3B020DB
+  UUID: DDDEAD39-7077-3134-B421-7CB7B6433986
   Functions: 29
-  Symbols:   168
+  Symbols:   167
   CStrings:  108
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXHeadphoneProxServiceGlue accessibilityInitializeBundle] : 148 -> 152
~ ___59+[AXHeadphoneProxServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___59+[AXHeadphoneProxServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 112 -> 120
~ _accessibilityLocalizedString : 176 -> 184
~ -[HeadphoneBatteryContainerAccessibility accessibilityFrame] : 268 -> 276
~ +[LabelledBatteryViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[LabelledBatteryViewAccessibility accessibilityLabel] : 432 -> 484
~ _accessibilityLabelForBatteryTypeString : 200 -> 208
~ -[LabelledBatteryViewAccessibility accessibilityValue] : 84 -> 92
~ -[LabelledBatteryViewAccessibility accessibilityHint] : 84 -> 92
~ +[HeadphoneMovieBatteryViewAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[HeadphoneMovieBatteryViewAccessibility accessibilityFrame] : 268 -> 276
~ -[HeadphoneMovieBatteryViewAccessibility _axSetupLabels] : 300 -> 320

```
