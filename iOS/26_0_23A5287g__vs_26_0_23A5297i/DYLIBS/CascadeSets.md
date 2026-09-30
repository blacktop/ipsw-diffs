## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-197.0.0.0.0
-  __TEXT.__text: 0x56168
-  __TEXT.__auth_stubs: 0xd40
+198.0.0.0.0
+  __TEXT.__text: 0x5523c
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x48b4
+  __TEXT.__objc_methlist: 0x4824
   __TEXT.__const: 0x394
-  __TEXT.__gcc_except_tab: 0x10e0
-  __TEXT.__cstring: 0x3ed2
-  __TEXT.__oslogstring: 0x4d14
+  __TEXT.__gcc_except_tab: 0x124c
+  __TEXT.__cstring: 0x3ee2
+  __TEXT.__oslogstring: 0x4ba4
   __TEXT.__dlopen_cstrs: 0x278
   __TEXT.__swift5_typeref: 0x168
   __TEXT.__swift5_fieldmd: 0xd4

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x15e0
+  __TEXT.__unwind_info: 0x15f0
   __TEXT.__eh_frame: 0x2f8
-  __TEXT.__objc_classname: 0xb3f
-  __TEXT.__objc_methname: 0xa50e
-  __TEXT.__objc_methtype: 0x1f7e
-  __TEXT.__objc_stubs: 0x6de0
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__objc_classlist: 0x358
+  __TEXT.__objc_classname: 0xb22
+  __TEXT.__objc_methname: 0xa330
+  __TEXT.__objc_methtype: 0x2053
+  __TEXT.__objc_stubs: 0x6dc0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24d0
+  __DATA_CONST.__objc_selrefs: 0x24a0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6b0
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0xaeb0
-  __AUTH_CONST.__objc_intobj: 0x420
+  __AUTH_CONST.__objc_const: 0xabe8
+  __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH.__objc_data: 0x3e8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x4e0
-  __DATA.__data: 0xcac
+  __DATA.__objc_ivar: 0x4c0
+  __DATA.__data: 0xd6c
   __DATA.__bss: 0x48
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1ef0
+  __DATA_DIRTY.__objc_data: 0x1e00
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2424884B-9FC5-3CD5-8916-1E5D52FD5BFC
-  Functions: 2029
-  Symbols:   6686
-  CStrings:  3411
+  UUID: 7F1C4CF4-DDE5-3FD4-8F42-3F7A0BC7C79E
+  Functions: 2016
+  Symbols:   6638
+  CStrings:  3389
 
