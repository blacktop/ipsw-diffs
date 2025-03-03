## ClockAngel

> `/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel`

```diff

-2963.10.3.0.0
-  __TEXT.__text: 0x70c
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0xb8
-  __TEXT.__cstring: 0x209
-  __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x3ae
+2963.10.8.0.0
+  __TEXT.__text: 0xdec
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x148
+  __TEXT.__cstring: 0x417
+  __TEXT.__objc_classname: 0x184
+  __TEXT.__objc_methname: 0x410
   __TEXT.__objc_methtype: 0x3b
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__cfstring: 0x260
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x2d0
-  __DATA.__objc_selrefs: 0xf8
-  __DATA.__objc_data: 0x190
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0x510
+  __DATA.__objc_selrefs: 0x120
+  __DATA.__objc_data: 0x2d0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21
-  Symbols:   118
-  CStrings:  70
+  Functions: 33
+  Symbols:   170
+  CStrings:  106
 
Symbols:
+ +[SecureStopwatchControllerAccessibility _accessibilityPerformValidations:]
+ +[SecureStopwatchControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SecureStopwatchControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[StopwatchApertureControllerAccessibility _accessibilityPerformValidations:]
+ +[StopwatchApertureControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[StopwatchApertureControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[StopwatchApertureControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ GCC_except_table3
+ _OBJC_CLASS_$_CALayer
+ _OBJC_CLASS_$_CAStateController
+ _OBJC_CLASS_$_SecureStopwatchControllerAccessibility
+ _OBJC_CLASS_$_StopwatchApertureControllerAccessibility
+ _OBJC_CLASS_$___SecureStopwatchControllerAccessibility_super
+ _OBJC_CLASS_$___StopwatchApertureControllerAccessibility_super
+ _OBJC_METACLASS_$_SecureStopwatchControllerAccessibility
+ _OBJC_METACLASS_$_StopwatchApertureControllerAccessibility
+ _OBJC_METACLASS_$___SecureStopwatchControllerAccessibility_super
+ _OBJC_METACLASS_$___StopwatchApertureControllerAccessibility_super
+ __OBJC_$_CLASS_METHODS_SecureStopwatchControllerAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_StopwatchApertureControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_SecureStopwatchControllerAccessibility
+ __OBJC_$_INSTANCE_METHODS_StopwatchApertureControllerAccessibility
+ __OBJC_CLASS_RO_$_SecureStopwatchControllerAccessibility
+ __OBJC_CLASS_RO_$_StopwatchApertureControllerAccessibility
+ __OBJC_CLASS_RO_$___SecureStopwatchControllerAccessibility_super
+ __OBJC_CLASS_RO_$___StopwatchApertureControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_SecureStopwatchControllerAccessibility
+ __OBJC_METACLASS_RO_$_StopwatchApertureControllerAccessibility
+ __OBJC_METACLASS_RO_$___SecureStopwatchControllerAccessibility_super
+ __OBJC_METACLASS_RO_$___StopwatchApertureControllerAccessibility_super
+ __Unwind_Resume
+ ___84-[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___84-[SecureStopwatchControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___86-[StopwatchApertureControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___86-[StopwatchApertureControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___UIAccessibilityCastAsClass
+ ___UIAccessibilitySafeClass
+ ___block_descriptor_40_e8_32w_e15_"NSString"8?0lw32l8
+ ___objc_personality_v0
+ __block_literal_global.276
+ __block_literal_global.285
+ __block_literal_global.290
+ __block_literal_global.296
+ __block_literal_global.298
+ __block_literal_global.300
+ _abort
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$name
+ _objc_msgSend$safeSwiftEnumCase
+ _objc_msgSend$safeValueForKey:
+ _objc_msgSend$stateOfLayer:
+ _objc_msgSend$validateClass:hasInstanceVariable:withType:
- __block_literal_global.279
- __block_literal_global.288
- __block_literal_global.299
- __block_literal_global.301
- __block_literal_global.303
CStrings:
+ "BSUICAPackageView"
+ "CALayer"
+ "CAStateController"
+ "ClockAngel.SecureStopwatchController"
+ "ClockAngel.SpinnyResetView"
+ "ClockAngel.SpinnyResetView.Mode"
+ "ClockAngel.StopwatchApertureController"
+ "Mode"
+ "Optional<BSUICAPackageView>"
+ "Optional<SpinnyResetView>"
+ "Optional<UIView & SBUISystemApertureAccessoryView>"
+ "SecureStopwatchControllerAccessibility"
+ "StopwatchApertureControllerAccessibility"
+ "__SecureStopwatchControllerAccessibility_super"
+ "__StopwatchApertureControllerAccessibility_super"
+ "_rootLayer"
+ "_stateController"
+ "cancel"
+ "cancel.button"
+ "lap"
+ "lap.button"
+ "lapCancelButton"
+ "leadingView"
+ "minimalView"
+ "mode"
+ "name"
+ "pausePlayPackage"
+ "play"
+ "safeSwiftEnumCase"
+ "safeValueForKey:"
+ "spinnyResetView"
+ "stateOfLayer:"
+ "stopwatch"
+ "validateClass:hasInstanceVariable:withType:"

```
