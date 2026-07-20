## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__chain_fixups`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__common`

```diff

-1490.0.5.0.0
-  __TEXT.__text: 0x4ef094
+1490.0.20.0.0
+  __TEXT.__text: 0x4f1ecc
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__const: 0xf2260
-  __TEXT.__cstring: 0x3d8e2
-  __TEXT.__swift5_typeref: 0xcf0c
+  __TEXT.__const: 0xf2320
+  __TEXT.__cstring: 0x3df02
+  __TEXT.__swift5_typeref: 0xcf4c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0xb26c
+  __TEXT.__swift5_reflstr: 0xb27c
   __TEXT.__swift5_assocty: 0x7158
-  __TEXT.__swift5_fieldmd: 0x1256c
-  __TEXT.__constg_swiftt: 0x16368
+  __TEXT.__swift5_fieldmd: 0x125e0
+  __TEXT.__constg_swiftt: 0x163e0
   __TEXT.__swift5_builtin: 0xed8
   __TEXT.__swift5_mpenum: 0x534
   __TEXT.__swift5_protos: 0x494
-  __TEXT.__swift5_proto: 0x2e0c
-  __TEXT.__swift5_types: 0x1588
+  __TEXT.__swift5_proto: 0x2e14
+  __TEXT.__swift5_types: 0x1590
   __TEXT.__swift5_types2: 0x58
   __TEXT.__objc_methtype: 0x226
   __TEXT.__swift_as_entry: 0x22c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x21e4c
-  __DATA.__data: 0xce60
+  __TEXT.__eh_frame: 0x21efc
+  __DATA.__data: 0xcf50
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0x1130
-  __DATA.__const: 0x35668
+  __DATA.__auth_ptr: 0x1138
+  __DATA.__const: 0x35770
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x190

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x20
   __DATA.__common: 0x21ff1
-  __DATA.__bss: 0x1b7e8
+  __DATA.__bss: 0x1b818
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 19216
+  Functions: 19268
   Symbols:   29
-  CStrings:  6041
+  CStrings:  6081
 
CStrings:
+ "  %s:"
+ "  frame permissions: read%s%s\n"
+ "  removed permissions: %#06lx\n"
+ " %s"
+ " bytes) does not fit in one frame ("
+ " execute"
+ " write"
+ "%s boot untyped %#018lx { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s untyped { ftid=%#03x; base=%#018llx; size=%#018llx; types=%#08llx; perms=%#06lx }\n"
+ "%s(%zu): delete boot untyped %#018lx"
+ "%s(%zu): delete root normal r/w untyped cap"
+ "%s(%zu): delete root normal r/x untyped cap"
+ "(invalid type)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BOKs5n/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_first_contact.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotConclaveSupport.build/DerivedSources/StackshotDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/Modules/ConclaveSupportInternal/ConclaveSupportInternal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/StackshotConclaveSupport.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen+DSLList.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ConsumerInterface.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Engine/MEBuilder.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Regex/ASTConversion.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/exclave_launcher_new/xrtr_main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/BundleDERParserStandalone.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/CNode.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/ComponentResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/BootTimingResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ClientNotificationEndpointResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/CpuResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DeviceTreeResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DomainInitExecutionContextResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclaveKitImageResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclavesMemoryMapRegionResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExternalAddressSpaceServerResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitEndpointResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitExecutionContextResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/NamedMMIOResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/RingGateResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/SubgraphResource.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DERComponentGraph.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DTBlob.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExclaveCoreExternalVirtualSpace.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExclaveKitExternalVirtualSpace.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalPhysAllocator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/GraphReader.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/Macho.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/PMMInstance.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ResourceManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/StorageInterface.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/cbootinfo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/internalpmm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/l4_vspace_table.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/Launcher/DeviceTree.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "Boot-args string ("
+ "Empty-VLA endpoint marker missing argument position: "
+ "Empty-VLA marker collides with another argument at position "
+ "Failed to get bootargs "
+ "Failed to vas_slot_alloc() for boot-args"
+ "InternalExclaveLauncher/BootArgs.swift"
+ "L4_BootInfo_GetType(untyped_entry) == L4_Type_Untyped"
+ "L4_Type_"
+ "OWNERINFO"
+ "PMMInstance could not create Frame of "
+ "Unable to copy boot-args frame cap="
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
+ "dyld_enable_stdio"
+ "ensureDeviceTreeMapped()"
+ "exclave_disable_serial"
+ "exclaves_ec_initial_stack_frames"
+ "failed to mint boot-args cap"
+ "freed slot was not most recently allocated"
+ "init(allocateUntypedSize:with:rwFrames:)"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
+ "keeping"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:195)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:719)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2730)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2905)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:969)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:458)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:995)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1035)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
+ "malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:990)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1034)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:971)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sN9Alc/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
+ "received single-type untyped in roottask for type: %s"
+ "removed types"
+ "roottask finished"
+ "sanitized"
+ "types"
+ "x untyped must only be used to create r/x frame objects from normal managed memory, got (ftid: "
- "%s(%zu): Failed to copy frame parent cap to child cap"
- "%s(%zu): Failed to mint frame parent cap"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen+DSLList.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ByteCodeGen.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/ConsumerInterface.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Engine/MEBuilder.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift-experimental-string-processing/Sources/_StringProcessing/Regex/ASTConversion.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7TM16m/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/exclave_launcher_new/xrtr_main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/BundleDERParserStandalone.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/CNode.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/ComponentResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/BootTimingResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ClientNotificationEndpointResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/CpuResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DeviceTreeResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/DomainInitExecutionContextResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclaveKitImageResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExclavesMemoryMapRegionResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/ExternalAddressSpaceServerResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitEndpointResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/InitExecutionContextResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/NamedMMIOResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/RingGateResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ComponentResources/Types/SubgraphResource.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DERComponentGraph.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/DTBlob.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExclaveCoreExternalVirtualSpace.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExclaveKitExternalVirtualSpace.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalPhysAllocator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ExternalVirtualSpaceManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/GraphReader.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/Macho.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/PMMInstance.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/ResourceManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/StorageInterface.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/cbootinfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/internalpmm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/InternalExclaveLauncher/l4_vspace_table.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/exclave_launcher/frameworks/Launcher/DeviceTree.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotConclaveSupport.build/DerivedSources/StackshotDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/Modules/ConclaveSupportInternal/ConclaveSupportInternal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Sources/ExclaveStackshot_exclavecore/StackshotConclaveSupport/StackshotConclaveSupport.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_first_contact.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "Creating launcher IPMM freelist span"
- "Creating launcher frame zero span"
- "Entered main Sc"
- "InternalExclaveLauncher/RunFlags.swift"
- "Parsing bundle device"
- "Serialized boot timing data"
- "Serializing boot timing data..."
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Copy( frame_cap_parent, frame_cap_child)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Mint_Untyped( L4_BootInfo_GetSlot(entry), frame_cap_parent, (((L4_Word_t) 1) << (2)) | (((L4_Word_t) 1) << (1)), 0, 0, (((L4_TypeBitmap_t) 1) << (L4_Type_Arm64_FrameLevel0)), ((L4_Word_t) (0)) | (((L4_Word_t) 1) << (0)))'"
- "[StackshotConclaveSupport] discard_address_space_info no shared memory available"
- "[runflags warning] Couldn't get bootargs. Using metadata defaults only"
- "[xrt] liblibc_plat_cl4_entry:xrt__init_mapped_nonroot:default"
- "init(allocateUntypedSize:with:)"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:195)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:719)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2730)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2905)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:969)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:458)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:995)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1035)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:990)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1034)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:971)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2Y8Za7/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "mapDeviceTree()"
- "no fixup data for faultable range [%#lx, %#lx) found"
```
