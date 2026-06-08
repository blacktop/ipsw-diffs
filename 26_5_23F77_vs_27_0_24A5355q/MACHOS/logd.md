## logd

> `/usr/libexec/logd`

```diff

-1861.120.4.0.0
-  __TEXT.__text: 0x270a4
-  __TEXT.__auth_stubs: 0x19c0
-  __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_stubs: 0x760
+1952.0.0.0.0
+  __TEXT.__text: 0x26fc4
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x488b
-  __TEXT.__objc_methname: 0x4ee
-  __TEXT.__objc_classname: 0x2c
+  __TEXT.__cstring: 0x47e1
+  __TEXT.__objc_methname: 0x3e2
+  __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__auth_got: 0xce8
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2110
-  __DATA_CONST.__cfstring: 0x5a0
+  __TEXT.__unwind_info: 0x688
+  __DATA_CONST.__const: 0x2398
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0xdb8
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x1f0
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x1cf4
+  __DATA.__data: 0x1cf5
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xeaf8
-  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
+  __DATA.__bss: 0xeb68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DFC231EE-5761-3327-91F8-14D1D00C6D3F
-  Functions: 508
-  Symbols:   470
-  CStrings:  656
+  UUID: B906B878-B926-35F1-8A14-106F9A2A071E
+  Functions: 515
+  Symbols:   493
+  CStrings:  654
 
Symbols:
+ __os_feature_enabled_impl
+ __os_trace_strdup
+ _kpersona_info
+ _kpersona_pidinfo
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_storeStrong
+ _os_map_128_clear
+ _os_map_128_count
+ _os_map_128_destroy
+ _os_map_128_find
+ _os_map_128_foreach
+ _os_map_128_init
+ _os_map_128_insert
+ _os_map_32_clear
+ _os_map_32_count
+ _os_map_32_destroy
+ _os_map_32_find
+ _os_map_32_foreach
+ _os_map_32_init
+ _os_map_32_insert
+ _os_map_str_delete
+ _os_map_str_destroy
+ _os_map_str_entry
+ _os_map_str_foreach
+ _os_set_128_ptr_clear
+ _os_set_128_ptr_delete
+ _os_set_128_ptr_destroy
+ _os_set_128_ptr_find
+ _os_set_128_ptr_foreach
+ _os_set_128_ptr_init
+ _os_set_128_ptr_insert
+ _xpc_array_append_value
+ _xpc_array_create
- _OBJC_CLASS_$_RadarComponent
- _OBJC_CLASS_$_RadarDraft
- _OBJC_CLASS_$_TapToRadarService
- __ZNSt3__112__next_primeEm
- __ZdlPv
- __ZdlPvSt19__type_descriptor_t
- __ZnwmSt19__type_descriptor_t
- _abort
- _dlopen
- _objc_opt_class
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]I{?=(?=@@)b1}^{tracev3_buffer_uuidinfo_s}^{_os_opaque_128_ptr_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]I{?=(?=^{logd_realtime_client_s}^{firehose_client_s})b1}^{tracev3_buffer_uuidinfo_s}^{_os_opaque_128_ptr_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
+ "B16@?0^{os_set_128_key_s=[2Q]}8"
+ "B20@?0I8^v12"
+ "B32@?0{os_map_128_key_s=[2Q]}8^v24"
+ "CompressionAlgorithmMemory"
+ "CompressionAlgorithmPersist"
+ "Failed to get persona for %d, %d %s, falling back to metadata page %d"
+ "Libtrace"
+ "No kernel firehose context to get UUID information from."
+ "No kernel firehose context to get subsystems from."
+ "Quarantine"
+ "RealtimeClientHarvestIntervalNS"
+ "com.apple.private.logging.kernel-info"
+ "identifier"
+ "kernel_kext_uuids"
+ "kernel_main_uuid"
+ "kernel_shared_cache_uuid"
+ "kernel_subsystems"
+ "kext_load_addr"
+ "kext_load_size"
+ "kext_uuid"
+ "lz4"
+ "lzbitmap"
+ "lzbitmap0"
+ "lzbitmap0_fast"
+ "lzbitmap1"
+ "lzbitmap1_fast"
+ "lzbitmap2"
+ "lzbitmap2_fast"
+ "lzfse"
+ "personas_in_oslog"
+ "v16@?0^{logd_buffer_info_s=^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{_os_opaque_128_map_s}^{_os_opaque_128_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"
- "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
- "A secure indicator violation has been detected by the system. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call..."
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]{?=(?=@@)b1}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]{?=(?=^{logd_realtime_client_s}^{firehose_client_s})b1}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
- "Exclaves"
- "Fallback Indicator triggered"
- "Fallback Indicator was triggered due to an unexpected policy violation. Please describe what you were doing at the time. List any behaviors that may have used the camera or the microphone; taking a photo, invoking Siri, taking a phone call, turning on/off display, phone in pocket, etc ..."
- "Quaratine"
- "Secure Indicator Violation Detected"
- "Security Policy"
- "Unable to Create TTR draft: %s (%ld)"
- "a fallback indicator was triggered"
- "a secure indicator violation has been detected"
- "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
- "initWithName:version:identifier:"
- "localizedDescription"
- "setAttachments:"
- "setClassification:"
- "setComponent:"
- "setDeleteOnAttach:"
- "setDeviceIDs:"
- "setDiagnosticExtensionIDs:"
- "setProblemDescription:"
- "setTitle:"
- "shared"
- "v16@?0@\"NSError\"8"
- "v16@?0^{logd_buffer_info_s=^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{os_procinfo_map_s}^{os_procinfo_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"

```
