## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t6050.RELEASE.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__chain_fixups`
- `__DATA.__data`
- `__DATA.__mod_init_func`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__common`

```diff

-1195.160.7.0.1
-  __TEXT.__text: 0x4bb500
+1195.160.9.0.0
+  __TEXT.__text: 0x4bad9c
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xedbe0
-  __TEXT.__cstring: 0x3b672
-  __TEXT.__swift5_typeref: 0xc122
+  __TEXT.__const: 0xedba0
+  __TEXT.__cstring: 0x3bbb2
+  __TEXT.__swift5_typeref: 0xc152
   __TEXT.__swift5_capture: 0x1608
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_fieldmd: 0x11008

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1cecc
+  __TEXT.__eh_frame: 0x1ce14
   __DATA.__data: 0xbe90
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0xfa0
-  __DATA.__const: 0x30b88
+  __DATA.__auth_ptr: 0xfa8
+  __DATA.__const: 0x30c38
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x198

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__common: 0x21fb1
-  __DATA.__bss: 0x13100
+  __DATA.__bss: 0x13130
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 17667
+  Functions: 17683
   Symbols:   27
-  CStrings:  5882
+  CStrings:  5916
 
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " execute"
+ " write"
+ "%s boot untyped %#018lx { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s(%zu): delete boot untyped %#018lx"
+ "%s(%zu): delete root normal r/w untyped cap"
+ "%s(%zu): delete root normal r/x untyped cap"
+ "(invalid type)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/exclave_launcher_new/xrtr_main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/BundleDERParserStandalone.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/CNode.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/ComponentResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/BootTimingResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ClientNotificationEndpointResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/CpuResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DeviceTreeResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DomainInitExecutionContextResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclaveKitImageResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclavesMemoryMapRegionResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExternalAddressSpaceServerResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitEndpointResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitExecutionContextResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/NamedMMIOResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/RingGateResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/SubgraphResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DERComponentGraph.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DTBlob.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalPhysAllocator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceRaw.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceVAS.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/GraphReader.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/Macho.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/PMMInstance.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ResourceManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/StorageInterface.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/cbootinfo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/internalpmm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/l4_vspace_table.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/Launcher/DeviceTree.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Jx4EoM/Sources/SystemBundler_exclavecore/lib/ComponentGraph/ComponentGraph.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ConsumerInterface.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Engine/MEBuilder.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Regex/ASTConversion.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotConclaveSupport.build/DerivedSources/StackshotDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/Modules/ConclaveSupportInternal/ConclaveSupportInternal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/StackshotConclaveSupport.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sLoSrR/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "PMMInstance could not create Frame of "
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( _boot_info.normal_untyped.rw_cap, frame_cap_parent )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy(_boot_info.normal_untyped.rx_cap, slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(L4_BootInfo_GetSlot(entry))'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(_boot_info.normal_untyped.rw_cap)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(_boot_info.normal_untyped.rx_cap)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( source_cap, dest_slot, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), L4_BootInfo_Untyped_GetBase(untyped_entry), L4_BootInfo_Untyped_GetSize(untyped_entry), type_bitmap, permissions )'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Move(entry_slot, temp_slot)'"
+ "_mint_reduced_untyped"
+ "_sanitize_untyped_entry"
+ "attempted to copy non-existant normal r/x untyped"
+ "cannot sanitize untypeds before bootinfo initialized"
+ "cbinfo_copy_normal_rx_untyped"
+ "cbinfo_drop_untypeds"
+ "created"
+ "deleting"
+ "derived"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "keeping"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8165)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7639)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2586)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2701)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7236)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:871)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:897)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:937)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6254)"
+ "malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:936)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:873)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2110)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Im8pcK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5129)"
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/exclave_launcher_new/xrtr_main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/BundleDERParserStandalone.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/CNode.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/ComponentResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/BootTimingResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ClientNotificationEndpointResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/CpuResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DeviceTreeResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DomainInitExecutionContextResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclaveKitImageResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclavesMemoryMapRegionResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExternalAddressSpaceServerResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitEndpointResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitExecutionContextResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/NamedMMIOResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/RingGateResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/SubgraphResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DERComponentGraph.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DTBlob.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalPhysAllocator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceRaw.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceVAS.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/GraphReader.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/Macho.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/PMMInstance.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ResourceManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/StorageInterface.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/cbootinfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/internalpmm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/l4_vspace_table.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/Launcher/DeviceTree.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EgGMrP/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotConclaveSupport.build/DerivedSources/StackshotDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/Modules/ConclaveSupportInternal/ConclaveSupportInternal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/StackshotConclaveSupport.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eiclaD/Sources/SystemBundler_exclavecore/lib/ComponentGraph/ComponentGraph.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ConsumerInterface.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Engine/MEBuilder.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Regex/ASTConversion.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
- "PMMInstance could not create Frame"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "init(allocateUntypedSize:with:)"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8165)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7639)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2581)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2696)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7236)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6254)"
- "malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2110)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o9AZ1x/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5129)"
```
