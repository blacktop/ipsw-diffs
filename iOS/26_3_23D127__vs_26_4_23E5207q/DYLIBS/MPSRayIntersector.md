## MPSRayIntersector

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector`

```diff

-129.3.8.1.0
-  __TEXT.__text: 0x42258
-  __TEXT.__auth_stubs: 0x630
+129.4.1.0.0
+  __TEXT.__text: 0x43c90
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x14c4
-  __TEXT.__const: 0x4f8
+  __TEXT.__const: 0x5b8
   __TEXT.__gcc_except_tab: 0x16f0
-  __TEXT.__cstring: 0x5b96
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__eh_frame: 0xb0
+  __TEXT.__cstring: 0x704b
+  __TEXT.__unwind_info: 0xce8
   __TEXT.__objc_classname: 0x283
   __TEXT.__objc_methname: 0x37c5
   __TEXT.__objc_methtype: 0xe84
   __TEXT.__objc_stubs: 0x1c80
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x29c0
+  __DATA_CONST.__const: 0x3e70
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcb8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x398
   __AUTH_CONST.__cfstring: 0x33a0
   __AUTH_CONST.__objc_const: 0x24e0
   __DATA.__objc_ivar: 0x1c4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 611246DA-9DAD-3548-80E1-29354804219E
-  Functions: 1012
-  Symbols:   203
-  CStrings:  1586
+  UUID: A44FE9FD-E267-370B-A181-2FA659D3F68F
+  Functions: 1040
+  Symbols:   204
+  CStrings:  1598
 
Symbols:
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptions23MPSForwardProgressUsageP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_EPSR_ISO_E
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSAccelerationStructure.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSAccelerationStructureGroup.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSBVH.h"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSBVH.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSCPUBVHBuilder.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSGPUBVHBuilder.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSInstanceAccelerationStructure.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPerfCounters.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPolygonAccelerationStructure.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPolygonBuffer.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSQuadrilateralAccelerationStructure.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSRayIntersector.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSSVGF.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSTemporalAA.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSTriangleAccelerationStructure.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSAccelerationStructure.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSAccelerationStructureGroup.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSBVH.h"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSBVH.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSCPUBVHBuilder.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSGPUBVHBuilder.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSInstanceAccelerationStructure.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPerfCounters.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPolygonAccelerationStructure.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSPolygonBuffer.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSQuadrilateralAccelerationStructure.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSRayIntersector.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSSVGF.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSTemporalAA.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSRayIntersector/MPSTriangleAccelerationStructure.mm"

```
