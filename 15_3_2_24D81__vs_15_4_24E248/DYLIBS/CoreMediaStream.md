## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/Versions/A/CoreMediaStream`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0xd1348
-  __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x6478
+751.0.104.0.0
+  __TEXT.__text: 0xd1188
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x74c0
   __TEXT.__const: 0x1eb
-  __TEXT.__gcc_except_tab: 0x2a78
   __TEXT.__cstring: 0x9ff1
-  __TEXT.__oslogstring: 0xe865
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x2858
+  __TEXT.__gcc_except_tab: 0x2c18
+  __TEXT.__oslogstring: 0xe865
+  __TEXT.__unwind_info: 0x2878
   __TEXT.__objc_classname: 0x813
   __TEXT.__objc_methname: 0x12951
   __TEXT.__objc_methtype: 0x4265

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d00
+  __DATA_CONST.__objc_selrefs: 0x3e90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x6e8
   __AUTH_CONST.__const: 0x2380
   __AUTH_CONST.__cfstring: 0x8020
-  __AUTH_CONST.__objc_const: 0xa648
+  __AUTH_CONST.__objc_const: 0x8728
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x650

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 71CF53DA-85C2-32CD-B43C-5B6634736DDE
-  Functions: 3358
-  Symbols:   7181
+  UUID: BCA7C224-C488-37A1-A492-D9DCA96D33CC
+  Functions: 3352
+  Symbols:   7184
   CStrings:  6262
 
