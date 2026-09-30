## ControlCenterUI

> `/System/iOSSupport/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/Contents/MacOS/ControlCenterUI`

```diff

-2948.2.0.0.0
-  __TEXT.__text: 0x19a4
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_methlist: 0x400
-  __TEXT.__cstring: 0x829
+2950.1.2.0.0
+  __TEXT.__text: 0x1eac
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_methlist: 0x4c0
+  __TEXT.__cstring: 0x992
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x469
-  __TEXT.__objc_methname: 0x648
-  __TEXT.__objc_methtype: 0x71
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_classname: 0x509
+  __TEXT.__objc_methname: 0x7d6
+  __TEXT.__objc_methtype: 0x79
+  __TEXT.__objc_stubs: 0x520
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x120
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0xcf0
-  __AUTH.__objc_data: 0x730
+  __AUTH_CONST.__cfstring: 0xa60
+  __AUTH_CONST.__objc_const: 0xf30
+  __AUTH.__objc_data: 0x870
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 76
-  Symbols:   294
-  CStrings:  82
+  Functions: 89
+  Symbols:   339
+  CStrings:  97
 
Symbols:
+ +[CCUIHeaderPocketViewAccessibility _accessibilityPerformValidations:]
+ +[CCUIHeaderPocketViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CCUIHeaderPocketViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CCUIPagingViewControllerAccessibility _accessibilityPerformValidations:]
+ +[CCUIPagingViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CCUIPagingViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[CCUIHeaderPocketViewAccessibility _accessibilityServesAsFirstElement]
+ -[CCUIHeaderPocketViewAccessibility _accessibilitySortPriority]
+ -[CCUIHeaderPocketViewAccessibility layoutSubviews]
+ -[CCUIPagingViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[CCUIPagingViewControllerAccessibility controlsGalleryViewControllerWillDismiss:]
+ -[CCUIPagingViewControllerAccessibility controlsGalleryViewControllerWillPresent:]
+ _OBJC_CLASS_$_CCUIHeaderPocketViewAccessibility
+ _OBJC_CLASS_$_CCUIPagingViewControllerAccessibility
+ _OBJC_CLASS_$___CCUIHeaderPocketViewAccessibility_super
+ _OBJC_CLASS_$___CCUIPagingViewControllerAccessibility_super
+ _OBJC_METACLASS_$_CCUIHeaderPocketViewAccessibility
+ _OBJC_METACLASS_$_CCUIPagingViewControllerAccessibility
+ _OBJC_METACLASS_$___CCUIHeaderPocketViewAccessibility_super
+ _OBJC_METACLASS_$___CCUIPagingViewControllerAccessibility_super
+ _UIApp
+ __OBJC_$_CLASS_METHODS_CCUIHeaderPocketViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CCUIPagingViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CCUIHeaderPocketViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_CCUIPagingViewControllerAccessibility
+ __OBJC_CLASS_RO_$_CCUIHeaderPocketViewAccessibility
+ __OBJC_CLASS_RO_$_CCUIPagingViewControllerAccessibility
+ __OBJC_CLASS_RO_$___CCUIHeaderPocketViewAccessibility_super
+ __OBJC_CLASS_RO_$___CCUIPagingViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_CCUIHeaderPocketViewAccessibility
+ __OBJC_METACLASS_RO_$_CCUIPagingViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___CCUIHeaderPocketViewAccessibility_super
+ __OBJC_METACLASS_RO_$___CCUIPagingViewControllerAccessibility_super
+ ___51-[CCUIHeaderPocketViewAccessibility layoutSubviews]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e14_"NSArray"8?0ls32l8s40l8
+ __block_literal_global.293
+ __block_literal_global.299
+ _objc_msgSend$_accessibilityStatusBarElements:sorted:
+ _objc_msgSend$_setAccessibilityServesAsFirstElement:
+ _objc_msgSend$axSafelyAddObjectsFromArray:
+ _objc_msgSend$setAccessibilityElementsBlock:
+ _objc_msgSend$setAccessibilityElementsHidden:
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$validateClass:hasSwiftField:withSwiftType:
+ _objc_release_x8
+ _objc_retain_x20
+ _objc_retain_x21
- __block_literal_global.289
- __block_literal_global.295
CStrings:
+ "@\"NSArray\"8@?0"
+ "CCUIHeaderPocketView"
+ "CCUIHeaderPocketViewAccessibility"
+ "CCUIPagingViewControllerAccessibility"
+ "CCUISControlsGalleryViewController"
+ "Optional<UIButton>"
+ "UIButton"
+ "addButton"
+ "control.center.add.controls"
+ "control.center.power"
+ "controlsGalleryViewControllerWillDismiss:"
+ "controlsGalleryViewControllerWillPresent:"
+ "editButton"
+ "powerButton"
+ "presentedViewController"

```
