## CarPlay

> `/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay`

```diff

-3048.0.0.0.0
-  __TEXT.__text: 0x6c8
-  __TEXT.__objc_methlist: 0xe4
-  __TEXT.__cstring: 0x146
-  __TEXT.__unwind_info: 0xa0
+3050.3.0.0.0
+  __TEXT.__text: 0x214
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__cstring: 0x60
+  __TEXT.__unwind_info: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x48
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x310
+  __DATA_CONST.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x20
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0xd0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 19
-  Symbols:   118
-  CStrings:  19
+  Functions: 9
+  Symbols:   56
+  CStrings:  6
 
Symbols:
- +[CARFolderViewAccessibility _accessibilityPerformValidations:]
- +[CARFolderViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[CARFolderViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[CARIconScrollViewAccessibility _accessibilityPerformValidations:]
- +[CARIconScrollViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[CARIconScrollViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[CARFolderViewAccessibility _accessibilityUserTestingChildrenFromSBRootFolderView]
- -[CARFolderViewAccessibility automationElements]
- -[CARIconScrollViewAccessibility automationElements]
- _AXGuaranteedMutableArray
- _AXSafeClassFromString
- _OBJC_CLASS_$_CARFolderViewAccessibility
- _OBJC_CLASS_$_CARIconScrollViewAccessibility
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_UIAccessibilitySafeCategory
- _OBJC_CLASS_$_UIView
- _OBJC_CLASS_$_UIViewController
- _OBJC_CLASS_$___CARFolderViewAccessibility_super
- _OBJC_CLASS_$___CARIconScrollViewAccessibility_super
- _OBJC_METACLASS_$_CARFolderViewAccessibility
- _OBJC_METACLASS_$_CARIconScrollViewAccessibility
- _OBJC_METACLASS_$_UIAccessibilitySafeCategory
- _OBJC_METACLASS_$___CARFolderViewAccessibility_super
- _OBJC_METACLASS_$___CARIconScrollViewAccessibility_super
- __OBJC_$_CLASS_METHODS_CARFolderViewAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_CARIconScrollViewAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_CARFolderViewAccessibility
- __OBJC_$_INSTANCE_METHODS_CARIconScrollViewAccessibility
- __OBJC_CLASS_RO_$_CARFolderViewAccessibility
- __OBJC_CLASS_RO_$_CARIconScrollViewAccessibility
- __OBJC_CLASS_RO_$___CARFolderViewAccessibility_super
- __OBJC_CLASS_RO_$___CARIconScrollViewAccessibility_super
- __OBJC_METACLASS_RO_$_CARFolderViewAccessibility
- __OBJC_METACLASS_RO_$_CARIconScrollViewAccessibility
- __OBJC_METACLASS_RO_$___CARFolderViewAccessibility_super
- __OBJC_METACLASS_RO_$___CARIconScrollViewAccessibility_super
- ___52-[CARIconScrollViewAccessibility automationElements]_block_invoke
- ___UIAccessibilityCastAsClass
- ___UIAccessibilityCastAsSafeCategory
- ___block_descriptor_32_e8_B16?08l
- _abort
- _objc_msgSend$_accessibilityAncestorIsKindOf:
- _objc_msgSend$_accessibilityFindAncestor:startWithSelf:
- _objc_msgSend$_accessibilityViewController
- _objc_msgSend$automationElements
- _objc_msgSend$axArrayByIgnoringNilElementsWithCount:
- _objc_msgSend$axArrayWithPossiblyNilArrays:
- _objc_msgSend$installSafeCategory:canInteractWithTargetClass:
- _objc_msgSend$removeObject:
- _objc_msgSend$safeValueForKey:
- _objc_msgSend$subviews
- _objc_msgSend$validateClass:
- _objc_msgSend$validateClass:hasInstanceMethod:withFullSignature:
- _objc_msgSend$validateClass:isKindOfClass:
- _objc_msgSend$view
- _objc_opt_isKindOfClass
- _objc_release
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_retain_x2
Functions:
~ ___46+[AXCarPlayGlue accessibilityInitializeBundle]_block_invoke_3 : 80 -> 4
CStrings:
- "@"
- "B16@?0@8"
- "CARFolderViewAccessibility"
- "CARIconScrollViewAccessibility"
- "DBFolderView"
- "DBIconScrollView"
- "DBTodayViewController"
- "DashBoard.DBDashboardHomeViewController"
- "SBFolderView"
- "UIView"
- "UIViewController"
- "pageControl"
- "todayViewController"
```
