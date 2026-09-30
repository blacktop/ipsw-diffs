## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-1850.80.3.0.0
-  __TEXT.__text: 0xcc494
-  __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_methlist: 0x5f94
-  __TEXT.__const: 0x8960
-  __TEXT.__gcc_except_tab: 0x17e8
-  __TEXT.__cstring: 0x92e6
-  __TEXT.__oslogstring: 0x10240
+1902.100.119.0.0
+  __TEXT.__text: 0xd2270
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0x6a5c
+  __TEXT.__const: 0x8f40
+  __TEXT.__gcc_except_tab: 0x18e0
+  __TEXT.__cstring: 0x855e
+  __TEXT.__oslogstring: 0x10bb7
   __TEXT.__dlopen_cstrs: 0xca
-  __TEXT.__unwind_info: 0x2af0
-  __TEXT.__objc_classname: 0x873
-  __TEXT.__objc_methname: 0xcb7c
-  __TEXT.__objc_methtype: 0x338c
-  __TEXT.__objc_stubs: 0xaa20
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xcb0
-  __DATA_CONST.__objc_classlist: 0x300
+  __TEXT.__unwind_info: 0x2bd8
+  __TEXT.__objc_classname: 0x8b0
+  __TEXT.__objc_methname: 0xd3a2
+  __TEXT.__objc_methtype: 0x3331
+  __TEXT.__objc_stubs: 0xac80
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0xc70
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31e0
+  __DATA_CONST.__objc_selrefs: 0x33c0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x2f0
-  __DATA_CONST.__objc_arraydata: 0x4f8
-  __AUTH_CONST.__auth_got: 0xb98
-  __AUTH_CONST.__const: 0x1cc8
-  __AUTH_CONST.__cfstring: 0xa0c0
-  __AUTH_CONST.__objc_const: 0x13f28
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_arraydata: 0x618
+  __AUTH_CONST.__auth_got: 0xb88
+  __AUTH_CONST.__const: 0x1de8
+  __AUTH_CONST.__cfstring: 0x9ae0
+  __AUTH_CONST.__objc_const: 0x14200
+  __AUTH_CONST.__objc_intobj: 0x6c0
+  __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0xdc0
+  __AUTH.__objc_data: 0xd20
+  __DATA.__objc_ivar: 0xe78
   __DATA.__data: 0x58515
   __DATA.__bss: 0x1c0
-  __DATA_DIRTY.__objc_data: 0x12c0
+  __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C13E8070-6C00-39C8-87A9-1D9D1C4727CC
-  Functions: 4073
-  Symbols:   8818
-  CStrings:  7465
+  UUID: 40A8A0D0-CBF8-31DF-BB35-D6C961C815B9
+  Functions: 4195
+  Symbols:   9075
+  CStrings:  7508
 
