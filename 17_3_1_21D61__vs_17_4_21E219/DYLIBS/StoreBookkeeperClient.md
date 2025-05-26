## StoreBookkeeperClient

> `/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient`

```diff

-4023.300.2.0.0
-  __TEXT.__text: 0x3238
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x4fc
+4023.500.19.0.0
+  __TEXT.__text: 0x2828
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x390
-  __TEXT.__oslogstring: 0x66
-  __TEXT.__unwind_info: 0x184
-  __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methname: 0x10d0
-  __TEXT.__objc_methtype: 0x36d
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x200
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__cstring: 0x2f5
+  __TEXT.__oslogstring: 0x2f9
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_classname: 0x1b0
+  __TEXT.__objc_methname: 0x116c
+  __TEXT.__objc_methtype: 0x30d
+  __TEXT.__objc_stubs: 0xae0
+  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd50
-  __DATA_CONST.__objc_selrefs: 0x3a0
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x3a8
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__objc_const: 0xcc8
+  __DATA_CONST.__objc_selrefs: 0x3e8
+  __DATA_CONST.__objc_classrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__objc_const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__auth_got: 0x138
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x3c0
+  __DATA.__objc_ivar: 0x48
+  __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper
+  - /System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary
+  - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 125
-  Symbols:   571
-  CStrings:  288
+  Functions: 99
+  Symbols:   475
+  CStrings:  290
 
Symbols:
+ -[ICPlaybackPositionEntity(SBCPrivate) sbcEntity]
+ -[SBCPlaybackPositionEntity iTunesCloudEntity]
+ GCC_except_table51
+ _ICPlaybackPositionServiceDomainDefault
+ _ICPlaybackPositionServiceDomainExtras
+ _OBJC_CLASS_$_ICPlaybackPositionClient
+ _OBJC_CLASS_$_ICPlaybackPositionEntity
+ _OBJC_CLASS_$_ML3MusicLibrary
+ _OBJC_CLASS_$_NSMutableArray
+ _SBCPathWithScrubbedMount
+ __OBJC_$_CATEGORY_ICPlaybackPositionEntity_$_SBCPrivate
+ __OBJC_$_INSTANCE_METHODS_ICPlaybackPositionEntity(SBCPrivate)
+ ___46-[SBCPlaybackPositionEntity iTunesCloudEntity]_block_invoke
+ ___49-[ICPlaybackPositionEntity(SBCPrivate) sbcEntity]_block_invoke
+ ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke.7
+ ___block_descriptor_40_e8_32s_e41_v32?0"ICPlaybackPositionEntity"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e49_v28?0B8"NSError"12"ICPlaybackPositionEntity"20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e32_v32?0"ML3MusicLibrary"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e32_v32?0"ML3MusicLibrary"8Q16^B24ls32l8s40l8
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_msgSend$addObject:
+ _objc_msgSend$allLibraries
+ _objc_msgSend$array
+ _objc_msgSend$autoupdatingSharedLibrary
+ _objc_msgSend$bookmarkTimeModified
+ _objc_msgSend$bookmarkTimestampModified
+ _objc_msgSend$boolValue
+ _objc_msgSend$count
+ _objc_msgSend$databasePath
+ _objc_msgSend$deletePlaybackPositionEntitiesFromLibraryWithIdentifier:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$foreignDatabasePath
+ _objc_msgSend$getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:
+ _objc_msgSend$hasBeenPlayedModified
+ _objc_msgSend$iTunesCloudEntity
+ _objc_msgSend$initWithDomain:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$itemPersistentIdentifier
+ _objc_msgSend$libraryIdentifier
+ _objc_msgSend$libraryUID
+ _objc_msgSend$longLongValue
+ _objc_msgSend$msv_description
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$playbackPositionDomain
+ _objc_msgSend$playbackPositionKey
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$sbcEntity
+ _objc_msgSend$setItemPersistentIdentifier:
+ _objc_msgSend$setLibraryIdentifier:
+ _objc_msgSend$setPlaybackPositionKey:
+ _objc_msgSend$sharedService
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$userPlayCountModified
+ _objc_release_x25
- +[SBCPlaybackPositionService _serviceForPlaybackPositionDomain:]
- +[SBCPlaybackPositionServiceInterface serviceClientInterface]
- +[SBCPlaybackPositionServiceInterface serviceInterface]
- +[SBCPlaybackPositionServiceInterface serviceName]
- -[SBCPlaybackPositionEntity SBKUniversalPlaybackPositionMetadata]
- -[SBCPlaybackPositionEntity copyWithValuesFromSBKUniversalPlaybackPositionMetadata:]
- -[SBCPlaybackPositionService didConnectToService]
- -[SBCXPCService _openServiceConnection]
- -[SBCXPCService queue]
- GCC_except_table88
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSNull
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_SBKStoreURLBagContext
- _OBJC_CLASS_$_SBKUniversalPlaybackPositionMetadata
- _OBJC_IVAR_$_SBCXPCService._queue
- __NSConcreteGlobalBlock
- __OBJC_$_CLASS_METHODS_SBCPlaybackPositionServiceInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBCDomainSyncServiceProtocol_Internal
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBCPlaybackPositionServiceProtocol_Internal
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBCDomainSyncServiceProtocol_Internal
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBCPlaybackPositionServiceProtocol_Internal
- __OBJC_$_PROTOCOL_REFS_SBCDomainSyncServiceProtocol_Internal
- __OBJC_$_PROTOCOL_REFS_SBCPlaybackPositionClientProtocol
- __OBJC_$_PROTOCOL_REFS_SBCPlaybackPositionServiceProtocol_Internal
- __OBJC_LABEL_PROTOCOL_$_SBCDomainSyncServiceProtocol_Internal
- __OBJC_LABEL_PROTOCOL_$_SBCPlaybackPositionClientProtocol
- __OBJC_LABEL_PROTOCOL_$_SBCPlaybackPositionServiceProtocol_Internal
- __OBJC_PROTOCOL_$_SBCDomainSyncServiceProtocol_Internal
- __OBJC_PROTOCOL_$_SBCPlaybackPositionClientProtocol
- __OBJC_PROTOCOL_$_SBCPlaybackPositionServiceProtocol_Internal
- __OBJC_PROTOCOL_REFERENCE_$_SBCPlaybackPositionClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SBCPlaybackPositionServiceProtocol_Internal
- __ServerDidLaunchNotification
- ___39-[SBCXPCService _openServiceConnection]_block_invoke
- ___39-[SBCXPCService _openServiceConnection]_block_invoke_2
- ___55+[SBCPlaybackPositionServiceInterface serviceInterface]_block_invoke
- ___61+[SBCPlaybackPositionServiceInterface serviceClientInterface]_block_invoke
- ___64+[SBCPlaybackPositionService _serviceForPlaybackPositionDomain:]_block_invoke
- ___64+[SBCPlaybackPositionService _serviceForPlaybackPositionDomain:]_block_invoke.1
- ___73-[SBCPlaybackPositionService pullPlaybackPositionEntity:completionBlock:]_block_invoke_2
- ___73-[SBCPlaybackPositionService pullPlaybackPositionEntity:completionBlock:]_block_invoke_3
- ___73-[SBCPlaybackPositionService pullPlaybackPositionEntity:completionBlock:]_block_invoke_4
- ___73-[SBCPlaybackPositionService pushPlaybackPositionEntity:completionBlock:]_block_invoke_2
- ___73-[SBCPlaybackPositionService pushPlaybackPositionEntity:completionBlock:]_block_invoke_3
- ___73-[SBCPlaybackPositionService pushPlaybackPositionEntity:completionBlock:]_block_invoke_4
- ___74-[SBCPlaybackPositionService synchronizeImmediatelyWithCompletionHandler:]_block_invoke
- ___74-[SBCPlaybackPositionService synchronizeImmediatelyWithCompletionHandler:]_block_invoke_2
- ___74-[SBCPlaybackPositionService synchronizeImmediatelyWithCompletionHandler:]_block_invoke_3
- ___74-[SBCPlaybackPositionService synchronizeImmediatelyWithCompletionHandler:]_block_invoke_4
- ___89-[SBCPlaybackPositionService persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke_2
- ___89-[SBCPlaybackPositionService persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke_3
- ___89-[SBCPlaybackPositionService persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke_4
- ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke_2
- ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke_3
- ___92-[SBCPlaybackPositionService pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:]_block_invoke_4
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8
- ___block_descriptor_40_e8_32bs_e50_v28?0B8"NSError"12"SBCPlaybackPositionEntity"20ls32l8
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_literal_global
- ___block_literal_global.26
- ___block_literal_global.85
- __serviceForPlaybackPositionDomain:.bookkeepers
- __serviceForPlaybackPositionDomain:.onceToken
- __serviceForPlaybackPositionDomain:.queue
- _dispatch_async
- _dispatch_get_global_queue
- _dispatch_once
- _dispatch_queue_create
- _dispatch_sync
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$ExtrasDomainIdentifier
- _objc_msgSend$UPPDomainIdentifier
- _objc_msgSend$UTF8String
- _objc_msgSend$_openServiceConnection
- _objc_msgSend$_serverDidLaunch
- _objc_msgSend$_serviceForPlaybackPositionDomain:
- _objc_msgSend$beginAccessingPlaybackPositionEntities
- _objc_msgSend$clientConfiguration
- _objc_msgSend$copy
- _objc_msgSend$deletePlaybackPositionEntities
- _objc_msgSend$didConnectToService
- _objc_msgSend$endAccessingPlaybackPositionEntities
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$isConnectionConfigured
- _objc_msgSend$metadataWithItemIdentifier:bookmarkTime:bookmarkTimestamp:hasBeenPlayed:playCount:
- _objc_msgSend$objectForKey:
- _objc_msgSend$playCount
- _objc_msgSend$pullLocalPlaybackPositionForEntityIdentifiers:completionBlock:
- _objc_msgSend$remoteObjectProxy
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$resume
- _objc_msgSend$setByAddingObjectsFromSet:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setClientConfiguration:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$supportsSyncProtocol
- _objc_msgSend$synchronizeImmediatelyWithCompletionHandler:
- _objc_msgSend$timestamp
- _objc_msgSend$ubiquitousIdentifier
- _objc_msgSend$validateConnectionConfiguration
- _objc_msgSend$xpcConnection
- _objc_release_x1
- _objc_retainAutorelease
- _serviceClientInterface.interface
- _serviceClientInterface.onceToken
- _serviceInterface.interface
- _serviceInterface.onceToken
CStrings:
+ "%{public}@ persistPlaybackPositionEntity completed. success=%{BOOL}u"
+ "%{public}@ persistPlaybackPositionEntity completed. success=%{BOOL}u error=%{public}@"
+ "%{public}@ pullLocalPlaybackPositionForEntityIdentifiers completed with %lu entities. success=%{BOOL}u"
+ "%{public}@ pullLocalPlaybackPositionForEntityIdentifiers completed with %lu entities. success=%{BOOL}u error=%{public}@"
+ "%{public}@ pullPlaybackPositionEntity completed. success=%{BOOL}u entity=%{public}@"
+ "%{public}@ pullPlaybackPositionEntity completed. success=%{BOOL}u entity=%{public}@ error=%{public}@"
+ "%{public}@ pushPlaybackPositionEntity completed. success=%{BOOL}u entity=%{public}@"
+ "%{public}@ pushPlaybackPositionEntity completed. success=%{BOOL}u entity=%{public}@ error=%{public}@"
+ "/private"
+ "SBCPrivate"
+ "T@\"NSString\",?,R,C"
+ "addObject:"
+ "allLibraries"
+ "array"
+ "autoupdatingSharedLibrary"
+ "boolValue"
+ "count"
+ "databasePath"
+ "deletePlaybackPositionEntitiesFromLibraryWithIdentifier:"
+ "doubleValue"
+ "enumerateObjectsUsingBlock:"
+ "getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:"
+ "iTunesCloudEntity"
+ "initWithDomain:"
+ "isEqualToString:"
+ "itemPersistentIdentifier"
+ "libraryIdentifier"
+ "libraryUID"
+ "longLongValue"
+ "msv_description"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInteger:"
+ "playbackPositionKey"
+ "rangeOfString:"
+ "sbcEntity"
+ "setItemPersistentIdentifier:"
+ "setLibraryIdentifier:"
+ "setPlaybackPositionKey:"
+ "sharedService"
+ "stringByReplacingCharactersInRange:withString:"
+ "synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:"
+ "unsignedIntValue"
+ "v28@?0B8@\"NSError\"12@\"ICPlaybackPositionEntity\"20"
+ "v32@?0@\"ICPlaybackPositionEntity\"8Q16^B24"
+ "v32@?0@\"ML3MusicLibrary\"8Q16^B24"
- "\x14"
- "@\"NSObject<OS_dispatch_queue>\""
- "Did connect to storebookkeeperd"
- "ExtrasDomainIdentifier"
- "Invalid parameter.  No database provided."
- "Reconnected to storebookkeeperd - making service active."
- "SBCDomainSyncServiceProtocol_Internal"
- "SBCPlaybackPositionClientProtocol"
- "SBCPlaybackPositionService.m"
- "SBCPlaybackPositionServiceProtocol_Internal"
- "SBKUniversalPlaybackPositionMetadata"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "UPPDomainIdentifier"
- "UTF8String"
- "Use +serviceForPlaybackPositionDomain: instead for %@"
- "Vv24@0:8@\"SBCClientConfiguration\"16"
- "Vv24@0:8@?<v@?B@\"NSError\">16"
- "_openServiceConnection"
- "_queue"
- "_serviceForPlaybackPositionDomain:"
- "com.apple.%@"
- "com.apple.storebookkeeperd.launched"
- "com.apple.storebookkeeperd.xpc"
- "copy"
- "copyWithValuesFromSBKUniversalPlaybackPositionMetadata:"
- "interfaceWithProtocol:"
- "metadataWithItemIdentifier:bookmarkTime:bookmarkTimestamp:hasBeenPlayed:playCount:"
- "objectForKey:"
- "playCount"
- "queue"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setByAddingObjectsFromSet:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setWithObjects:"
- "timestamp"
- "v12@?0B8"
- "v16@?0@\"NSError\"8"
- "v28@?0B8@\"NSError\"12@\"SBCPlaybackPositionEntity\"20"
- "v8@?0"

```
