## logd

> `/usr/libexec/logd`

```diff

-1481.40.16.0.0
-  __TEXT.__text: 0x20f5c
+1510.100.35.0.1
+  __TEXT.__text: 0x2107c
   __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x3f4
-  __TEXT.__cstring: 0x3037
+  __TEXT.__const: 0x3fc
+  __TEXT.__cstring: 0x30a5
   __TEXT.__objc_methname: 0x3d7
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x10

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x180
-  __DATA.__objc_classrefs: 0x50
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1ca5
   __DATA.__crash_info: 0x40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B8FC84A-60E4-30CB-A532-A86420207FBA
-  Functions: 458
+  UUID: 2BB71620-9656-331E-BEF5-21395106043E
+  Functions: 459
   Symbols:   410
-  CStrings:  497
+  CStrings:  499
 
CStrings:
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]@^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BS{os_unfair_lock_s=I}CB[0c]}8"
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]^{firehose_client_s}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BS{os_unfair_lock_s=I}CB[0c]}8"
+ "Received a Periodic Request from CacheDelete on volume %s"
+ "Received a Purge Request from CacheDelete on volume %s with urgency: %d and goal: %lld"
+ "Received a Purgeable Request from CacheDelete on volume: %s"
+ "Super Quarantined %s, dropping clients logs."
+ "disableSuperQuarantine"
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]@^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]S{os_unfair_lock_s=I}CB[0c]}8"
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]^{firehose_client_s}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]S{os_unfair_lock_s=I}CB[0c]}8"
- "Received a Periodic Request from CacheDelete"
- "Received a Purge Request from CacheDelete with urgency: %d and goal: %lld"
- "Received a Purgeable Request from CacheDelete"

```
