## SpringBoard

> `/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`

```diff

-3050.3.0.0.0
-  __TEXT.__text: 0x390fc
-  __TEXT.__objc_methlist: 0x4d04
+3050.3.1.0.0
+  __TEXT.__text: 0x390b8
+  __TEXT.__objc_methlist: 0x4d0c
   __TEXT.__dlopen_cstrs: 0x98
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0xb50
-  __TEXT.__cstring: 0xa66e
+  __TEXT.__cstring: 0xa657
   __TEXT.__oslogstring: 0x9fb
   __TEXT.__unwind_info: 0x1718
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2628
+  __DATA_CONST.__objc_selrefs: 0x2630
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x5d0
-  __AUTH_CONST.__const: 0x790
+  __AUTH_CONST.__const: 0x770
   __AUTH_CONST.__cfstring: 0xbc20
   __AUTH_CONST.__objc_const: 0xb390
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xd70
+  __AUTH.__objc_data: 0xb90
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x248
   __DATA.__common: 0x11
-  __DATA_DIRTY.__objc_data: 0x50f0
+  __DATA_DIRTY.__objc_data: 0x52d0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1619
-  Symbols:   4758
+  Symbols:   4759
   CStrings:  1666
 
Symbols:
+ -[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]
+ ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke
+ ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke_2
+ ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke_3
+ _objc_msgSend$_accessibilityElementsForStatusBar:sorted:
- ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_6
- ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_7
- ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_8
- ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_9
Functions:
~ +[SBDeviceApplicationCounterRotatableSceneOverlayViewAccessibility _accessibilityPerformValidations:] : 208 -> 232
~ -[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:] : 3804 -> 3708
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_4 : 436 -> 272
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_5 : 96 -> 84
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_6 -> -[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:] : 8 -> 272
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_7 -> ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke : 16 -> 184
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_8 -> ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke_2 : 272 -> 96
~ ___82-[SpringBoardAccessibility _accessibilityStatusBarElements:sorted:forWindowScene:]_block_invoke_9 -> ___70-[SpringBoardAccessibility _accessibilityElementsForStatusBar:sorted:]_block_invoke_3 : 84 -> 8
CStrings:
+ "SBSceneView"
- "AXStatusBarHasSyntheticElementsKey"
```
