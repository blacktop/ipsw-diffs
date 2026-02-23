## MPSCore

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`

```diff

-129.4.1.0.0
-  __TEXT.__text: 0x94754
+129.4.3.0.0
+  __TEXT.__text: 0x94934
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x27d4
   __TEXT.__const: 0x28c4
-  __TEXT.__cstring: 0xa875
+  __TEXT.__cstring: 0xa94b
   __TEXT.__oslogstring: 0x79
   __TEXT.__gcc_except_tab: 0x4d90
   __TEXT.__unwind_info: 0x1e18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84718CAC-65BA-3A7F-95E2-BD20DDBA8B7E
+  UUID: 37AFB159-E4F9-3F8B-ACEF-7358E31284AB
   Functions: 1712
   Symbols:   799
-  CStrings:  2545
+  CStrings:  2549
 
Functions:
~ _MPSGetDataTypeName : 748 -> 960
~ sub_235d767f8 -> sub_235e4a8cc : 2444 -> 2492
~ __Z16dataTypeToString11MPSDataType : 900 -> 1092
~ __ZNK9MPSDevice19isDataTypeSupportedE11MPSDataType : 340 -> 368
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSStateInternal.h"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Filters/MPSKernel.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/MPSState.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Types/MPSImage.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Types/MPSMatrix.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Types/MPSNDArray.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/Float2Half.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSCommandBufferImageCache.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevice.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDeviceComputePipelineState.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevicePixeInfo.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelDAG.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelUserDAG.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSLibrary.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSPredicate.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelRandom.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelReduce.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelScan.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelSort.mm"
+ "MPSDataTypeFloat4e2m1"
+ "MPSDataTypeFloat6e2m3"
+ "MPSDataTypeFloat6e3m2"
+ "MPSDataTypeFloat8e8m0"
+ "MPSDataTypeInt8p6"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSStateInternal.h"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Filters/MPSKernel.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/MPSState.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSImage.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSMatrix.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Types/MPSNDArray.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/Float2Half.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSCommandBufferImageCache.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevice.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDeviceComputePipelineState.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSDevicePixeInfo.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelDAG.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSKernelUserDAG.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSLibrary.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSCore/Utility/MPSPredicate.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelRandom.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelReduce.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelScan.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSParallelPrimitives/Kernels/MPSParallelSort.mm"
- "MPSDataTypeFloat4m3fn"

```
