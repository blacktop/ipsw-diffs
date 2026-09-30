## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-6.4.2.0.0
-  __TEXT.__text: 0x1165438
+6.5.1.0.0
+  __TEXT.__text: 0x11655bc
   __TEXT.__auth_stubs: 0x32d0
   __TEXT.__mpsgraph_init_: 0x18
   __TEXT.__objc_methlist: 0x7704
-  __TEXT.__const: 0x4eb98
+  __TEXT.__const: 0x4eb88
   __TEXT.__cstring: 0x9a6bc
   __TEXT.__swift5_typeref: 0x2fb
   __TEXT.__swift5_capture: 0x10

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__gcc_except_tab: 0x5b2d4
+  __TEXT.__gcc_except_tab: 0x5b2e0
   __TEXT.__oslogstring: 0x6ed
   __TEXT.__unwind_info: 0x2cbc0
   __TEXT.__eh_frame: 0x2af0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 36A253B3-0D61-3F26-92E5-23686A9B9ED0
+  UUID: 3C5669EC-32A9-3697-A95B-D64A6CB8FD1C
   Functions: 66931
   Symbols:   204674
   CStrings:  17696
Symbols:
+ __ZN16GPURegionRuntime16tryGetStaticTypeEN4mlir5ValueE
- __ZN16GPURegionRuntime13getStaticTypeEN4mlir5ValueE
Functions:
~ __ZN16GPURegionRuntime13getStaticTypeEN4mlir5ValueE -> __ZN16GPURegionRuntime16tryGetStaticTypeEN4mlir5ValueE : 500 -> 492
~ __ZN16GPURegionRuntime26allocateTensorDataForValueEN4mlir5ValueEPU27objcproto16MTLCommandBuffer11objc_objectbmm : 4656 -> 5052
CStrings:
+ "260500"
+ "6.5.1"
- "260400"
- "6.4.2"

```
