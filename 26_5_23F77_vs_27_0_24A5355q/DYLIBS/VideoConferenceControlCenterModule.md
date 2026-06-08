## VideoConferenceControlCenterModule

> `/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xdd4
-  __TEXT.__auth_stubs: 0x210
+3036.2.0.0.0
+  __TEXT.__text: 0xd24
   __TEXT.__objc_methlist: 0x1e0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x33e
   __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__cstring: 0x33e
   __TEXT.__oslogstring: 0x50
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x58c
-  __TEXT.__objc_methtype: 0x60
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84101390-55EE-3DD0-8860-9B6C2AA1E562
-  Functions: 48
-  Symbols:   248
-  CStrings:  133
+  UUID: 541A900D-4ACD-3996-AE99-D038D6B99817
+  Functions: 46
+  Symbols:   246
+  CStrings:  61
 
Symbols:
+ GCC_except_table23
+ GCC_except_table24
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.384
+ ___block_literal_global.390
+ ___block_literal_global.397
+ ___block_literal_global.70
+ _accessibilityInitializeBundle.onceToken.69
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXReplayKitModuleGlue accessibilityInitializeBundle].cold.1
- +[AXVideoConferenceControlCenterModuleGlue accessibilityInitializeBundle].cold.1
- GCC_except_table5
- GCC_except_table6
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.363
- ___block_literal_global.369
- ___block_literal_global.376
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[RPControlCenterMenuModuleViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[RPControlCenterMenuModuleViewControllerAccessibility updateStateAndUI] : 96 -> 92
~ -[RPControlCenterMenuModuleViewControllerAccessibility _axSpeakAndGo:] : 196 -> 188
~ -[RPControlCenterMenuModuleViewControllerAccessibility transitionToCountdownState] : 148 -> 144
~ +[AXVideoConferenceControlCenterModuleGlue accessibilityInitializeBundle] : 44 -> 40
~ ___73+[AXVideoConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___73+[AXVideoConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___73+[AXVideoConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 144 -> 136
~ _accessibilityLocalizedString : 168 -> 160
~ +[VideoConferenceControlCenterModuleEffectControlAccessibility _accessibilityPerformValidations:] : 188 -> 180
~ -[VideoConferenceControlCenterModuleEffectControlAccessibility accessibilityLabel] : 144 -> 132
~ -[VideoConferenceControlCenterModuleEffectControlAccessibility accessibilityCustomActions] : 456 -> 436
~ ___90-[VideoConferenceControlCenterModuleEffectControlAccessibility accessibilityCustomActions]_block_invoke_2 : 216 -> 208
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
- "AXVideoConferenceControlCenterModuleGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__RPControlCenterMenuModuleViewControllerAccessibility_super"
- "__VideoConferenceControlCenterModuleEffectControlAccessibility_super"
- "__VideoEffectsViewAccessibility_super"
- "_accessibilityControlCenterButtonAdditionalTraits"
- "_accessibilityPerformValidations:"
- "_axCountdownTimer"
- "_axSpeakAndGo:"
- "_setAXCountdownTimer:"
- "accessibilityBundles"
- "accessibilityContainerType"
- "accessibilityCustomActions"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "addDegate:"
- "afterDelay:processBlock:"
- "array"
- "axSafelyAddObject:"
- "bundleForClass:"
- "cancel"
- "didChangeAvailability:"
- "didUpdateClientStateWithAvailableExtensions:completionHandler:"
- "initWithName:actionHandler:"
- "initWithTargetSerialQueue:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "mutableCopy"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "recordingTimerDidUpdate"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeSwiftBoolForKey:"
- "safeSwiftEnumCase"
- "safeSwiftStringForKey:"
- "safeSwiftValueForKey:"
- "safeValueForKey:"
- "sendActionsForControlEvents:"
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
- "validateClass:hasSwiftField:withSwiftType:"
- "validateProtocol:hasMethod:isInstanceMethod:isRequired:"

```
