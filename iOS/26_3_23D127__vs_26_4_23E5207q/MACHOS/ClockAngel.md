## ClockAngel

> `/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xdec
-  __TEXT.__auth_stubs: 0x1b0
+3005.16.0.0.0
+  __TEXT.__text: 0xe90
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x148
   __TEXT.__cstring: 0x3f7

   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x4e0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8052D17D-DBEE-36E0-81F3-E20974531CFD
+  UUID: DB6D9BAF-386C-34E2-A6B2-9D82AAFCCA8B
   Functions: 33
-  Symbols:   170
+  Symbols:   169
   CStrings:  144
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXClockAngelGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXClockAngelGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___49+[AXClockAngelGlue accessibilityInitializeBundle]_block_invoke_3 : 132 -> 140
~ _accessibilityLocalizedString : 176 -> 184
~ -[TimerCompressedControllerAccessibility _accessibilityLoadAccessibilityInformation] : 172 -> 176
~ +[SecureStopwatchControllerAccessibility _accessibilityPerformValidations:] : 276 -> 284
~ -[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation] : 408 -> 416
~ ___84-[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 216 -> 232
~ ___84-[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 476 -> 516
~ +[StopwatchApertureControllerAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[StopwatchApertureControllerAccessibility _accessibilityLoadAccessibilityInformation] : 148 -> 156
~ +[TimerApertureElementControllerAccessibility _accessibilityPerformValidations:] : 252 -> 260
~ -[TimerApertureElementControllerAccessibility viewWillTransitionToSize:withTransitionCoordinator:] : 208 -> 212
~ ___98-[TimerApertureElementControllerAccessibility viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 212 -> 228
~ -[TimerApertureElementControllerAccessibility playPausedAction] : 240 -> 260

```
