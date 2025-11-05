## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x4f1ac
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x3d18
-  __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0xee0
-  __TEXT.__cstring: 0x3867
-  __TEXT.__oslogstring: 0x3de1
-  __TEXT.__dlopen_cstrs: 0x2bf
-  __TEXT.__unwind_info: 0x1388
-  __TEXT.__objc_classname: 0xad5
-  __TEXT.__objc_methname: 0x911c
-  __TEXT.__objc_methtype: 0x1cb5
-  __TEXT.__objc_stubs: 0x63a0
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x4e0
-  __DATA_CONST.__objc_classlist: 0x340
+166.17.1.0.0
+  __TEXT.__text: 0x54c48
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x44cc
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0x1130
+  __TEXT.__cstring: 0x39e6
+  __TEXT.__oslogstring: 0x46b5
+  __TEXT.__dlopen_cstrs: 0x278
+  __TEXT.__unwind_info: 0x13d0
+  __TEXT.__objc_classname: 0xac2
+  __TEXT.__objc_methname: 0x9af1
+  __TEXT.__objc_methtype: 0x1da1
+  __TEXT.__objc_stubs: 0x6a80
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x518
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20c8
+  __DATA_CONST.__objc_selrefs: 0x22f0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2c8
-  __AUTH_CONST.__auth_got: 0x3d8
-  __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0xb530
-  __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2080
-  __DATA.__objc_ivar: 0x47c
-  __DATA.__data: 0xa98
-  __DATA.__bss: 0x138
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x38
+  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0x10f0
+  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__objc_const: 0xa9e0
+  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_floatobj: 0x40
+  __AUTH.__objc_data: 0x2030
+  __DATA.__objc_ivar: 0x498
+  __DATA.__data: 0xaf8
+  __DATA.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
+  - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 67D339E0-371B-3FB7-91D0-D91046878737
-  Functions: 1787
-  Symbols:   4412
-  CStrings:  3043
+  UUID: 72D8F3AA-A0C3-350A-86CD-0177A575AA12
+  Functions: 1829
+  Symbols:   4545
+  CStrings:  3188
 
