## AccessibilitySettings

> `/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-2905.4.0.0.0
-  __TEXT.__text: 0x20648
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x1fcc
-  __TEXT.__cstring: 0x2862
-  __TEXT.__oslogstring: 0x250
+2909.1.4.3.0
+  __TEXT.__text: 0x21288
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x203c
+  __TEXT.__cstring: 0x28ce
+  __TEXT.__oslogstring: 0x27d
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x86c
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0xa6b
-  __TEXT.__objc_methname: 0x5727
-  __TEXT.__objc_methtype: 0x9c4
-  __TEXT.__objc_stubs: 0x4940
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x468
+  __TEXT.__objc_methname: 0x5904
+  __TEXT.__objc_methtype: 0x9e7
+  __TEXT.__objc_stubs: 0x4ae0
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x508
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x25c0
-  __DATA_CONST.__objc_selrefs: 0x1908
+  __DATA_CONST.__objc_const: 0x2600
+  __DATA_CONST.__objc_selrefs: 0x1980
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0x3140
+  __AUTH_CONST.__cfstring: 0x31e0
   __AUTH_CONST.__objc_const: 0x1440
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH.__objc_data: 0x14a0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x388
-  __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_superrefs: 0x198
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80C9CD15-8892-3355-8108-8FD6AE251095
-  Functions: 714
-  Symbols:   2891
-  CStrings:  1903
+  UUID: E0BEB281-CCBB-394D-8522-DDA8E880D17D
+  Functions: 729
+  Symbols:   2942
+  CStrings:  1932
 
Symbols:
+ -[LiveSpeechController .cxx_destruct]
+ -[LiveSpeechController _selectedVoiceNameForVoiceSpecifier:]
+ -[LiveSpeechController init]
+ -[LiveSpeechController setSpeechModelController:]
+ -[LiveSpeechController speechModelController]
+ -[LiveSpeechController tableView:didSelectRowAtIndexPath:]
+ -[LiveSpeechSettingsModelController voiceIdentifierForLiveSpeechKeyboardID:]
+ -[QuickActionsV2Controller quickActionSwitchState]
+ -[QuickActionsV2Controller setQuickActionSwitchState:]
+ -[VoiceOverController areVoiceOverHandGesturesEnabled]
+ -[WatchControlController _watchQuickActionsV2SwitchDescription]
+ -[ZoomController areZoomHandGesturesEnabled]
+ GCC_except_table3
+ _AXActivePairedDeviceSupportsQuickActionsAlwaysOnState
+ _LiveSpeechLogCommon
+ _OBJC_CLASS_$_UIKeyboardInputModeController
+ _OBJC_IVAR_$_LiveSpeechController._speechModelController
+ __OBJC_$_INSTANCE_VARIABLES_LiveSpeechController
+ __OBJC_$_PROP_LIST_LiveSpeechController
+ ___58-[LiveSpeechController tableView:didSelectRowAtIndexPath:]_block_invoke
+ ___58-[LiveSpeechController tableView:didSelectRowAtIndexPath:]_block_invoke_2
+ ___73-[AccessibilityBridgeSettingsController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___73-[AccessibilityBridgeSettingsController tableView:cellForRowAtIndexPath:]_block_invoke_2
+ ___73-[AccessibilityBridgeSettingsController tableView:cellForRowAtIndexPath:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_Q8?0ls32l8
+ ___block_descriptor_48_e8_32s40w_e15_"NSString"8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e18_v16?0"NSString"8ls32l8w40l8
+ ___block_literal_global.279
+ __unnamed_array_storage.244
+ __unnamed_array_storage.343
+ __unnamed_array_storage.436
+ __unnamed_array_storage.437
+ _objc_msgSend$accessibilityLabel
+ _objc_msgSend$accessibilityTraits
+ _objc_msgSend$accessibilityValue
+ _objc_msgSend$enabledInputModeLanguages
+ _objc_msgSend$quickActionSwitchState
+ _objc_msgSend$setAccessibilityLabelBlock:
+ _objc_msgSend$setAccessibilityTraitsBlock:
+ _objc_msgSend$setAccessibilityValueBlock:
+ _objc_msgSend$setShowPersonalVoices:
+ _objc_msgSend$sharedInputModeController
+ _objc_msgSend$voiceIdentifierForLiveSpeechKeyboardID:
+ _objc_msgSend$voiceOverHandGesturesEnabled
+ _objc_msgSend$zoomHandGesturesEnabled
- -[LiveSpeechSettingsModelController selectedVoiceIdentifierForSpeechSourceKey:languageCode:]
- -[VoiceOverController voiceOverSetUsesSiriVoice:specifier:]
- -[VoiceOverController voiceOverUsesSiriVoice:]
- ___block_literal_global.282
- __unnamed_array_storage.242
- __unnamed_array_storage.331
- __unnamed_array_storage.424
- __unnamed_array_storage.425
- _kAXSVoiceOverUseActiveSiriVoice
CStrings:
+ "0E581E21-36BA-4770-9408-0467585E8495"
+ "9A815CF5-4377-41E5-A00A-161FC5C51956"
+ "@\"AXSpeechSettingsModelController\""
+ "AccessibilitySettings-elton"
+ "Bridge: Will set voiceID=%@ to keyboardID=%@"
+ "LIVE_SPEECH_VOICES_FOOTER"
+ "Q8@?0"
+ "QUICK_ACTIONS_SWITCH_FOOTER"
+ "T@\"AXSpeechSettingsModelController\",&,N,V_speechModelController"
+ "_selectedVoiceNameForVoiceSpecifier:"
+ "_watchQuickActionsV2SwitchDescription"
+ "accessibilityTraits"
+ "accessibilityValue"
+ "areVoiceOverHandGesturesEnabled"
+ "areZoomHandGesturesEnabled"
+ "colorfilters"
+ "enabledInputModeLanguages"
+ "quickActionSwitchState"
+ "setAccessibilityLabelBlock:"
+ "setAccessibilityTraitsBlock:"
+ "setAccessibilityValueBlock:"
+ "setQuickActionSwitchState:"
+ "setShowPersonalVoices:"
+ "sharedInputModeController"
+ "voiceIdentifierForLiveSpeechKeyboardID:"
+ "voiceOverHandGesturesEnabled"
+ "yue"
+ "zoomHandGesturesEnabled"
- "43E00559-AA2F-4680-9118-AD6ABDFEDCD2"
- "LIVE_SPEECH_PREFERRED_VOICE_GROUP"
- "voiceOverSetUsesSiriVoice:specifier:"
- "voiceOverUsesSiriVoice:"

```
