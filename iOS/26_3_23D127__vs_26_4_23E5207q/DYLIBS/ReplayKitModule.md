## ReplayKitModule

> `/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x62c
+3005.16.0.0.0
+  __TEXT.__text: 0x664
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x108
   __TEXT.__const: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DBE28F8-799F-3DD2-9CE7-AD3D863BCB5F
+  UUID: 81907510-511D-307E-A5DA-9C66EA2551B8
   Functions: 26
   Symbols:   142
   CStrings:  76
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[RPControlCenterMenuModuleViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[RPControlCenterMenuModuleViewControllerAccessibility updateStateAndUI] : 92 -> 96
~ -[RPControlCenterMenuModuleViewControllerAccessibility _axSpeakAndGo:] : 188 -> 196
~ -[RPControlCenterMenuModuleViewControllerAccessibility transitionToCountdownState] : 144 -> 148
~ -[AXReplayKitClientDelegate didStopRecordingOrBroadcast] : 120 -> 124
~ -[AXReplayKitClientDelegate didStartRecordingOrBroadcast] : 120 -> 124
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke : 136 -> 140
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_2 : 196 -> 200
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 96
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_5 : 92 -> 96

```
