## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-763.0.0.502.1
-  __TEXT.__text: 0x699ec
+769.0.0.0.0
+  __TEXT.__text: 0x69b78
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4140
+  __TEXT.__objc_methlist: 0x4158
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xe800
-  __TEXT.__oslogstring: 0x7926
+  __TEXT.__cstring: 0xe852
+  __TEXT.__oslogstring: 0x79a0
   __TEXT.__gcc_except_tab: 0x1d80
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x17e8
   __TEXT.__objc_classname: 0x8ae
-  __TEXT.__objc_methname: 0xad0e
+  __TEXT.__objc_methname: 0xad37
   __TEXT.__objc_methtype: 0x23eb
-  __TEXT.__objc_stubs: 0x6040
+  __TEXT.__objc_stubs: 0x6080
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1b60
+  __DATA_CONST.__const: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2080
+  __DATA_CONST.__objc_selrefs: 0x2090
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x59e0
-  __AUTH_CONST.__objc_const: 0xada0
+  __AUTH_CONST.__cfstring: 0x5a20
+  __AUTH_CONST.__objc_const: 0xadb0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36A2B1C7-E9A0-3DA0-AAFE-D0015E1D952D
-  Functions: 1958
-  Symbols:   6480
-  CStrings:  4154
+  UUID: D1F42976-7B8F-31BA-B07E-CDC9E0011C32
+  Functions: 1961
+  Symbols:   6492
+  CStrings:  4162
 
Symbols:
+ -[IXDataPromise preflightPath]
+ -[IXOwnedDataPromise preflightPath]
+ GCC_except_table20
+ GCC_except_table57
+ _IXAdditionalDiskSpaceRequiredErrorKey
+ _IXTotalDiskSpaceRequiredErrorKey
+ ___32-[IXDataPromise resetWithError:]_block_invoke.31
+ ___36-[IXDataPromise preflightWithError:]_block_invoke.33
+ ___37-[IXDataPromise resetWithCompletion:]_block_invoke.30
+ ___41-[IXDataPromise preflightWithCompletion:]_block_invoke.32
+ ___46-[IXDataPromise cancelForReason:client:error:]_block_invoke.29
+ ___57+[IXDataPromise(IXTesting) promiseExists:withUUID:error:]_block_invoke.140
+ ___58+[IXDataPromise(IXTesting) outstandingPromisesForCreator:]_block_invoke.138
+ ___block_descriptor_40_e8_32bs_e20_v24?0d8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e20_v24?0d8"NSError"16lr32l8
+ ___block_literal_global.137
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$userVolumeURL
- GCC_except_table16
- GCC_except_table19
- GCC_except_table42
- GCC_except_table65
- GCC_except_table68
- ___32-[IXDataPromise resetWithError:]_block_invoke.30
- ___36-[IXDataPromise preflightWithError:]_block_invoke.31
- ___37-[IXDataPromise resetWithCompletion:]_block_invoke.29
- ___46-[IXDataPromise cancelForReason:client:error:]_block_invoke.28
- ___57+[IXDataPromise(IXTesting) promiseExists:withUUID:error:]_block_invoke.135
- ___58+[IXDataPromise(IXTesting) outstandingPromisesForCreator:]_block_invoke.133
- ___block_literal_global.132
CStrings:
+ "%s: WARNING: Preflight called on %@ which assumes data will end up on the volume containing %@; this may not be accurate."
+ "-[IXDataPromise preflightPath]"
+ "AdditionalDiskSpaceRequired"
+ "TotalDiskSpaceRequired"
+ "localizedStringWithFormat:"
+ "preflightPath"

```
