## AccessibilityFoundation

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityFoundation.framework/Versions/A/AccessibilityFoundation`

```diff

-453.0.0.0.0
-  __TEXT.__text: 0x49a64
-  __TEXT.__objc_methlist: 0x6ca4
+455.1.5.0.0
+  __TEXT.__text: 0x49ee4
+  __TEXT.__objc_methlist: 0x6d14
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x4d5f
-  __TEXT.__oslogstring: 0xe34
+  __TEXT.__cstring: 0x4dc2
+  __TEXT.__oslogstring: 0xec3
   __TEXT.__gcc_except_tab: 0x35c
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__dof_Accessibi: 0x609
-  __TEXT.__unwind_info: 0x1660
+  __TEXT.__unwind_info: 0x1690
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fc8
+  __DATA_CONST.__objc_selrefs: 0x3fe8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__got: 0x618
-  __AUTH_CONST.__const: 0x1110
+  __AUTH_CONST.__const: 0x1150
   __AUTH_CONST.__cfstring: 0x6a80
-  __AUTH_CONST.__objc_const: 0xb370
+  __AUTH_CONST.__objc_const: 0xb420
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1568
-  __AUTH.__data: 0x58
+  __AUTH.__data: 0x60
   __DATA.__objc_ivar: 0x3f0
   __DATA.__data: 0x540
-  __DATA.__bss: 0x4b0
+  __DATA.__bss: 0x4c8
   __DATA_DIRTY.__objc_data: 0x208
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accessibility.framework/Versions/A/Accessibility

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2648
-  Symbols:   5627
-  CStrings:  999
+  Functions: 2665
+  Symbols:   5647
+  CStrings:  1003
 
Symbols:
+ -[AXFMouse obscureCursorInPlace]
+ -[AXFMouse warpToLocation:keepCursorObscured:]
+ -[AXFMouseTest obscureCursorInPlace]
+ -[AXFMouseTest warpToLocation:keepCursorObscured:]
+ -[AXFUIElement accessibilityLabelOrTitle]
+ -[AXFUIElement hasAccessibilityLabelOrTitle]
+ -[_AXFMouseHardware obscureCursorInPlace]
+ -[_AXFMouseHardware warpToLocation:keepCursorObscured:]
+ GCC_except_table310
+ GCC_except_table367
+ SkyLightLibrary.sLib
+ SkyLightLibrary.sOnce
+ _AXFCanWarpKeepingCursorObscured.canWarp
+ _AXFCanWarpKeepingCursorObscured.onceToken
+ ___AXFCanWarpKeepingCursorObscured_block_invoke
+ ___SkyLightLibrary_block_invoke
+ ____AXFCanWarpKeepingCursorObscured_block_invoke
+ _dlopen
+ _initSLSWarpCursorPositionAndKeepObscured
+ _objc_msgSend$accessibilityLabelOrTitle
+ _objc_msgSend$obscureCursorInPlace
+ _objc_msgSend$warpToLocation:keepCursorObscured:
+ _softLinkSLSWarpCursorPositionAndKeepObscured
+ initSLSWarpCursorPositionAndKeepObscured
- -[AXFTextMarkerRange toIndexBased]
- GCC_except_table308
- GCC_except_table365
- _objc_msgSend$toIndexBased
CStrings:
+ "/System/Library/PrivateFrameworks/SkyLight.framework/SkyLight"
+ "AXFMouseHardware: obscured cursor warp failed (%d), falling back to a visible warp"
+ "AXFMouseHardware: obscuring the cursor in place failed (%d)"
+ "SLSWarpCursorPositionAndKeepObscured"
```
