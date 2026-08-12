## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-247.0.1.0.0
-  __TEXT.__text: 0xa7868
-  __TEXT.__objc_methlist: 0x6534
-  __TEXT.__const: 0x3c98
-  __TEXT.__gcc_except_tab: 0x1840
-  __TEXT.__cstring: 0x8997
-  __TEXT.__oslogstring: 0x4dd0
-  __TEXT.__dlopen_cstrs: 0x37a
+250.0.0.1.0
+  __TEXT.__text: 0xa9f90
+  __TEXT.__objc_methlist: 0x669c
+  __TEXT.__const: 0x3cc8
+  __TEXT.__gcc_except_tab: 0x18bc
+  __TEXT.__cstring: 0x8d37
+  __TEXT.__oslogstring: 0x5400
+  __TEXT.__dlopen_cstrs: 0x3d8
   __TEXT.__swift5_typeref: 0xe33
   __TEXT.__constg_swiftt: 0x16bc
   __TEXT.__swift5_reflstr: 0x1354

   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_mpenum: 0xd0
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x31a0
+  __TEXT.__unwind_info: 0x3220
   __TEXT.__eh_frame: 0x2970
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c40
-  __DATA_CONST.__objc_classlist: 0x4f8
+  __DATA_CONST.__const: 0x1ca8
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3188
+  __DATA_CONST.__objc_selrefs: 0x3270
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0x6c8
-  __AUTH_CONST.__const: 0x38c8
-  __AUTH_CONST.__cfstring: 0x5b00
-  __AUTH_CONST.__objc_const: 0x12168
+  __DATA_CONST.__got: 0x6d8
+  __AUTH_CONST.__const: 0x38e8
+  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__objc_const: 0x12428
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xd28
-  __AUTH.__objc_data: 0x1188
+  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH.__objc_data: 0x1278
   __AUTH.__data: 0x6d0
-  __DATA.__objc_ivar: 0x680
+  __DATA.__objc_ivar: 0x694
   __DATA.__data: 0x1a10
-  __DATA.__bss: 0x1d10
+  __DATA.__bss: 0x1d40
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x1890
   __DATA_DIRTY.__data: 0x13f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4558
-  Symbols:   6284
-  CStrings:  1285
+  Functions: 4613
+  Symbols:   6382
+  CStrings:  1324
 
