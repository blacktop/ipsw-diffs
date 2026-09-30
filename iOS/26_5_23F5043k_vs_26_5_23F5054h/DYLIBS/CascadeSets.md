## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-209.16.0.0.0
-  __TEXT.__text: 0x65004
+209.17.0.1.0
+  __TEXT.__text: 0x64c1c
   __TEXT.__auth_stubs: 0xd00
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x5614
+  __TEXT.__objc_methlist: 0x563c
   __TEXT.__const: 0x3c4
-  __TEXT.__gcc_except_tab: 0x1470
-  __TEXT.__cstring: 0x535c
-  __TEXT.__oslogstring: 0x44b4
+  __TEXT.__gcc_except_tab: 0x1460
+  __TEXT.__cstring: 0x53bc
+  __TEXT.__oslogstring: 0x4374
   __TEXT.__dlopen_cstrs: 0x2ec
   __TEXT.__swift5_typeref: 0x166
   __TEXT.__swift5_fieldmd: 0xd4

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x1930
+  __TEXT.__unwind_info: 0x1940
   __TEXT.__eh_frame: 0x2e8
   __TEXT.__objc_classname: 0xdd1
-  __TEXT.__objc_methname: 0xc99a
-  __TEXT.__objc_methtype: 0x2708
-  __TEXT.__objc_stubs: 0x8420
+  __TEXT.__objc_methname: 0xc96a
+  __TEXT.__objc_methtype: 0x26c8
+  __TEXT.__objc_stubs: 0x8400
   __DATA_CONST.__got: 0x530
-  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__const: 0x17c8
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ab8
+  __DATA_CONST.__objc_selrefs: 0x2ac8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0xc2e0
+  __AUTH_CONST.__cfstring: 0x4720
+  __AUTH_CONST.__objc_const: 0xc330
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x5b4
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0xfb0
   __DATA.__bss: 0x70
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BA08AA2C-75F1-3E6D-B51F-D559FE06DD2E
-  Functions: 2298
-  Symbols:   7589
-  CStrings:  3972
+  UUID: A71A97B1-CB72-3098-952D-56ED41DA2795
+  Functions: 2294
+  Symbols:   7574
+  CStrings:  3973
 
