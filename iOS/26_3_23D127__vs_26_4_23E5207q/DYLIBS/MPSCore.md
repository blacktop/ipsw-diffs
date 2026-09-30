## MPSCore

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`

```diff

-129.3.8.1.0
-  __TEXT.__text: 0x8ea40
-  __TEXT.__auth_stubs: 0x9c0
+129.4.1.0.0
+  __TEXT.__text: 0x94754
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x27d4
-  __TEXT.__const: 0x2714
-  __TEXT.__cstring: 0xa025
+  __TEXT.__const: 0x28c4
+  __TEXT.__cstring: 0xa875
   __TEXT.__oslogstring: 0x79
-  __TEXT.__gcc_except_tab: 0x4ad8
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__gcc_except_tab: 0x4d90
+  __TEXT.__unwind_info: 0x1e18
   __TEXT.__objc_classname: 0x4f6
   __TEXT.__objc_methname: 0x56fc
   __TEXT.__objc_methtype: 0x2878
   __TEXT.__objc_stubs: 0x2c80
   __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x36a0
+  __DATA_CONST.__const: 0x5850
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x13c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x188
-  __AUTH_CONST.__auth_got: 0x4f8
-  __AUTH_CONST.__const: 0x5428
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__const: 0x5e48
   __AUTH_CONST.__cfstring: 0x37e0
   __AUTH_CONST.__objc_const: 0x5200
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x9a8
+  __DATA.__common: 0x28
   __DATA.__bss: 0x1c
-  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__bss: 0x210

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3131F423-A759-35B4-AEBA-6C309858DD4A
-  Functions: 1706
-  Symbols:   793
-  CStrings:  2542
+  UUID: 84718CAC-65BA-3A7F-95E2-BD20DDBA8B7E
+  Functions: 1712
+  Symbols:   799
+  CStrings:  2545
 
Symbols:
+ __ZN10MPSLibrary13MPSKey_CreateEPK17PrivateKernelInfoRK23MPSFunctionConstantListb30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptions23MPSForwardProgressUsagePFvPS0_EP8NSStringmy
+ __ZN10MPSLibrary17GetCacheKeyAtomicEPK17PrivateKernelInfoRK23MPSFunctionConstantListbPNSt3__16atomicIP11MPSKey_dataEE30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptions23MPSForwardProgressUsageP8NSStringm
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptions23MPSForwardProgressUsageP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_EPSR_ISO_E
+ __ZN21MPSKernelMiddlefixDAG10_totalDAGsE
+ __ZN21MPSKernelMiddlefixDAG13getDAGAndHashEPU21objcproto10MTLLibrary11objc_objectP14MPSDAGKernelOpP19NSMutableDictionaryIP8NSStringPU22objcproto11MTLFunction11objc_objectEP14NSMutableArrayIS6_ERDv4_yPb
+ __ZN21MPSKernelMiddlefixDAGC1ERKNSt3__16vectorIP10BaseTensorNS0_9allocatorIS3_EEEEPKc
+ __ZN21MPSKernelMiddlefixDAGC2ERKNSt3__16vectorIP10BaseTensorNS0_9allocatorIS3_EEEEPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZTV21MPSKernelMiddlefixDAG
+ _objc_retain_x28
- __ZN10MPSLibrary13MPSKey_CreateEPK17PrivateKernelInfoRK23MPSFunctionConstantListb30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsPFvPS0_EP8NSStringmy
- __ZN10MPSLibrary17GetCacheKeyAtomicEPK17PrivateKernelInfoRK23MPSFunctionConstantListbPNSt3__16atomicIP11MPSKey_dataEE30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP8NSStringm
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
- _objc_retain_x26
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSStateInternal.h"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Filters/MPSKernel.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/MPSState.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSImage.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSMatrix.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSNDArray.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/Float2Half.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSCommandBufferImageCache.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevice.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDeviceComputePipelineState.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevicePixeInfo.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelDAG.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelUserDAG.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSLibrary.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSPredicate.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelRandom.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelReduce.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelScan.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelSort.mm"
- "/Library/Caches/com.apple.xbs/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSStateInternal.h"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Filters/MPSKernel.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/MPSState.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Types/MPSImage.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Types/MPSMatrix.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Types/MPSNDArray.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/Float2Half.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSCommandBufferImageCache.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevice.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDeviceComputePipelineState.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevicePixeInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelDAG.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelUserDAG.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSLibrary.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSPredicate.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelRandom.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelReduce.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelScan.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelSort.mm"

```
