## AssistantIsland

> `/System/Library/AccessibilityBundles/AssistantIsland.axbundle/AssistantIsland`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x18c
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__cstring: 0x6e
-  __TEXT.__unwind_info: 0x70
+3050.3.22.0.0
+  __TEXT.__text: 0x340
+  __TEXT.__objc_methlist: 0x68
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0xf7
+  __TEXT.__unwind_info: 0x88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48
-  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__objc_const: 0x1b0
   __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5
-  Symbols:   34
-  CStrings:  6
+  Functions: 11
+  Symbols:   60
+  CStrings:  14
 
Symbols:
+ +[StageViewAccessibility _accessibilityPerformValidations:]
+ +[StageViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[StageViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[StageViewAccessibility accessibilityPerformEscape]
+ -[StageViewAccessibility handleTapOutsideToDismiss:]
+ _AXPerformSafeBlock
+ _OBJC_CLASS_$_StageViewAccessibility
+ _OBJC_CLASS_$_UIAccessibilitySafeCategory
+ _OBJC_CLASS_$___StageViewAccessibility_super
+ _OBJC_METACLASS_$_StageViewAccessibility
+ _OBJC_METACLASS_$_UIAccessibilitySafeCategory
+ _OBJC_METACLASS_$___StageViewAccessibility_super
+ _UIAccessibilityPostNotification
+ _UIAccessibilityScreenChangedNotification
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_StageViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_StageViewAccessibility
+ __OBJC_CLASS_RO_$_StageViewAccessibility
+ __OBJC_CLASS_RO_$___StageViewAccessibility_super
+ __OBJC_METACLASS_RO_$_StageViewAccessibility
+ __OBJC_METACLASS_RO_$___StageViewAccessibility_super
+ ___52-[StageViewAccessibility accessibilityPerformEscape]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_retain_x2
Functions:
~ ___54+[AXAssistantIslandGlue accessibilityInitializeBundle]_block_invoke_3 : 4 -> 20
CStrings:
+ "@"
+ "AssistantIsland.StageView"
+ "StageViewAccessibility"
+ "UITapGestureRecognizer"
+ "dismissTapGestureRecognizer"
+ "handleTapOutsideToDismiss:"
+ "v"
+ "v8@?0"
```
