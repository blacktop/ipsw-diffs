## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__bss`
- `__DATA.__common`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`
- `__PDATA.__common`

```diff

-1777.0.16.0.0
-  __TEXT.__text: 0x5c68d8
+1777.0.20.0.0
+  __TEXT.__text: 0x5c7fb8
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0x4df91
-  __TEXT.__const: 0x11f1d4
+  __TEXT.__cstring: 0x4e081
+  __TEXT.__const: 0x11f234
   __TEXT.__swift5_typeref: 0x12eb8
-  __TEXT.__swift5_reflstr: 0x111b8
+  __TEXT.__swift5_reflstr: 0x11228
   __TEXT.__swift5_assocty: 0x78e8
-  __TEXT.__swift5_fieldmd: 0x1a5cc
-  __TEXT.__constg_swiftt: 0x2594c
+  __TEXT.__swift5_fieldmd: 0x1a614
+  __TEXT.__constg_swiftt: 0x25984
   __TEXT.__swift5_protos: 0x8a4
   __TEXT.__swift5_proto: 0x394c
   __TEXT.__swift5_types: 0x2204

   __TEXT.__swift5_builtin: 0x1568
   __TEXT.__swift5_capture: 0xf9c
   __TEXT.__objc_methtype: 0xe1
-  __TEXT.__swift5_mpenum: 0x3cc
+  __TEXT.__swift5_mpenum: 0x39c
   __TEXT.__swift_as_entry: 0x994
   __TEXT.__swift_as_ret: 0xb08
   __TEXT.__swift_as_cont: 0x11f8

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb0
-  __TEXT.__eh_frame: 0x32dcc
+  __TEXT.__eh_frame: 0x32dc4
   __DATA.__TIGHTBEAM_VT: 0x720
   __DATA.__TIGHTBEAM: 0x1d8
-  __DATA.__const: 0x3ab98
-  __DATA.__data: 0x16618
+  __DATA.__const: 0x3abb8
+  __DATA.__data: 0x16650
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x1a221
   __DATA.__auth_ptr: 0x1fd8

   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xc4a8
+  __PDATA.__bss: 0xc4b8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 22431
+  Functions: 22442
   Symbols:   1
-  CStrings:  7114
+  CStrings:  7123
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/EntropyBroker.build/DerivedSources/EntropyBroker_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotPanicInfo_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotSupport_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/DeviceMemoryContext/device_memory_context.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmem-util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmemory.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xnu-proxy/panic-handler/panic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/irq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/notify.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/debug/trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2RnX0V/Sources/ExclavePlatform_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadWriteMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadWriteMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericDMAMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5fVTMW/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericPreparation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BOKs5n/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Binaries/libtrace_exclavecore/install/TempContent/Objects/libtrace.build/libtrace_exclavecore.build/DerivedSources/OSLogExclaves_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/LogServerExclaves/Sources/Overlay/libtrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/backtrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/console.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/format.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/log.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/log_server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/tracepoint_internal.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BUzbve/Sources/libtrace_exclavecore/libtrace-exclaves/utils.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Components/ComponentRuntime.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_first_contact.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C0LF1X/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateComponent_ec.build/DerivedSources/StackshotDelegateComponent_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateSupport_ec.build/DerivedSources/StackshotDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ff9iYt/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PBwZw7/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer-utils.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PBwZw7/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PBwZw7/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/shmem_component_helper.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PHD2Xt/Binaries/ExclaveStackshot_services_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotLayoutManagerComponent.build/DerivedSources/StackshotLayoutManagerComponent_c.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SrFklq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPControl.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SrFklq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPEndpoint.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SrFklq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XKUcCZ/Sources/DebugExclave_exclavecore/debug/dbgexclave_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bLPqjD/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/xnu-proxy.build/xnu-proxy.build/DerivedSources/XnuProxy_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/XrtHosted/hosted.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/allocator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/constant.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/cpus.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler_early_init.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/turnstile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/downcall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/exclaves.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/panic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/upcall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rSgAJi/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/xnu.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rkWezK/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddy.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rkWezK/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddyDeviceTreeHelper.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rkWezK/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddyCore/RTBuddyCL4ProxyConnection.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zIIR3q/Sources/DriverKit_services_exclavecore/ExclaveDriverKit/DeviceServer/DeviceServerCapabilities/DeviceServerCapabilities.c"
+ "1"
+ "OWNERINFO"
+ "Stop prox policy (reset)"
+ "[B] Stop prox policy (reset)"
+ "exbright_mot_enable"
+ "failed to shutdown host with exit code: %d"
+ "freed slot was not most recently allocated"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
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
+ "policy-override-chill-pill"
+ "policy-override-chill-pill exceeds MOT, setting back to default to "
+ "yes"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4wxuNq/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.69qzzx/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddy.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.69qzzx/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddyDeviceTreeHelper.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.69qzzx/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddyCore/RTBuddyCL4ProxyConnection.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7TM16m/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/xnu-proxy.build/xnu-proxy.build/DerivedSources/XnuProxy_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/XrtHosted/hosted.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/allocator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/constant.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/cpus.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler_early_init.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/turnstile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/downcall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/exclaves.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/panic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/upcall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/xnu.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DOLG9e/Sources/DebugExclave_exclavecore/debug/dbgexclave_message.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DaTLCO/Binaries/ExclaveStackshot_services_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotLayoutManagerComponent.build/DerivedSources/StackshotLayoutManagerComponent_c.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadWriteMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadWriteMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericDMAMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericPreparation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GuUu1k/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer-utils.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GuUu1k/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GuUu1k/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/shmem_component_helper.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateComponent_ec.build/DerivedSources/StackshotDelegateComponent_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateSupport_ec.build/DerivedSources/StackshotDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fPU5k2/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Components/ComponentRuntime.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_first_contact.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Binaries/libtrace_exclavecore/install/TempContent/Objects/libtrace.build/libtrace_exclavecore.build/DerivedSources/OSLogExclaves_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/LogServerExclaves/Sources/Overlay/libtrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/backtrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/console.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/format.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/log.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/log_server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/tracepoint_internal.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.p5QOL6/Sources/libtrace_exclavecore/libtrace-exclaves/utils.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vIKaKX/Sources/DriverKit_services_exclavecore/ExclaveDriverKit/DeviceServer/DeviceServerCapabilities/DeviceServerCapabilities.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/EntropyBroker.build/DerivedSources/EntropyBroker_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotPanicInfo_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotSupport_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/DeviceMemoryContext/device_memory_context.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmem-util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmemory.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xnu-proxy/panic-handler/panic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/irq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/notify.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/debug/trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vupMeC/Sources/ExclavePlatform_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zg4NIx/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPControl.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zg4NIx/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPEndpoint.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zg4NIx/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPManager.swift"
- "[SCHED] Scheduling %s 0x%04hx (%zu/%zu)\n"
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
- "no fixup data for faultable range [%#lx, %#lx) found"
- "non-zero exit return: %d"
```