Symbols:
+ -[CCDatabaseConnection executeCommand:error:returningRowBlock:]
+ -[CCDatabaseConnection firstResultOfSelect:outNumberValue:error:]
+ -[CCDatabaseEnumerationResult dealloc]
+ -[CCDatabaseEnumerationResult nextRow]
+ -[CCDatabaseReader firstResultOfSelect:outNumberValue:error:]
+ -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.3
+ -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.4
+ -[CCMutableSetChange appendAddedDevices:]
+ -[CCMutableSetChange appendAddedLocalInstances:]
+ -[CCMutableSetChange appendAllDevices:]
+ -[CCMutableSetChange appendAllLocalInstances:]
+ -[CCMutableSetChange appendRemovedDevices:]
+ -[CCMutableSetChange appendRemovedLocalInstances:]
+ -[CCSQLiteDatabase executeCommand:options:error:returningRowBlock:]
+ -[CCSQLiteDatabase lastExtendedErrorCode]
+ -[CCSQLitePreparedStatement columnCount]
+ -[CCSQLitePreparedStatement dataValueAtColumnIndex:]
+ -[CCSQLitePreparedStatement numberValueAtColumnIndex:]
+ -[CCSQLitePreparedStatement stringValueAtColumnIndex:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table17
+ GCC_except_table32
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table60
+ GCC_except_table8
+ _CCDatabaseValueAsData
+ _CCDatabaseValueAsNumber
+ _CCDatabaseValueAsString
+ _OBJC_IVAR_$_CCSQLitePreparedStatement._count
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDatabaseValueRow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDatabaseValueRowEnumerator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDatabaseValueRow
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDatabaseValueRowEnumerator
+ __OBJC_CLASS_PROTOCOLS_$_CCDatabaseEnumerationResult
+ __OBJC_CLASS_PROTOCOLS_$_CCSQLitePreparedStatement
+ __OBJC_LABEL_PROTOCOL_$_CCDatabaseValueRow
+ __OBJC_LABEL_PROTOCOL_$_CCDatabaseValueRowEnumerator
+ __OBJC_PROTOCOL_$_CCDatabaseValueRow
+ __OBJC_PROTOCOL_$_CCDatabaseValueRowEnumerator
+ ___129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke.37
+ ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.10
+ ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.13
+ ___150-[CCDatabaseUpdater _insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:]_block_invoke
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54.cold.1
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54.cold.2
+ ___54-[CCDatabaseUpdater _insertDeviceSite:returningRowId:]_block_invoke
+ ___64-[CCDatabaseUpdater _deleteSourceItemIdHash:outProvenanceRowId:]_block_invoke
+ ___65-[CCDatabaseConnection firstResultOfSelect:outNumberValue:error:]_block_invoke
+ ___96-[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e44_B32?0"NSObject<CCDatabaseRecord>"8^16^B24ls32l8
+ ___block_descriptor_40_e8_32r_e38_v16?0"NSObject<CCDatabaseValueRow>"8lr32l8
+ ___block_descriptor_40_e8_32r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr32l8
+ ___block_descriptor_48_e8_32bs_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lu40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e44_B32?0"NSObject<CCDatabaseRecord>"8^16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e38_v16?0"NSObject<CCDatabaseValueRow>"8lr32l8r40l8r48l8
+ ___block_descriptor_80_e8_32r40r48r56r64r72r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
+ __columnValueFromSQLiteStatement.cold.1
+ _objc_msgSend$appendAddedDevices:
+ _objc_msgSend$appendAddedLocalInstances:
+ _objc_msgSend$appendAllDevices:
+ _objc_msgSend$appendAllLocalInstances:
+ _objc_msgSend$appendRemovedDevices:
+ _objc_msgSend$appendRemovedLocalInstances:
+ _objc_msgSend$columnCount
+ _objc_msgSend$executeCommand:error:returningRowBlock:
+ _objc_msgSend$executeCommand:options:error:returningRowBlock:
+ _objc_msgSend$firstResultOfSelect:outNumberValue:error:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$lastExtendedErrorCode
+ _objc_msgSend$minusSet:
+ _objc_msgSend$nextRow
- +[CCDatabaseEnumerationResult emptyResult]
- -[CCDatabaseConnection _getRowResultsOfSelect:outRows:error:]
- -[CCDatabaseConnection executeCommand:error:returningRow:]
- -[CCDatabaseEnumerationResult _next]
- -[CCDatabaseEnumerationResult column_count]
- -[CCDatabaseEnumerationResult next]
- -[CCDatabaseEnumerationResult peek]
- -[CCDatabaseEnumerationResult peekedNext]
- -[CCDatabaseExecutionResult .cxx_destruct]
- -[CCDatabaseExecutionResult beginMachTime]
- -[CCDatabaseExecutionResult command]
- -[CCDatabaseExecutionResult description]
- -[CCDatabaseExecutionResult endMachTime]
- -[CCDatabaseExecutionResult error]
- -[CCDatabaseExecutionResult initWithCommand:beginMachTime:endMachTime:rowValueTuples:error:]
- -[CCDatabaseExecutionResult init]
- -[CCDatabaseExecutionResult rowValueTuples]
- -[CCDatabaseSetStateReader _enumerateProvenanceRecordsFromCommand:error:usingBlock:]
- -[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]
- -[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:].cold.1
- -[CCDatabaseValueRow .cxx_destruct]
- -[CCDatabaseValueRow count]
- -[CCDatabaseValueRow dataValueAtColumnIndex:]
- -[CCDatabaseValueRow description]
- -[CCDatabaseValueRow initWithDatabaseValueArray:]
- -[CCDatabaseValueRow init]
- -[CCDatabaseValueRow numberValueAtColumnIndex:]
- -[CCDatabaseValueRow stringValueAtColumnIndex:]
- -[CCDatabaseValueRowEnumerator .cxx_destruct]
- -[CCDatabaseValueRowEnumerator enumerationResult]
- -[CCDatabaseValueRowEnumerator error]
- -[CCDatabaseValueRowEnumerator initWithEnumerationResult:]
- -[CCDatabaseValueRowEnumerator next]
- -[CCDatabaseValueRowEnumerator peek]
- -[CCSQLiteDatabase executeCommand:options:]
- GCC_except_table145
- GCC_except_table30
- GCC_except_table35
- GCC_except_table47
- GCC_except_table49
- GCC_except_table53
- GCC_except_table55
- GCC_except_table61
- _OBJC_CLASS_$_CCDatabaseExecutionResult
- _OBJC_CLASS_$_CCDatabaseValueRow
- _OBJC_CLASS_$_CCDatabaseValueRowEnumerator
- _OBJC_IVAR_$_CCDatabaseEnumerationResult._column_count
- _OBJC_IVAR_$_CCDatabaseEnumerationResult._peekedNext
- _OBJC_IVAR_$_CCDatabaseExecutionResult._beginMachTime
- _OBJC_IVAR_$_CCDatabaseExecutionResult._command
- _OBJC_IVAR_$_CCDatabaseExecutionResult._endMachTime
- _OBJC_IVAR_$_CCDatabaseExecutionResult._error
- _OBJC_IVAR_$_CCDatabaseExecutionResult._rowValueTuples
- _OBJC_IVAR_$_CCDatabaseValueRow._databaseValueArray
- _OBJC_IVAR_$_CCDatabaseValueRowEnumerator._enumerationResult
- _OBJC_METACLASS_$_CCDatabaseExecutionResult
- _OBJC_METACLASS_$_CCDatabaseValueRow
- _OBJC_METACLASS_$_CCDatabaseValueRowEnumerator
- __OBJC_$_CLASS_METHODS_CCDatabaseEnumerationResult
- __OBJC_$_INSTANCE_METHODS_CCDatabaseExecutionResult
- __OBJC_$_INSTANCE_METHODS_CCDatabaseValueRow
- __OBJC_$_INSTANCE_METHODS_CCDatabaseValueRowEnumerator
- __OBJC_$_INSTANCE_VARIABLES_CCDatabaseExecutionResult
- __OBJC_$_INSTANCE_VARIABLES_CCDatabaseValueRow
- __OBJC_$_INSTANCE_VARIABLES_CCDatabaseValueRowEnumerator
- __OBJC_$_PROP_LIST_CCDatabaseExecutionResult
- __OBJC_$_PROP_LIST_CCDatabaseValueRowEnumerator
- __OBJC_CLASS_RO_$_CCDatabaseExecutionResult
- __OBJC_CLASS_RO_$_CCDatabaseValueRow
- __OBJC_CLASS_RO_$_CCDatabaseValueRowEnumerator
- __OBJC_METACLASS_RO_$_CCDatabaseExecutionResult
- __OBJC_METACLASS_RO_$_CCDatabaseValueRow
- __OBJC_METACLASS_RO_$_CCDatabaseValueRowEnumerator
- ___102-[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:]_block_invoke
- ___102-[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:]_block_invoke.cold.1
- ___129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke.36
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.9
- ___44-[CCDatabaseSetStateReader sharedItemCount:]_block_invoke
- ___44-[CCDatabaseSetStateReader sharedItemCount:]_block_invoke.cold.1
- ___46-[CCDatabaseSetStateReader itemInstanceCount:]_block_invoke
- ___46-[CCDatabaseSetStateReader itemInstanceCount:]_block_invoke.cold.1
- ___47-[CCDatabaseUpdater _selectLocalInstanceCount:]_block_invoke
- ___47-[CCDatabaseUpdater _selectLocalInstanceCount:]_block_invoke.cold.1
- ___47-[CCDatabaseUpdater _selectLocalInstanceCount:]_block_invoke.cold.2
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53.cold.1
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53.cold.2
- ___77-[CCDatabaseSetStateReader checkForPresentContent:filterByDeviceRowId:error:]_block_invoke
- ___77-[CCDatabaseSetStateReader checkForPresentContent:filterByDeviceRowId:error:]_block_invoke.cold.1
- ___77-[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]_block_invoke
- ___77-[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]_block_invoke.cold.1
- ___83-[CCDatabaseUpdater _selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:]_block_invoke
- ___83-[CCDatabaseUpdater _selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32r_e36_B32?0"CCDatabaseValueRow"8^16^B24lr32l8
- ___block_descriptor_48_e8_32bs_e36_B32?0"CCDatabaseValueRow"8^16^B24lu40l8s32l8
- ___block_descriptor_48_e8_32r40r_e36_B32?0"CCDatabaseValueRow"8^16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40r_e36_B32?0"CCDatabaseValueRow"8^16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e36_B32?0"CCDatabaseValueRow"8^16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e32_v24?0"CCProvenanceRecord"8^B16ls32l8s40l8
- ___block_descriptor_80_e8_32r40r48r56r64r72r_e36_B32?0"CCDatabaseValueRow"8^16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
- __createExecutionResult
- _mach_absolute_time
- _objc_msgSend$_enumerateProvenanceRecordsFromCommand:error:usingBlock:
- _objc_msgSend$_getRowResultsOfSelect:outRows:error:
- _objc_msgSend$_next
- _objc_msgSend$_selectRemoteContentHashPresent:remoteContentPresentPtr:
- _objc_msgSend$array
- _objc_msgSend$executeCommand:error:returningRow:
- _objc_msgSend$executeCommand:options:
- _objc_msgSend$executeCommand:options:error:
- _objc_msgSend$initWithCommand:beginMachTime:endMachTime:rowValueTuples:error:
- _objc_msgSend$initWithDatabaseValueArray:
- _objc_msgSend$initWithEnumerationResult:
- _objc_msgSend$intersectsOrderedSet:
- _objc_msgSend$minusOrderedSet:
- _objc_msgSend$peek
- _objc_msgSend$rowValueTuples
CStrings:
+ "@\"NSData\"24@0:8Q16"
+ "@\"NSError\"16@0:8"
+ "@\"NSNumber\"24@0:8Q16"
+ "@\"NSObject<CCDatabaseValueRow>\"16@0:8"
+ "@\"NSObject<CCDatabaseValueRowEnumerator>\""
+ "@\"NSObject<CCDatabaseValueRowEnumerator>\"32@0:8@\"CCDatabaseSelect\"16^@24"
+ "@\"NSString\"24@0:8Q16"
+ "@24@0:8@\"NSObject<CCDatabaseValueRow>\"16"
+ "B32@?0@\"NSObject<CCDatabaseValueRow>\"8^@16^B24"
+ "B40@0:8@\"CCDatabaseCommand\"16Q24^@32"
+ "B40@0:8@\"CCDatabaseCommand\"16^@24@?<v@?@\"NSObject<CCDatabaseValueRow>\">32"
+ "B40@0:8@\"CCDatabaseSelect\"16^@24@?<B@?@\"NSObject<CCDatabaseValueRow>\"^@^B>32"
+ "B40@0:8@\"CCDatabaseSelect\"16^@24^@32"
+ "B48@0:8@\"CCDatabaseCommand\"16Q24^@32@?<v@?@\"NSObject<CCDatabaseValueRow>\">40"
+ "B48@0:8@16Q24^@32@?40"
+ "Database result has more than a single value: %@"
+ "T@\"NSMutableSet\",R,N,V_addedDevices"
+ "T@\"NSMutableSet\",R,N,V_addedLocalInstances"
+ "T@\"NSMutableSet\",R,N,V_allDevices"
+ "T@\"NSMutableSet\",R,N,V_allLocalInstances"
+ "T@\"NSMutableSet\",R,N,V_removedDevices"
+ "T@\"NSMutableSet\",R,N,V_removedLocalInstances"
+ "appendAddedDevices:"
+ "appendAddedLocalInstances:"
+ "appendAllDevices:"
+ "appendAllLocalInstances:"
+ "appendRemovedDevices:"
+ "appendRemovedLocalInstances:"
+ "columnCount"
+ "executeCommand:error:returningRowBlock:"
+ "executeCommand:options:error:returningRowBlock:"
+ "firstResultOfSelect:outNumberValue:error:"
+ "intersectsSet:"
+ "joinedProvenanceFromDatabaseValueRow could not initialize provenance record from enumerator: %@"
+ "lastExtendedErrorCode"
+ "minusSet:"
+ "nextRow"
+ "v16@?0@\"NSObject<CCDatabaseValueRow>\"8"
+ "value with unknown column type (sqlite_column_index: %@, sqlite_column_type: %@)"
- "%@ {command: %@, beginMachTime: %@, endMachTime: %@, rowValueTuples: %@, error: %@}"
- "@\"CCDatabaseEnumerationResult\""
- "@\"CCDatabaseExecutionResult\"32@0:8@\"CCDatabaseCommand\"16Q24"
- "@\"CCDatabaseValueRowEnumerator\""
- "@\"CCDatabaseValueRowEnumerator\"32@0:8@\"CCDatabaseSelect\"16^@24"
- "@\"NSMutableOrderedSet\""
- "@24@0:8@\"CCDatabaseValueRow\"16"
- "@56@0:8@16Q24Q32@40@48"
- "B32@0:8@16^B24"
- "B32@?0@\"CCDatabaseValueRow\"8^@16^B24"
- "B40@0:8@\"CCDatabaseCommand\"16^@24^@32"
- "B40@0:8@\"CCDatabaseSelect\"16^@24@?<B@?@\"CCDatabaseValueRow\"^@^B>32"
- "CCDatabaseExecutionResult"
- "Counted %@ item records in the database. %@"
- "Expected deviceRowId from select but got unexpected row: %@"
- "Expected sequence number from provenance table select but got unexpected row: %@"
- "Select %@ returned invalid row: %@"
- "Select count returned invalid row: %@, %@"
- "T@\"CCDatabaseEnumerationResult\",R,N,V_enumerationResult"
- "T@\"NSArray\",R,N,V_peekedNext"
- "T@\"NSArray\",R,N,V_rowValueTuples"
- "T@\"NSMutableOrderedSet\",R,N,V_addedDevices"
- "T@\"NSMutableOrderedSet\",R,N,V_addedLocalInstances"
- "T@\"NSMutableOrderedSet\",R,N,V_allDevices"
- "T@\"NSMutableOrderedSet\",R,N,V_allLocalInstances"
- "T@\"NSMutableOrderedSet\",R,N,V_removedDevices"
- "T@\"NSMutableOrderedSet\",R,N,V_removedLocalInstances"
- "TQ,R,N,V_beginMachTime"
- "TQ,R,N,V_endMachTime"
- "Ti,R,N,V_column_count"
- "Unexpected row (%@) returned from content select: %@"
- "Unexpected row (%@) returned from metacontent select: %@"
- "_beginMachTime"
- "_column_count"
- "_databaseValueArray"
- "_endMachTime"
- "_enumerateProvenanceRecordsFromCommand:error:usingBlock:"
- "_enumerationResult"
- "_getRowResultsOfSelect:outRows:error:"
- "_next"
- "_peekedNext"
- "_rowValueTuples"
- "_selectRemoteContentHashPresent:remoteContentPresentPtr:"
- "array"
- "beginMachTime"
- "column_count"
- "emptyResult"
- "endMachTime"
- "enumerationResult"
- "executeCommand:error:returningRow:"
- "executeCommand:options:"
- "initWithCommand:beginMachTime:endMachTime:rowValueTuples:error:"
- "initWithDatabaseValueArray:"
- "initWithEnumerationResult:"
- "intersectsOrderedSet:"
- "joinedProvenanceFromDatabaseValueRow could not initialize provenance record from row: %@"
- "minusOrderedSet:"
- "peek"
- "peekedNext"
- "rowValueTuples"
- "value: %@ with unknown column type (sqlite_column_index: %@, sqlite_column_type: %@)"

```
