## NearField

> `/System/Library/PrivateFrameworks/NearField.framework/NearField`

```diff

-340.36.0.0.0
-  __TEXT.__text: 0x927ac
+341.9.0.0.0
+  __TEXT.__text: 0x94b90
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x4ea8
-  __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x5d94
-  __TEXT.__oslogstring: 0x47d7
+  __TEXT.__objc_methlist: 0x4ef0
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0x5fa3
+  __TEXT.__oslogstring: 0x4964
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x183c
-  __TEXT.__objc_classname: 0xe05
-  __TEXT.__objc_methname: 0xc723
-  __TEXT.__objc_methtype: 0x3346
-  __TEXT.__objc_stubs: 0x7860
+  __TEXT.__unwind_info: 0x18b4
+  __TEXT.__objc_classname: 0xe1f
+  __TEXT.__objc_methname: 0xc741
+  __TEXT.__objc_methtype: 0x33e4
+  __TEXT.__objc_stubs: 0x77a0
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x2370
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x2410
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9e88
-  __DATA_CONST.__objc_selrefs: 0x2de0
-  __AUTH_CONST.__cfstring: 0x3d20
+  __DATA_CONST.__objc_const: 0x9ff0
+  __DATA_CONST.__objc_selrefs: 0x2e00
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__cfstring: 0x3ee0
   __AUTH_CONST.__objc_intobj: 0x738
-  __AUTH_CONST.__objc_const: 0x2c40
+  __AUTH_CONST.__objc_const: 0x2cd0
   __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH.__objc_data: 0xd20
+  __AUTH.__objc_data: 0xd70
   __DATA.__objc_protorefs: 0x160
-  __DATA.__objc_classrefs: 0x3f0
-  __DATA.__objc_superrefs: 0x210
-  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_classrefs: 0x400
+  __DATA.__objc_superrefs: 0x218
+  __DATA.__objc_ivar: 0x4e4
   __DATA.__data: 0x1980
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_ivar: 0x140
+  __DATA_DIRTY.__objc_ivar: 0x148
   __DATA_DIRTY.__objc_data: 0x10e0
   __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E943F62C-A27A-3E2C-A88A-E57A8A62CEE1
-  Functions: 2304
-  Symbols:   7400
-  CStrings:  4389
+  UUID: FFF7B1AB-3E83-37FF-8632-88C5EEC6F1B1
+  Functions: 2327
+  Symbols:   7463
+  CStrings:  4442
 
Symbols:
+ +[NFReaderSessionPollConfig pollConfigWithTechnology:]
+ -[NFConnectionHandoverController initWithType:initiator:callbackQueue:]
+ -[NFConnectionHandoverInitiator handleSessionSuspended:token:reason:field:]
+ -[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]
+ -[NFConnectionHandoverReceiver _startWithAutoResume:]
+ -[NFConnectionHandoverReceiver forceResumeWithCompletionHandler:]
+ -[NFConnectionHandoverReceiver handleSessionResumed]
+ -[NFConnectionHandoverReceiver hceSession:triggeredByField:started:]
+ -[NFConnectionHandoverReceiver roleBroadcastInBackground]
+ -[NFConnectionHandoverReceiver startWithAutoResumeOnFieldDisable]
+ -[NFHCESession restartDiscovery]
+ -[NFHCESession resumeSessionFromWaitingOnFieldWithCompletion:]
+ -[NFHCESession suspensionStateUpdate:triggeredByField:]
+ -[NFHardwareManager startReaderSessionWithAttributes:completion:]
+ -[NFReaderSession startPollingWithConfig:error:]
+ -[NFReaderSessionPollConfig .cxx_destruct]
+ -[NFReaderSessionPollConfig asDictionary]
+ -[NFReaderSessionPollConfig ecp]
+ -[NFReaderSessionPollConfig fieldDetect]
+ -[NFReaderSessionPollConfig init]
+ -[NFReaderSessionPollConfig lpcd]
+ -[NFReaderSessionPollConfig pollDuration]
+ -[NFReaderSessionPollConfig setEcp:]
+ -[NFReaderSessionPollConfig setFieldDetect:]
+ -[NFReaderSessionPollConfig setLpcd:]
+ -[NFReaderSessionPollConfig setPollDuration:]
+ -[NFReaderSessionPollConfig setSkipMifareClassify:]
+ -[NFReaderSessionPollConfig setTechnology:]
+ -[NFReaderSessionPollConfig skipMifareClassify]
+ -[NFReaderSessionPollConfig technology]
+ -[NFRemoteAdminManager appletsDeleted:]
+ -[NFSession didEndCallback]
+ -[NFSession didStartCallback]
+ _ACCELERATED_POLL_DURATION_IN_MS
+ _CH_ECP_FRAME_PREFERRED_RX
+ _OBJC_CLASS_$_NFReaderSessionPollConfig
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_IVAR_$_NFConnectionHandoverController._initiator
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._ecp
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._fieldDetect
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._lpcd
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._pollDuration
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._skipMifareClassify
+ _OBJC_IVAR_$_NFReaderSessionPollConfig._technology
+ _OBJC_METACLASS_$_NFReaderSessionPollConfig
+ __GenerateInitiatorECPFrame
+ __GeneratePreferredReceiverECPFrame
+ __OBJC_$_CLASS_METHODS_NFReaderSessionPollConfig
+ __OBJC_$_INSTANCE_METHODS_NFReaderSessionPollConfig
+ __OBJC_$_INSTANCE_VARIABLES_NFReaderSessionPollConfig
+ __OBJC_$_PROP_LIST_NFReaderSessionPollConfig
+ __OBJC_CLASS_RO_$_NFReaderSessionPollConfig
+ __OBJC_METACLASS_RO_$_NFReaderSessionPollConfig
+ ___106-[NFSeshatSession allocateSlot:authorizingUser:authorizingUserToken:outToken:outWriteCount:trackingError:]_block_invoke.28
+ ___112-[NFReaderSession felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:error:]_block_invoke.129
+ ___27-[NFTrustSession listKeys:]_block_invoke.34
+ ___29-[NFHardwareManager preWarm:]_block_invoke.171
+ ___29-[NFSession _endProxySession]_block_invoke.27
+ ___30-[NFSession prioritizeSession]_block_invoke.31
+ ___31-[NFSession activateWithToken:]_block_invoke.36
+ ___32-[NFHCESession restartDiscovery]_block_invoke
+ ___33-[NFPeerPaymentSession deleteKey]_block_invoke.12
+ ___33-[NFSession setSessionTimeLimit:]_block_invoke.15
+ ___34-[NFHardwareManager setChipscope:]_block_invoke.241
+ ___34-[NFTrustSession deleteKey:error:]_block_invoke.21
+ ___35-[NFReaderSession ndefWrite:error:]_block_invoke.119
+ ___36-[NFReaderSession connectTag:error:]_block_invoke.110
+ ___36-[NFReaderSession performVAS:error:]_block_invoke.136
+ ___36-[NFReaderSession transceive:error:]_block_invoke.123
+ ___37-[NFNdefTagSession setTagData:error:]_block_invoke.23
+ ___37-[NFReaderSession ndefReadWithError:]_block_invoke.120
+ ___37-[NFSecureElementReaderSession stop:]_block_invoke.29
+ ___38-[NFNdefTagSession enableWrite:error:]_block_invoke.26
+ ___38-[NFSecureElementReaderSession start:]_block_invoke.28
+ ___39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.242
+ ___39-[NFReaderSession setECPPayload:error:]_block_invoke.101
+ ___39-[NFSession createSessionHandoffToken:]_block_invoke.34
+ ___40-[NFHardwareManager startSesHatSession:]_block_invoke.162
+ ___40-[NFNdefTagSession getTagDataWithError:]_block_invoke.24
+ ___40-[NFReaderSession felicaStateWithError:]_block_invoke.125
+ ___40-[NFReaderSession stopPollingWithError:]_block_invoke.106
+ ___40-[NFReaderSession updateUIAlertMessage:]_block_invoke.134
+ ___40-[NFRemoteAdminManager registrationInfo]_block_invoke.82
+ ___41-[NFReaderSession startPollingWithError:]_block_invoke.102
+ ___41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.104
+ ___41-[NFSeshatSession getHash:trackingError:]_block_invoke.67
+ ___42-[NFReaderSession checkPresenceWithError:]_block_invoke.115
+ ___42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.84
+ ___42-[NFTrustSession createKey:request:error:]_block_invoke.19
+ ___43-[NFNdefTagSession stopEmulationWithError:]_block_invoke.22
+ ___43-[NFReaderSession formatNdefWithKey:error:]_block_invoke.117
+ ___43-[NFReaderSession restartPollingWithError:]_block_invoke.107
+ ___43-[NFReaderSession setPollingProfile:error:]_block_invoke.139
+ ___43-[NFReaderSession skipMifareClassification]_block_invoke.135
+ ___43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.103
+ ___45-[NFECommercePaymentSession didStartSession:]_block_invoke.13
+ ___45-[NFECommercePaymentSession didStartSession:]_block_invoke.18
+ ___45-[NFReaderSession startLPCDPollingWithError:]_block_invoke.103
+ ___45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.106
+ ___45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.86
+ ___45-[NFSecureElementLoggingSession storeACLogs:]_block_invoke.15
+ ___46-[NFReaderSession felicaRequestService:error:]_block_invoke.130
+ ___46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.88
+ ___46-[NFSecureElementReaderSession disconnectTag:]_block_invoke.46
+ ___47-[NFLPEMConfigSession enableLPEMFeature:error:]_block_invoke.38
+ ___47-[NFSecureElementReaderSession stopVASPolling:]_block_invoke.33
+ ___47-[NFSeshatSession obliterateWithTrackingError:]_block_invoke.80
+ ___48-[NFLPEMConfigSession disableLPEMFeature:error:]_block_invoke.33
+ ___48-[NFLPEMConfigSession getLPEMFeaturesWithError:]_block_invoke.44
+ ___48-[NFReaderSession startPollingWithConfig:error:]_block_invoke
+ ___48-[NFReaderSession startPollingWithConfig:error:]_block_invoke.105
+ ___49-[NFSecureElementReaderSession connectTag:error:]_block_invoke.45
+ ___49-[NFSecureElementReaderSession performVAS:error:]_block_invoke.34
+ ___49-[NFSecureElementReaderSession transceive:error:]_block_invoke.30
+ ___50-[NFSecureElementLoggingSession enableSMBLogging:]_block_invoke.20
+ ___51-[NFReaderSession startPollingForTechnology:error:]_block_invoke.104
+ ___51-[NFSecureElementLoggingSession clearLogs:forSEID:]_block_invoke.14
+ ___52-[NFConnectionHandoverReceiver handleSessionResumed]_block_invoke
+ ___52-[NFLPEMConfigSession getLPEMBluetoothLogWithError:]_block_invoke.50
+ ___52-[NFSecureElementLoggingSession getSMBLogWithError:]_block_invoke.21
+ ___52-[NFSecureElementReaderSession selectApplets:error:]_block_invoke.27
+ ___53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.438
+ ___53-[NFConnectionHandoverReceiver _startWithAutoResume:]_block_invoke
+ ___53-[NFConnectionHandoverReceiver _startWithAutoResume:]_block_invoke_2
+ ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.207
+ ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke_2.208
+ ___54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.408
+ ___54-[NFSecureElementReaderSession startVASPolling:error:]_block_invoke.32
+ ___55-[NFHCESession suspensionStateUpdate:triggeredByField:]_block_invoke
+ ___55-[NFSecureElementLoggingSession getLogs:forSEID:error:]_block_invoke.12
+ ___55-[NFSecureElementReaderSession performSelectVAS:error:]_block_invoke.37
+ ___56-[NFReaderSession checkNdefSupportsRead:andWrite:error:]_block_invoke.113
+ ___56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.89
+ ___57-[NFLPEMConfigSession configureHardwareForLPEMWithError:]_block_invoke.28
+ ___57-[NFNdefTagSession startEmulation:withMessageType:error:]_block_invoke.21
+ ___57-[NFPeerPaymentSession performPeerPayment:request:error:]_block_invoke.13
+ ___57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.269
+ ___57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.107
+ ___57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.99
+ ___58-[NFReaderSession _disconnectTagWithCardRemoval:outError:]_block_invoke.112
+ ___58-[NFSeshatSession deleteSlot:outWriteCount:trackingError:]_block_invoke.54
+ ___58-[NFTrustSession signWithKey:request:authorization:error:]_block_invoke.25
+ ___60-[NFReaderSession felicaRequestService:forSystemCode:error:]_block_invoke.132
+ ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.236
+ ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.239
+ ___62-[NFHCESession resumeSessionFromWaitingOnFieldWithCompletion:]_block_invoke
+ ___62-[NFHCESession resumeSessionFromWaitingOnFieldWithCompletion:]_block_invoke.19
+ ___63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.81
+ ___65-[NFConnectionHandoverReceiver forceResumeWithCompletionHandler:]_block_invoke
+ ___65-[NFConnectionHandoverReceiver forceResumeWithCompletionHandler:]_block_invoke_2
+ ___65-[NFConnectionHandoverReceiver startWithAutoResumeOnFieldDisable]_block_invoke
+ ___65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.239
+ ___65-[NFHardwareManager startReaderSessionWithAttributes:completion:]_block_invoke
+ ___65-[NFHardwareManager startReaderSessionWithAttributes:completion:]_block_invoke_2
+ ___67-[NFECommercePaymentSession performECommercePayment:request:error:]_block_invoke.23
+ ___68-[NFConnectionHandoverReceiver hceSession:triggeredByField:started:]_block_invoke
+ ___68-[NFSeshatSession upgradeKey:inputData:outWriteCount:trackingError:]_block_invoke.74
+ ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.197
+ ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.201
+ ___70-[NFSeshatSession resetCounter:userToken:outWriteCount:trackingError:]_block_invoke.41
+ ___71-[NFSeshatSession derive:userHash:outData:outWriteCount:trackingError:]_block_invoke.35
+ ___73-[NFReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke.12
+ ___73-[NFTrustSession signWithKey:request:paymentRequest:authorization:error:]_block_invoke.33
+ ___74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.87
+ ___75-[NFConnectionHandoverInitiator handleSessionSuspended:token:reason:field:]_block_invoke
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.415
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.418
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.420
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.421
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_3.422
+ ___78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.179
+ ___79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.247
+ ___79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke
+ ___79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke.442
+ ___79-[NFSeshatSession getData:updateKUD:outWriteLimit:outWriteCount:trackingError:]_block_invoke.60
+ ___83-[NFSeshatSession authorizeUpdate:slotIndex:userToken:outWriteCount:trackingError:]_block_invoke.48
+ ___84-[NFSecureElementReaderSession performGetVASDataWithRequestList:responseList:error:]_block_invoke.43
+ ___85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.194
+ ___Block_byref_object_copy_.403
+ ___Block_byref_object_dispose_.404
+ ___block_descriptor_48_8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_49_8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.229
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.298
+ ___block_literal_global.33
+ __unnamed_array_storage
+ __unnamed_array_storage.141
+ __unnamed_array_storage.143
+ __unnamed_array_storage.144
+ _objc_msgSend$NF_arrayForKey:
+ _objc_msgSend$_startWithAutoResume:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$appletsDeleted:
+ _objc_msgSend$controllerDidDetectPotentialInitiator:
+ _objc_msgSend$ecp
+ _objc_msgSend$fieldDetect
+ _objc_msgSend$handleSessionSuspended:token:reason:field:
+ _objc_msgSend$hceSession:triggeredByField:started:
+ _objc_msgSend$isBackgroundTagReadingAvailable
+ _objc_msgSend$lpcd
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$pollConfigWithTechnology:
+ _objc_msgSend$pollDuration
+ _objc_msgSend$restartDiscovery
+ _objc_msgSend$resumeSessionFromWaitingOnFieldWithCompletion:
+ _objc_msgSend$setEcp:
+ _objc_msgSend$setPollDuration:
+ _objc_msgSend$setSessionDelegate:
+ _objc_msgSend$setSkipMifareClassify:
+ _objc_msgSend$setTechnology:
+ _objc_msgSend$skipMifareClassify
+ _objc_msgSend$startPollingWithConfig:completion:
+ _objc_msgSend$startPollingWithConfig:error:
+ _objc_msgSend$startReaderSessionWithAttributes:completion:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_retain_x5
- -[NFConnectionHandoverController initWithType:callbackQueue:]
- -[NFConnectionHandoverInitiator connectedTag]
- -[NFConnectionHandoverInitiator delayRequestCompletion]
- -[NFConnectionHandoverInitiator delayRequestTimer]
- -[NFConnectionHandoverInitiator delayRequest]
- -[NFConnectionHandoverInitiator readerSession]
- -[NFConnectionHandoverInitiator setDelayRequestCompletion:]
- -[NFConnectionHandoverInitiator setDelayRequestTimer:]
- -[NFConnectionHandoverInitiator setTagConnectionTimer:]
- -[NFConnectionHandoverInitiator tagConnectionTimer]
- -[NFConnectionHandoverReceiver _processDisconnect]
- -[NFConnectionHandoverReceiver _start]
- -[NFConnectionHandoverReceiver delaySendSelectCompletion]
- -[NFConnectionHandoverReceiver didConnect]
- -[NFConnectionHandoverReceiver emuAssertTimer]
- -[NFConnectionHandoverReceiver hceAppSelected]
- -[NFConnectionHandoverReceiver hceSession]
- -[NFConnectionHandoverReceiver pendingCHSelect]
- -[NFConnectionHandoverReceiver setDelaySendSelectCompletion:]
- -[NFConnectionHandoverReceiver setDidConnect:]
- -[NFConnectionHandoverReceiver setHceAppSelected:]
- -[NFHardwareManager _startReaderSessionWithUI:callback:]
- _OBJC_IVAR_$_NFConnectionHandoverReceiver._didConnect
- _OBJC_IVAR_$_NFConnectionHandoverReceiver._hceAppSelected
- ___106-[NFSeshatSession allocateSlot:authorizingUser:authorizingUserToken:outToken:outWriteCount:trackingError:]_block_invoke.16
- ___112-[NFReaderSession felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:error:]_block_invoke.52
- ___27-[NFTrustSession listKeys:]_block_invoke.22
- ___29-[NFHardwareManager preWarm:]_block_invoke.169
- ___29-[NFSession _endProxySession]_block_invoke.15
- ___30-[NFSession prioritizeSession]_block_invoke.19
- ___31-[NFSession activateWithToken:]_block_invoke.24
- ___33-[NFPeerPaymentSession deleteKey]_block_invoke.2
- ___33-[NFSession setSessionTimeLimit:]_block_invoke.5
- ___34-[NFHardwareManager setChipscope:]_block_invoke.224
- ___34-[NFTrustSession deleteKey:error:]_block_invoke.9
- ___35-[NFReaderSession ndefWrite:error:]_block_invoke.42
- ___36-[NFReaderSession connectTag:error:]_block_invoke.33
- ___36-[NFReaderSession performVAS:error:]_block_invoke.59
- ___36-[NFReaderSession transceive:error:]_block_invoke.46
- ___37-[NFNdefTagSession setTagData:error:]_block_invoke.13
- ___37-[NFReaderSession ndefReadWithError:]_block_invoke.43
- ___37-[NFSecureElementReaderSession stop:]_block_invoke.17
- ___38-[NFConnectionHandoverReceiver _start]_block_invoke
- ___38-[NFConnectionHandoverReceiver _start]_block_invoke_2
- ___38-[NFNdefTagSession enableWrite:error:]_block_invoke.16
- ___38-[NFSecureElementReaderSession start:]_block_invoke.16
- ___39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.225
- ___39-[NFReaderSession setECPPayload:error:]_block_invoke.25
- ___39-[NFSession createSessionHandoffToken:]_block_invoke.22
- ___40-[NFHardwareManager startSesHatSession:]_block_invoke.160
- ___40-[NFNdefTagSession getTagDataWithError:]_block_invoke.14
- ___40-[NFReaderSession felicaStateWithError:]_block_invoke.48
- ___40-[NFReaderSession stopPollingWithError:]_block_invoke.29
- ___40-[NFReaderSession updateUIAlertMessage:]_block_invoke.57
- ___40-[NFRemoteAdminManager registrationInfo]_block_invoke.80
- ___41-[NFReaderSession startPollingWithError:]_block_invoke.26
- ___41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.102
- ___41-[NFSeshatSession getHash:trackingError:]_block_invoke.55
- ___42-[NFReaderSession checkPresenceWithError:]_block_invoke.38
- ___42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.82
- ___42-[NFTrustSession createKey:request:error:]_block_invoke.7
- ___43-[NFNdefTagSession stopEmulationWithError:]_block_invoke.12
- ___43-[NFReaderSession formatNdefWithKey:error:]_block_invoke.40
- ___43-[NFReaderSession restartPollingWithError:]_block_invoke.30
- ___43-[NFReaderSession setPollingProfile:error:]_block_invoke.62
- ___43-[NFReaderSession skipMifareClassification]_block_invoke.58
- ___43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.101
- ___45-[NFECommercePaymentSession didStartSession:]_block_invoke.3
- ___45-[NFECommercePaymentSession didStartSession:]_block_invoke.8
- ___45-[NFReaderSession startLPCDPollingWithError:]_block_invoke.27
- ___45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.104
- ___45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.84
- ___45-[NFSecureElementLoggingSession storeACLogs:]_block_invoke.5
- ___46-[NFReaderSession felicaRequestService:error:]_block_invoke.53
- ___46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.86
- ___46-[NFSecureElementReaderSession disconnectTag:]_block_invoke.34
- ___47-[NFLPEMConfigSession enableLPEMFeature:error:]_block_invoke.26
- ___47-[NFSecureElementReaderSession stopVASPolling:]_block_invoke.21
- ___47-[NFSeshatSession obliterateWithTrackingError:]_block_invoke.68
- ___48-[NFLPEMConfigSession disableLPEMFeature:error:]_block_invoke.21
- ___48-[NFLPEMConfigSession getLPEMFeaturesWithError:]_block_invoke.32
- ___49-[NFSecureElementReaderSession connectTag:error:]_block_invoke.33
- ___49-[NFSecureElementReaderSession performVAS:error:]_block_invoke.22
- ___49-[NFSecureElementReaderSession transceive:error:]_block_invoke.18
- ___50-[NFConnectionHandoverReceiver _processDisconnect]_block_invoke
- ___50-[NFConnectionHandoverReceiver _processDisconnect]_block_invoke.442
- ___50-[NFSecureElementLoggingSession enableSMBLogging:]_block_invoke.8
- ___51-[NFReaderSession startPollingForTechnology:error:]_block_invoke.28
- ___51-[NFSecureElementLoggingSession clearLogs:forSEID:]_block_invoke.4
- ___52-[NFLPEMConfigSession getLPEMBluetoothLogWithError:]_block_invoke.38
- ___52-[NFSecureElementLoggingSession getSMBLogWithError:]_block_invoke.9
- ___52-[NFSecureElementReaderSession selectApplets:error:]_block_invoke.15
- ___53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.440
- ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.203
- ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke_2.206
- ___54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.409
- ___54-[NFSecureElementReaderSession startVASPolling:error:]_block_invoke.20
- ___55-[NFSecureElementLoggingSession getLogs:forSEID:error:]_block_invoke.2
- ___55-[NFSecureElementReaderSession performSelectVAS:error:]_block_invoke.25
- ___56-[NFHardwareManager _startReaderSessionWithUI:callback:]_block_invoke
- ___56-[NFHardwareManager _startReaderSessionWithUI:callback:]_block_invoke.144
- ___56-[NFReaderSession checkNdefSupportsRead:andWrite:error:]_block_invoke.36
- ___56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.87
- ___57-[NFLPEMConfigSession configureHardwareForLPEMWithError:]_block_invoke.16
- ___57-[NFNdefTagSession startEmulation:withMessageType:error:]_block_invoke.11
- ___57-[NFPeerPaymentSession performPeerPayment:request:error:]_block_invoke.3
- ___57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.192
- ___57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.105
- ___57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.97
- ___58-[NFReaderSession _disconnectTagWithCardRemoval:outError:]_block_invoke.35
- ___58-[NFSeshatSession deleteSlot:outWriteCount:trackingError:]_block_invoke.42
- ___58-[NFTrustSession signWithKey:request:authorization:error:]_block_invoke.13
- ___59-[NFConnectionHandoverReceiver hceSession:didReceiveField:]_block_invoke_2
- ___60-[NFReaderSession felicaRequestService:forSystemCode:error:]_block_invoke.55
- ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.228
- ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.231
- ___63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.79
- ___65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.222
- ___67-[NFECommercePaymentSession performECommercePayment:request:error:]_block_invoke.13
- ___68-[NFSeshatSession upgradeKey:inputData:outWriteCount:trackingError:]_block_invoke.62
- ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.195
- ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.199
- ___70-[NFSeshatSession resetCounter:userToken:outWriteCount:trackingError:]_block_invoke.29
- ___71-[NFSeshatSession derive:userHash:outData:outWriteCount:trackingError:]_block_invoke.23
- ___73-[NFReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke.2
- ___73-[NFTrustSession signWithKey:request:paymentRequest:authorization:error:]_block_invoke.21
- ___74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.85
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.416
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.419
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.421
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.422
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_3.423
- ___78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.177
- ___79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.239
- ___79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.241
- ___79-[NFSeshatSession getData:updateKUD:outWriteLimit:outWriteCount:trackingError:]_block_invoke.48
- ___83-[NFSeshatSession authorizeUpdate:slotIndex:userToken:outWriteCount:trackingError:]_block_invoke.36
- ___84-[NFSecureElementReaderSession performGetVASDataWithRequestList:responseList:error:]_block_invoke.31
- ___85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.192
- ___Block_byref_object_copy_.404
- ___Block_byref_object_dispose_.405
- ___block_literal_global.21
- ___block_literal_global.212
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.292
- __os_feature_enabled_impl
- _objc_msgSend$_processDisconnect
- _objc_msgSend$_startReaderSessionWithUI:callback:
- _objc_msgSend$connectedTag
- _objc_msgSend$controllerDidDetectUnsupportedInitiatorVersion:
- _objc_msgSend$delayRequest
- _objc_msgSend$delayRequestCompletion
- _objc_msgSend$delayRequestTimer
- _objc_msgSend$delaySendSelectCompletion
- _objc_msgSend$didConnect
- _objc_msgSend$emuAssertTimer
- _objc_msgSend$handleSessionSuspended:withToken:
- _objc_msgSend$hceAppSelected
- _objc_msgSend$hceSession
- _objc_msgSend$pendingCHSelect
- _objc_msgSend$readerSession
- _objc_msgSend$setConnectedTag:
- _objc_msgSend$setDelayRequest:
- _objc_msgSend$setDelayRequestCompletion:
- _objc_msgSend$setDelayRequestTimer:
- _objc_msgSend$setDelaySendSelectCompletion:
- _objc_msgSend$setDidConnect:
- _objc_msgSend$setECPPayload:error:
- _objc_msgSend$setEmuAssertTimer:
- _objc_msgSend$setHceAppSelected:
- _objc_msgSend$setHceSession:
- _objc_msgSend$setPendingCHSelect:
- _objc_msgSend$setReaderSession:
- _objc_msgSend$setTagConnectionTimer:
- _objc_msgSend$skipMifareClassification
- _objc_msgSend$startPollingForTechnology:completion:
- _objc_msgSend$startReaderSession:
- _objc_msgSend$tagConnectionTimer
CStrings:
+ "%c[%{public}s %{public}s]:%i Archive error=%{public}@"
+ "%c[%{public}s %{public}s]:%i Contains undefined RFU bits but existing feature definition matches"
+ "%c[%{public}s %{public}s]:%i Missing field"
+ "%c[%{public}s %{public}s]:%i Suspend on remote initiator field detected"
+ "%c[%{public}s %{public}s]:%i autoResume=%{public}d"
+ "%c[%{public}s %{public}s]:%i started=%d"
+ "@20@0:8I16"
+ "ECPBroadcast"
+ "ECPBroadcastFieldMatch"
+ "ECPBroadcastInterval"
+ "ECPBroadcastPollDuration"
+ "Field"
+ "Initiator detected"
+ "Initiator request detected"
+ "NFReaderSessionPollConfig"
+ "NF_arrayForKey:"
+ "ReasonCode"
+ "T@\"NSData\",&,N,V_ecp"
+ "T@?,C,N,V_didEndCallback"
+ "T@?,C,N,V_didStartCallback"
+ "TB,N,V_fieldDetect"
+ "TB,N,V_lpcd"
+ "TB,N,V_skipMifareClassify"
+ "TB,R,V_initiator"
+ "TI,N,V_pollDuration"
+ "TI,N,V_technology"
+ "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "_ecp"
+ "_fieldDetect"
+ "_initiator"
+ "_lpcd"
+ "_pollDuration"
+ "_processDisconnectWithPossibleDiscoveryRestart:"
+ "_skipMifareClassify"
+ "_startWithAutoResume:"
+ "addEntriesFromDictionary:"
+ "appletsDeleted:"
+ "controllerDidDetectPotentialInitiator:"
+ "didEndCallback"
+ "didStartCallback"
+ "disableAutostartOnField"
+ "ecp"
+ "fd"
+ "fieldDetect"
+ "forceResumeWithCompletionHandler:"
+ "handleSessionSuspended:token:reason:field:"
+ "hceSession:triggeredByField:started:"
+ "lpcd"
+ "mutableBytes"
+ "pollConfigWithTechnology:"
+ "pollDuration"
+ "restartDiscovery"
+ "resumeSessionFromWaitingOnFieldWithCompletion:"
+ "roleBroadcastInBackground"
+ "session.suspendOnECP"
+ "setEcp:"
+ "setFieldDetect:"
+ "setLpcd:"
+ "setPollDuration:"
+ "setSkipMifareClassify:"
+ "setTechnology:"
+ "skipMifareClassify"
+ "startPollingWithConfig:completion:"
+ "startPollingWithConfig:error:"
+ "startReaderSessionWithAttributes:completion:"
+ "startWithAutoResumeOnFieldDisable"
+ "suspensionStateUpdate:triggeredByField:"
+ "tech"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "v28@0:8B16@\"NFFieldNotification\"20"
+ "v28@0:8B16@20"
+ "v36@0:8@\"NFHCESession\"16@\"NFFieldNotification\"24B32"
+ "v48@0:8@\"NFSession\"16@\"NSData\"24q32@\"NFFieldNotification\"40"
+ "v48@0:8@16@24q32@40"
- "%c[%{public}s %{public}s]:%i Mismatch version detected"
- "@32@0:8q16@?24"
- "Sharing"
- "T@\"NFConnectionHandoverRequest\",&,N,V_delayRequest"
- "T@\"NFConnectionHandoverSelect\",&,N,V_pendingCHSelect"
- "T@\"NFHCESession\",&,N,V_hceSession"
- "T@\"NFReaderSession\",&,N,V_readerSession"
- "T@\"NFTag\",&,N,V_connectedTag"
- "T@\"NFTimer\",&,N,V_delayRequestTimer"
- "T@\"NFTimer\",&,N,V_emuAssertTimer"
- "T@\"NFTimer\",&,N,V_tagConnectionTimer"
- "T@?,C,N,V_delayRequestCompletion"
- "T@?,C,N,V_delaySendSelectCompletion"
- "TB,N,V_didConnect"
- "TB,N,V_hceAppSelected"
- "Vv28@0:8I16@?<v@?@\"NSError\">20"
- "_processDisconnect"
- "_startReaderSessionWithUI:callback:"
- "ch_v1"
- "connectedTag"
- "controllerDidDetectUnsupportedInitiatorVersion:"
- "delayRequest"
- "delayRequestCompletion"
- "delayRequestTimer"
- "delaySendSelectCompletion"
- "didConnect"
- "emuAssertTimer"
- "handleSessionSuspended:withToken:"
- "hceAppSelected"
- "hceSession"
- "pendingCHSelect"
- "readerSession"
- "setConnectedTag:"
- "setDelayRequest:"
- "setDelayRequestCompletion:"
- "setDelayRequestTimer:"
- "setDelaySendSelectCompletion:"
- "setDidConnect:"
- "setEmuAssertTimer:"
- "setHceAppSelected:"
- "setHceSession:"
- "setPendingCHSelect:"
- "setReaderSession:"
- "setTagConnectionTimer:"
- "startPollingForTechnology:completion:"
- "stopPollingForTechnology:error:"
- "tagConnectionTimer"
- "v32@0:8@\"NFSession\"16@\"NSData\"24"

```
