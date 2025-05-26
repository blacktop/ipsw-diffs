## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-341.16.2.0.0
-  __TEXT.__text: 0xc9180
+341.29.1.0.0
+  __TEXT.__text: 0xc93cc
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0xc188
-  __TEXT.__cstring: 0x23731
+  __TEXT.__objc_methlist: 0xc198
+  __TEXT.__cstring: 0x238ca
   __TEXT.__gcc_except_tab: 0x1400
   __TEXT.__const: 0x279
   __TEXT.__oslogstring: 0x271d
-  __TEXT.__unwind_info: 0x3458
+  __TEXT.__unwind_info: 0x345c
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_classname: 0x176a
-  __TEXT.__objc_methname: 0x16a5e
+  __TEXT.__objc_methname: 0x16a82
   __TEXT.__objc_methtype: 0x151f0
-  __TEXT.__objc_stubs: 0x11600
+  __TEXT.__objc_stubs: 0x11620
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x15c8
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35550
-  __DATA_CONST.__objc_selrefs: 0x4a68
-  __AUTH_CONST.__cfstring: 0xa860
+  __DATA_CONST.__objc_const: 0x355c0
+  __DATA_CONST.__objc_selrefs: 0x4a70
+  __AUTH_CONST.__cfstring: 0xa940
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x540
   __DATA.__objc_protorefs: 0x78

   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x1
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__const: 0x1b0
+  __DATA_DIRTY.__const: 0x190
   __DATA_DIRTY.__objc_const: 0x2b08
   __DATA_DIRTY.__objc_data: 0x2fd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4790
-  Symbols:   14962
-  CStrings:  6789
+  Functions: 4792
+  Symbols:   14967
+  CStrings:  6797
 
Symbols:
+ -[MTLToolsDevice supportsPartialRenderMemoryBarrier]
+ GCC_except_table197
+ GCC_except_table266
+ __ZL21validateCommonBarrierPU19objcproto9MTLDevice11objc_objectP18_MTLMessageContextmmm
+ ___block_literal_global.1624
+ _objc_msgSend$supportsPartialRenderMemoryBarrier
- GCC_except_table196
- GCC_except_table265
- ___block_literal_global.1621
CStrings:
+ "afterStages (0x%lx) can not contain MTLRenderStageTile or MTLRenderStageFragment on this device"
+ "afterStages has invalid value (0x%lx)"
+ "afterStages value (0x%lx) is not supported on this device"
+ "beforeStages has invalid value (0x%lx)"
+ "beforeStages value (0x%lx) is not supported on this device"
+ "scope (0x%lx) cannot contain MTLBarrierScopeRenderTargets on this device"
+ "scope (0x%lx) has an invalid value for render"
+ "supportsPartialRenderMemoryBarrier"

```
