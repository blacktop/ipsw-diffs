## libAWDSupportFramework.dylib

> `/usr/lib/libAWDSupportFramework.dylib`

```diff

 7019.0.0.0.0
-  __TEXT.__text: 0x322634
+  __TEXT.__text: 0x37289c
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x4acbc
   __TEXT.__cstring: 0xfccc
-  __TEXT.__unwind_info: 0x6260
+  __TEXT.__unwind_info: 0x6270
   __TEXT.__eh_frame: 0x3b0
   __TEXT.__objc_classname: 0x4265
-  __TEXT.__objc_methname: 0x63dda
+  __TEXT.__objc_methname: 0x63e0a
   __TEXT.__objc_methtype: 0x11830
-  __TEXT.__objc_stubs: 0xbc80
-  __DATA_CONST.__got: 0x500
+  __TEXT.__objc_stubs: 0xbd60
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xf18
   __DATA_CONST.__objc_classlist: 0x11a8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a470
+  __DATA_CONST.__objc_selrefs: 0x1a490
   __DATA_CONST.__objc_superrefs: 0x11a8
   __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__cfstring: 0x1cd60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7A33412-1434-3BB1-AD4B-2EEC6E3FC74C
+  UUID: AB6536A8-DC2F-39C7-AA6B-641CBD006F3C
   Functions: 25587
-  Symbols:   63067
-  CStrings:  28394
+  Symbols:   63070
+  CStrings:  28398
 
Symbols:
+ _objc_msgSend$_setError
+ _objc_msgSend$data
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$length
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
Functions:
~ _AWDAddressBookSyncFullSyncEventReadFrom : 1052 -> 1400
~ _AWDBltDelayAckFromSecondaryDeviceReadFrom : 1284 -> 1704
~ _AWDBltDelayAppReadyToSendReadFrom : 760 -> 956
~ _AWDBltDelayReceiveLocalReadFrom : 760 -> 956
~ _AWDBltDelayToPrimaryDeviceReadFrom : 936 -> 1208
~ _AWDBltDelayToSecondaryDeviceReadFrom : 936 -> 1208
~ _AWDBltDelayToSyncReadFrom : 888 -> 1156
~ _AWDBltDelayToSyncUnrestrictedReadFrom : 708 -> 904
~ _AWDBltDelayUIFromFactoryReadFrom : 760 -> 956
~ _AWDBltPrimaryDevicePublicationToResponseDelayReadFrom : 1104 -> 1452
~ _AWDBltPrimaryDeviceSendAttemptReadFrom : 708 -> 904
~ _AWDBltPrimaryDeviceSendInTimeReadFrom : 876 -> 1148
~ _AWDBltPrimaryDeviceSendTimeoutReadFrom : 876 -> 1148
~ _AWDBltRequestToResponseDelayReadFrom : 936 -> 1208
~ _AWDBltSecondaryConnectedToTransportReadFrom : 536 -> 648
~ _AWDBltSecondaryProcessStartedReadFrom : 536 -> 648
~ _AWDBltUIBuildAttemptReadFrom : 588 -> 708
~ _AWDBltUIBuildFailReadFrom : 588 -> 708
~ _AWDBltUIBuildSuccessReadFrom : 588 -> 708
~ _AWDCaptiveSessionReadFrom : 4160 -> 5648
~ _AWDCFNetworkCacheMetricsReadFrom : 756 -> 952
~ _AWDCFNetworkStreamTaskTimingReadFrom : 2568 -> 3568
~ _AWDCFNetworkTaskMetricsReadFrom : 2492 -> 3440
~ _AWDCFNetworkTransactionMetricsReadFrom : 3088 -> 4300
~ _AWDCFNetworkW3CNavigationTimingReadFrom : 3160 -> 4356
~ _AWDCompanionSyncErrorEventReadFrom : 936 -> 1208
~ _AWDCompanionSyncErrorNotificationReadFrom : 816 -> 1008
~ _AWDCompanionSyncFullSyncDurationReadFrom : 944 -> 1212
~ _AWDCompanionSyncReceiveEventReadFrom : 1100 -> 1448
~ _AWDCoreRoutineAssetVersionReadFrom : 708 -> 904
~ _AWDCoreRoutineDeletionGroupStatsReadFrom : 804 -> 1000
~ _AWDCoreRoutineDeletionRecordStatsReadFrom : 536 -> 648
~ _AWDCoreRoutineDeletionStatsReadFrom : 996 -> 1264
~ _AWDCoreRoutineFMCAssistanceInstanceReadFrom : 1104 -> 1452
~ _AWDCoreRoutineFMCCarParkedInstanceReadFrom : 1460 -> 1956
~ _AWDCoreRoutineFMCDailyAssessmentReadFrom : 1908 -> 2636
~ _AWDCoreRoutineFMCDailyAssessmentsReadFrom : 636 -> 756
~ _AWDCoreRoutineFMCReturnToCarInstanceReadFrom : 936 -> 1208
~ _AWDCoreRoutineFMCVehicleConnectionEventInstanceReadFrom : 876 -> 1148
~ _AWDCoreRoutineFMCViewedInstanceReadFrom : 760 -> 956
~ _AWDCoreRoutineHeroAppEngagementInstanceReadFrom : 936 -> 1208
~ _AWDCoreRoutineHeroAppImpressionInstanceReadFrom : 760 -> 956
~ _AWDCoreRoutineHeroAppSuggestionInstanceReadFrom : 1164 -> 1508
~ _AWDCoreRoutineHintSourceSubmissionInstanceReadFrom : 536 -> 648
~ _AWDCoreRoutineHintSourceSubmissionSetReadFrom : 636 -> 756
~ _AWDCoreRoutineHintSourceUsageInstanceReadFrom : 884 -> 1148
~ _AWDCoreRoutineHintSourceUsageSetReadFrom : 636 -> 756
~ _AWDCoreRoutineHistogramBinReadFrom : 720 -> 912
~ _AWDCoreRoutineLMPAutofillSelectedInstanceReadFrom : 760 -> 956
~ _AWDCoreRoutineLMPDailyAssessmentReadFrom : 1740 -> 2392
~ _AWDCoreRoutineLMPRequestedInstanceReadFrom : 1284 -> 1704
~ _AWDCoreRoutineLMPResponseInstanceReadFrom : 948 -> 1216
~ _AWDCoreRoutineLMPScoreBoardReadFrom : 672 -> 792
~ _AWDCoreRoutineLMPScoreBoardInstanceReadFrom : 1100 -> 1448
~ _AWDCoreRoutineLearnedLocationReconciliationVisitReadFrom : 2408 -> 3244
~ _AWDCoreRoutineLearnedLocationReconciliationVisitDensityReadFrom : 876 -> 1148
~ _AWDCoreRoutineLearnedLocationTrainingMetricsReadFrom : 2268 -> 3068
~ _AWDCoreRoutineLearnedRouteInstanceReadFrom : 2296 -> 3104
~ _AWDCoreRoutineLocationAwarenessBasicHistogramReadFrom : 748 -> 948
~ _AWDCoreRoutineLocationAwarenessHeartbeatStatisticsReadFrom : 912 -> 1108
~ _AWDCoreRoutineLocationAwarenessIntervalHistogramReadFrom : 964 -> 1160
~ _AWDCoreRoutineLocationAwarenessLocationTimeHistogramsReadFrom : 1072 -> 1204
~ _AWDCoreRoutineLocationAwarenessStatisticsReadFrom : 1364 -> 1504
~ _AWDCoreRoutineLocationTypeItemReadFrom : 720 -> 912
~ _AWDCoreRoutineMagicMomentsSuggestionInstanceReadFrom : 1204 -> 1552
~ _AWDCoreRoutineMagicalMomentsExpertInstanceReadFrom : 1228 -> 1576
~ _AWDCoreRoutineMagicalMomentsExpertsReadFrom : 1020 -> 1292
~ _AWDCoreRoutineMagicalMomentsFeatureAddonReadFrom : 584 -> 704
~ _AWDCoreRoutineMagicalMomentsIndividualMomentReadFrom : 936 -> 1208
~ _AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramInstanceReadFrom : 752 -> 948
~ _AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramSetReadFrom : 1320 -> 1744
~ _AWDCoreRoutineMapItemReadFrom : 940 -> 1212
~ _AWDCoreRoutineModelAlgorithmInstanceReadFrom : 2012 -> 2748
~ _AWDCoreRoutineModelAlgorithmSetReadFrom : 636 -> 756
~ _AWDCoreRoutineModelAvailabilityReadFrom : 876 -> 1148
~ _AWDCoreRoutineModelClusterMovementInstanceReadFrom : 536 -> 648
~ _AWDCoreRoutineModelClusterMovementNoiseSetReadFrom : 636 -> 756
~ _AWDCoreRoutineModelClusterStandardDeviationInstanceReadFrom : 720 -> 912
~ _AWDCoreRoutineModelClusterStandardDeviationSetReadFrom : 636 -> 756
~ _AWDCoreRoutineModelConsistencyReconsolidationReadFrom : 708 -> 904
~ _AWDCoreRoutineModelDominantPlaceCountReadFrom : 708 -> 904
~ _AWDCoreRoutineModelLearnedNonGeocodeableEventsReadFrom : 1052 -> 1400
~ _AWDCoreRoutineModelLengthReadFrom : 708 -> 904
~ _AWDCoreRoutineModelStatusReadFrom : 716 -> 908
~ _AWDCoreRoutineModelTransitionInstanceReadFrom : 812 -> 1008
~ _AWDCoreRoutineModelTransitionSetReadFrom : 636 -> 756
~ _AWDCoreRoutineModelVisitCountReadFrom : 808 -> 1004
~ _AWDCoreRoutinePersistenceMirroringAccountDevicesReadFrom : 1320 -> 1744
~ _AWDCoreRoutinePersistenceMirroringDelegateReadFrom : 888 -> 1156
~ _AWDCoreRoutinePersistenceMirroringDeviceProfileReadFrom : 1564 -> 2140
~ _AWDCoreRoutinePersistenceMirroringOperationsReadFrom : 1564 -> 2140
~ _AWDCoreRoutinePersistenceMirroringResetSyncReadFrom : 876 -> 1148
~ _AWDCoreRoutinePersistenceMirroringTickleFightReadFrom : 1284 -> 1712
~ _AWDCoreRoutinePersistenceStoreReadFrom : 888 -> 1156
~ _AWDCoreRoutinePersistenceStoreMigrationDurationReadFrom : 1664 -> 2336
~ _AWDCoreRoutinePlaceReadFrom : 548 -> 592
~ _AWDCoreRoutineRankRoutesRequestedInstanceReadFrom : 876 -> 1148
~ _AWDCoreRoutineRoadClassItemReadFrom : 720 -> 912
~ _AWDCoreRoutineSettingsClearAllReadFrom : 588 -> 708
~ _AWDCoreRoutineSettingsClusterLocationViewReadFrom : 936 -> 1208
~ _AWDCoreRoutineSettingsClusterLocationVisitViewReadFrom : 760 -> 956
~ _AWDCoreRoutineSettingsClusterViewReadFrom : 936 -> 1208
~ _AWDCoreRoutineSettingsDeleteTypeReadFrom : 760 -> 956
~ _AWDCoreRoutineSettingsEnableDisableReadFrom : 760 -> 956
~ _AWDCoreRoutineSettingsMapInteractionReadFrom : 936 -> 1208
~ _AWDCoreRoutineSettingsSessionDurationReadFrom : 936 -> 1208
~ _AWDCoreRoutineStateModelConfidenceReadFrom : 1052 -> 1400
~ _AWDCoreRoutineTrafficConditionsReadFrom : 1240 -> 1656
~ _AWDCoreRoutineTransitionMotionTypeReadFrom : 1384 -> 1864
~ _AWDCoreRoutineVisitReadFrom : 1068 -> 1340
~ _AWDDuetExpertCenterZKWOutcomeReadFrom : 1776 -> 2412
~ _AWDEventKitSyncCompletedNightlySyncReadFrom : 888 -> 1156
~ _AWDEventKitSyncIsNotifiableEventReadFrom : 1112 -> 1456
~ _AWDEventKitSyncSyncedAttendeeResponseFromWatchReadFrom : 720 -> 912
~ _AWDEventKitSyncSyncedEventCreatedOnWatchReadFrom : 720 -> 912
~ _AWDEventKitSyncSyncedTaskCreatedOnWatchReadFrom : 720 -> 912
~ _AWDFaceTimeCallAcceptReceivedReadFrom : 936 -> 1208
~ _AWDFaceTimeCallAcceptSentReadFrom : 1272 -> 1696
~ _AWDFaceTimeCallCancelSentReadFrom : 1452 -> 1952
~ _AWDFaceTimeCallConnectedReadFrom : 2320 -> 3176
~ _AWDFaceTimeCallDeclineSentReadFrom : 1452 -> 1952
~ _AWDFaceTimeCallEndedReadFrom : 7008 -> 9824
~ _AWDFaceTimeCallFailedReadFrom : 7008 -> 9824
~ _AWDFaceTimeCallInterruptionBeganReadFrom : 1452 -> 1952
~ _AWDFaceTimeCallInterruptionEndedReadFrom : 1624 -> 2200
~ _AWDFaceTimeCallInvitationReceivedReadFrom : 936 -> 1208
~ _AWDFaceTimeCallInvitationSentReadFrom : 1272 -> 1696
~ _AWDFaceTimeCallRelayInitiateReceivedReadFrom : 936 -> 1208
~ _AWDFaceTimeCallRelayInitiateSentReadFrom : 1272 -> 1696
~ _AWDFaceTimeCallRelayUpdateReceivedReadFrom : 936 -> 1208
~ _AWDFaceTimeCallRelayUpdateSentReadFrom : 1272 -> 1696
~ _AWDFaceTimeCallStartedReadFrom : 1452 -> 1952
~ _AWDHoneybeeSignatureReadFrom : 1160 -> 1348
~ _AWDIDSAppDeliveryReceiptReadFrom : 1268 -> 1692
~ _AWDIDSClientProcessReceivedMessageReadFrom : 1444 -> 1944
~ _AWDIDSCloudLinkReEstablishedReadFrom : 1052 -> 1400
~ _AWDIDSConnectedAfterPipeConnectedTimeInMsReadFrom : 720 -> 912
~ _AWDIDSDeviceConnectionDurationEventReadFrom : 2000 -> 2692
~ _AWDIDSDuplicatedMessageReadFrom : 536 -> 648
~ _AWDIDSExternalIPDetectionTimeReadFrom : 720 -> 912
~ _AWDIDSGenericConnectionSetupDurationEventReadFrom : 1400 -> 1896
~ _AWDIDSLocalDeliveryAppLevelAckReadFrom : 1100 -> 1448
~ _AWDIDSLocalDeliveryMessageDeliveredReadFrom : 1620 -> 2196
~ _AWDIDSLocalDeliveryMessageReceivedReadFrom : 1268 -> 1692
~ _AWDIDSLocalDeliveryMessageSentReadFrom : 1268 -> 1692
~ _AWDIDSLocalDeliverySocketClosedReadFrom : 2088 -> 2780
~ _AWDIDSLocalDeliverySocketOpenedReadFrom : 1380 -> 1804
~ _AWDIDSLocalMessageRTTReadFrom : 720 -> 912
~ _AWDIDSLocalMessageTimedOutReadFrom : 720 -> 912
~ _AWDIDSMagnetCorruptionReadFrom : 720 -> 912
~ _AWDIDSMagnetCorruptionDetailedReadFrom : 1384 -> 1864
~ _AWDIDSMagnetDataCorruptionRecoveryTimeInMsReadFrom : 720 -> 912
~ _AWDIDSMessageDeliveryPathReadFrom : 760 -> 956
~ _AWDIDSNoteMessageReceivedReadFrom : 1284 -> 1704
~ _AWDIDSOTRSessionNegotiationReadFrom : 1104 -> 1452
~ _AWDIDSOutgoingMessageDurationTraceReadFrom : 3692 -> 5224
~ _AWDIDSQRAllocationReadFrom : 1328 -> 1752
~ _AWDIDSQuickRelayReadFrom : 2424 -> 3376
~ _AWDIDSRealTimeEncryptionFirstReceivedPacketMKMTimeDeltaReadFrom : 936 -> 1208
~ _AWDIDSRealTimeEncryptionMembershipChangeEventFirstMKMTimeDeltaReadFrom : 936 -> 1208
~ _AWDIDSRealTimeEncryptionMissingPrekeysReadFrom : 932 -> 1204
~ _AWDIDSRegistrationAccountStatusReadFrom : 2160 -> 2932
~ _AWDIDSRegistrationAuthenticateReadFrom : 2160 -> 2932
~ _AWDIDSRegistrationAuthenticationParametersReceivedReadFrom : 876 -> 1148
~ _AWDIDSRegistrationCompletedReadFrom : 1272 -> 1696
~ _AWDIDSRegistrationControlChosenReadFrom : 1064 -> 1408
~ _AWDIDSRegistrationOperationReadFrom : 2160 -> 2932
~ _AWDIDSRegistrationPhoneNumberReceivedSMSReadFrom : 760 -> 956
~ _AWDIDSRegistrationPhoneNumberValidationFinishedReadFrom : 1104 -> 1452
~ _AWDIDSRegistrationProfileHandleOperationReadFrom : 1992 -> 2688
~ _AWDIDSRegistrationProfileOperationReadFrom : 1792 -> 2444
~ _AWDIDSRegistrationRenewCredentialsCompletedReadFrom : 936 -> 1208
~ _AWDIDSServerStorageStateMachineCompletedReadFrom : 1280 -> 1700
~ _AWDIDSSessionAcceptReceivedReadFrom : 588 -> 708
~ _AWDIDSSessionAcceptSentReadFrom : 588 -> 708
~ _AWDIDSSessionCancelReceivedReadFrom : 588 -> 708
~ _AWDIDSSessionCancelSentReadFrom : 936 -> 1208
~ _AWDIDSSessionCompletedReadFrom : 3780 -> 5264
~ _AWDIDSSessionConnectedReadFrom : 588 -> 708
~ _AWDIDSSessionDeclineReceivedReadFrom : 588 -> 708
~ _AWDIDSSessionDeclineSentReadFrom : 588 -> 708
~ _AWDIDSSessionEndedReadFrom : 4160 -> 5932
~ _AWDIDSSessionInvitationReceivedReadFrom : 588 -> 708
~ _AWDIDSSessionInvitationSentReadFrom : 760 -> 956
~ _AWDIDSSessionReinitiateConnectedReadFrom : 588 -> 708
~ _AWDIDSSessionReinitiateRequestedReadFrom : 588 -> 708
~ _AWDIDSSessionReinitiateStartedReadFrom : 588 -> 708
~ _AWDIDSSessionStartedReadFrom : 984 -> 1256
~ _AWDIDSSocketPairConnectionTCPInfoReadFrom : 1052 -> 1400
~ _AWDIDSStreamingReportReadFrom : 1744 -> 2292
~ _AWDIDSUniqueIncomingStreamIDsReadFrom : 720 -> 912
~ _AWDIDSWRMLinkRecommendationReadFrom : 1220 -> 1644
~ _AWDIDSWebTunnelRequestCompletedReadFrom : 1460 -> 1956
~ _AWDIDSWiFiSetupAttemptReadFrom : 1100 -> 1448
~ _AWDIDSWiProxConnectionFailedReadFrom : 720 -> 912
~ _AWDIDSWiProxConnectionSuccessReadFrom : 720 -> 912
~ _AWDIDSWiProxDidConnectToPeerReadFrom : 884 -> 1148
~ _AWDIDSWiProxDidDisconnectFromPeerReadFrom : 884 -> 1148
~ _AWDIDSWiProxDidSendDataReadFrom : 720 -> 912
~ _AWDIMessageAttachmentDownloadReadFrom : 2752 -> 3732
~ _AWDIMessageAttachmentUploadReadFrom : 3080 -> 4204
~ _AWDIMessageCloudKitAttachmentDownloadFailedReadFrom : 1384 -> 1808
~ _AWDIMessageCloudKitSyncFailedReadFrom : 1208 -> 1556
~ _AWDIMessageCloudKitValidatePurgeableAttachmentReadFrom : 1672 -> 2248
~ _AWDIMessageDeduplicatedReadFrom : 756 -> 952
~ _AWDIMessageDeliveredMessageReadFrom : 756 -> 952
~ _AWDIMessageDowngradeReadFrom : 936 -> 1208
~ _AWDIMessageHealthCheckPerformedReadFrom : 2476 -> 3464
~ _AWDIMessageNicknamePublishedReadFrom : 2044 -> 2736
~ _AWDIMessageNicknameRetrievedReadFrom : 1792 -> 2444
~ _AWDIMessageQueryFinishedReadFrom : 2320 -> 3176
~ _AWDIMessageReceivedMessageReadFrom : 1792 -> 2444
~ _AWDIMessageSentMessageReadFrom : 2152 -> 2932
~ _AWDSMSReceivedMessageReadFrom : 1624 -> 2200
~ _AWDSMSSentMessageReadFrom : 1792 -> 2444
~ _AWDIMRemoteURLLoadCompletedReadFrom : 2548 -> 3448
~ _AWDIMRemoteURLLoadFailedReadFrom : 2704 -> 3676
~ _AWDITesterAppStartReadFrom : 536 -> 648
~ _AWDITesterApplicationUUIDReadFrom : 588 -> 708
~ _AWDITesterApplyCustomInputsReadFrom : 536 -> 648
~ _AWDITesterCertApplePayTestFinishReadFrom : 976 -> 1172
~ _AWDITesterCertApplePayTestStartReadFrom : 636 -> 756
~ _AWDITesterCertApplePayTestSubmissionReadFrom : 692 -> 812
~ _AWDITesterCertHomeKitTestFinishReadFrom : 1080 -> 1276
~ _AWDITesterCertHomeKitTestStartReadFrom : 744 -> 864
~ _AWDITesterCertHomeKitTestSubmissionReadFrom : 744 -> 864
~ _AWDITesterCertTestFinishReadFrom : 868 -> 1060
~ _AWDITesterCertTestStartReadFrom : 692 -> 812
~ _AWDITesterCertTestSubmissionReadFrom : 692 -> 812
~ _AWDITesterTestFinishReadFrom : 820 -> 1012
~ _AWDITesterTestLoadReadFrom : 572 -> 684
~ _AWDITesterTestShareReadFrom : 636 -> 756
~ _AWDITesterTestStartReadFrom : 636 -> 756
~ _AWDLBClientConnectionReportReadFrom : 2332 -> 3124
~ _AWDLBConnectionReportReadFrom : 4228 -> 6052
~ _AWDLBEndpointsFetchReportReadFrom : 1388 -> 1888
~ _AWDLibnetcoreCellularFallbackReportReadFrom : 1848 -> 2408
~ _AWDLibnetcoreConnectionDataUsageSnapshotReadFrom : 1728 -> 2352
~ _AWDLibnetcoreConnectionStatisticsReportReadFrom : 8384 -> 11744
~ _AWDLibnetcoreMPTCPStatsReportReadFrom : 5236 -> 7404
~ _AWDLibnetcoreMbufStatsReportReadFrom : 1728 -> 2352
~ _AWDLibnetcoreNetworkdStatsReportReadFrom : 884 -> 1148
~ _AWDLibnetcoreRNFActivityNotificationReadFrom : 716 -> 908
~ _AWDLibnetcoreStatsReportReadFrom : 1472 -> 1652
~ _AWDLibnetcoreTCPConnectionReportReadFrom : 1436 -> 1764
~ _AWDLibnetcoreTCPECNInterfaceStatsReportReadFrom : 8276 -> 11812
~ _AWDLibnetcoreTCPECNStatsReportReadFrom : 3728 -> 5188
~ _AWDLibnetcoreTCPKernelStatsReadFrom : 2300 -> 3060
~ _AWDLibnetcoreTCPStatsReportReadFrom : 1728 -> 2352
~ _AWDLibnetcoreTCPTFOStatsReportReadFrom : 2124 -> 2824
~ _AWDMPTCPConnectionInterfaceReportReadFrom : 1884 -> 2516
~ _AWDMPTCPConnectionReportReadFrom : 2784 -> 3900
~ _AWDMPTCPSubflowSwitchingReportReadFrom : 820 -> 1012
~ _AWDNWAPIUsageReadFrom : 7636 -> 10744
~ _AWDNWAccumulatorReadFrom : 508 -> 544
~ _AWDNWActivityReadFrom : 1608 -> 2008
~ _AWDNWActivityEmptyTriggerReadFrom : 536 -> 648
~ _AWDNWActivityEpilogueReadFrom : 1712 -> 2188
~ _AWDNWConnectionReportReadFrom : 12904 -> 17960
~ _AWDNWDeviceReportReadFrom : 3480 -> 4756
~ _AWDNWDurationAccumulationReadFrom : 508 -> 544
~ _AWDNWDurationAccumulationStateReadFrom : 584 -> 704
~ _AWDNWL2ReportReadFrom : 3388 -> 4760
~ _AWDDNSDomainStatsReadFrom : 3568 -> 5024
~ _AWDMDNSResponderDNSMessageSizeStatsReadFrom : 1264 -> 1704
~ _AWDMDNSResponderDNSStatisticsReadFrom : 636 -> 756
~ _AWDMDNSResponderResolveStatsReadFrom : 716 -> 836
~ _AWDMDNSResponderResolveStatsDNSServerReadFrom : 752 -> 948
~ _AWDMDNSResponderResolveStatsDomainReadFrom : 508 -> 544
~ _AWDMDNSResponderResolveStatsHostnameReadFrom : 508 -> 544
~ _AWDMDNSResponderResolveStatsResultReadFrom : 932 -> 1204
~ _AWDMDNSResponderServicesStatsReadFrom : 708 -> 904
~ _AWDMMCSChunkingInfoReadFrom : 1568 -> 2064
~ _AWDMMCSErrorReadFrom : 684 -> 804
~ _AWDMMCSGetRequestInfoReadFrom : 2992 -> 3952
~ _AWDMMCSHttpInfoReadFrom : 5480 -> 7372
~ _AWDMMCSPutRequestInfoReadFrom : 3232 -> 4264
~ _AWDMMCSTcpInfoReadFrom : 7124 -> 10020
~ _AWDNanoPhoneEmergencyCallEndedReadFrom : 1420 -> 1904
~ _AWDNanoPhoneIncomingCallConnectedReadFrom : 1120 -> 1460
~ _AWDNanoPhoneIncomingCallPresentedReadFrom : 1120 -> 1460
~ _AWDNetworkServiceProxyConnectionStatisticsReadFrom : 4920 -> 6916
~ _AWDNetworkServiceProxyControlRequestStatisticsReadFrom : 2888 -> 4108
~ _AWDNetworkServiceProxyProbeStatisticsReadFrom : 1448 -> 1948
~ _AWDNetworkServiceProxyRequestStatisticsReadFrom : 3316 -> 4664
~ _AWDOSAnalyticsSubmissionsReadFrom : 1332 -> 1756
~ _AWDPairedSyncSyncReportReadFrom : 2364 -> 3192
~ _AWDAppBBPowerReadFrom : 756 -> 952
~ _AWDAppRRCConnectionStatsReadFrom : 1444 -> 1944
~ _AWDBacklightLuxMicroAmpsBucketReadFrom : 536 -> 648
~ _AWDBasebandPowerToolKPIsReadFrom : 6532 -> 9584
~ _AWDCpuLoadReadFrom : 584 -> 704
~ _AWDLQMDataTransferReadFrom : 1100 -> 1448
~ _AWDNetworkUsageReadFrom : 1272 -> 1696
~ _AWDPowerApMetricsReadFrom : 1388 -> 1888
~ _AWDPowerAppBBMetricsReadFrom : 636 -> 756
~ _AWDPowerAudioMetricsReadFrom : 1960 -> 2704
~ _AWDPowerBBAppRRCMetricsReadFrom : 808 -> 1004
~ _AWDPowerBBCallMetricInfoReadFrom : 1608 -> 2200
~ _AWDPowerBBCallMetricsReadFrom : 1700 -> 2248
~ _AWDPowerBBLQMDataTransferMetricsReadFrom : 1008 -> 1284
~ _AWDPowerBBNonDataMetricsReadFrom : 1564 -> 2140
~ _AWDPowerBBRATConnectedMetricsReadFrom : 636 -> 756
~ _AWDPowerBatteryMetricsReadFrom : 1908 -> 2636
~ _AWDPowerBluetoothMetricsReadFrom : 1564 -> 2140
~ _AWDPowerCameraMetricsReadFrom : 1052 -> 1400
~ _AWDPowerDisplayBacklightMetricsReadFrom : 4696 -> 6512
~ _AWDPowerNetworkUsageMetricsReadFrom : 636 -> 756
~ _AWDPowerPerProcessCPULoadMetricsReadFrom : 636 -> 756
~ _AWDPowerStateResidencyAndWeightReadFrom : 720 -> 912
~ _AWDPowerTouchMetricsReadFrom : 2152 -> 2880
~ _AWDPowerWifiMetricsReadFrom : 3552 -> 4944
~ _AWDRATConnectedPowerReadFrom : 884 -> 1148
~ _AWDPushConnectionConnectedReadFrom : 1624 -> 2200
~ _AWDPushConnectionDisconnectedReadFrom : 1452 -> 1952
~ _AWDPushFilterChangedReadFrom : 984 -> 1256
~ _AWDPushFilterSentReadFrom : 1104 -> 1452
~ _AWDPushKeepAliveFailedReadFrom : 2152 -> 2932
~ _AWDPushKeepAliveSentReadFrom : 2404 -> 3336
~ _AWDPushProxyManagerReceiveReadFrom : 984 -> 1256
~ _AWDPushProxyManagerSendReadFrom : 984 -> 1256
~ _AWDPushReceivedReadFrom : 1872 -> 2492
~ _AWDPushReceivedDroppedReadFrom : 1672 -> 2248
~ _AWDPushReceivedSlowReadFrom : 1672 -> 2248
~ _AWDPushSentReadFrom : 1872 -> 2492
~ _AWDPushTopicPolicyChangeReadFrom : 984 -> 1256
~ _AWDSafariActivatedHomeScreenQuickActionEventReadFrom : 708 -> 904
~ _AWDSafariAutoFillAuthenticationEventReadFrom : 1340 -> 1760
~ _AWDSafariAutoFillAuthenticationPreferenceEventReadFrom : 716 -> 908
~ _AWDSafariCKBookmarksMigrationFinishedEventReadFrom : 1152 -> 1500
~ _AWDSafariCKBookmarksMigrationStartedEventReadFrom : 1052 -> 1400
~ _AWDSafariCKBookmarksSyncEventReadFrom : 816 -> 1008
~ _AWDSafariContactAutoFillDidFillCustomContactSetEventReadFrom : 716 -> 908
~ _AWDSafariContactAutoFillDidSelectSetEventReadFrom : 888 -> 1156
~ _AWDSafariContactAutoFillDidShowSetsEventReadFrom : 892 -> 1156
~ _AWDSafariDedupedDAVBookmarksEventReadFrom : 884 -> 1148
~ _AWDSafariDidReceiveInvalidMessageFromWebProcessEventReadFrom : 588 -> 708
~ _AWDSafariDidTerminateWebProcessBeforeNavigationReadFrom : 708 -> 904
~ _AWDSafariDuplicatedPasswordsWarningEventReadFrom : 708 -> 904
~ _AWDSafariEnterPasswordsPreferencesEventReadFrom : 720 -> 912
~ _AWDSafariEnterTwoUpEventReadFrom : 708 -> 904
~ _AWDSafariInteractedWithGeneratedPasswordEventReadFrom : 708 -> 904
~ _AWDSafariPageLoadCompleteEventReadFrom : 1220 -> 1628
~ _AWDSafariPageLoadStartedEventReadFrom : 884 -> 1148
~ _AWDSafariParticipatedInPasswordAutoFillReadFrom : 708 -> 904
~ _AWDSafariReaderActiveOptInOutEventReadFrom : 708 -> 904
~ _AWDSafariReaderChangedOptInOutEventReadFrom : 708 -> 904
~ _AWDSafariSafeBrowsingUserActionAfterSeeingWarningEventReadFrom : 708 -> 904
~ _AWDSafariSafeBrowsingWarningShownEventReadFrom : 708 -> 904
~ _AWDSafariSelectedFavoritesGridItemEventReadFrom : 1564 -> 2140
~ _AWDSafariSetAutoFillQuickTypeSuggestionEventReadFrom : 876 -> 1148
~ _AWDSafariSharedPasswordEventReadFrom : 1052 -> 1400
~ _AWDSafariTappedAutoFillQuickTypeSuggestionEventReadFrom : 876 -> 1148
~ _AWDSafariTappedOnToolbarButtonEventReadFrom : 888 -> 1156
~ _AWDSafariTwoFingerTappedOnLinkEventReadFrom : 708 -> 904
~ _AWDSafariUnableToSilentlyMigrateToCKBookmarksEventReadFrom : 932 -> 1208
~ _AWDSafariUsingPrivateBrowsingEventReadFrom : 716 -> 908
~ _AWDSafariVersioningEventReadFrom : 760 -> 956
~ _AWDSafariViewControllerDismissedEventReadFrom : 708 -> 904
~ _AWDSafariViewControllerPresentedFromHostAppEventReadFrom : 588 -> 708
~ _AWDSafariViewControllerTappedOnToolbarButtonEventReadFrom : 888 -> 1156
~ _AWDSiriNetworkAnalyzerRunReadFrom : 2620 -> 3544
~ _AWDSiriRequestRecordReadFrom : 4864 -> 6752
~ _AWDSiriServerConnectionFailedReadFrom : 936 -> 1208
~ _AWDSiriServerConnectionOpenReadFrom : 876 -> 1148
~ _AWDSiriServerConnectionStartReadFrom : 536 -> 648
~ _AWDSiriSessionReadFrom : 1080 -> 1352
~ _AWDSiriSessionLoadTimeoutReadFrom : 1284 -> 1704
~ _AWDSiriSpeechRecognizedReadFrom : 884 -> 1148
~ _AWDSiriVoiceRecordingEndReadFrom : 720 -> 912
~ _AWDSiriVoiceRecordingStartReadFrom : 536 -> 648
~ _AWDSiriVoiceSendEndReadFrom : 720 -> 912
~ _AWDSiriVoiceSendStartReadFrom : 536 -> 648
~ _AWDTCPConnectionInfoReadFrom : 1556 -> 2108
~ _AWDTransportHistoryRecordReadFrom : 1320 -> 1744
~ _AWDSOSAutomaticCallCountdownEnabledReadFrom : 716 -> 908
~ _AWDSOSAutomaticNewtonEnabledReadFrom : 716 -> 908
~ _AWDSOSLongPressTriggersEmergencySOSReadFrom : 716 -> 908
~ _AWDSOSNumberOfVoiceLoopsReadFrom : 720 -> 912
~ _AWDSOSShouldPlayAudioDuringCountdownReadFrom : 716 -> 908
~ _AWDSOSTriggeredReadFrom : 708 -> 904
~ _AWDSpringBoardAppBrightnessReadFrom : 932 -> 1204
~ _AWDSpringBoardBiometricUnlockReadFrom : 720 -> 912
~ _AWDSpringBoardBreadcrumbReadFrom : 828 -> 1016
~ _AWDSpringBoardClawGestureReadFrom : 1420 -> 1904
~ _AWDSpringBoardDoNotDisturbChangeReadFrom : 720 -> 912
~ _AWDSpringBoardFolderStatsReadFrom : 1616 -> 2228
~ _AWDSpringBoardIconLaunchReadFrom : 1412 -> 1900
~ _AWDSpringBoardPressSequenceReadFrom : 1092 -> 1360
~ _AWDSpringBoardSOSAlertResponseReadFrom : 636 -> 756
~ _AWDSpringBoardSwitcherPresentationInteractionReadFrom : 768 -> 960
~ _AWDSpringBoardSwitcherToAppTransitionReadFrom : 944 -> 1212
~ _AWDSpringBoardSystemGestureReadFrom : 636 -> 756
~ _AWDTupleReadFrom : 720 -> 912
~ _AWDVPNSessionReadFrom : 2920 -> 4060
~ _AWDBTLEConnectionStatsReadFrom : 2124 -> 2824
~ _AWDChipCountersRxReadFrom : 3172 -> 4360
~ _AWDChipCountersTxReadFrom : 2468 -> 3296
~ _AWDChipErrorCountersTxReadFrom : 1220 -> 1628
~ _AWDControlFramesReadFrom : 1728 -> 2352
~ _AWDDataFramesReadFrom : 2704 -> 3676
~ _AWDHEStatsReadFrom : 4140 -> 5816
~ _AWDLinkQualityMeasurementsReadFrom : 16280 -> 23444
~ _AWDMacCountersRxReadFrom : 2704 -> 3676
~ _AWDMacCountersRxErrorsReadFrom : 1556 -> 2108
~ _AWDManagementFramesReadFrom : 2468 -> 3296
~ _AWDNwExclusionCountReadFrom : 884 -> 1148
~ _AWDOMICntrsReadFrom : 2124 -> 2824
~ _AWDRxPhyErrorsReadFrom : 884 -> 1148
~ _AWDScanStatsPerSliceReadFrom : 2076 -> 2792
~ _AWDSidecarBssSteeringReadFrom : 2548 -> 3448
~ _AWDSidecarHistogramBinReadFrom : 688 -> 952
~ _AWDSidecarPeerTrafficReadFrom : 1352 -> 1624
~ _AWDSlowWiFiNotificationReadFrom : 1400 -> 1896
~ _AWDSlowWiFiReportReadFrom : 724 -> 844
~ _AWDWAAssociatedAPInfoReadFrom : 424 -> 468
~ _AWDWADiagnosisActionAssociationDifferencesReadFrom : 1784 -> 2416
~ _AWDWAPeerDiscoveryInfoReadFrom : 1056 -> 1392
~ _AWDWAQuickDpsStatsReadFrom : 2628 -> 3548
~ _AWDWASymptomsDnsStatsReadFrom : 5156 -> 7164
~ _AWDWPA2CountersReadFrom : 2468 -> 3296
~ _AWDWiFiActionFrameEventReadFrom : 2892 -> 4044
~ _AWDWiFiAwdlSidecarReadFrom : 2552 -> 3372
~ _AWDWiFiAwdlSidecarCoalescedReadFrom : 3196 -> 4316
~ _AWDWiFiBlacklistingEventReadFrom : 1624 -> 2200
~ _AWDWiFiCLTMReadFrom : 636 -> 756
~ _AWDWiFiCLTMSliceSpecificReadFrom : 4248 -> 6108
~ _AWDWiFiConnectionQualityReadFrom : 6772 -> 9800
~ _AWDWiFiDPSAWDLSnapshotReadFrom : 1052 -> 1400
~ _AWDWiFiDPSActiveProbeStatsReadFrom : 1908 -> 2636
~ _AWDWiFiDPSBTSnapshotReadFrom : 876 -> 1148
~ _AWDWiFiDPSCountersSampleReadFrom : 732 -> 852
~ _AWDWiFiDPSEpilogueReadFrom : 2048 -> 2568
~ _AWDWiFiDPSNotificationReadFrom : 1064 -> 1408
~ _AWDWiFiDPSPerACTxCompletionSnapshotReadFrom : 2300 -> 3060
~ _AWDWiFiDPSReportReadFrom : 1072 -> 1192
~ _AWDWiFiDPSSnapshotReadFrom : 1052 -> 1020
~ _AWDWiFiLPMReportReadFrom : 5236 -> 7404
~ _AWDWiFiLTECoexBinReadFrom : 2468 -> 3296
~ _AWDWiFiLTECoexCountersReadFrom : 740 -> 860
~ _AWDWiFiLTECoexTxBlankingReadFrom : 1556 -> 2108
~ _AWDWiFiLTEWCI2CountersReadFrom : 2368 -> 3220
~ _AWDWiFiLTEWCI2CountersSliceSpecificReadFrom : 2300 -> 3060
~ _AWDWiFiLprxStatsReadFrom : 1564 -> 2140
~ _AWDWiFiMetric11axLinkChangeDataReadFrom : 8796 -> 12356
~ _AWDWiFiMetric11axStatsReadFrom : 644 -> 764
~ _AWDWiFiMetricActiveProbeStatsReadFrom : 2592 -> 3528
~ _AWDWiFiMetricCustomNetworkSettingReadFrom : 1740 -> 2392
~ _AWDWiFiMetricExtendedTrapInfoReadFrom : 5216 -> 7624
~ _AWDWiFiMetricHotspotTransportTypeReadFrom : 1052 -> 1400
~ _AWDWiFiMetricIPv4DHCPLatencyReadFrom : 1104 -> 1452
~ _AWDWiFiMetricInterfaceStatsReadFrom : 3072 -> 4236
~ _AWDWiFiMetricJoinTimeoutReadFrom : 2276 -> 3208
~ _AWDWiFiMetricLinkChangeDataReadFrom : 7756 -> 10968
~ _AWDWiFiMetricNetworkPrefsReadFrom : 2948 -> 4100
~ _AWDWiFiMetricRssiHistoryReadFrom : 3140 -> 4476
~ _AWDWiFiMetricScanStatsReadFrom : 636 -> 756
~ _AWDWiFiMetricWiFiStatsReadFrom : 644 -> 764
~ _AWDWiFiMetricWowStateReadFrom : 716 -> 908
~ _AWDWiFiMetricsAssociationHistoryReadFrom : 636 -> 756
~ _AWDWiFiMetricsAutoJoinNwExclusionReadFrom : 884 -> 1148
~ _AWDWiFiMetricsHealthUIEventReadFrom : 936 -> 1208
~ _AWDWiFiMetricsKnownNetworksEventReadFrom : 1872 -> 2492
~ _AWDWiFiMetricsManagerAssociationEventReadFrom : 816 -> 1012
~ _AWDWiFiMetricsManagerAutoJoinCumulativeReadFrom : 2640 -> 3688
~ _AWDWiFiMetricsManagerAutoJoinRecordReadFrom : 4124 -> 5828
~ _AWDWiFiMetricsManagerAutoJoinSessionReadFrom : 636 -> 756
~ _AWDWiFiMetricsManagerAwdlUsageReadFrom : 8152 -> 11328
~ _AWDWiFiMetricsManagerBGScanBlacklistedNetworksReadFrom : 688 -> 808
~ _AWDWiFiMetricsManagerBTCoexModeChangeReadFrom : 2152 -> 2880
~ _AWDWiFiMetricsManagerBTCoexStatsReadFrom : 6532 -> 9012
~ _AWDWiFiMetricsManagerBlacklistedNetworkInfoReadFrom : 864 -> 1060
~ _AWDWiFiMetricsManagerBlacklistingInstanceInfoReadFrom : 876 -> 1148
~ _AWDWiFiMetricsManagerChipCountersReadFrom : 1432 -> 1496
~ _AWDWiFiMetricsManagerChipMemoryReadFrom : 1564 -> 2140
~ _AWDWiFiMetricsManagerDeviceCountReadFrom : 1140 -> 1576
~ _AWDWiFiMetricsManagerEventReadFrom : 876 -> 1148
~ _AWDWiFiMetricsManagerFrameCounterStatsReadFrom : 1036 -> 1100
~ _AWDWiFiMetricsManagerInfraInterfaceReadFrom : 5360 -> 6880
~ _AWDWiFiMetricsManagerLastSSIDInfoReadFrom : 636 -> 756
~ _AWDWiFiMetricsManagerLeakyAPStatsReadFrom : 1152 -> 1500
~ _AWDWiFiMetricsManagerLinkQualityStatsReadFrom : 636 -> 756
~ _AWDWiFiMetricsManagerNetworkTransitionCumulativeReadFrom : 1104 -> 1456
~ _AWDWiFiMetricsManagerNetworkTransitionRecordReadFrom : 1972 -> 2736
~ _AWDWiFiMetricsManagerNetworkTransitionSessionReadFrom : 636 -> 756
~ _AWDWiFiMetricsManagerOneStatsAssociationInfoReadFrom : 872 -> 988
~ _AWDWiFiMetricsManagerP2pLegacyUsageReportReadFrom : 1224 -> 1648
~ _AWDWiFiMetricsManagerPowerStatsUpdateEventReadFrom : 1388 -> 1888
~ _AWDWiFiMetricsManagerPowerStickinessReadFrom : 876 -> 1148
~ _AWDWiFiMetricsManagerRCU1CoexModeChangeReadFrom : 2352 -> 3136
~ _AWDWiFiMetricsManagerRangingReportReadFrom : 3256 -> 4564
~ _AWDWiFiMetricsManagerRoamStatusReadFrom : 5728 -> 7956
~ _AWDWiFiMetricsManagerSoftErrorReadFrom : 3516 -> 4628
~ _AWDWiFiMetricsManagerSoftErrorUserFeedbackReadFrom : 1264 -> 1704
~ _AWDWiFiMetricsManagerStateMachineReadFrom : 708 -> 904
~ _AWDWiFiMetricsManagerUserBlacklistEventReadFrom : 1872 -> 2492
~ _AWDWiFiMetricsManagerWatchdogEventReadFrom : 3676 -> 4772
~ _AWDWiFiMetricsManagerWifidAvailabilityReadFrom : 804 -> 1080
~ _AWDWiFiMetricsScanObjReadFrom : 884 -> 1148
~ _AWDWiFiNWActivityReadFrom : 1204 -> 1288
~ _AWDWiFiNWActivityAggregateMetricsReadFrom : 4192 -> 5888
~ _AWDWiFiNWActivityAssocReadFrom : 6356 -> 9028
~ _AWDWiFiNWActivityBtCoexReadFrom : 3264 -> 4568
~ _AWDWiFiNWActivityBtCoexReqestReasonReadFrom : 2704 -> 3676
~ _AWDWiFiNWActivityControllerStatsReadFrom : 2868 -> 3728
~ _AWDWiFiNWActivityHistogramBinReadFrom : 584 -> 704
~ _AWDWiFiNWActivityImpedingFunctionsReadFrom : 4940 -> 6748
~ _AWDWiFiNWActivityInterfaceStatsReadFrom : 1352 -> 1604
~ _AWDWiFiNWActivityMpduLostReadFrom : 512 -> 556
~ _AWDWiFiNWActivityMpduWMEReadFrom : 1728 -> 2352
~ _AWDWiFiNWActivityPeerStatsReadFrom : 3136 -> 3936
~ _AWDWiFiNWActivityPerACTxCompletionsReadFrom : 3172 -> 4360
~ _AWDWiFiNWActivityPowerPStatsReadFrom : 720 -> 912
~ _AWDWiFiNWActivityPowerStatsReadFrom : 720 -> 912
~ _AWDWiFiNWActivityRateAndAggregationReadFrom : 2100 -> 2956
~ _AWDWiFiNWActivityScanActivityReadFrom : 2468 -> 3296
~ _AWDWiFiNWActivityStateBinReadFrom : 584 -> 704
~ _AWDWiFiNWActivityTrafficReadFrom : 708 -> 904
~ _AWDWiFiNWActivityTxCompletionsReadFrom : 2300 -> 3060
~ _AWDWiFiOtaSystemInfoReadFrom : 1476 -> 1736
~ _AWDWiFiP2PAirplayMetricsReadFrom : 5852 -> 8076
~ _AWDWiFiQualityScoreReadFrom : 1220 -> 1628
~ _AWDWiFiRangingRttDataReadFrom : 2860 -> 3904
~ _AWDWiFiRetStatsReadFrom : 884 -> 1148
~ _AWDWiFiSDBReadFrom : 808 -> 1004
~ _AWDWiFiSDBSliceSpecificReadFrom : 2592 -> 3528
~ _AWDWiFiSlowWiFiReportReadFrom : 812 -> 932
~ _AWDWiFiSoftAPReadFrom : 2924 -> 4008
~ _AWDWiFiSoftAPClientReadFrom : 1592 -> 2156
~ _AWDWiFiTDMReadFrom : 460 -> 496
~ _AWDWiFiTDMSliceReadFrom : 2504 -> 3368
~ _AWDWiFiTxInhibitEventReadFrom : 884 -> 1152
~ _AWDWiFiUIConfigureEventReadFrom : 936 -> 1208
~ _AWDWiFiUIEventReadFrom : 948 -> 1216
~ _AWDWiFiUIJoinEventReadFrom : 1084 -> 1356
~ _AWDWiFiUIScanCountReadFrom : 584 -> 704
~ _AWDWiFiUIScanSessionReadFrom : 868 -> 1064
~ _AWDWiFiUSBEventNotificationReadFrom : 1240 -> 1656
~ _AWDWiFiUsageSnapshotReadFrom : 876 -> 1148
~ _AWDWiFiWcpsStatsReadFrom : 7316 -> 10420
~ _AWDWifiAssociationReadFrom : 2096 -> 2788
~ _AWDWifiAwdlD2dMigrationStatsReadFrom : 1740 -> 2392
~ _AWDWifiAwdlHistogramBinReadFrom : 688 -> 952
~ _AWDWifiAwdlServiceRecordReadFrom : 1104 -> 1452
~ _AWDWifiAwdlStateInfoReadFrom : 708 -> 904
~ _AWDWifiHardwareVersionReadFrom : 588 -> 708
~ _AWDWifiLinkQualityRecordReadFrom : 5476 -> 7888
~ _AWDWifiMetricWiFiTetheredDeviceOUIReadFrom : 584 -> 704
~ _AWDWifiMostUsedNetworksReadFrom : 1780 -> 2424
~ _AWDWifiP2PAirplayHistogramBinReadFrom : 884 -> 1148
~ _AWDWifiPowerStateReadFrom : 716 -> 908
~ _AWDWifiStatsReadFrom : 2752 -> 3764
~ _AWDWifiCallingCallEndReportReadFrom : 3788 -> 5356
~ _AWDThroughputEvaluationReadFrom : 16400 -> 23192
~ _AWDWRMAntSelPolicyStatsReadFrom : 1240 -> 1656
~ _AWDWRMFacetimeRecommendationReadFrom : 5516 -> 7588
~ _AWDWRMLinkPrefChange1ReadFrom : 5276 -> 7380
~ _AWDWRMLinkPrefChange2ReadFrom : 4604 -> 6420
~ _AWDWRMLinkPrefChangeEventReadFrom : 7680 -> 10712
~ _AWDWRMLinkPrefInitReadFrom : 876 -> 1148
~ _AWDWRMLinkStateChangeReadFrom : 2824 -> 3872
~ _AWDWRMStreamingReportReadFrom : 2408 -> 3244
~ _AWDWRMULCACoexStatsReadFrom : 2164 -> 2888
~ _AWDWRMWiFiCallingEndReadFrom : 6436 -> 8852
~ _AWDWRMWiFiCell5GDataReadFrom : 9144 -> 12812
CStrings:
+ "_setError"
+ "getBytes:range:"
+ "position"
+ "setPosition:"

```
