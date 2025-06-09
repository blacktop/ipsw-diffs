## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-118.0.0.0.0
-  __TEXT.__text: 0x1fced4
-  __TEXT.__auth_stubs: 0x1610
-  __TEXT.__const: 0x1ad4e0
-  __TEXT.__cstring: 0x18f51
-  __TEXT.__oslogstring: 0x64c
-  __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__unwind_info: 0x2370
-  __TEXT.__eh_frame: 0xd8
-  __TEXT.__objc_methname: 0x9b
-  __TEXT.__objc_stubs: 0x100
+133.0.2.0.0
+  __TEXT.__text: 0x2211cc
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__const: 0x1adf40
+  __TEXT.__cstring: 0x19769
+  __TEXT.__oslogstring: 0x6b0
+  __TEXT.__gcc_except_tab: 0x25c
+  __TEXT.__unwind_info: 0x2160
+  __TEXT.__eh_frame: 0xe0
+  __TEXT.__objc_methname: 0xa9
+  __TEXT.__objc_stubs: 0x120
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x48a40
+  __DATA_CONST.__const: 0x48a20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0xb18
-  __AUTH_CONST.__const: 0x63a8
-  __AUTH_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x48
+  __AUTH_CONST.__auth_got: 0xb58
+  __AUTH_CONST.__const: 0x6598
+  __AUTH_CONST.__cfstring: 0x320
   __AUTH.__data: 0x18
   __DATA.__data: 0x68
-  __DATA.__bss: 0x5c0
-  __DATA.__common: 0x618
+  __DATA.__bss: 0x508
+  __DATA.__common: 0x6e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A575324C-1254-366A-A750-69F84F7DD4BA
-  Functions: 3598
-  Symbols:   554
-  CStrings:  5597
+  UUID: CF9870D5-AE55-330A-AB90-924A62DAD4A8
+  Functions: 3416
+  Symbols:   573
+  CStrings:  5641
 
