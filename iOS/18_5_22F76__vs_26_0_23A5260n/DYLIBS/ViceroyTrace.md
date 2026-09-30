## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2115.6.1.0.0
-  __TEXT.__text: 0xa21a4
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x85b8
-  __TEXT.__const: 0x2260
-  __TEXT.__cstring: 0xceef
-  __TEXT.__oslogstring: 0xb83f
-  __TEXT.__gcc_except_tab: 0x3a0
+2145.45.1.11.2
+  __TEXT.__text: 0xabac0
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_methlist: 0x8bf0
+  __TEXT.__const: 0x2478
+  __TEXT.__cstring: 0xe5de
+  __TEXT.__oslogstring: 0xc421
+  __TEXT.__gcc_except_tab: 0x3b4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1510
+  __TEXT.__unwind_info: 0x1668
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x19d03
-  __TEXT.__objc_methtype: 0x2124
-  __TEXT.__objc_stubs: 0xddc0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xce0
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __TEXT.__objc_classname: 0x599
+  __TEXT.__objc_methname: 0x1b640
+  __TEXT.__objc_methtype: 0x23c3
+  __TEXT.__objc_stubs: 0xeac0
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0xd68
+  __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e68
-  __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0x210
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xcf00
-  __AUTH_CONST.__objc_const: 0x153f0
+  __DATA_CONST.__objc_selrefs: 0x4200
+  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_arraydata: 0x220
+  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0xdbe0
+  __AUTH_CONST.__objc_const: 0x16640
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0x1e38
-  __DATA.__data: 0x648
-  __DATA.__bss: 0xe8
-  __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x10e0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x1fe0
+  __DATA.__data: 0x698
+  __DATA.__bss: 0x70
+  __DATA.__common: 0x1
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__common: 0x2
-  __DATA_DIRTY.__bss: 0x11
+  __DATA_DIRTY.__bss: 0x9a
+  __DATA_DIRTY.__common: 0x22
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle
-  - /System/Library/PrivateFrameworks/AlgosScoreFramework.framework/AlgosScoreFramework
+  - /System/Library/PrivateFrameworks/NetworkScore.framework/NetworkScore
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3EA47A89-2D1A-3CEB-8C5B-74674135FC45
-  Functions: 3718
-  Symbols:   12287
-  CStrings:  8629
+  UUID: 7C75EE57-C7AF-30F3-9EB4-A85FEB39E498
+  Functions: 3914
+  Symbols:   12905
+  CStrings:  9151
 
