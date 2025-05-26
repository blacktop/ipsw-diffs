## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2005.6.1.1.2
-  __TEXT.__text: 0x639118
+2010.3.1.0.0
+  __TEXT.__text: 0x63aea4
   __TEXT.__auth_stubs: 0x4c30
-  __TEXT.__objc_methlist: 0x2ab94
-  __TEXT.__const: 0x7a18
-  __TEXT.__cstring: 0x74dce
-  __TEXT.__oslogstring: 0xd999b
+  __TEXT.__objc_methlist: 0x2ac1c
+  __TEXT.__const: 0x79b8
+  __TEXT.__cstring: 0x750c0
+  __TEXT.__oslogstring: 0xd9b0f
   __TEXT.__gcc_except_tab: 0x1f84
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xc6bc
+  __TEXT.__unwind_info: 0xc714
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x42d9
-  __TEXT.__objc_methname: 0x69396
-  __TEXT.__objc_methtype: 0x20f39
-  __TEXT.__objc_stubs: 0x42a80
+  __TEXT.__objc_methname: 0x6952c
+  __TEXT.__objc_methtype: 0x21112
+  __TEXT.__objc_stubs: 0x42b80
   __DATA_CONST.__got: 0x1110
   __DATA_CONST.__const: 0x5a18
   __DATA_CONST.__objc_classlist: 0x1088
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f040
-  __DATA_CONST.__objc_selrefs: 0x131f0
+  __DATA_CONST.__objc_const: 0x4f120
+  __DATA_CONST.__objc_selrefs: 0x13238
   __DATA_CONST.__objc_arraydata: 0x1e38
-  __AUTH_CONST.__cfstring: 0x1faa0
+  __AUTH_CONST.__cfstring: 0x1fda0
   __AUTH_CONST.__objc_intobj: 0x3a20
   __AUTH_CONST.__objc_arrayobj: 0x14e8
   __AUTH_CONST.__objc_const: 0x0

   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x1208
   __DATA.__objc_superrefs: 0xee8
-  __DATA.__objc_ivar: 0x5d68
+  __DATA.__objc_ivar: 0x5d84
   __DATA.__data: 0x6f98
-  __DATA.__bss: 0xa20
+  __DATA.__bss: 0xa30
   __DATA.__common: 0x55
-  __DATA_DIRTY.__const: 0x2cf8
+  __DATA_DIRTY.__const: 0x2d18
   __DATA_DIRTY.__objc_const: 0xc980
   __DATA_DIRTY.__objc_data: 0xa550
-  __DATA_DIRTY.__data: 0x150
+  __DATA_DIRTY.__data: 0x148
   __DATA_DIRTY.__bss: 0x350
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 28077
-  Symbols:   78915
-  CStrings:  43877
+  Functions: 28107
+  Symbols:   78993
+  CStrings:  43936
 
