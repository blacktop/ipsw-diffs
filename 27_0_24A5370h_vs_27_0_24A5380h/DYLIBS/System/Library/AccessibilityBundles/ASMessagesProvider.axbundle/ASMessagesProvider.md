## ASMessagesProvider

> `/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider`

```diff

-  __TEXT.__text: 0xb428
-  __TEXT.__objc_methlist: 0x270c
+  __TEXT.__text: 0xb424
+  __TEXT.__objc_methlist: 0x2724
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x3cd5
+  __TEXT.__cstring: 0x3c7b
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x670
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__objc_classlist: 0x698
+  __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__got: 0x128
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x39a0
-  __AUTH_CONST.__objc_const: 0x76b0
+  __AUTH_CONST.__cfstring: 0x3940
+  __AUTH_CONST.__objc_const: 0x77d0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x41f0
+  __AUTH.__objc_data: 0x4290
   __DATA.__bss: 0x12
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 654
-  Symbols:   2613
-  CStrings:  964
+  Symbols:   2624
+  CStrings:  958
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
Symbols:
+ +[JULoadingViewControllerAccessibility _accessibilityPerformValidations:]
+ +[JULoadingViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[JULoadingViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[JULoadingViewControllerAccessibility _axRecursivelyHideSubtreeOfView:]
+ -[JULoadingViewControllerAccessibility viewDidLayoutSubviews]
+ _OBJC_CLASS_$_JULoadingViewControllerAccessibility
+ _OBJC_CLASS_$___JULoadingViewControllerAccessibility_super
+ _OBJC_METACLASS_$_JULoadingViewControllerAccessibility
+ _OBJC_METACLASS_$___JULoadingViewControllerAccessibility_super
+ __OBJC_$_CLASS_METHODS_JULoadingViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_JULoadingViewControllerAccessibility
+ __OBJC_CLASS_RO_$_JULoadingViewControllerAccessibility
+ __OBJC_CLASS_RO_$___JULoadingViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_JULoadingViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___JULoadingViewControllerAccessibility_super
+ _objc_msgSend$_axRecursivelyHideSubtreeOfView:
+ _objc_msgSend$setAccessibilityElementsHidden:
+ _objc_msgSend$superview
- -[AnnotationCollectionViewCellAccessibility _accessibilityOverridesInstructionsHint]
- -[AnnotationCollectionViewCellAccessibility _axIsAnnotationCellExpanded]
- -[AnnotationCollectionViewCellAccessibility _axIsSummaryExpandable]
- -[AnnotationCollectionViewCellAccessibility accessibilityHint]
- -[AnnotationCollectionViewCellAccessibility accessibilityTraits]
- _objc_msgSend$_axIsAnnotationCellExpanded
- _objc_msgSend$_axIsSummaryExpandable
Functions:
~ +[AppUpdatesDetailCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 216
~ -[AppUpdatesDetailCollectionViewCellAccessibility accessibilityTraits] : 72 -> 128
~ +[AlertActionTrailingImageViewAccessibility _accessibilityPerformValidations:] -> +[JULoadingViewControllerAccessibility _accessibilityPerformValidations:] : 64 -> 24
~ -[AlertActionTrailingImageViewAccessibility isAccessibilityElement] -> -[JULoadingViewControllerAccessibility _axRecursivelyHideSubtreeOfView:] : 8 -> 308
~ -[AlertActionTrailingImageViewAccessibility accessibilityLabel] -> -[JULoadingViewControllerAccessibility viewDidLayoutSubviews] : 12 -> 184
~ -[AlertActionTrailingImageViewAccessibility accessibilityTraits] -> +[AlertActionTrailingImageViewAccessibility(SafeCategory) safeCategoryTargetClassName] : 72 -> 12
~ +[AnnotationCollectionViewCellAccessibility(SafeCategory) safeCategoryBaseClass] -> +[AlertActionTrailingImageViewAccessibility _accessibilityPerformValidations:] : 12 -> 64
~ +[AnnotationCollectionViewCellAccessibility _accessibilityPerformValidations:] -> -[AlertActionTrailingImageViewAccessibility isAccessibilityElement] : 288 -> 8
~ -[AnnotationCollectionViewCellAccessibility isAccessibilityElement] -> -[AlertActionTrailingImageViewAccessibility accessibilityLabel] : 8 -> 12
~ -[AnnotationCollectionViewCellAccessibility accessibilityLabel] -> -[AlertActionTrailingImageViewAccessibility accessibilityTraits] : 200 -> 72
~ -[AnnotationCollectionViewCellAccessibility accessibilityCustomActions] -> +[AnnotationCollectionViewCellAccessibility _accessibilityPerformValidations:] : 248 -> 188
~ -[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:] -> -[AnnotationCollectionViewCellAccessibility isAccessibilityElement] : 112 -> 8
~ ___77-[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:]_block_invoke -> -[AnnotationCollectionViewCellAccessibility accessibilityLabel] : 8 -> 12
~ -[AnnotationCollectionViewCellAccessibility accessibilityTraits] -> -[AnnotationCollectionViewCellAccessibility accessibilityCustomActions] : 116 -> 236
~ -[AnnotationCollectionViewCellAccessibility accessibilityHint] -> -[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:] : 128 -> 112
~ -[AnnotationCollectionViewCellAccessibility _accessibilityOverridesInstructionsHint] -> ___77-[AnnotationCollectionViewCellAccessibility _accessibilityPerformLinkAction:]_block_invoke : 64 -> 8
CStrings:
+ "JULoadingViewControllerAccessibility"
+ "JetUI.JULoadingViewController"
- "AppUpdatesDetailCollectionViewCellAccessibility"
- "accessibilityCellIsExpanded"
- "accessibilityDetailItems"
- "accessibilityIsSummaryExpandable"
- "expand.annotation.cell"

```
