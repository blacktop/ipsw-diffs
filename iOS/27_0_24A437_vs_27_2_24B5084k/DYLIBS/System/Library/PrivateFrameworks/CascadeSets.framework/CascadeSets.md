## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0xa685c
-  __TEXT.__objc_methlist: 0x66a4
-  __TEXT.__const: 0x3cc8
-  __TEXT.__gcc_except_tab: 0x18bc
-  __TEXT.__cstring: 0x8d47
-  __TEXT.__oslogstring: 0x5410
+255.0.2.0.0
+  __TEXT.__text: 0xa9ef8
+  __TEXT.__objc_methlist: 0x65ec
+  __TEXT.__const: 0x4238
+  __TEXT.__gcc_except_tab: 0x1640
+  __TEXT.__cstring: 0x9377
+  __TEXT.__oslogstring: 0x5460
   __TEXT.__dlopen_cstrs: 0x3d8
-  __TEXT.__swift5_typeref: 0xe33
-  __TEXT.__constg_swiftt: 0x16bc
-  __TEXT.__swift5_reflstr: 0x1354
-  __TEXT.__swift5_fieldmd: 0x1a1c
-  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_typeref: 0xf73
+  __TEXT.__constg_swiftt: 0x1848
+  __TEXT.__swift5_reflstr: 0x1494
+  __TEXT.__swift5_fieldmd: 0x1be4
+  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x68
-  __TEXT.__swift5_proto: 0x214
-  __TEXT.__swift5_types: 0x1cc
-  __TEXT.__swift5_capture: 0x1b0
-  __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x3e28
-  __TEXT.__eh_frame: 0x2970
+  __TEXT.__swift5_proto: 0x254
+  __TEXT.__swift5_types: 0x1f8
+  __TEXT.__swift5_capture: 0x230
+  __TEXT.__swift5_mpenum: 0xd8
+  __TEXT.__swift5_protos: 0x3c
+  __TEXT.__unwind_info: 0x3f20
+  __TEXT.__eh_frame: 0x2cf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ca8
-  __DATA_CONST.__objc_classlist: 0x510
+  __DATA_CONST.__const: 0x1c08
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3278
+  __DATA_CONST.__objc_selrefs: 0x3218
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x360
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x6d8
-  __AUTH_CONST.__const: 0x38e8
-  __AUTH_CONST.__cfstring: 0x5ce0
-  __AUTH_CONST.__objc_const: 0x12428
-  __AUTH_CONST.__weak_auth_got: 0x18
+  __DATA_CONST.__got: 0x6e0
+  __AUTH_CONST.__const: 0x4010
+  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__objc_const: 0x12290
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xd70
-  __AUTH.__objc_data: 0x1278
-  __AUTH.__data: 0x6d0
-  __DATA.__objc_ivar: 0x694
-  __DATA.__data: 0x1a10
+  __AUTH.__objc_data: 0x1238
+  __AUTH.__data: 0x7c0
+  __DATA.__objc_ivar: 0x66c
+  __DATA.__data: 0x1a78
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x1890
-  __DATA_DIRTY.__data: 0x13f0
+  __DATA_DIRTY.__data: 0x13e0
   __DATA_DIRTY.__bss: 0x540
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4615
-  Symbols:   6384
-  CStrings:  1325
+  Functions: 4711
+  Symbols:   6341
+  CStrings:  1326
 
