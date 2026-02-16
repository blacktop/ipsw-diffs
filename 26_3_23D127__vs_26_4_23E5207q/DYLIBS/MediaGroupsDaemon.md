## MediaGroupsDaemon

> `/System/Library/PrivateFrameworks/MediaGroupsDaemon.framework/MediaGroupsDaemon`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0x24e44
-  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__text: 0x267f8
+  __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_methlist: 0x222c
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0x1118
   __TEXT.__oslogstring: 0x21a2
-  __TEXT.__gcc_except_tab: 0xc20
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_classname: 0x520
   __TEXT.__objc_methname: 0x47c8
   __TEXT.__objc_methtype: 0x1335

   __DATA_CONST.__objc_selrefs: 0x13b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0xf40
   __AUTH_CONST.__objc_const: 0x3ab0

   - /System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44ECD467-EBB0-3F54-BAAF-39BB4F754926
+  UUID: BEB21D52-242B-36EF-8A07-8ED4DA51CCCB
   Functions: 778
-  Symbols:   3048
+  Symbols:   3042
   CStrings:  1564
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
Functions:
~ +[MGRemoteQueryClientHandlerQuery handlerWithQuery:forGroupsQueryAgent:] : 112 -> 108
~ -[MGRemoteQueryClientHandlerQuery _initWithQuery:groupsQueryAgent:] : 168 -> 164
~ -[MGRemoteQueryClientHandlerQuery description] : 192 -> 212
~ -[MGRemoteQueryClientHandlerQuery prepareURL:] : 276 -> 304
~ -[MGRemoteQueryClientHandlerQuery validateResponse:] : 196 -> 204
~ -[MGRemoteQueryClientHandlerQuery handleCompleteResponse:jsonPayload:] : 1080 -> 1128
~ -[MGRemoteQueryClientHandlerPing description] : 124 -> 132
~ -[MGRemoteQueryClientHandlerPing handleCompleteResponse:jsonPayload:] : 328 -> 336
~ -[MGRemoteQueryClientBrowser initWithDelegate:dispatchQueue:] : 336 -> 348
~ -[MGRemoteQueryClientBrowser description] : 204 -> 220
~ -[MGRemoteQueryClientBrowser _startBrowsing] : 532 -> 564
~ -[MGRemoteQueryClientBrowser _invalidate] : 360 -> 372
~ -[MGRemoteQueryClientBrowser _invalidated] : 268 -> 276
~ ___42-[MGRemoteQueryClientBrowser _invalidated]_block_invoke : 120 -> 128
~ -[MGRemoteQueryClientBrowser _prepareBrowseDescriptor] : 120 -> 124
~ -[MGRemoteQueryClientBrowser _prepareBrowseParameters] : 108 -> 112
~ -[MGRemoteQueryClientBrowser _prepareBrowserHandlers] : 468 -> 476
~ ___53-[MGRemoteQueryClientBrowser _prepareBrowserHandlers]_block_invoke : 312 -> 316
~ ___53-[MGRemoteQueryClientBrowser _prepareBrowserHandlers]_block_invoke.9 : 468 -> 476
~ -[MGRemoteQueryClientBrowser _handleBrowseChangeFromTarget:toTarget:applyBatch:] : 444 -> 456
~ -[MGRemoteQueryClientBrowser _applyUpdates] : 728 -> 748
~ -[MGRemoteQueryClientBrowser _targetForBrowseResult:] : 520 -> 532
~ -[MGRemoteQueryClientBrowser setBrowser:] : 12 -> 64
~ -[MGRemoteQueryClientBrowser setKnownTargets:] : 12 -> 64
~ -[MGRemoteQueryClientBrowser setUpdatedTargets:] : 12 -> 64
~ -[MGRemoteQueryClientBrowser setError:] : 12 -> 64
~ -[MGRemoteQueryReply _initWithGroups:error:] : 156 -> 152
~ -[MGRemoteQueryReply description] : 184 -> 200
~ -[MGGroupsMediator dealloc] : 92 -> 96
~ -[MGGroupsMediator copyWithZone:] : 4 -> 40
~ -[MGGroupsMediator groups_unsafe] : 60 -> 68
~ -[MGGroupsMediator upsertGroup_unsafe:] : 160 -> 168
~ -[MGGroupsMediator removeGroup:ifExists_unsafe:] : 212 -> 224
~ -[MGGroupsMediator groupsForUpdate_unsafe] : 136 -> 144
~ -[MGGroupsMediator description] : 524 -> 536
~ ___31-[MGGroupsMediator description]_block_invoke : 104 -> 108
~ -[MGGroupsMediator currentGroups] : 256 -> 252
~ ___33-[MGGroupsMediator currentGroups]_block_invoke : 160 -> 168
~ -[MGGroupsMediator startActivityWithName:] : 208 -> 216
~ ___42-[MGGroupsMediator startActivityWithName:]_block_invoke : 112 -> 120
~ -[MGGroupsMediator endActivity:] : 312 -> 316
~ ___32-[MGGroupsMediator endActivity:]_block_invoke : 188 -> 196
~ -[MGGroupsMediator addGroup:] : 312 -> 316
~ ___29-[MGGroupsMediator addGroup:]_block_invoke : 128 -> 132
~ -[MGGroupsMediator removeGroup:] : 312 -> 316
~ ___32-[MGGroupsMediator removeGroup:]_block_invoke : 132 -> 136
~ -[MGGroupsMediator group:renameTo:] : 504 -> 492
~ ___35-[MGGroupsMediator group:renameTo:]_block_invoke : 408 -> 444
~ -[MGGroupsMediator group:addMember:] : 500 -> 488
~ ___36-[MGGroupsMediator group:addMember:]_block_invoke : 484 -> 532
~ -[MGGroupsMediator group:removeMember:] : 500 -> 488
~ ___39-[MGGroupsMediator group:removeMember:]_block_invoke : 484 -> 528
~ ___46-[MGGroupsMediator removeGroupWithIdentifier:]_block_invoke : 108 -> 116
~ -[MGGroupsActivity initWithName:] : 284 -> 288
~ -[MGGroupsActivity dealloc] : 316 -> 332
~ -[MGGroupsActivity description] : 176 -> 192
~ -[MGRemoteQueryServer initWithHomeHash:delegate:dispatchQueue:] : 344 -> 348
~ -[MGRemoteQueryServer description] : 232 -> 248
~ -[MGRemoteQueryServer _startListener] : 596 -> 632
~ -[MGRemoteQueryServer _invalidate] : 396 -> 412
~ -[MGRemoteQueryServer _invalidated] : 268 -> 276
~ ___35-[MGRemoteQueryServer _invalidated]_block_invoke : 120 -> 128
~ -[MGRemoteQueryServer _prepareListenerParameters] : 204 -> 212
~ -[MGRemoteQueryServer _prepareListenerTLS] : 176 -> 180
~ ___42-[MGRemoteQueryServer _prepareListenerTLS]_block_invoke : 144 -> 148
~ -[MGRemoteQueryServer _prepareListenerIdentity] : 112 -> 116
~ -[MGRemoteQueryServer _prepareListenerHTTP:] : 132 -> 136
~ -[MGRemoteQueryServer _prepareListenerAdvertisement] : 420 -> 436
~ -[MGRemoteQueryServer _prepareListenerHandlers] : 468 -> 476
~ ___47-[MGRemoteQueryServer _prepareListenerHandlers]_block_invoke : 312 -> 316
~ -[MGRemoteQueryServer _handleNewConnection:] : 752 -> 776
~ ___44-[MGRemoteQueryServer _handleNewConnection:]_block_invoke : 200 -> 216
~ ___44-[MGRemoteQueryServer _handleNewConnection:]_block_invoke_2 : 468 -> 480
~ -[MGRemoteQueryServer _clientAdd:] : 440 -> 460
~ -[MGRemoteQueryServer _clientFind:] : 564 -> 592
~ -[MGRemoteQueryServer _clientRemove:] : 336 -> 348
~ -[MGRemoteQueryServer clientLostTransaction:] : 136 -> 140
~ -[MGRemoteQueryServer _transactionCount] : 72 -> 76
~ -[MGRemoteQueryServer _unsafe_transactionCount] : 256 -> 260
~ -[MGRemoteQueryServer _updateConnectionLimit] : 156 -> 168
~ -[MGRemoteQueryServer _connectionLimit] : 240 -> 248
~ -[MGRemoteQueryServer setListener:] : 12 -> 64
~ -[MGRemoteQueryServer setClients:] : 12 -> 64
~ -[MGRemoteQueryServer setError:] : 12 -> 64
~ +[MGRemoteQueryClientWatchdog watchdogForTarget:dispatchQueue:delegate:usingSession:] : 160 -> 148
~ -[MGRemoteQueryClientWatchdog _initWithTarget:dispatchQueue:delegate:usingSession:] : 336 -> 328
~ -[MGRemoteQueryClientWatchdog description] : 200 -> 220
~ -[MGRemoteQueryClientWatchdog reset] : 136 -> 140
~ -[MGRemoteQueryClientWatchdog pingClient] : 256 -> 252
~ ___41-[MGRemoteQueryClientWatchdog pingClient]_block_invoke : 76 -> 80
~ -[MGRemoteQueryClientWatchdog _timerInit] : 296 -> 308
~ -[MGRemoteQueryClientWatchdog _timerReschedule] : 136 -> 144
~ -[MGRemoteQueryClientWatchdog _timerCancel] : 68 -> 72
~ -[MGRemoteQueryClientWatchdog _timerFired] : 236 -> 248
~ -[MGRemoteQueryClientWatchdog _pingStart] : 144 -> 148
~ ___41-[MGRemoteQueryClientWatchdog _pingStart]_block_invoke : 496 -> 532
~ -[MGRemoteQueryClientWatchdog _pingFinished:] : 444 -> 460
~ -[MGRemoteQueryClientWatchdog clientInvalidated:withError:] : 216 -> 208
~ ___59-[MGRemoteQueryClientWatchdog clientInvalidated:withError:]_block_invoke : 420 -> 424
~ ___59-[MGRemoteQueryClientWatchdog clientInvalidated:withError:]_block_invoke_2 : 100 -> 104
~ -[MGRemoteQueryClientWatchdog ping] : 60 -> 68
~ -[MGRemoteQueryClientWatchdog setPing:] : 124 -> 132
~ -[MGRemoteQueryServerHandlerQuery _initWithRequest:] : 128 -> 120
~ -[MGRemoteQueryServerHandlerQuery description] : 176 -> 192
~ +[MGRemoteQueryServerHandlerQuery urlPath] : 12 -> 60
~ -[MGRemoteQueryServerHandlerQuery validateRequest] : 196 -> 220
~ -[MGRemoteQueryServerHandlerQuery prepareResponse:] : 228 -> 244
~ -[MGRemoteQueryServerHandlerQuery _requestParse] : 640 -> 672
~ -[MGRemoteQueryServerHandlerQuery _queryStart] : 800 -> 840
~ ___46-[MGRemoteQueryServerHandlerQuery _queryStart]_block_invoke : 120 -> 116
~ -[MGRemoteQueryServerHandlerQuery _queryHandleResults:error:] : 332 -> 312
~ ___61-[MGRemoteQueryServerHandlerQuery _queryHandleResults:error:]_block_invoke : 112 -> 116
~ -[MGRemoteQueryServerHandlerQuery _querySendResults] : 1012 -> 1048
~ ___52-[MGRemoteQueryServerHandlerQuery _querySendResults]_block_invoke : 496 -> 516
~ -[MGRemoteQueryServerHandlerQuery queryGroups] : 60 -> 68
~ -[MGRemoteQueryServerHandlerQuery setQueryGroups:] : 124 -> 132
~ -[MGRemoteQueryServerHandlerQuery queryError] : 60 -> 68
~ -[MGRemoteQueryServerHandlerQuery setQueryError:] : 124 -> 132
~ -[MGRemoteQueryServerHandlerQuery setRequestPredicate:] : 12 -> 64
~ -[MGRemoteQueryServerHandlerQuery setResponseBoundary:] : 12 -> 64
~ -[MGRemoteQueryServerHandlerQuery setQuery:] : 12 -> 64
~ -[MGRemoteQueryServerHandlerPing _initWithRequest:] : 116 -> 108
~ -[MGRemoteQueryServerHandlerPing description] : 124 -> 132
~ +[MGRemoteQueryServerHandlerPing urlPath] : 12 -> 60
~ -[MGRemoteQueryServerHandlerPing validateRequest] : 140 -> 156
~ -[MGRemoteQueryServerHandlerPing prepareResponse:] : 256 -> 272
~ -[MGRemoteQueryServerHandlerPing provideResponseData:] : 164 -> 168
~ -[MGRemoteQueryServerHandlerPing setResponsePayload:] : 12 -> 64
~ +[MGRemoteQueryClient clientWithHandler:target:dispatchQueue:delegate:usingSession:] : 180 -> 164
~ -[MGRemoteQueryClient _initWithHandler:target:dispatchQueue:delegate:session:] : 444 -> 436
~ -[MGRemoteQueryClient description] : 248 -> 272
~ -[MGRemoteQueryClient _prepareConnection:] : 664 -> 720
~ -[MGRemoteQueryClient _handleError:] : 284 -> 296
~ -[MGRemoteQueryClient _invalidate] : 252 -> 264
~ -[MGRemoteQueryClient _invalidated] : 136 -> 148
~ -[MGRemoteQueryClient _prepareURL] : 336 -> 372
~ -[MGRemoteQueryClient _prepareRequest:] : 216 -> 224
~ -[MGRemoteQueryClient _responseStart:] : 468 -> 488
~ -[MGRemoteQueryClient _responseValidate:] : 372 -> 392
~ -[MGRemoteQueryClient _responseAppend:] : 636 -> 668
~ -[MGRemoteQueryClient _responseComplete] : 640 -> 668
~ -[MGRemoteQueryClient setError:] : 12 -> 64
~ -[MGRemoteQueryClient setResponse:] : 12 -> 64
~ -[MGRemoteQueryClient setPayload:] : 12 -> 64
~ -[MGRemoteQueryClientManager initWithQueryRunner:groupsQueryAgent:] : 460 -> 480
~ -[MGRemoteQueryClientManager dealloc] : 132 -> 140
~ -[MGRemoteQueryClientManager description] : 252 -> 280
~ -[MGRemoteQueryClientManager _prepareURLSession] : 660 -> 692
~ -[MGRemoteQueryClientManager _invalidate] : 64 -> 68
~ -[MGRemoteQueryClientManager _setupQuery] : 668 -> 704
~ ___41-[MGRemoteQueryClientManager _setupQuery]_block_invoke : 196 -> 200
~ ___41-[MGRemoteQueryClientManager _setupQuery]_block_invoke_2 : 636 -> 660
~ ___41-[MGRemoteQueryClientManager _setupQuery]_block_invoke_2.17 : 216 -> 224
~ -[MGRemoteQueryClientManager _browserUpdateState] : 196 -> 208
~ -[MGRemoteQueryClientManager _browserStart] : 436 -> 464
~ -[MGRemoteQueryClientManager _browserStop] : 320 -> 332
~ -[MGRemoteQueryClientManager _targetAdd:] : 760 -> 796
~ -[MGRemoteQueryClientManager _targetRemove:] : 420 -> 436
~ -[MGRemoteQueryClientManager _targetValidate:] : 612 -> 632
~ -[MGRemoteQueryClientManager browser:foundTarget:] : 216 -> 208
~ ___50-[MGRemoteQueryClientManager browser:foundTarget:]_block_invoke : 116 -> 120
~ -[MGRemoteQueryClientManager browser:lostTarget:] : 216 -> 208
~ ___49-[MGRemoteQueryClientManager browser:lostTarget:]_block_invoke : 116 -> 120
~ -[MGRemoteQueryClientManager browser:invalidatedWithError:] : 216 -> 208
~ ___59-[MGRemoteQueryClientManager browser:invalidatedWithError:]_block_invoke : 440 -> 452
~ -[MGRemoteQueryClientManager _queryAdd:] : 932 -> 980
~ -[MGRemoteQueryClientManager _queryRemove:] : 632 -> 660
~ -[MGRemoteQueryClientManager _clientStartWithQuery:target:] : 504 -> 540
~ -[MGRemoteQueryClientManager _clientStop:] : 272 -> 284
~ -[MGRemoteQueryClientManager _clientRemove:] : 532 -> 564
~ -[MGRemoteQueryClientManager _clientForTask:includeOthers:] : 624 -> 656
~ -[MGRemoteQueryClientManager _clientForTarget:withQuery:] : 480 -> 512
~ -[MGRemoteQueryClientManager _clientsWithQuery:] : 556 -> 584
~ -[MGRemoteQueryClientManager _clientsForTarget:] : 384 -> 400
~ -[MGRemoteQueryClientManager _watchdogForTarget:] : 132 -> 144
~ -[MGRemoteQueryClientManager _watchdogAdd:] : 524 -> 556
~ -[MGRemoteQueryClientManager _watchdogReset:] : 268 -> 280
~ -[MGRemoteQueryClientManager _watchdogRemove:] : 436 -> 456
~ -[MGRemoteQueryClientManager _watchdogFired:] : 488 -> 508
~ -[MGRemoteQueryClientManager clientInvalidated:withError:] : 216 -> 208
~ ___58-[MGRemoteQueryClientManager clientInvalidated:withError:]_block_invoke : 284 -> 296
~ ___44-[MGRemoteQueryClientManager watchdogFired:]_block_invoke : 284 -> 296
~ -[MGRemoteQueryClientManager URLSession:didReceiveChallenge:completionHandler:] : 408 -> 424
~ -[MGRemoteQueryClientManager URLSession:dataTask:didReceiveResponse:completionHandler:] : 436 -> 432
~ -[MGRemoteQueryClientManager URLSession:dataTask:didReceiveData:] : 340 -> 352
~ -[MGRemoteQueryClientManager URLSession:task:didCompleteWithError:] : 192 -> 200
~ -[MGRemoteQueryClientManager setBrowser:] : 12 -> 64
~ -[MGRemoteQueryClientManager setTargets:] : 12 -> 64
~ -[MGRemoteQueryClientManager setQueries:] : 12 -> 64
~ -[MGRemoteQueryClientManager setClients:] : 12 -> 64
~ -[MGRemoteQueryClientManager setWatchdogs:] : 12 -> 64
~ -[MGRemoteQueryClientManager setQuery:] : 12 -> 64
~ -[MGRemoteQueryClientManagerForwarder URLSession:didReceiveChallenge:completionHandler:] : 176 -> 168
~ -[MGRemoteQueryClientManagerForwarder URLSession:dataTask:didReceiveResponse:completionHandler:] : 192 -> 180
~ -[MGRemoteQueryClientManagerForwarder URLSession:dataTask:didReceiveData:] : 160 -> 152
~ -[MGRemoteQueryClientManagerForwarder URLSession:task:didCompleteWithError:] : 148 -> 140
~ -[MGRemoteQueryClient(MGRemoteQueryClientManagerConveniences) query] : 116 -> 124
~ _MGClassForMGGroupType : 452 -> 456
~ -[MGServiceListenerProvider initWithServiceName:entitlement:] : 152 -> 144
~ -[MGServiceListenerProvider dispatchQueue] : 148 -> 160
~ -[MGServiceListenerProvider serviceListener] : 104 -> 108
~ -[MGServiceListenerProvider serviceShouldAcceptNewConnection:] : 148 -> 160
~ -[MGGroup(RemoteQuery) rq_setSourcedRemotely:] : 108 -> 112
~ -[MGGroup(RemoteQuery) rq_sourcedRemotely] : 64 -> 68
~ +[MGGroup(RemoteQuery) rq_predicateForRestrictedTypes] : 332 -> 360
~ +[MGGroup(RemoteQuery) rq_predicateForInCurrentHome] : 236 -> 252
~ -[NSHTTPURLResponse(RemoteQuery) rq_protocolVersion] : 108 -> 116
~ -[NSHTTPURLResponse(RemoteQuery) rq_timeout] : 108 -> 116
~ -[MGGroupsQueryAgent initWithDelegate:] : 576 -> 596
~ -[MGGroupsQueryAgent setGroups:] : 316 -> 332
~ -[MGGroupsQueryAgent setGroupsByMediator:] : 656 -> 680
~ -[MGGroupsQueryAgent setCurrentIdentifier:] : 308 -> 316
~ -[MGGroupsQueryAgent _performQueryExchangeUsingGroups:currentIdentifier:] : 304 -> 288
~ -[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:] : 2804 -> 2916
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke : 240 -> 248
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke_2 : 212 -> 224
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke.24 : 72 -> 76
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke_2.26 : 152 -> 156
~ __AddContainmentForGroup : 588 -> 568
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke_2.60 : 372 -> 396
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke_3.64 : 708 -> 732
~ ___59-[MGGroupsQueryAgent _prepareWithGroups:currentIdentifier:]_block_invoke.65 : 160 -> 156
~ -[MGGroupsQueryAgent _queryOperation:didFindGroups:] : 460 -> 456
~ ___52-[MGGroupsQueryAgent _queryOperation:didFindGroups:]_block_invoke : 1080 -> 1148
~ ___42-[MGGroupsQueryAgent addOutstandingQuery:]_block_invoke : 524 -> 560
~ -[MGGroupsQueryAgent removeOutstandingQuery:] : 156 -> 160
~ ___45-[MGGroupsQueryAgent removeOutstandingQuery:]_block_invoke : 468 -> 492
~ -[MGGroupsQueryAgent outstandingQueryForIdentifier:] : 296 -> 292
~ ___52-[MGGroupsQueryAgent outstandingQueryForIdentifier:]_block_invoke : 108 -> 116
~ -[MGGroupsQueryAgent groupsMediator:didUpdateGroups:] : 196 -> 184
~ ___53-[MGGroupsQueryAgent groupsMediator:didUpdateGroups:]_block_invoke : 316 -> 332
~ ___44-[MGGroupsQueryAgent groupsMediatorRemoved:]_block_invoke : 296 -> 312
~ -[MGGroupsQueryOperation initWithAgent:query:groups:substitutionVariables:] : 256 -> 248
~ ___30-[MGGroupsQueryOperation main]_block_invoke : 232 -> 224
~ ____AddContainmentForGroup_block_invoke : 232 -> 248
~ -[NSPredicate(MediaGroupsDaemon) mg_containsCurrentDevice] : 64 -> 68
~ -[NSPredicate(MediaGroupsDaemon) mg_containsContainment] : 140 -> 148
~ -[NSPredicate(MediaGroupsDaemon) mg_evaluateConstraint:] : 284 -> 292
~ +[MGRemoteQueryClientTarget targetWithEndpoint:txtRecord:] : 136 -> 132
~ -[MGRemoteQueryClientTarget _initWithEndpoint:txtRecord:] : 160 -> 156
~ -[MGRemoteQueryClientTarget description] : 168 -> 180
~ -[MGRemoteQueryClientTarget copyWithZone:] : 4 -> 40
~ -[MGRemoteQueryClientTarget hash] : 80 -> 88
~ -[MGRemoteQueryClientTarget isEqual:] : 364 -> 376
~ -[MGRemoteQueryClientTarget _parseTXTRecord:] : 1008 -> 1028
~ -[MGRemoteQueryClientTarget _parseTXTRecord:forVersion:result:] : 276 -> 268
~ ___63-[MGRemoteQueryClientTarget _parseTXTRecord:forVersion:result:]_block_invoke : 176 -> 180
~ _MGSetServiceXPCInterfacesOnConnection : 1476 -> 1492
~ _MGGroupIdentifierCopyApplyingHashing : 684 -> 712
~ __MGRelevantComponentsForGroupIdentifierComponents : 568 -> 584
~ _MGAccessoryCategoryTypeForAccessory : 76 -> 84
~ _MGClassForGroupIdentifier : 740 -> 776
~ _MGGroupIdentifierForAccessory : 164 -> 180
~ _MGGroupIdentifierForAccessoryIdentifierInHome : 312 -> 308
~ __MGGroupIdentifierHomeKitComponents : 480 -> 468
~ _MGGroupIdentifierForHomeTheaterWithAppleTVAccessoryInHome : 180 -> 196
~ _MGGroupIdentifierForRoomInHome : 132 -> 144
~ _MGGroupIdentifierForHomeInHome : 132 -> 144
~ _MGGroupIdentifierForHomeIdentifierInHome : 136 -> 144
~ _MGHomeIdentifierForGroupIdentifier : 156 -> 180
~ _MGGroupIdentifierForZoneInHome : 132 -> 144
~ _MGGroupIdentifierForZoneIdentifierInHome : 136 -> 144
~ _MGGroupIdentifierForRoomIdentifierInHome : 136 -> 144
~ _MGGroupIdentifierForMediaSystemInHome : 132 -> 144
~ _MGGroupIdentifierForMediaSystemIdentifierInHome : 136 -> 144
~ -[MGRemoteQueryServerManager initWithQueryRunner:] : 360 -> 368
~ -[MGRemoteQueryServerManager dealloc] : 164 -> 176
~ -[MGRemoteQueryServerManager description] : 236 -> 252
~ -[MGRemoteQueryServerManager _updateState] : 168 -> 176
~ -[MGRemoteQueryServerManager _shouldRunServer] : 408 -> 424
~ -[MGRemoteQueryServerManager _startServer] : 460 -> 492
~ -[MGRemoteQueryServerManager _stopServer] : 320 -> 332
~ -[MGRemoteQueryServerManager _setupQuery] : 836 -> 888
~ ___41-[MGRemoteQueryServerManager _setupQuery]_block_invoke : 196 -> 200
~ ___41-[MGRemoteQueryServerManager _setupQuery]_block_invoke_2 : 744 -> 764
~ ___41-[MGRemoteQueryServerManager _setupQuery]_block_invoke_2.20 : 216 -> 224
~ -[MGRemoteQueryServerManager setHavePermissiveACL:] : 188 -> 196
~ -[MGRemoteQueryServerManager setHaveGroupsToAdvertise:] : 188 -> 196
~ -[MGRemoteQueryServerManager setHomeHash:] : 400 -> 416
~ -[MGRemoteQueryServerManager serverInvalidated:withError:] : 216 -> 208
~ ___58-[MGRemoteQueryServerManager serverInvalidated:withError:]_block_invoke : 304 -> 312
~ ___77-[MGRemoteQueryServerManager observeValueForKeyPath:ofObject:change:context:]_block_invoke : 412 -> 432
~ -[MGRemoteQueryServerManager setServer:] : 12 -> 64
~ -[MGRemoteQueryServerManager setQuery:] : 12 -> 64
~ -[MGRemoteQueryServerClient description] : 156 -> 168
~ -[MGRemoteQueryServerClient addNewConnection:completion:] : 216 -> 208
~ ___57-[MGRemoteQueryServerClient addNewConnection:completion:]_block_invoke : 264 -> 268
~ ___57-[MGRemoteQueryServerClient addNewConnection:completion:]_block_invoke_2 : 264 -> 272
~ ___45-[MGRemoteQueryServerClient transactionCount]_block_invoke : 92 -> 96
~ -[MGRemoteQueryServerClient _invalidate] : 288 -> 292
~ ___40-[MGRemoteQueryServerClient _invalidate]_block_invoke : 92 -> 96
~ -[MGRemoteQueryServerClient _transactionAdd:] : 624 -> 656
~ -[MGRemoteQueryServerClient _transactionRemove:] : 444 -> 448
~ ___48-[MGRemoteQueryServerClient _transactionRemove:]_block_invoke : 132 -> 136
~ ___48-[MGRemoteQueryServerClient _transactionExists:]_block_invoke : 96 -> 100
~ -[MGRemoteQueryServerClient _timerInit] : 296 -> 308
~ -[MGRemoteQueryServerClient _timerReschedule] : 188 -> 196
~ -[MGRemoteQueryServerClient _timerCancel] : 68 -> 72
~ -[MGRemoteQueryServerClient _timerFired] : 252 -> 264
~ -[MGRemoteQueryServerClient _delegateNotifyLostTransaction] : 84 -> 88
~ -[MGRemoteQueryServerClient _delegateNotifyInvalidated] : 84 -> 88
~ ___65-[MGRemoteQueryServerClient transaction:receivedTimeoutInterval:]_block_invoke : 336 -> 344
~ -[MGRemoteQueryServerClient transactions] : 60 -> 68
~ -[MGRemoteQueryServerClient setTransactions:] : 124 -> 132
~ -[NSDictionary(MGRemoteQueryCoding) rq_coded] : 440 -> 452
~ -[NSDictionary(MGRemoteQueryCoding) rq_stringForKey:] : 120 -> 128
~ -[NSDictionary(MGRemoteQueryCoding) rq_numberForKey:] : 120 -> 128
~ -[NSDictionary(MGRemoteQueryCoding) rq_decodedObjectOfClass:forKey:] : 104 -> 112
~ -[NSDictionary(MGRemoteQueryCoding) rq_arrayOfDecodedClass:forKey:] : 404 -> 408
~ -[NSArray(MGRemoteQueryCoding) rq_coded] : 328 -> 332
~ -[NSError(MGRemoteQueryCoding) rq_coded] : 252 -> 280
~ +[NSError(MGRemoteQueryCoding) rq_instanceFromCoded:] : 244 -> 256
~ -[MGGroupIdentifier(MGRemoteQueryCoding) rq_coded] : 100 -> 112
~ +[MGGroupIdentifier(MGRemoteQueryCoding) rq_instanceFromCoded:] : 188 -> 200
~ -[MGRemoteQueryReply(MGRemoteQueryCoding) rq_coded] : 200 -> 220
~ +[MGRemoteQueryReply(MGRemoteQueryCoding) rq_instanceFromCoded:] : 284 -> 300
~ -[MGGroup(MGRemoteQueryCoding) rq_coded] : 364 -> 404
~ +[MGGroup(MGRemoteQueryCoding) rq_instanceFromCoded:] : 504 -> 528
~ -[MGAppleTVAccessory(MGRemoteQueryCoding) rq_codedProperties] : 196 -> 208
~ +[MGAppleTVAccessory(MGRemoteQueryCoding) rq_decodedProperties:] : 192 -> 204
~ -[MGAudioReceiverAccessory(MGRemoteQueryCoding) rq_codedProperties] : 196 -> 208
~ +[MGAudioReceiverAccessory(MGRemoteQueryCoding) rq_decodedProperties:] : 192 -> 204
~ -[MGHomePodAccessory(MGRemoteQueryCoding) rq_codedProperties] : 300 -> 328
~ +[MGHomePodAccessory(MGRemoteQueryCoding) rq_decodedProperties:] : 304 -> 324
~ -[MGSpeakerAccessory(MGRemoteQueryCoding) rq_codedProperties] : 196 -> 208
~ +[MGSpeakerAccessory(MGRemoteQueryCoding) rq_decodedProperties:] : 192 -> 204
~ -[MGHomeTheater(MGRemoteQueryCoding) rq_codedProperties] : 188 -> 200
~ +[MGHomeTheater(MGRemoteQueryCoding) rq_decodedProperties:] : 192 -> 204
~ _MGLogForCategory : 100 -> 108
~ -[NSPredicate(RemoteQuery) rq_containsLocal] : 76 -> 80
~ -[MGRemoteQueryServerTransaction initWithConnection:delegate:dispatchQueue:] : 392 -> 396
~ -[MGRemoteQueryServerTransaction description] : 192 -> 208
~ -[MGRemoteQueryServerTransaction _updateState:] : 564 -> 576
~ -[MGRemoteQueryServerTransaction _prepareConnection] : 584 -> 600
~ ___52-[MGRemoteQueryServerTransaction _prepareConnection]_block_invoke : 248 -> 252
~ -[MGRemoteQueryServerTransaction _handleError:] : 268 -> 276
~ -[MGRemoteQueryServerTransaction _handleNWError:] : 128 -> 132
~ -[MGRemoteQueryServerTransaction _invalidate] : 416 -> 436
~ -[MGRemoteQueryServerTransaction _invalidated] : 84 -> 88
~ -[MGRemoteQueryServerTransaction _requestRead] : 436 -> 448
~ ___46-[MGRemoteQueryServerTransaction _requestRead]_block_invoke : 888 -> 908
~ -[MGRemoteQueryServerTransaction _requestProcess:] : 296 -> 308
~ -[MGRemoteQueryServerTransaction _requestParse:] : 456 -> 464
~ ___48-[MGRemoteQueryServerTransaction _requestParse:]_block_invoke : 96 -> 100
~ -[MGRemoteQueryServerTransaction _requestValidate] : 448 -> 472
~ -[MGRemoteQueryServerTransaction _responseStart] : 852 -> 884
~ ___48-[MGRemoteQueryServerTransaction _responseStart]_block_invoke : 276 -> 280
~ -[MGRemoteQueryServerTransaction _responseAppend:] : 600 -> 624
~ ___50-[MGRemoteQueryServerTransaction _responseAppend:]_block_invoke : 288 -> 292
~ -[MGRemoteQueryServerTransaction _responseEnd] : 608 -> 636
~ ___46-[MGRemoteQueryServerTransaction _responseEnd]_block_invoke : 288 -> 292
~ -[MGRemoteQueryServerTransaction _responseObtainPayloadFromHandler] : 708 -> 728
~ -[MGRemoteQueryServerTransaction _responseHandlePayloadFromHandler:error:] : 416 -> 428
~ -[MGRemoteQueryServerTransaction _delegateNotifyTimeoutInterval:] : 124 -> 132
~ -[MGRemoteQueryServerTransaction _delegateNotifyActivityOccurred] : 108 -> 116
~ -[MGRemoteQueryServerTransaction _delegateNotifyInvalidated] : 108 -> 116
~ -[MGRemoteQueryServerTransaction _handlerForRequest:] : 456 -> 476
~ ___53-[MGRemoteQueryServerTransaction _handlerForRequest:]_block_invoke : 184 -> 192
~ -[MGRemoteQueryServerTransaction setError:] : 12 -> 64
~ -[MGRemoteQueryServerTransaction setTransaction:] : 12 -> 64
~ -[MGRemoteQueryServerTransaction setRequest:] : 12 -> 64
~ -[MGRemoteQueryServerTransaction setResponseContext:] : 12 -> 64
~ -[MGRemoteQueryServerTransaction setHandler:] : 12 -> 64
~ -[NSURLRequest(RemoteQuery) rq_protocolVersion] : 108 -> 116
~ -[NSURLRequest(RemoteQuery) rq_timeout] : 108 -> 116
~ -[NSMutableURLRequest(RemoteQuery) rq_setProtocolVersion:] : 112 -> 116
~ -[NSMutableURLRequest(RemoteQuery) rq_setTimeout:] : 112 -> 116
~ -[MGDaemon initWithTopologyRequestHandler:serviceListenerProvider:] : 2016 -> 2064
~ ___67-[MGDaemon initWithTopologyRequestHandler:serviceListenerProvider:]_block_invoke_2 : 160 -> 164
~ ___67-[MGDaemon initWithTopologyRequestHandler:serviceListenerProvider:]_block_invoke_3 : 212 -> 224
~ ___67-[MGDaemon initWithTopologyRequestHandler:serviceListenerProvider:]_block_invoke.75 : 152 -> 160
~ ___38-[MGDaemon setTopologyRequestHandler:]_block_invoke : 592 -> 612
~ -[MGDaemon groupsQueryAgent:didFindResults:forQuery:] : 532 -> 528
~ ___53-[MGDaemon groupsQueryAgent:didFindResults:forQuery:]_block_invoke : 820 -> 848
~ ___53-[MGDaemon groupsQueryAgent:didFindResults:forQuery:]_block_invoke_2 : 248 -> 240
~ ___53-[MGDaemon groupsQueryAgent:didFindResults:forQuery:]_block_invoke_3 : 476 -> 480
~ ___53-[MGDaemon groupsQueryAgent:didFindResults:forQuery:]_block_invoke_4 : 240 -> 244
~ ___53-[MGDaemon groupsQueryAgent:didFindResults:forQuery:]_block_invoke.92 : 332 -> 336
~ -[MGDaemon _ingestHomeKitHome:] : 2396 -> 2464
~ ___31-[MGDaemon _ingestHomeKitHome:]_block_invoke_2 : 252 -> 256
~ ___31-[MGDaemon _ingestHomeKitHome:]_block_invoke.96 : 252 -> 256
~ ___31-[MGDaemon _ingestHomeKitHome:]_block_invoke.99 : 252 -> 256
~ -[MGDaemon addHomeKitHome:] : 144 -> 152
~ -[MGDaemon removeHomeKitHome:] : 336 -> 352
~ -[MGDaemon addHomeKitZone:fromHome:] : 144 -> 152
~ -[MGDaemon removeHomeKitZone:fromHome:] : 340 -> 356
~ -[MGDaemon addHomeKitRoom:fromHome:] : 144 -> 152
~ -[MGDaemon removeHomeKitRoom:fromHome:] : 340 -> 356
~ -[MGDaemon addHomeKitMediaSystem:fromHome:] : 144 -> 152
~ -[MGDaemon removeHomeKitMediaSystem:fromHome:] : 856 -> 872
~ ___46-[MGDaemon removeHomeKitMediaSystem:fromHome:]_block_invoke : 16 -> 72
~ -[MGDaemon addHomeKitMediaSystem:] : 100 -> 108
~ -[MGDaemon removeHomeKitMediaSystem:] : 100 -> 108
~ -[MGDaemon addHomeKitAccessory:fromHome:] : 144 -> 152
~ -[MGDaemon _addHomeKitAccessoryWithoutHomeIngestion:fromHome:] : 844 -> 896
~ -[MGDaemon removeHomeKitAccessory:fromHome:] : 1024 -> 1060
~ ___44-[MGDaemon removeHomeKitAccessory:fromHome:]_block_invoke : 16 -> 72
~ ___79-[MGDaemon _homeTheaterGroupIdentifierForAudioDestination:fromHome:completion:]_block_invoke : 280 -> 312
~ -[MGDaemon listener:shouldAcceptNewConnection:] : 700 -> 712
~ ___47-[MGDaemon listener:shouldAcceptNewConnection:]_block_invoke : 368 -> 376
~ -[MGDaemon createGroupWithType:name:members:completion:] : 1256 -> 1264
~ ___56-[MGDaemon createGroupWithType:name:members:completion:]_block_invoke : 632 -> 680
~ -[MGDaemon deleteGroup:completion:] : 220 -> 212
~ ___35-[MGDaemon deleteGroup:completion:]_block_invoke : 632 -> 680
~ ___35-[MGDaemon deleteGroup:completion:]_block_invoke_2 : 1012 -> 1040
~ -[MGDaemon HomeKitAccessoryOfType:accessoryIdentifier:homeIdentifier:categoryType:name:properties:completion:] : 844 -> 888
~ ___110-[MGDaemon HomeKitAccessoryOfType:accessoryIdentifier:homeIdentifier:categoryType:name:properties:completion:]_block_invoke : 428 -> 460
~ -[MGDaemon setName:group:completion:] : 228 -> 212
~ ___37-[MGDaemon setName:group:completion:]_block_invoke : 552 -> 560
~ -[MGDaemon addMember:group:completion:] : 228 -> 212
~ ___39-[MGDaemon addMember:group:completion:]_block_invoke : 552 -> 560
~ -[MGDaemon removeMember:group:completion:] : 228 -> 212
~ ___42-[MGDaemon removeMember:group:completion:]_block_invoke : 552 -> 560
~ -[MGDaemon startQueryWithPredicate:completion:] : 908 -> 964
~ -[MGDaemon stopQuery:completion:] : 236 -> 248
~ -[MGDaemon stopQuery:] : 272 -> 292
~ -[MGDaemon startInternalQueryWithPredicate:handler:] : 580 -> 604
~ -[MGDaemon stopInternalQuery:] : 328 -> 348
~ ___39-[MGDaemon _fetchGroupInfo:completion:]_block_invoke : 1124 -> 1148
~ ___39-[MGDaemon _fetchGroupInfo:completion:]_block_invoke.159 : 660 -> 680
~ -[MGDaemon startOutstandingQueryWithPredicate:handler:completion:] : 360 -> 340
~ ___66-[MGDaemon startOutstandingQueryWithPredicate:handler:completion:]_block_invoke : 400 -> 408
~ ___66-[MGDaemon startOutstandingQueryWithPredicate:handler:completion:]_block_invoke_2 : 100 -> 104
~ -[MGDaemon setServiceForIngestion:] : 12 -> 64
~ -[MGServiceClient initWithConnection:] : 136 -> 128
~ -[MGServiceClient isEqual:] : 160 -> 168
~ -[MGServiceClient hash] : 56 -> 60
~ -[MGServiceClient copyWithZone:] : 88 -> 92
~ -[MGServiceClient description] : 148 -> 160
~ -[MGServiceClient setQueries:] : 396 -> 412
~ ___28-[MGServiceClient addQuery:]_block_invoke : 148 -> 156
~ ___31-[MGServiceClient removeQuery:]_block_invoke : 132 -> 140
~ -[MGServiceClient outstandingQueryForIdentifier:] : 296 -> 292
~ ___49-[MGServiceClient outstandingQueryForIdentifier:]_block_invoke : 108 -> 116
~ -[MGServiceClient enumerateQueriesUsingBlock:] : 348 -> 344
~ ___46-[MGServiceClient enumerateQueriesUsingBlock:]_block_invoke : 76 -> 80
~ -[MGServiceClient setTransaction:] : 12 -> 64
~ -[MGServiceClientSet serviceClientForXPCConnection:] : 296 -> 292
~ ___52-[MGServiceClientSet serviceClientForXPCConnection:]_block_invoke : 108 -> 116
~ ___39-[MGServiceClientSet addClientService:]_block_invoke : 116 -> 124
~ ___42-[MGServiceClientSet removeClientService:]_block_invoke : 108 -> 116
~ -[MGServiceClientSet enumerateClientsUsingBlock:] : 356 -> 352
~ ___49-[MGServiceClientSet enumerateClientsUsingBlock:]_block_invoke : 120 -> 132

```
