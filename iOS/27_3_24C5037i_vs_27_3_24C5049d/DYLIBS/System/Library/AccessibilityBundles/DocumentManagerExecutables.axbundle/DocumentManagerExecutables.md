## DocumentManagerExecutables

> `/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x5800
-  __TEXT.__objc_methlist: 0xff4
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__cstring: 0x139f
-  __TEXT.__oslogstring: 0x75
-  __TEXT.__unwind_info: 0x310
+3050.3.22.0.0
+  __TEXT.__text: 0x5cbc
+  __TEXT.__objc_methlist: 0x1024
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__cstring: 0x13d1
+  __TEXT.__oslogstring: 0xcc
+  __TEXT.__unwind_info: 0x338
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2e0
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a0
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__cfstring: 0x18a0
   __AUTH_CONST.__objc_const: 0x2638
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 195
-  Symbols:   611
-  CStrings:  224
+  Functions: 200
+  Symbols:   621
+  CStrings:  227
 
Symbols:
+ -[DOCItemCollectionCellAccessibility _axDeferredMenuElementsDidArriveLate:forNode:]
+ -[DOCItemCollectionCellAccessibility _axDocNode]
+ -[DOCItemCollectionCellAccessibility _axStoreDeferredMenuElements:forNode:]
+ -[DOCItemCollectionCellAccessibility _axStoredDeferredMenuElementsForNode:]
+ GCC_except_table114
+ GCC_except_table18
+ GCC_except_table182
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table62
+ GCC_except_table76
+ _AXPerformBlockAsynchronouslyOnMainThread
+ ___77-[DOCItemCollectionCellAccessibility _axMenuElementsFromDeferredMenuElement:]_block_invoke_3
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r56w_e17_v16?0"NSArray"8lr40l8w56l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40bs48r56r64w_e5_v8?0ls40l8r48l8w64l8s32l8r56l8
+ __os_log_impl
- GCC_except_table109
- GCC_except_table15
- GCC_except_table177
- GCC_except_table57
- GCC_except_table71
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
CStrings:
+ "AXDeferredMenuElements"
+ "AXDeferredMenuElementsNode"
+ "Deferred context menu delivered %lu elements asynchronously"
+ "Deferred context menu elements weren't delivered synchronously, using %lu stored elements"
- "Deferred context menu elements weren't delivered synchronously"
```