Symbols:
+ _IORegistryEntryGetChildIterator
+ _IOServiceGetMatchingServices
+ _dyld_process_create_for_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_get_shared_cache
+ _dyld_shared_cache_for_file
+ _hwtrace_live_recording_system_options_set_chunk_size
+ _hwtrace_live_recording_system_options_set_trace_buffer_size
+ _hwtrace_recording_save_options_set_decode_compression
+ _hwtrace_recording_save_options_set_decode_in_memory
+ _hwtrace_section_load_address
+ _hwtrace_section_name
+ _hwtrace_segment_slide
+ _hwtrace_system_add_task
+ _hwtrace_system_stats
+ _hwtrace_task_add_image
+ _hwtrace_task_add_thread
+ _ktrace_chunk_copy_data
+ _memset_pattern16
+ _objc_release
- _sysctlnametomib
- _usleep
- _wmemchr
CStrings:
+ " (err="
+ " -> patched insn = "
+ " and in pid "
+ " chunks in wrap-no-copy mode but observe "
+ ") service does not support TraceKit"
+ ", key = "
+ ", pc = "
+ "Could not create child iterator for RTBuddy("
+ "Could not create matching dictionary for RTBuddy"
+ "Could not determine size of file at path: "
+ "Could not find IOService(s) matching RTBuddy"
+ "Could not open connection to RTBuddy"
+ "Could not open file at path: "
+ "DevelopmentTrace not supported for: "
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::deinitCarveout()"
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::deinitChunkQueue()"
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::initCarveout()"
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::initChunkNotification()"
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::initChunkQueue()"
+ "Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::initThrottleNotification()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::deinitCarveout()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::deinitChunkQueue()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::initCarveout()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::initChunkNotification()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::initChunkQueue()"
+ "Expected "
+ "Expected<std::string> getSharedCacheMainFile(task_read_t)"
+ "Expected<std::vector<uint64_t>> llvm::applehwtrace::getXnuRootStaticIfEntryOffsets()"
+ "FailedToDisasm"
+ "FailedToLoad"
+ "FallbackPID"
+ "IOConnectCallMethod Attach failed."
+ "IOConnectCallMethod Start failed."
+ "IOConnectCallMethod Stop failed."
+ "IOConnectCallMethod Unconfigure failed."
+ "InSection"
+ "Legacy xnu-based streaming-to-DRAM no longer supported (rdar://150685905 (APT: remove legacy multbuf code from xnu)), use --CPUTrace:driver=1"
+ "LiveRecording::configure"
+ "LiveRecording::configure(%{public}s)"
+ "MachOUtilities.cpp"
+ "Monitor: ReplaceExistingEvents = "
+ "No RTBuddy IOService matching role: "
+ "NotFinalized"
+ "NumExcessGaps"
+ "NumGaps"
+ "NumLostTraceBytes"
+ "NumStreamedTraceBytes"
+ "Pre-existing interval: "
+ "Prod trace is only supported through the Driver"
+ "ProductionTrace not supported for: "
+ "RTBuddy"
+ "RTBuddy("
+ "SIE{"
+ "StaticIfOffsets"
+ "Streaming to DRAM requires a driver"
+ "StreamingChunkSize"
+ "System does not support trace-to-VA, cannot changed wired trace allocation"
+ "This happened because an existing AppleProcessorTrace foreground session is active. Consider ending that session before starting a new one."
+ "This happened because the device is not provisioned to record a Processor Trace. Try navigating to Settings and enabling Processor Trace."
+ "Throttling requires streaming to be enabled"
+ "Unsupported"
+ "Unsupported CPUTRACE_METADATA_MAJOR_VERSION"
+ "VirtualTraceBufferSize"
+ "aop2/iop-aop2-nub"
+ "chunk{ chunk_index=%{public}u, chunk_id=%{public}llu, offset=%{public}llu, size=%{public}llu, checksum=%{public}llx, fill_size=%{public}llu, fill_wrap=%{public}u, fill_loss=%{public}u, cluster_id=%{public}u }"
+ "com.apple.RTBuddy.ChunkDispatchQueue"
+ "compressed-decoding-alg"
+ "cputrace-aslr-data-region"
+ "dyld_process_create_for_task"
+ "dyld_process_snapshot_create_for_process"
+ "error: failed to find section for "
+ "error: section lookup failed for "
+ "hwtrace_error ("
+ "kern.static_if_abi"
+ "kern.static_if_abi unsupported: "
+ "kern.static_if_modified_keys"
+ "kern.static_if_modified_keys retrieval failed"
+ "kern.static_if_modified_keys sizing failed"
+ "ktrace_chunk_copy_data failed with: "
+ "lib_topology.cpp"
+ "libhwtrace @ tag libhwtrace-133.0.2"
+ "libhwtrace @ tag libhwtrace-133.0.2\n"
+ "no shared cache found within snapshot"
+ "overlaps with newly inserted: "
+ "role"
+ "section lookup failed"
+ "segment lookup failed"
+ "setupHandlerOnTargetExit"
+ "sie.sie_base="
+ "sie.sie_link="
+ "sie.sie_target="
+ "static Expected<std::unique_ptr<RTBuddyDriverInterface>> llvm::applehwtrace::RTBuddyDriverInterface::get(StringRef)"
+ "static_if metadata not found"
+ "std::unique_ptr<uint8_t[]> llvm::applehwtrace::AppleHWAccess::readBuffer(uint64_t, uint64_t) const"
+ "stringForKey:"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::attach(UUIDHandle)"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::pause()"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::resume()"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::start()"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::stop()"
+ "virtual Error llvm::applehwtrace::AppleProcessorTraceDriverInterface::unconfigure()"
+ "virtual Error llvm::applehwtrace::RTBuddyDriverInterface::attach(UUIDHandle)"
+ "virtual Error llvm::applehwtrace::RTBuddyDriverInterface::start()"
+ "virtual Error llvm::applehwtrace::RTBuddyDriverInterface::stop()"
+ "virtual Error llvm::applehwtrace::RTBuddyDriverInterface::unconfigure()"
+ "virtual Expected<UUIDValue> llvm::applehwtrace::AppleProcessorTraceDriverInterface::configure(bool, const SystemOptions &, uint64_t, uint64_t)"
+ "virtual Expected<UUIDValue> llvm::applehwtrace::RTBuddyDriverInterface::configure(bool, const SystemOptions &, uint64_t, uint64_t)"
+ "warning: Disabling throttling in wrap-no-copy mode"
+ "{public}%s"
- " \t\n\v\f\r"
- " MB of physical carveout on this device"
- " is not mappable"
- " not aligned to ringbuffer size: "
- "%s"
- ") than is supported by this copy of libhwtrace (v"
- "). Please upgrade your OS or libhwtrace installation."
- ", nsects = "
- ", pure = "
- ", some = "
- ": read failed"
- "AppleProcessorTrace DevelopmentTrace not supported"
- "AppleProcessorTrace ProductionTrace not supported"
- "AppleProcessorTrace is only supported for XNU."
- "CarveoutSizeOverride"
- "Chunk size: "
- "Error llvm::applehwtrace::DriverInterface::attach(UUIDHandle)"
- "Error llvm::applehwtrace::DriverInterface::deinitCarveout()"
- "Error llvm::applehwtrace::DriverInterface::deinitChunkQueue()"
- "Error llvm::applehwtrace::DriverInterface::initCarveout()"
- "Error llvm::applehwtrace::DriverInterface::initChunkNotification()"
- "Error llvm::applehwtrace::DriverInterface::initChunkQueue()"
- "Error llvm::applehwtrace::DriverInterface::initThrottleNotification()"
- "Error llvm::applehwtrace::DriverInterface::pause()"
- "Error llvm::applehwtrace::DriverInterface::resume()"
- "Error llvm::applehwtrace::DriverInterface::start()"
- "Error llvm::applehwtrace::DriverInterface::stop()"
- "Error llvm::applehwtrace::DriverInterface::unconfigure()"
- "Expected<UUIDValue> llvm::applehwtrace::DriverInterface::configure(bool, const SystemOptions &, uint64_t, uint64_t)"
- "Failed to disassemble."
- "Failed to load section."
- "Failed to materialize"
- "HWTrace subchunk of size="
- "Images not finalized"
- "Infinite trace requires at least "
- "LiveRecording::start"
- "PROD_TRC_STRM_BASE0_GL2"
- "PROD_TRC_STRM_FILL0_EL1"
- "PROD_TRC_TLB_CFG_GL2"
- "PROD_TRC_TLB_MASK_GL2"
- "Prod filesystem streaming is only supported through the Driver"
- "Throttling requires a driver and streaming to be enabled"
- "Trace-to-VA : TLBI done.\n"
- "Trace-to-VA : doing TLBI.\n"
- "Trace-to-VA: "
- "Virtual ringbuffer size cannot be zero"
- "Your system does not support infinite trace, the hw.cputrace.multbuf_compat_version check failed."
- "Your system has a newer version of the infinite trace feature (v"
- "chunk{ chunk_index=%{public}u, chunk_id=%{public}llu, offset=%{public}llu, size=%{public}llu, checksum=%{public}llu, fill_size=%{public}llu, fill_wrap=%{public}u, fill_loss=%{public}u, cluster_id=%{public}u }"
- "could not request chunk: "
- "hw.cputrace.multbuf_chunk_request"
- "hw.cputrace.multbuf_chunk_size"
- "hw.cputrace.multbuf_chunk_size failed"
- "hw.cputrace.multbuf_compat_version"
- "hw.cputrace.multbuf_deinit"
- "hw.cputrace.multbuf_deinit failed: "
- "hw.cputrace.multbuf_init"
- "hw.cputrace.multbuf_init failed: "
- "hw.cputrace.multbuf_init_cluster_local_regs"
- "hw.cputrace.multbuf_init_cluster_local_regs failed"
- "hw.cputrace.multbuf_scratch_size"
- "hw.cputrace.multbuf_write_checkin"
- "libhwtrace @ tag libhwtrace-118"
- "libhwtrace @ tag libhwtrace-118\n"
- "mrs("
- "sysctlnametomib failed for multbuf_chunk_request: "
- "sysctlnametomib failed for multbuf_write_checkin: "

```
