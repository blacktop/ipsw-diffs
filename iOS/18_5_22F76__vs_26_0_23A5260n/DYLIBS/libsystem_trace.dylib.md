## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0x1669c
-  __TEXT.__auth_stubs: 0x1030
+1815.0.0.0.0
+  __TEXT.__text: 0x1aa14
+  __TEXT.__auth_stubs: 0x1140
   __TEXT.__delay_stubs: 0x108
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0x175
-  __TEXT.__cstring: 0x1452
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__objc_methlist: 0xf4
+  __TEXT.__const: 0x2a5
+  __TEXT.__cstring: 0x1b9b
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x137
-  __TEXT.__unwind_info: 0x430
-  __TEXT.__objc_classname: 0x24
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__objc_classname: 0x70
   __TEXT.__objc_methname: 0x38d
   __TEXT.__objc_methtype: 0xc5
   __TEXT.__objc_stubs: 0x500
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x858
-  __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__objc_const: 0x388
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__const: 0x358
+  __AUTH_CONST.__objc_const: 0x5c8
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x80
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x98
+  __DATA.__data: 0xe4
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x150
+  __DATA_DIRTY.__data: 0x360
   __DATA_DIRTY.__bss: 0x2d0
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_darwin.dylib
+  - /usr/lib/system/libsystem_featureflags.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_m.dylib
   - /usr/lib/system/libsystem_malloc.dylib

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: A800C18D-6DE4-3E08-9AE2-280796D10789
-  Functions: 304
-  Symbols:   955
-  CStrings:  406
+  UUID: BD83AED3-5715-3656-A076-C6B27928263C
+  Functions: 368
+  Symbols:   1086
+  CStrings:  485
 