Symbols:
+ -[CCDatabaseWriter(Compaction) _deleteRecordsForDeviceRowId:vectorType:sequenceRange:excludingRowId:error:]
+ -[CCDatabaseWriter(Compaction) _firstRowIdForDeviceRowId:vectorType:sequenceRange:rowId:error:]
+ -[CCDatabaseWriter(Compaction) _processRange:deviceRowId:vectorType:stateSets:error:]
+ -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:markerRowId:sequenceRange:skippedEmptyRun:error:]
+ -[CCProvenanceStateSets ineligibleRowCount]
+ -[CCProvenanceStateSets initWithEligibleSequences:compactedSequences:ineligibleRowCount:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:]
+ -[CCSetChangePublisher validateBookmarkValue:]
+ GCC_except_table27
+ _CCCompactionRunCriterion
+ _CCCompactionRunParameters
+ _OBJC_IVAR_$_CCProvenanceStateSets._ineligibleRowCount
+ _OUTLINED_FUNCTION_42
+ __CLASS_METHODS_CCSetMetrics
+ __DATA_CCSetMetrics
+ __DATA__TtCC11CascadeSets10SetMetrics10Statements
+ __INSTANCE_METHODS_CCSetMetrics
+ __IVARS__TtCC11CascadeSets10SetMetrics10Statements
+ __METACLASS_DATA_CCSetMetrics
+ __METACLASS_DATA__TtCC11CascadeSets10SetMetrics10Statements
+ ___95-[CCDatabaseWriter(Compaction) _firstRowIdForDeviceRowId:vectorType:sequenceRange:rowId:error:]_block_invoke
+ ___block_descriptor_129_e8_32s40s48s56s64s72bs80r88r96r104r112r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r80l8s72l8r88l8r96l8s48l8r104l8s56l8s64l8r112l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r72r_e24_v32?0{_NSRange=QQ}8^B24ls56l8s32l8s40l8s48l8r64l8r72l8
+ ___unnamed_9
+ __swiftEmptySetSingleton
+ __swift_stdlib_bridgeErrorToNSError
+ _associated conformance 11CascadeSets10SetMetricsC14DeviceIdentityVSHAASQ
+ _get_enum_tag_for_layout_string 11CascadeSets15SetMetricsErrorO
+ _objc_msgSend$_deleteRecordsForDeviceRowId:vectorType:sequenceRange:excludingRowId:error:
+ _objc_msgSend$_firstRowIdForDeviceRowId:vectorType:sequenceRange:rowId:error:
+ _objc_msgSend$_processRange:deviceRowId:vectorType:stateSets:error:
+ _objc_msgSend$_updateTombstoneRowsForDeviceRowId:vectorType:markerRowId:sequenceRange:skippedEmptyRun:error:
+ _objc_msgSend$computeAndReportMetricsFor:shouldDefer:
+ _objc_msgSend$criterionWithColumnName:NOTEQUALSColumnValue:
+ _objc_msgSend$ineligibleRowCount
+ _objc_msgSend$initWithEligibleSequences:compactedSequences:ineligibleRowCount:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:
+ _objc_msgSend$initWithUnsignedShort:
+ _symbolic $s11CascadeSets16MetricsReportingP
+ _symbolic SDySSSo8NSObjectCG
+ _symbolic SS3sql_t
+ _symbolic SS4scan_t
+ _symbolic So5CCSetC
+ _symbolic _____ 11CascadeSets10SetMetricsC
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC17ContentBlobCursorV
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC22RemoteProvenanceCursorV
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC25LocalContentBlobStatementV
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC25RemoteProvenanceStatementV
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC26MetaContentLengthStatementV
+ _symbolic _____ 11CascadeSets10SetMetricsC10StatementsC30RemoteOnlyContentBlobStatementV
+ _symbolic _____ 11CascadeSets10SetMetricsC14DeviceIdentityV
+ _symbolic _____ 11CascadeSets15SetMetricsErrorO
+ _symbolic _____ 11CascadeSets21CoreAnalyticsReporterV
+ _symbolic _____Iegd_ s6UInt64V
+ _symbolic _____Iegr_ s6UInt64V
+ _symbolic _____IeyBd_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____Sg 11CascadeSets10SetMetricsC10StatementsC25LocalContentBlobStatementV
+ _symbolic _____Sg 11CascadeSets10SetMetricsC10StatementsC25RemoteProvenanceStatementV
+ _symbolic _____Sg 11CascadeSets10SetMetricsC10StatementsC26MetaContentLengthStatementV
+ _symbolic _____Sg 11CascadeSets10SetMetricsC10StatementsC30RemoteOnlyContentBlobStatementV
+ _symbolic _____ySDySSSo8NSObjectCGG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____y_SSSgG So20CCDatabaseConnectionC11CascadeSetsE6ColumnV
+ _symbolic _____y_____G s10_NativeSetV 11CascadeSets0B7MetricsC14DeviceIdentityV
+ _symbolic _____y_____G s11_SetStorageC 11CascadeSets0A7MetricsC14DeviceIdentityV
+ _type_layout_string 11CascadeSets10SetMetricsC10StatementsC17ContentBlobCursorV
+ _type_layout_string 11CascadeSets10SetMetricsC10StatementsC22RemoteProvenanceCursorV
+ _type_layout_string 11CascadeSets10SetMetricsC10StatementsC25RemoteProvenanceStatementV
+ _type_layout_string 11CascadeSets10SetMetricsC10StatementsC30RemoteOnlyContentBlobStatementV
+ _type_layout_string 11CascadeSets10SetMetricsC14DeviceIdentityV
+ _type_layout_string 11CascadeSets15SetMetricsErrorO
- +[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]
- +[CCSetMetrics _populationStandardDeviation:mean:]
- +[CCSetMetrics computeAndReportMetricsForAllSets:shouldDefer:]
- +[CCSetMetrics reportAnalyticsEvent:withName:]
- +[CCSetMetrics shouldReportAnalyticsEventWithName:]
- -[CCDatabaseWriter(Compaction) _deleteRecordsWithRowIds:vectorType:error:]
- -[CCDatabaseWriter(Compaction) _processRange:deviceRowId:vectorType:stateSets:error:shouldDefer:]
- -[CCDatabaseWriter(Compaction) _sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:]
- -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:]
- -[CCProvenanceCompactionRecord .cxx_destruct]
- -[CCProvenanceCompactionRecord initWithRowId:]
- -[CCProvenanceCompactionRecord rowId]
- -[CCProvenanceStateSets description]
- -[CCProvenanceStateSets ineligibleSequences]
- -[CCProvenanceStateSets initWithIneligibleSequences:eligibleSequences:compactedSequences:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:]
- -[CCSetChangePublisher validateBookmark:]
- -[CCSetDistribution .cxx_construct]
- -[CCSetDistribution .cxx_destruct]
- -[CCSetDistribution addSetChange:]
- -[CCSetDistribution compute]
- -[CCSetDistribution initWithSet:sizeInBytes:]
- -[CCSetDistribution init]
- -[CCSetMetrics init]
- _CCAnalyticsEventNameSetDistribution
- _OBJC_CLASS_$_CCProvenanceCompactionRecord
- _OBJC_CLASS_$_CCSetDistribution
- _OBJC_IVAR_$_CCProvenanceCompactionRecord._rowId
- _OBJC_IVAR_$_CCProvenanceStateSets._ineligibleSequences
- _OBJC_IVAR_$_CCSetDistribution._contentLengths
- _OBJC_IVAR_$_CCSetDistribution._deviceContentCount
- _OBJC_IVAR_$_CCSetDistribution._devices
- _OBJC_IVAR_$_CCSetDistribution._localContentCount
- _OBJC_IVAR_$_CCSetDistribution._metaContentLengths
- _OBJC_IVAR_$_CCSetDistribution._set
- _OBJC_IVAR_$_CCSetDistribution._sizeInBytes
- _OBJC_IVAR_$_CCSetDistribution._sumContentLength
- _OBJC_IVAR_$_CCSetDistribution._sumMetaContentLength
- _OBJC_METACLASS_$_CCProvenanceCompactionRecord
- _OBJC_METACLASS_$_CCSetDistribution
- __OBJC_$_CLASS_METHODS_CCSetMetrics
- __OBJC_$_INSTANCE_METHODS_CCProvenanceCompactionRecord
- __OBJC_$_INSTANCE_METHODS_CCSetDistribution
- __OBJC_$_INSTANCE_METHODS_CCSetMetrics
- __OBJC_$_INSTANCE_VARIABLES_CCProvenanceCompactionRecord
- __OBJC_$_INSTANCE_VARIABLES_CCSetDistribution
- __OBJC_$_PROP_LIST_CCProvenanceCompactionRecord
- __OBJC_CLASS_RO_$_CCProvenanceCompactionRecord
- __OBJC_CLASS_RO_$_CCSetDistribution
- __OBJC_CLASS_RO_$_CCSetMetrics
- __OBJC_METACLASS_RO_$_CCProvenanceCompactionRecord
- __OBJC_METACLASS_RO_$_CCSetDistribution
- __OBJC_METACLASS_RO_$_CCSetMetrics
- __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorC1B9fqe220106EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt20bad_array_new_lengthC1Ev
- __ZNSt20bad_array_new_lengthD1Ev
- __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIjEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
- __ZNSt3__119__shared_weak_count14__release_weakEv
- __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220106Ev
- __ZNSt3__119__shared_weak_countD2Ev
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEED1Ev
- __ZNSt3__120__throw_length_errorB9fqe220106EPKc
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9fqe220106Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRjEEEPjDpOT_
- __ZSt28__throw_bad_array_new_lengthB9fqe220106v
- __ZTINSt3__119__shared_weak_countE
- __ZTINSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
- __ZTISt12length_error
- __ZTISt20bad_array_new_length
- __ZTSNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
- __ZTVN10__cxxabiv120__si_class_type_infoE
- __ZTVNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
- __ZTVSt12length_error
- __ZdlPv
- __ZdlPvSt19__type_descriptor_t
- __ZnwmSt19__type_descriptor_t
- ___141-[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:]_block_invoke
- ___56+[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]_block_invoke
- ___56+[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]_block_invoke_2
- ___92-[CCDatabaseWriter(Compaction) _sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64s72s80bs88r96r104r112r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r88l8s80l8r96l8r104l8s48l8r112l8s56l8s64l8s72l8
- ___block_descriptor_32_e38_16?0"CCProvenanceCompactionRecord"8l
- ___block_descriptor_40_e8_32s_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8
- ___block_descriptor_48_ea8_32r40r_e40_v24?0"BPSCompletion"8"<BMBookmark>"16lr32l8r40l8
- ___block_descriptor_72_ea8_32s40bs48r56r64r_e21_B16?0"CCSetChange"8lr48l8s40l8s32l8r56l8r64l8
- ___block_descriptor_81_e8_32s40s48s56bs64r72r_e24_v32?0{_NSRange=QQ}8^B24lr64l8s32l8s40l8s48l8r72l8s56l8
- ___cxa_allocate_exception
- ___cxa_free_exception
- ___cxa_throw
- _objc_msgSend$_computeMetricsForSet:shouldDefer:error:
- _objc_msgSend$_deleteRecordsWithRowIds:vectorType:error:
- _objc_msgSend$_pas_mappedArrayWithTransform:
- _objc_msgSend$_populationStandardDeviation:mean:
- _objc_msgSend$_processRange:deviceRowId:vectorType:stateSets:error:shouldDefer:
- _objc_msgSend$_sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:
- _objc_msgSend$_updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:
- _objc_msgSend$addSetChange:
- _objc_msgSend$compute
- _objc_msgSend$computeAndReportMetricsForAllSets:shouldDefer:
- _objc_msgSend$initWithIneligibleSequences:eligibleSequences:compactedSequences:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:
- _objc_msgSend$initWithRowId:
- _objc_msgSend$initWithSet:sizeInBytes:
- _objc_msgSend$reportAnalyticsEvent:withName:
- _objc_msgSend$rowId
- _objc_msgSend$shouldReportAnalyticsEventWithName:
- _objc_msgSend$subarrayWithRange:
- _objc_msgSend$unsafeGuardedData
- _os_variant_allows_internal_security_policies
CStrings:
+ "Aggregate produced no row: "
+ "CCDatabaseWriter+Compaction.m"
+ "Compaction: %@: _combineAndCompactRowsForDeviceRowId failed for device %@ %@ range %{public}@: %@"
+ "Compaction: %@: _deleteRecordsForDeviceRowId failed: %@"
+ "Compaction: %@: deferred before processing range %{public}@"
+ "Compaction: %@: deleting run %{public}@ from %@ failed - %@"
+ "Compaction: %@: state sets for %{public}@: %lu eligible, %lu ineligible, highest sequence %lld"
+ "Deferred during "
+ "Deferred mid distribution calculation after %{public}llu %{public}s rows"
+ "Preparing to compute metrics for %{public}ld set(s)"
+ "Reporting metrics for %{public}ld set(s)"
+ "SELECT\n    COALESCE(length(mc.metacontent), 0)\nFROM\n    (SELECT DISTINCT\n        instance_hash\n     FROM\n        metacontent_provenance\n     WHERE\n        (deleted_run_length != 0) = 0\n        AND instance_hash IS NOT NULL) d\nLEFT JOIN\n    metacontent mc ON mc.instance_hash = d.instance_hash"
+ "SELECT\n    c.content\nFROM\n    (SELECT DISTINCT\n        content_hash\n     FROM\n        metacontent_provenance\n     WHERE\n        (deleted_run_length != 0) = 0\n        AND content_hash IS NOT NULL) h\nLEFT JOIN\n    content c ON c.content_hash = h.content_hash"
+ "SELECT\n    c.content\nFROM\n    (SELECT DISTINCT\n        cp.content_hash\n     FROM\n        content_provenance cp\n     WHERE\n        (cp.deleted_run_length != 0) = 0\n        AND cp.content_hash IS NOT NULL\n        AND cp.device_row_id NOT IN (\n            SELECT device_row_id FROM device WHERE (options & 1) != 0 -- CCDeviceRecordOptionsLocal\n        )\n        AND NOT EXISTS (\n            SELECT 1 FROM metacontent_provenance mp\n            WHERE mp.content_hash = cp.content_hash AND (mp.deleted_run_length != 0) = 0\n        )) h\nLEFT JOIN\n    content c ON c.content_hash = h.content_hash"
+ "SELECT\n    cp.content_hash,\n    d.device_uuid,\n    d.ids_device_id,\n    d.device_platform\nFROM\n    content_provenance cp\nJOIN\n    device d ON d.device_row_id = cp.device_row_id\nWHERE\n    (cp.deleted_run_length != 0) = 0\n    AND (d.options & 1) = 0 -- CCDeviceRecordOptionsLocal\nORDER BY\n    cp.content_hash"
+ "Skipping metrics computation as the event: %{public}s is not used."
+ "rowId != NULL"
- "<CCProvenanceStateSets p:%@ d:%@ c:%@>"
- "@16@?0@\"CCProvenanceCompactionRecord\"8"
- "Compaction: %@: _deleteRecordsWithRowIds for content failed: %@"
- "Compaction: %@: _processDeletionForDeviceRowId failed for %@ %@: %@"
- "Compaction: %@: deferred during _processRange"
- "Compaction: %@: deleting rows from %@ fails for rowIds: %@ - %@"
- "Compaction: %@: state sets for %@: %@"
- "Deferred mid distribution calculation for set: %@ after enumerating %lu set changes"
- "Failed to get sizeOfSetInBytes for set: %@ error: %@"
- "Preparing to enumerate and compute metrics for %@ set(s)"
- "Reporting metrics for %@ set(s)"
- "Skipping metrics computation as the event: %@ is not used."
- "com.apple.Cascade"
- "contentCount"
- "sizeInBytes"
- "vector"
```
