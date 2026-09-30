## IDEDebugGaugeDataProviders

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/IDEDebugGaugeDataProviders.bundle/IDEDebugGaugeDataProviders`

```diff

-64573.4.1.0.0
-  __TEXT.__text: 0x72b0
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x554
+64575.69.1.0.0
+  __TEXT.__text: 0x99dc
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x6d4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x908
-  __TEXT.__objc_classname: 0x1b6
-  __TEXT.__objc_methname: 0x628
-  __TEXT.__objc_methtype: 0xcab
-  __TEXT.__gcc_except_tab: 0xd34
-  __TEXT.__unwind_info: 0x310
-  __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0xf80
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__cstring: 0xa80
+  __TEXT.__objc_methname: 0x660
+  __TEXT.__oslogstring: 0x77
+  __TEXT.__objc_classname: 0x226
+  __TEXT.__objc_methtype: 0xc7e
+  __TEXT.__gcc_except_tab: 0xd58
+  __TEXT.__unwind_info: 0x3a8
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__cfstring: 0x1140
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x120
-  __DATA.__objc_const: 0xa80
-  __DATA.__objc_selrefs: 0x248
-  __DATA.__objc_ivar: 0x40
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0xd70
+  __DATA.__objc_selrefs: 0x268
+  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x120
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 175ADF55-8493-30DA-8B45-714C08058185
-  Functions: 117
-  Symbols:   157
-  CStrings:  386
+  UUID: B15C85D5-760B-3003-BFCC-0F5A14DFB150
+  Functions: 165
+  Symbols:   183
+  CStrings:  431
 
Symbols:
+ _IDEDataProviderMemoryHostTotalKey
+ _IDEDataProviderMemoryHostUsedKey
+ _IDEDataProviderMemoryTaskLimitsKey
+ _IDEDataProviderMemoryTaskPhysicalFootprintKey
+ _OBJC_CLASS_$_IDEDataProvider_CPU
+ _OBJC_CLASS_$_IDEDataProvider_Memory
+ _OBJC_CLASS_$_IDEGaugeDataProviderService_CPU
+ _OBJC_CLASS_$_IDEGaugeDataProviderService_Memory
+ _OBJC_METACLASS_$_IDEDataProvider_CPU
+ _OBJC_METACLASS_$_IDEDataProvider_Memory
+ _OBJC_METACLASS_$_IDEGaugeDataProviderService_CPU
+ _OBJC_METACLASS_$_IDEGaugeDataProviderService_Memory
+ __os_log_default
+ __os_log_impl
+ _bzero
+ _host_processor_info
+ _host_statistics64
+ _mach_error_string
+ _mach_host_self
+ _mach_port_deallocate
+ _mach_task_self_
+ _mach_timebase_info
+ _mach_vm_deallocate
+ _memorystatus_control
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x24
+ _os_log_type_enabled
+ _sysctlbyname
+ _task_info
+ _task_name_for_pid
+ _vm_kernel_page_size
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "IDEDataProvider_CPU"
+ "IDEDataProvider_Memory"
+ "IDEGaugeDataProviderService_CPU"
+ "IDEGaugeDataProviderService_Memory"
+ "_lock"
+ "_taskNameForPid"
+ "allKeys"
+ "com.apple.xcode.debug-gauge-data-providers.CPU"
+ "com.apple.xcode.debug-gauge-data-providers.Memory"
+ "cpu.host.count"
+ "cpu.host.idle"
+ "cpu.host.nice"
+ "cpu.host.system"
+ "cpu.host.time"
+ "cpu.host.user"
+ "cpu.task.system"
+ "cpu.task.user"
+ "host_processor_info[PROCESSOR_CPU_LOAD_INFO]: %s"
+ "hw.memsize"
+ "mach_vm_deallocate[cpuload]: %s"
+ "memory.host.total"
+ "memory.host.used"
+ "memory.task.limits"
+ "memory.task.physical_footprint"
+ "minusSet:"
+ "mutableCopy"
+ "now"
+ "task_info[TASK_ABSOLUTETIME_INFO]: %s"
+ "{unordered_map<__NStatSource *, (anonymous namespace)::SourceInfo, std::hash<__NStatSource *>, std::equal_to<__NStatSource *>, std::allocator<std::pair<__NStatSource *const, (anonymous namespace)::SourceInfo>>>=\"__table_\"{__hash_table<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, std::__unordered_map_hasher<__NStatSource *, std::pair<__NStatSource *const, (anonymous namespace)::SourceInfo>, std::hash<__NStatSource *>, std::equal_to<__NStatSource *>>, std::__unordered_map_equal<__NStatSource *, std::pair<__NStatSource *const, (anonymous namespace)::SourceInfo>, std::equal_to<__NStatSource *>, std::hash<__NStatSource *>>, std::allocator<std::pair<__NStatSource *const, (anonymous namespace)::SourceInfo>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<int, (anonymous namespace)::ProcessInfo, std::hash<int>, std::equal_to<int>, std::allocator<std::pair<const int, (anonymous namespace)::ProcessInfo>>>=\"__table_\"{__hash_table<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, std::__unordered_map_hasher<int, std::pair<const int, (anonymous namespace)::ProcessInfo>, std::hash<int>, std::equal_to<int>>, std::__unordered_map_equal<int, std::pair<const int, (anonymous namespace)::ProcessInfo>, std::equal_to<int>, std::hash<int>>, std::allocator<std::pair<const int, (anonymous namespace)::ProcessInfo>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<__NStatSource *, (anonymous namespace)::SourceInfo, std::hash<__NStatSource *>, std::equal_to<__NStatSource *>, std::allocator<std::pair<__NStatSource *const, (anonymous namespace)::SourceInfo>>>=\"__table_\"{__hash_table<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, std::__unordered_map_hasher<__NStatSource *, std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, std::hash<__NStatSource *>, std::equal_to<__NStatSource *>>, std::__unordered_map_equal<__NStatSource *, std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, std::equal_to<__NStatSource *>, std::hash<__NStatSource *>>, std::allocator<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<__NStatSource *, (anonymous namespace)::SourceInfo>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<int, (anonymous namespace)::ProcessInfo, std::hash<int>, std::equal_to<int>, std::allocator<std::pair<const int, (anonymous namespace)::ProcessInfo>>>=\"__table_\"{__hash_table<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, std::__unordered_map_hasher<int, std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, std::hash<int>, std::equal_to<int>>, std::__unordered_map_equal<int, std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, std::equal_to<int>, std::hash<int>>, std::allocator<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<int, (anonymous namespace)::ProcessInfo>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
