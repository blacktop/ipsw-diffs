## HeadphoneSettingsUI

> `/System/Library/AccessibilityBundles/HeadphoneSettingsUI.axbundle/HeadphoneSettingsUI`

```diff

-3005.25.0.0.0
-  __TEXT.__text: 0x694
-  __TEXT.__auth_stubs: 0x160
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x188
+3005.27.0.0.0
+  __TEXT.__text: 0xd28
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0xec
   __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x332
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methname: 0x2fe
-  __TEXT.__objc_methtype: 0x2e
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x88
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_classname: 0xef
+  __TEXT.__objc_methname: 0x3b9
+  __TEXT.__objc_methtype: 0x39
+  __TEXT.__objc_stubs: 0x360
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH.__objc_data: 0x190
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F250DCE6-FEDB-3026-A4DE-DFA5794B990D
-  Functions: 14
-  Symbols:   109
-  CStrings:  73
+  UUID: 85A48F8D-BF76-3A46-8DAF-B4BF05DD3E9C
+  Functions: 23
+  Symbols:   159
+  CStrings:  125
 
Symbols:
+ +[HPSUISpatialProfileEnrollmentControllerAccessibility _accessibilityPerformValidations:]
+ +[HPSUISpatialProfileEnrollmentControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[HPSUISpatialProfileEnrollmentControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[HPSUISpatialProfileEnrollmentControllerAccessibility _axContinueButton]
+ -[HPSUISpatialProfileEnrollmentControllerAccessibility moveToStep:]
+ -[HPSUISpatialProfileEnrollmentControllerAccessibility viewWillLayoutSubviews]
+ _OBJC_CLASS_$_HPSUISpatialProfileEnrollmentControllerAccessibility
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_CLASS_$___HPSUISpatialProfileEnrollmentControllerAccessibility_super
+ _OBJC_METACLASS_$_HPSUISpatialProfileEnrollmentControllerAccessibility
+ _OBJC_METACLASS_$___HPSUISpatialProfileEnrollmentControllerAccessibility_super
+ _UIAccessibilityLayoutChangedNotification
+ _UIAccessibilityPostNotification
+ _UIAccessibilityScreenChangedNotification
+ _UIAccessibilitySpeakAndDoNotBeInterrupted
+ __OBJC_$_CLASS_METHODS_HPSUISpatialProfileEnrollmentControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_HPSUISpatialProfileEnrollmentControllerAccessibility
+ __OBJC_CLASS_RO_$_HPSUISpatialProfileEnrollmentControllerAccessibility
+ __OBJC_CLASS_RO_$___HPSUISpatialProfileEnrollmentControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_HPSUISpatialProfileEnrollmentControllerAccessibility
+ __OBJC_METACLASS_RO_$___HPSUISpatialProfileEnrollmentControllerAccessibility_super
+ ___67-[HPSUISpatialProfileEnrollmentControllerAccessibility moveToStep:]_block_invoke
+ ___67-[HPSUISpatialProfileEnrollmentControllerAccessibility moveToStep:]_block_invoke_2
+ ___67-[HPSUISpatialProfileEnrollmentControllerAccessibility moveToStep:]_block_invoke_3
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ __dispatch_main_q
+ _dispatch_async
+ _objc_msgSend$_accessibilitySetPearlEnrollViewController:
+ _objc_msgSend$_axContinueButton
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$safeIntegerForKey:
+ _objc_msgSend$safeStringForKey:
+ _objc_msgSend$validateClass:isKindOfClass:
+ _objc_opt_isKindOfClass
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain_x23
CStrings:
+ "@"
+ "BKUIPearlEnrollView"
+ "BKUIPearlPillContainerView"
+ "HPSUISpatialProfileEnrollmentController"
+ "HPSUISpatialProfileEnrollmentControllerAccessibility"
+ "HPSUISpatialProfileUIPearlEnrollView"
+ "NSObject<OS_dispatch_queue>"
+ "OBHeaderView"
+ "OBTemplateHeaderDetailLabel"
+ "OBTrayButton"
+ "UILabel"
+ "UIViewController"
+ "__HPSUISpatialProfileEnrollmentControllerAccessibility_super"
+ "_accessibilitySetPearlEnrollViewController:"
+ "_axContinueButton"
+ "_continueButton"
+ "_currentStep"
+ "_enrollView"
+ "_infoView"
+ "_pillContainer"
+ "_previousStep"
+ "_stepSerialQueue"
+ "detailLabel"
+ "moveToStep:"
+ "pillContainer"
+ "presentedViewController"
+ "safeIntegerForKey:"
+ "safeStringForKey:"
+ "text"
+ "v20@0:8i16"
+ "validateClass:isKindOfClass:"
+ "viewWillLayoutSubviews"

```
