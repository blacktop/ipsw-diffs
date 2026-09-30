## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

 27062.0.0.0.0
-  __TEXT.__text: 0x5c5cc
+  __TEXT.__text: 0x5c60c
   __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xe679
+  __TEXT.__cstring: 0xe699
   __TEXT.__unwind_info: 0x1ea8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0xb30
+  __DATA_CONST.__const: 0xb50
   __AUTH_CONST.__const: 0x3ee8
   __AUTH.__data: 0x470
   __DATA.__data: 0x1448

   __DATA.__common: 0x550
   __DATA_DIRTY.__all_image_info: 0x170
   Functions: 2756
-  Symbols:   2429
-  CStrings:  1468
+  Symbols:   2430
+  CStrings:  1470
 
Symbols:
+ __ZN5dyld3L14archCacheMagicE
Functions:
~ __ZNK12PatchTableV232forEachPatchableCacheUseOfExportEjjyU13block_pointerFyjEU13block_pointerFvyN6mach_o15PointerMetaDataEybE : 484 -> 480
~ __ZNK12PatchTableV432forEachPatchableCacheUseOfExportEjjyU13block_pointerFyjEU13block_pointerFvyN6mach_o15PointerMetaDataEybE : 464 -> 460
~ __ZN5dyld44APIs17findImageMappedAtEPKvPPKN6mach_o12UnsafeHeaderEPbPPKcPS2_PyPhPPKNS_6LoaderE : 924 -> 936
~ __ZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEv : 1852 -> 1848
~ __ZZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEvENKUlvE_clEv : 3228 -> 3248
~ __ZN3lsl6VectorI18AuthenticatedValueIPN5dyld411PseudoDylibEEE5eraseENS6_15CheckedIteratorIS5_EE : 164 -> 172
~ ____ZN5dyld412RuntimeState19addDynamicReferenceEPKNS_6LoaderES3__block_invoke : 180 -> 192
~ __ZN5dyld412RuntimeState18notifyDebuggerLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 620 -> 624
~ __ZN5dyld412RuntimeState10notifyLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE : 940 -> 932
~ __ZZN5dyld412RuntimeState28rebindMissingFlatLazySymbolsERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEEENK3$_0clERKNS0_17MissingFlatSymbolE : 300 -> 296
~ ____ZZN5dyld412RuntimeState16setObjCNotifiersENS_16ReadOnlyCallbackIPFvPKcPK11mach_headerEEENS1_IPFvS6_PvS6_PKvEEENS1_IPFvPK29_dyld_objc_notify_mapped_infoEEENS1_IPFvjSI_U13block_pointerFvjEEEEENK3$_0clEv_block_invoke : 1384 -> 1380
~ __ZN5dyld423ExternallyViewableState9addImagesERN3lsl9AllocatorES3_RKNSt3__14spanINS0_9ImageInfoELm18446744073709551615EEE : 1156 -> 1152
~ __ZNK5dyld416JustInTimeLoader11matchesPathERKNS_12RuntimeStateEPKc : 228 -> 232
~ ____ZN5dyld416JustInTimeLoader14loadDependentsER11DiagnosticsRNS_12RuntimeStateERKNS_6Loader11LoadOptionsE_block_invoke : 948 -> 952
~ __ZN5dyld46Loader16addWeakDefsToMapERNS_12RuntimeStateERKNSt3__14spanIPKS0_Lm18446744073709551615EEE : 260 -> 256
~ __ZN5dyld46Loader9interposeERNS_12RuntimeStateEmPKS0_ : 504 -> 516
~ ____ZNK5dyld46Loader27applyCachePatchesToOverrideERNS_12RuntimeStateEPKS0_tPKNS0_10DylibPatchERNS_34DyldCacheDataConstLazyScopedWriterE_block_invoke_2 : 680 -> 692
~ __ZN5dyld415PremappedLoader4makeERNS_12RuntimeStateEPKN6mach_o12UnsafeHeaderEPKcbbt : 1012 -> 1020
~ __ZN5dyld3L18preflightCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEiPNSt3__15arrayIA32_cLm128EEEPKS3_ : 1176 -> 1200
~ ____ZN5dyld3L26verboseSharedCacheMappingsEPK15DyldSharedCache_block_invoke : 72 -> 68
~ ___liblibc_memset : 240 -> 224
~ __ZNK6mach_o21FunctionVariantFixups12forEachFixupEU13block_pointerFvNS0_13InternalFixupEE : 88 -> 80
~ __ZNK6mach_o5Image13linkeditBytesENS_6Header13LinkEditRangeE : 172 -> 180
CStrings:
+ "dyld_v1  arm64e"
+ "dyld_v1arm64ex1"
```
