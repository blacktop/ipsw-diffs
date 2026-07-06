## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

-  __TEXT.__text: 0x5b73c
+  __TEXT.__text: 0x5bc7c
   __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xea6c
-  __TEXT.__unwind_info: 0x1e88
+  __TEXT.__cstring: 0xeaa5
+  __TEXT.__unwind_info: 0x1ea0
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0xaf0
-  __AUTH_CONST.__const: 0x3eb8
+  __AUTH_CONST.__const: 0x3f18
   __AUTH.__data: 0x470
   __DATA.__data: 0x1448
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__common: 0x550
   __DATA.__bss: 0xba3f8
   __DATA_DIRTY.__all_image_info: 0x170
-  Functions: 2740
-  Symbols:   2865
+  Functions: 2746
+  Symbols:   2872
   CStrings:  1463
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA_DIRTY.__all_image_info : content changed
Symbols:
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
+ ___ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke
+ ___ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke
+ ____ZNK15DyldSharedCache27forEachPatchableUseOfExportEjjU13block_pointerFvyN6mach_o15PointerMetaDataEyb12GOTPatchKindE_block_invoke_2
+ ____ZNK5dyld39MachOFile13hasExportTrieERyRj_block_invoke
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qjqnf0/Sources/libclosure_exclavekit/runtime.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/Array.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/CString.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/MachOLayout.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/Loader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Allocator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Allocator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Header.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Image.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Platform.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
+ "27059.3"
+ "__AUTH_CONST_GOT"
+ "getExportsTrie"
+ "malformed load command #%u of %u at %p with mh=%p, extends past sizeofcmds"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) is too large, load commands end at %p"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) not multiple of 4"
+ "malformed load command #%u of %u at %p with mh=%p, size (0x%X) too small"
+ "v36@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28I32"
+ "v40@?0Q8{PointerMetaData=b16b8b1b2b1b4}16Q20B28B32I36"
+ "write_float_string"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.450478/Sources/libclosure_exclavekit/runtime.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/Array.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/CString.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/MachOLayout.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/Loader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Allocator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Allocator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Header.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Image.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Platform.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
- "27056.1"
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
