## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2175.12.1.0.0
-  __TEXT.__text: 0x797700
+2175.13.1.0.0
+  __TEXT.__text: 0x798dd0
   __TEXT.__auth_stubs: 0x5630
-  __TEXT.__objc_methlist: 0x35c28
+  __TEXT.__objc_methlist: 0x35c60
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8f85a
-  __TEXT.__oslogstring: 0x10f5e1
-  __TEXT.__gcc_except_tab: 0x2aac
+  __TEXT.__cstring: 0x8f835
+  __TEXT.__oslogstring: 0x10f908
+  __TEXT.__gcc_except_tab: 0x2abc
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x108c0
+  __TEXT.__unwind_info: 0x108f0
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7df42
-  __TEXT.__objc_methtype: 0x282e0
-  __TEXT.__objc_stubs: 0x4ef20
+  __TEXT.__objc_methname: 0x7e027
+  __TEXT.__objc_methtype: 0x2831e
+  __TEXT.__objc_stubs: 0x4efc0
   __DATA_CONST.__got: 0x1a60
-  __DATA_CONST.__const: 0x6b38
+  __DATA_CONST.__const: 0x6b10
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16a10
+  __DATA_CONST.__objc_selrefs: 0x16a40
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b30
-  __AUTH_CONST.__const: 0x3c88
-  __AUTH_CONST.__cfstring: 0x26480
-  __AUTH_CONST.__objc_const: 0x63870
+  __AUTH_CONST.__const: 0x3ca8
+  __AUTH_CONST.__cfstring: 0x264e0
+  __AUTH_CONST.__objc_const: 0x638d0
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6cb0
+  __DATA.__objc_ivar: 0x6cbc
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3DFD4134-1C4B-3EEA-9E63-27BE92A89B00
-  Functions: 31615
-  Symbols:   97499
-  CStrings:  57300
+  UUID: 26C7289A-3D07-37F4-B0EC-FC93011AAE6B
+  Functions: 31633
+  Symbols:   97544
+  CStrings:  57328
 
