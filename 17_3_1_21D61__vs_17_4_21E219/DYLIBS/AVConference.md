## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2010.3.1.0.0
-  __TEXT.__text: 0x63aea4
+2015.3.1.0.0
+  __TEXT.__text: 0x63b6f8
   __TEXT.__auth_stubs: 0x4c30
-  __TEXT.__objc_methlist: 0x2ac1c
-  __TEXT.__const: 0x79b8
-  __TEXT.__cstring: 0x750c0
-  __TEXT.__oslogstring: 0xd9b0f
+  __TEXT.__objc_methlist: 0x2ac48
+  __TEXT.__const: 0x7a08
+  __TEXT.__cstring: 0x751a4
+  __TEXT.__oslogstring: 0xd9da9
   __TEXT.__gcc_except_tab: 0x1f84
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xc714
+  __TEXT.__unwind_info: 0xc728
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x42d9
-  __TEXT.__objc_methname: 0x6952c
-  __TEXT.__objc_methtype: 0x21112
-  __TEXT.__objc_stubs: 0x42b80
-  __DATA_CONST.__got: 0x1110
+  __TEXT.__objc_methname: 0x69646
+  __TEXT.__objc_methtype: 0x211b9
+  __TEXT.__objc_stubs: 0x42be0
+  __DATA_CONST.__got: 0x1118
   __DATA_CONST.__const: 0x5a18
   __DATA_CONST.__objc_classlist: 0x1088
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f120
-  __DATA_CONST.__objc_selrefs: 0x13238
-  __DATA_CONST.__objc_arraydata: 0x1e38
-  __AUTH_CONST.__cfstring: 0x1fda0
-  __AUTH_CONST.__objc_intobj: 0x3a20
-  __AUTH_CONST.__objc_arrayobj: 0x14e8
+  __DATA_CONST.__objc_const: 0x4f190
+  __DATA_CONST.__objc_selrefs: 0x13250
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x1200
+  __DATA_CONST.__objc_superrefs: 0xee8
+  __DATA_CONST.__objc_arraydata: 0x1eb8
+  __AUTH_CONST.__cfstring: 0x1fe20
+  __AUTH_CONST.__objc_intobj: 0x3a38
+  __AUTH_CONST.__objc_arrayobj: 0x1548
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__auth_ptr: 0xe0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x150
-  __AUTH_CONST.__const: 0x358
+  __AUTH_CONST.__const: 0x558
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__auth_got: 0x2630
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x1208
-  __DATA.__objc_superrefs: 0xee8
-  __DATA.__objc_ivar: 0x5d84
+  __DATA.__objc_ivar: 0x5d90
   __DATA.__data: 0x6f98
   __DATA.__bss: 0xa30
   __DATA.__common: 0x55
-  __DATA_DIRTY.__const: 0x2d18
+  __DATA_DIRTY.__const: 0x2b18
   __DATA_DIRTY.__objc_const: 0xc980
   __DATA_DIRTY.__objc_data: 0xa550
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x350
+  __DATA_DIRTY.__bss: 0x358
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 28107
-  Symbols:   78993
-  CStrings:  43936
+  Functions: 28122
+  Symbols:   79033
+  CStrings:  43964
 
