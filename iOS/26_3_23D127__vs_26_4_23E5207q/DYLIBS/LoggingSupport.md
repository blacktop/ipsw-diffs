## LoggingSupport

> `/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport`

```diff

-1815.80.2.0.0
-  __TEXT.__text: 0x61480
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x3b78
-  __TEXT.__const: 0x48f
-  __TEXT.__gcc_except_tab: 0x1244
-  __TEXT.__cstring: 0x7182
+1861.100.16.0.0
+  __TEXT.__text: 0x642a8
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0x3cc0
+  __TEXT.__const: 0x573
+  __TEXT.__gcc_except_tab: 0x128c
+  __TEXT.__cstring: 0x729b
   __TEXT.__oslogstring: 0x1272
-  __TEXT.__unwind_info: 0x12c0
-  __TEXT.__objc_classname: 0x7e6
-  __TEXT.__objc_methname: 0x7c01
-  __TEXT.__objc_methtype: 0x56cb
-  __TEXT.__objc_stubs: 0x5ee0
+  __TEXT.__unwind_info: 0x13e0
+  __TEXT.__objc_classname: 0x7e9
+  __TEXT.__objc_methname: 0x7f06
+  __TEXT.__objc_methtype: 0x569c
+  __TEXT.__objc_stubs: 0x6020
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x1ed8
+  __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e68
+  __DATA_CONST.__objc_selrefs: 0x1ef0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x450
-  __AUTH_CONST.__auth_got: 0xb08
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x458
+  __AUTH_CONST.__auth_got: 0xae8
   __AUTH_CONST.__const: 0xb88
-  __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x85e0
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0x8738
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x398
+  __AUTH.__objc_data: 0x370
   __AUTH.__os_assumes_log: 0x8
-  __DATA.__objc_ivar: 0x66c
-  __DATA.__data: 0x4fc
+  __DATA.__objc_ivar: 0x680
+  __DATA.__data: 0x504
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x238
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x14c8
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D975D4DD-CB61-373E-B2B5-2F07C6FC607C
-  Functions: 1770
-  Symbols:   5968
-  CStrings:  3580
+  UUID: BB910151-D4EE-3F0D-8579-841C2C2D4237
+  Functions: 1806
+  Symbols:   6048
+  CStrings:  3622
 
Symbols:
+ +[OSLogEventStore storeWithDirectoryURL:]
+ +[_OSLogCollectionReference URLDBRef:warningBlock:error:]
+ +[_OSLogCollectionReference _filesystemDBRef:timesyncPath:uuidPath:warningBlock:error:]
+ +[_OSLogCollectionReference localDBRefFromFilesystem:error:]
+ +[_OSLogCollectionReference localDBRefFromLogdWithError:]
+ +[_OSLogCollectionReference logarchiveDBRef:error:]
+ -[OSLogDeserializedEventStream observedSubsystemCategories]
+ -[OSLogEventLocalStore _createEventSource:metadata:timesync:]
+ -[OSLogEventLocalStore _createLCR:]
+ -[OSLogEventLocalStore _createLiveFD:error:]
+ -[OSLogEventLocalStore _createTSDB:error:]
+ -[OSLogEventLocalStore _finalizeEventSource:]
+ -[OSLogEventSerializer subsystemToCategories]
+ -[OSLogEventStore _addIndexFileForTraceFile:orChunkStore:toSource:]
+ -[OSLogEventStore _advanceProgress]
+ -[OSLogEventStore _createArchiveLCR:]
+ -[OSLogEventStore _createArchiveStoreMetadata:error:]
+ -[OSLogEventStore _createDirectoryStoreMetadata:error:]
+ -[OSLogEventStore _createEventSource:metadata:timesync:]
+ -[OSLogEventStore _createLCR:]
+ -[OSLogEventStore _createLiveFD:error:]
+ -[OSLogEventStore _createStoreMetadata:error:]
+ -[OSLogEventStore _createTSDB:error:]
+ -[OSLogEventStore _directoryURL]
+ -[OSLogEventStore _enumerateArchiveIntoSource:error:]
+ -[OSLogEventStore _enumerateDirectoryIntoSource:directory:dirname:]
+ -[OSLogEventStore _finalizeEventSource:]
+ -[OSLogEventStore _progress]
+ -[OSLogEventStore _reportProgressWithError:]
+ -[OSLogEventStore addFiles:toSource:]
+ -[OSLogEventStore initWithDirectoryURL:]
+ -[OSLogEventStore set_directoryURL:]
+ -[OSLogEventStore set_progress:]
+ -[OSLogPreferencesCategory oversizeMessagesEnabled]
+ -[OSLogPreferencesCategory setOversizeMessagesEnabled:]
+ -[OSLogPreferencesSubsystem _oversizeMessagesEnabledForCategory:]
+ -[OSLogPreferencesSubsystem _setOversizeMessagesEnabled:forCategory:]
+ -[OSLogPreferencesSubsystem oversizeMessagesEnabled]
+ -[OSLogPreferencesSubsystem setOversizeMessagesEnabled:]
+ -[OSLogPreferencesSubsystem setSignpostAllowStreaming:]
+ -[OSLogPreferencesSubsystem setSignpostBacktracesEnabled:]
+ -[OSLogPreferencesSubsystem setSignpostEnabled:]
+ -[OSLogPreferencesSubsystem setSignpostPersisted:]
+ -[OSLogPreferencesSubsystem signpostAllowStreaming]
+ -[OSLogPreferencesSubsystem signpostBacktracesEnabled]
+ -[OSLogPreferencesSubsystem signpostEnabled]
+ -[OSLogPreferencesSubsystem signpostPersisted]
+ -[_OSLogCatalogFilter catalogContainsSender:catalog:]
+ -[_OSLogCatalogFilter catalogContainsSubsystemOrCategory:catalog:]
+ -[_OSLogCatalogFilter evaluatePredicate:withCatalog:]
+ -[_OSLogEventSerializationMetadata setSubsystemToCategories:]
+ -[_OSLogEventSerializationMetadata subsystemToCategories]
+ GCC_except_table1070
+ GCC_except_table1077
+ GCC_except_table1103
+ GCC_except_table1115
+ GCC_except_table1118
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1293
+ GCC_except_table1325
+ GCC_except_table1351
+ GCC_except_table1393
+ GCC_except_table1511
+ GCC_except_table1532
+ GCC_except_table1537
+ GCC_except_table1539
+ GCC_except_table1630
+ GCC_except_table1631
+ GCC_except_table1636
+ GCC_except_table1639
+ GCC_except_table828
+ GCC_except_table843
+ GCC_except_table895
+ GCC_except_table896
+ GCC_except_table963
+ GCC_except_table966
+ GCC_except_table972
+ GCC_except_table982
+ GCC_except_table985
+ _OBJC_IVAR_$_OSLogEventLocalStore._livefd
+ _OBJC_IVAR_$_OSLogEventSerializer._subsystemToCategories
+ _OBJC_IVAR_$_OSLogEventStore._directoryURL
+ _OBJC_IVAR_$_OSLogEventStore._progress
+ _OBJC_IVAR_$__OSLogCatalogFilter._processNameToUUIDs
+ _OBJC_IVAR_$__OSLogCatalogFilter._senderNameToUUIDs
+ _OBJC_IVAR_$__OSLogCatalogFilter._structuredPredicate
+ _OBJC_IVAR_$__OSLogEventSerializationMetadata._subsystemToCategories
+ _OSLogConstructSourceDirectory
+ __OBJC_$_INSTANCE_VARIABLES_OSLogEventLocalStore
+ __OSLogCreateArchiveOptionsDictionary
+ __OSLogEventUnpackChunk.3980
+ __OSLogEventUnpackChunk.4437
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE4findIS7_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS9_S8_EEEERKT_
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fon210106EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9fon210106ERKS6_S9_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_S8_EEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fon210106ILi0EEEPKc
+ __ZSt28__throw_bad_array_new_lengthB9fon210106v
+ ___39-[_OSLogCatalogFilter buildDSCMappings]_block_invoke
+ ___39-[_OSLogCatalogFilter buildDSCMappings]_block_invoke_2
+ ___45-[OSLogEventLocalStore _finalizeEventSource:]_block_invoke
+ ___53-[OSLogEventStore _createArchiveStoreMetadata:error:]_block_invoke
+ ___53-[_OSLogCatalogFilter catalogContainsSender:catalog:]_block_invoke
+ ___54-[_OSLogCatalogFilter catalogContainsProcess:catalog:]_block_invoke
+ ___54-[_OSLogEventSerializationMetadata dataRepresentation]_block_invoke
+ ___55-[OSLogEventStore _createDirectoryStoreMetadata:error:]_block_invoke
+ ___56-[_OSLogCatalogFilter catalogContainsProcessID:catalog:]_block_invoke
+ ___63-[_OSLogEventSerializationMetadata initWithDataRepresentation:]_block_invoke_2
+ ___66-[_OSLogCatalogFilter catalogContainsSubsystemOrCategory:catalog:]_block_invoke
+ ___75-[OSLogEventSerializer initWithSource:dataProcessingBlock:completionBlock:]_block_invoke_3
+ ___Block_byref_object_copy_.2727
+ ___Block_byref_object_copy_.2995
+ ___Block_byref_object_copy_.4018
+ ___Block_byref_object_copy_.4441
+ ___Block_byref_object_dispose_.2728
+ ___Block_byref_object_dispose_.2996
+ ___Block_byref_object_dispose_.4019
+ ___Block_byref_object_dispose_.4442
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24ls32l8
+ ___block_descriptor_44_e8_32r_e9_v16?0^v8lr32l8
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.20.3179
+ ___block_descriptor_tmp.23.3113
+ ___block_descriptor_tmp.2514
+ ___block_descriptor_tmp.3.96
+ ___block_descriptor_tmp.3111
+ ___block_descriptor_tmp.3425
+ ___block_descriptor_tmp.5.3400
+ ___block_descriptor_tmp.57
+ ___block_literal_global.103
+ ___block_literal_global.140
+ ___block_literal_global.1589
+ ___block_literal_global.194
+ ___block_literal_global.205
+ ___block_literal_global.2123
+ ___block_literal_global.219
+ ___block_literal_global.2229
+ ___block_literal_global.236
+ ___block_literal_global.2628
+ ___block_literal_global.2858
+ ___block_literal_global.3386
+ ___block_literal_global.3392
+ ___block_literal_global.355
+ ___block_literal_global.422
+ ___block_literal_global.4279
+ ___block_literal_global.4468
+ ___block_literal_global.5.94
+ ___block_literal_global.56
+ ___block_literal_global.63.4470
+ ___block_literal_global.66
+ ___block_literal_global.766
+ ___enumerateAndDecompressSubchunk_block_invoke.3549
+ __enumerateArchiveIntoSource:error:.dirs
+ __os_trace_block_writes_allowed
+ _dirfd
+ _enumerateAndDecompressSubchunk.3548
+ _logarchive_key_directory
+ _objc_msgSend$URLDBRef:warningBlock:error:
+ _objc_msgSend$_addIndexFileForTraceFile:orChunkStore:toSource:
+ _objc_msgSend$_advanceProgress
+ _objc_msgSend$_createArchiveLCR:
+ _objc_msgSend$_createArchiveStoreMetadata:error:
+ _objc_msgSend$_createDirectoryStoreMetadata:error:
+ _objc_msgSend$_createEventSource:metadata:timesync:
+ _objc_msgSend$_createLCR:
+ _objc_msgSend$_createLiveFD:error:
+ _objc_msgSend$_createStoreMetadata:error:
+ _objc_msgSend$_createTSDB:error:
+ _objc_msgSend$_enumerateArchiveIntoSource:error:
+ _objc_msgSend$_enumerateDirectoryIntoSource:directory:dirname:
+ _objc_msgSend$_filesystemDBRef:timesyncPath:uuidPath:warningBlock:error:
+ _objc_msgSend$_finalizeEventSource:
+ _objc_msgSend$_oversizeMessagesEnabledForCategory:
+ _objc_msgSend$_progress
+ _objc_msgSend$_reportProgressWithError:
+ _objc_msgSend$_setOversizeMessagesEnabled:forCategory:
+ _objc_msgSend$addFiles:toSource:
+ _objc_msgSend$allObjects
+ _objc_msgSend$initWithDirectoryURL:
+ _objc_msgSend$localDBRefFromFilesystem:error:
+ _objc_msgSend$localDBRefFromLogdWithError:
+ _objc_msgSend$logarchiveDBRef:error:
+ _objc_msgSend$setSubsystemToCategories:
+ _objc_msgSend$set_progress:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$subsystemToCategories
+ _objc_release_x2
+ _os_variant_is_darwinos
- +[_OSLogCollectionReference localDBRefWithError:]
- -[OSLogEventLocalStore prepareWithCompletionHandler:]
- -[OSLogEventStore addFilesToSource:forCollection:withProgress:]
- -[_OSLogCatalogFilter addProcessID:]
- -[_OSLogCatalogFilter addProcessLookupSubstr:]
- -[_OSLogCatalogFilter addSenderLookupSubstr:]
- -[_OSLogCatalogFilter addSubsystem:]
- -[_OSLogCatalogFilter addUUID:]
- -[_OSLogCatalogFilter containsProcessID:]
- -[_OSLogCatalogFilter containsProcessLookupSubstr:]
- -[_OSLogCatalogFilter containsSenderLookupSubstr:]
- -[_OSLogCatalogFilter containsSubsystemSubstr:]
- -[_OSLogCatalogFilter containsUUID:]
- -[_OSLogCatalogFilter generateUUIDSet]
- -[_OSLogCatalogFilter handleDSOFile:]
- -[_OSLogCatalogFilter isKeptCatalog:]
- -[_OSLogCatalogFilter processComparisonPredicate:]
- -[_OSLogCatalogFilter readDSCUUIDs]
- -[_OSLogCatalogFilter readDSOUUIDs]
- GCC_except_table1078
- GCC_except_table1093
- GCC_except_table1110
- GCC_except_table1124
- GCC_except_table1127
- GCC_except_table1129
- GCC_except_table1130
- GCC_except_table1137
- GCC_except_table1289
- GCC_except_table1321
- GCC_except_table1344
- GCC_except_table1384
- GCC_except_table1501
- GCC_except_table1521
- GCC_except_table1526
- GCC_except_table1528
- GCC_except_table1597
- GCC_except_table1598
- GCC_except_table1603
- GCC_except_table1606
- GCC_except_table855
- GCC_except_table903
- GCC_except_table904
- GCC_except_table971
- GCC_except_table974
- GCC_except_table980
- GCC_except_table990
- GCC_except_table993
- _OBJC_IVAR_$__OSLogCatalogFilter._pidAccept
- _OBJC_IVAR_$__OSLogCatalogFilter._subsysSubstrAccept
- _OBJC_IVAR_$__OSLogCatalogFilter._uuidAccept
- _OSLogCreateArchiveWithPredicate
- __InitArchiveDictionary
- __OSLogEventUnpackChunk.3981
- __OSLogEventUnpackChunk.4402
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE4findIS7_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS9_S8_EEEERKT_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn200100EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn200100ERKS6_S9_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_S8_EEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
- __ZSt28__throw_bad_array_new_lengthB8nn200100v
- ___35-[_OSLogCatalogFilter readDSCUUIDs]_block_invoke
- ___35-[_OSLogCatalogFilter readDSCUUIDs]_block_invoke_2
- ___37-[_OSLogCatalogFilter isKeptCatalog:]_block_invoke
- ___37-[_OSLogCatalogFilter isKeptCatalog:]_block_invoke_2
- ___37-[_OSLogCatalogFilter isKeptCatalog:]_block_invoke_3
- ___48-[OSLogEventStore prepareWithCompletionHandler:]_block_invoke
- ___53-[OSLogEventLocalStore prepareWithCompletionHandler:]_block_invoke
- ___53-[OSLogEventLocalStore prepareWithCompletionHandler:]_block_invoke_2
- ___Block_byref_object_copy_.2720
- ___Block_byref_object_copy_.3007
- ___Block_byref_object_copy_.4013
- ___Block_byref_object_copy_.4406
- ___Block_byref_object_dispose_.2721
- ___Block_byref_object_dispose_.3008
- ___Block_byref_object_dispose_.4014
- ___Block_byref_object_dispose_.4407
- ___block_descriptor_48_e8_32s40r_e9_v16?0^v8ls32l8r40l8
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.2.93
- ___block_descriptor_tmp.20.3185
- ___block_descriptor_tmp.23.3119
- ___block_descriptor_tmp.2507
- ___block_descriptor_tmp.3117
- ___block_descriptor_tmp.3396
- ___block_descriptor_tmp.5.3371
- ___block_descriptor_tmp.57.3408
- ___block_literal_global.100
- ___block_literal_global.1593
- ___block_literal_global.180
- ___block_literal_global.185
- ___block_literal_global.186
- ___block_literal_global.197
- ___block_literal_global.2127
- ___block_literal_global.2233
- ___block_literal_global.234
- ___block_literal_global.2621
- ___block_literal_global.2865
- ___block_literal_global.3357
- ___block_literal_global.3363
- ___block_literal_global.353
- ___block_literal_global.4
- ___block_literal_global.420
- ___block_literal_global.4261
- ___block_literal_global.4434
- ___block_literal_global.55
- ___block_literal_global.62
- ___block_literal_global.63.4436
- ___block_literal_global.765
- ___enumerateAndDecompressSubchunk_block_invoke.3522
- __enumerateArchiveIntoSource
- __enumerateArchiveIntoSource.dirs
- __enumerateDirectoryIntoSource
- __os_log_fmt_compose_format_copy
- __progress
- _ctf_copy_membnames
- _enumerateAndDecompressSubchunk.3521
- _fdopen
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addFilesToSource:forCollection:withProgress:
- _objc_msgSend$addProcessID:
- _objc_msgSend$addProcessLookupSubstr:
- _objc_msgSend$addSenderLookupSubstr:
- _objc_msgSend$addSubsystem:
- _objc_msgSend$addUUID:
- _objc_msgSend$containsProcessID:
- _objc_msgSend$containsProcessLookupSubstr:
- _objc_msgSend$containsSenderLookupSubstr:
- _objc_msgSend$containsSubsystemSubstr:
- _objc_msgSend$containsUUID:
- _objc_msgSend$currentProgress
- _objc_msgSend$generateUUIDSet
- _objc_msgSend$handleDSOFile:
- _objc_msgSend$isKeptCatalog:
- _objc_msgSend$localDBRefWithError:
- _objc_msgSend$processLeftExpression:andRightExpression:
- _objc_msgSend$readDSCUUIDs
- _objc_msgSend$readDSOUUIDs
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "@\"NSProgress\""
+ "@32@0:8@?16^@24"
+ "@40@0:8@16@?24^@32"
+ "@56@0:8r*16r*24r*32@?40^@48"
+ "B32@0:8^i16^@24"
+ "Enable-Oversize-Messages"
+ "OSLogConstructSourceDirectory"
+ "SubsystemToCategories"
+ "T@\"NSDictionary\",&,N,V_subsystemToCategories"
+ "T@\"NSMutableDictionary\",R,N,V_subsystemToCategories"
+ "T@\"NSProgress\",&,N,V_progress"
+ "T@\"NSURL\",&,N,V_directoryURL"
+ "URLDBRef:warningBlock:error:"
+ "^{_os_timesync_db_s=}28@0:8i16^@20"
+ "_addIndexFileForTraceFile:orChunkStore:toSource:"
+ "_advanceProgress"
+ "_createArchiveLCR:"
+ "_createArchiveStoreMetadata:error:"
+ "_createDirectoryStoreMetadata:error:"
+ "_createEventSource:metadata:timesync:"
+ "_createLCR:"
+ "_createLiveFD:error:"
+ "_createStoreMetadata:error:"
+ "_createTSDB:error:"
+ "_directoryURL"
+ "_enumerateArchiveIntoSource:error:"
+ "_enumerateDirectoryIntoSource:directory:dirname:"
+ "_filesystemDBRef:timesyncPath:uuidPath:warningBlock:error:"
+ "_finalizeEventSource:"
+ "_livefd"
+ "_oversizeMessagesEnabledForCategory:"
+ "_processNameToUUIDs"
+ "_progress"
+ "_reportProgressWithError:"
+ "_senderNameToUUIDs"
+ "_setOversizeMessagesEnabled:forCategory:"
+ "_structuredPredicate"
+ "_subsystemToCategories"
+ "addFiles:toSource:"
+ "allObjects"
+ "com.apple.logd"
+ "directory"
+ "failed to open directory store: %s"
+ "failed to open local database"
+ "initWithDirectoryURL:"
+ "localDBRefFromFilesystem:error:"
+ "localDBRefFromLogdWithError:"
+ "logarchiveDBRef:error:"
+ "observedSubsystemCategories"
+ "oversizeMessagesEnabled"
+ "setOversizeMessagesEnabled:"
+ "setSubsystemToCategories:"
+ "set_directoryURL:"
+ "set_progress:"
+ "storeWithDirectoryURL:"
+ "stringByDeletingLastPathComponent"
+ "subsystemToCategories"
+ "uuidtext"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
+ "v40@0:8@16^{?=iQQ*iqqi{_opaque_pthread_mutex_t=q[56c]}^{_telldir}}24r*32"
- "B24@0:8^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}16"
- "_pidAccept"
- "_subsysSubstrAccept"
- "_uuidAccept"
- "addFilesToSource:forCollection:withProgress:"
- "addProcessLookupSubstr:"
- "addSenderLookupSubstr:"
- "addSubsystem:"
- "addUUID:"
- "containsProcessID:"
- "containsProcessLookupSubstr:"
- "containsSenderLookupSubstr:"
- "containsSubsystemSubstr:"
- "containsUUID:"
- "currentProgress"
- "generateUUIDSet"
- "handleDSOFile:"
- "isKeptCatalog:"
- "localDBRefWithError:"
- "processLeftExpression:andRightExpression:"
- "readDSCUUIDs"
- "readDSOUUIDs"
- "v24@0:8^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}16"
- "w+"

```
