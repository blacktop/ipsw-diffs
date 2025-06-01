## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x61744
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x6228
-  __TEXT.__oslogstring: 0x5cbf
-  __TEXT.__cstring: 0x77e5
+64.0.0.0.0
+  __TEXT.__text: 0x66624
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x64b0
+  __TEXT.__oslogstring: 0x5f57
+  __TEXT.__cstring: 0x7d30
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1124
-  __TEXT.__unwind_info: 0x16a4
-  __TEXT.__objc_classname: 0xeb2
-  __TEXT.__objc_methname: 0x13cfd
-  __TEXT.__objc_methtype: 0x1d33
-  __TEXT.__objc_stubs: 0xc6a0
+  __TEXT.__gcc_except_tab: 0x11d8
+  __TEXT.__unwind_info: 0x170c
+  __TEXT.__objc_classname: 0xe91
+  __TEXT.__objc_methname: 0x14b7f
+  __TEXT.__objc_methtype: 0x1e14
+  __TEXT.__objc_stubs: 0xcc60
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1a90
-  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__const: 0x1b70
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa310
-  __DATA_CONST.__objc_selrefs: 0x3718
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_const: 0xa7d8
+  __DATA_CONST.__objc_selrefs: 0x38a8
+  __DATA_CONST.__objc_arraydata: 0x168
   __AUTH_CONST.__objc_const: 0x3660
-  __AUTH_CONST.__cfstring: 0x5a60
-  __AUTH_CONST.__objc_intobj: 0x2a0
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__cfstring: 0x5ee0
+  __AUTH_CONST.__objc_intobj: 0x2d0
+  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_classrefs: 0x658
+  __DATA.__objc_classrefs: 0x660
   __DATA.__objc_superrefs: 0x2c8
-  __DATA.__objc_ivar: 0x814
+  __DATA.__objc_ivar: 0x878
   __DATA.__data: 0xb40
   __DATA.__bss: 0x3c
-  __DATA_DIRTY.__objc_data: 0x2030
+  __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AAAA4B1-1618-3266-A850-B81FF8398885
-  Functions: 2356
-  Symbols:   8594
-  CStrings:  5057
+  UUID: E9BC5D7E-888E-31D7-8032-64D6E8AC37ED
+  Functions: 2422
+  Symbols:   8801
+  CStrings:  5244
 
