## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-104.5.0.0.0
-  __TEXT.__cstring: 0x50af
-  __TEXT.__os_log: 0x3984
+124.1.0.0.0
+  __TEXT.__cstring: 0x5a91
+  __TEXT.__os_log: 0x4886
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x39088
+  __TEXT_EXEC.__text: 0x4180c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4b0
-  __DATA.__common: 0x780
+  __DATA.__data: 0x460
+  __DATA.__common: 0x820
   __DATA.__bss: 0x9
-  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__auth_got: 0x688
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0xf0
-  __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0x6230
-  __DATA_CONST.__kalloc_type: 0x1000
-  __DATA_CONST.__kalloc_var: 0xf00
-  __DATA_CONST.__assert: 0x78
-  UUID: E9349498-E22C-3603-9BA4-A97CEA8032A3
-  Functions: 1736
+  __DATA_CONST.__mod_init_func: 0xf8
+  __DATA_CONST.__mod_term_func: 0xf8
+  __DATA_CONST.__const: 0x6968
+  __DATA_CONST.__kalloc_type: 0x1100
+  __DATA_CONST.__kalloc_var: 0x1090
+  __DATA_CONST.__assert: 0xa0
+  UUID: 1081778F-9A65-31A6-845A-582BE344C588
+  Functions: 1877
   Symbols:   0
-  CStrings:  743
+  CStrings:  846
 
