## AccessibilitySettings

> `/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-2909.1.4.3.0
-  __TEXT.__text: 0x21288
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x203c
-  __TEXT.__cstring: 0x28ce
-  __TEXT.__oslogstring: 0x27d
+2909.1.4.13.0
+  __TEXT.__text: 0x221e4
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x207c
+  __TEXT.__cstring: 0x2b0b
   __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0x27d
   __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__objc_classname: 0xa6b
-  __TEXT.__objc_methname: 0x5904
-  __TEXT.__objc_methtype: 0x9e7
-  __TEXT.__objc_stubs: 0x4ae0
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x508
+  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__objc_classname: 0xa7b
+  __TEXT.__objc_methname: 0x59ec
+  __TEXT.__objc_methtype: 0x9fd
+  __TEXT.__objc_stubs: 0x4bc0
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2600
-  __DATA_CONST.__objc_selrefs: 0x1980
+  __DATA_CONST.__objc_selrefs: 0x19b8
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__cfstring: 0x3520
   __AUTH_CONST.__objc_const: 0x1440
-  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x14a0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x388
   __DATA.__objc_superrefs: 0x198
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x4e0
+  __DATA.__data: 0x4e8
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 729
-  Symbols:   2942
-  CStrings:  1533
+  Functions: 747
+  Symbols:   2992
+  CStrings:  1568
 
Symbols:
+ -[AccessibilityBridgeBaseController(EltonManagement) presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:]
+ -[VoiceOverController instructionsText]
+ -[VoiceOverController setVoiceOverTouchEnabled:specifier:]
+ -[VoiceOverController voiceOverTouchEnabled:]
+ -[ZoomController instructionsText]
+ _AFDictationLanguageForKeyboardLanguage
+ _AXActivePairedDeviceDisableElton
+ _AXActivePairedDeviceSupportsElton
+ _AXActivePairedDeviceSupportsHasEltonEnabled
+ _AXCFormattedString
+ _WAGPreferencesDomain
+ _WAGSettingsGestureModeKey
+ __OBJC_$_CLASS_METHODS_AccessibilityBridgeBaseController(EltonManagement)
+ __OBJC_$_INSTANCE_METHODS_AccessibilityBridgeBaseController(EltonManagement)
+ ___122-[AccessibilityBridgeBaseController(EltonManagement) presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:]_block_invoke
+ ___122-[AccessibilityBridgeBaseController(EltonManagement) presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:]_block_invoke_2
+ ___122-[AccessibilityBridgeBaseController(EltonManagement) presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:]_block_invoke_3
+ ___43-[ZoomController setZoomEnabled:specifier:]_block_invoke
+ ___43-[ZoomController setZoomEnabled:specifier:]_block_invoke_2
+ ___49-[WatchControlController setWatchControlEnabled:]_block_invoke
+ ___56-[ZoomHandGesturesController setHandGestures:specifier:]_block_invoke
+ ___58-[VoiceOverController setVoiceOverTouchEnabled:specifier:]_block_invoke
+ ___58-[VoiceOverController setVoiceOverTouchEnabled:specifier:]_block_invoke_2
+ ___61-[VoiceOverHandGesturesController setHandGestures:specifier:]_block_invoke
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v16?0"UIAlertAction"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e23_v16?0"UIAlertAction"8ls40l8s48l8s32l8
+ __unnamed_array_storage.356
+ __unnamed_array_storage.449
+ __unnamed_array_storage.450
+ _kAXSVoiceOverTouchEnabledPreference
+ _objc_msgSend$areVoiceOverHandGesturesEnabled
+ _objc_msgSend$areZoomHandGesturesEnabled
+ _objc_msgSend$integerForKey:keyExistsAndHasValidFormat:
+ _objc_msgSend$presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:
+ _objc_msgSend$setVoiceOverHandGestures:
+ _objc_msgSend$setZoomHandGestures:
+ _objc_msgSend$stringWithFormat:
- __OBJC_$_CLASS_METHODS_AccessibilityBridgeBaseController
- __OBJC_$_INSTANCE_METHODS_AccessibilityBridgeBaseController
- __unnamed_array_storage.343
- __unnamed_array_storage.436
- __unnamed_array_storage.437
CStrings:
+ "%@"
+ "%@\n\n%@"
+ "%@\n%@\n%@\n%@"
+ "%@%@"
+ "ACTION_CANCEL"
+ "ACTION_DISABLE_FEATURE"
+ "ACTION_USE_WIHOUT_GREY"
+ "ADJUST_MAG_INSTRUCTIONS"
+ "DISABLE_ELTON_ALERT_MESSAGE"
+ "DISABLE_ELTON_ALERT_MESSAGE_HAND_GESTURES"
+ "DISABLE_ELTON_ALERT_TITLE"
+ "EltonManagement"
+ "GREY_FEATURE_NAME_VOICEOVER"
+ "GREY_FEATURE_NAME_WATCH_CONTROL"
+ "GREY_FEATURE_NAME_ZOOM"
+ "PAN_INSTRUCTIONS"
+ "PRESS_ITEM_INSTRUCTION"
+ "SCROLL_ITEM_INSTRUCTION"
+ "SELECT_ITEM_INSTRUCTION"
+ "VOICEOVER_INTRO"
+ "VOICEOVER_WATCH_CONTROL_INSTRUCTION"
+ "WATCH_CONTROL_SWITCH_SECTION_FOOTER"
+ "WATCH_CONTROL_VOICEOVER_INSTRUCTION"
+ "ZOOM_INSTRUCTIONS"
+ "ZOOM_INTRO"
+ "com.apple.WatchGestures.prefs"
+ "gestureMode"
+ "instructionsText"
+ "integerForKey:keyExistsAndHasValidFormat:"
+ "presentDisableEltonAlert:greyOptional:confirmBlock:disableGreyBlock:"
+ "setVoiceOverHandGestures:"
+ "setVoiceOverTouchEnabled:specifier:"
+ "setZoomHandGestures:"
+ "stringWithFormat:"
+ "v44@0:8@16B24@?28@?36"

```
