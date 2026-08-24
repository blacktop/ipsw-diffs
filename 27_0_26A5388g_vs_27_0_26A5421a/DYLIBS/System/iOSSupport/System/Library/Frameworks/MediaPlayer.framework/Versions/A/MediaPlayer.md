## MediaPlayer

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

```diff

-4026.100.79.0.0
-  __TEXT.__text: 0x21a3d4
-  __TEXT.__objc_methlist: 0x21734
-  __TEXT.__const: 0x4d60
-  __TEXT.__cstring: 0x299f5
-  __TEXT.__oslogstring: 0xfd70
-  __TEXT.__gcc_except_tab: 0xa3e0
+4026.140.2.0.0
+  __TEXT.__text: 0x21b370
+  __TEXT.__objc_methlist: 0x2196c
+  __TEXT.__const: 0x4d90
+  __TEXT.__cstring: 0x29ba5
+  __TEXT.__oslogstring: 0xfee0
+  __TEXT.__gcc_except_tab: 0xa424
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x1dc
   __TEXT.__constg_swiftt: 0x32c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x9e90
+  __TEXT.__unwind_info: 0x9ee8
   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xad88
-  __DATA_CONST.__objc_classlist: 0x1118
+  __DATA_CONST.__const: 0xadd8
+  __DATA_CONST.__objc_classlist: 0x1130
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x102e8
+  __DATA_CONST.__objc_selrefs: 0x103c8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0xbb0
+  __DATA_CONST.__objc_superrefs: 0xbc8
   __DATA_CONST.__objc_arraydata: 0x818
-  __DATA_CONST.__got: 0x1e78
+  __DATA_CONST.__got: 0x1e90
   __AUTH_CONST.__const: 0x4b00
-  __AUTH_CONST.__cfstring: 0x20440
-  __AUTH_CONST.__objc_const: 0x382c0
+  __AUTH_CONST.__cfstring: 0x204a0
+  __AUTH_CONST.__objc_const: 0x38898
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xe70
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x1c70
-  __AUTH.__objc_data: 0x7040
+  __AUTH.__objc_data: 0x7130
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x222c
+  __DATA.__objc_ivar: 0x2278
   __DATA.__data: 0x2c30
   __DATA.__bss: 0x1bd0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13683
-  Symbols:   29939
-  CStrings:  5930
+  Functions: 13729
+  Symbols:   30051
+  CStrings:  5940
 
Symbols:
+ +[MPCloudEntityUpdateRegistration allLibraryAlbumsRegistration]
+ -[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]
+ -[MPCloudController unregisterForUpdatesUsingHandle:]
+ -[MPCloudController unregisterUpdatesForChannelID:reason:]
+ -[MPCloudEntityUpdate .cxx_destruct]
+ -[MPCloudEntityUpdate _initWithICUpdate:]
+ -[MPCloudEntityUpdate channelIDs]
+ -[MPCloudEntityUpdate copyWithZone:]
+ -[MPCloudEntityUpdate description]
+ -[MPCloudEntityUpdate error]
+ -[MPCloudEntityUpdate pushMessage]
+ -[MPCloudEntityUpdate resubscribeReason]
+ -[MPCloudEntityUpdate type]
+ -[MPCloudEntityUpdate unsubscribeReason]
+ -[MPCloudEntityUpdatePushMessage .cxx_destruct]
+ -[MPCloudEntityUpdatePushMessage _initWithICPushMessage:]
+ -[MPCloudEntityUpdatePushMessage channelID]
+ -[MPCloudEntityUpdatePushMessage contentType]
+ -[MPCloudEntityUpdatePushMessage copyWithZone:]
+ -[MPCloudEntityUpdatePushMessage description]
+ -[MPCloudEntityUpdatePushMessage goLiveDate]
+ -[MPCloudEntityUpdatePushMessage isRelevantForCatalogEntity]
+ -[MPCloudEntityUpdatePushMessage isRelevantForLibraryEntity]
+ -[MPCloudEntityUpdatePushMessage receivedDate]
+ -[MPCloudEntityUpdatePushMessage relevanceBitmask]
+ -[MPCloudEntityUpdatePushMessage storeID]
+ -[MPCloudEntityUpdatePushMessage storefront]
+ -[MPCloudEntityUpdateRegistration .cxx_destruct]
+ -[MPCloudEntityUpdateRegistration _icConfiguration]
+ -[MPCloudEntityUpdateRegistration channelID]
+ -[MPCloudEntityUpdateRegistration copyWithZone:]
+ -[MPCloudEntityUpdateRegistration description]
+ -[MPCloudEntityUpdateRegistration entityType]
+ -[MPCloudEntityUpdateRegistration expectedReleaseDate]
+ -[MPCloudEntityUpdateRegistration initWithChannelID:entityType:storeID:reason:expectedReleaseDate:]
+ -[MPCloudEntityUpdateRegistration observesAllLibraryAlbums]
+ -[MPCloudEntityUpdateRegistration reason]
+ -[MPCloudEntityUpdateRegistration storeID]
+ -[MPMusicPlayerApplicationController _isServiceStarted]
+ -[MPMusicPlayerApplicationController _locked_clearConnection]
+ -[MPMusicPlayerApplicationController _serverRepeatMode]
+ -[MPMusicPlayerApplicationController _serverShuffleMode]
+ -[MPMusicPlayerApplicationController _snapshot]
+ -[MPMusicPlayerController _hasXPCConnection]
+ -[MPMusicPlayerController _locked_clearConnection]
+ -[MPMusicPlayerController _locked_validateServer]
+ GCC_except_table100
+ GCC_except_table198
+ OBJC_IVAR_$_MPCloudEntityUpdate._channelIDs
+ OBJC_IVAR_$_MPCloudEntityUpdate._error
+ OBJC_IVAR_$_MPCloudEntityUpdate._pushMessage
+ OBJC_IVAR_$_MPCloudEntityUpdate._resubscribeReason
+ OBJC_IVAR_$_MPCloudEntityUpdate._type
+ OBJC_IVAR_$_MPCloudEntityUpdate._unsubscribeReason
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._channelID
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._contentType
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._goLiveDate
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._receivedDate
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._relevanceBitmask
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._storeID
+ OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._storefront
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._channelID
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._entityType
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._expectedReleaseDate
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._observesAllLibraryAlbums
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._reason
+ OBJC_IVAR_$_MPCloudEntityUpdateRegistration._storeID
+ _OBJC_CLASS_$_ICCloudAPNSChannelRegistrationConfiguration
+ _OBJC_CLASS_$_ICCloudEntityUpdateRegistrationToken
+ _OBJC_CLASS_$_MPCloudEntityUpdate
+ _OBJC_CLASS_$_MPCloudEntityUpdatePushMessage
+ _OBJC_CLASS_$_MPCloudEntityUpdateRegistration
+ _OBJC_METACLASS_$_MPCloudEntityUpdate
+ _OBJC_METACLASS_$_MPCloudEntityUpdatePushMessage
+ _OBJC_METACLASS_$_MPCloudEntityUpdateRegistration
+ __49-[MPMusicPlayerController _locked_validateServer]_block_invoke
+ __MRMediaRemoteNowPlayingMediaTypeForMPNowPlayingMediaType
+ __OBJC_$_CLASS_METHODS_MPCloudEntityUpdateRegistration
+ __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdate
+ __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdatePushMessage
+ __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdateRegistration
+ __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdate
+ __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdatePushMessage
+ __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdateRegistration
+ __OBJC_$_PROP_LIST_MPCloudEntityUpdate
+ __OBJC_$_PROP_LIST_MPCloudEntityUpdatePushMessage
+ __OBJC_$_PROP_LIST_MPCloudEntityUpdateRegistration
+ __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdate
+ __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdatePushMessage
+ __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdateRegistration
+ __OBJC_CLASS_RO_$_MPCloudEntityUpdate
+ __OBJC_CLASS_RO_$_MPCloudEntityUpdatePushMessage
+ __OBJC_CLASS_RO_$_MPCloudEntityUpdateRegistration
+ __OBJC_METACLASS_RO_$_MPCloudEntityUpdate
+ __OBJC_METACLASS_RO_$_MPCloudEntityUpdatePushMessage
+ __OBJC_METACLASS_RO_$_MPCloudEntityUpdateRegistration
+ ___49-[MPMusicPlayerController _locked_validateServer]_block_invoke
+ ___88-[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]_block_invoke
+ ___88-[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e29_v16?0"ICCloudEntityUpdate"8ls32l8
+ ___block_descriptor_40_e8_32bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16ls32l8
+ _kMRMediaRemoteMediaTypeAudioBook
+ _kMRMediaRemoteMediaTypeITunesRadio
+ _kMRMediaRemoteMediaTypeITunesU
+ _kMRMediaRemoteMediaTypeMusic
+ _kMRMediaRemoteMediaTypePodcast
+ _kMRMediaRemoteNowPlayingInfoMediaType
+ _kMRMediaRemoteNowPlayingInfoTypeAudio
+ _kMRMediaRemoteNowPlayingInfoTypeVideo
+ _objc_msgSend$_hasXPCConnection
+ _objc_msgSend$_icConfiguration
+ _objc_msgSend$_initWithICPushMessage:
+ _objc_msgSend$_initWithICUpdate:
+ _objc_msgSend$_isServiceStarted
+ _objc_msgSend$_locked_clearConnection
+ _objc_msgSend$_locked_validateServer
+ _objc_msgSend$allLibraryAlbumsConfiguration
+ _objc_msgSend$channelID
+ _objc_msgSend$channelIDs
+ _objc_msgSend$contentType
+ _objc_msgSend$goLiveDate
+ _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:
+ _objc_msgSend$pushMessage
+ _objc_msgSend$receivedDate
+ _objc_msgSend$registerForUpdatesWithConfiguration:updateHandler:completionHandler:
+ _objc_msgSend$relevanceBitmask
+ _objc_msgSend$resubscribeReason
+ _objc_msgSend$snapshotWithElapsedTime:duration:rate:atTimestamp:state:
+ _objc_msgSend$storefront
+ _objc_msgSend$unregisterForUpdatesToMonitoredEntityUsingToken:
+ _objc_msgSend$unregisterUpdatesForChannelID:reason:
+ _objc_msgSend$unsubscribeReason
- -[MPMusicPlayerApplicationController _clearConnection]
- -[MPMusicPlayerController _validateServer]
- GCC_except_table170
- GCC_except_table174
- GCC_except_table193
- GCC_except_table69
- GCC_except_table73
- _MRNowPlayingInfoContentTypeBook
- _MRNowPlayingInfoContentTypeGeneric
- _MRNowPlayingInfoContentTypeMusic
- _MRNowPlayingInfoContentTypePodcast
- _MRNowPlayingInfoContentTypeRadio
- _MRNowPlayingInfoMediaTypeAudio
- _MRNowPlayingInfoMediaTypeVideo
- __42-[MPMusicPlayerController _validateServer]_block_invoke
- __MRMediaRemoteStrictMediaTypeForMPNowPlayingMediaType
- ___42-[MPMusicPlayerController _validateServer]_block_invoke
- _kMRMediaRemoteNowPlayingInfoContentType
- _kMRMediaRemoteNowPlayingInfoStrictMediaType
- _objc_msgSend$_validateServer
CStrings:
+ "<%@ %p channelID=%@ contentType=%ld storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
+ "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ observesAllLibraryAlbums=%d>"
+ "<%@ %p type=%ld pushMessage=%@ error=%@ channelIDs=%@ unsubscribeReason=%ld resubscribeReason=%ld>"
+ "MPCloudController - register got unexpected token class %@; treating as failure."
+ "MPCloudController - unregister received handle of unexpected class %@; ignoring."
+ "MPCloudController - unregister received nil handle; ignoring."
+ "applicationQueuePlayer _establishConnectionIfNeeded post-connect retry timeout [ping did not pong]"
+ "applicationQueuePlayer:xpc:connect:wake:retry"
+ "v16@?0@\"ICCloudEntityUpdate\"8"
+ "v24@?0@\"ICCloudEntityUpdateRegistrationToken\"8@\"NSError\"16"
```