Symbols:
+ +[CBAnalytics aliasingMitigationsCount:]
+ +[CBAnalytics curveLevel:]
+ +[CBAnalytics userBrightnessChangeAfterSnapping:]
+ +[CBAnalyticsExtDisplayManager handleColorSample:]
+ +[CBAnalyticsExtDisplayManager sendEventOnceADayLazy:andDict:]
+ +[CBAnalyticsExtDisplayManager sharedInstance]
+ +[CBAnalyticsExtDisplayManager stopReporting:]
+ +[CBPresetsParser sharedInstance].cold.1
+ -[AABCHistograms LDeviceOff_EDR]
+ -[AABCHistograms LDevice_EDR]
+ -[AABCHistograms LLPM_EDR]
+ -[AABCHistograms LOff_EDR]
+ -[AABCHistograms L_EDR]
+ -[AABCHistograms autoBrightnessOn]
+ -[AABCHistograms builtInDisplay]
+ -[AABCHistograms ecoModeOn]
+ -[AABCHistograms firstBrightnessUpdate]
+ -[AABCHistograms lastBrightnessUpdateNitsEDR]
+ -[AABCHistograms lastBrightnessUpdateNits]
+ -[AABCHistograms lastBrightnessUpdateTimestamp]
+ -[AABCHistograms luminanceHistLogNitsSDR:andNitsEDR:]
+ -[AABCHistograms setAutoBrightnessOn:]
+ -[AABCHistograms setBuiltInDisplay:]
+ -[AABCHistograms setEcoModeOn:]
+ -[AABCHistograms setFirstBrightnessUpdate:]
+ -[AABCHistograms setLastBrightnessUpdateNits:]
+ -[AABCHistograms setLastBrightnessUpdateNitsEDR:]
+ -[AABCHistograms setLastBrightnessUpdateTimestamp:]
+ -[BLControl handlePILServiceArrival:]
+ -[BLControl handlePILServiceArrival:].cold.1
+ -[BLControl handlePILServiceArrival:].cold.2
+ -[BLControl handlePILServiceArrival:].cold.3
+ -[BLControl init].cold.6
+ -[BLControl startPILServiceLookup]
+ -[BLControl startPILServiceLookup].cold.1
+ -[BLControl stopPILServiceLookup]
+ -[CBALSServiceClient addHIDALSService:]
+ -[CBALSServiceClient addHIDServiceClient:]
+ -[CBALSServiceClient dealloc]
+ -[CBALSServiceClient getAggregatedLux:]
+ -[CBALSServiceClient handleHIDEvent:from:]
+ -[CBALSServiceClient initWithCallback:]
+ -[CBALSServiceClient removeHIDServiceClient:]
+ -[CBAnalyticsExtDisplayManager dealloc]
+ -[CBAnalyticsExtDisplayManager handleColorSampleInternal:]
+ -[CBAnalyticsExtDisplayManager init]
+ -[CBAnalyticsExtDisplayManager init].cold.1
+ -[CBAnalyticsExtDisplayManager init].cold.2
+ -[CBAnalyticsExtDisplayManager init].cold.3
+ -[CBAnalyticsExtDisplayManager isFirstEventToday:]
+ -[CBAnalyticsExtDisplayManager isSameDay:asDay:]
+ -[CBAnalyticsExtDisplayManager logAllColorSamples]
+ -[CBAnalyticsExtDisplayManager logAllColorSamples].cold.1
+ -[CBAnalyticsExtDisplayManager logColorSample:withType:]
+ -[CBAnalyticsExtDisplayManager sendEventLazy:andDict:]
+ -[CBAnalyticsExtDisplayManager sendEventOnceADayLazyInternal:andDict:]
+ -[CBAnalyticsExtDisplayManager setUserActive:]
+ -[CBAnalyticsExtDisplayManager startReporting]
+ -[CBAnalyticsExtDisplayManager stopReportingInternal:]
+ -[CBAnalyticsExtDisplayManager storeTimestamp:forEventName:]
+ -[CBAnalyticsExtDisplayManager stringForType:]
+ -[CBBlueLightClient setEnabled:withOption:].cold.1
+ -[CBBlueLightClient setMode:].cold.1
+ -[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:].cold.5
+ -[CBEDR shouldUpdateEDRForRequestedHeadroom:targetHeadroom:]
+ -[CBFloatArray objectAtIndexedSubscript:]
+ -[CBFrameInfoProvider dealloc]
+ -[CBFrameInfoProvider initWithDisplayServer:]
+ -[CBFrameInfoProvider initWithDisplayServer:].cold.1
+ -[CBFrameInfoProvider initWithDisplayServer:andQueue:]
+ -[CBFrameInfoProvider initWithDisplayServer:andQueue:].cold.1
+ -[CBFrameInfoProvider registerObserver:withCallback:]
+ -[CBFrameInfoProvider unregisterObserver:]
+ -[CBFrameStats initWithQueue:frameInfoProvider:andWindowServerDisplay:]
+ -[CBMILInterface getDutyCycleThreshold:]
+ -[CBMILInterface getDutyCycleThreshold:].cold.1
+ -[CBMILInterface hidServiceArrived:]
+ -[CBMILInterface lookupMILServiceTrusted]
+ -[CBMILInterface lookupMILServiceUntrusted]
+ -[CBMILInterface readData:withSize:fromRegister:]
+ -[CBMILInterface writeDataTrusted:]
+ -[CBMILInterface writeDataUntrusted:withSize:toRegister:withAddressSize:]
+ -[CBPILNode dealloc]
+ -[CBPILNode initWithService:]
+ -[CBPILNode initWithService:].cold.1
+ -[CBPILNode pil]
+ -[CBPILParams blackBezel]
+ -[CBPILParams dealloc]
+ -[CBPILParams initWithLuxArray:nitsArray:lutSize:andBlackBezel:]
+ -[CBPILParams initWithService:]
+ -[CBPILParams loadParametersFromService:]
+ -[CBPILParams loadParametersFromService:].cold.1
+ -[CBPILParams pilCurveLux]
+ -[CBPILParams pilCurveNits]
+ -[CBSBIM mitigatedHeadroomFromRequestedHeadroom].cold.1
+ -[CBSBIM mitigatedHeadroomFromRequestedHeadroom].cold.2
+ -[CBTrueToneClient setEnabled:].cold.1
+ -[CILController dutyCycleRangeFetched]
+ -[CILController getMaximumAchievableBrightness]
+ -[CILController getMinimumAchievableBrightness]
+ -[ConfidenceEstimatorStats collectStrength:andConfidence:]
+ -[ConfidenceEstimatorStats dealloc]
+ -[ConfidenceEstimatorStats initWithModelID:]
+ -[ConfidenceEstimatorStats outputsCE]
+ -[ConfidenceEstimatorStats submit]
+ -[KeyboardBacklight commitElements:direction:error:]
+ -[KeyboardBacklight newElementsArray]
+ -[MILController dutyCycleRangeFetched]
+ -[MILController fetchDutyCycleThresholdIfNeeded]
+ -[MILController fetchDutyCycleThresholdIfNeeded].cold.1
+ -[MILController getMaximumAchievableBrightness]
+ -[MILController getMinimumAchievableBrightness]
+ -[NightModeControl cancelSchedule].cold.1
+ -[NightModeControl cancelTransition].cold.1
+ -[NightModeControl initWithSupportObject:queue:callback:].cold.1
+ -[NightModeControl initWithSupportObject:queue:callback:].cold.2
+ -[NightModeControl initWithSupportObject:queue:callback:].cold.3
+ -[NightModeControl reevaluateCurrentStateWithFactorFadeOption:].cold.1
+ -[NightModeControl retrieveSunriseSunsetTimesFromBackup:].cold.1
+ -[NightModeControl retrieveSunriseSunsetTimesFromBackup:].cold.2
+ -[NightModeControl setProperty:forKey:].cold.1
+ -[NightModeControl setProperty:forKey:].cold.2
+ -[NightModeControl setSchedule:].cold.1
+ -[NightModeControl switchToUser:].cold.1
+ -[NightModeControl tearDownAllTimers].cold.1
+ -[NightModeControl updateSunriseSunsetInfo:].cold.1
+ -[NightModeControl updateSunriseSunsetInfo:].cold.2
+ -[NightModeControl updateSunriseSunsetInfo:].cold.3
+ -[NightModeControl updateTransitionTimesFromSchedule:].cold.1
+ -[NightModeControl updateTransitionTimesFromSchedule:].cold.2
+ -[NightModeControl updateTransitionTimesFromSchedule:].cold.3
+ -[NightModeControl updateTransitionTimesFromSchedule:].cold.4
+ -[NightModeControl updateTransitionTimesFromSunriseSunset:].cold.1
+ -[NightModeControl updateTransitionTimesFromSunriseSunset:].cold.2
+ -[NightModeControl updateTransitionTimesFromSunriseSunset:].cold.3
+ -[PILABCurve initWithParams:]
+ -[PILABCurve initWithParams:].cold.1
+ -[PILAutoBrightnessModule currentPILBrightness]
+ -[PILAutoBrightnessModule getMaximumAchievableBrightness]
+ -[PILAutoBrightnessModule getMinimumAchievableBrightness]
+ -[PILAutoBrightnessModule initWithQueue:PILParams:calibration:andALSServiceClient:]
+ -[PILAutoBrightnessModule initialiseControllersWithCalibration:]
+ -[PILAutoBrightnessModule updateCILRangeIfNeeded]
+ -[PILAutoBrightnessModule updateMILRangeIfNeeded]
+ -[PILContainer addHIDServiceClient:]
+ -[PILContainer copyIdentifiers]
+ -[PILContainer copyPropertyForKey:]
+ -[PILContainer copyPropertyInternalForKey:]
+ -[PILContainer dealloc]
+ -[PILContainer handleHIDEvent:from:]
+ -[PILContainer handleNotificationForKey:withProperty:from:]
+ -[PILContainer initWithParameters:]
+ -[PILContainer initWithParameters:].cold.1
+ -[PILContainer initWithParameters:].cold.2
+ -[PILContainer newStatusInfo]
+ -[PILContainer observeValueForKeyPath:ofObject:change:context:]
+ -[PILContainer registerForPILNotifications]
+ -[PILContainer removeHIDServiceClient:]
+ -[PILContainer sendNotificationForKey:andValue:]
+ -[PILContainer setProperty:forKey:]
+ -[PILContainer setupALSServices]
+ -[PILContainer setupModules]
+ -[PILContainer start]
+ -[PILContainer stop]
+ -[PILContainer tearDownModules]
+ -[PILContainer tearDownModules].cold.1
+ -[PILContainer unregisterForPILNotifications]
+ -[PILContainer updateBrightness]
+ -[SunriseSunsetProvider copySunriseSunsetInfo:].cold.1
+ -[SunriseSunsetProvider copySunriseSunsetInfo:].cold.2
+ -[SunriseSunsetProvider copySunriseSunsetInfo:].cold.3
+ -[SunriseSunsetProvider initWithCallback:].cold.1
+ -[SunriseSunsetProvider initWithCallback:].cold.2
+ -[SunriseSunsetProvider initWithCallback:].cold.3
+ -[SunriseSunsetProvider registerBlock:].cold.1
+ -[SunriseSunsetProvider unregisterBlock].cold.1
+ -[SunriseSunsetProvider unregisterNotification].cold.1
+ AABCFactoryFunction.cold.1
+ CBALCALSCopyALSServiceClient.cold.1
+ CBALCRegisterALSPluginCallback.cold.1
+ CBALCSetDictionary.cold.1
+ CBEDRServerStartServer.cold.1
+ CBU_ForceFrameAfterBrightnessUpdate.cold.1
+ CBU_ForceUpdateFrequencyAndFrameSkip.cold.1
+ CBU_ImplicitUserInteractedWithUI.cold.1
+ CBU_PassContrastEnhancerStrengthThroughSyncDBV.cold.1
+ CBU_RampLumaBoostFactorInAOD.cold.1
+ CBU_ShouldNotHandleExistingInternalDisplayAttachment.cold.1
+ CBU_SyncDisplayStateControlSupported.cold.1
+ GCC_except_table134
+ GCC_except_table219
+ GCC_except_table251
+ GCC_except_table266
+ GCC_except_table53
+ GCC_except_table68
+ LoadHIDSystemConnection.cold.1
+ OBJC_IVAR_$_AABCHistograms._LDeviceOff_EDR
+ OBJC_IVAR_$_AABCHistograms._LDevice_EDR
+ OBJC_IVAR_$_AABCHistograms._LLPM_EDR
+ OBJC_IVAR_$_AABCHistograms._LOff_EDR
+ OBJC_IVAR_$_AABCHistograms._L_EDR
+ OBJC_IVAR_$_AABCHistograms._autoBrightnessOn
+ OBJC_IVAR_$_AABCHistograms._builtInDisplay
+ OBJC_IVAR_$_AABCHistograms._ecoModeOn
+ OBJC_IVAR_$_AABCHistograms._firstBrightnessUpdate
+ OBJC_IVAR_$_AABCHistograms._lastBrightnessUpdateNits
+ OBJC_IVAR_$_AABCHistograms._lastBrightnessUpdateNitsEDR
+ OBJC_IVAR_$_AABCHistograms._lastBrightnessUpdateTimestamp
+ OBJC_IVAR_$_BLControl._ioNotificationObjectPIL
+ OBJC_IVAR_$_BLControl._ioNotificationPortPIL
+ OBJC_IVAR_$_BLControl._ioServiceArrivalIteratorPIL
+ OBJC_IVAR_$_BLControl._pilContainers
+ OBJC_IVAR_$_CBALSServiceClient._alsServices
+ OBJC_IVAR_$_CBALSServiceClient._callback
+ OBJC_IVAR_$_CBALSServiceClient._logHandle
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager._logHandle
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager._queue
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager._reportTimer
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager._timestamps
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager._userActive
+ OBJC_IVAR_$_CBAnalyticsExtDisplayManager.samples
+ OBJC_IVAR_$_CBDisplayModuleSKL._analyticsHist
+ OBJC_IVAR_$_CBDisplayModuleSKL._analyticsPeriodicSender
+ OBJC_IVAR_$_CBDisplayModuleSKL._firstABUpdate
+ OBJC_IVAR_$_CBDisplayModuleSKL._isSnapping
+ OBJC_IVAR_$_CBDisplayModuleSKL._lastUserBrightness
+ OBJC_IVAR_$_CBDisplayModuleSKL._snappingTimestamp
+ OBJC_IVAR_$_CBDisplayModuleiOS._aliasingMitigationActive
+ OBJC_IVAR_$_CBDisplayModuleiOS._analyticsHist
+ OBJC_IVAR_$_CBDisplayModuleiOS._analyticsPeriodicSender
+ OBJC_IVAR_$_CBDisplayModuleiOS._frameInfoProvider
+ OBJC_IVAR_$_CBFrameInfoProvider._logHandle
+ OBJC_IVAR_$_CBFrameInfoProvider._observers
+ OBJC_IVAR_$_CBFrameInfoProvider._queue
+ OBJC_IVAR_$_CBFrameInfoProvider._windowServerDisplay
+ OBJC_IVAR_$_CBFrameStats._frameInfoProvider
+ OBJC_IVAR_$_CBHIDEventManager._analyticsIlluminanceHist
+ OBJC_IVAR_$_CBHIDEventManager._analyticsPeriodicSender
+ OBJC_IVAR_$_CBMILInterface._milHIDSystemClient
+ OBJC_IVAR_$_CBMILInterface._milPlugin
+ OBJC_IVAR_$_CBPILNode._log
+ OBJC_IVAR_$_CBPILNode._pil
+ OBJC_IVAR_$_CBPILNode._service
+ OBJC_IVAR_$_CBPILParams._blackBezel
+ OBJC_IVAR_$_CBPILParams._log
+ OBJC_IVAR_$_CBPILParams._pilCurveLux
+ OBJC_IVAR_$_CBPILParams._pilCurveNits
+ OBJC_IVAR_$_CBSBIM._timerQueue
+ OBJC_IVAR_$_CILController._curveVersion
+ OBJC_IVAR_$_ConfidenceEstimatorStats._edgeMappingConfidence
+ OBJC_IVAR_$_ConfidenceEstimatorStats._edgeMappingStrength
+ OBJC_IVAR_$_ConfidenceEstimatorStats._modelID
+ OBJC_IVAR_$_ConfidenceEstimatorStats._outputsCE
+ OBJC_IVAR_$_KeyboardBacklight._backlightUpdateQueue
+ OBJC_IVAR_$_KeyboardBacklight._currentBrightness
+ OBJC_IVAR_$_KeyboardBacklight._currentEnableState
+ OBJC_IVAR_$_KeyboardBacklight._currentFadeSpeed
+ OBJC_IVAR_$_KeyboardBacklight._currentLevel
+ OBJC_IVAR_$_MILController._dutyCycleRangeFetched
+ OBJC_IVAR_$_NightModeControl._logHandle
+ OBJC_IVAR_$_PILABCurve._pilCurveLux
+ OBJC_IVAR_$_PILABCurve._pilCurveNits
+ OBJC_IVAR_$_PILAutoBrightnessModule._alsServiceClient
+ OBJC_IVAR_$_PILAutoBrightnessModule._cilBrightnessRangeSet
+ OBJC_IVAR_$_PILAutoBrightnessModule._maximumAchievableBrightness
+ OBJC_IVAR_$_PILAutoBrightnessModule._milBrightnessRangeSet
+ OBJC_IVAR_$_PILAutoBrightnessModule._minimumAchievableBrightness
+ OBJC_IVAR_$_PILContainer._alsServiceClient
+ OBJC_IVAR_$_PILContainer._modules
+ OBJC_IVAR_$_PILContainer._params
+ OBJC_IVAR_$_PILContainer._pilStateMonitor
+ OBJC_IVAR_$_PILContainer._relevantServices
+ OBJC_IVAR_$_SunriseSunsetProvider._logHandle
+ PILEventCallback.cold.1
+ _CFXCCT2xy_BlackBody
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientSetMatching
+ _OBJC_CLASS_$_CBALSServiceClient
+ _OBJC_CLASS_$_CBAnalyticsExtDisplayManager
+ _OBJC_CLASS_$_CBFrameInfoProvider
+ _OBJC_CLASS_$_CBPILNode
+ _OBJC_CLASS_$_CBPILParams
+ _OBJC_CLASS_$_ConfidenceEstimatorStats
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_PILContainer
+ _OBJC_METACLASS_$_CBALSServiceClient
+ _OBJC_METACLASS_$_CBAnalyticsExtDisplayManager
+ _OBJC_METACLASS_$_CBFrameInfoProvider
+ _OBJC_METACLASS_$_CBPILNode
+ _OBJC_METACLASS_$_CBPILParams
+ _OBJC_METACLASS_$_ConfidenceEstimatorStats
+ _OBJC_METACLASS_$_PILContainer
+ _PILEventCallback
+ _ZN4AABC16SetDisplayFactorEfb.cold.1
+ _ZN4AABC16SetDisplayFactorEfb.cold.2
+ _ZN4AABC16SetDisplayFactorEfb.cold.3
+ _ZN4AABC16SetDisplayFactorEfb.cold.4
+ _ZN4AABC4openEjiPFvPvPK10__CFStringPKvES0_.cold.14
+ _ZNK31PerceptualLuminanceThresholding27DurationFromPerceptualDeltaEf.cold.1
+ __25-[CBSBIM startMonitoring]_block_invoke.43
+ __27-[BLControl copyStatusInfo]_block_invoke.187
+ __27-[CBAurora startMonitoring]_block_invoke.12
+ __27-[CBAurora startMonitoring]_block_invoke_2.13
+ __28-[PILContainer setupModules]_block_invoke.cold.1
+ __31-[CBColorModule updateActivity]_block_invoke.202
+ __35-[CBHIDEventManager addHIDService:]_block_invoke.181
+ __37-[CBColorModule addHIDServiceClient:]_block_invoke.174
+ __37-[CBColorModule addHIDServiceClient:]_block_invoke.175
+ __38-[DisplayALSManager startALSIdleTimer]_block_invoke.143
+ __41-[CBMILInterface lookupMILServiceTrusted]_block_invoke.12
+ __47-[BLControl keyboardBacklightHIDDeviceArrived:]_block_invoke.256
+ __47-[SunriseSunsetProvider copySunriseSunsetInfo:]_block_invoke.cold.1
+ __48-[CBHIDEventManager updateInternalMedianFilter:]_block_invoke.89
+ __48-[SunriseSunsetProvider updateSunriseSunsetInfo]_block_invoke.cold.1
+ __51-[CBHIDEventManager initialiseHidEventSystemClient]_block_invoke.174
+ __51-[CBHIDEventManager initialiseHidEventSystemClient]_block_invoke.178
+ __52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.259
+ __53-[DisplayALSManager setDynamicSliderWithFade:length:]_block_invoke.139
+ __60-[DisplayALSManager setPerceptualBrightnessWithFade:length:]_block_invoke.140
+ __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.630
+ __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.630.cold.1
+ __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.637
+ __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.637.cold.1
+ __CFXCCT2xy_Generic
+ __DisplaySetProperty_block_invoke.540
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_CBAnalyticsExtDisplayManager
+ __OBJC_$_INSTANCE_METHODS_CBALSServiceClient
+ __OBJC_$_INSTANCE_METHODS_CBAnalyticsExtDisplayManager
+ __OBJC_$_INSTANCE_METHODS_CBFrameInfoProvider
+ __OBJC_$_INSTANCE_METHODS_CBPILNode
+ __OBJC_$_INSTANCE_METHODS_CBPILParams
+ __OBJC_$_INSTANCE_METHODS_ConfidenceEstimatorStats
+ __OBJC_$_INSTANCE_METHODS_PILContainer
+ __OBJC_$_INSTANCE_VARIABLES_CBALSServiceClient
+ __OBJC_$_INSTANCE_VARIABLES_CBAnalyticsExtDisplayManager
+ __OBJC_$_INSTANCE_VARIABLES_CBFrameInfoProvider
+ __OBJC_$_INSTANCE_VARIABLES_CBPILNode
+ __OBJC_$_INSTANCE_VARIABLES_CBPILParams
+ __OBJC_$_INSTANCE_VARIABLES_ConfidenceEstimatorStats
+ __OBJC_$_INSTANCE_VARIABLES_PILContainer
+ __OBJC_$_PROP_LIST_CBALSServiceClient
+ __OBJC_$_PROP_LIST_CBPILNode
+ __OBJC_$_PROP_LIST_CBPILParams
+ __OBJC_$_PROP_LIST_ConfidenceEstimatorStats
+ __OBJC_$_PROP_LIST_PILContainer
+ __OBJC_CLASS_PROTOCOLS_$_CBALSServiceClient
+ __OBJC_CLASS_PROTOCOLS_$_PILContainer
+ __OBJC_CLASS_RO_$_CBALSServiceClient
+ __OBJC_CLASS_RO_$_CBAnalyticsExtDisplayManager
+ __OBJC_CLASS_RO_$_CBFrameInfoProvider
+ __OBJC_CLASS_RO_$_CBPILNode
+ __OBJC_CLASS_RO_$_CBPILParams
+ __OBJC_CLASS_RO_$_ConfidenceEstimatorStats
+ __OBJC_CLASS_RO_$_PILContainer
+ __OBJC_METACLASS_RO_$_CBALSServiceClient
+ __OBJC_METACLASS_RO_$_CBAnalyticsExtDisplayManager
+ __OBJC_METACLASS_RO_$_CBFrameInfoProvider
+ __OBJC_METACLASS_RO_$_CBPILNode
+ __OBJC_METACLASS_RO_$_CBPILParams
+ __OBJC_METACLASS_RO_$_ConfidenceEstimatorStats
+ __OBJC_METACLASS_RO_$_PILContainer
+ __ZN14CoreBrightnessL11sbimLimits1E
+ __ZN4AABC41reportAutoBrightnessChangeToCoreAnalyticsEb
+ __ZNKSt3__110__val_exprINS_9_BinaryOpINS_7greaterIfEENS_8valarrayIfEES5_EEE3maxB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___20-[PILContainer stop]_block_invoke
+ ___21-[PILContainer start]_block_invoke
+ ___26-[CBSBIM dataTimerHandler]_block_invoke
+ ___27-[BLControl copyStatusInfo]_block_invoke_3
+ ___28-[PILContainer setupModules]_block_invoke
+ ___34-[ConfidenceEstimatorStats submit]_block_invoke
+ ___34-[ConfidenceEstimatorStats submit]_block_invoke_2
+ ___35-[PILContainer copyPropertyForKey:]_block_invoke
+ ___35-[PILContainer initWithParameters:]_block_invoke
+ ___35-[PILContainer setProperty:forKey:]_block_invoke
+ ___36-[PILContainer addHIDServiceClient:]_block_invoke
+ ___36-[PILContainer handleHIDEvent:from:]_block_invoke
+ ___37-[BLControl handlePILServiceArrival:]_block_invoke
+ ___39-[PILContainer removeHIDServiceClient:]_block_invoke
+ ___40-[BLControl addClientsToHIDEventManager]_block_invoke_2
+ ___41-[CBMILInterface lookupMILServiceTrusted]_block_invoke
+ ___42-[CBALSServiceClient handleHIDEvent:from:]_block_invoke
+ ___44-[ConfidenceEstimatorStats initWithModelID:]_block_invoke
+ ___45-[CBALSServiceClient removeHIDServiceClient:]_block_invoke
+ ___46+[CBAnalyticsExtDisplayManager sharedInstance]_block_invoke
+ ___46-[CBAnalyticsExtDisplayManager setUserActive:]_block_invoke
+ ___46-[CBAnalyticsExtDisplayManager startReporting]_block_invoke
+ ___46-[CBHIDEventManager initWithQueue:identifier:]_block_invoke
+ ___46-[CBHIDEventManager initWithQueue:identifier:]_block_invoke_2
+ ___48-[KeyboardBacklight forceBacklightUpdateRoutine]_block_invoke
+ ___48-[KeyboardBacklight forceBacklightUpdateRoutine]_block_invoke_2
+ ___48-[PILContainer sendNotificationForKey:andValue:]_block_invoke
+ ___48-[PILContainer sendNotificationForKey:andValue:]_block_invoke_2
+ ___49+[CBAnalytics userBrightnessChangeAfterSnapping:]_block_invoke
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke_2
+ ___53-[CBFrameInfoProvider registerObserver:withCallback:]_block_invoke
+ ___53-[CBFrameInfoProvider registerObserver:withCallback:]_block_invoke_2
+ ___53-[CBFrameInfoProvider registerObserver:withCallback:]_block_invoke_3
+ ___54-[CBAnalyticsExtDisplayManager sendEventLazy:andDict:]_block_invoke
+ ___54-[CBAnalyticsExtDisplayManager stopReportingInternal:]_block_invoke
+ ___57-[CBDisplayModuleSKL initWithBrightnessControl:andQueue:]_block_invoke
+ ___57-[CBDisplayModuleSKL initWithBrightnessControl:andQueue:]_block_invoke_2
+ ___58-[CBAnalyticsExtDisplayManager handleColorSampleInternal:]_block_invoke
+ ___70-[CBAnalyticsExtDisplayManager sendEventOnceADayLazyInternal:andDict:]_block_invoke
+ ___ZN14CBAuroraParams20loadFromCapabilitiesEP12NSDictionary_block_invoke.307
+ ___ZN14CBAuroraParams20loadFromCapabilitiesEP12NSDictionary_block_invoke.311
+ ____DisplayUpdateSlider_block_invoke.975
+ ____DisplayUpdateSlider_block_invoke.977
+ ___block_descriptor_40_e8_32o_e19_v40?0{?=QIBBBfff}8l
+ ___block_descriptor_40_e8_32o_e31_v16?0r^{?=IIQQQQIBBBfffQIBQQ}8l
+ ___block_descriptor_40_e8_32o_e39_v32?0^v8^v16^{__IOHIDServiceClient=}24l
+ ___block_descriptor_40_e8_32o_e50_v48?0Q8Q16"NSString"24"NSString"32"NSNumber"40l
+ ___block_descriptor_40_e8_32o_e79_v32?0"NSUUID"8"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>"16^B24l
+ ___block_descriptor_57_e8_32o40o_e5_v8?0l
+ ___block_descriptor_64_e8_32o40o48o56o_e19_"NSDictionary"8?0l
+ ___block_descriptor_72_e8_32o_e5_v8?0l
+ __block_literal_global.485
+ __block_literal_global.636
+ __block_literal_global.75
+ _defaultCurveLux
+ _defaultCurveNits
+ _objc_msgSend$allValues
+ _objc_msgSend$autoBrightnessOn
+ _objc_msgSend$blackBezel
+ _objc_msgSend$brightnessNotificationPowerOn
+ _objc_msgSend$curveLevel:
+ _objc_msgSend$displayWithDisplayId:
+ _objc_msgSend$dutyCycleRangeFetched
+ _objc_msgSend$fetchDutyCycleThresholdIfNeeded
+ _objc_msgSend$getDutyCycleThreshold:
+ _objc_msgSend$getMaximumAchievableBrightness
+ _objc_msgSend$getMinimumAchievableBrightness
+ _objc_msgSend$handlePILServiceArrival:
+ _objc_msgSend$hidServiceArrived:
+ _objc_msgSend$initWithDisplayServer:
+ _objc_msgSend$initWithDisplayServer:andQueue:
+ _objc_msgSend$initWithFirstDim:andSecondDim:
+ _objc_msgSend$initWithLong:
+ _objc_msgSend$initWithParameters:
+ _objc_msgSend$initWithParams:
+ _objc_msgSend$initWithQueue:PILParams:calibration:andALSServiceClient:
+ _objc_msgSend$initWithQueue:frameInfoProvider:andWindowServerDisplay:
+ _objc_msgSend$initialiseControllersWithCalibration:
+ _objc_msgSend$lookupMILServiceTrusted
+ _objc_msgSend$luminanceHistLogNitsSDR:andNitsEDR:
+ _objc_msgSend$newElementsArray
+ _objc_msgSend$pil
+ _objc_msgSend$pilCurveLux
+ _objc_msgSend$pilCurveNits
+ _objc_msgSend$pushNumberWeighted:withWeight:forFirstDimValue:
+ _objc_msgSend$readData:withSize:fromRegister:
+ _objc_msgSend$registerObserver:withCallback:
+ _objc_msgSend$setAutoBrightnessOn:
+ _objc_msgSend$setBuiltInDisplay:
+ _objc_msgSend$setEcoModeOn:
+ _objc_msgSend$setFirstBrightnessUpdate:
+ _objc_msgSend$setupALSServices
+ _objc_msgSend$setupModules
+ _objc_msgSend$shouldUpdateEDRForRequestedHeadroom:targetHeadroom:
+ _objc_msgSend$startPILServiceLookup
+ _objc_msgSend$stopPILServiceLookup
+ _objc_msgSend$tearDownModules
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$updateCILRangeIfNeeded
+ _objc_msgSend$updateMILRangeIfNeeded
+ _objc_msgSend$userBrightnessChangeAfterSnapping:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$writeDataTrusted:
+ _os_signpost_id_generate
+ _pilServiceArrivalCallback
+ copyALSPluginProtected.cold.1
+ copyPreferenceForKey.cold.1
+ load_libEDR.cold.1
+ lookupMILServiceTrusted.once
+ mach_time_now_in_milliseconds.cold.1
+ mach_time_now_in_nanoseconds.cold.1
+ mach_time_now_in_seconds.cold.1
+ mach_time_to_milliseconds.cold.1
+ mach_time_to_nanoseconds.cold.1
+ mach_time_to_seconds.cold.1
+ pluginArrivedBlock_block_invoke_2.cold.1
+ pluginDepartureBlock_block_invoke.cold.2
+ setPreferenceForKey.cold.1
- +[CBAnalytics cuveLevel:]
- +[CBAnalytics deviceColor:]
- +[CBAnalytics displayMaxCurrent:]
- +[CBAnalyticsManager handleColorSample:]
- +[CBAnalyticsManager sendEventOnceADayLazy:andDict:]
- +[CBAnalyticsManager sharedInstance]
- +[CBAnalyticsManager stopReporting:]
- -[AmbientLightSensorStats cancelALSIdleTimer]
- -[AmbientLightSensorStats dealloc]
- -[AmbientLightSensorStats floorTo2SigFig:]
- -[AmbientLightSensorStats init]
- -[AmbientLightSensorStats logALSEnabled:userChanged:]
- -[AmbientLightSensorStats logALSEvent:]
- -[AmbientLightSensorStats logALSEvent:].cold.1
- -[AmbientLightSensorStats logALSEvent:].cold.2
- -[AmbientLightSensorStats logALSEventLocked:forStats:]
- -[AmbientLightSensorStats logALSIdleEvent:]
- -[AmbientLightSensorStats logUserBrightnessChanged]
- -[AmbientLightSensorStats reportActivityFilteredLux:range:]
- -[AmbientLightSensorStats reportActivityFilteredLux:range:].cold.1
- -[AmbientLightSensorStats reportUnfilteredLux:range:changes:enabled:]
- -[AmbientLightSensorStats startALSIdleTimer]
- -[AmbientLightSensorStats updateALSEnabled:]
- -[CBAnalyticsManager dealloc]
- -[CBAnalyticsManager handleColorSampleInternal:]
- -[CBAnalyticsManager init]
- -[CBAnalyticsManager init].cold.1
- -[CBAnalyticsManager init].cold.2
- -[CBAnalyticsManager init].cold.3
- -[CBAnalyticsManager isFirstEventToday:]
- -[CBAnalyticsManager isSameDay:asDay:]
- -[CBAnalyticsManager logAllColorSamples]
- -[CBAnalyticsManager logAllColorSamples].cold.1
- -[CBAnalyticsManager logColorSample:withType:]
- -[CBAnalyticsManager sendEventLazy:andDict:]
- -[CBAnalyticsManager sendEventOnceADayLazyInternal:andDict:]
- -[CBAnalyticsManager setUserActive:]
- -[CBAnalyticsManager startReporting]
- -[CBAnalyticsManager stopReportingInternal:]
- -[CBAnalyticsManager storeTimestamp:forEventName:]
- -[CBAnalyticsManager stringForType:]
- -[CBAurora initWithQueue:andDisplayModule:andBrtCapabilities:]
- -[CBFrameStats initWithQueue:]
- -[CBFrameStats initialiseWindowServerDisplay]
- -[CBFrameStats initialiseWindowServerDisplay].cold.1
- -[CBMILInterface startMILServiceLookup]
- -[CBMILInterface writeData:withSize:toRegister:withAddressSize:]
- -[KeyboardBacklight didUpdateBacklightLevel:brightness:result:error:].cold.1
- -[KeyboardBacklight didUpdateBacklightLevel:brightness:result:error:].cold.2
- -[KeyboardBacklight updateBacklightDeviceWithFadeSpeed:commit:reason:].cold.2
- -[PILABCurve initWithConfiguration:]
- -[PILABCurve initWithConfiguration:].cold.1
- -[PILABCurve setLinearBrightnessMin:andMax:]
- -[PILABCurveConfiguration dealloc]
- -[PILABCurveConfiguration description]
- -[PILABCurveConfiguration hasValidLUT]
- -[PILABCurveConfiguration isEnergySaving]
- -[PILABCurveConfiguration lut]
- -[PILABCurveConfiguration setIsEnergySaving:]
- -[PILABCurveConfiguration setLut:]
- -[PILAutoBrightnessModule addHIDALSService:]
- -[PILAutoBrightnessModule addHIDServiceClient:]
- -[PILAutoBrightnessModule getAggregatedLux:]
- -[PILAutoBrightnessModule handleHIDEvent:from:]
- -[PILAutoBrightnessModule initWithQueue:andBrtCapabilities:]
- -[PILAutoBrightnessModule initWithQueue:andBrtCapabilities:].cold.1
- -[PILAutoBrightnessModule observeValueForKeyPath:ofObject:change:context:]
- -[PILAutoBrightnessModule registerForPILNotifications]
- -[PILAutoBrightnessModule removeHIDServiceClient:]
- -[PILAutoBrightnessModule unregisterForPILNotifications]
- -[SunriseSunsetProvider logLevel]
- -[SunriseSunsetProvider setLogLevel:]
- GCC_except_table132
- GCC_except_table136
- GCC_except_table217
- GCC_except_table249
- GCC_except_table264
- GCC_except_table71
- GCC_except_table88
- GCC_except_table98
- OBJC_IVAR_$_AmbientLightSensorStats._activityFilteredStats
- OBJC_IVAR_$_AmbientLightSensorStats._activityNotification
- OBJC_IVAR_$_AmbientLightSensorStats._alsEventLock
- OBJC_IVAR_$_AmbientLightSensorStats._alsIdleEventStartTime
- OBJC_IVAR_$_AmbientLightSensorStats._alsIdleTimer
- OBJC_IVAR_$_AmbientLightSensorStats._clamshellNotification
- OBJC_IVAR_$_AmbientLightSensorStats._clamshellOpened
- OBJC_IVAR_$_AmbientLightSensorStats._clamshellStateIterator
- OBJC_IVAR_$_AmbientLightSensorStats._hidEventSystemClient
- OBJC_IVAR_$_AmbientLightSensorStats._port
- OBJC_IVAR_$_AmbientLightSensorStats._reportTimer
- OBJC_IVAR_$_AmbientLightSensorStats._unfilteredStats
- OBJC_IVAR_$_AmbientLightSensorStats._userBrightnessTimer
- OBJC_IVAR_$_AmbientLightSensorStats._userIsActive
- OBJC_IVAR_$_CBAnalyticsManager._logHandle
- OBJC_IVAR_$_CBAnalyticsManager._queue
- OBJC_IVAR_$_CBAnalyticsManager._reportTimer
- OBJC_IVAR_$_CBAnalyticsManager._timestamps
- OBJC_IVAR_$_CBAnalyticsManager._userActive
- OBJC_IVAR_$_CBAnalyticsManager.samples
- OBJC_IVAR_$_CBDisplayContainerSKL._pilBrightnessModule
- OBJC_IVAR_$_CBFrameStats._windowServerDisplay
- OBJC_IVAR_$_DisplayALSManager._alsStats
- OBJC_IVAR_$_KeyboardBacklight._elements
- OBJC_IVAR_$_NightModeControl._logLevel
- OBJC_IVAR_$_PILABCurve._luxToNits
- OBJC_IVAR_$_PILABCurveConfiguration._isEnergySaving
- OBJC_IVAR_$_PILABCurveConfiguration._lut
- OBJC_IVAR_$_PILAutoBrightnessModule._alsServiceClients
- OBJC_IVAR_$_PILAutoBrightnessModule._pilStateMonitor
- OBJC_IVAR_$_SunriseSunsetProvider._logLevel
- PMRootStateChanged.cold.1
- PMRootStateChanged.cold.2
- _CFRunLoopAddSource
- _CFRunLoopGetCurrent
- _IONotificationPortGetRunLoopSource
- _Mul33MatrixBy33Matrix
- _NSLog
- _OBJC_CLASS_$_AmbientLightSensorStats
- _OBJC_CLASS_$_CBAnalyticsManager
- _OBJC_CLASS_$_PILABCurveConfiguration
- _OBJC_METACLASS_$_AmbientLightSensorStats
- _OBJC_METACLASS_$_CBAnalyticsManager
- _OBJC_METACLASS_$_PILABCurveConfiguration
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _PMRootStateChanged
- _ZN4AABC16SetDisplayFactorEf.cold.1
- _ZN4AABC16SetDisplayFactorEf.cold.2
- _ZN4AABC16SetDisplayFactorEf.cold.3
- _ZN4AABC16SetDisplayFactorEf.cold.4
- __25-[CBSBIM startMonitoring]_block_invoke.33
- __27-[BLControl copyStatusInfo]_block_invoke.184
- __27-[CBAurora startMonitoring]_block_invoke.13
- __27-[CBAurora startMonitoring]_block_invoke_2.14
- __31-[AmbientLightSensorStats init]_block_invoke.cold.1
- __31-[AmbientLightSensorStats init]_block_invoke.cold.2
- __31-[CBColorModule updateActivity]_block_invoke.205
- __35-[CBHIDEventManager addHIDService:]_block_invoke.177
- __37-[CBColorModule addHIDServiceClient:]_block_invoke.177
- __37-[CBColorModule addHIDServiceClient:]_block_invoke.178
- __38-[DisplayALSManager startALSIdleTimer]_block_invoke.144
- __47-[BLControl keyboardBacklightHIDDeviceArrived:]_block_invoke.250
- __47-[CBDisplayContainerSKL setupBrightnessModules]_block_invoke.167
- __47-[CBDisplayContainerSKL setupBrightnessModules]_block_invoke_2.168
- __47-[CBDisplayContainerSKL setupBrightnessModules]_block_invoke_3.166
- __47-[CBDisplayContainerSKL setupBrightnessModules]_block_invoke_3.166.cold.1
- __48-[CBHIDEventManager updateInternalMedianFilter:]_block_invoke.84
- __51-[CBHIDEventManager initialiseHidEventSystemClient]_block_invoke.169
- __51-[CBHIDEventManager initialiseHidEventSystemClient]_block_invoke.173
- __52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.246
- __53-[DisplayALSManager setDynamicSliderWithFade:length:]_block_invoke.140
- __60-[DisplayALSManager setPerceptualBrightnessWithFade:length:]_block_invoke.141
- __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.628
- __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.628.cold.1
- __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.635
- __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.635.cold.1
- __CFXCCT2xy_Shifted
- __DisplaySetProperty_block_invoke.537
- __OBJC_$_CLASS_METHODS_CBAnalyticsManager
- __OBJC_$_INSTANCE_METHODS_AmbientLightSensorStats
- __OBJC_$_INSTANCE_METHODS_CBAnalyticsManager
- __OBJC_$_INSTANCE_METHODS_PILABCurveConfiguration
- __OBJC_$_INSTANCE_VARIABLES_AmbientLightSensorStats
- __OBJC_$_INSTANCE_VARIABLES_CBAnalyticsManager
- __OBJC_$_INSTANCE_VARIABLES_PILABCurveConfiguration
- __OBJC_$_PROP_LIST_PILABCurveConfiguration
- __OBJC_$_PROP_LIST_SunriseSunsetProvider
- __OBJC_CLASS_RO_$_AmbientLightSensorStats
- __OBJC_CLASS_RO_$_CBAnalyticsManager
- __OBJC_CLASS_RO_$_PILABCurveConfiguration
- __OBJC_METACLASS_RO_$_AmbientLightSensorStats
- __OBJC_METACLASS_RO_$_CBAnalyticsManager
- __OBJC_METACLASS_RO_$_PILABCurveConfiguration
- __ZGVZ48-[CBSBIM mitigatedHeadroomFromRequestedHeadroom]E15recoveryHRdelta
- __ZGVZ48-[CBSBIM mitigatedHeadroomFromRequestedHeadroom]E17mitigationHRdelta
- __ZN4AABC16SetDisplayFactorEf
- __ZNKSt3__110__val_exprINS_9_BinaryOpINS_7greaterIfEENS_8valarrayIfEES5_EEE3maxB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__14listIN3AAB11CurveUpdateENS_9allocatorIS2_EEE6spliceENS_21__list_const_iteratorIS2_PvEERS5_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne180100IPfS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ48-[CBSBIM mitigatedHeadroomFromRequestedHeadroom]E15recoveryHRdelta
- __ZZ48-[CBSBIM mitigatedHeadroomFromRequestedHeadroom]E17mitigationHRdelta
- ___31-[AmbientLightSensorStats init]_block_invoke
- ___36+[CBAnalyticsManager sharedInstance]_block_invoke
- ___36-[CBAnalyticsManager setUserActive:]_block_invoke
- ___36-[CBAnalyticsManager startReporting]_block_invoke
- ___44-[AmbientLightSensorStats startALSIdleTimer]_block_invoke
- ___44-[CBAnalyticsManager sendEventLazy:andDict:]_block_invoke
- ___44-[CBAnalyticsManager stopReportingInternal:]_block_invoke
- ___47-[PILAutoBrightnessModule handleHIDEvent:from:]_block_invoke
- ___48-[CBAnalyticsManager handleColorSampleInternal:]_block_invoke
- ___50-[PILAutoBrightnessModule removeHIDServiceClient:]_block_invoke
- ___51-[AmbientLightSensorStats logUserBrightnessChanged]_block_invoke
- ___60-[CBAnalyticsManager sendEventOnceADayLazyInternal:andDict:]_block_invoke
- ___ZN14CBAuroraParams20loadFromCapabilitiesEP12NSDictionary_block_invoke.310
- ___ZN14CBAuroraParams20loadFromCapabilitiesEP12NSDictionary_block_invoke.314
- ____DisplayUpdateSlider_block_invoke.972
- ____DisplayUpdateSlider_block_invoke.974
- ___block_descriptor_120_e8_32o_e5_v8?0l
- ___block_descriptor_40_e8_32o_e28_v16?0r^{?=IIQQQQIBBBfffQI}8l
- __block_literal_global.461
- __block_literal_global.632
- __block_literal_global.69
- __dispatch_main_q
- _kDefaultBrightenDuration1
- _kDefaultDimDuration1
- _luxToNitsDefault
- _msgtracer_log_with_keys_skip_nulls
- _objc_msgSend$L
- _objc_msgSend$LDevice
- _objc_msgSend$LDeviceOff
- _objc_msgSend$LLPM
- _objc_msgSend$LOff
- _objc_msgSend$cancelALSIdleTimer
- _objc_msgSend$cuveLevel:
- _objc_msgSend$deviceColor:
- _objc_msgSend$displayMaxCurrent:
- _objc_msgSend$displays
- _objc_msgSend$floorTo2SigFig:
- _objc_msgSend$hasValidLUT
- _objc_msgSend$initWithQueue:andBrtCapabilities:
- _objc_msgSend$initWithQueue:andDisplayModule:andBrtCapabilities:
- _objc_msgSend$initialiseWindowServerDisplay
- _objc_msgSend$logALSEnabled:userChanged:
- _objc_msgSend$logALSEvent:
- _objc_msgSend$logALSEventLocked:forStats:
- _objc_msgSend$logALSIdleEvent:
- _objc_msgSend$logUserBrightnessChanged
- _objc_msgSend$lut
- _objc_msgSend$reportActivityFilteredLux:range:
- _objc_msgSend$reportUnfilteredLux:range:changes:enabled:
- _objc_msgSend$setLogLevel:
- _objc_msgSend$setLut:
- _objc_msgSend$startMILServiceLookup
- _objc_msgSend$updateALSEnabled:
- _objc_msgSend$writeData:withSize:toRegister:withAddressSize:
- _postMessageTracerLog
CStrings:
+ "%s: found client for MIL Control: %{public}@"
+ "-[CBMILInterface hidServiceArrived:]"
+ "-[PILContainer initWithParameters:]"
+ ".AliasingMitigationsCount"
+ ".ConfidenceEstimator"
+ ".UserBrightnessAfterSnapping"
+ "@\"AABCHistograms\""
+ "@\"CBALSServiceClient\""
+ "@\"CBFrameInfoProvider\""
+ "@\"CBHistogramBuilder2D\""
+ "@\"CBPILParams\""
+ "@44@0:8^f16^f24Q32B40"
+ "AOTCurve"
+ "AliasingMitigation.Active"
+ "AliasingMitigationActive"
+ "B24@0:8^S16"
+ "B28@0:8f16^f20"
+ "B40@0:8@16q24@32"
+ "Backlight update is scheduled already (in %f ms)."
+ "CBALSServiceClient"
+ "CBAODMinNits"
+ "CBAnalyticsExtDisplayManager"
+ "CBAnalyticsExtDisplayManager setUserActive=%d _userActive=%d"
+ "CBFrameInfoProvider"
+ "CBPILNode"
+ "CBPILParams"
+ "CBPILs"
+ "CIL minimum achieavable brightness: %f ; CIL maximum achieavable brightness: %f"
+ "ConfidenceEstimatorStats"
+ "CoreDuet framework dynamic load failed"
+ "Could not fetch duty cycle range for MIL Controller"
+ "Creating NightShift defaults status info"
+ "Creating default status info"
+ "CurveLevelHigh"
+ "CurveLevelLow"
+ "CurveLevelMed"
+ "Defaults invalid"
+ "Defaults valid and updated: %@"
+ "Display off with algoState=%d ts=%f"
+ "Duet context store not available"
+ "ERROR - sunrise/sunset provider not loaded information not available"
+ "EXBrightPILBrightness"
+ "FATAL ERROR - unable to obtain OFF transition time"
+ "FATAL ERROR - unable to obtain ON transition time"
+ "FATAL ERROR - unable to obtain sunrise date"
+ "FATAL ERROR - unable to obtain sunset date"
+ "Failed to create observers dictionary"
+ "Failed to create queue for FrameInfo!"
+ "Failed to fetch MIL duty cycle threshold correctly; readSuccess 0x%x"
+ "Failed to find WindowServer display #%d, frame information will not work"
+ "Failed to set MIL Brightness correctly; writeSuccess 0x%x"
+ "Failed with %d"
+ "Force Night Shift update on system wake"
+ "Initialised PIL Container"
+ "Invalid pil service arrived"
+ "Invalid service"
+ "Keyboard backlight update to %f level and %f brightness failed with error %@"
+ "Keyboard backlight updated successfully - level = %f, brightness = %f"
+ "LDeviceOff_EDR"
+ "LDevice_EDR"
+ "LLPM_EDR"
+ "LOff_EDR"
+ "LPM_EDR"
+ "L_EDR"
+ "MIL Controller updated with min duty cycle: %i and max duty cycle: %i"
+ "MIL minimum achieavable brightness: %f ; MIL maximum achieavable brightness: %f"
+ "Night Shift initialised: %@"
+ "Night Shift terminating"
+ "Night mode switch from user %@ to user %@"
+ "NightShift defaults found and valid"
+ "NightShift defaults invalid"
+ "NightShift status from preferences: %@"
+ "NightShift status update: %@ = %@"
+ "PIL"
+ "PIL (id: %lu) added to dictionary = %@"
+ "PIL device (ID=%@) arrived"
+ "PIL not supported"
+ "PILBrightnessModule"
+ "PILContainer"
+ "PILContainer.m"
+ "PILCurveDescription"
+ "Pdelta=%f timeConstant=%f i=%d"
+ "Ramp update denied (currentRampTarget: %f -> targetNits: %f) - target change too small (%f); ramp ongoing: %s"
+ "SBIM Monitoring"
+ "SBIM Request"
+ "Sunrise/Sunset transitions overlaping coeff=%f trLenghtActual=%f"
+ "SunriseSunsetProvider initialised successfully"
+ "SunriseSunsetProvider terminating"
+ "T@\"CBFloatArray\",R,V_pilCurveLux"
+ "T@\"CBFloatArray\",R,V_pilCurveNits"
+ "T@\"CBHistogramBuilder\",R,V_LDeviceOff_EDR"
+ "T@\"CBHistogramBuilder\",R,V_LDevice_EDR"
+ "T@\"CBHistogramBuilder\",R,V_LLPM_EDR"
+ "T@\"CBHistogramBuilder\",R,V_LOff_EDR"
+ "T@\"CBHistogramBuilder\",R,V_L_EDR"
+ "T@\"CBHistogramBuilder2D\",R,V_outputsCE"
+ "T@\"CBPILParams\",R,V_pil"
+ "TB,R,V_blackBezel"
+ "TB,R,V_dutyCycleRangeFetched"
+ "TB,V_autoBrightnessOn"
+ "TB,V_builtInDisplay"
+ "TB,V_ecoModeOn"
+ "TB,V_firstBrightnessUpdate"
+ "Tf,V_lastBrightnessUpdateNits"
+ "Tf,V_lastBrightnessUpdateNitsEDR"
+ "Tf,V_lastBrightnessUpdateTimestamp"
+ "Violation RGB=(%u,%u,%u) over %{xcode:duration}llu"
+ "Warning - invalid sunrise/sunset info, using defaults"
+ "[%f] START transition (%f -> %f) in %f sec "
+ "[New MIL Event] eventTimestamp=%llu PILData.(pilEnablementStatus=%i) \n"
+ "^{AABC=^^?ffffffffffffff^{UpdateCurveStrategy}{mutex={_opaque_pthread_mutex_t=q[56c]}}BfBii^{__IOHIDServiceClient}qff^?^viii^{__CFDictionary}^{__CFDictionary}BB^{__Display}f^{__CFDictionary}^{__CFDictionary}BBBBBBiB^{ALS}^{ALS}^{__IOHIDServiceClient}^{__IOHIDServiceClient}ifffBBiiiiiiffffffffII{?=ffff}i@IffffffB{_ALS_Struct=fiiiifffii}fiddfiIfffffffi[3{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}]{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{?=B{?=ff}{?=ff}{?=ff}f}{CurveCap=[4f][4f]d}{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}B[3{CustomCurve=[20f][20f]i}][3{CustomCurve=[20f][20f]i}]{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}ifIIIB{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}dB{?=I[3d]i}{?=Biddd}BBIffBBBf{_SETTINGS=ii{_INTERNAL_SETTINGS=iiifff}}iB{?={?=ff}{?=BB(_restriction={?=fffff}{?=ffff[2{?=[6f][6f]}]})}{?=BB(_restriction={?=fffff}{?=ffff[2{?=[6f][6f]}]})}}{?=i[12d][9d]QQI@}Bq@@IBBffiIIIii^fiffffff^{PerceptualLuminanceThresholding}IfiQi@@{?=fBfB}B}"
+ "_LDeviceOff_EDR"
+ "_LDevice_EDR"
+ "_LLPM_EDR"
+ "_LOff_EDR"
+ "_L_EDR"
+ "_aliasingMitigationActive"
+ "_alsServiceClient"
+ "_alsServices"
+ "_analyticsHist"
+ "_analyticsIlluminanceHist"
+ "_autoBrightnessOn"
+ "_backlightUpdateQueue"
+ "_blackBezel"
+ "_builtInDisplay"
+ "_cilBrightnessRangeSet"
+ "_currentBrightness"
+ "_currentEnableState"
+ "_currentFadeSpeed"
+ "_currentLevel"
+ "_ecoModeOn"
+ "_edgeMappingConfidence"
+ "_edgeMappingStrength"
+ "_firstABUpdate"
+ "_frameInfoProvider"
+ "_ioNotificationObjectPIL"
+ "_ioNotificationPortPIL"
+ "_ioServiceArrivalIteratorPIL"
+ "_isSnapping"
+ "_lastBrightnessUpdateNits"
+ "_lastBrightnessUpdateNitsEDR"
+ "_lastBrightnessUpdateTimestamp"
+ "_lastUserBrightness"
+ "_maximumAchievableBrightness"
+ "_milBrightnessRangeSet"
+ "_milHIDSystemClient"
+ "_milPlugin"
+ "_minimumAchievableBrightness"
+ "_modelID"
+ "_observers"
+ "_outputsCE"
+ "_params"
+ "_pil"
+ "_pilContainers"
+ "_pilCurveLux"
+ "_pilCurveNits"
+ "_snappingTimestamp"
+ "_timerQueue"
+ "aliasingMitigationsCount:"
+ "allValues"
+ "already stuck in a duet query, passing"
+ "already stuck in a querry, passing"
+ "autoBrightnessOn"
+ "black-bezel"
+ "blackBezel"
+ "blue light reduction factor ramp done (%f -> %f)"
+ "builtInDisplay"
+ "calling back with sun schedule update"
+ "cancel current transition"
+ "cancel next transition schedule"
+ "change to sun mode not permitted"
+ "clock changed"
+ "collectStrength:andConfidence:"
+ "com.apple.CoreBrightness.CBALSServiceClient"
+ "com.apple.CoreBrightness.CBAnalyticsExtDisplayManager"
+ "com.apple.CoreBrightness.FrameInfo"
+ "com.apple.CoreBrightness.KeyboardBacklight.BacklightUpdates"
+ "com.apple.CoreBrightness.NightShift"
+ "com.apple.CoreBrightness.PILAutoBrightnessModule"
+ "com.apple.CoreBrightness.PILContainer"
+ "com.apple.CoreBrightness.PILNode"
+ "confidenceEdge"
+ "currentPILBrightness"
+ "curveLevel:"
+ "disable all timers"
+ "dispatch time overflow - clamping to DISPATCH_TIME_FOREVER"
+ "display2.off_EDR"
+ "display2_EDR"
+ "displayWithDisplayId:"
+ "dutyCycleRangeFetched"
+ "dynamic-pil"
+ "ecoModeOn"
+ "error on initialisation"
+ "error: failed to create PIL container for service"
+ "factor=%f period=%f"
+ "fetchDutyCycleThresholdIfNeeded"
+ "firstBrightnessUpdate"
+ "flag=%d isDaylight=%d"
+ "getDutyCycleThreshold:"
+ "getMaximumAchievableBrightness"
+ "getMinimumAchievableBrightness"
+ "handlePILServiceArrival:"
+ "hidServiceArrived:"
+ "i24@0:8^S16"
+ "i40@0:8^S16^Q24Q32"
+ "inactivity check passed"
+ "initWithDisplayServer:"
+ "initWithDisplayServer:andQueue:"
+ "initWithLong:"
+ "initWithLuxArray:nitsArray:lutSize:andBlackBezel:"
+ "initWithModelID:"
+ "initWithParameters:"
+ "initWithParams:"
+ "initWithQueue:PILParams:calibration:andALSServiceClient:"
+ "initWithQueue:frameInfoProvider:andWindowServerDisplay:"
+ "initialiseControllersWithCalibration:"
+ "insufficient number of records in schedule"
+ "internal settings workaround"
+ "lastBrightnessUpdateNits"
+ "lastBrightnessUpdateNitsEDR"
+ "lastBrightnessUpdateTimestamp"
+ "lookupMILServiceTrusted"
+ "lookupMILServiceUntrusted"
+ "luminanceHistLogNitsSDR:andNitsEDR:"
+ "mitigations"
+ "mode=%d enable=%d option=%d"
+ "modelType"
+ "newElementsArray"
+ "next transition at %f (in %f seconds) \n"
+ "now=%f enabled=%d mode=%d algo=%d"
+ "off_EDR"
+ "outputsCE"
+ "pil"
+ "pil-aab-curve-lux"
+ "pil-aab-curve-nits"
+ "pilCurveLux"
+ "pilCurveNits"
+ "prev. sunrise=%f, prev. sunset=%f, sunrise=%f, sunset=%f, min factor=%f, max factor=%f"
+ "readData:withSize:fromRegister:"
+ "register async callback block"
+ "registerObserver:withCallback:"
+ "removing old pil container for id %@"
+ "reverting back to sun mode"
+ "setAutoBrightnessOn:"
+ "setBuiltInDisplay:"
+ "setEcoModeOn:"
+ "setFirstBrightnessUpdate:"
+ "setLastBrightnessUpdateNits:"
+ "setLastBrightnessUpdateNitsEDR:"
+ "setLastBrightnessUpdateTimestamp:"
+ "setupALSServices"
+ "setupModules"
+ "shouldUpdateEDRForRequestedHeadroom:targetHeadroom:"
+ "standard_EDR"
+ "startPILServiceLookup"
+ "stopPILServiceLookup"
+ "strengthEdge"
+ "sun schedule dictionary : %@"
+ "sunprovider"
+ "sunrise/sunset info: %@"
+ "sunrise/sunset info: unavailable but permited"
+ "sunrise/sunset not permitted"
+ "sunrise/sunset querry timeout"
+ "sunrise/sunset returned on time"
+ "taking a mark to return to sun mode"
+ "tear down PIL modules"
+ "tearDownModules"
+ "time zone changed from %@ to %@"
+ "timeout detected, calling back with an update"
+ "transitions overlaping coeff=%f trLenghtActual=%f"
+ "unable to create pil containers dictionary"
+ "unexpected status, ignore"
+ "unregisterObserver:"
+ "unregistering async callback block"
+ "unregistering notification"
+ "update NightShift schedule: %@"
+ "update from mode=%d to new mode=%d"
+ "update sun mode permission from %d to %d"
+ "updateCILRangeIfNeeded"
+ "updateMILRangeIfNeeded"
+ "updated factor=%f with fade %f"
+ "user changed mode - clearing out the sun mode revert mark"
+ "userBrightnessChangeAfterSnapping:"
+ "v16@?0r^{?=IIQQQQIBBBfffQIBQQ}8"
+ "v32@?0@\"NSUUID\"8@\"CBContainer<CBContainerProtocol><CBHIDServiceProtocol>\"16^B24"
+ "v40@?0{?=QIBBBfff}8"
+ "v48@0:8{?=QIBBBfff}16"
+ "v48@?0Q8Q16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40"
+ "valueWithPointer:"
+ "warning - sunrise/sunset key not found, waiting for recovery"
+ "writeDataTrusted:"
+ "writeDataUntrusted:withSize:toRegister:withAddressSize:"
- "%s mode=%d enable=%d option=%d"
- "%s: %@"
- "%s: %@ \n"
- "%s: %@ (%@) -> %@ \n"
- "%s: CoreDuet framework dynamic load failed \n"
- "%s: CoreDuet loaded dynamically \n"
- "%s: Creating defaults status info \n"
- "%s: Defaults found and invalid \n"
- "%s: Defaults found and valid \n"
- "%s: Duet context store not available \n"
- "%s: ERROR - sunrise/sunset provider not loaded information not available \n"
- "%s: ERROR: unexpected status, ignore \n"
- "%s: Force Night Shift update on system wake"
- "%s: Sunrise/Sunset transitions overlaping coeff=%f trLenghtActual=%f \n"
- "%s: SunriseSunsetProvider initialisation \n"
- "%s: Warning - invalid sunrise/sunset info, using defaults\n"
- "%s: [%f] START transition (%f -> %f) in %f sec "
- "%s: already stuck in a querry, passing \n"
- "%s: blue light reduction factor ramp done (%f -> %f)\n"
- "%s: calling back with an update \n"
- "%s: cancel current transition \n"
- "%s: cancel next transition schedule \n"
- "%s: change to sun mode not permitted \n"
- "%s: check incativity \n"
- "%s: disable all timers \n"
- "%s: dispatch time overflow - clamping to DISPATCH_TIME_FOREVER"
- "%s: error on initialisation \n"
- "%s: factor=%f"
- "%s: factor=%f period=%f"
- "%s: flag=%d isDaylight=%d\n"
- "%s: inactivity check passed \n"
- "%s: insufficient number of records in schedule"
- "%s: internal settings workaround \n"
- "%s: mode=%d \n"
- "%s: next transition at %f (in %f seconds) \n"
- "%s: now=%f"
- "%s: now=%f enabled=%d mode=%d algo=%d\n"
- "%s: prev. sunrise=%f, prev. sunset=%f, sunrise=%f, sunset=%f, min factor=%f, max factor=%f\n"
- "%s: register async callback block \n"
- "%s: reverting back to sun mode \n"
- "%s: sunrise/sunset info: %@"
- "%s: sunrise/sunset info: unavailable but permited \n"
- "%s: sunrise/sunset not permitted \n"
- "%s: sunrise/sunset querry timeout \n"
- "%s: sunrise/sunset returned on time\n"
- "%s: taking a mark to return to sun mode \n"
- "%s: timeout detected, calling back with an update \n"
- "%s: transitions overlaping coeff=%f trLenghtActual=%f \n"
- "%s: unregistering async callback block \n"
- "%s: unregistering notification \n"
- "%s: user changed mode - clearing out the sun mode revert mark \n"
- "%s: warning - sunrise/sunset key not found, waiting for recovery \n"
- "-[NightModeControl cancelSchedule]"
- "-[NightModeControl cancelTransition]"
- "-[NightModeControl clockChanged]_block_invoke"
- "-[NightModeControl copyStatusDictionaryFromPrefs]"
- "-[NightModeControl dealloc]"
- "-[NightModeControl enableBlueLightReduction:withOption:]"
- "-[NightModeControl initWithSupportObject:queue:callback:]"
- "-[NightModeControl initiateTransitionTo:andRampLength:]"
- "-[NightModeControl reevaluateCurrentStateWithFactorFadeOption:]"
- "-[NightModeControl retrieveSunriseSunsetTimesFromBackup:]"
- "-[NightModeControl scheduleNextTransition:withType:]"
- "-[NightModeControl setMode:]"
- "-[NightModeControl setNightModeFactor:withFadePeriod:]"
- "-[NightModeControl setProperty:forKey:]"
- "-[NightModeControl setSchedule:]"
- "-[NightModeControl setSunPermitted:]"
- "-[NightModeControl switchToUser:]"
- "-[NightModeControl tearDownAllTimers]"
- "-[NightModeControl timeZoneChanged]_block_invoke"
- "-[NightModeControl transitionTimerHandler]"
- "-[NightModeControl updateStatusDictionaryWithValue:forKey:]"
- "-[NightModeControl updateSunriseSunsetInfo:]"
- "-[NightModeControl updateTransitionTimes:]"
- "-[NightModeControl updateTransitionTimesFromSchedule:]"
- "-[NightModeControl updateTransitionTimesFromSunriseSunset:]"
- "-[SunriseSunsetProvider copySunriseSunsetInfo:]"
- "-[SunriseSunsetProvider copySunriseSunsetInfo:]_block_invoke"
- "-[SunriseSunsetProvider initWithCallback:]"
- "-[SunriseSunsetProvider registerBlock:]"
- "-[SunriseSunsetProvider unregisterBlock]"
- "-[SunriseSunsetProvider unregisterNotification]"
- "-[SunriseSunsetProvider updateSunriseSunsetInfo]"
- "-[SunriseSunsetProvider updateSunriseSunsetInfo]_block_invoke"
- ".DeviceColor"
- ".Display.CurrentMax"
- "@\"AmbientLightSensorStats\""
- "ALSStats: Lid closed"
- "ALSStats: Lid opened"
- "ALSStats: Received an ALS event with clamshell Open but NOT active, dropping lux value=%f"
- "ALSStats: Received an ALS event, but clamshell is closed...bailing"
- "ALSStats: User became active"
- "ALSStats: User became inactive"
- "ALSStats::logALSEvent initializing counts currentLux=%f\n"
- "ALSStats::logALSEventLocked: %s stats:\n\t incominglux=%f\n\t averageLux=%f\n\t lastLux=%f\n\t minLux=%f\n\t maxLux=%f\n\t averageLuxWeight=%f\n\t lastLuxWeight=%f\n\t timeAccumulated=%f\n\t timeSinceLastEventOrFilter=%f\n\t"
- "ALSStats::logALSIdleEvent User didn't change brightness within timeout\n"
- "ALSStats::logALSIdleEvent changed brightness within %ds\n"
- "ALSStats::logUserBrightnessChanged numChanges=%d\n"
- "ALSStats::reportActivityFilteredLux Reporting ALS stats averageLux=%d luxRange=%d\n"
- "ALSStats::reportUnfilteredLux Reporting ALS stats averageLux=%d luxRange=%d, userBrightnessChanges=%d alsEnabled=%d\n"
- "ALSStats::startALSIdleTimer ALSIdleTimer modified user prefs starting timer\n"
- "Activity Filtered"
- "AmbientLightSensorStats"
- "AppleARMBacklight"
- "Backlight update is scheduled already (in %f ms)"
- "Backlight updated successfully - level = %f, brightness = %f"
- "BlueLightReductionLogging"
- "CAWindowServer is not running"
- "CBAnalyticsManager"
- "CBAnalyticsManager setUserActive=%d _userActive=%d"
- "Display off with algoState=%d ts=%f\n"
- "DynamicPIL"
- "FATAL ERROR (%s) - unable to obtain OFF transition time\n"
- "FATAL ERROR (%s) - unable to obtain ON transition time\n"
- "FATAL ERROR (%s) - unable to obtain SR date\n"
- "FATAL ERROR (%s) - unable to obtain SS date\n"
- "Factor=%0.4f"
- "Failed to set MIL Brightness correctly; writeSuccessMSB 0x%x writeSuccessLSB 0x%x"
- "I20@0:8I16"
- "Invalid backlight service"
- "Night mode init"
- "Night mode switch user"
- "No elements"
- "PILAABCurve"
- "PILABCurveConfiguration"
- "PILCurveDescrption"
- "PILDynamicBrightness"
- "T@\"NSArray\",&,V_lut"
- "Ti,V_logLevel"
- "Turn off keyboard backlight"
- "Unfiltered"
- "[RAMP ONGOING] ramp update denied (currentRampTarget: %f -> targetNits: %f) - target change too small (%f)"
- "^^f"
- "^{AABC=^^?ffffffffffffff^{UpdateCurveStrategy}{mutex={_opaque_pthread_mutex_t=q[56c]}}BfBii^{__IOHIDServiceClient}qff^?^viii^{__CFDictionary}^{__CFDictionary}BB^{__Display}f^{__CFDictionary}^{__CFDictionary}BBBBBBiB^{ALS}^{ALS}^{__IOHIDServiceClient}^{__IOHIDServiceClient}ifffBBBiiiiiiffffffffII{?=ffff}i@IffffffB{_ALS_Struct=fiiiifffii}fiddfiIffffffi[3{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}]{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{?=B{?=ff}{?=ff}{?=ff}f}{CurveCap=[4f][4f]d}{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}B[3{CustomCurve=[20f][20f]i}][3{CustomCurve=[20f][20f]i}]{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}ifIIIB{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}dB{?=I[3d]i}{?=Biddd}BBIffBBBf{_SETTINGS=ii{_INTERNAL_SETTINGS=iiifff}}iB{?={?=ff}{?=BB(_restriction={?=fffff}{?=ffff[2{?=[6f][6f]}]})}{?=BB(_restriction={?=fffff}{?=ffff[2{?=[6f][6f]}]})}}{?=i[12d][9d]QQI@}q@@BBffiIIIii^fiffffff^{PerceptualLuminanceThresholding}IfiQi@@{?=fBfB}B}"
- "_activityFilteredStats"
- "_activityNotification"
- "_alsEventLock"
- "_alsIdleEventStartTime"
- "_alsIdleTimer"
- "_alsStats"
- "_clamshellOpened"
- "_clamshellStateIterator"
- "_elements"
- "_hidEventSystemClient"
- "_logLevel"
- "_lut"
- "_luxToNits"
- "_pilBrightnessModule"
- "_port"
- "_unfilteredStats"
- "_userBrightnessTimer"
- "_userIsActive"
- "cancelALSIdleTimer"
- "com.apple.BezelServices.ALSEnable"
- "com.apple.BezelServices.ALSStats"
- "com.apple.BezelServices.ALSStatsActivityFiltered"
- "com.apple.BezelServices.IdleTimer"
- "com.apple.CoreBrightness.CBAnalyticsManager"
- "com.apple.PILAutoBrightnessModule"
- "com.apple.corebrightness.harmony.state"
- "com.apple.message.result"
- "com.apple.message.value"
- "com.apple.message.value2"
- "com.apple.message.value3"
- "com.apple.message.value4"
- "cuveLevel:"
- "dataDictionary : %s"
- "deviceColor:"
- "displayMaxCurrent:"
- "displays"
- "energySaving=%d"
- "fail"
- "floorTo2SigFig:"
- "hasValidLUT"
- "initWithQueue:andBrtCapabilities:"
- "initWithQueue:andDisplayModule:andBrtCapabilities:"
- "initialiseWindowServerDisplay"
- "logALSEnabled:userChanged:"
- "logALSEvent:"
- "logALSEventLocked:forStats:"
- "logALSIdleEvent:"
- "logLevel"
- "logUserBrightnessChanged"
- "lut"
- "pass"
- "ramp denied (currentNits: %f -> targetNits: %f) - brightness change is too small (%f)"
- "reportActivityFilteredLux:range:"
- "reportUnfilteredLux:range:changes:enabled:"
- "setLogLevel:"
- "setLut:"
- "startMILServiceLookup"
- "updateALSEnabled:"
- "v16@?0r^{?=IIQQQQIBBBfffQI}8"
- "v24@0:8i16i20"
- "v28@0:8f16^{?=QfBQfffiB}20"
- "v32@0:8i16i20i24i28"
- "v96@0:8{?=IIQQQQIBBBfffQI}16"
- "writeData:withSize:toRegister:withAddressSize:"
- "{?=\"alsAccumulatedTimeSinceLastPost\"Q\"averageLux\"f\"isFirstReport\"B\"reportStatLastTimestamp\"Q\"lastLuxValue\"f\"minLuxValue\"f\"maxLuxValue\"f\"numberOfUserBrightnessChanges\"i\"alsEnabled\"B}"

```
