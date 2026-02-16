## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-200.6.0.0.0
-  __TEXT.__text: 0x558c0
-  __TEXT.__auth_stubs: 0xd30
+209.12.1.0.0
+  __TEXT.__text: 0x65024
+  __TEXT.__auth_stubs: 0xd00
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x486c
-  __TEXT.__const: 0x3b4
-  __TEXT.__gcc_except_tab: 0x1278
-  __TEXT.__cstring: 0x3f82
-  __TEXT.__oslogstring: 0x4ba4
-  __TEXT.__dlopen_cstrs: 0x278
-  __TEXT.__swift5_typeref: 0x168
+  __TEXT.__objc_methlist: 0x5614
+  __TEXT.__const: 0x3c4
+  __TEXT.__gcc_except_tab: 0x1470
+  __TEXT.__cstring: 0x535c
+  __TEXT.__oslogstring: 0x44b4
+  __TEXT.__dlopen_cstrs: 0x2ec
+  __TEXT.__swift5_typeref: 0x166
   __TEXT.__swift5_fieldmd: 0xd4
   __TEXT.__constg_swiftt: 0x15c
   __TEXT.__swift5_reflstr: 0x40

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x1608
-  __TEXT.__eh_frame: 0x2f8
-  __TEXT.__objc_classname: 0xb20
-  __TEXT.__objc_methname: 0xa3c5
-  __TEXT.__objc_methtype: 0x20b5
-  __TEXT.__objc_stubs: 0x6dc0
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x13c8
-  __DATA_CONST.__objc_classlist: 0x340
+  __TEXT.__unwind_info: 0x1938
+  __TEXT.__eh_frame: 0x308
+  __TEXT.__objc_classname: 0xdd1
+  __TEXT.__objc_methname: 0xc9aa
+  __TEXT.__objc_methtype: 0x2708
+  __TEXT.__objc_stubs: 0x8420
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24a0
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x6b0
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0xac08
-  __AUTH_CONST.__objc_intobj: 0x408
+  __DATA_CONST.__objc_selrefs: 0x2ab8
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_arraydata: 0x140
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__const: 0x5e8
+  __AUTH_CONST.__cfstring: 0x46e0
+  __AUTH_CONST.__objc_const: 0xc2e0
+  __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x7d0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0xd70
-  __DATA.__bss: 0x48
+  __DATA.__objc_ivar: 0x5b4
+  __DATA.__data: 0xfb0
+  __DATA.__bss: 0x70
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1a18
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x17e8
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1F8AD64B-D789-311F-B4A0-3DB2E2DBAA49
-  Functions: 2030
-  Symbols:   6657
-  CStrings:  3392
+  UUID: CE58D06B-8F2A-347C-B746-E50F0A64F0CF
+  Functions: 2299
+  Symbols:   7591
+  CStrings:  3972
 
