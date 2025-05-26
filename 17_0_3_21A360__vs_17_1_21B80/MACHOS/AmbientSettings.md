## AmbientSettings

> `/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings`

```diff

-52.2.1.0.0
-  __TEXT.__text: 0x18bc
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x480
-  __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x2d6
-  __TEXT.__objc_methname: 0x41f
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methtype: 0x3f
-  __TEXT.__unwind_info: 0xac
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x3e0
+52.7.100.0.0
+  __TEXT.__text: 0x225c
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x3dd
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__objc_methname: 0x721
+  __TEXT.__objc_classname: 0x62
+  __TEXT.__objc_methtype: 0x83
+  __TEXT.__unwind_info: 0xd4
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__cfstring: 0x520
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1b0
-  __DATA.__objc_selrefs: 0x168
-  __DATA.__objc_classrefs: 0x40
+  __DATA.__objc_const: 0x278
+  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_classrefs: 0x50
+  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/Ambient.framework/Ambient
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   58
-  CStrings:  85
+  Functions: 37
+  Symbols:   82
+  CStrings:  137
 
Symbols:
+ _OBJC_CLASS_$_AMAlwaysOnDisplaySettingsViewController
+ _OBJC_CLASS_$_AMAmbientDefaults
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_METACLASS_$_AMAlwaysOnDisplaySettingsViewController
+ _PSEnabledKey
+ _PSIsRadioGroupKey
+ _PSRadioGroupCheckedSpecifierKey
+ __AXSAttentionAwarenessFeaturesEnabled
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __dispatch_main_q
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSendSuper2
+ _objc_opt_new
+ _objc_release_x1
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
- _OBJC_CLASS_$_AMNightModeSettingsViewController
- _OBJC_METACLASS_$_AMNightModeSettingsViewController
- _objc_retain_x21
CStrings:
+ "\x06"
+ ".cxx_destruct"
+ "@\"<BSDefaultObserver>\""
+ "@\"PSSpecifier\""
+ "@24@0:8@16"
+ "ALWAYS_ON_DISPLAY_MODE"
+ "ALWAYS_ON_DISPLAY_OPTIONS"
+ "ALWAYS_ON_DISPLAY_TURN_OFF_AFTER_IDLE"
+ "ALWAYS_ON_DISPLAY_TURN_OFF_AUTOMATICALLY"
+ "ALWAYS_ON_DISPLAY_TURN_OFF_FOOTER"
+ "ALWAYS_ON_DISPLAY_TURN_OFF_NEVER"
+ "AMAlwaysOnDisplaySettingsViewController"
+ "AT_NIGHT"
+ "AT_NIGHT_GROUP_HEADER"
+ "MOTION_TO_WAKE_GROUP"
+ "TURN_DISPLAY_OFF_GROUP_HEADER"
+ "_AFTER_IDLE"
+ "_AUTOMATICALLY"
+ "_NEVER"
+ "_alwaysOnDisplayLinkSpecifier"
+ "_ambientDefaults"
+ "_isMotionToWakeAllowed"
+ "_isNightModeRequired"
+ "_modeAfterIdleSpecifier"
+ "_modeAutomaticallySpecifier"
+ "_modeGroupSpecifier"
+ "_modeNeverSpecifier"
+ "_motionToWakeSpecifierGroup"
+ "_nightModeEnabled:"
+ "_observerToken"
+ "_updateModeSelectionFromPreferences"
+ "_updateModeSelectionFromPreferencesAnimated:"
+ "_updateSpecifiersFromPreferences"
+ "addObjectsFromArray:"
+ "alwaysOnMode"
+ "countByEnumeratingWithState:objects:count:"
+ "dealloc"
+ "firstObject"
+ "groupSpecifierWithID:"
+ "groupSpecifierWithID:name:"
+ "identifier"
+ "indexForIndexPath:"
+ "indexOfSpecifierID:"
+ "invalidate"
+ "nightModeEnabled"
+ "numberWithInt:"
+ "observeDefault:onQueue:withBlock:"
+ "reloadSpecifier:"
+ "removeSpecifierWithID:"
+ "setAlwaysOnMode:"
+ "setName:"
+ "specifierAtIndex:"
+ "specifierForID:"
+ "stringByAppendingString:"
+ "stringWithUTF8String:"
+ "tableView:didSelectRowAtIndexPath:"
+ "v16@0:8"
+ "v20@0:8B16"
- "ALWAYS_ON_ENABLED"
- "ALWAYS_ON_ENABLED_FOOTER"
- "AMAlwaysOnEnabled"
- "AMNightModeSettingsViewController"
- "_alwaysOnSpecifier"
- "_motionToWakeEnabledSpecifier"
- "_nightModeLinkSpecifier"

```
