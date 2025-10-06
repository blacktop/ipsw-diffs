## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

```diff

-1519.0.0.0.0
-  __TEXT.__text: 0x2b8918
-  __TEXT.__auth_stubs: 0x2650
-  __TEXT.__objc_methlist: 0xfac8
-  __TEXT.__const: 0x15a8
-  __TEXT.__cstring: 0x36dc0
+1522.1.0.0.0
+  __TEXT.__text: 0x2baaac
+  __TEXT.__auth_stubs: 0x2660
+  __TEXT.__objc_methlist: 0xfc38
+  __TEXT.__const: 0x15f8
+  __TEXT.__cstring: 0x37369
   __TEXT.__swift5_typeref: 0x526
   __TEXT.__swift5_capture: 0x25c
   __TEXT.__constg_swiftt: 0x440

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x1796c
-  __TEXT.__oslogstring: 0x32b06
-  __TEXT.__unwind_info: 0x6a70
+  __TEXT.__gcc_except_tab: 0x17acc
+  __TEXT.__oslogstring: 0x32f64
+  __TEXT.__unwind_info: 0x6b08
   __TEXT.__eh_frame: 0x808
-  __TEXT.__objc_classname: 0x3441
-  __TEXT.__objc_methname: 0x1b532
-  __TEXT.__objc_methtype: 0x462f
-  __TEXT.__objc_stubs: 0x12b80
+  __TEXT.__objc_classname: 0x346f
+  __TEXT.__objc_methname: 0x1b9a2
+  __TEXT.__objc_methtype: 0x46c4
+  __TEXT.__objc_stubs: 0x12d40
   __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x45e8
-  __DATA_CONST.__objc_classlist: 0xe30
+  __DATA_CONST.__const: 0x4738
+  __DATA_CONST.__objc_classlist: 0xe38
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cb8
+  __DATA_CONST.__objc_selrefs: 0x5d50
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xb50
+  __DATA_CONST.__objc_superrefs: 0xb58
   __DATA_CONST.__objc_arraydata: 0x70f8
-  __AUTH_CONST.__auth_got: 0x1338
+  __AUTH_CONST.__auth_got: 0x1340
   __AUTH_CONST.__const: 0x1990
-  __AUTH_CONST.__cfstring: 0x1e100
-  __AUTH_CONST.__objc_const: 0x23fe0
+  __AUTH_CONST.__cfstring: 0x1e3e0
+  __AUTH_CONST.__objc_const: 0x24260
   __AUTH_CONST.__objc_dictobj: 0x20d0
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_arrayobj: 0x7980
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2e88
+  __AUTH.__objc_data: 0x2e38
   __AUTH.__data: 0x150
-  __DATA.__objc_ivar: 0x1724
-  __DATA.__data: 0x1069
-  __DATA.__bss: 0xe30
+  __DATA.__objc_ivar: 0x1744
+  __DATA.__data: 0x10c9
+  __DATA.__bss: 0xe29
   __DATA.__common: 0x5b8
   __DATA_DIRTY.__objc_ivar: 0x540
-  __DATA_DIRTY.__objc_data: 0x60b0
+  __DATA_DIRTY.__objc_data: 0x6150
   __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x630
+  __DATA_DIRTY.__bss: 0x638
   __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6AE856F6-976B-3665-B59A-30ADE7CAA991
-  Functions: 8210
-  Symbols:   26383
-  CStrings:  17413
+  UUID: C62DC177-9190-3F50-91D7-D8239B0D4B99
+  Functions: 8249
+  Symbols:   26517
+  CStrings:  17522
 
Symbols:
+ +[NSPersistentCloudKitContainerActivityVoucher qosClassForQualityOfService:]
+ +[NSPersistentCloudKitContainerActivityVoucher stringForQoSClass:]
+ +[PFCKAccountMonitor canEnableSyncWithAccountInfo:requireDeviceToDeviceEncryption:]
+ +[PFCKAccountMonitor shouldNotifyForChangeFromAccountInfo:toAccountInfo:requireDeviceToDeviceEncryption:]
+ -[NSCloudKitMirroringDelegate accountMonitorAccountChanged:]
+ -[NSCloudKitMirroringDelegate accountMonitor]
+ -[NSCloudKitMirroringDelegate qosClassForAccountMonitor:]
+ -[PFCKAccountMonitor .cxx_destruct]
+ -[PFCKAccountMonitor _assertContainer:]
+ -[PFCKAccountMonitor accountOrIdentityChanged:]
+ -[PFCKAccountMonitor beginMonitoringNotifications]
+ -[PFCKAccountMonitor clearEstablishedAccountInfoAndUserRecordID]
+ -[PFCKAccountMonitor container]
+ -[PFCKAccountMonitor currentAccountInfo]
+ -[PFCKAccountMonitor currentUserRecordID]
+ -[PFCKAccountMonitor dealloc]
+ -[PFCKAccountMonitor delegate]
+ -[PFCKAccountMonitor establishCurrentAccountInfoWithCompletionHandler:]
+ -[PFCKAccountMonitor establishCurrentUserRecordIDWithCompletionHandler:]
+ -[PFCKAccountMonitor initWithOptions:forStoreWithIdentifier:]
+ -[PFCKAccountMonitor observingNotifications]
+ -[PFCKAccountMonitor options]
+ -[PFCKAccountMonitor performBlockAtPreferredQoS:]
+ -[PFCKAccountMonitor registeredForAccountChangeNotifications]
+ -[PFCKAccountMonitor registeredForIdentityUpdateNotifications]
+ -[PFCKAccountMonitor setContainer:]
+ -[PFCKAccountMonitor setDelegate:]
+ -[PFCKAccountMonitor stopMonitoringNotifications]
+ -[PFCKAccountMonitor storeIdentifier]
+ -[PFCloudKitSetupAssistant accountMonitor]
+ -[PFCloudKitSetupAssistant initWithSetupRequest:mirroringOptions:accountMonitor:observedStore:]
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table70
+ _.str.1068
+ _.str.360
+ _.str.361
+ _.str.565
+ _.str.78
+ _OBJC_CLASS_$_PFCKAccountMonitor
+ _OBJC_IVAR_$_NSCachedFetchRequestInfo._isIneligibleForCaching
+ _OBJC_IVAR_$_NSCloudKitMirroringDelegate._accountMonitor
+ _OBJC_IVAR_$_PFCKAccountMonitor._container
+ _OBJC_IVAR_$_PFCKAccountMonitor._currentAccountInfo
+ _OBJC_IVAR_$_PFCKAccountMonitor._currentUserRecordID
+ _OBJC_IVAR_$_PFCKAccountMonitor._delegate
+ _OBJC_IVAR_$_PFCKAccountMonitor._observingNotifications
+ _OBJC_IVAR_$_PFCKAccountMonitor._options
+ _OBJC_IVAR_$_PFCKAccountMonitor._registeredForAccountChangeNotifications
+ _OBJC_IVAR_$_PFCKAccountMonitor._registeredForIdentityUpdateNotifications
+ _OBJC_IVAR_$_PFCKAccountMonitor._storeIdentifier
+ _OBJC_IVAR_$_PFCloudKitSetupAssistant._accountMonitor
+ _OBJC_METACLASS_$_PFCKAccountMonitor
+ _PFCKAccountMonitorAccountChangedNotificationName
+ _PFCKAccountMonitorAccountChangedNotificationNameKey
+ __OBJC_$_CLASS_METHODS_PFCKAccountMonitor
+ __OBJC_$_INSTANCE_METHODS_PFCKAccountMonitor
+ __OBJC_$_INSTANCE_VARIABLES_PFCKAccountMonitor
+ __OBJC_$_PROP_LIST_PFCKAccountMonitor
+ __OBJC_$_PROP_LIST_PFCloudKitSetupAssistant
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PFCKAccountMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PFCKAccountMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_PFCKAccountMonitorDelegate
+ __OBJC_CLASS_RO_$_PFCKAccountMonitor
+ __OBJC_LABEL_PROTOCOL_$_PFCKAccountMonitorDelegate
+ __OBJC_METACLASS_RO_$_PFCKAccountMonitor
+ __OBJC_PROTOCOL_$_PFCKAccountMonitorDelegate
+ ___108-[NSCloudKitMirroringDelegate _markZonesNeedingRecoveryFromManateeIdentityLoss:databaseScope:inStore:error:]_block_invoke.487
+ ___125-[NSCloudKitMirroringDelegate checkAndScheduleImportIfNecessaryFromPush:fromErrorRecovery:fromShareAccept:andStartAfterDate:]_block_invoke.444
+ ___47-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke.259
+ ___47-[PFCKAccountMonitor accountOrIdentityChanged:]_block_invoke
+ ___47-[PFCKAccountMonitor accountOrIdentityChanged:]_block_invoke_2
+ ___49-[PFCKAccountMonitor performBlockAtPreferredQoS:]_block_invoke
+ ___52-[NSCloudKitMirroringDelegate _performSetupRequest:]_block_invoke.274
+ ___52-[NSCloudKitMirroringDelegate _performSetupRequest:]_block_invoke.276
+ ___52-[NSCloudKitMirroringDelegate _persistUpdatedShare:]_block_invoke.513
+ ___56-[NSCloudKitMirroringDelegate _beginWatchingForChanges:]_block_invoke.208
+ ___56-[NSCloudKitMirroringDelegate _deleteShareWithRecordID:]_block_invoke.514
+ ___56-[NSCloudKitMirroringDelegate _deleteShareWithRecordID:]_block_invoke.516
+ ___56-[NSCloudKitMirroringDelegate _performResetZoneRequest:]_block_invoke.323
+ ___56-[NSCloudKitMirroringDelegate _performResetZoneRequest:]_block_invoke_2.324
+ ___57-[NSCloudKitMirroringDelegate _performExportWithRequest:]_block_invoke.314
+ ___60-[NSCloudKitMirroringDelegate _performMetadataResetRequest:]_block_invoke.344
+ ___64-[NSSQLiteConnection writeCorrelationMasterReordersFromTracker:]_block_invoke.387
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.496
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.503
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.555
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.557
+ ___67-[NSCloudKitMirroringDelegate _performSchemaInitializationRequest:]_block_invoke.497
+ ___69-[NSCloudKitMirroringDelegate _performAcceptShareInvitationsRequest:]_block_invoke.381
+ ___71-[PFCKAccountMonitor establishCurrentAccountInfoWithCompletionHandler:]_block_invoke
+ ___71-[PFCKAccountMonitor establishCurrentAccountInfoWithCompletionHandler:]_block_invoke.27
+ ___72-[PFCKAccountMonitor establishCurrentUserRecordIDWithCompletionHandler:]_block_invoke
+ ___72-[PFCKAccountMonitor establishCurrentUserRecordIDWithCompletionHandler:]_block_invoke.30
+ ___75-[PFCKAccountMonitor finishedAccountInfoFetchWith:error:completionHandler:]_block_invoke
+ ___75-[PFCKAccountMonitor finishedAccountInfoFetchWith:error:completionHandler:]_block_invoke_2
+ ___76-[PFCKAccountMonitor _fetchAccountInfoAndUserRecordIDWithCompletionHandler:]_block_invoke
+ ___76-[PFCKAccountMonitor _fetchAccountInfoAndUserRecordIDWithCompletionHandler:]_block_invoke_2
+ ___79-[NSCloudKitMirroringDelegate _acceptShareMetadatasInRequest:workBlockContext:]_block_invoke.393
+ ___79-[NSCloudKitMirroringDelegate _createSchemaForStore:withMonitor:options:error:]_block_invoke.505
+ ___83-[NSCloudKitMirroringDelegate observeChangesForStore:inPersistentStoreCoordinator:]_block_invoke.179
+ ___83-[NSCloudKitMirroringDelegate observeChangesForStore:inPersistentStoreCoordinator:]_block_invoke.186
+ ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.414
+ ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.430
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32b40w_e32_v24?0"CKRecordID"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32b40w_e35_v24?0"CKAccountInfo"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0I8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e8_v12?0I8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40w_e50_v32?0"CKAccountInfo"8"CKRecordID"16"NSError"24lw40l8s32l8
+ ___block_descriptor_56_e8_32o40b48w_e32_v24?0"CKRecordID"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e8_v12?0I8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48o56o_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.363
+ ___block_literal_global.423
+ _dispatch_block_create_with_qos_class
+ _objc_msgSend$accountMonitor
+ _objc_msgSend$beginMonitoringNotifications
+ _objc_msgSend$canEnableSyncWithAccountInfo:requireDeviceToDeviceEncryption:
+ _objc_msgSend$clearEstablishedAccountInfoAndUserRecordID
+ _objc_msgSend$currentAccountInfo
+ _objc_msgSend$currentUserRecordID
+ _objc_msgSend$establishCurrentAccountInfoWithCompletionHandler:
+ _objc_msgSend$establishCurrentUserRecordIDWithCompletionHandler:
+ _objc_msgSend$initWithOptions:forStoreWithIdentifier:
+ _objc_msgSend$initWithSetupRequest:mirroringOptions:accountMonitor:observedStore:
+ _objc_msgSend$qosClassForAccountMonitor:
+ _objc_msgSend$qosClassForQualityOfService:
+ _objc_msgSend$shouldNotifyForChangeFromAccountInfo:toAccountInfo:requireDeviceToDeviceEncryption:
+ _objc_msgSend$stopMonitoringNotifications
+ _objc_msgSend$stringForQoSClass:
- -[NSCloudKitMirroringDelegate ckAccountOrIdentityChangedHandler:]
- -[PFCloudKitSetupAssistant initWithSetupRequest:mirroringOptions:observedStore:]
- GCC_except_table122
- GCC_except_table84
- _.str.1065
- _.str.351
- _.str.352
- _.str.556
- _.str.74
- _OBJC_IVAR_$_NSCloudKitMirroringDelegate._accountChangeObserver
- _OBJC_IVAR_$_NSCloudKitMirroringDelegate._currentUserRecordID
- _OBJC_IVAR_$_NSCloudKitMirroringDelegate._registeredForIdentityUpdateNotifications
- _OBJC_IVAR_$_PFCloudKitSetupAssistant._currentUserRecordID
- ___108-[NSCloudKitMirroringDelegate _markZonesNeedingRecoveryFromManateeIdentityLoss:databaseScope:inStore:error:]_block_invoke.491
- ___125-[NSCloudKitMirroringDelegate checkAndScheduleImportIfNecessaryFromPush:fromErrorRecovery:fromShareAccept:andStartAfterDate:]_block_invoke.448
- ___47-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke.263
- ___47-[NSCloudKitMirroringDelegate initWithOptions:]_block_invoke_2
- ___52-[NSCloudKitMirroringDelegate _performSetupRequest:]_block_invoke.278
- ___52-[NSCloudKitMirroringDelegate _performSetupRequest:]_block_invoke.280
- ___52-[NSCloudKitMirroringDelegate _persistUpdatedShare:]_block_invoke.517
- ___56-[NSCloudKitMirroringDelegate _beginWatchingForChanges:]_block_invoke.212
- ___56-[NSCloudKitMirroringDelegate _deleteShareWithRecordID:]_block_invoke.518
- ___56-[NSCloudKitMirroringDelegate _deleteShareWithRecordID:]_block_invoke.520
- ___56-[NSCloudKitMirroringDelegate _performResetZoneRequest:]_block_invoke.327
- ___56-[NSCloudKitMirroringDelegate _performResetZoneRequest:]_block_invoke_2.328
- ___57-[NSCloudKitMirroringDelegate _performExportWithRequest:]_block_invoke.318
- ___60-[NSCloudKitMirroringDelegate _performMetadataResetRequest:]_block_invoke.348
- ___64-[NSSQLiteConnection writeCorrelationMasterReordersFromTracker:]_block_invoke.384
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.487
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.494
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.546
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.548
- ___67-[NSCloudKitMirroringDelegate _performSchemaInitializationRequest:]_block_invoke.501
- ___69-[NSCloudKitMirroringDelegate _performAcceptShareInvitationsRequest:]_block_invoke.385
- ___79-[NSCloudKitMirroringDelegate _acceptShareMetadatasInRequest:workBlockContext:]_block_invoke.397
- ___79-[NSCloudKitMirroringDelegate _createSchemaForStore:withMonitor:options:error:]_block_invoke.509
- ___83-[NSCloudKitMirroringDelegate observeChangesForStore:inPersistentStoreCoordinator:]_block_invoke.183
- ___83-[NSCloudKitMirroringDelegate observeChangesForStore:inPersistentStoreCoordinator:]_block_invoke.190
- ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.405
- ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.412
- ___block_descriptor_72_e8_32o40o48o56o64o_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.354
- ___block_literal_global.414
- _objc_msgSend$initWithSetupRequest:mirroringOptions:observedStore:
CStrings:
+ "-[PFCKAccountMonitor _finishedAccountInfoFetchFromNotificationNamed:withAccountInfo:userRecordID:error:]"
+ "-[PFCKAccountMonitor accountOrIdentityChanged:]"
+ "-[PFCKAccountMonitor clearEstablishedAccountInfoAndUserRecordID]"
+ "-[PFCKAccountMonitor establishCurrentAccountInfoWithCompletionHandler:]_block_invoke"
+ "-[PFCKAccountMonitor establishCurrentUserRecordIDWithCompletionHandler:]_block_invoke"
+ "-[PFCKAccountMonitor finishedAccountInfoFetchWith:error:completionHandler:]"
+ "-[PFCKAccountMonitor finishedAccountInfoFetchWith:error:completionHandler:]_block_invoke_2"
+ "@\"CKAccountInfo\""
+ "@\"NSObject<PFCKAccountMonitorDelegate>\""
+ "@\"PFCKAccountMonitor\""
+ "B36@0:8@16@24B32"
+ "CoreData+CloudKit: %s(%d): %@ for store %@ '%@' failed with error: %@"
+ "CoreData+CloudKit: %s(%d): %@ for store %@ clearing established account info.\n\t%@\n\t%@"
+ "CoreData+CloudKit: %s(%d): %@ for store %@ establishing current account info at '%@'."
+ "CoreData+CloudKit: %s(%d): %@ for store %@ establishing current user recordID at '%@'."
+ "CoreData+CloudKit: %s(%d): %@ for store %@ ignoring account change for the transition from:\n\t%@\n\t%@\nTo:\n\t%@\n\t%@\n\t%@"
+ "CoreData+CloudKit: %s(%d): %@ for store %@ observed '%@'."
+ "CoreData+CloudKit: %s(%d): %@ for store %@ posting '%@' for the transition from:\n\t%@\n\t%@\nTo:\n\t%@\n\t%@\n\t%@"
+ "CoreData: %@ can't execute '%@' without a container."
+ "CoreData: Illegal account change notification (missing the name of the notification that triggered it): %@"
+ "CoreData: Initializing query generations"
+ "CoreData: Unknown quality of service: %ld"
+ "CoreData: What qos class is this? %u"
+ "CoreData: fault: %@ can't execute '%@' without a container.\n"
+ "CoreData: fault: Illegal account change notification (missing the name of the notification that triggered it): %@\n"
+ "CoreData: fault: Unknown quality of service: %ld\n"
+ "CoreData: fault: What qos class is this? %u\n"
+ "I24@0:8@\"PFCKAccountMonitor\"16"
+ "I24@0:8@16"
+ "I24@0:8q16"
+ "Incompatible metadata after migration because the store version hashes didn't migrate."
+ "Maintenance"
+ "NSKeyedUnarchiveFromData"
+ "NSSecureUnarchiveFromData"
+ "NSUnarchiveFromData"
+ "PFCKAccountMonitor"
+ "PFCKAccountMonitorAccountChangedNotificationEncounteredError"
+ "PFCKAccountMonitorAccountChangedNotificationFromAccountInfoKey"
+ "PFCKAccountMonitorAccountChangedNotificationFromUserRecordIDKey"
+ "PFCKAccountMonitorAccountChangedNotificationName"
+ "PFCKAccountMonitorAccountChangedNotificationNameKey"
+ "PFCKAccountMonitorAccountChangedNotificationToAccountInfoKey"
+ "PFCKAccountMonitorAccountChangedNotificationToUserRecordIDKey"
+ "PFCKAccountMonitorDelegate"
+ "QOS_CLASS_BACKGROUND"
+ "QOS_CLASS_DEFAULT"
+ "QOS_CLASS_MAINTENANCE"
+ "QOS_CLASS_UNSPECIFIED"
+ "QOS_CLASS_USER_INITIATED"
+ "QOS_CLASS_USER_INTERACTIVE"
+ "QOS_CLASS_UTILITY"
+ "T@\"CKAccountInfo\",R,V_currentAccountInfo"
+ "T@\"CKRecordID\",R,V_currentUserRecordID"
+ "T@\"NSCloudKitMirroringDelegateOptions\",R,N,V_options"
+ "T@\"NSObject<PFCKAccountMonitorDelegate>\",W,N,V_delegate"
+ "T@\"PFCKAccountMonitor\",R,N,V_accountMonitor"
+ "TB,R,N,V_observingNotifications"
+ "TB,R,N,V_registeredForAccountChangeNotifications"
+ "TB,R,N,V_registeredForIdentityUpdateNotifications"
+ "Unknown QOS Class"
+ "_accountMonitor"
+ "_currentAccountInfo"
+ "_fetchAccountInfoAndUserRecordIDWithCompletionHandler:"
+ "_isIneligibleForCaching"
+ "_observingNotifications"
+ "accountMonitor"
+ "accountMonitorAccountChanged:"
+ "accountOrIdentityChanged:"
+ "beginMonitoringNotifications"
+ "canEnableSyncWithAccountInfo:requireDeviceToDeviceEncryption:"
+ "clearEstablishedAccountInfoAndUserRecordID"
+ "currentAccountInfo"
+ "currentUserRecordID"
+ "destination checksum"
+ "establishCurrentAccountInfoWithCompletionHandler:"
+ "establishCurrentUserRecordIDWithCompletionHandler:"
+ "initWithOptions:forStoreWithIdentifier:"
+ "initWithSetupRequest:mirroringOptions:accountMonitor:observedStore:"
+ "observingNotifications"
+ "qosClassForAccountMonitor:"
+ "qosClassForQualityOfService:"
+ "registeredForAccountChangeNotifications"
+ "registeredForIdentityUpdateNotifications"
+ "shouldNotifyForChangeFromAccountInfo:toAccountInfo:requireDeviceToDeviceEncryption:"
+ "source checksum"
+ "sqlIneligibleForCaching"
+ "stopMonitoringNotifications"
+ "stringForQoSClass:"
+ "v12@?0I8"
+ "v32@?0@\"CKAccountInfo\"8@\"CKRecordID\"16@\"NSError\"24"
+ "\xd2"
- "AccountChangeObserver"
- "_accountChangeObserver"
- "ckAccountOrIdentityChangedHandler:"
- "initWithSetupRequest:mirroringOptions:observedStore:"
- "\xe2"

```
