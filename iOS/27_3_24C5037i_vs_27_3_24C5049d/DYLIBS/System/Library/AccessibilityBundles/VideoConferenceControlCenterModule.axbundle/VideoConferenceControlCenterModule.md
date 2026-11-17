## VideoConferenceControlCenterModule

> `/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0xc94
-  __TEXT.__objc_methlist: 0x1e0
+3050.3.22.0.0
+  __TEXT.__text: 0x1358
+  __TEXT.__objc_methlist: 0x228
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x33c
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__cstring: 0x3d5
   __TEXT.__oslogstring: 0x50
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0x110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a0
+  __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__objc_const: 0x538
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 46
-  Symbols:   162
-  CStrings:  37
+  Functions: 54
+  Symbols:   182
+  CStrings:  48
 
Symbols:
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility _accessibilityLoadAccessibilityInformation]
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility _axIsExpandable]
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility _axToggleEffect]
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility _axUpdateButtonGlyph]
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility accessibilityActivate]
+ -[VideoConferenceControlCenterModuleEffectControlAccessibility setSelected:]
+ GCC_except_table33
+ _OBJC_CLASS_$_UIControl
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UISwitch
+ _OBJC_IVAR_$_AXReplayKitClientDelegate._didDisableScreenCurtain
+ _UIAccessibilityTraitSelected
+ __AXSVoiceOverTouchScreenCurtainEnabled
+ __AXSVoiceOverTouchSetScreenCurtainEnabled
+ __OBJC_$_INSTANCE_VARIABLES_AXReplayKitClientDelegate
+ ___106-[VideoConferenceControlCenterModuleEffectControlAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___79-[VideoConferenceControlCenterModuleEffectControlAccessibility _axToggleEffect]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e5_B8?0lw32l8
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
- ___kCFBooleanFalse
- ___kCFBooleanTrue
CStrings:
+ "B8@?0"
+ "UIControl"
+ "UILabel"
+ "autoColorLabel"
+ "autoColorToggle"
+ "buttonGlyph"
+ "collapse.button.label"
+ "effectTitleLabel"
+ "imageBackgroundView"
+ "isSelected"
+ "multiExpandable"
```
