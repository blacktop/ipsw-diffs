## MPSCore

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`

```diff

-128.5.2.0.0
-  __TEXT.__text: 0x8bc5c
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x2784
+129.0.14.0.0
+  __TEXT.__text: 0x8c1d4
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x27d4
   __TEXT.__const: 0x26d4
-  __TEXT.__cstring: 0x9d9d
+  __TEXT.__cstring: 0x9e45
   __TEXT.__oslogstring: 0x79
-  __TEXT.__gcc_except_tab: 0x49b4
-  __TEXT.__unwind_info: 0x1d78
+  __TEXT.__gcc_except_tab: 0x4a00
+  __TEXT.__unwind_info: 0x1db0
   __TEXT.__objc_classname: 0x4f6
-  __TEXT.__objc_methname: 0x55f6
-  __TEXT.__objc_methtype: 0x28e2
-  __TEXT.__objc_stubs: 0x2b80
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x3580
+  __TEXT.__objc_methname: 0x56a3
+  __TEXT.__objc_methtype: 0x283b
+  __TEXT.__objc_stubs: 0x2bc0
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x35c0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1398
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x188
-  __AUTH_CONST.__auth_got: 0x500
-  __AUTH_CONST.__const: 0x52f0
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x5308
   __AUTH_CONST.__cfstring: 0x37c0
-  __AUTH_CONST.__objc_const: 0x5198
-  __DATA.__objc_ivar: 0x324
+  __AUTH_CONST.__objc_const: 0x5200
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x9a8
   __DATA.__bss: 0x1c
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x54
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67E59461-201B-3B95-925A-E6FE8F2826C0
-  Functions: 1683
+  UUID: FDD1C771-2C5C-36EF-9965-BF50487CDD21
+  Functions: 1694
   Symbols:   792
-  CStrings:  2495
+  CStrings:  2520
 
Symbols:
+ __ZN16MPSKernelUserDAG10reciprocalEP20MPSKernelUserDAGNode11MPSDataType
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
CStrings:
+ " - TVOS"
+ "<unknown>"
+ "@\"<MTLTensor>\"40@0:8@\"MTLTensorDescriptor\"16Q24^@32"
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@36@0:8@16Q24B32"
+ "@40@0:8@16Q24^@32"
+ "C"
+ "D"
+ "G"
+ "GP"
+ "GetMPSDevice() no device found!\n"
+ "GetMPSDevice(): supportFamily = %lu%s, variantType = %s, DeviceSet = %d\n"
+ "MPS_DEVICE_SET set to: %s\n"
+ "P"
+ "T{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I},N,V_dynamicFCs"
+ "X"
+ "_compilationOnly"
+ "barrierAfterQueueStages:beforeStages:"
+ "initWithCommandBuffer:withDispatchType:compilationOnly:"
+ "newTensorWithDescriptor:offset:error:"
+ "newTextureViewWithDescriptor:"
+ "sparseBufferTier"
+ "sparseTextureTier"
+ "supportsAtomicWaitNotify"
+ "v40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}16"
+ "{unique_ptr<const std::vector<long>, std::default_delete<const std::vector<long>>>=^v}16@0:8"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}16@0:8"
- "T{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}},N,V_dynamicFCs"
- "v40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}16"
- "{unique_ptr<const std::vector<long>, std::default_delete<const std::vector<long>>>={__compressed_pair<const std::vector<long> *, std::default_delete<const std::vector<long>>>=^v}}16@0:8"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}16@0:8"

```
