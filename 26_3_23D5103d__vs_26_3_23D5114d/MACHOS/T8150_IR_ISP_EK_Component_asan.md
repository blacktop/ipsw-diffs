## T8150_IR_ISP_EK_Component_asan

> `/System/ExclaveKit/System/Library/Frameworks/T8150_IR_ISP_EK_Component.framework/T8150_IR_ISP_EK_Component_asan`

```diff

-5.305.1.0.0
-  __TEXT.__text: 0x2fb630
+5.308.0.0.0
+  __TEXT.__text: 0x2fb5b0
   __TEXT.__auth_stubs: 0x50e0
   __TEXT.__const: 0x49992
   __TEXT.__cstring: 0x465a6

   __DATA.__asan_liveness: 0x10560
   __DATA.__common: 0x4028
   __DATA.__bss: 0x5130
-  __LLVM_COV.__llvm_covfun: 0x36f6e
+  __LLVM_COV.__llvm_covfun: 0x36f76
   __LLVM_COV.__llvm_covmap: 0x1c50
   - /System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/ExclaveKit/System/Library/Frameworks/EXDataLoader.framework/EXDataLoader

   - /System/ExclaveKit/usr/lib/swift/libswift_Concurrency.dylib
   - /System/ExclaveKit/usr/lib/swift/libswift_StringProcessing.dylib
   - /System/ExclaveKit/usr/lib/swift/libswiftos.dylib
-  UUID: 389ACBE9-1F1D-38B2-8B9C-24CA6C332B22
+  UUID: 1BA79134-D8C3-3D02-A069-66752C462CCE
   Functions: 11542
   Symbols:   51930
   CStrings:  4725
Symbols:
+ .str.40.Build Date: Wed Jan 21 01:41:48 PST 2026
+ __asan_binder_.str.40.Build Date: Wed Jan 21 01:41:48 PST 2026
+ __asan_global_.str.40.Build Date: Wed Jan 21 01:41:48 PST 2026
- .str.40.Build Date: Wed Jan  7 21:39:04 PST 2026
- __asan_binder_.str.40.Build Date: Wed Jan  7 21:39:04 PST 2026
- __asan_global_.str.40.Build Date: Wed Jan  7 21:39:04 PST 2026
Functions:
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 76
~ _$s25T8150_IR_ISP_EK_Component12EKControllerC10setupFDMgrySbs6UInt32VF : 656 -> 564
~ _$s25T8150_IR_ISP_EK_Component12EKControllerC10setupADMgrySbs6UInt32VF : 516 -> 476
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 80
~ _$s25T8150_IR_ISP_EK_Component9EkMgrBaseC15setSEPBufRetainyySbF -> _$s25T8150_IR_ISP_EK_Component9EkMgrBaseC7controlyySbF : 204 -> 212
~ _$s25T8150_IR_ISP_EK_Component9EkMgrBaseC7controlyySbF -> _$s25T8150_IR_ISP_EK_Component9EkMgrBaseC15setSEPBufRetainyySbF : 212 -> 204
~ __ZL16markEyeOcclusionILi12EEvRAT__AT__KfRK23sCIspFwDetectorLandmarkRK26sCIspFwDetectorBoundingBoxRAT__AT__jPfRj18occlusionDirection : 184 -> 176
CStrings:
+ ".str.40.Build Date: Wed Jan 21 01:41:48 PST 2026"
- ".str.40.Build Date: Wed Jan  7 21:39:04 PST 2026"

```