Symbols:
+ -[AVCSessionParticipant initWithParticipantID:data:delegate:queue:].cold.7
+ -[VCAnsweringMachine destroyEventQueue]
+ -[VCAnsweringMachine enqueueInjectorAsset:blocksToDelay:]
+ -[VCAnsweringMachine enqueueInjectorAsset:blocksToDelay:].cold.1
+ -[VCAnsweringMachine flushEventQueue]
+ -[VCAnsweringMachine initWithConfiguration:delegate:delegateQueue:].cold.6
+ -[VCAnsweringMachine setUpAnnouncementAsset:isInitialAsset:]
+ -[VCAnsweringMachine setUpEventQueue]
+ -[VCAnsweringMachine setUpEventQueue].cold.1
+ -[VCAnsweringMachine setUpRealtimeContextWithToken:]
+ -[VCAnsweringMachine setUpRealtimeContextWithToken:].cold.1
+ -[VCAnsweringMachine setUpRealtimeContextWithToken:].cold.2
+ -[VCAnsweringMachine setUpRealtimeContextWithToken:].cold.3
+ -[VCMediaStream configureDefaultMediaKeyIndexForStreamConfig:]
+ -[VCMediaStream isRCCMCipherSuiteWithStreamConfig:]
+ -[VCRateControlMLEnrollment setPFLPath].cold.1
+ -[VCRateControlMLEnrollment setPFLPath].cold.2
+ -[VCRateControlMLEnrollment setPFLPath].cold.3
+ GCC_except_table110
+ GCC_except_table115
+ _OBJC_IVAR_$_AVCSessionParticipant._localStateQueue
+ _OBJC_IVAR_$_AVCSessionParticipant._stateQueueLock
+ _OBJC_IVAR_$_VCMediaStreamTransport._defaultMediaKeyIndex
+ _VCMediaKeyIndex_CreateMediaKeyIndexWithUUIDString
+ __VTP_DoubleReleaseDetection
+ __VTP_ReleaseVPKTPacket
+ ___21-[AVCSession dealloc]_block_invoke
+ ___39-[AVCSessionParticipant setStateQueue:]_block_invoke
+ ___48-[AVCSessionParticipant setSharedXPCConnection:]_block_invoke
+ ___48-[AVCSessionParticipant setSharedXPCConnection:]_block_invoke_2
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.206
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.207
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.207.cold.1
+ ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.240
+ ____AVCSessionParticipant_DispatchSyncToStateQueue_block_invoke
+ ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.246
+ ____VTP_HandleReceiveForNWConnection_block_invoke.74
+ _objc_msgSend$configureDefaultMediaKeyIndexForStreamConfig:
+ _objc_msgSend$destroyEventQueue
+ _objc_msgSend$enqueueInjectorAsset:blocksToDelay:
+ _objc_msgSend$flushEventQueue
+ _objc_msgSend$isRCCMCipherSuiteWithStreamConfig:
+ _objc_msgSend$setUpAnnouncementAsset:isInitialAsset:
+ _objc_msgSend$setUpEventQueue
+ _objc_msgSend$setUpRealtimeContextWithToken:
- -[AVCSessionParticipant stateQueue]
- -[VCAnsweringMachine setUpAnnouncementAssetInjection]
- -[VCAnsweringMachine setUpAnnouncementAssetInjection].cold.1
- -[VCAnsweringMachine setupRealtimeContextWithToken:]
- -[VCAnsweringMachine setupRealtimeContextWithToken:].cold.1
- -[VCAnsweringMachine setupRealtimeContextWithToken:].cold.2
- -[VCAnsweringMachine setupRealtimeContextWithToken:].cold.3
- GCC_except_table108
- GCC_except_table113
- GCC_except_table117
- __VTP_ReleasePacket
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.203
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.204
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.204.cold.1
- ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.237
- ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.240
- ____VTP_HandleReceiveForNWConnection_block_invoke.65
- ___block_descriptor_81_e8_32o40o48b_e5_v8?0ls32l8s48l8s40l8
- ___block_literal_global.69
- _objc_msgSend$securityKeyMaterialWithStaticMediaKeyIndex
- _objc_msgSend$setUpAnnouncementAssetInjection
- _objc_msgSend$setupRealtimeContextWithToken:
CStrings:
+ " [%s] %s:%d %@(%p) Failed to allocate the event"
+ " [%s] %s:%d %@(%p) Failed to create the event queue"
+ " [%s] %s:%d %@(%p) Failed to create the event queue. error=%i"
+ " [%s] %s:%d %@(%p) Failed to enqueu the new audio injector"
+ " [%s] %s:%d %@(%p) Failed to enqueue injector asset=%p. error=%0x"
+ " [%s] %s:%d Alloc packet %p with tag=0x%X, pktAddress=0x%llX"
+ " [%s] %s:%d Create VTP memory pool for VPKTLIST with double release detection and size=%lu)"
+ " [%s] %s:%d Destroy VTP memory pool for VPKTLIST!"
+ " [%s] %s:%d Failed to allocate the event"
+ " [%s] %s:%d Failed to create the event queue"
+ " [%s] %s:%d Failed to create the event queue. error=%i"
+ " [%s] %s:%d Failed to enqueu the new audio injector"
+ " [%s] %s:%d Failed to enqueue injector asset=%p. error=%0x"
+ " [%s] %s:%d Releasing packet %p with tag=0x%X, pktAddress=0x%llX"
+ "-[VCAnsweringMachine enqueueInjectorAsset:blocksToDelay:]"
+ "-[VCAnsweringMachine setUpAnnouncementAsset:isInitialAsset:]"
+ "-[VCAnsweringMachine setUpEventQueue]"
+ "-[VCAnsweringMachine setUpRealtimeContextWithToken:]"
+ "2175.13.1"
+ "B32@0:8^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB^v}16^@24"
+ "B64@0:8@16^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB^v}24B32B36@40@48^@56"
+ "Packet %p already released. tag=0x%X, pktAddress=0x%llX, releasePathID=%u, vfd=%d"
+ "Packet %p got allocated again with tag=0x%X, pktAddress=0x%llX, releasePathID=%u, vfd=%d"
+ "_VTP_DoubleReleaseDetection"
+ "_VTP_ReleaseAllocators"
+ "_VTP_ReleaseVPKTPacket"
+ "_defaultMediaKeyIndex"
+ "_localStateQueue"
+ "_stateQueueLock"
+ "com.apple.AVConference.AVCSessionParticipant.stateQueue"
+ "configureDefaultMediaKeyIndexForStreamConfig:"
+ "destroyEventQueue"
+ "enqueueInjectorAsset:blocksToDelay:"
+ "flushEventQueue"
+ "isRCCMCipherSuiteWithStreamConfig:"
+ "setUpAnnouncementAsset:isInitialAsset:"
+ "setUpEventQueue"
+ "setUpRealtimeContextWithToken:"
+ "{_VCMediaStreamTransportSetupInfo=\"setupType\"C\"\"(?=\"socketInfo\"{?=\"rtpSocket\"i\"rtcpSocket\"i}\"ipInfo\"{?=\"srcIPPORT\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}\"srcRTPIPPort\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}}\"transportStreamInfo\"{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"isRTCPReceiveFromMultipleSSRCsEnabled\"B\"transportStreamIndex\"i}\"nwConnection\"@\"NSObject<OS_nw_connection>\")\"sourceRate\"I\"datagramChannelToken\"I\"isSessionIDValid\"B\"defaultMediaKeyIndex\"^v}"
+ "{tagVCAnsweringMachineRealtimeContext=\"eventQueue\"^{opaqueCMSimpleQueue}\"announcementAssetInjector\"@\"VCAudioInjector\"\"blockCounter\"I\"blocksToDelay\"I\"sourceCommonContext\"{tagVCAnsweringMachineCommonRealtimeContext=\"flags\"C\"latestTimestamp\"I\"averageAudioPower\"f}\"audioMachineLearningCoordinator\"@\"VCAudioMachineLearningCoordinator\"\"sinkCommonContext\"{tagVCAnsweringMachineCommonRealtimeContext=\"flags\"C\"latestTimestamp\"I\"averageAudioPower\"f}\"mediaRecorder\"@\"VCMediaRecorder\"\"mediaRecorderRequesterID\"@\"NSString\"\"mediaRecorderTransactionID\"@\"NSString\"\"audioToken\"q\"hasPendingAnnouncementAsset\"B}"
- "-[AVCSessionParticipant setMediaState:forMediaType:]"
- "-[AVCSessionParticipant setMediaType:enabled:mediaString:xpcMessageKey:xpcOperationKey:completionBlock:]"
- "-[AVCSessionParticipant setMediaType:paused:mediaString:xpcMessageKey:xpcOperationKey:completionBlock:]"
- "-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:]"
- "-[AVCSessionParticipant setVideoPositionalInfo:]_block_invoke_2"
- "-[VCAnsweringMachine setUpAnnouncementAssetInjection]"
- "-[VCAnsweringMachine setupRealtimeContextWithToken:]"
- "2175.12.1"
- "B32@0:8^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB}16^@24"
- "B64@0:8@16^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB}24B32B36@40@48^@56"
- "_VTP_ReleasePacket"
- "setUpAnnouncementAssetInjection"
- "setupRealtimeContextWithToken:"
- "{_VCMediaStreamTransportSetupInfo=\"setupType\"C\"\"(?=\"socketInfo\"{?=\"rtpSocket\"i\"rtcpSocket\"i}\"ipInfo\"{?=\"srcIPPORT\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}\"srcRTPIPPort\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}}\"transportStreamInfo\"{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"isRTCPReceiveFromMultipleSSRCsEnabled\"B\"transportStreamIndex\"i}\"nwConnection\"@\"NSObject<OS_nw_connection>\")\"sourceRate\"I\"datagramChannelToken\"I\"isSessionIDValid\"B}"
- "{tagVCAnsweringMachineRealtimeContext=\"announcementAssetInjector\"@\"VCAudioInjector\"\"blockCounter\"I\"blocksToDelay\"I\"sourceCommonContext\"{tagVCAnsweringMachineCommonRealtimeContext=\"flags\"C\"latestTimestamp\"I\"averageAudioPower\"f}\"audioMachineLearningCoordinator\"@\"VCAudioMachineLearningCoordinator\"\"sinkCommonContext\"{tagVCAnsweringMachineCommonRealtimeContext=\"flags\"C\"latestTimestamp\"I\"averageAudioPower\"f}\"mediaRecorder\"@\"VCMediaRecorder\"\"mediaRecorderRequesterID\"@\"NSString\"\"mediaRecorderTransactionID\"@\"NSString\"\"audioToken\"q\"hasPendingAnnouncementAsset\"B}"

```