Symbols:
+ +[IRAVOutputDeviceDO aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:]
+ +[IRHistoryEventDO historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:]
+ +[IRMiLoPredictionEventDO miLoPredictionEventDOWithLabel:predictionId:]
+ +[IRRuleHistoryPattern filterHistoryByBrokeredDeviceScan:]
+ +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:]
+ +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:].cold.1
+ +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:].cold.2
+ +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:].cold.3
+ +[IRServiceStore adjustDBToStaticTokens:]
+ +[IRSessionServer isGlobalLowLatencyMiLoWithPersistenceManager:]
+ +[IRSystemStateDO systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:]
+ +[NSDate(IRExntensions) daysFromDate:toDate:]
+ -[IRAVOutputDeviceDO copyWithReplacementDiscoveredWithBroker:]
+ -[IRAVOutputDeviceDO discoveredWithBroker]
+ -[IRAVOutputDeviceDO initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:]
+ -[IRCMPDRFenceBridge dealloc]
+ -[IRCandidateClassificationDetectorSameSpace _isSameSpaceBasedOnPDRFenceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:]
+ -[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:]
+ -[IRCandidateDO(Extensions) isBrokeredDevice]
+ -[IRCandidateInspectionGenerator initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnBrokeredLOI:sameSpaceBasedOnPDRFence:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:]
+ -[IRCandidateInspectionGenerator sameSpaceBasedOnBrokeredLOI]
+ -[IRCandidateInspectionGenerator sameSpaceBasedOnPDRFence]
+ -[IRCandidateInspectionGenerator setSameSpaceBasedOnBrokeredLOI:]
+ -[IRCandidateInspectionGenerator setSameSpaceBasedOnPDRFence:]
+ -[IRCandidateManager deleteBrokerCandidates]
+ -[IRCandidateSelector _selectBasedOnMostRecentMainBrokeredDeviceFromCandidates:withSystemState:andHistoryEventsAsc:andDate:]
+ -[IRCandidateSelector candidateSelectorReasonBrokeredMainDeviceFirstUse]
+ -[IRCandidateSelector setCandidateSelectorReasonBrokeredMainDeviceFirstUse:]
+ -[IRCandidateWrapper isCallToAction]
+ -[IRCandidateWrapper sameSpaceBasedOnBrokeredLOI]
+ -[IRCandidateWrapper sameSpaceBasedOnPDRFence]
+ -[IRCandidateWrapper setIsCallToAction:]
+ -[IRCandidateWrapper setSameSpaceBasedOnBrokeredLOI:]
+ -[IRCandidateWrapper setSameSpaceBasedOnPDRFence:]
+ -[IRCandidatesContainerDO(Extension) candidateForCandidateIdentifier:]
+ -[IRClassificatonGenerator _nominateCallToActionForCandidate:withHistoryEventsAsc:andSystemState:]
+ -[IREligibilitySettings setUseBrokeredScanForMain:]
+ -[IREligibilitySettings setUseBrokeredScanForSecondary:]
+ -[IREligibilitySettings useBrokeredScanForMain]
+ -[IREligibilitySettings useBrokeredScanForSecondary]
+ -[IRHistoryEventDO copyWithReplacementSharingPolicy:]
+ -[IRHistoryEventDO initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:]
+ -[IRHistoryEventDO sharingPolicy]
+ -[IRHistoryManager addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:shouldLabelEventWithMilo:]
+ -[IRMiLoConnectionBridge enableMiLoAtCurrentLocation]
+ -[IRMiLoPredictionEventDO initWithLabel:predictionId:]
+ -[IRMiLoProvider requestSinglePredictionIdentifier]
+ -[IRMiLoProvider requestSinglePrediction]
+ -[IRMiLoProvider requestSpotOnLocationIdentifier]
+ -[IRMiLoProvider resetSpotOnLocationRequest]
+ -[IRMiLoProvider setRequestSinglePredictionIdentifier:]
+ -[IRMiLoProvider setRequestSpotOnLocationIdentifier:]
+ -[IRMiLoProvider setSpotOnLocation]
+ -[IRMiLoProvider setSpotOnLocation].cold.1
+ -[IRMiLoProvider startLowLatencyMiLo]
+ -[IRMiLoProvider startLowLatencyMiLo].cold.1
+ -[IRMiLoProvider startLowLatencyMiLo].cold.2
+ -[IRPolicyManager _checkAndStartLowLatencyMiLoIfNeededWithForce:]
+ -[IRPolicyManager didSpotOnLocationComplete:]
+ -[IRPolicyManager setSpotOnLocationWithParameters:andClientID:]
+ -[IRPolicyManager setSpotOnPendingClientIDs:]
+ -[IRPolicyManager setSpotOnTimeout:]
+ -[IRPolicyManager spotOnPendingClientIDs]
+ -[IRPolicyManager spotOnTimeout]
+ -[IRPreferences brokeredUseScansForEligibilityOfMainDevice]
+ -[IRPreferences brokeredUseScansForEligibilityOfSecondaryDevice]
+ -[IRPreferences candidateSelectorAllowSelectByLOI]
+ -[IRPreferences candidateSelectorCallToActionAppearThreshold]
+ -[IRPreferences candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents]
+ -[IRPreferences candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds]
+ -[IRPreferences loiSameSpaceEventsNumberOfEventsToWatch]
+ -[IRPreferences loiSameSpaceEventsTimeIntervalSeconds]
+ -[IRPreferences loiSameSpaceOverrideBrokerForAVODIDArray]
+ -[IRPreferences loiSameSpaceOverrideBrokerForCandidateIDArray]
+ -[IRPreferences miloRoomDetectionInCustomLOIEnabled]
+ -[IRPreferences miloTimeoutForSetSpotOnRequestSeconds]
+ -[IRPreferences pdrFenceCandidateSelectorAllowSelectByFence]
+ -[IRPreferences pdrFenceOtherThanRadiusTimeoutInSeconds]
+ -[IRPreferences pdrFenceRadiusInMeters]
+ -[IRPreferences pdrFenceRadiusTimeoutInSeconds]
+ -[IRReplayDatabaseHandler getSortedHistoryEventsForServiceIdentifier:].cold.1
+ -[IRServiceContainer setSpotOnLocationWithParameters:andClientID:]
+ -[IRServiceContainer(IRPolicyManagerDelegate) policyManager:didSpotOnLocationCompleteForClientIds:withError:]
+ -[IRServicePackageAdapterAppleTVControl filterHistory:withCandidatesContainer:]
+ -[IRServicePackageAdapterMedia filterHistory:withCandidatesContainer:]
+ -[IRServicePackageAdapterMedia shouldRejectEvent:withHistoryEventsContainer:]
+ -[IRSessionClientProxy _didSpotOnLocationComplete:]
+ -[IRSessionConnection _serviceIdentifierForClientIdentifier:]
+ -[IRSessionConnection _setSpotOnLocationWithParameters:]
+ -[IRSessionConnection didSpotOnLocationComplete:]
+ -[IRSessionServer(IRServiceContainerDelegate) serviceContainer:didSpotOnLocationCompleteForClientIds:withError:]
+ -[IRSystemStateDO copyWithReplacementPdrFenceActive:]
+ -[IRSystemStateDO initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:]
+ -[IRSystemStateDO pdrFenceActive]
+ -[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]
+ -[IRSystemStateManager _checkAndStopPDRFenceLogicIfNeeded]
+ -[IRSystemStateManager addEvent:forCandidate:]
+ -[IRSystemStateManager didSpotOnLocationCompleteWithError:]
+ -[IRSystemStateManager pdrFenceBridge]
+ -[IRSystemStateManager pdrFenceTimer]
+ -[IRSystemStateManager setPdrFenceBridge:]
+ -[IRSystemStateManager setPdrFenceTimer:]
+ GCC_except_table11
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table25
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table53
+ _IRAVInitialRouteSharingPolicyForBundleIdentifier
+ _IRContextChangeReasonDeleteBrokerCandidates
+ _IRContextChangeReasonPDRFenceCrossed
+ _OBJC_CLASS_$_CLMiLoCustomLoiConfiguration
+ _OBJC_CLASS_$_IRConfiguration
+ _OBJC_IVAR_$_IRAVOutputDeviceDO._discoveredWithBroker
+ _OBJC_IVAR_$_IRCandidateInspectionGenerator._sameSpaceBasedOnBrokeredLOI
+ _OBJC_IVAR_$_IRCandidateInspectionGenerator._sameSpaceBasedOnPDRFence
+ _OBJC_IVAR_$_IRCandidateSelector._candidateSelectorReasonBrokeredMainDeviceFirstUse
+ _OBJC_IVAR_$_IRCandidateWrapper._isCallToAction
+ _OBJC_IVAR_$_IRCandidateWrapper._sameSpaceBasedOnBrokeredLOI
+ _OBJC_IVAR_$_IRCandidateWrapper._sameSpaceBasedOnPDRFence
+ _OBJC_IVAR_$_IREligibilitySettings._useBrokeredScanForMain
+ _OBJC_IVAR_$_IREligibilitySettings._useBrokeredScanForSecondary
+ _OBJC_IVAR_$_IRHistoryEventDO._sharingPolicy
+ _OBJC_IVAR_$_IRMiLoProvider._requestSinglePredictionIdentifier
+ _OBJC_IVAR_$_IRMiLoProvider._requestSpotOnLocationIdentifier
+ _OBJC_IVAR_$_IRPolicyManager._spotOnPendingClientIDs
+ _OBJC_IVAR_$_IRPolicyManager._spotOnTimeout
+ _OBJC_IVAR_$_IRPreferences._brokeredUseScansForEligibilityOfMainDevice
+ _OBJC_IVAR_$_IRPreferences._brokeredUseScansForEligibilityOfSecondaryDevice
+ _OBJC_IVAR_$_IRPreferences._candidateSelectorAllowSelectByLOI
+ _OBJC_IVAR_$_IRPreferences._candidateSelectorCallToActionAppearThreshold
+ _OBJC_IVAR_$_IRPreferences._candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents
+ _OBJC_IVAR_$_IRPreferences._candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds
+ _OBJC_IVAR_$_IRPreferences._loiSameSpaceEventsNumberOfEventsToWatch
+ _OBJC_IVAR_$_IRPreferences._loiSameSpaceEventsTimeIntervalSeconds
+ _OBJC_IVAR_$_IRPreferences._loiSameSpaceOverrideBrokerForAVODIDArray
+ _OBJC_IVAR_$_IRPreferences._loiSameSpaceOverrideBrokerForCandidateIDArray
+ _OBJC_IVAR_$_IRPreferences._miloRoomDetectionInCustomLOIEnabled
+ _OBJC_IVAR_$_IRPreferences._miloTimeoutForSetSpotOnRequestSeconds
+ _OBJC_IVAR_$_IRPreferences._pdrFenceCandidateSelectorAllowSelectByFence
+ _OBJC_IVAR_$_IRPreferences._pdrFenceOtherThanRadiusTimeoutInSeconds
+ _OBJC_IVAR_$_IRPreferences._pdrFenceRadiusInMeters
+ _OBJC_IVAR_$_IRPreferences._pdrFenceRadiusTimeoutInSeconds
+ _OBJC_IVAR_$_IRSystemStateDO._pdrFenceActive
+ _OBJC_IVAR_$_IRSystemStateManager._pdrFenceBridge
+ _OBJC_IVAR_$_IRSystemStateManager._pdrFenceTimer
+ __OBJC_$_CLASS_METHODS_IRSessionServer(IRServiceContainerDelegate)
+ ___112-[IRSessionServer(IRServiceContainerDelegate) serviceContainer:didSpotOnLocationCompleteForClientIds:withError:]_block_invoke
+ ___112-[IRSessionServer(IRServiceContainerDelegate) serviceContainer:didSpotOnLocationCompleteForClientIds:withError:]_block_invoke_2
+ ___124-[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:]_block_invoke
+ ___166-[IRClassificatonGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.36
+ ___41+[IRServiceStore adjustDBToStaticTokens:]_block_invoke
+ ___41+[IRServiceStore adjustDBToStaticTokens:]_block_invoke_2
+ ___44-[IRCandidateManager deleteBrokerCandidates]_block_invoke
+ ___44-[IRCandidateManager deleteBrokerCandidates]_block_invoke_2
+ ___45-[IRCandidateDO(Extensions) isBrokeredDevice]_block_invoke
+ ___45-[IRCleanupManager _handleCleanupXPCActivity]_block_invoke.24
+ ___63-[IRPolicyManager setSpotOnLocationWithParameters:andClientID:]_block_invoke
+ ___66-[IRServiceContainer setSpotOnLocationWithParameters:andClientID:]_block_invoke
+ ___70-[IRCandidatesContainerDO(Extension) candidateForCandidateIdentifier:]_block_invoke
+ ___70-[IRServicePackageAdapterMedia filterHistory:withCandidatesContainer:]_block_invoke
+ ___82-[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]_block_invoke
+ ___82-[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]_block_invoke.18
+ ___82-[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e32_v24?0"IRCandidateWrapper"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_33_e35_v32?0"IRServiceContainer"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e28_v32?0"IRServiceMO"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e22_v24?0"IRNodeDO"8^B16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e28_v32?0"IRServiceDO"8Q16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e33_v32?0"IRHistoryEventDO"8Q16^B24lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e26_B16?0"IRHistoryEventDO"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r80r_e33_v32?0"IRHistoryEventDO"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e26_B16?0"IRHistoryEventDO"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.123
+ ___block_literal_global.135
+ ___block_literal_global.199
+ ___block_literal_global.31
+ ___block_literal_global.38
+ ___block_literal_global.49
+ ___block_literal_global.85
+ __unnamed_array_storage.70
+ _objc_msgSend$_checkAndStartLowLatencyMiLoIfNeededWithForce:
+ _objc_msgSend$_checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:
+ _objc_msgSend$_checkAndStopPDRFenceLogicIfNeeded
+ _objc_msgSend$_didSpotOnLocationComplete:
+ _objc_msgSend$_isSameSpaceBasedOnPDRFenceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:
+ _objc_msgSend$_isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:
+ _objc_msgSend$_nominateCallToActionForCandidate:withHistoryEventsAsc:andSystemState:
+ _objc_msgSend$_selectBasedOnMostRecentMainBrokeredDeviceFromCandidates:withSystemState:andHistoryEventsAsc:andDate:
+ _objc_msgSend$_serviceIdentifierForClientIdentifier:
+ _objc_msgSend$aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:
+ _objc_msgSend$addEvent:forCandidate:
+ _objc_msgSend$addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:shouldLabelEventWithMilo:
+ _objc_msgSend$adjustDBToStaticTokens:
+ _objc_msgSend$brokeredUseScansForEligibilityOfMainDevice
+ _objc_msgSend$brokeredUseScansForEligibilityOfSecondaryDevice
+ _objc_msgSend$candidateSelectorAllowSelectByLOI
+ _objc_msgSend$candidateSelectorCallToActionAppearThreshold
+ _objc_msgSend$candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents
+ _objc_msgSend$candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds
+ _objc_msgSend$candidateSelectorReasonBrokeredMainDeviceFirstUse
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$copyWithReplacementPdrFenceActive:
+ _objc_msgSend$createCustomLocationOfInterestAtCurrentLocationWithConfiguration:
+ _objc_msgSend$createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:
+ _objc_msgSend$day
+ _objc_msgSend$daysFromDate:toDate:
+ _objc_msgSend$deleteBrokerCandidates
+ _objc_msgSend$didSpotOnLocationComplete:
+ _objc_msgSend$didSpotOnLocationCompleteWithError:
+ _objc_msgSend$discoveredWithBroker
+ _objc_msgSend$enableMiLoAtCurrentLocation
+ _objc_msgSend$filterHistory:withCandidatesContainer:
+ _objc_msgSend$filterHistoryByBrokeredDeviceScan:
+ _objc_msgSend$historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:
+ _objc_msgSend$initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:
+ _objc_msgSend$initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnBrokeredLOI:sameSpaceBasedOnPDRFence:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:
+ _objc_msgSend$initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:
+ _objc_msgSend$initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:
+ _objc_msgSend$initWithEnableInRoomDetection:
+ _objc_msgSend$initWithLabel:predictionId:
+ _objc_msgSend$initWithServiceToken:
+ _objc_msgSend$isBrokeredDevice
+ _objc_msgSend$isCallToAction
+ _objc_msgSend$loiSameSpaceEventsNumberOfEventsToWatch
+ _objc_msgSend$loiSameSpaceEventsTimeIntervalSeconds
+ _objc_msgSend$loiSameSpaceOverrideBrokerForAVODIDArray
+ _objc_msgSend$loiSameSpaceOverrideBrokerForCandidateIDArray
+ _objc_msgSend$miLoPredictionEventDOWithLabel:predictionId:
+ _objc_msgSend$miloRoomDetectionInCustomLOIEnabled
+ _objc_msgSend$miloTimeoutForSetSpotOnRequestSeconds
+ _objc_msgSend$pdrFenceActive
+ _objc_msgSend$pdrFenceBridge
+ _objc_msgSend$pdrFenceCandidateSelectorAllowSelectByFence
+ _objc_msgSend$pdrFenceOtherThanRadiusTimeoutInSeconds
+ _objc_msgSend$pdrFenceRadiusInMeters
+ _objc_msgSend$pdrFenceRadiusTimeoutInSeconds
+ _objc_msgSend$pdrFenceTimer
+ _objc_msgSend$policyManager:didSpotOnLocationCompleteForClientIds:withError:
+ _objc_msgSend$requestSinglePrediction
+ _objc_msgSend$requestSinglePredictionIdentifier
+ _objc_msgSend$requestSpotOnLocationIdentifier
+ _objc_msgSend$resetAllBrokerDiscoveredCandidates
+ _objc_msgSend$resetSpotOnLocationRequest
+ _objc_msgSend$sameSpaceBasedOnBrokeredLOI
+ _objc_msgSend$sameSpaceBasedOnPDRFence
+ _objc_msgSend$serviceContainer:didSpotOnLocationCompleteForClientIds:withError:
+ _objc_msgSend$setCandidateSelectorReasonBrokeredMainDeviceFirstUse:
+ _objc_msgSend$setDiscoveredWithBroker:
+ _objc_msgSend$setIsCallToAction:
+ _objc_msgSend$setPdrFenceActive:
+ _objc_msgSend$setPdrFenceBridge:
+ _objc_msgSend$setPdrFenceTimer:
+ _objc_msgSend$setRequestSinglePredictionIdentifier:
+ _objc_msgSend$setRequestSpotOnLocationIdentifier:
+ _objc_msgSend$setSameSpaceBasedOnBrokeredLOI:
+ _objc_msgSend$setSameSpaceBasedOnPDRFence:
+ _objc_msgSend$setSharingPolicy:
+ _objc_msgSend$setSpotOnLocation
+ _objc_msgSend$setSpotOnLocationWithParameters:andClientID:
+ _objc_msgSend$setSpotOnPendingClientIDs:
+ _objc_msgSend$setSpotOnTimeout:
+ _objc_msgSend$setUseBrokeredScanForMain:
+ _objc_msgSend$setUseBrokeredScanForSecondary:
+ _objc_msgSend$sharingPolicy
+ _objc_msgSend$spotOnPendingClientIDs
+ _objc_msgSend$spotOnTimeout
+ _objc_msgSend$systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:
+ _objc_msgSend$useBrokeredScanForMain
+ _objc_msgSend$useBrokeredScanForSecondary
- +[IRAVOutputDeviceDO aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:]
- +[IRHistoryEventDO historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:]
- +[IRMiLoPredictionEventDO miLoPredictionEventDOWithLabel:predictionId:labelRealTime:predictionIdRealTime:]
- +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:]
- +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:].cold.1
- +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:].cold.2
- +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:].cold.3
- +[IRServiceContainer createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:].cold.4
- +[IRSessionConnectionAllowedClients allowedClientsToCreateServiceOnRun]
- +[IRSystemStateDO systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:]
- -[IRAVOutputDeviceDO initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:]
- -[IRCandidateInspectionGenerator initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:]
- -[IRCandidateManager candidateForCandidateIdentifier:]
- -[IRHistoryEventDO initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:]
- -[IRHistoryManager addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:andMiloPredictionRealTime:shouldLabelEventWithMilo:]
- -[IRHistoryManager lastMiLoLabelRealTime]
- -[IRHistoryManager setLastMiLoLabelRealTime:]
- -[IRMiLoPredictionEventDO copyWithReplacementLabelRealTime:]
- -[IRMiLoPredictionEventDO copyWithReplacementPredictionIdRealTime:]
- -[IRMiLoPredictionEventDO initWithLabel:predictionId:labelRealTime:predictionIdRealTime:]
- -[IRMiLoPredictionEventDO labelRealTime]
- -[IRMiLoPredictionEventDO predictionIdRealTime]
- -[IRMiLoProvider isRealTimeMiLoRequestedForPowerOptimizations]
- -[IRMiLoProvider requestSinglePredictionIdentifierRealTime]
- -[IRMiLoProvider requestSinglePredictionRealTime]
- -[IRMiLoProvider setIsRealTimeMiLoRequestedForPowerOptimizations:]
- -[IRMiLoProvider setRequestSinglePredictionIdentifierRealTime:]
- -[IRMiLoProvider startLowLatencyMiLoAndRequestSinglePredictionRealTime:]
- -[IRMiLoProvider startLowLatencyMiLoAndRequestSinglePredictionRealTime:].cold.1
- -[IRMiLoProvider startLowLatencyMiLoAndRequestSinglePredictionRealTime:].cold.2
- -[IRPolicyManager _checkAndStartLowLatencyMiLoIfNeeded]
- -[IRPolicyManager _handleMiLoRealTimeUponAddEvent:]
- -[IRPolicyManager _handleMiLoRealTimeUponContextChange]
- -[IRPolicyManager _handleMiLoRealTimeUponRequestCurrentContext]
- -[IRPolicyManager didReceiveMiloPredictionRealTime]
- -[IRPreferences controlledLiveOnMiLoRealTimeUponRequestCurrentContext]
- -[IRPreferences liveOnMiloEnableRealTimeDeprecated]
- -[IRReplayDatabaseHandler getSortedHistoryEventsForServiceIdentifier:useRealTimeMilo:]
- -[IRReplayDatabaseHandler getSortedHistoryEventsForServiceIdentifier:useRealTimeMilo:].cold.1
- -[IRServicePackageAdapterAppleTVControl filterHistory:]
- -[IRServicePackageAdapterMedia filterHistory:]
- -[IRSessionServer isGlobalLowLatencyMiLoWithPersistenceManager:]
- -[IRSystemStateDO initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:]
- -[IRSystemStateManager addEvent:]
- -[IRSystemStateManager miloProviderLslPredictionResultsRealTime]
- -[IRSystemStateManager onPredictionRealTime:]
- -[IRSystemStateManager requestSinglePredictionMiLoRealTime]
- -[IRSystemStateManager setMiloProviderLslPredictionResultsRealTime:]
- GCC_except_table18
- GCC_except_table22
- GCC_except_table24
- GCC_except_table28
- GCC_except_table38
- GCC_except_table50
- _OBJC_CLASS_$_IRSessionConnectionAllowedClients
- _OBJC_IVAR_$_IRHistoryManager._lastMiLoLabelRealTime
- _OBJC_IVAR_$_IRMiLoPredictionEventDO._labelRealTime
- _OBJC_IVAR_$_IRMiLoPredictionEventDO._predictionIdRealTime
- _OBJC_IVAR_$_IRMiLoProvider._isRealTimeMiLoRequestedForPowerOptimizations
- _OBJC_IVAR_$_IRMiLoProvider._requestSinglePredictionIdentifierRealTime
- _OBJC_IVAR_$_IRPreferences._controlledLiveOnMiLoRealTimeUponRequestCurrentContext
- _OBJC_IVAR_$_IRPreferences._liveOnMiloEnableRealTimeDeprecated
- _OBJC_IVAR_$_IRSystemStateManager._miloProviderLslPredictionResultsRealTime
- _OBJC_METACLASS_$_IRSessionConnectionAllowedClients
- __OBJC_$_CLASS_METHODS_IRSessionConnectionAllowedClients
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_IRServicePackageAdapter
- __OBJC_CLASS_RO_$_IRSessionConnectionAllowedClients
- __OBJC_METACLASS_RO_$_IRSessionConnectionAllowedClients
- ___166-[IRClassificatonGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.33
- ___45-[IRCleanupManager _handleCleanupXPCActivity]_block_invoke_3
- ___54-[IRCandidateManager candidateForCandidateIdentifier:]_block_invoke
- ___62-[IRMiLoProvider miLoConnection:queryServiceDidFailWithError:]_block_invoke
- ___71-[IRMiLoProvider miLoConnection:didDeleteServiceWithServiceIdentifier:]_block_invoke
- ___74-[IRCandidatesContainerDO(Extension) candidateNameForCandidateIdentifier:]_block_invoke
- ___86-[IRReplayDatabaseHandler getSortedHistoryEventsForServiceIdentifier:useRealTimeMilo:]_block_invoke
- ___88-[IRMiLoProvider miLoConnection:deleteServiceDidFailForServiceWithIdentifier:withError:]_block_invoke
- ___block_descriptor_32_e24_v16?0"IRMiLoProvider"8l
- ___block_descriptor_40_e8_32r_e33_v32?0"IRHistoryEventDO"8Q16^B24lr32l8
- ___block_descriptor_64_e8_32s40s48s56s_e26_B16?0"IRHistoryEventDO"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s56r_e28_v32?0"IRServiceDO"8Q16^B24ls32l8r56l8s40l8s48l8
- ___block_descriptor_80_e8_32r40r48r56r64r72r_e33_v32?0"IRHistoryEventDO"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e32_v24?0"IRCandidateWrapper"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.108
- ___block_literal_global.120
- ___block_literal_global.190
- ___block_literal_global.44
- ___block_literal_global.55
- ___block_literal_global.84
- _objc_autorelease
- _objc_msgSend$UUID
- _objc_msgSend$_checkAndStartLowLatencyMiLoIfNeeded
- _objc_msgSend$_handleMiLoRealTimeUponAddEvent:
- _objc_msgSend$_handleMiLoRealTimeUponContextChange
- _objc_msgSend$_handleMiLoRealTimeUponRequestCurrentContext
- _objc_msgSend$aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:
- _objc_msgSend$addEvent:
- _objc_msgSend$addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:andMiloPredictionRealTime:shouldLabelEventWithMilo:
- _objc_msgSend$allowedClientsToCreateServiceOnRun
- _objc_msgSend$controlledLiveOnMiLoRealTimeUponRequestCurrentContext
- _objc_msgSend$copyWithReplacementLabel:
- _objc_msgSend$copyWithReplacementPredictionId:
- _objc_msgSend$createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:
- _objc_msgSend$didReceiveMiloPredictionRealTime
- _objc_msgSend$fetchLatestServiceWithPersistenceManager:forClientIdentifier:
- _objc_msgSend$filterHistory:
- _objc_msgSend$getSortedHistoryEventsForServiceIdentifier:useRealTimeMilo:
- _objc_msgSend$historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:
- _objc_msgSend$initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:
- _objc_msgSend$initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:
- _objc_msgSend$initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:
- _objc_msgSend$initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:
- _objc_msgSend$initWithLabel:predictionId:labelRealTime:predictionIdRealTime:
- _objc_msgSend$isEqualToDate:
- _objc_msgSend$isRealTimeMiLoRequestedForPowerOptimizations
- _objc_msgSend$labelRealTime
- _objc_msgSend$lastMiLoLabelRealTime
- _objc_msgSend$liveOnMiloEnableRealTimeDeprecated
- _objc_msgSend$miLoPredictionEventDOWithLabel:predictionId:labelRealTime:predictionIdRealTime:
- _objc_msgSend$miloProviderLslPredictionResultsRealTime
- _objc_msgSend$onPredictionRealTime:
- _objc_msgSend$predictionIdRealTime
- _objc_msgSend$requestSinglePredictionIdentifierRealTime
- _objc_msgSend$requestSinglePredictionMiLoRealTime
- _objc_msgSend$requestSinglePredictionRealTime
- _objc_msgSend$setIsRealTimeMiLoRequestedForPowerOptimizations:
- _objc_msgSend$setLabelRealTime:
- _objc_msgSend$setLastMiLoLabelRealTime:
- _objc_msgSend$setMiloProviderLslPredictionResultsRealTime:
- _objc_msgSend$setPredictionIdRealTime:
- _objc_msgSend$setRequestSinglePredictionIdentifierRealTime:
- _objc_msgSend$startLowLatencyMiLoAndRequestSinglePredictionRealTime:
- _objc_msgSend$systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:
- _objc_retain_x9
CStrings:
+ "\x11*"
+ "\x14\x1a"
+ "\x1f\x0f\x0f\x0f\x0f\x0f\x04"
+ "\"!\x13"
+ "#db-cleanup-manager, Number of services in DB: %@, number of active services: %@"
+ "#db-cleanup-manager, Restarting isLowLatencyMiLo: %@"
+ "#milo-connection-bridge, "
+ "#milo-provider, [ErrorId - MiLo provider got setSpotOnLocation twice] MiLo already waiting for spotOn response for: %@"
+ "#session-connection, Creating service: %@, for client: %@, success: %@"
+ "#session-connection, [%@:%@]: Did Spot On Location Complete with error: [%@]"
+ "#session-server, [ErrorId - Server Init - DB access error] Cannot connect to store during server init"
+ "%@{UWB:%@, BLE:%@, MILO:%@, BrokeredInLOI:%@, PDRFence:%@}"
+ "%s[%@], Adding event (%@) type:%@, subtype:%@ to candidate:%@, miloLabel:%@, shouldLabelEventWithMilo:%@"
+ "%s[%@], MiLo not connected, responding to setSpotOnLocation with error"
+ "%s[%@], MiLo provider got callback for requestID: %@ with errorCode: %@, requestSpotOnLocationIdentifier: %@"
+ "%s[%@], MiLo provider got setSpotOnLocation"
+ "%s[%@], MiLo room detection in custom LOI is disabled and LOI is custom, disabling sameSpaceBasedOnMiLo"
+ "%s[%@], PDR fence crossed"
+ "%s[%@], PDR fence timeout"
+ "%s[%@], SameSpaceCandidate: name: %@, identifier: %@, MiLo: %@, BrokeredDeviceInLOI: %@, uwbRange: %@, bleRange: %@"
+ "%s[%@], Set Spot On for clietId: %@, shouldResetBrokeredDevices: %@"
+ "%s[%@], Set Spot On for clietId: %@, there is already a pending request for: %@"
+ "%s[%@], Single prediction requested, complied = %@, request-id (updated if copmplied): %@"
+ "%s[%@], Starting LowLatency connection for MiLo"
+ "%s[%@], Starting PDRFence PDR fence logic"
+ "%s[%@], Stopping PDR fence logic"
+ "%s[%@], [ErrorId - spot on timer conflict] Spot on timer retriggered while is still ongoing"
+ "%s[%@], enableMiLoAtCurrentLocation new API, miloRoomDetectionInCustomLOIEnabled: %@"
+ "%s[%@], got call for didSpotOnLocationComplete with error: %@, answering relevent clients and removing all spotOnPendingClients"
+ "%s[%@], resetting spotOnLocationRquest, removing requestID: %@"
+ "%s[%@], spot on milo request timeout, returning error"
+ "(C2A)"
+ "<IRAVOutputDeviceDO | deviceID:%@ modelID:%@ deviceName:%@ hasAirplayProperties:%@ discoveredOverInfra:%@ discoveredWithBroker:%@ deviceType:%@ deviceSubType:%@>"
+ "<IRHistoryEventDO | date:%@ candidateIdentifier:%@ event:%@ miloPredictionEvent:%@ systemState:%@ sharingPolicy:%@>"
+ "<IRMiLoPredictionEventDO | label:%@ predictionId:%@>"
+ "<IRSystemStateDO | appInFocusBundleID:%@ appInFocusWindowValid:%@ deviceWiFiSSID:%@ locationSemanticUserSpecificPlaceType:%@ locationSemanticLoiIdentifier:%@ iCloudId:%@ avInitialRouteSharingPolicy:%@ mediaRouteGroupLeaderOutputDeviceID:%@ timeZoneSeconds:%@ outputDeviceName:%@ outputDeviceType:%@ outputDeviceSubType:%@ predictedOutputDeviceName:%@ predictedOutputDeviceType:%@ predictedOutputDeviceSubType:%@ appInFocusWindowScreenUnlockEvent:%@ pdrFenceActive:%@>"
+ "@\"IRHistoryEventsContainerDO\"32@0:8@\"IRHistoryEventsContainerDO\"16@\"IRCandidatesContainerDO\"24"
+ "@136@0:8@16B24@28i36@40@48@56@64q72@80Q88Q96@104Q112Q120B128B132"
+ "@68@0:8@16@24@32B40B44B48Q52Q60"
+ "@68@0:8q16@24B32B36B40B44B48@52@60"
+ "Brokered Main Device First Use"
+ "Could not run service, unknown client"
+ "Custom"
+ "Delete Broker candidates"
+ "General_N_airplay_playback_events_custom_loi_Weekly"
+ "General_Weekly_N_days_since_last_brokered_scan"
+ "IRbrokeredUseScansForEligibilityOfMainDevice"
+ "IRbrokeredUseScansForEligibilityOfSecondaryDevice"
+ "IRcandidateSelectorAllowSelectByLOI"
+ "IRcandidateSelectorCallToActionAppearThreshold"
+ "IRcandidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents"
+ "IRcandidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds"
+ "IRloiSameSpaceEventsNumberOfEventsToWatch"
+ "IRloiSameSpaceEventsTimeIntervalSeconds"
+ "IRloiSameSpaceOverrideBrokerForAVODIDArray"
+ "IRloiSameSpaceOverrideBrokerForCandidateIDArray"
+ "IRmiloRoomDetectionInCustomLOIEnabled"
+ "IRmiloTimeoutForSetSpotOnRequestSeconds"
+ "IRpdrFenceCandidateSelectorAllowSelectByFence"
+ "IRpdrFenceOtherThanRadiusTimeoutInSeconds"
+ "IRpdrFenceRadiusInMeters"
+ "IRpdrFenceRadiusTimeoutInSeconds"
+ "IsDiscoveredWithBroker"
+ "MiLo Unavailable"
+ "Missing serialized value for IRAVOutputDeviceDO.discoveredWithBroker"
+ "Missing serialized value for IRSystemStateDO.pdrFenceActive"
+ "PDR fence crossed"
+ "PDRFence"
+ "Same space {UWB:%@, BLE:%@, MILO:%@, BrokeredInLOI:%@, PDRFence:%@}"
+ "T@\"IRCMPDRFenceBridge\",&,N,V_pdrFenceBridge"
+ "T@\"IRTimer\",&,N,V_pdrFenceTimer"
+ "T@\"IRTimer\",&,N,V_spotOnTimeout"
+ "T@\"NSArray\",R,N,V_loiSameSpaceOverrideBrokerForAVODIDArray"
+ "T@\"NSArray\",R,N,V_loiSameSpaceOverrideBrokerForCandidateIDArray"
+ "T@\"NSMutableSet\",&,N,V_spotOnPendingClientIDs"
+ "T@\"NSNumber\",R,N,V_brokeredUseScansForEligibilityOfMainDevice"
+ "T@\"NSNumber\",R,N,V_brokeredUseScansForEligibilityOfSecondaryDevice"
+ "T@\"NSNumber\",R,N,V_candidateSelectorAllowSelectByLOI"
+ "T@\"NSNumber\",R,N,V_candidateSelectorCallToActionAppearThreshold"
+ "T@\"NSNumber\",R,N,V_candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents"
+ "T@\"NSNumber\",R,N,V_candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds"
+ "T@\"NSNumber\",R,N,V_loiSameSpaceEventsNumberOfEventsToWatch"
+ "T@\"NSNumber\",R,N,V_loiSameSpaceEventsTimeIntervalSeconds"
+ "T@\"NSNumber\",R,N,V_miloRoomDetectionInCustomLOIEnabled"
+ "T@\"NSNumber\",R,N,V_miloTimeoutForSetSpotOnRequestSeconds"
+ "T@\"NSNumber\",R,N,V_pdrFenceCandidateSelectorAllowSelectByFence"
+ "T@\"NSNumber\",R,N,V_pdrFenceOtherThanRadiusTimeoutInSeconds"
+ "T@\"NSNumber\",R,N,V_pdrFenceRadiusInMeters"
+ "T@\"NSNumber\",R,N,V_pdrFenceRadiusTimeoutInSeconds"
+ "T@\"NSString\",R,N,V_sharingPolicy"
+ "T@\"NSUUID\",&,N,V_requestSinglePredictionIdentifier"
+ "T@\"NSUUID\",&,N,V_requestSpotOnLocationIdentifier"
+ "TB,N,V_candidateSelectorReasonBrokeredMainDeviceFirstUse"
+ "TB,N,V_isCallToAction"
+ "TB,N,V_sameSpaceBasedOnBrokeredLOI"
+ "TB,N,V_sameSpaceBasedOnPDRFence"
+ "TB,N,V_useBrokeredScanForMain"
+ "TB,N,V_useBrokeredScanForSecondary"
+ "TB,R,N,V_discoveredWithBroker"
+ "TB,R,N,V_pdrFenceActive"
+ "UI_Event_Is_Location_Custom"
+ "Unarchived unexpected class for IRHistoryEventDO key \"sharingPolicy\" (expected %@, decoded %@)"
+ "[Brokered Device]"
+ "[C2A Exceeded]"
+ "[C2A interaction]"
+ "[PDR Fence/MiLo Room Detection Disabled]"
+ "_brokeredUseScansForEligibilityOfMainDevice"
+ "_brokeredUseScansForEligibilityOfSecondaryDevice"
+ "_candidateSelectorAllowSelectByLOI"
+ "_candidateSelectorCallToActionAppearThreshold"
+ "_candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents"
+ "_candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds"
+ "_candidateSelectorReasonBrokeredMainDeviceFirstUse"
+ "_checkAndStartLowLatencyMiLoIfNeededWithForce:"
+ "_checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:"
+ "_checkAndStopPDRFenceLogicIfNeeded"
+ "_didSpotOnLocationComplete:"
+ "_discoveredWithBroker"
+ "_isCallToAction"
+ "_isSameSpaceBasedOnPDRFenceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:"
+ "_isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:"
+ "_loiSameSpaceEventsNumberOfEventsToWatch"
+ "_loiSameSpaceEventsTimeIntervalSeconds"
+ "_loiSameSpaceOverrideBrokerForAVODIDArray"
+ "_loiSameSpaceOverrideBrokerForCandidateIDArray"
+ "_miloRoomDetectionInCustomLOIEnabled"
+ "_miloTimeoutForSetSpotOnRequestSeconds"
+ "_nominateCallToActionForCandidate:withHistoryEventsAsc:andSystemState:"
+ "_pdrFenceActive"
+ "_pdrFenceBridge"
+ "_pdrFenceCandidateSelectorAllowSelectByFence"
+ "_pdrFenceOtherThanRadiusTimeoutInSeconds"
+ "_pdrFenceRadiusInMeters"
+ "_pdrFenceRadiusTimeoutInSeconds"
+ "_pdrFenceTimer"
+ "_requestSinglePredictionIdentifier"
+ "_requestSpotOnLocationIdentifier"
+ "_sameSpaceBasedOnBrokeredLOI"
+ "_sameSpaceBasedOnPDRFence"
+ "_selectBasedOnMostRecentMainBrokeredDeviceFromCandidates:withSystemState:andHistoryEventsAsc:andDate:"
+ "_serviceIdentifierForClientIdentifier:"
+ "_setSpotOnLocationWithParameters:"
+ "_sharingPolicy"
+ "_spotOnPendingClientIDs"
+ "_spotOnTimeout"
+ "_useBrokeredScanForMain"
+ "_useBrokeredScanForSecondary"
+ "aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:"
+ "addEvent:forCandidate:"
+ "addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:shouldLabelEventWithMilo:"
+ "adjustDBToStaticTokens:"
+ "appInFocusBundleID: %@\n appInFocusWindowValid: %@\n appInFocusWindowScreenUnlockEvent: %@\n deviceWiFiSSID: %@\n locationSemanticLoiIdentifier: %@\n iCloudId: %@\n locationSemanticUserSpecificPlaceType: %@\n avInitialRouteSharingPolicy: %@\n mediaRouteGroupLeaderOutputDeviceID: %@\n outputDevice: Name - %@, Type - %@, SubType - %@\n predictedOutputDevice: Name - %@, Type - %@, SubType - %@\n pdrFenceActive: %@\n"
+ "brokeredUseScansForEligibilityOfMainDevice"
+ "brokeredUseScansForEligibilityOfSecondaryDevice"
+ "candidateSelectorAllowSelectByLOI"
+ "candidateSelectorCallToActionAppearThreshold"
+ "candidateSelectorMostRecentBrokeredDeviceMaximumNumberOfEvents"
+ "candidateSelectorMostRecentBrokeredMainDeviceIntervalSeconds"
+ "candidateSelectorReasonBrokeredMainDeviceFirstUse"
+ "com.apple.APSUIApp"
+ "com.apple.MusicUIService"
+ "com.apple.springboard"
+ "components:fromDate:toDate:options:"
+ "copyWithReplacementDiscoveredWithBroker:"
+ "copyWithReplacementPdrFenceActive:"
+ "copyWithReplacementSharingPolicy:"
+ "createCustomLocationOfInterestAtCurrentLocationWithConfiguration:"
+ "createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:"
+ "day"
+ "daysFromDate:toDate:"
+ "deleteBrokerCandidates"
+ "didSpotOnLocationComplete:"
+ "didSpotOnLocationCompleteWithError:"
+ "discoveredWithBroker"
+ "enableMiLoAtCurrentLocation"
+ "filterHistory:withCandidatesContainer:"
+ "filterHistoryByBrokeredDeviceScan:"
+ "historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:"
+ "initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:"
+ "initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnBrokeredLOI:sameSpaceBasedOnPDRFence:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:"
+ "initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:sharingPolicy:"
+ "initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:discoveredWithBroker:deviceType:deviceSubType:"
+ "initWithEnableInRoomDetection:"
+ "initWithLabel:predictionId:"
+ "initWithServiceToken:"
+ "isBrokeredDevice"
+ "isCallToAction"
+ "isDiscoveredWithBroker"
+ "kIsBrokeredDevice"
+ "loiSameSpaceEventsNumberOfEventsToWatch"
+ "loiSameSpaceEventsTimeIntervalSeconds"
+ "loiSameSpaceOverrideBrokerForAVODIDArray"
+ "loiSameSpaceOverrideBrokerForCandidateIDArray"
+ "miLoPredictionEventDOWithLabel:predictionId:"
+ "miloRoomDetectionInCustomLOIEnabled"
+ "miloTimeoutForSetSpotOnRequestSeconds"
+ "pdrFenceActive"
+ "pdrFenceBridge"
+ "pdrFenceCandidateSelectorAllowSelectByFence"
+ "pdrFenceOtherThanRadiusTimeoutInSeconds"
+ "pdrFenceRadiusInMeters"
+ "pdrFenceRadiusTimeoutInSeconds"
+ "pdrFenceTimer"
+ "policyManager:didSpotOnLocationCompleteForClientIds:withError:"
+ "q32@0:8@16@24"
+ "requestSinglePrediction"
+ "requestSinglePredictionIdentifier"
+ "requestSpotOnLocationIdentifier"
+ "resetAllBrokerDiscoveredCandidates"
+ "resetSpotOnLocationRequest"
+ "sameSpaceBasedOnBrokeredLOI"
+ "sameSpaceBasedOnPDRFence"
+ "serviceContainer:didSpotOnLocationCompleteForClientIds:withError:"
+ "setCandidateSelectorReasonBrokeredMainDeviceFirstUse:"
+ "setDiscoveredWithBroker:"
+ "setIsCallToAction:"
+ "setPdrFenceActive:"
+ "setPdrFenceBridge:"
+ "setPdrFenceTimer:"
+ "setRequestSinglePredictionIdentifier:"
+ "setRequestSpotOnLocationIdentifier:"
+ "setSameSpaceBasedOnBrokeredLOI:"
+ "setSameSpaceBasedOnPDRFence:"
+ "setSharingPolicy:"
+ "setSpotOnLocation"
+ "setSpotOnLocationWithParameters:andClientID:"
+ "setSpotOnPendingClientIDs:"
+ "setSpotOnTimeout:"
+ "setUseBrokeredScanForMain:"
+ "setUseBrokeredScanForSecondary:"
+ "sharingPolicy"
+ "spotOnPendingClientIDs"
+ "spotOnTimeout"
+ "systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:"
+ "timeout"
+ "useBrokeredScanForMain"
+ "useBrokeredScanForSecondary"
+ "v24@0:8@\"IRSessionSpotOnLocationParameters\"16"
+ "v32@0:8@\"IRSessionSpotOnLocationParameters\"16@\"NSString\"24"
+ "v32@?0@\"IRServiceContainer\"8Q16^B24"
+ "v32@?0@\"IRServiceMO\"8Q16^B24"
+ "v40@0:8@\"IRPolicyManager\"16@\"NSSet\"24@\"NSError\"32"
+ "v40@0:8@\"IRServiceContainer\"16@\"NSSet\"24@\"NSError\"32"
+ "v52@0:8@16@24@32@40B48"
- "\x11("
- "\x15\x18"
- "\x1f\x0f\x0f\x0f\x0f\x05"
- "\"!\x12"
- "#db-cleanup-manager, Number of services in DB: %@, number of active services: %@, isLowLatencyMiLo: %@"
- "#service-container, [ErrorId - Service package missmatch] Diff in params: stored service package: %@, provided service package: %@"
- "#session-connection, [ErrorId - Run with no service token in DB] [%@:%@]:runSessionWithNoTokensForClient, creating service, success = %@, services previously in database = %@"
- "#session-server, [ErrorId - Server Init - DB access error] Cannot connect to store during server init - skipping duplicate detection"
- "%@:%@"
- "%@{UWB:%@, BLE:%@, MILO:%@}"
- "%@|%@"
- "%s[%@], Adding event (%@) type:%@, subtype:%@ to candidate:%@, miloLabel:%@, miloLabelRealTime:%@, shouldLabelEventWithMilo:%@"
- "%s[%@], Real time prediction requested, complied = %@, request-id (updated if copmplied): %@"
- "%s[%@], Received MiLo prediction real time: %@ with quality: %@ and reason: %@"
- "%s[%@], SameSpaceCandidate: name: %@, identifier: %@, MiLo: %@, uwbRange: %@, bleRange: %@"
- "%s[%@], Starting LowLatency connection for MiLo, predictionIdentifier: %@"
- "%s[%@], [ErrorId - MiLo provider complete error] MiLo complete client requested with error: %@, requestIdentifier: %@, requestSinglePredictionIdentifierRealTime: %@"
- "%s[%@], didReceiveMiloPredictionRealTime was called"
- "<IRAVOutputDeviceDO | deviceID:%@ modelID:%@ deviceName:%@ hasAirplayProperties:%@ discoveredOverInfra:%@ deviceType:%@ deviceSubType:%@>"
- "<IRHistoryEventDO | date:%@ candidateIdentifier:%@ event:%@ miloPredictionEvent:%@ systemState:%@>"
- "<IRMiLoPredictionEventDO | label:%@ predictionId:%@ labelRealTime:%@ predictionIdRealTime:%@>"
- "<IRSystemStateDO | appInFocusBundleID:%@ appInFocusWindowValid:%@ deviceWiFiSSID:%@ locationSemanticUserSpecificPlaceType:%@ locationSemanticLoiIdentifier:%@ iCloudId:%@ avInitialRouteSharingPolicy:%@ mediaRouteGroupLeaderOutputDeviceID:%@ timeZoneSeconds:%@ outputDeviceName:%@ outputDeviceType:%@ outputDeviceSubType:%@ predictedOutputDeviceName:%@ predictedOutputDeviceType:%@ predictedOutputDeviceSubType:%@ appInFocusWindowScreenUnlockEvent:%@>"
- "@\"IRHistoryEventsContainerDO\"24@0:8@\"IRHistoryEventsContainerDO\"16"
- "@132@0:8@16B24@28i36@40@48@56@64q72@80Q88Q96@104Q112Q120B128"
- "@52@0:8@16@24@32@40B48"
- "@60@0:8q16@24B32B36B40@44@52"
- "@64@0:8@16@24@32B40B44Q48Q56"
- "@max.lastSeenDate"
- "B24@0:8^@16"
- "Could not create new service"
- "IRSessionConnectionAllowedClients"
- "IRcontrolledLiveOnMiLoRealTimeUponRequestCurrentContext"
- "IRliveOnMiloEnableRealTimeDeprecated"
- "Milo prediction real time"
- "Same space {UWB:%@, BLE:%@, MILO:%@}"
- "T@\"IRMiloLslPredictionDO\",&,N,V_miloProviderLslPredictionResultsRealTime"
- "T@\"NSNumber\",R,N,V_controlledLiveOnMiLoRealTimeUponRequestCurrentContext"
- "T@\"NSNumber\",R,N,V_liveOnMiloEnableRealTimeDeprecated"
- "T@\"NSString\",&,N,V_lastMiLoLabelRealTime"
- "T@\"NSString\",R,N,V_labelRealTime"
- "T@\"NSString\",R,N,V_predictionIdRealTime"
- "T@\"NSUUID\",&,N,V_requestSinglePredictionIdentifierRealTime"
- "TB,N,V_isRealTimeMiLoRequestedForPowerOptimizations"
- "UUID"
- "Unarchived unexpected class for IRMiLoPredictionEventDO key \"labelRealTime\" (expected %@, decoded %@)"
- "Unarchived unexpected class for IRMiLoPredictionEventDO key \"predictionIdRealTime\" (expected %@, decoded %@)"
- "_checkAndStartLowLatencyMiLoIfNeeded"
- "_controlledLiveOnMiLoRealTimeUponRequestCurrentContext"
- "_handleMiLoRealTimeUponAddEvent:"
- "_handleMiLoRealTimeUponContextChange"
- "_handleMiLoRealTimeUponRequestCurrentContext"
- "_isRealTimeMiLoRequestedForPowerOptimizations"
- "_labelRealTime"
- "_lastMiLoLabelRealTime"
- "_liveOnMiloEnableRealTimeDeprecated"
- "_miloProviderLslPredictionResultsRealTime"
- "_predictionIdRealTime"
- "_requestSinglePredictionIdentifierRealTime"
- "a"
- "aVOutputDeviceDOWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:"
- "addEvent:"
- "addEvent:forCandidateIdentifier:withSystemState:andMiloPrediction:andMiloPredictionRealTime:shouldLabelEventWithMilo:"
- "allowedClientsToCreateServiceOnRun"
- "appInFocusBundleID: %@\n appInFocusWindowValid: %@\n appInFocusWindowScreenUnlockEvent: %@\n deviceWiFiSSID: %@\n locationSemanticLoiIdentifier: %@\n iCloudId: %@\n locationSemanticUserSpecificPlaceType: %@\n avInitialRouteSharingPolicy: %@\n mediaRouteGroupLeaderOutputDeviceID: %@\n outputDevice: Name - %@, Type - %@, SubType - %@\n predictedOutputDevice: Name - %@, Type - %@, SubType - %@\n"
- "controlledLiveOnMiLoRealTimeUponRequestCurrentContext"
- "copyWithReplacementLabelRealTime:"
- "copyWithReplacementPredictionIdRealTime:"
- "createServiceWithClientIdentifier:serviceIdentifier:parameters:persistenceManager:allowOneServicePerClient:"
- "didReceiveMiloPredictionRealTime"
- "filterHistory:"
- "getSortedHistoryEventsForServiceIdentifier:useRealTimeMilo:"
- "historyEventDOWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:"
- "initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:"
- "initWithClassification:ClassificationDescription:sameSpaceBasedOnMiLo:sameSpaceBasedOnUWB:sameSpaceBasedOnBLE:candidateSelectorReasons:forCandidate:"
- "initWithDate:candidateIdentifier:event:miloPredictionEvent:systemState:"
- "initWithDeviceID:modelID:deviceName:hasAirplayProperties:discoveredOverInfra:deviceType:deviceSubType:"
- "initWithLabel:predictionId:labelRealTime:predictionIdRealTime:"
- "isEqualToDate:"
- "isRealTimeMiLoRequestedForPowerOptimizations"
- "labelRealTime"
- "lastMiLoLabelRealTime"
- "liveOnMiloEnableRealTimeDeprecated"
- "miLoPredictionEventDOWithLabel:predictionId:labelRealTime:predictionIdRealTime:"
- "miloProviderLslPredictionResultsRealTime"
- "onPredictionRealTime:"
- "predictionIdRealTime"
- "requestSinglePredictionIdentifierRealTime"
- "requestSinglePredictionMiLoRealTime"
- "requestSinglePredictionRealTime"
- "setIsRealTimeMiLoRequestedForPowerOptimizations:"
- "setLabelRealTime:"
- "setLastMiLoLabelRealTime:"
- "setMiloProviderLslPredictionResultsRealTime:"
- "setPredictionIdRealTime:"
- "setRequestSinglePredictionIdentifierRealTime:"
- "startLowLatencyMiLoAndRequestSinglePredictionRealTime:"
- "systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:"
- "v60@0:8@16@24@32@40@48B56"

```
