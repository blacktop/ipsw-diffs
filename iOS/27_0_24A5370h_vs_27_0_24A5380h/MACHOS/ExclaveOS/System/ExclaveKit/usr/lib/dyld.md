## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

-  __TEXT.__text: 0x5b508
+  __TEXT.__text: 0x5bb58
   __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xe4dd
-  __TEXT.__unwind_info: 0x1e68
+  __TEXT.__cstring: 0xe51e
+  __TEXT.__unwind_info: 0x1e80
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0xaf0
-  __AUTH_CONST.__const: 0x3e58
+  __AUTH_CONST.__const: 0x3ee8
   __AUTH.__data: 0x470
   __DATA.__data: 0x1448
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__common: 0x550
   __DATA.__bss: 0xba3f8
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2737
-  Symbols:   2861
-  CStrings:  1460
+  Functions: 2744
+  Symbols:   2871
+  CStrings:  1461
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA_DIRTY.__all_image_info : content changed
Symbols:
+ _OUTLINED_FUNCTION_15
+ _ZNK5dyld46Loader14getExportsTrieERyRj
+ __ZN5dyld3L18preflightCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEiPNSt3__15arrayIA32_cLm128EEEPKS3_
+ __ZNK10PatchTable30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK12PatchTableV330forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK12PatchTableV430forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK15DyldSharedCache14fixupDataPagesElb
+ __ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE
+ __ZNK15DyldSharedCache30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybb12GOTPatchKindE
+ __ZNK5dyld39MachOFile13hasExportTrieERyRj
+ __ZNK5dyld39MachOFile18forEachLoadCommandER11DiagnosticsU13block_pointerFvPK12load_commandRbE
+ __ZNK5dyld413ProcessConfig9DyldCache13areGotsMappedEv
+ __ZNK5dyld416JustInTimeLoader14getExportsTrieERyRj
+ __ZNK5dyld46Loader14getExportsTrieERyRj
+ __ZNK6mach_o12UnsafeHeader25headerAndLoadCommandsSizeEv
+ __ZNK6mach_o6Header10hasSegmentE7CString
+ ___ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke
+ ___ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke_2
+ ____ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke
+ ____ZNK6mach_o6Header10hasSegmentE7CString_block_invoke
+ _write_float_string
- _ZN5dyld413ProcessConfig7ProcessC2EPKNS_10KernelArgsERNS_15SyscallDelegateERN3lsl9AllocatorE
- __ZN5dyld317OverflowSafeArrayIN5dyld418PreMappedFileEntryELy4294967295EE6resizeEy
- __ZN5dyld317OverflowSafeArrayIN5dyld418PreMappedFileEntryELy4294967295EE9push_backEOS2_
- __ZN5dyld3L18preflightCacheFileERKNS_18SharedCacheOptionsEPNS_19SharedCacheLoadInfoEPNS_9CacheInfoEiPNSt3__15arrayIA32_cLm128EEE
- __ZN6mach_o12read_uleb128ENSt3__14spanIKhLm18446744073709551615EEERmRb
- __ZNK10PatchTable30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK12PatchTableV330forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK12PatchTableV430forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK15DyldSharedCache14fixupDataPagesEl
- __ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK15DyldSharedCache30forEachPatchableGOTUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE
- __ZNK6mach_o11GenericTrie14recursiveVisitEmmmRbU13block_pointerFvNSt3__14spanIKhLm18446744073709551615EEES1_EU13block_pointerFb7CStringymmS1_EPNS_5ErrorE
- ___ZNK6mach_o11GenericTrie4findE7CStringb_block_invoke
- ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEybE_block_invoke
- ____ZNK6mach_o11GenericTrie4findE7CStringb_block_invoke
- _write_float
CStrings:
+ "  including auth GOT mapping\n"
+ "  skipping auth GOT mapping\n"
+ "27059.3"
+ "__AUTH_CONST_GOT"
+ "__ETC"
+ "getExportsTrie"
+ "malformed load command #%u of %u at %p with mh=%p, extends past sizeofcmds"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) is too large, load commands end at %p"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) not multiple of 4"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) too small"
+ "v36@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28I32"
+ "v40@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28B32I36"
+ "write_float_string"
- "27056"
- "B56@?0{CString=*Q}8Q24Q32Q40^B48"
- "Process"
- "malformed trie node, child node name extends beyond trie data"
- "malformed trie, childNodeOffset==0"
- "malformed trie, node offset=0x%04lX past end=0x%04lX"
- "malformed trie, terminalSize extends beyond trie data at offset=0x%04lX"
- "malformed uleb128 for child node offset at 0x%04lX"
- "malformed uleb128 for terminal payload size at offset=0x%04lX"
- "this->startupContractVersion == 1"
- "v32@?0{span<const unsigned char, 18446744073709551615UL>=*Q}8^B24"
- "write_float"

```
