## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_sharedcache`

```diff

-  __TEXT.__text: 0x5e8978
+  __TEXT.__text: 0x5e7b24
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0x4ffc1
-  __TEXT.__const: 0x121014
-  __TEXT.__swift5_typeref: 0x13de2
-  __TEXT.__swift5_reflstr: 0x11df8
-  __TEXT.__swift5_assocty: 0x7a08
-  __TEXT.__swift5_fieldmd: 0x1b914
-  __TEXT.__constg_swiftt: 0x27094
-  __TEXT.__swift5_protos: 0x96c
-  __TEXT.__swift5_proto: 0x3ca0
-  __TEXT.__swift5_types: 0x239c
-  __TEXT.__swift5_types2: 0x58
+  __TEXT.__cstring: 0x4f291
+  __TEXT.__const: 0x122134
+  __TEXT.__swift5_typeref: 0x14022
+  __TEXT.__swift5_reflstr: 0x11ef8
+  __TEXT.__swift5_assocty: 0x7a20
+  __TEXT.__swift5_fieldmd: 0x1bfc8
+  __TEXT.__constg_swiftt: 0x27e48
+  __TEXT.__swift5_protos: 0x970
+  __TEXT.__swift5_proto: 0x3cb4
+  __TEXT.__swift5_types: 0x2474
+  __TEXT.__swift5_types2: 0x60
   __TEXT.__swift5_builtin: 0x1590
-  __TEXT.__swift5_capture: 0xfe8
+  __TEXT.__swift5_capture: 0x1018
   __TEXT.__objc_methtype: 0xe1
   __TEXT.__swift5_mpenum: 0x3cc
-  __TEXT.__swift_as_entry: 0x988
-  __TEXT.__swift_as_ret: 0xafc
-  __TEXT.__swift_as_cont: 0x11b0
+  __TEXT.__swift_as_entry: 0x994
+  __TEXT.__swift_as_ret: 0xb08
+  __TEXT.__swift_as_cont: 0x11f8
   __TEXT.__oslogstring: 0xb5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0xb0
-  __TEXT.__eh_frame: 0x34e68
+  __TEXT.__chain_fixups: 0xb8
+  __TEXT.__eh_frame: 0x34f10
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3e5f8
-  __DATA.__data: 0x171e0
+  __DATA.__const: 0x3d578
+  __DATA.__data: 0x186b0
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x19af0
-  __DATA.__auth_ptr: 0x2318
+  __DATA.__ENDPOINTS: 0x1a221
+  __DATA.__auth_ptr: 0x2338
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__MMIOREGS: 0x795
   __DATA.__DARTS: 0x93f
-  __DATA.__got: 0x18
+  __DATA.__got: 0x10
   __DATA.__thread_vars: 0x90
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0xe360
+  __DATA.__bss: 0xe3e0
   __DATA.__common: 0x71a
-  __PDATA.__auth_ptr: 0x268
-  __PDATA.__const: 0x6698
+  __PDATA.__auth_ptr: 0x280
+  __PDATA.__const: 0x67b0
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xc8e8
+  __PDATA.__bss: 0xc4a8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 22975
+  Functions: 22927
   Symbols:   1
-  CStrings:  7332
+  CStrings:  7291
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA.__TIGHTBEAM_VT : content changed
~ __DATA.__TIGHTBEAM : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__thread_vars : content changed
~ __DATA.__common : content changed
~ __PDATA.__mod_init_func : content changed
~ __PDATA.__data : content changed
~ __PDATA.__shared_cache : content changed
~ __PDATA.__common : content changed
CStrings:
+ " nodes; falling back to first node"
+ "Deferred send unsupported"
+ "Invalid configuration"
+ "Message encode failed"
+ "No notification pending"
+ "Notification check-in failed"
+ "Notification receive failed"
+ "Validation failed"
+ "] Created Contrast Checker with configuration: "
+ "] No matching contrast-indicator node found among "
+ "contrast-indicator-"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2730)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2905)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:969)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:995)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1035)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:990)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1034)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:971)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
+ "no fixup data for faultable range [%#lx, %#lx) found"
+ "rawServiceConnection: message is not backed by a service connection"
+ "write_float_string"
- "ALSManager is already configured!"
- "invalid handler object, does not conform to AneUpcallsMethods"
- "invalid handler object, does not conform to AoeUpcallsMethods"
- "invalid handler object, does not conform to BackingMethods"
- "invalid handler object, does not conform to ConclaveUpcallsMethods"
- "invalid handler object, does not conform to CoreAudioOrchestrationUpcallsMethods"
- "invalid handler object, does not conform to DaemonNotificationServerMethods"
- "invalid handler object, does not conform to DartMethods"
- "invalid handler object, does not conform to DeviceServerMethods"
- "invalid handler object, does not conform to DriverUpcallsMethods"
- "invalid handler object, does not conform to DumpMethods"
- "invalid handler object, does not conform to EXBrightComponentMethods"
- "invalid handler object, does not conform to EXDARTDriverMethods"
- "invalid handler object, does not conform to EntropyBrokerComponentMethods"
- "invalid handler object, does not conform to ExclaveAudioArbiterControllerMethods"
- "invalid handler object, does not conform to ExclaveCoprocessorEndpointComponentMethods"
- "invalid handler object, does not conform to ExclaveCoprocessorGatewayComponentMethods"
- "invalid handler object, does not conform to ExclaveCredentialManagerComponentMethods"
- "invalid handler object, does not conform to ExclaveDARTMemoryMapperComponentMethods"
- "invalid handler object, does not conform to ExclaveIndicatorControllerMethods"
- "invalid handler object, does not conform to ExclaveSEPManagerMethods"
- "invalid handler object, does not conform to ExfiltrationUpcallsMethods"
- "invalid handler object, does not conform to IDumpMethods"
- "invalid handler object, does not conform to IReadAccessMethods"
- "invalid handler object, does not conform to IWriteAccessMethods"
- "invalid handler object, does not conform to LegacyUpcallsMethods"
- "invalid handler object, does not conform to LogServerMethods"
- "invalid handler object, does not conform to LpwUpcallsMethods"
- "invalid handler object, does not conform to MemoryUpcallsMethods"
- "invalid handler object, does not conform to NotificationUpcallsMethods"
- "invalid handler object, does not conform to ReadAccessMethods"
- "invalid handler object, does not conform to RedactedLogServerMethods"
- "invalid handler object, does not conform to Span0Methods"
- "invalid handler object, does not conform to Span1Methods"
- "invalid handler object, does not conform to Span2Methods"
- "invalid handler object, does not conform to Span3Methods"
- "invalid handler object, does not conform to Span4Methods"
- "invalid handler object, does not conform to Span5Methods"
- "invalid handler object, does not conform to Span6Methods"
- "invalid handler object, does not conform to Span7Methods"
- "invalid handler object, does not conform to StackshotServerFilterMethods"
- "invalid handler object, does not conform to StackshotServerRedactedComponentMethods"
- "invalid handler object, does not conform to StatsServerComponentMethods"
- "invalid handler object, does not conform to StorageUpcallsMethods"
- "invalid handler object, does not conform to TestUpcallsMethods"
- "invalid handler object, does not conform to WriteAccessMethods"
- "invalid handler object, does not conform to XBackingMethods"
- "invalid handler object, does not conform to XDumpMethods"
- "invalid handler object, does not conform to XReadAccessMethods"
- "invalid handler object, does not conform to XWriteAccessMethods"
- "invalid handler object, does not conform to XnuAccessMethods"
- "invalid handler object, does not conform to XnuContentUpcallsMethods"
- "invalid handler object, does not conform to XnuProxyNotificationServerMethods"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8856)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8284)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2723)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2897)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7826)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:963)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:989)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1029)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6822)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:984)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1028)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:965)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5328)"
- "serviceConnection: message is not backed by a service connection"
- "write_float"

```
