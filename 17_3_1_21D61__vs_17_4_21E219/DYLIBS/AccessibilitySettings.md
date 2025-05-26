## AccessibilitySettings

> `/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-2909.1.4.18.0
-  __TEXT.__text: 0x221e4
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x207c
-  __TEXT.__cstring: 0x2b0b
-  __TEXT.__const: 0x50
+2909.23.0.0.0
+  __TEXT.__text: 0x22848
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x2104
+  __TEXT.__cstring: 0x2c1e
+  __TEXT.__const: 0x60
   __TEXT.__oslogstring: 0x27d
   __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x8d8
-  __TEXT.__objc_classname: 0xa7b
-  __TEXT.__objc_methname: 0x59ec
+  __TEXT.__unwind_info: 0x8f0
+  __TEXT.__objc_classname: 0xaa0
+  __TEXT.__objc_methname: 0x5a86
   __TEXT.__objc_methtype: 0x9fd
-  __TEXT.__objc_stubs: 0x4bc0
-  __DATA_CONST.__got: 0x488
+  __TEXT.__objc_stubs: 0x4be0
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2600
-  __DATA_CONST.__objc_selrefs: 0x19b8
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x1440
-  __AUTH_CONST.__const: 0xe0
+  __DATA_CONST.__objc_const: 0x26a8
+  __DATA_CONST.__objc_selrefs: 0x19d8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __AUTH_CONST.__cfstring: 0x3660
+  __AUTH_CONST.__objc_const: 0x1488
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x408
-  __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x388
-  __DATA.__objc_superrefs: 0x198
+  __AUTH_CONST.__auth_got: 0x410
+  __AUTH.__objc_data: 0x14f0
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x28

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 747
-  Symbols:   2992
-  CStrings:  1568
+  Functions: 757
+  Symbols:   3020
+  CStrings:  1584
 
Symbols:
+ -[AccessibilityBridgeSettingsController isIncreaseBrightnessFloorEnabled:]
+ -[AccessibilityBridgeSettingsController setIncreaseBrightnessFloorEnabled:specifier:]
+ -[VoiceOverController voiceOverDoubleTapInterval:]
+ -[VoiceOverDoubleTapIntervalController maximumValueForSpecifier:]
+ -[VoiceOverDoubleTapIntervalController minimumValueForSpecifier:]
+ -[VoiceOverDoubleTapIntervalController specifier:setValue:]
+ -[VoiceOverDoubleTapIntervalController specifiers]
+ -[VoiceOverDoubleTapIntervalController stepValueForSpecifier:]
+ -[VoiceOverDoubleTapIntervalController stringValueForSpecifier:]
+ -[VoiceOverDoubleTapIntervalController valueForSpecifier:]
+ _AXActivePairedDeviceIsLighthouseEOrLater
+ _AXRuntimeCheck_SupportsIncreaseBrightnessFloor
+ _OBJC_CLASS_$_VoiceOverDoubleTapIntervalController
+ _OBJC_METACLASS_$_VoiceOverDoubleTapIntervalController
+ __OBJC_$_INSTANCE_METHODS_VoiceOverDoubleTapIntervalController
+ __OBJC_$_PROP_LIST_VoiceOverDoubleTapIntervalController
+ __OBJC_CLASS_PROTOCOLS_$_VoiceOverDoubleTapIntervalController
+ __OBJC_CLASS_RO_$_VoiceOverDoubleTapIntervalController
+ __OBJC_METACLASS_RO_$_VoiceOverDoubleTapIntervalController
+ ___block_literal_global.303
+ __unnamed_array_storage.268
+ __unnamed_array_storage.475
+ _kAXSIncreaseBrightnessFloorEnabledPreference
+ _kAXSVoiceOverDoubleTapIntervalMax
+ _kAXSVoiceOverDoubleTapIntervalMin
+ _objc_msgSend$objectAtIndexedSubscript:
- ___73-[WatchControlController setSideButtonConfirmWithWatchControl:specifier:]_block_invoke
- ___block_literal_global.279
- __unnamed_array_storage.244
- __unnamed_array_storage.356
- __unnamed_array_storage.449
- __unnamed_array_storage.450
CStrings:
+ "%d"
+ "0"
+ "APP_SWITCHER_AUTO_SELECT_DETAILS"
+ "AppSwitcherAutoSelect"
+ "AppSwitcherAutoSelectGroup"
+ "COLOR_FILTERS_GROUP"
+ "DOUBLE_TAP_INTERVAL_FOOTER_TEXT"
+ "INCREASE_BRIGHTNESS_FLOOR_ROW_TITLE"
+ "INCREASE_BRIGHTNESS_FLOOR_SECTION_FOOTER"
+ "INCREASE_BRIGHTNESS_FLOOR_SWITCH_ID"
+ "T@\"NSString\",?,R,C"
+ "VoiceOverDoubleTapInterval"
+ "VoiceOverDoubleTapIntervalController"
+ "WatchControlDisableSideButtonConfirm"
+ "isIncreaseBrightnessFloorEnabled:"
+ "objectAtIndexedSubscript:"
+ "setIncreaseBrightnessFloorEnabled:specifier:"
+ "voiceOverDoubleTapInterval:"
- "COLOR_FILTERS"
- "WalkieTalkieTapToTalkGroup"

```
