## SessionSyncEngine

> `/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine`

```diff

-200.0.0.0.0
+200.100.0.0.0
   __TEXT.__text: 0x415ec
   __TEXT.__auth_stubs: 0xe80
   __TEXT.__objc_methlist: 0x70

   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_protorefs: 0x20
   __AUTH_CONST.__auth_got: 0x740
-  __AUTH_CONST.__auth_ptr: 0x3e0
+  __AUTH_CONST.__auth_ptr: 0x3e8
   __AUTH_CONST.__const: 0x1998
   __AUTH_CONST.__objc_const: 0x1ca0
   __AUTH.__objc_data: 0x90

   __DATA.__data: 0x700
   __DATA.__bss: 0x3500
   __DATA_DIRTY.__objc_data: 0x1a0
-  __DATA_DIRTY.__data: 0xd20
+  __DATA_DIRTY.__data: 0xd10
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1188
   Symbols:   209
-  CStrings:  0
+  CStrings:  446
 
CStrings:
+ ":"
+ "CaseSilentMode"
+ "N,V_unitTest_profileReadyObserverDidFinish"
+ "T@\"<HTDeveloperAppsFinderDelegate>\",W,N,V_delegate"
+ "T@\"HDAnalyticsDailyEventManager\",&,N,V_dailyAnalyticsManager"
+ "T@\"HDAppAnalyticsUpdateManager\",R,N,V_appAnalyticsUpdateManager"
+ "T@\"HDCloudSyncManager\",W,N,V_unitTest_cloudSyncManager"
+ "T@\"HDDataManager\",&,N,V_dataManager"
+ "T@\"HDDeviceContextStoreManager\",W,N,V_unitTest_deviceContextStoreManager"
+ "T@\"HDHAHealthAppApplicationInstallationManager\",&,N,V_appInstallationManager"
+ "T@\"HDHAHealthPluginHostFeedGenerator\",&,N,V_feedGenerator"
+ "T@\"HDHealthAppDataObserver\",&,N,V_dataObserver"
+ "T@\"HDHealthAppEmergencySOSManager\",&,N,V_emergencySOSManager"
+ "T@\"HDHealthAppLabConceptObserver\",&,N,V_labConceptObserver"
+ "T@\"HDHealthAppRestorableAlarmManager\",&,N,V_restorableAlarmManager"
+ "T@\"HDHealthAppSharingEntryObserver\",&,N,V_sharingEntryObserver"
+ "T@\"HDHealthAppSharingReminderRestorableAlarm\",&,N,V_sharableReminderAlarm"
+ "T@\"HDNotificationSyncClient\",&,N,V_healthAppNewDeviceNotificationSyncClient"
+ "T@\"HDNotificationSyncClient\",&,N,V_healthSharingNotificationSyncClient"
+ "T@\"HDSummarySharingEntryManager\",&,N,V_sharingEntryManager"
+ "T@\"HDUserDomainConceptManager\",&,N,V_userDomainConceptManager"
+ "T@\"HKCoreTelephonyClient\",&,N,V_coreTelephonyClient"
+ "T@\"HTHangSymbolicator\",R"
+ "T@\"HTProcessTerminationSettings\",R,N"
+ "T@\"LSApplicationRecord\",R,C,N,V_processRecord"
+ "T@\"NSArray\",&,N,V_allowedProcessNames"
+ "T@\"NSDate\",&,N,V_unitTest_currentDate"
+ "T@\"NSDictionary\",&,N,V_allowedSubReasons"
+ "T@\"NSMutableArray\",&,N,V_folderWatchDispatchSrcs"
+ "T@\"NSMutableDictionary\",&,N,V_logCountByPath"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_debounceQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_folderWatchTaskQueue"
+ "T@\"NSPredicate\",&,N,V_hangLogPredicate"
+ "T@\"NSSet\",&,N,V_observedProfileIdentifiers"
+ "T@\"NSString\",R,C,N,V_duration"
+ "T@\"NSString\",R,C,N,V_hangID"
+ "T@\"NSString\",R,C,N,V_hangId"
+ "T@\"NSString\",R,C,N,V_processBundleID"
+ "T@\"NSString\",R,C,N,V_processPath"
+ "T@\"NSString\",R,N,V_processPath"
+ "T@\"UNUserNotificationCenter\",&,N,V_unitTest_userNotificationCenter"
+ "T@\"UNUserNotificationCenter\",W,N,V_unitTest_userNotificationCenter"
+ "T@\"_HKDelayedOperation\",&,N,V_delayedOperation"
+ "T@?,C,N,V_logUpdateCallback"
+ "T@?,C,N,V_tailspinSavedCallback"
+ "TB,N,GisForceQuitDetectionEnabled,SsetForceQuitDetectionEnabled:"
+ "TB,N,GisHUDEnabled,SsetHUDEnabled:"
+ "TB,N,V_allowListingOnDemandVPNs"
+ "TB,N,V_allowsAllProcesses"
+ "TB,R,N,V_isLogFile"
+ "T{os_unfair_lock_s=I},N,V_observerLock"
+ "_alarmHandlers"
+ "_allowedReasons"
+ "_appAnalyticsUpdateManager"
+ "_appInstallationManager"
+ "_approximateDaysSinceLastAppOpen"
+ "_areHealthAppNotificationsAuthorized"
+ "_areTrendNotificationsEnabled"
+ "_dailyAnalyticsManager"
+ "_delayedOperation"
+ "_deviceContextStoreManager"
+ "_emergencySOSManager"
+ "_feedGenerator"
+ "_floorInteger:toSignificantFigures:"
+ "_handleCompletionWithAlarmEvent:success:error:restorableAlarmManager:completion:"
+ "_hangID"
+ "_hangId"
+ "_healthAppNewDeviceNotificationSyncClient"
+ "_healthSharingNotificationSyncClient"
+ "_isHealthAppOnboardedString"
+ "_isTimeInDaylightEnabledForDataSource:"
+ "_labConceptObserver"
+ "_logCountByPath"
+ "_observedProfileIdentifiers"
+ "_orchestrationConnection"
+ "_pluginHostConnection"
+ "_queue_removeAlarmEvent:"
+ "_queue_scheduleAlarmEvent:completion:"
+ "_rescheduleAlarmEvent:dueDate:completion:"
+ "_restorableAlarmManager"
+ "_scheduleAlarmEventWithHandler:dueDate:eventOptions:completion:"
+ "_sharableReminderAlarm"
+ "_sharingEntryObserver"
+ "_sharingKeyValueDomain"
+ "_supportsSecureContainer"
+ "_unitTest_cloudSyncManager"
+ "_unitTest_deviceContextStoreManager"
+ "_unitTest_profileReadyObserverDidFinish"
+ "_unitTest_userNotificationCenter"
+ "_welcomeFlowCompletedDate"
+ "acceptanceForAgreement:version:transaction:error:"
+ "acceptancesForAgreement:transaction:error:"
+ "actionIdentifierForOnboardingStatus:"
+ "allAcceptancesInTransaction:error:"
+ "allReasonsValue"
+ "clearPendingFollowUpItems"
+ "createAlarmEventWithIdentifier:dueDate:eventOptions:"
+ "createSharingReminderNotificationAndReturnError:"
+ "currentVersionForAgreement:"
+ "currentVersionImproveHealthAgreement"
+ "currentVersionImproveHealthRecords"
+ "deleteAcceptanceForAgreement:version:transaction:error:"
+ "deleteAcceptancesForAgreement:transaction:error:"
+ "es:"
+ "followUpItemDescription"
+ "getEmergencyOnboardingStatus"
+ "handleAlarmEvent:restorableAlarmManager:completion:"
+ "hangsDataEntryWithFullPath:extendedAttributes:cachedAppRecords:"
+ "initWithProfile:userNotificationCenter:"
+ "ionThresholdLSTM:"
+ "makeFollowUpItemWithActionIdentifier:"
+ "nextSharingReminderDateFromDate:"
+ "processBundleID"
+ "remote_applyDifferencesWithDifferences:inDomain:completion:"
+ "remote_fetchPinnedContentInDomain:withCompletion:"
+ "remote_movePinnedContentWithIdentifier:inDomain:toIndex:completion:"
+ "remote_pinContentWithIdentifier:inDomain:atIndex:completion:"
+ "remote_unpinAllContentInDomain:withCompletion:"
+ "setCancellationVelocityThreshold:"
+ "setCaseSound:"
+ "setChiralityLeftHandPresenceThresholdOverride:"
+ "setChiralityRightHandPresenceThresholdOverride:"
+ "setConnectedHeadphones:"
+ "setCrossedPinchMaxVelocity:"
+ "setDDFOVDistances:"
+ "setDDFOVNoiseValues:"
+ "setDSFOVDistances:"
+ "setDSFOVNoiseValues:"
+ "setDebug1:"
+ "setDetectionAvgBoneLengthOverride:"
+ "setDetectionChiralityThresholdOverride:"
+ "setDetectionConfidenceThresholdOverride:"
+ "setDetectionDepthNormalizationFactorOverride:"
+ "setDetectionGraphDeadline:"
+ "setDetectionInputImageStreams:"
+ "setDetectionLowerConfidenceThresholdOverride:"
+ "setDetectionSensitivityNoiseMagnitude:"
+ "setDetectionUvOThresholdOverride:"
+ "setDisabledHand:"
+ "setDoublePinchBreakThreshold:"
+ "setDroppingHandHDThreshold:"
+ "setDumpARKitResult:"
+ "setDumpFrequency:"
+ "setEnable640Mode:"
+ "setEnableActionBreakRangeFilter:"
+ "setEnableArmScroll:"
+ "setEnableCameraPairTransitionCorrection:"
+ "setEnableCameraSelectionHysteresis:"
+ "setEnableCoreAnalytics:"
+ "setEnableCrossedPinchCancellation:"
+ "setEnableDebugDataOutput:"
+ "setEnableDetectionSensitivity:"
+ "setEnableDoublePinchRecovery:"
+ "setEnableDoubleTrackerFilter:"
+ "setEnableDroppingHandCancellation:"
+ "setEnableEnrolment:"
+ "setEnableGestureRecognition:"
+ "setEnableGracefulFailureCloseToHMD:"
+ "setEnableGracefulFailureHandOutOfFOV:"
+ "setEnableInfieldCalibration:"
+ "setEnableLSTMCancellation:"
+ "setEnableMissingFinger:"
+ "setEnableNonlinearFusion:"
+ "setEnableObjectInteractionForActionForGeneralObject:"
+ "setEnableObjectInteractionForActionForPencilObject:"
+ "setEnableObjectInteractionState:"
+ "setEnableOverlappingHandsFilter:"
+ "setEnablePinchBreak:"
+ "setEnablePinchCancellation:"
+ "setEnablePosePrewiring:"
+ "setEnablePrewiring:"
+ "setEnableRepetitiveAccidentalSuppression:"
+ "setEnableScrollRecovery:"
+ "setEnableSelectionRecoveryInBreak:"
+ "setEnableSkipPose:"
+ "setEnableSlidingPinchCancellation:"
+ "setEnableTrackingSensitivity:"
+ "setEnableTurningPointFilterForSwipe:"
+ "setEnableTwoHandsOcclusionOnlyForNonDoubleTrackedHands:"
+ "setEnableTwoHandsOcclusionSuppressor:"
+ "setEnableTwoHandsOcclussionFilter:"
+ "setEnableUnsurePinchFilters:"
+ "setEnableUnsureScorePostProcessing:"
+ "setEnableWristScroll:"
+ "setEncodeInputImageJpeg:"
+ "setEstimatedBboxVisibilitySaturation:"
+ "setFOV2dCircles:"
+ "setFilterDetectedHandsByDistanceThresh:"
+ "setFilterInWorldCoordinates:"
+ "setFindMyNetworkEnable:"
+ "setFindMyNetworkSession:"
+ "setFindMyNetworkSupport:"
+ "setFindMyNetworkValueUpdated:"
+ "setForceQuitDetectionThreshold:"
+ "setGTInjections:"
+ "setHandCenterAngleDeadzone:"
+ "setHandCenterAngleGrayzone:"
+ "setHandCenterAngleGrayzoneReductionFactor:"
+ "setHandPresenceModel:"
+ "setHandRadius:"
+ "setHandsGraphType:"
+ "setHeightExtensionOfObjectProximityCone:"
+ "setInjectLeftHandsMissingFingerData:"
+ "setInputImageStreams:"
+ "setInputStreamKeyToSource:"
+ "setIsAirpods:"
+ "setIsCaseSoundSupported:"
+ "setIsResettingFindMyNetworkOnError:"
+ "setIsSettingCaseSoundValue:"
+ "setJointsObjectOcclusionThresholdOverride:"
+ "setLatents:"
+ "setLeftHandPreferredForEnrolment:"
+ "setLocalizer:"
+ "setMaxSwipeTurns:"
+ "setMaxUncertaintyForFetchBoneLength:"
+ "setMaximumAllowedHDForObjectProximityCone:"
+ "setMaximumObjectDistanceToJoints:"
+ "setMiddleDoubleTapBounceDist:"
+ "setMiddleDoubleTapBounceRiseFrac:"
+ "setMiddleDoubleTapHandInMotionDistThreshold:"
+ "setMiddleDoubleTapIdleAngle:"
+ "setMiddleDoubleTapIdleDist:"
+ "setMiddleDoubleTapIndexFingerProximityThreshold:"
+ "setMiddleDoubleTapJointOcclusionTheshold:"
+ "setMiddleDoubleTapJointUncertainityMax:"
+ "setMiddleDoubleTapMaxDropDur:"
+ "setMiddleDoubleTapMaxTapDistDiff:"
+ "setMiddleDoubleTapMaxTapDur:"
+ "setMiddleDoubleTapMinBounceDropDist:"
+ "setMiddleDoubleTapMinReadyDur:"
+ "setMiddleDoubleTapMinResetDur:"
+ "setMiddleDoubleTapMinSignalToNoiseRatio:"
+ "setMiddleDoubleTapMinTapDur:"
+ "setMiddleDoubleTapMinTapDurDiff:"
+ "setMiddleDoubleTapMinTravelDistNoiseRatio:"
+ "setMiddleDoubleTapNoiseWindowSize:"
+ "setMiddleDoubleTapReadyDist:"
+ "setMiddleDoubleTapRestingGestureMinIndexKnuckleVelocity:"
+ "setNumOfPreEnrolmentFrames:"
+ "setOOEDistanceThreshold:"
+ "setOOEVisibilityThreshold:"
+ "setObjectInteractionGeneralBreakThresholdOverride:"
+ "setObjectInteractionGeneralMakeThresholdOverride:"
+ "setObjectInteractionGeneralNumFramesBreakDelay:"
+ "setObjectInteractionGeneralNumFramesToEnableBreakDelay:"
+ "setObjectInteractionGeneralNumFramesToLockHighConfidence:"
+ "setObjectInteractionGeneralRequireConfidenceForBlockingAction:"
+ "setObjectInteractionPencilBreakThresholdOverride:"
+ "setObjectInteractionPencilMakeThresholdOverride:"
+ "setObjectInteractionPencilNumFramesBreakDelay:"
+ "setObjectInteractionPencilNumFramesToEnableBreakDelay:"
+ "setObjectInteractionPencilNumFramesToLockHighConfidence:"
+ "setObjectInteractionPencilRequireConfidenceForBlockingAction:"
+ "setObjectInteractionStateSupressPinchRecovery:"
+ "setOisDistanceToPreventEnterObjectInteractionStateAfterIntentional:"
+ "setOisEnterOISWhenEnterEatingMode:"
+ "setOisIntentionScoreThresholdToPreventStrictEatingMode:"
+ "setOisMaxMovementSecondAttemptExit:"
+ "setOisNearHandToMouthTracjectoryDistanceThreshold:"
+ "setOisNearHandToMouthTracjectoryTimeThreshold:"
+ "setOisPinchAcceptorDuringTouchOcclusionThreshold:"
+ "setOisPinchAcceptorHighIntentionMakeIntentionThresholds:"
+ "setOisPinchAcceptorHighIntentionMakeMinTouchFrameToAllowMakes:"
+ "setOisPinchAcceptorIgnoreSidePinch:"
+ "setOisPinchAcceptorMediumIntentionThreshold:"
+ "setOisPinchAcceptorMinDistanceToMouth:"
+ "setOisPinchAcceptorMinTouchFrameToAllowMake:"
+ "setOisPinchAcceptorScrollMovementRange:"
+ "setOisPinchAcceptorStaticHandHoverDistanceReductionThreshold:"
+ "setOisPinchAcceptorStaticHandIntentionThreshold:"
+ "setOisPinchAcceptorStrictIntentionThreshold:"
+ "setOisPinchAcceptorUsingUnsureCond:"
+ "setOisRecoveryPinchSuppressionInStrictEatingMode:"
+ "setOisSegmentationProcessingHeightRatio:"
+ "setOisSegmentationProcessingWidthRatio:"
+ "setOisStaticHandBufferLength:"
+ "setOisStaticHandMaxAngle:"
+ "setOisStaticHandMaxMovement:"
+ "setOisStrictEatingModeEnabled:"
+ "setOisStrictEatingModeNumberOfRepetitionsToEnter:"
+ "setOisTimeBetweenEating:"
+ "setOisTimeToReenterOisDueToRecentEating:"
+ "setOisTooFarHandToMouthTracjectoryDistanceThreshold:"
+ "setOisUseLstmInEatingModeOnly:"
+ "setOpenLoopErrorInjectionForTesting:"
+ "setOperationalEnvelopeEdgeThreshold:"
+ "setOutputRawPose:"
+ "setOverwrittenPinchBreakThreshold:"
+ "setOverwrittenPinchMakeThreshold:"
+ "setPendingConnectedHeadphones:"
+ "setPinchBreakModelName:"
+ "setPinchCancellationModelName:"
+ "setPinchIntentionModelName:"
+ "setPinchModel:"
+ "setPinchScoreSuppressionThreshold:"
+ "setPmeMediaEnabled:"
+ "setPmeVoiceEnabled:"
+ "setPoseCropMode:"
+ "setPoseFilter:"
+ "setPoseGraphDeadline:"
+ "setPoseModel:"
+ "setPosePipelineType:"
+ "setPoseSchedulerBboxVisibilityRequirement:"
+ "setPoseSchedulerBboxVisibilityTolerance:"
+ "setPoseStdDev:"
+ "setPredictionErroLutForSpeed:"
+ "setPressHoldAuto:"
+ "setPressHoldDefaults"
+ "setPressHoldNoiseCancel:"
+ "setPressHoldOff:"
+ "setPressHoldTransparency:"
+ "setPrintStatistics:"
+ "setRecoveryBreakUnsureScoreThreshold:"
+ "setRecoveryHighActionScoreFrames:"
+ "setRecoveryHighActionScoreThreshold:"
+ "setRecoveryMakeBreakSimilarityThreshold:"
+ "setRecoveryPinchHoverDistanceThreshold:"
+ "setRecoveryPinchIndexOcclusionThreshold:"
+ "setRecoveryPinchThumbOcclusionThreshold:"
+ "setRecoveryStationaryTapMovementRange:"
+ "setRelaxedBreakThreshold:"
+ "setRequiresAssociationHandPresenceThresholdOverride:"
+ "setRigidTransformJointVisibilityThreshold:"
+ "setSDFOVDistances:"
+ "setSDFOVNoiseValues:"
+ "setSchedulerInterval:"
+ "setSchedulerIntervalOneHand:"
+ "setSchedulerIntervalZeroHand:"
+ "setScrollBreakDistanceThreshold:"
+ "setSearchBreakThresholdRange:"
+ "setSearchMakeThresholdRange:"
+ "setSegmentationProcessingDeadline:"
+ "setSelectiveSpeechListening:"
+ "setSerializeInternalData:"
+ "setSerializeMesh:"
+ "setSerializeRawImages:"
+ "setSlidingFingerDistanceThreshold:"
+ "setSlidingPinchCounterThreshold:"
+ "setSlidingPinchThreshold:"
+ "setSpatialProfileExists:"
+ "setStripRawData:"
+ "setThreadSize:"
+ "setThresholdAdaptiveMakeRange:"
+ "setThresholdAngle:"
+ "setThresholdArmScrollDurationMax:"
+ "setThresholdArmScrollDurationMin:"
+ "setThresholdArmScrollWristPitch:"
+ "setThresholdBreakTipOcclusion:"
+ "setThresholdHandSpeed:"
+ "setThresholdHdDiff:"
+ "setThresholdKuckleDiff:"
+ "setThresholdOcclusion:"
+ "setThresholdPreciseBreakFrameBreakRange:"
+ "setThresholdPreciseBreakFrameRawActionScore:"
+ "setThresholdPreciseMakeFrameMakeRange:"
+ "setThresholdPreciseMakeFrameRawActionScore:"
+ "setThresholdScrollMaxPinchSpeedRecovery:"
+ "setThresholdScrollMinSwipeFramesRecovery:"
+ "setThresholdScrollPinchCentroidMovement:"
+ "setThresholdScrollPinkyKnuckleMovement:"
+ "setThresholdScrollRelativeSpeedRatioRecovery:"
+ "setThresholdTapDurationMax:"
+ "setThresholdTapHDVectorDiffAngle:"
+ "setThresholdTapHoverDistance:"
+ "setThresholdTapKuckleDiff:"
+ "setThresholdTapPalmOrientationDiff:"
+ "setThresholdTapPinchCentroidDiff:"
+ "setThresholdTapPinchCentroidMovement:"
+ "setThresholdTapPinkyKnuckleMovement:"
+ "setThsFroceFovContinuity:"
+ "setTimeToExitObjectInteractionStateAfterInactivity:"
+ "setTimeToUseHandCloseToMouthToGateObjectInteractionStates:"
+ "setTrackedSubReasons:forReason:"
+ "setTrackingHealthDriftAveragingFactor:"
+ "setTrackingHealthGhostHandAveragingFactor:"
+ "setTrackingHealthScoreEnableFovHysDis:"
+ "setTrackingHealthScoreFovHysDis:"
+ "setTrackingHealthSpeedAveragingFactor:"
+ "setTrackingSensitivityNoiseMagnitude:"
+ "setUberPoseModel:"
+ "setUnsureNetBreakThreshold:"
+ "setUnsureNetHDThreshold:"
+ "setUse30HzMemoryForSegmentation:"
+ "setUseAvgBoneLengthFromPose:"
+ "setUseBinned640Streams:"
+ "setUseBreakForTapRecovery:"
+ "setUseGeneralObjectProximityCone:"
+ "setUseHandCloseToMouthToGateObjectInteractionState:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateAllowEnterWithoutObject:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateHandToMouthDistanceThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateHandToMouthDistanceUpperThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateHandToMouthStrictDistanceThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateHoverDistanceThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateLastObjectInteractionTimeThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateMaxAllowedDistancesToMouthIncrease:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateMaxAllowedTimeNearMouth:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateMouthToHandTrajectoryDistanceThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateNumberOfRepetitionThresholds:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateRequireObjects:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateTrajectoryExtendFrames:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateTrajectoryHoverDistanceThreshold:"
+ "setUseHandCloseToMouthToGateObjectInteractionStateWithMaxAllowedTimeNearMouth:"
+ "setUseKalmanFiltering:"
+ "setUseMonoActionModel:"
+ "setUseMonoOnlineEnrollment:"
+ "setUseMonoUnsure:"
+ "setUseOIHSegmentationMask:"
+ "setUsePinchSuppressionAfterCancellation:"
+ "setUsePinchSuppressionAfterScrollBreak:"
+ "setUsePinchThresholdsSearch:"
+ "setUsePolarisWarperMesh:"
+ "setUseSegmentationOIHForObjectInteractionState:"
+ "setUseStaticHandStateForOIS:"
+ "setUseUnwarpedFrameForPose:"
+ "setUseWorldPoseInput:"
+ "setUvODcamLeftRotation:"
+ "setUvODcamRightRotation:"
+ "setUvOEnableForceDcamRotation:"
+ "setUvdJoints:"
+ "setUvdJointsStdDev:"
+ "setVelocityLimit:"
+ "setVisibilityThresholdOfROI:"
+ "setVolumeControlToggle:"
+ "setVolumeControlView:"
+ "setWristRotation:"
+ "setWristRotationStdDev:"
+ "setWristStdDevLowerThreshold:"
+ "setWristStdDevUpperThreshold:"
+ "shiftIntrinsics:"
+ "spatialProfileExists"
+ "symbolicateLogFiles:completion:"
+ "toJSONDataWithPrettyFormat:"
+ "toJSONString"
+ "topLevelUIHandler"
+ "tryToSerializeToData"
+ "unitTest_userNotificationCenter"
+ "unpairWithHpDevice:"
+ "unprojectPoint:andIntrinsics:andDistortion:andImageSize:forCameraModel:"
+ "updateDeviceConfigWithHpDevice:settings:"
+ "updateWithEnrolmentResults:"
+ "uvdJoints"
+ "validatePressHoldCombination"
+ "variance:ofSize:"
+ "volumeControlToggle"
+ "wristRotation"
+ "wristRotationStdDev"

```