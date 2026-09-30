## logd

> `/usr/libexec/logd`

```diff

-1815.80.2.0.0
-  __TEXT.__text: 0x26b14
+1861.100.16.0.0
+  __TEXT.__text: 0x270b4
   __TEXT.__auth_stubs: 0x19d0
   __TEXT.__delay_helper: 0x14c
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x477a
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0x49ed
   __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x6c0
-  __TEXT.__eh_frame: 0x50
+  __TEXT.__unwind_info: 0x6c8
   __DATA_CONST.__auth_got: 0xcf0
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2098
+  __DATA_CONST.__const: 0x2110
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10

   __DATA.__objc_const: 0x120
   __DATA.__objc_selrefs: 0x1f0
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x1d24
+  __DATA.__data: 0x1cf4
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xeaf8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DE1DCC4D-55E7-316E-9E86-6F41418F6DE9
-  Functions: 506
+  UUID: 1D209C40-8DE8-381E-9FE3-7FF712C0BF81
+  Functions: 508
   Symbols:   471
-  CStrings:  653
+  CStrings:  657
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
+ _os_variant_is_darwinos
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_storeStrong
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH8zugCz39Hwlo75Pm4jPykadxo3W-_cLfftE9s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Library/Caches/com.apple.xbs/985B05C5-5B1D-4136-A868-78BE8E4D2B74/TemporaryDirectory.psmime/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/logd.build/DerivedSources/OSLogDarwin_C.c"
+ "TB_FATAL: invalid result returned from setPreferences"
+ "TB_FATAL: invalid result returned from setPreferences (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[OSLogDarwin.PrefsValue]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[OSLogDarwin.PrefsValue]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: overflow detected when multiplying"
+ "TB_FATAL: overflow detected when multiplying (%s:%d)\n"
+ "logd_rt_client_q == NULL"
+ "v16@?0^{logd_book_s=^?*CQQqqAqiiQQBBi[4q]QQc}8"
+ "v16@?0^{logd_buffer_info_s=^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{os_procinfo_map_s}^{os_procinfo_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"
- "/Library/Caches/com.apple.xbs/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/logd.build/DerivedSources/OSLogDarwin_C.c"
- "BUG IN CLIENT OF LIBTRACE: Nope"
- "TB_FATAL: invalid tag in array metadata: 0x%x"
- "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
- "_client_queue == NULL"
- "v16@?0^{logd_book_s=^?*C@QQqqAqiiQQBi[4q]QQc}8"
- "v16@?0^{logd_buffer_info_s=^{dispatch_queue_s}^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{os_procinfo_map_s}^{os_procinfo_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"

```