Symbols:
+ +[CCAdminXPCClient performMaintenanceOnAllSets:activity:completion:]
+ +[CCAdminXPCClient removeAllSets:completion:]
+ +[CCDaemon runNightlyMaintenanceActivity:completion:]
+ +[CCDatabaseDeviceMapping _validateSiteIdentifier:outFormat:error:]
+ +[CCDatabaseDeviceMapping decodeAttestationGenerationFromSiteIdentifier:error:]
+ +[CCDatabaseDeviceMapping decodeDeviceUUIDFromSiteIdentifier:error:]
+ +[CCDatabaseDeviceMapping decodeFormatFromSiteIdentifier:error:]
+ +[CCDatabaseDeviceMapping decodeResourceGenerationFromSiteIdentifier:error:]
+ +[CCDatabaseDeviceMapping descriptionForSiteIdentifier:]
+ +[CCDatabaseDeviceMapping dictionaryFromSiteIdentifier:error:]
+ +[CCDatabaseDeviceMapping encodeSiteIdentifierWithFormat:fromDeviceRecord:error:]
+ +[CCDatabaseEnumerationResult emptyResult]
+ +[CCDatabaseSetStateVectorBuilder removeSiteIdentifiers:fromStateVector:]
+ +[CCDatabaseUpdater selectLocalSourceValidityHashInDatabase:error:]
+ +[CCDatabaseUpdater selectLocalSourceVersionInDatabase:error:]
+ +[CCDatabaseUpdater updaterForDatabase:]
+ +[CCDatabaseUpdater updaterForDonateRequest:toDatabase:]
+ +[CCDatabaseUpdater updaterForDonateRequest:toDatabase:].cold.1
+ +[CCDeviceSite deviceSiteForLocalDeviceUUID:resourceGeneration:idsDeviceId:platform:]
+ +[CCDeviceSite deviceSiteFromRecord:]
+ +[CCDeviceSite supportsSecureCoding]
+ +[CCItemMessage contentMessageForItemType:jsonDictionary:error:]
+ +[CCItemMessage metaContentMessageForItemType:jsonDictionary:error:]
+ +[CCSerializedSetEnumerator enumeratorForSerializedSets:]
+ +[CCSerializedSetEnumerator supportsSecureCoding]
+ +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]
+ +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:].cold.1
+ +[CCSetDonation donationWithName:itemType:service:errorCode:priorVersion:]
+ +[CCSetDonation remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:]
+ +[CCSetMetrics _computeMetricsForSet:error:]
+ +[CCSetsAccessDaemonDelegate defaultInstance]
+ +[CCSnapshotUtilities _filenameWithTimestamp:set:format:]
+ +[CCSnapshotUtilities _filenameWithTimestamp:set:format:].cold.1
+ +[CCSnapshotUtilities _filenameWithTimestamp:set:format:].cold.2
+ -[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:].cold.1
+ -[CCDataResourceReadAccess databaseReadAccessForSet:error:]
+ -[CCDataResourceWriteAccess _removeContainerOverriddenResource:]
+ -[CCDataResourceWriteAccess _removeContainerOverriddenResource:].cold.1
+ -[CCDataResourceWriteAccess purgeTombstonedResources:]
+ -[CCDataResourceWriteAccess purgeTombstonedResources:].cold.1
+ -[CCDataResourceWriteAccess requestAccess:forResource:withMode:useCase:error:]
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:]
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.1
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.10
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.2
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.3
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.4
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.5
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.6
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.7
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.8
+ -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceSite:].cold.9
+ -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.5
+ -[CCDataResourceWriter initializeDatabaseWithLocalDeviceSite:]
+ -[CCDatabaseDeviceMapping allActiveDeviceSites]
+ -[CCDatabaseDeviceMapping deviceForDeviceRowId:]
+ -[CCDatabaseDeviceMapping deviceRowIdForDeviceSite:]
+ -[CCDatabaseDeviceMapping initWithDeviceRecords:siteIdentifierFormat:error:]
+ -[CCDatabaseDeviceMapping localDeviceSite]
+ -[CCDatabaseSetChangeEnumerator _contentMessageFromContentData:]
+ -[CCDatabaseSetChangeEnumerator _contentMessageFromContentData:].cold.1
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:]
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.1
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.10
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.11
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.12
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.13
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.14
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.15
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.16
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.17
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.18
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.19
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.2
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.20
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.3
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.4
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.5
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.6
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.7
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.8
+ -[CCDatabaseSetChangeEnumerator _imputeChanges:].cold.9
+ -[CCDatabaseSetChangeEnumerator _lastDeltaDate]
+ -[CCDatabaseSetChangeEnumerator _lastDeltaDate].cold.1
+ -[CCDatabaseSetChangeEnumerator _localResourceGenerationFromDatabaseDeviceMapping]
+ -[CCDatabaseSetChangeEnumerator _localResourceGenerationFromDatabaseDeviceMapping].cold.1
+ -[CCDatabaseSetChangeEnumerator _metaContentMessageFromMetaContentData:]
+ -[CCDatabaseSetChangeEnumerator _metaContentMessageFromMetaContentData:].cold.1
+ -[CCDatabaseSetChangeEnumerator _obtainDatabaseAccess:]
+ -[CCDatabaseSetChangeEnumerator isBookmarkUpToDate:].cold.2
+ -[CCDatabaseSetChangeEnumerator nextBookmark].cold.1
+ -[CCDatabaseSetChangeEnumerator nextBookmark].cold.2
+ -[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]
+ -[CCDatabaseSetStateReader initWithDatabaseAccess:siteIdentifierFormat:]
+ -[CCDatabaseUpdater _deleteDeviceRowId:]
+ -[CCDatabaseUpdater _deleteDeviceRowId:].cold.1
+ -[CCDatabaseUpdater _expireAndTombstoneAllProvenanceForDeviceRowId:]
+ -[CCDatabaseUpdater _expireDeviceRowId:]
+ -[CCDatabaseUpdater _expireDeviceRowId:].cold.1
+ -[CCDatabaseUpdater _expireDeviceRowId:].cold.2
+ -[CCDatabaseUpdater _incrementCachedIntegerWithKey:]
+ -[CCDatabaseUpdater _incrementCachedIntegerWithKey:].cold.1
+ -[CCDatabaseUpdater _insertContent:contentHash:outExists:]
+ -[CCDatabaseUpdater _insertContent:contentHash:outExists:].cold.1
+ -[CCDatabaseUpdater _insertDeviceSite:returningRowId:]
+ -[CCDatabaseUpdater _insertDeviceSite:returningRowId:].cold.1
+ -[CCDatabaseUpdater _persistCachedIntegers]
+ -[CCDatabaseUpdater _persistIntegerWithKey:cachedValue:]
+ -[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:]
+ -[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:].cold.1
+ -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:]
+ -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.1
+ -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.2
+ -[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:].cold.3
+ -[CCDatabaseUpdater _selectLocalDeviceRecord:]
+ -[CCDatabaseUpdater _selectLocalDeviceRecord:].cold.1
+ -[CCDatabaseUpdater _selectLocalInstanceCount:].cold.2
+ -[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]
+ -[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:].cold.1
+ -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:]
+ -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.1
+ -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.2
+ -[CCDatabaseUpdater _tombstoneProvenanceRowsForExpiredDeviceRowId:].cold.3
+ -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:]
+ -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.1
+ -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.2
+ -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.3
+ -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:]
+ -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:].cold.1
+ -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:].cold.2
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:]
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.1
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.2
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.3
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.4
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.5
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.6
+ -[CCDatabaseUpdater compactContiguousRunsOfDeletes:].cold.7
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.1
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.2
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.3
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.4
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.5
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.6
+ -[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:].cold.7
+ -[CCDatabaseUpdater initWithDatabase:request:]
+ -[CCDatabaseUpdater initWithDatabase:request:].cold.1
+ -[CCDatabaseUpdater initWithDatabase:request:].cold.2
+ -[CCDatabaseUpdater initWithDatabase:request:].cold.3
+ -[CCDatabaseUpdater localDeviceRecord]
+ -[CCDatabaseUpdater priorLocalSourceValidityHash]
+ -[CCDatabaseUpdater priorLocalSourceVersion]
+ -[CCDatabaseUpdater registerLocalDeviceSite:]
+ -[CCDatabaseUpdater registerLocalDeviceSite:].cold.1
+ -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:]
+ -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:].cold.1
+ -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:].cold.2
+ -[CCDatabaseUpdater selectAllDeviceRecords]
+ -[CCDatabaseUpdater selectAllDeviceRecords].cold.1
+ -[CCDatabaseUpdater selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:].cold.1
+ -[CCDatabaseUpdater updatedLocalSourceValidityHash]
+ -[CCDatabaseUpdater updatedLocalSourceVersion]
+ -[CCDevice deviceUUID]
+ -[CCDevice dictionaryRepresentation]
+ -[CCDevice idsDeviceIdentifier]
+ -[CCDevice initFromDictionary:]
+ -[CCDevice initWithDeviceUUID:idsDeviceId:platform:options:]
+ -[CCDevice initWithDeviceUUID:idsDeviceId:platform:options:].cold.1
+ -[CCDevice platform]
+ -[CCDeviceRecord attestationGeneration]
+ -[CCDeviceRecord deviceUUID]
+ -[CCDeviceRecord expirationDate]
+ -[CCDeviceRecord idsDeviceId]
+ -[CCDeviceRecord platform]
+ -[CCDeviceRecord recordOptions]
+ -[CCDeviceRecord resourceGeneration]
+ -[CCDeviceSite .cxx_destruct]
+ -[CCDeviceSite copyWithExpirationDate:]
+ -[CCDeviceSite copyWithZone:]
+ -[CCDeviceSite description]
+ -[CCDeviceSite device]
+ -[CCDeviceSite dictionaryRepresentation]
+ -[CCDeviceSite encodeWithCoder:]
+ -[CCDeviceSite expirationDate]
+ -[CCDeviceSite hash]
+ -[CCDeviceSite initFromDictionary:]
+ -[CCDeviceSite initWithCoder:]
+ -[CCDeviceSite initWithDevice:resourceGeneration:expirationDate:]
+ -[CCDeviceSite init]
+ -[CCDeviceSite isEqual:]
+ -[CCDeviceSite isEqualToSetContributor:]
+ -[CCDeviceSite resourceGeneration]
+ -[CCDonateXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
+ -[CCDonateXPCClient mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCMutableSetChange containsChangesAfterDeduplication]
+ -[CCRemoteCRDTSetDonation mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:]
+ -[CCSerializedSet _deduplicateItemsOfType:localInstances:error:]
+ -[CCSerializedSet _placeholderLocalDevice:]
+ -[CCSerializedSetEnumerator encodeWithCoder:]
+ -[CCSerializedSetEnumerator initWithCoder:]
+ -[CCSet copyWithOptions:error:]
+ -[CCSet dictionaryRepresentation]
+ -[CCSet initFromDictionary:]
+ -[CCSet initFromDictionary:].cold.1
+ -[CCSetChangeBookmark initWithContentVector:metaContentVector:localResourceGeneration:lastDeltaDate:set:]
+ -[CCSetChangeBookmark localResourceGeneration]
+ -[CCSetDistribution initWithSet:sharedItemCount:localInstanceCount:]
+ -[CCSetDonation initWithName:itemType:service:errorCode:priorVersion:flushThreshold:]
+ -[CCSetDonation mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCSetsAccessDaemonDelegate _loadOrCreateContainerInfo:readOnly:]
+ -[CCSetsAccessDaemonDelegate _loadOrCreateContainerInfo:readOnly:].cold.1
+ -[CCSetsAccessDaemonDelegate _storedLocalIDSIdentifierInContainer:]
+ -[CCSetsAccessDaemonDelegate _validateCurrentLocalDeviceUUIDsAgainstContainerInfo:container:]
+ -[CCSetsAccessDaemonDelegate _validateCurrentLocalDeviceUUIDsAgainstContainerInfo:container:].cold.1
+ -[CCSetsAccessDaemonDelegate _validateCurrentSchemaAgainstContainerInfo:container:]
+ -[CCSetsAccessDaemonDelegate _validateReadOnlyContainer:]
+ -[CCSetsAccessDaemonDelegate incrementResourceGenerationCounter]
+ -[CCSetsAccessDaemonDelegate incrementResourceGenerationCounter].cold.1
+ -[CCSetsAccessDaemonDelegate initWithBaseSystemPath:notifySourcesOnReset:]
+ -[CCSetsAccessDaemonDelegate loadOrCreateResourceGenerationCounter]
+ -[CCSetsAccessDaemonDelegate loadOrCreateResourceGenerationCounter].cold.1
+ -[CCSetsAccessDaemonDelegate localIDSDeviceId]
+ -[CCSetsAccessDaemonDelegate setsDirectoryInContainer:]
+ CCDateFormattedStringFromTimeMicros.cold.1
+ CCSetLibraryConfigurationRegistryBridge.cold.1
+ CCTypeIdentifierRegistryBridge.cold.1
+ GCC_except_table161
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table44
+ GCC_except_table51
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table76
+ OBJC_IVAR_$_CCDatabaseDeviceMapping._localDeviceSite
+ OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._localResourceGeneration
+ OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._nextRow
+ OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._readAccess
+ OBJC_IVAR_$_CCDatabaseSetStateReader._siteIdentifierFormat
+ OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestAttestationGeneration
+ OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestContentSequenceNumber
+ OBJC_IVAR_$_CCDatabaseUpdater._cachedLocalHighestMetaContentSequenceNumber
+ OBJC_IVAR_$_CCDatabaseUpdater._localDeviceRecord
+ OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceValidityHash
+ OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceVersion
+ OBJC_IVAR_$_CCDatabaseUpdater._updatedLocalSourceValidityHash
+ OBJC_IVAR_$_CCDatabaseUpdater._updatedLocalSourceVersion
+ OBJC_IVAR_$_CCDevice._deviceUUID
+ OBJC_IVAR_$_CCDevice._idsDeviceIdentifier
+ OBJC_IVAR_$_CCDevice._platform
+ OBJC_IVAR_$_CCDeviceRecord._attestationGeneration
+ OBJC_IVAR_$_CCDeviceRecord._deviceUUID
+ OBJC_IVAR_$_CCDeviceRecord._expirationDate
+ OBJC_IVAR_$_CCDeviceRecord._idsDeviceId
+ OBJC_IVAR_$_CCDeviceRecord._platform
+ OBJC_IVAR_$_CCDeviceRecord._recordOptions
+ OBJC_IVAR_$_CCDeviceRecord._resourceGeneration
+ OBJC_IVAR_$_CCDeviceSite._device
+ OBJC_IVAR_$_CCDeviceSite._expirationDate
+ OBJC_IVAR_$_CCDeviceSite._resourceGeneration
+ OBJC_IVAR_$_CCSerializedSetChangeEnumerator._localDevice
+ OBJC_IVAR_$_CCSerializedSetChangeEnumerator._remoteDevices
+ OBJC_IVAR_$_CCSetChangeBookmark._localResourceGeneration
+ OBJC_IVAR_$_CCSetsAccessDaemonDelegate._baseSystemPath
+ OBJC_IVAR_$_CCSetsAccessDaemonDelegate._localDeviceUUID
+ OBJC_IVAR_$_CCSetsAccessDaemonDelegate._notifySourcesOnReset
+ OBJC_IVAR_$_CCSetsAccessDaemonDelegate._resourceGenerationCounter
+ _BMDataFromNSUUID
+ _BMDevicePlatformFromString
+ _BMDevicePlatformToString
+ _BMGetOrCreateDirectoryURL
+ _BMRemoveItemIfExistsAtURL
+ _BMUseCaseMaintenance
+ _CCAdminServiceResultDescription
+ _CCDatabaseColumnAttestationGeneration
+ _CCDatabaseColumnDevicePlatform
+ _CCDatabaseColumnDeviceUUID
+ _CCDatabaseColumnExpirationDate
+ _CCDatabaseColumnIDSDeviceId
+ _CCDatabaseColumnResourceGeneration
+ _CCDatabaseDeviceMappingErrorDomain
+ _CCDatabaseIndexProvenanceContentHashMetaContentState
+ _CCDateAsSecondsFromNow
+ _CCDonateServiceOptionsDescription
+ _CCPersistedKeyValueKeyLocalHighestAttestationGeneration
+ _CCPersistedKeyValueKeyLocalSourceValidityHash
+ _CCPersistedKeyValueKeyLocalSourceVersion
+ _CCSecondsFromNowUntilDate
+ _OBJC_CLASS_$_BMDeviceMetadataUtils
+ _OBJC_CLASS_$_BMFileBackedCounter
+ _OBJC_CLASS_$_BMFileBackedDictionary
+ _OBJC_CLASS_$_BMResourceContainerManager
+ _OBJC_CLASS_$_BMXPCConnectionFactory
+ _OBJC_CLASS_$_CCDeviceSite
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_METACLASS_$_CCDeviceSite
+ __129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke.40
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.12
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.14
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.24
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.28
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.33
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.35
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.35.cold.1
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.29
+ __136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.29.cold.1
+ __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.11
+ __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.11.cold.1
+ __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.9
+ __30-[CCSetChangeXPCNotifier init]_block_invoke.7
+ __30-[CCSetChangeXPCNotifier init]_block_invoke.7.cold.1
+ __33+[CCDaemon registerXPCActivities]_block_invoke.3
+ __44+[CCSetMetrics _computeMetricsForSet:error:]_block_invoke.9
+ __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke.14
+ __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_2.16
+ __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_2.cold.1
+ __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_3.cold.1
+ __47+[CCSerializedSet _serializeSet:useCase:error:]_block_invoke.123
+ __48-[CCDatabaseSetChangeEnumerator _imputeChanges:]_block_invoke.48
+ __48-[CCDatabaseSetChangeEnumerator _imputeChanges:]_block_invoke.52
+ __50-[CCSerializedSetChangeEnumerator _nextWithError:]_block_invoke.70
+ __52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38
+ __52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38.cold.1
+ __52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38.cold.2
+ __52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.cold.1
+ __52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.cold.2
+ __53+[CCDaemon runNightlyMaintenanceActivity:completion:]_block_invoke.cold.1
+ __60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke.28
+ __66-[CCXPCClient requestBiomeEndpointForAppScopedService:user:reply:]_block_invoke.22
+ __71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.45
+ __71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.45.cold.1
+ __71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.cold.1
+ __77-[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]_block_invoke.cold.1
+ __87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.18
+ __87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.21
+ __CCSetLibraryConfigurationRegistryBridge_block_invoke.cold.1
+ __CCTypeIdentifierRegistryBridge_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_CCDatabaseDeviceMapping
+ __OBJC_$_CLASS_METHODS_CCDatabaseEnumerationResult
+ __OBJC_$_CLASS_METHODS_CCDatabaseSetStateVectorBuilder
+ __OBJC_$_CLASS_METHODS_CCDeviceSite
+ __OBJC_$_CLASS_METHODS_CCSerializedSetEnumerator
+ __OBJC_$_CLASS_METHODS_CCSetsAccessDaemonDelegate
+ __OBJC_$_CLASS_PROP_LIST_CCDeviceSite
+ __OBJC_$_CLASS_PROP_LIST_CCSerializedSetEnumerator
+ __OBJC_$_INSTANCE_METHODS_CCDeviceSite
+ __OBJC_$_INSTANCE_VARIABLES_CCDeviceSite
+ __OBJC_$_PROP_LIST_CCDeviceSite
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMOPACKCodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMOPACKCodable
+ __OBJC_CLASS_PROTOCOLS_$_CCDeviceSite
+ __OBJC_CLASS_RO_$_CCDeviceSite
+ __OBJC_LABEL_PROTOCOL_$_BMOPACKCodable
+ __OBJC_METACLASS_RO_$_CCDeviceSite
+ __OBJC_PROTOCOL_$_BMOPACKCodable
+ __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorItNS_9allocatorItEEE7reserveEm
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___111-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:]_block_invoke
+ ___117-[CCDonateXPCClient beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]_block_invoke
+ ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke
+ ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2
+ ___43-[CCDatabaseUpdater selectAllDeviceRecords]_block_invoke
+ ___44+[CCSetMetrics _computeMetricsForSet:error:]_block_invoke
+ ___45+[CCAdminXPCClient removeAllSets:completion:]_block_invoke
+ ___46-[CCDatabaseUpdater _selectLocalDeviceRecord:]_block_invoke
+ ___48-[CCDatabaseSetChangeEnumerator _imputeChanges:]_block_invoke
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke
+ ___53+[CCDaemon runNightlyMaintenanceActivity:completion:]_block_invoke
+ ___62-[CCDataResourceWriter initializeDatabaseWithLocalDeviceSite:]_block_invoke
+ ___68+[CCAdminXPCClient performMaintenanceOnAllSets:activity:completion:]_block_invoke
+ ___68-[CCSetDonation mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
+ ___71-[CCDatabaseUpdater _selectLatestDeviceRecordWithDeviceUUID:outRecord:]_block_invoke
+ ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke
+ ___75-[CCDatabaseUpdater _selectDeviceRecords:withOptions:beyondExpirationDate:]_block_invoke
+ ___77-[CCDatabaseUpdater _selectRemoteContentHashPresent:remoteContentPresentPtr:]_block_invoke
+ ___83-[CCDonateXPCClient mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
+ ___90+[CCSetDonation remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48r56r64r72r80r88r96r_e21_B16?0"CCSetChange"8l
+ ___block_descriptor_40_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_e8_32r_e30_v40?0{_NSRange=QQ}8C24C28^B32l
+ ___block_descriptor_40_e8_32r_e40_v24?0"BPSCompletion"8"<BMBookmark>"16l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e44_B32?0"NSObject<CCDatabaseRecord>"8^16^B24l
+ ___block_descriptor_40_e8_32s_e50_v24?0"NSObject<CCAdminServiceServer>"8?<v?S>16l
+ ___block_descriptor_40_ea8_32r_e21_B16?0"CCSetChange"8l
+ ___block_descriptor_48_e8_32bs40r_e49_B24?0"NSObject<CCDatabaseReadWriteAccess>"8^Q16l
+ ___block_descriptor_48_ea8_32r40r_e40_v24?0"BPSCompletion"8"<BMBookmark>"16l
+ ___block_descriptor_56_e8_32s40s48r_e36_B32?0"CCDatabaseValueRow"8^16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16l
+ ___block_descriptor_66_e8_32s40s_e47_v24?0"NSObject<CCDonateService>"8?<v?SqQ>16l
+ ___block_descriptor_74_e8_32s40s48s56bs64r_e14_v28?0S8q12Q20l
+ ___block_descriptor_82_e8_32s40s48s56r64r72r_e8_v16?0q8l
+ ___block_descriptor_84_e8_32s40s48bs56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r56r64r72r80r88r96r
+ ___copy_helper_block_ea8_32r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r96r
+ ___destroy_helper_block_ea8_32r
+ __block_literal_global.170
+ __block_literal_global.31
+ __decodeDevice
+ __encodeDescriptors
+ __encodeDevice
+ __missingRecordPropertyError
+ __resolveItemMessageSubclass
+ __unsupportedFormatError
+ _decodeDevice.cold.1
+ _notify_post
+ _objc_msgSend$_computeMetricsForSet:error:
+ _objc_msgSend$_contentMessageFromContentData:
+ _objc_msgSend$_createDatabaseIfNotExistsWithLocalDeviceSite:
+ _objc_msgSend$_deduplicateItemsOfType:localInstances:error:
+ _objc_msgSend$_deleteDeviceRowId:
+ _objc_msgSend$_expireAndTombstoneAllProvenanceForDeviceRowId:
+ _objc_msgSend$_expireDeviceRowId:
+ _objc_msgSend$_filenameWithTimestamp:set:format:
+ _objc_msgSend$_imputeChanges:
+ _objc_msgSend$_incrementCachedIntegerWithKey:
+ _objc_msgSend$_insertContent:contentHash:outExists:
+ _objc_msgSend$_insertDeviceSite:returningRowId:
+ _objc_msgSend$_lastDeltaDate
+ _objc_msgSend$_loadOrCreateContainerInfo:readOnly:
+ _objc_msgSend$_localResourceGenerationFromDatabaseDeviceMapping
+ _objc_msgSend$_metaContentMessageFromMetaContentData:
+ _objc_msgSend$_obtainDatabaseAccess:
+ _objc_msgSend$_persistCachedIntegers
+ _objc_msgSend$_persistIntegerWithKey:cachedValue:
+ _objc_msgSend$_placeholderLocalDevice:
+ _objc_msgSend$_removeContainerOverriddenResource:
+ _objc_msgSend$_selectDeviceRecords:withOptions:beyondExpirationDate:
+ _objc_msgSend$_selectLatestDeviceRecordWithDeviceUUID:outRecord:
+ _objc_msgSend$_selectLocalDeviceRecord:
+ _objc_msgSend$_selectRemoteContentHashPresent:remoteContentPresentPtr:
+ _objc_msgSend$_setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:
+ _objc_msgSend$_storedLocalIDSIdentifierInContainer:
+ _objc_msgSend$_tombstoneProvenanceRowsForExpiredDeviceRowId:
+ _objc_msgSend$_updateDeviceRowId:expirationDate:
+ _objc_msgSend$_updateLocalSourceVersion:localSourceValidityHash:
+ _objc_msgSend$_validateCurrentLocalDeviceUUIDsAgainstContainerInfo:container:
+ _objc_msgSend$_validateCurrentSchemaAgainstContainerInfo:container:
+ _objc_msgSend$_validateReadOnlyContainer:
+ _objc_msgSend$_validateSiteIdentifier:outFormat:error:
+ _objc_msgSend$addClockValuesInIndexSet:forSiteIdentifier:
+ _objc_msgSend$allSetsResourceSpecifierWithOptions:
+ _objc_msgSend$allValues
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$attestationGeneration
+ _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:
+ _objc_msgSend$biomeDirectoryForDomain:
+ _objc_msgSend$clockValuesForSiteIdentifier:
+ _objc_msgSend$compactContiguousRunsOfDeletes:
+ _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:
+ _objc_msgSend$containsChangesAfterDeduplication
+ _objc_msgSend$copyWithExpirationDate:
+ _objc_msgSend$criterionWithColumnName:NOTEQUALSColumnValue:
+ _objc_msgSend$databaseReadAccessForSet:error:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decodeAttestationGenerationFromSiteIdentifier:error:
+ _objc_msgSend$decodeDeviceUUIDFromSiteIdentifier:error:
+ _objc_msgSend$decodeFormatFromSiteIdentifier:error:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$decodeResourceGenerationFromSiteIdentifier:error:
+ _objc_msgSend$deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord
+ _objc_msgSend$deleteExpiredRemoteDeviceState:shouldTombstoneSet:
+ _objc_msgSend$descriptionForSiteIdentifier:
+ _objc_msgSend$device
+ _objc_msgSend$deviceForDeviceRowId:
+ _objc_msgSend$deviceSiteForLocalDeviceUUID:resourceGeneration:idsDeviceId:platform:
+ _objc_msgSend$deviceSiteFromRecord:
+ _objc_msgSend$deviceUUID
+ _objc_msgSend$dictionaryFromSiteIdentifier:error:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$donationWithName:itemType:service:errorCode:priorVersion:
+ _objc_msgSend$drivableSinkWithBookmark:completion:shouldContinue:
+ _objc_msgSend$emptyResult
+ _objc_msgSend$encodeSiteIdentifierWithFormat:fromDeviceRecord:error:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$fileUUID
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$idsDeviceId
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$incrementCount:error:
+ _objc_msgSend$incrementResourceGenerationCounter
+ _objc_msgSend$initFromDictionary:
+ _objc_msgSend$initWithBaseSystemPath:notifySourcesOnReset:
+ _objc_msgSend$initWithContentVector:metaContentVector:localResourceGeneration:lastDeltaDate:set:
+ _objc_msgSend$initWithDatabase:request:
+ _objc_msgSend$initWithDatabaseAccess:siteIdentifierFormat:
+ _objc_msgSend$initWithDevice:resourceGeneration:expirationDate:
+ _objc_msgSend$initWithDeviceRecords:siteIdentifierFormat:error:
+ _objc_msgSend$initWithDeviceUUID:idsDeviceId:platform:options:
+ _objc_msgSend$initWithDeviceUUID:idsDeviceIdentifier:platformString:options:error:
+ _objc_msgSend$initWithFilename:protectionClass:directory:domain:error:
+ _objc_msgSend$initWithFilename:protectionClass:directory:readOnly:create:initialDictionary:error:
+ _objc_msgSend$initWithItemType:setIdentifier:personaIdentifier:descriptors:sharedItemCount:localItemInstanceCount:localDevice:remoteDevices:items:options:error:
+ _objc_msgSend$initWithItemType:sharedIdentifier:localInstanceIdentifiers:content:localMetaContent:remoteDeviceIndices:error:
+ _objc_msgSend$initWithName:itemType:service:errorCode:priorVersion:flushThreshold:
+ _objc_msgSend$initWithObjects:forKeys:
+ _objc_msgSend$initWithSet:sharedItemCount:localInstanceCount:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initializeDatabaseWithLocalDeviceSite:
+ _objc_msgSend$intersectsOrderedSet:
+ _objc_msgSend$isEqualToSetContributor:
+ _objc_msgSend$isRemoteSync
+ _objc_msgSend$loadOrCreateResourceGenerationCounter
+ _objc_msgSend$localDevice
+ _objc_msgSend$localDeviceSite
+ _objc_msgSend$localIDSDeviceId
+ _objc_msgSend$localInstanceIdentifiers
+ _objc_msgSend$localMetaContent
+ _objc_msgSend$localResourceGeneration
+ _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:
+ _objc_msgSend$minusOrderedSet:
+ _objc_msgSend$minusVector:
+ _objc_msgSend$modifiedRowCount
+ _objc_msgSend$openContainerForResource:mode:error:
+ _objc_msgSend$performMaintenanceOnAllSets:activity:completion:
+ _objc_msgSend$performMaintenanceOnAllSets:completion:
+ _objc_msgSend$platform
+ _objc_msgSend$platformString
+ _objc_msgSend$recordOptions
+ _objc_msgSend$registerLocalDeviceSite:
+ _objc_msgSend$remoteDeviceIndices
+ _objc_msgSend$remoteDevices
+ _objc_msgSend$removeAllSets:completion:
+ _objc_msgSend$removeSiteIdentifiers:fromStateVector:
+ _objc_msgSend$resourceGeneration
+ _objc_msgSend$runNightlyMaintenanceActivity:completion:
+ _objc_msgSend$selectLocalSourceValidityHashInDatabase:error:
+ _objc_msgSend$selectLocalSourceVersionInDatabase:error:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setIdentifier
+ _objc_msgSend$setLimit:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sourceValidity
+ _objc_msgSend$sourceVersion
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$updaterForDatabase:
+ _sharedQueue.cold.1
+ _sharedXPCClientFactory.cold.1
- +[CCAdminXPCClient removeSetsRootDirectory:]
- +[CCAdminXPCClient triggerMaintenanceActivity:completion:]
- +[CCDataResourceWriter purgeTombstonedResources:]
- +[CCDataResourceWriter purgeTombstonedResources:].cold.1
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.1
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.2
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.3
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.4
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.5
- +[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:].cold.6
- +[CCDatabaseUpdater insertOrUpdateLocalDeviceIdentifier:database:]
- +[CCDatabaseUpdater insertResourceVersion:database:]
- +[CCDatabaseUpdater selectLocalHighestContentSequenceNumberInDatabase:error:]
- +[CCDatabaseUpdater selectLocalHighestMetaContentSequenceNumberInDatabase:error:]
- +[CCDatabaseUpdater selectSetValidityHashInDatabase:error:]
- +[CCDatabaseUpdater selectSetVersionInDatabase:error:]
- +[CCReplicatedEntityEnumeratorBookmark currentVersion]
- +[CCReplicatedEntityEnumeratorBookmark supportsSecureCoding]
- +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]
- +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:].cold.1
- +[CCSetDonation donationWithName:itemType:service:payload:]
- +[CCSetDonation remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:]
- +[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]
- +[CCSnapshotUtilities _filenameFromDate:set:format:]
- +[CCSnapshotUtilities _filenameFromDate:set:format:].cold.1
- +[CCSnapshotUtilities _filenameFromDate:set:format:].cold.2
- -[CCDataResourceReadAccess databaseReadAccessForSet:]
- -[CCDataResourceReadAccess databaseReadAccessForSet:].cold.1
- -[CCDataResourceReadAccess databaseReadAccessForSet:].cold.2
- -[CCDataResourceReadAccess localDeviceIdForSet:]
- -[CCDataResourceReadAccess localDeviceIdForSet:].cold.1
- -[CCDataResourceWriteAccess requestAccess:forResource:withMode:error:]
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:]
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.1
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.10
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.11
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.12
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.2
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.3
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.4
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.5
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.6
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.7
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.8
- -[CCDataResourceWriter _createDatabaseIfNotExistsWithLocalDeviceIdentifier:].cold.9
- -[CCDataResourceWriter initializeDatabaseWithLocalDeviceIdentifier:error:]
- -[CCDatabaseDeviceMapping initWithDeviceRecords:]
- -[CCDatabaseSetChangeEnumerator _cachedDeviceWithRowId:]
- -[CCDatabaseSetChangeEnumerator beginWithBookmark:error:].cold.1
- -[CCDatabaseSetChangeEnumerator contentMessageFromContentData:]
- -[CCDatabaseSetChangeEnumerator contentMessageFromContentData:].cold.1
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:]
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.1
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.10
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.11
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.12
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.13
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.14
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.15
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.16
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.17
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.18
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.19
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.2
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.3
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.4
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.5
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.6
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.7
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.8
- -[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:].cold.9
- -[CCDatabaseSetChangeEnumerator initWithSet:readAccess:].cold.1
- -[CCDatabaseSetChangeEnumerator initWithSet:readAccess:].cold.2
- -[CCDatabaseSetChangeEnumerator lastDeltaDate]
- -[CCDatabaseSetChangeEnumerator lastDeltaDate].cold.1
- -[CCDatabaseSetChangeEnumerator metaContentMessageFromMetaContentData:]
- -[CCDatabaseSetChangeEnumerator metaContentMessageFromMetaContentData:].cold.1
- -[CCDatabaseSetChangeEnumerator resourceVersion]
- -[CCDatabaseSetChangeEnumerator resourceVersion].cold.1
- -[CCDatabaseSetStateReader constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:]
- -[CCDatabaseSetStateReader initWithDatabaseAccess:]
- -[CCDatabaseSetStateReader initWithDatabaseAccess:].cold.1
- -[CCDatabaseSetStateReader localDeviceIdentifier:]
- -[CCDatabaseSetStateReader resourceVersion:]
- -[CCDatabaseUpdater _incrementLocalHighestContentSequenceNumber]
- -[CCDatabaseUpdater _incrementLocalHighestContentSequenceNumber].cold.1
- -[CCDatabaseUpdater _incrementLocalHighestContentSequenceNumber].cold.2
- -[CCDatabaseUpdater _incrementLocalHighestMetaContentSequenceNumber]
- -[CCDatabaseUpdater _incrementLocalHighestMetaContentSequenceNumber].cold.1
- -[CCDatabaseUpdater _incrementLocalHighestMetaContentSequenceNumber].cold.2
- -[CCDatabaseUpdater _insertContentIfNotExists:contentHash:]
- -[CCDatabaseUpdater _insertContentIfNotExists:contentHash:].cold.1
- -[CCDatabaseUpdater _insertContentIfNotExists:contentHash:].cold.2
- -[CCDatabaseUpdater _insertDeviceReturningRowId:]
- -[CCDatabaseUpdater _registerDevice]
- -[CCDatabaseUpdater _registerDevice].cold.1
- -[CCDatabaseUpdater _registerSetVersionAndValidity]
- -[CCDatabaseUpdater _registerSetVersionAndValidity].cold.1
- -[CCDatabaseUpdater _registerSetVersionAndValidity].cold.2
- -[CCDatabaseUpdater _selectDeviceRowId:options:]
- -[CCDatabaseUpdater _selectDeviceRowId:options:].cold.1
- -[CCDatabaseUpdater _updateLocalHighestSequenceNumbers]
- -[CCDatabaseUpdater _updateLocalHighestSequenceNumbers].cold.1
- -[CCDatabaseUpdater _updateLocalHighestSequenceNumbers].cold.2
- -[CCDatabaseUpdater _updateSetVersionAndValidity]
- -[CCDatabaseUpdater _updateSetVersionAndValidity].cold.1
- -[CCDatabaseUpdater _updateSetVersionAndValidity].cold.2
- -[CCDatabaseUpdater deviceRowId]
- -[CCDatabaseUpdater initWithDatabase:device:request:startTimeMicros:]
- -[CCDatabaseUpdater initWithDatabase:device:request:startTimeMicros:].cold.1
- -[CCDatabaseUpdater initWithDatabase:device:request:startTimeMicros:].cold.2
- -[CCDatabaseUpdater initWithDatabase:device:request:startTimeMicros:].cold.3
- -[CCDatabaseUpdater initWithDatabase:device:request:startTimeMicros:].cold.4
- -[CCDatabaseUpdater priorValidityHash]
- -[CCDatabaseUpdater priorVersion]
- -[CCDatabaseUpdater setHash]
- -[CCDatabaseUpdater updateValidityHash]
- -[CCDatabaseUpdater updateVersion]
- -[CCDevice initWithIdentifier:options:]
- -[CCDeviceRecord deviceId]
- -[CCDeviceRecord options]
- -[CCDictionaryLog .cxx_destruct]
- -[CCDictionaryLog _loadLogOrCreate:readOnly:error:]
- -[CCDictionaryLog _loadLogOrCreate:readOnly:error:].cold.1
- -[CCDictionaryLog _loadLogOrCreate:readOnly:error:].cold.2
- -[CCDictionaryLog _loadLogOrCreate:readOnly:error:].cold.3
- -[CCDictionaryLog _loadLogOrCreate:readOnly:error:].cold.4
- -[CCDictionaryLog allKeys]
- -[CCDictionaryLog clear:]
- -[CCDictionaryLog clear:].cold.1
- -[CCDictionaryLog clearObjectForKey:error:]
- -[CCDictionaryLog clearObjectForKey:error:].cold.1
- -[CCDictionaryLog clearObjectForKey:error:].cold.2
- -[CCDictionaryLog clearObjectForKey:error:].cold.3
- -[CCDictionaryLog count]
- -[CCDictionaryLog description]
- -[CCDictionaryLog hash]
- -[CCDictionaryLog initWithFilename:directory:readOnly:error:]
- -[CCDictionaryLog initWithFilename:protectionClass:directory:readOnly:create:error:]
- -[CCDictionaryLog init]
- -[CCDictionaryLog isEqual:]
- -[CCDictionaryLog isEqualToDictionaryLog:]
- -[CCDictionaryLog isReadOnly]
- -[CCDictionaryLog mutableDictionaryForKey:error:]
- -[CCDictionaryLog mutableDictionaryForKey:error:].cold.1
- -[CCDictionaryLog objectForKey:]
- -[CCDictionaryLog writeUpdatedObject:forKey:error:]
- -[CCDictionaryLog writeUpdatedObjects:forKeys:error:]
- -[CCDictionaryLog writeUpdatedObjects:forKeys:error:].cold.1
- -[CCDonateXPCClient beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:]
- -[CCDonateXPCClient mergeDelta:completion:]
- -[CCIncrementalSetDonation priorVersion]
- -[CCMutableSetChange containsChanges]
- -[CCRemoteCRDTSetDonation mergeDelta:]
- -[CCReplicatedEntityEnumeratorBookmark .cxx_destruct]
- -[CCReplicatedEntityEnumeratorBookmark contentVector]
- -[CCReplicatedEntityEnumeratorBookmark encodeWithCoder:]
- -[CCReplicatedEntityEnumeratorBookmark initWithCoder:]
- -[CCReplicatedEntityEnumeratorBookmark initWithContentVector:metaContentVector:]
- -[CCReplicatedEntityEnumeratorBookmark initWithContentVector:metaContentVector:version:]
- -[CCReplicatedEntityEnumeratorBookmark init]
- -[CCReplicatedEntityEnumeratorBookmark isEqual:]
- -[CCReplicatedEntityEnumeratorBookmark metaContentVector]
- -[CCReplicatedEntityEnumeratorBookmark version]
- -[CCSerializedSet _deduplicateItemsOfType:localInstances:deviceIndexes:error:]
- -[CCSetChangeBookmark initWithContentVector:metaContentVector:resourceVersion:lastDeltaDate:set:]
- -[CCSetChangeBookmark resourceVersion]
- -[CCSetDistribution initWithSet:]
- -[CCSetDonation _mergeDelta:]
- -[CCSetDonation initWithName:itemType:service:payload:flushThreshold:]
- -[CCSetsAccessDaemonDelegate _loadOrCreateContainerInfo:]
- -[CCSetsAccessDaemonDelegate _loadOrCreateContainerInfo:].cold.1
- -[CCSetsAccessDaemonDelegate init]
- -[CCXPCClient serviceArrayRespondingRequestWithCompletion:usingBlock:]
- -[CCXPCClient serviceOptionsRespondingRequest:completion:usingBlock:]
- CCWritePropertyList.cold.1
- GCC_except_table11
- GCC_except_table24
- GCC_except_table28
- GCC_except_table34
- GCC_except_table37
- GCC_except_table40
- GCC_except_table41
- GCC_except_table42
- GCC_except_table45
- GCC_except_table46
- OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._currentMutableSetChange
- OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._deviceCache
- OBJC_IVAR_$_CCDatabaseSetChangeEnumerator._resourceVersion
- OBJC_IVAR_$_CCDatabaseUpdater._deviceId
- OBJC_IVAR_$_CCDatabaseUpdater._deviceOptions
- OBJC_IVAR_$_CCDatabaseUpdater._deviceRowId
- OBJC_IVAR_$_CCDatabaseUpdater._encodedDescriptors
- OBJC_IVAR_$_CCDatabaseUpdater._itemTypeNumber
- OBJC_IVAR_$_CCDatabaseUpdater._localHighestContentSequenceNumber
- OBJC_IVAR_$_CCDatabaseUpdater._localHighestMetaContentSequenceNumber
- OBJC_IVAR_$_CCDatabaseUpdater._priorValidityHash
- OBJC_IVAR_$_CCDatabaseUpdater._priorVersion
- OBJC_IVAR_$_CCDatabaseUpdater._setHash
- OBJC_IVAR_$_CCDatabaseUpdater._updateValidityHash
- OBJC_IVAR_$_CCDatabaseUpdater._updateVersion
- OBJC_IVAR_$_CCDatabaseUpdater._versionNumber
- OBJC_IVAR_$_CCDeviceRecord._deviceId
- OBJC_IVAR_$_CCDeviceRecord._options
- OBJC_IVAR_$_CCDictionaryLog._log
- OBJC_IVAR_$_CCDictionaryLog._logFileURL
- OBJC_IVAR_$_CCDictionaryLog._protectionClass
- OBJC_IVAR_$_CCReplicatedEntityEnumeratorBookmark._contentVector
- OBJC_IVAR_$_CCReplicatedEntityEnumeratorBookmark._metaContentVector
- OBJC_IVAR_$_CCReplicatedEntityEnumeratorBookmark._version
- OBJC_IVAR_$_CCSetChangeBookmark._resourceVersion
- OBJC_IVAR_$_CCSetsAccessDaemonDelegate._localDeviceId
- _BMSetsResource
- _CCDatabaseColumnDeviceId
- _CCDictionaryLogErrorDomain
- _CCGetOrCreateDirectoryPath
- _CCGetOrCreateDirectoryURL
- _CCPersistedKeyValueKeyLocalDeviceIdentifier
- _CCPersistedKeyValueKeyResourceVersion
- _CCPersistedKeyValueKeySourceValidityHash
- _CCPersistedKeyValueKeySourceVersion
- _CCReadPropertyList
- _CCRemoveItemIfExistsAtPath
- _CCRemoveItemIfExistsAtURL
- _CCReplicatedEntityEnumeratorBookmarkCurrentVersion
- _CCWritePropertyList
- _OBJC_CLASS_$_BMAccessConnectionFactory
- _OBJC_CLASS_$_CCDictionaryLog
- _OBJC_CLASS_$_CCReplicatedEntityEnumeratorBookmark
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSFileHandle
- _OBJC_CLASS_$_NSPropertyListSerialization
- _OBJC_METACLASS_$_CCDictionaryLog
- _OBJC_METACLASS_$_CCReplicatedEntityEnumeratorBookmark
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- __129-[CCDatabaseSetStateReader _resolveSequenceNumberRangesOfDeltaVector:appendToCriteria:seenStateVectorBuilder:deviceMapping:type:]_block_invoke.34
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.12
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.14
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.24
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.28
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.33
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.35
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.35.cold.1
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.29
- __141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.29.cold.1
- __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.5
- __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.7
- __149-[CCDatabaseSetStateReader enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:]_block_invoke.7.cold.1
- __30-[CCSetChangeXPCNotifier init]_block_invoke.3
- __30-[CCSetChangeXPCNotifier init]_block_invoke.3.cold.1
- __33+[CCDaemon registerXPCActivities]_block_invoke.5
- __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke.7
- __46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_2.9
- __47+[CCSerializedSet _serializeSet:useCase:error:]_block_invoke.109
- __48-[CCDatabaseUpdater _selectDeviceRowId:options:]_block_invoke.cold.1
- __56+[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]_block_invoke.9
- __60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke.30
- __66-[CCXPCClient requestBiomeEndpointForAppScopedService:user:reply:]_block_invoke.24
- __87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke.32
- __87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke.32.cold.1
- __87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke.32.cold.2
- __87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke.cold.1
- __87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke.cold.2
- __87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.12
- __87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.15
- __97-[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:]_block_invoke.33
- __OBJC_$_CLASS_METHODS_CCReplicatedEntityEnumeratorBookmark
- __OBJC_$_CLASS_PROP_LIST_CCReplicatedEntityEnumeratorBookmark
- __OBJC_$_INSTANCE_METHODS_CCDictionaryLog
- __OBJC_$_INSTANCE_METHODS_CCReplicatedEntityEnumeratorBookmark
- __OBJC_$_INSTANCE_VARIABLES_CCDictionaryLog
- __OBJC_$_INSTANCE_VARIABLES_CCReplicatedEntityEnumeratorBookmark
- __OBJC_$_PROP_LIST_CCReplicatedEntityEnumeratorBookmark
- __OBJC_CLASS_PROTOCOLS_$_CCReplicatedEntityEnumeratorBookmark
- __OBJC_CLASS_RO_$_CCDictionaryLog
- __OBJC_CLASS_RO_$_CCReplicatedEntityEnumeratorBookmark
- __OBJC_METACLASS_RO_$_CCDictionaryLog
- __OBJC_METACLASS_RO_$_CCReplicatedEntityEnumeratorBookmark
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___110-[CCDatabaseSetStateReader constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:]_block_invoke
- ___110-[CCDonateXPCClient beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:]_block_invoke
- ___112+[CCSetDonation remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:]_block_invoke
- ___131-[CCXPCClient initWithRemoteObjectXPCInterface:exportedXPCInterface:connection:clientId:interruptionCode:invalidationCode:useCase:]_block_invoke
- ___141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke
- ___141+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2
- ___29-[CCSetDonation _mergeDelta:]_block_invoke
- ___43-[CCDonateXPCClient mergeDelta:completion:]_block_invoke
- ___44+[CCAdminXPCClient removeSetsRootDirectory:]_block_invoke
- ___48-[CCDatabaseUpdater _selectDeviceRowId:options:]_block_invoke
- ___56+[CCSetMetrics _computeMetricsForSet:shouldDefer:error:]_block_invoke
- ___58+[CCAdminXPCClient triggerMaintenanceActivity:completion:]_block_invoke
- ___69-[CCXPCClient serviceOptionsRespondingRequest:completion:usingBlock:]_block_invoke
- ___70-[CCXPCClient serviceArrayRespondingRequestWithCompletion:usingBlock:]_block_invoke
- ___74-[CCDataResourceWriter initializeDatabaseWithLocalDeviceIdentifier:error:]_block_invoke
- ___87+[CCDatabaseUpdater compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:]_block_invoke
- ___97-[CCDatabaseSetChangeEnumerator imputeChangesSinceLastContentVector:lastMetaContentVector:error:]_block_invoke
- ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_32_e50_v24?0"NSObject<CCAdminServiceServer>"8?<v?S>16l
- ___block_descriptor_40_e8_32bs_e49_B24?0"NSObject<CCDatabaseReadWriteAccess>"8^Q16l
- ___block_descriptor_40_e8_32r_e23_v16?0"BPSCompletion"8l
- ___block_descriptor_40_e8_32w_e5_v8?0l
- ___block_descriptor_48_ea8_32bs40r_e21_B16?0"CCSetChange"8l
- ___block_descriptor_48_ea8_32r40r_e23_v16?0"BPSCompletion"8l
- ___block_descriptor_56_e8_32s40r48r_e36_B32?0"CCDatabaseValueRow"8^16^B24l
- ___block_descriptor_66_e8_32s40s48s_e46_v24?0"NSObject<CCDonateService>"8?<v?SQ>16l
- ___block_descriptor_74_e8_32s40s48s56bs64r_e11_v20?0S8Q12l
- ___block_descriptor_76_e8_32s40s48bs56r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e21_v16?0"CCSetChange"8l
- ___copy_helper_block_ea8_32b40r
- ___destroy_helper_block_ea8_32s40r
- ___getCCSerializedSetItemInstanceClass_block_invoke
- ___getCCSerializedSetSharedItemClass_block_invoke
- __block_literal_global.17
- __block_literal_global.173
- __block_literal_global.4
- __block_literal_global.8
- __getCCSerializedSetItemInstanceClass_block_invoke.cold.1
- __getCCSerializedSetSharedItemClass_block_invoke.cold.1
- _getCCSerializedSetDescriptorClass
- _getCCSerializedSetItemInstanceClass
- _getCCSerializedSetSharedItemClass
- _objc_msgSend$URLByDeletingLastPathComponent
- _objc_msgSend$_cachedDeviceWithRowId:
- _objc_msgSend$_computeMetricsForSet:shouldDefer:error:
- _objc_msgSend$_createDatabaseIfNotExistsWithLocalDeviceIdentifier:
- _objc_msgSend$_deduplicateItemsOfType:localInstances:deviceIndexes:error:
- _objc_msgSend$_filenameFromDate:set:format:
- _objc_msgSend$_incrementLocalHighestContentSequenceNumber
- _objc_msgSend$_incrementLocalHighestMetaContentSequenceNumber
- _objc_msgSend$_insertContentIfNotExists:contentHash:
- _objc_msgSend$_insertDeviceReturningRowId:
- _objc_msgSend$_loadLogOrCreate:readOnly:error:
- _objc_msgSend$_loadOrCreateContainerInfo:
- _objc_msgSend$_mergeDelta:
- _objc_msgSend$_registerDevice
- _objc_msgSend$_registerSetVersionAndValidity
- _objc_msgSend$_selectDeviceRowId:options:
- _objc_msgSend$_setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:
- _objc_msgSend$_updateLocalHighestSequenceNumbers
- _objc_msgSend$_updateSetVersionAndValidity
- _objc_msgSend$beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:
- _objc_msgSend$compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:
- _objc_msgSend$constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:
- _objc_msgSend$containsChanges
- _objc_msgSend$contentMessageFromContentData:
- _objc_msgSend$currentVersion
- _objc_msgSend$dataWithContentsOfURL:options:error:
- _objc_msgSend$dataWithPropertyList:format:options:error:
- _objc_msgSend$databaseReadAccessForSet:
- _objc_msgSend$deviceId
- _objc_msgSend$deviceIdentifier
- _objc_msgSend$deviceIndexes
- _objc_msgSend$deviceRecordForDeviceRowId:
- _objc_msgSend$devices
- _objc_msgSend$donationWithName:itemType:service:payload:
- _objc_msgSend$fileURLWithPath:relativeToURL:
- _objc_msgSend$imputeChangesSinceLastContentVector:lastMetaContentVector:error:
- _objc_msgSend$initWithContent:sharedIdentifier:error:
- _objc_msgSend$initWithContentVector:metaContentVector:resourceVersion:lastDeltaDate:set:
- _objc_msgSend$initWithContentVector:metaContentVector:version:
- _objc_msgSend$initWithDatabaseAccess:
- _objc_msgSend$initWithDeviceIdentifier:options:error:
- _objc_msgSend$initWithDeviceRecords:
- _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
- _objc_msgSend$initWithFilename:protectionClass:directory:readOnly:create:error:
- _objc_msgSend$initWithIdentifier:options:
- _objc_msgSend$initWithItemType:personaIdentifier:descriptors:sharedItemCount:localItemInstanceCount:devices:items:options:error:
- _objc_msgSend$initWithMetaContent:instanceIdentifier:error:
- _objc_msgSend$initWithName:itemType:service:payload:flushThreshold:
- _objc_msgSend$initWithSet:
- _objc_msgSend$initWithSharedItem:deviceIndexes:localInstances:error:
- _objc_msgSend$initializeDatabaseWithLocalDeviceIdentifier:error:
- _objc_msgSend$insertOrUpdateLocalDeviceIdentifier:database:
- _objc_msgSend$insertResourceVersion:database:
- _objc_msgSend$isEqualToDictionaryLog:
- _objc_msgSend$isReadOnly
- _objc_msgSend$legacySetsRootDirectoryURL
- _objc_msgSend$localDeviceIdentifier:
- _objc_msgSend$localInstances
- _objc_msgSend$mergeDelta:completion:
- _objc_msgSend$metaContentMessageFromMetaContentData:
- _objc_msgSend$propertyListWithData:options:format:error:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$removeSetsRootDirectory:
- _objc_msgSend$resourceVersion
- _objc_msgSend$resourceVersion:
- _objc_msgSend$selectLocalHighestContentSequenceNumberInDatabase:error:
- _objc_msgSend$selectLocalHighestMetaContentSequenceNumberInDatabase:error:
- _objc_msgSend$selectSetValidityHashInDatabase:error:
- _objc_msgSend$selectSetVersionInDatabase:error:
- _objc_msgSend$sinkWithCompletion:receiveInput:
- _objc_msgSend$sinkWithCompletion:shouldContinue:
- _objc_msgSend$startMaintenanceActivity:
- _objc_msgSend$triggerMaintenanceActivity:completion:
- _objc_msgSend$validity
- _objc_msgSend$version
- _objc_msgSend$writeData:error:
- _open_dprotected_np
- getCCSerializedSetItemInstanceClass.softClass
- getCCSerializedSetSharedItemClass.softClass
CStrings:
+ " as persona: %@"
+ " device: %@ resourceGeneration: %@%@"
+ " deviceRowId: %@, deviceId: %@ idsDeviceId: %@ platform: %@ recordOptions %X, resourceGeneration: %@, attestationGeneration: %@, expiration: %@"
+ " expirationDate: %@"
+ "%@ Failed to increment resource generation counter: %@"
+ "%@ Ignoring nil IDS identifier"
+ "%@ Local IDS device identifier %@ is not equal to stored %@ in container: %@"
+ "%@ Local device identifier %@ is not equal to stored: %@ in container: %@"
+ "%@ Will complete enumeration without error due to invalid database state"
+ "%@ failed access database"
+ "%@ failed to construct device mapping"
+ "%@ failed to load resourceGeneration counter %@"
+ "%@ maintenance at container: %@ %@"
+ "%@ nightly maintenance"
+ "%@ resourceGeneration counter loaded with deviceUUID: %@"
+ "%@ startTimeMicros: %@"
+ "%s expected method override: %@"
+ "%s nil deviceUUID"
+ "(%@) Failed to complete data resource-specific maintenance"
+ "(%@) Failed to select persisted key: %@ with error: %@"
+ "(%@) Key not cached: %@"
+ "(%@) Maintenance failed to tombstone set: %@"
+ "(%@) Persisted value for key: %@ is: %@"
+ "(%@) Tombstoning set after maintenance removed all remaining state"
+ "-[CCDataResourceWriteAccess _removeContainerOverriddenResource:]"
+ "-[CCDevice initWithDeviceUUID:idsDeviceId:platform:options:]"
+ ":[%@]"
+ "<%@> identifier: %@ idsIdentifier: %@ isLocal: %@ platform: %@"
+ "@\"BMFileBackedCounter\""
+ "@\"BMFileBackedDictionary\""
+ "@\"CCDatabaseJoinedProvenance\""
+ "@\"CCDevice\""
+ "@\"CCDeviceRecord\""
+ "@\"CCDeviceSite\""
+ "@\"NSDate\""
+ "@24@0:8@\"NSDictionary\"16"
+ "@28@0:8C16^@20"
+ "@36@0:8@16C24^@28"
+ "@36@0:8C16@20^@28"
+ "@40@0:8@16Q24Q32"
+ "@44@0:8@16@24q32C40"
+ "@52@0:8@16S24@28q36Q44"
+ "@56@0:8^@16@24Q32@40^@48"
+ "@60@0:8@16S24@28q36Q44Q52"
+ "Aborted"
+ "All conditions met for set tombstone eligibility. %@"
+ "B32@0:8@16^B24"
+ "B32@0:8@?16^B24"
+ "B36@0:8@16B24^@28"
+ "B36@0:8^@16C24@28"
+ "B40@0:8@16@24@32"
+ "B40@0:8@16@24^B32"
+ "B40@0:8@16^C24^@32"
+ "B48@0:8@16^@24^@32^@40"
+ "BMOPACKCodable"
+ "Bookmark for Cascade Set: %@ resourceGeneration: %lld lastDelta: %@ <bv:%u> sharedItemCount: %lu localItemInstanceCount: %lu"
+ "C32@0:8@16^@24"
+ "CCDatabaseDeviceMapping.m"
+ "CCDeviceSite"
+ "CREATE INDEX \"%@\" ON \"%@\" (\"%@\",\"%@\",\"%@\",\"%@\");"
+ "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer PRIMARY KEY, \"%@\" blob NOT NULL, \"%@\" varchar NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE);"
+ "Cannot decode site identifier missing data: %@"
+ "Cannot re-register local device record: %@ with site: %@. %@"
+ "Cannot register local device with invalid device site: %@"
+ "Cannot update device row id: %@ with nil expiration date. %@"
+ "Client provided state vector contains present content for site: %@ which has already expired and been cleaned up: %@"
+ "Completed"
+ "Could not create database, failed to register local device site"
+ "Could not prepare resource: %@"
+ "Could not update key: %@ with cached value: %@. %@"
+ "Current schema (expected: %@) not initialized yet (found: %@) in container: %@"
+ "Database initializer -"
+ "Database resource generation (%lld) invalidates the provided bookmark (%lld): %@"
+ "Deferred uncompleted"
+ "Delete failed: %@"
+ "Deleting any content records no longer referenced by provenance"
+ "Deleting device record: %@"
+ "Device identifier UUID is nil: %@. %@"
+ "Device record (%@) missing required property: %@"
+ "Device record enumeration failed: %@ %@"
+ "Device table contains nonzero remote device records - not eligible for tombstone"
+ "Error"
+ "Expiring device record: %@"
+ "Expiring device record: %@ and associated state which is now invalid due to registration of device site %@. %@"
+ "Extending expiration date from %@ to %@ due to re-attestation of device site %@. %@"
+ "Failed to access database for bookmark: %@ error: %@"
+ "Failed to asssume default persona for maintenace %@"
+ "Failed to assume persona %@ for set change event from set %@ with error %@, not invoking batch block"
+ "Failed to assume persona %@ for set change event from set %@ with error %@, not invoking client block"
+ "Failed to complete client activity (serviceResult: %@): %@"
+ "Failed to construct device mapping: %@"
+ "Failed to decode serialized set device: %@"
+ "Failed to initialize CCSet from OPACK with error %@"
+ "Failed to resolve container for legacySetsRootDirectoryURL: %@"
+ "Failed to select local source version for tombstone eligibility: %@"
+ "Failed to write container info: %@"
+ "Finished database tombstone compaction operation with deleted count: %@"
+ "Finished running activity \"com.apple.cascade.database-maintenance\""
+ "Found %u active remote device records past their expiration date %@"
+ "Found %u expired remote device records past the tombstone preservation interval %@"
+ "Found expired site: %@ eligible for cleanup from the client provided state vector"
+ "Ignoring re-attested expiration date of device site %@ which occurs sooner than the stored device record (%@). %@"
+ "Inserting device record due to re-attestation of device site %@. %@"
+ "Inserting first record of device site %@. %@"
+ "Inserting latest record of device site %@. %@"
+ "Interrupted"
+ "Invalid site identifier length (%u) expected %u for format %u"
+ "Invalidated"
+ "LocalBookmark"
+ "Not an attestation - inheriting expiration date from prior device record (%@) for device site: %@. %@"
+ "Posted notification \"%s\""
+ "Provenance table contains nonzero records - not eligible for tombstone"
+ "Provided NSNumber %@ for float field %@ is outside of -FLT_MAX"
+ "Provided NSNumber %@ for float field %@ is outside of -FLT_MIN"
+ "Provided NSNumber %@ for float field %@ is outside of FLT_MAX"
+ "Provided NSNumber %@ for float field %@ is outside of FLT_MIN"
+ "Remote device site: %@ already expired (compared to: %@). %@"
+ "RemoteCRDT"
+ "RemoteSync"
+ "Resolved TTL seconds: %@ from expiration date: %@ during OPACK encoding for device site: %@"
+ "Resolved entitled set identifiers to enumerate data resources on disk %@"
+ "Resolved expiration date: %@ from TTL seconds: %@ during OPACK decoding for device site: %@"
+ "Returning nil bookmark after enumerator error: %@"
+ "Running activity \"com.apple.cascade.database-maintenance\""
+ "Running default maintenance%@"
+ "Select %@ returned invalid row: %@, %@"
+ "Select (%@) returned an unexpected number of local device records: %@. %@"
+ "Sets directory (%@) initialized with schema version: %@ localDeviceId: %@ idsDeviceId: %@"
+ "Skipping access request to remove resource: %@ with container override: %@"
+ "Skipping registration - stored resource generation %@ in the databse is more recent than device site %@. %@"
+ "Skipping unattested registration of new device site %@. %@"
+ "Starting nightly maintenance"
+ "T@\"CCDevice\",R,N,V_device"
+ "T@\"CCDeviceRecord\",R,N,V_localDeviceRecord"
+ "T@\"NSDate\",R,N,V_expirationDate"
+ "T@\"NSNumber\",R,N,V_attestationGeneration"
+ "T@\"NSNumber\",R,N,V_priorLocalInstanceCount"
+ "T@\"NSNumber\",R,N,V_priorLocalSourceValidityHash"
+ "T@\"NSNumber\",R,N,V_priorLocalSourceVersion"
+ "T@\"NSNumber\",R,N,V_resourceGeneration"
+ "T@\"NSNumber\",R,N,V_updatedLocalSourceValidityHash"
+ "T@\"NSNumber\",R,N,V_updatedLocalSourceVersion"
+ "T@\"NSString\",R,N,V_idsDeviceId"
+ "T@\"NSString\",R,N,V_idsDeviceIdentifier"
+ "T@\"NSUUID\",R,N,V_deviceUUID"
+ "TC,R,N,V_recordOptions"
+ "Timeout"
+ "TombstoneSet"
+ "Tq,R,N,V_localResourceGeneration"
+ "Tq,R,N,V_platform"
+ "Unexpected - count not produced from select: %@"
+ "Unexpected - local resource version not found in device mapping: %@"
+ "Unexpected remote device site: %@ has isLocal flag set. %@"
+ "Unexpected remote device site: %@ missing expiration date for attestation. %@"
+ "Unknown (%u)"
+ "Unsupported site identifier format: %u"
+ "Vv32@0:8@\"BMResourceSpecifier\"16@?<v@?S>24"
+ "Vv32@0:8@16@?24"
+ "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?SqQ>52"
+ "Vv60@0:8S16@20Q28@36Q44@?52"
+ "_[%@]"
+ "_attestationGeneration"
+ "_baseSystemPath"
+ "_cachedLocalHighestAttestationGeneration"
+ "_cachedLocalHighestContentSequenceNumber"
+ "_cachedLocalHighestMetaContentSequenceNumber"
+ "_computeMetricsForSet:error:"
+ "_contentMessageFromContentData:"
+ "_createDatabaseIfNotExistsWithLocalDeviceSite:"
+ "_deduplicateItemsOfType:localInstances:error:"
+ "_deleteDeviceRowId:"
+ "_device"
+ "_deviceUUID"
+ "_expirationDate"
+ "_expireAndTombstoneAllProvenanceForDeviceRowId:"
+ "_expireDeviceRowId:"
+ "_filenameWithTimestamp:set:format:"
+ "_idsDeviceId"
+ "_idsDeviceIdentifier"
+ "_imputeChanges:"
+ "_incrementCachedIntegerWithKey:"
+ "_insertContent:contentHash:outExists:"
+ "_insertDeviceSite:returningRowId:"
+ "_loadOrCreateContainerInfo:readOnly:"
+ "_localDevice"
+ "_localDeviceRecord"
+ "_localDeviceSite"
+ "_localDeviceUUID"
+ "_localResourceGeneration"
+ "_localResourceGenerationFromDatabaseDeviceMapping"
+ "_metaContentMessageFromMetaContentData:"
+ "_nextRow"
+ "_notifySourcesOnReset"
+ "_obtainDatabaseAccess:"
+ "_persistCachedIntegers"
+ "_persistIntegerWithKey:cachedValue:"
+ "_placeholderLocalDevice:"
+ "_platform"
+ "_priorLocalSourceValidityHash"
+ "_priorLocalSourceVersion"
+ "_recordOptions"
+ "_remoteDevices"
+ "_removeContainerOverriddenResource:"
+ "_resourceGeneration"
+ "_resourceGenerationCounter"
+ "_selectDeviceRecords:withOptions:beyondExpirationDate:"
+ "_selectLatestDeviceRecordWithDeviceUUID:outRecord:"
+ "_selectLocalDeviceRecord:"
+ "_selectRemoteContentHashPresent:remoteContentPresentPtr:"
+ "_setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:"
+ "_siteIdentifierFormat"
+ "_storedLocalIDSIdentifierInContainer:"
+ "_tombstoneProvenanceRowsForExpiredDeviceRowId:"
+ "_updateDeviceRowId:expirationDate:"
+ "_updateLocalSourceVersion:localSourceValidityHash:"
+ "_updatedLocalSourceValidityHash"
+ "_updatedLocalSourceVersion"
+ "_validateCurrentLocalDeviceUUIDsAgainstContainerInfo:container:"
+ "_validateCurrentSchemaAgainstContainerInfo:container:"
+ "_validateReadOnlyContainer:"
+ "_validateSiteIdentifier:outFormat:error:"
+ "addClockValuesInIndexSet:forSiteIdentifier:"
+ "allActiveDeviceSites"
+ "allSetsResourceSpecifierWithOptions:"
+ "allValues"
+ "arrayWithArray:"
+ "attestationGeneration"
+ "attestationVersion"
+ "attestation_generation"
+ "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:"
+ "biomeDirectoryForDomain:"
+ "clockValuesForSiteIdentifier:"
+ "com.apple.CascadeSets.CCDatabaseDeviceMapping"
+ "com.apple.CascadeSets.DonateNow"
+ "compactContiguousRunsOfDeletes:"
+ "constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:"
+ "containsChangesAfterDeduplication"
+ "contentMessageForItemType:jsonDictionary:error:"
+ "copyWithExpirationDate:"
+ "copyWithOptions:error:"
+ "databaseReadAccessForSet:error:"
+ "dateWithTimeIntervalSinceNow:"
+ "decodeAttestationGenerationFromSiteIdentifier:error:"
+ "decodeDeviceUUIDFromSiteIdentifier:error:"
+ "decodeFormatFromSiteIdentifier:error:"
+ "decodeObjectOfClasses:forKey:"
+ "decodeResourceGenerationFromSiteIdentifier:error:"
+ "deleteExpiredRemoteDeviceState:shouldTombstoneSet:"
+ "descriptionForSiteIdentifier:"
+ "deviceForDeviceRowId:"
+ "devicePlatform"
+ "deviceRowIdForDeviceSite:"
+ "deviceSiteForLocalDeviceUUID:resourceGeneration:idsDeviceId:platform:"
+ "deviceSiteFromRecord:"
+ "deviceUUID"
+ "device_platform"
+ "device_uuid"
+ "dictionaryFromSiteIdentifier:error:"
+ "dictionaryRepresentation"
+ "donationWithName:itemType:service:errorCode:priorVersion:"
+ "drivableSinkWithBookmark:completion:shouldContinue:"
+ "emptyResult"
+ "encodeSiteIdentifierWithFormat:fromDeviceRecord:error:"
+ "enumeratorForSerializedSets:"
+ "expirationDate"
+ "expiration_date"
+ "fileUUID"
+ "format"
+ "getBytes:length:"
+ "idsDeviceId"
+ "idsDeviceIdentifier"
+ "ids_device_id"
+ "idx_provenance_content_hash_metacontent_state"
+ "incrementCount:error:"
+ "incrementResourceGenerationCounter"
+ "initFromDictionary:"
+ "initWithBaseSystemPath:notifySourcesOnReset:"
+ "initWithContentVector:metaContentVector:localResourceGeneration:lastDeltaDate:set:"
+ "initWithDatabase:request:"
+ "initWithDatabaseAccess:siteIdentifierFormat:"
+ "initWithDevice:resourceGeneration:expirationDate:"
+ "initWithDeviceRecords:siteIdentifierFormat:error:"
+ "initWithDeviceUUID:idsDeviceId:platform:options:"
+ "initWithDeviceUUID:idsDeviceIdentifier:platformString:options:error:"
+ "initWithFilename:protectionClass:directory:domain:error:"
+ "initWithFilename:protectionClass:directory:readOnly:create:initialDictionary:error:"
+ "initWithItemType:setIdentifier:personaIdentifier:descriptors:sharedItemCount:localItemInstanceCount:localDevice:remoteDevices:items:options:error:"
+ "initWithItemType:sharedIdentifier:localInstanceIdentifiers:content:localMetaContent:remoteDeviceIndices:error:"
+ "initWithName:itemType:service:errorCode:priorVersion:flushThreshold:"
+ "initWithObjects:forKeys:"
+ "initWithSet:sharedItemCount:localInstanceCount:"
+ "initWithUUIDBytes:"
+ "initializeDatabaseWithLocalDeviceSite:"
+ "intersectsOrderedSet:"
+ "invalid donate request (%@)"
+ "isEqualToSetContributor:"
+ "isRemoteSync"
+ "loadOrCreateResourceGenerationCounter"
+ "localDevice"
+ "localDeviceRecord"
+ "localDeviceSite"
+ "localDeviceUUID"
+ "localHighestAttestationGeneration"
+ "localIDSDeviceId"
+ "localInstanceIdentifiers"
+ "localMetaContent"
+ "localResourceGeneration"
+ "localSourceValidityHash"
+ "localSourceVersion"
+ "mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:"
+ "metaContentMessageForItemType:jsonDictionary:error:"
+ "minusOrderedSet:"
+ "minusVector:"
+ "openContainerForResource:mode:error:"
+ "performMaintenanceOnAllSets:activity:completion:"
+ "performMaintenanceOnAllSets:completion:"
+ "platform"
+ "platformString"
+ "priorLocalSourceValidityHash"
+ "priorLocalSourceVersion"
+ "provenance enumerator was not initialized, returning nil bookmark"
+ "recordOptions"
+ "registerLocalDeviceSite:"
+ "registerRemoteDeviceSite:isAttestation:returningRowId:"
+ "remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:"
+ "remoteDeviceIndices"
+ "remoteDevices"
+ "removeAllSets"
+ "removeAllSets:completion:"
+ "removeSiteIdentifiers:fromStateVector:"
+ "requestAccess:forResource:withMode:useCase:error:"
+ "resourceGeneration"
+ "resource_generation"
+ "runNightlyMaintenanceActivity:completion:"
+ "selectAllDeviceRecords"
+ "selectLocalSourceValidityHashInDatabase:error:"
+ "selectLocalSourceVersionInDatabase:error:"
+ "setDateFormat:"
+ "setWithObjects:"
+ "sourceValidity"
+ "timeIntervalSinceNow"
+ "timeToLiveSeconds"
+ "updatedLocalSourceValidityHash"
+ "updatedLocalSourceVersion"
+ "updaterForDatabase:"
+ "updaterForDonateRequest:toDatabase:"
+ "v24@?0@\"BPSCompletion\"8@\"<BMBookmark>\"16"
+ "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?SqQ>16"
+ "v28@?0S8q12Q20"
+ "v48@0:8@\"CKMergeableDelta\"16@\"CCDeviceSite\"24@\"NSArray\"32@?<v@?S>40"
+ "v48@0:8@16@24@32@?40"
+ "v92@0:8S16@20@28Q36@44Q52@60@68Q76@?84"
+ "yyyy.MM.dd_hh-mm-ss.SSSZZZ"
- "\nt"
- " deviceRowId: %@, deviceId: %@ options %X"
- " logFile: %@"
- "%@"
- "%@local deviceId: %@ not yet registered. Inserting new device record. %@"
- "(%@) Failed to perform data resource-specific maintenance"
- "(%@) Local highest content sequence number: %@"
- "(%@) Local highest metacontent sequence number: %@"
- ":remote=%@"
- "<%@> identifier: %@ isLocal: %@"
- "@\"CCDictionaryLog\""
- "@\"CCMutableSetChange\""
- "@\"NSDictionary\""
- "@40@0:8@16@24Q32"
- "@40@0:8@16@?24^@32"
- "@44@0:8@16@24B32^@36"
- "@44@0:8@16S24@28Q36"
- "@48@0:8^@16@24Q32^@40"
- "@52@0:8@16S24@28Q36Q44"
- "@52@0:8@16i24@28B36B40^@44"
- "B32@0:8B16B20^@24"
- "B32@0:8^@16^C24"
- "B40@0:8@16^Q24@?32"
- "B48@0:8^@16^@24^@32^@40"
- "Bookmark for Cascade Set: %@ created: %@ lastDelta: %@ <bv:%u> sharedItemCount: %lu localItemInstanceCount: %lu"
- "CCDatabaseSetStateReader.m"
- "CCDictionaryLog"
- "CCReplicatedEntityEnumeratorBookmark"
- "CCReplicatedEntityEnumeratorBookmark.m"
- "CCSerializedSetItemInstance"
- "CCSerializedSetSharedItem"
- "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer PRIMARY KEY, \"%@\" varchar NOT NULL, \"%@\" integer);"
- "Class getCCSerializedSetItemInstanceClass(void)_block_invoke"
- "Class getCCSerializedSetSharedItemClass(void)_block_invoke"
- "Could not create database, failed to insert local device identifier"
- "Could not create database, failed to insert resource version"
- "Could not create database, missing local device identifier"
- "Could not determine a valid resource version for the current set - returning no results from enumeration"
- "Could not prepare resource: %@ error: %@"
- "Could not update local highest content sequence number - update failed. %@"
- "Could not update local highest metacontent sequence number - update failed. %@"
- "Current schema (expected: %@) not initialized yet (found: %@) container: %@"
- "Database resource version (%lld) invalidates the provided bookmark (%lld): %@"
- "Deleted %u tombstone(s) from the database."
- "Expected mutable plist class (%@) but received class (%@) for object: %@ at path: %@"
- "Failed to complete client activity (serviceResult: %u): %@"
- "Failed to count modified rows after insert %@ error: %@"
- "Failed to obtain database read access."
- "Failed to read prior log file at path: %@ error: %@"
- "Failed to record schema version and localDeviceId: %@"
- "Failed to remove log file at path: %@"
- "Failed to resolve localDeviceIdentifier for set: %@ error: %@"
- "Failed to resolve resource for set: %@ in container: %@"
- "Failed to retrieve database access."
- "Failed to select local highest content sequence number with error: %@"
- "Failed to select local highest metacontent sequence number with error: %@"
- "Failed to write removal for key: %@ reverting to prior object: %@"
- "Failed to write updated object(s): %@ for key(s): %@ reverting to prior object(s): %@"
- "Finished database tombstone compaction operation with deleted count: %u"
- "Initializing empty log file at path: %@"
- "Invalid item URL: %@"
- "Invalid key: %@"
- "Invalid path: \"%@\""
- "Invalid {filename: %@, directory: %@}"
- "Invalid {object: %@ key: %@}"
- "Maintenance for all resources finished with status: %@, error: %@"
- "No object exists for key: %@"
- "No prior log found at path: %@"
- "Non-"
- "Parent directory: %@ does not exist (isDirectory: %i)"
- "Provided NSNumber %@ for double field %@ is greater than DBL_MAX"
- "Provided NSNumber %@ for double field %@ is less than DBL_MIN"
- "Provided NSNumber %@ for float field %@ is greater than FLT_MAX"
- "Provided NSNumber %@ for float field %@ is less than FLT_MIN"
- "Removed object: %@ for key: %@"
- "Row %@ for deviceId: %@ has device options value %i inconsistent with expected: %i"
- "Select device row returned invalid row: %@, %@"
- "Sets directory (%@) initialized with schema version: %@ localDeviceId: %@"
- "State reader creation failed."
- "T@\"NSNumber\",R,N,V_priorValidityHash"
- "T@\"NSNumber\",R,N,V_setHash"
- "T@\"NSNumber\",R,N,V_updateValidityHash"
- "T@\"NSString\",R,N,V_deviceId"
- "TI,R,N,V_priorLocalInstanceCount"
- "TQ,R,N,V_updateVersion"
- "TQ,R,N,V_version"
- "Tq,R,N,V_resourceVersion"
- "URLByDeletingLastPathComponent"
- "Unexpected number of objects: %@ for keys: %@"
- "Unexpected object: %@ for key: %@ expected: %@"
- "Unexpected plist class (%@) of object: %@ at path: %@"
- "Updated object(s): %@ for key(s): %@ replacing prior object(s): %@"
- "Vv24@0:8@?<v@?S>16"
- "Vv60@0:8S16@\"CCDevice\"20@\"NSString\"28Q36@\"NSString\"44@?<v@?SQ>52"
- "Vv60@0:8S16@20@28Q36@44@?52"
- "XPC connection %@ for client %@ interrupted"
- "_<%@>"
- "_cachedDeviceWithRowId:"
- "_computeMetricsForSet:shouldDefer:error:"
- "_createDatabaseIfNotExistsWithLocalDeviceIdentifier:"
- "_currentMutableSetChange"
- "_deduplicateItemsOfType:localInstances:deviceIndexes:error:"
- "_deviceCache"
- "_deviceId"
- "_deviceOptions"
- "_filenameFromDate:set:format:"
- "_incrementLocalHighestContentSequenceNumber"
- "_incrementLocalHighestMetaContentSequenceNumber"
- "_insertContentIfNotExists:contentHash:"
- "_insertDeviceReturningRowId:"
- "_itemTypeNumber"
- "_loadLogOrCreate:readOnly:error:"
- "_loadOrCreateContainerInfo:"
- "_localDeviceId"
- "_localHighestContentSequenceNumber"
- "_localHighestMetaContentSequenceNumber"
- "_logFileURL"
- "_mergeDelta:"
- "_priorValidityHash"
- "_protectionClass"
- "_registerDevice"
- "_registerSetVersionAndValidity"
- "_resourceVersion"
- "_selectDeviceRowId:options:"
- "_setDonationWithItemType:forAccount:descriptors:remoteDevice:version:validity:serviceProvider:queue:timeoutNanos:completion:"
- "_setHash"
- "_updateLocalHighestSequenceNumbers"
- "_updateSetVersionAndValidity"
- "_updateValidityHash"
- "_updateVersion"
- "_version"
- "_versionNumber"
- "aborted"
- "beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:"
- "com.apple.CascadeSets.DictionaryLog"
- "compactContiguousRunsOfDeletesInDatabase:deletedCount:shouldDefer:"
- "constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:"
- "containsChanges"
- "contentMessageFromContentData:"
- "currentVersion"
- "dataWithContentsOfURL:options:error:"
- "dataWithPropertyList:format:options:error:"
- "databaseReadAccessForSet:"
- "deviceId"
- "deviceIdentifier"
- "deviceIndexes"
- "device_id"
- "devices"
- "donationWithName:itemType:service:payload:"
- "failed to read resource version for set: %@ error: %@"
- "fileURLWithPath:relativeToURL:"
- "finished running activity \"com.apple.cascade.database-maintenance\""
- "imputeChangesSinceLastContentVector:lastMetaContentVector:error:"
- "initWithContent:sharedIdentifier:error:"
- "initWithContentVector:metaContentVector:"
- "initWithContentVector:metaContentVector:resourceVersion:lastDeltaDate:set:"
- "initWithContentVector:metaContentVector:version:"
- "initWithDatabase:device:request:startTimeMicros:"
- "initWithDatabaseAccess:"
- "initWithDeviceIdentifier:options:error:"
- "initWithDeviceRecords:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithFilename:directory:readOnly:error:"
- "initWithFilename:protectionClass:directory:readOnly:create:error:"
- "initWithIdentifier:options:"
- "initWithItemType:personaIdentifier:descriptors:sharedItemCount:localItemInstanceCount:devices:items:options:error:"
- "initWithMetaContent:instanceIdentifier:error:"
- "initWithName:itemType:service:payload:flushThreshold:"
- "initWithSet:"
- "initWithSharedItem:deviceIndexes:localInstances:error:"
- "initializeDatabaseWithLocalDeviceIdentifier:error:"
- "insertOrUpdateLocalDeviceIdentifier:database:"
- "insertResourceVersion:database:"
- "instance: %@ is read only."
- "isEqualToDictionaryLog:"
- "isReadOnly"
- "legacySetsRootDirectoryURL"
- "local-device-placeholder"
- "localDeviceId"
- "localDeviceIdForSet:"
- "localDeviceIdentifier"
- "localDeviceIdentifier:"
- "localInstances"
- "mergeDelta:"
- "mergeDelta:completion:"
- "metaContentMessageFromMetaContentData:"
- "mutableDictionaryForKey:error:"
- "nil deviceId"
- "nil encodedDescriptors"
- "nil request"
- "object: %@ is already recorded for key: %@"
- "priorValidityHash"
- "propertyListWithData:options:format:error:"
- "remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:"
- "removeObjectForKey:"
- "removeSetsRootDirectory"
- "removeSetsRootDirectory:"
- "request: %@, startTimeMicros: %@"
- "requestAccess:forResource:withMode:error:"
- "resetRootDirectoryIfNecessary failed to resolve legacy root directory"
- "resourceVersion"
- "resourceVersion:"
- "running activity \"com.apple.cascade.database-maintenance\""
- "selectLocalHighestContentSequenceNumberInDatabase:error:"
- "selectLocalHighestMetaContentSequenceNumberInDatabase:error:"
- "selectSetValidityHashInDatabase:error:"
- "selectSetVersionInDatabase:error:"
- "serviceArrayRespondingRequestWithCompletion:usingBlock:"
- "serviceOptionsRespondingRequest:completion:usingBlock:"
- "setHash"
- "sinkWithCompletion:receiveInput:"
- "sinkWithCompletion:shouldContinue:"
- "sourceValidityHash"
- "startMaintenanceActivity:"
- "triggerMaintenanceActivity:completion:"
- "updateValidityHash"
- "updateVersion"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@\"CCSetChange\"8"
- "v20@?0S8Q12"
- "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?SQ>16"
- "v32@0:8@\"CKMergeableDelta\"16@?<v@?S>24"
- "v32@0:8@?16@?24"
- "v60@0:8S16@20@28@36@44@?52"
- "v92@0:8S16@20@28@36Q44@52@60@68Q76@?84"
- "validity"
- "version"
- "writeData:error:"
- "writeUpdatedObject:forKey:error:"

```
