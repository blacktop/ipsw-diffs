## ShortcutsUI

> `/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI`

```diff

-  __TEXT.__text: 0x468
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x163
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__text: 0x978
+  __TEXT.__objc_methlist: 0x13c
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x26c
+  __TEXT.__unwind_info: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__objc_selrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x3e0
+  __AUTH_CONST.__objc_const: 0x3f0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x230
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   82
-  CStrings:  36
+  Functions: 25
+  Symbols:   144
+  CStrings:  67
 
Sections:
~ __AUTH_CONST.__const : content changed
Symbols:
+ +[WFEggTimerControlAccessibility _accessibilityPerformValidations:]
+ +[WFEggTimerControlAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[WFEggTimerControlAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[WFEggTimerViewControllerAccessibility _accessibilityPerformValidations:]
+ +[WFEggTimerViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[WFEggTimerViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[WFEggTimerControlAccessibility _axAdjustTimerValueForward:]
+ -[WFEggTimerControlAccessibility accessibilityDecrement]
+ -[WFEggTimerControlAccessibility accessibilityElements]
+ -[WFEggTimerControlAccessibility accessibilityIncrement]
+ -[WFEggTimerControlAccessibility accessibilityLabel]
+ -[WFEggTimerControlAccessibility accessibilityTraits]
+ -[WFEggTimerControlAccessibility accessibilityValue]
+ -[WFEggTimerControlAccessibility isAccessibilityElement]
+ -[WFEggTimerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ _AXDurationStringForDurationWithSeconds
+ _AXPerformSafeBlock
+ _OBJC_CLASS_$_WFEggTimerControlAccessibility
+ _OBJC_CLASS_$_WFEggTimerViewControllerAccessibility
+ _OBJC_CLASS_$___WFEggTimerControlAccessibility_super
+ _OBJC_CLASS_$___WFEggTimerViewControllerAccessibility_super
+ _OBJC_METACLASS_$_WFEggTimerControlAccessibility
+ _OBJC_METACLASS_$_WFEggTimerViewControllerAccessibility
+ _OBJC_METACLASS_$___WFEggTimerControlAccessibility_super
+ _OBJC_METACLASS_$___WFEggTimerViewControllerAccessibility_super
+ _UIAccessibilityTraitAdjustable
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_WFEggTimerControlAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_WFEggTimerViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_WFEggTimerControlAccessibility
+ __OBJC_$_INSTANCE_METHODS_WFEggTimerViewControllerAccessibility
+ __OBJC_CLASS_RO_$_WFEggTimerControlAccessibility
+ __OBJC_CLASS_RO_$_WFEggTimerViewControllerAccessibility
+ __OBJC_CLASS_RO_$___WFEggTimerControlAccessibility_super
+ __OBJC_CLASS_RO_$___WFEggTimerViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_WFEggTimerControlAccessibility
+ __OBJC_METACLASS_RO_$_WFEggTimerViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___WFEggTimerControlAccessibility_super
+ __OBJC_METACLASS_RO_$___WFEggTimerViewControllerAccessibility_super
+ ___61-[WFEggTimerControlAccessibility _axAdjustTimerValueForward:]_block_invoke
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$_axAdjustTimerValueForward:
+ _objc_msgSend$safeDoubleForKey:
+ _objc_msgSend$setCurrentValue:
+ _objc_msgSend$validateClass:isKindOfClass:
+ _objc_msgSend$valueChangedHandler
Functions:
~ ___50+[AXShortcutsUIGlue accessibilityInitializeBundle]_block_invoke_3 : 20 -> 112
CStrings:
+ "UIControl"
+ "WFEggTimerControl"
+ "WFEggTimerControlAccessibility"
+ "WFEggTimerViewController"
+ "WFEggTimerViewControllerAccessibility"
+ "currentValue"
+ "d"
+ "durationValueLabel"
+ "egg.timer.control.label"
+ "rangeMax"
+ "rangeMin"
+ "setCurrentValue:"
+ "stepSize"
+ "timerControl"
+ "v"
+ "v8@?0"
+ "valueChangedHandler"

```
