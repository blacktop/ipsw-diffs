## AudioConferenceControlCenterModule

> `/System/Library/AccessibilityBundles/AudioConferenceControlCenterModule.axbundle/AudioConferenceControlCenterModule`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xa1c
-  __TEXT.__auth_stubs: 0x1b0
+3005.16.0.0.0
+  __TEXT.__text: 0xa80
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x1d8
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x2f7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C856EA3-8120-3CD7-B31E-7CC7E1E1EF67
+  UUID: FF4B38FB-7D03-3458-B1EB-DDC1A8160F71
   Functions: 45
-  Symbols:   219
+  Symbols:   217
   CStrings:  115
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[RPControlCenterMenuModuleViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[RPControlCenterMenuModuleViewControllerAccessibility updateStateAndUI] : 92 -> 96
~ -[RPControlCenterMenuModuleViewControllerAccessibility _axSpeakAndGo:] : 188 -> 196
~ -[RPControlCenterMenuModuleViewControllerAccessibility transitionToCountdownState] : 144 -> 148
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___73+[AXAudioConferenceControlCenterModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 136 -> 144
~ _accessibilityLocalizedString : 160 -> 168
~ +[AudioConferenceControlCenterModuleEffectControlAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[AudioConferenceControlCenterModuleEffectControlAccessibility accessibilityLabel] : 132 -> 144
~ -[AXReplayKitClientDelegate didStopRecordingOrBroadcast] : 120 -> 124
~ -[AXReplayKitClientDelegate didStartRecordingOrBroadcast] : 120 -> 124
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke : 136 -> 140
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_2 : 196 -> 200
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 96
~ ___54+[AXReplayKitModuleGlue accessibilityInitializeBundle]_block_invoke_5 : 92 -> 96

```
