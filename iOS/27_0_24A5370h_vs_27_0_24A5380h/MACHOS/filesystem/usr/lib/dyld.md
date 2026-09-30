## dyld

> `/usr/lib/dyld`

```diff

-  __TEXT.__text: 0x9e104
+  __TEXT.__text: 0x9e8bc
   __TEXT.__const: 0x1978
-  __TEXT.__cstring: 0x12295
-  __TEXT.__unwind_info: 0x3590
-  __DATA_CONST.__const: 0x5540
+  __TEXT.__cstring: 0x12497
+  __TEXT.__unwind_info: 0x35b0
+  __DATA_CONST.__const: 0x5590
   __AUTH_CONST.__const: 0x2758
-  __DATA.__data: 0x1c8
+  __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0
   __DATA.__bss: 0x508
+  __DATA_DIRTY.__data: 0x6c
   __DATA_DIRTY.__all_image_info: 0x170
-  __DATA_DIRTY.__data: 0x64
   __DATA_DIRTY.__common: 0x1160
   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3414
-  Symbols:   4681
-  CStrings:  2227
+  Functions: 3421
+  Symbols:   4684
+  CStrings:  2243
 
Sections:
~ __TEXT.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA_DIRTY.__all_image_info : content changed
Symbols:
+ _ZNK5dyld46Loader14getExportsTrieERyRj
+ __ZN5dyld3L18preflightCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEiPNSt3__15arrayIA32_cLm128EEEPKS3_
+ __ZN5dyld3L21preflightSubCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEPcPKcPKS3_
+ __ZNK10PatchTable30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK12PatchTableV330forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK12PatchTableV430forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK15DyldSharedCache14fixupDataPagesElb
+ __ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE
+ __ZNK15DyldSharedCache30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK5dyld39MachOFile13hasExportTrieERyRj
+ __ZNK5dyld412RuntimeState34allowProgramsToSaveUpdatedClosuresEPKNS_17PrebuiltLoaderSetENSt3__18optionalI7CStringEE
+ __ZNK5dyld413ProcessConfig9DyldCache13areGotsMappedEv
+ __ZNK5dyld414PrebuiltLoader14getExportsTrieERyRj
+ __ZNK5dyld416JustInTimeLoader14getExportsTrieERyRj
+ __ZNK5dyld46Loader14getExportsTrieERyRj
+ __ZNK6mach_o12UnsafeHeader25headerAndLoadCommandsSizeEv
+ __ZNK6mach_o6Policy26enforceSegmentSectionNamesEv
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke_2
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke_3
+ ____ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke
+ ____ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke_2
- __ZN5dyld38MultiMapI43SwiftTypeProtocolConformanceDiskLocationKey40SwiftTypeProtocolConformanceDiskLocationN5dyld422HashTypeConformanceKeyENS3_23EqualTypeConformanceKeyEEC1EPvPKy
- __ZN5dyld38MultiMapI47SwiftMetadataProtocolConformanceDiskLocationKey44SwiftMetadataProtocolConformanceDiskLocationN5dyld426HashMetadataConformanceKeyENS3_27EqualMetadataConformanceKeyEEC1EPvPKy
- __ZN5dyld38MultiMapI50SwiftForeignTypeProtocolConformanceDiskLocationKey47SwiftForeignTypeProtocolConformanceDiskLocationN5dyld425HashForeignConformanceKeyENS3_26EqualForeignConformanceKeyEEC1EPvPKy
- __ZN5dyld3L18preflightCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEiPNSt3__15arrayIA32_cLm128EEE
- __ZN5dyld3L21preflightSubCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEPcPKc
- __ZN6mach_o12read_uleb128ENSt3__14spanIKhLm18446744073709551615EEERmRb
- __ZNK10PatchTable30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK12PatchTableV330forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK12PatchTableV430forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK15DyldSharedCache14fixupDataPagesEl
- __ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK15DyldSharedCache30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE_block_invoke
- ____ZNK6mach_o11GenericTrie4findE7CStringb_block_invoke
- ____ZNK6mach_o11GenericTrie4findE7CStringb_block_invoke_2
CStrings:
+ "  including auth GOT mapping\n"
+ "  skipping auth GOT mapping\n"
+ "/AppleInternal/"
+ "27059.3"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Jul  1 23:22:14 PDT 2026; root:libignition-64~9224/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Wed Jul  1 23:22:14 PDT 2026; root:libignition-64~9224/libignition_core/RELEASE_ARM64E"
+ "__AUTH_CONST_GOT"
+ "customer"
+ "development"
+ "dyld cache mapped system-wide: %s, auth GOTs: %s\n"
+ "getExportsTrie"
+ "mapped"
+ "section '%s' has an empty segment name"
+ "section '%s' segment name '%s' does not match containing segment's name '%s'"
+ "section in segment '%s' has an empty section name"
+ "segment load command has an empty segment name"
+ "unmapped"
+ "v36@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28I32"
+ "v40@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28B32I36"
- "27056"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Jun 18 19:34:31 PDT 2026; root:libignition-64~7581/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Jun 18 19:34:31 PDT 2026; root:libignition-64~7581/libignition_core/RELEASE_ARM64E"

```
