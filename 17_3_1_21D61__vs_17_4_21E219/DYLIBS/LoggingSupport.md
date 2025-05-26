## LoggingSupport

> `/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport`

```diff

-1481.40.16.0.0
-  __TEXT.__text: 0x4e1c0
-  __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_methlist: 0x2b44
-  __TEXT.__const: 0x537
-  __TEXT.__gcc_except_tab: 0x82c
-  __TEXT.__cstring: 0x5838
+1510.100.35.0.1
+  __TEXT.__text: 0x4ea04
+  __TEXT.__auth_stubs: 0x1530
+  __TEXT.__objc_methlist: 0x2b94
+  __TEXT.__const: 0x943
+  __TEXT.__gcc_except_tab: 0x830
+  __TEXT.__cstring: 0x5e82
   __TEXT.__oslogstring: 0x88c
-  __TEXT.__unwind_info: 0xfb4
+  __TEXT.__unwind_info: 0xfb8
   __TEXT.__objc_classname: 0x698
-  __TEXT.__objc_methname: 0x642b
-  __TEXT.__objc_methtype: 0x40d7
-  __TEXT.__objc_stubs: 0x4aa0
+  __TEXT.__objc_methname: 0x6589
+  __TEXT.__objc_methtype: 0x40fe
+  __TEXT.__objc_stubs: 0x4b20
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x18a8
+  __DATA_CONST.__const: 0x18d0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6038
-  __DATA_CONST.__objc_selrefs: 0x1820
+  __DATA_CONST.__objc_const: 0x60d0
+  __DATA_CONST.__objc_selrefs: 0x1858
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x410
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x2680
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x26e0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xaa0
+  __AUTH_CONST.__auth_got: 0xaa8
   __AUTH.__os_assumes_log: 0x8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x2a0
-  __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x53c
+  __DATA.__objc_ivar: 0x548
   __DATA.__data: 0x384
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8
   __DATA.__bss: 0x180
-  __DATA_DIRTY.__const: 0x728
+  __DATA_DIRTY.__const: 0x708
   __DATA_DIRTY.__objc_const: 0x1440
   __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1489
-  Symbols:   4889
-  CStrings:  2566
+  Functions: 1497
+  Symbols:   4915
+  CStrings:  2582
 
Symbols:
+ -[OSLogEventProxy _tracepoint_id]
+ -[OSLogEventProxy _unreliableIdentifier]
+ -[OSLogEventProxy set_tracepoint_id:]
+ -[OSLogEventProxy set_unreliableIdentifier:]
+ -[_OSLogChunkStore .cxx_destruct]
+ -[_OSLogChunkStore fileName]
+ -[_OSLogChunkStore setFileName:]
+ -[_OSLogTracepointBuffer insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:]
+ -[_OSLogTracepointBuffer insertSimpleChunk:chunkOffset:chunkSetStartAddr:subchunk:options:]
+ -[_OSLogTracepointBuffer insertStatedumpChunk:chunkOffset:chunkSetStartAddr:subchunk:]
+ -[_OSLogTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]
+ GCC_except_table1078
+ GCC_except_table1113
+ GCC_except_table1153
+ GCC_except_table1266
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table385
+ GCC_except_table456
+ GCC_except_table479
+ GCC_except_table493
+ GCC_except_table522
+ GCC_except_table544
+ GCC_except_table619
+ GCC_except_table630
+ GCC_except_table632
+ GCC_except_table633
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table831
+ GCC_except_table832
+ GCC_except_table856
+ GCC_except_table866
+ GCC_except_table869
+ GCC_except_table904
+ GCC_except_table911
+ GCC_except_table929
+ GCC_except_table930
+ _OBJC_IVAR_$_OSLogEventProxy._tracepoint_id
+ _OBJC_IVAR_$_OSLogEventProxy._unreliableIdentifier
+ _OBJC_IVAR_$__OSLogChunkStore.fileName
+ __OBJC_$_PROP_LIST__OSLogChunkStore
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8un170006EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8un170006ERKS6_S9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8un170006ILi0EEEPKc
+ __ZSt28__throw_bad_array_new_lengthB8un170006v
+ ___61-[_OSLogEnumeratorCatalogSubchunk enumerateChunksUsingBlock:]_block_invoke_2
+ ___Block_byref_object_copy_.865
+ ___Block_byref_object_dispose_.866
+ ___block_descriptor_52_e8_32s40s_e774_B32?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8q16^v24ls32l8s40l8
+ ___block_descriptor_56_e8_32bs_e771_B24?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8^v16ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e336_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e336_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16lu48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e767_B16?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s_e76_B16?0^{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}8ls32l8
+ ___block_descriptor_72_e8_32bs40r48r56r_e290_B16?0^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}8lr40l8r48l8s32l8r56l8
+ ___block_descriptor_tmp.1115
+ ___block_descriptor_tmp.16.931
+ ___block_descriptor_tmp.1870
+ ___block_descriptor_tmp.2157
+ ___block_descriptor_tmp.2416
+ ___block_descriptor_tmp.5.2391
+ ___block_descriptor_tmp.57.2437
+ ___block_descriptor_tmp.65.2428
+ ___block_descriptor_tmp.935
+ ___block_literal_global.1113
+ ___block_literal_global.1364
+ ___block_literal_global.1621
+ ___block_literal_global.1710
+ ___block_literal_global.1941
+ ___block_literal_global.2380
+ ___block_literal_global.2386
+ ___block_literal_global.271
+ ___block_literal_global.2947
+ ___block_literal_global.354
+ ___block_literal_global.421
+ ___block_literal_global.55.1944
+ ___block_literal_global.592
+ ___block_literal_global.697
+ ___block_literal_global.907
+ ___block_literal_global.916
+ __unnamed_array_storage.1287
+ __unnamed_array_storage.1849
+ __unnamed_array_storage.687
+ _objc_msgSend$fileName
+ _objc_msgSend$insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:
+ _objc_msgSend$insertSimpleChunk:chunkOffset:chunkSetStartAddr:subchunk:options:
+ _objc_msgSend$insertStatedumpChunk:chunkOffset:chunkSetStartAddr:subchunk:
+ _objc_msgSend$insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$setFileName:
+ _objc_msgSend$set_unreliableIdentifier:
+ _objc_retain_x6
- -[_OSLogTracepointBuffer insertChunk:timestamp:subchunk:]
- -[_OSLogTracepointBuffer insertSimpleChunk:subchunk:options:]
- -[_OSLogTracepointBuffer insertStatedumpChunk:subchunk:]
- -[_OSLogTracepointBuffer insertTracepoints:subchunk:options:]
- GCC_except_table1070
- GCC_except_table1105
- GCC_except_table1145
- GCC_except_table1258
- GCC_except_table332
- GCC_except_table335
- GCC_except_table381
- GCC_except_table449
- GCC_except_table471
- GCC_except_table485
- GCC_except_table514
- GCC_except_table536
- GCC_except_table611
- GCC_except_table617
- GCC_except_table622
- GCC_except_table624
- GCC_except_table673
- GCC_except_table675
- GCC_except_table823
- GCC_except_table824
- GCC_except_table848
- GCC_except_table858
- GCC_except_table861
- GCC_except_table896
- GCC_except_table903
- GCC_except_table913
- GCC_except_table914
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB7v160006ERKS6_S9_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EEclEPKvm
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___Block_byref_object_copy_.836
- ___Block_byref_object_dispose_.837
- ___block_descriptor_52_e8_32s40s_e767_B16?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e327_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16ls40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e767_B16?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e327_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16lu48l8s32l8s40l8
- ___block_descriptor_56_e8_32s_e76_B16?0^{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}8ls32l8
- ___block_descriptor_72_e8_32bs40r48r56r_e281_B16?0^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}8lr40l8r48l8s32l8r56l8
- ___block_descriptor_tmp.1078
- ___block_descriptor_tmp.16.902
- ___block_descriptor_tmp.1838
- ___block_descriptor_tmp.2121
- ___block_descriptor_tmp.2389
- ___block_descriptor_tmp.5.2364
- ___block_descriptor_tmp.57.2410
- ___block_descriptor_tmp.65.2401
- ___block_descriptor_tmp.906
- ___block_literal_global.1076
- ___block_literal_global.1327
- ___block_literal_global.1590
- ___block_literal_global.1677
- ___block_literal_global.1909
- ___block_literal_global.2353
- ___block_literal_global.2359
- ___block_literal_global.264
- ___block_literal_global.2929
- ___block_literal_global.348
- ___block_literal_global.408
- ___block_literal_global.55.1912
- ___block_literal_global.587
- ___block_literal_global.675
- ___block_literal_global.878
- ___block_literal_global.887
- __unnamed_array_storage.1254
- __unnamed_array_storage.1817
- __unnamed_array_storage.665
- _objc_msgSend$insertChunk:timestamp:subchunk:
- _objc_msgSend$insertSimpleChunk:subchunk:options:
- _objc_msgSend$insertStatedumpChunk:subchunk:
- _objc_msgSend$insertTracepoints:subchunk:options:
CStrings:
+ "%s-%llu-%llu"
+ "B16@?0^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}8"
+ "B24@?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16"
+ "B24@?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8^v16"
+ "B32@?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8q16^v24"
+ "B40@0:8^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16Q24^{mach_timebase_info=II}32"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,VfileName"
+ "T@\"NSString\",N,V_tracepoint_id"
+ "TB,N,V_unreliableIdentifier"
+ "WallTime"
+ "^{?=IQ[1024c]qq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}"
+ "_tracepoint_id"
+ "_unreliableIdentifier"
+ "fileName"
+ "filePathAssemblerError"
+ "insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:"
+ "insertSimpleChunk:chunkOffset:chunkSetStartAddr:subchunk:options:"
+ "insertStatedumpChunk:chunkOffset:chunkSetStartAddr:subchunk:"
+ "insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:"
+ "pathWithComponents:"
+ "setFileName:"
+ "set_tracepoint_id:"
+ "set_unreliableIdentifier:"
+ "v48@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16q24^v32@40"
+ "v52@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16q24^v32@40I48"
+ "v56@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16q24^v32Q40@48"
- "B16@?0^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}8"
- "B24@?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16"
- "B40@0:8^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16Q24^{mach_timebase_info=II}32"
- "^{?=IQ(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}"
- "insertChunk:timestamp:subchunk:"
- "insertSimpleChunk:subchunk:options:"
- "insertStatedumpChunk:subchunk:"
- "insertTracepoints:subchunk:options:"
- "v32@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16@24"
- "v36@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16@24I32"
- "v40@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16Q24@32"

```