Symbols:
+ GCC_except_table1002
+ GCC_except_table1003
+ GCC_except_table1006
+ GCC_except_table1012
- _strcmp
Functions:
~ _MSASPlatform : 80 -> 72
~ -[MSASModelBase initWithPersonID:databasePath:currentVersion:] : 588 -> 580
~ -[MSMediaStreamDaemon nextActivityDate] : 252 -> 248
~ -[MSPublisher publishStorageProtocolDidFinishPublishingAllAssets:] : 4420 -> 4448
~ -[MSPublisher publishStorageProtocol:didRequestFDForAsset:] : 1496 -> 1500
~ -[MSPublisher submitAssetCollectionsForPublication:skipAssetCollections:] : 3852 -> 3776
~ -[MSPublisher publish] : 716 -> 760
- sub_1bdb10de8
~ -[MSSubscriber reauthorizationProtocol:reauthorizedAssets:rejectedAssets:error:] : 1492 -> 1476
~ -[MSSubscriber _stopOutSubscriberState:outRetrievalState:] : 316 -> 320
- sub_1bdb162dc
~ -[MSSubscriber _didFinishRetrievingSubscriptionUpdate] : 272 -> 276
~ -[MSAsset hash] : 96 -> 84
~ -[MSAssetCollection encodeWithCoder:] : 264 -> 268
~ -[MSAssetCollection setDerivedAssets:] : 336 -> 332
~ _MSSHA1HashForData : 280 -> 268
~ ___38-[NSError(MSErrorUtilities) MSIsFatal]_block_invoke : 384 -> 380
~ ___43-[NSError(MSErrorUtilities) MSNeedsBackoff]_block_invoke : 284 -> 280
~ -[NSString(MSStringUtilities) MSHexData] : 320 -> 316
~ -[NSData(MSDataUtilities) MSInitWithBase64Encoding:] : 664 -> 672
~ -[MSPublishStreamsProtocol sendUploadCompleteForAssetCollections:] : 564 -> 560
~ -[MSPublishStreamsProtocol sendMetadataForAssetCollections:] : 1368 -> 1364
~ -[MSSubscribeStreamsProtocol _assetCollectionsFromCoreArray:personID:outError:] : 1424 -> 1420
~ -[MSSubscribeStreamsProtocol pollForSubscriptionUpdatesWithAccountAnchors:] : 448 -> 444
~ -[MSPublishMMCSProtocol publishAssets:URL:] : 1136 -> 1144
~ -[MSSubscribeMMCSProtocol retrieveAssets:] : 2192 -> 2200
- _MSSSPCChunkParsingInitialize
~ __performNextStateAction : 2300 -> 2312
- sub_1bdb2b32c
~ _MPSStateResponseReadFrom : 1048 -> 1052
- sub_1bdb2cc58
~ -[MPSStateResponse icplActionAsString:] : 100 -> 112
~ -[MPSStateResponse mpsActionAsString:] : 100 -> 112
~ _MSSPCStartHTTPTransaction : 2476 -> 2452
~ _MSSPCCreateHexStringFromData : 240 -> 248
~ _MSPCUNumberFormatterWithSystemLocale : 68 -> 72
~ _MPSStateRequestReadFrom : 724 -> 744
- sub_1bdb30e74
~ _MSMMCSHashForData : 184 -> 180
~ _MSMMCSHashForFD : 288 -> 296
~ -[MSServerSideConfigProtocol queryConfiguration] : 20 -> 16
~ -[MSReauthorizationProtocol requestReauthorizationForAssets:] : 664 -> 660
~ -[MSObjectQueue commitObjectsWrappers:] : 1352 -> 1348
~ -[MSObjectQueue dealloc] : 240 -> 232
~ -[MSObjectQueue initWithPath:] : 1176 -> 1172
~ -[MSDeleteStreamsProtocol sendDeletionRequestForAssetCollections:] : 704 -> 700
~ _didFinish.3409 : 972 -> 968
~ -[MSASAlbum description] : 508 -> 512
~ -[MSASAssetCollection isAutoloopVideo] : 84 -> 140
~ -[MSASAssetCollection isPhotoIris] : 68 -> 116
~ -[MSASAssetCollection setMetadata:] : 408 -> 472
~ -[MSASAssetCollection encodeWithCoder:] : 1220 -> 1272
~ -[MSASAssetCollection description] : 796 -> 792
~ -[MSAlbumSharingDaemon workQueueForgetEverythingAboutPersonID:completionBlock:] : 712 -> 704
~ ___79-[MSAlbumSharingDaemon workQueueForgetEverythingAboutPersonID:completionBlock:]_block_invoke_2 : 228 -> 248
~ ___79-[MSAlbumSharingDaemon workQueueForgetEverythingAboutPersonID:completionBlock:]_block_invoke_3 : 344 -> 368
~ ___105-[MSAlbumSharingDaemon mapQueueShutDownStateMachineInMap:personIDs:index:forDestruction:completionBlock:]_block_invoke : 228 -> 244
~ -[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:] : 1152 -> 1128
~ __72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.414 : 400 -> 420
~ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke_2 : 3016 -> 3044
~ __72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.417 : 380 -> 376
~ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke : 980 -> 976
~ __90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.395 : 1196 -> 1188
~ __90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.396 : 896 -> 884
~ __90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.397 : 696 -> 688
~ ___71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke : 1132 -> 1128
~ __71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke.386 : 700 -> 684
~ ___81-[MSASStateMachine setMultipleContributorsEnabled:forAlbum:info:completionBlock:]_block_invoke : 516 -> 504
~ __81-[MSASStateMachine setMultipleContributorsEnabled:forAlbum:info:completionBlock:]_block_invoke.385 : 312 -> 304
~ ___73-[MSASStateMachine setPublicAccessEnabled:forAlbum:info:completionBlock:]_block_invoke : 516 -> 504
~ __73-[MSASStateMachine setPublicAccessEnabled:forAlbum:info:completionBlock:]_block_invoke.380 : 312 -> 304
~ -[MSASStateMachine _addCommentDisposition:params:] : 1408 -> 1376
~ __50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.362 : 388 -> 408
~ -[MSASStateMachine _removeSharingRelationshipsDisposition:params:] : 908 -> 892
~ ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke : 320 -> 332
~ ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke_2 : 1016 -> 1036
~ __66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke.354 : 348 -> 344
~ __66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke_2.356 : 484 -> 480
~ -[MSASStateMachine _addSharingRelationshipsDisposition:params:] : 908 -> 892
~ ___63-[MSASStateMachine _addSharingRelationshipsDisposition:params:]_block_invoke : 408 -> 424
~ __63-[MSASStateMachine _addSharingRelationshipsDisposition:params:]_block_invoke.350 : 212 -> 232
~ ___63-[MSASStateMachine _addSharingRelationshipsDisposition:params:]_block_invoke_2 : 1068 -> 1044
~ -[MSASStateMachine _sendGetUploadTokensDisposition:params:] : 1320 -> 1304
~ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke : 340 -> 360
~ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2 : 1612 -> 1592
~ __59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke.338 : 140 -> 136
~ __59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2.339 : 292 -> 284
~ -[MSASStateMachine _sendPutAssetCollectionsDisposition:params:] : 1192 -> 1188
~ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke : 400 -> 392
~ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2 : 3480 -> 3460
~ __63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke.327 : 580 -> 572
~ __63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2.328 : 336 -> 328
~ __63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_3.331 : 396 -> 388
~ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_4 : 280 -> 272
~ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_5 : 440 -> 420
~ -[MSASStateMachine _sendUploadCompleteDisposition:params:] : 1948 -> 1944
~ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke : 440 -> 456
~ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2 : 3712 -> 3636
~ __58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke.319 : 140 -> 136
~ __58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.320 : 200 -> 196
~ __58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.322 : 1008 -> 996
~ -[MSASStateMachine _updateAlbumDisposition:params:] : 896 -> 884
~ ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke : 300 -> 316
~ ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke_2 : 1024 -> 1008
~ __51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke.302 : 140 -> 136
~ __51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke_2.304 : 248 -> 244
~ -[MSASStateMachine _createAlbumDisposition:params:] : 768 -> 756
~ ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke : 380 -> 372
~ ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke_2 : 1052 -> 1036
~ __51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke.293 : 140 -> 136
~ __51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke_2.295 : 248 -> 244
~ -[MSASStateMachine _deleteCommentDisposition:params:] : 1320 -> 1288
~ __53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.285 : 340 -> 364
~ ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke_2 : 1104 -> 1096
~ __53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.286 : 144 -> 140
~ __53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.287 : 144 -> 140
~ -[MSASStateMachine _deleteAssetCollectionsDisposition:params:] : 964 -> 948
~ ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke : 300 -> 316
~ ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke_2 : 1132 -> 1124
~ __62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke.280 : 348 -> 344
~ __62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke_2.282 : 448 -> 444
~ -[MSASStateMachine _deleteAlbumDisposition:params:] : 768 -> 756
~ ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke : 280 -> 264
~ ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke_2 : 1008 -> 1000
~ __51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke.275 : 140 -> 136
~ __51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke_2.277 : 248 -> 244
~ -[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:] : 1184 -> 1168
~ __69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke.267 : 388 -> 372
~ ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke_2 : 892 -> 920
~ -[MSASStateMachine _setAlbumSyncedStateDisposition:params:] : 1352 -> 1340
~ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke_2 : 840 -> 884
~ -[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:] : 1088 -> 1084
~ ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_2 : 360 -> 356
~ __64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke.246 : 888 -> 880
~ __64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke.247 : 144 -> 140
~ __64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_2.248 : 232 -> 220
~ ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_3 : 144 -> 140
~ -[MSASStateMachine _checkForCommentChangesDisposition:params:] : 1320 -> 1304
~ __62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.231 : 376 -> 388
~ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke_2 : 1100 -> 1092
~ __62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.232 : 356 -> 352
~ __62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke_2.234 : 344 -> 336
~ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke_3 : 652 -> 648
~ -[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:] : 1512 -> 1468
~ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke_2 : 400 -> 392
~ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke_3 : 1212 -> 1200
~ __70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.218 : 140 -> 136
~ -[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:] : 772 -> 760
~ ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke : 1004 -> 988
~ __68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke.200 : 140 -> 136
~ ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke_2 : 248 -> 244
~ -[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:] : 864 -> 848
~ ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke : 1068 -> 1060
~ __68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke.196 : 140 -> 136
~ ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke_2 : 252 -> 248
~ -[MSASStateMachine _unsubscribeFromAlbumDisposition:params:] : 792 -> 780
~ ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke : 300 -> 316
~ ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke_2 : 1020 -> 1012
~ __60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke.188 : 140 -> 136
~ __60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke_2.190 : 248 -> 244
~ -[MSASStateMachine _subscribeToAlbumDisposition:params:] : 768 -> 756
~ ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke : 280 -> 264
~ ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke_2 : 1012 -> 996
~ __56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke.179 : 140 -> 136
~ __56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke_2.181 : 248 -> 244
~ -[MSASStateMachine _getAccessControlsDisposition:params:] : 1140 -> 1116
~ __57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.170 : 352 -> 368
~ ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke_2 : 956 -> 940
~ __57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.171 : 144 -> 140
~ __57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.172 : 144 -> 140
~ -[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:] : 1488 -> 1456
~ ___62-[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:]_block_invoke_2 : 468 -> 456
~ ___62-[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:]_block_invoke_3 : 2428 -> 2408
~ __62-[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:]_block_invoke.162 : 148 -> 144
~ __62-[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:]_block_invoke.163 : 408 -> 404
~ __62-[MSASStateMachine _checkForUpdatesInAlbumDisposition:params:]_block_invoke_2.165 : 220 -> 216
~ -[MSASStateMachine _checkForChangesDisposition:params:] : 876 -> 868
~ ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke : 480 -> 472
~ ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke_2 : 2248 -> 2244
~ __55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke.139 : 140 -> 136
~ __55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke.148 : 136 -> 132
~ -[MSASStateMachine workQueuePerformNextCommand] : 1616 -> 1612
~ ___60-[MSASStateMachine MSBackoffManagerDidUpdateNextExpiryDate:]_block_invoke : 532 -> 536
~ ___60-[MSASStateMachine MSBackoffManagerDidUpdateNextExpiryDate:]_block_invoke_2 : 564 -> 556
~ -[MSASStateMachine latestNextActivityDate] : 628 -> 624
~ ___78-[MSASStateMachine _serverSideConfigDictionaryByApplyingDefaultsToDictionary:]_block_invoke : 680 -> 696
~ -[MSASStateMachine setPendingRootCtag:] : 412 -> 416
~ ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke_2 : 692 -> 684
~ -[MSASStateMachine _workQueueEmptyFileTransferQueuesCompletionBlock:] : 260 -> 252
~ ___48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke : 180 -> 176
~ __48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke.42 : 336 -> 328
~ __48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke.47 : 336 -> 328
~ __48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke.51 : 444 -> 428
~ __48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke_2.48 : 328 -> 316
~ __48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke_2.43 : 200 -> 188
~ ___57-[MSASPersonModel enqueueAssetCollectionForUpload:album:]_block_invoke : 1356 -> 1348
~ ___59-[MSASPersonModel enqueueAssetForDownload:inAlbumWithGUID:]_block_invoke : 1492 -> 1488
~ -[MSASPersonModel dbQueueIsGUIDQueued:inQueue:] : 456 -> 460
~ -[MSASPersonModel dbQueueIsAssetCollectionWithGUIDPending:] : 176 -> 188
~ ___54-[MSASPersonModel setParams:forCommandWithIdentifier:]_block_invoke : 736 -> 732
~ -[MSASModelBase dbQueuePersistentDataForKey:] : 572 -> 568
~ ___56-[MSASModelBase shutDownForDestruction:completionBlock:]_block_invoke_2 : 216 -> 208
~ +[MSFileUtilities hardlinkOrCopyFileFromPath:toPath:outError:] : 736 -> 728
~ -[MMCSEngine _initItemIDPersistence] : 144 -> 136
~ ___48-[MMCSEngine putAssets:requestURL:DSID:options:]_block_invoke : 1300 -> 1296
~ ___48-[MMCSEngine getAssets:requestURL:DSID:options:]_block_invoke : 1216 -> 1224
~ ___56-[MMCSEngine registerAssets:forDownloadCompletionBlock:]_block_invoke : 412 -> 416
~ ___53-[MMCSEngine registerAssetForUpload:completionBlock:]_block_invoke : 564 -> 568
~ ___42-[MMCSEngine cancelOperationsWithContext:]_block_invoke : 140 -> 128
~ -[MMCSEngine _requestCompletedRequestorContext:] : 472 -> 460
~ -[MMCSEngine _getFileDescriptorAndContentTypeFromItemID:outFD:outItemType:outError:] : 688 -> 680
~ ___36-[NSError(MMCSKit) MMCSIsFatalError]_block_invoke : 200 -> 196
~ ___71-[MSASAssetUploader MMCSEngine:didFinishPuttingAsset:putReceipt:error:]_block_invoke : 2608 -> 2612
~ ___85-[MSASAssetUploader workQueueRegisterAssetCollections:index:results:completionBlock:]_block_invoke : 296 -> 312
~ -[MSASAssetUploader workQueueUploadNextBatch] : 3896 -> 3884
~ -[MSASAssetUploader _workQueueStop] : 112 -> 104
~ ___48-[MSASAssetDownloader didFinishGettingAllAssets]_block_invoke : 916 -> 904
~ ___63-[MSASAssetDownloader workQueueRegisterAssets:completionBlock:]_block_invoke : 100 -> 92
~ ___54-[MSASAssetDownloader registerAssets:completionBlock:]_block_invoke_2 : 100 -> 92
~ ___47-[MSASAssetTransferer shutDownCompletionBlock:]_block_invoke_2 : 100 -> 92
~ +[MSProtocolUtilities fetchMPSStateWithBaseAvailabilityURL:personID:originalLibrarySize:completionBlock:] : 1876 -> 1852
~ +[MSProtocolUtilities Win32SHA1OfUDID:] : 328 -> 324
~ -[MSASSharingRelationship redactedDescription] : 316 -> 320
~ -[MSASSharingRelationship description] : 452 -> 456
~ -[MSASSharingRelationship isEqualToSharingRelationship:] : 996 -> 988
~ -[MSASComment description] : 796 -> 764
~ -[MSASModelEnumerator initWithDatabase:query:stepBlock:] : 408 -> 396
~ ___100-[MSASServerSideModel MSASStateMachine:didFinishAddingComment:toAssetCollection:inAlbum:info:error:]_block_invoke_2 : 224 -> 240
~ ___103-[MSASServerSideModel MSASStateMachine:didFinishRemovingSharingRelationship:fromOwnedAlbum:info:error:]_block_invoke : 204 -> 224
~ ___98-[MSASServerSideModel MSASStateMachine:didFinishSendingInvitationByPhone:toOwnedAlbum:info:error:]_block_invoke : 228 -> 248
~ ___90-[MSASServerSideModel MSASStateMachine:didFinishAddingAssetCollection:toAlbum:info:error:]_block_invoke_2 : 204 -> 224
~ ___110-[MSASServerSideModel MSASStateMachine:didRequestAssetsForAddingAssetCollections:inAlbum:specifications:info:]_block_invoke : 324 -> 340
~ ___74-[MSASServerSideModel MSASStateMachine:didFinishUpdatingAlbum:info:error:]_block_invoke : 524 -> 536
~ ___74-[MSASServerSideModel MSASStateMachine:didFinishCreatingAlbum:info:error:]_block_invoke_2 : 184 -> 196
~ ___102-[MSASServerSideModel MSASStateMachine:didFinishDeletingComment:inAssetCollection:inAlbum:info:error:]_block_invoke : 224 -> 240
~ ___92-[MSASServerSideModel MSASStateMachine:didFinishDeletingAssetCollection:inAlbum:info:error:]_block_invoke_2 : 204 -> 224
~ ___74-[MSASServerSideModel MSASStateMachine:didFinishDeletingAlbum:info:error:]_block_invoke_2 : 184 -> 196
~ ___120-[MSASServerSideModel MSASStateMachine:didFinishSettingSyncedStateForAssetCollection:inAlbum:assetStateCtag:info:error:]_block_invoke : 128 -> 116
~ ___105-[MSASServerSideModel MSASStateMachine:didFinishSettingSyncedStateForAlbum:info:error:newAlbumStateCtag:]_block_invoke : 128 -> 116
~ ___128-[MSASServerSideModel MSASStateMachine:didFinishCheckingForCommentChangesInAssetCollectionWithGUID:largestCommentID:info:error:]_block_invoke : 148 -> 136
~ ___109-[MSASServerSideModel MSASStateMachine:didFindCommentChanges:inAssetCollectionWithGUID:inAlbumWithGUID:info:]_block_invoke : 1496 -> 1484
~ ___79-[MSASServerSideModel MSASStateMachine:didFinishRetrievingAsset:inAlbum:error:]_block_invoke : 664 -> 684
~ ___79-[MSASServerSideModel MSASStateMachine:didFinishRetrievingAsset:inAlbum:error:]_block_invoke_2 : 376 -> 392
~ ___83-[MSASServerSideModel MSASStateMachine:didFinishUnsubscribingFromAlbum:info:error:]_block_invoke_2 : 184 -> 196
~ ___83-[MSASServerSideModel MSASStateMachine:didFinishUnsubscribingFromAlbum:info:error:]_block_invoke_4 : 184 -> 196
~ ___83-[MSASServerSideModel MSASStateMachine:didFinishUnsubscribingFromAlbum:info:error:]_block_invoke_6 : 184 -> 196
~ ___79-[MSASServerSideModel MSASStateMachine:didFinishSubscribingToAlbum:info:error:]_block_invoke_2 : 204 -> 224
~ ___79-[MSASServerSideModel MSASStateMachine:didFinishSubscribingToAlbum:info:error:]_block_invoke_4 : 184 -> 196
~ ___79-[MSASServerSideModel MSASStateMachine:didFinishSubscribingToAlbum:info:error:]_block_invoke_6 : 184 -> 196
~ ___65-[MSASServerSideModel MSASStateMachine:didFindAlbumChanges:info:]_block_invoke : 3956 -> 3960
~ ___78-[MSASServerSideModel dbQueueSetUnviewedState:onAssetCollectionWithGUID:info:]_block_invoke : 192 -> 208
~ ___91-[MSASServerSideModel dbQueueSetAssetCollectionMetadataAssetCollectionGUID:key:value:info:]_block_invoke : 204 -> 224
~ ___57-[MSASServerSideModel dbQueueDeleteCommentWithGUID:info:]_block_invoke : 204 -> 224
~ ___73-[MSASServerSideModel dbQueueSetComment:forAssetCollectionWithGUID:info:]_block_invoke : 232 -> 256
~ ___73-[MSASServerSideModel dbQueueSetComment:forAssetCollectionWithGUID:info:]_block_invoke_4 : 204 -> 224
~ ___73-[MSASServerSideModel dbQueueSetComment:forAssetCollectionWithGUID:info:]_block_invoke_2 : 204 -> 224
~ ___65-[MSASServerSideModel dbQueueDeleteAssetCollectionWithGUID:info:]_block_invoke : 184 -> 196
~ ___70-[MSASServerSideModel dbQueueSetAssetCollection:inAlbumWithGUID:info:]_block_invoke : 212 -> 232
~ ___70-[MSASServerSideModel dbQueueSetAssetCollection:inAlbumWithGUID:info:]_block_invoke_4 : 184 -> 196
~ ___70-[MSASServerSideModel dbQueueSetAssetCollection:inAlbumWithGUID:info:]_block_invoke_2 : 184 -> 196
~ -[MSASServerSideModel dbQueueInvitationWithAlbumGUID:outObject:outInvitationGUID:outEmail:outUserInfoData:] : 376 -> 372
~ -[MSASServerSideModel dbQueueInvitationWithGUID:outObject:outAlbumGUID:outEmail:outUserInfoData:] : 376 -> 372
~ ___63-[MSASServerSideModel dbQueueDeleteAccessControlWithGUID:info:]_block_invoke : 184 -> 196
~ -[MSASServerSideModel dbQueueSetAccessControl:info:] : 1704 -> 1712
~ ___52-[MSASServerSideModel dbQueueSetAccessControl:info:]_block_invoke : 212 -> 232
~ ___52-[MSASServerSideModel dbQueueSetAccessControl:info:]_block_invoke_4 : 184 -> 196
~ ___52-[MSASServerSideModel dbQueueSetAccessControl:info:]_block_invoke_2 : 184 -> 196
~ ___50-[MSASServerSideModel deleteCommentWithGUID:info:]_block_invoke_2 : 204 -> 224
~ __94-[MSASServerSideModel markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:info:]_block_invoke.344 : 184 -> 196
~ ___92-[MSASServerSideModel setMultipleContributorsEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke : 344 -> 340
~ ___92-[MSASServerSideModel setMultipleContributorsEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke_2 : 640 -> 624
~ ___92-[MSASServerSideModel setMultipleContributorsEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke_4 : 368 -> 356
~ ___84-[MSASServerSideModel setPublicAccessEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke : 344 -> 340
~ ___84-[MSASServerSideModel setPublicAccessEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke_2 : 640 -> 624
~ ___84-[MSASServerSideModel setPublicAccessEnabled:forAlbumWithGUID:info:completionBlock:]_block_invoke_4 : 380 -> 368
~ ___92-[MSASServerSideModel MSASStateMachine:didFinishMarkingAsSpamInvitationForToken:info:error:]_block_invoke : 212 -> 232
~ ___92-[MSASServerSideModel MSASStateMachine:didFinishMarkingAsSpamInvitationForToken:info:error:]_block_invoke_2 : 184 -> 196
~ ___107-[MSASServerSideModel MSASStateMachine:didFinishMarkingAsSpamInvitationForAlbum:invitationGUID:info:error:]_block_invoke : 212 -> 232
~ ___107-[MSASServerSideModel MSASStateMachine:didFinishMarkingAsSpamInvitationForAlbum:invitationGUID:info:error:]_block_invoke_2 : 184 -> 216
~ ___86-[MSASServerSideModel markAlbumGUIDAsViewed:moveLastViewedAssetCollectionMarker:info:]_block_invoke : 916 -> 920
~ -[MSASServerSideModel shutDownForDestruction:completionBlock:] : 224 -> 212
~ _MSSqliteBindStringOrNull : 124 -> 136
~ ___74-[MSASProtocol getTokensForAssets:inAlbum:albumURLString:completionBlock:]_block_invoke : 1392 -> 1388
~ -[MSASProtocol deleteComment:fromAssetCollection:inAlbum:albumURLString:completionBlock:] : 1008 -> 1004
~ -[MSASProtocol addComment:toAssetCollection:inAlbum:albumURLString:completionBlock:] : 1028 -> 1024
~ -[MSASProtocol sendUploadCompleteSuccessfulAssetCollections:failedAssetCollections:album:completionBlock:] : 2248 -> 2244
~ -[MSASProtocol responseDict:containsLimitErrorCode:outMaxAllowed:] : 448 -> 444
~ ___106-[MSASProtocol getUploadTokens:forAssetCollectionWithGUID:inAlbumWithGUID:albumURLString:completionBlock:]_block_invoke : 1028 -> 1024
~ ___77-[MSASProtocol putAssetCollections:intoAlbum:albumURLString:completionBlock:]_block_invoke : 3812 -> 3800
~ ___44-[MSASProtocol createAlbum:completionBlock:]_block_invoke : 1512 -> 1516
~ ___91-[MSASProtocol _sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:]_block_invoke_2 : 2588 -> 2572
~ ___91-[MSASProtocol sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:]_block_invoke : 972 -> 964
~ ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_9 : 700 -> 696
~ ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_7 : 700 -> 696
~ ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_5 : 800 -> 808
~ __65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_3.107 : 800 -> 808
~ __65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke.101 : 800 -> 808
~ __65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_3.96 : 800 -> 808
~ __65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke.90 : 700 -> 696
~ ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke_2 : 700 -> 696
~ ___50-[MSASGroupedQueue shutDownFlush:completionBlock:]_block_invoke : 120 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/coremediastream/MSPerformanceLogger.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/coremediastream/MSPerformanceLogger.m"

```