Symbols:
+ +[CCCachedDocumentUtilities _documentCachePredicateFromAssociatedSetKeyPrefixedIdentifier:documentCacheSet:error:]
+ +[CCCachedDocumentUtilities documentCachePredicateFromAssociatedSetPredicate:documentCacheSet:error:]
+ +[CCDatabaseWriter(CorruptionRecovery) isInternalOrSeedBuild]
+ +[CCItemDeletedFieldTypes deletedFieldTypesByUnioning:with:]
+ +[CCItemDeletedFieldTypes deletedFieldTypesWithPackedData:error:]
+ +[CCItemDeletedFieldTypes empty]
+ +[CCItemMutableDeletedFieldTypes builder]
+ +[CCSpaceAttribution registerAttributions:]
+ -[CCDataResourceReadAccess enumerateReadableDataResourcesWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:]
+ -[CCDatabaseConnection beginWriteTransactionReturningToken:error:]
+ -[CCDatabaseConnection commitTransactionWithToken:error:]
+ -[CCDatabaseConnection rollbackTransactionWithToken:error:]
+ -[CCDatabaseWriter _tombstoneExpiredItemInstances:error:]
+ -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:error:]
+ -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:]
+ -[CCDatabaseWriter(CorruptionRecovery) _checkLocalSequenceCounterRegressionForKey:derivedHighWater:outCorruptionDetected:error:]
+ -[CCDonationServicePriors description]
+ -[CCItemDeletedFieldTypes _initEmpty]
+ -[CCItemDeletedFieldTypes containsFieldType:]
+ -[CCItemDeletedFieldTypes count]
+ -[CCItemDeletedFieldTypes dealloc]
+ -[CCItemDeletedFieldTypes immutableCopy]
+ -[CCItemDeletedFieldTypes isEmpty]
+ -[CCItemDeletedFieldTypes packedData]
+ -[CCItemMessage _deletedFieldTypesForMergeUnderParent:]
+ -[CCItemMessage copyApplyingPatch:deletedFieldTypes:error:]
+ -[CCItemMutableDeletedFieldTypes addFieldType:]
+ -[CCItemMutableDeletedFieldTypes immutableCopy]
+ -[CCItemMutableDeletedFieldTypes removeFieldType:]
+ -[CCItemMutableDeletedFieldTypes unionDeletedFieldTypes:]
+ -[CCProvenanceStateSets hasDuplicateSequenceNumbers]
+ -[CCProvenanceStateSets highestSequenceNumber]
+ -[CCProvenanceStateSets initWithIneligibleSequences:eligibleSequences:compactedSequences:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:]
+ -[CCProvenanceStateSets scanComplete]
+ -[CCSetDistribution initWithSet:sizeInBytes:]
+ OBJC_IVAR_$_CCItemDeletedFieldTypes._set
+ _CCDatabaseErrorIsLogicalCorruption
+ _CCDatabaseErrorIsSQLiteCorruption
+ _CCDatabaseLogicalCorruptionError
+ _CCDatabaseTransactionTokenNone
+ _CFRelease
+ _CFSetAddValue
+ _CFSetApplyFunction
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _CFSetGetCount
+ _CFSetRemoveValue
+ _OBJC_CLASS_$_CCItemDeletedFieldTypes
+ _OBJC_CLASS_$_CCItemMutableDeletedFieldTypes
+ _OBJC_CLASS_$_CCSpaceAttribution
+ _OBJC_IVAR_$_CCDatabaseConnection._transactionToken
+ _OBJC_IVAR_$_CCDatabaseWriter._transactionToken
+ _OBJC_IVAR_$_CCProvenanceStateSets._hasDuplicateSequenceNumbers
+ _OBJC_IVAR_$_CCProvenanceStateSets._highestSequenceNumber
+ _OBJC_IVAR_$_CCProvenanceStateSets._scanComplete
+ _OBJC_METACLASS_$_CCItemDeletedFieldTypes
+ _OBJC_METACLASS_$_CCItemMutableDeletedFieldTypes
+ _OBJC_METACLASS_$_CCSpaceAttribution
+ _SpaceAttributionLibrary
+ _SpaceAttributionLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_CCDatabaseWriter(Compaction|CorruptionRecovery)
+ __OBJC_$_CLASS_METHODS_CCItemDeletedFieldTypes
+ __OBJC_$_CLASS_METHODS_CCItemMutableDeletedFieldTypes
+ __OBJC_$_CLASS_METHODS_CCSpaceAttribution
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseWriter(Compaction|CorruptionRecovery)
+ __OBJC_$_INSTANCE_METHODS_CCItemDeletedFieldTypes
+ __OBJC_$_INSTANCE_METHODS_CCItemMutableDeletedFieldTypes
+ __OBJC_$_INSTANCE_VARIABLES_CCItemDeletedFieldTypes
+ __OBJC_$_PROP_LIST_CCItemDeletedFieldTypes
+ __OBJC_CLASS_RO_$_CCItemDeletedFieldTypes
+ __OBJC_CLASS_RO_$_CCItemMutableDeletedFieldTypes
+ __OBJC_CLASS_RO_$_CCSpaceAttribution
+ __OBJC_METACLASS_RO_$_CCItemDeletedFieldTypes
+ __OBJC_METACLASS_RO_$_CCItemMutableDeletedFieldTypes
+ __OBJC_METACLASS_RO_$_CCSpaceAttribution
+ ___140-[CCDataResourceReadAccess enumerateReadableDataResourcesWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:]_block_invoke
+ ___141-[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:]_block_invoke
+ ___187-[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:error:]_block_invoke
+ ___32+[CCItemDeletedFieldTypes empty]_block_invoke
+ ___43+[CCSpaceAttribution registerAttributions:]_block_invoke
+ ___43+[CCSpaceAttribution registerAttributions:]_block_invoke_2
+ ___SpaceAttributionLibraryCore_block_invoke
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80bs88r96r104r112r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r88l8s80l8r96l8r104l8s48l8r112l8s56l8s64l8s72l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s_e32_v32?0"NSURL"8"NSString"16^B24lu40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e28_v24?0"CCDataResource"8^B16ls32l8r40l8r48l8
+ ___block_descriptor_84_e8_32s40s48bs56r64r72r_e28_v24?0"CCDataResource"8^B16ls32l8r56l8s48l8r64l8s40l8r72l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72r80r_e18_B16?0"NSNumber"8ls48l8r56l8s32l8s40l8r64l8r72l8r80l8
+ ___getSAPathInfoClass_block_invoke
+ ___getSAPathManagerClass_block_invoke
+ __appendFieldTypeToBuffer
+ __copyValueIntoSet
+ _arc4random_buf
+ _audit_stringSpaceAttribution
+ _empty.once
+ _empty.sEmpty
+ _getSAPathInfoClass.softClass
+ _getSAPathManagerClass.softClass
+ _kCFAllocatorDefault
+ _objc_msgSend$_checkLocalSequenceCounterRegressionForKey:derivedHighWater:outCorruptionDetected:error:
+ _objc_msgSend$_compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:error:
+ _objc_msgSend$_deletedFieldTypesForMergeUnderParent:
+ _objc_msgSend$_documentCachePredicateFromAssociatedSetKeyPrefixedIdentifier:documentCacheSet:error:
+ _objc_msgSend$_initEmpty
+ _objc_msgSend$_tombstoneExpiredItemInstances:error:
+ _objc_msgSend$_updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:skippedEmptyRun:error:
+ _objc_msgSend$beginWriteTransactionReturningToken:error:
+ _objc_msgSend$boolForEntitlement:
+ _objc_msgSend$commitTransactionWithToken:error:
+ _objc_msgSend$copyApplyingPatch:error:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$deletedFieldTypesByUnioning:with:
+ _objc_msgSend$empty
+ _objc_msgSend$enumerateReadableDataResourcesWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:
+ _objc_msgSend$hasDuplicateSequenceNumbers
+ _objc_msgSend$highestSequenceNumber
+ _objc_msgSend$immutableCopy
+ _objc_msgSend$initWithIneligibleSequences:eligibleSequences:compactedSequences:highestSequenceNumber:scanComplete:hasDuplicateSequenceNumbers:
+ _objc_msgSend$initWithSet:sizeInBytes:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isInternalOrSeedBuild
+ _objc_msgSend$localDeviceRecord
+ _objc_msgSend$packedData
+ _objc_msgSend$predicateForAssociatedInstanceUUID:error:
+ _objc_msgSend$registerAttributions:
+ _objc_msgSend$registerPaths:completionHandler:
+ _objc_msgSend$rollbackTransactionWithToken:error:
+ _objc_msgSend$scanComplete
+ _objc_msgSend$setBundleID:
- +[CCCachedDocumentUtilities documentCachePredicateFromAssociatedSetPredicate:error:]
- +[CCDataResource enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:]
- +[CCItemInstancePatch unpackDeletedFieldTypes:usingBlock:]
- -[CCDatabaseConnection beginWriteTransactionWithError:]
- -[CCDatabaseWriter dealloc]
- -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]
- -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:]
- -[CCProvenanceStateSets initWithIneligibleSequences:eligibleSequences:compactedSequences:]
- -[CCSetDistribution initWithSet:sharedItemCount:localInstanceCount:sizeInBytes:]
- GCC_except_table16
- GCC_except_table27
- GCC_except_table31
- _OBJC_IVAR_$_CCDatabaseWriter._finalized
- __OBJC_$_CLASS_METHODS_CCDatabaseWriter
- __OBJC_$_CLASS_METHODS_CCItemInstancePatch
- __OBJC_$_INSTANCE_METHODS_CCDatabaseWriter(Compaction)
- __ZNSt3__16vectorIjNS_9allocatorIjEEE7reserveEm
- ___115+[CCDataResource enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:]_block_invoke
- ___124-[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]_block_invoke
- ___125-[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:]_block_invoke
- ___126+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:discoverableOnly:startAfterSet:sorted:usingBlock:]_block_invoke_3
- ___126+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:discoverableOnly:startAfterSet:sorted:usingBlock:]_block_invoke_4
- ___block_descriptor_56_e8_32bs40r48r_e19_v24?0"CCSet"8^B16ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40bs48r56r64r_e18_B16?0"NSNumber"8ls40l8r48l8r56l8s32l8r64l8
- ___block_descriptor_76_e8_32s40s48bs56r64r_e28_v24?0"CCDataResource"8^B16ls32l8r56l8s48l8r64l8s40l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r80l8s72l8s48l8s56l8s64l8
- _objc_msgSend$_compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:
- _objc_msgSend$_updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:
- _objc_msgSend$enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:
- _objc_msgSend$initWithIneligibleSequences:eligibleSequences:compactedSequences:
- _objc_msgSend$initWithSet:sharedItemCount:localInstanceCount:sizeInBytes:
- _objc_msgSend$rollbackUpdate:
CStrings:
+ "; set will be deleted"
+ "<CCDonationServicePriors v:%llu d:%@ fd:%@ rt:%@ rg:%@ o:%hu>"
+ "Attempted to commit a transaction opened by a different writer: %llu != %llu"
+ "CCDatabaseConnection.m"
+ "CCItemDeletedFieldTypes: packed data length %lu is not a multiple of sizeof(CCFieldType)"
+ "CCItemDeletedFieldTypes: packedData must be NSData, got %@"
+ "CCSetDonationRequestListener refusing connection from %{public}@(%d), process not properly entitled"
+ "CCSpaceAttribution.m"
+ "CCSpaceAttribution: attempting to register %lu attributions"
+ "CCSpaceAttribution: failed to register %lu path(s): %{private}@"
+ "CCSpaceAttribution: registered %lu path(s) successfully"
+ "Cannot translate associated-set keyPrefixedIdentifier (identifier type %u) into a DocumentCache predicate: %@"
+ "Class getSAPathInfoClass(void)_block_invoke"
+ "Class getSAPathManagerClass(void)_block_invoke"
+ "Compaction: %@: no rows for claimed run %@ in %@%{public}s. rdar://182604090."
+ "Denied read access to set: %@ error: %@"
+ "Detected %{public}@ regression for set %{public}@: persisted %lld below derived high-water %lld. rdar://182750141."
+ "Found duplicate content sequence number(s) for set %{public}@%{public}s. rdar://182750141."
+ "Found duplicate metacontent sequence number(s) for set %{public}@%{public}s. rdar://181440946."
+ "Refusing rollback from a non-owner while another writer's transaction is active: %llu != %llu"
+ "SAPathInfo"
+ "SAPathManager"
+ "Set enumeration found no directory on disk for set identifier %{public}@ in container %{public}@"
+ "Set enumeration halting on unexpected access error for entitled resource: %@ error: %@"
+ "Set enumeration halting on unexpected discovery error for resource: %@ error: %@"
+ "Set enumeration in container %{public}@ excluded %lu existing on-disk set resource(s) (%lu missing database file, %lu undiscoverable)"
+ "Set enumeration skipping resource that is absent on disk: %@ for access error: %@"
+ "Set enumeration skipping resource with no database file on disk: %@ (%@)"
+ "Set enumeration skipping undiscoverable resource: %@ (%@)"
+ "com.apple.private.cascade.donation-requester"
+ "commitTransactionWithError: called on a connection with an active owned write transaction — use commitTransactionWithToken:error:. rdar://181440946"
+ "compaction run with no backing rows"
+ "content counter below derived high-water"
+ "duplicate content sequence numbers"
+ "duplicate metacontent sequence numbers"
+ "logical database corruption"
+ "metacontent counter below derived high-water"
+ "outToken != NULL"
+ "rollbackTransactionWithError: called on a connection with an active owned write transaction — use rollbackTransactionWithToken:error:. rdar://181440946"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution"
+ "v32@?0@\"NSURL\"8@\"NSString\"16^B24"
+ "void *SpaceAttributionLibrary(void)"
- "%@: Automatically rolling back update"
- "%@: Failed to rollback update: %@"
- "Set enumeration skipping resource: %@ for access error: %@"
```
