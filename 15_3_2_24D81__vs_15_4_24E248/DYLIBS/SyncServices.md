## SyncServices

> `/System/Library/Frameworks/SyncServices.framework/Versions/A/SyncServices`

```diff

 733.0.0.0.0
-  __TEXT.__text: 0xb67b4
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xa490
-  __TEXT.__const: 0x1ac
-  __TEXT.__gcc_except_tab: 0x32b0
-  __TEXT.__cstring: 0x22e3d
+  __TEXT.__text: 0xb91a4
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0xacb8
+  __TEXT.__const: 0x19c
+  __TEXT.__gcc_except_tab: 0x3298
+  __TEXT.__cstring: 0x22e3a
   __TEXT.__oslogstring: 0x157
-  __TEXT.__unwind_info: 0x3348
+  __TEXT.__unwind_info: 0x3370
   __TEXT.__objc_classname: 0xc56
   __TEXT.__objc_methname: 0x18ed5
   __TEXT.__objc_methtype: 0x28ba
   __TEXT.__objc_stubs: 0x12be0
   __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x12c0
+  __DATA_CONST.__const: 0x12c8
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58e0
+  __DATA_CONST.__objc_selrefs: 0x59f8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x280
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x538
   __AUTH_CONST.__cfstring: 0x152c0
-  __AUTH_CONST.__objc_const: 0xe5b8
+  __AUTH_CONST.__objc_const: 0xd668
   __AUTH.__objc_data: 0x1ef0
   __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0x6a9

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 65B9DA2F-D5A7-3FAC-8921-2DC3E8D32376
-  Functions: 3709
-  Symbols:   9054
-  CStrings:  10173
+  UUID: 63DEBDB1-61A4-3028-B9C5-606A33F5D5AD
+  Functions: 3953
+  Symbols:   9358
+  CStrings:  10172
 
Symbols:
+ +[ISDRecordIdMapper legacyGlobalIdFromConstructedLocalId:].cold.1
+ +[ISDStructuredDelta applyRecordDictionary:toRecord:forClient:generation:entity:syncState:takeUnformattedRelationshipsFromRecord:saveUnformattedValues:ignoredProperties:].cold.1
+ +[ISDStructuredDelta applyRecordDictionary:toRecord:forClient:generation:entity:syncState:takeUnformattedRelationshipsFromRecord:saveUnformattedValues:ignoredProperties:].cold.2
+ +[ISDStructuredDelta applyRecordDictionary:toRecord:forClient:generation:entity:syncState:takeUnformattedRelationshipsFromRecord:saveUnformattedValues:ignoredProperties:].cold.3
+ +[ISDStructuredDelta applyRecordDictionary:toRecord:forClient:generation:entity:syncState:takeUnformattedRelationshipsFromRecord:saveUnformattedValues:ignoredProperties:].cold.4
+ +[ISDStructuredDelta applyRecordDictionary:toRecord:forClient:generation:entity:syncState:takeUnformattedRelationshipsFromRecord:saveUnformattedValues:ignoredProperties:].cold.5
+ +[ISyncManager setDataReferencesDirectory:].cold.1
+ +[ISyncManager setSyncServerName:dataDirectoryPath:].cold.1
+ +[ISyncSession _sessionWithClient:entityNames:beforeDate:clientHasTruthForEntityNames:quietlyPushTruth:target:selector:anchors:hasChanges:skip:error:].cold.1
+ +[NSArray(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSCalendarDate(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSColor(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSData(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSDate(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSDecimalNumber(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSDictionary(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSMachPort portForTrivialMessages].cold.1
+ +[NSNull(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSString(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ +[NSURL(SyncServicesSqliteExtensions) isd_propertyValueWithType:bytesEncodedForSqlite:].cold.1
+ -[ISDChange encodeWithCoder:].cold.1
+ -[ISDChange encodeWithCoder:].cold.2
+ -[ISDChange initWithChangeType:entityName:recordId:propertyChanges:clientId:fromGeneration:toGeneration:index:].cold.1
+ -[ISDChange initWithChangeType:entityName:recordId:propertyChanges:clientId:fromGeneration:toGeneration:index:].cold.2
+ -[ISDChange initWithCoder:].cold.1
+ -[ISDChange initWithCoder:].cold.2
+ -[ISDChangeBuilder initWithClientId:recordId:entity:propertyNamesSynchronizedByClient:lastModifiedGeneration:currentGeneration:clientIsTrusted:clientState:].cold.1
+ -[ISDChangeBuilder initWithClientId:recordId:entity:propertyNamesSynchronizedByClient:lastModifiedGeneration:currentGeneration:clientIsTrusted:clientState:].cold.2
+ -[ISDChangeBuilder initWithClientId:recordId:entity:propertyNamesSynchronizedByClient:lastModifiedGeneration:currentGeneration:clientIsTrusted:clientState:].cold.3
+ -[ISDChangeBuilder isOldValue:equalToNewValue:propertyDescription:].cold.1
+ -[ISDChangeBuilder shouldCreateDeltaForProperty:].cold.1
+ -[ISDChangeBuilder validateValue:forPropertyDescription:].cold.1
+ -[ISDChangePuller changeBuilder:didCreateDelta:betweenOldValue:newValue:].cold.1
+ -[ISDChangePuller changeBuilder:didCreateDelta:betweenOldValue:newValue:].cold.2
+ -[ISDChangeStore appendChange:].cold.1
+ -[ISDChangeStore appendChange:].cold.2
+ -[ISDChangeStore initWithPath:].cold.1
+ -[ISDClient encodeWithCoder:].cold.1
+ -[ISDClient initWithCoder:].cold.1
+ -[ISDClient morphInToObject:].cold.1
+ -[ISDClient morphInToObject:].cold.2
+ -[ISDClient morphInToObject:].cold.3
+ -[ISDConflict encodeWithCoder:].cold.1
+ -[ISDConflict initWithCoder:].cold.1
+ -[ISDDataClass encodeWithCoder:].cold.1
+ -[ISDDataClass initWithCoder:].cold.1
+ -[ISDDataClass morphInToObject:].cold.1
+ -[ISDDataClass morphInToObject:].cold.2
+ -[ISDDataClass morphInToObject:].cold.3
+ -[ISDDataDatabase enumerateRecordIdsForRecordsWithMatchingAttributes:asArgumentsToFunction:context:matchAll:].cold.1
+ -[ISDDataManager _dataClassNameFromStubEntity:].cold.1
+ -[ISDDataManager _ensureDataDirectoryExistsForClientWithId:].cold.1
+ -[ISDDataManager _getDataClassesDeleted:dataClassesAdded:inParsedSchemas:].cold.1
+ -[ISDDataManager _getEntityComponentsDeleted:modified:incompatiblyModified:inParsedSchemas:].cold.1
+ -[ISDDataManager clientWithIdentifier:].cold.1
+ -[ISDDataManager enableFlush].cold.1
+ -[ISDDataManager noteChangesFromClient:key:value:].cold.1
+ -[ISDDataManager noteChangesFromClient:key:value:].cold.2
+ -[ISDDataManager noteChangesFromDataClass:key:value:].cold.1
+ -[ISDDataManager noteChangesFromEntity:key:value:].cold.1
+ -[ISDDataManager noteChangesFromFileReference:key:value:].cold.1
+ -[ISDDataManager noteChangesFromSchema:key:value:].cold.1
+ -[ISDDataManager noteChangesFromSyncState:key:value:].cold.1
+ -[ISDDataManager registerSchemaWithDescription:descriptionFilePath:bundlePath:helper:linkedOnTiger:].cold.1
+ -[ISDDataManager registerSchemaWithDescription:descriptionFilePath:bundlePath:helper:linkedOnTiger:].cold.2
+ -[ISDDataManager rollback].cold.1
+ -[ISDDataObject setDataManager:].cold.1
+ -[ISDDatabase(SqliteHelpers) bindInt:atIndex:inStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) bindObject:atIndex:inStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) bindUnsignedLongLong:atIndex:inStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) createDataFromColumn:inStatement:copyBytes:].cold.1
+ -[ISDDatabase(SqliteHelpers) createGlobalIdFromColumn:inStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) createStringFromColumn:inStatement:uniqueInStringTable:].cold.1
+ -[ISDDatabase(SqliteHelpers) finalizeStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) intFromColumn:inStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) prepareStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) resetStatement:unbindValuesThroughIndex:].cold.1
+ -[ISDDatabase(SqliteHelpers) stepStatement:].cold.1
+ -[ISDDatabase(SqliteHelpers) unsignedLongLongFromColumn:inStatement:].cold.1
+ -[ISDEntity attributeWithName:].cold.1
+ -[ISDEntity encodeWithCoder:].cold.1
+ -[ISDEntity initWithCoder:].cold.1
+ -[ISDEntity morphInToObjectExceptingProperties:].cold.1
+ -[ISDEntity morphInToObjectExceptingProperties:].cold.2
+ -[ISDEntity morphInToObjectExceptingProperties:].cold.3
+ -[ISDEntity relationshipWithName:].cold.1
+ -[ISDEntityComponent attributeWithName:].cold.1
+ -[ISDEntityComponent encodeWithCoder:].cold.1
+ -[ISDEntityComponent encodeWithCoder:].cold.2
+ -[ISDEntityComponent initWithCoder:].cold.1
+ -[ISDEntityComponent initWithCoder:].cold.2
+ -[ISDEntityComponent initWithExtensionName:entity:].cold.1
+ -[ISDEntityComponent initWithExtensionName:entity:].cold.2
+ -[ISDEntityComponent morphInToObject:].cold.1
+ -[ISDEntityComponent morphInToObject:].cold.2
+ -[ISDEntityComponent morphInToObject:].cold.3
+ -[ISDEntityComponent morphInToObject:].cold.4
+ -[ISDEntityComponent relationshipWithName:].cold.1
+ -[ISDFastCDSyncHelper _tryOpeningFastSyncStorage].cold.1
+ -[ISDFastCDSyncHelper _tryOpeningFastSyncStorage].cold.2
+ -[ISDFastCDSyncHelper setStoragePath:].cold.1
+ -[ISDFileReference encodeWithCoder:].cold.1
+ -[ISDFileReference initWithCoder:].cold.1
+ -[ISDFileReference initWithPath:bundleId:bundleRelativePath:windowsBinRelativePath:].cold.1
+ -[ISDFileReference initWithPath:bundleId:bundleRelativePath:windowsBinRelativePath:].cold.2
+ -[ISDNameNumberProvider canCreateNewMapping].cold.1
+ -[ISDNameNumberProvider clientMapping].cold.1
+ -[ISDNameNumberProvider entityMapping].cold.1
+ -[ISDNameNumberProvider refresh].cold.1
+ -[ISDProperty encodeWithCoder:].cold.1
+ -[ISDProperty initWithCoder:].cold.1
+ -[ISDProperty initWithName:entity:].cold.1
+ -[ISDProperty initWithName:entity:].cold.2
+ -[ISDProperty morphInToObject:].cold.1
+ -[ISDProperty morphInToObject:].cold.2
+ -[ISDProperty morphInToObject:].cold.3
+ -[ISDPropertyChange encodeWithCoder:].cold.1
+ -[ISDPropertyChange encodeWithCoder:].cold.2
+ -[ISDPropertyChange initWithCoder:].cold.1
+ -[ISDPropertyChange initWithCoder:].cold.2
+ -[ISDPropertyConflict encodeWithCoder:].cold.1
+ -[ISDPropertyConflict initWithCoder:].cold.1
+ -[ISDPropertyConflict setUserValues:].cold.1
+ -[ISDPropertyValue encodeWithCoder:].cold.1
+ -[ISDPropertyValue encodeWithCoder:].cold.2
+ -[ISDPropertyValue initDeletedPropertyValueWithPropertyType:name:deletedValue:lastModifiedGeneration:clientId:].cold.1
+ -[ISDPropertyValue initDeletedPropertyValueWithPropertyType:name:deletedValue:lastModifiedGeneration:clientId:].cold.2
+ -[ISDPropertyValue initWithCoder:].cold.1
+ -[ISDPropertyValue initWithCoder:].cold.2
+ -[ISDPropertyValue initWithPropertyType:name:value:lastModifiedGeneration:clientId:].cold.1
+ -[ISDPropertyValue initWithPropertyType:name:value:lastModifiedGeneration:clientId:].cold.2
+ -[ISDPropertyValue setValue:inGeneration:byClientWithId:].cold.1
+ -[ISDRecord encodeWithCoder:].cold.1
+ -[ISDRecord encodeWithCoder:].cold.2
+ -[ISDRecord initWithCoder:].cold.1
+ -[ISDRecord initWithCoder:].cold.2
+ -[ISDRecord initWithCoder:].cold.3
+ -[ISDRecordIdMapper _safeGlobalIdForLocalId:useConstructedIdMap:].cold.1
+ -[ISDRecordIdMapper entityNameForGlobalId:].cold.1
+ -[ISDRecordIdMapper entityNameForLocalId:].cold.1
+ -[ISDRecordIdMapper globalIdFromConstructedLocalId:].cold.1
+ -[ISDRecordIdMapper localIdConstructedFromGlobalId:useLocalIdAsGlobalId:].cold.1
+ -[ISDRecordIdMapper localIdForGlobalId:useLocalIdAsGlobalId:].cold.1
+ -[ISDRecordIdMapper noteUnresolvedPhantomWithGlobalId:].cold.1
+ -[ISDRecordIdMapper replaceGlobalId:withGlobalId:].cold.1
+ -[ISDRecordIdMapper replaceGlobalId:withGlobalId:].cold.2
+ -[ISDRecordIdMapper replaceGlobalId:withGlobalId:].cold.3
+ -[ISDRecordIdMapper replaceLocalId:withLocalId:].cold.1
+ -[ISDRecordIdMapper replaceLocalId:withLocalId:].cold.2
+ -[ISDRecordIdMapper replaceLocalId:withLocalId:].cold.3
+ -[ISDRecordIdMapper setMappingWithGlobalId:localId:entityName:].cold.1
+ -[ISDRecordIdMapper setMappingWithGlobalId:localId:entityName:].cold.2
+ -[ISDRecordStore recordIdentifiersOfRecordsInStates:count:entityNames:].cold.1
+ -[ISDRelationship encodeWithCoder:].cold.1
+ -[ISDRelationship initWithCoder:].cold.1
+ -[ISDRelationship morphInToObject:].cold.1
+ -[ISDRelationship morphInToObject:].cold.2
+ -[ISDRelationship morphInToObject:].cold.3
+ -[ISDRelationship ordering].cold.1
+ -[ISDRelationship setDeleteRule:].cold.1
+ -[ISDRelationship setOrdering:].cold.1
+ -[ISDRelationship setOrdering:].cold.2
+ -[ISDSchema encodeWithCoder:].cold.1
+ -[ISDSchema encodeWithCoder:].cold.2
+ -[ISDSchema initWithCoder:].cold.1
+ -[ISDSchema initWithCoder:].cold.2
+ -[ISDSchema morphInToObject:].cold.1
+ -[ISDSchema morphInToObject:].cold.2
+ -[ISDSchema morphInToObject:].cold.3
+ -[ISDSchemaParser _newRelationshipInDescription:component:schema:].cold.1
+ -[ISDSchemaParser _newRelationshipInDescription:component:schema:].cold.2
+ -[ISDSchemaParser _parseRelationshipsInDescription:component:schema:].cold.1
+ -[ISDSchemaParser parseDescription:bundleRef:linkedOnTiger:].cold.1
+ -[ISDServer _startMonitoringConnectionForProxy:clientId:].cold.1
+ -[ISDServer _startMonitoringConnectionForProxy:clientId:].cold.2
+ -[ISDServer _stopMonitoringConnectionForClientId:].cold.1
+ -[ISDServer clientWithId:auditTokenUUID:wantsToBeginSyncPlanBeforeDate:entityNames:pushTruthForEntityNames:quietlyPushingTruth:callback:withPlanIdentifier:hasChanges:skip:].cold.1
+ -[ISDServer clientWithId:auditTokenUUID:wantsToBeginSyncPlanBeforeDate:entityNames:pushTruthForEntityNames:quietlyPushingTruth:callback:withPlanIdentifier:hasChanges:skip:].cold.2
+ -[ISDServer clientWithId:didBeginPushingChangesInSyncPlan:negotiatedSyncStates:].cold.1
+ -[ISDServer clientWithId:didBeginPushingChangesInSyncPlan:negotiatedSyncStates:].cold.2
+ -[ISDServer clientWithId:didEndPushingChangesInSyncPlan:hasChanges:].cold.1
+ -[ISDServer clientWithId:didEndPushingChangesInSyncPlan:hasChanges:].cold.2
+ -[ISDServer clientWithId:didEndSyncPlan:finishedSyncing:].cold.1
+ -[ISDServer clientWithId:didEndSyncPlan:finishedSyncing:].cold.2
+ -[ISDServer setShouldReplaceClientRecords:forEntityNames:forClientWithIdentifier:].cold.1
+ -[ISDServer setShouldReplaceClientRecords:forEntityNames:forClientWithIdentifier:].cold.2
+ -[ISDServer setShouldReplaceClientRecords:forEntityNames:forClientWithIdentifier:].cold.3
+ -[ISDServer setSyncMode:forEntityNames:forClientWithIdentifier:].cold.1
+ -[ISDServer setSyncMode:forEntityNames:forClientWithIdentifier:].cold.2
+ -[ISDServer startWatchdog].cold.1
+ -[ISDSqliteChangeStore enumerateChangesForEntityNames:changeType:state:maxToEnumerate:asArgumentToFunction:context:].cold.1
+ -[ISDStructuredDelta changeForClientBetweenOldRecord:newRecord:].cold.1
+ -[ISDStructuredDelta changeForClientBetweenOldRecord:newRecord:].cold.2
+ -[ISDSyncManager _getSyncPlan:participant:forClient:].cold.1
+ -[ISDSyncManager _getSyncPlan:participant:forClient:].cold.2
+ -[ISDSyncManager _getSyncPlan:participant:forClient:].cold.3
+ -[ISDSyncManager client:didBeginPushingChangesInSyncPlan:negotiatedSyncStates:].cold.1
+ -[ISDSyncManager client:didBeginPushingChangesInSyncPlan:negotiatedSyncStates:].cold.2
+ -[ISDSyncManager client:didEndPushingChangesInSyncPlan:hasChanges:].cold.1
+ -[ISDSyncManager client:didEndPushingChangesInSyncPlan:hasChanges:].cold.2
+ -[ISDSyncManager client:wantsToBeginSyncPlanRightNow:].cold.1
+ -[ISDSyncManager client:wantsToBeginSyncPlanRightNow:].cold.2
+ -[ISDSyncManager removeClient:fromPendingSyncPlans:fromRunningSyncPlans:didFinishSyncing:notifyClient:reason:].cold.1
+ -[ISDSyncManager removeClient:fromSpecificSyncPlan:didFinishSyncing:notifyClient:reason:].cold.1
+ -[ISDSyncManager removeClient:fromSpecificSyncPlan:didFinishSyncing:notifyClient:reason:].cold.2
+ -[ISDSyncParticipant getTransientSyncMode:forEntityName:].cold.1
+ -[ISDSyncParticipant removeTransientSyncModeForEntityName:].cold.1
+ -[ISDSyncParticipant setApprovedToPushTruth:forEntityName:].cold.1
+ -[ISDSyncParticipant setSyncMode:forEntityName:].cold.1
+ -[ISDSyncParticipant setSyncMode:forEntityName:].cold.2
+ -[ISDSyncParticipant setTransientSyncMode:forEntityName:].cold.1
+ -[ISDSyncParticipant syncModeForEntityName:].cold.1
+ -[ISDSyncParticipant syncModeForEntityName:].cold.2
+ -[ISDSyncPlan _shouldTransitionToPushingPhase].cold.1
+ -[ISDSyncPlan participantDidBeginPushingChanges:negotiatedSyncStates:].cold.1
+ -[ISDSyncPlan participantDidBeginPushingChanges:negotiatedSyncStates:].cold.2
+ -[ISDSyncPlan participantDidBeginPushingChanges:negotiatedSyncStates:].cold.3
+ -[ISDSyncPlan participantDidEndPushingChanges:].cold.1
+ -[ISDSyncPlan participantDidEndPushingChanges:].cold.2
+ -[ISDSyncPlan participantDidEndPushingChanges:].cold.3
+ -[ISDSyncPlan participantWantsToBeginRightNow:].cold.1
+ -[ISDSyncPlan participantWantsToBeginRightNow:].cold.2
+ -[ISDSyncState encodeWithCoder:].cold.1
+ -[ISDSyncState initWithCoder:].cold.1
+ -[ISyncConcreteChange encodeWithCoder:].cold.1
+ -[ISyncConcreteChange encodeWithCoder:].cold.2
+ -[ISyncConcreteChange initWithCoder:].cold.1
+ -[ISyncConcreteChange initWithCoder:].cold.2
+ -[ISyncConcreteManager _connectToServerNoLock].cold.1
+ -[ISyncConcreteManager _stopObservingSyncPlan:].cold.1
+ -[ISyncConcreteManager applySyncPlanInfo:toSyncPlan:].cold.1
+ -[ISyncConcreteRecordReference encodeWithCoder:].cold.1
+ -[ISyncConcreteRecordReference initWithCoder:].cold.1
+ -[ISyncConcreteSession _changeForChangeEnumerator:betweenTruthRecord:clientRecord:].cold.1
+ -[ISyncConcreteSession _changeForChangeEnumerator:betweenTruthRecord:clientRecord:].cold.2
+ -[ISyncConcreteSession _enterPushing].cold.1
+ -[ISyncConcreteSession _enterPushing].cold.2
+ -[ISyncConcreteSession _enterPushing].cold.3
+ -[ISyncConcreteSession _enterPushing].cold.4
+ -[ISyncConcreteSession _enterPushing].cold.5
+ -[ISyncConcreteSession _prepareRecordStoreForSlowSyncingEntityNames:].cold.1
+ -[ISyncConcreteSession clientWithId:canBeginSyncingPlanWithId:currentGeneration:syncModes:entities:truthPullers:].cold.1
+ -[ISyncConcreteSession unresolvedReferencesAreForUnknownTypes:].cold.1
+ -[NSException(ISDFriendlyException) _friendlyInitWithName:reason:userInfo:].cold.1
+ -[NSException(ISDFriendlyException) _friendlyRaise].cold.1
+ _ISDClientNameSymlinkPathForClient.cold.1
+ _ISDHexDataDirectoryPathForClient.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __ISDDefaultSyncServicesDirectoryPath.cold.1
+ __ISDDefaultSyncServicesLogDirectoryPath.cold.1
+ __withMachPortsForUUIDs_block_invoke.cold.1
+ withMachPortsForUUIDs.cold.1
- _strncmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDAdminDatabase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDChange.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDChangeStore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDClientState.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDConflict.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDConflictManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataDatabase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataObject.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataReference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDEntity.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDFileReference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDIdMapDatabase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDNameNumberMapping.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPersistentStoreSyncer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyChange.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyConflict.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyValue.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyValueEncoding.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDQuickDirtyCoder.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecord.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecordIdMapper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecordStore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSchemaParser.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDServer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteChangeStore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteDatabase.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteRecordIdMapper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDStructuredDelta.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSyncPlan.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncChange.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncClient.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncRecordSnapshot.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/Miscellaneous.m"
+ "22:57:54"
+ "Mar  7 2025"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDAdminDatabase.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDChange.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDChangeStore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDClientState.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDConflict.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDConflictManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataDatabase.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataObject.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDDataReference.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDEntity.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDFileReference.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDIdMapDatabase.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDNameNumberMapping.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPersistentStoreSyncer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyChange.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyConflict.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyValue.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDPropertyValueEncoding.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDQuickDirtyCoder.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecord.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecordIdMapper.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDRecordStore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSchemaParser.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDServer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteChangeStore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteDatabase.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSqliteRecordIdMapper.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDStructuredDelta.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSyncManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISDSyncPlan.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncChange.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncClient.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncRecordSnapshot.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/ISyncSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SyncServices2/SyncServices/Miscellaneous.m"
- "00:56:33"
- "Dec 14 2024"
- "ok"

```
