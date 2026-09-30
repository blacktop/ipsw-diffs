## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-414.0.0.0.0
-  __TEXT.__text: 0xf0330
+415.0.0.0.0
+  __TEXT.__text: 0xf0200
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x5e9c
   __TEXT.__const: 0x348
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x1839e
-  __TEXT.__oslogstring: 0xc66a
-  __TEXT.__gcc_except_tab: 0x9d94
+  __TEXT.__cstring: 0x18399
+  __TEXT.__oslogstring: 0xc615
+  __TEXT.__gcc_except_tab: 0x9d64
   __TEXT.__unwind_info: 0x2118
   __TEXT.__objc_classname: 0xb34
   __TEXT.__objc_methname: 0xd955
   __TEXT.__objc_methtype: 0x1a44
-  __TEXT.__objc_stubs: 0x7e00
+  __TEXT.__objc_stubs: 0x7de0
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x3b80
   __DATA_CONST.__objc_classlist: 0x418

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x29a0
-  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xbc8
   __AUTH_CONST.__const: 0xb00
-  __AUTH_CONST.__cfstring: 0xd0a0
+  __AUTH_CONST.__cfstring: 0xd080
   __AUTH_CONST.__objc_const: 0x104f0
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C342CA94-6764-3279-81FE-081D5592A000
+  UUID: A281747E-7CCF-3155-A2AF-9D425C81D4CA
   Functions: 2829
-  Symbols:   9704
-  CStrings:  8568
+  Symbols:   9702
+  CStrings:  8564
 
Symbols:
+ _.str.98
+ ___23+[SABinary clearCaches]_block_invoke.99
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.499
+ ___32-[SASegment addTailspinSymbols:]_block_invoke.31
+ ___34-[SASegment addInfoFromCSSegment:]_block_invoke.40
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.492
+ ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.140
+ ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.142
+ ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.355
+ ___block_literal_global.102
+ ___block_literal_global.104
+ ___block_literal_global.111
+ ___block_literal_global.127
+ ___block_literal_global.144
+ ___block_literal_global.151
+ ___block_literal_global.358
+ ___block_literal_global.421
+ ___block_literal_global.464
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.491
+ ___block_literal_global.768
- _.str.101
- __OBJC_PROTOCOL_REFERENCE_$_SAJSONSerialization
- ___23+[SABinary clearCaches]_block_invoke.102
- ___31+[SASharedCache addDSCSymData:]_block_invoke.502
- ___32-[SASegment addTailspinSymbols:]_block_invoke.34
- ___34-[SASegment addInfoFromCSSegment:]_block_invoke.43
- ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.495
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.143
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.145
- ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.358
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.114
- ___block_literal_global.130
- ___block_literal_global.147
- ___block_literal_global.154
- ___block_literal_global.361
- ___block_literal_global.427
- ___block_literal_global.467
- ___block_literal_global.469
- ___block_literal_global.471
- ___block_literal_global.482
- ___block_literal_global.494
- ___block_literal_global.771
- _objc_msgSend$conformsToProtocol:
Functions:
~ -[SASegment applyLength:] : 1400 -> 1248
~ -[SABinary applyLength:] : 532 -> 376
~ +[SABinaryLoadInfo binaryLoadInfoForAddress:inBinaryLoadInfos:] : 304 -> 308
CStrings:
- "%@ has length above max: 0x%llx"
- "%@ setting length above max for text segment: 0x%llx"
- "TEXT"

```
