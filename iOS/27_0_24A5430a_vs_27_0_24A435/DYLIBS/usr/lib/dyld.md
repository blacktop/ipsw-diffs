## dyld

> `/usr/lib/dyld`

```diff

 27062.0.0.0.0
-  __TEXT.__text: 0x9edac
+  __TEXT.__text: 0x9eda4
   __TEXT.__const: 0x1978
-  __TEXT.__cstring: 0x124de
-  __TEXT.__unwind_info: 0x35b8
-  __DATA_CONST.__const: 0x55b0
+  __TEXT.__cstring: 0x12573
+  __TEXT.__unwind_info: 0x35b0
+  __DATA_CONST.__const: 0x55f0
   __AUTH_CONST.__const: 0x2758
   __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3423
-  Symbols:   3271
-  CStrings:  2244
+  Functions: 3422
+  Symbols:   3273
+  CStrings:  2255
 
Symbols:
+ __ZN5dyld3L14archCacheMagicE
+ __ZN5dyld3L9archNamesE
Functions:
~ __ZNK6mach_o5Image13linkeditBytesENS_6Header13LinkEditRangeE : 152 -> 160
~ ____chkstk_darwin : 12 -> 20
~ __ZNK6mach_o11GenericTrie14recursiveVisitEmmmRbU13block_pointerFvNSt3__14spanIKhLm18446744073709551615EEES1_EU13block_pointerFb7CStringymmS1_EPNS_5ErrorE : 756 -> 740
~ __ZN5dyld423ExternallyViewableState17createMinimalInfoERN3lsl9AllocatorEyPKcyS5_PK15DyldSharedCache : 1612 -> 1608
~ __ZN5dyld4L7prepareERNS_4APIsEPKN6mach_o12UnsafeHeaderE : 5640 -> 5656
~ ____ZN5dyld44APIs28_dyld_for_each_objc_protocolEPKcNS_16ReadOnlyCallbackIU13block_pointerFvPvbPbEEE_block_invoke : 164 -> 160
~ __ZN5dyld4L15fixupPageAuth64EPvPK12mwl_info_hdrPK30dyld_chained_starts_in_segmentjb : 384 -> 388
~ __ZNK6mach_o19GradedArchitectures9bestSliceENSt3__14spanIKhLm18446744073709551615EEERS4_ : 556 -> 552
~ __ZN5dyld3L10validMagicERKNS_18SharedCacheOptionsEPK15DyldSharedCache : 108 -> 132
~ __ZN5dyld412RuntimeState23recursiveMarkNonDelayedEPKNS_6LoaderEPNS1_14LinksWithChainES5_ : 664 -> 672
~ __ZN5dyld412RuntimeState18notifyDebuggerLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 760 -> 764
~ __ZN5dyld423ExternallyViewableState9addImagesERN3lsl9AllocatorES3_RKNSt3__14spanINS0_9ImageInfoELm18446744073709551615EEE : 1440 -> 1436
~ ____ZN5dyld416JustInTimeLoader14loadDependentsER11DiagnosticsRNS_12RuntimeStateERKNS_6Loader11LoadOptionsE_block_invoke : 988 -> 992
~ __ZN5dyld412RuntimeState13incDlRefCountEPKNS_6LoaderE : 284 -> 296
~ __ZNK6mach_o6Header22validStructureLinkeditERKNS_6PolicyEy : 1584 -> 1580
~ ____ZNK6mach_o5Image13validLinkeditERKNS_6PolicyE_block_invoke : 756 -> 760
~ __ZN5dyld46Loader11mapSegmentsER11DiagnosticsRNS_12RuntimeStateEPKciyRKNS0_19CodeSignatureInFileEbNSt3__14spanIKNS0_6RegionELm18446744073709551615EEEbbRKNS0_18FileValidationInfoE : 1500 -> 1496
~ __ZN5dyld46Loader12validateFileER11DiagnosticsRKNS_12RuntimeStateEiPKcRKNS0_19CodeSignatureInFileERKNS0_18FileValidationInfoE : 748 -> 752
~ __ZN5dyld416JustInTimeLoader4makeERNS_12RuntimeStateEPKN6mach_o12UnsafeHeaderEPKcRKNS_6FileIDEybbbt : 1320 -> 1328
~ __ZNK6mach_o5Image11exportsTrieEv : 188 -> 192
~ __ZN3lsl14ProtectedStack18withProtectedStackEU13block_pointerFvvE : 616 -> 628
- _OUTLINED_FUNCTION_35
~ __ZN5dyld412RuntimeState10notifyLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 1400 -> 1392
~ __ZZZN5dyld412RuntimeState10notifyLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEEEUb_ENK3$_8clEv : 1232 -> 1224
~ ____ZZN5dyld412RuntimeState16setObjCNotifiersENS_16ReadOnlyCallbackIPFvPKcPK11mach_headerEEENS1_IPFvS6_PvS6_PKvEEENS1_IPFvPK29_dyld_objc_notify_mapped_infoEEENS1_IPFvjSI_U13block_pointerFvjEEEEENK3$_0clEv_block_invoke : 1572 -> 1568
~ __ZZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEvENKUlvE_clEv : 3804 -> 3828
~ __ZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEv : 2524 -> 2520
~ ____ZN5dyld44APIs25_dyld_for_each_objc_classEPKcNS_16ReadOnlyCallbackIU13block_pointerFvPvbPbEEE_block_invoke : 164 -> 160
~ __ZN5dyld413ProcessConfig13PathOverridesC2ERKNS0_7ProcessERKNS0_8SecurityERKNS0_7LoggingERKNS0_9DyldCacheERNS_15SyscallDelegateERN3lsl9AllocatorE : 804 -> 808
~ __ZNK5dyld416JustInTimeLoader11matchesPathERKNS_12RuntimeStateEPKc : 268 -> 272
~ __ZNK5dyld413ProcessConfig7Process13forEachEnvVarEU13block_pointerFvNSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE7CStringRbE : 216 -> 212
~ __ZNK15DyldSharedCache29findLaunchLoaderSetWithCDHashEPKc : 180 -> 176
- _OUTLINED_FUNCTION_9
~ __ZN5dyld412RuntimeState18notifyDebuggerLoadEPKNS_6LoaderE : 364 -> 372
~ __ZN6mach_o5Image24forEachCodeDirectoryBlobEPKNS_6HeaderENSt3__14spanIKhLm18446744073709551615EEEU13block_pointerFvS7_E : 520 -> 532
~ __ZNK12objc_visitor7Visitor11findSectionENSt3__14spanIKPKcLm18446744073709551615EEES4_ : 232 -> 236
~ ____ZNK12objc_visitor7Visitor11findSectionENSt3__14spanIKPKcLm18446744073709551615EEES4__block_invoke : 280 -> 276
~ _OUTLINED_FUNCTION_2 : 24 -> 20
~ _OUTLINED_FUNCTION_33 : 12 -> 44
+ _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_34
~ _OUTLINED_FUNCTION_7 : 40 -> 24
+ _OUTLINED_FUNCTION_35
~ _OUTLINED_FUNCTION_35 : 44 -> 12
~ __ZN5dyld416JustInTimeLoader14loadDependentsER11DiagnosticsRNS_12RuntimeStateERKNS_6Loader11LoadOptionsE.cold.1 : 100 -> 104
~ ____ZNK5dyld311MachOLoaded21fixupAllChainedFixupsER11DiagnosticsPK28dyld_chained_starts_in_imagemNS_5ArrayIPKvEEU13block_pointerFvPvSA_E_block_invoke : 456 -> 460
~ __ZN5dyld46Loader8leafNameEPKc : 68 -> 72
~ __ZNK12PatchTableV214imageHasClientEjj : 112 -> 108
~ __ZNK12PatchTableV222forEachPatchableExportEjU13block_pointerFvjPKc9PatchKindE : 192 -> 188
~ __ZNK12PatchTableV234forEachPatchableUseOfExportInImageEjjjU13block_pointerFvjN6mach_o15PointerMetaDataEybE : 256 -> 252
~ __ZNK12PatchTableV434forEachPatchableUseOfExportInImageEjjjU13block_pointerFvjN6mach_o15PointerMetaDataEybE : 224 -> 220
~ __ZNK12PatchTableV232forEachPatchableCacheUseOfExportEjjyU13block_pointerFyjEU13block_pointerFvyN6mach_o15PointerMetaDataEybE : 480 -> 468
~ __ZNK12PatchTableV432forEachPatchableCacheUseOfExportEjjyU13block_pointerFyjEU13block_pointerFvyN6mach_o15PointerMetaDataEybE : 464 -> 448
~ __ZNK12PatchTableV330forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE : 356 -> 348
~ __ZNK12PatchTableV430forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE : 328 -> 320
~ __ZNK12PatchTableV231clientsExportsForImageAndClientEjj : 144 -> 140
~ ____ZNK5dyld313MachOAnalyzer15withChainStartsER11DiagnosticsyU13block_pointerFvPK28dyld_chained_starts_in_imageE_block_invoke : 452 -> 456
~ ____ZN5dyld44APIs24_dyld_visit_objc_classesENS_16ReadOnlyCallbackIU13block_pointerFvPKvEEE_block_invoke : 112 -> 108
~ __ZN3lsl6VectorI18AuthenticatedValueIPN5dyld411PseudoDylibEEE5eraseENS6_15CheckedIteratorIS5_EE : 184 -> 192
~ __ZN3lsl6VectorIPKN5dyld46LoaderEEcvNSt3__14spanIS4_Lm18446744073709551615EEEEv : 76 -> 84
~ __ZN5dyld412RuntimeState23recordInDataConstBitmapEy : 356 -> 368
~ __ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj : 1752 -> 1728
~ __ZN5dyld46Reaper14garbageCollectEv : 216 -> 200
~ __ZN5dyld412RuntimeState19garbageCollectInnerEv : 856 -> 872
~ __ZN5dyld412RuntimeState12notifyUnloadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 4612 -> 4540
~ __ZN5dyld412RuntimeState13removeLoadersERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 172 -> 164
~ ____ZN5dyld412RuntimeState12notifyDtraceERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE_block_invoke : 152 -> 156
~ __ZN5dyld412RuntimeState20notifyDebuggerUnloadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 364 -> 360
~ ____ZN5dyld412RuntimeState12notifyUnloadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE_block_invoke : 412 -> 408
~ ____ZN5dyld412RuntimeState12notifyUnloadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE_block_invoke_2 : 340 -> 336
~ __ZZN5dyld412RuntimeState28rebindMissingFlatLazySymbolsERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEEENK3$_0clERKNS0_17MissingFlatSymbolE : 296 -> 292
~ __ZN3lsl6VectorIN5dyld412RuntimeState11DlopenCountEE5eraseENS4_15CheckedIteratorIS3_EE : 184 -> 192
~ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZN5dyld412RuntimeLocks20withLoadersWriteLockIZNS2_12RuntimeState12notifyUnloadERKNSt3__14spanIPKNS2_6LoaderELm18446744073709551615EEEE3$_1EEvT_EUlvE_EEvSF__block_invoke : 568 -> 560
~ __ZN5dyld423ExternallyViewableState12removeImagesERN3lsl9AllocatorES3_RNSt3__14spanIPK11mach_headerLm18446744073709551615EEE : 1496 -> 1492
~ __ZN5dyld423ExternallyViewableState19removeRosettaImagesERNSt3__14spanIPK11mach_headerLm18446744073709551615EEE : 392 -> 388
~ __ZN5dyld46Loader16addWeakDefsToMapERNS_12RuntimeStateERKNSt3__14spanIPKS0_Lm18446744073709551615EEE : 248 -> 240
~ __ZN5dyld4L11fixupPage64EPvPK12mwl_info_hdrPK30dyld_chained_starts_in_segmentjb : 236 -> 240
~ __ZN5dyld4L12fixupChain32EPjPK12mwl_info_hdrPK30dyld_chained_starts_in_segmentPKjS0_ : 192 -> 196
~ __ZN5dyld412PrebuiltObjC22generatePerImageFixupsERNS_12RuntimeStateE : 636 -> 632
~ __ZN5dyld412PrebuiltObjC4makeER11DiagnosticsRNS_12RuntimeStateE : 3288 -> 3292
~ __ZN5dyld3L22preflightMainCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEPcPNSt3__15arrayIA32_cLm128EEE : 488 -> 528
~ _ccsha384_vng_arm_hw_compress : 4 -> 12
~ __ZNK6mach_o21FunctionVariantFixups5validENSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE : 188 -> 184
~ __ZNK6mach_o21FunctionVariantFixups12forEachFixupEU13block_pointerFvNS0_13InternalFixupEE : 88 -> 80
~ __ZNK6mach_o19GradedArchitectures8bestArchENSt3__14spanIKNS_12ArchitectureELm18446744073709551615EEE : 164 -> 148
~ __ZNK6mach_o19GradedArchitectures9archNamesER14CStringBuilder : 244 -> 240
~ __ZZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEvENKUlvE_clEv.cold.3 : 108 -> 116
~ ____ZNK6mach_o6Header20getAllLinkEditRangesERNSt3__14spanINS0_13LinkEditRangeELm18446744073709551615EEEPNS_5ErrorE_block_invoke.cold.2 : 300 -> 364
CStrings:
+ "16777228--2147483636"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:26:15 PDT 2026; root:libignition-64~19679/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:26:15 PDT 2026; root:libignition-64~19679/libignition_core/RELEASE_ARM64E"
+ "arm64.x1"
+ "arm64.x2"
+ "arm64e.x1"
+ "arm64e.x1.kernel"
+ "arm64e.x1.old"
+ "arm64e.x2"
+ "arm64e.x2.kernel"
+ "arm64e_x1"
+ "dyld_v1  arm64e"
+ "dyld_v1arm64ex1"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 22:12:59 PDT 2026; root:libignition-64~19689/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 22:12:59 PDT 2026; root:libignition-64~19689/libignition_core/RELEASE_ARM64E"
```