Symbols:
+ +[LogDumpUtility fileCleanupDispatchQueuePriority]
+ -[VCAVFoundationCapture collectCaptureFrameRateStats:]
+ -[VCConnectionManagerIDS isEndToEndLinkAvailable]
+ -[VCConnectionManagerIDS isEndToEndLinkWithCellAvailable:]
+ -[VCNetworkFeedbackController reportWRMMetrics:].cold.1
+ -[VCNetworkFeedbackController sendStatusUpdate:].cold.1
+ -[VCSession(OneToOne) detailedErrorCodeForNoRemotePacketsError]
+ -[VCTransportSession addNetworkAssertionWithInterfaceType:]
+ -[VCTransportSession removeNetworkAssertion]
+ -[VCTransportSessionNW addNetworkAssertion]
+ -[VCTransportSessionNW removeNetworkAssertion]
+ -[VCTransportSessionSocket addNetworkAssertion]
+ -[VCTransportSessionSocket removeNetworkAssertion]
+ GCC_except_table137
+ GCC_except_table82
+ GCC_except_table87
+ _OBJC_IVAR_$_VCAVFoundationCapture._captureDuration
+ _OBJC_IVAR_$_VCAVFoundationCapture._captureFrameCount
+ _OBJC_IVAR_$_VCAVFoundationCapture._captureStartTime
+ _OBJC_IVAR_$_VCAudioTransmitter._audioTierChangeCount
+ _OBJC_IVAR_$_VCAudioTransmitter._tierInfo
+ _OBJC_IVAR_$_VCConnectionManager._lastReceivedReportingStats
+ _OBJC_IVAR_$_VCTransportSession._didAddNetworkAssertion
+ _VCConnection_ReportingConnectionType
+ _VCConnection_ReportingInterface
+ _VCFeatureFlagManager_SkipNonInfraWiFiAssertion
+ _VCFeatureFlagManager_SkipNonInfraWiFiAssertion.onceToken
+ _VCFeatureFlagManager_SkipNonInfraWiFiAssertion.result
+ _VCNWConnectionMonitor_ResetWlanStats
+ _VCNWConnectionMonitor_ResetWlanStats.cold.1
+ _VCVideoPlayer_CollectVideoPlayerStatsForReporting
+ _VCVideoPlayer_GetVideoPlayerStatsForJB
+ _VTP_GetReportingStats
+ _VTP_GetReportingStats.cold.1
+ _VTP_GetReportingStats.cold.2
+ __OBJC_$_PROP_LIST_VCVideoCaptureServer.697
+ __VideoTransmitter_UpdateAVHostTimeStats
+ ___36-[VCVideoCaptureServer pausePreview]_block_invoke.310
+ ___42-[VCSessionParticipant setSharingEnabled:]_block_invoke
+ ___43-[VCTransportSessionNW addNetworkAssertion]_block_invoke
+ ___46-[VCTransportSessionNW removeNetworkAssertion]_block_invoke
+ ___47-[VCTransportSessionSocket addNetworkAssertion]_block_invoke
+ ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.335
+ ___50-[VCTransportSessionSocket removeNetworkAssertion]_block_invoke
+ ___54-[VCAVFoundationCapture collectCaptureFrameRateStats:]_block_invoke
+ ___VCFeatureFlagManager_SkipNonInfraWiFiAssertion_block_invoke
+ ____VCNWConnectionMonitor_DispatchedCreateWithInterfaceName_block_invoke.19
+ ____VCNWConnectionMonitor_DispatchedSetNotificationHandler_block_invoke.24
+ ____VCNWConnectionMonitor_DispatchedSetPacketEventHandler_block_invoke.28
+ ____VCNWConnectionMonitor_DispatchedSetStatisticsHandler_block_invoke.33
+ ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.708
+ ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.710
+ ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.702
+ ___block_descriptor_40_e8_32o_e385_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8ls32l8
+ ___block_descriptor_40_e8_32r_e1156_v24?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}{tagVTransportReportingStats=qqqq}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}}16lr32l8
+ ___block_descriptor_48_e8_32r40r_e385_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e1156_v24?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}{tagVTransportReportingStats=qqqq}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}}16lr32l8
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.208
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.372
+ ___block_descriptor_tmp.424
+ ___block_descriptor_tmp.426
+ ___block_literal_global.314
+ __unnamed_array_storage.135
+ __unnamed_array_storage.138
+ _objc_msgSend$addNetworkAssertion
+ _objc_msgSend$addNetworkAssertionWithInterfaceType:
+ _objc_msgSend$collectCaptureFrameRateStats:
+ _objc_msgSend$deleteCharactersInRange:
+ _objc_msgSend$detailedErrorCodeForNoRemotePacketsError
+ _objc_msgSend$fileCleanupDispatchQueuePriority
+ _objc_msgSend$isEndToEndLinkAvailable
+ _objc_msgSend$isEndToEndLinkWithCellAvailable:
+ _objc_msgSend$removeNetworkAssertion
- GCC_except_table138
- GCC_except_table81
- GCC_except_table86
- _VCVideoPlayer_GetVideoPlayerStats
- __OBJC_$_PROP_LIST_VCVideoCaptureServer.695
- __VCConnectionManager_SetDuplicationEnabled
- ___36-[VCVideoCaptureServer pausePreview]_block_invoke.308
- ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.333
- ____VCNWConnectionMonitor_DispatchedCreateWithInterfaceName_block_invoke.15
- ____VCNWConnectionMonitor_DispatchedSetNotificationHandler_block_invoke.20
- ____VCNWConnectionMonitor_DispatchedSetPacketEventHandler_block_invoke.24
- ____VCNWConnectionMonitor_DispatchedSetStatisticsHandler_block_invoke.29
- ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.706
- ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.708
- ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.700
- ___block_descriptor_40_e8_32o_e382_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8ls32l8
- ___block_descriptor_40_e8_32r_e1122_v24?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}}16lr32l8
- ___block_descriptor_48_e8_32r40r_e382_v192?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8lr32l8r40l8
- ___block_descriptor_48_e8_32r_e1122_v24?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}}16lr32l8
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.366
- ___block_descriptor_tmp.418
- ___block_descriptor_tmp.420
- ___block_literal_global.312
- __unnamed_array_storage.114
- __unnamed_array_storage.117
- _objc_msgSend$noRemotePacketInterval
CStrings:
+ " [%s] %s:%d @=@ Health: VCConnectionManager [%p] interfaceName=%@ offChannelRatio=%2.3f btCoex=%d frequencyBand=%d qualityScoreDelayRx=%d qualityScoreDelayTx=%d qualityScoreLossRx=%d qualityScoreLossTx=%d qualityScoreChannel=%d maxRadioCoex=0x%X accumulatedOffChannelTime=%lld maxSingleOutagePeriod=%u"
+ " [%s] %s:%d Cannot check in VTP handle"
+ " [%s] %s:%d NetworkAgent assertion added"
+ " [%s] %s:%d NetworkAgent assertion removed"
+ " [%s] %s:%d Unexpected: Adding assertion multiple times"
+ " [%s] %s:%d WRM metric report cannot be null"
+ " [%s] %s:%d WRM status update cannot be null"
+ "%@:%@,"
+ "%c%c%d%c"
+ "-[VCNetworkFeedbackController reportWRMMetrics:]"
+ "-[VCNetworkFeedbackController sendStatusUpdate:]"
+ "-[VCTransportSession addNetworkAssertionWithInterfaceType:]"
+ "-[VCTransportSession removeNetworkAssertion]"
+ "2010.3.1"
+ "ATierChangeCount"
+ "AVHTDAbsSum"
+ "AVHTDCount"
+ "AVHTDMax"
+ "AVHTDMin"
+ "AVHTDSum"
+ "B32@0:8^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16d24"
+ "BitRateAlt"
+ "BundleAlt"
+ "CAMDUR"
+ "CAMFC"
+ "NWOffChannelTime"
+ "NWOutagePeriodMax"
+ "NWRadioCoexMax"
+ "PayloadAlt"
+ "RedMaxDelayAlt"
+ "RedPayloadsAlt"
+ "ReportingFrequency"
+ "SkipNonInfraWiFiAssertion"
+ "SkipNonInfraWiFiAssertion=%d"
+ "VCConnection_ReportingConnectionType"
+ "VCConnection_ReportingInterface"
+ "VCNWConnectionMonitor_ResetWlanStats"
+ "VCVideoPlayer_CollectVideoPlayerStatsForReporting"
+ "VCVideoPlayer_GetVideoPlayerStatsForJB"
+ "VPFDC"
+ "VPFDCD"
+ "VTPDownlinkEgressMediaPkts"
+ "VTPDownlinkIngressMediaPkts"
+ "VTPUplinkEgressPkts"
+ "VTPUplinkIngressPkts"
+ "VTP_GetReportingStats"
+ "[300{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}]"
+ "_audioTierChangeCount"
+ "_captureDuration"
+ "_captureFrameCount"
+ "_captureStartTime"
+ "_didAddNetworkAssertion"
+ "_lastReceivedReportingStats"
+ "_tierInfo"
+ "addNetworkAssertion"
+ "addNetworkAssertionWithInterfaceType:"
+ "collectCaptureFrameRateStats:"
+ "deleteCharactersInRange:"
+ "detailedErrorCodeForNoRemotePacketsError"
+ "fileCleanupDispatchQueuePriority"
+ "isEndToEndLinkAvailable"
+ "isEndToEndLinkWithCellAvailable:"
+ "removeNetworkAssertion"
+ "v192@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8"
+ "v200@0:8{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16"
+ "v24@?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}{tagVTransportReportingStats=qqqq}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}@@@}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}}16"
+ "{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}"
+ "{tagTierInfo=\"tier\"I\"duplication\"I\"redPayloads\"I\"redMaxDelay\"I\"bundling\"I\"codecPayload\"I\"codecBitrate\"I}"
+ "{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]\"maxRadioCoex\"C\"accumulatedOffChannelTime\"q\"maxSingleOutagePeriod\"S}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}"
+ "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}24@0:8^{?=iSd(?={?=SCSCcIIII}{?=SSS[6{?=CS[500S]}]}{?=SS})}16"
+ "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]CqS}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}28@0:8i16d20"
+ "{tagVTransportReportingStats=\"totalDownlinkIngressMediaPackets\"q\"totalDownlinkEgressMediaPackets\"q\"totalUplinkIngressPackets\"q\"totalUplinkEgressPackets\"q}"
- " [%s] %s:%d @=@ Health: VCConnectionManager [%p] interfaceName=%@ offChannelRatio=%2.3f btCoex=%d frequencyBand=%d qualityScoreDelayRx=%d qualityScoreDelayTx=%d qualityScoreLossRx=%d qualityScoreLossTx=%d qualityScoreChannel=%d"
- "%d:%d:%d:%d:%d:%d:%d:%d:%d"
- "2005.6.1.1.2"
- "B32@0:8^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16d24"
- "VCVideoPlayer_GetVideoPlayerStats"
- "[300{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}]"
- "v192@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}8"
- "v200@0:8{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}16"
- "v24@?0^{tagVTRANSPORT=qqSSii^{OpaqueFigThread}B{_opaque_pthread_mutex_t=q[56c]}^?^v[1024i]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}[1024B]{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDLIST}{_opaque_pthread_rwlock_t=q[192c]}^{tagVFDSETLIST}{_opaque_pthread_mutex_t=q[56c]}^{tagIFMAP}i^{tagVCMemoryPool}^{tagVFDRESULT}^{tagHANDLE}BB[924B][924^{__CFString}][924^{tagHANDLE}]BBiIC{_opaque_pthread_rwlock_t=q[192c]}^{__CFDictionary}^{tagVPKTLIST}IId{VTransportHealthStats=[2{_VTransportConnectionHealthStats=IIII}]{_VTransportDemuxPacketHealthStats=IIIII}{_VTransportTrafficClassHealthStats=III}dd}Iddi^{__CFAllocator}^{__CFAllocator}^{tagVCMemoryPool}^{__CFAllocator}@@@}8^{tagVFDLIST=iiiiiiCCCBi^iiIIII{tagIPPORT=i[16c](?=I[16C])S}^{tagVPKTLIST}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}ii[4C]{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{tagVFDLIST}^{tagHANDLE}B{?=i[12C]}{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}}16"
- "{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}"
- "{tagVCStatisticsMessage=\"type\"i\"priority\"i\"arrivalTime\"d\"isVCRCInternal\"B\"shouldFlushAndProcess\"B\"shouldDrainAndProcess\"B\"statisticsUpdateOnly\"B\"\"(?=\"baseband\"{?=\"queueDepth1\"I\"queueDepth2\"I\"txBitrate\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d\"bbString\"[64c]\"radioTechnology\"i}\"feedback\"{?=\"sendTimestamp\"I\"queuingDelay\"I\"remoteBWEstimation\"I\"remoteBWEStability\"I\"maxVideoBurstyLoss\"I\"audioConsecutiveLoss\"I\"mostBurstyLoss\"I\"audioReceivedPackets\"I\"videoReceivedPackets\"I\"totalSentPackets\"I\"echoedSendTimestamp\"I\"mediaTimestamp\"I\"owrd\"d\"packetLossRate\"d\"actualBitrate\"I\"instantBitrate\"I\"roundTripTime\"d\"receiveQueueTarget\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"connectionStats\"{?=\"sequenceNumber\"S\"isDuplicatePacket\"B\"isReceivedOnPrimary\"B\"connectionStatsBuffer\"I}\"ecnStats\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"ecnRecvd\"{tagVCStatisticsECNStats=\"ecnECT1Count\"S\"ecnCECount\"S}\"isECNEnabled\"B}\"network\"{?=\"packetLossPercentage\"d\"packetLossPercentageAudio\"d\"packetLossPercentageVideo\"d\"burstPacketLoss\"I\"roundTripTimeMilliseconds\"I\"isNetworkCongested\"I\"owrd\"I\"targetBitrate\"I\"statisticsID\"Q\"videoPacketsReceived\"I}\"probing\"{?=\"estimatorID\"I\"deregisterEstimator\"B\"isProbingSequence\"B\"isEndOfProbingSequence\"B\"probingSequenceID\"I\"messageLength\"I\"arrivalTime\"d\"mediaTimestamp\"I\"isPacketReceivedValid\"B\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}}\"serverStats\"{?=\"linkID\"C\"sendTimestamp\"I\"receiveTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"I\"totalByteReceived\"I\"serverStatsByteUsed\"I\"bandwidthSample\"I\"bandwidthEstimation\"I\"roundTripTime\"d\"owrd\"d\"packetLossRate\"d\"packetLossRateShortWindow\"d\"actualBitrate\"I\"instantBitrate\"I\"serverStatsBitrate\"I\"expectedBitrate\"I}\"packetSent\"{?=\"packetId\"I\"totalPacketsSent\"I\"totalBytesSent\"I\"sendTimestamp\"d}\"packetReceived\"{?=\"packetType\"i\"packetId\"I\"sampleRate\"I\"totalPacketsReceived\"I\"receiveTimestamp\"d\"owrd\"d\"targetJitterQueueSize\"d\"bandwidthEstimation\"I\"localBurstyLoss\"I}\"rtcpRR\"{?=\"ssrc\"I\"packetLossPercentage\"I\"lastSequenceNumber\"I\"roundTripTimeMilliseconds\"I}\"config\"{?=\"mode\"I\"remoteRadioAccessTechnology\"I\"localRadioAccessTechnology\"I\"maxBitrate\"I\"minBitrate\"I\"initialBitrate\"I\"isTrafficBursty\"B\"featureFlags\"I}\"mediaEvent\"{?=\"mediaEventType\"I\"additionalFlushCount\"I\"transactionID\"I\"audioStallBitrate\"I\"audioErasure\"f\"isKeyFrame\"B\"isTransitionToFEC\"B\"videoStallTimeDelta\"d\"videoStallTimeTotal\"d\"refreshFrameTimestamp\"I\"refreshFramePayloadType\"I\"refreshFramePacketCount\"I\"idsParticipantID\"Q}\"nwConnection\"{?=\"version\"C\"direction\"C\"interfaceType\"C\"timestamp\"Q\"maxThroughputBps\"Q\"totalByteCount\"Q\"flushableQueueSize\"I\"nonFlushableQueueSize\"I\"averageDelayMillisecond\"I\"averageThroughputBps\"Q\"rateTrendSuggestion\"i\"packetLossPerFrame\"I\"\"(?=\"wifi\"{?=\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"detectedFrequentOffChannelActivity\"B\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]}\"baseband\"{?=\"radioAccessTechnology\"C\"referenceSignalLevel\"s\"signalLevel\"s\"signalQuality\"c\"uplinkBLER\"C\"downlinkBLER\"C\"bandwidthLimitationIndication\"C\"cdrxState\"C\"cdrxCycle\"S\"estimatedOutagePeriod\"S\"outageState\"C})}\"videoLossFeedback\"{tagVCStatisticsVideoLossFeedback=\"frameRTPTimestamp\"I\"packetsReceived\"S\"frameSize\"C\"packetsLost\"C})}"
- "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}24@0:8^{?=iSd(?={?=SCSCcIIII}{?=SSS[6{?=CS[500S]}]}{?=SS})}16"
- "{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIddddd[64c]i}{?=IIIIIIIIIIIIddIIdIB{?=iIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}B}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIdddII}{?=IIII}{?=IIIIIIBI}{?=IIIIfBBddIIIQ}{?=CCCQQQIIIQiI(?={?=CCSSCCCCCCCfBS[6I]}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC})}28@0:8i16d20"

```
