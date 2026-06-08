## ReplicatorCore

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore`

```diff

-126.5.4.0.0
-  __TEXT.__text: 0x7a880
-  __TEXT.__auth_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0x628
-  __TEXT.__const: 0xea0
-  __TEXT.__constg_swiftt: 0xd10
-  __TEXT.__swift5_typeref: 0xdf6
-  __TEXT.__swift5_reflstr: 0x67d
-  __TEXT.__swift5_fieldmd: 0x6d0
+164.0.0.0.0
+  __TEXT.__text: 0x7810c
+  __TEXT.__objc_methlist: 0x630
+  __TEXT.__const: 0xeb8
+  __TEXT.__constg_swiftt: 0xd2c
+  __TEXT.__swift5_typeref: 0xdf7
+  __TEXT.__swift5_reflstr: 0x68d
+  __TEXT.__swift5_fieldmd: 0x6ec
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x2218
-  __TEXT.__cstring: 0x95c
-  __TEXT.__swift5_capture: 0x2b8
+  __TEXT.__oslogstring: 0x2306
+  __TEXT.__cstring: 0xa16
+  __TEXT.__swift5_capture: 0x328
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_proto: 0x64
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__unwind_info: 0xcc0
-  __TEXT.__eh_frame: 0x2060
-  __TEXT.__objc_classname: 0x677
-  __TEXT.__objc_methname: 0x11a0
-  __TEXT.__objc_methtype: 0x716
-  __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x958
-  __DATA_CONST.__const: 0x90
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__unwind_info: 0xc38
+  __TEXT.__eh_frame: 0x1e68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x70
-  __AUTH_CONST.__auth_got: 0x16b8
-  __AUTH_CONST.__const: 0xe68
-  __AUTH_CONST.__objc_const: 0x1ac0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xff8
+  __AUTH_CONST.__objc_const: 0x1ae8
+  __AUTH_CONST.__auth_got: 0x18e8
   __AUTH.__objc_data: 0x168
   __AUTH.__data: 0x100
-  __DATA.__data: 0x7e8
+  __DATA.__data: 0x730
   __DATA.__bss: 0x380
-  __DATA.__common: 0x18
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x758
-  __DATA_DIRTY.__data: 0x1328
+  __DATA_DIRTY.__data: 0x13a0
   __DATA_DIRTY.__bss: 0x380
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Combine.framework/Combine
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
-  - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
+  - /System/Library/PrivateFrameworks/ReplicatorDependencies.framework/ReplicatorDependencies
   - /System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine
   - /System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6789A8C7-9F53-39DA-8462-42DCD2D0992C
-  Functions: 894
-  Symbols:   810
-  CStrings:  471
+  UUID: 06BAE5EE-B952-3F19-8C7E-A6D448D70A2F
+  Functions: 888
+  Symbols:   953
+  CStrings:  222
 
