## AudioConferenceControlCenterModule

> `/System/Library/AccessibilityBundles/AudioConferenceControlCenterModule.axbundle/AudioConferenceControlCenterModule`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xa80
-  __TEXT.__auth_stubs: 0x190
+3036.2.0.0.0
+  __TEXT.__text: 0x9ec
   __TEXT.__objc_methlist: 0x1d8
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x2f7
   __TEXT.__oslogstring: 0x50
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x1a0
-  __TEXT.__objc_methname: 0x4da
-  __TEXT.__objc_methtype: 0x60
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EFD2DD6-E1A6-3268-879A-825EA79943CB
-  Functions: 45
-  Symbols:   217
-  CStrings:  115
+  UUID: E66492A9-014B-3118-8CC3-3299002F8F98
+  Functions: 43
+  Symbols:   215
+  CStrings:  52
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.384
+ ___block_literal_global.390
+ ___block_literal_global.397
+ ___block_literal_global.68
+ _accessibilityInitializeBundle.onceToken.67
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle].cold.1
- +[AXReplayKitModuleGlue accessibilityInitializeBundle].cold.1
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
~ +[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle] : 44 -> 40
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 144 -> 136
~ _accessibilityLocalizedString : 168 -> 160
~ +[AudioConferenceControlCenterModuleEffectControlAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[AudioConferenceControlCenterModuleEffectControlAccessibility accessibilityLabel] : 144 -> 132
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
- "AXAudioConferenceControlCenterModuleGlue"
- "AXReplayKitClientDelegate"
- "AXReplayKitModuleGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__AudioConferenceControlCenterModuleEffectControlAccessibility_super"
- "__AudioSettingsViewAccessibility_super"
- "__RPControlCenterMenuModuleViewControllerAccessibility_super"
- "_accessibilityControlCenterButtonAdditionalTraits"
- "_accessibilityPerformValidations:"
- "_axCountdownTimer"
- "_axSpeakAndGo:"
- "_setAXCountdownTimer:"
- "accessibilityBundles"
- "accessibilityContainerType"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityTraits"
- "addDegate:"
- "afterDelay:processBlock:"
- "bundleForClass:"
- "cancel"
- "didChangeAvailability:"
- "didUpdateClientStateWithAvailableExtensions:completionHandler:"
- "initWithTargetSerialQueue:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "recordingTimerDidUpdate"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeSwiftBoolForKey:"
- "safeSwiftStringForKey:"
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
- "validateClass:hasSwiftField:withSwiftType:"
- "validateProtocol:hasMethod:isInstanceMethod:isRequired:"

```
