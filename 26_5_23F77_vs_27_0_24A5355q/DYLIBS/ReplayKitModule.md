## ReplayKitModule

> `/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x664
-  __TEXT.__auth_stubs: 0x180
+3036.2.0.0.0
+  __TEXT.__text: 0x614
   __TEXT.__objc_methlist: 0x108
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x179
   __TEXT.__oslogstring: 0x50
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x3f7
-  __TEXT.__objc_methtype: 0x50
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x50
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x240
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F9BE8E3-6A80-3BEC-9D37-F8A6E25528EA
-  Functions: 26
-  Symbols:   142
-  CStrings:  76
+  UUID: 3E288D9C-1568-32A2-B6AD-40C00CE2AA9E
+  Functions: 25
+  Symbols:   140
+  CStrings:  29
 
Symbols:
+ ___block_literal_global.362
+ ___block_literal_global.384
+ ___block_literal_global.390
+ ___block_literal_global.397
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXReplayKitModuleGlue accessibilityInitializeBundle].cold.1
- ___block_literal_global.341
- ___block_literal_global.363
- ___block_literal_global.369
- ___block_literal_global.376
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[RPControlCenterMenuModuleViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[RPControlCenterMenuModuleViewControllerAccessibility updateStateAndUI] : 96 -> 92
~ -[RPControlCenterMenuModuleViewControllerAccessibility _axSpeakAndGo:] : 196 -> 188
~ -[RPControlCenterMenuModuleViewControllerAccessibility transitionToCountdownState] : 148 -> 144
~ -[AXReplayKitClientDelegate didStopRecordingOrBroadcast] : 124 -> 120
~ -[AXReplayKitClientDelegate didStartRecordingOrBroadcast] : 124 -> 120
~ +[AXReplayKitModuleGlue accessibilityInitializeBundle] : 44 -> 40
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke : 140 -> 136
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_2 : 200 -> 196
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 96 -> 92
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_5 : 96 -> 92
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXReplayKitClientDelegate"
- "AXReplayKitModuleGlue"
- "Q16@0:8"
- "SafeCategory"
- "__RPControlCenterMenuModuleViewControllerAccessibility_super"
- "_accessibilityControlCenterButtonAdditionalTraits"
- "_accessibilityPerformValidations:"
- "_axCountdownTimer"
- "_axSpeakAndGo:"
- "_setAXCountdownTimer:"
- "accessibilityBundles"
- "accessibilityInitializeBundle"
- "addDegate:"
- "afterDelay:processBlock:"
- "cancel"
- "didChangeAvailability:"
- "didUpdateClientStateWithAvailableExtensions:completionHandler:"
- "initWithTargetSerialQueue:"
- "installSafeCategory:canInteractWithTargetClass:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "recordingTimerDidUpdate"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "sessionDidFailToStart"
- "sessionIsStarting"
- "setDebugBuild:"
- "setNeedsLoadAccessibilityInformation"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "startSystemSession"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@16@?24"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateProtocol:hasMethod:isInstanceMethod:isRequired:"

```
