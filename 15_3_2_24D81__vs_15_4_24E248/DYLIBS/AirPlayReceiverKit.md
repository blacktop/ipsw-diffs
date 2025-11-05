## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/Versions/A/AirPlayReceiverKit`

```diff

-845.5.1.0.0
-  __TEXT.__text: 0x21df4
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0xfa4
-  __TEXT.__cstring: 0x7c68
+850.19.1.0.0
+  __TEXT.__text: 0x231d0
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x1214
+  __TEXT.__cstring: 0x7c69
   __TEXT.__const: 0x62
-  __TEXT.__gcc_except_tab: 0x44c
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__gcc_except_tab: 0x470
+  __TEXT.__unwind_info: 0xa40
   __TEXT.__objc_classname: 0x1bd
   __TEXT.__objc_methname: 0x47aa
   __TEXT.__objc_methtype: 0xdbb

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1050
+  __DATA_CONST.__objc_selrefs: 0x1120
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0xb10
   __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0x23a8
+  __AUTH_CONST.__objc_const: 0x1f40
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x254

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 518D780C-B20D-3121-B99D-2236A5C938D1
-  Functions: 579
-  Symbols:   1765
+  UUID: 601A8EBA-2232-3100-9E1A-3800A547C97C
+  Functions: 877
+  Symbols:   2081
   CStrings:  1809
 
Symbols:
+ +[APRKStreamRenderingManager getAdvertisingAccessMode].cold.1
+ +[APRKStreamRenderingManager getAdvertisingAccessMode].cold.2
+ +[APRKStreamRenderingManager getAppHasSetAdvertisingAccessModeEntitlement].cold.1
+ +[APRKStreamRenderingManager listeningForAlternateBonjourBrowsing].cold.1
+ +[APRKStreamRenderingManager setAdvertisingAccessMode:withError:].cold.1
+ +[APRKStreamRenderingManager setAdvertisingAccessMode:withError:].cold.2
+ +[APRKStreamRenderingManager setAdvertisingAccessMode:withError:].cold.3
+ +[APRKStreamRenderingManager setAdvertisingAccessMode:withError:].cold.4
+ +[APRKStreamRenderingManager setListeningForAlternateBonjourBrowsing:].cold.1
+ +[APRKStreamRenderingManager sharedInstance].cold.1
+ +[APRKUtilities secureStopURL].cold.1
+ -[APRKContentKeyHelper contentKeySessionDidGenerateExpiredSessionReport:].cold.1
+ -[APRKContentKeyHelper contentKeySessionDidGenerateExpiredSessionReport:].cold.2
+ -[APRKContentKeyHelper forgetAllActiveContentKeyRequests].cold.1
+ -[APRKContentKeyHelper init].cold.1
+ -[APRKContentKeyHelper init].cold.2
+ -[APRKContentKeyHelper processStreamingKeyRequestWithDictionary:withCompletionBlock:].cold.1
+ -[APRKContentKeyHelper processStreamingKeyRequestWithDictionary:withCompletionBlock:].cold.2
+ -[APRKContentKeyHelper processStreamingKeyRequestWithDictionary:withCompletionBlock:].cold.3
+ -[APRKContentKeyHelper processUnhandledURLResponseWithDictionary:error:].cold.1
+ -[APRKContentKeyHelper processUnhandledURLResponseWithDictionary:error:].cold.2
+ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.1
+ -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.2
+ -[APRKMediaPlayer _fixedIPContentLocationFromURLString:error:].cold.1
+ -[APRKMediaPlayer _fixedIPContentLocationFromURLString:error:].cold.2
+ -[APRKMediaPlayer _getPropertyWithDictionary:].cold.1
+ -[APRKMediaPlayer _getPropertyWithDictionary:].cold.2
+ -[APRKMediaPlayer _getPropertyWithDictionary:].cold.3
+ -[APRKMediaPlayer _getPropertyWithDictionary:].cold.4
+ -[APRKMediaPlayer _handleCurrentItemChangedNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentItemFailedToPlayToEndNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentItemFailedToPlayToEndNotification:].cold.2
+ -[APRKMediaPlayer _handleCurrentItemPlaybackStalledNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentItemPlaybackStalledNotification:].cold.2
+ -[APRKMediaPlayer _handleCurrentItemPlayedToEndNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentItemPlayedToEndNotification:].cold.2
+ -[APRKMediaPlayer _handleCurrentPlayerItemMediaSelectionDidChangeNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentPlayerItemMediaSelectionDidChangeNotification:].cold.2
+ -[APRKMediaPlayer _handleCurrentPlayerItemNewAccessLogEntryNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPauseBufferingNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPauseBufferingNotification:].cold.2
+ -[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPausePlaybackNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPausePlaybackNotification:].cold.2
+ -[APRKMediaPlayer _handleSeekDidCompleteNotification:].cold.1
+ -[APRKMediaPlayer _handleSeekDidCompleteNotification:].cold.2
+ -[APRKMediaPlayer _handleTimeJumpedNotification:].cold.1
+ -[APRKMediaPlayer _handleTimeJumpedNotification:].cold.2
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.1
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.2
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.3
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.4
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.5
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.6
+ -[APRKMediaPlayer _processMessageWithDictionaryInternal:].cold.1
+ -[APRKMediaPlayer _processStreamingKeyWithDictionary:].cold.1
+ -[APRKMediaPlayer _processUnhandledURLWithDictionary:].cold.1
+ -[APRKMediaPlayer _processUnhandledURLWithDictionary:].cold.2
+ -[APRKMediaPlayer _removePlayQueueItemWithDictionary:].cold.1
+ -[APRKMediaPlayer _removePlayQueueItemWithDictionary:].cold.2
+ -[APRKMediaPlayer _removePlayQueueItemWithDictionary:].cold.3
+ -[APRKMediaPlayer _sendUpstreamErrorMessageWithError:].cold.1
+ -[APRKMediaPlayer _sendUpstreamMessageWithDictionary:].cold.1
+ -[APRKMediaPlayer _sendUpstreamPlaybackStateMessageWithPlaybackStateString:stoppedBecauseInterrupted:].cold.1
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.1
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.2
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.3
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.4
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.5
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.6
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.7
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.8
+ -[APRKMediaPlayer _setRateWithDictionary:].cold.1
+ -[APRKMediaPlayer _setRateWithDictionary:].cold.2
+ -[APRKMediaPlayer _setRateWithDictionary:].cold.3
+ -[APRKMediaPlayer _setRateWithDictionary:].cold.4
+ -[APRKMediaPlayer _stopWithDictionary:].cold.1
+ -[APRKMediaPlayer _updateAudioSessionMode:].cold.1
+ -[APRKMediaPlayer _updateAudioSessionMode:].cold.2
+ -[APRKMediaPlayer _updateAudioSessionMode:].cold.3
+ -[APRKMediaPlayer invalidate].cold.1
+ -[APRKMediaPlayer processMessageWithIDAndDictionaryAsync:messageSessionID:].cold.1
+ -[APRKMediaPlayer selectedMediaArrayForItem:].cold.1
+ -[APRKPlayerItem initWithDictionary:resourceLoaderHelper:contentKeyHelper:options:].cold.1
+ -[APRKPlayerItem initWithDictionary:resourceLoaderHelper:contentKeyHelper:options:].cold.2
+ -[APRKPlayerItem setTextStyleRulesUsingArray:].cold.1
+ -[APRKPlayerItem setTextStyleRulesUsingArray:].cold.2
+ -[APRKResourceLoaderHelper forgetAllActiveResourceLoadingRequests].cold.1
+ -[APRKResourceLoaderHelper init].cold.1
+ -[APRKResourceLoaderHelper processUnhandledURLResponseWithDictionary:error:].cold.1
+ -[APRKResourceLoaderHelper resourceLoader:didCancelAuthenticationChallenge:].cold.1
+ -[APRKResourceLoaderHelper resourceLoader:shouldWaitForLoadingOfRequestedResource:].cold.1
+ -[APRKResourceLoaderHelper resourceLoader:shouldWaitForResponseToAuthenticationChallenge:].cold.1
+ -[APRKStreamRecorder _recordSampleBuffer:toTrackWithID:].cold.1
+ -[APRKStreamRecorder startRecordingAtURL:].cold.1
+ -[APRKStreamRecorder startRecordingAtURL:].cold.2
+ -[APRKStreamRenderer _cleanupPreviousRecordingIfExisting].cold.1
+ -[APRKStreamRenderer _enqueueSampleBufferForRecording:isAudioSBuf:].cold.1
+ -[APRKStreamRenderer _enqueueSampleBufferForRecording:isAudioSBuf:].cold.2
+ -[APRKStreamRenderer _performStartRecordingWithOutputURL:].cold.1
+ -[APRKStreamRenderer _performStopRecording].cold.1
+ -[APRKStreamRenderer _performUIControllerActionWithBlock:].cold.1
+ -[APRKStreamRenderer _performUIControllerActionWithBlock:].cold.2
+ -[APRKStreamRenderer initWithUniqueID:clientName:UIController:useCALayerForMirroring:].cold.1
+ -[APRKStreamRenderer makeNowPlayingRenderer].cold.1
+ -[APRKStreamRenderer postVideoV1EventWithType:params:].cold.1
+ -[APRKStreamRenderer setSampleBufferDelegate:].cold.1
+ -[APRKStreamRenderer setVideoV1Delegate:withDelegateQueue:].cold.1
+ -[APRKStreamRenderer updateDisplayInfo].cold.1
+ -[APRKStreamRenderingManager _customDisplayHDRModeFromPrefsWithDefault:].cold.1
+ -[APRKStreamRenderingManager _customDisplayHDRModeFromPrefsWithDefault:].cold.2
+ -[APRKStreamRenderingManager _setPTPClockEnabled:].cold.1
+ -[APRKStreamRenderingManager _setRandomPassword].cold.1
+ -[APRKStreamRenderingManager _setRandomPassword].cold.2
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.1
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.10
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.2
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.3
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.4
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.5
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.6
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.7
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.8
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.9
+ -[APRKStreamRenderingManager altAdvertisingEnabled].cold.1
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.1
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.2
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.3
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.4
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.5
+ -[APRKStreamRenderingManager assistedInfoForAWDL].cold.6
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.1
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.2
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.3
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.4
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.5
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.6
+ -[APRKStreamRenderingManager assistedInfoForDiscovery].cold.7
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.1
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.2
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.3
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.4
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.5
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.6
+ -[APRKStreamRenderingManager assistedInfoForIPAddress:].cold.7
+ -[APRKStreamRenderingManager assistedInfoForMode:options:].cold.1
+ -[APRKStreamRenderingManager assistedInfoForMode:options:].cold.2
+ -[APRKStreamRenderingManager assistedInfoForMode:options:].cold.3
+ -[APRKStreamRenderingManager forcePINRefresh].cold.1
+ -[APRKStreamRenderingManager init].cold.1
+ -[APRKStreamRenderingManager isAirPlayReceiverSupported].cold.1
+ -[APRKStreamRenderingManager setAltAdvertisingEnabled:].cold.1
+ -[APRKStreamRenderingManager setDemoModeEnabled:].cold.1
+ -[APRKStreamRenderingManager setDisplayHDRMode:].cold.1
+ -[APRKStreamRenderingManager setEnableMixingMediaAudio:].cold.1
+ -[APRKStreamRenderingManager setForcePermissionDialog:].cold.1
+ -[APRKStreamRenderingManager setPreemptionPolicy:].cold.1
+ -[APRKStreamRenderingManager setShouldForwardLayers:].cold.1
+ -[APRKStreamRenderingManager setSupportsSenderUIEvents:].cold.1
+ -[APRKStreamRenderingManager setUseCALayerForMirroring:].cold.1
+ -[APRKStreamRenderingManager setUsesHomeKitIntegration:].cold.1
+ -[APRKStreamRenderingManager setUsesHomeKitIntegration:].cold.2
+ -[APRKStreamRenderingManager stopReceiverServer].cold.1
+ -[APRKStreamRenderingManager stopReceiverServer].cold.2
+ -[APRKStreamRenderingManager stopReceiverServer].cold.3
+ -[APRKStreamRenderingManager stopReceiverServer].cold.4
+ SBufConsumerCreate.cold.1
+ SBufConsumerCreate.cold.2
+ SBufConsumerCreate.cold.3
+ SBufConsumerCreate.cold.4
+ UIControllerCopyTLSInfo.cold.1
+ UIControllerCreate.cold.1
+ UIControllerCreate.cold.2
+ UIControllerPostVideoV1Event.cold.1
+ UIControllerPostVideoV1Event.cold.2
+ UIControllerPostVideoV1Event.cold.3
+ UIControllerSendUpstreamMessage.cold.1
+ UIControllerSendUpstreamMessage.cold.2
+ UIControllerSendUpstreamMessage.cold.3
+ UIControllerSendUpstreamMessage.cold.4
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __21-[AWDLActivator init]_block_invoke.cold.1
+ __38-[AWDLActivator startWithMaxDuration:]_block_invoke.cold.1
+ __38-[AWDLActivator startWithMaxDuration:]_block_invoke.cold.2
+ __38-[AWDLActivator startWithMaxDuration:]_block_invoke.cold.3
+ __38-[AWDLActivator startWithMaxDuration:]_block_invoke.cold.4
+ __39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke.169.cold.1
+ __39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke.176.cold.1
+ __42-[APRKMediaPlayer _setRateWithDictionary:]_block_invoke.cold.1
+ __42-[APRKStreamRenderer _updateStreamingMode]_block_invoke_2.cold.1
+ __43-[APRKStreamRenderer processSenderUIEvent:]_block_invoke.cold.1
+ __44+[APRKStreamRenderingManager sharedInstance]_block_invoke.cold.1
+ __48-[APRKMediaPlayer _pausePlayerIfNeededForState:]_block_invoke.cold.1
+ __49-[APRKStreamRenderingManager _isPermittedClient:]_block_invoke.cold.1
+ __50-[APRKStreamRenderingManager _addPermittedClient:]_block_invoke.cold.1
+ __51-[APRKStreamRenderingManager _initPermittedClients]_block_invoke.cold.1
+ __54-[APRKMediaPlayer _handleSeekDidCompleteNotification:]_block_invoke.cold.1
+ __54-[APRKMediaPlayer _handleSeekDidCompleteNotification:]_block_invoke_2.cold.1
+ __54-[APRKMediaPlayer _sendUpstreamMessageWithDictionary:]_block_invoke.cold.1
+ __54-[APRKStreamRenderer processHidePasscodePromptRequest]_block_invoke.cold.1
+ __54-[APRKStreamRenderer setIsMirroringVideoStreamPaused:]_block_invoke.cold.1
+ __55-[APRKStreamRenderer processShowPasscodePromptRequest:]_block_invoke.cold.1
+ __55-[APRKStreamRenderer processShowPasscodePromptRequest:]_block_invoke.cold.2
+ __57-[APRKMediaPlayer _registerNotificationHandlersForPlayer]_block_invoke.cold.1
+ __57-[APRKStreamRenderingManager removeRendererWithUniqueID:]_block_invoke.cold.1
+ __57-[APRKStreamRenderingManager removeRendererWithUniqueID:]_block_invoke_2.cold.1
+ __58-[APRKStreamRenderer _performStartRecordingWithOutputURL:]_block_invoke_2.cold.1
+ __59-[APRKMediaPlayer _unregisterNotificationHandlersForPlayer]_block_invoke.cold.1
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.1
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.2
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.3
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.4
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.5
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.6
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.7
+ __66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.cold.1
+ __66-[APRKStreamRenderer processStartScreenPresentationWithSessionID:]_block_invoke.cold.1
+ __66-[APRKStreamRenderer processStartScreenPresentationWithSessionID:]_block_invoke.cold.2
+ __66-[APRKStreamRenderer processStartScreenPresentationWithSessionID:]_block_invoke_2.cold.1
+ __66-[APRKStreamRenderer processStopAudioSessionRequestWithSessionID:]_block_invoke.cold.1
+ __66-[APRKStreamRenderer processStopAudioSessionRequestWithSessionID:]_block_invoke_3.cold.1
+ __68-[APRKStreamRenderingManager processHideGlobalPasscodePromptRequest]_block_invoke.cold.1
+ __69-[APRKStreamRenderer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.cold.1
+ __70-[APRKMediaPlayer _unregisterNotificationHandlersAndRemovePlayerItem:]_block_invoke.cold.1
+ __70-[APRKMediaPlayer _unregisterNotificationHandlersAndRemovePlayerItem:]_block_invoke.cold.2
+ __74+[APRKStreamRenderingManager getAppHasSetAdvertisingAccessModeEntitlement]_block_invoke.cold.1
+ __74+[APRKStreamRenderingManager getAppHasSetAdvertisingAccessModeEntitlement]_block_invoke.cold.2
+ __74+[APRKStreamRenderingManager getAppHasSetAdvertisingAccessModeEntitlement]_block_invoke.cold.3
+ __74-[APRKMediaPlayer processMessageWithIDAndDictionarySync:messageSessionID:]_block_invoke.cold.1
+ __75-[APRKStreamRenderingManager isAllowedToProceedForClientWithName:clientID:]_block_invoke.207.cold.1
+ __75-[APRKStreamRenderingManager isAllowedToProceedForClientWithName:clientID:]_block_invoke.212.cold.1
+ __78-[APRKMediaPlayer _registerNotificationHandlersAndInsertPlayerItem:afterItem:]_block_invoke.cold.1
+ __78-[APRKMediaPlayer _registerNotificationHandlersAndInsertPlayerItem:afterItem:]_block_invoke.cold.2
+ __80-[APRKStreamRenderer processStartVideoPlaybackRequestWithWithSessionID:version:]_block_invoke.77.cold.1
+ __81-[APRKStreamRenderer processStartAudioSessionRequestWithSessionID:isScreenAudio:]_block_invoke.cold.1
+ __81-[APRKStreamRenderer processStartAudioSessionRequestWithSessionID:isScreenAudio:]_block_invoke.cold.2
+ __84-[APRKStreamRenderingManager processShowGlobalPasscodePromptRequest:withClientName:]_block_invoke.cold.1
+ __85-[APRKContentKeyHelper processStreamingKeyRequestWithDictionary:withCompletionBlock:]_block_invoke.cold.1
+ __87-[APRKStreamRenderingManager createStreamRendererWithUniqueID:clientName:UIController:]_block_invoke.cold.1
+ __87-[APRKStreamRenderingManager createStreamRendererWithUniqueID:clientName:UIController:]_block_invoke_2.cold.1
+ __sbufConsumer_connect_block_invoke.cold.1
+ __sbufConsumer_enqueueAudioSample_block_invoke.cold.1
+ __sbufConsumer_enqueueVideoFrame_block_invoke.cold.1
+ __uiController_copyProperty_block_invoke_4.cold.1
+ __uiController_handleDateRangeEventV1_block_invoke.cold.1
+ _memcpy
+ sbufConsumer_disconnect.cold.1
+ sbufConsumer_disconnect.cold.2
+ sbufConsumer_finalize.cold.1
+ uiController_controlVideoPlayback.cold.1
+ uiController_controlVideoPlayback.cold.2
+ uiController_copyProperty.cold.1
+ uiController_finalize.cold.1
+ uiController_handleDateRangeEventV1.cold.1
+ uiController_handleDateRangeEventV1.cold.2
+ uiController_handleDateRangeEventV1.cold.3
+ uiController_handleErrorEventV1.cold.1
+ uiController_handleErrorEventV1.cold.2
+ uiController_handleFailedURLRequestV1.cold.1
+ uiController_handleFailedURLRequestV1.cold.2
+ uiController_handleMetaDataEventV1.cold.1
+ uiController_handleMetaDataEventV1.cold.2
+ uiController_handleOtherEventV1.cold.1
+ uiController_handleOtherEventV1.cold.2
+ uiController_handlePlaylistEventV1.cold.1
+ uiController_handlePlaylistEventV1.cold.2
+ uiController_handleSenderUIEventsChannelIncomingMessage.cold.1
+ uiController_hidePIN.cold.1
+ uiController_isAllowedToProceed.cold.1
+ uiController_setProperty.cold.1
+ uiController_showPIN.cold.1
+ uiController_startAudioSession.cold.1
+ uiController_startScreenPresentation.cold.1
+ uiController_startScreenPresentation.cold.2
+ uiController_startSession.cold.1
+ uiController_startVideoPlayback.cold.1
+ uiController_startVideoPlayback.cold.2
+ uiController_stopAudioSession.cold.1
+ uiController_stopScreenPresentation.cold.1
+ uiController_stopVideoPlayback.cold.1
CStrings:
+ "850.19.1"
- "845.5.1"

```
