## LoggingSupport

> `/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0x5dd50
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x3978
-  __TEXT.__const: 0x483
-  __TEXT.__gcc_except_tab: 0x12b4
-  __TEXT.__cstring: 0x6cf6
-  __TEXT.__oslogstring: 0x12aa
-  __TEXT.__unwind_info: 0x1160
-  __TEXT.__objc_classname: 0x7bf
-  __TEXT.__objc_methname: 0x7891
-  __TEXT.__objc_methtype: 0x5568
-  __TEXT.__objc_stubs: 0x5c00
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x1df8
-  __DATA_CONST.__objc_classlist: 0x260
+1815.0.0.0.0
+  __TEXT.__text: 0x60850
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0x3ad8
+  __TEXT.__const: 0x48b
+  __TEXT.__gcc_except_tab: 0x1298
+  __TEXT.__cstring: 0x6f64
+  __TEXT.__oslogstring: 0x1272
+  __TEXT.__unwind_info: 0x11a8
+  __TEXT.__objc_classname: 0x7ce
+  __TEXT.__objc_methname: 0x7b29
+  __TEXT.__objc_methtype: 0x56a4
+  __TEXT.__objc_stubs: 0x5e00
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x1e68
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d90
+  __DATA_CONST.__objc_selrefs: 0x1e40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xb10
-  __AUTH_CONST.__const: 0xa28
-  __AUTH_CONST.__cfstring: 0x3100
-  __AUTH_CONST.__objc_const: 0x81b8
+  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_arraydata: 0x450
+  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__const: 0xa48
+  __AUTH_CONST.__cfstring: 0x36a0
+  __AUTH_CONST.__objc_const: 0x84a8
+  __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x370
   __AUTH.__os_assumes_log: 0x8
-  __DATA.__objc_ivar: 0x638
+  __DATA.__objc_ivar: 0x660
   __DATA.__data: 0x4fc
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x200
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x230
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x14f0
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3825671C-4C43-314E-8D7B-CB62A95936D6
-  Functions: 1710
-  Symbols:   5778
-  CStrings:  3417
+  UUID: 64844BD9-5470-32D1-A2C2-3A3041F29EE1
+  Functions: 1745
+  Symbols:   5885
+  CStrings:  3554
 
Symbols:
+ -[OSLogBootEntry .cxx_destruct]
+ -[OSLogBootEntry bootDate]
+ -[OSLogBootEntry init:]
+ -[OSLogBootEntry mach_info]
+ -[OSLogBootEntry tz]
+ -[OSLogBootEntry unixTimeNs]
+ -[OSLogBootEntry uuid]
+ -[OSLogEventProxy _fillFromMessageV1:withTimebase:]
+ -[OSLogEventProxy _fillFromMessageV2:withTimebase:]
+ -[OSLogEventProxy _fillFromOSLogMessage:]
+ -[OSLogEventProxy _realTimeIdentifier]
+ -[OSLogEventProxy metricData]
+ -[OSLogEventProxy metricDimensions]
+ -[OSLogEventProxy metricLabel]
+ -[OSLogEventProxy metricMetadata]
+ -[OSLogEventProxy set_realTimeIdentifier:]
+ -[OSLogStatistics handler]
+ -[OSLogStatistics setEventHandler:]
+ -[OSLogStatistics setHandler:]
+ -[_OSLogDeserializedEventProxy metricData]
+ -[_OSLogDeserializedEventProxy metricDimensions]
+ -[_OSLogDeserializedEventProxy metricLabel]
+ -[_OSLogDeserializedEventProxy metricMetadata]
+ -[_OSLogPredicateMapper caseInsensitiveMapKeywordToConstantExpression:keywordMap:]
+ -[_OSLogPredicateMapper validateKeyPath:]
+ GCC_except_table1053
+ GCC_except_table1060
+ GCC_except_table1068
+ GCC_except_table1085
+ GCC_except_table1099
+ GCC_except_table1102
+ GCC_except_table1103
+ GCC_except_table1104
+ GCC_except_table1105
+ GCC_except_table1112
+ GCC_except_table1264
+ GCC_except_table1296
+ GCC_except_table1319
+ GCC_except_table1359
+ GCC_except_table1476
+ GCC_except_table1496
+ GCC_except_table1501
+ GCC_except_table1503
+ GCC_except_table1572
+ GCC_except_table1573
+ GCC_except_table1578
+ GCC_except_table1581
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table411
+ GCC_except_table482
+ GCC_except_table504
+ GCC_except_table517
+ GCC_except_table540
+ GCC_except_table652
+ GCC_except_table658
+ GCC_except_table663
+ GCC_except_table665
+ GCC_except_table666
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table830
+ GCC_except_table878
+ GCC_except_table879
+ GCC_except_table946
+ GCC_except_table955
+ GCC_except_table965
+ GCC_except_table968
+ _OBJC_CLASS_$_OSLogBootEntry
+ _OBJC_IVAR_$_OSLogBootEntry._mach_info
+ _OBJC_IVAR_$_OSLogBootEntry._tz
+ _OBJC_IVAR_$_OSLogBootEntry._unixTimeNs
+ _OBJC_IVAR_$_OSLogBootEntry._uuid
+ _OBJC_IVAR_$_OSLogEventProxy._metricDimensions
+ _OBJC_IVAR_$_OSLogEventProxy._metricLabel
+ _OBJC_IVAR_$_OSLogEventProxy._metricMetadata
+ _OBJC_IVAR_$_OSLogEventProxy._realTimeIdentifier
+ _OBJC_IVAR_$_OSLogStatistics._handler
+ _OBJC_IVAR_$__OSLogPredicateMapper._validKeyPathPrefixes
+ _OBJC_METACLASS_$_OSLogBootEntry
+ __OBJC_$_INSTANCE_METHODS_OSLogBootEntry
+ __OBJC_$_INSTANCE_VARIABLES_OSLogBootEntry
+ __OBJC_$_PROP_LIST_OSLogBootEntry
+ __OBJC_CLASS_RO_$_OSLogBootEntry
+ __OBJC_METACLASS_RO_$_OSLogBootEntry
+ __OSLogEventUnpackChunk.3957
+ __OSLogEventUnpackChunk.4370
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn200100EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn200100ERKS6_S9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ ___29-[OSActivityStream stopLocal]_block_invoke
+ ___41-[OSLogEventProxy _fillFromOSLogMessage:]_block_invoke
+ ___Block_byref_object_copy_.2731
+ ___Block_byref_object_copy_.2976
+ ___Block_byref_object_copy_.3989
+ ___Block_byref_object_copy_.4373
+ ___Block_byref_object_copy_.998
+ ___Block_byref_object_dispose_.2732
+ ___Block_byref_object_dispose_.2977
+ ___Block_byref_object_dispose_.3990
+ ___Block_byref_object_dispose_.4374
+ ___Block_byref_object_dispose_.999
+ ___OSLogInstallProfilePayload_block_invoke.9
+ ____enumerate_boots_impl_block_invoke
+ ____os_activity_stream_resume_with_filter_block_invoke.18
+ ____prefsLogHandle_block_invoke
+ ___block_descriptor_40_e8_32s_e103_v16?0^{os_timesync_boot_entry_s={os_timesync_header_s=SSI}[16C]{mach_timebase_info=II}Q{timezone=ii}}8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e851_B16?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})[0c]}8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e854_B20?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})[0c]}8i16ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e854_B20?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})[0c]}8i16lr32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56w_e25_v16?0"OSLogEventProxy"8ls32l8s40l8s48l8w56l8
+ ___block_descriptor_tmp.1074
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.1247
+ ___block_descriptor_tmp.13
+ ___block_descriptor_tmp.16.1070
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.19
+ ___block_descriptor_tmp.20.3161
+ ___block_descriptor_tmp.23.3095
+ ___block_descriptor_tmp.2518
+ ___block_descriptor_tmp.3093
+ ___block_descriptor_tmp.3370
+ ___block_descriptor_tmp.5.3345
+ ___block_descriptor_tmp.57.3382
+ ___block_descriptor_tmp.96
+ ___block_literal_global.1047
+ ___block_literal_global.1055
+ ___block_literal_global.1245
+ ___block_literal_global.1607
+ ___block_literal_global.17
+ ___block_literal_global.177
+ ___block_literal_global.186
+ ___block_literal_global.190
+ ___block_literal_global.197
+ ___block_literal_global.20
+ ___block_literal_global.2141
+ ___block_literal_global.222
+ ___block_literal_global.222.765
+ ___block_literal_global.2248
+ ___block_literal_global.243
+ ___block_literal_global.246
+ ___block_literal_global.258
+ ___block_literal_global.2632
+ ___block_literal_global.2874
+ ___block_literal_global.3331
+ ___block_literal_global.3337
+ ___block_literal_global.345
+ ___block_literal_global.37
+ ___block_literal_global.40
+ ___block_literal_global.417
+ ___block_literal_global.4229
+ ___block_literal_global.4401
+ ___block_literal_global.443
+ ___block_literal_global.458
+ ___block_literal_global.620
+ ___block_literal_global.63.4403
+ ___block_literal_global.775
+ ___block_literal_global.80
+ ___block_literal_global.94
+ ___enumerateAndDecompressSubchunk_block_invoke.3496
+ __chunk_support_parse_log
+ __fillFromOSLogMessage:.onceToken
+ __fillFromOSLogMessage:.timebase
+ __metric_get_percentile
+ __metric_serialize_basic
+ __os_activity_stream_entry_get_version
+ __os_trace_calloc_typed
+ __os_trace_malloc_typed
+ __os_trace_realloc_typed
+ __os_trace_zalloc_typed
+ __parse_metric_context_data
+ __prefsLogHandle
+ __prefsLogHandle.handle
+ __prefsLogHandle.onceToken
+ __resolve_uuid_slow_single
+ __timesync_for_each_boot
+ _create_timesync_error
+ _enumerateAndDecompressSubchunk.3495
+ _enumerate_boots
+ _hashtable_create
+ _mapLeftExpression:andRightExpression:.keypathMaps.455
+ _mapLeftExpression:andRightExpression:.once.456
+ _objc_msgSend$_fillFromMessageV1:withTimebase:
+ _objc_msgSend$_fillFromMessageV2:withTimebase:
+ _objc_msgSend$_fillFromOSLogMessage:
+ _objc_msgSend$caseInsensitiveMapKeywordToConstantExpression:keywordMap:
+ _objc_msgSend$handler
+ _objc_msgSend$init:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$metricData
+ _objc_msgSend$metricDimensions
+ _objc_msgSend$metricLabel
+ _objc_msgSend$metricMetadata
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$unixTimeNs
+ _objc_msgSend$validateKeyPath:
+ _property_getAttributes
+ _stopLocal.onceToken
+ _stopLocal.stop_lock
+ _validKeyPaths.once.441
+ _xpc_data_get_bytes_ptr
- -[OSLogEventProxy _fillFromXPCEventObject:]
- GCC_except_table1034
- GCC_except_table1041
- GCC_except_table1049
- GCC_except_table1056
- GCC_except_table1070
- GCC_except_table1073
- GCC_except_table1074
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1083
- GCC_except_table1233
- GCC_except_table1263
- GCC_except_table1286
- GCC_except_table1326
- GCC_except_table1439
- GCC_except_table1459
- GCC_except_table1464
- GCC_except_table1466
- GCC_except_table1535
- GCC_except_table1536
- GCC_except_table1541
- GCC_except_table1544
- GCC_except_table348
- GCC_except_table351
- GCC_except_table397
- GCC_except_table468
- GCC_except_table490
- GCC_except_table503
- GCC_except_table526
- GCC_except_table636
- GCC_except_table642
- GCC_except_table647
- GCC_except_table649
- GCC_except_table650
- GCC_except_table698
- GCC_except_table700
- GCC_except_table814
- GCC_except_table862
- GCC_except_table863
- GCC_except_table930
- GCC_except_table933
- GCC_except_table939
- GCC_except_table952
- __OSLogEventUnpackChunk.3834
- __OSLogEventUnpackChunk.4243
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __Znwm
- ___43-[OSLogEventProxy _fillFromXPCEventObject:]_block_invoke
- ___Block_byref_object_copy_.2650
- ___Block_byref_object_copy_.2879
- ___Block_byref_object_copy_.3868
- ___Block_byref_object_copy_.4246
- ___Block_byref_object_copy_.904
- ___Block_byref_object_dispose_.2651
- ___Block_byref_object_dispose_.2880
- ___Block_byref_object_dispose_.3869
- ___Block_byref_object_dispose_.4247
- ___Block_byref_object_dispose_.905
- ___OSLogInstallProfilePayload_block_invoke_2
- ____os_activity_stream_resume_with_filter_block_invoke.42
- ___block_descriptor_48_e8_32s40bs_e837_B16?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})}8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e840_B20?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})}8i16ls32l8s40l8
- ___block_descriptor_56_e8_32r40r48r_e840_B20?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ})}8i16lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48w_e25_v16?0"OSLogEventProxy"8ls32l8w48l8s40l8
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.1155
- ___block_descriptor_tmp.16.971
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.20.974
- ___block_descriptor_tmp.2440
- ___block_descriptor_tmp.2991
- ___block_descriptor_tmp.3256
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.47
- ___block_descriptor_tmp.5.3231
- ___block_descriptor_tmp.57.3268
- ___block_descriptor_tmp.95
- ___block_descriptor_tmp.976
- ___block_literal_global.1153
- ___block_literal_global.126
- ___block_literal_global.1524
- ___block_literal_global.16
- ___block_literal_global.171
- ___block_literal_global.19
- ___block_literal_global.192
- ___block_literal_global.205
- ___block_literal_global.2065
- ___block_literal_global.208
- ___block_literal_global.2171
- ___block_literal_global.226
- ___block_literal_global.237
- ___block_literal_global.241
- ___block_literal_global.2555
- ___block_literal_global.2736
- ___block_literal_global.274
- ___block_literal_global.3217
- ___block_literal_global.3223
- ___block_literal_global.359
- ___block_literal_global.36
- ___block_literal_global.39
- ___block_literal_global.4102
- ___block_literal_global.423
- ___block_literal_global.4274
- ___block_literal_global.438
- ___block_literal_global.576
- ___block_literal_global.63.4276
- ___block_literal_global.718
- ___block_literal_global.82
- ___block_literal_global.93
- ___block_literal_global.948
- ___block_literal_global.956
- ___enumerateAndDecompressSubchunk_block_invoke.3381
- ___sprintf_chk
- __fillFromXPCEventObject:.onceToken
- __fillFromXPCEventObject:.timebase
- __os_trace_calloc
- __os_trace_malloc
- __os_trace_realloc
- __os_trace_zalloc
- __parse_log_message
- _catalog_subchunk_string_insert
- _ctf_ref_dec
- _enumerateAndDecompressSubchunk.3380
- _fwrite
- _mapLeftExpression:andRightExpression:.keypathMaps.435
- _mapLeftExpression:andRightExpression:.once.436
- _objc_msgSend$_fillFromXPCEventObject:
- _validKeyPaths.once.421
CStrings:
+ "%s."
+ "<compose failure: 0x%llx>"
+ "<malformed>"
+ "<missing>"
+ "@\"NSDictionary\"16@0:8"
+ "@24@0:8^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})[0c]}16"
+ "@24@0:8^{os_timesync_boot_entry_s={os_timesync_header_s=SSI}[16C]{mach_timebase_info=II}Q{timezone=ii}}16"
+ "B16@?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})[0c]}8"
+ "B20@?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})[0c]}8i16"
+ "BUG IN LIBTRACE: Nope. Invalid message version"
+ "BUG IN LIBTRACE: Nope. Invalid version for stream object."
+ "Invalid bounds %llu for %s"
+ "OSLogBootEntry"
+ "OSLogTimesyncErrorDomain"
+ "Profile installation requested"
+ "Profile removal requested"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@?,C,N,V_handler"
+ "TB,N,V_realTimeIdentifier"
+ "TQ,R,N,V_unixTimeNs"
+ "T{mach_timebase_info=II},R,N,V_mach_info"
+ "Unable to open archive at path: %@: %s (%d)"
+ "Unable to open timesync database: %s (%d)"
+ "_fillFromMessageV1:withTimebase:"
+ "_fillFromMessageV2:withTimebase:"
+ "_fillFromOSLogMessage:"
+ "_handler"
+ "_mach_info"
+ "_metricDimensions"
+ "_metricLabel"
+ "_metricMetadata"
+ "_realTimeIdentifier"
+ "_unixTimeNs"
+ "_validKeyPathPrefixes"
+ "average"
+ "base_type"
+ "binCount"
+ "binInterval"
+ "binType"
+ "bins"
+ "bootDate"
+ "caseInsensitiveMapKeywordToConstantExpression:keywordMap:"
+ "counter"
+ "double"
+ "ema"
+ "encodeWithOSLogCoder:options:maxLength:"
+ "entryData"
+ "ff"
+ "gauge"
+ "handler"
+ "histogram"
+ "init:"
+ "initWithUTF8String:"
+ "int64"
+ "linear"
+ "log2"
+ "logdata.statistics.0.db"
+ "lowercaseString"
+ "mach_info"
+ "max"
+ "metricData"
+ "metricDimensions"
+ "metricEvent"
+ "metricLabel"
+ "metricMetadata"
+ "min"
+ "mtd"
+ "mtdi"
+ "mtl"
+ "mtm"
+ "numberWithChar:"
+ "numberWithUnsignedChar:"
+ "os_log_preferences"
+ "p95"
+ "p99"
+ "q1"
+ "q2"
+ "q3"
+ "scale"
+ "sd"
+ "setHandler:"
+ "set_realTimeIdentifier:"
+ "sma"
+ "uint64"
+ "unit"
+ "unixTimeNs"
+ "v16@?0^{os_timesync_boot_entry_s={os_timesync_header_s=SSI}[16C]{mach_timebase_info=II}Q{timezone=ii}}8"
+ "v24@0:8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}16"
+ "v32@0:8@16{mach_timebase_info=II}24"
+ "v36@0:8^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})[0c]}16r*24B32"
+ "validateKeyPath:"
+ "value"
+ "var"
+ "wgt"
+ "{?=\"type\"Q\"pid\"i\"uid\"I\"proc_id\"Q\"pidversion\"I\"proc_imageuuid\"*\"proc_imagepath\"*\"activity_id\"Q\"parent_id\"Q\"common\"{?=\"trace_id\"Q\"timestamp\"Q\"thread\"Q\"timebase\"{mach_timebase_info=\"numer\"I\"denom\"I}\"dsc_uuid\"*\"image_uuid\"*\"image_path\"*\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}\"offset\"Q\"format_offset\"Q\"opaque_flags\"I\"message\"*\"sz\"Q}\"\"(?=\"activity_create\"{?=\"creator_aid\"Q\"unique_pid\"Q}\"activity_transition\"{?=\"transition_id\"Q}\"log_message\"{?=\"buffer\"*\"buffer_sz\"Q\"hdr\"^{os_log_fmt_hdr_s}\"pubdata\"^v\"pubdata_sz\"S\"privdata\"*\"privdata_sz\"Q\"subsystem\"*\"category\"*\"oversize_id\"I\"ttl\"C\"persisted\"B\"signpost_scope\"C\"\"(?=\"signpost_type\"C\"metric_base_type\"C)\"\"(?=\"signpost_id\"Q\"metric_value\"Q)\"signpost_name_offset\"Q\"signpost_name\"*\"has_context_data\"B}\"useraction\"{?=\"persisted\"B}\"timesync\"{?=\"boot_uuid\"[16C]\"flags\"Q\"continuous_time\"Q\"wallclock_nsec\"Q\"ttl\"C}\"loss\"{?=\"start\"{?=\"stamp\"Q\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}}\"end\"{?=\"stamp\"Q\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}}\"count\"I})\"statedump\"{?=\"message_size\"Q\"ttl\"C}}"
+ "{mach_timebase_info=\"numer\"I\"denom\"I}"
+ "{mach_timebase_info=II}16@0:8"
- "@24@0:8^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})}16"
- "B16@?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})}8"
- "B20@?0^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})}8i16"
- "Invalid bounds %d for %s"
- "Profile installation requested with dictionary: %{public}@"
- "Profile removal requested with dictionary: %{public}@"
- "Wall Clock adjustment detected - results might be strange while using --end\n"
- "_fillFromXPCEventObject:"
- "v24@0:8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}16"
- "v36@0:8^{os_activity_stream_entry_s=IiQI**QQ(?={os_activity_stream_common_s=QQQ**{timeval=qi}{timezone=ii}QQI}{os_activity_stream_common_with_name_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_activity_create_s=QQQ**{timeval=qi}{timezone=ii}QQI*QQ}{os_activity_transition_s=QQQ**{timeval=qi}{timezone=ii}QQIQ}{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@}{os_activity_useraction_s=QQQ**{timeval=qi}{timezone=ii}QQI*B}{os_activity_statedump_s=QQQ**{timeval=qi}{timezone=ii}QQI*Q}{os_activity_timesync_s=QQQ**{timeval=qi}{timezone=ii}QQI[16C]QQQC}{os_activity_loss_s=QQQ**{timeval=qi}{timezone=ii}QQIQQI}{os_activity_breadcrumb_s=IQQ***}{os_activity_stream_activity_s=QQQ**{timeval=qi}{timezone=ii}QQI*}{os_trace_message_s=QQQ**{timeval=qi}{timezone=ii}QQI*^vQ@})}16r*24B32"
- "{?=\"type\"Q\"pid\"i\"uid\"I\"proc_id\"Q\"pidversion\"I\"proc_imageuuid\"*\"proc_imagepath\"*\"activity_id\"Q\"parent_id\"Q\"common\"{?=\"trace_id\"Q\"timestamp\"Q\"thread\"Q\"timebase\"{mach_timebase_info=\"numer\"I\"denom\"I}\"dsc_uuid\"*\"image_uuid\"*\"image_path\"*\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}\"offset\"Q\"format_offset\"Q\"opaque_flags\"I\"message\"*\"sz\"Q}\"\"(?=\"activity_create\"{?=\"creator_aid\"Q\"unique_pid\"Q}\"activity_transition\"{?=\"transition_id\"Q}\"log_message\"{?=\"buffer\"*\"buffer_sz\"Q\"hdr\"^{os_log_fmt_hdr_s}\"pubdata\"^v\"pubdata_sz\"S\"privdata\"*\"privdata_sz\"Q\"subsystem\"*\"category\"*\"oversize_id\"I\"ttl\"C\"persisted\"B\"signpost_scope\"C\"signpost_type\"C\"signpost_id\"Q\"signpost_name_offset\"Q\"signpost_name\"*\"has_context_data\"B}\"useraction\"{?=\"persisted\"B}\"timesync\"{?=\"boot_uuid\"[16C]\"flags\"Q\"continuous_time\"Q\"wallclock_nsec\"Q\"ttl\"C}\"loss\"{?=\"start\"{?=\"stamp\"Q\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}}\"end\"{?=\"stamp\"Q\"tv_gmt\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"tz\"{timezone=\"tz_minuteswest\"i\"tz_dsttime\"i}}\"count\"I})\"statedump\"{?=\"message_size\"Q\"ttl\"C}}"

```
