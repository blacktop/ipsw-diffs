## CoreNFC

> `/System/Library/Frameworks/CoreNFC.framework/CoreNFC`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x43a28
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x2024
-  __TEXT.__const: 0x14b0
-  __TEXT.__swift5_typeref: 0x6fc
-  __TEXT.__swift5_fieldmd: 0x6f4
-  __TEXT.__constg_swiftt: 0x81c
-  __TEXT.__cstring: 0x3373
-  __TEXT.__swift5_reflstr: 0x744
-  __TEXT.__swift5_builtin: 0x78
+364.20.0.0.0
+  __TEXT.__text: 0x41118
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x205c
+  __TEXT.__const: 0x1520
+  __TEXT.__swift5_typeref: 0x74a
+  __TEXT.__swift5_fieldmd: 0x738
+  __TEXT.__constg_swiftt: 0x868
+  __TEXT.__swift5_reflstr: 0x784
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__cstring: 0x2d8e
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift5_capture: 0x3a8
-  __TEXT.__oslogstring: 0x292d
-  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift5_capture: 0x388
+  __TEXT.__oslogstring: 0x24d4
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_proto: 0x54
-  __TEXT.__swift_as_entry: 0x78
-  __TEXT.__swift_as_ret: 0x80
-  __TEXT.__unwind_info: 0x1018
-  __TEXT.__eh_frame: 0xe00
-  __TEXT.__objc_classname: 0x430
-  __TEXT.__objc_methname: 0x3a0b
-  __TEXT.__objc_methtype: 0x1644
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0xae0
-  __DATA_CONST.__objc_classlist: 0x150
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__unwind_info: 0x1048
+  __TEXT.__eh_frame: 0x1018
+  __TEXT.__objc_classname: 0x6c9
+  __TEXT.__objc_methname: 0x3f58
+  __TEXT.__objc_methtype: 0x19dd
+  __TEXT.__objc_stubs: 0x2d00
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0xad8
+  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_selrefs: 0xf00
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x1a10
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x1b58
   __AUTH_CONST.__cfstring: 0xec0
-  __AUTH_CONST.__objc_const: 0x3a98
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xea8
-  __AUTH.__data: 0x7d0
-  __DATA.__objc_ivar: 0x144
-  __DATA.__data: 0xe88
+  __AUTH_CONST.__objc_const: 0x3bb8
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH.__objc_data: 0xef8
+  __AUTH.__data: 0x7e0
+  __DATA.__objc_ivar: 0x14c
+  __DATA.__data: 0xea0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x2dd
-  __DATA.__bss: 0xab0
+  __DATA.__bss: 0xbb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D3A56D5B-67D9-339B-9B1D-7C0888719A82
-  Functions: 1502
-  Symbols:   269
-  CStrings:  1515
+  UUID: 6ED73D03-3D24-3B7E-86E4-7E735F91B780
+  Functions: 1526
+  Symbols:   261
+  CStrings:  1528
 
