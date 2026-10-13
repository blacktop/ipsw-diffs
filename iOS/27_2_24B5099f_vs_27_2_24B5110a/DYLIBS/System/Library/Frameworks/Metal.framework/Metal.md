## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-382.5.6.0.0
-  __TEXT.__text: 0x1e3eb0
+383.1.2.0.0
+  __TEXT.__text: 0x1e3fc0
   __TEXT.__objc_methlist: 0x1ee04
-  __TEXT.__cstring: 0x237a7
-  __TEXT.__gcc_except_tab: 0xc3c8
+  __TEXT.__cstring: 0x237a6
+  __TEXT.__gcc_except_tab: 0xc3fc
   __TEXT.__const: 0x2e620
-  __TEXT.__oslogstring: 0x22d6
+  __TEXT.__oslogstring: 0x22d7
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0xa188
+  __TEXT.__unwind_info: 0xa190
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 13563
-  Symbols:   22584
+  Symbols:   22588
   CStrings:  4605
 
Symbols:
+ GCC_except_table149
+ GCC_except_table155
+ GCC_except_table166
+ GCC_except_table275
+ GCC_except_table292
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table305
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table326
+ GCC_except_table330
+ GCC_except_table339
+ GCC_except_table370
+ GCC_except_table385
+ GCC_except_table389
+ GCC_except_table412
+ GCC_except_table417
+ GCC_except_table419
+ GCC_except_table426
+ GCC_except_table429
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table462
+ __ZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNSt3__16vectorIS0_NS3_9allocatorIS0_EEEE
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Lb0EEEvT1_SD_T0_NS_15iterator_traitsISD_E15difference_typeEb
+ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_EEbT1_SD_T0_
+ __ZNSt3__17__sort4B9fqe220106INS_17_ClassicAlgPolicyERZNK10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Li0EEEvT1_SD_SD_SD_T0_
- GCC_except_table235
- GCC_except_table242
- GCC_except_table295
- GCC_except_table298
- GCC_except_table304
- GCC_except_table313
- GCC_except_table317
- GCC_except_table325
- GCC_except_table366
- GCC_except_table373
- GCC_except_table384
- GCC_except_table388
- GCC_except_table415
- GCC_except_table418
- GCC_except_table425
- GCC_except_table428
- GCC_except_table450
- GCC_except_table454
- GCC_except_table461
- GCC_except_table468
- __ZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNSt3__16vectorIS0_NS3_9allocatorIS0_EEEE
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Lb0EEEvT1_SD_T0_NS_15iterator_traitsISD_E15difference_typeEb
- __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_EEbT1_SD_T0_
- __ZNSt3__17__sort4B9fqe220106INS_17_ClassicAlgPolicyERZN10MTLHashKey16areBitcodesEqualEPK12MTLUINT256_tNS_6vectorIS3_NS_9allocatorIS3_EEEEE3$_0PS3_Li0EEEvT1_SD_SD_SD_T0_
Functions:
~ -[_MTLBinaryArchive loadFromURL:error:] : 2364 -> 2352
~ __ZN26MTLArchiveLinkResolverImpl19decodeAIRNTSectionsEyNSt3__16vectorI11SectionDataNS0_9allocatorIS2_EEEE : 2328 -> 2484
~ +[MTLLoader(MTLLoaderAIRNT) deserializeObjectFromAIRNTHeaderAtSection:reader:errorHandler:handler:] : 1560 -> 1568
~ ___75-[_MTLBinaryArchive loadAirntBlocksForSlice:sliceOffset:skipAIRValidation:]_block_invoke_2 : 1284 -> 1320
~ __ZN26MTLArchiveLinkResolverImpl12resolveLinksEv : 200 -> 396
~ ___75-[_MTLBinaryArchive loadAirntBlocksForSlice:sliceOffset:skipAIRValidation:]_block_invoke : 744 -> 636
~ +[MTLLoader deserializeMachOContainerWithHandlerInternal:expectAIRNTFormat:objectHandler:pipelineHandler:errorHandler:reader:] : 2836 -> 2820
~ -[_MTLBinaryArchive materializeAirNTAllForSlice:entryList:] : 1560 -> 1556
~ -[_MTLBinaryArchive materializeEntryForKey:fileIndex:containsEntry:addEntry:] : 264 -> 268
~ __Z19getArchiveReferenceNSt3__117basic_string_viewIcNS_11char_traitsIcEEEE : 752 -> 764
CStrings:
+ "Unable to resolve all the internal/external links in the archive."
+ "Unable to resolve link:"
- "Unable to resolve all the internal/external links in the archive"
- "Unable to resolve link :"
```