CStrings:
+ "\"%s: Failed to complete memory descriptor(%p) at index %u\" @%s:%d"
+ "\"Invalid Mapping Command\" @%s:%d"
+ "%s: ByteCount is not virtualPageSize(%u) aligned\n"
+ "%s: Copy Mappings Failed(0x%x)\n"
+ "%s: Failed to allocate IOGPUVirtualMemory object\n"
+ "%s: Failed to allocate array of descriptors\n"
+ "%s: Failed to allocate array of sub memory descriptors\n"
+ "%s: Failed to allocate descriptor bitmap\n"
+ "%s: Failed to allocate metadata memory descriptor\n"
+ "%s: Failed to allocate residency data kernel map\n"
+ "%s: Failed to allocate residency data memory descriptor\n"
+ "%s: Failed to allocate resource object\n"
+ "%s: Failed to allocate shared event fence\n"
+ "%s: Failed to allocate sub memory descriptors at index %u\n"
+ "%s: Failed to create memory descriptors\n"
+ "%s: Failed to find command queue\n"
+ "%s: Failed to find shared event reference\n"
+ "%s: Failed to mark virtual memory non-volatile err 0x%x\n"
+ "%s: Failed to prepare memory descriptor(%p) at index %u\n"
+ "%s: Failed to prepare metadata (%p)\n"
+ "%s: Failed to prepare residency data (%p)\n"
+ "%s: Failed to update memory at index %u\n"
+ "%s: IOMemoryDescriptor::getPageCounts returned 0x%08x for meta data\n"
+ "%s: IOMemoryDescriptor::getPageCounts returned 0x%08x for residency data\n"
+ "%s: Incompatible virtual page sizes source(%u), destination(%u)\n"
+ "%s: Invalid Arguments\n"
+ "%s: Invalid Index (%u), Capacity (%u)\n"
+ "%s: Invalid arguments\n"
+ "%s: Invalid newCommandQueueArgsSize (%u) expected (%u)\n"
+ "%s: Invalid virtualPageSize(%u)\n"
+ "%s: PID %d may be leaking IOGPUResource (count=%d)\n"
+ "%s: Post Mapping wait failed\n"
+ "%s: Protection violation\n"
+ "%s: Shared event wait timed out for value : %llx\n"
+ "%s: Unsupported purgeability option (%u)\n"
+ "%s: Update Mappings Failed(0x%x)\n"
+ "%s: destination resoource memory is not a virtual memory\n"
+ "%s: device handle is null and failed to add texture buffer size to device allocation size\n"
+ "%s: failed to create client map for meta data\n"
+ "%s: memory is not a virtual memory\n"
+ "%s: minVirtualPageSize is not a power of 2\n"
+ "%s: source resource memory is not a sys memory\n"
+ "%s: updateGPUPageTable failed\n"
+ "%s: virtual_page_size(%u) is not minimum VirtualPageSize(%u) aligned\n"
+ "%s:kIOGPUKernelCommandCopyMappings: Copy Mappings Failed\n"
+ "%s:kIOGPUKernelCommandCopyMappings: Failed to add mapping command to descriptor \n"
+ "%s:kIOGPUKernelCommandCopyMappings: Failed to allocated Async Mapping Descriptor \n"
+ "%s:kIOGPUKernelCommandCopyMappings: Insufficient bytes (%llu) for sIOGPUCopyMappings (%lu)\n"
+ "%s:kIOGPUKernelCommandCopyMappings: Insufficient bytes (%llu) or size overflow for sIOGPUUpdateMappings (%lu)\n"
+ "%s:kIOGPUKernelCommandCopyMappings: Invalid destination resourceID %08x\n"
+ "%s:kIOGPUKernelCommandCopyMappings: Invalid source resourceID %08x\n"
+ "%s:kIOGPUKernelCommandDebugSleep: Insufficient bytes (%llu) for sIOGPUKernelCommandDebugSleepArgs (%lu)\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Async Mapping Descriptor not allocated\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Async Mapping Disabled\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Failed to allocated Mapping fence\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Failed to schedule post mapping event\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Insufficient bytes (%llu) for sIOGPUKernelCommandSignalOrWaitEventArgs (%lu)\n"
+ "%s:kIOGPUKernelCommandPostMappingWaitEvent: Invalid signal event port name: %d obj: %p\n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Failed to add mapping command to descriptor \n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Failed to allocated Async Mapping Descriptor \n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Insufficient bytes (%llu) for sIOGPUUpdateMappings (%lu)\n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Insufficient bytes (%llu) or size overflow for sIOGPUUpdateMappings (%lu)\n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Invalid destinationResourceID %08x\n"
+ "%s:kIOGPUKernelCommandUpdateMappings: Update Mappings Failed\n"
+ "1211111121211222222222211112221112222211111211122222211112221222212222"
+ "12111111222122202222222221200000"
+ "121111122111212111111112221211121112"
+ "121121121"
+ "12112121121111222222222222222222221221112112"
+ "121222221211122"
+ "1212222212111221111122222211111222222"
+ "12122222121112221121211122"
+ "12122222121112222212111112"
+ "121222222222222222222211121"
+ "12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222111111122222222222222222121112222222211"
+ "2222222211211"
+ "Aliased Virtual Resource (Virtual Size = %llu bytes)"
+ "Can't upgrade IOGPUMemory.protectionOptions while still wired (0x%x->0x%x)\n"
+ "IOGPUCommandDescriptor.cpp"
+ "IOGPUMappingCommand"
+ "IOGPUMappingCommandDescriptor"
+ "IOGPUMappingFence"
+ "IOGPUVirtualMemory"
+ "IOGPUVirtualMemory.cpp"
+ "IOReturn IOGPUCommandQueue::schedule_shared_event(mach_port_name_t, uint64_t, bool, uint32_t)"
+ "IOReturn IOGPUDevice::set_resource_purgeable(const uint32_t, eIOGPUResourcePurgeable, eIOGPUResourcePurgeable *)"
+ "IOReturn IOGPUDeviceUserClient::t_signal_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "IOReturn IOGPUDeviceUserClient::t_signal_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "IOReturn IOGPUDeviceUserClient::t_wait_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "IOReturn IOGPUDeviceUserClient::t_wait_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "IOReturn IOGPUResource::copyMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)"
+ "IOReturn IOGPUResource::updateMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)"
+ "IOReturn IOGPUVirtualMemory::copyMemoryAtIndexAndLength(IOGPUVirtualMemory *, uint32_t, uint32_t, uint32_t)"
+ "Metal 4 Disable Async Mapping"
+ "Virtual"
+ "bits.h"
+ "bool IOGPUMemoryMap::update_pte(uint32_t, IOMemoryDescriptor *, IOMemoryDescriptor *)"
+ "iogpu_boost_cpu_priority"
+ "metal4_disable_async_mapping"
+ "nbits > 0"
+ "site.IOGPUMappingCommand"
+ "site.IOGPUMappingCommandDescriptor"
+ "site.IOGPUMappingFence"
+ "site.IOGPUVirtualMemory"
+ "static OSPtr<IOGPUResource> IOGPUResource::newVirtualResource(IOGPU *, IOGPUDevice *, IOGPUNewResourceArgs *)"
+ "static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t, task_t)"
+ "virtual IOMemoryDescriptor **IOGPUSysMemory::get_memory_descriptors(uint32_t, IOOptionBits, uint32_t *)"
+ "virtual IOReturn IOGPUCommandQueue::schedulePostMappingWaitEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)"
+ "virtual IOReturn IOGPUVirtualMemory::updateMemoryAtIndexLocked(uint32_t, IOMemoryDescriptor *)"
+ "virtual IOReturn IOGPUVirtualMemory::wire()"
+ "virtual bool IOGPUVirtualMemory::init(IOGPU *, uint64_t, uint32_t, bool, uint64_t, uint64_t, task_t)"
+ "virtual void IOGPUCommandQueue::signalSharedEvent(IOSurfaceSharedEvent *, uint64_t)"
+ "virtual void IOGPUCommandQueue::waitSharedEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)"
+ "virtual void IOGPUVirtualMemory::describeAllocation(OSDictionary *)"
+ "virtual void IOGPUVirtualMemory::unwire()"
+ "void IOGPUMappingCommand::execute()"
+ "wq_timeout_sec"
- "%s: PID %d likely leaking IOGPUResource (count=%d)\n"
- "%s:kIOGPUKernelCommandCollectTimeStamp: Insufficient bytes (%llu) for sIOGPUKernelCommandDebugSleepArgs (%lu)\n"
- "121111112121122222222221111222111222221111121112222221111222122222222"
- "12111111222122202222222212000000"
- "12111112211121211111111222121112"
- "12122222121112"
- "121222221211121111122222211111222222"
- "121222221211122112122"
- "12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221111111222222222222222221211122222221"
- "222222221111"
- "Resource Limit Count"
- "rsrc_limit"
- "static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t)"
- "trying to get apparently bogus resource handle %d\n"

```
