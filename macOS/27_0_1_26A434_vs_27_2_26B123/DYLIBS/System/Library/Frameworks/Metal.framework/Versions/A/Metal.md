## Metal

> `/System/Library/Frameworks/Metal.framework/Versions/A/Metal`

```diff

-382.5.3.0.0
-  __TEXT.__text: 0x1fa6b8
+383.1.0.0.0
+  __TEXT.__text: 0x1fa810
   __TEXT.__objc_methlist: 0x1fac4
-  __TEXT.__cstring: 0x2429f
-  __TEXT.__gcc_except_tab: 0xc590
+  __TEXT.__cstring: 0x242b9
+  __TEXT.__gcc_except_tab: 0xc5d4
   __TEXT.__const: 0x2e750
-  __TEXT.__oslogstring: 0x2400
+  __TEXT.__oslogstring: 0x2401
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0x8e10
+  __TEXT.__unwind_info: 0x8e20
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xef8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x4420
+  __AUTH.__objc_data: 0x4150
   __DATA.__objc_ivar: 0x2388
-  __DATA.__data: 0x4498
-  __DATA.__bss: 0x3e4
+  __DATA.__data: 0x4490
+  __DATA.__bss: 0x3dc
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x4240
-  __DATA_DIRTY.__data: 0x108
-  __DATA_DIRTY.__bss: 0x378
+  __DATA_DIRTY.__objc_data: 0x4510
+  __DATA_DIRTY.__data: 0x110
+  __DATA_DIRTY.__bss: 0x388
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 14034
-  Symbols:   26355
-  CStrings:  4726
+  Symbols:   26357
+  CStrings:  4727
 
Symbols:
+ GCC_except_table195
+ GCC_except_table250
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table295
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table327
+ GCC_except_table333
+ GCC_except_table342
+ GCC_except_table346
+ GCC_except_table349
+ GCC_except_table363
+ GCC_except_table396
+ GCC_except_table398
+ GCC_except_table403
+ GCC_except_table440
+ GCC_except_table454
+ GCC_except_table457
+ GCC_except_table478
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table496
+ __ZGVZN18MTLCompilerFSCache8openSyncEvE20sShaderCacheReadOnly
+ __ZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNSt3__16vectorIS0_NS3_9allocatorIS0_EEEE
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Lb0EEEvT1_SD_T0_NS_15iterator_traitsISD_E15difference_typeEb
+ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_EEbT1_SD_T0_
+ __ZNSt3__17__sort4B9nqe220106INS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Li0EEEvT1_SD_SD_SD_T0_
+ __ZZN18MTLCompilerFSCache8openSyncEvE20sShaderCacheReadOnly
- GCC_except_table256
- GCC_except_table259
- GCC_except_table261
- GCC_except_table288
- GCC_except_table294
- GCC_except_table300
- GCC_except_table302
- GCC_except_table307
- GCC_except_table316
- GCC_except_table319
- GCC_except_table326
- GCC_except_table332
- GCC_except_table341
- GCC_except_table345
- GCC_except_table356
- GCC_except_table362
- GCC_except_table394
- GCC_except_table397
- GCC_except_table401
- GCC_except_table416
- GCC_except_table438
- GCC_except_table443
- GCC_except_table453
- GCC_except_table477
- GCC_except_table481
- GCC_except_table488
- GCC_except_table498
- __ZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNSt3__16vectorIS0_NS3_9allocatorIS0_EEEE
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Lb0EEEvT1_SD_T0_NS_15iterator_traitsISD_E15difference_typeEb
- __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_EEbT1_SD_T0_
- __ZNSt3__17__sort4B9nqe220106INS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Li0EEEvT1_SD_SD_SD_T0_
Functions:
~ __ZN18MTLCompilerFSCache8openSyncEv : 916 -> 1032
~ -[_MTLBinaryArchive loadFromURL:error:] : 2364 -> 2352
~ -[_MTLBinaryArchive materializeAirNTAllForSlice:entryList:] : 1440 -> 1424
~ ___75-[_MTLBinaryArchive loadAirntBlocksForSlice:sliceOffset:skipAIRValidation:]_block_invoke : 744 -> 636
~ __75-[_MTLBinaryArchive loadAirntBlocksForSlice:sliceOffset:skipAIRValidation:]_block_invoke.327 : 1272 -> 1308
~ __ZN26MTLArchiveLinkResolverImpl19decodeAIRNTSectionsEyNSt3__16vectorI11SectionDataNS0_9allocatorIS2_EEEE : 2284 -> 2440
~ __ZN26MTLArchiveLinkResolverImpl12resolveLinksEv : 200 -> 396
~ +[MTLLoader deserializeMachOContainerWithHandlerInternal:expectAIRNTFormat:objectHandler:pipelineHandler:errorHandler:reader:] : 2844 -> 2820
CStrings:
+ "18:03:27"
+ "MTL_SHADER_CACHE_READ_ONLY"
+ "Oct  3 2026"
+ "Oct  3 2026 18:03:27"
+ "Unable to resolve all the internal/external links in the archive."
+ "Unable to resolve link:"
- "23:04:37"
- "Aug  9 2026"
- "Aug  9 2026 23:04:37"
- "Unable to resolve all the internal/external links in the archive"
- "Unable to resolve link :"
```