Symbols:
+ +[CCCachedDocumentUtilities _validateItemCacheContent:error:]
+ +[CCCachedDocumentUtilities cacheDescriptorsFromAssociatedSet:error:]
+ +[CCCachedDocumentUtilities cacheRetrieverForAssociatedSet:withUseCase:error:]
+ +[CCCachedDocumentUtilities documentCachePredicateFromAssociatedSetPredicate:error:]
+ +[CCCachedDocumentUtilities documentCacheSetIdentifier]
+ +[CCCachedDocumentUtilities hashFromCacheContent:error:]
+ +[CCCachedDocumentUtilities htmlFromCacheContent:error:]
+ +[CCCachedDocumentUtilities isCacheEnabledAssociatedSet:]
+ +[CCCachedDocumentUtilities isCacheEnabledSourceIdentifier:]
+ +[CCCachedDocumentUtilities isDocumentCacheSet:]
+ +[CCCachedDocumentUtilities itemCacheContentWithText:html:error:]
+ +[CCCachedDocumentUtilities joinDonatedDocumentCacheContents:withAssociatedItemContents:associatedItemMetaContents:associatedSet:outContents:outMetaContents:error:]
+ +[CCCachedDocumentUtilities predicateForAssociatedInstanceUUID:error:]
+ +[CCCachedDocumentUtilities predicateForAssociatedSourceItemIdentifier:error:]
+ +[CCCachedDocumentUtilities predicateForCacheContentHash:error:]
+ +[CCCachedDocumentUtilities retrieveCacheContentWithPredicate:retriever:error:]
+ +[CCCachedDocumentUtilities textFromCacheContent:error:]
+ +[CCCachedDocumentUtilities validateItemCacheContent:error:]
+ +[CCContentProvenanceRecord genSQLCreateStatements]
+ +[CCContentProvenanceRecord recordFromDatabaseValueRow:]
+ +[CCContentProvenanceRecord tableName]
+ +[CCDataResource enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:]
+ +[CCDatabaseConnection connectionToDatabaseAtURL:dataProtectionClass:openMode:busyTimeout:accessAssertion:]
+ +[CCDatabaseItemFieldIndexer descriptorAllowList:allowsSet:]
+ +[CCDatabaseItemFieldIndexer indexerFromConfiguration:forBlobTable:set:]
+ +[CCDatabaseItemFieldIndexer isFieldType:applicableToBlobTable:]
+ +[CCDatabaseItemRetriever itemRetrieverForSet:database:]
+ +[CCDatabaseItemRetriever itemRetrieverForSet:database:setConfiguration:contentIndexer:metaContentIndexer:]
+ +[CCDatabaseWriter beginUpdateForDonationRequest:withDatabase:changeNotifier:error:]
+ +[CCDatabaseWriter beginUpdateForMaintenanceOfSet:withDatabase:changeNotifier:error:]
+ +[CCDatabaseWriter beginUpdateForPreparationOfSet:withDatabase:error:]
+ +[CCDonationServicePriors supportsSecureCoding]
+ +[CCDonationXPCClient errorDomain]
+ +[CCDonationXPCClient interruptionErrorCode]
+ +[CCDonationXPCClient invalidationErrorCode]
+ +[CCItemFieldPredicate predicateWithFieldType:equalsDataValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:equalsNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:equalsStringValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:greaterThanNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:greaterThanOrEqualToNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:lessThanNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithFieldType:lessThanOrEqualToNumberValue:error:]
+ +[CCItemFieldPredicate predicateWithItemInstanceIdentifier:error:]
+ +[CCItemFieldPredicate predicateWithKeyPrefixedIdentifier:error:]
+ +[CCItemFieldPredicate predicateWithSharedItemIdentifier:error:]
+ +[CCItemFieldPredicate predicateWithSourceItemIdentifier:error:]
+ +[CCItemFieldPredicate supportsSecureCoding]
+ +[CCItemMessage lazilyDecodedContentMessageForItemType:trustedItemMessageData:error:]
+ +[CCItemMessage lazilyDecodedMetaContentMessageForItemType:trustedItemMessageData:error:]
+ +[CCMaintenenaceXPCClient clientWithId:]
+ +[CCMaintenenaceXPCClient errorDomain]
+ +[CCMaintenenaceXPCClient interruptionErrorCode]
+ +[CCMaintenenaceXPCClient invalidationErrorCode]
+ +[CCMetaContentProvenanceRecord genSQLCreateStatements]
+ +[CCMetaContentProvenanceRecord recordFromDatabaseValueRow:]
+ +[CCMetaContentProvenanceRecord tableName]
+ +[CCSQLCommandCriterion criterionWithColumnName:GREATERTHANColumnValue:]
+ +[CCSQLCommandCriterion criterionWithColumnName:sqlOperator:columnValue:]
+ +[CCSQLCommandGenerator _produceSelectClauseWithTableName:columnNames:count:distinct:]
+ +[CCSQLCommandGenerator dropTableIfExistsWithName:]
+ +[CCSQLCommandGenerator selectFromTableWithName:columns:count:distinct:joinTables:criterion:order:limit:offset:ctes:unionSelects:unionAll:]
+ +[CCSet itemIdentifierComponentOfKeyPrefixedIdentifier:error:]
+ +[CCSet keyComponentOfKeyPrefixedIdentifier:error:]
+ +[CCSetChangeXPCClient clientWithId:]
+ +[CCSetChangeXPCClient errorDomain]
+ +[CCSetChangeXPCClient interruptionErrorCode]
+ +[CCSetChangeXPCClient invalidationErrorCode]
+ +[CCSetDonation _defaultXPCClientFactory]
+ +[CCSetDonation _defaultXPCClientFactory].cold.1
+ +[CCSetDonation _deleteSetWithItemType:descriptors:serviceProvider:error:]
+ +[CCSetDonation _fullSetDonationWithItemType:descriptors:options:serviceProvider:error:]
+ +[CCSetDonation _incrementalSetDonationWithItemType:descriptors:options:serviceProvider:error:]
+ +[CCSetDonation _incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:error:]
+ +[CCSetDonation _remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:error:]
+ +[CCSetDonation _setDonationWithItemType:descriptors:version:validity:serviceOptions:serviceProvider:error:]
+ +[CCSetDonation deleteSetWithItemType:descriptors:error:]
+ +[CCSetDonation deleteSetWithItemType:error:]
+ +[CCSetDonation donationWithName:itemType:service:serviceOptions:errorCode:priors:]
+ +[CCSetDonation startFullSetDonationWithItemType:descriptors:error:]
+ +[CCSetDonation startFullSetDonationWithItemType:descriptors:options:error:]
+ +[CCSetDonation startFullSetDonationWithItemType:error:]
+ +[CCSetDonation startIncrementalSetDonationWithItemType:descriptors:error:]
+ +[CCSetDonation startIncrementalSetDonationWithItemType:descriptors:options:error:]
+ +[CCSetDonation startIncrementalSetDonationWithItemType:descriptors:version:validity:error:]
+ +[CCSetDonation startIncrementalSetDonationWithItemType:error:]
+ +[CCSetDonation(Deprecations) deleteSetWithItemType:completion:]
+ +[CCSetDonation(Deprecations) deleteSetWithItemType:descriptors:completion:]
+ +[CCSetDonation(Deprecations) fullSetDonationWithItemType:completion:]
+ +[CCSetDonation(Deprecations) fullSetDonationWithItemType:descriptors:completion:]
+ +[CCSetDonation(Deprecations) fullSetDonationWithItemType:descriptors:error:]
+ +[CCSetDonation(Deprecations) fullSetDonationWithItemType:descriptors:options:error:]
+ +[CCSetDonation(Deprecations) fullSetDonationWithItemType:error:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:completion:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:completion:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:error:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:options:error:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:version:validity:completion:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:version:validity:error:]
+ +[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:error:]
+ +[CCSetDonation(DocumentCache) isCacheEnabledSourceIdentifier:]
+ +[CCSetDonation(DocumentCache) itemCacheContentWithText:html:error:]
+ +[CCSetDonation(ServiceProviderDeprecations) fullSetDonationWithItemType:descriptors:serviceProvider:completion:]
+ +[CCSetDonation(ServiceProviderDeprecations) incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:completion:]
+ +[CCSetItemRetriever itemRetrieverForSet:readAccess:]
+ +[CCSetItemRetriever itemRetrieverForSet:useCase:]
+ +[CCSetStoreAdminXPCClient errorDomain]
+ +[CCSetStoreAdminXPCClient interruptionErrorCode]
+ +[CCSetStoreAdminXPCClient invalidationErrorCode]
+ +[CCTypeIdentifierRegistryBase isSourceItemIdentifierFieldType:]
+ +[CCXPCClient errorDomain]
+ +[CCXPCClient interruptionErrorCode]
+ +[CCXPCClient invalidationErrorCode]
+ -[CCContentProvenanceRecord .cxx_destruct]
+ -[CCContentProvenanceRecord contentHash]
+ -[CCContentProvenanceRecord deletedDate]
+ -[CCContentProvenanceRecord deletedRunLength]
+ -[CCContentProvenanceRecord description]
+ -[CCContentProvenanceRecord deviceRowId]
+ -[CCContentProvenanceRecord hash]
+ -[CCContentProvenanceRecord initWithDatabaseValueRow:]
+ -[CCContentProvenanceRecord init]
+ -[CCContentProvenanceRecord isEqual:]
+ -[CCContentProvenanceRecord isEqualToRecord:]
+ -[CCContentProvenanceRecord sequenceNumber]
+ -[CCDataResource protectionClass]
+ -[CCDataResource protectionClass].cold.1
+ -[CCDataResource protectionClass].cold.2
+ -[CCDataResource tombstoneResource:]
+ -[CCDataResourceReadAccess _currentPersonaShouldSkipEnumeratingContainer:]
+ -[CCDataResourceReadAccess _currentPersonaShouldSkipEnumeratingContainer:].cold.1
+ -[CCDataResourceReadAccess _currentPersonaShouldSkipEnumeratingResource:]
+ -[CCDataResourceReadAccess _resourceIsUserWithPotentialDomainOverrides:]
+ -[CCDataResourceReadAccess _shouldSkipEnumeratingResourceForAccessError:]
+ -[CCDataResourceReadAccess enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:]
+ -[CCDataResourceReadAccess enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:].cold.1
+ -[CCDataResourceWriteAccess _performMaintenanceForSet:withResource:accessAssertion:shouldDefer:]
+ -[CCDataResourceWriteAccess _purgeTombstonedResources:]
+ -[CCDataResourceWriteAccess _purgeTombstonedResources:].cold.1
+ -[CCDataResourceWriteAccess databaseWriterForDonationRequest:outDataResource:error:]
+ -[CCDataResourceWriteAccess initWithAssertionOverride:changeNotifier:]
+ -[CCDatabaseCommandCache .cxx_destruct]
+ -[CCDatabaseCommandCache commandForKey:]
+ -[CCDatabaseCommandCache initWithCapacity:]
+ -[CCDatabaseCommandCache setCommand:forKey:]
+ -[CCDatabaseConnection beginReadTransactionWithError:]
+ -[CCDatabaseConnection beginReadTransactionWithError:].cold.1
+ -[CCDatabaseConnection beginWriteTransactionWithError:]
+ -[CCDatabaseConnection beginWriteTransactionWithError:].cold.1
+ -[CCDatabaseConnection columnNamesOfTable:error:]
+ -[CCDatabaseDeviceMapping localDeviceRowId]
+ -[CCDatabaseItemFieldIndexer .cxx_destruct]
+ -[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]
+ -[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:].cold.1
+ -[CCDatabaseItemFieldIndexer blobPrimaryKeyColumnName]
+ -[CCDatabaseItemFieldIndexer blobTableName]
+ -[CCDatabaseItemFieldIndexer configuredColumnNames]
+ -[CCDatabaseItemFieldIndexer description]
+ -[CCDatabaseItemFieldIndexer enumerateInsertCommandsForItemMessage:withBlobPrimaryKey:error:usingBlock:]
+ -[CCDatabaseItemFieldIndexer enumerateInsertCommandsForItemMessage:withBlobPrimaryKey:error:usingBlock:].cold.1
+ -[CCDatabaseItemFieldIndexer expirationDateFieldType]
+ -[CCDatabaseItemFieldIndexer genSQLCreateStatements]
+ -[CCDatabaseItemFieldIndexer indexedItemFieldCount]
+ -[CCDatabaseItemFieldIndexer initWithIndexedFieldConfiguration:blobTableName:itemType:]
+ -[CCDatabaseItemFieldIndexer isValidPredicate:error:]
+ -[CCDatabaseItemFieldIndexer itemFieldTableName]
+ -[CCDatabaseItemFieldIndexer itemMessageSubclass]
+ -[CCDatabaseItemFieldIndexer stringForItemFieldDataType:]
+ -[CCDatabaseItemRetriever .cxx_destruct]
+ -[CCDatabaseItemRetriever _enumerateContentHashesMatchingPredicate:indexer:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateInstanceHashesMatchingPredicate:indexer:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateItemInstancesWithContentHash:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateItemInstancesWithInstanceHash:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateItemInstancesWithItemIdentifier:itemIdentifierType:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateItemInstancesWithSourceItemIdentifier:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSharedItemsMatchingIndexedFieldPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSharedItemsWithContentHash:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSharedItemsWithInstanceHash:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSharedItemsWithItemIdentifier:itemIdentifierType:error:usingBlock:]
+ -[CCDatabaseItemRetriever _enumerateSharedItemsWithSourceItemIdentifier:error:usingBlock:]
+ -[CCDatabaseItemRetriever _errorForUnexpectedRow:fromCommand:]
+ -[CCDatabaseItemRetriever _indexerForPredicate:error:]
+ -[CCDatabaseItemRetriever _obtainDatabaseAccess:]
+ -[CCDatabaseItemRetriever _setDatabase:]
+ -[CCDatabaseItemRetriever _validateAndExtractKeyPrefixedIdentifier:outItemIdentifierType:outItemIdentifier:error:]
+ -[CCDatabaseItemRetriever _validateRow:fromCommmand:outItemInstance:error:]
+ -[CCDatabaseItemRetriever _validateRow:fromCommmand:outSharedItem:error:]
+ -[CCDatabaseItemRetriever enumerateItemInstancesMatchingPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever enumerateSharedItemsMatchingPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:]
+ -[CCDatabaseItemRetriever initWithSet:readAccess:]
+ -[CCDatabaseItemRetriever singleItemInstanceMatchingPredicate:error:]
+ -[CCDatabaseItemRetriever singleSharedItemMatchingPredicate:error:]
+ -[CCDatabaseJoinedProvenance contentHash]
+ -[CCDatabaseJoinedProvenance contentSequenceNumber]
+ -[CCDatabaseJoinedProvenance contentState]
+ -[CCDatabaseJoinedProvenance deviceRowId]
+ -[CCDatabaseJoinedProvenance hasContentInformation]
+ -[CCDatabaseJoinedProvenance hasMetaContentInformation]
+ -[CCDatabaseJoinedProvenance initWithContentHash:contentSequenceNumber:contentDeletedRunLength:contentData:sourceItemIdHash:instanceHash:metaContentSequenceNumber:metaContentDeletedRunLength:metaContentData:deviceRowId:]
+ -[CCDatabaseJoinedProvenance instanceHash]
+ -[CCDatabaseJoinedProvenance metaContentSequenceNumber]
+ -[CCDatabaseJoinedProvenance metaContentState]
+ -[CCDatabaseJoinedProvenance sourceItemIdHash]
+ -[CCDatabaseSelectBuilder setCommonTableExpressions:]
+ -[CCDatabaseSelectBuilder setDistinct:]
+ -[CCDatabaseSelectBuilder setJoinTables:]
+ -[CCDatabaseSelectBuilder setUnionWithSelects:unionAll:]
+ -[CCDatabaseSetEnumerator _searchForKey:options:outSet:error:]
+ -[CCDatabaseSetEnumerator allSetsWithItemType:descriptors:options:error:]
+ -[CCDatabaseSetEnumerator allSetsWithItemType:options:error:]
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:].cold.1
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithItemType:error:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithItemType:options:error:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSetsWithOptions:error:usingBlock:]
+ -[CCDatabaseSetEnumerator setWithKey:error:]
+ -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]
+ -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:].cold.1
+ -[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
+ -[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:].cold.1
+ -[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:]
+ -[CCDatabaseSetStateReader enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
+ -[CCDatabaseSetStateReader enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
+ -[CCDatabaseUpdateTracker .cxx_destruct]
+ -[CCDatabaseUpdateTracker deltaProduced]
+ -[CCDatabaseUpdateTracker initWithSet:]
+ -[CCDatabaseUpdateTracker localInstanceAddedCount]
+ -[CCDatabaseUpdateTracker localInstanceDeltaProduced]
+ -[CCDatabaseUpdateTracker localInstanceRemovedCount]
+ -[CCDatabaseUpdateTracker localInstanceUpdatedCount]
+ -[CCDatabaseUpdateTracker modifiedRowCount]
+ -[CCDatabaseUpdateTracker setLocalInstanceAddedCount:]
+ -[CCDatabaseUpdateTracker setLocalInstanceRemovedCount:]
+ -[CCDatabaseUpdateTracker setLocalInstanceUpdatedCount:]
+ -[CCDatabaseUpdateTracker setModifiedRowCount:]
+ -[CCDatabaseUpdateTracker setSharedItemAddedCount:]
+ -[CCDatabaseUpdateTracker setSharedItemRemovedCount:]
+ -[CCDatabaseUpdateTracker setSharedItemRevisedCount:]
+ -[CCDatabaseUpdateTracker set]
+ -[CCDatabaseUpdateTracker sharedItemAddedCount]
+ -[CCDatabaseUpdateTracker sharedItemRemovedCount]
+ -[CCDatabaseUpdateTracker sharedItemRevisedCount]
+ -[CCDatabaseWriter .cxx_destruct]
+ -[CCDatabaseWriter _ageOfMaintenanceFromPriorRunCount:maintenanceHistory:]
+ -[CCDatabaseWriter _calculateMinimumTombstoneAgeWithMaintenanceHistory:]
+ -[CCDatabaseWriter _countDeviceRecords:withOptions:error:]
+ -[CCDatabaseWriter _deleteDeviceRowId:error:]
+ -[CCDatabaseWriter _deleteExpiredItemInstances:]
+ -[CCDatabaseWriter _deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:]
+ -[CCDatabaseWriter _deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:].cold.1
+ -[CCDatabaseWriter _deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:].cold.2
+ -[CCDatabaseWriter _deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:].cold.3
+ -[CCDatabaseWriter _enumerateLocalInstancesWithError:selectingOnlyUnwritten:usingBlock:]
+ -[CCDatabaseWriter _errorForUnexpectedRow:fromCommand:]
+ -[CCDatabaseWriter _executeCreateTableStatements:error:]
+ -[CCDatabaseWriter _expireAndTombstoneAllContentProvenanceForDeviceRowId:error:]
+ -[CCDatabaseWriter _expireDeviceRowId:error:]
+ -[CCDatabaseWriter _incrementCachedIntegerWithKey:error:]
+ -[CCDatabaseWriter _incrementLocalDeltaGeneration:]
+ -[CCDatabaseWriter _insertContent:contentHash:outExists:error:]
+ -[CCDatabaseWriter _insertContentProvenanceWithDeviceRowId:contentHash:sequenceNumber:error:]
+ -[CCDatabaseWriter _insertDeviceSite:returningRowId:error:]
+ -[CCDatabaseWriter _insertIndexedFieldsForItemMessage:withBlobPrimaryKey:indexer:error:]
+ -[CCDatabaseWriter _insertLocalContentWithProvenance:contentHash:isNew:error:]
+ -[CCDatabaseWriter _insertMetaContent:instanceHash:outIsDuplicate:error:]
+ -[CCDatabaseWriter _insertMetaContentProvenanceWithSourceItemIdHash:instanceHash:contentHash:error:]
+ -[CCDatabaseWriter _persistCachedIntegers:]
+ -[CCDatabaseWriter _rebuildIndexedItemFieldTableWithIndexer:error:]
+ -[CCDatabaseWriter _selectContentProvenenceWithContentHash:deviceRowId:outSequenceNumber:error:]
+ -[CCDatabaseWriter _selectDeviceRecords:withOptions:beyondExpirationDate:error:]
+ -[CCDatabaseWriter _selectLatestDeviceRecordWithDeviceUUID:outRecord:error:]
+ -[CCDatabaseWriter _selectLocalDeviceRecord:error:]
+ -[CCDatabaseWriter _selectLocalInstanceCount:error:]
+ -[CCDatabaseWriter _selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:error:]
+ -[CCDatabaseWriter _selectMetaContentWithInstanceHash:outRecord:error:]
+ -[CCDatabaseWriter _selectPersistedValueForKey:outValue:valueClass:error:]
+ -[CCDatabaseWriter _tombstoneContentProvenanceRowsForExpiredDeviceRowId:error:]
+ -[CCDatabaseWriter _tombstoneMetaContentWithSourceItemIdHash:tombstoneContentIfNoLongerPresent:error:]
+ -[CCDatabaseWriter _updateDeviceRowId:deltaGeneration:expirationDate:error:]
+ -[CCDatabaseWriter _updateLocalSourceVersion:localSourceValidityHash:error:]
+ -[CCDatabaseWriter _updateMaintenanceHistory:]
+ -[CCDatabaseWriter _updateMetaContent:tombstoneContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:]
+ -[CCDatabaseWriter _upsertInteger:forKey:error:]
+ -[CCDatabaseWriter _upsertInteger:forKey:skipIfNil:error:]
+ -[CCDatabaseWriter _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:error:]
+ -[CCDatabaseWriter commitUpdate:]
+ -[CCDatabaseWriter dealloc]
+ -[CCDatabaseWriter dealloc].cold.1
+ -[CCDatabaseWriter deleteAllLocalInstances:]
+ -[CCDatabaseWriter deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord:]
+ -[CCDatabaseWriter deleteSourceItemIdHash:error:]
+ -[CCDatabaseWriter description]
+ -[CCDatabaseWriter enumerateLocalInstancesMatchingPredicate:error:usingBlock:]
+ -[CCDatabaseWriter enumerateUnwrittenLocalInstancesWithError:usingBlock:]
+ -[CCDatabaseWriter expireRemoteDeviceUUID:error:]
+ -[CCDatabaseWriter initWithSet:database:changeNotifier:request:isPrepared:error:]
+ -[CCDatabaseWriter insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:error:]
+ -[CCDatabaseWriter insertRemoteContent:contentHash:sequenceNumber:onDeviceRowId:error:]
+ -[CCDatabaseWriter localDeviceRecord]
+ -[CCDatabaseWriter performMaintenanceWithShouldTombstone:shouldDefer:error:]
+ -[CCDatabaseWriter prepareDatabaseWithLocalDeviceSite:error:]
+ -[CCDatabaseWriter prepareItemFieldIndexes:]
+ -[CCDatabaseWriter priorLocalDonationDate]
+ -[CCDatabaseWriter priorLocalFullSetDonationDate]
+ -[CCDatabaseWriter priorLocalInstanceCount]
+ -[CCDatabaseWriter priorLocalSourceRevisionToken]
+ -[CCDatabaseWriter priorLocalSourceValidityHash]
+ -[CCDatabaseWriter priorLocalSourceVersion]
+ -[CCDatabaseWriter registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:error:]
+ -[CCDatabaseWriter rollbackUpdate:]
+ -[CCDatabaseWriter selectAllDeviceRecords:]
+ -[CCDatabaseWriter selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:]
+ -[CCDatabaseWriter selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:].cold.1
+ -[CCDatabaseWriter tombstoneContentSequenceNumbersInRange:forRemoteDeviceRowId:error:]
+ -[CCDatabaseWriter updateContent:andMetaContent:sourceItemIdHash:contentHash:instanceHash:isDuplicate:error:]
+ -[CCDatabaseWriter updateLastLocalDonationDate:error:]
+ -[CCDatabaseWriter updateMetaContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:]
+ -[CCDatabaseWriter updateRevisionToken:error:]
+ -[CCDatabaseWriter updatedLocalSourceValidityHash]
+ -[CCDatabaseWriter updatedLocalSourceVersion]
+ -[CCDatabaseWriter(Compaction) _combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:]
+ -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:minimumTombstoneAge:shouldDefer:error:]
+ -[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]
+ -[CCDatabaseWriter(Compaction) _deleteRecordsWithRowIds:vectorType:error:]
+ -[CCDatabaseWriter(Compaction) _deviceRowIdentifiersWithError:]
+ -[CCDatabaseWriter(Compaction) _markTombstoneRowForVectorType:provenanceRowId:sequenceRange:error:]
+ -[CCDatabaseWriter(Compaction) _markTombstoneRowForVectorType:provenanceRowId:sequenceRange:error:].cold.1
+ -[CCDatabaseWriter(Compaction) _processRange:deviceRowId:vectorType:stateSets:error:shouldDefer:]
+ -[CCDatabaseWriter(Compaction) _sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:]
+ -[CCDatabaseWriter(Compaction) _stateSetsForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]
+ -[CCDatabaseWriter(Compaction) _updateModifiedRowCount]
+ -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:]
+ -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:].cold.1
+ -[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:].cold.2
+ -[CCDatabaseWriter(Compaction) compactContiguousTombstonesWithMinimumTombstoneAge:shouldDefer:error:]
+ -[CCDatabaseWriter(Compaction) compactContiguousTombstonesWithMinimumTombstoneAge:shouldDefer:error:].cold.1
+ -[CCDonationServicePriors .cxx_destruct]
+ -[CCDonationServicePriors donationDate]
+ -[CCDonationServicePriors encodeWithCoder:]
+ -[CCDonationServicePriors fullSetDonationDate]
+ -[CCDonationServicePriors initWithCoder:]
+ -[CCDonationServicePriors initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:]
+ -[CCDonationServicePriors instanceCount]
+ -[CCDonationServicePriors isAwaitingFullSet]
+ -[CCDonationServicePriors options]
+ -[CCDonationServicePriors revisionToken]
+ -[CCDonationServicePriors version]
+ -[CCDonationXPCClient addItemsWithContents:metaContents:cacheContents:reply:]
+ -[CCDonationXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]
+ -[CCDonationXPCClient cancelSetDonation:]
+ -[CCDonationXPCClient endSetDonationWithOptions:revisionToken:reply:]
+ -[CCDonationXPCClient initWithClientId:]
+ -[CCDonationXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]
+ -[CCDonationXPCClient removeItemsMatchingPredicate:reply:]
+ -[CCDonationXPCClient removeSourceItemIdentifier:reply:]
+ -[CCDonationXPCClientFactory makeConnection:]
+ -[CCFullSetDonation registerItem:cacheContent:error:]
+ -[CCIncrementalSetDonation addOrUpdateItem:cacheContent:error:]
+ -[CCIncrementalSetDonation removeItemsMatchingPredicate:error:]
+ -[CCIndexedFieldConfiguration .cxx_destruct]
+ -[CCIndexedFieldConfiguration dataType]
+ -[CCIndexedFieldConfiguration descriptorAllowList]
+ -[CCIndexedFieldConfiguration fieldType]
+ -[CCIndexedFieldConfiguration indexedFieldType]
+ -[CCIndexedFieldConfiguration initWithFieldType:dataType:descriptorAllowList:]
+ -[CCIndexedFieldConfiguration initWithFieldType:dataType:indexedFieldType:descriptorAllowList:]
+ -[CCItemFieldPredicate .cxx_destruct]
+ -[CCItemFieldPredicate copyWithFieldType:]
+ -[CCItemFieldPredicate copyWithZone:]
+ -[CCItemFieldPredicate description]
+ -[CCItemFieldPredicate encodeWithCoder:]
+ -[CCItemFieldPredicate fieldType]
+ -[CCItemFieldPredicate hash]
+ -[CCItemFieldPredicate initWithCoder:]
+ -[CCItemFieldPredicate initWithPredicateType:fieldType:value:operatorType:]
+ -[CCItemFieldPredicate init]
+ -[CCItemFieldPredicate isEqual:]
+ -[CCItemFieldPredicate isEqualToItemFieldPredicate:]
+ -[CCItemFieldPredicate operatorType]
+ -[CCItemFieldPredicate predicateType]
+ -[CCItemFieldPredicate value]
+ -[CCItemInstance initWithSharedIdentifier:instanceIdentifier:content:metaContent:sourceItemIdentifierHash:]
+ -[CCItemInstance sourceItemIdentifierHash]
+ -[CCItemMessage _initWithInnerData:error:]
+ -[CCItemMessage decodeFieldValuesFromData:error:]
+ -[CCItemMessage ensureDecodedWithError:]
+ -[CCItemMessage ensureDecodedWithError:].cold.1
+ -[CCItemMessage initLazyDecodedWithTrustedItemMessageData:error:]
+ -[CCItemMessage initWithItemMessageData:error:]
+ -[CCItemMessage itemMessageData]
+ -[CCMetaContentProvenanceRecord .cxx_destruct]
+ -[CCMetaContentProvenanceRecord contentHash]
+ -[CCMetaContentProvenanceRecord deletedDate]
+ -[CCMetaContentProvenanceRecord deletedRunLength]
+ -[CCMetaContentProvenanceRecord description]
+ -[CCMetaContentProvenanceRecord deviceRowId]
+ -[CCMetaContentProvenanceRecord hash]
+ -[CCMetaContentProvenanceRecord initWithDatabaseValueRow:]
+ -[CCMetaContentProvenanceRecord init]
+ -[CCMetaContentProvenanceRecord instanceHash]
+ -[CCMetaContentProvenanceRecord isEqual:]
+ -[CCMetaContentProvenanceRecord isEqualToRecord:]
+ -[CCMetaContentProvenanceRecord sequenceNumber]
+ -[CCMetaContentProvenanceRecord sourceItemIdHash]
+ -[CCMetaContentProvenanceRecord writtenDate]
+ -[CCMutableSetChange _deduplicateRemovedObjects:withAdded:presentNonAdded:outAll:outAdded:outRemoved:]
+ -[CCMutableSetChange appendAddedDevice:]
+ -[CCMutableSetChange appendAddedLocalInstance:]
+ -[CCMutableSetChange appendPresentNonAddedDevice:]
+ -[CCMutableSetChange appendPresentNonAddedLocalInstance:]
+ -[CCMutableSetChange appendRemovedDevice:]
+ -[CCMutableSetChange appendRemovedLocalInstance:]
+ -[CCMutableSetChange finalizeSetChange]
+ -[CCMutableSetChange hasContentHash:]
+ -[CCMutableSetChange initWithSharedIdentifier:]
+ -[CCMutableSetChange setSharedItem:]
+ -[CCProvenanceCompactionRecord .cxx_destruct]
+ -[CCProvenanceCompactionRecord initWithRowId:]
+ -[CCProvenanceCompactionRecord rowId]
+ -[CCProvenanceStateSets .cxx_destruct]
+ -[CCProvenanceStateSets compactedSequencesLock]
+ -[CCProvenanceStateSets description]
+ -[CCProvenanceStateSets eligibleSequences]
+ -[CCProvenanceStateSets ineligibleSequences]
+ -[CCProvenanceStateSets initWithIneligibleSequences:eligibleSequences:compactedSequences:]
+ -[CCRemoteCRDTSetDonation remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]
+ -[CCSQLCommandCTE .cxx_destruct]
+ -[CCSQLCommandCTE copyWithZone:]
+ -[CCSQLCommandCTE hash]
+ -[CCSQLCommandCTE initWithName:select:]
+ -[CCSQLCommandCTE isEqual:]
+ -[CCSQLCommandCTE name]
+ -[CCSQLCommandCTE select]
+ -[CCSQLCommandJoinTable initWithTable:joinType:joinCriterion:]
+ -[CCSQLCommandJoinTable joinType]
+ -[CCSQLCommandUnion .cxx_destruct]
+ -[CCSQLCommandUnion copyWithZone:]
+ -[CCSQLCommandUnion hash]
+ -[CCSQLCommandUnion initWithSelects:]
+ -[CCSQLCommandUnion isEqual:]
+ -[CCSQLCommandUnion selects]
+ -[CCSQLiteDatabase _executePragma:outError:]
+ -[CCSQLiteDatabase beginReadTransactionWithError:]
+ -[CCSQLiteDatabase beginWriteTransactionWithError:]
+ -[CCSQLiteDatabase busyTimeout]
+ -[CCSQLiteDatabase cacheSpill]
+ -[CCSQLiteDatabase initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:busyTimeout:cacheSpill:]
+ -[CCSQLiteDatabase initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:busyTimeout:cacheSpill:].cold.1
+ -[CCSerializedSet itemRetrieverWithUseCase:]
+ -[CCSerializedSetEnumerator _searchForKey:options:outSet:error:]
+ -[CCSerializedSetEnumerator _shouldFilterOutSet:withOptionsFilter:]
+ -[CCSerializedSetEnumerator allSetsWithItemType:descriptors:options:error:]
+ -[CCSerializedSetEnumerator allSetsWithItemType:options:error:]
+ -[CCSerializedSetEnumerator enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:]
+ -[CCSerializedSetEnumerator enumerateAllSetsWithItemType:error:usingBlock:]
+ -[CCSerializedSetEnumerator enumerateAllSetsWithItemType:options:error:usingBlock:]
+ -[CCSerializedSetEnumerator enumerateAllSetsWithOptions:error:usingBlock:]
+ -[CCSerializedSetEnumerator setWithKey:error:]
+ -[CCSerializedSetItemRetriever .cxx_destruct]
+ -[CCSerializedSetItemRetriever enumerateItemInstancesMatchingPredicate:error:usingBlock:]
+ -[CCSerializedSetItemRetriever enumerateSharedItemsMatchingPredicate:error:usingBlock:]
+ -[CCSerializedSetItemRetriever initWithSetMessage:]
+ -[CCSerializedSetItemRetriever singleItemInstanceMatchingPredicate:error:]
+ -[CCSerializedSetItemRetriever singleSharedItemMatchingPredicate:error:]
+ -[CCSet _keyData]
+ -[CCSet identifier]
+ -[CCSet itemRetrieverWithUseCase:]
+ -[CCSet keyPrefixedIdentifierForItemInstance:]
+ -[CCSet keyPrefixedIdentifierForSharedItem:]
+ -[CCSet keyPrefixedSourceItemIdentifierForItemInstance:]
+ -[CCSet key]
+ -[CCSet prefixedInstanceIdentifierAsUUID:]
+ -[CCSet prefixedSharedIdentifierAsUUID:]
+ -[CCSetConfiguration dataProtectionClass]
+ -[CCSetConfiguration indexedFields]
+ -[CCSetConfiguration initWithSetIdentifier:setUUID:resourceDomain:configuredDescriptors:syncPolicy:indexedFields:dataProtectionClass:]
+ -[CCSetDonation _addItem:cacheContent:error:]
+ -[CCSetDonation _finishWithServiceOptions:error:]
+ -[CCSetDonation _priorRevisionTokenOrEmptyDictionary]
+ -[CCSetDonation _priorRevisionTokenOrEmptyDictionary].cold.1
+ -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]
+ -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:].cold.1
+ -[CCSetDonation _removeItemsMatchingPredicate:error:]
+ -[CCSetDonation initWithName:itemType:service:serviceOptions:errorCode:priors:flushThreshold:]
+ -[CCSetDonation initWithName:itemType:service:serviceOptions:errorCode:priors:flushThreshold:].cold.1
+ -[CCSetDonation priorRevisionTokenWithKey:]
+ -[CCSetDonation updateRevisionToken:withKey:error:]
+ -[CCSetIntegrityCheck checkRunMarkerCorruptionInDatabase:set:error:]
+ -[CCSetIntegrityCheck checkSequenceGapsAndOverlapsInDatabase:set:error:]
+ -[CCSetIntegrityCheck descriptionForSet:]
+ -[CCSetIntegrityCheck performIntegrityCheckOnSets:error:]
+ -[CCSetIntegrityCheckResult .cxx_destruct]
+ -[CCSetIntegrityCheckResult checksFailed]
+ -[CCSetIntegrityCheckResult checksPerformed]
+ -[CCSetIntegrityCheckResult description]
+ -[CCSetIntegrityCheckResult initWithPassed:checksPerformed:checksFailed:issues:]
+ -[CCSetIntegrityCheckResult issues]
+ -[CCSetIntegrityCheckResult passed]
+ -[CCSetItemRetriever .cxx_destruct]
+ -[CCSetItemRetriever description]
+ -[CCSetItemRetriever enumerateItemInstancesMatchingPredicate:error:usingBlock:]
+ -[CCSetItemRetriever enumerateSharedItemsMatchingPredicate:error:usingBlock:]
+ -[CCSetItemRetriever initWithSet:retriever:]
+ -[CCSetItemRetriever singleItemInstanceMatchingPredicate:error:]
+ -[CCSetItemRetriever singleSharedItemMatchingPredicate:error:]
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:]
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.1
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.2
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.3
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.4
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.5
+ -[CCSetsAccessDaemonDelegate _atomicallyCreateDataResource:withResourceGeneration:].cold.6
+ -[CCSetsAccessDaemonDelegate _atomicallyRemoveDataResource:]
+ -[CCSetsAccessDaemonDelegate _atomicallyRemoveDataResource:].cold.1
+ -[CCSetsAccessDaemonDelegate _atomicallyRemoveDataResource:].cold.2
+ -[CCSetsAccessDaemonDelegate _temporaryDirectoryForDataResource:]
+ -[CCXPCClient _connectionTerminationHandlerWithErrorCode:]
+ -[CCXPCClient connectionErrorCode]
+ -[CCXPCClient initWithRemoteObjectInterface:exportedInterface:connection:clientId:useCase:]
+ -[CCXPCClient initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:useCase:]
+ -[CCXPCClient initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:useCase:]
+ -[CCXPCClient initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:useCase:].cold.1
+ -[CCXPCClient remoteObjectProxy:errorHandler:]
+ -[CCXPCClient requestBiomeEndpointForAppScopedService:user:reply:].cold.1
+ -[CCXPCClient setConnectionErrorCode:]
+ GCC_except_table21
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table64
+ OBJC_IVAR_$_CCItemMessage._hasBeenDecoded
+ OBJC_IVAR_$_CCItemMessage._lazyDecodingEnabled
+ _BMUseCaseInternalTool
+ _CCAttributedSourcesConfig
+ _CCAttributionFunctionForSet
+ _CCDatabaseColumnCreatedDate
+ _CCDatabaseColumnDeletedDate
+ _CCDatabaseColumnDeletedRunLength
+ _CCDatabaseColumnModifiedDate
+ _CCDatabaseColumnSequenceNumber
+ _CCDatabaseColumnWrittenDate
+ _CCDatabaseIndexContentProvenanceContentHash
+ _CCDatabaseIndexContentProvenanceSequenceNumber
+ _CCDatabaseIndexDeviceOptions
+ _CCDatabaseIndexDeviceUUID
+ _CCDatabaseIndexItemFieldPrefix
+ _CCDatabaseIndexMetaContentProvenanceContentHash
+ _CCDatabaseIndexMetaContentProvenanceInstanceHash
+ _CCDatabaseIndexMetaContentProvenanceSequenceNumber
+ _CCDatabaseIndexMetaContentProvenanceSourceItemIdHash
+ _CCDatabaseIndexMetaContentProvenanceWrittenDate
+ _CCDatabaseTableNameContentField
+ _CCDatabaseTableNameContentProvenance
+ _CCDatabaseTableNameMetaContentField
+ _CCDatabaseTableNameMetaContentProvenance
+ _CCDatabaseWriterCompactionDefaultMinimumMaintenanceRuns
+ _CCDatabaseWriterCompactionDefaultMinimumTombstoneAge
+ _CCDatabaseWriterCompactionErrorDomain
+ _CCDonationServiceOptionsDescription
+ _CCDonationServiceRequestDescription
+ _CCDonationServiceRequestParametersDescription
+ _CCDonationServiceStatusDescription
+ _CCDonationServiceStatusIsActive
+ _CCItemErrorDescription
+ _CCItemFieldColumnNameForType
+ _CCItemFieldPredicateTypeDescription
+ _CCItemInstanceIdentifierHash
+ _CCJSONStringFromRevisionTokenDictionary
+ _CCPersistedKeyValueKeyMaintenanceHistory
+ _CCProvenanceRecordAtomState
+ _CCProvenanceRecordAtomStateFromDeletedRunLength
+ _CCProvenanceRecordClockValueRange
+ _CCProvenanceRecordIsDeletedRun
+ _CCProvenanceRecordPresent
+ _CCProvenanceRecordTombstoned
+ _CCRevisionTokenDictionaryFromJSONString
+ _CCSerializationErrorDescription
+ _CCSetDonationErrorDescription
+ _CCSetDonationErrorDomain
+ _CCSetErrorDescription
+ _CCSetErrorWithDetails
+ _CCSetKeyHash
+ _CCSetKeyPrefixedIdentifierUnpack
+ _CCSetKeyPrefixedItemIdentifierPack
+ _CCSharedItemIdentifierHash
+ _CCSourceItemIdentifierHash
+ _NSStringFromRange
+ _NSUnionRange
+ _OBJC_CLASS_$_CCCachedDocumentUtilities
+ _OBJC_CLASS_$_CCContentProvenanceRecord
+ _OBJC_CLASS_$_CCDatabaseCommandCache
+ _OBJC_CLASS_$_CCDatabaseItemFieldIndexer
+ _OBJC_CLASS_$_CCDatabaseItemRetriever
+ _OBJC_CLASS_$_CCDatabaseUpdateTracker
+ _OBJC_CLASS_$_CCDatabaseWriter
+ _OBJC_CLASS_$_CCDonationServicePriors
+ _OBJC_CLASS_$_CCDonationXPCClient
+ _OBJC_CLASS_$_CCDonationXPCClientFactory
+ _OBJC_CLASS_$_CCIndexedFieldConfiguration
+ _OBJC_CLASS_$_CCItemFieldPredicate
+ _OBJC_CLASS_$_CCMaintenenaceXPCClient
+ _OBJC_CLASS_$_CCMetaContentProvenanceRecord
+ _OBJC_CLASS_$_CCProvenanceCompactionRecord
+ _OBJC_CLASS_$_CCProvenanceStateSets
+ _OBJC_CLASS_$_CCSQLCommandCTE
+ _OBJC_CLASS_$_CCSQLCommandUnion
+ _OBJC_CLASS_$_CCSerializedSetItemRetriever
+ _OBJC_CLASS_$_CCSetChangeXPCClient
+ _OBJC_CLASS_$_CCSetIntegrityCheck
+ _OBJC_CLASS_$_CCSetIntegrityCheckResult
+ _OBJC_CLASS_$_CCSetItemRetriever
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_IVAR_$_CCContentProvenanceRecord._contentHash
+ _OBJC_IVAR_$_CCContentProvenanceRecord._deletedDate
+ _OBJC_IVAR_$_CCContentProvenanceRecord._deletedRunLength
+ _OBJC_IVAR_$_CCContentProvenanceRecord._deviceRowId
+ _OBJC_IVAR_$_CCContentProvenanceRecord._sequenceNumber
+ _OBJC_IVAR_$_CCDataResourceWriteAccess._changeNotifier
+ _OBJC_IVAR_$_CCDatabaseCommandCache._cache
+ _OBJC_IVAR_$_CCDatabaseDeviceMapping._localDeviceRowId
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._blobPrimaryKeyColumnName
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._blobTableName
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._cachedInsertCommand
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._configuration
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._indexedItemFieldCount
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._itemFieldTableName
+ _OBJC_IVAR_$_CCDatabaseItemFieldIndexer._itemMessageSubclass
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._cache
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._contentIndexer
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._database
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._metaContentIndexer
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._readAccess
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._set
+ _OBJC_IVAR_$_CCDatabaseItemRetriever._setConfiguration
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._contentHash
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._contentSequenceNumber
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._contentState
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._deviceRowId
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._instanceHash
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._metaContentSequenceNumber
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._metaContentState
+ _OBJC_IVAR_$_CCDatabaseJoinedProvenance._sourceItemIdHash
+ _OBJC_IVAR_$_CCDatabaseSelectBuilder._ctes
+ _OBJC_IVAR_$_CCDatabaseSelectBuilder._distinct
+ _OBJC_IVAR_$_CCDatabaseSelectBuilder._joinTables
+ _OBJC_IVAR_$_CCDatabaseSelectBuilder._unionAll
+ _OBJC_IVAR_$_CCDatabaseSelectBuilder._unionSelects
+ _OBJC_IVAR_$_CCDatabaseSetEnumerator._setKeyCache
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._localInstanceAddedCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._localInstanceRemovedCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._localInstanceUpdatedCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._modifiedRowCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._set
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._sharedItemAddedCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._sharedItemRemovedCount
+ _OBJC_IVAR_$_CCDatabaseUpdateTracker._sharedItemRevisedCount
+ _OBJC_IVAR_$_CCDatabaseWriter._cachedLocalHighestAttestationGeneration
+ _OBJC_IVAR_$_CCDatabaseWriter._cachedLocalHighestContentSequenceNumber
+ _OBJC_IVAR_$_CCDatabaseWriter._cachedLocalHighestMetaContentSequenceNumber
+ _OBJC_IVAR_$_CCDatabaseWriter._changeNotifier
+ _OBJC_IVAR_$_CCDatabaseWriter._commandCache
+ _OBJC_IVAR_$_CCDatabaseWriter._contentIndexer
+ _OBJC_IVAR_$_CCDatabaseWriter._database
+ _OBJC_IVAR_$_CCDatabaseWriter._localDeviceRecord
+ _OBJC_IVAR_$_CCDatabaseWriter._metaContentIndexer
+ _OBJC_IVAR_$_CCDatabaseWriter._priorActiveRemoteDeviceCount
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalDonationDate
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalFullSetDonationDate
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalInstanceCount
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalSourceRevisionToken
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalSourceValidityHash
+ _OBJC_IVAR_$_CCDatabaseWriter._priorLocalSourceVersion
+ _OBJC_IVAR_$_CCDatabaseWriter._requestDescription
+ _OBJC_IVAR_$_CCDatabaseWriter._set
+ _OBJC_IVAR_$_CCDatabaseWriter._setConfiguration
+ _OBJC_IVAR_$_CCDatabaseWriter._startTimeMicros
+ _OBJC_IVAR_$_CCDatabaseWriter._tracker
+ _OBJC_IVAR_$_CCDatabaseWriter._updatedLocalSourceValidityHash
+ _OBJC_IVAR_$_CCDatabaseWriter._updatedLocalSourceVersion
+ _OBJC_IVAR_$_CCDonationServicePriors._donationDate
+ _OBJC_IVAR_$_CCDonationServicePriors._fullSetDonationDate
+ _OBJC_IVAR_$_CCDonationServicePriors._instanceCount
+ _OBJC_IVAR_$_CCDonationServicePriors._options
+ _OBJC_IVAR_$_CCDonationServicePriors._revisionToken
+ _OBJC_IVAR_$_CCDonationServicePriors._version
+ _OBJC_IVAR_$_CCIndexedFieldConfiguration._dataType
+ _OBJC_IVAR_$_CCIndexedFieldConfiguration._descriptorAllowList
+ _OBJC_IVAR_$_CCIndexedFieldConfiguration._fieldType
+ _OBJC_IVAR_$_CCIndexedFieldConfiguration._indexedFieldType
+ _OBJC_IVAR_$_CCItemFieldPredicate._fieldType
+ _OBJC_IVAR_$_CCItemFieldPredicate._operatorType
+ _OBJC_IVAR_$_CCItemFieldPredicate._predicateType
+ _OBJC_IVAR_$_CCItemFieldPredicate._value
+ _OBJC_IVAR_$_CCItemInstance._sourceItemIdentifierHash
+ _OBJC_IVAR_$_CCItemMessage._decodeLock
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._contentHash
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._deletedDate
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._deletedRunLength
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._deviceRowId
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._instanceHash
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._sequenceNumber
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._sourceItemIdHash
+ _OBJC_IVAR_$_CCMetaContentProvenanceRecord._writtenDate
+ _OBJC_IVAR_$_CCMutableSetChange._addedInstances
+ _OBJC_IVAR_$_CCMutableSetChange._presentNonAddedDevices
+ _OBJC_IVAR_$_CCMutableSetChange._presentNonAddedInstances
+ _OBJC_IVAR_$_CCMutableSetChange._removedInstances
+ _OBJC_IVAR_$_CCMutableSetChange._sharedIdentifier
+ _OBJC_IVAR_$_CCProvenanceCompactionRecord._rowId
+ _OBJC_IVAR_$_CCProvenanceStateSets._compactedSequencesLock
+ _OBJC_IVAR_$_CCProvenanceStateSets._eligibleSequences
+ _OBJC_IVAR_$_CCProvenanceStateSets._ineligibleSequences
+ _OBJC_IVAR_$_CCSQLCommandCTE._name
+ _OBJC_IVAR_$_CCSQLCommandCTE._select
+ _OBJC_IVAR_$_CCSQLCommandJoinTable._joinType
+ _OBJC_IVAR_$_CCSQLCommandUnion._selects
+ _OBJC_IVAR_$_CCSQLiteDatabase._busyTimeout
+ _OBJC_IVAR_$_CCSQLiteDatabase._cacheSpill
+ _OBJC_IVAR_$_CCSerializedSetItemRetriever._setMessage
+ _OBJC_IVAR_$_CCSet._key
+ _OBJC_IVAR_$_CCSetConfiguration._dataProtectionClass
+ _OBJC_IVAR_$_CCSetConfiguration._indexedFields
+ _OBJC_IVAR_$_CCSetDonation._cacheContentBuffers
+ _OBJC_IVAR_$_CCSetDonation._priorRevisionTokenDictionary
+ _OBJC_IVAR_$_CCSetDonation._updatedRevisionTokenDictionary
+ _OBJC_IVAR_$_CCSetIntegrityCheckResult._checksFailed
+ _OBJC_IVAR_$_CCSetIntegrityCheckResult._checksPerformed
+ _OBJC_IVAR_$_CCSetIntegrityCheckResult._issues
+ _OBJC_IVAR_$_CCSetIntegrityCheckResult._passed
+ _OBJC_IVAR_$_CCSetItemRetriever._retriever
+ _OBJC_IVAR_$_CCSetItemRetriever._set
+ _OBJC_IVAR_$_CCXPCClient._connectionErrorCode
+ _OBJC_METACLASS_$_CCCachedDocumentUtilities
+ _OBJC_METACLASS_$_CCContentProvenanceRecord
+ _OBJC_METACLASS_$_CCDatabaseCommandCache
+ _OBJC_METACLASS_$_CCDatabaseItemFieldIndexer
+ _OBJC_METACLASS_$_CCDatabaseItemRetriever
+ _OBJC_METACLASS_$_CCDatabaseUpdateTracker
+ _OBJC_METACLASS_$_CCDatabaseWriter
+ _OBJC_METACLASS_$_CCDonationServicePriors
+ _OBJC_METACLASS_$_CCDonationXPCClient
+ _OBJC_METACLASS_$_CCDonationXPCClientFactory
+ _OBJC_METACLASS_$_CCIndexedFieldConfiguration
+ _OBJC_METACLASS_$_CCItemFieldPredicate
+ _OBJC_METACLASS_$_CCMaintenenaceXPCClient
+ _OBJC_METACLASS_$_CCMetaContentProvenanceRecord
+ _OBJC_METACLASS_$_CCProvenanceCompactionRecord
+ _OBJC_METACLASS_$_CCProvenanceStateSets
+ _OBJC_METACLASS_$_CCSQLCommandCTE
+ _OBJC_METACLASS_$_CCSQLCommandUnion
+ _OBJC_METACLASS_$_CCSerializedSetItemRetriever
+ _OBJC_METACLASS_$_CCSetChangeXPCClient
+ _OBJC_METACLASS_$_CCSetIntegrityCheck
+ _OBJC_METACLASS_$_CCSetIntegrityCheckResult
+ _OBJC_METACLASS_$_CCSetItemRetriever
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.MobileAddressBook
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.MobileSMS
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.Music
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.Passbook
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.email.SearchIndexer
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.homed
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilecal
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilemail
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilenotes
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilesafari
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobileslideshow
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.podcasts
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.reminders
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.shortcuts
+ __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.usernotificationsd
+ __ATTRIBUTE_WORK_TO__UNKNOWN
+ __OBJC_$_CLASS_METHODS_CCCachedDocumentUtilities
+ __OBJC_$_CLASS_METHODS_CCContentProvenanceRecord
+ __OBJC_$_CLASS_METHODS_CCDatabaseItemFieldIndexer
+ __OBJC_$_CLASS_METHODS_CCDatabaseItemRetriever
+ __OBJC_$_CLASS_METHODS_CCDatabaseWriter
+ __OBJC_$_CLASS_METHODS_CCDonationServicePriors
+ __OBJC_$_CLASS_METHODS_CCDonationXPCClient
+ __OBJC_$_CLASS_METHODS_CCItemFieldPredicate
+ __OBJC_$_CLASS_METHODS_CCMaintenenaceXPCClient
+ __OBJC_$_CLASS_METHODS_CCMetaContentProvenanceRecord
+ __OBJC_$_CLASS_METHODS_CCSetChangeXPCClient
+ __OBJC_$_CLASS_METHODS_CCSetDonation(DocumentCache|Deprecations|ServiceProviderDeprecations)
+ __OBJC_$_CLASS_METHODS_CCSetItemRetriever
+ __OBJC_$_CLASS_METHODS_CCXPCClient
+ __OBJC_$_CLASS_PROP_LIST_CCDonationServicePriors
+ __OBJC_$_CLASS_PROP_LIST_CCItemFieldPredicate
+ __OBJC_$_INSTANCE_METHODS_CCContentProvenanceRecord
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseCommandCache
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseItemFieldIndexer
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseItemRetriever
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseUpdateTracker
+ __OBJC_$_INSTANCE_METHODS_CCDatabaseWriter(Compaction)
+ __OBJC_$_INSTANCE_METHODS_CCDonationServicePriors
+ __OBJC_$_INSTANCE_METHODS_CCDonationXPCClient
+ __OBJC_$_INSTANCE_METHODS_CCDonationXPCClientFactory
+ __OBJC_$_INSTANCE_METHODS_CCIndexedFieldConfiguration
+ __OBJC_$_INSTANCE_METHODS_CCItemFieldPredicate
+ __OBJC_$_INSTANCE_METHODS_CCMetaContentProvenanceRecord
+ __OBJC_$_INSTANCE_METHODS_CCProvenanceCompactionRecord
+ __OBJC_$_INSTANCE_METHODS_CCProvenanceStateSets
+ __OBJC_$_INSTANCE_METHODS_CCSQLCommandCTE
+ __OBJC_$_INSTANCE_METHODS_CCSQLCommandUnion
+ __OBJC_$_INSTANCE_METHODS_CCSerializedSetItemRetriever
+ __OBJC_$_INSTANCE_METHODS_CCSetIntegrityCheck
+ __OBJC_$_INSTANCE_METHODS_CCSetIntegrityCheckResult
+ __OBJC_$_INSTANCE_METHODS_CCSetItemRetriever
+ __OBJC_$_INSTANCE_VARIABLES_CCContentProvenanceRecord
+ __OBJC_$_INSTANCE_VARIABLES_CCDatabaseCommandCache
+ __OBJC_$_INSTANCE_VARIABLES_CCDatabaseItemFieldIndexer
+ __OBJC_$_INSTANCE_VARIABLES_CCDatabaseItemRetriever
+ __OBJC_$_INSTANCE_VARIABLES_CCDatabaseUpdateTracker
+ __OBJC_$_INSTANCE_VARIABLES_CCDatabaseWriter
+ __OBJC_$_INSTANCE_VARIABLES_CCDonationServicePriors
+ __OBJC_$_INSTANCE_VARIABLES_CCIndexedFieldConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CCItemFieldPredicate
+ __OBJC_$_INSTANCE_VARIABLES_CCMetaContentProvenanceRecord
+ __OBJC_$_INSTANCE_VARIABLES_CCProvenanceCompactionRecord
+ __OBJC_$_INSTANCE_VARIABLES_CCProvenanceStateSets
+ __OBJC_$_INSTANCE_VARIABLES_CCSQLCommandCTE
+ __OBJC_$_INSTANCE_VARIABLES_CCSQLCommandUnion
+ __OBJC_$_INSTANCE_VARIABLES_CCSerializedSetItemRetriever
+ __OBJC_$_INSTANCE_VARIABLES_CCSetIntegrityCheckResult
+ __OBJC_$_INSTANCE_VARIABLES_CCSetItemRetriever
+ __OBJC_$_PROP_LIST_CCContentProvenanceRecord
+ __OBJC_$_PROP_LIST_CCDatabaseItemFieldIndexer
+ __OBJC_$_PROP_LIST_CCDatabaseUpdateTracker
+ __OBJC_$_PROP_LIST_CCDatabaseWriter
+ __OBJC_$_PROP_LIST_CCDonationServicePriors
+ __OBJC_$_PROP_LIST_CCIndexedFieldConfiguration
+ __OBJC_$_PROP_LIST_CCItemFieldPredicate
+ __OBJC_$_PROP_LIST_CCItemMetaContent
+ __OBJC_$_PROP_LIST_CCMetaContentProvenanceRecord
+ __OBJC_$_PROP_LIST_CCProvenanceCompactionRecord
+ __OBJC_$_PROP_LIST_CCProvenanceStateSets
+ __OBJC_$_PROP_LIST_CCSQLCommandCTE
+ __OBJC_$_PROP_LIST_CCSQLCommandUnion
+ __OBJC_$_PROP_LIST_CCSetIntegrityCheckResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDatabaseUpdateSummary
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonationService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonationServiceProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCItemFieldEnumerable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCItemMetaContent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCItemRetriever
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCProvenanceRecord
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDatabaseUpdateSummary
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonationServiceProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCItemFieldEnumerable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCItemMetaContent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCItemRetriever
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCProvenanceRecord
+ __OBJC_$_PROTOCOL_REFS_CCDonationServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCDonationServiceServer
+ __OBJC_$_PROTOCOL_REFS_CCItemContent
+ __OBJC_$_PROTOCOL_REFS_CCItemMetaContent
+ __OBJC_$_PROTOCOL_REFS_CCProvenanceRecord
+ __OBJC_CLASS_PROTOCOLS_$_CCContentProvenanceRecord
+ __OBJC_CLASS_PROTOCOLS_$_CCDatabaseItemRetriever
+ __OBJC_CLASS_PROTOCOLS_$_CCDatabaseUpdateTracker
+ __OBJC_CLASS_PROTOCOLS_$_CCDonationServicePriors
+ __OBJC_CLASS_PROTOCOLS_$_CCDonationXPCClient
+ __OBJC_CLASS_PROTOCOLS_$_CCDonationXPCClientFactory
+ __OBJC_CLASS_PROTOCOLS_$_CCItemFieldPredicate
+ __OBJC_CLASS_PROTOCOLS_$_CCMetaContentProvenanceRecord
+ __OBJC_CLASS_PROTOCOLS_$_CCSQLCommandCTE
+ __OBJC_CLASS_PROTOCOLS_$_CCSQLCommandUnion
+ __OBJC_CLASS_PROTOCOLS_$_CCSerializedSetItemRetriever
+ __OBJC_CLASS_RO_$_CCCachedDocumentUtilities
+ __OBJC_CLASS_RO_$_CCContentProvenanceRecord
+ __OBJC_CLASS_RO_$_CCDatabaseCommandCache
+ __OBJC_CLASS_RO_$_CCDatabaseItemFieldIndexer
+ __OBJC_CLASS_RO_$_CCDatabaseItemRetriever
+ __OBJC_CLASS_RO_$_CCDatabaseUpdateTracker
+ __OBJC_CLASS_RO_$_CCDatabaseWriter
+ __OBJC_CLASS_RO_$_CCDonationServicePriors
+ __OBJC_CLASS_RO_$_CCDonationXPCClient
+ __OBJC_CLASS_RO_$_CCDonationXPCClientFactory
+ __OBJC_CLASS_RO_$_CCIndexedFieldConfiguration
+ __OBJC_CLASS_RO_$_CCItemFieldPredicate
+ __OBJC_CLASS_RO_$_CCMaintenenaceXPCClient
+ __OBJC_CLASS_RO_$_CCMetaContentProvenanceRecord
+ __OBJC_CLASS_RO_$_CCProvenanceCompactionRecord
+ __OBJC_CLASS_RO_$_CCProvenanceStateSets
+ __OBJC_CLASS_RO_$_CCSQLCommandCTE
+ __OBJC_CLASS_RO_$_CCSQLCommandUnion
+ __OBJC_CLASS_RO_$_CCSerializedSetItemRetriever
+ __OBJC_CLASS_RO_$_CCSetChangeXPCClient
+ __OBJC_CLASS_RO_$_CCSetIntegrityCheck
+ __OBJC_CLASS_RO_$_CCSetIntegrityCheckResult
+ __OBJC_CLASS_RO_$_CCSetItemRetriever
+ __OBJC_LABEL_PROTOCOL_$_CCDatabaseUpdateSummary
+ __OBJC_LABEL_PROTOCOL_$_CCDonationService
+ __OBJC_LABEL_PROTOCOL_$_CCDonationServiceClient
+ __OBJC_LABEL_PROTOCOL_$_CCDonationServiceProvider
+ __OBJC_LABEL_PROTOCOL_$_CCDonationServiceServer
+ __OBJC_LABEL_PROTOCOL_$_CCItemContent
+ __OBJC_LABEL_PROTOCOL_$_CCItemFieldEnumerable
+ __OBJC_LABEL_PROTOCOL_$_CCItemMetaContent
+ __OBJC_LABEL_PROTOCOL_$_CCItemRetriever
+ __OBJC_LABEL_PROTOCOL_$_CCProvenanceRecord
+ __OBJC_METACLASS_RO_$_CCCachedDocumentUtilities
+ __OBJC_METACLASS_RO_$_CCContentProvenanceRecord
+ __OBJC_METACLASS_RO_$_CCDatabaseCommandCache
+ __OBJC_METACLASS_RO_$_CCDatabaseItemFieldIndexer
+ __OBJC_METACLASS_RO_$_CCDatabaseItemRetriever
+ __OBJC_METACLASS_RO_$_CCDatabaseUpdateTracker
+ __OBJC_METACLASS_RO_$_CCDatabaseWriter
+ __OBJC_METACLASS_RO_$_CCDonationServicePriors
+ __OBJC_METACLASS_RO_$_CCDonationXPCClient
+ __OBJC_METACLASS_RO_$_CCDonationXPCClientFactory
+ __OBJC_METACLASS_RO_$_CCIndexedFieldConfiguration
+ __OBJC_METACLASS_RO_$_CCItemFieldPredicate
+ __OBJC_METACLASS_RO_$_CCMaintenenaceXPCClient
+ __OBJC_METACLASS_RO_$_CCMetaContentProvenanceRecord
+ __OBJC_METACLASS_RO_$_CCProvenanceCompactionRecord
+ __OBJC_METACLASS_RO_$_CCProvenanceStateSets
+ __OBJC_METACLASS_RO_$_CCSQLCommandCTE
+ __OBJC_METACLASS_RO_$_CCSQLCommandUnion
+ __OBJC_METACLASS_RO_$_CCSerializedSetItemRetriever
+ __OBJC_METACLASS_RO_$_CCSetChangeXPCClient
+ __OBJC_METACLASS_RO_$_CCSetIntegrityCheck
+ __OBJC_METACLASS_RO_$_CCSetIntegrityCheckResult
+ __OBJC_METACLASS_RO_$_CCSetItemRetriever
+ __OBJC_PROTOCOL_$_CCDatabaseUpdateSummary
+ __OBJC_PROTOCOL_$_CCDonationService
+ __OBJC_PROTOCOL_$_CCDonationServiceClient
+ __OBJC_PROTOCOL_$_CCDonationServiceProvider
+ __OBJC_PROTOCOL_$_CCDonationServiceServer
+ __OBJC_PROTOCOL_$_CCItemContent
+ __OBJC_PROTOCOL_$_CCItemFieldEnumerable
+ __OBJC_PROTOCOL_$_CCItemMetaContent
+ __OBJC_PROTOCOL_$_CCItemRetriever
+ __OBJC_PROTOCOL_$_CCProvenanceRecord
+ __OBJC_PROTOCOL_REFERENCE_$_CCDonationServiceClient
+ __OBJC_PROTOCOL_REFERENCE_$_CCDonationServiceServer
+ __OBJC_PROTOCOL_REFERENCE_$_CCItemContent
+ __OBJC_PROTOCOL_REFERENCE_$_CCItemMetaContent
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe210106Ev
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEED1Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE7reserveEm
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZTINSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceINS_6vectorIjNS_9allocatorIjEEEENS2_IS4_EEEE
+ ___102-[CCDatabaseWriter _tombstoneMetaContentWithSourceItemIdHash:tombstoneContentIfNoLongerPresent:error:]_block_invoke
+ ___104-[CCDatabaseItemFieldIndexer enumerateInsertCommandsForItemMessage:withBlobPrimaryKey:error:usingBlock:]_block_invoke
+ ___106+[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:version:validity:completion:]_block_invoke
+ ___106-[CCDatabaseWriter(Compaction) _stateSetsForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]_block_invoke
+ ___108+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:serviceOptions:serviceProvider:error:]_block_invoke
+ ___109-[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke
+ ___110-[CCDatabaseSetEnumerator enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:]_block_invoke
+ ___110-[CCDatabaseWriter(Compaction) _combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:]_block_invoke
+ ___110-[CCDatabaseWriter(Compaction) _combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:]_block_invoke_2
+ ___110-[CCDatabaseWriter(Compaction) _combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:]_block_invoke_3
+ ___110-[CCDatabaseWriter(Compaction) _combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:]_block_invoke_4
+ ___111-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]_block_invoke_2
+ ___113+[CCSetDonation(ServiceProviderDeprecations) fullSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
+ ___113-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]_block_invoke
+ ___113-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:]_block_invoke_2
+ ___113-[CCDonationXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]_block_invoke
+ ___114-[CCDonationXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]_block_invoke
+ ___115+[CCDataResource enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:]_block_invoke
+ ___117-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:]_block_invoke
+ ___117-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:]_block_invoke_2
+ ___117-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:]_block_invoke_3
+ ___124-[CCDatabaseWriter(Compaction) _compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:]_block_invoke
+ ___125-[CCDatabaseWriter(Compaction) _updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:]_block_invoke
+ ___131-[CCDataResourceReadAccess enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:]_block_invoke
+ ___131-[CCDataResourceReadAccess enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:]_block_invoke.26
+ ___137+[CCSetDonation(ServiceProviderDeprecations) incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:completion:]_block_invoke
+ ___147-[CCDatabaseSetStateReader enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
+ ___151-[CCDatabaseSetStateReader enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
+ ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
+ ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.12
+ ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_2
+ ___153-[CCDatabaseSetStateReader _enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_3
+ ___23-[CCSetDonation cancel]_block_invoke
+ ___23-[CCSetDonation cancel]_block_invoke.cold.1
+ ___41+[CCSetDonation _defaultXPCClientFactory]_block_invoke
+ ___41-[CCDonationXPCClient cancelSetDonation:]_block_invoke
+ ___43-[CCDatabaseWriter selectAllDeviceRecords:]_block_invoke
+ ___44-[CCDatabaseWriter deleteAllLocalInstances:]_block_invoke
+ ___46-[CCXPCClient remoteObjectProxy:errorHandler:]_block_invoke
+ ___46-[CCXPCClient remoteObjectProxy:errorHandler:]_block_invoke.cold.1
+ ___48-[CCDatabaseWriter _deleteExpiredItemInstances:]_block_invoke
+ ___49-[CCSetDonation _finishWithServiceOptions:error:]_block_invoke
+ ___51-[CCDatabaseWriter _selectLocalDeviceRecord:error:]_block_invoke
+ ___53-[CCSetDonation _removeItemsMatchingPredicate:error:]_block_invoke
+ ___56-[CCDonationXPCClient removeSourceItemIdentifier:reply:]_block_invoke
+ ___58-[CCDonationXPCClient removeItemsMatchingPredicate:reply:]_block_invoke
+ ___58-[CCXPCClient _connectionTerminationHandlerWithErrorCode:]_block_invoke
+ ___58-[CCXPCClient _connectionTerminationHandlerWithErrorCode:]_block_invoke.cold.1
+ ___59-[CCDatabaseWriter _insertDeviceSite:returningRowId:error:]_block_invoke
+ ___62-[CCDatabaseSetEnumerator _searchForKey:options:outSet:error:]_block_invoke
+ ___63-[CCDatabaseWriter(Compaction) _deviceRowIdentifiersWithError:]_block_invoke
+ ___64+[CCSetDonation(Deprecations) deleteSetWithItemType:completion:]_block_invoke
+ ___64-[CCSerializedSetEnumerator _searchForKey:options:outSet:error:]_block_invoke
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke.64
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_10
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_2
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_3
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_4
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_5
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_6
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_7
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_8
+ ___65-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]_block_invoke_9
+ ___67-[CCDatabaseItemRetriever singleSharedItemMatchingPredicate:error:]_block_invoke
+ ___67-[CCDatabaseWriter _rebuildIndexedItemFieldTableWithIndexer:error:]_block_invoke
+ ___68-[CCSetIntegrityCheck checkRunMarkerCorruptionInDatabase:set:error:]_block_invoke
+ ___69-[CCDatabaseItemRetriever singleItemInstanceMatchingPredicate:error:]_block_invoke
+ ___69-[CCDonationXPCClient endSetDonationWithOptions:revisionToken:reply:]_block_invoke
+ ___70+[CCSetDonation(Deprecations) fullSetDonationWithItemType:completion:]_block_invoke
+ ___71-[CCDatabaseWriter _selectMetaContentWithInstanceHash:outRecord:error:]_block_invoke
+ ___72+[CCDatabaseItemFieldIndexer indexerFromConfiguration:forBlobTable:set:]_block_invoke
+ ___72-[CCSetIntegrityCheck checkSequenceGapsAndOverlapsInDatabase:set:error:]_block_invoke
+ ___72-[CCSetIntegrityCheck checkSequenceGapsAndOverlapsInDatabase:set:error:]_block_invoke_2
+ ___72-[CCSetIntegrityCheck checkSequenceGapsAndOverlapsInDatabase:set:error:]_block_invoke_3
+ ___72-[CCSetIntegrityCheck checkSequenceGapsAndOverlapsInDatabase:set:error:]_block_invoke_4
+ ___73-[CCDatabaseSetEnumerator allSetsWithItemType:descriptors:options:error:]_block_invoke
+ ___75-[CCSerializedSetEnumerator allSetsWithItemType:descriptors:options:error:]_block_invoke
+ ___76+[CCSetDonation(Deprecations) deleteSetWithItemType:descriptors:completion:]_block_invoke
+ ___76-[CCDatabaseWriter _selectLatestDeviceRecordWithDeviceUUID:outRecord:error:]_block_invoke
+ ___77+[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:completion:]_block_invoke
+ ___77-[CCDonationXPCClient addItemsWithContents:metaContents:cacheContents:reply:]_block_invoke
+ ___78-[CCDatabaseWriter enumerateLocalInstancesMatchingPredicate:error:usingBlock:]_block_invoke
+ ___80-[CCDatabaseWriter _selectDeviceRecords:withOptions:beyondExpirationDate:error:]_block_invoke
+ ___81-[CCDatabaseItemRetriever _enumerateSharedItemsWithContentHash:error:usingBlock:]_block_invoke
+ ___82+[CCSetDonation(Deprecations) fullSetDonationWithItemType:descriptors:completion:]_block_invoke
+ ___82-[CCDatabaseItemRetriever _enumerateSharedItemsWithInstanceHash:error:usingBlock:]_block_invoke
+ ___83-[CCDatabaseItemRetriever _enumerateItemInstancesWithContentHash:error:usingBlock:]_block_invoke
+ ___84-[CCDatabaseItemRetriever _enumerateItemInstancesWithInstanceHash:error:usingBlock:]_block_invoke
+ ___88-[CCDatabaseWriter _insertIndexedFieldsForItemMessage:withBlobPrimaryKey:indexer:error:]_block_invoke
+ ___89+[CCSetDonation(Deprecations) incrementalSetDonationWithItemType:descriptors:completion:]_block_invoke
+ ___89-[CCDatabaseItemRetriever enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:]_block_invoke
+ ___90-[CCDatabaseItemRetriever _enumerateSharedItemsWithSourceItemIdentifier:error:usingBlock:]_block_invoke
+ ___92-[CCDatabaseItemRetriever _enumerateItemInstancesWithSourceItemIdentifier:error:usingBlock:]_block_invoke
+ ___92-[CCDatabaseWriter selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:]_block_invoke
+ ___92-[CCDatabaseWriter(Compaction) _sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:]_block_invoke
+ ___93-[CCDatabaseItemRetriever _enumerateContentHashesMatchingPredicate:indexer:error:usingBlock:]_block_invoke
+ ___93-[CCDatabaseSetEnumerator enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:]_block_invoke
+ ___94-[CCDatabaseItemRetriever _enumerateInstanceHashesMatchingPredicate:indexer:error:usingBlock:]_block_invoke
+ ___95-[CCDatabaseItemRetriever _enumerateSharedItemsMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke
+ ___95-[CCDatabaseItemRetriever _enumerateSharedItemsMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke_2
+ ___95-[CCSerializedSetEnumerator enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:]_block_invoke
+ ___96-[CCDataResourceWriteAccess _performMaintenanceForSet:withResource:accessAssertion:shouldDefer:]_block_invoke
+ ___96-[CCDataResourceWriteAccess _performMaintenanceForSet:withResource:accessAssertion:shouldDefer:]_block_invoke.cold.1
+ ___97-[CCDatabaseItemRetriever _enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke
+ ___97-[CCDatabaseItemRetriever _enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke_2
+ ___97-[CCDatabaseItemRetriever _enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke_3
+ ___97-[CCDatabaseItemRetriever _enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:]_block_invoke_4
+ ___block_descriptor_32_e20_v20?0C8"NSError"12l
+ ___block_descriptor_32_e38_16?0"CCProvenanceCompactionRecord"8l
+ ___block_descriptor_32_e69_q24?0"CCIndexedFieldConfiguration"8"CCIndexedFieldConfiguration"16l
+ ___block_descriptor_40_e8_32bs_e23_v32?0"NSData"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v24?0"NSObject<CCProvenanceRecord>"8^B16ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0I8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0f8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0d8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ ___block_descriptor_40_e8_32r_e24_v32?0{_NSRange=QQ}8^B24lr32l8
+ ___block_descriptor_40_e8_32r_e27_v16?0"NSMutableIndexSet"8lr32l8
+ ___block_descriptor_40_e8_32r_e39_v24?0"CCContentProvenanceRecord"8^B16lr32l8
+ ___block_descriptor_40_e8_32r_e43_v24?0"CCMetaContentProvenanceRecord"8^B16lr32l8
+ ___block_descriptor_40_e8_32s_e24_v32?0{_NSRange=QQ}8^B24ls32l8
+ ___block_descriptor_40_e8_32s_e35_v16?0"NSObject<CCDatabaseValue>"8ls32l8
+ ___block_descriptor_40_e8_32s_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e59_"CCSQLCommandCriterion"28?0"NSNumber"8"NSIndexSet"16C24ls32l8
+ ___block_descriptor_41_e8_32s_e24_v32?0{_NSRange=QQ}8^B24ls32l8
+ ___block_descriptor_41_e8_32s_e44_v32?0"NSNumber"8"NSMutableIndexSet"16^B24ls32l8
+ ___block_descriptor_48_e8_32bs40r_e22_v24?0"NSNumber"8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e26_v24?0"CCSharedItem"8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"CCItemInstance"8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0C8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v16?0"CCSet"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e18_B16?0"NSNumber"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e26_B16?0"CCDatabaseInsert"8ls32l8r40l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32s40bs_e42_v24?0"NSObject<CCProvenanceRecord>"8^B16ls32l8s40l8
+ ___block_descriptor_50_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e19_v24?0"CCSet"8^B16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32bs40r48r_e28_v24?0"CCDataResource"8^B16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32r_e27_v16?0"NSMutableIndexSet"8lr32l8
+ ___block_descriptor_56_e8_32s40r48r_e18_B16?0"NSNumber"8lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e26_v24?0"CCSharedItem"8^B16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e28_v24?0"CCItemInstance"8^B16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e15_v16?0"CCSet"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e21_v16?0"CCItemField"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40s48r56r_e48_v28?0C8"NSError"12"CCDonationServicePriors"20ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e22_v24?0"NSNumber"8^B16ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e28_v24?0"CCDataResource"8^B16lr56l8s48l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_74_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r72r_e24_v32?0{_NSRange=QQ}8^B24lr64l8s32l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_82_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e38_v16?0"NSObject<CCDatabaseValueRow>"8lr48l8r56l8r64l8r72l8s32l8s40l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64bs72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8r80l8r88l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24ls32l8s40l8r80l8s72l8s48l8s56l8s64l8
+ ___block_literal_global.249
+ ___block_literal_global.85
+ ___getCCAppIntentsIndexedEntityMetaContentClass_block_invoke
+ ___getCCAppIntentsIndexedEntityMetaContentClass_block_invoke.cold.1
+ ___getCCCachedDocumentContentClass_block_invoke
+ ___getCCCachedDocumentContentClass_block_invoke.cold.1
+ ___getCCCachedDocumentMetaContentClass_block_invoke
+ ___getCCCachedDocumentMetaContentClass_block_invoke.cold.1
+ __defaultXPCClientFactory.onceToken
+ __defaultXPCClientFactory.sharedFactory
+ __os_feature_enabled_impl
+ __os_log_default
+ __sqlite3_maintain_load_factor
+ __sqlite_trace_callback
+ _block_copy_helper.45
+ _block_descriptor.47
+ _block_destroy_helper.46
+ _getCCAppIntentsIndexedEntityMetaContentClass.softClass
+ _getCCCachedDocumentContentClass
+ _getCCCachedDocumentContentClass.softClass
+ _getCCCachedDocumentMetaContentClass.softClass
+ _get_type_metadata 15Synchronization5MutexVySbG noncopyable.11
+ _kCFNull
+ _objc_msgSend$_addItem:cacheContent:error:
+ _objc_msgSend$_ageOfMaintenanceFromPriorRunCount:maintenanceHistory:
+ _objc_msgSend$_atomicallyCreateDataResource:withResourceGeneration:
+ _objc_msgSend$_atomicallyRemoveDataResource:
+ _objc_msgSend$_calculateMinimumTombstoneAgeWithMaintenanceHistory:
+ _objc_msgSend$_combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:
+ _objc_msgSend$_compactContiguousTombstonesForDeviceRowId:minimumTombstoneAge:shouldDefer:error:
+ _objc_msgSend$_compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:
+ _objc_msgSend$_connectionTerminationHandlerWithErrorCode:
+ _objc_msgSend$_countDeviceRecords:withOptions:error:
+ _objc_msgSend$_createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:
+ _objc_msgSend$_currentPersonaShouldSkipEnumeratingContainer:
+ _objc_msgSend$_currentPersonaShouldSkipEnumeratingResource:
+ _objc_msgSend$_deduplicateRemovedObjects:withAdded:presentNonAdded:outAll:outAdded:outRemoved:
+ _objc_msgSend$_defaultXPCClientFactory
+ _objc_msgSend$_deleteDeviceRowId:error:
+ _objc_msgSend$_deleteExpiredItemInstances:
+ _objc_msgSend$_deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:
+ _objc_msgSend$_deleteRecordsWithRowIds:vectorType:error:
+ _objc_msgSend$_deleteSetWithItemType:descriptors:serviceProvider:error:
+ _objc_msgSend$_deviceRowIdentifiersWithError:
+ _objc_msgSend$_enumerateContentHashesMatchingPredicate:indexer:error:usingBlock:
+ _objc_msgSend$_enumerateInstanceHashesMatchingPredicate:indexer:error:usingBlock:
+ _objc_msgSend$_enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:
+ _objc_msgSend$_enumerateItemInstancesWithContentHash:error:usingBlock:
+ _objc_msgSend$_enumerateItemInstancesWithInstanceHash:error:usingBlock:
+ _objc_msgSend$_enumerateItemInstancesWithItemIdentifier:itemIdentifierType:error:usingBlock:
+ _objc_msgSend$_enumerateItemInstancesWithSourceItemIdentifier:error:usingBlock:
+ _objc_msgSend$_enumerateLocalInstancesWithError:selectingOnlyUnwritten:usingBlock:
+ _objc_msgSend$_enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
+ _objc_msgSend$_enumerateSharedItemsMatchingIndexedFieldPredicate:error:usingBlock:
+ _objc_msgSend$_enumerateSharedItemsWithContentHash:error:usingBlock:
+ _objc_msgSend$_enumerateSharedItemsWithInstanceHash:error:usingBlock:
+ _objc_msgSend$_enumerateSharedItemsWithItemIdentifier:itemIdentifierType:error:usingBlock:
+ _objc_msgSend$_enumerateSharedItemsWithSourceItemIdentifier:error:usingBlock:
+ _objc_msgSend$_errorForUnexpectedRow:fromCommand:
+ _objc_msgSend$_executeCreateTableStatements:error:
+ _objc_msgSend$_executePragma:outError:
+ _objc_msgSend$_expireAndTombstoneAllContentProvenanceForDeviceRowId:error:
+ _objc_msgSend$_expireDeviceRowId:error:
+ _objc_msgSend$_finishWithServiceOptions:error:
+ _objc_msgSend$_fullSetDonationWithItemType:descriptors:options:serviceProvider:error:
+ _objc_msgSend$_incrementCachedIntegerWithKey:error:
+ _objc_msgSend$_incrementLocalDeltaGeneration:
+ _objc_msgSend$_incrementalSetDonationWithItemType:descriptors:options:serviceProvider:error:
+ _objc_msgSend$_incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:error:
+ _objc_msgSend$_indexerForPredicate:error:
+ _objc_msgSend$_initWithInnerData:error:
+ _objc_msgSend$_insertContent:contentHash:outExists:error:
+ _objc_msgSend$_insertContentProvenanceWithDeviceRowId:contentHash:sequenceNumber:error:
+ _objc_msgSend$_insertDeviceSite:returningRowId:error:
+ _objc_msgSend$_insertIndexedFieldsForItemMessage:withBlobPrimaryKey:indexer:error:
+ _objc_msgSend$_insertLocalContentWithProvenance:contentHash:isNew:error:
+ _objc_msgSend$_insertMetaContent:instanceHash:outIsDuplicate:error:
+ _objc_msgSend$_insertMetaContentProvenanceWithSourceItemIdHash:instanceHash:contentHash:error:
+ _objc_msgSend$_keyData
+ _objc_msgSend$_markTombstoneRowForVectorType:provenanceRowId:sequenceRange:error:
+ _objc_msgSend$_pas_mappedArrayWithTransform:
+ _objc_msgSend$_performMaintenanceForSet:withResource:accessAssertion:shouldDefer:
+ _objc_msgSend$_persistCachedIntegers:
+ _objc_msgSend$_priorRevisionTokenOrEmptyDictionary
+ _objc_msgSend$_processRange:deviceRowId:vectorType:stateSets:error:shouldDefer:
+ _objc_msgSend$_produceSelectClauseWithTableName:columnNames:count:distinct:
+ _objc_msgSend$_purgeTombstonedResources:
+ _objc_msgSend$_rebuildIndexedItemFieldTableWithIndexer:error:
+ _objc_msgSend$_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:
+ _objc_msgSend$_removeItemsMatchingPredicate:error:
+ _objc_msgSend$_resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:
+ _objc_msgSend$_resourceIsUserWithPotentialDomainOverrides:
+ _objc_msgSend$_searchForKey:options:outSet:error:
+ _objc_msgSend$_selectContentProvenenceWithContentHash:deviceRowId:outSequenceNumber:error:
+ _objc_msgSend$_selectDeviceRecords:withOptions:beyondExpirationDate:error:
+ _objc_msgSend$_selectLatestDeviceRecordWithDeviceUUID:outRecord:error:
+ _objc_msgSend$_selectLocalDeviceRecord:error:
+ _objc_msgSend$_selectLocalInstanceCount:error:
+ _objc_msgSend$_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:error:
+ _objc_msgSend$_selectMetaContentWithInstanceHash:outRecord:error:
+ _objc_msgSend$_selectPersistedValueForKey:outValue:valueClass:error:
+ _objc_msgSend$_setDatabase:
+ _objc_msgSend$_setDonationWithItemType:descriptors:version:validity:serviceOptions:serviceProvider:error:
+ _objc_msgSend$_shouldFilterOutSet:withOptionsFilter:
+ _objc_msgSend$_shouldSkipEnumeratingResourceForAccessError:
+ _objc_msgSend$_sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:
+ _objc_msgSend$_stateSetsForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:
+ _objc_msgSend$_temporaryDirectoryForDataResource:
+ _objc_msgSend$_tombstoneContentProvenanceRowsForExpiredDeviceRowId:error:
+ _objc_msgSend$_tombstoneMetaContentWithSourceItemIdHash:tombstoneContentIfNoLongerPresent:error:
+ _objc_msgSend$_updateDeviceRowId:deltaGeneration:expirationDate:error:
+ _objc_msgSend$_updateLocalSourceVersion:localSourceValidityHash:error:
+ _objc_msgSend$_updateMaintenanceHistory:
+ _objc_msgSend$_updateMetaContent:tombstoneContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:
+ _objc_msgSend$_updateModifiedRowCount
+ _objc_msgSend$_updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:
+ _objc_msgSend$_upsertInteger:forKey:error:
+ _objc_msgSend$_upsertInteger:forKey:skipIfNil:error:
+ _objc_msgSend$_validateAndExtractKeyPrefixedIdentifier:outItemIdentifierType:outItemIdentifier:error:
+ _objc_msgSend$_validateItemCacheContent:error:
+ _objc_msgSend$_validateRow:fromCommmand:outItemInstance:error:
+ _objc_msgSend$_validateRow:fromCommmand:outSharedItem:error:
+ _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:error:
+ _objc_msgSend$accessAssertion
+ _objc_msgSend$addItemsWithContents:metaContents:cacheContents:reply:
+ _objc_msgSend$allSetsWithItemType:descriptors:options:error:
+ _objc_msgSend$allSetsWithItemType:options:error:
+ _objc_msgSend$allowsAccessToAllSetsWithMode:
+ _objc_msgSend$appendAddedDevice:
+ _objc_msgSend$appendAddedLocalInstance:
+ _objc_msgSend$appendDatabaseValues:fromItemField:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendPresentNonAddedDevice:
+ _objc_msgSend$appendPresentNonAddedLocalInstance:
+ _objc_msgSend$appendRemovedDevice:
+ _objc_msgSend$appendRemovedLocalInstance:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$beginReadTransactionWithError:
+ _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:
+ _objc_msgSend$beginUpdateForDonationRequest:withDatabase:changeNotifier:error:
+ _objc_msgSend$beginUpdateForMaintenanceOfSet:withDatabase:changeNotifier:error:
+ _objc_msgSend$beginUpdateForPreparationOfSet:withDatabase:error:
+ _objc_msgSend$beginWriteTransactionWithError:
+ _objc_msgSend$blobTableName
+ _objc_msgSend$bytesValueNoCopy
+ _objc_msgSend$cacheDescriptorsFromAssociatedSet:error:
+ _objc_msgSend$cancelSetDonation:
+ _objc_msgSend$checkRunMarkerCorruptionInDatabase:set:error:
+ _objc_msgSend$checkSequenceGapsAndOverlapsInDatabase:set:error:
+ _objc_msgSend$clientWithId:
+ _objc_msgSend$columnNamesOfTable:error:
+ _objc_msgSend$commandForKey:
+ _objc_msgSend$commitUpdate:
+ _objc_msgSend$compactContiguousTombstonesWithMinimumTombstoneAge:shouldDefer:error:
+ _objc_msgSend$compactedSequencesLock
+ _objc_msgSend$configuredColumnNames
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$connectionErrorCode
+ _objc_msgSend$connectionToDatabaseAtURL:dataProtectionClass:openMode:busyTimeout:accessAssertion:
+ _objc_msgSend$containsIndex:
+ _objc_msgSend$copyWithFieldType:
+ _objc_msgSend$criterionWithColumnName:GREATERTHANColumnValue:
+ _objc_msgSend$criterionWithColumnName:INColumnValues:
+ _objc_msgSend$criterionWithColumnName:sqlOperator:columnValue:
+ _objc_msgSend$dataProtectionClass
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$decodeFieldValuesFromData:error:
+ _objc_msgSend$deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord:
+ _objc_msgSend$deleteSetWithItemType:descriptors:error:
+ _objc_msgSend$deleteSetWithItemType:error:
+ _objc_msgSend$deleteSourceItemIdHash:error:
+ _objc_msgSend$deletedDate
+ _objc_msgSend$deletedRunLength
+ _objc_msgSend$deltaProduced
+ _objc_msgSend$descriptionForSet:
+ _objc_msgSend$descriptorAllowList
+ _objc_msgSend$descriptorAllowList:allowsSet:
+ _objc_msgSend$domainIdentifier
+ _objc_msgSend$donationWithName:itemType:service:serviceOptions:errorCode:priors:
+ _objc_msgSend$dropTableIfExistsWithName:
+ _objc_msgSend$eligibleSequences
+ _objc_msgSend$endSetDonationWithOptions:revisionToken:reply:
+ _objc_msgSend$enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:
+ _objc_msgSend$enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:
+ _objc_msgSend$enumerateAllSetsWithItemType:error:usingBlock:
+ _objc_msgSend$enumerateAllSetsWithOptions:error:usingBlock:
+ _objc_msgSend$enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
+ _objc_msgSend$enumerateInsertCommandsForItemMessage:withBlobPrimaryKey:error:usingBlock:
+ _objc_msgSend$enumerateItemInstancesMatchingPredicate:error:usingBlock:
+ _objc_msgSend$enumerateLocalInstancesMatchingPredicate:error:usingBlock:
+ _objc_msgSend$enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumerateRangesInRange:options:usingBlock:
+ _objc_msgSend$enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:
+ _objc_msgSend$enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:
+ _objc_msgSend$enumerateSharedItemsMatchingPredicate:error:usingBlock:
+ _objc_msgSend$enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:
+ _objc_msgSend$errorDomain
+ _objc_msgSend$expirationDateFieldType
+ _objc_msgSend$finalizeSetChange
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$hasContentHash:
+ _objc_msgSend$hasContentInformation
+ _objc_msgSend$hasMetaContentInformation
+ _objc_msgSend$html
+ _objc_msgSend$indexedFieldType
+ _objc_msgSend$indexedFields
+ _objc_msgSend$indexedItemFieldCount
+ _objc_msgSend$indexerFromConfiguration:forBlobTable:set:
+ _objc_msgSend$init
+ _objc_msgSend$initLazyDecodedWithTrustedItemMessageData:error:
+ _objc_msgSend$initWithAssertionOverride:changeNotifier:
+ _objc_msgSend$initWithContent:metaContent:error:
+ _objc_msgSend$initWithContentHash:contentSequenceNumber:contentDeletedRunLength:contentData:sourceItemIdHash:instanceHash:metaContentSequenceNumber:metaContentDeletedRunLength:metaContentData:deviceRowId:
+ _objc_msgSend$initWithFieldType:dataType:indexedFieldType:descriptorAllowList:
+ _objc_msgSend$initWithIndexedFieldConfiguration:blobTableName:itemType:
+ _objc_msgSend$initWithIndexesInRange:
+ _objc_msgSend$initWithIneligibleSequences:eligibleSequences:compactedSequences:
+ _objc_msgSend$initWithItemMessageData:error:
+ _objc_msgSend$initWithName:itemType:service:serviceOptions:errorCode:priors:flushThreshold:
+ _objc_msgSend$initWithName:select:
+ _objc_msgSend$initWithPassed:checksPerformed:checksFailed:issues:
+ _objc_msgSend$initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:busyTimeout:cacheSpill:
+ _objc_msgSend$initWithPredicateType:fieldType:value:operatorType:
+ _objc_msgSend$initWithRemoteObjectInterface:exportedInterface:connection:clientId:useCase:
+ _objc_msgSend$initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:useCase:
+ _objc_msgSend$initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:useCase:
+ _objc_msgSend$initWithRowId:
+ _objc_msgSend$initWithSelects:
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$initWithSet:database:changeNotifier:request:isPrepared:error:
+ _objc_msgSend$initWithSet:retriever:
+ _objc_msgSend$initWithSharedIdentifier:
+ _objc_msgSend$initWithSharedIdentifier:instanceIdentifier:content:metaContent:sourceItemIdentifierHash:
+ _objc_msgSend$initWithSourceItemIdentifier:associatedInstanceUUID:associatedDomainIdentifier:expirationDate:documentType:error:
+ _objc_msgSend$initWithTable:joinType:joinCriterion:
+ _objc_msgSend$initWithText:html:error:
+ _objc_msgSend$int32Value
+ _objc_msgSend$int64Value
+ _objc_msgSend$interruptionErrorCode
+ _objc_msgSend$invalidationErrorCode
+ _objc_msgSend$isCacheEnabledSourceIdentifier:
+ _objc_msgSend$isEqualToItemFieldPredicate:
+ _objc_msgSend$isEqualToRecord:
+ _objc_msgSend$isFieldType:applicableToBlobTable:
+ _objc_msgSend$isSourceItemIdentifierFieldType:
+ _objc_msgSend$isValidPredicate:error:
+ _objc_msgSend$itemCacheContentWithText:html:error:
+ _objc_msgSend$itemFieldTableName
+ _objc_msgSend$itemMessageData
+ _objc_msgSend$itemMessageSubclass
+ _objc_msgSend$itemRetrieverForSet:database:
+ _objc_msgSend$itemRetrieverForSet:database:setConfiguration:contentIndexer:metaContentIndexer:
+ _objc_msgSend$itemRetrieverForSet:readAccess:
+ _objc_msgSend$itemRetrieverForSet:useCase:
+ _objc_msgSend$itemRetrieverWithUseCase:
+ _objc_msgSend$itemTypeForFieldType:error:
+ _objc_msgSend$keyPrefixedIdentifierForItemInstance:
+ _objc_msgSend$keyPrefixedIdentifierForSharedItem:
+ _objc_msgSend$lazilyDecodedContentMessageForItemType:trustedItemMessageData:error:
+ _objc_msgSend$lazilyDecodedMetaContentMessageForItemType:trustedItemMessageData:error:
+ _objc_msgSend$localDeviceRowId
+ _objc_msgSend$localInstanceAddedCount
+ _objc_msgSend$localInstanceDeltaProduced
+ _objc_msgSend$localInstanceRemovedCount
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$noBusyWait
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$operatorType
+ _objc_msgSend$performMaintenanceOnAllSets:clientId:shouldDeferBlock:
+ _objc_msgSend$performMaintenanceWithShouldTombstone:shouldDefer:error:
+ _objc_msgSend$predicateType
+ _objc_msgSend$predicateWithFieldType:equalsDataValue:error:
+ _objc_msgSend$predicateWithFieldType:lessThanNumberValue:error:
+ _objc_msgSend$predicateWithSharedItemIdentifier:error:
+ _objc_msgSend$predicateWithSourceItemIdentifier:error:
+ _objc_msgSend$prepareDatabaseWithLocalDeviceSite:error:
+ _objc_msgSend$prepareItemFieldIndexes:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$protectionClass
+ _objc_msgSend$rawEnumValue
+ _objc_msgSend$recursivelyEnumerateFieldsWithError:usingBlock:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$remoteObjectProxy:errorHandler:
+ _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:
+ _objc_msgSend$removeIndexesInRange:
+ _objc_msgSend$removeItemsMatchingPredicate:reply:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeSourceItemIdentifier:reply:
+ _objc_msgSend$repeatedBoolValue
+ _objc_msgSend$repeatedBytesValueNoCopy
+ _objc_msgSend$repeatedDoubleValue
+ _objc_msgSend$repeatedFloatValue
+ _objc_msgSend$repeatedInt32Value
+ _objc_msgSend$repeatedInt64Value
+ _objc_msgSend$repeatedRawEnumValue
+ _objc_msgSend$repeatedStringValueNoCopy
+ _objc_msgSend$repeatedUInt32Value
+ _objc_msgSend$repeatedUInt64Value
+ _objc_msgSend$rollbackUpdate:
+ _objc_msgSend$rowId
+ _objc_msgSend$select
+ _objc_msgSend$selectFromTableWithName:columns:count:distinct:joinTables:criterion:order:limit:offset:ctes:unionSelects:unionAll:
+ _objc_msgSend$selects
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$setCommand:forKey:
+ _objc_msgSend$setCommonTableExpressions:
+ _objc_msgSend$setConfigurationForItemType:
+ _objc_msgSend$setConnectionErrorCode:
+ _objc_msgSend$setDistinct:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setJoinTables:
+ _objc_msgSend$setLocalInstanceAddedCount:
+ _objc_msgSend$setLocalInstanceRemovedCount:
+ _objc_msgSend$setModifiedRowCount:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setSharedItem:
+ _objc_msgSend$setSharedItemAddedCount:
+ _objc_msgSend$setSharedItemRemovedCount:
+ _objc_msgSend$setSharedItemRevisedCount:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$setUnionWithSelects:unionAll:
+ _objc_msgSend$sharedItemAddedCount
+ _objc_msgSend$sharedItemRemovedCount
+ _objc_msgSend$sharedItemRevisedCount
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$singleItemInstanceMatchingPredicate:error:
+ _objc_msgSend$singleSharedItemMatchingPredicate:error:
+ _objc_msgSend$sourceItemIdentifierHash
+ _objc_msgSend$startFullSetDonationWithItemType:descriptors:error:
+ _objc_msgSend$startFullSetDonationWithItemType:descriptors:options:error:
+ _objc_msgSend$startFullSetDonationWithItemType:error:
+ _objc_msgSend$startIncrementalSetDonationWithItemType:descriptors:error:
+ _objc_msgSend$startIncrementalSetDonationWithItemType:descriptors:options:error:
+ _objc_msgSend$startIncrementalSetDonationWithItemType:descriptors:version:validity:error:
+ _objc_msgSend$startIncrementalSetDonationWithItemType:error:
+ _objc_msgSend$stringForItemFieldDataType:
+ _objc_msgSend$stringValueNoCopy
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$text
+ _objc_msgSend$tombstoneResource:
+ _objc_msgSend$uint32Value
+ _objc_msgSend$uint64Value
+ _objc_msgSend$unsafeGuardedData
+ _objc_msgSend$validateItemCacheContent:error:
+ _objc_msgSend$writtenDate
+ _objectdestroy.15Tm
+ _sqlite3_sql
+ _sqlite3_trace_v2
+ _swift_bridgeObjectRelease_n
- +[CCDataResourceWriter defaultDataProtectionClass]
- +[CCDataResourceWriter incrementRowsModified:database:]
- +[CCDataResourceWriter incrementRowsModified:database:].cold.1
- +[CCDataResourceWriter incrementRowsModified:database:].cold.2
- +[CCDatabaseConnection connectionToDatabaseAtURL:dataProtectionClass:openMode:accessAssertion:]
- +[CCDatabaseJoinedProvenance joinedProvenanceFromDatabaseValueRow:].cold.1
- +[CCDatabaseUpdater _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:]
- +[CCDatabaseUpdater selectLocalSourceValidityHashInDatabase:error:]
- +[CCDatabaseUpdater selectLocalSourceVersionInDatabase:error:]
- +[CCDatabaseUpdater selectRowsModifiedCountInDatabase:error:]
- +[CCDatabaseUpdater updaterForDatabase:]
- +[CCDatabaseUpdater updaterForDonateRequest:toDatabase:]
- +[CCDatabaseUpdater updaterForDonateRequest:toDatabase:].cold.1
- +[CCDatabaseUpdater upsertLastMaintenanceDate:database:error:]
- +[CCDatabaseUpdater upsertRowsModified:database:error:]
- +[CCDonateServicePriors supportsSecureCoding]
- +[CCInstanceRecord genSQLCreateStatements]
- +[CCInstanceRecord recordFromDatabaseValueRow:]
- +[CCInstanceRecord tableName]
- +[CCProvenanceRecord genSQLCreateStatements]
- +[CCProvenanceRecord recordFromDatabaseValueRow:]
- +[CCProvenanceRecord tableName]
- +[CCSQLCommandGenerator _produceSelectClauseWithTableName:columnNames:count:]
- +[CCSQLCommandGenerator selectFromTableWithName:columns:count:join:criterion:order:limit:offset:]
- +[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]
- +[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:].cold.1
- +[CCSetDonation deleteSetWithItemType:descriptors:completion:]
- +[CCSetDonation deleteSetWithItemType:descriptors:serviceProvider:completion:]
- +[CCSetDonation donationWithName:itemType:service:errorCode:priors:]
- +[CCSetDonation fullSetDonationWithItemType:completion:]
- +[CCSetDonation fullSetDonationWithItemType:descriptors:completion:]
- +[CCSetDonation fullSetDonationWithItemType:descriptors:serviceProvider:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:descriptors:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:descriptors:version:validity:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:completion:]
- +[CCSetDonation remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:]
- -[CCDataResourceReadAccess _isDefaultPersonaRequestingUserResource:]
- -[CCDataResourceReadAccess _shouldEnumerateContainer:]
- -[CCDataResourceReadAccess _shouldEnumerateContainer:].cold.1
- -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]
- -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:].cold.1
- -[CCDataResourceWriteAccess initWithAssertionOverride:]
- -[CCDataResourceWriteAccess purgeTombstonedResources:]
- -[CCDataResourceWriteAccess purgeTombstonedResources:].cold.1
- -[CCDataResourceWriteAccess setWriterForSet:accessAssertion:]
- -[CCDataResourceWriter .cxx_destruct]
- -[CCDataResourceWriter _cleanupDatabaseIfRequired]
- -[CCDataResourceWriter _cleanupDatabaseIfRequired].cold.1
- -[CCDataResourceWriter _cleanupDatabaseIfRequired].cold.2
- -[CCDataResourceWriter _cleanupDatabaseIfRequired].cold.3
- -[CCDataResourceWriter _cleanupDatabaseIfRequired].cold.4
- -[CCDataResourceWriter _cleanupDatabaseIfRequired].cold.5
- -[CCDataResourceWriter _clearTombstoneStatus:]
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:]
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.1
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.2
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.3
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.4
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.5
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.6
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.7
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.8
- -[CCDataResourceWriter _createDatabaseWithLocalDeviceSite:].cold.9
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.1
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.2
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.3
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.4
- -[CCDataResourceWriter _executeDatabaseTransactionUsingBlock:]
- -[CCDataResourceWriter _executeDatabaseTransactionUsingBlock:].cold.1
- -[CCDataResourceWriter _executeDatabaseTransactionUsingBlock:].cold.2
- -[CCDataResourceWriter _executeDatabaseTransactionUsingBlock:].cold.3
- -[CCDataResourceWriter _executeDatabaseTransactionUsingBlock:].cold.4
- -[CCDataResourceWriter _loadDatabase:]
- -[CCDataResourceWriter _removeResource:]
- -[CCDataResourceWriter _removeResource:].cold.1
- -[CCDataResourceWriter _removeResource:].cold.2
- -[CCDataResourceWriter _removeResource:].cold.3
- -[CCDataResourceWriter _temporaryDirectoryURLWithError:]
- -[CCDataResourceWriter _temporaryDirectoryURLWithError:].cold.1
- -[CCDataResourceWriter _temporaryDirectoryURLWithError:].cold.2
- -[CCDataResourceWriter _tombstoneResource:]
- -[CCDataResourceWriter clearTombstoneStatus:]
- -[CCDataResourceWriter dataResource]
- -[CCDataResourceWriter description]
- -[CCDataResourceWriter initWithDataResource:accessAssertion:]
- -[CCDataResourceWriter initializeDatabaseWithLocalDeviceSite:]
- -[CCDataResourceWriter performMaintenance:shouldDefer:]
- -[CCDataResourceWriter removeResource:]
- -[CCDataResourceWriter submitDatabaseTransactionUsingBlock:]
- -[CCDataResourceWriter tombstoneResource:]
- -[CCDatabaseConnection _createTableWithRecordClass:error:]
- -[CCDatabaseConnection beginTransactionWithError:]
- -[CCDatabaseConnection beginTransactionWithError:].cold.1
- -[CCDatabaseConnection cleanup:]
- -[CCDatabaseConnection cleanup:].cold.1
- -[CCDatabaseConnection prepareWithError:]
- -[CCDatabaseConnection prepareWithError:].cold.1
- -[CCDatabaseJoinedProvenance initWithProvenance:contentData:metaContentData:]
- -[CCDatabaseJoinedProvenance provenance]
- -[CCDatabaseSelectBuilder setJoinWithType:tables:]
- -[CCDatabaseSetEnumerator allSetsWithOptions:itemType:descriptors:error:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:usingBlock:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:].cold.1
- -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:]
- -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:].cold.1
- -[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:].cold.2
- -[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]
- -[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:].cold.1
- -[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]
- -[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:].cold.1
- -[CCDatabaseUpdater .cxx_destruct]
- -[CCDatabaseUpdater _deleteDeviceRowId:]
- -[CCDatabaseUpdater _deleteDeviceRowId:].cold.1
- -[CCDatabaseUpdater _deleteSourceItemIdHash:outProvenanceRowId:]
- -[CCDatabaseUpdater _deleteSourceItemIdHash:outProvenanceRowId:].cold.1
- -[CCDatabaseUpdater _deleteSourceItemIdHash:outProvenanceRowId:].cold.2
- -[CCDatabaseUpdater _enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:]
- -[CCDatabaseUpdater _enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:].cold.1
- -[CCDatabaseUpdater _enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:].cold.2
- -[CCDatabaseUpdater _enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:].cold.3
- -[CCDatabaseUpdater _expireAndTombstoneAllProvenanceForDeviceRowId:]
- -[CCDatabaseUpdater _expireDeviceRowId:]
- -[CCDatabaseUpdater _expireDeviceRowId:].cold.1
- -[CCDatabaseUpdater _expireDeviceRowId:].cold.2
- -[CCDatabaseUpdater _incrementCachedIntegerWithKey:]
- -[CCDatabaseUpdater _incrementCachedIntegerWithKey:].cold.1
- -[CCDatabaseUpdater _incrementLocalDeltaGeneration]
- -[CCDatabaseUpdater _incrementLocalDeltaGeneration].cold.1
- -[CCDatabaseUpdater _insertContent:contentHash:outExists:]
- -[CCDatabaseUpdater _insertContent:contentHash:outExists:].cold.1
- -[CCDatabaseUpdater _insertContent:contentHash:outSequenceNumber:]
- -[CCDatabaseUpdater _insertDeviceSite:returningRowId:]
- -[CCDatabaseUpdater _insertDeviceSite:returningRowId:].cold.1
- -[CCDatabaseUpdater _insertLocalInstanceForItemWithSourceItemIdHash:provenanceRowId:]
- -[CCDatabaseUpdater _insertLocalInstanceForItemWithSourceItemIdHash:provenanceRowId:].cold.1
- -[CCDatabaseUpdater _insertMetaContent:instanceHash:outSequenceNumber:outIsDuplicate:]
- -[CCDatabaseUpdater _insertMetaContent:instanceHash:outSequenceNumber:outIsDuplicate:].cold.1
- -[CCDatabaseUpdater _insertNewProvenanceAndTombstonePriorProvenanceRow:outInsertedProvenanceRowId:instanceHash:contentHash:contentSequenceNumber:metaContentSequenceNumber:contentChanged:]
- -[CCDatabaseUpdater _insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:]
- -[CCDatabaseUpdater _insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:].cold.1
- -[CCDatabaseUpdater _persistCachedIntegers]
- -[CCDatabaseUpdater _persistDateWithDeltaProduced:isFullSet:]
- -[CCDatabaseUpdater _persistRevisionTokenIfNotNil:]
- -[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:]
- -[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:].cold.1
- -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:]
- -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.1
- -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.2
- -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.3
- -[CCDatabaseUpdater _selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:]
- -[CCDatabaseUpdater _selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:].cold.1
- -[CCDatabaseUpdater _selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:].cold.2
- -[CCDatabaseUpdater _selectLocalDeviceRecord:]
- -[CCDatabaseUpdater _selectLocalDeviceRecord:].cold.1
- -[CCDatabaseUpdater _selectLocalInstanceCount:]
- -[CCDatabaseUpdater _selectLocalInstanceCount:].cold.1
- -[CCDatabaseUpdater _selectLocalInstanceCount:].cold.2
- -[CCDatabaseUpdater _selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:]
- -[CCDatabaseUpdater _selectMetaContentWithInstanceHash:outRecord:]
- -[CCDatabaseUpdater _selectMetaContentWithInstanceHash:outRecord:].cold.1
- -[CCDatabaseUpdater _selectPersistedValueForKey:outValue:valueClass:]
- -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:]
- -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.1
- -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.2
- -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.3
- -[CCDatabaseUpdater _selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:].cold.4
- -[CCDatabaseUpdater _selectProvenenceWithRowId:outInstanceHash:outContentHash:]
- -[CCDatabaseUpdater _selectProvenenceWithRowId:outInstanceHash:outContentHash:].cold.1
- -[CCDatabaseUpdater _selectProvenenceWithRowId:outInstanceHash:outContentHash:].cold.2
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:]
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.1
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.2
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.3
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.4
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.5
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.6
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.7
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.8
- -[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:].cold.9
- -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:]
- -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.1
- -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.2
- -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.3
- -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:]
- -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.1
- -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.2
- -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.3
- -[CCDatabaseUpdater _updateLocalInstanceRowId:provenanceRowId:]
- -[CCDatabaseUpdater _updateLocalInstanceRowId:provenanceRowId:].cold.1
- -[CCDatabaseUpdater _updateLocalInstanceRowId:provenanceRowId:].cold.2
- -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:]
- -[CCDatabaseUpdater _upsertInteger:forKey:]
- -[CCDatabaseUpdater _upsertInteger:forKey:skipIfNil:]
- -[CCDatabaseUpdater _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:]
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:]
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.1
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.2
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.3
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.4
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.5
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.6
- -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.7
- -[CCDatabaseUpdater deleteAllLocalInstances]
- -[CCDatabaseUpdater deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord]
- -[CCDatabaseUpdater deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord].cold.1
- -[CCDatabaseUpdater deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord].cold.2
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.1
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.2
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.3
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.4
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.5
- -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.6
- -[CCDatabaseUpdater deleteSourceItemIdHash:]
- -[CCDatabaseUpdater description]
- -[CCDatabaseUpdater enumerateUnmodifiedLocalInstancesUsingBlock:]
- -[CCDatabaseUpdater expireRemoteDeviceUUID:]
- -[CCDatabaseUpdater finishAndDetectDelta:updateRevisionToken:isFullSet:]
- -[CCDatabaseUpdater initWithDatabase:request:]
- -[CCDatabaseUpdater initWithDatabase:request:].cold.1
- -[CCDatabaseUpdater insertContent:contentHash:sequenceNumber:onDeviceRowId:]
- -[CCDatabaseUpdater insertContent:contentHash:sequenceNumber:onDeviceRowId:].cold.1
- -[CCDatabaseUpdater insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:]
- -[CCDatabaseUpdater localDeviceRecord]
- -[CCDatabaseUpdater localInstanceAddedCount]
- -[CCDatabaseUpdater localInstanceRemovedCount]
- -[CCDatabaseUpdater localInstanceUpdatedCount]
- -[CCDatabaseUpdater modifiedRowCount]
- -[CCDatabaseUpdater priorLocalDonationDate]
- -[CCDatabaseUpdater priorLocalFullSetDonationDate]
- -[CCDatabaseUpdater priorLocalInstanceCount]
- -[CCDatabaseUpdater priorLocalSourceRevisionToken]
- -[CCDatabaseUpdater priorLocalSourceValidityHash]
- -[CCDatabaseUpdater priorLocalSourceVersion]
- -[CCDatabaseUpdater registerLocalDeviceSite:]
- -[CCDatabaseUpdater registerLocalDeviceSite:].cold.1
- -[CCDatabaseUpdater registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:]
- -[CCDatabaseUpdater selectAllDeviceRecords]
- -[CCDatabaseUpdater selectAllDeviceRecords].cold.1
- -[CCDatabaseUpdater selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:]
- -[CCDatabaseUpdater selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:].cold.1
- -[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:]
- -[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:].cold.1
- -[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:].cold.2
- -[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:].cold.3
- -[CCDatabaseUpdater sharedItemAddedCount]
- -[CCDatabaseUpdater sharedItemProvenanceUpdatedCount]
- -[CCDatabaseUpdater sharedItemRemovedCount]
- -[CCDatabaseUpdater tombstoneContentSequenceNumbersInRange:forDeviceRowId:]
- -[CCDatabaseUpdater tombstoneContentSequenceNumbersInRange:forDeviceRowId:].cold.1
- -[CCDatabaseUpdater tombstoneContentSequenceNumbersInRange:forDeviceRowId:].cold.2
- -[CCDatabaseUpdater updateContent:andMetaContent:localInstanceRowId:priorProvenanceRowId:contentHash:instanceHash:isDuplicate:]
- -[CCDatabaseUpdater updateMetaContent:localInstanceRowId:provenanceRowId:priorInstanceHash:instanceHash:contentHash:contentSequenceNumber:isDuplicate:]
- -[CCDatabaseUpdater updatedLocalSourceValidityHash]
- -[CCDatabaseUpdater updatedLocalSourceVersion]
- -[CCDonateServicePriors .cxx_destruct]
- -[CCDonateServicePriors donationDate]
- -[CCDonateServicePriors encodeWithCoder:]
- -[CCDonateServicePriors fullSetDonationDate]
- -[CCDonateServicePriors initWithCoder:]
- -[CCDonateServicePriors initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:]
- -[CCDonateServicePriors instanceCount]
- -[CCDonateServicePriors isAwaitingFullSet]
- -[CCDonateServicePriors options]
- -[CCDonateServicePriors revisionToken]
- -[CCDonateServicePriors version]
- -[CCDonateXPCClient abortSetDonation]
- -[CCDonateXPCClient addItemsWithContents:metaContents:completion:]
- -[CCDonateXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
- -[CCDonateXPCClient endSetDonationWithOptions:revisionToken:completion:]
- -[CCDonateXPCClient initWithClientId:]
- -[CCDonateXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCDonateXPCClient removeSourceItemIdentifier:completion:]
- -[CCDonateXPCClientFactory makeConnection:]
- -[CCDonateXPCClientFactory terminateConnection:]
- -[CCInstanceRecord .cxx_destruct]
- -[CCInstanceRecord description]
- -[CCInstanceRecord hash]
- -[CCInstanceRecord initWithDatabaseValueRow:]
- -[CCInstanceRecord init]
- -[CCInstanceRecord isEqual:]
- -[CCInstanceRecord isEqualToItemRecord:]
- -[CCInstanceRecord modified]
- -[CCInstanceRecord provenanceRowId]
- -[CCInstanceRecord sourceItemIdHash]
- -[CCItemInstance initWithSharedIdentifier:instanceIdentifier:content:metaContent:]
- -[CCMaintenanceClient client]
- -[CCMutableSetChange addedDevices]
- -[CCMutableSetChange addedLocalInstances]
- -[CCMutableSetChange allDevices]
- -[CCMutableSetChange allLocalInstances]
- -[CCMutableSetChange appendAddedDevices:]
- -[CCMutableSetChange appendAddedLocalInstances:]
- -[CCMutableSetChange appendAllDevices:]
- -[CCMutableSetChange appendAllLocalInstances:]
- -[CCMutableSetChange appendRemovedDevices:]
- -[CCMutableSetChange appendRemovedLocalInstances:]
- -[CCMutableSetChange containsChangesAfterDeduplication]
- -[CCMutableSetChange containsContentHash:]
- -[CCMutableSetChange copyWithZone:]
- -[CCMutableSetChange initWithSharedItem:changeType:]
- -[CCMutableSetChange removedDevices]
- -[CCMutableSetChange removedLocalInstances]
- -[CCMutableSetChange setSharedItemChangeType:]
- -[CCMutableSetChange sharedItemChangeType]
- -[CCProvenanceRecord .cxx_destruct]
- -[CCProvenanceRecord contentHash]
- -[CCProvenanceRecord contentSequenceNumberEndOfRun]
- -[CCProvenanceRecord contentSequenceNumber]
- -[CCProvenanceRecord contentState]
- -[CCProvenanceRecord description]
- -[CCProvenanceRecord deviceRowId]
- -[CCProvenanceRecord hash]
- -[CCProvenanceRecord initWithDatabaseValueRow:]
- -[CCProvenanceRecord init]
- -[CCProvenanceRecord instanceHash]
- -[CCProvenanceRecord isEqual:]
- -[CCProvenanceRecord isEqualToItemRecord:]
- -[CCProvenanceRecord metaContentSequenceNumberEndOfRun]
- -[CCProvenanceRecord metaContentSequenceNumber]
- -[CCProvenanceRecord metaContentState]
- -[CCProvenanceRecord provenanceRowId]
- -[CCRemoteCRDTSetDonation remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
- -[CCSQLCommandJoin .cxx_destruct]
- -[CCSQLCommandJoin description]
- -[CCSQLCommandJoin initWithJoinType:joinTables:]
- -[CCSQLCommandJoin init]
- -[CCSQLCommandJoin joinTables]
- -[CCSQLCommandJoin joinType]
- -[CCSQLCommandJoinTable initWithTable:joinCriterion:]
- -[CCSQLiteDatabase beginTransactionWithError:]
- -[CCSQLiteDatabase cleanup:]
- -[CCSQLiteDatabase initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:]
- -[CCSQLiteDatabase initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:].cold.1
- -[CCSQLiteDatabase openWithError:].cold.2
- -[CCSerializedSetEnumerator allSetsWithOptions:itemType:descriptors:error:]
- -[CCSerializedSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]
- -[CCSerializedSetEnumerator enumerateAllSets:withOptions:itemType:usingBlock:]
- -[CCSet _computeUniqueHash]
- -[CCSet uniqueHash]
- -[CCSetChangeRemoteXPCNotifier client]
- -[CCSetConfiguration initWithSetIdentifier:setUUID:resourceDomain:configuredDescriptors:syncPolicy:]
- -[CCSetDonation _addItem:error:]
- -[CCSetDonation _finishWithOptions:error:]
- -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
- -[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.1
- -[CCSetDonation initWithName:itemType:service:errorCode:priors:flushThreshold:]
- -[CCSetDonation initWithName:itemType:service:errorCode:priors:flushThreshold:].cold.1
- -[CCSetDonation priorRevisionToken]
- -[CCSetDonation queue]
- -[CCSetDonation updateRevisionToken:error:]
- -[CCXPCClient _errorHandlerWithCompletion:]
- -[CCXPCClient _failureHandlerWithResponse:]
- -[CCXPCClient _remoteObjectProxy:errorCompletion:]
- -[CCXPCClient failureCode]
- -[CCXPCClient initWithRemoteObjectInterface:exportedInterface:connection:clientId:interruptionCode:invalidationCode:useCase:]
- -[CCXPCClient initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:interruptionCode:invalidationCode:useCase:]
- -[CCXPCClient initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:interruptionCode:invalidationCode:useCase:]
- -[CCXPCClient initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:interruptionCode:invalidationCode:useCase:].cold.1
- -[CCXPCClient interruptionCode]
- -[CCXPCClient servicePriorsRespondingRequest:completion:usingBlock:]
- -[CCXPCClient serviceRequest:completion:usingBlock:]
- -[CCXPCClient serviceThrowingRequest:completion:usingBlock:]
- -[CCXPCClient setFailureCode:]
- GCC_except_table100
- GCC_except_table105
- GCC_except_table136
- GCC_except_table140
- GCC_except_table144
- GCC_except_table40
- GCC_except_table41
- GCC_except_table44
- GCC_except_table46
- GCC_except_table48
- GCC_except_table50
- GCC_except_table51
- GCC_except_table52
- GCC_except_table6
- GCC_except_table60
- _CCAttributionIdentifier
- _CCConcatenateHash64
- _CCConcatenatedHash64Prefix
- _CCConcatenatedHash64Suffix
- _CCDatabaseColumnContentSequenceNumber
- _CCDatabaseColumnContentSequenceNumberEndOfRun
- _CCDatabaseColumnContentState
- _CCDatabaseColumnMetaContentSequenceNumber
- _CCDatabaseColumnMetaContentSequenceNumberEndOfRun
- _CCDatabaseColumnMetaContentState
- _CCDatabaseColumnModified
- _CCDatabaseColumnProvenanceRowId
- _CCDatabaseIndexInstanceModified
- _CCDatabaseIndexProvenanceContentHash
- _CCDatabaseIndexProvenanceContentHashMetaContentState
- _CCDatabaseIndexProvenanceContentSequenceNumber
- _CCDatabaseIndexProvenanceMetaContentSequenceNumber
- _CCDatabaseSetAtomState
- _CCDatabaseSetClockValueRange
- _CCDatabaseTableNameInstance
- _CCDatabaseTableNameProvenance
- _CCDonateErrorCodeFromServiceResponse
- _CCDonateServiceOptionsDescription
- _CCDonateServiceRequestDescription
- _CCDonateServiceResponseDescription
- _CCItemStateDescription
- _CCPersistedKeyValueKeyDatabaseLastMaintenanceDate
- _CCPersistedKeyValueKeyDatabaseRowsModified
- _NSStringFromProtocol
- _OBJC_CLASS_$_CCDataResourceWriter
- _OBJC_CLASS_$_CCDatabaseUpdater
- _OBJC_CLASS_$_CCDonateServicePriors
- _OBJC_CLASS_$_CCDonateXPCClient
- _OBJC_CLASS_$_CCDonateXPCClientFactory
- _OBJC_CLASS_$_CCInstanceRecord
- _OBJC_CLASS_$_CCProvenanceRecord
- _OBJC_CLASS_$_CCSQLCommandJoin
- _OBJC_IVAR_$_CCDataResourceWriter._accessAssertion
- _OBJC_IVAR_$_CCDataResourceWriter._dataResource
- _OBJC_IVAR_$_CCDataResourceWriter._queue
- _OBJC_IVAR_$_CCDatabaseJoinedProvenance._provenance
- _OBJC_IVAR_$_CCDatabaseSelectBuilder._join
- _OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestAttestationGeneration
- _OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestContentSequenceNumber
- _OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestMetaContentSequenceNumber
- _OBJC_IVAR_$_CCDatabaseUpdater._commandCache
- _OBJC_IVAR_$_CCDatabaseUpdater._database
- _OBJC_IVAR_$_CCDatabaseUpdater._isLocalDonation
- _OBJC_IVAR_$_CCDatabaseUpdater._localDeviceRecord
- _OBJC_IVAR_$_CCDatabaseUpdater._localInstanceAddedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._localInstanceRemovedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._localInstanceUpdatedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._modifiedRowCount
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalDonationDate
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalFullSetDonationDate
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalInstanceCount
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceRevisionToken
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceValidityHash
- _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceVersion
- _OBJC_IVAR_$_CCDatabaseUpdater._requestDescription
- _OBJC_IVAR_$_CCDatabaseUpdater._sharedItemAddedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._sharedItemProvenanceUpdatedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._sharedItemRemovedCount
- _OBJC_IVAR_$_CCDatabaseUpdater._startTimeMicros
- _OBJC_IVAR_$_CCDatabaseUpdater._updatedLocalSourceValidityHash
- _OBJC_IVAR_$_CCDatabaseUpdater._updatedLocalSourceVersion
- _OBJC_IVAR_$_CCDonateServicePriors._donationDate
- _OBJC_IVAR_$_CCDonateServicePriors._fullSetDonationDate
- _OBJC_IVAR_$_CCDonateServicePriors._instanceCount
- _OBJC_IVAR_$_CCDonateServicePriors._options
- _OBJC_IVAR_$_CCDonateServicePriors._revisionToken
- _OBJC_IVAR_$_CCDonateServicePriors._version
- _OBJC_IVAR_$_CCInstanceRecord._modified
- _OBJC_IVAR_$_CCInstanceRecord._provenanceRowId
- _OBJC_IVAR_$_CCInstanceRecord._sourceItemIdHash
- _OBJC_IVAR_$_CCMutableSetChange._addedLocalInstances
- _OBJC_IVAR_$_CCMutableSetChange._allDevices
- _OBJC_IVAR_$_CCMutableSetChange._allLocalInstances
- _OBJC_IVAR_$_CCMutableSetChange._removedLocalInstances
- _OBJC_IVAR_$_CCMutableSetChange._sharedItemChangeType
- _OBJC_IVAR_$_CCProvenanceRecord._contentHash
- _OBJC_IVAR_$_CCProvenanceRecord._contentSequenceNumber
- _OBJC_IVAR_$_CCProvenanceRecord._contentSequenceNumberEndOfRun
- _OBJC_IVAR_$_CCProvenanceRecord._contentState
- _OBJC_IVAR_$_CCProvenanceRecord._deviceRowId
- _OBJC_IVAR_$_CCProvenanceRecord._instanceHash
- _OBJC_IVAR_$_CCProvenanceRecord._metaContentSequenceNumber
- _OBJC_IVAR_$_CCProvenanceRecord._metaContentSequenceNumberEndOfRun
- _OBJC_IVAR_$_CCProvenanceRecord._metaContentState
- _OBJC_IVAR_$_CCProvenanceRecord._provenanceRowId
- _OBJC_IVAR_$_CCSQLCommandJoin._joinTables
- _OBJC_IVAR_$_CCSQLCommandJoin._joinType
- _OBJC_IVAR_$_CCSet._uniqueHash
- _OBJC_IVAR_$_CCSetDonation._queue
- _OBJC_IVAR_$_CCSetDonation._revisionToken
- _OBJC_IVAR_$_CCXPCClient._failureCode
- _OBJC_IVAR_$_CCXPCClient._interruptionCode
- _OBJC_METACLASS_$_CCDataResourceWriter
- _OBJC_METACLASS_$_CCDatabaseUpdater
- _OBJC_METACLASS_$_CCDonateServicePriors
- _OBJC_METACLASS_$_CCDonateXPCClient
- _OBJC_METACLASS_$_CCDonateXPCClientFactory
- _OBJC_METACLASS_$_CCInstanceRecord
- _OBJC_METACLASS_$_CCProvenanceRecord
- _OBJC_METACLASS_$_CCSQLCommandJoin
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- __OBJC_$_CLASS_METHODS_CCDataResourceWriter
- __OBJC_$_CLASS_METHODS_CCDatabaseUpdater
- __OBJC_$_CLASS_METHODS_CCDonateServicePriors
- __OBJC_$_CLASS_METHODS_CCInstanceRecord
- __OBJC_$_CLASS_METHODS_CCProvenanceRecord
- __OBJC_$_CLASS_METHODS_CCSetDonation
- __OBJC_$_CLASS_PROP_LIST_CCDonateServicePriors
- __OBJC_$_INSTANCE_METHODS_CCDataResourceWriter
- __OBJC_$_INSTANCE_METHODS_CCDatabaseUpdater
- __OBJC_$_INSTANCE_METHODS_CCDonateServicePriors
- __OBJC_$_INSTANCE_METHODS_CCDonateXPCClient
- __OBJC_$_INSTANCE_METHODS_CCDonateXPCClientFactory
- __OBJC_$_INSTANCE_METHODS_CCInstanceRecord
- __OBJC_$_INSTANCE_METHODS_CCProvenanceRecord
- __OBJC_$_INSTANCE_METHODS_CCSQLCommandJoin
- __OBJC_$_INSTANCE_VARIABLES_CCDataResourceWriter
- __OBJC_$_INSTANCE_VARIABLES_CCDatabaseUpdater
- __OBJC_$_INSTANCE_VARIABLES_CCDonateServicePriors
- __OBJC_$_INSTANCE_VARIABLES_CCInstanceRecord
- __OBJC_$_INSTANCE_VARIABLES_CCProvenanceRecord
- __OBJC_$_INSTANCE_VARIABLES_CCSQLCommandJoin
- __OBJC_$_PROP_LIST_CCDataResourceWriter
- __OBJC_$_PROP_LIST_CCDatabaseUpdater
- __OBJC_$_PROP_LIST_CCDonateServicePriors
- __OBJC_$_PROP_LIST_CCInstanceRecord
- __OBJC_$_PROP_LIST_CCProvenanceRecord
- __OBJC_$_PROP_LIST_CCSQLCommandJoin
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonateService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonateServiceProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonateService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonateServiceProvider
- __OBJC_$_PROTOCOL_REFS_CCDonateServiceClient
- __OBJC_$_PROTOCOL_REFS_CCDonateServiceServer
- __OBJC_CLASS_PROTOCOLS_$_CCDonateServicePriors
- __OBJC_CLASS_PROTOCOLS_$_CCDonateXPCClient
- __OBJC_CLASS_PROTOCOLS_$_CCDonateXPCClientFactory
- __OBJC_CLASS_PROTOCOLS_$_CCInstanceRecord
- __OBJC_CLASS_PROTOCOLS_$_CCMutableSetChange
- __OBJC_CLASS_PROTOCOLS_$_CCProvenanceRecord
- __OBJC_CLASS_RO_$_CCDataResourceWriter
- __OBJC_CLASS_RO_$_CCDatabaseUpdater
- __OBJC_CLASS_RO_$_CCDonateServicePriors
- __OBJC_CLASS_RO_$_CCDonateXPCClient
- __OBJC_CLASS_RO_$_CCDonateXPCClientFactory
- __OBJC_CLASS_RO_$_CCInstanceRecord
- __OBJC_CLASS_RO_$_CCProvenanceRecord
- __OBJC_CLASS_RO_$_CCSQLCommandJoin
- __OBJC_LABEL_PROTOCOL_$_CCDonateService
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceClient
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceProvider
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceServer
- __OBJC_METACLASS_RO_$_CCDataResourceWriter
- __OBJC_METACLASS_RO_$_CCDatabaseUpdater
- __OBJC_METACLASS_RO_$_CCDonateServicePriors
- __OBJC_METACLASS_RO_$_CCDonateXPCClient
- __OBJC_METACLASS_RO_$_CCDonateXPCClientFactory
- __OBJC_METACLASS_RO_$_CCInstanceRecord
- __OBJC_METACLASS_RO_$_CCProvenanceRecord
- __OBJC_METACLASS_RO_$_CCSQLCommandJoin
- __OBJC_PROTOCOL_$_CCDonateService
- __OBJC_PROTOCOL_$_CCDonateServiceClient
- __OBJC_PROTOCOL_$_CCDonateServiceProvider
- __OBJC_PROTOCOL_$_CCDonateServiceServer
- __OBJC_PROTOCOL_REFERENCE_$_CCDonateServiceClient
- __OBJC_PROTOCOL_REFERENCE_$_CCDonateServiceServer
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEED1Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorItNS_9allocatorItEEE7reserveEm
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- __ZTINSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceINS_6vectorItNS_9allocatorItEEEENS2_IS4_EEEE
- ___103-[CCSetDonation _remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
- ___106-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:]_block_invoke
- ___106-[CCDatabaseSetStateReader _createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:]_block_invoke_2
- ___108-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:]_block_invoke
- ___116-[CCDonateXPCClient remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
- ___117-[CCDonateXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]_block_invoke
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.21
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.26
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22.cold.1
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28.cold.1
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_3
- ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_4
- ___125-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]_block_invoke
- ___125-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]_block_invoke.21
- ___129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke
- ___129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke.37
- ___129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke_2
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.10
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.13
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_2
- ___149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke_2.cold.1
- ___150-[CCDatabaseUpdater _insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:]_block_invoke
- ___153-[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:]_block_invoke
- ___153-[CCDatabaseUpdater selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:]_block_invoke.cold.1
- ___37-[CCDonateXPCClient abortSetDonation]_block_invoke
- ___39-[CCDataResourceWriter removeResource:]_block_invoke
- ___42-[CCSetDonation _finishWithOptions:error:]_block_invoke
- ___43-[CCDatabaseUpdater selectAllDeviceRecords]_block_invoke
- ___43-[CCXPCClient _errorHandlerWithCompletion:]_block_invoke
- ___43-[CCXPCClient _errorHandlerWithCompletion:]_block_invoke.cold.1
- ___43-[CCXPCClient _failureHandlerWithResponse:]_block_invoke
- ___43-[CCXPCClient _failureHandlerWithResponse:]_block_invoke.cold.1
- ___44-[CCDatabaseUpdater deleteAllLocalInstances]_block_invoke
- ___46-[CCDatabaseUpdater _selectLocalDeviceRecord:]_block_invoke
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54.cold.1
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.54.cold.2
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.cold.1
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.cold.2
- ___54-[CCDatabaseUpdater _insertDeviceSite:returningRowId:]_block_invoke
- ___55-[CCDataResourceWriter performMaintenance:shouldDefer:]_block_invoke
- ___59-[CCDonateXPCClient removeSourceItemIdentifier:completion:]_block_invoke
- ___60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke
- ___60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke.27
- ___60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke.27.cold.1
- ___60-[CCDataResourceWriter submitDatabaseTransactionUsingBlock:]_block_invoke
- ___60-[CCXPCClient serviceThrowingRequest:completion:usingBlock:]_block_invoke
- ___62-[CCDataResourceWriter initializeDatabaseWithLocalDeviceSite:]_block_invoke
- ___64-[CCDatabaseUpdater _deleteSourceItemIdHash:outProvenanceRowId:]_block_invoke
- ___66-[CCDatabaseUpdater _selectMetaContentWithInstanceHash:outRecord:]_block_invoke
- ___66-[CCDonateXPCClient addItemsWithContents:metaContents:completion:]_block_invoke
- ___68-[CCXPCClient servicePriorsRespondingRequest:completion:usingBlock:]_block_invoke
- ___71-[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:]_block_invoke
- ___72-[CCDonateXPCClient endSetDonationWithOptions:revisionToken:completion:]_block_invoke
- ___73-[CCDatabaseSetEnumerator allSetsWithOptions:itemType:descriptors:error:]_block_invoke
- ___75-[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:]_block_invoke
- ___75-[CCSerializedSetEnumerator allSetsWithOptions:itemType:descriptors:error:]_block_invoke
- ___78+[CCSetDonation deleteSetWithItemType:descriptors:serviceProvider:completion:]_block_invoke
- ___79-[CCDatabaseUpdater _selectProvenenceWithRowId:outInstanceHash:outContentHash:]_block_invoke
- ___79-[CCDatabaseUpdater _selectProvenenceWithRowId:outInstanceHash:outContentHash:]_block_invoke.cold.1
- ___84+[CCSetDonation fullSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
- ___88-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]_block_invoke
- ___90+[CCSetDonation remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
- ___90-[CCSerializedSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]_block_invoke
- ___91+[CCSetDonation incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
- ___96-[CCDatabaseUpdater _tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:]_block_invoke
- ___96-[CCDatabaseUpdater selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:]_block_invoke
- ____sharedXPCClientFactory_block_invoke
- ___block_descriptor_32_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16l
- ___block_descriptor_32_e49_B24?0"NSObject<CCDatabaseReadWriteAccess>"8^Q16l
- ___block_descriptor_32_e66_v24?0"NSObject<CCMaintenanceServerProtocol>"8?<v?"NSError">16l
- ___block_descriptor_40_e8_32bs_e35_v24?0"CCSetDonation"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e39_v24?0"CCFullSetDonation"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e8_v12?0S8ls32l8
- ___block_descriptor_40_e8_32r_e32_v24?0"CCProvenanceRecord"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e35_v24?0"CCSetDonation"8"NSError"16lr32l8
- ___block_descriptor_40_e8_32r_e8_v12?0S8lr32l8
- ___block_descriptor_40_e8_32s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8
- ___block_descriptor_40_e8_32s_e54_v24?0"NSObject<CCSetChangeRelayProtocol>"8?<v?S>16ls32l8
- ___block_descriptor_40_e8_32s_e58_v24?0"NSObject<CCSetStoreAdminServiceServer>"8?<v?S>16ls32l8
- ___block_descriptor_42_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_42_e8_32s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8
- ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32bs40r_e49_B24?0"NSObject<CCDatabaseReadWriteAccess>"8^Q16ls32l8r40l8
- ___block_descriptor_48_e8_32r40r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0S8ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e18_B16?0"NSNumber"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e44_B32?0"NSObject<CCDatabaseRecord>"8^16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e59_"CCSQLCommandCriterion"28?0"NSNumber"8"NSIndexSet"16C24ls32l8s40l8
- ___block_descriptor_50_e8_32s40bs_e32_v24?0"CCProvenanceRecord"8^B16ls32l8s40l8
- ___block_descriptor_56_e8_32bs40r48r_e28_v24?0"CCDataResource"8^B16ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32r40r48r_e38_v16?0"NSObject<CCDatabaseValueRow>"8lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e62_v48?0"CKDistributedSiteIdentifier"8{_NSRange=QQ}16C32C36^B40ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48s_e44_v32?0"NSNumber"8"NSMutableIndexSet"16^B24ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s_e70_v24?0"NSObject<CCDonateService>"8?<v?Sq"CCDonateServicePriors">16ls32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e62_v48?0"CKDistributedSiteIdentifier"8{_NSRange=QQ}16C32C36^B40ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_e8_32s40s48s56s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40bs48r56r64r_e28_v24?0"CCDataResource"8^B16lr48l8s32l8s40l8r56l8r64l8
- ___block_descriptor_74_e8_32s40s48s56bs64r_e37_v28?0S8q12"CCDonateServicePriors"20ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32r40r48r56r64r72r_e46_B32?0"NSObject<CCDatabaseValueRow>"8^16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
- ___block_descriptor_80_e8_32s40s48bs56r64w_e5_v8?0lr56l8w64l8s32l8s40l8s48l8
- ___block_descriptor_84_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.197
- __sharedXPCClientFactory
- __sharedXPCClientFactory.cold.1
- __sharedXPCClientFactory.onceToken
- __sharedXPCClientFactory.sharedFactory
- _block_copy_helper.44
- _block_descriptor.46
- _block_destroy_helper.45
- _dispatch_after
- _dispatch_time
- _get_type_metadata 15Synchronization5MutexVySbG.11
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_addItem:error:
- _objc_msgSend$_cleanupDatabaseIfRequired
- _objc_msgSend$_clearTombstoneStatus:
- _objc_msgSend$_computeUniqueHash
- _objc_msgSend$_createDatabaseWithLocalDeviceSite:
- _objc_msgSend$_createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:
- _objc_msgSend$_createTableWithRecordClass:error:
- _objc_msgSend$_deleteDeviceRowId:
- _objc_msgSend$_deleteSourceItemIdHash:outProvenanceRowId:
- _objc_msgSend$_didCompleteMaintenance:shouldDefer:
- _objc_msgSend$_enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:
- _objc_msgSend$_errorHandlerWithCompletion:
- _objc_msgSend$_executeDatabaseTransactionUsingBlock:
- _objc_msgSend$_expireAndTombstoneAllProvenanceForDeviceRowId:
- _objc_msgSend$_expireDeviceRowId:
- _objc_msgSend$_failureHandlerWithResponse:
- _objc_msgSend$_finishWithOptions:error:
- _objc_msgSend$_incrementCachedIntegerWithKey:
- _objc_msgSend$_incrementLocalDeltaGeneration
- _objc_msgSend$_insertContent:contentHash:outExists:
- _objc_msgSend$_insertContent:contentHash:outSequenceNumber:
- _objc_msgSend$_insertDeviceSite:returningRowId:
- _objc_msgSend$_insertLocalInstanceForItemWithSourceItemIdHash:provenanceRowId:
- _objc_msgSend$_insertMetaContent:instanceHash:outSequenceNumber:outIsDuplicate:
- _objc_msgSend$_insertNewProvenanceAndTombstonePriorProvenanceRow:outInsertedProvenanceRowId:instanceHash:contentHash:contentSequenceNumber:metaContentSequenceNumber:contentChanged:
- _objc_msgSend$_insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:
- _objc_msgSend$_isDefaultPersonaRequestingUserResource:
- _objc_msgSend$_loadDatabase:
- _objc_msgSend$_persistCachedIntegers
- _objc_msgSend$_persistDateWithDeltaProduced:isFullSet:
- _objc_msgSend$_persistRevisionTokenIfNotNil:
- _objc_msgSend$_produceSelectClauseWithTableName:columnNames:count:
- _objc_msgSend$_remoteObjectProxy:errorCompletion:
- _objc_msgSend$_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$_removeResource:
- _objc_msgSend$_resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:
- _objc_msgSend$_selectDeviceRecords:withOptions:beyondExpirationDate:
- _objc_msgSend$_selectLatestDeviceRecordWithDeviceUUID:outRecord:
- _objc_msgSend$_selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:
- _objc_msgSend$_selectLocalDeviceRecord:
- _objc_msgSend$_selectLocalInstanceCount:
- _objc_msgSend$_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:
- _objc_msgSend$_selectMetaContentWithInstanceHash:outRecord:
- _objc_msgSend$_selectPersistedValueForKey:outValue:valueClass:
- _objc_msgSend$_selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:
- _objc_msgSend$_setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:
- _objc_msgSend$_shouldEnumerateContainer:
- _objc_msgSend$_temporaryDirectoryURLWithError:
- _objc_msgSend$_tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:
- _objc_msgSend$_tombstoneProvenanceRowsForExpiredDeviceRowId:
- _objc_msgSend$_tombstoneResource:
- _objc_msgSend$_updateDeviceRowId:deltaGeneration:expirationDate:
- _objc_msgSend$_updateLocalInstanceRowId:provenanceRowId:
- _objc_msgSend$_updateLocalSourceVersion:localSourceValidityHash:
- _objc_msgSend$_upsertInteger:forKey:
- _objc_msgSend$_upsertInteger:forKey:skipIfNil:
- _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:
- _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:
- _objc_msgSend$abortSetDonation
- _objc_msgSend$addItemsWithContents:metaContents:completion:
- _objc_msgSend$allSetsWithOptions:itemType:descriptors:error:
- _objc_msgSend$appendAddedDevices:
- _objc_msgSend$appendAddedLocalInstances:
- _objc_msgSend$appendAllDevices:
- _objc_msgSend$appendAllLocalInstances:
- _objc_msgSend$appendRemovedDevices:
- _objc_msgSend$appendRemovedLocalInstances:
- _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:
- _objc_msgSend$beginTransactionWithError:
- _objc_msgSend$cleanup:
- _objc_msgSend$clearTombstoneStatus:
- _objc_msgSend$client
- _objc_msgSend$compactContiguousRunsOfDeletes:
- _objc_msgSend$connectionToDatabaseAtURL:dataProtectionClass:openMode:accessAssertion:
- _objc_msgSend$containsChangesAfterDeduplication
- _objc_msgSend$containsContentHash:
- _objc_msgSend$contentSequenceNumberEndOfRun
- _objc_msgSend$criterionWithColumnName:INSubQuery:
- _objc_msgSend$criterionWithColumnName:ISColumnValue:
- _objc_msgSend$criterionWithColumnName:ISNOTColumnValue:
- _objc_msgSend$criterionWithNOTSubCriteria:
- _objc_msgSend$defaultDataProtectionClass
- _objc_msgSend$deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord
- _objc_msgSend$deleteExpiredRemoteDeviceState:shouldTombstoneSet:
- _objc_msgSend$deleteSetWithItemType:descriptors:serviceProvider:completion:
- _objc_msgSend$deleteSourceItemIdHash:
- _objc_msgSend$donationWithName:itemType:service:errorCode:priors:
- _objc_msgSend$endSetDonationWithOptions:revisionToken:completion:
- _objc_msgSend$enumerateAllSets:withOptions:itemType:descriptors:usingBlock:
- _objc_msgSend$enumerateAllSets:withOptions:itemType:usingBlock:
- _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:
- _objc_msgSend$enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
- _objc_msgSend$enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:
- _objc_msgSend$failureCode
- _objc_msgSend$fullSetDonationWithItemType:descriptors:completion:
- _objc_msgSend$fullSetDonationWithItemType:descriptors:serviceProvider:completion:
- _objc_msgSend$hasDatavaultEntitlement
- _objc_msgSend$incrementRowsModified:database:
- _objc_msgSend$incrementalSetDonationWithItemType:descriptors:completion:
- _objc_msgSend$incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:
- _objc_msgSend$incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:completion:
- _objc_msgSend$initWithAssertionOverride:
- _objc_msgSend$initWithDataResource:accessAssertion:
- _objc_msgSend$initWithDatabase:request:
- _objc_msgSend$initWithJoinType:joinTables:
- _objc_msgSend$initWithName:itemType:service:errorCode:priors:flushThreshold:
- _objc_msgSend$initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:
- _objc_msgSend$initWithProvenance:contentData:metaContentData:
- _objc_msgSend$initWithRemoteObjectInterface:exportedInterface:connection:clientId:interruptionCode:invalidationCode:useCase:
- _objc_msgSend$initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:interruptionCode:invalidationCode:useCase:
- _objc_msgSend$initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:interruptionCode:invalidationCode:useCase:
- _objc_msgSend$initWithSharedIdentifier:instanceIdentifier:content:metaContent:
- _objc_msgSend$initWithSharedItem:changeType:
- _objc_msgSend$initWithTable:joinCriterion:
- _objc_msgSend$initializeDatabaseWithLocalDeviceSite:
- _objc_msgSend$interruptionCode
- _objc_msgSend$intersectsSet:
- _objc_msgSend$joinTables
- _objc_msgSend$metaContentSequenceNumberEndOfRun
- _objc_msgSend$minusSet:
- _objc_msgSend$modified
- _objc_msgSend$performMaintenance:shouldDefer:
- _objc_msgSend$prepareWithError:
- _objc_msgSend$protocol
- _objc_msgSend$provenance
- _objc_msgSend$provenanceRowId
- _objc_msgSend$purgeTombstonedResources:
- _objc_msgSend$registerLocalDeviceSite:
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:
- _objc_msgSend$removeResource:
- _objc_msgSend$removeSourceItemIdentifier:completion:
- _objc_msgSend$selectFromTableWithName:columns:count:join:criterion:order:limit:offset:
- _objc_msgSend$selectRowsModifiedCountInDatabase:error:
- _objc_msgSend$servicePriorsRespondingRequest:completion:usingBlock:
- _objc_msgSend$serviceRequest:completion:usingBlock:
- _objc_msgSend$serviceThrowingRequest:completion:usingBlock:
- _objc_msgSend$setFailureCode:
- _objc_msgSend$setJoinWithType:tables:
- _objc_msgSend$setSharedItemChangeType:
- _objc_msgSend$terminateConnection:
- _objc_msgSend$timeIntervalSinceReferenceDate
- _objc_msgSend$uniqueHash
- _objc_msgSend$unsignedShortValue
- _objc_msgSend$updaterForDatabase:
- _objc_msgSend$upsertLastMaintenanceDate:database:error:
- _objc_msgSend$upsertRowsModified:database:error:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _objectdestroy.14Tm
CStrings:
+ " "
+ " (%@)"
+ " (operator: %u)"
+ " UNION "
+ " UNION ALL "
+ " deviceRowId: %@, contentHash: %@, sequenceNumber: %@, deletedRunLength: %@, deletedDate: %@"
+ " deviceRowId: %@, sourceItemIdHash: %@, instanceHash: %@, contentHash: %@, sequenceNumber: %@, deletedRunLength: %@, writtenDate: %@, deletedDate: %@"
+ " table: %@, joinType: %ld, criterion: %@"
+ "\"%@\" %@ NULLABLE"
+ "#"
+ "%@ - %@"
+ "%@ > %@"
+ "%@ AS (%@)"
+ "%@ NOT creating resource %@ with access mode %@"
+ "%@ failed to find a set matching key: %@"
+ "%@%@"
+ "%@%@%@"
+ "%@-%@ [%@]"
+ "%@: All conditions met for set tombstone eligibility"
+ "%@: Attempt to insert:\n\n\t{instanceHash: %@ metaContent: %@}\n\ncollided with existing record:\n\n\t{instanceHash: %@ metaContent: %@}"
+ "%@: Automatically rolling back update"
+ "%@: Built indexed field table: %@ (columns: %@) indexing %u blobs from table: %@"
+ "%@: Cannot expire local device record: %@ with deviceUUID: %@"
+ "%@: Cannot re-register local device record: %@ with site %@"
+ "%@: Database prepared"
+ "%@: Deleted %u expired item instance(s)"
+ "%@: Deleting any content records no longer referenced by provenance"
+ "%@: Deleting device record: %@"
+ "%@: Device table contains nonzero remote device records - not eligible for tombstone"
+ "%@: Expiring device record: %@"
+ "%@: Expiring device record: %@ and associated state which is now invalid due to registration of device site %@"
+ "%@: Extending expiration date from %@ to %@ due to re-attestation of device site %@ compared to record: %@"
+ "%@: Failed to query metaContentRecord for instanceHash: %@ after collision: %@"
+ "%@: Failed to read existing columns of table: %@ error: %@"
+ "%@: Failed to rollback update: %@"
+ "%@: Found %u active remote device records past their expiration date %@"
+ "%@: Found %u expired remote device records past the tombstone preservation interval %@"
+ "%@: Found no device record to expire with deviceUUID: %@"
+ "%@: Ignoring re-attested expiration date of device site %@ which occurs sooner than the stored device record: %@"
+ "%@: Ignoring registration of relayed device site %@ matching peerDeviceUUID: %@"
+ "%@: Incrementing local delta generation from %@ to %@"
+ "%@: IndexedItemField table requires rebuilding to match configuration: %@ (required columns: %@) (current columns: %@)"
+ "%@: Inserting device record due to re-attestation of device site %@"
+ "%@: Inserting first record of device site %@"
+ "%@: Inserting latest record of device site %@"
+ "%@: Persisted value for key: %@ is: %@"
+ "%@: Record with sourceItemIdHash: %@ has already been updated - donation contains items with duplicate sourceItemIdentifiers"
+ "%@: Set contains present content - not eligible for tombstone"
+ "%@: Set has received a local source donation - not eligible for tombstone"
+ "%@: Skipping new registration of device site %@"
+ "%@: Skipping registration - delta generation of record: %@ is more recent than device site %@"
+ "%@: Skipping registration - resource generation of record: %@ is more recent than device site %@"
+ "%@: Skipping relayed device site %@ already expired (compared to: %@)"
+ "%@: Skipping relayed device site %@ matching local deviceUUID: %@"
+ "%@: Skipping unattested registration of device site %@"
+ "%@: Skipping unattested registration of device site %@ for expired record: %@"
+ "%@: Skipping unattested registration of device site %@ which would progress the deltaGeneration for record: %@"
+ "%@: Unexpected peer device site %@ is expired (compared to: %@)"
+ "%@: Unexpected peer device site %@ matches local deviceUUID: %@"
+ "%@: Unexpected peer device site %@ not matching peerDeviceUUID: %@"
+ "%@: Unexpected remote device site %@ has isLocal flag set"
+ "%@: Unexpected remote device site %@ missing expiration date"
+ "%@: Unexpected row result: %@ from command: %@"
+ "%@: cannot insert device site with invalid deviceUUID: %@"
+ "%@: cannot register local device with invalid device site: %@"
+ "%@: cannot tombstone sequence number range for localDeviceRowId: %@"
+ "%@: cannot update device row id: %@ with nil expiration date"
+ "%@: content sequence number is unexpectedly nil"
+ "%@: device site %@ has regressed deltaGeneration compared with record: %@"
+ "%@: device site %@ has regressed resourceGeneration compared with record: %@"
+ "%@: device site %@ not expected to invalidate record: %@"
+ "%@: device site %@ not expected to progress deltaGeneration for record: %@"
+ "%@: deviceUUID: %@ record already expired: %@"
+ "%@: failed to decode maintenance history (%@) - starting new empty list: %@"
+ "%@: invalid deviceUUID: %@"
+ "%@: invalid sourceItemIdentifer: %@"
+ "%@: persistedKey not cached: %@"
+ "%@: prior history contains unexpected entry at position %u: %@ history: %@"
+ "%@: select: %@ produced no count"
+ "%@: select: %@ returned an unexpected number of local device records: %@"
+ "%@: using the elapsed time interval from %u prior maintenance runs as minimum tombstone age: %f instead of default: %f"
+ "%@: writer - startTimeMicros: %@"
+ "%@:%@:%@%@ value: %@"
+ "%s skipping unexpected field: %@"
+ "(%@) Failed to begin update for maintenance: %@"
+ "(%@) Maintenance cancelled for set: %@ error: %@"
+ "(%@) Maintenance completed for set: %@"
+ "(%@) Maintenance failed to tombstone set: %@ error: %@"
+ "(%@) Starting maintenance for set: %@"
+ "(%@) Tombstoning set: %@ after maintenance removed all remaining state"
+ "-[CCDatabaseItemFieldIndexer appendDatabaseValues:fromItemField:]"
+ "-[CCMaintenanceClient _performNightlyMaintenanceSynchronously:completion:]"
+ ":%@"
+ "<%@:%@:%@%@>"
+ "<CCProvenanceStateSets p:%@ d:%@ c:%@>"
+ "<CCSetIntegrityCheckResult: passed=%@ checks=%lu failed=%lu issues=%lu>"
+ "@\"CCDatabaseCommandCache\""
+ "@\"CCDatabaseInsert\""
+ "@\"CCDatabaseItemFieldIndexer\""
+ "@\"CCDatabaseUpdateTracker\""
+ "@\"CCDonationServicePriors\""
+ "@\"CCItemInstance\"32@0:8@\"CCItemFieldPredicate\"16^@24"
+ "@\"CCSet\"16@0:8"
+ "@\"CCSet\"32@0:8@\"NSNumber\"16^@24"
+ "@\"CCSetConfiguration\""
+ "@\"CCSharedItem\"32@0:8@\"CCItemFieldPredicate\"16^@24"
+ "@\"NSArray\"32@0:8@\"NSString\"16^@24"
+ "@\"NSArray\"40@0:8S16@\"NSArray\"20S28^@32"
+ "@\"NSCache\""
+ "@\"NSDictionary\""
+ "@\"NSIndexSet\""
+ "@\"NSObject<CCDonationService>\""
+ "@\"NSObject<CCDonationService>\"24@0:8@\"NSString\"16"
+ "@\"NSObject<CCItemRetriever>\""
+ "@\"NSObject<CCSetChangeNotifierProtocol>\""
+ "@\"NSObject<NSSecureCoding>\""
+ "@100@0:8@16@24B32B36@40@48@56@64@72@80@88B96"
+ "@16@?0@\"CCProvenanceCompactionRecord\"8"
+ "@32@0:8S16C20@24"
+ "@36@0:8@16@24S32"
+ "@36@0:8S16C20C24@28"
+ "@40@0:8@16@24B32B36"
+ "@40@0:8@16^@24^@32"
+ "@40@0:8@16q24@32"
+ "@40@0:8C16S20@24q32"
+ "@40@0:8S16@20S28^@32"
+ "@44@0:8@16#24C32@36"
+ "@44@0:8B16Q20Q28@36"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8S16@20S28@32^@40"
+ "@52@0:8@16C24d28@?36^@44"
+ "@52@0:8@16C24{_NSRange=QQ}28^@44"
+ "@52@0:8@16i24q28d36@44"
+ "@52@0:8S16@20Q28@36^@44"
+ "@56@0:8@16S24@28S36q40@48"
+ "@60@0:8@16@24@32@40B48^@52"
+ "@60@0:8@16q24q32i40C44d48I56"
+ "@60@0:8S16@20Q28@36@44^@52"
+ "@64@0:8@16S24@28S36q40@48Q56"
+ "@64@0:8S16@20@28@36S44@48^@56"
+ "@68@0:8@16@24Q32@40@48@56C64"
+ "@96@0:8@16@24@32@40@48@56@64@72@80@88"
+ "@?24@0:8q16"
+ "Access denied"
+ "Access request for set failed: %@"
+ "AppIntentsIndexedEntity-com.apple.MobileAddressBook"
+ "AppIntentsIndexedEntity-com.apple.MobileSMS"
+ "AppIntentsIndexedEntity-com.apple.Music"
+ "AppIntentsIndexedEntity-com.apple.Passbook"
+ "AppIntentsIndexedEntity-com.apple.email.SearchIndexer"
+ "AppIntentsIndexedEntity-com.apple.homed"
+ "AppIntentsIndexedEntity-com.apple.mobilecal"
+ "AppIntentsIndexedEntity-com.apple.mobilemail"
+ "AppIntentsIndexedEntity-com.apple.mobilenotes"
+ "AppIntentsIndexedEntity-com.apple.mobilesafari"
+ "AppIntentsIndexedEntity-com.apple.mobileslideshow"
+ "AppIntentsIndexedEntity-com.apple.podcasts"
+ "AppIntentsIndexedEntity-com.apple.reminders"
+ "AppIntentsIndexedEntity-com.apple.shortcuts"
+ "AppIntentsIndexedEntity-com.apple.usernotificationsd"
+ "Asked to defer maintenance"
+ "B16@?0@\"CCDatabaseInsert\"8"
+ "B28@0:8@16C24"
+ "B28@0:8B16^@20"
+ "B28@0:8S16@20"
+ "B32@0:8^@16@?<v@?@\"CCItemField\">24"
+ "B32@0:8^@16^@24"
+ "B36@0:8@16B24^@28"
+ "B36@0:8S16@20^@28"
+ "B36@0:8S16^@20@?28"
+ "B36@0:8S16^@20@?<v@?@\"CCSet\">28"
+ "B36@0:8^@16B24@?28"
+ "B36@0:8^@16C24^@28"
+ "B40@0:8@\"CCItemFieldPredicate\"16^@24@?<v@?@\"CCItemInstance\"^B>32"
+ "B40@0:8@\"CCItemFieldPredicate\"16^@24@?<v@?@\"CCSharedItem\"^B>32"
+ "B40@0:8@?16^B24^@32"
+ "B40@0:8S16S20^@24@?32"
+ "B40@0:8S16S20^@24@?<v@?@\"CCSet\">32"
+ "B40@0:8^B16@?24^@32"
+ "B40@0:8d16@?24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B44@0:8@16C24^@28@?36"
+ "B44@0:8@16S24^@28^@36"
+ "B44@0:8S16@20@28^@36"
+ "B44@0:8^@16C24@28^@36"
+ "B48@0:8@16@24@32@?40"
+ "B48@0:8@16@24@32^@40"
+ "B48@0:8@16@24^@32@?40"
+ "B48@0:8@16@24^@32^@40"
+ "B48@0:8@16@24^B32^@40"
+ "B48@0:8@16^@24#32^@40"
+ "B48@0:8@16^C24^@32^@40"
+ "B48@0:8@16d24@?32^@40"
+ "B48@0:8S16@\"NSArray\"20S28^@32@?<v@?@\"CCSet\">40"
+ "B48@0:8S16@20S28^@32@?40"
+ "B48@0:8{_NSRange=QQ}16@32^@40"
+ "B52@0:8@16C24d28@?36^@44"
+ "B52@0:8C16@20{_NSRange=QQ}28^@44"
+ "B56@0:8@16@24@32@40^@48"
+ "B56@0:8@16@24B32B36^@40^@48"
+ "B56@0:8@16C24C28@32^@40@?48"
+ "B56@0:8@16^@24^@32^B40^@48"
+ "B60@0:8@16@24S32@36^@44@?52"
+ "B60@0:8@16C24@28@36@44^@52"
+ "B60@0:8@16C24{_NSRange=QQ}28@44^@52"
+ "B64@0:8@16#24C32C36@40^@48@?56"
+ "B64@0:8@16@24@32@40^B48^@56"
+ "B64@0:8@16@24@32@40q48^@56"
+ "B64@0:8@16@24C32@36B44^@48@?56"
+ "B64@0:8^@16^@24^@32^@40^@48^@56"
+ "B68@0:8@16@24@32@40B48^@52@?60"
+ "B68@0:8@16B24@28@36@44^B52^@60"
+ "B68@0:8@16C24@28{_NSRange=QQ}36@52^@60"
+ "B68@0:8{_NSRange=QQ}16@32C40@44^@52@?60"
+ "B72@0:8@16@24@32@40@48^B56^@64"
+ "B72@0:8@16@24@32@40^@48^@56^@64"
+ "BEGIN DEFERRED TRANSACTION"
+ "BEGIN IMMEDIATE TRANSACTION"
+ "Beginning read transaction"
+ "Beginning write transaction"
+ "CCAppIntentsIndexedEntityMetaContent"
+ "CCCachedDocumentContent"
+ "CCCachedDocumentMetaContent"
+ "CCCachedDocumentUtilities"
+ "CCCachedDocumentUtilities.m"
+ "CCContentProvenanceRecord"
+ "CCDatabaseCommandCache"
+ "CCDatabaseItemFieldIndexer"
+ "CCDatabaseItemRetriever"
+ "CCDatabaseUpdateSummary"
+ "CCDatabaseUpdateTracker"
+ "CCDatabaseWriter"
+ "CCDonationService"
+ "CCDonationServiceClient"
+ "CCDonationServicePriors"
+ "CCDonationServiceProvider"
+ "CCDonationServiceServer"
+ "CCDonationXPCClient"
+ "CCDonationXPCClientFactory"
+ "CCIndexedFieldConfiguration"
+ "CCItemContent"
+ "CCItemFieldEnumerable"
+ "CCItemFieldPredicate"
+ "CCItemMetaContent"
+ "CCItemRetriever"
+ "CCMaintenenaceXPCClient"
+ "CCMetaContentProvenanceRecord"
+ "CCProvenanceCompactionRecord"
+ "CCProvenanceStateSets"
+ "CCSQLCommandCTE"
+ "CCSQLCommandUnion"
+ "CCSerializedSetItemRetriever"
+ "CCSetChangeXPCClient"
+ "CCSetIntegrityCheck"
+ "CCSetIntegrityCheckResult"
+ "CCSetItemRetriever"
+ "CREATE INDEX \"%@\" ON \"%@\" (\"%@\",\"%@\" DESC);"
+ "CREATE INDEX \"%@\" ON \"%@\" (\"%@\",\"%@\");"
+ "CREATE INDEX \"%@%@\" ON \"%@\" (\"%@\");"
+ "CREATE INDEX \"%@_%@\" ON \"%@\" (\"%@\");"
+ "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer NOT NULL, \"%@\" integer NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE, FOREIGN KEY (\"%@\") REFERENCES \"%@\" (\"%@\") ON UPDATE CASCADE ON DELETE CASCADE ); "
+ "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer NOT NULL, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, FOREIGN KEY (\"%@\") REFERENCES \"%@\" (\"%@\") ON UPDATE CASCADE ON DELETE CASCADE ); "
+ "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer NOT NULL, %@, FOREIGN KEY (\"%@\") REFERENCES \"%@\" (\"%@\") ON UPDATE CASCADE ON DELETE CASCADE ); "
+ "Cache content contains asymmetrical batch counts: {%@, %@, %@}"
+ "Call to _sqlite3_maintain_load_factor failed for database at path: %@"
+ "Cancelation returned error: %@"
+ "Canceled"
+ "Cannot translate indexed field predicate for DocumentCache: %@"
+ "Cascade"
+ "CascadeSets"
+ "Class getCCAppIntentsIndexedEntityMetaContentClass(void)_block_invoke"
+ "Class getCCCachedDocumentContentClass(void)_block_invoke"
+ "Class getCCCachedDocumentMetaContentClass(void)_block_invoke"
+ "Compaction"
+ "Compaction: %@: Starting with minimum tombstone age of %f"
+ "Compaction: %@: _deleteRecordsWithRowIds for content failed: %@"
+ "Compaction: %@: _deviceRowIdentifiersWithError failed: %@"
+ "Compaction: %@: _markTombstoneRowForVectorType failed: %@"
+ "Compaction: %@: _processDeletionForDeviceRowId failed for %@ %@: %@"
+ "Compaction: %@: compaction failed for device %@: %@"
+ "Compaction: %@: compaction time: %f"
+ "Compaction: %@: completed compaction for device %@"
+ "Compaction: %@: deferred at beginning of device %@"
+ "Compaction: %@: deferred during _processRange"
+ "Compaction: %@: deferred during _stateSetsForDeviceRowId"
+ "Compaction: %@: deleting rows from %@ fails for rowIds: %@ - %@"
+ "Compaction: %@: failure during _stateSetsForDeviceRowId for %@: %@"
+ "Compaction: %@: failure during processing for %@: %@"
+ "Compaction: %@: processing %@ for device %@"
+ "Compaction: %@: starting compaction for device %@"
+ "Compaction: %@: state sets for %@: %@"
+ "Connection terminated"
+ "Could not remove resource: %@"
+ "Could not retrieve set config for %@, defaulting to PROTECTION_CLASS_C"
+ "Creating dataResource: %@ in temporary path: %@"
+ "Current persona is %@default (%@) Skipping serialized set with %@null persona: %@"
+ "DROP TABLE IF EXISTS %@"
+ "Database Writer failed to be initialized for dataResource: %@ with error: %@"
+ "Database Writer failed to finish update for dataResource: %@ with error: %@"
+ "Database contains present contentHash: %@ from deviceRowId: %@ associated with sequenceNumber: %@ different from current insert: %@"
+ "Database failed to be prepared for dataResource: %@ with error: %@"
+ "Database: writer - startTimeMicros: %@"
+ "Deprecations"
+ "DocumentCache"
+ "Donation %@ cache content has invalid buffer: %@ associated item: %@"
+ "Donation %@ cache content must be less than %lu bytes, received %lu: %@ associated item: %@"
+ "Donation inactive"
+ "Encoded revisionToken pairs exceed size limit: %lu bytes (max %lu bytes)"
+ "End of buffer"
+ "F%X"
+ "Failed to create database read access"
+ "Failed to decode %{public}@: %{public}@"
+ "Failed to decode priorRevisionToken: %@ error: %@"
+ "Failed to decode revisionToken JSON %@ error: %@"
+ "Failed to encode revisionToken dictionary to JSON: %@"
+ "Failed to enumerate indexed fields of itemMessage: %@ error: %@"
+ "Failed to establish connection to donation service for set donation %@"
+ "Failed to execute pragma command: %@"
+ "Failed to finish set donation %@ error: %@"
+ "Failed to resolve set from dataResource: %@ error: %@"
+ "Failed to skip field"
+ "Finished"
+ "Finished set donation %@"
+ "Incorrect class"
+ "IndexedField"
+ "Invalid bookmark"
+ "Invalid buffer"
+ "Invalid field predicate"
+ "Invalid item type"
+ "Invalid value"
+ "Invalid variable-length field length"
+ "ItemInstanceIdentifier"
+ "KeyPrefixedIdentifier"
+ "KeyPrefixedIdentifier key (%@) does not match the current set (%@): %@"
+ "Maintenance %@completed at container: %@ %@"
+ "Max group recursion depth"
+ "Mismatched field accessor"
+ "Missing sourceItemIdentifier"
+ "NOT "
+ "NULL AS %@"
+ "No prior source version"
+ "No such set"
+ "NoSetCreation"
+ "Operation failed"
+ "PRAGMA %@"
+ "PRAGMA table_info(%@);"
+ "Predicate not supported: %@"
+ "Received more than a single item instance result matching predicate: %@ results: %@"
+ "Received more than a single shared item result matching predicate: %@ results: %@"
+ "Received zero item instance results matching predicate: %@"
+ "Received zero shared item results matching predicate: %@"
+ "RemoteDeltaMerge"
+ "RemoteDeviceAttestation"
+ "RemoteDeviceExpiration"
+ "Revised"
+ "SELECT DISTINCT %@ FROM %@"
+ "Serialized set item retrieval not supported"
+ "Service timeout"
+ "ServiceProviderDeprecations"
+ "Set %@: negative run length at %@ sequence %@, run length = %@"
+ "Set %@: sequence gap in %@ sequence: %@"
+ "Set %@: sequence overlap in %@ sequence %@"
+ "Set enumeration skipping resource: %@ for access error: %@"
+ "SharedItemIdentifier"
+ "Skipping enumeration for container: %@ as persona: %@"
+ "Skipping enumeration for user-domain resource: %@ as persona: %@"
+ "Skipping integrity check for set %@: %{public}@"
+ "Source validity mismatch"
+ "Source version equals prior version"
+ "Source version inconsistent"
+ "SourceItemIdentifier"
+ "Successfully renamed temporary directory and moved to final path: %s"
+ "T#,R,N,V_itemMessageSubclass"
+ "T@\"CCDatabaseSelect\",R,N,V_select"
+ "T@\"CCDonationServicePriors\",R,N,V_priors"
+ "T@\"NSArray\",R,N,V_descriptorAllowList"
+ "T@\"NSArray\",R,N,V_indexedFields"
+ "T@\"NSArray\",R,N,V_issues"
+ "T@\"NSArray\",R,N,V_selects"
+ "T@\"NSIndexSet\",R,N,V_eligibleSequences"
+ "T@\"NSIndexSet\",R,N,V_ineligibleSequences"
+ "T@\"NSNumber\",R,N,V_deletedDate"
+ "T@\"NSNumber\",R,N,V_deletedRunLength"
+ "T@\"NSNumber\",R,N,V_key"
+ "T@\"NSNumber\",R,N,V_rowId"
+ "T@\"NSNumber\",R,N,V_sequenceNumber"
+ "T@\"NSNumber\",R,N,V_writtenDate"
+ "T@\"NSObject<NSSecureCoding>\",R,N,V_value"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_blobPrimaryKeyColumnName"
+ "T@\"NSString\",R,N,V_blobTableName"
+ "T@\"NSString\",R,N,V_itemFieldTableName"
+ "T@\"NSString\",R,N,V_name"
+ "T@\"_PASLock\",R,N,V_compactedSequencesLock"
+ "TB,R,N,V_passed"
+ "TC,R,N,V_contentState"
+ "TC,R,N,V_dataProtectionClass"
+ "TC,R,N,V_databaseOptions"
+ "TC,R,N,V_indexedFieldType"
+ "TC,R,N,V_metaContentState"
+ "TC,R,N,V_predicateType"
+ "TI,N,V_localInstanceAddedCount"
+ "TI,N,V_localInstanceRemovedCount"
+ "TI,N,V_localInstanceUpdatedCount"
+ "TI,N,V_modifiedRowCount"
+ "TI,N,V_sharedItemAddedCount"
+ "TI,N,V_sharedItemRemovedCount"
+ "TI,N,V_sharedItemRevisedCount"
+ "TQ,R,N,V_cacheSpill"
+ "TQ,R,N,V_checksFailed"
+ "TQ,R,N,V_checksPerformed"
+ "TQ,R,N,V_indexedItemFieldCount"
+ "Td,R,N,V_busyTimeout"
+ "Ti,R,D,N"
+ "Tq,R,N,V_operatorType"
+ "Tq,V_connectionErrorCode"
+ "UNKNOWN"
+ "Unable to resolve valid SQL data type from indexed field configuration: %@"
+ "Unexpected column count in device query"
+ "Unexpected column count in provenance query"
+ "Unexpected dataProtectionClass value %ld for %@, defaulting to PROTECTION_CLASS_C"
+ "Unexpected row: %@ returned from table info (%@) in database %@"
+ "Unexpected service error processing donation: %@"
+ "Unexpected state"
+ "Unknown (%@)"
+ "Unknown: %u"
+ "Unrecognized identifier"
+ "Unrecognized itemIdentifierType: %u"
+ "Unsupported predicate (expecting indexed field type): %@"
+ "Unsupported predicate (fieldType not recognized): %@"
+ "Update in progress"
+ "WITH "
+ "XPC connection error handler invoked for client %@ error: %@"
+ "XPC connection terminated (%@) for client %@"
+ "XPC connection terminated for client %@"
+ "[%@]"
+ "_addItem:cacheContent:error:"
+ "_addedInstances"
+ "_ageOfMaintenanceFromPriorRunCount:maintenanceHistory:"
+ "_atomicallyCreateDataResource:withResourceGeneration:"
+ "_atomicallyRemoveDataResource:"
+ "_blobPrimaryKeyColumnName"
+ "_blobTableName"
+ "_busyTimeout"
+ "_cache"
+ "_cacheContentBuffers"
+ "_cacheSpill"
+ "_cachedInsertCommand"
+ "_calculateMinimumTombstoneAgeWithMaintenanceHistory:"
+ "_changeNotifier"
+ "_checksFailed"
+ "_checksPerformed"
+ "_combineAndCompactRowsForDeviceRowId:vectorType:sequenceRange:stateSets:error:"
+ "_compactContiguousTombstonesForDeviceRowId:minimumTombstoneAge:shouldDefer:error:"
+ "_compactContiguousTombstonesForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:"
+ "_compactedSequencesLock"
+ "_configuration"
+ "_connectionErrorCode"
+ "_connectionTerminationHandlerWithErrorCode:"
+ "_contentIndexer"
+ "_countDeviceRecords:withOptions:error:"
+ "_createProvenanceSelectCommandFromDeviceRowIdToClockValues:recordClass:state:columns:"
+ "_ctes"
+ "_currentPersonaShouldSkipEnumeratingContainer:"
+ "_currentPersonaShouldSkipEnumeratingResource:"
+ "_decodeLock"
+ "_deduplicateRemovedObjects:withAdded:presentNonAdded:outAll:outAdded:outRemoved:"
+ "_defaultXPCClientFactory"
+ "_deleteDeviceRowId:error:"
+ "_deleteExpiredItemInstances:"
+ "_deleteExpiredRemoteDeviceState:shouldTombstoneSet:error:"
+ "_deleteRecordsWithRowIds:vectorType:error:"
+ "_deleteSetWithItemType:descriptors:serviceProvider:error:"
+ "_deletedDate"
+ "_deletedRunLength"
+ "_descriptorAllowList"
+ "_deviceRowIdentifiersWithError:"
+ "_distinct"
+ "_eligibleSequences"
+ "_enumerateContentHashesMatchingPredicate:indexer:error:usingBlock:"
+ "_enumerateInstanceHashesMatchingPredicate:indexer:error:usingBlock:"
+ "_enumerateItemInstancesMatchingIndexedFieldPredicate:error:usingBlock:"
+ "_enumerateItemInstancesWithContentHash:error:usingBlock:"
+ "_enumerateItemInstancesWithInstanceHash:error:usingBlock:"
+ "_enumerateItemInstancesWithItemIdentifier:itemIdentifierType:error:usingBlock:"
+ "_enumerateItemInstancesWithSourceItemIdentifier:error:usingBlock:"
+ "_enumerateLocalInstancesWithError:selectingOnlyUnwritten:usingBlock:"
+ "_enumerateProvenanceRecordsForStateVector:recordClass:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
+ "_enumerateSharedItemsMatchingIndexedFieldPredicate:error:usingBlock:"
+ "_enumerateSharedItemsWithContentHash:error:usingBlock:"
+ "_enumerateSharedItemsWithInstanceHash:error:usingBlock:"
+ "_enumerateSharedItemsWithItemIdentifier:itemIdentifierType:error:usingBlock:"
+ "_enumerateSharedItemsWithSourceItemIdentifier:error:usingBlock:"
+ "_errorForUnexpectedRow:fromCommand:"
+ "_executeCreateTableStatements:error:"
+ "_executePragma:outError:"
+ "_expireAndTombstoneAllContentProvenanceForDeviceRowId:error:"
+ "_expireDeviceRowId:error:"
+ "_finishWithServiceOptions:error:"
+ "_fullSetDonationWithItemType:descriptors:options:serviceProvider:error:"
+ "_hasBeenDecoded"
+ "_incrementCachedIntegerWithKey:error:"
+ "_incrementLocalDeltaGeneration:"
+ "_incrementalSetDonationWithItemType:descriptors:options:serviceProvider:error:"
+ "_incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:error:"
+ "_indexedFieldType"
+ "_indexedFields"
+ "_indexedItemFieldCount"
+ "_indexerForPredicate:error:"
+ "_ineligibleSequences"
+ "_initWithInnerData:error:"
+ "_insertContent:contentHash:outExists:error:"
+ "_insertContentProvenanceWithDeviceRowId:contentHash:sequenceNumber:error:"
+ "_insertDeviceSite:returningRowId:error:"
+ "_insertIndexedFieldsForItemMessage:withBlobPrimaryKey:indexer:error:"
+ "_insertLocalContentWithProvenance:contentHash:isNew:error:"
+ "_insertMetaContent:instanceHash:outIsDuplicate:error:"
+ "_insertMetaContentProvenanceWithSourceItemIdHash:instanceHash:contentHash:error:"
+ "_issues"
+ "_itemFieldTableName"
+ "_itemMessageSubclass"
+ "_keyData"
+ "_lazyDecodingEnabled"
+ "_localDeviceRowId"
+ "_markTombstoneRowForVectorType:provenanceRowId:sequenceRange:error:"
+ "_metaContentIndexer"
+ "_operatorType"
+ "_pas_mappedArrayWithTransform:"
+ "_passed"
+ "_performMaintenanceForSet:withResource:accessAssertion:shouldDefer:"
+ "_persistCachedIntegers:"
+ "_predicateType"
+ "_presentNonAddedDevices"
+ "_presentNonAddedInstances"
+ "_priorActiveRemoteDeviceCount"
+ "_priorRevisionTokenDictionary"
+ "_priorRevisionTokenOrEmptyDictionary"
+ "_processRange:deviceRowId:vectorType:stateSets:error:shouldDefer:"
+ "_produceSelectClauseWithTableName:columnNames:count:distinct:"
+ "_purgeTombstonedResources:"
+ "_rebuildIndexedItemFieldTableWithIndexer:error:"
+ "_remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:error:"
+ "_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:"
+ "_removeItemsMatchingPredicate:error:"
+ "_removedInstances"
+ "_resolveSequenceNumberRangesOfDeltaVector:seenStateVectorBuilder:deviceMapping:tableName:"
+ "_resourceIsUserWithPotentialDomainOverrides:"
+ "_retriever"
+ "_rowId"
+ "_searchForKey:options:outSet:error:"
+ "_select"
+ "_selectContentProvenenceWithContentHash:deviceRowId:outSequenceNumber:error:"
+ "_selectDeviceRecords:withOptions:beyondExpirationDate:error:"
+ "_selectLatestDeviceRecordWithDeviceUUID:outRecord:error:"
+ "_selectLocalDeviceRecord:error:"
+ "_selectLocalInstanceCount:error:"
+ "_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:error:"
+ "_selectMetaContentWithInstanceHash:outRecord:error:"
+ "_selectPersistedValueForKey:outValue:valueClass:error:"
+ "_selects"
+ "_sequenceNumber"
+ "_setConfiguration"
+ "_setDatabase:"
+ "_setDonationWithItemType:descriptors:version:validity:serviceOptions:serviceProvider:error:"
+ "_setKeyCache"
+ "_sharedItemRevisedCount"
+ "_shouldFilterOutSet:withOptionsFilter:"
+ "_shouldSkipEnumeratingResourceForAccessError:"
+ "_sortedRecordsForDeviceRowId:vectorType:sequenceRange:error:"
+ "_sourceItemIdentifierHash"
+ "_stateSetsForDeviceRowId:vectorType:minimumTombstoneAge:shouldDefer:error:"
+ "_temporaryDirectoryForDataResource:"
+ "_tombstoneContentProvenanceRowsForExpiredDeviceRowId:error:"
+ "_tombstoneMetaContentWithSourceItemIdHash:tombstoneContentIfNoLongerPresent:error:"
+ "_tracker"
+ "_unionAll"
+ "_unionSelects"
+ "_updateDeviceRowId:deltaGeneration:expirationDate:error:"
+ "_updateLocalSourceVersion:localSourceValidityHash:error:"
+ "_updateMaintenanceHistory:"
+ "_updateMetaContent:tombstoneContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:"
+ "_updateModifiedRowCount"
+ "_updateTombstoneRowsForDeviceRowId:vectorType:recordsToCompact:sequenceRange:stateSets:error:"
+ "_updatedRevisionTokenDictionary"
+ "_upsertInteger:forKey:error:"
+ "_upsertInteger:forKey:skipIfNil:error:"
+ "_validateAndExtractKeyPrefixedIdentifier:outItemIdentifierType:outItemIdentifier:error:"
+ "_validateItemCacheContent:error:"
+ "_validateRow:fromCommmand:outItemInstance:error:"
+ "_validateRow:fromCommmand:outSharedItem:error:"
+ "_value"
+ "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:error:"
+ "_writtenDate"
+ "accessAssertion"
+ "addItemsWithContents:metaContents:cacheContents:reply:"
+ "addOrUpdateItem:cacheContent:error:"
+ "allSetsWithItemType:descriptors:options:error:"
+ "allSetsWithItemType:options:error:"
+ "allowsAccessToAllSetsWithMode:"
+ "appendAddedDevice:"
+ "appendAddedLocalInstance:"
+ "appendDatabaseValues:fromItemField:"
+ "appendFormat:"
+ "appendPresentNonAddedDevice:"
+ "appendPresentNonAddedLocalInstance:"
+ "appendRemovedDevice:"
+ "appendRemovedLocalInstance:"
+ "arrayByAddingObject:"
+ "arrayByAddingObjectsFromArray:"
+ "associatedSet"
+ "beginReadTransactionWithError:"
+ "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:"
+ "beginUpdateForDonationRequest:withDatabase:changeNotifier:error:"
+ "beginUpdateForMaintenanceOfSet:withDatabase:changeNotifier:error:"
+ "beginUpdateForPreparationOfSet:withDatabase:error:"
+ "beginWriteTransactionWithError:"
+ "blob"
+ "blobPrimaryKeyColumnName"
+ "blobTableName"
+ "busyTimeout"
+ "busy_timeout=%u"
+ "cacheDescriptorsFromAssociatedSet:error:"
+ "cacheRetrieverForAssociatedSet:withUseCase:error:"
+ "cacheSpill"
+ "cache_spill=%u"
+ "cancelSetDonation:"
+ "checkRunMarkerCorruptionInDatabase:set:error:"
+ "checkSequenceGapsAndOverlapsInDatabase:set:error:"
+ "checksFailed"
+ "checksPerformed"
+ "clientWithId:"
+ "columnNamesOfTable:error:"
+ "com.apple.CascadeSets.CCXPCClient"
+ "com.apple.CascadeSets.DatabaseWriter.Compaction"
+ "com.apple.CascadeSets.Donation"
+ "com.apple.CascadeSets.SetStoreAdmin"
+ "com.apple.email.SearchIndexer"
+ "com.apple.mobilemail"
+ "combined"
+ "commandForKey:"
+ "commitUpdate:"
+ "compactContiguousTombstonesWithMinimumTombstoneAge:shouldDefer:error:"
+ "compactedSequencesLock"
+ "configuredColumnNames"
+ "connectionErrorCode"
+ "connectionToDatabaseAtURL:dataProtectionClass:openMode:busyTimeout:accessAssertion:"
+ "containsIndex:"
+ "content_field"
+ "content_provenance"
+ "copyWithFieldType:"
+ "created_date"
+ "criterionWithColumnName:GREATERTHANColumnValue:"
+ "criterionWithColumnName:sqlOperator:columnValue:"
+ "d24@0:8@16"
+ "d32@0:8Q16@24"
+ "d40@0:8{shared_ptr<std::vector<unsigned int>>=^v^{__shared_weak_count}}16d32"
+ "dataWithJSONObject:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "databaseWriterForDonationRequest:outDataResource:error:"
+ "decodeFieldValuesFromData:error:"
+ "decoded revisionToken JSON did not produce a dictionary: %@"
+ "deleteAllLocalInstances:"
+ "deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord:"
+ "deleteSetWithItemType:completion:"
+ "deleteSetWithItemType:descriptors:error:"
+ "deleteSetWithItemType:error:"
+ "deleteSourceItemIdHash:error:"
+ "deletedDate"
+ "deletedRunLength"
+ "deleted_date"
+ "deleted_run_length"
+ "deltaProduced"
+ "descriptionForSet:"
+ "descriptorAllowList"
+ "descriptorAllowList:allowsSet:"
+ "documentCachePredicateFromAssociatedSetPredicate:error:"
+ "documentCacheSetIdentifier"
+ "domainIdentifier"
+ "donationWithName:itemType:service:serviceOptions:errorCode:priors:"
+ "dropTableIfExistsWithName:"
+ "eligibleSequences"
+ "endSetDonationWithOptions:revisionToken:reply:"
+ "ensureDecodedWithError:"
+ "enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:"
+ "enumerateAllSetsWithItemType:descriptors:options:error:usingBlock:"
+ "enumerateAllSetsWithItemType:error:usingBlock:"
+ "enumerateAllSetsWithItemType:options:error:usingBlock:"
+ "enumerateAllSetsWithOptions:error:usingBlock:"
+ "enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
+ "enumerateInsertCommandsForItemMessage:withBlobPrimaryKey:error:usingBlock:"
+ "enumerateItemInstancesMatchingPredicate:error:usingBlock:"
+ "enumerateLocalInstancesMatchingPredicate:error:usingBlock:"
+ "enumerateMetaContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
+ "enumerateObjectsUsingBlock:"
+ "enumerateRangesInRange:options:usingBlock:"
+ "enumerateReadableSetsWithIdentifiers:descriptors:resourceOptions:startAfterSet:sorted:error:usingBlock:"
+ "enumerateSetPartitionsWithIdentifier:descriptors:container:startAfterSet:sorted:error:usingBlock:"
+ "enumerateSharedItemsMatchingPredicate:error:usingBlock:"
+ "enumerateSourceItemIdHashesMatchingPredicate:error:usingBlock:"
+ "enumerateUnwrittenLocalInstancesWithError:usingBlock:"
+ "errorDomain"
+ "expirationDateFieldType"
+ "expireRemoteDeviceUUID:error:"
+ "filter"
+ "finalizeSetChange"
+ "foreign_keys=ON"
+ "fullSetDonationWithItemType:descriptors:error:"
+ "fullSetDonationWithItemType:descriptors:options:error:"
+ "fullSetDonationWithItemType:error:"
+ "getUUIDBytes:"
+ "h"
+ "hasContentHash:"
+ "hasContentInformation"
+ "hasMetaContentInformation"
+ "hashFromCacheContent:error:"
+ "html"
+ "htmlFromCacheContent:error:"
+ "idx_cp_content_hash"
+ "idx_cp_sequence_number"
+ "idx_device_options"
+ "idx_device_uuid"
+ "idx_field"
+ "idx_mp_content_hash"
+ "idx_mp_instance_hash"
+ "idx_mp_sequence_number"
+ "idx_mp_source_item_id_hash"
+ "idx_mp_written_date"
+ "incrementalSetDonationWithItemType:descriptors:error:"
+ "incrementalSetDonationWithItemType:descriptors:options:error:"
+ "incrementalSetDonationWithItemType:descriptors:version:validity:error:"
+ "incrementalSetDonationWithItemType:error:"
+ "indexedFieldType"
+ "indexedFields"
+ "indexedItemFieldCount"
+ "indexerFromConfiguration:forBlobTable:set:"
+ "ineligibleSequences"
+ "initLazyDecodedWithTrustedItemMessageData:error:"
+ "initWithAssertionOverride:changeNotifier:"
+ "initWithContentHash:contentSequenceNumber:contentDeletedRunLength:contentData:sourceItemIdHash:instanceHash:metaContentSequenceNumber:metaContentDeletedRunLength:metaContentData:deviceRowId:"
+ "initWithFieldType:dataType:descriptorAllowList:"
+ "initWithFieldType:dataType:indexedFieldType:descriptorAllowList:"
+ "initWithIndexedFieldConfiguration:blobTableName:itemType:"
+ "initWithIndexesInRange:"
+ "initWithIneligibleSequences:eligibleSequences:compactedSequences:"
+ "initWithItemMessageData:error:"
+ "initWithName:itemType:service:serviceOptions:errorCode:priors:flushThreshold:"
+ "initWithName:select:"
+ "initWithPassed:checksPerformed:checksFailed:issues:"
+ "initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:busyTimeout:cacheSpill:"
+ "initWithPredicateType:fieldType:value:operatorType:"
+ "initWithRemoteObjectInterface:exportedInterface:connection:clientId:useCase:"
+ "initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:useCase:"
+ "initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:useCase:"
+ "initWithRowId:"
+ "initWithSelects:"
+ "initWithSet:"
+ "initWithSet:database:changeNotifier:request:isPrepared:error:"
+ "initWithSet:retriever:"
+ "initWithSetIdentifier:setUUID:resourceDomain:configuredDescriptors:syncPolicy:indexedFields:dataProtectionClass:"
+ "initWithSharedIdentifier:"
+ "initWithSharedIdentifier:instanceIdentifier:content:metaContent:sourceItemIdentifierHash:"
+ "initWithSourceItemIdentifier:associatedInstanceUUID:associatedDomainIdentifier:expirationDate:documentType:error:"
+ "initWithTable:joinType:joinCriterion:"
+ "initWithText:html:error:"
+ "insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:error:"
+ "insertRemoteContent:contentHash:sequenceNumber:onDeviceRowId:error:"
+ "integer"
+ "interruptionErrorCode"
+ "invalidationErrorCode"
+ "isCacheEnabledAssociatedSet:"
+ "isCacheEnabledSourceIdentifier:"
+ "isDocumentCacheSet:"
+ "isEqualToItemFieldPredicate:"
+ "isEqualToRecord:"
+ "isFieldType:applicableToBlobTable:"
+ "isSourceItemIdentifierFieldType:"
+ "isValidPredicate:error:"
+ "issues"
+ "itemCacheContent"
+ "itemCacheContentWithText:html:error:"
+ "itemFieldTableName"
+ "itemIdentifierComponentOfKeyPrefixedIdentifier:error:"
+ "itemInstanceIdentifier"
+ "itemMessageData"
+ "itemMessageSubclass"
+ "itemRetrieverForSet:database:"
+ "itemRetrieverForSet:database:setConfiguration:contentIndexer:metaContentIndexer:"
+ "itemRetrieverForSet:readAccess:"
+ "itemRetrieverForSet:useCase:"
+ "itemRetrieverWithUseCase:"
+ "joinDonatedDocumentCacheContents:withAssociatedItemContents:associatedItemMetaContents:associatedSet:outContents:outMetaContents:error:"
+ "journal_mode=WAL"
+ "keyComponentOfKeyPrefixedIdentifier:error:"
+ "keyPrefixedIdentifier"
+ "keyPrefixedIdentifier: %@ has unexpected itemIdentifierType bits: %u"
+ "keyPrefixedIdentifier: %@ missing expected UUID variant bits"
+ "keyPrefixedIdentifier: %@ missing expected UUID version 8 bits"
+ "keyPrefixedIdentifierForItemInstance:"
+ "keyPrefixedIdentifierForSharedItem:"
+ "keyPrefixedSourceItemIdentifierForItemInstance:"
+ "lazilyDecodedContentMessageForItemType:trustedItemMessageData:error:"
+ "lazilyDecodedMetaContentMessageForItemType:trustedItemMessageData:error:"
+ "localDeviceRowId"
+ "localInstanceDeltaProduced"
+ "localizedDescription"
+ "maintenanceHistory"
+ "metacontent_field"
+ "metacontent_provenance"
+ "modified_date"
+ "noBusyWait"
+ "non"
+ "numberValue"
+ "numberWithFloat:"
+ "operatorType"
+ "passed"
+ "performIntegrityCheckOnSets:error:"
+ "performMaintenanceWithShouldTombstone:shouldDefer:error:"
+ "predicate"
+ "predicate %@ not supported by indexed field configuration"
+ "predicate missing field value: %@"
+ "predicateForAssociatedInstanceUUID:error:"
+ "predicateForAssociatedSourceItemIdentifier:error:"
+ "predicateForCacheContentHash:error:"
+ "predicateType"
+ "predicateWithFieldType:equalsDataValue:error:"
+ "predicateWithFieldType:equalsNumberValue:error:"
+ "predicateWithFieldType:equalsStringValue:error:"
+ "predicateWithFieldType:greaterThanNumberValue:error:"
+ "predicateWithFieldType:greaterThanOrEqualToNumberValue:error:"
+ "predicateWithFieldType:lessThanNumberValue:error:"
+ "predicateWithFieldType:lessThanOrEqualToNumberValue:error:"
+ "predicateWithItemInstanceIdentifier:error:"
+ "predicateWithKeyPrefixedIdentifier:error:"
+ "predicateWithSharedItemIdentifier:error:"
+ "predicateWithSourceItemIdentifier:error:"
+ "prefixedInstanceIdentifierAsUUID:"
+ "prefixedSharedIdentifierAsUUID:"
+ "prepareDatabaseWithLocalDeviceSite:error:"
+ "prepareItemFieldIndexes:"
+ "priorRevisionTokenWithKey:"
+ "propertyListWithData:options:format:error:"
+ "protectionClass"
+ "q24@?0@\"CCIndexedFieldConfiguration\"8@\"CCIndexedFieldConfiguration\"16"
+ "real"
+ "registerItem:cacheContent:error:"
+ "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:error:"
+ "remoteObjectProxy:errorHandler:"
+ "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:"
+ "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:"
+ "removeIndexesInRange:"
+ "removeItemsMatchingPredicate: %@"
+ "removeItemsMatchingPredicate:error:"
+ "removeItemsMatchingPredicate:reply:"
+ "removeObjectForKey:"
+ "removeSourceItemIdentifier:reply:"
+ "requestBiomeEndpointForAppScopedService: biome endpoint requested from an invalid context"
+ "retrieveCacheContentWithPredicate:retriever:error:"
+ "revisionTokenKey"
+ "rollbackUpdate:"
+ "rowId"
+ "select"
+ "selectAllDeviceRecords:"
+ "selectFromTableWithName:columns:count:distinct:joinTables:criterion:order:limit:offset:ctes:unionSelects:unionAll:"
+ "selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:"
+ "selects"
+ "sequenceNumber"
+ "sequence_number"
+ "setCommand:forKey:"
+ "setCommonTableExpressions:"
+ "setConnectionErrorCode:"
+ "setDistinct:"
+ "setJoinTables:"
+ "setLocalInstanceAddedCount:"
+ "setLocalInstanceRemovedCount:"
+ "setLocalInstanceUpdatedCount:"
+ "setModifiedRowCount:"
+ "setObject:atIndexedSubscript:"
+ "setSharedItem:"
+ "setSharedItemAddedCount:"
+ "setSharedItemRemovedCount:"
+ "setSharedItemRevisedCount:"
+ "setUnionWithSelects:unionAll:"
+ "setWithKey:error:"
+ "sharedItemIdentifier"
+ "sharedItemRevisedCount"
+ "singleItemInstanceMatchingPredicate:error:"
+ "singleSharedItemMatchingPredicate:error:"
+ "sourceItemIdentifierHash"
+ "spotlightInlineTextContent"
+ "spotlightInlineTextContentAllBundles"
+ "sqlite_trace[%@]: (%0.0f ms) %s"
+ "startFullSetDonationWithItemType:descriptors:error:"
+ "startFullSetDonationWithItemType:descriptors:options:error:"
+ "startFullSetDonationWithItemType:error:"
+ "startIncrementalSetDonationWithItemType:descriptors:error:"
+ "startIncrementalSetDonationWithItemType:descriptors:options:error:"
+ "startIncrementalSetDonationWithItemType:descriptors:version:validity:error:"
+ "startIncrementalSetDonationWithItemType:error:"
+ "stringForItemFieldDataType:"
+ "subarrayWithRange:"
+ "text"
+ "textFromCacheContent:error:"
+ "tombstoneContentSequenceNumbersInRange:forRemoteDeviceRowId:error:"
+ "unexpected encoded revisionToken: %@"
+ "unexpected keyPrefixedIdentifier: %@"
+ "unsafeGuardedData"
+ "updateContent:andMetaContent:sourceItemIdHash:contentHash:instanceHash:isDuplicate:error:"
+ "updateLastLocalDonationDate:error:"
+ "updateMetaContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:"
+ "updateRevisionToken:withKey:error:"
+ "v16@?0@\"NSMutableIndexSet\"8"
+ "v16@?0@\"NSObject<CCDatabaseValue>\"8"
+ "v20@?0C8@\"NSError\"12"
+ "v24@0:8@?<v@?C@\"NSError\">16"
+ "v24@?0@\"CCContentProvenanceRecord\"8^B16"
+ "v24@?0@\"CCItemInstance\"8^B16"
+ "v24@?0@\"CCMetaContentProvenanceRecord\"8^B16"
+ "v24@?0@\"CCSharedItem\"8^B16"
+ "v24@?0@\"NSNumber\"8^B16"
+ "v24@?0@\"NSObject<CCProvenanceRecord>\"8^B16"
+ "v28@0:8@16B24"
+ "v28@0:8@16C24"
+ "v28@?0C8@\"NSError\"12@\"CCDonationServicePriors\"20"
+ "v32@0:8@\"CCItemFieldPredicate\"16@?<v@?C@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?C@\"NSError\">24"
+ "v32@?0@\"NSData\"8Q16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v36@0:8S16@\"NSString\"20@?<v@?C@\"NSError\">28"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@?<v@?C@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v56@0:8S16@\"NSString\"20@\"NSNumber\"28@\"NSString\"36S44@?<v@?C@\"NSError\"@\"CCDonationServicePriors\">48"
+ "v56@0:8S16@20@28@36S44@?48"
+ "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?C@\"NSError\">52"
+ "v64@0:8@16@24@32^@40^@48^@56"
+ "validateItemCacheContent:error:"
+ "varchar"
+ "writtenDate"
+ "written_date"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{shared_ptr<std::vector<unsigned int>>=\"__ptr_\"^v\"__cntrl_\"^{__shared_weak_count}}"
- " joinTables: %@"
- " provenanceRowId: %@, deviceRowId: %@, instanceHash: %@, contentHash: %@, contentSequenceNumber: %@, endOfRun: %@, contentState: %@, metaContentSequenceNumber: %@, endOfRun: %@, metaContentState: %@"
- " table: %@, criterion: %@"
- "%@ %@"
- "%@ (%u)"
- "%@ - invalidating connection"
- "%@ maintenance at container: %@ %@"
- "%@ startTimeMicros: %@"
- "(%@) Aborting maintenance after failing to record date"
- "(%@) Aborting maintenance due to deferral signal"
- "(%@) Creating database in temporary path: %@"
- "(%@) Database cleanup is %@ required. %@ rows have been modified since last cleanup"
- "(%@) Failed to begin transaction: %@"
- "(%@) Failed to clean database"
- "(%@) Failed to cleanup database: %@"
- "(%@) Failed to commit transaction: %@"
- "(%@) Failed to complete data resource-specific maintenance"
- "(%@) Failed to open database: %@"
- "(%@) Failed to reset rows modified in database: %@"
- "(%@) Failed to rollback transaction: %@"
- "(%@) Failed to select database rows modified with error: %@"
- "(%@) Failed to select persisted key: %@ with error: %@"
- "(%@) Finished database maintenance"
- "(%@) Key not cached: %@"
- "(%@) Maintenance failed to tombstone set: %@"
- "(%@) Persisted value for key: %@ is: %@"
- "(%@) Starting data resource-specific maintenance"
- "(%@) Successfully committed database transaction"
- "(%@) Successfully renamed temporary directory and moved to final path: %s"
- "(%@) Tombstoning set after maintenance removed all remaining state"
- "(%u) \"%@\""
- ":[%@]"
- "<%@:%@:%llu%@%@%@>"
- "@\"CCDataResource\""
- "@\"CCDonateServicePriors\""
- "@\"CCProvenanceRecord\""
- "@\"CCSQLCommandJoin\""
- "@\"NSArray\"40@0:8S16S20@\"NSArray\"24^@32"
- "@\"NSObject<CCDatabaseReadWriteAccess>\""
- "@\"NSObject<CCDonateService>\""
- "@\"NSObject<CCDonateService>\"24@0:8@\"NSString\"16"
- "@28@0:8@16S24"
- "@36@0:8@16@24B32"
- "@40@0:8@16C24C28@32"
- "@40@0:8S16S20@24^@32"
- "@44@0:8@16i24q28@36"
- "@52@0:8@16S24@28q36@44"
- "@52@0:8@16q24q32i40q44"
- "@56@0:8@16@24Q32@40@48"
- "@60@0:8@16S24@28q36@44Q52"
- "@64@0:8@16@24@32@40S48S52@56"
- "@76@0:8@16@24B32@36@44@52@60@68"
- "@?20@0:8S16"
- "@?24@0:8@?16"
- "Aborted"
- "Aborted maintenance for resource: %@"
- "Accepted"
- "All conditions met for set tombstone eligibility. %@"
- "Attempt to insert:\n\n\t{instanceHash: %@ metaContent: %@}\n\ncollided with existing record:\n\n\t{instanceHash: %@ metaContent: %@}"
- "Attempted to cleanup while transaction is active"
- "B24@0:8@?16"
- "B24@0:8B16B20"
- "B24@?0@\"NSObject<CCDatabaseReadWriteAccess>\"8^Q16"
- "B28@0:8@16B24"
- "B28@0:8B16@?20"
- "B32@0:8#16^@24"
- "B32@0:8@?16^B24"
- "B32@0:8Q16@24"
- "B36@0:8@16@24B32"
- "B36@0:8^@16C24@28"
- "B36@0:8^B16@24B32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^B32"
- "B40@0:8@16^@24#32"
- "B40@0:8@16^B24^B32"
- "B40@0:8Q16@24^@32"
- "B40@0:8^@16S24S28@?32"
- "B40@0:8^@16S24S28@?<v@?@\"CCSet\">32"
- "B40@0:8{_NSRange=QQ}16@32"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24B32B36^@40"
- "B48@0:8@16@24^@32^B40"
- "B48@0:8^@16S24S28@\"NSArray\"32@?<v@?@\"CCSet\">40"
- "B48@0:8^@16S24S28@32@?40"
- "B52@0:8@16C24@28@36@44"
- "B56@0:8@16@24@32@40q48"
- "B56@0:8^@16^@24^@32^@40^@48"
- "B60@0:8@16C24C28C32@36^@44@?52"
- "B60@0:8^@16S24@28@36@44@?52"
- "B64@0:8@16@24@32@40@48^@56"
- "B64@0:8@16@24@32@40@48^B56"
- "B64@0:8^@16C24@28@36@44B52@?56"
- "B68@0:8@16^@24@32@40@48@56B64"
- "B72@0:8@16@24@32@40@48@56^B64"
- "B72@0:8@16@24@32@40q48@56^@64"
- "B72@0:8@16^@24^@32^@40^@48^@56^B64"
- "B80@0:8@16@24@32@40@48@56@64^B72"
- "BEGIN TRANSACTION"
- "Beginning transaction"
- "CCDataResourceWriter"
- "CCDatabaseUpdater"
- "CCDonateService"
- "CCDonateServiceClient"
- "CCDonateServicePriors"
- "CCDonateServiceProvider"
- "CCDonateServiceServer"
- "CCDonateXPCClient"
- "CCDonateXPCClientFactory"
- "CCInstanceRecord"
- "CCSQLCommandJoin"
- "CCSetChangeRelayClient"
- "CCSetDonation.instance"
- "CREATE INDEX \"%@\" ON \"%@\" (\"%@\" ASC);"
- "CREATE INDEX \"%@\" ON \"%@\" (\"%@\",\"%@\",\"%@\" DESC);"
- "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, PRIMARY KEY (\"%@\") FOREIGN KEY (\"%@\") REFERENCES \"%@\" (\"%@\") ON UPDATE CASCADE ON DELETE CASCADE );"
- "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer PRIMARY KEY, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, \"%@\" integer NULLABLE, FOREIGN KEY (\"%@\") REFERENCES \"%@\" (\"%@\") ON UPDATE CASCADE ON DELETE CASCADE ); "
- "Cannot expire local device record: %@ with deviceUUID: %@. %@"
- "Cannot re-register local device record: %@ with site %@. %@"
- "Cannot register local device with invalid device site: %@"
- "Cannot request access for user-domain resource: %@ as persona: %@"
- "Cannot update device row id: %@ with nil expiration date. %@"
- "Cleaning database."
- "Clear prior state of deletion compaction command: %@"
- "Client process is not authorized to donate"
- "Client process is not authorized to donate this set"
- "Client timed out waiting %lf seconds for donate service to accept a new donation %@"
- "Compact content sequence numbers command: %@"
- "Compact content sequence numbers failed. error: %@"
- "Compact metacontent sequence numbers command failed. error: %@"
- "Compact metacontent sequence numbers command: %@"
- "Completed"
- "Completed maintenance for resource (%@)"
- "Could not begin database transaction with error: %@"
- "Could not close database connection with error: %@"
- "Could not commit database transaction with error: %@"
- "Could not create database, failed to register local device site"
- "Could not obtain set from data resource: %@ with error: %@"
- "Could not open database connection with error: %@"
- "Could not prepare database connection with error: %@"
- "Could not remove resource: %@ error: %@"
- "Could not resolve set identifier for item type %hu'"
- "Could not resolve temporary database path with error: %@"
- "Could not resolve temporary directory path with error: %@"
- "Current persona is default (%@) Skipping serialized set with a nonnull persona: %@"
- "Database initializer -"
- "Delete command: %@"
- "Delete dangling content records failed %@ error: %@"
- "Delete failed. %@ error: %@"
- "Delete failed. error: %@"
- "Delete failed: %@"
- "Deleted"
- "Deleting any content records no longer referenced by provenance"
- "Deleting device record: %@"
- "Device identifier UUID is nil: %@. %@"
- "Device record enumeration failed: %@ %@"
- "Device site %@ already expired (compared to: %@). %@"
- "Device site %@ matches local deviceUUID: %@. %@"
- "Device table contains nonzero remote device records - not eligible for tombstone"
- "Donate service connection interrupted"
- "Donate service connection invalidated"
- "Donate service encountered an internal error"
- "Donate service timed out attempting to process donation"
- "Donation %@ request (%@) failed: %@"
- "Expected instance hash and content hash from provenance table select but got unexpected row: %@"
- "Expected itemRowId and hash from select but got unexpected row: %@"
- "Expected rowId from select but got unexpected row: %@"
- "Expiring device record: %@"
- "Expiring device record: %@ and associated state which is now invalid due to registration of device site %@. %@"
- "Extending expiration date from %@ to %@ due to re-attestation of device site %@ compared to record: %@. %@"
- "Failed to build delete with params: {%@}, %@"
- "Failed to build provenance with params: {%@}, %@ error: %@"
- "Failed to build update with params: (%@}, %@"
- "Failed to check for local source donation: %@"
- "Failed to check for present content: %@"
- "Failed to clear prior state of deletion compaction. error: %@"
- "Failed to construct device mapping: %@"
- "Failed to construct local instance enumerator. %@ error: %@"
- "Failed to count modified rows after content delete %@ error: %@"
- "Failed to count modified rows after provenance update %@ error: %@"
- "Failed to create table on prepare operation."
- "Failed to enable WAL journal_mode with errorCode: %@, extendedCode: %@"
- "Failed to establish connection to donate service for set donation %@"
- "Failed to extract content and metacontent state vectors. error: %@"
- "Failed to open set donation %@ - %@"
- "Failed to retrieve the number of tombstones being deleted, error: %@"
- "Failed to select persisted value for key: %@ error: %@ %@"
- "Failed to select rows modified in database: %@"
- "Failed to update last maintenance date: %@"
- "Failed to update rows modified in database: %@"
- "Failed to write persisted value: %@ for key: %@ error: %@ %@"
- "Finished database tombstone compaction operation with deleted count: %@"
- "Found %u active remote device records past their expiration date %@"
- "Found %u expired remote device records past the tombstone preservation interval %@"
- "Found no device record to expire with deviceUUID: %@. %@"
- "Ignoring re-attested expiration date of device site %@ which occurs sooner than the stored device record: %@. %@"
- "Ignoring registration of relayed device site %@ matching peerDeviceUUID: %@. %@"
- "Ignoring service response (%@) for timed out request %@"
- "Incrementing local delta generation from %@ to %@, %@"
- "Insert %@ failed. %@ error: %@"
- "Insert failed. %@ error: %@"
- "Inserting device record due to re-attestation of device site %@. %@"
- "Inserting first record of device site %@. %@"
- "Inserting latest record of device site %@. %@"
- "Local instance enumeration failed. %@ error: %@"
- "No item exists with sourceItemIdHash: %@"
- "PRAGMA busy_timeout = %d"
- "PRAGMA cache_spill = %d"
- "PRAGMA foreign_keys = ON;"
- "PRAGMA journal_mode=WAL"
- "Present"
- "Record with sourceItemIdHash: %@ has already been updated - donated set (%@) contains items with duplicate sourceItemIdentifiers"
- "Select (%@) returned an unexpected number of local device records: %@. %@"
- "Select failed. %@ error: %@"
- "Set contains present content - not eligible for tombstone"
- "Set has received a local source donation - not eligible for tombstone"
- "Skip enumerating container: %@ as persona: %@"
- "Skipping access request: %@"
- "Skipping new registration of device site %@. %@"
- "Skipping registration - delta generation of record: %@ is more recent than device site %@. %@"
- "Skipping registration - resource generation of record: %@ is more recent than device site %@. %@"
- "Skipping unattested registration of device site %@ for expired record: %@. %@"
- "Skipping unattested registration of device site %@ which would progress the deltaGeneration for record: %@. %@"
- "Skipping unattested registration of device site %@. %@"
- "Starting database tombstone compaction operation"
- "T@\"CCDataResource\",R,N,V_dataResource"
- "T@\"CCDonateServicePriors\",R,N,V_priors"
- "T@\"CCProvenanceRecord\",R,N,V_provenance"
- "T@\"NSArray\",R,N,V_joinTables"
- "T@\"NSMutableSet\",R,N,V_addedDevices"
- "T@\"NSMutableSet\",R,N,V_addedLocalInstances"
- "T@\"NSMutableSet\",R,N,V_allDevices"
- "T@\"NSMutableSet\",R,N,V_allLocalInstances"
- "T@\"NSMutableSet\",R,N,V_removedDevices"
- "T@\"NSMutableSet\",R,N,V_removedLocalInstances"
- "T@\"NSNumber\",R,N,V_contentSequenceNumberEndOfRun"
- "T@\"NSNumber\",R,N,V_contentState"
- "T@\"NSNumber\",R,N,V_metaContentSequenceNumberEndOfRun"
- "T@\"NSNumber\",R,N,V_metaContentState"
- "T@\"NSNumber\",R,N,V_modified"
- "T@\"NSNumber\",R,N,V_provenanceRowId"
- "T@\"NSNumber\",R,N,V_uniqueHash"
- "T@\"NSString\",R,D,N"
- "TI,R,N,V_localInstanceAddedCount"
- "TI,R,N,V_localInstanceRemovedCount"
- "TI,R,N,V_localInstanceUpdatedCount"
- "TI,R,N,V_modifiedRowCount"
- "TI,R,N,V_sharedItemAddedCount"
- "TI,R,N,V_sharedItemProvenanceUpdatedCount"
- "TI,R,N,V_sharedItemRemovedCount"
- "TS,N,V_sharedItemChangeType"
- "TS,R,N,V_interruptionCode"
- "TS,V_failureCode"
- "Tq,R,N,V_databaseOptions"
- "Undefined"
- "Unexpected - count not produced from select: %@"
- "Unexpected peer device site %@ not matching peerDeviceUUID: %@. %@"
- "Unexpected remote device site %@ has isLocal flag set. %@"
- "Unexpected remote device site %@ missing expiration date. %@"
- "Unexpected state vector type: %u"
- "Update failed. %@ error: %@"
- "Update provenance for content failed. %@ error: %@"
- "Update provenance for metacontent failed. %@ error: %@"
- "Update provenance rows for content state failed. %@ error: %@"
- "VACUUM"
- "Vv36@0:8S16@\"NSString\"20@?<v@?S>28"
- "Vv36@0:8S16@20@?28"
- "Vv56@0:8S16@\"NSString\"20Q28@\"NSString\"36S44@?<v@?Sq@\"CCDonateServicePriors\">48"
- "Vv56@0:8S16@20Q28@36S44@?48"
- "XPC connection terminated (%u) for client %@"
- "XPC request hit error (%@) for client %@"
- "[BiomeAccess] CCDataResourceReadAccess could not obtain access assertion for %@ using useCase: %@ with error: %@"
- "_addItem:error:"
- "_cleanupDatabaseIfRequired"
- "_clearTombstoneStatus:"
- "_computeUniqueHash"
- "_contentSequenceNumberEndOfRun"
- "_createDatabaseWithLocalDeviceSite:"
- "_createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:"
- "_createTableWithRecordClass:error:"
- "_dataResource"
- "_deleteDeviceRowId:"
- "_deleteSourceItemIdHash:outProvenanceRowId:"
- "_didCompleteMaintenance:shouldDefer:"
- "_enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:"
- "_errorHandlerWithCompletion:"
- "_executeDatabaseTransactionUsingBlock:"
- "_expireAndTombstoneAllProvenanceForDeviceRowId:"
- "_expireDeviceRowId:"
- "_failureCode"
- "_failureHandlerWithResponse:"
- "_finishWithOptions:error:"
- "_incrementCachedIntegerWithKey:"
- "_incrementLocalDeltaGeneration"
- "_insertContent:contentHash:outExists:"
- "_insertContent:contentHash:outSequenceNumber:"
- "_insertDeviceSite:returningRowId:"
- "_insertLocalInstanceForItemWithSourceItemIdHash:provenanceRowId:"
- "_insertMetaContent:instanceHash:outSequenceNumber:outIsDuplicate:"
- "_insertNewProvenanceAndTombstonePriorProvenanceRow:outInsertedProvenanceRowId:instanceHash:contentHash:contentSequenceNumber:metaContentSequenceNumber:contentChanged:"
- "_insertProvenanceForItemWithContentHash:contentSequenceNumber:metaContentSequenceNumber:instanceHash:onDeviceRowId:insertedRowId:"
- "_interruptionCode"
- "_isDefaultPersonaRequestingUserResource:"
- "_isLocalDonation"
- "_join"
- "_loadDatabase:"
- "_metaContentSequenceNumberEndOfRun"
- "_modified"
- "_persistCachedIntegers"
- "_persistDateWithDeltaProduced:isFullSet:"
- "_persistRevisionTokenIfNotNil:"
- "_produceSelectClauseWithTableName:columnNames:count:"
- "_provenance"
- "_provenanceRowId"
- "_remoteObjectProxy:errorCompletion:"
- "_remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
- "_removeResource:"
- "_resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:"
- "_selectDeviceRecords:withOptions:beyondExpirationDate:"
- "_selectLatestDeviceRecordWithDeviceUUID:outRecord:"
- "_selectLocalDeviceProvenenceWithContentHash:outSequenceNumber:"
- "_selectLocalDeviceRecord:"
- "_selectLocalInstanceCount:"
- "_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:"
- "_selectMetaContentWithInstanceHash:outRecord:"
- "_selectPersistedValueForKey:outValue:valueClass:"
- "_selectProvenanceWithContentHash:outLocalInstancePresent:outRemoteContentPresent:"
- "_selectProvenenceWithRowId:outInstanceHash:outContentHash:"
- "_setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:"
- "_sharedItemProvenanceUpdatedCount"
- "_shouldEnumerateContainer:"
- "_temporaryDirectoryURLWithError:"
- "_tombstoneMetaContentWithProvenanceRowId:tombstoneContentIfNoLongerPresent:"
- "_tombstoneProvenanceRowsForExpiredDeviceRowId:"
- "_tombstoneResource:"
- "_uniqueHash"
- "_updateDeviceRowId:deltaGeneration:expirationDate:"
- "_updateLocalInstanceRowId:provenanceRowId:"
- "_updateLocalSourceVersion:localSourceValidityHash:"
- "_upsertInteger:forKey:"
- "_upsertInteger:forKey:skipIfNil:"
- "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:"
- "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:"
- "abortSetDonation"
- "add %u item(s)"
- "addItemsWithContents:metaContents:completion:"
- "allSetsWithOptions:itemType:descriptors:error:"
- "appendAddedDevices:"
- "appendAddedLocalInstances:"
- "appendAllDevices:"
- "appendAllLocalInstances:"
- "appendRemovedDevices:"
- "appendRemovedLocalInstances:"
- "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:"
- "beginTransactionWithError:"
- "cleanup:"
- "client"
- "com.apple.CascadeSets.Donate"
- "compactContiguousRunsOfDeletes:"
- "completion parameter is nil."
- "connectionToDatabaseAtURL:dataProtectionClass:openMode:accessAssertion:"
- "containsChangesAfterDeduplication"
- "containsContentHash:"
- "contentSequenceNumber is unexpectedly nil %@"
- "contentSequenceNumberEndOfRun"
- "content_sequence_number"
- "content_sequence_number_end_of_run"
- "content_state"
- "d40@0:8{shared_ptr<std::vector<unsigned short>>=^v^{__shared_weak_count}}16d32"
- "dataResource"
- "defaultDataProtectionClass"
- "deleteAllLocalInstances"
- "deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord"
- "deleteExpiredRemoteDeviceState:shouldTombstoneSet:"
- "deleteSetWithItemType:descriptors:serviceProvider:completion:"
- "deleteSourceItemIdHash:"
- "device site %@ has regressed deltaGeneration compared with record: %@. %@"
- "device site %@ has regressed resourceGeneration compared with record: %@. %@"
- "device site %@ not expected to invalidate record: %@. %@"
- "device site %@ not expected to progress deltaGeneration for record: %@. %@"
- "deviceUUID: %@ record already expired: %@. %@"
- "donationWithName:itemType:service:errorCode:priors:"
- "endSetDonationWithOptions:revisionToken:completion:"
- "enumerateAllSets:withOptions:itemType:descriptors:usingBlock:"
- "enumerateAllSets:withOptions:itemType:usingBlock:"
- "enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:"
- "enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
- "enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:"
- "enumerateUnmodifiedLocalInstancesUsingBlock:"
- "expireRemoteDeviceUUID:"
- "failureCode"
- "finishAndDetectDelta:updateRevisionToken:isFullSet:"
- "hasDatavaultEntitlement"
- "idx_instance_modified"
- "idx_provenance_content_hash"
- "idx_provenance_content_hash_metacontent_state"
- "idx_provenance_content_sequence_number"
- "idx_provenance_metacontent_sequence_number"
- "incrementRowsModified:database:"
- "incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:"
- "initWithAssertionOverride:"
- "initWithDataResource:accessAssertion:"
- "initWithDatabase:request:"
- "initWithJoinType:joinTables:"
- "initWithName:itemType:service:errorCode:priors:flushThreshold:"
- "initWithPath:accessPermission:threadingMode:dataProtectionClass:databaseOptions:"
- "initWithProvenance:contentData:metaContentData:"
- "initWithRemoteObjectInterface:exportedInterface:connection:clientId:interruptionCode:invalidationCode:useCase:"
- "initWithRemoteObjectInterface:exportedInterface:serviceName:clientId:interruptionCode:invalidationCode:useCase:"
- "initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:interruptionCode:invalidationCode:useCase:"
- "initWithSetIdentifier:setUUID:resourceDomain:configuredDescriptors:syncPolicy:"
- "initWithSharedIdentifier:instanceIdentifier:content:metaContent:"
- "initWithSharedItem:changeType:"
- "initWithTable:joinCriterion:"
- "initializeDatabaseWithLocalDeviceSite:"
- "insertContent:contentHash:sequenceNumber:onDeviceRowId:"
- "insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:"
- "instance"
- "interruptionCode"
- "intersectsSet:"
- "invalid donate request (%@)"
- "joinTables"
- "joinedProvenanceFromDatabaseValueRow could not initialize provenance record from enumerator: %@"
- "metaContentSequenceNumberEndOfRun"
- "metacontent_sequence_number"
- "metacontent_sequence_number_end_of_run"
- "metacontent_state"
- "minusSet:"
- "modified"
- "nil database"
- "not "
- "performMaintenance:shouldDefer:"
- "prepareWithError:"
- "priorRevisionToken"
- "protocol"
- "provenance"
- "provenanceRowId"
- "provenance_row_id"
- "purgeTombstonedResources:"
- "registerLocalDeviceSite:"
- "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:"
- "remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:"
- "remoteObjectInterface"
- "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:"
- "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
- "removeResource:"
- "removeSourceItemIdentifier:completion:"
- "rowsModified"
- "selectAllDeviceRecords"
- "selectFromTableWithName:columns:count:join:criterion:order:limit:offset:"
- "selectLocalSourceValidityHashInDatabase:error:"
- "selectLocalSourceVersionInDatabase:error:"
- "selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:"
- "selectRowsModifiedCountInDatabase:error:"
- "selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:"
- "servicePriorsRespondingRequest:completion:usingBlock:"
- "serviceRequest:completion:usingBlock:"
- "serviceThrowingRequest:completion:usingBlock:"
- "setFailureCode:"
- "setJoinWithType:tables:"
- "setSharedItemChangeType:"
- "setWriterForSet:accessAssertion:"
- "sharedItemProvenanceUpdatedCount"
- "sourceItemIdHash: %@, provenanceRowId: %@, modified: %@"
- "sourceItemIdentifier not found"
- "submitDatabaseTransactionUsingBlock:"
- "terminateConnection:"
- "timeIntervalSinceReferenceDate"
- "tombstoneContentSequenceNumbersInRange:forDeviceRowId:"
- "uniqueHash"
- "unsignedShortValue"
- "updateContent:andMetaContent:localInstanceRowId:priorProvenanceRowId:contentHash:instanceHash:isDuplicate:"
- "updateMetaContent:localInstanceRowId:provenanceRowId:priorInstanceHash:instanceHash:contentHash:contentSequenceNumber:isDuplicate:"
- "updaterForDatabase:"
- "updaterForDonateRequest:toDatabase:"
- "upsertLastMaintenanceDate:database:error:"
- "upsertRowsModified:database:error:"
- "v24@0:8@\"NSObject<CCDonateService>\"16"
- "v24@?0@\"CCFullSetDonation\"8@\"NSError\"16"
- "v24@?0@\"CCProvenanceRecord\"8^B16"
- "v24@?0@\"CCSetDonation\"8@\"NSError\"16"
- "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?S>16"
- "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?Sq@\"CCDonateServicePriors\">16"
- "v24@?0@\"NSObject<CCMaintenanceServerProtocol>\"8@?<v@?@\"NSError\">16"
- "v24@?0@\"NSObject<CCSetChangeRelayProtocol>\"8@?<v@?S>16"
- "v24@?0@\"NSObject<CCSetStoreAdminServiceServer>\"8@?<v@?S>16"
- "v28@?0S8q12@\"CCDonateServicePriors\"20"
- "v32@0:8@\"NSString\"16@?<v@?S>24"
- "v32@0:8q16@24"
- "v36@0:8B16@?20@?28"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?S>32"
- "v52@0:8@16@24@32@40C48"
- "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?S>52"
- "v80@0:8S16@20Q28@36S44@48@56Q64@?72"
- "{shared_ptr<std::vector<unsigned short>>=\"__ptr_\"^v\"__cntrl_\"^{__shared_weak_count}}"

```
