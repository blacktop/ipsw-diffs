## logd

> `/usr/libexec/logd`

```diff

-1815.40.20.0.0
-  __TEXT.__text: 0x268dc
+1815.60.3.0.0
+  __TEXT.__text: 0x269a0
   __TEXT.__auth_stubs: 0x19d0
   __TEXT.__delay_helper: 0x110
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4667
+  __TEXT.__cstring: 0x4681
   __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 91DFE915-7056-3DD0-9F7D-3386397FA84A
+  UUID: 5A110225-1745-35B6-BCA6-3555ABF092B0
   Functions: 506
   Symbols:   471
-  CStrings:  646
+  CStrings:  647
 
Functions:
~ sub_100005dc4 : 288 -> 280
~ sub_100006e44 -> sub_100006e3c : 272 -> 284
~ sub_100011e10 -> sub_100011e14 : 1076 -> 1120
~ sub_1000242ec -> sub_10002431c : 1660 -> 1792
~ sub_100024a28 -> sub_100024adc : 764 -> 780
CStrings:
+ "B16@?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8"
+ "[%03u]\n\t%10s : %llu@%u\n\t%10s : %d\n\t%10s : %u\n\t%10s : %u\n\t%10s : %u\n\t%10s : %x\n"
+ "persona_id"
+ "v16@?0^{logd_buffer_info_s=^{dispatch_queue_s}^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSSSS[1S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{os_procinfo_map_s}^{os_procinfo_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"
- "B16@?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8"
- "[%03u]\n\t%10s : %llu@%u\n\t%10s : %d\n\t%10s : %u\n\t%10s : %u\n\t%10s : %x\n"
- "v16@?0^{logd_buffer_info_s=^{dispatch_queue_s}^{logd_book_s}QQ{timespec=qq}{logd_chunk_buffer_s=[4{logd_data_buffer_s={tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}^{os_procinfo_map_s}^{os_procinfo_map_s}*III}]{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{logd_unified_buffer_s=^{logd_iov_buffer_s}{logd_buffer_state_s=(logd_buffer_lock_u=Q{?=II})QQii}}{rb_tree=[8^v]}CI}8"

```
