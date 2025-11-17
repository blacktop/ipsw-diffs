## DisplayAndBrightnessSettings

> `/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`

```diff

-1185.2.1.0.0
-  __TEXT.__text: 0x2bf4c
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x2c9c
-  __TEXT.__const: 0x2f4
+1185.2.2.100.0
+  __TEXT.__text: 0x2c5a8
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_methlist: 0x2cdc
+  __TEXT.__const: 0x304
   __TEXT.__gcc_except_tab: 0x440
-  __TEXT.__cstring: 0x31dc
-  __TEXT.__oslogstring: 0x6f1
+  __TEXT.__cstring: 0x335c
+  __TEXT.__oslogstring: 0x73d
   __TEXT.__constg_swiftt: 0x84
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xa50
+  __TEXT.__unwind_info: 0xa68
   __TEXT.__objc_classname: 0x84e
-  __TEXT.__objc_methname: 0x8919
-  __TEXT.__objc_methtype: 0xebd
-  __TEXT.__objc_stubs: 0x7360
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0x610
+  __TEXT.__objc_methname: 0x8a81
+  __TEXT.__objc_methtype: 0xec9
+  __TEXT.__objc_stubs: 0x7440
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22e8
+  __DATA_CONST.__objc_selrefs: 0x2330
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x3460
-  __AUTH_CONST.__objc_const: 0x49f8
+  __AUTH_CONST.__cfstring: 0x35c0
+  __AUTH_CONST.__objc_const: 0x4a28
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xd30
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x32c
+  __DATA.__objc_ivar: 0x330
   __DATA.__data: 0x768
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AF362031-B478-3716-A606-B5EE553BF7BF
-  Functions: 969
-  Symbols:   4001
-  CStrings:  2596
+  UUID: 31F01923-EF14-3066-A4DA-B46B9DC46889
+  Functions: 976
+  Symbols:   4023
+  CStrings:  2631
 
Symbols:
+ -[DBSExternalDisplayPreferencesController externalBrightnessSliderTouchEnded:]
+ -[DBSExternalDisplayPreferencesController externalBrightnessSlider]
+ -[DBSExternalDisplayPreferencesController setExternalBrightnessSlider:]
+ -[DBSLiquidGlassController _changeGlassLegibilitySettingForSpecifier:]
+ -[DBSLiquidGlassController _newAlertControllerForChangesDisabledForSpecifier:]
+ -[DBSLiquidGlassController tableView:willSelectRowAtIndexPath:]
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_DBSExternalDisplayPreferencesController._externalBrightnessSlider
+ __AXSSetDarkenSystemColors
+ __AXSSetEnhanceBackgroundContrastEnabled
+ ___77-[DBSExternalDisplayPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke.92
+ ___78-[DBSLiquidGlassController _newAlertControllerForChangesDisabledForSpecifier:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ _objc_msgSend$_changeGlassLegibilitySettingForSpecifier:
+ _objc_msgSend$_newAlertControllerForChangesDisabledForSpecifier:
+ _objc_msgSend$appendString:
+ _objc_msgSend$externalBrightnessSlider
+ _objc_msgSend$removeTarget:action:forControlEvents:
+ _objc_msgSend$setExternalBrightnessSlider:
+ _objc_msgSend$stringWithString:
- ___77-[DBSExternalDisplayPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke.90
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_DisplayAndBrightnessSettings
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_DisplayAndBrightnessSettings
CStrings:
+ "\n\n%@"
+ "@\"UISlider\""
+ "External Display: Committing final brightness value on touch up: %{public}f"
+ "LIQUID_GLASS_ALERT_BODY_IC_ON"
+ "LIQUID_GLASS_ALERT_BODY_RT_ON"
+ "LIQUID_GLASS_ALERT_BODY_RT_ON_IC_ON"
+ "LIQUID_GLASS_ALERT_CANCEL_ACTION_TITLE"
+ "LIQUID_GLASS_ALERT_PRIMARY_ACTION_TITLE"
+ "LIQUID_GLASS_ALERT_TITLE_IC_ON"
+ "LIQUID_GLASS_ALERT_TITLE_RT_ON"
+ "LIQUID_GLASS_ALERT_TITLE_RT_ON_IC_ON"
+ "LIQUID_GLASS_SETTING_ACCESSIBILITY_FOOTER_IC_ON"
+ "LIQUID_GLASS_SETTING_ACCESSIBILITY_FOOTER_RT_ON"
+ "LIQUID_GLASS_SETTING_ACCESSIBILITY_FOOTER_RT_ON_IC_ON"
+ "T@\"UISlider\",W,N,V_externalBrightnessSlider"
+ "_changeGlassLegibilitySettingForSpecifier:"
+ "_externalBrightnessSlider"
+ "_newAlertControllerForChangesDisabledForSpecifier:"
+ "appendString:"
+ "externalBrightnessSlider"
+ "externalBrightnessSliderTouchEnded:"
+ "removeTarget:action:forControlEvents:"
+ "setExternalBrightnessSlider:"
+ "stringWithString:"
+ "tableView:willSelectRowAtIndexPath:"
- "LIQUID_GLASS_SETTING_ACCESSIBILITY_FOOTER"

```
