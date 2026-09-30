## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

```diff

-907.15.0.0.0
-  __TEXT.__text: 0x95b8
-  __TEXT.__auth_stubs: 0x530
+1061.1.1.0.0
+  __TEXT.__text: 0x115a0
+  __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_stubs: 0x1800
-  __TEXT.__objc_methlist: 0xca4
+  __TEXT.__objc_methlist: 0xc9c
   __TEXT.__cstring: 0x2174
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x2228
-  __TEXT.__objc_methtype: 0x9f1
-  __TEXT.__const: 0x68
+  __TEXT.__objc_methname: 0x21cb
+  __TEXT.__objc_methtype: 0x947
   __TEXT.__oslogstring: 0xe30
-  __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xb28
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__unwind_info: 0x268
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0xb10
   __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xde0
-  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_const: 0xdd8
+  __DATA.__objc_selrefs: 0x978
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x420

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AF5068CA-C421-3AAF-8895-22EDA035AF5A
-  Functions: 209
-  Symbols:   165
-  CStrings:  641
+  UUID: 3F450BA5-4FBE-3DE7-A7A2-4DB3DB8068B9
+  Functions: 206
+  Symbols:   1721
+  CStrings:  636
 
Symbols:
+ 
+ +[WOWorkoutConfigurationEntity columnDefinitionsWithCount:]
+ +[WOWorkoutConfigurationEntity dateProperties]
+ +[WOWorkoutConfigurationEntity integerProperties]
+ +[WOWorkoutConfigurationEntity isPropertyFatal:version:]
+ +[WOWorkoutConfigurationEntity persistenceType]
+ +[WOWorkoutConfigurationEntity propertyForConfigurationType]
+ +[WOWorkoutConfigurationEntity tableName]
+ +[WOWorkoutEntity _cleanupDeletedObjectsWithProfile:type:]
+ +[WOWorkoutEntity _cleanupTombstoneExpirationIntervalForPersistenceType:]
+ +[WOWorkoutEntity _lookup:ofType:profile:transaction:]
+ +[WOWorkoutEntity _nonRaceConfigPredicate:]
+ +[WOWorkoutEntity _shouldInsertOrReplaceLocal:withRemote:]
+ +[WOWorkoutEntity allProperties]
+ +[WOWorkoutEntity bind:provenance:syncIdentity:toBinder:]
+ +[WOWorkoutEntity classForPersistenceType:]
+ +[WOWorkoutEntity columnDefinitionsWithCount:]
+ +[WOWorkoutEntity dataProperties]
+ +[WOWorkoutEntity databaseTable]
+ +[WOWorkoutEntity dateProperties]
+ +[WOWorkoutEntity decodeSyncObjectWithData:]
+ +[WOWorkoutEntity generateSyncObjectsForSession:syncAnchorRange:profile:messageHandler:error:]
+ +[WOWorkoutEntity integerProperties]
+ +[WOWorkoutEntity isPropertyFatal:version:]
+ +[WOWorkoutEntity nextSyncAnchorWithSession:startSyncAnchor:profile:error:]
+ +[WOWorkoutEntity persistenceFromRow:type:profile:transaction:]
+ +[WOWorkoutEntity persistenceType]
+ +[WOWorkoutEntity preparePersistenceForDelete:]
+ +[WOWorkoutEntity propertyForObjectModificationDate]
+ +[WOWorkoutEntity propertyForObjectState]
+ +[WOWorkoutEntity propertyForSyncIdentity]
+ +[WOWorkoutEntity propertyForSyncProvenance]
+ +[WOWorkoutEntity propertyForUUID]
+ +[WOWorkoutEntity protectionClass]
+ +[WOWorkoutEntity protoPersistenceFromRow:type:profile:transaction:]
+ +[WOWorkoutEntity receiveSyncObjects:version:syncStore:profile:error:]
+ +[WOWorkoutEntity stringProperties]
+ +[WOWorkoutEntity syncEntityDependenciesForSyncProtocolVersion:]
+ +[WOWorkoutEntity syncEntityIdentifier]
+ +[WOWorkoutEntity tableName]
+ +[WOWorkoutExternalConfigurationProviderEntity columnDefinitionsWithCount:]
+ +[WOWorkoutExternalConfigurationProviderEntity dataProperties]
+ +[WOWorkoutExternalConfigurationProviderEntity dateProperties]
+ +[WOWorkoutExternalConfigurationProviderEntity integerProperties]
+ +[WOWorkoutExternalConfigurationProviderEntity persistenceType]
+ +[WOWorkoutExternalConfigurationProviderEntity preparePersistenceForDelete:]
+ +[WOWorkoutExternalConfigurationProviderEntity propertyForProviderIdentifier]
+ +[WOWorkoutExternalConfigurationProviderEntity stringProperties]
+ +[WOWorkoutExternalConfigurationProviderEntity tableName]
+ +[WOWorkoutExternalProviderObserver sharedInstance]
+ +[WOWorkoutGymKitNFCManager _isWorkoutNFCAllDayEnabledString]
+ +[WOWorkoutGymKitNFCManager disableGymKitNFCSwitchOnOldHardwareIfNeeded]
+ +[WOWorkoutHealthProfileExtension _isOldWatchSeries:]
+ +[WOWorkoutHealthSchemaProvider _addExternalConfigurationProviderColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addManagedConfigurationsColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addManagedProtoConfigurationsColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addOccurrenceColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addProtoConfigurationsColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addSyncIdentityColumnWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _addSyncObjectColumnsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _deleteRaceWorkoutConfigurationsWithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion2WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion3WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion4WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion5WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion6WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion7WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion8WithMigrator:]
+ +[WOWorkoutHealthSchemaProvider currentSchemaVersionForProtectionClass:]
+ +[WOWorkoutHealthSchemaProvider databaseEntitiesForProtectionClass:]
+ +[WOWorkoutHealthSchemaProvider registerMigrationStepsForProtectionClass:migrator:]
+ +[WOWorkoutManagedConfigurationEntity columnDefinitionsWithCount:]
+ +[WOWorkoutManagedConfigurationEntity dateProperties]
+ +[WOWorkoutManagedConfigurationEntity isPropertyFatal:version:]
+ +[WOWorkoutManagedConfigurationEntity persistenceType]
+ +[WOWorkoutManagedConfigurationEntity propertyForManagedSourceIdentifier]
+ +[WOWorkoutManagedConfigurationEntity stringProperties]
+ +[WOWorkoutManagedConfigurationEntity tableName]
+ +[WOWorkoutQueryServer serverWithClient:profile:error:]
+ -[WOWorkoutExternalProviderObserver .cxx_destruct]
+ -[WOWorkoutExternalProviderObserver _init]
+ -[WOWorkoutExternalProviderObserver applicationsDidUninstall:]
+ -[WOWorkoutExternalProviderObserver dealloc]
+ -[WOWorkoutExternalProviderObserver queue_evaluateRemovedBundleIdentifiers:]
+ -[WOWorkoutHealthPlugin currentSchemaVersionForProtectionClass:]
+ -[WOWorkoutHealthPlugin databaseEntitiesForProtectionClass:]
+ -[WOWorkoutHealthPlugin extensionForHealthDaemon:]
+ -[WOWorkoutHealthPlugin extensionForProfile:]
+ -[WOWorkoutHealthPlugin orderedSyncEntities]
+ -[WOWorkoutHealthPlugin pluginIdentifier]
+ -[WOWorkoutHealthPlugin registerMigrationStepsForProtectionClass:migrator:]
+ -[WOWorkoutHealthPlugin schemaName]
+ -[WOWorkoutHealthPlugin syncSchemaIdentifier]
+ -[WOWorkoutHealthProfileExtension .cxx_destruct]
+ -[WOWorkoutHealthProfileExtension exportObjectForListener:client:error:]
+ -[WOWorkoutHealthProfileExtension initWithProfile:]
+ -[WOWorkoutHealthProfileExtension listenerEndpointForClient:error:]
+ -[WOWorkoutHealthProfileExtension listener]
+ -[WOWorkoutHealthProfileExtension profile]
+ -[WOWorkoutHealthProfileExtension setListener:]
+ -[WOWorkoutHealthProfileExtension setProfile:]
+ -[WOWorkoutQueryServer .cxx_destruct]
+ -[WOWorkoutQueryServer _delete:ofType:withCompletion:]
+ -[WOWorkoutQueryServer _deleteConfigurations:ofType:withCompletion:]
+ -[WOWorkoutQueryServer _deleteExternalProvidersWithSourceIdentifier:completion:]
+ -[WOWorkoutQueryServer _deleteManagedFromSource:withCompletion:]
+ -[WOWorkoutQueryServer _fetch:ofType:state:withCompletion:]
+ -[WOWorkoutQueryServer _fetchAll:withCompletion:]
+ -[WOWorkoutQueryServer _fetchManagedFromSource:withCompletion:]
+ -[WOWorkoutQueryServer _fetchProtoAll:state:withCompletion:]
+ -[WOWorkoutQueryServer _fetchProviderWithSourceIdentifier:withCompletion:]
+ -[WOWorkoutQueryServer _save:withCompletion:]
+ -[WOWorkoutQueryServer _saveConfigurations:ofType:withCompletion:]
+ -[WOWorkoutQueryServer _statePredicateForClass:state:]
+ -[WOWorkoutQueryServer _validateConfigurations:withPersistenceType:error:]
+ -[WOWorkoutQueryServer client]
+ -[WOWorkoutQueryServer connectionInvalidated]
+ -[WOWorkoutQueryServer exportedInterface]
+ -[WOWorkoutQueryServer initWithClient:profile:]
+ -[WOWorkoutQueryServer profile]
+ -[WOWorkoutQueryServer remoteInterface]
+ -[WOWorkoutQueryServer remote_addManagedConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer remote_deleteConfiguration:withCompletion:]
+ -[WOWorkoutQueryServer remote_deleteExternalProvider:withCompletion:]
+ -[WOWorkoutQueryServer remote_deleteManagedConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer remote_fetchAllConfigurationsAsSerializedPersistenceWithCompletion:]
+ -[WOWorkoutQueryServer remote_fetchAllDeletedConfigurationsAsSerializedPersistenceWithCompletion:]
+ -[WOWorkoutQueryServer remote_fetchAllExternalProvidersWithCompletion:]
+ -[WOWorkoutQueryServer remote_fetchConfiguration:withCompletion:]
+ -[WOWorkoutQueryServer remote_fetchDeletedConfiguration:withCompletion:]
+ -[WOWorkoutQueryServer remote_fetchExternalProviderForIdentifier:withCompletion:]
+ -[WOWorkoutQueryServer remote_fetchManagedConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer remote_fetchManagedConfigurationsByProviderWithCompletion:]
+ -[WOWorkoutQueryServer remote_removeManagedConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer remote_saveConfiguration:withCompletion:]
+ -[WOWorkoutQueryServer remote_saveConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer remote_setManagedConfigurations:withCompletion:]
+ -[WOWorkoutQueryServer setClient:]
+ -[WOWorkoutQueryServer setProfile:]
+ -[WOWorkoutQueryServer setTemporaryString:]
+ -[WOWorkoutQueryServer temporaryString]
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutConfigurationEntity.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutEntity.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutExternalConfigurationProviderEntity.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutExternalProviderObserver.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutGymKitNFCManager.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutHealthPlugin.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutHealthProfileExtension.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutHealthSchemaProvider.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutManagedConfigurationEntity.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutHealthPlugin.build/Objects-normal/arm64e/WOWorkoutQueryServer.o
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutHealthPlugin/
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutHealthPlugin/Entities/
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutHealthPlugin/GymKitNFC/
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutHealthPlugin/SchemaProvider/
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table26
+ GCC_except_table34
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table48
+ OBJC_IVAR_$_WOWorkoutExternalProviderObserver._workerQueue
+ OBJC_IVAR_$_WOWorkoutHealthProfileExtension._listener
+ OBJC_IVAR_$_WOWorkoutHealthProfileExtension._profile
+ OBJC_IVAR_$_WOWorkoutQueryServer._client
+ OBJC_IVAR_$_WOWorkoutQueryServer._profile
+ OBJC_IVAR_$_WOWorkoutQueryServer._temporaryString
+ WOWorkoutConfigurationEntity.m
+ WOWorkoutEntity.m
+ WOWorkoutExternalConfigurationProviderEntity.m
+ WOWorkoutExternalProviderObserver.m
+ WOWorkoutGymKitNFCManager.m
+ WOWorkoutHealthPlugin.m
+ WOWorkoutHealthProfileExtension.m
+ WOWorkoutHealthSchemaProvider.m
+ WOWorkoutManagedConfigurationEntity.m
+ WOWorkoutQueryServer.m
+ __70+[WOWorkoutEntity receiveSyncObjects:version:syncStore:profile:error:]_block_invoke.341
+ __80-[WOWorkoutQueryServer _deleteExternalProvidersWithSourceIdentifier:completion:]_block_invoke.332
+ __OBJC_$_CLASS_METHODS_WOWorkoutConfigurationEntity
+ __OBJC_$_CLASS_METHODS_WOWorkoutEntity
+ __OBJC_$_CLASS_METHODS_WOWorkoutExternalConfigurationProviderEntity
+ __OBJC_$_CLASS_METHODS_WOWorkoutExternalProviderObserver
+ __OBJC_$_CLASS_METHODS_WOWorkoutGymKitNFCManager
+ __OBJC_$_CLASS_METHODS_WOWorkoutHealthProfileExtension
+ __OBJC_$_CLASS_METHODS_WOWorkoutHealthSchemaProvider
+ __OBJC_$_CLASS_METHODS_WOWorkoutManagedConfigurationEntity
+ __OBJC_$_CLASS_METHODS_WOWorkoutQueryServer
+ __OBJC_$_CLASS_PROP_LIST_HDSyncEntity
+ __OBJC_$_CLASS_PROP_LIST_WOWorkoutEntity
+ __OBJC_$_INSTANCE_METHODS_WOWorkoutExternalProviderObserver
+ __OBJC_$_INSTANCE_METHODS_WOWorkoutHealthPlugin
+ __OBJC_$_INSTANCE_METHODS_WOWorkoutHealthProfileExtension
+ __OBJC_$_INSTANCE_METHODS_WOWorkoutQueryServer
+ __OBJC_$_INSTANCE_VARIABLES_WOWorkoutExternalProviderObserver
+ __OBJC_$_INSTANCE_VARIABLES_WOWorkoutHealthProfileExtension
+ __OBJC_$_INSTANCE_VARIABLES_WOWorkoutQueryServer
+ __OBJC_$_PROP_LIST_HDDatabaseSchemaProvider
+ __OBJC_$_PROP_LIST_HDPlugin
+ __OBJC_$_PROP_LIST_HDSyncEntityProvider
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_WOWorkoutEntity
+ __OBJC_$_PROP_LIST_WOWorkoutExternalProviderObserver
+ __OBJC_$_PROP_LIST_WOWorkoutHealthPlugin
+ __OBJC_$_PROP_LIST_WOWorkoutHealthProfileExtension
+ __OBJC_$_PROP_LIST_WOWorkoutQueryServer
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HDSyncEntity
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_HDNanoSyncEntity
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_HDPlugin
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_HDSyncEntity
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDDatabaseSchemaProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDPlugin
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSyncEntityProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDPlugin
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDProfileExtension
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__HKXPCExportable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WOWorkoutServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKXPCExportable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDDatabaseSchemaProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDNanoSyncEntity
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDPlugin
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDProfileExtension
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDSyncEntity
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDSyncEntityProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WOWorkoutServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HKXPCExportable
+ __OBJC_$_PROTOCOL_REFS_HDNanoSyncEntity
+ __OBJC_$_PROTOCOL_REFS_HDPlugin
+ __OBJC_$_PROTOCOL_REFS_HDProfileExtension
+ __OBJC_$_PROTOCOL_REFS_HDSyncEntity
+ __OBJC_$_PROTOCOL_REFS_HDSyncEntityProvider
+ __OBJC_$_PROTOCOL_REFS_HDXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_LSApplicationWorkspaceObserverProtocol
+ __OBJC_$_PROTOCOL_REFS_WOWorkoutServerInterface
+ __OBJC_$_PROTOCOL_REFS__HKXPCExportable
+ __OBJC_CLASS_PROTOCOLS_$_WOWorkoutEntity
+ __OBJC_CLASS_PROTOCOLS_$_WOWorkoutExternalProviderObserver
+ __OBJC_CLASS_PROTOCOLS_$_WOWorkoutHealthPlugin
+ __OBJC_CLASS_PROTOCOLS_$_WOWorkoutHealthProfileExtension
+ __OBJC_CLASS_PROTOCOLS_$_WOWorkoutQueryServer
+ __OBJC_CLASS_RO_$_WOWorkoutConfigurationEntity
+ __OBJC_CLASS_RO_$_WOWorkoutEntity
+ __OBJC_CLASS_RO_$_WOWorkoutExternalConfigurationProviderEntity
+ __OBJC_CLASS_RO_$_WOWorkoutExternalProviderObserver
+ __OBJC_CLASS_RO_$_WOWorkoutGymKitNFCManager
+ __OBJC_CLASS_RO_$_WOWorkoutHealthPlugin
+ __OBJC_CLASS_RO_$_WOWorkoutHealthProfileExtension
+ __OBJC_CLASS_RO_$_WOWorkoutHealthSchemaProvider
+ __OBJC_CLASS_RO_$_WOWorkoutManagedConfigurationEntity
+ __OBJC_CLASS_RO_$_WOWorkoutQueryServer
+ __OBJC_LABEL_PROTOCOL_$_HDDatabaseSchemaProvider
+ __OBJC_LABEL_PROTOCOL_$_HDNanoSyncEntity
+ __OBJC_LABEL_PROTOCOL_$_HDPlugin
+ __OBJC_LABEL_PROTOCOL_$_HDProfileExtension
+ __OBJC_LABEL_PROTOCOL_$_HDSyncEntity
+ __OBJC_LABEL_PROTOCOL_$_HDSyncEntityProvider
+ __OBJC_LABEL_PROTOCOL_$_HDXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_WOWorkoutServerInterface
+ __OBJC_LABEL_PROTOCOL_$__HKXPCExportable
+ __OBJC_METACLASS_RO_$_WOWorkoutConfigurationEntity
+ __OBJC_METACLASS_RO_$_WOWorkoutEntity
+ __OBJC_METACLASS_RO_$_WOWorkoutExternalConfigurationProviderEntity
+ __OBJC_METACLASS_RO_$_WOWorkoutExternalProviderObserver
+ __OBJC_METACLASS_RO_$_WOWorkoutGymKitNFCManager
+ __OBJC_METACLASS_RO_$_WOWorkoutHealthPlugin
+ __OBJC_METACLASS_RO_$_WOWorkoutHealthProfileExtension
+ __OBJC_METACLASS_RO_$_WOWorkoutHealthSchemaProvider
+ __OBJC_METACLASS_RO_$_WOWorkoutManagedConfigurationEntity
+ __OBJC_METACLASS_RO_$_WOWorkoutQueryServer
+ __OBJC_PROTOCOL_$_HDDatabaseSchemaProvider
+ __OBJC_PROTOCOL_$_HDNanoSyncEntity
+ __OBJC_PROTOCOL_$_HDPlugin
+ __OBJC_PROTOCOL_$_HDProfileExtension
+ __OBJC_PROTOCOL_$_HDSyncEntity
+ __OBJC_PROTOCOL_$_HDSyncEntityProvider
+ __OBJC_PROTOCOL_$_HDXPCListenerDelegate
+ __OBJC_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_WOWorkoutServerInterface
+ __OBJC_PROTOCOL_$__HKXPCExportable
+ ___49-[WOWorkoutQueryServer _fetchAll:withCompletion:]_block_invoke
+ ___49-[WOWorkoutQueryServer _fetchAll:withCompletion:]_block_invoke_2
+ ___51+[WOWorkoutExternalProviderObserver sharedInstance]_block_invoke
+ ___54+[WOWorkoutEntity _lookup:ofType:profile:transaction:]_block_invoke
+ ___54-[WOWorkoutQueryServer _delete:ofType:withCompletion:]_block_invoke
+ ___58+[WOWorkoutEntity _cleanupDeletedObjectsWithProfile:type:]_block_invoke
+ ___59-[WOWorkoutQueryServer _fetch:ofType:state:withCompletion:]_block_invoke
+ ___59-[WOWorkoutQueryServer _fetch:ofType:state:withCompletion:]_block_invoke_2
+ ___60-[WOWorkoutQueryServer _fetchProtoAll:state:withCompletion:]_block_invoke
+ ___60-[WOWorkoutQueryServer _fetchProtoAll:state:withCompletion:]_block_invoke_2
+ ___62-[WOWorkoutExternalProviderObserver applicationsDidUninstall:]_block_invoke
+ ___63-[WOWorkoutQueryServer _fetchManagedFromSource:withCompletion:]_block_invoke
+ ___63-[WOWorkoutQueryServer _fetchManagedFromSource:withCompletion:]_block_invoke_2
+ ___64-[WOWorkoutQueryServer _deleteManagedFromSource:withCompletion:]_block_invoke
+ ___66-[WOWorkoutQueryServer _saveConfigurations:ofType:withCompletion:]_block_invoke
+ ___66-[WOWorkoutQueryServer _saveConfigurations:ofType:withCompletion:]_block_invoke_2
+ ___67+[WOWorkoutHealthSchemaProvider _addOccurrenceColumnsWithMigrator:]_block_invoke
+ ___67+[WOWorkoutHealthSchemaProvider _addSyncObjectColumnsWithMigrator:]_block_invoke
+ ___68+[WOWorkoutHealthSchemaProvider _addSyncIdentityColumnWithMigrator:]_block_invoke
+ ___68+[WOWorkoutHealthSchemaProvider _addSyncIdentityColumnWithMigrator:]_block_invoke_2
+ ___68+[WOWorkoutHealthSchemaProvider _addSyncIdentityColumnWithMigrator:]_block_invoke_3
+ ___70+[WOWorkoutEntity receiveSyncObjects:version:syncStore:profile:error:]_block_invoke
+ ___74-[WOWorkoutQueryServer _fetchProviderWithSourceIdentifier:withCompletion:]_block_invoke
+ ___74-[WOWorkoutQueryServer _fetchProviderWithSourceIdentifier:withCompletion:]_block_invoke_2
+ ___76+[WOWorkoutHealthSchemaProvider _addProtoConfigurationsColumnsWithMigrator:]_block_invoke
+ ___76-[WOWorkoutExternalProviderObserver queue_evaluateRemovedBundleIdentifiers:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion2WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion3WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion4WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion5WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion6WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion7WithMigrator:]_block_invoke
+ ___77+[WOWorkoutHealthSchemaProvider _emptyMigrationToSchemaVersion8WithMigrator:]_block_invoke
+ ___78+[WOWorkoutHealthSchemaProvider _addManagedConfigurationsColumnsWithMigrator:]_block_invoke
+ ___78+[WOWorkoutHealthSchemaProvider _deleteRaceWorkoutConfigurationsWithMigrator:]_block_invoke
+ ___80-[WOWorkoutQueryServer _deleteExternalProvidersWithSourceIdentifier:completion:]_block_invoke
+ ___82-[WOWorkoutQueryServer remote_fetchManagedConfigurationsByProviderWithCompletion:]_block_invoke
+ ___82-[WOWorkoutQueryServer remote_fetchManagedConfigurationsByProviderWithCompletion:]_block_invoke_2
+ ___82-[WOWorkoutQueryServer remote_fetchManagedConfigurationsByProviderWithCompletion:]_block_invoke_3
+ ___83+[WOWorkoutHealthSchemaProvider _addManagedProtoConfigurationsColumnsWithMigrator:]_block_invoke
+ ___86+[WOWorkoutHealthSchemaProvider _addExternalConfigurationProviderColumnsWithMigrator:]_block_invoke
+ ___91-[WOWorkoutQueryServer remote_fetchAllConfigurationsAsSerializedPersistenceWithCompletion:]_block_invoke
+ ___94+[WOWorkoutEntity generateSyncObjectsForSession:syncAnchorRange:profile:messageHandler:error:]_block_invoke
+ ___94+[WOWorkoutEntity generateSyncObjectsForSession:syncAnchorRange:profile:messageHandler:error:]_block_invoke_2
+ ___98-[WOWorkoutQueryServer remote_fetchAllDeletedConfigurationsAsSerializedPersistenceWithCompletion:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e70_q40?0"HDDatabaseMigrator"8"HDDatabaseMigrationTransaction"16q24^32l
+ ___block_descriptor_40_e8_32bs_e57_v24?0"WOHealthBridgeProtoPersistenceArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e23_v16?0^{sqlite3_stmt=}8lr32l8
+ ___block_descriptor_40_e8_32r_e26_B24?0^{HDSQLiteRow=}8^16lr32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e35_v24?0"WOPersistence"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"WOPersistence"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e34_v16?0^{HDSQLiteStatementBinder=}8lu48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8u48l8s40l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32lu56l8s32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s_e34_v16?0^{HDSQLiteStatementBinder=}8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32lu56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e51_B64?08"NSArray"16^{HDSQLiteRow=}24q32Q40^B48^56ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8u48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32lu56l8s32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8u64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32lu56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8u48l8s40l8
+ ___block_descriptor_80_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8r56l8s40l8s48l8
+ ___block_literal_global
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_1_8_0
+ ___os_log_helper_16_2_1_8_64
+ ___os_log_helper_16_2_1_8_66
+ ___os_log_helper_16_2_2_8_0_8_66
+ ___os_log_helper_16_2_2_8_64_8_0
+ ___os_log_helper_16_2_2_8_64_8_64
+ ___os_log_helper_16_2_2_8_66_8_2
+ ___os_log_helper_16_2_2_8_66_8_66
+ ___os_log_helper_16_2_3_8_66_8_0_8_66
+ ___os_log_helper_16_2_3_8_66_8_64_8_64
+ ___os_log_helper_16_2_4_8_64_8_0_8_64_8_64
+ ___os_log_helper_16_2_4_8_64_8_64_8_64_8_64
+ ___os_log_helper_16_2_4_8_66_8_64_8_64_8_64
+ ___os_log_helper_16_2_4_8_66_8_66_8_0_8_64
+ __block_literal_global.297
+ __block_literal_global.319
+ __block_literal_global.321
+ __block_literal_global.334
+ __block_literal_global.336
+ __block_literal_global.341
+ __block_literal_global.343
+ __block_literal_global.351
+ __block_literal_global.368
+ __block_literal_global.370
+ __block_literal_global.375
+ __block_literal_global.377
+ __block_literal_global.397
+ __block_literal_global.399
+ __block_literal_global.407
+ _memset
+ _objc_msgSend$_addExternalConfigurationProviderColumnsWithMigrator:
+ _objc_msgSend$_addManagedConfigurationsColumnsWithMigrator:
+ _objc_msgSend$_addManagedProtoConfigurationsColumnsWithMigrator:
+ _objc_msgSend$_addOccurrenceColumnsWithMigrator:
+ _objc_msgSend$_addProtoConfigurationsColumnsWithMigrator:
+ _objc_msgSend$_addSyncIdentityColumnWithMigrator:
+ _objc_msgSend$_addSyncObjectColumnsWithMigrator:
+ _objc_msgSend$_cleanupDeletedObjectsWithProfile:type:
+ _objc_msgSend$_cleanupTombstoneExpirationIntervalForPersistenceType:
+ _objc_msgSend$_delete:ofType:withCompletion:
+ _objc_msgSend$_deleteConfigurations:ofType:withCompletion:
+ _objc_msgSend$_deleteExternalProvidersWithSourceIdentifier:completion:
+ _objc_msgSend$_deleteManagedFromSource:withCompletion:
+ _objc_msgSend$_deleteRaceWorkoutConfigurationsWithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion2WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion3WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion4WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion5WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion6WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion7WithMigrator:
+ _objc_msgSend$_emptyMigrationToSchemaVersion8WithMigrator:
+ _objc_msgSend$_fetch:ofType:state:withCompletion:
+ _objc_msgSend$_fetchAll:withCompletion:
+ _objc_msgSend$_fetchManagedFromSource:withCompletion:
+ _objc_msgSend$_fetchProtoAll:state:withCompletion:
+ _objc_msgSend$_fetchProviderWithSourceIdentifier:withCompletion:
+ _objc_msgSend$_init
+ _objc_msgSend$_isOldWatchSeries:
+ _objc_msgSend$_isWorkoutNFCAllDayEnabledString
+ _objc_msgSend$_lookup:ofType:profile:transaction:
+ _objc_msgSend$_nonRaceConfigPredicate:
+ _objc_msgSend$_save:withCompletion:
+ _objc_msgSend$_saveConfigurations:ofType:withCompletion:
+ _objc_msgSend$_shouldInsertOrReplaceLocal:withRemote:
+ _objc_msgSend$_statePredicateForClass:state:
+ _objc_msgSend$_validateConfigurations:withPersistenceType:error:
+ _objc_msgSend$addKeyedDatas:
+ _objc_msgSend$addKeyedDates:
+ _objc_msgSend$addKeyedNumbers:
+ _objc_msgSend$addKeyedStrings:
+ _objc_msgSend$addMigrationForSchema:toVersion:foreignKeyStatus:handler:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addPersistences:
+ _objc_msgSend$allObjects
+ _objc_msgSend$allProperties
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$bind:provenance:syncIdentity:toBinder:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$classForPersistenceType:
+ _objc_msgSend$client
+ _objc_msgSend$compare:
+ _objc_msgSend$compoundPredicateWithPredicate:otherPredicate:
+ _objc_msgSend$concreteIdentityForIdentity:shouldCreate:transaction:error:
+ _objc_msgSend$connection
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentDeviceProductType
+ _objc_msgSend$currentSchemaVersionForProtectionClass:
+ _objc_msgSend$currentSyncIdentityPersistentID
+ _objc_msgSend$data
+ _objc_msgSend$dataProperties
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$database
+ _objc_msgSend$databaseEntitiesForProtectionClass:
+ _objc_msgSend$databaseIdentifier
+ _objc_msgSend$date
+ _objc_msgSend$dateProperties
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$deleteEntitiesWithPredicate:healthDatabase:error:
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$disableGymKitNFCSwitchOnOldHardwareIfNeeded
+ _objc_msgSend$endpoint
+ _objc_msgSend$entity
+ _objc_msgSend$enumerateEntitiesForSyncWithProperties:predicate:session:syncAnchorRange:limit:lastSyncAnchor:healthDatabase:error:block:
+ _objc_msgSend$enumerateProperties:withPredicate:healthDatabase:error:enumerationHandler:
+ _objc_msgSend$executeSQL:error:bindingHandler:enumerationHandler:
+ _objc_msgSend$executeSQLStatements:error:
+ _objc_msgSend$executeUncachedSQL:error:
+ _objc_msgSend$firstObject
+ _objc_msgSend$handleUninstalledAppIds:completion:
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasRequiredEntitlement:error:
+ _objc_msgSend$hk_dataForUUIDBytes
+ _objc_msgSend$hk_error:description:
+ _objc_msgSend$identifierWithSchema:entity:
+ _objc_msgSend$identity
+ _objc_msgSend$identityForEntityID:transaction:error:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithClient:profile:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithHardwareIdentifier:databaseIdentifier:instanceDiscriminator:
+ _objc_msgSend$initWithLabel:
+ _objc_msgSend$initWithProfile:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithVersion:type:uuid:persistedData:persistedProtoData:objectState:objectModificationDate:syncIdentity:
+ _objc_msgSend$insertOrReplaceEntity:database:properties:error:bindingHandler:
+ _objc_msgSend$instanceDiscriminator
+ _objc_msgSend$integerProperties
+ _objc_msgSend$invalidate
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isPropertyFatal:version:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$keyedDatas
+ _objc_msgSend$keyedDates
+ _objc_msgSend$keyedNumbers
+ _objc_msgSend$keyedStrings
+ _objc_msgSend$legacySyncIdentity
+ _objc_msgSend$length
+ _objc_msgSend$listener
+ _objc_msgSend$nextSyncAnchorWithStartAnchor:predicate:session:healthDatabase:error:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$objectModificationDate
+ _objc_msgSend$objectState
+ _objc_msgSend$performReadTransactionWithHealthDatabase:error:block:
+ _objc_msgSend$performWriteTransactionWithHealthDatabase:error:block:
+ _objc_msgSend$persistedData
+ _objc_msgSend$persistedProtoData
+ _objc_msgSend$persistenceFromRow:type:profile:transaction:
+ _objc_msgSend$persistenceType
+ _objc_msgSend$persistentID
+ _objc_msgSend$predicateWithProperty:equalToValue:
+ _objc_msgSend$predicateWithProperty:lessThanValue:
+ _objc_msgSend$predicateWithProperty:notEqualToValue:
+ _objc_msgSend$preparePersistenceForDelete:
+ _objc_msgSend$process
+ _objc_msgSend$profileType
+ _objc_msgSend$propertyForConfigurationType
+ _objc_msgSend$propertyForManagedSourceIdentifier
+ _objc_msgSend$propertyForObjectModificationDate
+ _objc_msgSend$propertyForObjectState
+ _objc_msgSend$propertyForProviderIdentifier
+ _objc_msgSend$propertyForUUID
+ _objc_msgSend$protoPersistenceFromRow:type:profile:transaction:
+ _objc_msgSend$queue_evaluateRemovedBundleIdentifiers:
+ _objc_msgSend$registerMigrationStepsForProtectionClass:migrator:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$resume
+ _objc_msgSend$sendCodableChange:resultAnchor:sequence:done:error:
+ _objc_msgSend$serverWithClient:profile:error:
+ _objc_msgSend$set
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setDatabaseIdentifier:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setHardwareIdentifier:
+ _objc_msgSend$setInstanceDiscriminator:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setKeyedDatas:
+ _objc_msgSend$setKeyedDates:
+ _objc_msgSend$setKeyedNumbers:
+ _objc_msgSend$setKeyedStrings:
+ _objc_msgSend$setListener:
+ _objc_msgSend$setNumber:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setObjectModificationDate:
+ _objc_msgSend$setObjectModificationTimeSinceReferenceDate:
+ _objc_msgSend$setObjectState:
+ _objc_msgSend$setOurData:
+ _objc_msgSend$setPersistedData:
+ _objc_msgSend$setPersistedProtoData:
+ _objc_msgSend$setProfile:
+ _objc_msgSend$setString:
+ _objc_msgSend$setTimeSinceReferenceDate:
+ _objc_msgSend$setType:
+ _objc_msgSend$setUuid:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$sharedBehavior
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$stringProperties
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$syncIdentity
+ _objc_msgSend$syncIdentityManager
+ _objc_msgSend$syncProvenance
+ _objc_msgSend$tableName
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$type
+ _objc_msgSend$unprotectedDatabase
+ _objc_msgSend$uuid
+ _objc_msgSend$version
+ _objc_msgSend$zeroObjectModificationDate
+ _objc_retainAutoreleasedReturnValue
+ columnDefinitionsWithCount:.columnDefinitions
+ sharedInstance.onceToken
+ sharedInstance.shared
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- radr://5614542
CStrings:
+ "invalidateAndWait"
- "nextSyncAnchorWithSession:predicate:startSyncAnchor:profile:error:"
- "q48@0:8@\"NSArray\"16@\"<HDSyncStore>\"24@\"HDProfile\"32^@40"
- "q48@0:8@16@24@32^@40"
- "q56@0:8@\"HDSyncSession\"16@\"HDSQLitePredicate\"24q32@\"HDProfile\"40^@48"
- "q56@0:8@16@24q32@40^@48"
- "receiveSyncObjects:syncStore:profile:error:"

```