Symbols:
+ _OBJC_CLASS_$_NFCTagReaderSessionConfiguration
+ _OBJC_CLASS_$_NFCoreNFCPollConfig
+ _OBJC_METACLASS_$_NFCTagReaderSessionConfiguration
+ ___error
+ _clock_gettime_nsec_np
+ _swift_allocBox
- _NFLogGetLogger
- _class_isMetaClass
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
- _object_getClass
- _object_getClassName
CStrings:
+ "%{public}s:%i "
+ "%{public}s:%i %@"
+ "%{public}s:%i %@ in commandConfiguration asNSDataWithError"
+ "%{public}s:%i %@ in readConfiguration asNSDataArrayWithUID"
+ "%{public}s:%i %@ with response length = %lu"
+ "%{public}s:%i Archive error: %@"
+ "%{public}s:%i Block data length must be 16 bytes long"
+ "%{public}s:%i Block list element must be 2 or 3 bytes long"
+ "%{public}s:%i Block list size exceeds the maximum limit"
+ "%{public}s:%i Block range must be between 0 to 255 inclusively"
+ "%{public}s:%i Command packet length must be between 1 to 254 inclusively"
+ "%{public}s:%i ConnectedTag[%ld]: %@"
+ "%{public}s:%i Connection ID has been updated; skip cleanup"
+ "%{public}s:%i Current connectedTag: %@"
+ "%{public}s:%i Custom command code must be between 0xA0 to 0xDF inclusively"
+ "%{public}s:%i Data block length must be greater than 0"
+ "%{public}s:%i Defaulting to CoreNFCSessionTypeUnknown"
+ "%{public}s:%i Delegate conforms to [NFCNDEFReaderSessionDelegate readerSession:didDetectTags]; polling is auto restarted."
+ "%{public}s:%i Delegate does not implement -readerSession:didDetectTags: method"
+ "%{public}s:%i Delegate does not implement -readerSessionDidBecomeActive: method"
+ "%{public}s:%i Delegate does not implement -tagReaderSession:didDetectTags: method"
+ "%{public}s:%i Delegate does not implement -tagReaderSessionDidBecomeActive: method"
+ "%{public}s:%i Delegate object does not conform to %@ protocol"
+ "%{public}s:%i Disconnecting previous tag"
+ "%{public}s:%i Dispatch resource init failed"
+ "%{public}s:%i Drop XPC interrupt callback"
+ "%{public}s:%i Elements in the data block list are inconsistent in size"
+ "%{public}s:%i Empty string"
+ "%{public}s:%i Error=%@"
+ "%{public}s:%i External reader detected"
+ "%{public}s:%i Failed to connect to NFCD"
+ "%{public}s:%i Forcing minimum 20ms delay"
+ "%{public}s:%i Get time error: %d"
+ "%{public}s:%i HW state query timeout"
+ "%{public}s:%i HW support state update: %lu"
+ "%{public}s:%i Invalid APDU format"
+ "%{public}s:%i Invalid NFCPollingOption parameter: 0x%lx"
+ "%{public}s:%i Invalid UTF8 URI string"
+ "%{public}s:%i Invalid expectedResponseLength value; should be from 1 to 65536 or -1"
+ "%{public}s:%i Invalid handle"
+ "%{public}s:%i Invalid payload length"
+ "%{public}s:%i Invalid state, %ld"
+ "%{public}s:%i Invalid tag index: %ld"
+ "%{public}s:%i Invalid tag object"
+ "%{public}s:%i Missing URI field"
+ "%{public}s:%i Missing data specified by Lc"
+ "%{public}s:%i Missing data when Lc is > 0"
+ "%{public}s:%i NDEF payload exceeds the size limit"
+ "%{public}s:%i No suitable NDEF tag found"
+ "%{public}s:%i No suitable tag found"
+ "%{public}s:%i Node size must be 2 bytes long"
+ "%{public}s:%i Not implemented"
+ "%{public}s:%i Number of elements in the block list and the block data list does not match"
+ "%{public}s:%i Number of nodes must be between 1 to 32 inclusively"
+ "%{public}s:%i Number of service codes must be between 1 to 16 inclusively"
+ "%{public}s:%i Only tag from the current session is allowed"
+ "%{public}s:%i PACE-polling enabled"
+ "%{public}s:%i Previous operation in progress"
+ "%{public}s:%i Record serialization error"
+ "%{public}s:%i Resource unavailable; assertion is currently in placed."
+ "%{public}s:%i Resource unavailable; system in cool-down period"
+ "%{public}s:%i Restart polling"
+ "%{public}s:%i Session does not support invalidation with error"
+ "%{public}s:%i Session has been invalidated"
+ "%{public}s:%i Session has not begun"
+ "%{public}s:%i Session queue is nil"
+ "%{public}s:%i Session queue is not available; dispatching on main queue"
+ "%{public}s:%i Specified range length does not match the number of elements in the data block list"
+ "%{public}s:%i Stack error: %@"
+ "%{public}s:%i System code must not contain the 0xFF wildcard value"
+ "%{public}s:%i Tag is not connected"
+ "%{public}s:%i Total size of all NDEF records exceeds the size limit"
+ "%{public}s:%i Unarchive error: %@"
+ "%{public}s:%i Unexpected Lc & Le field combination"
+ "%{public}s:%i Unexpected block size of 0"
+ "%{public}s:%i Unexpected class type for the message"
+ "%{public}s:%i Unexpected error type"
+ "%{public}s:%i Unexpected extended Lc & short Le combination"
+ "%{public}s:%i Unexpected lc & le field combination"
+ "%{public}s:%i Unexpected short Lc & extended Le combination"
+ "%{public}s:%i Unknown delegate type: %ld"
+ "%{public}s:%i XPC Error: %@"
+ "%{public}s:%i XPC error: %@"
+ "%{public}s:%i assertion=%lu"
+ "%{public}s:%i code=%ld, finalUIState=%ld, activateCallback=%ld"
+ "%{public}s:%i error:%@, errorCode: 0x%lx"
+ "%{public}s:%i error=%{public}@"
+ "%{public}s:%i expired"
+ "%{public}s:%i handle=%lu"
+ "%{public}s:%i sessionState=%ld, proxy=%@"
+ "%{public}s:%i sessionState=%ld, proxy=%@, error=%@"
+ "+[NFCNDEFPayload(ConvenienceHelpers) wellKnownTypeURIPayloadWithString:]"
+ "+[NFCoreNFCPollConfig(NFCTagReaderSessionHelper) configWithNFCPollingOption:sessionType:]"
+ "-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:]_block_invoke"
+ "-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:]_block_invoke"
+ "-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:]_block_invoke"
+ "-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:]_block_invoke"
+ "-[NFCFeliCaTag sendFeliCaCommandPacket:completionHandler:]_block_invoke"
+ "-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:]_block_invoke"
+ "-[NFCHardwareManager _releasePresentmentSuppressionAssertion:completion:]"
+ "-[NFCHardwareManager _releasePresentmentSuppressionAssertion:completion:]_block_invoke"
+ "-[NFCHardwareManager areFeaturesSupported:expiry:completion:]"
+ "-[NFCHardwareManager areFeaturesSupported:outError:]"
+ "-[NFCHardwareManager didExpire]"
+ "-[NFCHardwareManager hwStateDidChange:]"
+ "-[NFCHardwareManager queueCardFieldDetectSession:completionHandler:]_block_invoke_2"
+ "-[NFCHardwareManager queueCardSession:sessionConfig:completionHandler:]_block_invoke_2"
+ "-[NFCHardwareManager queueReaderSession:sessionConfig:completionHandler:]_block_invoke_2"
+ "-[NFCHardwareManager releasePresentmentSuppression:completion:]"
+ "-[NFCHardwareManager releasePresentmentSuppression:completion:]_block_invoke"
+ "-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]"
+ "-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]_block_invoke_2"
+ "-[NFCISO15693ReaderSession didDetectTags:connectedTagIndex:]"
+ "-[NFCISO15693ReaderSessionTag readMultipleBlocksWithConfiguration:completionHandler:]"
+ "-[NFCISO15693ReaderSessionTag sendCustomCommandWithConfiguration:completionHandler:]"
+ "-[NFCISO15693Tag _wtxRetryWithCommnand:maxRetry:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag customCommandWithRequestFlag:customCommandCode:customRequestParameters:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke_2"
+ "-[NFCISO15693Tag extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedLockBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedReadMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedReadSingleBlockWithRequestFlags:blockNumber:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag getMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag readMultipleBlocksWithRequestFlags:blockRange:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:]_block_invoke"
+ "-[NFCISO15693Tag writeSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:]_block_invoke"
+ "-[NFCISO7816APDU initWithData:]"
+ "-[NFCISO7816APDU initWithInstructionClass:instructionCode:p1Parameter:p2Parameter:data:expectedResponseLength:]"
+ "-[NFCNDEFMessage initWithNDEFRecords:]"
+ "-[NFCNDEFPayload asData]"
+ "-[NFCNDEFPayload initWithFormatType:type:identifier:payload:chunkSize:]"
+ "-[NFCNDEFPayload(ConvenienceHelpers) wellKnownTypeTextPayloadWithLocale:]"
+ "-[NFCNDEFReaderSession _callbackDidBecomeActive]"
+ "-[NFCNDEFReaderSession connectToTag:completionHandler:]"
+ "-[NFCNDEFReaderSession didDetectNDEFMessages:fromTags:connectedTagIndex:updateUICallback:]"
+ "-[NFCNDEFReaderSession restartPolling]"
+ "-[NFCNDEFTag dispatchBlockOnDelegateQueueAsync:]"
+ "-[NFCNDEFTag initWithCoder:]"
+ "-[NFCPresentmentSuppression startAssertionTimer:]_block_invoke"
+ "-[NFCReaderSession _callbackDidBecomeActive]"
+ "-[NFCReaderSession _callbackDidInvalidateWithError:]"
+ "-[NFCReaderSession _connectTag:error:]"
+ "-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]"
+ "-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke"
+ "-[NFCReaderSession beginSessionWithConfig:]_block_invoke"
+ "-[NFCReaderSession beginSessionWithConfig:]_block_invoke_2"
+ "-[NFCReaderSession checkPresenceWithError:]"
+ "-[NFCReaderSession connectTag:error:]"
+ "-[NFCReaderSession didDetectExternalReader]"
+ "-[NFCReaderSession didDetectTags:connectedTagIndex:]"
+ "-[NFCReaderSession didInvalidate]"
+ "-[NFCReaderSession didTerminate:]"
+ "-[NFCReaderSession didUIControllerInvalidate:]"
+ "-[NFCReaderSession disconnectTagWithError:]"
+ "-[NFCReaderSession handleSessionResumed]"
+ "-[NFCReaderSession handleSessionSuspended:]"
+ "-[NFCReaderSession initWithDelegate:sessionDelegateType:sessionType:pollConfig:queue:]"
+ "-[NFCReaderSession setAlertMessage:]_block_invoke"
+ "-[NFCReaderSession submitBlockOnDelegateQueue:]"
+ "-[NFCReaderSession submitBlockOnSessionQueue:]"
+ "-[NFCReaderSession submitBlockOnSessionQueueWithDelay:block:]"
+ "-[NFCReaderSession transceive:tagUpdate:error:]"
+ "-[NFCReaderSession validateDelegate:expectedType:]"
+ "-[NFCSession _connectIfNeeded]"
+ "-[NFCTag capacity]"
+ "-[NFCTag dispatchOnDelegateQueueAsync:]"
+ "-[NFCTag initWithCoder:]"
+ "-[NFCTag isNDEFFormatted]"
+ "-[NFCTag isReadOnly]"
+ "-[NFCTag queryNDEFStatusWithCompletionHandler:]_block_invoke_2"
+ "-[NFCTagReaderSession _callbackDidBecomeActive]"
+ "-[NFCTagReaderSession connectToTag:completionHandler:]"
+ "-[NFCTagReaderSession didDetectTags:connectedTagIndex:]"
+ "-[NFCVASReaderSession _callbackDidBecomeActive]"
+ "-[NFCVASReaderSession didDetectTags:connectedTagIndex:]"
+ "-[NFCVASReaderSession didDetectTags:connectedTagIndex:]_block_invoke"
+ "-[NSUserActivity(CoreNFC) ndefMessagePayload]"
+ "-[NSUserActivity(CoreNFCPrivate) setNdefMessagePayload:]"
+ "@\"NFCoreNFCPollConfig\""
+ "@32@0:8q16Q24"
+ "@48@0:8@16@24Q32@40"
+ "@56@0:8@16q24Q32@40@48"
+ "CoreNFC/NFCTagReaderSession.swift"
+ "Invalid AID entry: "
+ "Invalid ISO7816 select identifier entry: "
+ "Invalid system code entry: "
+ "Invalid system codes entry: "
+ "NFCPaymentTagReadeSession only supports NFCPollingISO14443."
+ "NFCTagReaderSession restartPollingWithConfiguration:"
+ "NFCTagReaderSessionConfiguration"
+ "NFCTagReaderSessionHelper"
+ "NF_dataWithHexString:"
+ "T@\"NFCoreNFCPollConfig\",&,N,V_pollConfig"
+ "T@\"NSArray\",&,N,V_felicaSystemCodes"
+ "T@\"NSArray\",&,N,V_iso7816SelectIdentifiers"
+ "Tq,N,V_polling"
+ "Vv32@0:8@\"NFReaderSessionPollConfig\"16@?<v@?@\"NSError\">24"
+ "[NFCPresentmentIntentAssertion] acquire"
+ "[NFCPresentmentIntentAssertion] deinit"
+ "[NFCPresentmentIntentAssertion] event monitor stopped"
+ "_createCheckedThrowingContinuation(_:)"
+ "_felicaSystemCodes"
+ "_iso7816SelectIdentifiers"
+ "_lastPresentmentSuppressionReleaseTime"
+ "_pollConfig"
+ "_polling"
+ "_releasePresentmentSuppressionAssertion:completion:"
+ "_restartPollingWithConfig:"
+ "_restartPollingWithConfig:completionHandler:"
+ "_startPollingWithConfig:completionHandler:"
+ "_supportsPACE"
+ "configWithNFCPollingOption:sessionType:"
+ "encodeToPollConfig"
+ "felicaSystemCodes"
+ "init(configuration:delegate:queue:)"
+ "init(delegate:sessionDelegateType:sessionType:pollConfig:queue:)"
+ "initWithConfiguration:delegate:queue:"
+ "initWithDelegate:sessionDelegateType:sessionType:pollConfig:queue:"
+ "initWithPollConfig:swiftDelegate:sessionType:queue:"
+ "initWithPollingOption:iso7816SelectIdentifiers:felicaSystemCodes:"
+ "iso7816SelectIdentifiers"
+ "pollConfig"
+ "pollConfigWithOption:sessionConfig:"
+ "polling"
+ "pollingOption"
+ "proxyExecute(_:)"
+ "removeNFCHardwareManagerCallbacksListener:"
+ "removeObject:"
+ "restartPollingWithConfig:"
+ "restartPollingWithConfiguration:"
+ "restartPollingWithConfiguration:completion:"
+ "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:"
+ "setFelicaSystemCodes:"
+ "setIso7816SelectIdentifiers:"
+ "setPollConfig:"
+ "setPolling:"
+ "setPollingOption:"
+ "startPollingWithConfig:completion:"
+ "supportsPACE"
- "%c[%{public}s %{public}s]:%i "
- "%c[%{public}s %{public}s]:%i %@"
- "%c[%{public}s %{public}s]:%i %@ in commandConfiguration asNSDataWithError"
- "%c[%{public}s %{public}s]:%i %@ in readConfiguration asNSDataArrayWithUID"
- "%c[%{public}s %{public}s]:%i %@ with response length = %lu"
- "%c[%{public}s %{public}s]:%i Archive error: %@"
- "%c[%{public}s %{public}s]:%i Block data length must be 16 bytes long"
- "%c[%{public}s %{public}s]:%i Block list element must be 2 or 3 bytes long"
- "%c[%{public}s %{public}s]:%i Block list size exceeds the maximum limit"
- "%c[%{public}s %{public}s]:%i Block range must be between 0 to 255 inclusively"
- "%c[%{public}s %{public}s]:%i Command packet length must be between 1 to 254 inclusively"
- "%c[%{public}s %{public}s]:%i ConnectedTag[%ld]: %@"
- "%c[%{public}s %{public}s]:%i Connection ID has been updated; skip cleanup"
- "%c[%{public}s %{public}s]:%i Current connectedTag: %@"
- "%c[%{public}s %{public}s]:%i Custom command code must be between 0xA0 to 0xDF inclusively"
- "%c[%{public}s %{public}s]:%i Data block length must be greater than 0"
- "%c[%{public}s %{public}s]:%i De-assert error=%@"
- "%c[%{public}s %{public}s]:%i Defaulting to CoreNFCSessionTypeUnknown"
- "%c[%{public}s %{public}s]:%i Delegate conforms to [NFCNDEFReaderSessionDelegate readerSession:didDetectTags]; polling is auto restarted."
- "%c[%{public}s %{public}s]:%i Delegate does not implement -readerSession:didDetectTags: method"
- "%c[%{public}s %{public}s]:%i Delegate does not implement -readerSessionDidBecomeActive: method"
- "%c[%{public}s %{public}s]:%i Delegate does not implement -tagReaderSession:didDetectTags: method"
- "%c[%{public}s %{public}s]:%i Delegate does not implement -tagReaderSessionDidBecomeActive: method"
- "%c[%{public}s %{public}s]:%i Delegate object does not conform to %@ protocol"
- "%c[%{public}s %{public}s]:%i Disconnecting previous tag"
- "%c[%{public}s %{public}s]:%i Dispatch resource init failed"
- "%c[%{public}s %{public}s]:%i Drop XPC interrupt callback"
- "%c[%{public}s %{public}s]:%i Elements in the data block list are inconsistent in size"
- "%c[%{public}s %{public}s]:%i Empty string"
- "%c[%{public}s %{public}s]:%i Error=%@"
- "%c[%{public}s %{public}s]:%i External reader detected"
- "%c[%{public}s %{public}s]:%i Failed to connect to NFCD"
- "%c[%{public}s %{public}s]:%i Forcing minimum 20ms delay"
- "%c[%{public}s %{public}s]:%i HW state query timeout"
- "%c[%{public}s %{public}s]:%i HW support state update: %lu"
- "%c[%{public}s %{public}s]:%i Invalid APDU format"
- "%c[%{public}s %{public}s]:%i Invalid NFCPollingOption parameter: 0x%lx"
- "%c[%{public}s %{public}s]:%i Invalid UTF8 URI string"
- "%c[%{public}s %{public}s]:%i Invalid expectedResponseLength value; should be from 1 to 65536 or -1"
- "%c[%{public}s %{public}s]:%i Invalid handle"
- "%c[%{public}s %{public}s]:%i Invalid payload length"
- "%c[%{public}s %{public}s]:%i Invalid state, %ld"
- "%c[%{public}s %{public}s]:%i Invalid tag index: %ld"
- "%c[%{public}s %{public}s]:%i Invalid tag object"
- "%c[%{public}s %{public}s]:%i Missing URI field"
- "%c[%{public}s %{public}s]:%i Missing data specified by Lc"
- "%c[%{public}s %{public}s]:%i Missing data when Lc is > 0"
- "%c[%{public}s %{public}s]:%i NDEF payload exceeds the size limit"
- "%c[%{public}s %{public}s]:%i No suitable NDEF tag found"
- "%c[%{public}s %{public}s]:%i No suitable tag found"
- "%c[%{public}s %{public}s]:%i Node size must be 2 bytes long"
- "%c[%{public}s %{public}s]:%i Not implemented"
- "%c[%{public}s %{public}s]:%i Number of elements in the block list and the block data list does not match"
- "%c[%{public}s %{public}s]:%i Number of nodes must be between 1 to 32 inclusively"
- "%c[%{public}s %{public}s]:%i Number of service codes must be between 1 to 16 inclusively"
- "%c[%{public}s %{public}s]:%i Only tag from the current session is allowed"
- "%c[%{public}s %{public}s]:%i PACE-polling enabled"
- "%c[%{public}s %{public}s]:%i Previous operation in progress"
- "%c[%{public}s %{public}s]:%i Record serialization error"
- "%c[%{public}s %{public}s]:%i Resource unavailable"
- "%c[%{public}s %{public}s]:%i Restart polling"
- "%c[%{public}s %{public}s]:%i Session does not support invalidation with error"
- "%c[%{public}s %{public}s]:%i Session has been invalidated"
- "%c[%{public}s %{public}s]:%i Session has not begun"
- "%c[%{public}s %{public}s]:%i Session queue is nil"
- "%c[%{public}s %{public}s]:%i Session queue is not available; dispatching on main queue"
- "%c[%{public}s %{public}s]:%i Specified range length does not match the number of elements in the data block list"
- "%c[%{public}s %{public}s]:%i Stack error: %@"
- "%c[%{public}s %{public}s]:%i System code must not contain the 0xFF wildcard value"
- "%c[%{public}s %{public}s]:%i Tag is not connected"
- "%c[%{public}s %{public}s]:%i Total size of all NDEF records exceeds the size limit"
- "%c[%{public}s %{public}s]:%i Unarchive error: %@"
- "%c[%{public}s %{public}s]:%i Unexpected Lc & Le field combination"
- "%c[%{public}s %{public}s]:%i Unexpected block size of 0"
- "%c[%{public}s %{public}s]:%i Unexpected class type for the message"
- "%c[%{public}s %{public}s]:%i Unexpected error type"
- "%c[%{public}s %{public}s]:%i Unexpected extended Lc & short Le combination"
- "%c[%{public}s %{public}s]:%i Unexpected lc & le field combination"
- "%c[%{public}s %{public}s]:%i Unexpected short Lc & extended Le combination"
- "%c[%{public}s %{public}s]:%i Unknown delegate type: %ld"
- "%c[%{public}s %{public}s]:%i XPC Error: %@"
- "%c[%{public}s %{public}s]:%i XPC error: %@"
- "%c[%{public}s %{public}s]:%i XPC error=%@"
- "%c[%{public}s %{public}s]:%i code=%ld, finalUIState=%ld, activateCallback=%ld"
- "%c[%{public}s %{public}s]:%i error:%@, errorCode: 0x%lx"
- "%c[%{public}s %{public}s]:%i error=%{public}@"
- "%c[%{public}s %{public}s]:%i expired"
- "%c[%{public}s %{public}s]:%i handle=%lu"
- "%c[%{public}s %{public}s]:%i sessionState=%ld, proxy=%@"
- "%c[%{public}s %{public}s]:%i sessionState=%ld, proxy=%@, error=%@"
- "%s: %ld: cooldown completed"
- "%s:%i NFCSession: Connection (ID=%ld) interrupted"
- "%s:%i NFCSession: Connection (ID=%ld) invalidated"
- "@48@0:8q16@24Q32@40"
- "@56@0:8q16@24q32Q40@48"
- "@64@0:8@16q24@32Q40Q48Q56"
- "NFCPresentmentIntentAssertion.deinit"
- "T@\"NFAssertionInternal\",R,N,V_assertion"
- "T@\"NSNumber\",R,N,V_externalHandle"
- "T@\"NSObject<NFCPresentmentSuppressionDelegate>\",N,V_delegate"
- "TQ,N,V_pollOption"
- "TQ,N,V_sessionConfig"
- "Vv32@0:8Q16@?<v@?@\"NSError\">24"
- "Vv40@0:8Q16Q24@?32"
- "Vv40@0:8Q16Q24@?<v@?@\"NSError\">32"
- "[NFCPresentmentIntentAssertion] Cooldown completed"
- "[NFCPresentmentIntentAssertion] acquire()"
- "_cooldownTimer"
- "_pollOption"
- "_restartPollingWithCompletionHandler:"
- "_sessionConfig"
- "_startPollingWithMethod:sessionConfig:completionHandler:"
- "assertion"
- "assertionWithAssertion:delegate:"
- "asyncProxyExecute(isolation:_:)"
- "didFinishCooldown"
- "externalHandle"
- "init(delegate:sessionDelegateType:queue:pollMethod:sessionType:sessionConfig:)"
- "initWithAssertion:delegate:"
- "initWithDelegate:sessionDelegateType:queue:pollMethod:sessionType:sessionConfig:"
- "initWithPollingOption:delegate:delegateType:sessionType:queue:"
- "initWithPollingOption:swiftDelegate:sessionType:queue:"
- "pollOption"
- "restartPollingWithCompletion:"
- "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:"
- "setDelegate:"
- "setPollOption:"
- "startAssertion:"
- "startCooldown:"
- "startPollingForNDEFMessagesWithSessionConfig:completion:"
- "startPollingForTags:sessionConfig:completion:"
- "v40@0:8Q16Q24@?32"

```