Symbols:
+ _DMIsMigrationNeeded
+ _DMPerformMigrationIfNeeded
+ _OBJC_CLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_CLASS_$_NSUserDefaults
+ ___swift__destructor
+ ___swift__destructor.55
+ ___swift__destructor.74
+ ___swift__destructor.77
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_allocate_boxed_opaque_existential_1Tm
+ ___swift_assign_boxed_opaque_existential_0
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.11Tm
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.49
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.53
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.65
+ ___swift_closure_destructor.68
+ ___swift_closure_destructor.72
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.80
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.91
+ ___swift_closure_destructorTm
+ ___swift_project_boxed_opaque_existential_1Tm
+ _block_copy_helper.11
+ _block_copy_helper.14
+ _block_copy_helper.25
+ _block_copy_helper.3
+ _block_copy_helper.32
+ _block_copy_helper.45
+ _block_copy_helper.51
+ _block_copy_helper.67
+ _block_copy_helper.86
+ _block_copy_helper.93
+ _block_copy_helper.96
+ _block_descriptor.13
+ _block_descriptor.16
+ _block_descriptor.27
+ _block_descriptor.34
+ _block_descriptor.47
+ _block_descriptor.5
+ _block_descriptor.53
+ _block_descriptor.69
+ _block_descriptor.88
+ _block_descriptor.95
+ _block_descriptor.98
+ _block_destroy_helper.12
+ _block_destroy_helper.15
+ _block_destroy_helper.26
+ _block_destroy_helper.33
+ _block_destroy_helper.4
+ _block_destroy_helper.46
+ _block_destroy_helper.52
+ _block_destroy_helper.68
+ _block_destroy_helper.87
+ _block_destroy_helper.94
+ _block_destroy_helper.97
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$defaultMultiplexer
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$setMultiplexer:
+ _objc_msgSend$standardUserDefaults
+ _objc_release_x9
+ _sleep
+ _swift_release_x1
+ _swift_release_x11
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x3
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_retain_x9
+ _symbolic SDySS_____G 18ReplicatorServices16ClientDescriptorV
+ _symbolic SDy__________G 18ReplicatorServices0A6RecordV2IDV AA030ReplicationXPCServerParametersC0C
+ _symbolic Si
+ _symbolic _____ 14ReplicatorCore18SystemDataMigratorV
+ _symbolic _____ 22ReplicatorDependencies10DeviceTypeO
+ _symbolic _____Sg 22ReplicatorDependencies04TestB0V
+ _symbolic _____Sg 22ReplicatorDependencies20IDSAbstractingDeviceV
+ _symbolic ______p 16ReplicatorEngine17PersonaMonitoringP
+ _symbolic ______p 18ReplicatorServices13TestingServerP
+ _symbolic ______p 22ReplicatorDependencies14IDSAbstractingP
+ _symbolic ______pSg 14ReplicatorCore14StateCapturingP
+ _symbolic ______pSg 16ReplicatorEngine19HandshakeSchedulingP
+ _symbolic ______pSg 18ReplicatorServices13TestingServerP
+ _symbolic ______pSg 22ReplicatorDependencies24StatusKitClientProvidingP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 22ReplicatorDependencies10DeviceTypeO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 16ReplicatorEngine28HandshakeConditionMonitoringP
- _OBJC_CLASS_$_IDSDevice
- _OBJC_CLASS_$_IDSService
- ___swift_project_boxed_opaque_existential_5
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_ReplicatorCore
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_ReplicatorCore
- _block_copy_helper.100
- _block_copy_helper.109
- _block_copy_helper.113
- _block_copy_helper.23
- _block_copy_helper.33
- _block_copy_helper.4
- _block_copy_helper.41
- _block_copy_helper.47
- _block_copy_helper.65
- _block_descriptor.102
- _block_descriptor.111
- _block_descriptor.115
- _block_descriptor.25
- _block_descriptor.35
- _block_descriptor.43
- _block_descriptor.49
- _block_descriptor.6
- _block_descriptor.67
- _block_destroy_helper.101
- _block_destroy_helper.110
- _block_destroy_helper.114
- _block_destroy_helper.24
- _block_destroy_helper.34
- _block_destroy_helper.42
- _block_destroy_helper.48
- _block_destroy_helper.5
- _block_destroy_helper.66
- _objc_msgSend$initWithEndpoint:
- _objc_msgSend$initWithService:
- _objc_msgSend$nsuuid
- _objc_msgSend$pushToken
- _objc_msgSend$uniqueIDOverride
- _objectdestroy.11Tm
- _objectdestroyTm
- _swift_stdlib_isStackAllocationSafe
- _symbolic SS3key______5valuetSg 18ReplicatorServices14ZoneDescriptorV
- _symbolic SS3key______5valuetSg 18ReplicatorServices16ClientDescriptorV
- _symbolic SS_Se_SEpt
- _symbolic So10IDSServiceC
- _symbolic _____ 16ReplicatorEngine10DeviceTypeO
- _symbolic _____3key______5valuetSg 16ReplicatorEngine6RecordV2IDC AC5ValueV
- _symbolic _____3key______5valuetSg s6UInt64V 18ReplicatorServices0B6RecordV5ValueV
- _symbolic _____Sg 18ReplicatorServices0A6RecordV2IDV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 16ReplicatorEngine10DeviceTypeO
CStrings:
+ "Blocking on simulated data migration"
+ "Blocking on system data migration"
+ "Done simulating migration"
+ "ReplicationServer"
+ "Simulating migration for %{public}lds"
+ "System data migration completed in %{public}f"
+ "System data migration unnecessary"
+ "com.apple.replicatord.finishMigration"
+ "com.apple.replicatord.simulateMigration"
+ "handshakeScheduler"
+ "simulateMigration"
- "#16@0:8"
- "$__lazy_storage_$_hasUnlockedSinceBootPublisher"
- ".cxx_destruct"
- "@\"BSObjCMethod\"16@?0@\"BSObjCMethod\"8"
- "@\"NSData\"24@0:8^@16"
- "@\"NSData\"32@0:8@\"NSData\"16^@24"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8^@16"
- "@\"NSString\"32@0:8@\"NSString\"16^@24"
- "@\"_TtC18ReplicatorServices36MigrationXPCServerResponseGetRecords\"24@0:8^@16"
- "@\"_TtC18ReplicatorServices38ReplicationXPCServerResponseGetRecords\"32@0:8@\"NSData\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"NSData\"16^@24"
- "B32@0:8@\"_TtC18ReplicatorServices40ReplicationXPCServerParametersAddRecords\"16^@24"
- "B32@0:8@16^@24"
- "BSServiceConnectionCommonConfiguring"
- "BSServiceInitiatingConnectionConfiguring"
- "BSServiceListenerConnectionConfiguring"
- "IDS service has no device list"
- "NSObject"
- "OS_dispatch_source"
- "OS_dispatch_source_signal"
- "Q16@0:8"
- "ReplicatorCore"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
- "_TtC14ReplicatorCore12DataMigrator"
- "_TtC14ReplicatorCore15MigrationClient"
- "_TtC14ReplicatorCore16ClientDataSource"
- "_TtC14ReplicatorCore16StateCaptureItem"
- "_TtC14ReplicatorCore17ReplicationServer"
- "_TtC14ReplicatorCore17StateCaptureEntry"
- "_TtC14ReplicatorCore18StateCaptureServer"
- "_TtC14ReplicatorCore19StateCaptureService"
- "_TtC14ReplicatorCore21AllowedClientVerifier"
- "_TtC14ReplicatorCore23ReplicatorControlServer"
- "_TtC14ReplicatorCore23StateCaptureInvalidator"
- "_TtC14ReplicatorCore25NotifydNotificationPoster"
- "_TtC14ReplicatorCore26ClientRecordChangeNotifier"
- "_TtC14ReplicatorCore28DebouncingNotificationPoster"
- "_TtC14ReplicatorCore32FixedStateFirstLockStateProvider"
- "_TtC14ReplicatorCore34MobileKeybagFirstLockStateProvider"
- "_TtC14ReplicatorCore6Daemon"
- "_TtC14ReplicatorCoreP33_0666CD86C1D3D7360744851506CB0C776Client"
- "_TtC14ReplicatorCoreP33_586791E780FEDC6114754B28ABA431B16Client"
- "_TtP18ReplicatorServices18MigrationXPCClient_"
- "_TtP18ReplicatorServices18MigrationXPCServer_"
- "_TtP18ReplicatorServices20ReplicationXPCClient_"
- "_TtP18ReplicatorServices20ReplicationXPCServer_"
- "_TtP18ReplicatorServices21StateCaptureXPCClient_"
- "_TtP18ReplicatorServices21StateCaptureXPCServer_"
- "_TtP18ReplicatorServices26ReplicatorControlXPCClient_"
- "_TtP18ReplicatorServices26ReplicatorControlXPCServer_"
- "_hasUnlockedSinceBootPublisher"
- "_queue_hasUnlockedSinceBoot"
- "activate"
- "activateManualDomain:"
- "addIDToAllowListWithParameters:error:"
- "addRecordsWithParameters:error:"
- "all"
- "allowListAndReturnError:"
- "allowedClientVerifier"
- "autorelease"
- "bluetoothIdentifier"
- "bundleID"
- "captureHandler"
- "class"
- "clientDefinedRecordIDsWithParameters:error:"
- "clientDescriptor"
- "clientDescriptorStore"
- "clientDescriptorWithParameters:error:"
- "clientDescriptorsAndReturnError:"
- "clientIDs"
- "clientSettingsStore"
- "closeAndReturnError:"
- "configurationWithDomain:service:"
- "configure:"
- "conformsToProtocol:"
- "connection"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "contentsAtPath:"
- "contentsOfDirectoryAtPath:error:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "controlServer"
- "copyAsOnewayVoid"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dataPathAndReturnError:"
- "dataWithPropertyList:format:options:error:"
- "database"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "delegate"
- "description"
- "deviceClass"
- "deviceType"
- "devices"
- "devicesAndReturnError:"
- "disableClientWithParameters:error:"
- "enableAllowListWithParameters:error:"
- "enableClientWithParameters:error:"
- "eraseAndReturnError:"
- "fileExistsAtPath:"
- "fileHandleForReadingFromURL:error:"
- "handle"
- "handleRecordChangesWithParameters:"
- "hasEntitlement:"
- "hasUnlockedSinceBoot"
- "hash"
- "identifier"
- "idsService"
- "init"
- "initWithEndpoint:"
- "initWithService:"
- "innerPoster"
- "interfaceWithIdentifier:configurator:"
- "invalidatable"
- "invalidate"
- "invalidated"
- "isAllowListEnabledAndReturnError:"
- "isClientEnabledWithParameters:error:"
- "isEnabled"
- "isEnabledAndReturnError:"
- "isEqual:"
- "isKindOfClass:"
- "isLocked"
- "isMemberOfClass:"
- "isProxy"
- "isXPCServerEnabled"
- "itemsByIdentifier"
- "listener"
- "listenerWithConfiguration:handler:"
- "localDeviceAndReturnError:"
- "localDeviceIDAndReturnError:"
- "lock"
- "lock_clients"
- "lock_dataSources"
- "lock_descriptors"
- "lock_devices"
- "lock_incomingMessages"
- "messagesWithParameters:error:"
- "migrationClient"
- "mkbEvent"
- "moveItemAtURL:toURL:error:"
- "notificationPoster"
- "notificationQueue"
- "nsuuid"
- "pairWithParameters:completion:"
- "pairingID"
- "pdrPairingIDWithParameters:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personaIntroducer"
- "pid"
- "predefinedClientDescriptorIDs"
- "protocolForProtocol:"
- "protocolForProtocol:interpreter:"
- "pushToken"
- "pushTokenWithParameters:error:"
- "queue"
- "queueWithName:targetQueue:"
- "queue_pendingNotifications"
- "recordChangeNotifier"
- "recordDataStore"
- "recordMetadataStore"
- "recordStore"
- "recordVersionsWithParameters:error:"
- "recordsAndReturnError:"
- "recordsWithParameters:error:"
- "registerClientWithParameters:error:"
- "release"
- "remoteTarget"
- "remoteToken"
- "removeFromAllowListWithParameters:error:"
- "removeItemAtURL:error:"
- "removeRecordsWithParameters:error:"
- "replicator"
- "requestProcessingQueue"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retryStuckRelationshipsAndReturnError:"
- "selector"
- "self"
- "sendMessageExpectingResponseWithParameters:completion:"
- "sendMessageWithParameters:error:"
- "setActivationHandler:"
- "setAllowListWithParameters:error:"
- "setClient:"
- "setEnabledWithParameters:error:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setName:"
- "setQueue:"
- "setServer:"
- "setUserInfo:"
- "sharedInstance"
- "sigtermSource"
- "stages"
- "stateCaptureManager"
- "stateCaptureServer"
- "stateFor:error:"
- "subitemsByIdentifier"
- "subscriptions"
- "superclass"
- "syncAndReturnError:"
- "syncService"
- "title"
- "unavailableWithParameters:error:"
- "uniqueIDOverride"
- "unpairWithParameters:error:"
- "unregisterClientWithParameters:error:"
- "url"
- "v16@0:8"
- "v16@?0@\"<BSServiceInitiatingConnectionConfiguring>\"8"
- "v16@?0@\"<BSServiceListenerConnectionConfiguring>\"8"
- "v16@?0@\"<OS_xpc_object>\"8"
- "v16@?0@\"BSMutableServiceInterface\"8"
- "v16@?0@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\"8"
- "v16@?0@\"BSServiceListenerConnection\"8"
- "v16@?0@\"BSServiceListenerConnection<BSServiceConnectionContext>\"8"
- "v20@?0i8r^{__CFDictionary=}12"
- "v24@0:8@\"<NSCopying>\"16"
- "v24@0:8@\"BSServiceInterface\"16"
- "v24@0:8@\"BSServiceQueue\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\">16"
- "v24@0:8@?<v@?@\"BSServiceListenerConnection<BSServiceConnectionContext>\">16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v8@?0"
- "xpcNotifier"
- "zone"
- "zoneDescriptor"

```
