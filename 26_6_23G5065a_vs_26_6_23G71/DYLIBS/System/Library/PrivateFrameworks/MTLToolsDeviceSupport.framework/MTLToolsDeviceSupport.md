## MTLToolsDeviceSupport

> `/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

 310.8.0.0.0
-  __TEXT.__text: 0x35500
+  __TEXT.__text: 0x355a8
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0xeac
   __TEXT.__gcc_except_tab: 0x2e0c
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0x326e2
+  __TEXT.__cstring: 0x328a2
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__objc_classname: 0x1d2
   __TEXT.__objc_methname: 0x446b
   __TEXT.__objc_methtype: 0x1117

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 807
+  Functions: 808
   Symbols:   1791
-  CStrings:  6215
+  CStrings:  6229
 
Functions:
~ __ZN8GPUTools3MTL24GetMTLFeatureSetAsStringEyb : 744 -> 892
~ __ZN8GPUTools3MTL23GetMTLGPUFamilyAsStringEyb : 588 -> 548
+ sub_26205d048
~ __ZN8GPUTools3MTL25GetMTLPixelFormatAsStringEyb : 5740 -> 5760
CStrings:
+ "Apple8"
+ "MTLFeatureSet_tvOS_GPUFamily2_v1"
+ "MTLFeatureSet_tvOS_GPUFamily2_v2"
+ "MTLFeatureSet_watchOS_GPUFamily1_v1"
+ "MTLFeatureSet_watchOS_GPUFamily2_v1"
+ "MTLGPUFamilyApple8"
+ "MTLPixelFormatYCBCRA8_444_1P"
+ "YCBCRA8_444_1P"
+ "[%@ computeCommandEncoderWithParallelExecution]"
+ "[%@ dispatchBarrier]"
+ "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
+ "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
+ "tvOS_GPUFamily2_v1"
+ "tvOS_GPUFamily2_v2"
+ "watchOS_GPUFamily1_v1"
+ "watchOS_GPUFamily2_v1"
- "0xffffc0e9"
- "0xffffc0ea"
```
