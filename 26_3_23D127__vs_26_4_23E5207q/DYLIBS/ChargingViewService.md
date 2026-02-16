## ChargingViewService

> `/System/Library/AccessibilityBundles/ChargingViewService.axbundle/ChargingViewService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x45c
+3005.16.0.0.0
+  __TEXT.__text: 0x494
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x104
   __TEXT.__cstring: 0x179

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAE02744-70E8-3A95-B8DB-2B63DB8C79F6
+  UUID: A0048CF9-153A-3121-8601-C34B79E2CE46
   Functions: 20
   Symbols:   120
   CStrings:  64
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___58+[AXChargingViewServiceGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___58+[AXChargingViewServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___58+[AXChargingViewServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 112 -> 120
~ +[EngagementViewControllerAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[EngagementViewControllerAccessibility viewDidLoad] : 104 -> 108
~ +[PlatterContentViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PlatterContentViewAccessibility accessibilityValue] : 152 -> 168

```
