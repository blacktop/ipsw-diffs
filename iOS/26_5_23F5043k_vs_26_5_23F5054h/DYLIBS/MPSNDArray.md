## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.4.6.0.0
-  __TEXT.__text: 0x1160bc
+129.5.1.0.0
+  __TEXT.__text: 0x116018
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x6ee4
   __TEXT.__const: 0x897b0
   __TEXT.__gcc_except_tab: 0x452c
-  __TEXT.__cstring: 0x10185
+  __TEXT.__cstring: 0x100e3
   __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x1d25

   __DATA_CONST.__objc_superrefs: 0x848
   __AUTH_CONST.__auth_got: 0x598
   __AUTH_CONST.__const: 0x4450
-  __AUTH_CONST.__cfstring: 0x7cc0
+  __AUTH_CONST.__cfstring: 0x7c80
   __AUTH_CONST.__objc_const: 0xf2d8
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x750

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BBA28ED-0F77-3AF2-A8B8-1C98AB1F6883
+  UUID: 99DAA598-6F43-3980-B5B6-5A32B9FE84CD
   Functions: 2341
   Symbols:   7847
-  CStrings:  4015
+  CStrings:  4011
 
Symbols:
+ ___block_literal_global.416
- ___block_literal_global.422
Functions:
~ __ZL26EncodeMatrixVectorMultiplyPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP10MPSNDArrayS6_S6_S6_PK23NDArrayMultiaryCallInfo : 16284 -> 16016
~ __ZL25EncodeSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttention7MTLSize : 6960 -> 7064
CStrings:
- "LORADOWN GEMV Kernel - matrixRowPadElements will overflow its fc bit allocation."
- "LORADOWN GEMV Kernel - vectorRowPadElements will overflow its fc bit allocation."

```