Symbols:
+ -[OS__os_metric dealloc]
+ -[OS_os_metric_dimensions dealloc]
+ -[OS_os_metric_group dealloc]
+ -[OS_os_metric_label dealloc]
+ GCC_except_table12
+ GCC_except_table15
+ _OBJC_CLASS_$_OS__os_metric
+ _OBJC_CLASS_$_OS_os_metric_dimensions
+ _OBJC_CLASS_$_OS_os_metric_group
+ _OBJC_CLASS_$_OS_os_metric_label
+ _OBJC_METACLASS_$_OS__os_metric
+ _OBJC_METACLASS_$_OS_os_metric_dimensions
+ _OBJC_METACLASS_$_OS_os_metric_group
+ _OBJC_METACLASS_$_OS_os_metric_label
+ _RTBinIndexForType
+ _RTLogBufferAddResource
+ _RTLogBufferAllocateResource
+ _RTLogBufferCheckStatus
+ _RTLogBufferGetHeader
+ _RTLogBufferGetResource
+ _RTLogBufferGetResourceSize
+ _RTLogBufferInitialize
+ _RTLogBufferIterate
+ _RTLogBufferRequiredStorageSize
+ _RTLogConnect
+ _RTLogConnectMemoryConfigFromString
+ _RTLogConnectRingBuffer
+ _RTLogDisconnect
+ _RTLogRingBufferCreateManaged
+ _RTLogRingBufferDataSize
+ _RTLogRingBufferGetSegmentCount
+ _RTLogRingBufferGetSegmentSize
+ _RTLogRingBufferInit
+ _RTLogRingBufferIterate
+ _RTLogRingBufferIterateFrom
+ _RTLogRingBufferJoinManaged
+ _RTLogRingBufferReadAt
+ _RTLogRingBufferWriteBuffer
+ _RTLogRingBufferWriteMessage
+ _RTLogRingBufferWriteWithCallback
+ __OBJC_$_INSTANCE_METHODS_OS__os_metric
+ __OBJC_$_INSTANCE_METHODS_OS_os_metric_dimensions
+ __OBJC_$_INSTANCE_METHODS_OS_os_metric_group
+ __OBJC_$_INSTANCE_METHODS_OS_os_metric_label
+ __OBJC_CLASS_RO_$_OS__os_metric
+ __OBJC_CLASS_RO_$_OS_os_metric_dimensions
+ __OBJC_CLASS_RO_$_OS_os_metric_group
+ __OBJC_CLASS_RO_$_OS_os_metric_label
+ __OBJC_METACLASS_RO_$_OS__os_metric
+ __OBJC_METACLASS_RO_$_OS_os_metric_dimensions
+ __OBJC_METACLASS_RO_$_OS_os_metric_group
+ __OBJC_METACLASS_RO_$_OS_os_metric_label
+ ___GLOBAL_init_65535
+ ___assert_rtn
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.291
+ ___block_descriptor_tmp.3.487
+ ___block_descriptor_tmp.301
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.35.303
+ ___block_descriptor_tmp.474
+ ___block_descriptor_tmp.508
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.83
+ ___block_literal_global.100
+ ___block_literal_global.164
+ ___block_literal_global.289
+ ___block_literal_global.366
+ ___block_literal_global.436
+ ___block_literal_global.486
+ ___block_literal_global.503
+ ___block_literal_global.85
+ ___cxa_atexit
+ ___xpcConnectionStart_block_invoke
+ ___xpc_connection_set_logging
+ __os_activity_stream_entry_encode_v2
+ __os_log_shim_with_CFString_impl
+ __os_metric_create_impl
+ __os_metric_double_create_impl
+ __os_metric_double_op_impl
+ __os_metric_emit_value
+ __os_metric_int64_create_impl
+ __os_metric_int64_op_impl
+ __os_metric_label_create_impl
+ __os_metric_label_create_internal
+ __os_metric_label_create_v
+ __os_metric_label_flatten
+ __os_metric_reset_data
+ __os_metric_reset_impl
+ __os_metric_set_scale_impl
+ __os_metric_set_unit_impl
+ __os_metric_uint64_create_impl
+ __os_metric_uint64_op_impl
+ __os_object_alloc
+ __os_trace_calloc_typed
+ __os_trace_malloc_typed
+ __os_trace_realloc_typed
+ __os_trace_zalloc_typed
+ _abort
+ _detail_double_default
+ _detail_int64_default
+ _detail_uint64_default
+ _flatWriteCallback
+ _log2
+ _logDestructor
+ _log_bin_config
+ _mach_make_memory_entry_64
+ _messageWriteCallback
+ _metric_defaults
+ _metric_lock
+ _objc_msgSendSuper2
+ _objc_release_x24
+ _objc_retain_x24
+ _os_log_shim_to_stdout
+ _os_log_shim_with_CFString_4NSLog
+ _os_log_with_args_4syslog
+ _os_metric_dimensions_add
+ _os_metric_dimensions_create
+ _os_metric_group_create
+ _puts
+ _rand
+ _rt_globals
+ _strtol
+ _transport_add_public_tracepoint
+ _transport_add_tracepoint
+ _transport_ringbuffer_add_tracepoint
+ _voucher_activity_get_logging_preferences_with_port
+ _writeData
+ _writeSegmentsToBuffer
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_send_message
+ _xpc_connection_set_event_handler
+ _xpc_dictionary_set_mach_send
- GCC_except_table10
- GCC_except_table13
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.211
- ___block_descriptor_tmp.221
- ___block_descriptor_tmp.3.393
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.380
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.72.280
- ___block_descriptor_tmp.77
- ___block_literal_global.108
- ___block_literal_global.209
- ___block_literal_global.286
- ___block_literal_global.33
- ___block_literal_global.349
- ___block_literal_global.392
- ___block_literal_global.79
- ___sprintf_chk
- __os_trace_calloc
- __os_trace_malloc
- __os_trace_realloc
- __os_trace_zalloc
- _objc_release_x22
- _objc_retain_x23
CStrings:
+ "(len + 1) == RTLOG_BUFFER_HEADER_MARKER_LENGTH"
+ "(uint64_t)ptr % RTLOG_BUFFER_ALIGN == 0"
+ "0"
+ "0 == RTLogRingBufferCreateManaged( &rt_globals.eventBin[i], placement_in_logbuffer, log_bin_config[i].segment_count, log_bin_config[i].segment_size)"
+ "BUG IN CLIENT OF LIBTRACE: label cannot be NULL"
+ "BUG IN LIBTRACE: Nope. Invalid stream object version"
+ "Cannot shim OS_LOG_DEFAULT to stdout"
+ "Cannot shim OS_LOG_DISABLED to stdout"
+ "OSLogClientType"
+ "OSLogRTBufferConfig"
+ "OSLogRateLimit"
+ "OS__os_metric"
+ "OS_os_metric_dimensions"
+ "OS_os_metric_group"
+ "OS_os_metric_label"
+ "RTLogBufferAddResource"
+ "RTLogBufferAllocateResource"
+ "RTLogBufferCheckStatus"
+ "RTLogBufferGetHeader"
+ "RTLogBufferGetResource"
+ "RTLogBufferGetResourceSize"
+ "RTLogBufferInitialize"
+ "RTLogBufferIterate"
+ "RTLogConnectRingBuffer"
+ "RTLogRingBufferCreateManaged"
+ "RTLogRingBufferGetSegmentCount"
+ "RTLogRingBufferGetSegmentSize"
+ "RTLogRingBufferInit"
+ "RTLogRingBufferIterate"
+ "RTLogRingBufferIterateFrom"
+ "RTLogRingBufferJoinManaged"
+ "RTLogRingBufferReadAt"
+ "RTLogRingBufferWriteBuffer"
+ "RTLogRingBufferWriteWithCallback"
+ "RTSharedMemoryConfigure"
+ "[==========LOGBUFFER==========]"
+ "_os_metric_double_op_impl"
+ "_os_metric_get_bins"
+ "_os_metric_int64_op_impl"
+ "_os_metric_uint64_op_impl"
+ "buffer && base"
+ "callback"
+ "com.apple.logd.realtime"
+ "config"
+ "configureEventBins"
+ "connection.c"
+ "dest"
+ "entryData"
+ "header->catalog.count < RTLOG_RESOURCE_COUNT"
+ "i28@?0[16c]8I16I20I24"
+ "kr == KERN_SUCCESS"
+ "large"
+ "medium"
+ "metric->metadata.bins > 0"
+ "metric.c"
+ "metric_internal.h"
+ "offset + aligned_size <= header->RTLogBufferSize"
+ "oslogbuffer.c"
+ "out_ring_buffer && size_buffer && msg_part_buffer && data_buffer"
+ "placement_in_logbuffer"
+ "ring"
+ "ring && buffer"
+ "ring && buffer && callback"
+ "ring && callback"
+ "ring && data"
+ "ring && offset && buffer && callback"
+ "ring && size && data"
+ "ringbuffer.c"
+ "rt_message_type"
+ "rt_shmem_descriptor"
+ "rt_shmem_size"
+ "seg_count > 0"
+ "shared_memory.c"
+ "size >= LOGUTIL_ROUNDUP(sizeof(RTLogBufferHeader), RTLOG_BUFFER_ALIGN)"
+ "small"
+ "transport_ringbuffer.c"
+ "v16@?0^v8"
+ "version"
+ "writeIovMessageParts"
+ "writeIovOnePart"
- "i24@?0[16c]8I16I20"

```
