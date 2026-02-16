## SiriCore

> `/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore`

```diff

 3500.6.1.0.0
-  __TEXT.__text: 0x34a3c
-  __TEXT.__auth_stubs: 0x13c0
+  __TEXT.__text: 0x35fc8
+  __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_methlist: 0x3dbc
   __TEXT.__const: 0xc4
-  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__gcc_except_tab: 0x24c
   __TEXT.__cstring: 0x591d
   __TEXT.__oslogstring: 0x2be0
-  __TEXT.__unwind_info: 0xaf0
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__objc_classname: 0x86b
   __TEXT.__objc_methname: 0xa128
   __TEXT.__objc_methtype: 0x1c54

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH_CONST.__auth_got: 0x9c0
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x3960
   __AUTH_CONST.__objc_const: 0x7410

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 02B9DEB6-8196-3100-A85D-A91D5FDF893D
-  Functions: 1254
-  Symbols:   4944
+  UUID: D639E35A-C3CE-3563-83C0-355434183881
+  Functions: 1255
+  Symbols:   4938
   CStrings:  3439
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
Functions:
+ sub_2721378f0
~ -[SiriCoreNetworkActivityTracing _networkActivityRemoveNWConnection:completion:] : 224 -> 220
~ -[SiriCoreNetworkActivityTracing _networkActivityStop:withReason:andError:] : 564 -> 560
~ -[SiriCoreNetworkActivityTracing _networkActivityStart:activate:] : 556 -> 564
~ -[SiriCoreNetworkActivity nwActivity] : 8 -> 56
~ -[SiriCoreNetworkActivity stopWithCompletionReason:andError:] : 592 -> 604
~ -[SiriCoreNetworkActivity removeConnection:] : 108 -> 116
~ -[SiriCoreNetworkActivityTracing currentNetworkActivityTokenWithCompletion:] : 152 -> 160
~ ___76-[SiriCoreNetworkActivityTracing currentNetworkActivityTokenWithCompletion:]_block_invoke : 160 -> 168
~ -[SiriCoreNetworkActivityTracing networkActivityRemoveNWConnection:completion:] : 196 -> 188
~ -[SiriCoreNetworkActivityTracing networkActivityAddNWConnection:] : 152 -> 160
~ -[SiriCoreNetworkActivityTracing networkActivityStop:withReason:andError:] : 172 -> 180
~ -[SiriCoreNetworkActivityTracing init] : 228 -> 236
~ +[SiriCoreNetworkActivityTracing sharedNetworkActivityTracing] : 84 -> 100
~ -[_SiriCoreSQLiteColumnInfo initWithIdentifier:name:type:isPrimaryKey:isNotNull:defaultValue:] : 232 -> 224
~ -[SiriCoreLinkRecommendationInfo linkMetrics] : 8 -> 56
~ -[SiriCoreLinkRecommendationInfo setLinkMetrics:] : 12 -> 64
~ _initWRM_iRATInterface : 84 -> 100
~ _WRM_iRATInterfaceFunction : 12 -> 60
~ -[SiriCoreLinkRecommendationInfo initWithPreferences:wifiPreference:timeTaken:metrics:] : 156 -> 148
~ ___55-[SiriCoreNetworkSessionProvider writeData:completion:]_block_invoke : 172 -> 184
~ ___43-[SiriCoreNetworkSessionProvider readData:]_block_invoke : 256 -> 264
~ -[SiriCoreNetworkSessionProvider _closeWithError:] : 604 -> 608
~ -[SiriCoreNetworkSessionProvider resolvedHost] : 8 -> 56
~ -[SiriCoreNetworkSessionProvider providerStatsIndicatePoorLinkQuality] : 452 -> 456
~ -[SiriCoreNetworkSessionProvider analysisInfo] : 176 -> 184
~ -[SiriCoreNetworkSessionProvider connectionType] : 828 -> 852
~ -[SiriCoreNetworkSessionProvider openConnectionForURL:withConnectionId:initialPayload:completion:] : 2668 -> 2728
~ -[SiriCoreNetworkSessionProvider _setupOpenTimer] : 244 -> 240
~ -[SiriCoreNetworkSessionProvider _setupStaleConnectionTimer] : 332 -> 328
~ ___60-[SiriCoreNetworkSessionProvider _setupStaleConnectionTimer]_block_invoke : 440 -> 444
~ -[SiriCoreNetworkSessionProvider _streamDidBecomeUnviable] : 252 -> 260
~ -[SiriCoreNetworkSessionProvider URLSession:didBecomeInvalidWithError:] : 372 -> 368
~ -[SiriCoreNetworkSessionProvider stream:handleEvent:] : 404 -> 420
~ -[_SiriCoreSQLiteIndexInfo initWithName:columns:] : 156 -> 152
~ -[SiriCoreConnectionMetrics setRemoteMetrics:] : 12 -> 64
~ -[SiriCoreConnectionMetrics getConnectionMetricsDescription] : 164 -> 180
~ -[SiriCoreConnectionMetrics setConnectionMetricsForIDS:messageDelay:openErrorCode:] : 192 -> 204
~ -[SiriCoreConnectionMetrics setConnectionMetricsFromNWConnectionForPOP:withCompletion:] : 140 -> 136
~ -[SiriCoreConnectionMetrics setConnectionMetricsFromNWConnectionForDirect:isMPTCP:attemptedEndpoints:withCompletion:] : 1440 -> 1460
~ ___117-[SiriCoreConnectionMetrics setConnectionMetricsFromNWConnectionForDirect:isMPTCP:attemptedEndpoints:withCompletion:]_block_invoke : 204 -> 216
~ ___117-[SiriCoreConnectionMetrics setConnectionMetricsFromNWConnectionForDirect:isMPTCP:attemptedEndpoints:withCompletion:]_block_invoke_2 : 132 -> 140
~ -[SiriCoreConnectionMetrics setConnectionMetricsFromConnection:isPop:isMPTCP:attemptedEndpoints:completion:] : 316 -> 308
~ -[SiriCoreConnectionMetrics _setConnectionMetricsFromNSPControlConnection:withCompletion:] : 340 -> 336
~ ___90-[SiriCoreConnectionMetrics _setConnectionMetricsFromNSPControlConnection:withCompletion:]_block_invoke : 944 -> 964
~ ___58-[SiriCoreConnectionMetrics _setConnectionMetricsTCPInfo:]_block_invoke : 188 -> 192
~ _SiriCoreConnectionTCPInfoMetricsCreate : 848 -> 928
~ -[SiriCoreConnectionMetrics setConnectionMetricsFromStreamForPOP:withCompletion:] : 140 -> 136
~ -[SiriCoreConnectionMetrics setConnectionMetricsFromStreamForDirect:withCompletion:] : 852 -> 876
~ ___84-[SiriCoreConnectionMetrics setConnectionMetricsFromStreamForDirect:withCompletion:]_block_invoke : 188 -> 192
~ -[SiriCoreErrorInfo setError:] : 12 -> 64
~ -[SiriCoreSiriBackgroundConnection setPeerProviderClass:] : 12 -> 64
~ -[SiriCoreSiriBackgroundConnection getConnectionMetrics:withCompletion:] : 1488 -> 1520
~ -[SiriCoreSiriBackgroundConnection _connectionMethodDescription] : 320 -> 328
~ -[SiriCoreSiriBackgroundConnection _handleAceEnd] : 336 -> 340
~ -[SiriCoreSiriBackgroundConnection _handleAcePong:] : 276 -> 280
~ -[SiriCoreSiriBackgroundConnection _tryReadingParsedDataFromBytes:length:packet:object:bytesParsed:error:] : 736 -> 744
~ -[SiriCoreSiriBackgroundConnection _tryParsingHTTPHeaderData:partialMessage:statusCode:bytesRead:error:] : 656 -> 672
~ -[SiriCoreSiriBackgroundConnection _tryReadingHTTPHeaderData:withMessage:bytesRead:error:] : 704 -> 720
~ -[SiriCoreSiriBackgroundConnection _setupReadHandlerOnProvider] : 184 -> 188
~ ___63-[SiriCoreSiriBackgroundConnection _setupReadHandlerOnProvider]_block_invoke : 516 -> 512
~ ___63-[SiriCoreSiriBackgroundConnection _setupReadHandlerOnProvider]_block_invoke.218 : 544 -> 548
~ -[SiriCoreSiriBackgroundConnection _sendAcePongWithId:error:] : 476 -> 484
~ -[SiriCoreSiriBackgroundConnection _sendAcePingWithId:error:] : 476 -> 484
~ -[SiriCoreSiriBackgroundConnection sendCommand:moreComing:errorHandler:] : 896 -> 888
~ -[SiriCoreSiriBackgroundConnection _prepareProviderHeaderWithForceReconnect:] : 252 -> 264
~ -[SiriCoreSiriBackgroundConnection _tryToWriteBufferedOutputData] : 520 -> 524
~ -[SiriCoreSiriBackgroundConnection _headerDataForURL:aceHost:languageCode:syncAssistantId:] : 1688 -> 1736
~ ___91-[SiriCoreSiriBackgroundConnection _headerDataForURL:aceHost:languageCode:syncAssistantId:]_block_invoke_2 : 164 -> 160
~ -[SiriCoreSiriBackgroundConnection _networkProviderDidOpen] : 508 -> 528
~ -[SiriCoreSiriBackgroundConnection _connectionHasBytesAvailable:] : 1596 -> 1572
~ -[SiriCoreSiriBackgroundConnection _consumeAceDataWithData:bytesRead:error:] : 820 -> 844
~ -[SiriCoreSiriBackgroundConnection connectionProvider:receivedViabilityChangeNotification:] : 448 -> 452
~ -[SiriCoreSiriBackgroundConnection connectionProvider:receivedIntermediateError:] : 152 -> 160
~ -[SiriCoreSiriBackgroundConnection connectionProvider:receivedError:] : 196 -> 188
~ ___69-[SiriCoreSiriBackgroundConnection connectionProvider:receivedError:]_block_invoke : 536 -> 544
~ -[SiriCoreSiriBackgroundConnection _cancelOutstandingBarriers] : 308 -> 312
~ -[SiriCoreSiriBackgroundConnection _handleBarrierReply:] : 140 -> 148
~ -[SiriCoreSiriBackgroundConnection _checkPings] : 340 -> 344
~ -[SiriCoreSiriBackgroundConnection _pingTimerFired] : 1412 -> 1440
~ -[SiriCoreSiriBackgroundConnection _aceHeaderTimeoutFired:afterTimeout:] : 1048 -> 1064
~ -[SiriCoreSiriBackgroundConnection _scheduleAceHeaderTimeoutTimerWithInterval:] : 492 -> 484
~ -[SiriCoreSiriBackgroundConnection _getWifiMetrics:] : 360 -> 368
~ -[SiriCoreSiriBackgroundConnection _getCellularMetrics:] : 184 -> 172
~ -[SiriCoreSiriBackgroundConnection _fallBackToNextConnectionMethodWithError:orElse:] : 988 -> 1008
~ __SiriCoreSiriConnectionMethodGetNextSupported : 328 -> 340
~ -[SiriCoreSiriBackgroundConnection _fallBackToNextConnectionMethod:fromError:afterDelay:] : 696 -> 704
~ -[SiriCoreSiriBackgroundConnection _shouldTrySameConnectionMethodForMethod:error:] : 260 -> 272
~ -[SiriCoreSiriBackgroundConnection _bestErrorBetweenError:peerError:] : 168 -> 164
~ -[SiriCoreSiriBackgroundConnection _didEncounterError:] : 716 -> 740
~ ___55-[SiriCoreSiriBackgroundConnection _didEncounterError:]_block_invoke : 1300 -> 1380
~ -[SiriCoreSiriBackgroundConnection _initializeBufferedGeneralOutputDataWithInitialPayload:] : 424 -> 452
~ -[SiriCoreSiriBackgroundConnection _httpHeaderData] : 200 -> 224
~ -[SiriCoreSiriBackgroundConnection _forceTriggerRetry] : 128 -> 132
~ -[SiriCoreSiriBackgroundConnection _startSecondaryConnection] : 888 -> 940
~ ___61-[SiriCoreSiriBackgroundConnection _startSecondaryConnection]_block_invoke : 680 -> 708
~ -[SiriCoreSiriBackgroundConnection updateActiveBackgroundConnectionWithSecondary] : 372 -> 388
~ -[SiriCoreSiriBackgroundConnection _startNetworkProviderWithInfo:] : 876 -> 896
~ ___66-[SiriCoreSiriBackgroundConnection _startNetworkProviderWithInfo:]_block_invoke : 868 -> 892
~ -[SiriCoreSiriBackgroundConnection _updateBuffersForInitialPayload:bufferedLength:forceReconnect:] : 476 -> 472
~ -[SiriCoreSiriBackgroundConnection _getInitialPayloadWithBufferedLength:forceReconnect:] : 280 -> 304
~ -[SiriCoreSiriBackgroundConnection _providerClass] : 520 -> 528
~ -[SiriCoreSiriBackgroundConnection _setNetworkProvider:] : 144 -> 160
~ -[SiriCoreSiriBackgroundConnection _startWithConnectionInfo:proposedFallbackMethod:allowFallbackToNewMethod:] : 1828 -> 1848
~ -[SiriCoreSiriBackgroundConnection _nextConnectionMethod] : 104 -> 112
~ -[SiriCoreSiriBackgroundConnection _usingPOPOnPeer] : 116 -> 124
~ -[SiriCoreSiriBackgroundConnection _usingFlorence] : 116 -> 124
~ -[SiriCoreSiriBackgroundConnection initWithQueue:] : 156 -> 164
~ -[SiriCoreSiriConnectionInfo description] : 480 -> 496
~ -[SiriCoreNWContext nwContext] : 8 -> 56
~ -[SiriCoreNWContext init] : 128 -> 132
~ +[SiriCoreNWContext sharedInstance] : 84 -> 100
~ -[SiriCoreSQLiteQueryOrder copyWithZone:] : 4 -> 40
~ +[SiriCoreNetworkingAnalytics(SessionConnectionFail) sessionConnectionFailedError:connectionMode:sessionType:sessionState:dormant:analysisInfo:] : 788 -> 828
~ +[SiriCoreNetworkingAnalytics(SessionConnectionFail) sessionStateFromString:] : 384 -> 388
~ +[SiriCoreNetworkingAnalytics(SessionConnectionFail) sessionTypeFromString:] : 160 -> 164
~ +[SiriCoreNetworkingAnalytics(SessionConnectionFail) connectionModeFromString:] : 104 -> 108
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) providerFromString:] : 228 -> 248
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) sessionConnectionQualityFromSiriCoreConnectionMetrics:] : 460 -> 468
~ ___112+[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) sessionConnectionQualityFromSiriCoreConnectionMetrics:]_block_invoke : 228 -> 232
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) qualityFromString:] : 124 -> 128
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) pingInfoFromSiriCoreConnectionMetrics:] : 208 -> 220
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) debugNetworkInterfacesFromSiriCoreConnectionMetrics:] : 236 -> 244
~ ___110+[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) debugNetworkInterfacesFromSiriCoreConnectionMetrics:]_block_invoke : 900 -> 964
~ ___110+[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) debugNetworkInterfacesFromSiriCoreConnectionMetrics:]_block_invoke_2 : 208 -> 204
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) debugSessionConnectionNetworkFromSiriCoreConnectionMetrics:] : 252 -> 268
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) phyModeFromString:] : 300 -> 304
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) sessionConnectionNetworkFromSiriCoreConnectionMetrics:] : 708 -> 772
~ ___90+[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) networkInterfacesFromDictionary:]_block_invoke : 184 -> 180
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) connectionTypeFromString:] : 664 -> 668
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) connectionMethodFromString:] : 244 -> 248
~ +[SiriCoreNetworkingAnalytics(SessionConnectionSnapshot) tlsFromString:] : 208 -> 212
~ -[SiriCoreSQLiteQueryResult description] : 372 -> 380
~ -[SiriCoreSQLiteQueryResult initWithQuery:beginMachTime:endMachTime:statement:columnNameTuple:columnValueTuples:columnValuesMap:rowValueTuples:rowValueMaps:records:error:] : 440 -> 396
~ -[_SiriCoreSQLiteTableInfo initWithName:columns:] : 156 -> 152
~ _SiriCoreGetConnectionNetworkPathReport : 768 -> 792
~ ___SiriCoreGetConnectionNetworkPathReport_block_invoke : 284 -> 296
~ ___SiriCoreGetConnectionNetworkPathReport_block_invoke_2 : 72 -> 76
~ __getConnectionDescription : 100 -> 104
~ __getEndpointInfo : 240 -> 248
~ _SiriCoreGetConnectionReadyReport : 820 -> 836
~ ___SiriCoreGetConnectionReadyReport_block_invoke : 244 -> 256
~ ___SiriCoreGetConnectionReadyReport_block_invoke_2 : 360 -> 376
~ +[SiriCoreAceSerialization _insufficientDataErrorForBytesNeeded:available:] : 260 -> 276
~ +[SiriCoreAceSerialization tryParsingPacketWithBytes:length:rawPacket:object:bytesRead:error:] : 696 -> 720
~ +[SiriCoreAceSerialization _tryParsingSpeechPacketBytes:length:] : 488 -> 480
~ +[SiriCoreAceSerialization _tryParsingPlistPacketBytes:length:] : 112 -> 116
~ +[SiriCoreAceSerialization tryParsingAceHeaderData:compressionType:bytesRead:error:] : 584 -> 592
~ +[SiriCoreAceSerialization dataForSpeechPacket:error:] : 1064 -> 1096
~ +[SiriCoreAceSerialization dataForObject:error:] : 340 -> 360
~ -[SiriCoreSyncRecord setCheckHash:] : 12 -> 64
~ -[SiriCoreSyncRecord setMetaValue:] : 12 -> 64
~ -[SiriCoreSyncRecord setAddedValue:] : 12 -> 64
~ -[SiriCoreSyncRecord setDataValue:] : 12 -> 64
~ -[SiriCoreSyncRecord setDebugValue:] : 12 -> 64
~ -[SiriCoreSyncRecord setIdentifier:] : 12 -> 64
~ -[SiriCoreSyncRecord setKey:] : 12 -> 64
~ -[SiriCoreSyncRecord description] : 216 -> 224
~ -[SiriCoreSyncRecord setUpdateTimeToNow] : 88 -> 92
~ -[SiriCoreSyncRecord updateHash] : 300 -> 304
~ -[SiriCoreSyncRecord initWithKey:identifier:priority:debugValue:dataValue:addedValue:appMeta:] : 320 -> 296
~ +[SiriCoreSyncRecord syncRecordWithKey:identifier:] : 144 -> 140
~ +[SiriCoreSyncRecord syncRecordWithKey:identifier:priority:debugValue:dataValue:addedValue:appMeta:] : 232 -> 208
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) handShakeProtocolFromArray:] : 656 -> 680
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) handshakeProtocolFromString:] : 132 -> 136
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) proxyConfigurationFromDictionary:] : 268 -> 284
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) establishmentResolutionFromArray:] : 880 -> 928
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) pathStatusFromNumber:] : 152 -> 156
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) pathInterfacesFromArray:] : 656 -> 680
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) pathTypeFromNumber:] : 180 -> 184
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) endpointsFromArray:] : 360 -> 364
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) endpointFromDictionary:] : 288 -> 304
~ +[SiriCoreNetworkingAnalytics(NetworkConnectionState) endpointTypeFromNumber:] : 180 -> 184
~ _SiriCoreSQLiteQueryCreateColumnDefinition : 744 -> 780
~ _SiriCoreSQLiteQueryCreateEscapedAndCommaSeparatedString : 432 -> 444
~ _SiriCoreSQLiteQueryCreateCriterionExpression : 1936 -> 1996
~ _SiriCoreSQLiteQueryCreateOrderExpression : 220 -> 228
~ -[SiriCoreSiriConnection setPeerProviderClass:] : 12 -> 64
~ -[SiriCoreSiriConnection siriBackgroundConnection:willStartConnectionWithHTTPHeader:] : 152 -> 160
~ -[SiriCoreSiriConnection siriBackgroundConnection:didEncounterIntermediateError:] : 200 -> 188
~ ___81-[SiriCoreSiriConnection siriBackgroundConnection:didEncounterIntermediateError:]_block_invoke : 592 -> 600
~ -[SiriCoreSiriConnection siriBackgroundConnection:didEncounterError:analysisInfo:] : 276 -> 260
~ ___82-[SiriCoreSiriConnection siriBackgroundConnection:didEncounterError:analysisInfo:]_block_invoke : 588 -> 568
~ -[SiriCoreSiriConnection siriBackgroundConnectionDidClose:] : 152 -> 160
~ -[SiriCoreSiriConnection siriBackgroundConnection:didReceiveAceObject:] : 332 -> 320
~ -[SiriCoreSiriConnection siriBackgroundConnection:didOpenWithConnectionType:routeId:delay:] : 296 -> 276
~ ___91-[SiriCoreSiriConnection siriBackgroundConnection:didOpenWithConnectionType:routeId:delay:]_block_invoke : 528 -> 536
~ -[SiriCoreSiriConnection siriBackgroundConnection:willStartWithConnectionType:] : 308 -> 304
~ -[SiriCoreSiriConnection _activeOrAnyPendingConnection] : 64 -> 84
~ ___51-[SiriCoreSiriConnection _waitForActiveConnection:]_block_invoke : 128 -> 124
~ ___71-[SiriCoreSiriConnection getConnectionMetricsSynchronously:completion:]_block_invoke : 256 -> 264
~ -[SiriCoreSiriConnection getAnalysisInfo:] : 152 -> 160
~ ___42-[SiriCoreSiriConnection getAnalysisInfo:]_block_invoke : 132 -> 140
~ -[SiriCoreSiriConnection analysisInfo] : 240 -> 236
~ ___38-[SiriCoreSiriConnection analysisInfo]_block_invoke : 104 -> 112
~ ___34-[SiriCoreSiriConnection barrier:]_block_invoke : 112 -> 116
~ -[SiriCoreSiriConnection sendCommands:errorHandler:] : 196 -> 188
~ ___52-[SiriCoreSiriConnection sendCommands:errorHandler:]_block_invoke : 160 -> 168
~ -[SiriCoreSiriConnection sendCommand:errorHandler:] : 196 -> 188
~ ___51-[SiriCoreSiriConnection sendCommand:errorHandler:]_block_invoke : 160 -> 168
~ -[SiriCoreSiriConnection start] : 2028 -> 2092
~ -[SiriCoreSiriConnection _scheduleBackgroundConnectionWithRoute:delay:policy:] : 384 -> 372
~ ___78-[SiriCoreSiriConnection _scheduleBackgroundConnectionWithRoute:delay:policy:]_block_invoke : 324 -> 328
~ -[SiriCoreSiriConnection _startBackgroundConnectionWithRoute:policy:] : 688 -> 696
~ -[SiriCoreSiriConnection _connectionInfoForRoute:policy:] : 744 -> 768
~ -[SiriCoreSiriConnection dealloc] : 116 -> 120
~ -[SiriCoreSiriConnection initWithQueue:] : 304 -> 300
~ -[SiriCoreSymptomsReporter setLock:] : 12 -> 64
~ -[SiriCoreSymptomsReporter setKeysRejectedWithTimestamp:] : 12 -> 64
~ -[SiriCoreSymptomsReporter setKeysAcceptedWithTimestamp:] : 12 -> 64
~ -[SiriCoreSymptomsReporter reportIssueForType:subType:context:processIdentifier:walkboutStatus:withPcap:] : 720 -> 736
~ ___105-[SiriCoreSymptomsReporter reportIssueForType:subType:context:processIdentifier:walkboutStatus:withPcap:]_block_invoke : 304 -> 324
~ -[SiriCoreSymptomsReporter reportIssueWithBackOffTimerForType:subType:context:processIdentifier:walkboutStatus:] : 836 -> 860
~ -[SiriCoreSymptomsReporter reportIssueForType:subType:context:processIdentifier:walkboutStatus:] : 196 -> 192
~ -[SiriCoreSymptomsReporter _subtypeContextStringFromContext:] : 284 -> 288
~ ___61-[SiriCoreSymptomsReporter _subtypeContextStringFromContext:]_block_invoke_2 : 164 -> 172
~ -[SiriCoreSymptomsReporter reportIssueForError:type:subtype:context:processIdentifier:walkboutStatus:triggerForIDSIdentifiers:withPcap:] : 420 -> 392
~ ___136-[SiriCoreSymptomsReporter reportIssueForError:type:subtype:context:processIdentifier:walkboutStatus:triggerForIDSIdentifiers:withPcap:]_block_invoke : 548 -> 564
~ -[SiriCoreSymptomsReporter reportIssueForError:type:subtype:context:processIdentifier:walkboutStatus:triggerForIDSIdentifiers:] : 236 -> 224
~ -[SiriCoreSymptomsReporter _getTypeForError:completion:] : 548 -> 560
~ ___56-[SiriCoreSymptomsReporter _getTypeForError:completion:]_block_invoke : 168 -> 172
~ +[SiriCoreSymptomsReporter sharedInstance] : 84 -> 100
~ -[SiriCoreSQLiteQueryCriterion copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteQueryCriterion initWithColumnName:comparisonOperator:logicalOperator:value:values:subcriteriaProvider:] : 184 -> 180
~ -[SiriCoreSQLiteQueryCriterion initWithColumnName:comparisonOperator:logicalOperator:value:values:subcriteria:] : 256 -> 244
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) likeQueryCriterionWithColumnName:value:negation:] : 148 -> 144
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) isQueryCriterionWithColumnName:value:negation:] : 144 -> 140
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) inQueryCriterionWithColumnName:values:negation:] : 148 -> 144
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) betweenQueryCriterionWithColumnName:fromValue:toValue:negation:] : 268 -> 264
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) notEqualToQueryCriterionWithColumnName:value:] : 132 -> 128
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) lessThanOrEqualToQueryCriterionWithColumnName:value:] : 132 -> 128
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) lessThanQueryCriterionWithColumnName:value:] : 132 -> 128
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) greaterThanOrEqualToQueryCriterionWithColumnName:value:] : 132 -> 128
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) greaterThanQueryCriterionWithColumnName:value:] : 132 -> 128
~ +[SiriCoreSQLiteQueryCriterion(SiriCoreSQLiteQueryCriterionConveniences) equalToQueryCriterionWithColumnName:value:] : 132 -> 128
~ -[SiriCoreSQLiteQueryRange copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteTableDescription copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteTableDescription initWithName:columns:constraints:] : 192 -> 184
~ -[NSString(SiriCoreSQLiteValue) siriCoreSQLiteValue_toNumber] : 544 -> 556
~ -[NSString(SiriCoreSQLiteValue) siriCoreSQLiteValue_escapedString:] : 200 -> 208
~ -[NSNumber(SiriCoreSQLiteValue) siriCoreSQLiteValue_type] : 320 -> 316
~ -[NSNumber(SiriCoreSQLiteValue) siriCoreSQLiteValue_toData] : 76 -> 84
~ -[NSNumber(SiriCoreSQLiteValue) siriCoreSQLiteValue_escapedString:] : 228 -> 232
~ -[NSDecimalNumber(SiriCoreSQLiteValue) siriCoreSQLiteValue_textRepresentation] : 60 -> 64
~ -[NSData(SiriCoreSQLiteValue) siriCoreSQLiteValue_toNumber] : 76 -> 84
~ -[NSData(SiriCoreSQLiteValue) siriCoreSQLiteValue_escapedString:] : 292 -> 296
~ -[NSError(SiriCoreUtilities) siriCore_isNetworkDownError] : 220 -> 232
~ -[SiriCorePingInfo markPongReceivedWithIndex:] : 216 -> 220
~ -[SiriCorePingInfo markPingSentWithIndex:] : 180 -> 184
~ -[SiriCoreSQLiteColumnConstraint copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteColumnConstraint initWithName:type:value:options:] : 180 -> 176
~ +[SiriCoreSQLiteColumnConstraint(SiriCoreSQLiteColumnConstraintConveniences) defaultColumnConstraintWithName:value:] : 124 -> 120
~ -[SiriCoreSQLiteIndexDescription copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteIndexDescription initWithName:tableName:columnNames:options:] : 208 -> 200
~ -[SiriCoreNetEventMessage setClientEvent:] : 12 -> 64
~ -[SiriCoreNetEventMessage setNetId:] : 12 -> 64
~ -[SiriCoreNetworkingAnalytics logPeerConnectionFailed:] : 172 -> 168
~ ___55-[SiriCoreNetworkingAnalytics logPeerConnectionFailed:]_block_invoke : 716 -> 728
~ -[SiriCoreNetworkingAnalytics logSessionConnectionFailed:] : 172 -> 168
~ ___58-[SiriCoreNetworkingAnalytics logSessionConnectionFailed:]_block_invoke : 716 -> 728
~ ___73-[SiriCoreNetworkingAnalytics logDebugSessionConnectionSnapshotCaptured:]_block_invoke : 768 -> 776
~ -[SiriCoreNetworkingAnalytics logSessionConnectionSnapshotCaptured:] : 172 -> 168
~ ___68-[SiriCoreNetworkingAnalytics logSessionConnectionSnapshotCaptured:]_block_invoke : 768 -> 776
~ ___83-[SiriCoreNetworkingAnalytics logDebugNetworkConnectionStateReadySnapshotCaptured:]_block_invoke : 716 -> 728
~ -[SiriCoreNetworkingAnalytics logNetworkConnectionStateReadySnapshotCaptured:] : 172 -> 168
~ ___78-[SiriCoreNetworkingAnalytics logNetworkConnectionStateReadySnapshotCaptured:]_block_invoke : 716 -> 728
~ ___89-[SiriCoreNetworkingAnalytics logDebugNetworkConnectionStatePreparationSnapshotCaptured:]_block_invoke : 716 -> 728
~ -[SiriCoreNetworkingAnalytics logNetworkConnectionStatePreparationSnapshotCaptured:] : 172 -> 168
~ ___84-[SiriCoreNetworkingAnalytics logNetworkConnectionStatePreparationSnapshotCaptured:]_block_invoke : 716 -> 728
~ -[SiriCoreNetworkingAnalytics logSessionConnectionHttpHeaderCreated:] : 172 -> 168
~ ___69-[SiriCoreNetworkingAnalytics logSessionConnectionHttpHeaderCreated:]_block_invoke : 716 -> 728
~ ___83-[SiriCoreNetworkingAnalytics logRequestLinkBetweenOrchestratorAndNetworkComponent]_block_invoke : 804 -> 816
~ ___57-[SiriCoreNetworkingAnalytics _emitAllCachedMessagesFor:]_block_invoke : 2612 -> 2756
~ -[SiriCoreNetworkingAnalytics _createSchemaClientEventFromNetId:networkConnectionId:connectionProvider:] : 284 -> 292
~ -[SiriCoreNetworkingAnalytics orchestratorRequestId] : 240 -> 236
~ ___52-[SiriCoreNetworkingAnalytics orchestratorRequestId]_block_invoke : 20 -> 68
~ -[SiriCoreNetworkingAnalytics setOrchestratorRequestId:] : 152 -> 160
~ -[SiriCoreNetworkingAnalytics setConnectionProvider:] : 152 -> 160
~ -[SiriCoreNetworkingAnalytics setNetworkConnectionId:] : 152 -> 160
~ ___54-[SiriCoreNetworkingAnalytics setNetworkConnectionId:]_block_invoke : 204 -> 220
~ -[SiriCoreNetworkingAnalytics setNetId:] : 152 -> 160
~ ___41-[SiriCoreNetworkingAnalytics resetNetId]_block_invoke : 224 -> 228
~ -[SiriCoreNetworkingAnalytics _init] : 356 -> 364
~ -[SiriCoreNetworkingAnalytics init] : 128 -> 132
~ +[SiriCoreNetworkingAnalytics sharedSiriCoreNetworkingAnalytics] : 84 -> 100
~ -[SiriCoreNetworkManager signalStrengthChanged:info:] : 264 -> 260
~ -[SiriCoreNetworkManager simStatusDidChange:status:] : 356 -> 348
~ -[SiriCoreNetworkManager _signalStrengthChange:] : 244 -> 248
~ ___47-[SiriCoreNetworkManager _signalStrengthUpdate]_block_invoke_2 : 328 -> 324
~ ___47-[SiriCoreNetworkManager _signalStrengthUpdate]_block_invoke_3 : 240 -> 236
~ ___54-[SiriCoreNetworkManager _dataServiceDescriptorUpdate]_block_invoke_2 : 276 -> 272
~ ___57-[SiriCoreNetworkManager _dataSubscriptionContextChange:]_block_invoke : 192 -> 200
~ ___57-[SiriCoreNetworkManager _dataSubscriptionContextChange:]_block_invoke_2 : 256 -> 268
~ ___57-[SiriCoreNetworkManager registerWithWirelessCoexManager]_block_invoke : 480 -> 476
~ _initWRM_iRATInterface.2578 : 84 -> 100
~ _WRM_iRATInterfaceFunction.2585 : 12 -> 60
~ -[SiriCoreNetworkManager _getLinkRecommendationSafe:recommendation:] : 1176 -> 1180
~ ___68-[SiriCoreNetworkManager _getLinkRecommendationSafe:recommendation:]_block_invoke : 728 -> 740
~ ___68-[SiriCoreNetworkManager _getLinkRecommendationSafe:recommendation:]_block_invoke.28 : 356 -> 364
~ ___68-[SiriCoreNetworkManager _getLinkRecommendationSafe:recommendation:]_block_invoke.29 : 220 -> 224
~ -[SiriCoreNetworkManager _subscribeToLinkRecommendations:] : 172 -> 168
~ ___58-[SiriCoreNetworkManager _subscribeToLinkRecommendations:]_block_invoke : 328 -> 332
~ ___47-[SiriCoreNetworkManager acquireWiFiAssertion:]_block_invoke : 84 -> 88
~ ___43-[SiriCoreNetworkManager forceFastDormancy]_block_invoke : 236 -> 240
~ -[SiriCoreNetworkManager getQualityReport:] : 152 -> 160
~ -[SiriCoreNetworkManager getNetworkPerformanceFeed] : 144 -> 148
~ -[SiriCoreNetworkManager startMonitoringNetworkForHost:] : 152 -> 160
~ ___56-[SiriCoreNetworkManager startMonitoringNetworkForHost:]_block_invoke : 476 -> 480
~ -[SiriCoreNetworkManager _pathUpdated:] : 640 -> 644
~ -[SiriCoreNetworkManager _wiFiManagerClient] : 84 -> 92
~ -[SiriCoreNetworkManager removeObserver:] : 152 -> 160
~ -[SiriCoreNetworkManager addObserver:] : 152 -> 160
~ -[SiriCoreNetworkManager _init] : 268 -> 276
~ +[SiriCoreNetworkManager acquireDormancySuspendAssertion:] : 632 -> 636
~ +[SiriCoreNetworkManager connectionTypeForInterface:] : 128 -> 132
~ +[SiriCoreNetworkManager getCarrierName:signalStrength:subscriptionCount:] : 440 -> 444
~ +[SiriCoreNetworkManager connectionSubTypeForCellularInterface] : 64 -> 68
~ +[SiriCoreNetworkManager sharedInstance] : 84 -> 100
~ _SiriCoreNetworkQuality : 128 -> 132
~ -[SiriCoreConnectionType description] : 156 -> 164
~ _SiriCoreConnectionTechnologyGetDescription : 408 -> 404
~ -[SiriCoreSQLiteDatabase checkpointWriteAheadLogWithError:] : 400 -> 412
~ _SiriCoreSQLiteDatabaseCreateSQLiteAPIErrorFromResultCode : 292 -> 300
~ -[SiriCoreSQLiteDatabase executeQuery:error:] : 96 -> 104
~ -[SiriCoreSQLiteDatabase executeQuery:] : 6036 -> 6156
~ -[SiriCoreSQLiteDatabase closeWithError:] : 640 -> 652
~ -[SiriCoreSQLiteDatabase openWithError:] : 1696 -> 1752
~ -[SiriCoreSQLiteDatabase initWithPath:dataProtectionClass:options:] : 192 -> 196
~ _SiriCoreSQLiteDatabaseIsErrorUnrecoverable : 228 -> 248
~ -[SiriCoreDataCompressor compressedDataForData:error:] : 8 -> 56
~ -[SiriCoreDataDecompressor decompressedDataForData:error:] : 8 -> 56
~ -[SiriCoreZlibDataCompressor compressedDataForData:error:] : 664 -> 652
~ ___58-[SiriCoreZlibDataCompressor compressedDataForData:error:]_block_invoke : 288 -> 244
~ -[SiriCoreZlibDataCompressor dealloc] : 84 -> 76
~ -[SiriCoreZlibDataCompressor init] : 300 -> 292
~ -[SiriCoreZlibDataDecompressor decompressedDataForData:error:] : 752 -> 740
~ ___62-[SiriCoreZlibDataDecompressor decompressedDataForData:error:]_block_invoke : 296 -> 252
~ -[SiriCoreZlibDataDecompressor dealloc] : 84 -> 76
~ -[SiriCoreZlibDataDecompressor init] : 296 -> 288
~ -[SiriCoreSQLiteDatabase(Update) updateTableWithName:columnName:columnValue:criterion:error:] : 380 -> 388
~ ___79-[SiriCoreSQLiteDatabase(Update) updateTableWithName:valueMap:criterion:error:]_block_invoke : 200 -> 204
~ -[SiriCoreSQLiteDatabase(Select) countValuesInTableWithName:columnName:behavior:indexedBy:criterion:range:error:] : 816 -> 852
~ -[SiriCoreSQLiteDatabase(Select) selectValuesFromTableWithName:columnName:behavior:indexedBy:criterion:order:range:error:] : 716 -> 748
~ -[SiriCoreSQLiteDatabase(Select) selectRecordsFromTableWithName:columnNames:behavior:indexedBy:criterion:order:range:recordBuilder:error:] : 872 -> 920
~ -[SiriCoreSQLiteDatabase(Select) selectValueMapsFromTableWithName:columnNames:behavior:indexedBy:criterion:order:range:error:] : 856 -> 904
~ -[SiriCoreSQLiteDatabase(Select) selectValueTuplesFromTableWithName:columnNames:behavior:indexedBy:criterion:order:range:error:] : 856 -> 904
~ -[SiriCoreSQLiteDatabase(Schema) dropIndexWithName:error:] : 168 -> 172
~ -[SiriCoreSQLiteDatabase(Schema) createIndex:error:] : 320 -> 344
~ -[SiriCoreSQLiteDatabase(Schema) alterTableWithName:addColumn:error:] : 204 -> 208
~ -[SiriCoreSQLiteDatabase(Schema) alterTableWithName:renameTo:error:] : 208 -> 212
~ -[SiriCoreSQLiteDatabase(Schema) dropTableWithName:error:] : 168 -> 172
~ -[SiriCoreSQLiteDatabase(Schema) createTable:error:] : 960 -> 1024
~ -[SiriCoreSQLiteDatabase(Schema) fetchTableWithName:error:] : 864 -> 908
~ -[SiriCoreSQLiteDatabase(Schema) fetchTableNamesWithError:] : 264 -> 280
~ -[SiriCoreSQLiteDatabase(Savepoint) rollbackToSavepointWithName:error:] : 168 -> 172
~ -[SiriCoreSQLiteDatabase(Savepoint) releaseSavepointWithName:error:] : 168 -> 172
~ -[SiriCoreSQLiteDatabase(Savepoint) savepointWithName:error:] : 168 -> 172
~ -[SiriCoreSQLiteDatabase(Insert) insertIntoTableWithName:record:error:] : 500 -> 496
~ ___71-[SiriCoreSQLiteDatabase(Insert) insertIntoTableWithName:record:error:]_block_invoke : 184 -> 188
~ -[SiriCoreSQLiteDatabase(Insert) insertIntoTableWithName:valueMap:error:] : 460 -> 464
~ ___73-[SiriCoreSQLiteDatabase(Insert) insertIntoTableWithName:valueMap:error:]_block_invoke : 108 -> 112
~ -[SiriCoreSQLiteDatabase(Delete) deleteFromTableWithName:indexedBy:criterion:error:] : 288 -> 292
~ -[SiriCoreSQLiteTableConstraint copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteTableConstraint initWithName:type:columnNames:] : 164 -> 160
~ +[SiriCoreSQLiteTableConstraint(SiriCoreSQLiteTableConstraintConveniences) uniqueTableConstraintWithName:columnNames:] : 120 -> 116
~ +[SiriCoreSQLiteTableConstraint(SiriCoreSQLiteTableConstraintConveniences) primaryKeyTableConstraintWithName:columnNames:] : 120 -> 116
~ -[SiriCoreNWConnection _addCorrespondingMetricsFromConnection:inState:] : 1464 -> 1572
~ ___71-[SiriCoreNWConnection _addCorrespondingMetricsFromConnection:inState:]_block_invoke : 1196 -> 1292
~ -[SiriCoreNWConnection _getAttemptedEndpoints] : 528 -> 524
~ ___60-[SiriCoreNWConnection providerStatsIndicatePoorLinkQuality]_block_invoke : 488 -> 492
~ -[SiriCoreNWConnection _setParametersForHost:useTLS:initialPayload:] : 1004 -> 1012
~ ___68-[SiriCoreNWConnection _setParametersForHost:useTLS:initialPayload:]_block_invoke : 164 -> 168
~ ___68-[SiriCoreNWConnection _setParametersForHost:useTLS:initialPayload:]_block_invoke_2 : 232 -> 240
~ -[SiriCoreNWConnection resolvedHost] : 8 -> 56
~ -[SiriCoreNWConnection _closeWithError:] : 908 -> 892
~ ___40-[SiriCoreNWConnection _closeWithError:]_block_invoke : 256 -> 268
~ -[SiriCoreNWConnection updateConnectionMetrics:completion:] : 900 -> 960
~ -[SiriCoreNWConnection analysisInfo] : 224 -> 232
~ ___45-[SiriCoreNWConnection writeData:completion:]_block_invoke : 416 -> 428
~ -[SiriCoreNWConnection readData:] : 264 -> 268
~ ___33-[SiriCoreNWConnection readData:]_block_invoke : 492 -> 496
~ -[SiriCoreNWConnection _setupOpenSlowTimer] : 244 -> 240
~ ___43-[SiriCoreNWConnection _setupOpenSlowTimer]_block_invoke : 432 -> 436
~ -[SiriCoreNWConnection _setupOpenTimer] : 268 -> 264
~ ___39-[SiriCoreNWConnection _setupOpenTimer]_block_invoke : 436 -> 440
~ -[SiriCoreNWConnection _configureConnection:] : 828 -> 856
~ ___45-[SiriCoreNWConnection _configureConnection:]_block_invoke : 992 -> 1012
~ ___45-[SiriCoreNWConnection _configureConnection:]_block_invoke.27 : 840 -> 868
~ ___45-[SiriCoreNWConnection _configureConnection:]_block_invoke.50 : 296 -> 292
~ -[SiriCoreNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:] : 464 -> 456
~ ___88-[SiriCoreNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:]_block_invoke : 132 -> 136
~ -[SiriCoreNWConnection _getNWConnectionWithInitialData:completion:] : 960 -> 988
~ -[SiriCoreNWConnection _setupStaleConnectionTimer] : 332 -> 328
~ ___50-[SiriCoreNWConnection _setupStaleConnectionTimer]_block_invoke : 440 -> 444
~ ___53-[SiriCoreNWConnection _startConnectionUnviableTimer]_block_invoke : 184 -> 188
~ -[SiriCoreNWConnection _connectionId] : 8 -> 56
~ -[SiriCoreNWConnection _url] : 8 -> 56
~ -[SiriCoreNWConnection _queue] : 8 -> 56
~ -[SiriCoreNWConnection initWithQueue:] : 124 -> 116
~ -[SiriCoreSpeechPacket setPackets:] : 12 -> 64
~ -[SiriCoreSpeechPacket copyWithZone:] : 148 -> 156
~ -[SiriCoreSpeechPacket groupIdentifier] : 16 -> 64
~ -[SiriCoreSpeechPacket encodedClassName] : 16 -> 64
~ -[SiriCoreSpeechPacket description] : 156 -> 164
~ -[SiriCoreSQLiteQuery description] : 428 -> 444
~ -[SiriCoreSQLiteQuery initWithString:statement:parameters:recordBuilder:options:] : 236 -> 224
~ _SiriCoreUserAgentStringCreate : 268 -> 296
~ _productTypeFromUserAgentString : 172 -> 184
~ _buildVersionFromUserAgentString : 184 -> 188
~ -[SiriCoreSQLiteColumnDescription copyWithZone:] : 4 -> 40
~ -[SiriCoreSQLiteColumnDescription initWithName:type:constraints:] : 192 -> 184
~ +[SiriCoreSQLiteColumnDescription(SiriCoreSQLiteColumnDescriptionConveniences) uniqueTextColumnWithName:] : 244 -> 248
~ +[SiriCoreSQLiteColumnDescription(SiriCoreSQLiteColumnDescriptionConveniences) integerPrimaryKeyColumnWithName:] : 244 -> 248
~ +[SiriCoreTrialUtilities experimentIdentifiersForTrialProject:trialNamespace:] : 120 -> 128
~ +[SiriCoreTrialUtilities getDirectoryPathForTrialProject:trialNamespace:trialFactor:] : 432 -> 452
~ +[SiriCoreTrialUtilities trialClientForProject:] : 400 -> 404
~ -[SiriCoreConnectionTCPInfoMetrics description] : 216 -> 224
~ -[SiriCoreConnectionTCPInfoMetrics initWithInterfaceName:rttCurrent:rttSmoothed:rttVariance:rttBest:packetsSent:bytesSent:bytesRetransmitted:bytesUnacked:packetsReceived:bytesReceived:duplicateBytesReceived:outOfOrderBytesReceived:sendBufferBytes:sendBandwidth:synRetransmits:tfoSynDataAcked:] : 808 -> 752
~ -[SiriCoreAceConnectionAnalysisInfo initWithConnectionURL:interfaceIndex:sendBufferSize:wwanPreferred:connectionType:policyId:] : 256 -> 240
~ -[SiriCoreSyncDatabase _enumerateKey:updatedAfter:fromTable:usingBlock:error:] : 640 -> 644
~ ___78-[SiriCoreSyncDatabase _enumerateKey:updatedAfter:fromTable:usingBlock:error:]_block_invoke : 816 -> 912
~ -[SiriCoreSyncDatabase _countKey:fromTable:updatedAfter:error:] : 380 -> 404
~ -[SiriCoreSyncDatabase _insertSyncRec:intoTable:error:] : 748 -> 784
~ -[SiriCoreSyncDatabase removeAllItemsOfKey:error:] : 468 -> 476
~ -[SiriCoreSyncDatabase remove:error:] : 800 -> 828
~ -[SiriCoreSyncDatabase succeedOrRollbackOnFail:error:whileExecuting:] : 680 -> 676
~ -[SiriCoreSyncDatabase rollbackTransactionWithError:] : 240 -> 248
~ -[SiriCoreSyncDatabase commitTransactionWithError:] : 240 -> 248
~ -[SiriCoreSyncDatabase beginTransactionWithError:] : 240 -> 248
~ -[SiriCoreSyncDatabase prepare] : 1064 -> 1024
~ -[SiriCoreSyncDatabase initWithPath:] : 168 -> 160
~ +[SiriCoreSyncDatabase removeCurrentSyncDatabase] : 552 -> 568
~ __SiriCoreSharedResourcesDirectory : 84 -> 100
~ ____SiriCoreSharedResourcesDirectory_block_invoke : 92 -> 100
~ +[SiriCoreSyncDatabase currentSyncDatabase] : 284 -> 316
~ -[NSDate(SiriCoreUtilities) siriCore_isWithin1HourInterval] : 96 -> 100
~ -[NSDate(SiriCoreUtilities) siriCore_isWithin24HourInterval] : 96 -> 100

```
