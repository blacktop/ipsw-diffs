## AccessoryMediaLibrary

> `/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x11198
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0xed4
-  __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x1e27
-  __TEXT.__cstring: 0xc41
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__unwind_info: 0x3e8
-  __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x2379
-  __TEXT.__objc_methtype: 0x748
-  __TEXT.__objc_stubs: 0xee0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x18
+1176.0.26.502.1
+  __TEXT.__text: 0x141f4
+  __TEXT.__objc_methlist: 0x1364
+  __TEXT.__const: 0x100
+  __TEXT.__oslogstring: 0x2220
+  __TEXT.__cstring: 0xcaa
+  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x790
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x878
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__objc_const: 0x1690
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x30
+  __DATA_CONST.__objc_selrefs: 0xa38
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__got: 0x88
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x1e48
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x174
+  __DATA.__data: 0x318
+  __DATA.__bss: 0x60
   __DATA.__common: 0xc
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5382620-877E-326A-83FD-21B379F350D9
-  Functions: 358
-  Symbols:   1367
-  CStrings:  761
+  UUID: 138CF996-3A13-33A1-9403-5E338A504416
+  Functions: 470
+  Symbols:   1785
+  CStrings:  283
 
Symbols:
+ -[ACCMediaLibraryProvider _checkPlaylistContentToSend:accessory:].cold.4
+ -[ACCMediaLibraryProvider initWithDelegate:queue:listenerEndpoint:]
+ -[ACCMediaLibraryProvider initWithDelegate:queue:listenerEndpoint:].cold.1
+ -[ACCMediaLibraryProvider listenerEndpoint]
+ -[ACCMediaLibraryProvider setListenerEndpoint:]
+ -[AccessoryMediaLibraryClient .cxx_destruct]
+ -[AccessoryMediaLibraryClient _connectToServiceOnQueue]
+ -[AccessoryMediaLibraryClient _connectToServiceOnQueue].cold.1
+ -[AccessoryMediaLibraryClient _connectToServiceOnQueue].cold.2
+ -[AccessoryMediaLibraryClient _connectToServiceOnQueue].cold.3
+ -[AccessoryMediaLibraryClient _disconnectOnQueue]
+ -[AccessoryMediaLibraryClient _performWithRemoteObject:]
+ -[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]
+ -[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:].cold.1
+ -[AccessoryMediaLibraryClient accessoryDetached:]
+ -[AccessoryMediaLibraryClient accessoryDetached:].cold.1
+ -[AccessoryMediaLibraryClient accessoryUpdate:windowPerLibrary:]
+ -[AccessoryMediaLibraryClient attachedAccessoryUIDs]
+ -[AccessoryMediaLibraryClient availableLibrariesDidChange:]
+ -[AccessoryMediaLibraryClient availableLibrariesDidChange:].cold.1
+ -[AccessoryMediaLibraryClient checkPendingResetForLibrary:]
+ -[AccessoryMediaLibraryClient clientQueue]
+ -[AccessoryMediaLibraryClient confirmPlaylistContentUpdate:library:lastRevision:]
+ -[AccessoryMediaLibraryClient confirmUpdate:library:lastRevision:updateCount:]
+ -[AccessoryMediaLibraryClient connectToService]
+ -[AccessoryMediaLibraryClient dealloc]
+ -[AccessoryMediaLibraryClient decrementUserCount]
+ -[AccessoryMediaLibraryClient delegate]
+ -[AccessoryMediaLibraryClient disconnect]
+ -[AccessoryMediaLibraryClient featureUserCount]
+ -[AccessoryMediaLibraryClient incrementUserCount]
+ -[AccessoryMediaLibraryClient init]
+ -[AccessoryMediaLibraryClient isConnected]
+ -[AccessoryMediaLibraryClient isServiceReady]
+ -[AccessoryMediaLibraryClient lastAvailableLibraries]
+ -[AccessoryMediaLibraryClient libraryResetUpdate:accessory:]
+ -[AccessoryMediaLibraryClient libraryResetUpdate:accessory:].cold.1
+ -[AccessoryMediaLibraryClient libraryResetUpdate:accessory:].cold.2
+ -[AccessoryMediaLibraryClient libraryStateDidChange:stateType:enabled:]
+ -[AccessoryMediaLibraryClient libraryStateDidChange:stateType:enabled:].cold.1
+ -[AccessoryMediaLibraryClient libraryUpdate:revision:content:accessory:]
+ -[AccessoryMediaLibraryClient libraryUpdate:revision:content:accessory:].cold.1
+ -[AccessoryMediaLibraryClient libraryUpdate:updates:accessory:]
+ -[AccessoryMediaLibraryClient libraryUpdate:updates:accessory:].cold.1
+ -[AccessoryMediaLibraryClient mockListenerEndpoint]
+ -[AccessoryMediaLibraryClient mutableAttachedAccessoryUIDs]
+ -[AccessoryMediaLibraryClient pendingResetLibraryUIDs]
+ -[AccessoryMediaLibraryClient playAllSongs:library:startItem:]
+ -[AccessoryMediaLibraryClient playCollection:library:collection:type:startIndex:]
+ -[AccessoryMediaLibraryClient playCollection:library:collection:type:startItem:]
+ -[AccessoryMediaLibraryClient playCurrentSelection:library:]
+ -[AccessoryMediaLibraryClient playItems:library:itemList:startIndex:]
+ -[AccessoryMediaLibraryClient remoteObject]
+ -[AccessoryMediaLibraryClient requestLibraryInfoUpdate:]
+ -[AccessoryMediaLibraryClient serviceConnection]
+ -[AccessoryMediaLibraryClient setClientQueue:]
+ -[AccessoryMediaLibraryClient setDelegate:]
+ -[AccessoryMediaLibraryClient setFeatureUserCount:]
+ -[AccessoryMediaLibraryClient setIsServiceReady:]
+ -[AccessoryMediaLibraryClient setLastAvailableLibraries:]
+ -[AccessoryMediaLibraryClient setMockListenerEndpoint:]
+ -[AccessoryMediaLibraryClient setMutableAttachedAccessoryUIDs:]
+ -[AccessoryMediaLibraryClient setPendingResetLibraryUIDs:]
+ -[AccessoryMediaLibraryClient setRemoteObject:]
+ -[AccessoryMediaLibraryClient setServiceConnection:]
+ -[AccessoryMediaLibraryClient startMediaLibraryUpdate:library:lastRevision:requestedInfo:]
+ -[AccessoryMediaLibraryClient stopAllMediaLibraryUpdate:]
+ -[AccessoryMediaLibraryClient stopMediaLibraryUpdate:library:]
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table34
+ GCC_except_table4
+ GCC_except_table58
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table67
+ _OBJC_CLASS_$_AccessoryMediaLibraryClient
+ _OBJC_IVAR_$_ACCMediaLibraryProvider._listenerEndpoint
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._clientQueue
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._delegate
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._featureUserCount
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._isServiceReady
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._lastAvailableLibraries
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._mockListenerEndpoint
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._mutableAttachedAccessoryUIDs
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._pendingResetLibraryUIDs
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._remoteObject
+ _OBJC_IVAR_$_AccessoryMediaLibraryClient._serviceConnection
+ _OBJC_METACLASS_$_AccessoryMediaLibraryClient
+ __MergedGlobals.4
+ __OBJC_$_INSTANCE_METHODS_AccessoryMediaLibraryClient
+ __OBJC_$_INSTANCE_VARIABLES_AccessoryMediaLibraryClient
+ __OBJC_$_PROP_LIST_AccessoryMediaLibraryClient
+ __OBJC_$_PROP_LIST_AccessoryMediaLibraryClientAPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACCMediaLibraryFeatureServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AccessoryMediaLibraryClientAPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACCMediaLibraryFeatureServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AccessoryMediaLibraryClientAPI
+ __OBJC_$_PROTOCOL_REFS_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_$_PROTOCOL_REFS_ACCMediaLibraryFeatureServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_AccessoryMediaLibraryClientAPI
+ __OBJC_CLASS_PROTOCOLS_$_AccessoryMediaLibraryClient
+ __OBJC_CLASS_RO_$_AccessoryMediaLibraryClient
+ __OBJC_LABEL_PROTOCOL_$_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_ACCMediaLibraryFeatureServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_AccessoryMediaLibraryClientAPI
+ __OBJC_METACLASS_RO_$_AccessoryMediaLibraryClient
+ __OBJC_PROTOCOL_$_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_PROTOCOL_$_ACCMediaLibraryFeatureServiceProtocol
+ __OBJC_PROTOCOL_$_AccessoryMediaLibraryClientAPI
+ __OBJC_PROTOCOL_REFERENCE_$_ACCMediaLibraryFeatureClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ACCMediaLibraryFeatureServiceProtocol
+ ___169-[ACCMediaLibraryProvider startMediaLibraryUpdate:library:lastRevision:mediaItemProperties:playlistProperties:playlistContentStyle:playlistContentProperties:reqOptions:]_block_invoke.121
+ ___41-[AccessoryMediaLibraryClient disconnect]_block_invoke
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.97
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.97.cold.1
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.98
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.98.cold.1
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.99
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.99.cold.1
+ ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.99.cold.2
+ ___43-[ACCMediaLibraryAccessory clearAllUpdates]_block_invoke
+ ___43-[ACCMediaLibraryAccessory clearAllUpdates]_block_invoke.cold.1
+ ___47-[AccessoryMediaLibraryClient connectToService]_block_invoke
+ ___49-[AccessoryMediaLibraryClient accessoryDetached:]_block_invoke
+ ___49-[AccessoryMediaLibraryClient accessoryDetached:]_block_invoke.cold.1
+ ___49-[AccessoryMediaLibraryClient decrementUserCount]_block_invoke
+ ___49-[AccessoryMediaLibraryClient decrementUserCount]_block_invoke.cold.1
+ ___49-[AccessoryMediaLibraryClient decrementUserCount]_block_invoke.cold.2
+ ___49-[AccessoryMediaLibraryClient incrementUserCount]_block_invoke
+ ___49-[AccessoryMediaLibraryClient incrementUserCount]_block_invoke.cold.1
+ ___52-[AccessoryMediaLibraryClient attachedAccessoryUIDs]_block_invoke
+ ___53-[ACCMediaLibraryProvider stopAllMediaLibraryUpdate:]_block_invoke.127
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.100
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.100.cold.1
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.100.cold.2
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.103
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.103.cold.1
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.96
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.98
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.98.cold.1
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.98.cold.2
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke_2
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke_2.97
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke_2.97.cold.1
+ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke_2.cold.1
+ ___56-[ACCMediaLibraryProvider playCurrentSelection:library:]_block_invoke.134
+ ___56-[AccessoryMediaLibraryClient _performWithRemoteObject:]_block_invoke
+ ___56-[AccessoryMediaLibraryClient requestLibraryInfoUpdate:]_block_invoke
+ ___57-[ACCMediaLibraryProvider accessoryMediaLibraryDetached:]_block_invoke.112
+ ___57-[AccessoryMediaLibraryClient stopAllMediaLibraryUpdate:]_block_invoke
+ ___58-[ACCMediaLibraryAccessory confirmUpdates:revision:count:]_block_invoke.cold.4
+ ___58-[ACCMediaLibraryProvider playAllSongs:library:startItem:]_block_invoke.146
+ ___58-[ACCMediaLibraryProvider stopMediaLibraryUpdate:library:]_block_invoke.124
+ ___59-[ACCMediaLibraryProvider accessoryMediaLibraryAllDetached]_block_invoke.113
+ ___59-[ACCMediaLibraryProvider accessoryMediaLibraryAllDetached]_block_invoke.cold.1
+ ___59-[ACCMediaLibraryProvider accessoryMediaLibraryAllDetached]_block_invoke.cold.2
+ ___59-[AccessoryMediaLibraryClient checkPendingResetForLibrary:]_block_invoke
+ ___60-[AccessoryMediaLibraryClient libraryResetUpdate:accessory:]_block_invoke
+ ___60-[AccessoryMediaLibraryClient playCurrentSelection:library:]_block_invoke
+ ___62-[AccessoryMediaLibraryClient playAllSongs:library:startItem:]_block_invoke
+ ___62-[AccessoryMediaLibraryClient stopMediaLibraryUpdate:library:]_block_invoke
+ ___64-[AccessoryMediaLibraryClient accessoryUpdate:windowPerLibrary:]_block_invoke
+ ___65-[ACCMediaLibraryProvider playItems:library:itemList:startIndex:]_block_invoke.137
+ ___66-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]_block_invoke
+ ___66-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]_block_invoke.cold.1
+ ___66-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]_block_invoke.cold.2
+ ___66-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]_block_invoke.cold.3
+ ___69-[AccessoryMediaLibraryClient playItems:library:itemList:startIndex:]_block_invoke
+ ___72-[ACCMediaLibraryProvider accessoryMediaLibraryUpdate:windowPerLibrary:]_block_invoke.116
+ ___74-[ACCMediaLibraryProvider accessoryMediaLibraryAttached:windowPerLibrary:]_block_invoke.109
+ ___74-[ACCMediaLibraryProvider confirmUpdate:library:lastRevision:updateCount:]_block_invoke.130
+ ___76-[ACCMediaLibraryProvider playCollection:library:collection:type:startItem:]_block_invoke.140
+ ___77-[ACCMediaLibraryProvider confirmPlaylistContentUpdate:library:lastRevision:]_block_invoke.131
+ ___77-[ACCMediaLibraryProvider playCollection:library:collection:type:startIndex:]_block_invoke.143
+ ___78-[ACCMediaLibraryAccessory copyPendingPlaylistContentUpdatesToSendForLibrary:]_block_invoke.cold.4
+ ___78-[AccessoryMediaLibraryClient confirmUpdate:library:lastRevision:updateCount:]_block_invoke
+ ___80-[AccessoryMediaLibraryClient playCollection:library:collection:type:startItem:]_block_invoke
+ ___81-[AccessoryMediaLibraryClient confirmPlaylistContentUpdate:library:lastRevision:]_block_invoke
+ ___81-[AccessoryMediaLibraryClient playCollection:library:collection:type:startIndex:]_block_invoke
+ ___90-[AccessoryMediaLibraryClient startMediaLibraryUpdate:library:lastRevision:requestedInfo:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_44_e8_32s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8
+ ___block_descriptor_68_e8_32s40s_e49_v16?0"<ACCMediaLibraryFeatureServiceProtocol>"8ls32l8s40l8
+ ___block_descriptor_tmp.3
+ ___block_literal_global.102
+ ___block_literal_global.203
+ ___block_literal_global.233
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _dispatch_assert_queue_not$V2
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_getProperty
+ _objc_msgSend$_connectToServiceOnQueue
+ _objc_msgSend$_disconnectOnQueue
+ _objc_msgSend$_performWithRemoteObject:
+ _objc_msgSend$accessories
+ _objc_msgSend$accessoryArrived:windowPerLibrary:
+ _objc_msgSend$accessoryLeft:
+ _objc_msgSend$accessoryUpdate:windowPerLibrary:
+ _objc_msgSend$albumArtist
+ _objc_msgSend$albumArtistPersistentID
+ _objc_msgSend$albumDiscCount
+ _objc_msgSend$albumDiscNumber
+ _objc_msgSend$albumPersistentID
+ _objc_msgSend$albumTitle
+ _objc_msgSend$albumTrackCount
+ _objc_msgSend$albumTrackNumber
+ _objc_msgSend$artist
+ _objc_msgSend$artistPersistentID
+ _objc_msgSend$attachedAccessoryUIDs
+ _objc_msgSend$chapterCount
+ _objc_msgSend$clientQueue
+ _objc_msgSend$clientWillDisconnect
+ _objc_msgSend$composer
+ _objc_msgSend$composerPersistentID
+ _objc_msgSend$confirmPlaylistContentUpdate:library:lastRevision:
+ _objc_msgSend$confirmUpdate:library:lastRevision:updateCount:
+ _objc_msgSend$confirmedRevisionList
+ _objc_msgSend$containsObject:
+ _objc_msgSend$contentList
+ _objc_msgSend$contentStyle
+ _objc_msgSend$copy
+ _objc_msgSend$duration
+ _objc_msgSend$featureUserCount
+ _objc_msgSend$folder
+ _objc_msgSend$geniusMix
+ _objc_msgSend$genre
+ _objc_msgSend$genrePersistentID
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$isServiceReady
+ _objc_msgSend$lastAvailableLibraries
+ _objc_msgSend$lastUpdateType
+ _objc_msgSend$libraries
+ _objc_msgSend$listQueue
+ _objc_msgSend$listenerEndpoint
+ _objc_msgSend$local
+ _objc_msgSend$mediaLibraryAvailableLibrariesDidChange:accessory:
+ _objc_msgSend$mediaLibraryStateDidChange:stateType:enabled:accessory:
+ _objc_msgSend$mediaLibraryUpdate:revision:content:accessory:
+ _objc_msgSend$mediaLibraryUpdate:updates:accessory:
+ _objc_msgSend$mockListenerEndpoint
+ _objc_msgSend$mutableAttachedAccessoryUIDs
+ _objc_msgSend$name
+ _objc_msgSend$parentPersistentID
+ _objc_msgSend$partOfCompilation
+ _objc_msgSend$pendingPlaylistContentUpdates
+ _objc_msgSend$pendingResetLibraryUIDs
+ _objc_msgSend$pendingUpdates
+ _objc_msgSend$playAllSongs:library:firstItemPersistentID:
+ _objc_msgSend$playCollection:library:collection:type:firstItemIndex:
+ _objc_msgSend$playCollection:library:collection:type:firstItemPersistentID:
+ _objc_msgSend$playCurrentSelection:library:
+ _objc_msgSend$playItems:library:itemList:firstItemIndex:
+ _objc_msgSend$playlistPersistentID
+ _objc_msgSend$provider
+ _objc_msgSend$radioStation
+ _objc_msgSend$radioStationOrdering
+ _objc_msgSend$rating
+ _objc_msgSend$serviceConnection
+ _objc_msgSend$setAccessories:
+ _objc_msgSend$setConfirmedRevisionList:
+ _objc_msgSend$setContentList:
+ _objc_msgSend$setFeatureUserCount:
+ _objc_msgSend$setIsServiceReady:
+ _objc_msgSend$setLastAvailableLibraries:
+ _objc_msgSend$setLibraries:
+ _objc_msgSend$setMockListenerEndpoint:
+ _objc_msgSend$setPendingPlaylistContentUpdates:
+ _objc_msgSend$setPendingUpdates:
+ _objc_msgSend$setServiceConnection:
+ _objc_msgSend$setWaitingConfirm:
+ _objc_msgSend$smartPlaylist
+ _objc_msgSend$startUpdate:library:lastRevision:requestedInfo:
+ _objc_msgSend$stopAllUpdate:
+ _objc_msgSend$stopUpdate:library:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$title
+ _objc_msgSend$validMask
+ _objc_msgSend$waitingConfirm
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_setProperty_atomic
- -[ACCMediaLibraryAccessory clearAllUpdates].cold.1
- -[ACCMediaLibraryProvider initWithDelegate:queue:]
- -[ACCMediaLibraryProvider initWithDelegate:queue:].cold.1
- GCC_except_table0
- GCC_except_table5
- GCC_except_table59
- GCC_except_table68
- _ACCMediaLibraryUpdateEntryKey
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- ___169-[ACCMediaLibraryProvider startMediaLibraryUpdate:library:lastRevision:mediaItemProperties:playlistProperties:playlistContentStyle:playlistContentProperties:reqOptions:]_block_invoke.125
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.102
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.102.cold.1
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.104.cold.2
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.108
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.108.cold.1
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.109
- ___42-[ACCMediaLibraryProvider connectToServer]_block_invoke.109.cold.1
- ___50-[ACCMediaLibraryProvider initWithDelegate:queue:]_block_invoke
- ___50-[ACCMediaLibraryProvider initWithDelegate:queue:]_block_invoke.cold.1
- ___50-[ACCMediaLibraryProvider initWithDelegate:queue:]_block_invoke.cold.2
- ___53-[ACCMediaLibraryProvider stopAllMediaLibraryUpdate:]_block_invoke.131
- ___56-[ACCMediaLibraryProvider playCurrentSelection:library:]_block_invoke.138
- ___57-[ACCMediaLibraryProvider accessoryMediaLibraryDetached:]_block_invoke.116
- ___58-[ACCMediaLibraryProvider playAllSongs:library:startItem:]_block_invoke.150
- ___58-[ACCMediaLibraryProvider stopMediaLibraryUpdate:library:]_block_invoke.128
- ___59-[ACCMediaLibraryProvider accessoryMediaLibraryAllDetached]_block_invoke.117
- ___65-[ACCMediaLibraryProvider playItems:library:itemList:startIndex:]_block_invoke.141
- ___72-[ACCMediaLibraryProvider accessoryMediaLibraryUpdate:windowPerLibrary:]_block_invoke.120
- ___74-[ACCMediaLibraryProvider accessoryMediaLibraryAttached:windowPerLibrary:]_block_invoke.113
- ___74-[ACCMediaLibraryProvider confirmUpdate:library:lastRevision:updateCount:]_block_invoke.134
- ___76-[ACCMediaLibraryProvider playCollection:library:collection:type:startItem:]_block_invoke.144
- ___77-[ACCMediaLibraryProvider confirmPlaylistContentUpdate:library:lastRevision:]_block_invoke.135
- ___77-[ACCMediaLibraryProvider playCollection:library:collection:type:startIndex:]_block_invoke.147
- ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
- ___block_literal_global.107
- _objc_msgSend$initWithMachServiceName:options:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s:%d serviceConnection=%p remoteObject=%p isServiceReady=%d"
+ "'"
+ "("
+ "-[AccessoryMediaLibraryClient _connectToServiceOnQueue]"
+ "Getting remote object for MediaLibrary service..."
+ "MediaLibrary XPC service connection invalidated!"
+ "MediaLibrary XPC service error: %@"
+ "MediaLibrary XPC service interrupted (service crash). Will reconnect on next call..."
+ "MediaLibrary initConnection error: %@"
+ "MediaLibrary service ready: %d"
+ "No more MediaLibrary users, disconnecting from service..."
+ "Received availableLibrariesDidChange from service: %@"
+ "Received libraryContentUpdate from service: lib=%@ accessory=%@ revision=%@"
+ "Received libraryResetUpdate from service: lib=%@ accessory=%@"
+ "Received libraryStateDidChange from service: %@ type=%d enabled=%d"
+ "Received libraryUpdate from service: lib=%@ accessory=%@ count=%lu"
+ "XPC connection interrupted: providerUID:%@, notify of detach"
+ "accessoryAttached: %@ windowPerLibrary=%u"
+ "accessoryAttached: remoteObject is nil! Cannot send accessoryArrived for %@"
+ "accessoryAttached: sending accessoryArrived to service for %@"
+ "accessoryDetached: %@"
+ "accessoryDetached: sending accessoryLeft to service for %@"
+ "clearAllUpdates: %@, pendingUpdates.count=%lu waitingConfirm.count=%lu pendingPlaylistContentUpdates.count=%lu confirmedRevisionList.count=%lu"
+ "com.apple.accessories.media-library-client"
+ "com.apple.accessories.media-library-feature"
+ "decrementUserCount: %d -> %d"
+ "foundDeletionOrAdd=%d providerUID:%@ self.libraries= %@ -> %@"
+ "incrementUserCount: %d -> %d"
+ "update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ self.lastUpdateType=%d"
+ "update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ self.lastUpdateType=%d, UNKNOWN TYPE!!!"
+ "v16@?0@\"<ACCMediaLibraryFeatureServiceProtocol>\"8"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<ACCMediaLibraryProviderDelegateProtocol>\""
- "@\"<ACCMediaLibraryXPCServerProtocol>\""
- "@\"ACCMediaLibraryProvider\""
- "@\"ACCMediaLibraryUpdateLibraryInfo\""
- "@\"ACCMediaLibraryUpdatePlaylistContent\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16@24I32"
- "@36@0:8@16@24i32"
- "@36@0:8@16I24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24Q32"
- "@44@0:8@16@24i32@36"
- "ACCMediaLibraryAccessory"
- "ACCMediaLibraryInfo"
- "ACCMediaLibraryProvider"
- "ACCMediaLibraryUpdateEntryKey"
- "ACCMediaLibraryUpdateItem"
- "ACCMediaLibraryUpdateLibraryInfo"
- "ACCMediaLibraryUpdatePlaylist"
- "ACCMediaLibraryUpdatePlaylistContent"
- "ACCMediaLibraryUpdatePlaylistContentItem"
- "ACCMediaLibraryXPCClientProtocol"
- "ACCMediaLibraryXPCServerProtocol"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8i16B20"
- "B32@0:8@16@24"
- "I"
- "I16@0:8"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "S"
- "S16@0:8"
- "Server availability changed! State: %d"
- "T#,R"
- "T@\"<ACCMediaLibraryProviderDelegateProtocol>\",W,N,V_delegate"
- "T@\"<ACCMediaLibraryXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"ACCMediaLibraryProvider\",R,W,N,V_provider"
- "T@\"ACCMediaLibraryUpdateLibraryInfo\",R,N,V_info"
- "T@\"ACCMediaLibraryUpdatePlaylistContent\",&,N,V_content"
- "T@\"NSMutableArray\",&,N,V_contentList"
- "T@\"NSMutableDictionary\",&,N,V_accessories"
- "T@\"NSMutableDictionary\",&,N,V_confirmedRevisionList"
- "T@\"NSMutableDictionary\",&,N,V_libraries"
- "T@\"NSMutableDictionary\",&,N,V_pendingPlaylistContentUpdates"
- "T@\"NSMutableDictionary\",&,N,V_pendingUpdates"
- "T@\"NSMutableDictionary\",&,N,V_waitingConfirm"
- "T@\"NSMutableDictionary\",R,N,V_libraries"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_processingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_listQueue"
- "T@\"NSObject<OS_dispatch_queue>\",W,N,V_delegateQ"
- "T@\"NSString\",&,N,V_albumArtist"
- "T@\"NSString\",&,N,V_albumTitle"
- "T@\"NSString\",&,N,V_artist"
- "T@\"NSString\",&,N,V_composer"
- "T@\"NSString\",&,N,V_genre"
- "T@\"NSString\",&,N,V_mediaLibraryUID"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",&,N,V_revision"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_accessoryUID"
- "T@\"NSString\",R,N,V_libraryUID"
- "T@\"NSString\",R,N,V_revision"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "T@,R,N,V_item"
- "TB,N,V_folder"
- "TB,N,V_geniusMix"
- "TB,N,V_local"
- "TB,N,V_partOfCompilation"
- "TB,N,V_radioStation"
- "TB,N,V_smartPlaylist"
- "TI,N,V_duration"
- "TI,N,V_windowPerLibrary"
- "TQ,N,V_albumArtistPersistentID"
- "TQ,N,V_albumPersistentID"
- "TQ,N,V_artistPersistentID"
- "TQ,N,V_composerPersistentID"
- "TQ,N,V_genrePersistentID"
- "TQ,N,V_parentPersistentID"
- "TQ,N,V_persistentID"
- "TQ,N,V_playlistPersistentID"
- "TQ,R"
- "TQ,R,N,V_validMask"
- "TS,N,V_albumDiscCount"
- "TS,N,V_albumDiscNumber"
- "TS,N,V_albumTrackCount"
- "TS,N,V_albumTrackNumber"
- "TS,N,V_chapterCount"
- "TS,N,V_radioStationOrdering"
- "Ti,N,V_contentStyle"
- "Ti,N,V_lastUpdateType"
- "Ti,N,V_rating"
- "Ti,N,V_type"
- "Ti,R,N,V_type"
- "Trying to connect to server..."
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XPC connection interupted: providerUID:%@, notify of detach"
- "[2B]"
- "^{_NSZone=}16@0:8"
- "_ACCMediaLibraryAccessoryPendingUpdateItem"
- "_accessories"
- "_accessoryUID"
- "_addConfirmedRevisionForLibrary:revision:"
- "_addConfirmedRevisionForLibrary:revisionsToAdd:"
- "_addToWaitlistForLibrary:item:"
- "_addToWaitlistForLibrary:list:"
- "_albumArtist"
- "_albumArtistPersistentID"
- "_albumDiscCount"
- "_albumDiscNumber"
- "_albumPersistentID"
- "_albumTitle"
- "_albumTrackCount"
- "_albumTrackNumber"
- "_artist"
- "_artistPersistentID"
- "_chapterCount"
- "_checkPlaylistContentToSend:accessory:"
- "_composer"
- "_composerPersistentID"
- "_confirmedRevisionList"
- "_confirmedRevisionListForLibrary:createIfNotExist:"
- "_confirmedRevisionListRemoveLibraryIfEmpty:"
- "_content"
- "_contentList"
- "_contentStyle"
- "_delegate"
- "_delegateQ"
- "_duration"
- "_folder"
- "_geniusMix"
- "_genre"
- "_genrePersistentID"
- "_info"
- "_item"
- "_lastUpdateType"
- "_libraries"
- "_libraryUID"
- "_listQueue"
- "_local"
- "_mediaLibraryUID"
- "_name"
- "_notifyRemoteOfAvailableLibraries"
- "_parentPersistentID"
- "_partOfCompilation"
- "_pendingAndWaitingConfirmUpdatesCountForLibrary:"
- "_pendingPlaylistContentUpdates"
- "_pendingPlaylistContentUpdatesCountForLibrary:"
- "_pendingPlaylistContentUpdatesForLibrary:createIfNotExist:"
- "_pendingPlaylistContentUpdatesRemoveLibraryIfEmpty:"
- "_pendingUpdates"
- "_pendingUpdatesAndWaitingConfirmFullForLibrary:"
- "_pendingUpdatesForLibrary:createIfNotExist:"
- "_pendingUpdatesRemoveLibraryIfEmpty:"
- "_persistentID"
- "_playlistPersistentID"
- "_processingQueue"
- "_provider"
- "_providerUID"
- "_radioStation"
- "_radioStationOrdering"
- "_rating"
- "_remoteObject"
- "_revision"
- "_serverConnection"
- "_smartPlaylist"
- "_state"
- "_stateInit"
- "_title"
- "_type"
- "_validMask"
- "_waitingConfirm"
- "_waitingUpdatesForLibrary:createIfNotExist:"
- "_waitingUpdatesRemoveLibraryIfEmpty:"
- "_windowPerLibrary"
- "accessories"
- "accessoryMediaLibraryAllDetached"
- "accessoryMediaLibraryAttached:windowPerLibrary:"
- "accessoryMediaLibraryDetached:"
- "accessoryMediaLibraryUpdate:windowPerLibrary:"
- "accessoryUID"
- "addContentItem:"
- "addContentPersistentID:"
- "addLibraryInfo:"
- "addObject:"
- "addObjectsFromArray:"
- "addPlaylistContentUpdate:library:"
- "addUpdate:library:"
- "albumArtist"
- "albumArtistPersistentID"
- "albumDiscCount"
- "albumDiscNumber"
- "albumPersistentID"
- "albumTitle"
- "albumTrackCount"
- "albumTrackNumber"
- "allKeys"
- "allValues"
- "arrayWithArray:"
- "artist"
- "artistPersistentID"
- "autorelease"
- "chapterCount"
- "class"
- "clearAllUpdates"
- "clearAllUpdates: %@, pendingUpdates.count=%lu waitingConfirm.count=%lu pendingUpdates.count=%lu waitingConfirm.count=%lu"
- "clearAllUpdatesForLibrary:"
- "com.apple.accessories.medialibrary"
- "com.apple.accessories.medialibrary.availability-changed"
- "composer"
- "composerPersistentID"
- "confirmPlaylistContentUpdate:library:lastRevision:"
- "confirmPlaylistContentUpdates:revision:"
- "confirmUpdate:library:lastRevision:updateCount:"
- "confirmUpdates:revision:count:"
- "confirmedRevisionList"
- "conformsToProtocol:"
- "connectToServer"
- "content"
- "contentList"
- "contentListCount"
- "contentStyle"
- "copyContentDictList"
- "copyContentList"
- "copyDict"
- "copyNSRepresentation:"
- "copyPendingNonContentUpdatesToSendForLibrary:"
- "copyPendingPlaylistContentUpdatesToSendForLibrary:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "delegate"
- "delegateQ"
- "description"
- "duration"
- "fillStruct:"
- "flushUpdates:accessory:"
- "folder"
- "foundDeletionOrAdd=%d providerUID:%@ _libraries= %@ -> %@"
- "geniusMix"
- "genre"
- "genrePersistentID"
- "getContentItemAtIndex:"
- "getState:"
- "hash"
- "i"
- "i16@0:8"
- "info"
- "init"
- "initConnection:"
- "initWithCapacity:"
- "initWithDelegate:queue:"
- "initWithDict:"
- "initWithInfo:"
- "initWithLibrary:revision:type:item:"
- "initWithMachServiceName:options:"
- "initWithMediaLibrary:dict:"
- "initWithMediaLibrary:name:type:"
- "initWithMediaLibrary:persistentID:playlistPersistentID:"
- "initWithMediaLibrary:persistentID:revision:"
- "initWithMediaLibrary:playlistPersistentID:dict:"
- "initWithMediaLibrary:revision:dict:"
- "initWithUID:windowPerLibrary:provider:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "item"
- "iterateContentItems:"
- "iterateContentPersistentIDs:"
- "lastUpdateType"
- "libraries"
- "libraryUID"
- "listQueue"
- "local"
- "mediaLibrary:accessoryArrived:windowPerLibrary:"
- "mediaLibrary:accessoryLeft:"
- "mediaLibrary:accessoryUpdate:windowPerLibrary:"
- "mediaLibrary:confirmPlaylistContentUpdate:lastRevision:accessory:"
- "mediaLibrary:confirmUpdate:lastRevision:updateCount:accessory:"
- "mediaLibrary:play:collection:type:firstItemIndex:accessory:"
- "mediaLibrary:play:collection:type:firstItemPersistentID:accessory:"
- "mediaLibrary:play:itemList:firstItemIndex:accessory:"
- "mediaLibrary:playAllSongs:firstItemPersistentID:accessory:"
- "mediaLibrary:playCurrentSelection:accessory:"
- "mediaLibrary:startUpdate:lastRevision:requestedInfo:accessory:"
- "mediaLibrary:stopAllUpdate:"
- "mediaLibrary:stopUpdate:accessory:"
- "mediaLibraryUID"
- "name"
- "notify:stateChange:enabled:"
- "notifyAvailableLibraries:"
- "notifyAvailableLibraries:provider:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectForKey:"
- "parentPersistentID"
- "partOfCompilation"
- "pendingAndWaitingConfirmUpdatesCountForLibrary:"
- "pendingPlaylistContentUpdates"
- "pendingPlaylistContentUpdatesCountForLibrary:"
- "pendingUpdates"
- "pendingUpdatesAndWaitingConfirmFullForLibrary:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentID"
- "playAllSongs:library:startItem:"
- "playCollection:library:collection:type:startIndex:"
- "playCollection:library:collection:type:startItem:"
- "playCurrentSelection:library:"
- "playItems:library:itemList:startIndex:"
- "playlistPersistentID"
- "processingQueue"
- "provider"
- "providerUID"
- "q44@0:8@16@24C32@36"
- "q48@0:8@16@24@32@40"
- "q52@0:8@16@24@32C40@44"
- "q52@0:8@16@24Q32C40@44"
- "q64@0:8@16@24Q32i40@44C52@56"
- "radioStation"
- "radioStationOrdering"
- "rating"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInRange:"
- "replaceContentItem:atIndex:"
- "replaceContentList:"
- "replaceContentPersistentID:atIndex:"
- "replaceObjectAtIndex:withObject:"
- "resetUpdate:accessory:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "revision"
- "self"
- "serverConnection"
- "setAccessories:"
- "setAlbumArtist:"
- "setAlbumArtistPersistentID:"
- "setAlbumDiscCount:"
- "setAlbumDiscNumber:"
- "setAlbumPersistentID:"
- "setAlbumTitle:"
- "setAlbumTrackCount:"
- "setAlbumTrackNumber:"
- "setArtist:"
- "setArtistPersistentID:"
- "setChapterCount:"
- "setComposer:"
- "setComposerPersistentID:"
- "setConfirmedRevisionList:"
- "setContent:"
- "setContentList:"
- "setContentStyle:"
- "setDelegate:"
- "setDelegateQ:"
- "setDuration:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFolder:"
- "setGeniusMix:"
- "setGenre:"
- "setGenrePersistentID:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastUpdateType:"
- "setLibraries:"
- "setLocal:"
- "setMediaLibraryUID:"
- "setName:"
- "setObject:forKey:"
- "setParentPersistentID:"
- "setPartOfCompilation:"
- "setPendingPlaylistContentUpdates:"
- "setPendingUpdates:"
- "setPersistentID:"
- "setPlaylistPersistentID:"
- "setProcessingQueue:"
- "setProviderUID:"
- "setRadioStation:"
- "setRadioStationOrdering:"
- "setRating:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setRevision:"
- "setServerConnection:"
- "setSmartPlaylist:"
- "setState:value:"
- "setTitle:"
- "setType:"
- "setWaitingConfirm:"
- "setWindowPerLibrary:"
- "smartPlaylist"
- "startMediaLibraryUpdate:library:lastRevision:mediaItemProperties:playlistProperties:playlistContentStyle:playlistContentProperties:reqOptions:"
- "stopAllMediaLibraryUpdate:"
- "stopMediaLibraryUpdate:library:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "title"
- "type"
- "unionSet:"
- "unsignedCharValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "unsignedShortValue"
- "update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ _lastUpdateType=%d"
- "update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ _lastUpdateType=%d, UNKNOWN TYPE!!!"
- "update:revision:content:accessory:"
- "update:revision:deleteItem:progress:accessory:"
- "update:revision:deletePlaylist:progress:accessory:"
- "update:revision:item:progress:accessory:"
- "update:revision:persistentID:type:updateInfo:progress:accessory:"
- "update:revision:playlist:progress:accessory:"
- "update:revision:progress:accessory:"
- "update:updates:accessory:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8Q16"
- "v24@0:8^{?=**i}16"
- "v24@0:8^{?=IQ******}16"
- "v24@0:8^{?=IQ*CCIQ*SSSSQ*Q*Q*Q*CCS}16"
- "v24@0:8^{?=IQ*QCCCCCS}16"
- "v28@0:8@\"NSString\"16I24"
- "v28@0:8@16I24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16i24B28"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8@16i24B28"
- "v32@0:8Q16Q24"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24Q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24Q32"
- "v44@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32I40"
- "v44@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32I40"
- "v44@0:8@16@24@32I40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24Q32i40I44"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24Q32i40I44"
- "v52@0:8@\"NSString\"16@\"NSString\"24Q32i40Q44"
- "v52@0:8@16@24Q32i40Q44"
- "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40Q48i56Q60Q68"
- "v76@0:8@16@24@32Q40Q48i56Q60Q68"
- "validMask"
- "waitingConfirm"
- "windowPerLibrary"
- "zone"

```
