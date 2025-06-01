## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-123.2.8.0.0
-  __TEXT.__text: 0x3f234
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x71e0
-  __TEXT.__objc_methlist: 0x3274
-  __TEXT.__const: 0xfe0
-  __TEXT.__objc_methname: 0x8df1
-  __TEXT.__oslogstring: 0x4af4
-  __TEXT.__cstring: 0x42db
-  __TEXT.__objc_classname: 0x6c6
-  __TEXT.__objc_methtype: 0x1560
-  __TEXT.__gcc_except_tab: 0x5f0
+123.5.23.1.0
+  __TEXT.__text: 0x40ba8
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_stubs: 0x7300
+  __TEXT.__objc_methlist: 0x3314
+  __TEXT.__const: 0x1038
+  __TEXT.__objc_methname: 0x907b
+  __TEXT.__oslogstring: 0x4e3e
+  __TEXT.__cstring: 0x45d5
+  __TEXT.__objc_classname: 0x6f3
+  __TEXT.__objc_methtype: 0x1602
+  __TEXT.__gcc_except_tab: 0x6bc
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0xe34
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0xdb8
-  __DATA_CONST.__cfstring: 0x38a0
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__unwind_info: 0xe5c
+  __DATA_CONST.__auth_got: 0x688
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0xdf8
+  __DATA_CONST.__cfstring: 0x3aa0
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__objc_arrayobj: 0x6d8
-  __DATA_CONST.__objc_intobj: 0x1c8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x4a8
+  __DATA_CONST.__objc_arrayobj: 0x708
+  __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x6120
-  __DATA.__objc_selrefs: 0x2308
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3b8
-  __DATA.__objc_superrefs: 0x188
-  __DATA.__objc_ivar: 0x36c
-  __DATA.__objc_data: 0x1040
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0xd8
+  __DATA.__objc_const: 0x62d8
+  __DATA.__objc_selrefs: 0x2368
+  __DATA.__objc_ivar: 0x380
+  __DATA.__objc_data: 0x1090
+  __DATA.__data: 0x600
+  __DATA.__bss: 0xe0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
+  - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: ED24FD07-7EC7-3DC3-A17C-5509C6549198
-  Functions: 1424
-  Symbols:   327
-  CStrings:  3151
+  UUID: 1A31AF87-5930-3439-86CD-EBCF7C91CB57
+  Functions: 1456
+  Symbols:   330
+  CStrings:  3222
 
