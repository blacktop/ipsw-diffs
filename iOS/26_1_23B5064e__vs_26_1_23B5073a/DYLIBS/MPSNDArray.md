## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.1.4.0.0
-  __TEXT.__text: 0x104d64
+129.1.5.0.0
+  __TEXT.__text: 0x10695c
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x6a84
   __TEXT.__const: 0x83c18
-  __TEXT.__gcc_except_tab: 0x3d04
-  __TEXT.__cstring: 0xdad8
-  __TEXT.__unwind_info: 0x1868
+  __TEXT.__gcc_except_tab: 0x3ea4
+  __TEXT.__cstring: 0xdb90
+  __TEXT.__unwind_info: 0x1878
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6bf8
+  __TEXT.__objc_methname: 0x6c21
   __TEXT.__objc_methtype: 0x1ea9
-  __TEXT.__objc_stubs: 0x3260
+  __TEXT.__objc_stubs: 0x32c0
   __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__const: 0xedb0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x1540
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x3fe0
-  __AUTH_CONST.__cfstring: 0x6ba0
+  __AUTH_CONST.__cfstring: 0x6bc0
   __AUTH_CONST.__objc_const: 0xe888
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x6a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCFF1B2C-8047-3895-AB41-1B4ED3B6152D
-  Functions: 2236
-  Symbols:   7527
-  CStrings:  3645
+  UUID: 392E3933-34D1-3A5D-B8D8-723484FA6A4C
+  Functions: 2237
+  Symbols:   7533
+  CStrings:  3657
 
Symbols:
+ __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ _objc_msgSend$createFallbackKernels:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$numberWithInteger:
Functions:
~ __ZL10EncodeSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 792 -> 1088
+ __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
CStrings:
+ "Currently SDPA fallback only supports MPSNDArraySDPALayoutBHXF"
+ "Fallback to multi-dispatch (2Gemm) encoding\n"
+ "QK^T"
+ "insertObject:atIndex:"
+ "keyTransposeTensor"
+ "maskAdd"
+ "maskTensor"
+ "numberWithInteger:"
+ "queryTensor"
+ "scaleMul"
+ "scaleTensor"

```
