## Silex

> `/System/Library/PrivateFrameworks/Silex.framework/Silex`

```diff

-5871.1.0.0.0
-  __TEXT.__text: 0x1282b4
+5877.1.0.0.0
+  __TEXT.__text: 0x128578
   __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x1e634
+  __TEXT.__objc_methlist: 0x1e644
   __TEXT.__const: 0x4ec
   __TEXT.__cstring: 0xa00c
   __TEXT.__gcc_except_tab: 0x25e0
-  __TEXT.__oslogstring: 0x2420
+  __TEXT.__oslogstring: 0x2510
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x5720
+  __TEXT.__unwind_info: 0x5730
   __TEXT.__objc_classname: 0x784c
   __TEXT.__objc_methname: 0x3be1f
   __TEXT.__objc_methtype: 0xe833

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CE6E625-42BA-3931-98E6-43B3F4A27EF1
-  Functions: 8581
-  Symbols:   34609
-  CStrings:  14683
+  UUID: DA3C1893-B07F-3436-ABEC-DD3819405BD9
+  Functions: 8583
+  Symbols:   34613
+  CStrings:  14685
 
Symbols:
+ -[SXLayoutOperation start].cold.1
+ -[SXLayoutPipeline dealloc]
+ __OBJC_$_PROP_LIST_SXLayoutPipeline.105
+ ___35-[SXLayoutPipeline layoutWithTask:]_block_invoke.13
- __OBJC_$_PROP_LIST_SXLayoutPipeline.103
- ___35-[SXLayoutPipeline layoutWithTask:]_block_invoke.9
Functions:
+ -[SXLayoutPipeline dealloc]
~ -[SXLayoutOperation start] : 800 -> 860
~ -[SXLayoutOperation layoutBlueprint:containsComponents:] : 524 -> 896
+ -[SXLayoutOperation start].cold.1
CStrings:
+ "Component identifier mismatch — blueprint=%lu, DOM=%lu, missing-from-blueprint=%{public}@, extra-in-blueprint=%{public}@, order-only-mismatch=%d"
+ "Layout loop exceeded 10 iterations, breaking to prevent CPU spin, task-identifier=%{public}@"

```
