## MobileSafariUI

> `/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI`

```diff

-  __TEXT.__text: 0xadbc
-  __TEXT.__objc_methlist: 0xe18
+  __TEXT.__text: 0xa4e0
+  __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__cstring: 0x2490
+  __TEXT.__cstring: 0x2399
   __TEXT.__oslogstring: 0x80
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x320
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
-  __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__objc_selrefs: 0x788
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x2788
+  __AUTH_CONST.__cfstring: 0x2d40
+  __AUTH_CONST.__objc_const: 0x2668
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x690
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 288
-  Symbols:   1302
-  CStrings:  805
+  Functions: 274
+  Symbols:   1254
+  CStrings:  769
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ -[UnifiedTabBarAccessibility _setResolvedItemArrangement:animated:andScrollTo:completionHandler:]
+ GCC_except_table251
+ GCC_except_table260
- +[TabBarItemViewAccessibility _accessibilityPerformValidations:]
- +[TabBarItemViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[TabBarItemViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[TabBarItemViewAccessibility _accessibilityHitTest:withEvent:]
- -[TabBarItemViewAccessibility _accessibilityIsSpeakThisElement]
- -[TabBarItemViewAccessibility _accessibilityLoadAccessibilityInformation]
- -[TabBarItemViewAccessibility _accessibilityUpdateAXInfo]
- -[TabBarItemViewAccessibility accessibilityLabel]
- -[TabBarItemViewAccessibility isAccessibilityElement]
- -[TabBarItemViewAccessibility setActive:]
- -[TabBarItemViewAccessibility setFrame:]
- -[TabBarItemViewAccessibility setPinned:]
- -[TabBarItemViewAccessibility setTitleText:]
- -[TabControllerAccessibility _axTabBarItemViewForTabDocument:]
- -[UnifiedTabBarAccessibility _setResolvedItemArrangement:animated:keepingItemVisible:completionHandler:]
- GCC_except_table265
- GCC_except_table274
- _CGRectContainsPoint
- _OBJC_CLASS_$_TabBarItemViewAccessibility
- _OBJC_CLASS_$___TabBarItemViewAccessibility_super
- _OBJC_METACLASS_$_TabBarItemViewAccessibility
- _OBJC_METACLASS_$___TabBarItemViewAccessibility_super
- _UIAccessibilityFrameForBounds
- _UIAccessibilityPointForPoint
- _UIAccessibilityTraitSelected
- __OBJC_$_CLASS_METHODS_TabBarItemViewAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_TabBarItemViewAccessibility
- __OBJC_CLASS_RO_$_TabBarItemViewAccessibility
- __OBJC_CLASS_RO_$___TabBarItemViewAccessibility_super
- __OBJC_METACLASS_RO_$_TabBarItemViewAccessibility
- __OBJC_METACLASS_RO_$___TabBarItemViewAccessibility_super
- _objc_msgSend$_accessibilityParentView
- _objc_msgSend$_accessibilityUpdateAXInfo
- _objc_msgSend$accessibilityFrame
- _objc_msgSend$setAccessibilityFrame:
- _objc_msgSend$setAccessibilityRespondsToUserInteraction:
- _objc_msgSend$setIsAccessibilityElement:
CStrings:
+ "_setResolvedItemArrangement:animated:andScrollTo:completionHandler:"
- "TabBarItem"
- "TabBarItemLayoutInfo"
- "TabBarItemView"
- "TabBarItemViewAccessibility"
- "_isPinnedAndNarrow"
- "_setResolvedItemArrangement:animated:keepingItemVisible:completionHandler:"
- "_tabBarItem"
- "_titleLabel"
- "_titleText"
- "close.tab"
- "closeButton"
- "isPinned"
- "layoutInfo"
- "setPinned:"
- "setTitleText:"
- "tab.hint"
- "tab.pinned"
- "tab.view"
- "tabBarItemView"

```