Symbols:
+ -[AVAudioClient shouldSetUpXPCConnection]
+ -[VCAudioStreamSendGroup configureAudioStreams:deviceRole:operatingMode:].cold.4
+ -[VCAudioStreamSendGroup startCaptureIfNeeded:]
+ -[VCAudioStreamSendGroup startCaptureIfNeeded:].cold.1
+ -[VCAudioStreamSendGroup stopCaptureForEndToEndStreamIfNeeded]
+ -[VCRateControlMediaController disableBasebandFlush]
+ -[VCSession(OneToOne) revertMultiwayToOneToOneModeSwitchConfigure]
+ -[VCVideoStream remoteCameraReportingClientType]
+ -[VCVideoStream screenSharingReportingClientType]
+ GCC_except_table74
+ _OBJC_IVAR_$_VCAudioCaptions._previousConverterSamples
+ _OBJC_IVAR_$_VCMediaControlInfoFaceTimeAudio._controlInfoReceivedKBytes
+ _OBJC_IVAR_$_VCMediaControlInfoFaceTimeVideo._controlInfoReceivedKBytes
+ _OBJC_IVAR_$_VCRateControlMediaController._disableBasebandFlush
+ _OBJC_IVAR_$_VCSessionParticipant._mediaTypeMixingListLock
+ _VCConnection_GetDataMode
+ _VCConnection_GetDataMode.cold.1
+ __AVCRateController_ApplyServerBagBasebandConfig
+ __OBJC_$_PROP_LIST_VCVideoCaptureServer.698
+ __VCAudioCaptions_DestroyCopyBufferAllocator
+ ___135-[VideoConference(SessionDelegate) session:receivedRemoteFrame:atTime:withScreenAttributes:videoAttributes:isFirstFrame:isVideoPaused:]_block_invoke.632
+ ___40-[VCConnectionManagerIDS addConnection:]_block_invoke.43
+ ___47-[VCNetworkFeedbackController cleanupWRMClient]_block_invoke_2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.171
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.174
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.174.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.174.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.178
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.188
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.188.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.188.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.188.cold.3
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.188.cold.4
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.217
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.232
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.263
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.274
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.274.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.281
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.281.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.288
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.288.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.295
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.295.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.302
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.302.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.309
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.309.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.316
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.316.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.323
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.334
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.345
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.348
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.350
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.357
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.221
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.240
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.267
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.267.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.330
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.330.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.341
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.341.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.354
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.225
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.225.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.242
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.242.cold.1
+ ___50-[VCCallSession(PrivateMethods) updateDeviceRole:]_block_invoke.1458
+ ___50-[VCCallSession(PrivateMethods) updateDeviceRole:]_block_invoke.1465
+ ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke.109
+ ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.114
+ ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.114.cold.1
+ ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.114.cold.2
+ ___53-[VCCallSession(Messages) setupSymptomEnabledMessage]_block_invoke.1816
+ ___54-[VCAudioStreamSendGroup setDeviceRole:operatingMode:]_block_invoke.cold.3
+ ___60-[VCCallSession(PrivateMethods) setupCalleeSIPStartTimeout:]_block_invoke.1255
+ ___76-[VCCallSession(PrivateMethods) getAllCompatibleVideoPayloads:forMediaType:]_block_invoke.1419
+ ___84-[VCCallSession(PrivateMethods) disconnectInternal:disconnectError:didRemoteCancel:]_block_invoke.1584
+ ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.224
+ ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.709
+ ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.711
+ ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.703
+ ____VCVideoStream_DidReceiveRemoteFrame_block_invoke.793
+ ____VideoReceiver_SendRTCP_block_invoke.cold.1
+ ___block_descriptor_40_e8_32o_e389_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8ls32l8
+ ___block_descriptor_48_e8_32r40r_e389_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8lr32l8r40l8
+ ___block_descriptor_tmp.378
+ ___block_descriptor_tmp.427
+ ___block_descriptor_tmp.429
+ ___block_literal_global.180
+ ___block_literal_global.183
+ ___block_literal_global.219
+ ___block_literal_global.223
+ ___block_literal_global.234
+ ___block_literal_global.250
+ ___block_literal_global.265
+ ___block_literal_global.276
+ ___block_literal_global.283
+ ___block_literal_global.297
+ ___block_literal_global.304
+ ___block_literal_global.311
+ ___block_literal_global.318
+ ___block_literal_global.325
+ ___block_literal_global.332
+ ___block_literal_global.336
+ ___block_literal_global.343
+ __unnamed_array_storage.1300
+ __unnamed_array_storage.1333
+ __unnamed_array_storage.1336
+ __unnamed_array_storage.1778
+ __unnamed_array_storage.1782
+ __unnamed_array_storage.1785
+ __unnamed_array_storage.1797
+ __unnamed_array_storage.1800
+ __unnamed_array_storage.1818
+ __unnamed_array_storage.323
+ __unnamed_array_storage.332
+ __unnamed_array_storage.341
+ __unnamed_array_storage.350
+ __unnamed_array_storage.368
+ __unnamed_array_storage.371
+ __unnamed_array_storage.436
+ __unnamed_array_storage.439
+ __unnamed_array_storage.449
+ __unnamed_array_storage.517
+ __unnamed_array_storage.520
+ __unnamed_array_storage.523
+ __unnamed_array_storage.526
+ __unnamed_array_storage.529
+ __unnamed_array_storage.532
+ __unnamed_array_storage.593
+ __unnamed_array_storage.596
+ __unnamed_array_storage.599
+ __unnamed_array_storage.602
+ __unnamed_array_storage.605
+ __unnamed_array_storage.608
+ __unnamed_array_storage.611
+ __unnamed_array_storage.612
+ _objc_msgSend$remoteCameraReportingClientType
+ _objc_msgSend$revertMultiwayToOneToOneModeSwitchConfigure
+ _objc_msgSend$screenSharingReportingClientType
+ _objc_msgSend$shouldSetUpXPCConnection
+ _objc_msgSend$startCaptureIfNeeded:
+ _objc_msgSend$stopCaptureForEndToEndStreamIfNeeded
+ _sRTCReportingPeerCamClientName
- -[VCAudioCaptions destroyAudioConverter:]
- -[VCDefaults forceEnableAudioMockInputPathForAppleTV]
- -[VCVideoStream reportingClientTypeForClientName]
- GCC_except_table73
- _OBJC_CLASS_$_NSDecimalNumber
- _OBJC_IVAR_$_VCMediaControlInfoFaceTimeAudio._controlInfoReceivedKbits
- _OBJC_IVAR_$_VCMediaControlInfoFaceTimeVideo._controlInfoReceivedKbits
- __OBJC_$_PROP_LIST_VCVideoCaptureServer.697
- __VCAudioPlayerDTMF_InitializeRunTimeParams
- __VCJBTargetEstimatorSynchronizer_Initialize
- ___135-[VideoConference(SessionDelegate) session:receivedRemoteFrame:atTime:withScreenAttributes:videoAttributes:isFirstFrame:isVideoPaused:]_block_invoke.631
- ___35-[VCNetworkFeedbackController stop]_block_invoke
- ___40-[VCConnectionManagerIDS addConnection:]_block_invoke.40
- ___43-[VCSessionParticipant mediaTypeMixingList]_block_invoke
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.170
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.173
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.173.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.173.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.177
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.187
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.187.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.187.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.187.cold.3
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.187.cold.4
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.216
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.231
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.247
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.247.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.262
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.273
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.273.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.280
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.280.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.287
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.287.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.294
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.294.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.301
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.301.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.308
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.308.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.315
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.315.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.322
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.333
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.344
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.347
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.349
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.356
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.220
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.239
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.266
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.266.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.329
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.329.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.340
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.340.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.353
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.224
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.224.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.241
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.241.cold.1
- ___50-[VCCallSession(PrivateMethods) updateDeviceRole:]_block_invoke.1457
- ___50-[VCCallSession(PrivateMethods) updateDeviceRole:]_block_invoke.1464
- ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke.108
- ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.113
- ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.113.cold.1
- ___51-[AVCCaptionsClient registerBlocksForNotifications]_block_invoke_2.113.cold.2
- ___53-[VCCallSession(Messages) setupSymptomEnabledMessage]_block_invoke.1815
- ___60-[VCCallSession(PrivateMethods) setupCalleeSIPStartTimeout:]_block_invoke.1254
- ___76-[VCCallSession(PrivateMethods) getAllCompatibleVideoPayloads:forMediaType:]_block_invoke.1418
- ___84-[VCCallSession(PrivateMethods) disconnectInternal:disconnectError:didRemoteCancel:]_block_invoke.1583
- ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.223
- ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.708
- ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.710
- ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.702
- ____VCVideoStream_DidReceiveRemoteFrame_block_invoke.791
- ___block_descriptor_40_e8_32o_e385_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8ls32l8
- ___block_descriptor_48_e8_32r40r_e385_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8lr32l8r40l8
- ___block_descriptor_tmp.372
- ___block_descriptor_tmp.424
- ___block_descriptor_tmp.426
- ___block_literal_global.182
- ___block_literal_global.222
- ___block_literal_global.226
- ___block_literal_global.233
- ___block_literal_global.249
- ___block_literal_global.264
- ___block_literal_global.268
- ___block_literal_global.289
- ___block_literal_global.303
- ___block_literal_global.310
- ___block_literal_global.317
- ___block_literal_global.324
- ___block_literal_global.331
- ___block_literal_global.335
- ___block_literal_global.351
- __unnamed_array_storage.1299
- __unnamed_array_storage.1332
- __unnamed_array_storage.1335
- __unnamed_array_storage.1777
- __unnamed_array_storage.1781
- __unnamed_array_storage.1784
- __unnamed_array_storage.1796
- __unnamed_array_storage.1799
- __unnamed_array_storage.1817
- __unnamed_array_storage.320
- __unnamed_array_storage.329
- __unnamed_array_storage.338
- __unnamed_array_storage.356
- __unnamed_array_storage.358
- __unnamed_array_storage.359
- __unnamed_array_storage.361
- __unnamed_array_storage.364
- __unnamed_array_storage.367
- __unnamed_array_storage.434
- __unnamed_array_storage.451
- __unnamed_array_storage.454
- __unnamed_array_storage.515
- __unnamed_array_storage.518
- __unnamed_array_storage.521
- __unnamed_array_storage.524
- __unnamed_array_storage.527
- __unnamed_array_storage.530
- __unnamed_array_storage.591
- _objc_msgSend$destroyAudioConverter:
- _objc_msgSend$notANumber
- _objc_msgSend$reportingClientTypeForClientName
CStrings:
+ " [%s] %s:%d %@(%p) Failed to restart capture"
+ " [%s] %s:%d %@(%p) Starting capture failed with error=%@"
+ " [%s] %s:%d %@(%p) pause audio stream failed"
+ " [%s] %s:%d Failed to restart capture"
+ " [%s] %s:%d Starting capture failed with error=%@"
+ " [%s] %s:%d pause audio stream failed"
+ "-[VCAudioStreamSendGroup startCaptureIfNeeded:]"
+ "2015.3.1"
+ "@192@0:8{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}16"
+ "ARxPLR"
+ "AVCRC [%s] %s:%d [%p] config for key=%s serverBagContainsGroup=%d basebandAdaptationEnabled=%d"
+ "B116@0:8{?=IBBBIIdIB{?=iIIIIdddII}}16I104^@108"
+ "B32@0:8^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16d24"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,GisNetworkProvider"
+ "TB,?,N,GisNexusProvider"
+ "TB,?,N,GisSpecificUseOnly"
+ "TB,?,N,GisSpecificUseOnly,VspecificUseOnly"
+ "TB,?,N,V_followSystemCamera"
+ "TB,?,R,N"
+ "TB,?,R,N,V_is1080pCameraAvailable"
+ "TB,R,N,V_disableBasebandFlush"
+ "Ti,?,R,N"
+ "Ti,?,R,N,V_bestCameraCaptureFrameRate"
+ "VCConnection_GetDataMode"
+ "VCRC [%s] %s:%d [%p] config for key=%s serverBagContainsGroup=%d _disableBasebandFlush=%d"
+ "VCVideoPlayer [%s] %s:%d Created VCVideoPlayer[%p] successfully with enableAVLooseSync=%d minPlaybackInterval=%f minPlaybackInterval=%f, enableQueueAlarmForDisplay=%d, enableImmediateDecode=%d, useInternalClockForPresentation=%d, enableJitterBuffer=%d"
+ "VideoReceiver [%s] %s:%d Failed to create reporting event dictionary"
+ "[300{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalReceivedKBytes\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}]"
+ "^{tagVCStatisticsCollection={?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=iIIIIdddII}{?=IIIIfBBddIIIQ}{tagVCStatisticsVideoLossFeedback=ISCC}}"
+ "_AVCRateController_ApplyServerBagBasebandConfig"
+ "_VideoReceiver_CreateReportingEventDictionary"
+ "_controlInfoReceivedKBytes"
+ "_disableBasebandFlush"
+ "_mediaTypeMixingListLock"
+ "_previousConverterSamples"
+ "baseband"
+ "connectionDataMode"
+ "disableBasebandFlush"
+ "remoteCameraReportingClientType"
+ "revertMultiwayToOneToOneModeSwitchConfigure"
+ "screenSharingReportingClientType"
+ "shouldSetUpXPCConnection"
+ "startCaptureIfNeeded:"
+ "stopCaptureForEndToEndStreamIfNeeded"
+ "totalReceviedKBytes"
+ "v208@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8"
+ "v216@0:8{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16"
+ "{?=\"timeStamp\"S\"bandwithEstimation\"S\"videoBurstLoss\"S\"videoReceviedPkts\"S\"audioBurstLoss\"S\"audioReceviedPkts\"S\"totalReceivedKBytes\"I\"receiveQueueTarget\"I\"queuingDelay\"I\"sendTimestamp\"S\"owrd\"I\"connectionStatsBuffer\"I\"ecnECT1Count\"S\"ecnCECount\"S}"
+ "{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalReceivedKBytes\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"totalReceivedKBytes\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}"
+ "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}24@0:8^{?=iSd(?={?=SCSCcIIII}{?=SSS[6{?=CS[500S]}]}{?=SS})}16"
+ "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}28@0:8i16d20"
- "2010.3.1"
- "@176@0:8{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}16"
- "B108@0:8{?=IBBBIIdIB{?=iIIIdddII}}16I96^@100"
- "B32@0:8^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16d24"
- "TB,N,GisNetworkProvider"
- "TB,N,GisNexusProvider"
- "TB,N,GisSpecificUseOnly"
- "TB,N,GisSpecificUseOnly,VspecificUseOnly"
- "TB,N,V_followSystemCamera"
- "TB,R,N,V_is1080pCameraAvailable"
- "Ti,R,N,V_bestCameraCaptureFrameRate"
- "VCVideoPlayer [%s] %s:%d Created VCVideoPlayer[%p] successfully with enableAVLooseSync=%d minPlaybackInterval=%f"
- "[300{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}]"
- "^{tagVCStatisticsCollection={?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=iIIIdddII}{?=IIIIfBBddIIIQ}{tagVCStatisticsVideoLossFeedback=ISCC}}"
- "_controlInfoReceivedKbits"
- "destroyAudioConverter:"
- "notANumber"
- "reportingClientTypeForClientName"
- "totalReceviedKbits"
- "v192@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8"
- "v200@0:8{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16"
- "v24@0:8^{OpaqueAudioConverter=}16"
- "{?=\"timeStamp\"S\"bandwithEstimation\"S\"videoBurstLoss\"S\"videoReceviedPkts\"S\"audioBurstLoss\"S\"audioReceviedPkts\"S\"totalReceviedKbits\"I\"receiveQueueTarget\"I\"queuingDelay\"I\"sendTimestamp\"S\"owrd\"I\"connectionStatsBuffer\"I\"ecnECT1Count\"S\"ecnCECount\"S}"
- "{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}"
- "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}24@0:8^{?=iSd(?={?=SCSCcIIII}{?=SSS[6{?=CS[500S]}]}{?=SS})}16"
- "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}28@0:8i16d20"

```
