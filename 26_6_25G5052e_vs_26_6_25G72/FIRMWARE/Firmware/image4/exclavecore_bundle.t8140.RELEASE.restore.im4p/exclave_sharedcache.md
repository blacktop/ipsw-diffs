## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__bss`
- `__DATA.__common`
- `__PDATA.__data`
- `__PDATA.__const`
- `__PDATA.__shared_cache`
- `__PDATA.__mod_init_func`
- `__PDATA.__auth_ptr`
- `__PDATA.__bss`
- `__PDATA.__common`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0x5d2cf4
+  __TEXT.__text: 0x5d1820
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x498a1
+  __TEXT.__cstring: 0x498d1
   __TEXT.__const: 0x112864
   __TEXT.__swift5_typeref: 0x11c20
   __TEXT.__swift5_reflstr: 0xf458

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xa8
-  __TEXT.__eh_frame: 0x326a0
+  __TEXT.__eh_frame: 0x32530
   __DATA.__TIGHTBEAM_VT: 0x600
   __DATA.__TIGHTBEAM: 0x190
   __DATA.__data: 0x13ac8

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 23390
+  Functions: 23397
   Symbols:   1
-  CStrings:  6767
+  CStrings:  6768
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadWriteMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadWriteMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericDMAMap.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1nwbZ6/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericPreparation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/xnu-proxy.build/xnu-proxy.build/DerivedSources/XnuProxy_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/XrtHosted/hosted.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/allocator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/constant.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/cpus.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler_early_init.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/turnstile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/downcall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/exclaves.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/panic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/upcall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3nPjZL/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/xnu.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Components/ComponentRuntime.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.88dxNd/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotPanicInfo_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotSupport_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmem-util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmemory.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xnu-proxy/panic-handler/panic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/irq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/notify.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/debug/trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ACOXcv/Sources/ExclavePlatform_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AMEOdJ/Sources/DriverKit_services_exclavecore/ExclaveDriverKit/DeviceServer/DeviceServerCapabilities/DeviceServerCapabilities.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Binaries/libtrace_exclavecore/install/TempContent/Objects/libtrace.build/libtrace_exclavecore.build/DerivedSources/OSLogExclaves_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/LogServerExclaves/Sources/Overlay/libtrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/backtrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/console.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/format.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/log.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/log_server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/tracepoint_internal.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.E67AXG/Sources/libtrace_exclavecore/libtrace-exclaves/utils.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.H6bHQu/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer-utils.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.H6bHQu/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.H6bHQu/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/shmem_component_helper.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QxcmJX/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VS8BXk/Sources/DebugExclave_exclavecore/debug/dbgexclave_message.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.amEOVq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPControl.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.amEOVq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPEndpoint.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.amEOVq/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateComponent_ec.build/DerivedSources/StackshotDelegateComponent_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateSupport_ec.build/DerivedSources/StackshotDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fG3tUh/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hoDS2o/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddy.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hoDS2o/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddyDeviceTreeHelper.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hoDS2o/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddyCore/RTBuddyCL4ProxyConnection.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qXsR1T/Binaries/ExclaveStackshot_services_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotLayoutManagerComponent.build/DerivedSources/StackshotLayoutManagerComponent_c.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sLoSrR/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
+ "freed slot was not most recently allocated"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/xnu-proxy.build/xnu-proxy.build/DerivedSources/XnuProxy_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/XrtHosted/hosted.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/allocator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/constant.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/cpus.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/scheduler_early_init.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/thread.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/native-scheduler/native-scheduler/turnstile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/downcall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/exclaves.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/panic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/upcall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xnu-proxy/src/xnu.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EgGMrP/Binaries/ExclaveSharedMemory_exclavecore/install/TempContent/Objects/ExclaveSharedMemory.build/SharedMemory_ec.build/DerivedSources/SharedMemory_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S27XVa/Sources/DriverKit_services_exclavecore/ExclaveDriverKit/DeviceServer/DeviceServerCapabilities/DeviceServerCapabilities.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateComponent_ec.build/DerivedSources/StackshotDelegateComponent_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Binaries/ExclaveStackshot_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotDelegateSupport_ec.build/DerivedSources/StackshotDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.TMNwWb/Sources/ExclaveStackshot_exclavecore/StackshotDelegateComponent/stackshot_delegate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WsF6ZW/Binaries/ExclaveStackshot_services_exclavecore/install/TempContent/Objects/ExclaveStackshot.build/StackshotLayoutManagerComponent.build/DerivedSources/StackshotLayoutManagerComponent_c.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Binaries/libtrace_exclavecore/install/TempContent/Objects/libtrace.build/libtrace_exclavecore.build/DerivedSources/OSLogExclaves_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/LogServerExclaves/Sources/Overlay/libtrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/backtrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/console.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/format.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/log.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/log_server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/tracepoint_internal.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGB6Uc/Sources/libtrace_exclavecore/libtrace-exclaves/utils.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c93mdV/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddy.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c93mdV/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddy/SecureRTBuddyDeviceTreeHelper.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c93mdV/Sources/RTBuddy_exclavecore/RTBuddyExclaves/SecureRTBuddyCore/RTBuddyCL4ProxyConnection.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Components/ComponentRuntime.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBW3q1/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer-utils.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBW3q1/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/SharedMemoryServer.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBW3q1/Sources/ExclaveSharedMemory_services_exclavecore/SharedMemoryComponent/shmem_component_helper.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorDMADeviceReadWriteMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_AnyIOMemoryDescriptor/_AnyIOMemoryDescriptorReadWriteMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericDMAMap.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/ExclaveDriverKit/Memory/_IOMemoryDescriptorGeneric/_IOMemoryDescriptorGenericPreparation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotPanicInfo_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Binaries/ExclavePlatform_exclavecore/install/TempContent/Objects/xnu-proxy.build/panichandler.build/DerivedSources/StackshotSupport_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/liblibc_plat_cl4_standalone/liblibc_plat_cl4_vmem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmem-util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmemory.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xnu-proxy/panic-handler/panic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/irq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/notify.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/debug/trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nOkDRn/Sources/ExclavePlatform_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oxYQOD/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPControl.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oxYQOD/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPEndpoint.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oxYQOD/Sources/AppleSEPManager_exclavecore/ExclaveSEPManager/Sources/ExclaveSEPManager/ExclaveSEPManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sSAsRU/Sources/swiftlang_stdlib_exclavecore/swift/lib/Demangling/Demangler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zJ0wXs/Sources/DebugExclave_exclavecore/debug/dbgexclave_message.c"
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