Symbols:
+ -[CCDatabaseDeviceClockValues compacted]
+ -[CCDatabaseDeviceClockValues initWithDeviceRowId:missingAtomsImplied:trackCompactedAtoms:]
+ -[CCDatabaseSetChangeEnumerator _verifyTombstonesFromDeltaRemovalsVector:withStateVectorType:areNotCompactedInDatabase:error:]
+ -[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:]
+ -[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]
+ -[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:].cold.1
+ -[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:].cold.2
+ -[CCDatabaseSetStateVectorBuilder _getOrCreateClockValuesForDeviceRowId:]
+ -[CCDatabaseSetStateVectorBuilder addProvenanceRow:]
+ -[CCDatabaseSetStateVectorBuilder compactedAtomsForDeviceRowId:]
+ -[CCDatabaseSetStateVectorBuilder initWithDeviceMapping:missingAtomsImplied:trackCompactedAtoms:]
+ _OBJC_IVAR_$_CCDatabaseDeviceClockValues._compacted
+ _OBJC_IVAR_$_CCDatabaseSetStateVectorBuilder._lastDeviceClockValues
+ _OBJC_IVAR_$_CCDatabaseSetStateVectorBuilder._trackCompactedAtoms
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke.10
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke.18
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke.cold.1
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke_2
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke_3
+ ___107-[CCDatabaseSetStateReader enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:]_block_invoke_4
+ ___126-[CCDatabaseSetChangeEnumerator _verifyTombstonesFromDeltaRemovalsVector:withStateVectorType:areNotCompactedInDatabase:error:]_block_invoke
+ ___141-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:]_block_invoke
+ ___141-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"CCContentProvenanceRecord"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e30_v40?0{_NSRange=QQ}8C24C28^B32ls32l8r40l8
+ _objc_msgSend$_getOrCreateClockValuesForDeviceRowId:
+ _objc_msgSend$_verifyTombstonesFromDeltaRemovalsVector:withStateVectorType:areNotCompactedInDatabase:error:
+ _objc_msgSend$addProvenanceRow:
+ _objc_msgSend$compacted
+ _objc_msgSend$compactedAtomsForDeviceRowId:
+ _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:
+ _objc_msgSend$initWithDeviceMapping:missingAtomsImplied:trackCompactedAtoms:
+ _objc_msgSend$initWithDeviceRowId:missingAtomsImplied:trackCompactedAtoms:
- -[CCDatabaseDeviceClockValues initWithDeviceRowId:missingAtomsImplied:]
- -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.17
- -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.18
- -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.19
- -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.20
- -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]
- -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:].cold.1
- -[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
- -[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:].cold.1
- -[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]
- -[CCDatabaseSetStateReader enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
- -[CCDatabaseSetStateReader enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
- -[CCDatabaseSetStateVectorBuilder initWithDeviceMapping:missingAtomsImplied:]
- GCC_except_table20
- _OBJC_IVAR_$_CCDatabaseSetStateVectorBuilder._deviceClockValues
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- ___111-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]_block_invoke
- ___111-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]_block_invoke_2
- ___113-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]_block_invoke
- ___113-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]_block_invoke_2
- ___147-[CCDatabaseSetStateReader enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
- ___151-[CCDatabaseSetStateReader enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
- ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
- ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.12
- ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_2
- ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_3
- ___48-[CCDatabaseSetChangeEnumerator _imputeChanges:]_block_invoke.48
- ___48-[CCDatabaseSetChangeEnumerator _imputeChanges:]_block_invoke.50
- ___block_descriptor_40_e8_32bs_e42_v24?0"NSObject<CCProvenanceRecord>"8^B16ls32l8
- ___block_descriptor_40_e8_32r_e39_v24?0"CCContentProvenanceRecord"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e43_v24?0"CCMetaContentProvenanceRecord"8^B16lr32l8
- ___block_descriptor_41_e8_32s_e24_v32?0{_NSRange=QQ}8^B24ls32l8
- ___block_descriptor_41_e8_32s_e44_v32?0"NSNumber"8"NSMutableIndexSet"16^B24ls32l8
- ___block_descriptor_49_e8_32s40bs_e42_v24?0"NSObject<CCProvenanceRecord>"8^B16ls32l8s40l8
- ___block_descriptor_50_e8_32s40r_e30_v40?0{_NSRange=QQ}8C24C28^B32ls32l8r40l8
- _objc_msgSend$_createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:
- _objc_msgSend$_enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
- _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:
- _objc_msgSend$criterionWithColumnName:GREATERTHANColumnValue:
- _objc_msgSend$criterionWithColumnName:LESSTHANOrEqualColumnValue:
- _objc_msgSend$enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
- _objc_msgSend$enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
- _objc_msgSend$initWithDeviceMapping:missingAtomsImplied:
- _objc_msgSend$initWithDeviceRowId:missingAtomsImplied:
CStrings:
+ "%@ Bookmark is invalid and cannot be resumed from as it is too old and tombstones have been cleaned up (%@:%@:%@)"
+ "%@ Failed to construct content and metacontent state vectors from database"
+ "@32@0:8@16B24B28"
+ "B44@0:8@16C24@28^@36"
+ "Enumerating clock value (%@) which is in state %u when expecting to enumerate present clock values"
+ "No present clock values found in state vector: %@"
+ "T@\"NSMutableIndexSet\",R,N,V_compacted"
+ "_compacted"
+ "_getOrCreateClockValuesForDeviceRowId:"
+ "_lastDeviceClockValues"
+ "_trackCompactedAtoms"
+ "_verifyTombstonesFromDeltaRemovalsVector:withStateVectorType:areNotCompactedInDatabase:error:"
+ "addProvenanceRow:"
+ "compacted"
+ "compactedAtomsForDeviceRowId:"
+ "constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:"
+ "enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:"
+ "initWithDeviceMapping:missingAtomsImplied:trackCompactedAtoms:"
+ "initWithDeviceRowId:missingAtomsImplied:trackCompactedAtoms:"
- "@44@0:8@16#24C32@36"
- "B48@0:8@16^@24^@32^@40"
- "B56@0:8@16C24C28@32^@40@?48"
- "B64@0:8@16#24C32C36@40^@48@?56"
- "Bookmark is invalid and cannot be resumed from as it is too old and tombstones have been cleaned up"
- "Enumerating clock value (%lu - %lu) which is in state %u when expecting to enumerate clock values in state %u"
- "Failed to construct content and metacontent state vectors from database: %@"
- "Failed to enumerate provenance rows for tombstoned content: %@"
- "Failed to enumerate provenance rows for tombstoned metacontent: %@"
- "No clock values found with state %u in state vector: %@"
- "_createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:"
- "_deviceClockValues"
- "_enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
- "constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:"
- "enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
- "enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
- "initWithDeviceMapping:missingAtomsImplied:"
- "initWithDeviceRowId:missingAtomsImplied:"
- "v24@?0@\"CCMetaContentProvenanceRecord\"8^B16"
- "v24@?0@\"NSObject<CCProvenanceRecord>\"8^B16"

```