Symbols:
+ +[VCAggregatorUtils videoResolutionForWidth:height:]
+ +[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:]
+ +[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:].cold.1
+ +[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:].cold.2
+ +[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:].cold.3
+ +[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:].cold.4
+ -[CallSegment callAverageAudioRxBitrate]
+ -[CallSegment callAverageAudioTxBitrate]
+ -[CallSegment fecStatsHolder]
+ -[CallSegment setCallAverageAudioRxBitrate:]
+ -[CallSegment setCallAverageAudioTxBitrate:]
+ -[DownlinkSegment lateKeyFrameAssembledCount]
+ -[DownlinkSegment latePFrameAssembledCount]
+ -[DownlinkSegment processRTEvent:now:]
+ -[DownlinkSegment setLateKeyFrameAssembledCount:]
+ -[DownlinkSegment setLatePFrameAssembledCount:]
+ -[MultiwayCall audioErasureTotalTimeAlt:]
+ -[MultiwayCall fecStatsHolder]
+ -[MultiwayCall lossFecHistogram]
+ -[MultiwayCall lossHistogram]
+ -[MultiwayCall lossPattern]
+ -[MultiwaySegment VCRCML_activeMLEngagedDuration]
+ -[MultiwaySegment VCRCML_isMLEngaged]
+ -[MultiwaySegment VCRCML_modelID]
+ -[MultiwaySegment VCRCML_nIteration]
+ -[MultiwaySegment VCRCML_recipeID]
+ -[MultiwaySegment VCRCML_reportingGroup]
+ -[MultiwaySegment VCRCML_targetBitrateAtTimeOfDisengagement]
+ -[MultiwaySegment appendPathMTU:delta:]
+ -[MultiwaySegment fecHeaderVersion]
+ -[MultiwaySegment fecStatsHolder]
+ -[MultiwaySegment finalizePathMTUForTime:]
+ -[MultiwaySegment localParticipantID]
+ -[MultiwaySegment processFrameSizeBasedFECTelemetry:statsHolder:direction:]
+ -[MultiwaySegment processPathMTU:now:]
+ -[MultiwaySegment processRTEventCommon:now:]
+ -[MultiwaySegment remoteDeviceType]
+ -[MultiwaySegment reportVCRCMLStats:]
+ -[MultiwaySegment setFecHeaderVersion:]
+ -[MultiwaySegment setLocalParticipantID:]
+ -[MultiwaySegment setRemoteDeviceType:]
+ -[MultiwaySegment setVCRCML_activeMLEngagedDuration:]
+ -[MultiwaySegment setVCRCML_isMLEngaged:]
+ -[MultiwaySegment setVCRCML_modelID:]
+ -[MultiwaySegment setVCRCML_nIteration:]
+ -[MultiwaySegment setVCRCML_recipeID:]
+ -[MultiwaySegment setVCRCML_reportingGroup:]
+ -[MultiwaySegment setVCRCML_targetBitrateAtTimeOfDisengagement:]
+ -[MultiwayStream audioErasureTotalTimeAlt]
+ -[MultiwayStream averageVideoRxMetadataOverheadBitrate]
+ -[MultiwayStream averageVideoTxMetadataOverheadBitrate]
+ -[MultiwayStream lateKeyFrameAssembledCount]
+ -[MultiwayStream latePFrameAssembledCount]
+ -[MultiwayStream totalAudioErasureTimeAlt]
+ -[RTCReportingAgent remoteDataProducer]
+ -[RTCReportingAgent sendMessageToAWDAdaptorWithCategory:type:payload:]
+ -[RTCReportingAgent sendNetworkScoreDictionary:networkScoreType:]
+ -[RTCReportingAgent sendNetworkScoreDictionary:networkScoreType:].cold.1
+ -[RTCReportingAgent setUpAWDAdapter]
+ -[RTCReportingAgent sharedAWDAdaptorClass]
+ -[RTCReportingAgent sharedAWDAdaptorClass].cold.1
+ -[StreamGroupStats averageMetadataRxBitrate]
+ -[StreamGroupStats averageMetadataTxBitrate]
+ -[StreamGroupStats finalizeStats]
+ -[StreamGroupStats lateKeyFrameAssembledCount]
+ -[StreamGroupStats latePFrameAssembledCount]
+ -[StreamGroupStats mlEnhancedPercentInputResolutions]
+ -[StreamGroupStats mlEnhancedPercentOutputResolutions]
+ -[StreamGroupStats processMLStreamData:]
+ -[StreamGroupStats resetMLStats]
+ -[StreamGroupStats setAverageMetadataRxBitrate:]
+ -[StreamGroupStats setAverageMetadataTxBitrate:]
+ -[StreamGroupStats setLateKeyFrameAssembledCount:]
+ -[StreamGroupStats setLatePFrameAssembledCount:]
+ -[StreamGroupStats setTotalDecodedFrameCount:]
+ -[StreamGroupStats setUpMLHistograms]
+ -[StreamGroupStats totalDecodedFrameCount]
+ -[UplinkSegment processRTEvent:now:]
+ -[VCAggregator addAggregateAudioInjectorMetricsToReport:]
+ -[VCAggregator addFECStats:parameters:]
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:]
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.1
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.2
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.3
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.4
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.5
+ -[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:].cold.6
+ -[VCAggregator addFECStatsHolderKPIs:usingFECStatsHolder:]
+ -[VCAggregator addFECStatsHolderKPIs:usingFECStatsHolder:reportFrameSizeTelemetry:reportLevels:]
+ -[VCAggregator addFECStatsHolderKPIs:usingFECStatsHolder:reportFrameSizeTelemetry:reportLevels:].cold.1
+ -[VCAggregator mediaAnalyzerDataCollector]
+ -[VCAggregator processAudioInjectionInitWithPayload:currentTime:]
+ -[VCAggregator processAudioInjectionReadyWithCurrentTime:]
+ -[VCAggregator updateFECStats:usingUpdateValuesIn:]
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:]
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:].cold.1
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:].cold.2
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:].cold.3
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:].cold.4
+ -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:].cold.5
+ -[VCAggregatorAirPlay processEndpointChanged:]
+ -[VCAggregatorAnsweringMachine dealloc]
+ -[VCAggregatorAudioStream aggregatedSegmentReport:]
+ -[VCAggregatorAudioStream composeSegmentReport:]
+ -[VCAggregatorAudioStream defaultProcessEventWithCategory:type:payload:]
+ -[VCAggregatorAudioStream messageTypeForSegmentReportWithDirection:]
+ -[VCAggregatorAudioStream processEndpointChanged:]
+ -[VCAggregatorAudioStream reportSegment]
+ -[VCAggregatorAudioStream reportSegment].cold.1
+ -[VCAggregatorAudioStream reportingClientType]
+ -[VCAggregatorAudioStream reset]
+ -[VCAggregatorAudioStream startNewSegment]
+ -[VCAggregatorAudioStream supportsSegmentReporting]
+ -[VCAggregatorAudioStream supportsSessionReporting]
+ -[VCAggregatorAudioStream telephonyCallingProcessAWDMetrics:]
+ -[VCAggregatorMultiway addBoundedAlgoScoreWithTime:].cold.1
+ -[VCAggregatorMultiway audioErasureTotalTimeAlt:]
+ -[VCAggregatorMultiway boundedTalgos].cold.1
+ -[VCAggregatorMultiway lossFecHistogram]
+ -[VCAggregatorMultiway lossHistogram]
+ -[VCAggregatorMultiway lossPattern]
+ -[VCAggregatorMultiway processFecConfigData:]
+ -[VCAggregatorMultiway processNearbyStopWithPayload:]
+ -[VCAggregatorMultiway reallocateAndStartBoundedAlgoScorerWithTime:]
+ -[VCAggregatorMultiway remoteDeviceType]
+ -[VCAggregatorMultiway reportVCRCMLStats:]
+ -[VCAggregatorMultiway resetRateControlMLEnrollmentAndStatsInSegment:]
+ -[VCAggregatorMultiway resetVideoStatsForU1OrMultiwaySwitch:participantID:]
+ -[VCAggregatorMultiway setAlgosScorerVideoResolution:time:participantID:]
+ -[VCAggregatorMultiway setAlgosScorerVideoResolution:time:participantID:].cold.1
+ -[VCAggregatorMultiway setAlgosScorerVideoResolution:time:participantID:].cold.2
+ -[VCAggregatorMultiway setRemoteDeviceType:]
+ -[VCAggregatorMultiway startAlgosScorer:time:]
+ -[VCAggregatorMultiway startAlgosScorer:time:].cold.1
+ -[VCAggregatorMultiway updateClientExperiments:]
+ -[VCAggregatorMultiway updateClientExperiments:].cold.1
+ -[VCAggregatorMultiway updateClientExperiments:].cold.2
+ -[VCAggregatorMultiway updateClientExperiments:].cold.3
+ -[VCAggregatorMultiway updateRateControlMachineLearningEnrollment:]
+ -[VCAggregatorMultiway updateRateControlMachineLearningEnrollment:].cold.1
+ -[VCAggregatorMultiway updateRateControlMachineLearningRateControllerStats:]
+ -[VCAggregatorMultiway updateRateControlMachineLearningRateControllerStats:].cold.1
+ -[VCAlgosStreamingScoreAggregator algoScorerParticipantIDList]
+ -[VCCaptionsDataCollector addAggregatedLanguageDetectorMetricsToReport:]
+ -[VCCaptionsDataCollector explicitLanguageFilterEnabled]
+ -[VCCaptionsDataCollector languageDetectorEnabled]
+ -[VCCaptionsDataCollector processCaptionsConfiguration:].cold.2
+ -[VCCaptionsDataCollector processCaptionsConfiguration:].cold.3
+ -[VCCaptionsDataCollector processCaptionsEnabled:withCurrentTime:]
+ -[VCCaptionsDataCollector setExplicitLanguageFilterEnabled:]
+ -[VCCaptionsDataCollector setLanguageDetectorEnabled:]
+ -[VCHistogram convertHistogramIntoComplementaryPercentage:]
+ -[VCHistogram convertHistogramIntoComplementaryPercentage:].cold.1
+ -[VCHistogram convertHistogramIntoPercentageUsingValuesFrom:]
+ -[VCHistogram convertHistogramIntoPercentageUsingValuesFrom:].cold.1
+ -[VCMediaAnalyzerDataCollector addAggregatedMediaAnalyzerMetricsToReport:]
+ -[VCMediaAnalyzerDataCollector dealloc]
+ -[VCMediaAnalyzerDataCollector initWithDispatchQueue:]
+ -[VCMediaAnalyzerDataCollector initWithDispatchQueue:].cold.1
+ -[VCMediaAnalyzerDataCollector initWithDispatchQueue:].cold.2
+ -[VCMediaAnalyzerDataCollector processMediaAnalyzerEnabled:withCurrentTime:]
+ -[VCMediaAnalyzerDataCollector processMediaAnalyzerMetrics:]
+ -[VCMediaAnalyzerDataCollector setMediaAnalyzerEnabled:]
+ -[VCPersistentDataStore deregisterDataProducerWithType:]
+ -[VCPersistentDataStore finalizeInternal]
+ -[VCPersistentDataStore finalizeInternal].cold.1
+ -[VCPersistentDataStore initWithIdentifier:]
+ -[VCPersistentDataStore initWithIdentifier:].cold.1
+ -[VCPersistentDataStore initWithIdentifier:].cold.10
+ -[VCPersistentDataStore initWithIdentifier:].cold.11
+ -[VCPersistentDataStore initWithIdentifier:].cold.12
+ -[VCPersistentDataStore initWithIdentifier:].cold.13
+ -[VCPersistentDataStore initWithIdentifier:].cold.14
+ -[VCPersistentDataStore initWithIdentifier:].cold.2
+ -[VCPersistentDataStore initWithIdentifier:].cold.3
+ -[VCPersistentDataStore initWithIdentifier:].cold.4
+ -[VCPersistentDataStore initWithIdentifier:].cold.5
+ -[VCPersistentDataStore initWithIdentifier:].cold.6
+ -[VCPersistentDataStore initWithIdentifier:].cold.7
+ -[VCPersistentDataStore initWithIdentifier:].cold.8
+ -[VCPersistentDataStore initWithIdentifier:].cold.9
+ -[VCPersistentDataStore registerDataProducerWithType:producerCallback:]
+ -[VCPersistentDataStore runDataProducers]
+ -[VCPersistentDataStore runDataProducers].cold.1
+ -[VCRateControlMachineLearningLocalTrainingDataProducer dealloc]
+ -[VCRateControlMachineLearningLocalTrainingDataProducer initWithDataStore:recipeID:]
+ -[VCRateControlMachineLearningLocalTrainingDataProducer initWithDataStore:recipeID:].cold.1
+ -[VCRateControlMachineLearningLocalTrainingDataProducer initWithDataStore:recipeID:].cold.2
+ -[VCRateControlMachineLearningLocalTrainingDataProducer removeDatabaseFile]
+ -[VCRateControlMachineLearningLocalTrainingDataProducer runTrainingDataPostProcessing:]
+ -[VCRateControlMachineLearningLocalTrainingDataProducer runTrainingDataPostProcessing:].cold.1
+ -[VCRateControlMachineLearningLocalTrainingDataProducer runTrainingDataPostProcessing:].cold.2
+ -[VCRateControlMachineLearningLocalTrainingDataProducer runTrainingDataPostProcessing:].cold.3
+ -[VCRateControlMachineLearningLocalTrainingDataProducer setUpTrainingDataForPlugin]
+ -[VCRateControlMachineLearningLocalTrainingDataProducer setUpTrainingDataForPlugin].cold.1
+ -[VCRateControlMachineLearningLocalTrainingDataProducer shouldGenerateTrainingDataWithDatabase:]
+ -[VCRemoteDataCollectionDumpProducer coreAnalyticsCallback:fileHandle:]
+ -[VCRemoteDataCollectionDumpProducer coreAnalyticsCallback:fileHandle:].cold.1
+ -[VCRemoteDataCollectionDumpProducer coreAnalyticsCallback:fileHandle:].cold.2
+ -[VCRemoteDataCollectionDumpProducer coreAnalyticsCallback:fileHandle:].cold.3
+ -[VCRemoteDataCollectionDumpProducer createDumpAndSubmitToCoreAnalytics]
+ -[VCRemoteDataCollectionDumpProducer createDumpAndSubmitToCoreAnalytics].cold.1
+ -[VCRemoteDataCollectionDumpProducer createDumpAndSubmitToCoreAnalytics].cold.2
+ -[VCRemoteDataCollectionDumpProducer dealloc]
+ -[VCRemoteDataCollectionDumpProducer disableRemoteDataCollection]
+ -[VCRemoteDataCollectionDumpProducer initWithDataStore:]
+ -[VCRemoteDataCollectionDumpProducer initWithDataStore:].cold.1
+ -[VCRemoteDataCollectionDumpProducer newHeaderString]
+ -[VCRemoteDataCollectionDumpProducer newHeaderString].cold.1
+ -[VCRemoteDataCollectionDumpProducer removeDatabaseFile]
+ -[VCRemoteDataCollectionDumpProducer runPostProcessing:]
+ -[VCRemoteDataCollectionDumpProducer submitToCoreAnalytics:]
+ -[VCRemoteDataCollectionDumpProducer submitToCoreAnalytics:].cold.1
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:]
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.1
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.2
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.3
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.4
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.5
+ -[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:].cold.6
+ -[VCReportingBiDirectionalHistogram addValue:withDelta:]
+ -[VCReportingBiDirectionalHistogram convertHistogramIntoPercentageUsingValuesFrom:]
+ -[VCReportingBiDirectionalHistogram convertHistogramIntoPercentageUsingValuesFrom:].cold.1
+ -[VCReportingBiDirectionalHistogram dealloc]
+ -[VCReportingBiDirectionalHistogram description]
+ -[VCReportingBiDirectionalHistogram initWithType:bucketValues:]
+ -[VCReportingCommon addClientExperimentsToReport:]
+ -[VCReportingCommon backgroundReplacementStatus]
+ -[VCReportingCommon clientExperiments]
+ -[VCReportingCommon setBackgroundReplacementStatus:]
+ -[VCReportingCommon setClientExperiments:]
+ -[VCSymptomReporter reportInvalidVideoTxCaptureFrameCountWithOptionalDictionary:]
+ -[VCSymptomReporter reportUnbinnedCameraFormatSelected]
+ -[VCSymptomReporter reportUnexpectedHighRTTWithOptionalDictionary:]
+ -[VCSymptomReporter reportV1SpeechAPIEnabled]
+ -[VCVideoFECData updateWithPayload:blockFecLevels:]
+ -[VCVideoFECStatsHolder dealloc]
+ -[VCVideoFECStatsHolder fecLevelDuration]
+ -[VCVideoFECStatsHolder frameSizeCount]
+ -[VCVideoFECStatsHolder frameSizeVsDeltaBetweenParityAndLoss]
+ -[VCVideoFECStatsHolder frameSizeVsFailedCount]
+ -[VCVideoFECStatsHolder frameSizeVsParityCount]
+ -[VCVideoFECStatsHolder init]
+ -[VCVideoFECStatsHolder totalFECMediaPacketCount]
+ -[VCVideoFECStatsHolder totalFECParityPacketCount]
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table39
+ GCC_except_table48
+ GCC_except_table483
+ GCC_except_table7
+ GCC_except_table76
+ _AudioInjectorFileSize
+ _AudioInjectorLength
+ _LanguageCode
+ _MediaAnalyzerMeanProcessingTimes
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NWSAlgosScoreCombiner
+ _OBJC_CLASS_$_NWSAlgosStreamScore
+ _OBJC_CLASS_$_NWSMetricReporter
+ _OBJC_CLASS_$_VCMediaAnalyzerDataCollector
+ _OBJC_CLASS_$_VCRateControlMachineLearningLocalTrainingDataProducer
+ _OBJC_CLASS_$_VCRemoteDataCollectionDumpProducer
+ _OBJC_CLASS_$_VCReportingBiDirectionalHistogram
+ _OBJC_IVAR_$_CallSegment._callAverageAudioRxBitrate
+ _OBJC_IVAR_$_CallSegment._callAverageAudioTxBitrate
+ _OBJC_IVAR_$_CallSegment._fecStatsHolder
+ _OBJC_IVAR_$_DownlinkSegment._lateKeyFrameAssembledCount
+ _OBJC_IVAR_$_DownlinkSegment._latePFrameAssembledCount
+ _OBJC_IVAR_$_MultiwayCall._fecStatsHolder
+ _OBJC_IVAR_$_MultiwayCall._lossFecHistogram
+ _OBJC_IVAR_$_MultiwayCall._lossHistogram
+ _OBJC_IVAR_$_MultiwayCall._lossPattern
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_activeMLEngagedDuration
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_isMLEngaged
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_modelID
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_nIteration
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_recipeID
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_reportingGroup
+ _OBJC_IVAR_$_MultiwaySegment._VCRCML_targetBitrateAtTimeOfDisengagement
+ _OBJC_IVAR_$_MultiwaySegment._currentMTUDurationStartTime
+ _OBJC_IVAR_$_MultiwaySegment._currentPathMTU
+ _OBJC_IVAR_$_MultiwaySegment._fecHeaderVersion
+ _OBJC_IVAR_$_MultiwaySegment._fecStatsHolder
+ _OBJC_IVAR_$_MultiwaySegment._isFinalized
+ _OBJC_IVAR_$_MultiwaySegment._localParticipantID
+ _OBJC_IVAR_$_MultiwaySegment._maxPathMTU
+ _OBJC_IVAR_$_MultiwaySegment._minPathMTU
+ _OBJC_IVAR_$_MultiwaySegment._pathMTUArray
+ _OBJC_IVAR_$_MultiwaySegment._pathMTUCounter
+ _OBJC_IVAR_$_MultiwaySegment._pathMTUDurationArray
+ _OBJC_IVAR_$_MultiwaySegment._remoteDeviceType
+ _OBJC_IVAR_$_MultiwayStream._averageVideoRxMetadataOverheadBitrate
+ _OBJC_IVAR_$_MultiwayStream._averageVideoTxMetadataOverheadBitrate
+ _OBJC_IVAR_$_MultiwayStream._lateKeyFrameAssembledCount
+ _OBJC_IVAR_$_MultiwayStream._latePFrameAssembledCount
+ _OBJC_IVAR_$_MultiwayStream._totalAudioErasureTimeAlt
+ _OBJC_IVAR_$_RTCReportingAgent._awdAdaptor
+ _OBJC_IVAR_$_RTCReportingAgent._networkScoreUUIDString
+ _OBJC_IVAR_$_RTCReportingAgent._nwsMetricReporter
+ _OBJC_IVAR_$_RTCReportingAgent._nwsMetricReporterQueue
+ _OBJC_IVAR_$_RTCReportingAgent._remoteDataProducer
+ _OBJC_IVAR_$_RTCReportingAgent._vcrcmlTrainingDataProducer
+ _OBJC_IVAR_$_StreamGroupStats._averageMetadataRxBitrate
+ _OBJC_IVAR_$_StreamGroupStats._averageMetadataTxBitrate
+ _OBJC_IVAR_$_StreamGroupStats._isFinalized
+ _OBJC_IVAR_$_StreamGroupStats._lateKeyFrameAssembledCount
+ _OBJC_IVAR_$_StreamGroupStats._latePFrameAssembledCount
+ _OBJC_IVAR_$_StreamGroupStats._mlEnhancedPercentInputResolutions
+ _OBJC_IVAR_$_StreamGroupStats._mlEnhancedPercentOutputResolutions
+ _OBJC_IVAR_$_StreamGroupStats._totalDecodedFrameCount
+ _OBJC_IVAR_$_VCAggregator._audioInjectorCreatedTime
+ _OBJC_IVAR_$_VCAggregator._audioInjectorFileSizeHistogram
+ _OBJC_IVAR_$_VCAggregator._audioInjectorMessageLengthHistogram
+ _OBJC_IVAR_$_VCAggregator._audioInjectorSetUpTime
+ _OBJC_IVAR_$_VCAggregator._fecStatsHolder
+ _OBJC_IVAR_$_VCAggregator._mediaAnalyzerDataCollector
+ _OBJC_IVAR_$_VCAggregatorAirPlay._codecLayers
+ _OBJC_IVAR_$_VCAggregatorAirPlay._currentNumberEndpoints
+ _OBJC_IVAR_$_VCAggregatorAirPlay._maxNumberEndpoints
+ _OBJC_IVAR_$_VCAggregatorAnsweringMachine._answeringMachineUsageHistogram
+ _OBJC_IVAR_$_VCAggregatorAudioStream._currentNumberEndpoints
+ _OBJC_IVAR_$_VCAggregatorAudioStream._maxNumberEndpoints
+ _OBJC_IVAR_$_VCAggregatorAudioStream._ratType
+ _OBJC_IVAR_$_VCAggregatorFaceTime._callAverageAudioRxBitrate
+ _OBJC_IVAR_$_VCAggregatorFaceTime._callAverageAudioTxBitrate
+ _OBJC_IVAR_$_VCAggregatorFaceTime._sensitiveContentAnalysisForCamRxEnabled
+ _OBJC_IVAR_$_VCAggregatorFaceTime._sensitiveContentAnalysisForCamTxEnabled
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_activeMLEngagedDuration
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_isMLEngaged
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_modelID
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_nIteration
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_recipeID
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_reportingGroup
+ _OBJC_IVAR_$_VCAggregatorMultiway._VCRCML_targetBitrateAtTimeOfDisengagement
+ _OBJC_IVAR_$_VCAggregatorMultiway._fecHeaderVersion
+ _OBJC_IVAR_$_VCAggregatorMultiway._lossFecHistogram
+ _OBJC_IVAR_$_VCAggregatorMultiway._lossHistogram
+ _OBJC_IVAR_$_VCAggregatorMultiway._lossPattern
+ _OBJC_IVAR_$_VCAggregatorMultiway._nearbyStats
+ _OBJC_IVAR_$_VCAggregatorMultiway._remoteDeviceType
+ _OBJC_IVAR_$_VCAggregatorMultiway._sensitiveContentAnalysisForCamRxEnabled
+ _OBJC_IVAR_$_VCAggregatorMultiway._sensitiveContentAnalysisForCamTxEnabled
+ _OBJC_IVAR_$_VCCaptionsDataCollector._callTypeHistogram
+ _OBJC_IVAR_$_VCCaptionsDataCollector._captionsEnabledDuration
+ _OBJC_IVAR_$_VCCaptionsDataCollector._captionsLocale
+ _OBJC_IVAR_$_VCCaptionsDataCollector._captionsSourceLocale
+ _OBJC_IVAR_$_VCCaptionsDataCollector._captionsSpeechModel
+ _OBJC_IVAR_$_VCCaptionsDataCollector._detectedLanguageCodeHistogram
+ _OBJC_IVAR_$_VCCaptionsDataCollector._isExplicitLanguageFilterEnabled
+ _OBJC_IVAR_$_VCCaptionsDataCollector._isLanguageDetectorEnabled
+ _OBJC_IVAR_$_VCCaptionsDataCollector._lastCaptionsEnabledTime
+ _OBJC_IVAR_$_VCCaptionsDataCollector._translatedLatencyAverage
+ _OBJC_IVAR_$_VCCaptionsDataCollector._translatedUtteranceCount
+ _OBJC_IVAR_$_VCCaptionsDataCollector._utteranceCount
+ _OBJC_IVAR_$_VCMediaAnalyzerDataCollector._isMediaAnalyzerEnabled
+ _OBJC_IVAR_$_VCMediaAnalyzerDataCollector._mediaAnalyzerEnabledDuration
+ _OBJC_IVAR_$_VCMediaAnalyzerDataCollector._mediaAnalyzerLastEnabledTime
+ _OBJC_IVAR_$_VCMediaAnalyzerDataCollector._mediaAnalyzerMeanProcessingTimesHistogram
+ _OBJC_IVAR_$_VCMediaAnalyzerDataCollector._stateQueue
+ _OBJC_IVAR_$_VCPersistentDataStore._localTrainingDataProducerCallback
+ _OBJC_IVAR_$_VCPersistentDataStore._numberOfRegisteredProducers
+ _OBJC_IVAR_$_VCPersistentDataStore._remoteDataCollectionProducerCallback
+ _OBJC_IVAR_$_VCRateControlMachineLearningLocalTrainingDataProducer._database
+ _OBJC_IVAR_$_VCRateControlMachineLearningLocalTrainingDataProducer._databasePath
+ _OBJC_IVAR_$_VCRateControlMachineLearningLocalTrainingDataProducer._directoryPath
+ _OBJC_IVAR_$_VCRateControlMachineLearningLocalTrainingDataProducer._recipeID
+ _OBJC_IVAR_$_VCRemoteDataCollectionDumpProducer._dataStore
+ _OBJC_IVAR_$_VCRemoteDataCollectionDumpProducer._database
+ _OBJC_IVAR_$_VCRemoteDataCollectionDumpProducer._databasePath
+ _OBJC_IVAR_$_VCReportingBiDirectionalHistogram._signedBuckets
+ _OBJC_IVAR_$_VCReportingCommon._backgroundReplacementStatus
+ _OBJC_IVAR_$_VCReportingCommon._clientExperiments
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._fecLevelDuration
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._frameSizeCount
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._frameSizeVsDeltaBetweenParityAndLoss
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._frameSizeVsFailedCount
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._frameSizeVsParityCount
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._totalFECMediaPacketCount
+ _OBJC_IVAR_$_VCVideoFECStatsHolder._totalFECParityPacketCount
+ _OBJC_METACLASS_$_VCMediaAnalyzerDataCollector
+ _OBJC_METACLASS_$_VCRateControlMachineLearningLocalTrainingDataProducer
+ _OBJC_METACLASS_$_VCRemoteDataCollectionDumpProducer
+ _OBJC_METACLASS_$_VCReportingBiDirectionalHistogram
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _VCAggregatorUtils_GetSizeForVideoResolution
+ _VCAggregatorUtils_GetSizeForVideoResolution.cold.1
+ _VCAggregatorUtils_GetVideoResolutionForDimensions
+ _VCPersistentDataStore_Finalize
+ __OBJC_$_INSTANCE_METHODS_VCMediaAnalyzerDataCollector
+ __OBJC_$_INSTANCE_METHODS_VCRateControlMachineLearningLocalTrainingDataProducer
+ __OBJC_$_INSTANCE_METHODS_VCRemoteDataCollectionDumpProducer
+ __OBJC_$_INSTANCE_METHODS_VCReportingBiDirectionalHistogram
+ __OBJC_$_INSTANCE_VARIABLES_VCMediaAnalyzerDataCollector
+ __OBJC_$_INSTANCE_VARIABLES_VCRateControlMachineLearningLocalTrainingDataProducer
+ __OBJC_$_INSTANCE_VARIABLES_VCRemoteDataCollectionDumpProducer
+ __OBJC_$_INSTANCE_VARIABLES_VCReportingBiDirectionalHistogram
+ __OBJC_CLASS_RO_$_VCMediaAnalyzerDataCollector
+ __OBJC_CLASS_RO_$_VCRateControlMachineLearningLocalTrainingDataProducer
+ __OBJC_CLASS_RO_$_VCRemoteDataCollectionDumpProducer
+ __OBJC_CLASS_RO_$_VCReportingBiDirectionalHistogram
+ __OBJC_METACLASS_RO_$_VCMediaAnalyzerDataCollector
+ __OBJC_METACLASS_RO_$_VCRateControlMachineLearningLocalTrainingDataProducer
+ __OBJC_METACLASS_RO_$_VCRemoteDataCollectionDumpProducer
+ __OBJC_METACLASS_RO_$_VCReportingBiDirectionalHistogram
+ __VCPersistentDataStore_BindAndExecute.cold.88
+ __VCPersistentDataStore_BindAndExecute.cold.89
+ __VCPersistentDataStore_BindAndExecute.cold.90
+ __VCRemoteDataCollectionDumpProducer_WriteToCSVCallback
+ __VCRemoteDataCollectionDumpProducer_WriteToCSVCallbackColumns
+ ___36-[RTCReportingAgent setUpAWDAdapter]_block_invoke
+ ___36-[RTCReportingAgent setUpAWDAdapter]_block_invoke.cold.1
+ ___42-[RTCReportingAgent sharedAWDAdaptorClass]_block_invoke
+ ___42-[RTCReportingAgent sharedAWDAdaptorClass]_block_invoke.cold.1
+ ___42-[RTCReportingAgent sharedAWDAdaptorClass]_block_invoke.cold.2
+ ___51-[VCAggregatorAudioStream aggregatedSegmentReport:]_block_invoke
+ ___56-[VCRemoteDataCollectionDumpProducer initWithDataStore:]_block_invoke
+ ___60-[VCRemoteDataCollectionDumpProducer submitToCoreAnalytics:]_block_invoke
+ ___62-[VCAggregatorFaceTime processEventWithCategory:type:payload:]_block_invoke_7
+ ___62-[VCAggregatorFaceTime processEventWithCategory:type:payload:]_block_invoke_8
+ ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.227
+ ___84-[VCRateControlMachineLearningLocalTrainingDataProducer initWithDataStore:recipeID:]_block_invoke
+ ___VCPersistentDataStore_DumpMessage_block_invoke.cold.1
+ ___VCPersistentDataStore_DumpMessage_block_invoke.cold.2
+ ___VCPersistentDataStore_DumpMessage_block_invoke.cold.3
+ ___VCPersistentDataStore_DumpMessage_block_invoke.cold.4
+ ___VCPersistentDataStore_Finalize_block_invoke
+ ___block_descriptor_208_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32o_e18_v16?0"NSString"8ls32l8
+ ___block_literal_global.224
+ ___block_literal_global.514
+ ___block_literal_global.523
+ ___block_literal_global.607
+ ___reportingSetUserInfo_block_invoke.519
+ ___reportingSetUserInfo_block_invoke.520
+ ___reportingSetUserInfo_block_invoke.520.cold.1
+ _answeringMachineUsage
+ _captionsCallType
+ _captionsSpeechModel
+ _fecLevelBucketRanges
+ _fecframeSizeBucketRanges
+ _objc_msgSend$addAggregateAudioInjectorMetricsToReport:
+ _objc_msgSend$addAggregatedLanguageDetectorMetricsToReport:
+ _objc_msgSend$addAggregatedMediaAnalyzerMetricsToReport:
+ _objc_msgSend$addClientExperimentsToReport:
+ _objc_msgSend$addFECStats:parameters:
+ _objc_msgSend$addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:
+ _objc_msgSend$addFECStatsHolderKPIs:usingFECStatsHolder:
+ _objc_msgSend$addFECStatsHolderKPIs:usingFECStatsHolder:reportFrameSizeTelemetry:reportLevels:
+ _objc_msgSend$addValue:withDelta:
+ _objc_msgSend$algoScorerParticipantIDList
+ _objc_msgSend$appendPathMTU:delta:
+ _objc_msgSend$audioErasureTotalTimeAlt
+ _objc_msgSend$audioErasureTotalTimeAlt:
+ _objc_msgSend$averageMetadataRxBitrate
+ _objc_msgSend$averageMetadataTxBitrate
+ _objc_msgSend$averageVideoRxMetadataOverheadBitrate
+ _objc_msgSend$averageVideoTxMetadataOverheadBitrate
+ _objc_msgSend$callAverageAudioRxBitrate
+ _objc_msgSend$callAverageAudioTxBitrate
+ _objc_msgSend$classNamed:
+ _objc_msgSend$clientExperiments
+ _objc_msgSend$convertHistogramIntoComplementaryPercentage:
+ _objc_msgSend$convertHistogramIntoPercentageUsingValuesFrom:
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$createDefaultAttributeDirectoryIfNeeded:
+ _objc_msgSend$createDumpAndSubmitToCoreAnalytics
+ _objc_msgSend$defaultProcessEventWithCategory:type:payload:
+ _objc_msgSend$deregisterDataProducerWithType:
+ _objc_msgSend$disableRemoteDataCollection
+ _objc_msgSend$fecLevelDuration
+ _objc_msgSend$fecStatsHolder
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$finalizeInternal
+ _objc_msgSend$finalizePathMTUForTime:
+ _objc_msgSend$finalizeStats
+ _objc_msgSend$frameSizeCount
+ _objc_msgSend$frameSizeVsDeltaBetweenParityAndLoss
+ _objc_msgSend$frameSizeVsFailedCount
+ _objc_msgSend$frameSizeVsParityCount
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithDataStore:
+ _objc_msgSend$initWithDataStore:recipeID:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithPath:
+ _objc_msgSend$isLoaded
+ _objc_msgSend$lateKeyFrameAssembledCount
+ _objc_msgSend$latePFrameAssembledCount
+ _objc_msgSend$load
+ _objc_msgSend$mediaAnalyzerDataCollector
+ _objc_msgSend$mlEnhancedPercentInputResolutions
+ _objc_msgSend$mlEnhancedPercentOutputResolutions
+ _objc_msgSend$newHeaderString
+ _objc_msgSend$now
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$processAudioInjectionInitWithPayload:currentTime:
+ _objc_msgSend$processAudioInjectionReadyWithCurrentTime:
+ _objc_msgSend$processCaptionsEnabled:withCurrentTime:
+ _objc_msgSend$processEndpointChanged:
+ _objc_msgSend$processFecConfigData:
+ _objc_msgSend$processFrameSizeBasedFECTelemetry:statsHolder:direction:
+ _objc_msgSend$processMLStreamData:
+ _objc_msgSend$processMediaAnalyzerEnabled:withCurrentTime:
+ _objc_msgSend$processMediaAnalyzerMetrics:
+ _objc_msgSend$processNearbyStopWithPayload:
+ _objc_msgSend$processPathMTU:now:
+ _objc_msgSend$processRTEvent:now:
+ _objc_msgSend$processRTEventCommon:now:
+ _objc_msgSend$reallocateAndStartBoundedAlgoScorerWithTime:
+ _objc_msgSend$registerDataProducerWithType:producerCallback:
+ _objc_msgSend$remoteDataProducer
+ _objc_msgSend$replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
+ _objc_msgSend$reportInvalidVideoTxCaptureFrameCountWithOptionalDictionary:
+ _objc_msgSend$reportSegment
+ _objc_msgSend$reportUnbinnedCameraFormatSelected
+ _objc_msgSend$reportUnexpectedHighRTTWithOptionalDictionary:
+ _objc_msgSend$reportV1SpeechAPIEnabled
+ _objc_msgSend$reportVCRCMLStats:
+ _objc_msgSend$reportingClientType
+ _objc_msgSend$resetMLStats
+ _objc_msgSend$resetRateControlMLEnrollmentAndStatsInSegment:
+ _objc_msgSend$resetVideoStatsForU1OrMultiwaySwitch:participantID:
+ _objc_msgSend$runDataProducers
+ _objc_msgSend$runPostProcessing:
+ _objc_msgSend$runTrainingDataPostProcessing:
+ _objc_msgSend$sendMessageToAWDAdaptorWithCategory:type:payload:
+ _objc_msgSend$sendMessageWithMethodPrivate:respCode:dict:
+ _objc_msgSend$sendNetworkScoreDictionary:networkScoreType:
+ _objc_msgSend$sendStreamMetrics:onQueue:
+ _objc_msgSend$setAlgosScorerVideoResolution:time:participantID:
+ _objc_msgSend$setAverageMetadataRxBitrate:
+ _objc_msgSend$setAverageMetadataTxBitrate:
+ _objc_msgSend$setCallAverageAudioRxBitrate:
+ _objc_msgSend$setCallAverageAudioTxBitrate:
+ _objc_msgSend$setClientExperiments:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setExplicitLanguageFilterEnabled:
+ _objc_msgSend$setFecHeaderVersion:
+ _objc_msgSend$setLanguageDetectorEnabled:
+ _objc_msgSend$setLateKeyFrameAssembledCount:
+ _objc_msgSend$setLatePFrameAssembledCount:
+ _objc_msgSend$setMediaAnalyzerEnabled:
+ _objc_msgSend$setTotalDecodedFrameCount:
+ _objc_msgSend$setUpAWDAdapter
+ _objc_msgSend$setUpMLHistograms
+ _objc_msgSend$setUpTrainingDataForPlugin
+ _objc_msgSend$setVCRCML_activeMLEngagedDuration:
+ _objc_msgSend$setVCRCML_isMLEngaged:
+ _objc_msgSend$setVCRCML_modelID:
+ _objc_msgSend$setVCRCML_nIteration:
+ _objc_msgSend$setVCRCML_recipeID:
+ _objc_msgSend$setVCRCML_reportingGroup:
+ _objc_msgSend$setVCRCML_targetBitrateAtTimeOfDisengagement:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sharedAWDAdaptorClass
+ _objc_msgSend$shouldGenerateTrainingDataWithDatabase:
+ _objc_msgSend$startAlgosScorer:time:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$strong
+ _objc_msgSend$submitToCoreAnalytics:
+ _objc_msgSend$supportsSegmentReporting
+ _objc_msgSend$supportsSessionReporting
+ _objc_msgSend$telephonyCallingProcessAWDMetrics:
+ _objc_msgSend$totalDecodedFrameCount
+ _objc_msgSend$totalFECMediaPacketCount
+ _objc_msgSend$totalFECParityPacketCount
+ _objc_msgSend$updateClientExperiments:
+ _objc_msgSend$updateFECStats:usingUpdateValuesIn:
+ _objc_msgSend$updateRateControlMachineLearningEnrollment:
+ _objc_msgSend$updateRateControlMachineLearningRateControllerStats:
+ _objc_msgSend$updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:
+ _objc_msgSend$updateWithPayload:blockFecLevels:
+ _objc_msgSend$weakObjectHolderWithObject:
+ _objc_msgSend$writeToFile:atomically:
+ _objc_retain_x20
+ _objc_retain_x21
+ _sRTCReportingCompositorServicesClientName
+ _sRTCReportingImmersiveMediaClientName
+ _sRTCReportingThirdPartyScreenSharingClientName
+ _sRTCReportingThirdPartyScreenSharingServiceName
+ _sharedAWDAdaptorClass.awdAdaptorClass
+ _sharedAWDAdaptorClass.gksPerformanceClientBundle
+ _sharedAWDAdaptorClass.onceToken
+ _sqlite3_bind_text
+ _sqlite3_column_int
+ _sqlite3_column_text
+ _videoResolutions
- +[VCAggregatorUtils sizeForVideoResolution:].cold.1
- +[VCDiskUtils createDefaultDirectoryIfNeeded:]
- +[VCDiskUtils createDefaultDirectoryIfNeeded:].cold.1
- +[VCDiskUtils createDefaultDirectoryIfNeeded:].cold.2
- +[VCDiskUtils createDefaultDirectoryIfNeeded:].cold.3
- +[VCDiskUtils createDefaultDirectoryIfNeeded:].cold.4
- -[CallSegment backgroundReplacementStatus]
- -[CallSegment fecStatsDict]
- -[CallSegment setBackgroundReplacementStatus:]
- -[DownlinkSegment localParticipantID]
- -[DownlinkSegment processRTEvent:]
- -[DownlinkSegment setLocalParticipantID:]
- -[MultiwaySegment backgroundReplacementStatus]
- -[MultiwaySegment fecStatsDict]
- -[MultiwaySegment processRTEventCommon:]
- -[MultiwaySegment setBackgroundReplacementStatus:]
- -[UplinkSegment processRTEvent:]
- -[VCAggregator addAggregatedCannedAudioMetricsToReport:]
- -[VCAggregator backgroundReplacementStatus]
- -[VCAggregator processCannedAudioInjectionInitWithPayload:currentTime:]
- -[VCAggregator processCannedAudioInjectionReadyWithCurrentTime:]
- -[VCAggregator segmentFECReport:parameters:]
- -[VCAggregator segmentFECReport:parameters:].cold.1
- -[VCAggregator segmentFECReport:parameters:].cold.2
- -[VCAggregator segmentFECReport:parameters:].cold.3
- -[VCAggregator segmentFECReport:parameters:].cold.4
- -[VCAggregator segmentFECReport:parameters:].cold.5
- -[VCAggregator segmentFECReport:parameters:].cold.6
- -[VCAggregator setBackgroundReplacementStatus:]
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:]
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:].cold.1
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:].cold.2
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:].cold.3
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:].cold.4
- -[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:].cold.5
- -[VCAggregatorAirPlay sessionFECReport]
- -[VCAggregatorAudioStream remoteMicProcessEventWithCategory:type:payload:]
- -[VCAggregatorAudioStream screenSharingProcessEventWithCategory:payload:]
- -[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:]
- -[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:].cold.1
- -[VCAggregatorMultiway processSliceStatusABCSymptoms:currentSegmentName:]
- -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]
- -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:].cold.1
- -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]
- -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:].cold.1
- -[VCAggregatorMultiway reallocateBoundedAlgoScorerWithTime:]
- -[VCAggregatorMultiway startBoundedAlgoScorerWithTime:]
- -[VCAggregatorSecondDisplay sessionFECReport]
- -[VCPersistentDataStore coreAnalyticsCallback:fileHandle:]
- -[VCPersistentDataStore coreAnalyticsCallback:fileHandle:].cold.1
- -[VCPersistentDataStore coreAnalyticsCallback:fileHandle:].cold.2
- -[VCPersistentDataStore coreAnalyticsCallback:fileHandle:].cold.3
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:]
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.1
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.10
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.11
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.12
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.13
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.14
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.2
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.3
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.4
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.5
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.6
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.7
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.8
- -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.9
- -[VCPersistentDataStore invalidateInternalWithReason:]
- -[VCPersistentDataStore invalidateInternalWithReason:].cold.1
- -[VCPersistentDataStore submitToCoreAnalytics]
- -[VCPersistentDataStore submitToCoreAnalytics].cold.1
- -[VCPersistentDataStore submitToCoreAnalytics].cold.2
- -[VCPersistentDataStore submitToCoreAnalytics].cold.3
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:]
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:].cold.1
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:].cold.2
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:].cold.3
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:].cold.4
- -[VCPersistentDataStore writeVCRCMLDumpToCSVPath:].cold.5
- -[VCSymptomReporter reportConnectionSliceStatus:]
- -[VCSymptomReporter reportUnexpectedHighRTT]
- -[VCVideoFECStatsHolder setCompleteFECFrameCount:]
- -[VCVideoFECStatsHolder setFailedFECFrameCount:]
- -[VCVideoFECStatsHolder setTotalFECDataByteCount:]
- -[VCVideoFECStatsHolder setTotalFECFrameCount:]
- -[VCVideoFECStatsHolder setTotalFECParityByteCount:]
- -[VCVideoFECStatsHolder setUnfixableFECFrameCount:]
- GCC_except_table114
- GCC_except_table116
- GCC_except_table218
- GCC_except_table219
- GCC_except_table221
- GCC_except_table227
- GCC_except_table34
- GCC_except_table45
- GCC_except_table481
- GCC_except_table74
- _CFStringCreateCopy
- _CannedAudioInjectorFileSize
- _CannedAudioInjectorLength
- _OBJC_CLASS_$_AlgosScoreCombiner
- _OBJC_CLASS_$_AlgosStreamScore
- _OBJC_IVAR_$_CallSegment._fecStatsDict
- _OBJC_IVAR_$_DownlinkSegment._localParticipantID
- _OBJC_IVAR_$_MultiwaySegment._fecStatsDict
- _OBJC_IVAR_$_VCAggregator._cannedAudioInjectorCreatedTime
- _OBJC_IVAR_$_VCAggregator._cannedAudioInjectorFileSizeHistogram
- _OBJC_IVAR_$_VCAggregator._cannedAudioInjectorMessageLengthHistogram
- _OBJC_IVAR_$_VCAggregator._cannedAudioInjectorSetUpTime
- _OBJC_IVAR_$_VCAggregatorAirPlay._fecStatsDict
- _OBJC_IVAR_$_VCAggregatorSecondDisplay._fecStatsDict
- _OBJC_IVAR_$_VCPersistentDataStore._isDataCollectionEnabled
- _VCPersistentDataStore_Invalidate
- __VCPersistentDataStore_WriteToCSVCallback
- __VCPersistentDataStore_WriteToCSVCallbackColumns
- ___46-[VCPersistentDataStore submitToCoreAnalytics]_block_invoke
- ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.164
- ___VCPersistentDataStore_Invalidate_block_invoke
- ___block_descriptor_184_e8_32o_e5_v8?0ls32l8
- ___block_literal_global.430
- ___block_literal_global.440
- ___block_literal_global.524
- ___reportingSetUserInfo_block_invoke.436
- ___reportingSetUserInfo_block_invoke.437
- ___reportingSetUserInfo_block_invoke.437.cold.1
- _objc_msgSend$addAggregatedCannedAudioMetricsToReport:
- _objc_msgSend$checkSliceStatus:hasValuesOnlyForStatus:
- _objc_msgSend$createDefaultDirectoryIfNeeded:
- _objc_msgSend$fecStatsDict
- _objc_msgSend$initWithIdentifier:dataCollectionEnabled:
- _objc_msgSend$invalidateInternalWithReason:
- _objc_msgSend$processCannedAudioInjectionInitWithPayload:currentTime:
- _objc_msgSend$processCannedAudioInjectionReadyWithCurrentTime:
- _objc_msgSend$processRTEventCommon:
- _objc_msgSend$processSliceStatusABCSymptoms:currentSegmentName:
- _objc_msgSend$processSliceStatusFailedABCSymptom:
- _objc_msgSend$processSliceStatusNotReceivedABCSymptom:
- _objc_msgSend$reallocateBoundedAlgoScorerWithTime:
- _objc_msgSend$remoteMicProcessEventWithCategory:type:payload:
- _objc_msgSend$reportConnectionSliceStatus:
- _objc_msgSend$reportUnexpectedHighRTT
- _objc_msgSend$screenSharingProcessEventWithCategory:payload:
- _objc_msgSend$segmentFECReport:parameters:
- _objc_msgSend$sessionFECReport
- _objc_msgSend$setCompleteFECFrameCount:
- _objc_msgSend$setDataStore:
- _objc_msgSend$setFailedFECFrameCount:
- _objc_msgSend$setTotalFECDataByteCount:
- _objc_msgSend$setTotalFECFrameCount:
- _objc_msgSend$setTotalFECParityByteCount:
- _objc_msgSend$setUnfixableFECFrameCount:
- _objc_msgSend$startBoundedAlgoScorerWithTime:
- _objc_msgSend$submitToCoreAnalytics
- _objc_msgSend$updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:
- _receivedVideoTierDuration
CStrings:
+ " [%s] %s:%d %@(%p) Failed to Save JSON file with training metadata at trainingMetadataPath=%@"
+ " [%s] %s:%d %@(%p) Failed to create duplicate database with databasePath=%@, error=%@"
+ " [%s] %s:%d %@(%p) Failed to create header string for remote dump"
+ " [%s] %s:%d %@(%p) Failed to create valid local training data directory directoryPath=%@ "
+ " [%s] %s:%d %@(%p) Failed to delete RemoteDataCollectionDumpProducer database with databasePath=%@, error=%@"
+ " [%s] %s:%d %@(%p) Failed to find bucket for call type=%hhu"
+ " [%s] %s:%d %@(%p) Failed to find bucket for speech model=%hhu"
+ " [%s] %s:%d %@(%p) Failed to initialize SQLite database"
+ " [%s] %s:%d %@(%p) Failed to replace database at path=%@, error=%@"
+ " [%s] %s:%d %@(%p) Failed to save csv with filePath=%@, core analytics submission cancelled"
+ " [%s] %s:%d %@(%p) ML array size does not match histogram size! inputResolutionArraySize=%d outputResolutionArraySize=%d VCReportingVideoResolutionCount=%d"
+ " [%s] %s:%d %@(%p) No registered producers"
+ " [%s] %s:%d %@(%p) SQLite Error: could not read metadata status=%d"
+ " [%s] %s:%d %@(%p) Session data is too small or too big to be used for training"
+ " [%s] %s:%d %@(%p) Training table has numberOfRows=%d, requiredRange=[%d, %d]"
+ " [%s] %s:%d Failed to Save JSON file with training metadata at trainingMetadataPath=%@"
+ " [%s] %s:%d Failed to create duplicate database with databasePath=%@, error=%@"
+ " [%s] %s:%d Failed to create header string for remote dump"
+ " [%s] %s:%d Failed to create valid local training data directory directoryPath=%@ "
+ " [%s] %s:%d Failed to delete RemoteDataCollectionDumpProducer database with databasePath=%@, error=%@"
+ " [%s] %s:%d Failed to find bucket for call type=%hhu"
+ " [%s] %s:%d Failed to find bucket for speech model=%hhu"
+ " [%s] %s:%d Failed to initialize SQLite database"
+ " [%s] %s:%d Failed to replace database at path=%@, error=%@"
+ " [%s] %s:%d Failed to report audio stream segment: Invalid stream direction"
+ " [%s] %s:%d Failed to save csv with filePath=%@, core analytics submission cancelled"
+ " [%s] %s:%d Invalid AlgosStreamingScorer"
+ " [%s] %s:%d ML array size does not match histogram size! inputResolutionArraySize=%d outputResolutionArraySize=%d VCReportingVideoResolutionCount=%d"
+ " [%s] %s:%d No registered producers"
+ " [%s] %s:%d SQLite Error: could not bind data=%s with return code=%d"
+ " [%s] %s:%d SQLite Error: could not read metadata status=%d"
+ " [%s] %s:%d Session data is too small or too big to be used for training"
+ " [%s] %s:%d SymptomReporter: reporting symptom InvalidVideoTxCaptureFrameCount for session=%u (frame count=%d)"
+ " [%s] %s:%d SymptomReporter: reporting symptom UnexpectedHighRTT with remote participant for session %u"
+ " [%s] %s:%d SymptomReporter: reporting symptom V1SpeechAPIEnabled for session=%u"
+ " [%s] %s:%d SymptomReporter: reporting symptom on UnbinnedCameraFormatSelected for callID=%u"
+ " [%s] %s:%d The number of buckets are not same in both histograms"
+ " [%s] %s:%d Training table has numberOfRows=%d, requiredRange=[%d, %d]"
+ " [%s] %s:%d VCPersistentDataStore already finalized!"
+ " [%s] %s:%d Video resolution not set for participantID=%@"
+ " [%s] %s:%d algosScorerBoundedScoreList length exceeded talgosBounded=%f"
+ " [%s] %s:%d algosScorerBoundedScoreList must not be empty"
+ "%@%d"
+ "%@/%@_%@%s"
+ "%@/%s"
+ "%@_%@_%d"
+ "%s fileSchemaVersion=%d conversationID=%s participantID=%s deviceClass=%d\n"
+ "%s fileSchemaVersion=%d conversationID=%s participantID=%s deviceClass=%d internalTesting=%d\n"
+ "+[VCDiskUtils createDefaultAttributeDirectoryIfNeeded:]"
+ ",%@"
+ "-[RTCReportingAgent sendMessageToAWDAdaptorWithCategory:type:payload:]"
+ "-[RTCReportingAgent sendNetworkScoreDictionary:networkScoreType:]"
+ "-[RTCReportingAgent setUpAWDAdapter]_block_invoke"
+ "-[RTCReportingAgent sharedAWDAdaptorClass]_block_invoke"
+ "-[StreamGroupStats processMLStreamData:]"
+ "-[VCAggregator addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:]"
+ "-[VCAggregator addFECStatsHolderKPIs:usingFECStatsHolder:reportFrameSizeTelemetry:reportLevels:]"
+ "-[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:]"
+ "-[VCAggregatorAudioStream composeSegmentReport:]"
+ "-[VCAggregatorAudioStream reportSegment]"
+ "-[VCAggregatorMultiway addBoundedAlgoScoreWithTime:]"
+ "-[VCAggregatorMultiway boundedTalgos]"
+ "-[VCAggregatorMultiway setAlgosScorerVideoResolution:time:participantID:]"
+ "-[VCAggregatorMultiway startAlgosScorer:time:]"
+ "-[VCAggregatorMultiway updateClientExperiments:]"
+ "-[VCAggregatorMultiway updateRateControlMachineLearningEnrollment:]"
+ "-[VCAggregatorMultiway updateRateControlMachineLearningRateControllerStats:]"
+ "-[VCHistogram convertHistogramIntoComplementaryPercentage:]"
+ "-[VCHistogram convertHistogramIntoPercentageUsingValuesFrom:]"
+ "-[VCMediaAnalyzerDataCollector initWithDispatchQueue:]"
+ "-[VCPersistentDataStore finalizeInternal]"
+ "-[VCPersistentDataStore initWithIdentifier:]"
+ "-[VCPersistentDataStore runDataProducers]"
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer initWithDataStore:recipeID:]"
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer removeDatabaseFile]"
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer runTrainingDataPostProcessing:]"
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer setUpTrainingDataForPlugin]"
+ "-[VCRateControlMachineLearningLocalTrainingDataProducer shouldGenerateTrainingDataWithDatabase:]"
+ "-[VCRemoteDataCollectionDumpProducer coreAnalyticsCallback:fileHandle:]"
+ "-[VCRemoteDataCollectionDumpProducer createDumpAndSubmitToCoreAnalytics]"
+ "-[VCRemoteDataCollectionDumpProducer initWithDataStore:]"
+ "-[VCRemoteDataCollectionDumpProducer newHeaderString]"
+ "-[VCRemoteDataCollectionDumpProducer removeDatabaseFile]"
+ "-[VCRemoteDataCollectionDumpProducer runPostProcessing:]"
+ "-[VCRemoteDataCollectionDumpProducer submitToCoreAnalytics:]"
+ "-[VCRemoteDataCollectionDumpProducer writeVCRCMLDumpToCSVPath:]"
+ "-[VCReportingBiDirectionalHistogram convertHistogramIntoPercentageUsingValuesFrom:]"
+ "-[VCSymptomReporter reportInvalidVideoTxCaptureFrameCountWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportUnbinnedCameraFormatSelected]"
+ "-[VCSymptomReporter reportUnexpectedHighRTTWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportV1SpeechAPIEnabled]"
+ "/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework"
+ "@\"NSMutableString\""
+ "@\"NWSAlgosStreamScore\""
+ "@\"NWSMetricReporter\""
+ "@\"VCMediaAnalyzerDataCollector\""
+ "@\"VCRateControlMachineLearningLocalTrainingDataProducer\""
+ "@\"VCRemoteDataCollectionDumpProducer\""
+ "@\"VCReportingBiDirectionalHistogram\""
+ "@\"VCVideoFECStatsHolder\""
+ "@160@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}{tagVCPersistentDataStoreConfiguration=BB^{__CFString}}}16"
+ "AAMU"
+ "ACCallType"
+ "ACExplicitLanguageFilterEnabled"
+ "ACLC"
+ "ACLocale"
+ "ACSourceLocale"
+ "ACSpeechModel"
+ "ACTranslatedLatencyAverage"
+ "ACTranslatedUtteranceCount"
+ "ACUtteranceCount"
+ "AMCU"
+ "ANBDUR"
+ "ANBMPC"
+ "ANBSC"
+ "AVConference_AlgosScore"
+ "AWDAdaptor"
+ "AudioStream: segmentReport"
+ "B24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}{tagVCPersistentDataStoreConfiguration=BB^{__CFString}}}16"
+ "B24@0:8^{sqlite3=}16"
+ "CDCL"
+ "CREATE TABLE IF NOT EXISTS Feedback ( state INT, timestamp DOUBLE, arrivalTime DOUBLE, targetBitrate INT, bitrate INT, basebandFlush INT, rateControlTime FLOAT(24,4), owrd FLOAT(24,4), nowrd FLOAT(24,4), nowrda FLOAT(24,4), roundTripTime FLOAT(24,4), roundTripTimeAverage FLOAT(24,4), roundTripTimeMinEnvelope FLOAT(24,4), audioPacketLossRate FLOAT(24,4), audioPacketLossRateShort FLOAT(24,4), videoPacketLossRate FLOAT(24,4), ecnCERatio FLOAT(24,4), bandwidthEstimate INT, trainingValue FLOAT(24, 4), trainingAction INT, trainingActionLogProbability FLOAT(24, 4) );"
+ "CREATE TABLE IF NOT EXISTS Metadata ( conversationID TEXT, participantID TEXT, deviceClass INT );"
+ "CREATE TABLE VCRCMLoutput  ( state INT, timestamp DOUBLE, arrivalTime DOUBLE, targetBitrate INT, bitrate INT, basebandFlush INT, rateControlTime FLOAT(24,4), owrd FLOAT(24,4), nowrd FLOAT(24,4), nowrda FLOAT(24,4), roundTripTime FLOAT(24,4), roundTripTimeAverage FLOAT(24,4), roundTripTimeMinEnvelope FLOAT(24,4), audioPacketLossRate FLOAT(24,4), audioPacketLossRateShort FLOAT(24,4), videoPacketLossRate FLOAT(24,4), ecnCERatio FLOAT(24,4), bandwidthEstimate INT, nwConnectionTimestamp BIGINT, frequencyBand INT, intermittentState INT, estimatedIntermittentPeriod INT, singleOutagePeriod INT, btCoex INT, radioCoex INT, qualityScoreDelayRx INT, qualityScoreDelayTx INT, qualityScoreLossRx INT, qualityScoreLossTx INT, qualityScoreChannel INT, offChannelTimeRatio FLOAT, wlanDutyCycle INT, observedTxBitrateBE INT, observedTxBitrateBK INT, observedTxBitrateVI INT, observedTxBitrateVO INT, observedTxBitrateLLW0 INT, observedTxBitrateLLW1 INT, radioTechnology INT, flushableQueueDepth INT, unflushableQueueDepth INT, averageBitrate INT, averageBitrateShort INT, averageBitrateLong INT, txBitrate INT, averageQueueDepth DOUBLE, expectedQueuingDelay DOUBLE, bdcd DOUBLE, normalizedBDCD DOUBLE, normalizedDelay DOUBLE, bytesInFlight INT, bytesInFlightRollingAverage INT, mode INT, localRAT INT, remoteRAT INT, minTargetBitrate INT, maxTargetBitrate INT, algorithmVersion INT, trainingValue FLOAT(24, 4), trainingAction INT, trainingActionLogProbability FLOAT(24, 4) ); "
+ "CREATE TABLE VCRCMLoutput  ( timestamp DOUBLE, targetBitrate INT, bitrate INT, rateControlTime FLOAT(24,4), owrd FLOAT(24,4), nowrd FLOAT(24,4), roundTripTime FLOAT(24,4), audioPacketLossRate FLOAT(24,4), videoPacketLossRate FLOAT(24,4), bandwidthEstimate INT, averageBitrate INT, expectedQueuingDelay DOUBLE, bytesInFlight INT, mode INT, localRAT INT, remoteRAT INT, maxTargetBitrate INT, trainingValue FLOAT(24, 4), trainingAction INT, trainingActionLogProbability FLOAT(24, 4) ); "
+ "CodecLayers"
+ "CompositorServices"
+ "DIAFELD"
+ "DecOutMLEnhancedHistInputRes"
+ "DecOutMLEnhancedHistOutputRes"
+ "ENDPTC"
+ "FECFDF"
+ "FECFDPL"
+ "FECFP"
+ "FECHDRVER"
+ "FECLVL"
+ "FECMPR"
+ "FECPPR"
+ "FecHeaderVer"
+ "INSERT INTO Feedback (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, rateControlTime, owrd, nowrd, nowrda, roundTripTime, roundTripTimeAverage, roundTripTimeMinEnvelope, audioPacketLossRate, audioPacketLossRateShort, videoPacketLossRate, ecnCERatio, bandwidthEstimate, trainingValue, trainingAction, trainingActionLogProbability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
+ "INSERT INTO Metadata (conversationID, participantID, deviceClass) VALUES (?, ?, ?);"
+ "INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, rateControlTime, owrd, nowrd, nowrda, roundTripTime, roundTripTimeAverage, roundTripTimeMinEnvelope, audioPacketLossRate, audioPacketLossRateShort, videoPacketLossRate, ecnCERatio, bandwidthEstimate, trainingValue, trainingAction, trainingActionLogProbability) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, ROUND(rateControlTime,3), ROUND(owrd, 3), ROUND(nowrd,3), ROUND(nowrda,3), ROUND(roundTripTime,3), ROUND(roundTripTimeAverage,3), ROUND(roundTripTimeMinEnvelope,3), ROUND(audioPacketLossRate,3), ROUND(audioPacketLossRateShort,3), ROUND(videoPacketLossRate,3), ROUND(ecnCERatio,3), bandwidthEstimate, ROUND(trainingValue,3), trainingAction, ROUND(trainingActionLogProbability,3) FROM Feedback; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, nwConnectionTimestamp, frequencyBand, intermittentState, estimatedIntermittentPeriod, singleOutagePeriod, btCoex, radioCoex, qualityScoreDelayRx, qualityScoreDelayTx, qualityScoreLossRx, qualityScoreLossTx, qualityScoreChannel, offChannelTimeRatio, wlanDutyCycle, observedTxBitrateBE, observedTxBitrateBK, observedTxBitrateVI, observedTxBitrateVO, observedTxBitrateLLW0, observedTxBitrateLLW1) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, nwConnectionTimestamp, frequencyBand, intermittentState, estimatedIntermittentPeriod, singleOutagePeriod, btCoex, radioCoex, qualityScoreDelayRx, qualityScoreDelayTx, qualityScoreLossRx, qualityScoreLossTx, qualityScoreChannel, ROUND(offChannelTimeRatio,2), wlanDutyCycle, observedTxBitrateBE, observedTxBitrateBK, observedTxBitrateVI, observedTxBitrateVO, observedTxBitrateLLW0, observedTxBitrateLLW1 FROM Network; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, radioTechnology, flushableQueueDepth, unflushableQueueDepth, averageBitrate, averageBitrateShort, averageBitrateLong, txBitrate, averageQueueDepth, expectedQueuingDelay, bdcd, normalizedBDCD, normalizedDelay) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, radioTechnology, flushableQueueDepth, unflushableQueueDepth, averageBitrate, averageBitrateShort, averageBitrateLong, txBitrate, ROUND(averageQueueDepth,2), ROUND(expectedQueuingDelay,3), ROUND(bdcd,3), ROUND(normalizedBDCD,3), ROUND(normalizedDelay,3) FROM Baseband; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, bytesInFlight, bytesInFlightRollingAverage) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, bytesInFlight, bytesInFlightRollingAverage FROM LocalRCEvents; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, mode, localRAT, remoteRAT, minTargetBitrate, maxTargetBitrate, algorithmVersion) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, mode, localRAT, remoteRAT, minTargetBitrate, maxTargetBitrate, algorithmVersion FROM RateControllerConfiguration; "
+ "INSERT INTO VCRCMLoutput (timestamp, targetBitrate, bitrate, rateControlTime, owrd, nowrd, roundTripTime, audioPacketLossRate, videoPacketLossRate,  bandwidthEstimate, trainingValue, trainingAction, trainingActionLogProbability) SELECT ROUND(timestamp,3), targetBitrate, bitrate, ROUND(rateControlTime,3), ROUND(owrd, 3), ROUND(nowrd,3), ROUND(roundTripTime,3), ROUND(audioPacketLossRate,3), ROUND(videoPacketLossRate,3), bandwidthEstimate, trainingValue, trainingAction, trainingActionLogProbability FROM Feedback; INSERT INTO VCRCMLoutput (timestamp, targetBitrate, bitrate) SELECT ROUND(timestamp,3), targetBitrate, bitrate FROM Network; INSERT INTO VCRCMLoutput (timestamp, targetBitrate, bitrate, averageBitrate, expectedQueuingDelay) SELECT ROUND(timestamp,3), targetBitrate, bitrate, averageBitrate, ROUND(expectedQueuingDelay,3) FROM Baseband; INSERT INTO VCRCMLoutput (timestamp, targetBitrate, bitrate, bytesInFlight) SELECT ROUND(timestamp,3), targetBitrate, bitrate, bytesInFlight FROM LocalRCEvents; INSERT INTO VCRCMLoutput (timestamp, targetBitrate, bitrate, mode, localRAT, remoteRAT, maxTargetBitrate) SELECT ROUND(timestamp,3), targetBitrate, bitrate, mode, localRAT, remoteRAT, maxTargetBitrate FROM RateControllerConfiguration; "
+ "ImmersiveMediaSupport"
+ "InvalidVideoTxCaptureFrameCount"
+ "LKFASC"
+ "LPFASC"
+ "MAMPT"
+ "MAXPMTU"
+ "METRIC_DATE"
+ "MINPMTU"
+ "MLRIFP"
+ "MLROFP"
+ "NBDUR"
+ "NBMPC"
+ "PMTU"
+ "PMTUAR"
+ "PMTUDRTN"
+ "RATT"
+ "RATType"
+ "RemoteEndpoints"
+ "ReportingVC [%s] %s:%d %@(%p) Disabled Remote Data collection"
+ "ReportingVC [%s] %s:%d %@(%p) Failed to initialize DataStore"
+ "ReportingVC [%s] %s:%d %@(%p) Failed to initialize remoteDataProducer"
+ "ReportingVC [%s] %s:%d %@(%p) Failed to initialize vcrcmlTrainingDataProducer"
+ "ReportingVC [%s] %s:%d %@(%p) VCPersistentDataStore %s with identifier=%@ isRemoteDataCollectionDumpEnabled=%d isRateControlLocalTrainingDataCollectionEnabled=%d"
+ "ReportingVC [%s] %s:%d %@(%p) VCPersistentDataStore finalized with result=%d"
+ "ReportingVC [%s] %s:%d AWDAdapter failed to respond to mandatory selector"
+ "ReportingVC [%s] %s:%d Could not create AWDAdaptor"
+ "ReportingVC [%s] %s:%d Could not load AWDAdaptor class"
+ "ReportingVC [%s] %s:%d Disabled Remote Data collection"
+ "ReportingVC [%s] %s:%d Failed to initialize DataStore"
+ "ReportingVC [%s] %s:%d Failed to initialize remoteDataProducer"
+ "ReportingVC [%s] %s:%d Failed to initialize vcrcmlTrainingDataProducer"
+ "ReportingVC [%s] %s:%d Failed to load GKSPerformance bundle"
+ "ReportingVC [%s] %s:%d Sending Network score dictionary=%@"
+ "ReportingVC [%s] %s:%d VCPersistentDataStore %s with identifier=%@ isRemoteDataCollectionDumpEnabled=%d isRateControlLocalTrainingDataCollectionEnabled=%d"
+ "ReportingVC [%s] %s:%d VCPersistentDataStore finalized with result=%d"
+ "ReportingVC [%s] %s:%d algosScoreDictionary is nil"
+ "SELECT COUNT(*) FROM Feedback;"
+ "SELECT conversationID, participantID, deviceClass FROM Metadata LIMIT 1;"
+ "StreamConnectionTime"
+ "SymptomReporterOptionalKeyCaptureFrameCount"
+ "T@\"NSArray\",&,V_screenControlDurationsMsec"
+ "T@\"NSArray\",&,V_screenShareDurationsMsec"
+ "T@\"NSArray\",R,V_mlEnhancedPercentInputResolutions"
+ "T@\"NSArray\",R,V_mlEnhancedPercentOutputResolutions"
+ "T@\"NSMutableDictionary\",&,V_clientExperiments"
+ "T@\"NSString\",&,V_VCRCML_modelID"
+ "T@\"NSString\",&,V_VCRCML_recipeID"
+ "T@\"VCMediaAnalyzerDataCollector\",R,N,V_mediaAnalyzerDataCollector"
+ "T@\"VCRemoteDataCollectionDumpProducer\",R,V_remoteDataProducer"
+ "T@\"VCReportingBiDirectionalHistogram\",R,V_frameSizeVsDeltaBetweenParityAndLoss"
+ "T@\"VCReportingHistogram\",R,V_completeFECFrameCount"
+ "T@\"VCReportingHistogram\",R,V_failedFECFrameCount"
+ "T@\"VCReportingHistogram\",R,V_fecLevelDuration"
+ "T@\"VCReportingHistogram\",R,V_frameSizeCount"
+ "T@\"VCReportingHistogram\",R,V_frameSizeVsFailedCount"
+ "T@\"VCReportingHistogram\",R,V_frameSizeVsParityCount"
+ "T@\"VCReportingHistogram\",R,V_totalFECDataByteCount"
+ "T@\"VCReportingHistogram\",R,V_totalFECFrameCount"
+ "T@\"VCReportingHistogram\",R,V_totalFECMediaPacketCount"
+ "T@\"VCReportingHistogram\",R,V_totalFECParityByteCount"
+ "T@\"VCReportingHistogram\",R,V_totalFECParityPacketCount"
+ "T@\"VCReportingHistogram\",R,V_unfixableFECFrameCount"
+ "T@\"VCVideoFECStatsHolder\",R,V_fecStatsHolder"
+ "TB,N,V_isExplicitLanguageFilterEnabled"
+ "TB,N,V_isLanguageDetectorEnabled"
+ "TB,V_VCRCML_isMLEngaged"
+ "TI,R,V_averageVideoRxMetadataOverheadBitrate"
+ "TI,R,V_averageVideoTxMetadataOverheadBitrate"
+ "TI,R,V_lateKeyFrameAssembledCount"
+ "TI,R,V_latePFrameAssembledCount"
+ "TI,V_VCRCML_nIteration"
+ "TI,V_VCRCML_reportingGroup"
+ "TI,V_VCRCML_targetBitrateAtTimeOfDisengagement"
+ "TI,V_averageMetadataRxBitrate"
+ "TI,V_averageMetadataTxBitrate"
+ "TI,V_fecHeaderVersion"
+ "TI,V_lateKeyFrameAssembledCount"
+ "TI,V_latePFrameAssembledCount"
+ "TI,V_totalDecodedFrameCount"
+ "Td,R,V_totalAudioErasureTimeAlt"
+ "Td,V_VCRCML_activeMLEngagedDuration"
+ "Td,V_callAverageAudioRxBitrate"
+ "Td,V_callAverageAudioTxBitrate"
+ "Td,V_lateKeyFrameAssembledCount"
+ "Td,V_latePFrameAssembledCount"
+ "ThirdPartyScreenShare"
+ "T{tagVCReportingClientExperimentSettings=BBB},N,V_reportingClientExperimentSettings"
+ "T{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}},V_persistentSettings"
+ "UnbinnedCameraFormatSelected"
+ "V1SpeechAPIEnabled"
+ "VCACCT"
+ "VCACED"
+ "VCACELFE"
+ "VCACL"
+ "VCACSL"
+ "VCACSM"
+ "VCACTLA"
+ "VCACTUC"
+ "VCACUC"
+ "VCADLC"
+ "VCALDE"
+ "VCAggregatorUtils_GetSizeForVideoResolution"
+ "VCMAE"
+ "VCMAED"
+ "VCMAMPT"
+ "VCMediaAnalyzerDataCollector"
+ "VCRCMLD"
+ "VCRCMLE"
+ "VCRCMLMID"
+ "VCRCMLNI"
+ "VCRCMLRCTBR"
+ "VCRCMLRG"
+ "VCRCMLRID"
+ "VCRCML_activeMLEngagedDuration"
+ "VCRCML_isMLEngaged"
+ "VCRCML_modelID"
+ "VCRCML_nIteration"
+ "VCRCML_recipeID"
+ "VCRCML_reportingGroup"
+ "VCRCML_targetBitrateAtTimeOfDisengagement"
+ "VCRateControlMachineLearningLocalTrainingDataProducer"
+ "VCRemoteDataCollectionDumpProducer"
+ "VCReportingBiDirectionalHistogram"
+ "VCSCACAMRX"
+ "VCSCACAMTX"
+ "VFecMPC"
+ "VFecPPC"
+ "VFecSVDPL"
+ "VFecSVFAC"
+ "VFecSVFC"
+ "VFecSVPC"
+ "VPBLKFAR"
+ "VPBLPFAR"
+ "VTxFecStats"
+ "[50{tagVCPersistentDataStoreMessage=\"type\"i\"\"(?=\"data\"{tagVCRateControlDataCollectionMessage=\"state\"C\"timestamp\"d\"arrivalTime\"d\"targetBitrate\"I\"bitrate\"I\"basebandFlush\"B\"\"(?=\"feedback\"{tagVCDataCollectionFeedback=\"rateControlTime\"d\"owrd\"d\"nowrd\"d\"nowrda\"d\"roundTripTime\"d\"roundTripTimeAverage\"d\"roundTripTimeMinEnvelope\"d\"audioPacketLossRate\"d\"audioPacketLossRateShort\"d\"videoPacketLossRate\"d\"ecnCERatio\"d\"bandwidthEstimate\"I\"trainingValue\"d\"trainingAction\"I\"trainingActionLogProbability\"d}\"localRCEvent\"{tagVCDataCollectionLocalRCEvent=\"bytesInFlight\"I\"bytesInFlightRollingAverage\"I}\"nwConnection\"{tagVCDataCollectionNWConnection=\"nwConnectionTimestamp\"Q\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]}\"baseband\"{tagVCDataCollectionBaseband=\"radioTechnology\"I\"flushableQueueDepth\"I\"unflushableQueueDepth\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"txBitrate\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d}\"configuration\"{tagVCDataCollectionRCConfiguration=\"algorithmVersion\"i\"mode\"I\"radioAccessTechnology\"I\"remoteRadioAccessTechnology\"I\"minTargetBitrate\"I\"maxTargetBitrate\"I})}\"metadata\"{tagVCDataCollectionMetadata=\"conversationID\"^{__CFString}\"participantID\"^{__CFString}\"deviceClass\"I})}]"
+ "[7*]"
+ "[75B]"
+ "[7^{sqlite3_stmt}]"
+ "^q"
+ "_VCPersistentDataStore_SaveMetadata"
+ "_VCRCML_activeMLEngagedDuration"
+ "_VCRCML_isMLEngaged"
+ "_VCRCML_modelID"
+ "_VCRCML_nIteration"
+ "_VCRCML_recipeID"
+ "_VCRCML_reportingGroup"
+ "_VCRCML_targetBitrateAtTimeOfDisengagement"
+ "_answeringMachineUsageHistogram"
+ "_audioInjectorCreatedTime"
+ "_audioInjectorFileSizeHistogram"
+ "_audioInjectorMessageLengthHistogram"
+ "_audioInjectorSetUpTime"
+ "_averageMetadataRxBitrate"
+ "_averageMetadataTxBitrate"
+ "_awdAdaptor"
+ "_callAverageAudioRxBitrate"
+ "_callAverageAudioTxBitrate"
+ "_callTypeHistogram"
+ "_captionsEnabledDuration"
+ "_captionsLocale"
+ "_captionsSourceLocale"
+ "_captionsSpeechModel"
+ "_clientExperiments"
+ "_codecLayers"
+ "_currentMTUDurationStartTime"
+ "_currentNumberEndpoints"
+ "_currentPathMTU"
+ "_detectedLanguageCodeHistogram"
+ "_directoryPath"
+ "_fecHeaderVersion"
+ "_fecLevelDuration"
+ "_fecStatsHolder"
+ "_frameSizeCount"
+ "_frameSizeVsDeltaBetweenParityAndLoss"
+ "_frameSizeVsFailedCount"
+ "_frameSizeVsParityCount"
+ "_isExplicitLanguageFilterEnabled"
+ "_isLanguageDetectorEnabled"
+ "_isMediaAnalyzerEnabled"
+ "_lastCaptionsEnabledTime"
+ "_lateKeyFrameAssembledCount"
+ "_latePFrameAssembledCount"
+ "_localTrainingDataProducerCallback"
+ "_maxNumberEndpoints"
+ "_maxPathMTU"
+ "_mediaAnalyzerDataCollector"
+ "_mediaAnalyzerEnabledDuration"
+ "_mediaAnalyzerLastEnabledTime"
+ "_mediaAnalyzerMeanProcessingTimesHistogram"
+ "_minPathMTU"
+ "_mlEnhancedPercentInputResolutions"
+ "_mlEnhancedPercentOutputResolutions"
+ "_nearbyStats"
+ "_networkScoreUUIDString"
+ "_numberOfRegisteredProducers"
+ "_nwsMetricReporter"
+ "_nwsMetricReporterQueue"
+ "_pathMTUArray"
+ "_pathMTUCounter"
+ "_pathMTUDurationArray"
+ "_ratType"
+ "_recipeID"
+ "_remoteDataCollectionProducerCallback"
+ "_remoteDataProducer"
+ "_sensitiveContentAnalysisForCamRxEnabled"
+ "_sensitiveContentAnalysisForCamTxEnabled"
+ "_signedBuckets"
+ "_totalAudioErasureTimeAlt"
+ "_totalDecodedFrameCount"
+ "_totalFECMediaPacketCount"
+ "_totalFECParityPacketCount"
+ "_translatedLatencyAverage"
+ "_translatedUtteranceCount"
+ "_utteranceCount"
+ "_vcrcmlTrainingDataProducer"
+ "addAggregateAudioInjectorMetricsToReport:"
+ "addAggregatedLanguageDetectorMetricsToReport:"
+ "addAggregatedMediaAnalyzerMetricsToReport:"
+ "addClientExperimentsToReport:"
+ "addFECStats:parameters:"
+ "addFECStats:parameters:reportFrameSizeTelemetry:reportLevels:"
+ "addFECStatsHolderKPIs:usingFECStatsHolder:"
+ "addFECStatsHolderKPIs:usingFECStatsHolder:reportFrameSizeTelemetry:reportLevels:"
+ "addValue:withDelta:"
+ "algoScorerParticipantIDList"
+ "appendPathMTU:delta:"
+ "audioErasureTotalTimeAlt"
+ "audioErasureTotalTimeAlt:"
+ "averageMetadataRxBitrate"
+ "averageMetadataTxBitrate"
+ "averageVideoRxMetadataOverheadBitrate"
+ "averageVideoTxMetadataOverheadBitrate"
+ "bundle-id"
+ "callAverageAudioRxBitrate"
+ "callAverageAudioTxBitrate"
+ "classNamed:"
+ "clientExperiments"
+ "com.apple.VideoConference.nwsMetricReporter"
+ "com.apple.mobilephone"
+ "com.apple.rtcreporting"
+ "convertHistogramIntoComplementaryPercentage:"
+ "convertHistogramIntoPercentageUsingValuesFrom:"
+ "copyItemAtPath:toPath:error:"
+ "createDefaultAttributeDirectoryIfNeeded:"
+ "createDumpAndSubmitToCoreAnalytics"
+ "defaultProcessEventWithCategory:type:payload:"
+ "deregisterDataProducerWithType:"
+ "disableRemoteDataCollection"
+ "environmentType"
+ "explicitLanguageFilterEnabled"
+ "fecHeaderVersion"
+ "fecLevelDuration"
+ "fecStatsHolder"
+ "fileExistsAtPath:"
+ "finalizeInternal"
+ "finalizePathMTUForTime:"
+ "finalizeStats"
+ "frameSizeCount"
+ "frameSizeVsDeltaBetweenParityAndLoss"
+ "frameSizeVsFailedCount"
+ "frameSizeVsParityCount"
+ "generation_time"
+ "initFileURLWithPath:"
+ "initWithDataStore:"
+ "initWithDataStore:recipeID:"
+ "initWithIdentifier:"
+ "initWithPath:"
+ "isLoaded"
+ "label"
+ "label-call"
+ "label-periodic"
+ "languageDetectorEnabled"
+ "lateKeyFrameAssembledCount"
+ "latePFrameAssembledCount"
+ "load"
+ "mediaAnalyzerDataCollector"
+ "mlEnhancedPercentInputResolutions"
+ "mlEnhancedPercentOutputResolutions"
+ "newHeaderString"
+ "no-label"
+ "now"
+ "numberWithLongLong:"
+ "path"
+ "processAudioInjectionInitWithPayload:currentTime:"
+ "processAudioInjectionReadyWithCurrentTime:"
+ "processCaptionsEnabled:withCurrentTime:"
+ "processEndpointChanged:"
+ "processFecConfigData:"
+ "processFrameSizeBasedFECTelemetry:statsHolder:direction:"
+ "processMLStreamData:"
+ "processMediaAnalyzerEnabled:withCurrentTime:"
+ "processMediaAnalyzerMetrics:"
+ "processNearbyStopWithPayload:"
+ "processPathMTU:now:"
+ "processRTEvent:now:"
+ "processRTEventCommon:now:"
+ "rc_fl_data"
+ "reallocateAndStartBoundedAlgoScorerWithTime:"
+ "recipe_id"
+ "registerDataProducerWithType:producerCallback:"
+ "remoteDataProducer"
+ "replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:"
+ "reportInvalidVideoTxCaptureFrameCountWithOptionalDictionary:"
+ "reportSegment"
+ "reportUnbinnedCameraFormatSelected"
+ "reportUnexpectedHighRTTWithOptionalDictionary:"
+ "reportV1SpeechAPIEnabled"
+ "reportVCRCMLStats:"
+ "reportingClientType"
+ "resetMLStats"
+ "resetRateControlMLEnrollmentAndStatsInSegment:"
+ "resetVideoStatsForU1OrMultiwaySwitch:participantID:"
+ "runDataProducers"
+ "runPostProcessing:"
+ "runTrainingDataPostProcessing:"
+ "sendMessageToAWDAdaptorWithCategory:type:payload:"
+ "sendMessageWithMethodPrivate:respCode:dict:"
+ "sendNetworkScoreDictionary:networkScoreType:"
+ "sendStreamMetrics:onQueue:"
+ "setAlgosScorerVideoResolution:time:participantID:"
+ "setAverageMetadataRxBitrate:"
+ "setAverageMetadataTxBitrate:"
+ "setCallAverageAudioRxBitrate:"
+ "setCallAverageAudioTxBitrate:"
+ "setClientExperiments:"
+ "setDateFormat:"
+ "setExplicitLanguageFilterEnabled:"
+ "setFecHeaderVersion:"
+ "setLanguageDetectorEnabled:"
+ "setLateKeyFrameAssembledCount:"
+ "setLatePFrameAssembledCount:"
+ "setMediaAnalyzerEnabled:"
+ "setTotalDecodedFrameCount:"
+ "setUpAWDAdapter"
+ "setUpMLHistograms"
+ "setUpTrainingDataForPlugin"
+ "setVCRCML_activeMLEngagedDuration:"
+ "setVCRCML_isMLEngaged:"
+ "setVCRCML_modelID:"
+ "setVCRCML_nIteration:"
+ "setVCRCML_recipeID:"
+ "setVCRCML_reportingGroup:"
+ "setVCRCML_targetBitrateAtTimeOfDisengagement:"
+ "setValue:forKey:"
+ "sharedAWDAdaptorClass"
+ "shouldGenerateTrainingDataWithDatabase:"
+ "startAlgosScorer:time:"
+ "stringFromDate:"
+ "submitToCoreAnalytics:"
+ "supportsSegmentReporting"
+ "supportsSessionReporting"
+ "telephonyCallingProcessAWDMetrics:"
+ "totalAudioErasureTimeAlt"
+ "totalDecodedFrameCount"
+ "totalFECMediaPacketCount"
+ "totalFECParityPacketCount"
+ "totalMetadataOverheadSendBitrateSum"
+ "totalMetadataSendBitrateCounter"
+ "training_data.db"
+ "training_data.json"
+ "updateClientExperiments:"
+ "updateFECStats:usingUpdateValuesIn:"
+ "updateRateControlMachineLearningEnrollment:"
+ "updateRateControlMachineLearningRateControllerStats:"
+ "updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:direction:"
+ "updateWithPayload:blockFecLevels:"
+ "v160@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}{tagVCPersistentDataStoreConfiguration=BB^{__CFString}}}16"
+ "v19@0:8{tagVCReportingClientExperimentSettings=BBB}16"
+ "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
+ "v28@0:8@\"VCAlgosStreamingScoreAggregator\"16C24"
+ "v28@0:8@16C24"
+ "v28@0:8I16q20"
+ "v28@0:8S16d20"
+ "v28@0:8i16@?20"
+ "v36@0:8@16@24i32"
+ "v40@0:8@16@24B32B36"
+ "v40@0:8@16^{tagVCFECSegmentReportParameters=@@@@IIII}24B32B36"
+ "v40@0:8{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16"
+ "v60@0:8@16@24@32@40@48i56"
+ "videoResolutionForWidth:height:"
+ "writeToFile:atomically:"
+ "yyyy-MM-dd'T'HH:mm:ssZ"
+ "yyyy-MM-dd'T'HH:mm:ssZZZZZ"
+ "{tagVCDataCollectionMetadata=\"conversationID\"^{__CFString}\"participantID\"^{__CFString}\"deviceClass\"I}"
+ "{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B\"detectInactiveAudioFramesAACELD\"B}"
+ "{tagVCReportingClientExperimentSettings=BBB}16@0:8"
+ "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B\"detectInactiveAudioFramesAACELD\"B}}"
+ "{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BBB}}16@0:8"
- " [%s] %s:%d %@(%p) Created database file with databasePath=%@"
- " [%s] %s:%d %@(%p) Data store not available if data collection is disabled"
- " [%s] %s:%d %@(%p) Deleted database with databasePath=%@"
- " [%s] %s:%d %@(%p) Failed to create save csv with filePath=%@, core analytics submission cancelled"
- " [%s] %s:%d %@(%p) Failed to initialize SQLite database with path=%@"
- " [%s] %s:%d Already reported"
- " [%s] %s:%d Created database file with databasePath=%@"
- " [%s] %s:%d Data store not available if data collection is disabled"
- " [%s] %s:%d Deleted database with databasePath=%@"
- " [%s] %s:%d Failed to create save csv with filePath=%@, core analytics submission cancelled"
- " [%s] %s:%d Failed to initialize SQLite database with path=%@"
- " [%s] %s:%d Supplied status has no value"
- " [%s] %s:%d SymptomReporter: reporting symptom UnexpectedHighRTT for session %u"
- " [%s] %s:%d SymptomReporter: reporting symptom on connection Slice status for callID=%u symptomID=%d"
- " [%s] %s:%d VCPersistentDataStore already invalid!"
- "%@/%@%s"
- "%s fileSchemaVersion=%d conversationID=%@ participantID=%@ deviceClass=%d \n"
- "+[VCAggregatorUtils sizeForVideoResolution:]"
- "+[VCDiskUtils createDefaultDirectoryIfNeeded:]"
- "-[VCAggregator segmentFECReport:parameters:]"
- "-[VCAggregator updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:]"
- "-[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:]"
- "-[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]"
- "-[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]"
- "-[VCPersistentDataStore coreAnalyticsCallback:fileHandle:]"
- "-[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:]"
- "-[VCPersistentDataStore invalidateInternalWithReason:]"
- "-[VCPersistentDataStore submitToCoreAnalytics]"
- "-[VCPersistentDataStore writeVCRCMLDumpToCSVPath:]"
- "-[VCSymptomReporter reportConnectionSliceStatus:]"
- "-[VCSymptomReporter reportUnexpectedHighRTT]"
- "@\"AlgosStreamScore\""
- "@152@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}B}16"
- "@28@0:8@16B24"
- "B24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}B}16"
- "B28@0:8@16i24"
- "CREATE TABLE IF NOT EXISTS Feedback ( state INT, timestamp DOUBLE, arrivalTime DOUBLE, targetBitrate INT, bitrate INT, basebandFlush INT, rateControlTime FLOAT(24,4), owrd FLOAT(24,4), nowrd FLOAT(24,4), nowrda FLOAT(24,4), roundTripTime FLOAT(24,4), roundTripTimeAverage FLOAT(24,4), roundTripTimeMinEnvelope FLOAT(24,4), audioPacketLossRate FLOAT(24,4), audioPacketLossRateShort FLOAT(24,4), videoPacketLossRate FLOAT(24,4), ecnCERatio FLOAT(24,4), bandwidthEstimate INT );"
- "CREATE TABLE VCRCMLoutput  ( state INT, timestamp DOUBLE, arrivalTime DOUBLE, targetBitrate INT, bitrate INT, basebandFlush INT, rateControlTime FLOAT(24,4), owrd FLOAT(24,4), nowrd FLOAT(24,4), nowrda FLOAT(24,4), roundTripTime FLOAT(24,4), roundTripTimeAverage FLOAT(24,4), roundTripTimeMinEnvelope FLOAT(24,4), audioPacketLossRate FLOAT(24,4), audioPacketLossRateShort FLOAT(24,4), videoPacketLossRate FLOAT(24,4), ecnCERatio FLOAT(24,4), bandwidthEstimate INT, nwConnectionTimestamp BIGINT, frequencyBand INT, intermittentState INT, estimatedIntermittentPeriod INT, singleOutagePeriod INT, btCoex INT, radioCoex INT, qualityScoreDelayRx INT, qualityScoreDelayTx INT, qualityScoreLossRx INT, qualityScoreLossTx INT, qualityScoreChannel INT, offChannelTimeRatio FLOAT, wlanDutyCycle INT, observedTxBitrateBE INT, observedTxBitrateBK INT, observedTxBitrateVI INT, observedTxBitrateVO INT, observedTxBitrateLLW0 INT, observedTxBitrateLLW1 INT, radioTechnology INT, flushableQueueDepth INT, unflushableQueueDepth INT, averageBitrate INT, averageBitrateShort INT, averageBitrateLong INT, txBitrate INT, averageQueueDepth DOUBLE, expectedQueuingDelay DOUBLE, bdcd DOUBLE, normalizedBDCD DOUBLE, normalizedDelay DOUBLE, bytesInFlight INT, bytesInFlightRollingAverage INT, mode INT, localRAT INT, remoteRAT INT, minTargetBitrate INT, maxTargetBitrate INT, algorithmVersion INT ); "
- "CallConnectionTime"
- "FECFC0"
- "FECVPNR0"
- "INSERT INTO Feedback (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, rateControlTime, owrd, nowrd, nowrda, roundTripTime, roundTripTimeAverage, roundTripTimeMinEnvelope, audioPacketLossRate, audioPacketLossRateShort, videoPacketLossRate, ecnCERatio, bandwidthEstimate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
- "INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, rateControlTime, owrd, nowrd, nowrda, roundTripTime, roundTripTimeAverage, roundTripTimeMinEnvelope, audioPacketLossRate, audioPacketLossRateShort, videoPacketLossRate, ecnCERatio, bandwidthEstimate) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, ROUND(rateControlTime,3), ROUND(owrd, 3), ROUND(nowrd,3), ROUND(nowrda,3), ROUND(roundTripTime,3), ROUND(roundTripTimeAverage,3), ROUND(roundTripTimeMinEnvelope,3), ROUND(audioPacketLossRate,3), ROUND(audioPacketLossRateShort,3), ROUND(videoPacketLossRate,3), ROUND(ecnCERatio,3), bandwidthEstimate FROM Feedback; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, nwConnectionTimestamp, frequencyBand, intermittentState, estimatedIntermittentPeriod, singleOutagePeriod, btCoex, radioCoex, qualityScoreDelayRx, qualityScoreDelayTx, qualityScoreLossRx, qualityScoreLossTx, qualityScoreChannel, offChannelTimeRatio, wlanDutyCycle, observedTxBitrateBE, observedTxBitrateBK, observedTxBitrateVI, observedTxBitrateVO, observedTxBitrateLLW0, observedTxBitrateLLW1) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, nwConnectionTimestamp, frequencyBand, intermittentState, estimatedIntermittentPeriod, singleOutagePeriod, btCoex, radioCoex, qualityScoreDelayRx, qualityScoreDelayTx, qualityScoreLossRx, qualityScoreLossTx, qualityScoreChannel, ROUND(offChannelTimeRatio,2), wlanDutyCycle, observedTxBitrateBE, observedTxBitrateBK, observedTxBitrateVI, observedTxBitrateVO, observedTxBitrateLLW0, observedTxBitrateLLW1 FROM Network; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, radioTechnology, flushableQueueDepth, unflushableQueueDepth, averageBitrate, averageBitrateShort, averageBitrateLong, txBitrate, averageQueueDepth, expectedQueuingDelay, bdcd, normalizedBDCD, normalizedDelay) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, radioTechnology, flushableQueueDepth, unflushableQueueDepth, averageBitrate, averageBitrateShort, averageBitrateLong, txBitrate, ROUND(averageQueueDepth,2), ROUND(expectedQueuingDelay,3), ROUND(bdcd,3), ROUND(normalizedBDCD,3), ROUND(normalizedDelay,3) FROM Baseband; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, bytesInFlight, bytesInFlightRollingAverage) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, bytesInFlight, bytesInFlightRollingAverage FROM LocalRCEvents; INSERT INTO VCRCMLoutput (state, timestamp, arrivalTime, targetBitrate, bitrate, basebandFlush, mode, localRAT, remoteRAT, minTargetBitrate, maxTargetBitrate, algorithmVersion) SELECT state, ROUND(timestamp,3), ROUND(arrivalTime,3), targetBitrate, bitrate, basebandFlush, mode, localRAT, remoteRAT, minTargetBitrate, maxTargetBitrate, algorithmVersion FROM RateControllerConfiguration; "
- "ReportingVC [%s] %s:%d %@(%p) VCPersistentDataStore %s with identifier=%@ dataCollectionEnabled=%d"
- "ReportingVC [%s] %s:%d %@(%p) VCPersistentDataStore disabled with result=%d"
- "ReportingVC [%s] %s:%d %@(%p) VCPersistentDataStore invalidated with result=%d"
- "ReportingVC [%s] %s:%d VCPersistentDataStore %s with identifier=%@ dataCollectionEnabled=%d"
- "ReportingVC [%s] %s:%d VCPersistentDataStore disabled with result=%d"
- "ReportingVC [%s] %s:%d VCPersistentDataStore invalidated with result=%d"
- "SliceInterfaceFailed"
- "SliceInterfaceNotReceived"
- "T@\"NSArray\",V_screenControlDurationsMsec"
- "T@\"NSArray\",V_screenShareDurationsMsec"
- "T@\"NSMutableDictionary\",R,V_fecStatsDict"
- "TI,V_completeFECFrameCount"
- "TI,V_failedFECFrameCount"
- "TI,V_totalFECFrameCount"
- "TI,V_unfixableFECFrameCount"
- "TQ,V_totalFECDataByteCount"
- "TQ,V_totalFECParityByteCount"
- "Tc,N,V_backgroundReplacementStatus"
- "T{tagVCReportingClientExperimentSettings=BB},N,V_reportingClientExperimentSettings"
- "T{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}},V_persistentSettings"
- "[50{tagVCPersistentDataStoreMessage=\"type\"i\"\"(?=\"data\"{tagVCRateControlDataCollectionMessage=\"state\"C\"timestamp\"d\"arrivalTime\"d\"targetBitrate\"I\"bitrate\"I\"basebandFlush\"B\"\"(?=\"feedback\"{tagVCDataCollectionFeedback=\"rateControlTime\"d\"owrd\"d\"nowrd\"d\"nowrda\"d\"roundTripTime\"d\"roundTripTimeAverage\"d\"roundTripTimeMinEnvelope\"d\"audioPacketLossRate\"d\"audioPacketLossRateShort\"d\"videoPacketLossRate\"d\"ecnCERatio\"d\"bandwidthEstimate\"I}\"localRCEvent\"{tagVCDataCollectionLocalRCEvent=\"bytesInFlight\"I\"bytesInFlightRollingAverage\"I}\"nwConnection\"{tagVCDataCollectionNWConnection=\"nwConnectionTimestamp\"Q\"frequencyBand\"C\"intermittentState\"C\"estimatedIntermittentPeriod\"S\"singleOutagePeriod\"S\"btCoex\"C\"radioCoex\"C\"qualityScoreDelayRx\"C\"qualityScoreDelayTx\"C\"qualityScoreLossRx\"C\"qualityScoreLossTx\"C\"qualityScoreChannel\"C\"offChannelTimeRatio\"f\"wlanDutyCycle\"S\"wifiObservedTxBitrate\"[6I]}\"baseband\"{tagVCDataCollectionBaseband=\"radioTechnology\"I\"flushableQueueDepth\"I\"unflushableQueueDepth\"I\"averageBitrate\"I\"averageBitrateShort\"I\"averageBitrateLong\"I\"txBitrate\"I\"averageQueueDepth\"d\"expectedQueuingDelay\"d\"bdcd\"d\"normalizedBDCD\"d\"normalizedDelay\"d}\"configuration\"{tagVCDataCollectionRCConfiguration=\"algorithmVersion\"i\"mode\"I\"radioAccessTechnology\"I\"remoteRadioAccessTechnology\"I\"minTargetBitrate\"I\"maxTargetBitrate\"I})}\"metadata\"{tagVCDataCollectionMetadata=\"conversationID\"^{__CFString}\"participantID\"^{__CFString}\"deviceClass\"I\"fileSchemaVersion\"C})}]"
- "[6*]"
- "[6^{sqlite3_stmt}]"
- "[72B]"
- "_cannedAudioInjectorCreatedTime"
- "_cannedAudioInjectorFileSizeHistogram"
- "_cannedAudioInjectorMessageLengthHistogram"
- "_cannedAudioInjectorSetUpTime"
- "_fecStatsDict"
- "_isDataCollectionEnabled"
- "addAggregatedCannedAudioMetricsToReport:"
- "checkSliceStatus:hasValuesOnlyForStatus:"
- "createDefaultDirectoryIfNeeded:"
- "fecStatsDict"
- "i20@0:8I16"
- "initWithIdentifier:dataCollectionEnabled:"
- "invalidateInternalWithReason:"
- "processCannedAudioInjectionInitWithPayload:currentTime:"
- "processCannedAudioInjectionReadyWithCurrentTime:"
- "processRTEventCommon:"
- "processSliceStatusABCSymptoms:currentSegmentName:"
- "processSliceStatusFailedABCSymptom:"
- "processSliceStatusNotReceivedABCSymptom:"
- "reallocateBoundedAlgoScorerWithTime:"
- "remoteMicProcessEventWithCategory:type:payload:"
- "reportConnectionSliceStatus:"
- "reportUnexpectedHighRTT"
- "screenSharingProcessEventWithCategory:payload:"
- "segmentFECReport:parameters:"
- "sessionFECReport"
- "setCompleteFECFrameCount:"
- "setFailedFECFrameCount:"
- "setTotalFECDataByteCount:"
- "setTotalFECFrameCount:"
- "setTotalFECParityByteCount:"
- "setUnfixableFECFrameCount:"
- "startBoundedAlgoScorerWithTime:"
- "submitToCoreAnalytics"
- "updateVideoFECStatsOnSegment:fecStats:segmentLossPattern:segmentLossHistogram:segmentLossFecHistogram:"
- "v152@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}B}16"
- "v18@0:8{tagVCReportingClientExperimentSettings=BB}16"
- "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v40@0:8{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
- "{tagVCDataCollectionMetadata=\"conversationID\"^{__CFString}\"participantID\"^{__CFString}\"deviceClass\"I\"fileSchemaVersion\"C}"
- "{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B}"
- "{tagVCReportingClientExperimentSettings=BB}16@0:8"
- "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B}}"
- "{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16@0:8"

```
