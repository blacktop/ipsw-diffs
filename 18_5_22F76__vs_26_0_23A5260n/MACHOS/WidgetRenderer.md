## WidgetRenderer

> `/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer`

```diff

-2963.10.30.1.0
-  __TEXT.__text: 0x774
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x114
-  __TEXT.__cstring: 0x269
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x3cd
+2994.2.0.0.0
+  __TEXT.__text: 0xeb8
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x440
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__cstring: 0x3d1
+  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__objc_methname: 0x500
   __TEXT.__objc_methtype: 0x4c
-  __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x480
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x3f0
-  __DATA.__objc_selrefs: 0x118
-  __DATA.__objc_data: 0x230
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x510
+  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_data: 0x2d0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB0513AA-0397-3E9C-AD11-43F9C1A415DA
-  Functions: 21
-  Symbols:   122
-  CStrings:  103
+  UUID: A696C956-18F5-3E0D-B067-F68FA815F214
+  Functions: 32
+  Symbols:   167
+  CStrings:  141
 
Symbols:
+ +[SystemApertureElementViewControllerAccessibility _accessibilityPerformValidations:]
+ +[SystemApertureElementViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SystemApertureElementViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[SystemApertureElementViewControllerAccessibility _accessibilityApertureLayoutMode]
+ -[SystemApertureElementViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[SystemApertureElementViewControllerAccessibility addChildViewController:]
+ -[SystemApertureElementViewControllerAccessibility updateSystemApertureElements]
+ GCC_except_table5
+ _OBJC_CLASS_$_SystemApertureElementViewControllerAccessibility
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_CLASS_$___SystemApertureElementViewControllerAccessibility_super
+ _OBJC_METACLASS_$_SystemApertureElementViewControllerAccessibility
+ _OBJC_METACLASS_$___SystemApertureElementViewControllerAccessibility_super
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_SystemApertureElementViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_SystemApertureElementViewControllerAccessibility
+ __OBJC_CLASS_RO_$_SystemApertureElementViewControllerAccessibility
+ __OBJC_CLASS_RO_$___SystemApertureElementViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_SystemApertureElementViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___SystemApertureElementViewControllerAccessibility_super
+ __Unwind_Resume
+ ___80-[SystemApertureElementViewControllerAccessibility updateSystemApertureElements]_block_invoke
+ ___80-[SystemApertureElementViewControllerAccessibility updateSystemApertureElements]_block_invoke_2
+ ___80-[SystemApertureElementViewControllerAccessibility updateSystemApertureElements]_block_invoke_3
+ ___80-[SystemApertureElementViewControllerAccessibility updateSystemApertureElements]_block_invoke_4
+ ___UIAccessibilityCastAsClass
+ ___UIAccessibilitySafeClass
+ ___block_descriptor_40_e8_32w_e5_B8?0lw32l8
+ ___objc_personality_v0
+ __block_literal_global.279
+ __block_literal_global.288
+ _abort
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_accessibilityApertureLayoutMode
+ _objc_msgSend$_accessibilityWindowScene
+ _objc_msgSend$_setAccessibilityElementsHiddenBlock:
+ _objc_msgSend$safeIntForKey:
+ _objc_msgSend$safeSwiftValueForKey:
+ _objc_msgSend$updateSystemApertureElements
+ _objc_msgSend$validateClass:hasSwiftField:withSwiftType:
+ _objc_msgSend$validateClass:isKindOfClass:
+ _objc_msgSend$view
+ _objc_release_x24
+ _objc_release_x25
- __block_literal_global.276
- __block_literal_global.285
CStrings:
+ "B8@?0"
+ "Optional<_JindoAccessoryViewController>"
+ "SBUISystemApertureElementSource"
+ "SystemApertureElementViewControllerAccessibility"
+ "UIViewController"
+ "UIWindowScene"
+ "WidgetRenderer.SystemApertureElementViewController"
+ "__SystemApertureElementViewControllerAccessibility_super"
+ "_accessibilityApertureLayoutMode"
+ "_accessibilityLoadAccessibilityInformation"
+ "_accessibilityWindowScene"
+ "_setAccessibilityElementsHiddenBlock:"
+ "addChildViewController:"
+ "expandedUIHostingController"
+ "layoutMode"
+ "leadingUIHostingController"
+ "minimalUIHostingController"
+ "q"
+ "safeIntForKey:"
+ "safeSwiftValueForKey:"
+ "systemApertureElementSource"
+ "trailingUIHostingController"
+ "updateSystemApertureElements"
+ "validateClass:hasSwiftField:withSwiftType:"
+ "validateClass:isKindOfClass:"
+ "view"

```