Symbols:
+ _OBJC_CLASS_$_BMAccount
+ _OBJC_CLASS_$_GDXPCCoordinationService
+ _RPOptionStatusFlags
+ __os_feature_enabled_impl
- _OBJC_CLASS_$_BMStoreConfig
CStrings:
+ "\x01\x13\x13"
+ "\x01\x16"
+ "\x02!\x11"
+ "%@:remotes:%@"
+ "-shm"
+ "@\"<BMSyncChangeReporter>\""
+ "@\"BMAccount\""
+ "@\"GDXPCCoordinationService\""
+ "@40@0:8@16Q24@32"
+ "App.InFocus"
+ "B40@0:8@\"NSString\"16@\"NSString\"24^@32"
+ "BMCoordinationXPCSyncEventReporter: stream %@: failed to notify coordination service of changes: %@"
+ "BMCoordinationXPCSyncEventReporter: stream %@: failed to notify coordination service of user deletions: %@"
+ "BMRapportManager: discovery client already exists"
+ "BMRapportSyncEngine%@: Attempting to use discovered devices cache to identify account for %@"
+ "BMRapportSyncEngine%@: createDistributedSyncManagerFromOptions unable to determine sender account info: %@"
+ "BMRapportSyncEngine%@: fetchAtomBatchRequest is nil, skip sending request to device: %@"
+ "BMRapportSyncEngine%@: rejecting request from communal device to sync outside home %@"
+ "BMRapportSyncEngine%@: unable to create a sync manager for account %@"
+ "BMRapportSyncEngine%@: unable to create sync manager for %{public}@"
+ "BMRappowrtSyncEngine%@: rejecting request from personal device to sync cross account %@"
+ "BMSyncChangeReporter"
+ "BMXPCSyncChangeReporter"
+ "Biome"
+ "CREATE INDEX IF NOT EXISTS idx_syncsessionlog_start_timestamp ON SyncSessionLog(start_timestamp DESC)"
+ "Creation"
+ "Cross account"
+ "DELETE FROM AtomMergedLog WHERE session_id NOT IN (SELECT session_id from SyncSessionLog)"
+ "DELETE FROM SyncMessageLog"
+ "DELETE FROM SyncMessageLog WHERE session_id NOT IN (SELECT session_id from SyncSessionLog)"
+ "DELETE FROM SyncSessionLog WHERE session_id NOT IN (SELECT session_id from SyncSessionLog ORDER BY start_timestamp DESC LIMIT 1000)"
+ "Effective database for stream %{public}@ not available for current request"
+ "Failed to create sync manager"
+ "Messages.SharedWithYou.Feedback"
+ "MultiUserDeviceSync"
+ "Outside home"
+ "SharedSyncGeneration"
+ "T@\"BMAccount\",R,N"
+ "T@\"BMDistributedSyncMultiStreamManager\",&,N,V_primaryUserSyncStreamManager"
+ "T@\"BMSyncDatabase\",&,N,V_primaryDatabase"
+ "T@\"BMSyncDatabase\",R,N,V_primaryDatabase"
+ "T@\"NSMutableDictionary\",&,N,V_registeredRequestOptions"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",&,N"
+ "_account"
+ "_accountDatabase"
+ "_changeReporter"
+ "_coordinationService"
+ "_options"
+ "_primaryDatabase"
+ "_primarySyncManager"
+ "_primaryUserSyncStreamManager"
+ "_registeredRequestOptions"
+ "account"
+ "accountAltDSID"
+ "accountFromRapportOptions:"
+ "bookmark is nil, presumably because the referenced atom was a placeholder append (dead on arrival) %@"
+ "computeAggregatedSessionLogsWithHandlerBlock:"
+ "copyWithRemoteName:"
+ "createDatabaseForAccount:queue:"
+ "createDistributedSyncManagerForAccount:"
+ "createPrimaryDatabaseWithQueue:"
+ "defaultStore"
+ "enforceMaxSessionLogPrunePolicy"
+ "failed to create path at: %@, reason: %@"
+ "failed to delete corrupt database SHM file: %@"
+ "failed to delete corrupt database WAL file: %@"
+ "failed to delete remotes for stream %@ BM Account %@: %@"
+ "finishRequest:toDevice:withError:peerInfo:peerStatusTracker:"
+ "getBytes:length:"
+ "getUUIDBytes:"
+ "initWithAccountIdentifier:"
+ "initWithDistributedSyncManagers:peerStatusTracker:accountDatabase:"
+ "initWithPath:options:queue:"
+ "initWithQueue:primarySyncManager:primaryDatabase:"
+ "initWithQueue:primarySyncManager:rapportManager:atomBatchChunkerPolicy:primaryDatabase:"
+ "initWithStreamConfiguration:locationAssignerPolicy:localSiteIdentifier:database:changeReporter:account:"
+ "initWithStreamConfiguration:streamCRDT:database:localSiteIdentifier:changeReporter:"
+ "initWithUUIDBytes:"
+ "multiStreamManagerWithPrimaryDatabase:account:queue:"
+ "pathForSharedSyncWithAccount:domain:"
+ "pathForSharedSyncWithAccount:streamType:domain:"
+ "populateAtomBatch missing event for bookmark %@, adding a placeholder append"
+ "primaryDatabase"
+ "primaryDatabasePath"
+ "primaryDatabaseWALPath"
+ "primaryUserSyncStreamManager"
+ "registerRequestID:options:requestHandler:"
+ "registeredRequestOptions"
+ "remoteDevicesForAccount:reply:"
+ "remoteName"
+ "senderAccountAltDSID"
+ "setPrimaryDatabase:"
+ "setPrimaryUserSyncStreamManager:"
+ "setRegisteredRequestOptions:"
+ "setSharedSyncGeneration:"
+ "sharedSyncGeneration"
+ "streamRemoteIdentifierForStreamName:deviceIdentifier:"
+ "streamUpdatedForStreamName:deviceIdentifier:error:"
+ "streamUpdatedWithStreamName:isDelete:error:"
+ "userDeletesForStreamName:deviceIdentifier:error:"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@0:8@\"BMAccount\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v56@0:8@16@24@32@40@48"
- "\x01\x12\x11\x12"
- "\x01\x17"
- "\x02\x11\x11"
- "\b"
- "@28@0:8@16B24"
- "BMRapportManager: createSharedDiscoveryClientIfNotExists not currently supported"
- "BMRapportManager: registerEventID %@"
- "BMRapportManager: shared discovery client already exists"
- "BMRapportManager: shared-use only supported internally"
- "BMSyncMetadata"
- "T@\"BMDistributedSyncMultiStreamManager\",&,N,V_distributedSyncMultiStreamManager"
- "T@\"BMSyncDatabase\",&,N,V_defaultDatabase"
- "T@\"BMSyncDatabase\",R,N,V_database"
- "T@\"NSDictionary\",&,N,V_sharedSyncDatabases"
- "_defaultDatabase"
- "_distributedSyncMultiStreamManager"
- "_sharedSyncDatabases"
- "_sharedUse"
- "a"
- "bm_accountIds"
- "bookmark is nil, presumably because the referenced atom was a dummy append (dead on arrival) %@"
- "computeAggregatedSessionLogs"
- "createSharedDiscoveryClientIfNotExists"
- "defaultDatabase"
- "defaultDatabasePath"
- "defaultDatabaseWALPath"
- "distributedSyncMultiStreamManager"
- "distributedSyncMultiStreamManagerWithDatabase:"
- "failed to create path: %@"
- "finishRequest:toDevice:withError:peerInfo:"
- "initWithDistributedSyncManagers:peerStatusTracker:"
- "initWithQueue:forSharedUse:"
- "initWithQueue:multiStreamManager:rapportManager:atomBatchChunkerPolicy:database:"
- "initWithStoreBasePath:segmentSize:"
- "initWithStreamConfiguration:locationAssignerPolicy:localSiteIdentifier:database:"
- "initWithStreamConfiguration:streamCRDT:database:localSiteIdentifier:"
- "localDeviceUpdatingIfNecessary"
- "pathForSharedSyncUserIdentifier:streamType:domain:"
- "registerEventID:eventHandler:"
- "registerEventID:options:handler:"
- "registerRequestID:requestHandler:"
- "remoteDevicesWithReply:"
- "remoteStreamName"
- "segmentSize"
- "setDefaultDatabase:"
- "setDistributedSyncMultiStreamManager:"
- "setRemoteStreamName:"
- "setSharedSyncDatabases:"
- "setStoreLocationOption:"
- "sharedSyncDatabases"
- "v48@0:8@16@24@32@40"

```
