## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-696.40.6.0.0
-  __TEXT.__text: 0xc3f78
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1b8f4
-  __TEXT.__const: 0x540
-  __TEXT.__cstring: 0xe56b
-  __TEXT.__oslogstring: 0xc31f
-  __TEXT.__gcc_except_tab: 0x1290
-  __TEXT.__unwind_info: 0x1d50
-  __TEXT.__objc_classname: 0xb97
-  __TEXT.__objc_methname: 0x3e58b
-  __TEXT.__objc_methtype: 0x4108
-  __TEXT.__objc_stubs: 0xcbe0
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x14f8
-  __DATA_CONST.__objc_classlist: 0x308
+696.60.3.0.0
+  __TEXT.__text: 0xd3464
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x1cba4
+  __TEXT.__const: 0x638
+  __TEXT.__cstring: 0xee56
+  __TEXT.__oslogstring: 0xd41b
+  __TEXT.__gcc_except_tab: 0x12cc
+  __TEXT.__unwind_info: 0x1ff8
+  __TEXT.__objc_classname: 0xd3a
+  __TEXT.__objc_methname: 0x3f798
+  __TEXT.__objc_methtype: 0x422d
+  __TEXT.__objc_stubs: 0xd640
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54b8
+  __DATA_CONST.__objc_selrefs: 0x5958
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2e0
-  __DATA_CONST.__objc_arraydata: 0x6fb8
-  __AUTH_CONST.__auth_got: 0x588
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0xc0c0
-  __AUTH_CONST.__objc_const: 0x36ef0
-  __AUTH_CONST.__objc_intobj: 0x978
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
-  __AUTH_CONST.__objc_dictobj: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_arraydata: 0x7188
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__cfstring: 0xd260
+  __AUTH_CONST.__objc_const: 0x39290
+  __AUTH_CONST.__objc_intobj: 0xa38
+  __AUTH_CONST.__objc_arrayobj: 0x4b0
+  __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0xd0
-  __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x3c50
+  __AUTH_CONST.__objc_floatobj: 0x10
+  __AUTH.__objc_data: 0x1b30
+  __DATA.__objc_ivar: 0x3de8
   __DATA.__data: 0x6c8
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E279118A-2D55-3CE9-BF82-7F5F8ED9FB44
-  Functions: 9843
-  Symbols:   27032
-  CStrings:  9003
+  UUID: 47CD1179-3D87-3EA0-B10F-649DFF8AA62F
+  Functions: 10330
+  Symbols:   28402
+  CStrings:  9651
 
Symbols:
+ +[PowerUITTEManager log]
+ +[PowerUITTEManager manager]
+ +[PowerUITTEManager manager].cold.1
+ +[PowerUITTEUtility calculateActualPowerWithDefaults:withStartEnergy:withCurrentEnergy:]
+ +[PowerUITTEUtility fetchPresentRemEnergy]
+ +[PowerUITTEUtility fetchPresentRemEnergy].cold.1
+ +[PowerUITTEUtility fetchPresentRemEnergy].cold.2
+ +[PowerUITTEUtility fetchPresentRemEnergy].cold.3
+ +[PowerUITTEUtility fetchPresentSOC]
+ +[PowerUITTEUtility fetchPresentSOC].cold.1
+ +[PowerUITTEUtility fetchPresentSOC].cold.2
+ +[PowerUITTEUtility fetchPresentSOC].cold.3
+ +[PowerUITTEUtility fetchPresentTemperature]
+ +[PowerUITTEUtility fetchPresentTemperature].cold.1
+ +[PowerUITTEUtility fetchPresentTemperature].cold.2
+ +[PowerUITTEUtility fetchPresentTemperature].cold.3
+ +[PowerUITTEUtility fetchWatchModelType]
+ +[PowerUITTEUtility fetchWatchModelType].cold.1
+ +[PowerUITTEUtility findTimeBuckets:]
+ +[PowerUITTEUtility getTTEDatafromSMC]
+ +[PowerUITTEUtility getTTEDatafromSMC].cold.1
+ +[PowerUITTEUtility getTTEDatafromSMC].cold.2
+ +[PowerUITTEUtility getTTEDatafromSMC].cold.3
+ +[PowerUITTEUtility getTTEDatafromSMC].cold.4
+ +[PowerUITTEUtility readPlistToDictionary:]
+ +[PowerUITTEUtility readPlistToDictionary:].cold.1
+ +[PowerUITTEUtility safeExtractDictionary:forKey:]
+ +[PowerUITTEUtility safeExtractNumber:forKey:]
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:]
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:].cold.1
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:].cold.2
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:].cold.3
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:].cold.4
+ +[PowerUITTEUtility safeFetchNumberFromDefaults:forKey:functionName:].cold.5
+ +[PowerUITTEUtility safeFetchPosFloatFromDefaults:forKey:]
+ +[PowerUITTEUtility safeFetchPosFloatFromDefaults:forKey:].cold.1
+ +[PowerUITTEUtility safeFetchPosIntFromDefaults:forKey:]
+ +[PowerUITTEUtility safeFetchPosIntFromDefaults:forKey:].cold.1
+ +[PowerUITTEUtility searchValueForPlist:withKeyArray:]
+ +[PowerUITTEUtility stringForTriggerReason:]
+ +[PowerUITTEUtility writeDictionaryToPlist:withFilePath:]
+ +[PowerUITTEUtility writeDictionaryToPlist:withFilePath:].cold.1
+ +[PowerUITTEUtility writeDictionaryToPlist:withFilePath:].cold.2
+ +[TTE_Model_SeB URLOfModelInThisBundle]
+ +[TTE_Model_SeB URLOfModelInThisBundle].cold.1
+ +[TTE_Model_SeB loadContentsOfURL:configuration:completionHandler:]
+ +[TTE_Model_SeB loadWithConfiguration:completionHandler:]
+ +[TTE_Model_SeS URLOfModelInThisBundle]
+ +[TTE_Model_SeS URLOfModelInThisBundle].cold.1
+ +[TTE_Model_SeS loadContentsOfURL:configuration:completionHandler:]
+ +[TTE_Model_SeS loadWithConfiguration:completionHandler:]
+ +[TTE_Model_SeriesB URLOfModelInThisBundle]
+ +[TTE_Model_SeriesB URLOfModelInThisBundle].cold.1
+ +[TTE_Model_SeriesB loadContentsOfURL:configuration:completionHandler:]
+ +[TTE_Model_SeriesB loadWithConfiguration:completionHandler:]
+ +[TTE_Model_SeriesS URLOfModelInThisBundle]
+ +[TTE_Model_SeriesS URLOfModelInThisBundle].cold.1
+ +[TTE_Model_SeriesS loadContentsOfURL:configuration:completionHandler:]
+ +[TTE_Model_SeriesS loadWithConfiguration:completionHandler:]
+ +[TTE_Model_Ultra URLOfModelInThisBundle]
+ +[TTE_Model_Ultra URLOfModelInThisBundle].cold.1
+ +[TTE_Model_Ultra loadContentsOfURL:configuration:completionHandler:]
+ +[TTE_Model_Ultra loadWithConfiguration:completionHandler:]
+ -[PowerUINotificationManager postTTEPredictionNotification:]
+ -[PowerUINotificationManager removeAllNotificationsExceptFor:]
+ -[PowerUITTEManager .cxx_destruct]
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected]
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.1
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.2
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.3
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.4
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.5
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.6
+ -[PowerUITTEManager calculateAndUpdatePaverageOnPluginDetected].cold.7
+ -[PowerUITTEManager calculateTTEWithPower:]
+ -[PowerUITTEManager calculateTTEWithPower:].cold.1
+ -[PowerUITTEManager calculateTTEWithPower:].cold.2
+ -[PowerUITTEManager changeStateTo:]
+ -[PowerUITTEManager chargingStatus]
+ -[PowerUITTEManager context]
+ -[PowerUITTEManager correctAveragePower:]
+ -[PowerUITTEManager correctAveragePower:].cold.1
+ -[PowerUITTEManager correctAveragePower:].cold.2
+ -[PowerUITTEManager correctAveragePower:].cold.3
+ -[PowerUITTEManager correctAveragePower:].cold.4
+ -[PowerUITTEManager correctedPower]
+ -[PowerUITTEManager currentState]
+ -[PowerUITTEManager currentStatus]
+ -[PowerUITTEManager defaults]
+ -[PowerUITTEManager formatTTEToRightScale]
+ -[PowerUITTEManager getCorrectedPower]
+ -[PowerUITTEManager handleCallback:]
+ -[PowerUITTEManager handleCallback:].cold.1
+ -[PowerUITTEManager handleCallback:].cold.2
+ -[PowerUITTEManager handleCallback:].cold.3
+ -[PowerUITTEManager handleIsEnabledChangeWithFlag:]
+ -[PowerUITTEManager initWithContextStore:]
+ -[PowerUITTEManager init]
+ -[PowerUITTEManager isEnabled]
+ -[PowerUITTEManager isEngaged]
+ -[PowerUITTEManager lastNotificationTime]
+ -[PowerUITTEManager lastPluggedInDate]
+ -[PowerUITTEManager lastSOCValue]
+ -[PowerUITTEManager lastUnpluggedDate]
+ -[PowerUITTEManager log]
+ -[PowerUITTEManager monitorBatteryStateOfChargeChange]
+ -[PowerUITTEManager monitorUnpluggedChange]
+ -[PowerUITTEManager pauseChargingCheckDate]
+ -[PowerUITTEManager postPredictionNotificationWithReason:]
+ -[PowerUITTEManager postPredictionNotificationWithReason:].cold.1
+ -[PowerUITTEManager postPredictionNotification]
+ -[PowerUITTEManager queue]
+ -[PowerUITTEManager recordDischargeSessionAt:]
+ -[PowerUITTEManager recordDischargeSessionAt:].cold.1
+ -[PowerUITTEManager recordDischargeSessionAt:].cold.2
+ -[PowerUITTEManager remEnergyDischargeEnd]
+ -[PowerUITTEManager resetSessionForTTE]
+ -[PowerUITTEManager resetState]
+ -[PowerUITTEManager setChargingStatus:]
+ -[PowerUITTEManager setContext:]
+ -[PowerUITTEManager setCorrectedPower:]
+ -[PowerUITTEManager setCurrentStatus:]
+ -[PowerUITTEManager setDefaults:]
+ -[PowerUITTEManager setLastNotificationTime:]
+ -[PowerUITTEManager setLastPluggedInDate:]
+ -[PowerUITTEManager setLastSOCValue:]
+ -[PowerUITTEManager setLastUnpluggedDate:]
+ -[PowerUITTEManager setLog:]
+ -[PowerUITTEManager setPauseChargingCheckDate:]
+ -[PowerUITTEManager setQueue:]
+ -[PowerUITTEManager setRemEnergyDischargeEnd:]
+ -[PowerUITTEManager setStateDescriptions:]
+ -[PowerUITTEManager setTTE:]
+ -[PowerUITTEManager setTimer:]
+ -[PowerUITTEManager setTteFormatted:]
+ -[PowerUITTEManager setTteInMinutes:]
+ -[PowerUITTEManager setTteMonitor:]
+ -[PowerUITTEManager setTtePredictions:]
+ -[PowerUITTEManager setTtePredictor:]
+ -[PowerUITTEManager setUnpluggedTimer:]
+ -[PowerUITTEManager stateDescriptions]
+ -[PowerUITTEManager timer]
+ -[PowerUITTEManager tteFormatted]
+ -[PowerUITTEManager tteInMinutes]
+ -[PowerUITTEManager tteMonitor]
+ -[PowerUITTEManager ttePredictions]
+ -[PowerUITTEManager ttePredictor]
+ -[PowerUITTEManager unpluggedTimer]
+ -[PowerUITTEManager updateFeatureEnable]
+ -[PowerUITTEManager updateLearningTableEntry:withTimeBuckets:withPaverage:andHours:]
+ -[PowerUITTEMonitor .cxx_destruct]
+ -[PowerUITTEMonitor _tteMonitorStatus]
+ -[PowerUITTEMonitor caculateInferredTTE]
+ -[PowerUITTEMonitor context]
+ -[PowerUITTEMonitor defaults]
+ -[PowerUITTEMonitor initWithDefaultsDomain:withContextStore:]
+ -[PowerUITTEMonitor log]
+ -[PowerUITTEMonitor postAnalyticsEventAtEnd:]
+ -[PowerUITTEMonitor postAnalyticsEventAtPrediction]
+ -[PowerUITTEMonitor postAnalyticsEventDurCorrection:]
+ -[PowerUITTEMonitor reset]
+ -[PowerUITTEMonitor setContext:]
+ -[PowerUITTEMonitor setDefaults:]
+ -[PowerUITTEMonitor setLog:]
+ -[PowerUITTEMonitor setTteSessionID:]
+ -[PowerUITTEMonitor set_tteMonitorStatus:]
+ -[PowerUITTEMonitor tteSessionID]
+ -[PowerUITTEMonitor updateTTEMonitorSession:]
+ -[PowerUITTEMonitor updateTTEMonitorSession:].cold.1
+ -[PowerUITTEMonitor updateTTEMonitorSession:].cold.2
+ -[PowerUITTEMonitor updateTTEMonitorSession:].cold.3
+ -[PowerUITTEPredParam init]
+ -[PowerUITTEPredParam maxPower]
+ -[PowerUITTEPredParam minPower]
+ -[PowerUITTEPredParam setMaxPower:]
+ -[PowerUITTEPredParam setMinPower:]
+ -[PowerUITTEPredResults averagePower]
+ -[PowerUITTEPredResults confidenceWidth]
+ -[PowerUITTEPredResults init]
+ -[PowerUITTEPredResults isValid]
+ -[PowerUITTEPredResults loadResultsWithDefaults:]
+ -[PowerUITTEPredResults setAveragePower:]
+ -[PowerUITTEPredResults setConfidenceWidth:]
+ -[PowerUITTEPredResults setTtePreResultsStatus:]
+ -[PowerUITTEPredResults ttePreResultsStatus]
+ -[PowerUITTEPredictor .cxx_destruct]
+ -[PowerUITTEPredictor context]
+ -[PowerUITTEPredictor defaults]
+ -[PowerUITTEPredictor exportLearnTable]
+ -[PowerUITTEPredictor fetchLearningTable]
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:]
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.1
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.10
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.11
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.12
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.13
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.14
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.15
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.16
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.17
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.2
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.3
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.4
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.5
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.6
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.7
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.8
+ -[PowerUITTEPredictor getInputFeaturesForTTEPrediction:].cold.9
+ -[PowerUITTEPredictor getModelVersion]
+ -[PowerUITTEPredictor initWithDefaultsDomain:withContextStore:]
+ -[PowerUITTEPredictor inputFeatures]
+ -[PowerUITTEPredictor learnTableLock]
+ -[PowerUITTEPredictor loadTTELearningTable]
+ -[PowerUITTEPredictor loadTTELearningTable].cold.1
+ -[PowerUITTEPredictor loadTTELearningTable].cold.2
+ -[PowerUITTEPredictor loadTTEModelFromBundle:]
+ -[PowerUITTEPredictor loadTTEModelFromBundle:].cold.1
+ -[PowerUITTEPredictor loadTTEModelFromBundle:].cold.2
+ -[PowerUITTEPredictor loadTTEModelFromBundle:].cold.3
+ -[PowerUITTEPredictor log]
+ -[PowerUITTEPredictor modelLock]
+ -[PowerUITTEPredictor modelName]
+ -[PowerUITTEPredictor modelType]
+ -[PowerUITTEPredictor name]
+ -[PowerUITTEPredictor predictTTEAt:withReason:]
+ -[PowerUITTEPredictor predictedFeatureNames]
+ -[PowerUITTEPredictor predictedTTEWithStartTimeStamp:]
+ -[PowerUITTEPredictor predictedTTEWithStartTimeStamp:].cold.1
+ -[PowerUITTEPredictor predictedTTEWithStartTimeStamp:].cold.2
+ -[PowerUITTEPredictor predictedTTEWithStartTimeStamp:].cold.3
+ -[PowerUITTEPredictor processModelInference:]
+ -[PowerUITTEPredictor processModelInference:].cold.1
+ -[PowerUITTEPredictor reset]
+ -[PowerUITTEPredictor runModelInferenceforTTEPrediction]
+ -[PowerUITTEPredictor runModelInferenceforTTEPrediction].cold.1
+ -[PowerUITTEPredictor setContext:]
+ -[PowerUITTEPredictor setDefaults:]
+ -[PowerUITTEPredictor setInputFeatures:]
+ -[PowerUITTEPredictor setLearnTableLock:]
+ -[PowerUITTEPredictor setLog:]
+ -[PowerUITTEPredictor setModelLock:]
+ -[PowerUITTEPredictor setModelName:]
+ -[PowerUITTEPredictor setModelType:]
+ -[PowerUITTEPredictor setName:]
+ -[PowerUITTEPredictor setPredictedFeatureNames:]
+ -[PowerUITTEPredictor setTteLearningTable:]
+ -[PowerUITTEPredictor setTtePredictionModel:]
+ -[PowerUITTEPredictor setTtePredictionModelStatus:]
+ -[PowerUITTEPredictor setTtePredictionParameters:]
+ -[PowerUITTEPredictor setVersion:]
+ -[PowerUITTEPredictor tteLearningTable]
+ -[PowerUITTEPredictor ttePredictionModelStatus]
+ -[PowerUITTEPredictor ttePredictionModel]
+ -[PowerUITTEPredictor ttePredictionParameters]
+ -[PowerUITTEPredictor updateLearningTable:]
+ -[PowerUITTEPredictor updateLearningTable:].cold.1
+ -[PowerUITTEPredictor updateLearningTable:].cold.2
+ -[PowerUITTEPredictor updateLearningTable:].cold.3
+ -[PowerUITTEPredictor updateLearningTable:].cold.4
+ -[PowerUITTEPredictor updateLearningTable:].cold.5
+ -[PowerUITTEPredictor validationLastPredSessionWithValidFlag:withActiveFlag:]
+ -[PowerUITTEPredictor validationLastPredSessionWithValidFlag:withActiveFlag:].cold.1
+ -[PowerUITTEPredictor version]
+ -[TTE_Model_SeB .cxx_destruct]
+ -[TTE_Model_SeB initWithConfiguration:error:]
+ -[TTE_Model_SeB initWithContentsOfURL:configuration:error:]
+ -[TTE_Model_SeB initWithContentsOfURL:error:]
+ -[TTE_Model_SeB initWithMLModel:]
+ -[TTE_Model_SeB init]
+ -[TTE_Model_SeB model]
+ -[TTE_Model_SeB predictionFromFeatures:completionHandler:]
+ -[TTE_Model_SeB predictionFromFeatures:error:]
+ -[TTE_Model_SeB predictionFromFeatures:options:completionHandler:]
+ -[TTE_Model_SeB predictionFromFeatures:options:error:]
+ -[TTE_Model_SeB predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:]
+ -[TTE_Model_SeB predictionsFromInputs:options:error:]
+ -[TTE_Model_SeBInput featureNames]
+ -[TTE_Model_SeBInput featureValueForName:]
+ -[TTE_Model_SeBInput initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:]
+ -[TTE_Model_SeBInput setX1:]
+ -[TTE_Model_SeBInput setX2:]
+ -[TTE_Model_SeBInput setX3:]
+ -[TTE_Model_SeBInput setX4:]
+ -[TTE_Model_SeBInput setX5:]
+ -[TTE_Model_SeBInput setX6:]
+ -[TTE_Model_SeBInput setX7:]
+ -[TTE_Model_SeBInput setX8:]
+ -[TTE_Model_SeBInput setX9:]
+ -[TTE_Model_SeBInput x1]
+ -[TTE_Model_SeBInput x2]
+ -[TTE_Model_SeBInput x3]
+ -[TTE_Model_SeBInput x4]
+ -[TTE_Model_SeBInput x5]
+ -[TTE_Model_SeBInput x6]
+ -[TTE_Model_SeBInput x7]
+ -[TTE_Model_SeBInput x8]
+ -[TTE_Model_SeBInput x9]
+ -[TTE_Model_SeBOutput featureNames]
+ -[TTE_Model_SeBOutput featureValueForName:]
+ -[TTE_Model_SeBOutput initWithPrediction:]
+ -[TTE_Model_SeBOutput prediction]
+ -[TTE_Model_SeBOutput setPrediction:]
+ -[TTE_Model_SeS .cxx_destruct]
+ -[TTE_Model_SeS initWithConfiguration:error:]
+ -[TTE_Model_SeS initWithContentsOfURL:configuration:error:]
+ -[TTE_Model_SeS initWithContentsOfURL:error:]
+ -[TTE_Model_SeS initWithMLModel:]
+ -[TTE_Model_SeS init]
+ -[TTE_Model_SeS model]
+ -[TTE_Model_SeS predictionFromFeatures:completionHandler:]
+ -[TTE_Model_SeS predictionFromFeatures:error:]
+ -[TTE_Model_SeS predictionFromFeatures:options:completionHandler:]
+ -[TTE_Model_SeS predictionFromFeatures:options:error:]
+ -[TTE_Model_SeS predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:]
+ -[TTE_Model_SeS predictionsFromInputs:options:error:]
+ -[TTE_Model_SeSInput featureNames]
+ -[TTE_Model_SeSInput featureValueForName:]
+ -[TTE_Model_SeSInput initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:]
+ -[TTE_Model_SeSInput setX1:]
+ -[TTE_Model_SeSInput setX2:]
+ -[TTE_Model_SeSInput setX3:]
+ -[TTE_Model_SeSInput setX4:]
+ -[TTE_Model_SeSInput setX5:]
+ -[TTE_Model_SeSInput setX6:]
+ -[TTE_Model_SeSInput setX7:]
+ -[TTE_Model_SeSInput setX8:]
+ -[TTE_Model_SeSInput setX9:]
+ -[TTE_Model_SeSInput x1]
+ -[TTE_Model_SeSInput x2]
+ -[TTE_Model_SeSInput x3]
+ -[TTE_Model_SeSInput x4]
+ -[TTE_Model_SeSInput x5]
+ -[TTE_Model_SeSInput x6]
+ -[TTE_Model_SeSInput x7]
+ -[TTE_Model_SeSInput x8]
+ -[TTE_Model_SeSInput x9]
+ -[TTE_Model_SeSOutput featureNames]
+ -[TTE_Model_SeSOutput featureValueForName:]
+ -[TTE_Model_SeSOutput initWithPrediction:]
+ -[TTE_Model_SeSOutput prediction]
+ -[TTE_Model_SeSOutput setPrediction:]
+ -[TTE_Model_SeriesB .cxx_destruct]
+ -[TTE_Model_SeriesB initWithConfiguration:error:]
+ -[TTE_Model_SeriesB initWithContentsOfURL:configuration:error:]
+ -[TTE_Model_SeriesB initWithContentsOfURL:error:]
+ -[TTE_Model_SeriesB initWithMLModel:]
+ -[TTE_Model_SeriesB init]
+ -[TTE_Model_SeriesB model]
+ -[TTE_Model_SeriesB predictionFromFeatures:completionHandler:]
+ -[TTE_Model_SeriesB predictionFromFeatures:error:]
+ -[TTE_Model_SeriesB predictionFromFeatures:options:completionHandler:]
+ -[TTE_Model_SeriesB predictionFromFeatures:options:error:]
+ -[TTE_Model_SeriesB predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:]
+ -[TTE_Model_SeriesB predictionsFromInputs:options:error:]
+ -[TTE_Model_SeriesBInput featureNames]
+ -[TTE_Model_SeriesBInput featureValueForName:]
+ -[TTE_Model_SeriesBInput initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:]
+ -[TTE_Model_SeriesBInput setX1:]
+ -[TTE_Model_SeriesBInput setX2:]
+ -[TTE_Model_SeriesBInput setX3:]
+ -[TTE_Model_SeriesBInput setX4:]
+ -[TTE_Model_SeriesBInput setX5:]
+ -[TTE_Model_SeriesBInput setX6:]
+ -[TTE_Model_SeriesBInput setX7:]
+ -[TTE_Model_SeriesBInput setX8:]
+ -[TTE_Model_SeriesBInput setX9:]
+ -[TTE_Model_SeriesBInput x1]
+ -[TTE_Model_SeriesBInput x2]
+ -[TTE_Model_SeriesBInput x3]
+ -[TTE_Model_SeriesBInput x4]
+ -[TTE_Model_SeriesBInput x5]
+ -[TTE_Model_SeriesBInput x6]
+ -[TTE_Model_SeriesBInput x7]
+ -[TTE_Model_SeriesBInput x8]
+ -[TTE_Model_SeriesBInput x9]
+ -[TTE_Model_SeriesBOutput featureNames]
+ -[TTE_Model_SeriesBOutput featureValueForName:]
+ -[TTE_Model_SeriesBOutput initWithPrediction:]
+ -[TTE_Model_SeriesBOutput prediction]
+ -[TTE_Model_SeriesBOutput setPrediction:]
+ -[TTE_Model_SeriesS .cxx_destruct]
+ -[TTE_Model_SeriesS initWithConfiguration:error:]
+ -[TTE_Model_SeriesS initWithContentsOfURL:configuration:error:]
+ -[TTE_Model_SeriesS initWithContentsOfURL:error:]
+ -[TTE_Model_SeriesS initWithMLModel:]
+ -[TTE_Model_SeriesS init]
+ -[TTE_Model_SeriesS model]
+ -[TTE_Model_SeriesS predictionFromFeatures:completionHandler:]
+ -[TTE_Model_SeriesS predictionFromFeatures:error:]
+ -[TTE_Model_SeriesS predictionFromFeatures:options:completionHandler:]
+ -[TTE_Model_SeriesS predictionFromFeatures:options:error:]
+ -[TTE_Model_SeriesS predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:]
+ -[TTE_Model_SeriesS predictionsFromInputs:options:error:]
+ -[TTE_Model_SeriesSInput featureNames]
+ -[TTE_Model_SeriesSInput featureValueForName:]
+ -[TTE_Model_SeriesSInput initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:]
+ -[TTE_Model_SeriesSInput setX1:]
+ -[TTE_Model_SeriesSInput setX2:]
+ -[TTE_Model_SeriesSInput setX3:]
+ -[TTE_Model_SeriesSInput setX4:]
+ -[TTE_Model_SeriesSInput setX5:]
+ -[TTE_Model_SeriesSInput setX6:]
+ -[TTE_Model_SeriesSInput setX7:]
+ -[TTE_Model_SeriesSInput setX8:]
+ -[TTE_Model_SeriesSInput setX9:]
+ -[TTE_Model_SeriesSInput x1]
+ -[TTE_Model_SeriesSInput x2]
+ -[TTE_Model_SeriesSInput x3]
+ -[TTE_Model_SeriesSInput x4]
+ -[TTE_Model_SeriesSInput x5]
+ -[TTE_Model_SeriesSInput x6]
+ -[TTE_Model_SeriesSInput x7]
+ -[TTE_Model_SeriesSInput x8]
+ -[TTE_Model_SeriesSInput x9]
+ -[TTE_Model_SeriesSOutput featureNames]
+ -[TTE_Model_SeriesSOutput featureValueForName:]
+ -[TTE_Model_SeriesSOutput initWithPrediction:]
+ -[TTE_Model_SeriesSOutput prediction]
+ -[TTE_Model_SeriesSOutput setPrediction:]
+ -[TTE_Model_Ultra .cxx_destruct]
+ -[TTE_Model_Ultra initWithConfiguration:error:]
+ -[TTE_Model_Ultra initWithContentsOfURL:configuration:error:]
+ -[TTE_Model_Ultra initWithContentsOfURL:error:]
+ -[TTE_Model_Ultra initWithMLModel:]
+ -[TTE_Model_Ultra init]
+ -[TTE_Model_Ultra model]
+ -[TTE_Model_Ultra predictionFromFeatures:completionHandler:]
+ -[TTE_Model_Ultra predictionFromFeatures:error:]
+ -[TTE_Model_Ultra predictionFromFeatures:options:completionHandler:]
+ -[TTE_Model_Ultra predictionFromFeatures:options:error:]
+ -[TTE_Model_Ultra predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:]
+ -[TTE_Model_Ultra predictionsFromInputs:options:error:]
+ -[TTE_Model_UltraInput featureNames]
+ -[TTE_Model_UltraInput featureValueForName:]
+ -[TTE_Model_UltraInput initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:]
+ -[TTE_Model_UltraInput setX1:]
+ -[TTE_Model_UltraInput setX2:]
+ -[TTE_Model_UltraInput setX3:]
+ -[TTE_Model_UltraInput setX4:]
+ -[TTE_Model_UltraInput setX5:]
+ -[TTE_Model_UltraInput setX6:]
+ -[TTE_Model_UltraInput setX7:]
+ -[TTE_Model_UltraInput setX8:]
+ -[TTE_Model_UltraInput setX9:]
+ -[TTE_Model_UltraInput x1]
+ -[TTE_Model_UltraInput x2]
+ -[TTE_Model_UltraInput x3]
+ -[TTE_Model_UltraInput x4]
+ -[TTE_Model_UltraInput x5]
+ -[TTE_Model_UltraInput x6]
+ -[TTE_Model_UltraInput x7]
+ -[TTE_Model_UltraInput x8]
+ -[TTE_Model_UltraInput x9]
+ -[TTE_Model_UltraOutput featureNames]
+ -[TTE_Model_UltraOutput featureValueForName:]
+ -[TTE_Model_UltraOutput initWithPrediction:]
+ -[TTE_Model_UltraOutput prediction]
+ -[TTE_Model_UltraOutput setPrediction:]
+ _CONVERT_TO_32BIT
+ _FIXED_TO_FLOAT_SIGNED
+ _MLModelVersionStringKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_PowerUITTEManager
+ _OBJC_CLASS_$_PowerUITTEMonitor
+ _OBJC_CLASS_$_PowerUITTEPredParam
+ _OBJC_CLASS_$_PowerUITTEPredResults
+ _OBJC_CLASS_$_PowerUITTEPredictor
+ _OBJC_CLASS_$_PowerUITTEUtility
+ _OBJC_CLASS_$_TTE_Model_SeB
+ _OBJC_CLASS_$_TTE_Model_SeBInput
+ _OBJC_CLASS_$_TTE_Model_SeBOutput
+ _OBJC_CLASS_$_TTE_Model_SeS
+ _OBJC_CLASS_$_TTE_Model_SeSInput
+ _OBJC_CLASS_$_TTE_Model_SeSOutput
+ _OBJC_CLASS_$_TTE_Model_SeriesB
+ _OBJC_CLASS_$_TTE_Model_SeriesBInput
+ _OBJC_CLASS_$_TTE_Model_SeriesBOutput
+ _OBJC_CLASS_$_TTE_Model_SeriesS
+ _OBJC_CLASS_$_TTE_Model_SeriesSInput
+ _OBJC_CLASS_$_TTE_Model_SeriesSOutput
+ _OBJC_CLASS_$_TTE_Model_Ultra
+ _OBJC_CLASS_$_TTE_Model_UltraInput
+ _OBJC_CLASS_$_TTE_Model_UltraOutput
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_PowerUITTEManager._chargingStatus
+ _OBJC_IVAR_$_PowerUITTEManager._context
+ _OBJC_IVAR_$_PowerUITTEManager._correctedPower
+ _OBJC_IVAR_$_PowerUITTEManager._currentState
+ _OBJC_IVAR_$_PowerUITTEManager._currentStatus
+ _OBJC_IVAR_$_PowerUITTEManager._defaults
+ _OBJC_IVAR_$_PowerUITTEManager._lastNotificationTime
+ _OBJC_IVAR_$_PowerUITTEManager._lastPluggedInDate
+ _OBJC_IVAR_$_PowerUITTEManager._lastSOCValue
+ _OBJC_IVAR_$_PowerUITTEManager._lastUnpluggedDate
+ _OBJC_IVAR_$_PowerUITTEManager._log
+ _OBJC_IVAR_$_PowerUITTEManager._pauseChargingCheckDate
+ _OBJC_IVAR_$_PowerUITTEManager._queue
+ _OBJC_IVAR_$_PowerUITTEManager._remEnergyDischargeEnd
+ _OBJC_IVAR_$_PowerUITTEManager._stateDescriptions
+ _OBJC_IVAR_$_PowerUITTEManager._timer
+ _OBJC_IVAR_$_PowerUITTEManager._tteFormatted
+ _OBJC_IVAR_$_PowerUITTEManager._tteInMinutes
+ _OBJC_IVAR_$_PowerUITTEManager._tteMonitor
+ _OBJC_IVAR_$_PowerUITTEManager._ttePredictions
+ _OBJC_IVAR_$_PowerUITTEManager._ttePredictor
+ _OBJC_IVAR_$_PowerUITTEManager._unpluggedTimer
+ _OBJC_IVAR_$_PowerUITTEMonitor.__tteMonitorStatus
+ _OBJC_IVAR_$_PowerUITTEMonitor._context
+ _OBJC_IVAR_$_PowerUITTEMonitor._defaults
+ _OBJC_IVAR_$_PowerUITTEMonitor._log
+ _OBJC_IVAR_$_PowerUITTEMonitor._tteSessionID
+ _OBJC_IVAR_$_PowerUITTEPredParam._maxPower
+ _OBJC_IVAR_$_PowerUITTEPredParam._minPower
+ _OBJC_IVAR_$_PowerUITTEPredResults._averagePower
+ _OBJC_IVAR_$_PowerUITTEPredResults._confidenceWidth
+ _OBJC_IVAR_$_PowerUITTEPredResults._ttePreResultsStatus
+ _OBJC_IVAR_$_PowerUITTEPredictor._context
+ _OBJC_IVAR_$_PowerUITTEPredictor._defaults
+ _OBJC_IVAR_$_PowerUITTEPredictor._inputFeatures
+ _OBJC_IVAR_$_PowerUITTEPredictor._learnTableLock
+ _OBJC_IVAR_$_PowerUITTEPredictor._log
+ _OBJC_IVAR_$_PowerUITTEPredictor._modelLock
+ _OBJC_IVAR_$_PowerUITTEPredictor._modelName
+ _OBJC_IVAR_$_PowerUITTEPredictor._modelType
+ _OBJC_IVAR_$_PowerUITTEPredictor._name
+ _OBJC_IVAR_$_PowerUITTEPredictor._predictedFeatureNames
+ _OBJC_IVAR_$_PowerUITTEPredictor._tteLearningTable
+ _OBJC_IVAR_$_PowerUITTEPredictor._ttePredictionModel
+ _OBJC_IVAR_$_PowerUITTEPredictor._ttePredictionModelStatus
+ _OBJC_IVAR_$_PowerUITTEPredictor._ttePredictionParameters
+ _OBJC_IVAR_$_PowerUITTEPredictor._version
+ _OBJC_IVAR_$_TTE_Model_SeB._model
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x1
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x2
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x3
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x4
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x5
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x6
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x7
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x8
+ _OBJC_IVAR_$_TTE_Model_SeBInput._x9
+ _OBJC_IVAR_$_TTE_Model_SeBOutput._prediction
+ _OBJC_IVAR_$_TTE_Model_SeS._model
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x1
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x2
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x3
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x4
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x5
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x6
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x7
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x8
+ _OBJC_IVAR_$_TTE_Model_SeSInput._x9
+ _OBJC_IVAR_$_TTE_Model_SeSOutput._prediction
+ _OBJC_IVAR_$_TTE_Model_SeriesB._model
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x1
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x2
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x3
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x4
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x5
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x6
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x7
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x8
+ _OBJC_IVAR_$_TTE_Model_SeriesBInput._x9
+ _OBJC_IVAR_$_TTE_Model_SeriesBOutput._prediction
+ _OBJC_IVAR_$_TTE_Model_SeriesS._model
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x1
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x2
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x3
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x4
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x5
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x6
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x7
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x8
+ _OBJC_IVAR_$_TTE_Model_SeriesSInput._x9
+ _OBJC_IVAR_$_TTE_Model_SeriesSOutput._prediction
+ _OBJC_IVAR_$_TTE_Model_Ultra._model
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x1
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x2
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x3
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x4
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x5
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x6
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x7
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x8
+ _OBJC_IVAR_$_TTE_Model_UltraInput._x9
+ _OBJC_IVAR_$_TTE_Model_UltraOutput._prediction
+ _OBJC_METACLASS_$_PowerUITTEManager
+ _OBJC_METACLASS_$_PowerUITTEMonitor
+ _OBJC_METACLASS_$_PowerUITTEPredParam
+ _OBJC_METACLASS_$_PowerUITTEPredResults
+ _OBJC_METACLASS_$_PowerUITTEPredictor
+ _OBJC_METACLASS_$_PowerUITTEUtility
+ _OBJC_METACLASS_$_TTE_Model_SeB
+ _OBJC_METACLASS_$_TTE_Model_SeBInput
+ _OBJC_METACLASS_$_TTE_Model_SeBOutput
+ _OBJC_METACLASS_$_TTE_Model_SeS
+ _OBJC_METACLASS_$_TTE_Model_SeSInput
+ _OBJC_METACLASS_$_TTE_Model_SeSOutput
+ _OBJC_METACLASS_$_TTE_Model_SeriesB
+ _OBJC_METACLASS_$_TTE_Model_SeriesBInput
+ _OBJC_METACLASS_$_TTE_Model_SeriesBOutput
+ _OBJC_METACLASS_$_TTE_Model_SeriesS
+ _OBJC_METACLASS_$_TTE_Model_SeriesSInput
+ _OBJC_METACLASS_$_TTE_Model_SeriesSOutput
+ _OBJC_METACLASS_$_TTE_Model_Ultra
+ _OBJC_METACLASS_$_TTE_Model_UltraInput
+ _OBJC_METACLASS_$_TTE_Model_UltraOutput
+ __OBJC_$_CLASS_METHODS_PowerUITTEManager
+ __OBJC_$_CLASS_METHODS_PowerUITTEUtility
+ __OBJC_$_CLASS_METHODS_TTE_Model_SeB
+ __OBJC_$_CLASS_METHODS_TTE_Model_SeS
+ __OBJC_$_CLASS_METHODS_TTE_Model_SeriesB
+ __OBJC_$_CLASS_METHODS_TTE_Model_SeriesS
+ __OBJC_$_CLASS_METHODS_TTE_Model_Ultra
+ __OBJC_$_INSTANCE_METHODS_PowerUITTEManager
+ __OBJC_$_INSTANCE_METHODS_PowerUITTEMonitor
+ __OBJC_$_INSTANCE_METHODS_PowerUITTEPredParam
+ __OBJC_$_INSTANCE_METHODS_PowerUITTEPredResults
+ __OBJC_$_INSTANCE_METHODS_PowerUITTEPredictor
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeB
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeBInput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeBOutput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeS
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeSInput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeSOutput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesB
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesBInput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesBOutput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesS
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesSInput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_SeriesSOutput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_Ultra
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_UltraInput
+ __OBJC_$_INSTANCE_METHODS_TTE_Model_UltraOutput
+ __OBJC_$_INSTANCE_VARIABLES_PowerUITTEManager
+ __OBJC_$_INSTANCE_VARIABLES_PowerUITTEMonitor
+ __OBJC_$_INSTANCE_VARIABLES_PowerUITTEPredParam
+ __OBJC_$_INSTANCE_VARIABLES_PowerUITTEPredResults
+ __OBJC_$_INSTANCE_VARIABLES_PowerUITTEPredictor
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeB
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeBInput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeBOutput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeS
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeSInput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeSOutput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesB
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesBInput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesBOutput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesS
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesSInput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_SeriesSOutput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_Ultra
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_UltraInput
+ __OBJC_$_INSTANCE_VARIABLES_TTE_Model_UltraOutput
+ __OBJC_$_PROP_LIST_PowerUITTEManager
+ __OBJC_$_PROP_LIST_PowerUITTEMonitor
+ __OBJC_$_PROP_LIST_PowerUITTEPredParam
+ __OBJC_$_PROP_LIST_PowerUITTEPredResults
+ __OBJC_$_PROP_LIST_PowerUITTEPredictor
+ __OBJC_$_PROP_LIST_TTE_Model_SeB
+ __OBJC_$_PROP_LIST_TTE_Model_SeBInput
+ __OBJC_$_PROP_LIST_TTE_Model_SeBOutput
+ __OBJC_$_PROP_LIST_TTE_Model_SeS
+ __OBJC_$_PROP_LIST_TTE_Model_SeSInput
+ __OBJC_$_PROP_LIST_TTE_Model_SeSOutput
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesB
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesBInput
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesBOutput
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesS
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesSInput
+ __OBJC_$_PROP_LIST_TTE_Model_SeriesSOutput
+ __OBJC_$_PROP_LIST_TTE_Model_Ultra
+ __OBJC_$_PROP_LIST_TTE_Model_UltraInput
+ __OBJC_$_PROP_LIST_TTE_Model_UltraOutput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeBInput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeBOutput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeSInput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeSOutput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeriesBInput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeriesBOutput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeriesSInput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_SeriesSOutput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_UltraInput
+ __OBJC_CLASS_PROTOCOLS_$_TTE_Model_UltraOutput
+ __OBJC_CLASS_RO_$_PowerUITTEManager
+ __OBJC_CLASS_RO_$_PowerUITTEMonitor
+ __OBJC_CLASS_RO_$_PowerUITTEPredParam
+ __OBJC_CLASS_RO_$_PowerUITTEPredResults
+ __OBJC_CLASS_RO_$_PowerUITTEPredictor
+ __OBJC_CLASS_RO_$_PowerUITTEUtility
+ __OBJC_CLASS_RO_$_TTE_Model_SeB
+ __OBJC_CLASS_RO_$_TTE_Model_SeBInput
+ __OBJC_CLASS_RO_$_TTE_Model_SeBOutput
+ __OBJC_CLASS_RO_$_TTE_Model_SeS
+ __OBJC_CLASS_RO_$_TTE_Model_SeSInput
+ __OBJC_CLASS_RO_$_TTE_Model_SeSOutput
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesB
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesBInput
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesBOutput
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesS
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesSInput
+ __OBJC_CLASS_RO_$_TTE_Model_SeriesSOutput
+ __OBJC_CLASS_RO_$_TTE_Model_Ultra
+ __OBJC_CLASS_RO_$_TTE_Model_UltraInput
+ __OBJC_CLASS_RO_$_TTE_Model_UltraOutput
+ __OBJC_METACLASS_RO_$_PowerUITTEManager
+ __OBJC_METACLASS_RO_$_PowerUITTEMonitor
+ __OBJC_METACLASS_RO_$_PowerUITTEPredParam
+ __OBJC_METACLASS_RO_$_PowerUITTEPredResults
+ __OBJC_METACLASS_RO_$_PowerUITTEPredictor
+ __OBJC_METACLASS_RO_$_PowerUITTEUtility
+ __OBJC_METACLASS_RO_$_TTE_Model_SeB
+ __OBJC_METACLASS_RO_$_TTE_Model_SeBInput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeBOutput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeS
+ __OBJC_METACLASS_RO_$_TTE_Model_SeSInput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeSOutput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesB
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesBInput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesBOutput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesS
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesSInput
+ __OBJC_METACLASS_RO_$_TTE_Model_SeriesSOutput
+ __OBJC_METACLASS_RO_$_TTE_Model_Ultra
+ __OBJC_METACLASS_RO_$_TTE_Model_UltraInput
+ __OBJC_METACLASS_RO_$_TTE_Model_UltraOutput
+ ___28+[PowerUITTEManager manager]_block_invoke
+ ___42-[PowerUITTEManager initWithContextStore:]_block_invoke
+ ___42-[PowerUITTEManager initWithContextStore:]_block_invoke.63
+ ___43-[PowerUITTEManager monitorUnpluggedChange]_block_invoke
+ ___43-[PowerUITTEManager monitorUnpluggedChange]_block_invoke_2
+ ___45-[PowerUITTEMonitor postAnalyticsEventAtEnd:]_block_invoke
+ ___51-[PowerUITTEMonitor postAnalyticsEventAtPrediction]_block_invoke
+ ___53-[PowerUITTEMonitor postAnalyticsEventDurCorrection:]_block_invoke
+ ___54-[PowerUITTEManager monitorBatteryStateOfChargeChange]_block_invoke
+ ___54-[PowerUITTEManager monitorBatteryStateOfChargeChange]_block_invoke_2
+ ___58-[TTE_Model_SeB predictionFromFeatures:completionHandler:]_block_invoke
+ ___58-[TTE_Model_SeS predictionFromFeatures:completionHandler:]_block_invoke
+ ___60-[TTE_Model_Ultra predictionFromFeatures:completionHandler:]_block_invoke
+ ___62-[PowerUINotificationManager removeAllNotificationsExceptFor:]_block_invoke
+ ___62-[TTE_Model_SeriesB predictionFromFeatures:completionHandler:]_block_invoke
+ ___62-[TTE_Model_SeriesS predictionFromFeatures:completionHandler:]_block_invoke
+ ___66-[TTE_Model_SeB predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___66-[TTE_Model_SeS predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___67+[TTE_Model_SeB loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___67+[TTE_Model_SeS loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___68-[TTE_Model_Ultra predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___69+[TTE_Model_Ultra loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___70-[TTE_Model_SeriesB predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___70-[TTE_Model_SeriesS predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___71+[TTE_Model_SeriesB loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___71+[TTE_Model_SeriesS loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___84-[PowerUITTEManager updateLearningTableEntry:withTimeBuckets:withPaverage:andHours:]_block_invoke
+ ___block_descriptor_40_e42_v24?0"NSMutableDictionary"8"NSString"16l
+ ___block_descriptor_44_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$averagePower
+ _objc_msgSend$bytes
+ _objc_msgSend$caculateInferredTTE
+ _objc_msgSend$calculateActualPowerWithDefaults:withStartEnergy:withCurrentEnergy:
+ _objc_msgSend$calculateAndUpdatePaverageOnPluginDetected
+ _objc_msgSend$calculateTTEWithPower:
+ _objc_msgSend$changeStateTo:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$confidenceWidth
+ _objc_msgSend$correctAveragePower:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$fetchLearningTable
+ _objc_msgSend$fetchPresentRemEnergy
+ _objc_msgSend$fetchPresentSOC
+ _objc_msgSend$fetchPresentTemperature
+ _objc_msgSend$fetchWatchModelType
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$findTimeBuckets:
+ _objc_msgSend$formatTTEToRightScale
+ _objc_msgSend$getCorrectedPower
+ _objc_msgSend$getInputFeaturesForTTEPrediction:
+ _objc_msgSend$getTTEDatafromSMC
+ _objc_msgSend$handleIsEnabledChangeWithFlag:
+ _objc_msgSend$initWithDefaultsDomain:withContextStore:
+ _objc_msgSend$initWithPrediction:
+ _objc_msgSend$initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:
+ _objc_msgSend$inputFeatures
+ _objc_msgSend$isValid
+ _objc_msgSend$loadResultsWithDefaults:
+ _objc_msgSend$loadTTELearningTable
+ _objc_msgSend$loadTTEModelFromBundle:
+ _objc_msgSend$maxPower
+ _objc_msgSend$minPower
+ _objc_msgSend$monitorUnpluggedChange
+ _objc_msgSend$month
+ _objc_msgSend$postAnalyticsEventAtEnd:
+ _objc_msgSend$postAnalyticsEventAtPrediction
+ _objc_msgSend$postAnalyticsEventDurCorrection:
+ _objc_msgSend$postPredictionNotificationWithReason:
+ _objc_msgSend$postTTEPredictionNotification:
+ _objc_msgSend$predictTTEAt:withReason:
+ _objc_msgSend$predictedTTEWithStartTimeStamp:
+ _objc_msgSend$prediction
+ _objc_msgSend$processModelInference:
+ _objc_msgSend$readPlistToDictionary:
+ _objc_msgSend$recordDischargeSessionAt:
+ _objc_msgSend$reset
+ _objc_msgSend$runModelInferenceforTTEPrediction
+ _objc_msgSend$safeExtractDictionary:forKey:
+ _objc_msgSend$safeExtractNumber:forKey:
+ _objc_msgSend$safeFetchNumberFromDefaults:forKey:functionName:
+ _objc_msgSend$safeFetchPosFloatFromDefaults:forKey:
+ _objc_msgSend$safeFetchPosIntFromDefaults:forKey:
+ _objc_msgSend$searchValueForPlist:withKeyArray:
+ _objc_msgSend$setAveragePower:
+ _objc_msgSend$setConfidenceWidth:
+ _objc_msgSend$setInputFeatures:
+ _objc_msgSend$setTTE:
+ _objc_msgSend$setTtePreResultsStatus:
+ _objc_msgSend$setTtePredictionModelStatus:
+ _objc_msgSend$string
+ _objc_msgSend$stringForTriggerReason:
+ _objc_msgSend$ttePreResultsStatus
+ _objc_msgSend$ttePredictionModel
+ _objc_msgSend$ttePredictionParameters
+ _objc_msgSend$updateFeatureEnable
+ _objc_msgSend$updateLearningTable:
+ _objc_msgSend$updateLearningTableEntry:withTimeBuckets:withPaverage:andHours:
+ _objc_msgSend$updateTTEMonitorSession:
+ _objc_msgSend$validationLastPredSessionWithValidFlag:withActiveFlag:
+ _objc_msgSend$writeDictionaryToPlist:withFilePath:
+ _objc_msgSend$writeToURL:options:error:
+ _objc_msgSend$x1
+ _objc_msgSend$x2
+ _objc_msgSend$x3
+ _objc_msgSend$x4
+ _objc_msgSend$x5
+ _objc_msgSend$x6
+ _objc_msgSend$x7
+ _objc_msgSend$x8
+ _objc_msgSend$x9
CStrings:
+ " "
+ " Days"
+ " Hours"
+ " Minutes"
+ " reason:"
+ " use fall back prediction"
+ "%.2f"
+ "%02x "
+ "%@ is either null or not met"
+ "%@: Exception accessing defaults for key %@: %@"
+ "%@: No value found for key %@"
+ "%@: Value for key %@ is not a number (type: %@)"
+ "%@: defaults is nil for key %@"
+ "%@: key is nil or empty"
+ "(nil key)"
+ ", "
+ ";"
+ "@\"<MLFeatureProvider>\""
+ "@\"PowerUITTEMonitor\""
+ "@\"PowerUITTEPredParam\""
+ "@\"PowerUITTEPredResults\""
+ "@\"PowerUITTEPredictor\""
+ "@88@0:8d16d24d32d40d48d56d64d72d80"
+ "@96@0:8d16d24d32d40d48d56d64d72d80^@88"
+ "AlgoTemperature"
+ "Asset path for %@ not found"
+ "Battery SOC changed"
+ "Calculated Paverage: %.2f (energy consumed: %.2f over %.2f minutes)"
+ "Clearing TTE monitor table from NSUserDefaults"
+ "Configured TTE predictor for model type %d using model: %@"
+ "Corrected power is invalid: %f, using predicted power"
+ "Could not find plist path for writing (normal in test environment)"
+ "Could not load TTE_Model_SeB.mlmodelc in the bundle resource"
+ "Could not load TTE_Model_SeS.mlmodelc in the bundle resource"
+ "Could not load TTE_Model_SeriesB.mlmodelc in the bundle resource"
+ "Could not load TTE_Model_SeriesS.mlmodelc in the bundle resource"
+ "Could not load TTE_Model_Ultra.mlmodelc in the bundle resource"
+ "D0"
+ "D1"
+ "D2"
+ "D3"
+ "D4"
+ "D5"
+ "D6"
+ "Enter statemachine. Trigger: %@ (currentState: [%@] batteryLevel: %ld, isPluggedIn: %d)"
+ "Error while run predictionFromFeatures: %@"
+ "Estimated: %@"
+ "Failed to create IOPMPowerSource service"
+ "Failed to extract AlgoTemperature from SMC data"
+ "Failed to extract StateOfCharge from SMC data"
+ "Failed to extract remainingEnergy from SMC data"
+ "Failed to find the tteLearningTable"
+ "Failed to load valid TTE learning table from plist"
+ "Failed to read %@ with error %@"
+ "Failed to retrieve SMC data for AlgoTemperature"
+ "Failed to retrieve SMC data for StateOfCharge"
+ "Failed to retrieve SMC data for remaining energy"
+ "Failed to serialize dictionary to plist data with error %@"
+ "Failed to write to file %@ with error %@"
+ "Failed to write updated TTE learning table to plist (may be read-only in test environment)"
+ "H0"
+ "H1"
+ "H2"
+ "H3"
+ "Harry"
+ "ISS"
+ "Initializing TTE predictor and monitor"
+ "Input features: x1=%.3f, x2=%.3f, x3=%.3f, x4=%.3f, x5=%.3f, x6=%.3f, x7=%.3f, x8=%.3f, x9=%.3f"
+ "Invalid learning table structure - missing or invalid %@"
+ "Invalid learning table type - not a dictionary"
+ "Invalid power prediction: %f, using fallback"
+ "Invalid predicted power and actual power,use default fallback"
+ "Invalid predicted power but valid actual power,use actual power"
+ "Last session was active and valid, reuse it"
+ "Loading TTE learning table from %@"
+ "ML model file for %@ not found"
+ "Model unavailable"
+ "Molly"
+ "Power correction - Predicted: %.2f, Actual: %.2f, RemEnergy%%: %.2f, Corrected: %.2f"
+ "PowerUITTEManager"
+ "PowerUITTEMonitor"
+ "PowerUITTEPredParam"
+ "PowerUITTEPredResults"
+ "PowerUITTEPredictor"
+ "PowerUITTEUtility"
+ "Rate limiting: skipping notification within %f of previous"
+ "Remaining Battery Runtime"
+ "S0"
+ "S1"
+ "S2"
+ "S3"
+ "SOC change in discharge mode"
+ "Saving TTE monitor metrics to NSUserDefaults"
+ "StateOfCharge"
+ "Successfully updated power tables and wrote to plist"
+ "T@\"<MLFeatureProvider>\",&,N,V_inputFeatures"
+ "T@\"MLModel\",&,N,V_ttePredictionModel"
+ "T@\"NSArray\",&,N,V_predictedFeatureNames"
+ "T@\"NSDate\",&,N,V_lastNotificationTime"
+ "T@\"NSDate\",&,V_lastPluggedInDate"
+ "T@\"NSDate\",&,V_lastUnpluggedDate"
+ "T@\"NSDate\",&,V_pauseChargingCheckDate"
+ "T@\"NSDictionary\",&,N,V_stateDescriptions"
+ "T@\"NSDictionary\",&,N,V_tteLearningTable"
+ "T@\"NSString\",&,N,V_modelName"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_version"
+ "T@\"NSString\",&,V_tteFormatted"
+ "T@\"NSUUID\",&,V_tteSessionID"
+ "T@\"PowerUITTEMonitor\",&,N,V_tteMonitor"
+ "T@\"PowerUITTEPredParam\",&,N,V_ttePredictionParameters"
+ "T@\"PowerUITTEPredResults\",&,V_ttePredictions"
+ "T@\"PowerUITTEPredictor\",&,N,V_ttePredictor"
+ "TQ,R,N,V_currentState"
+ "TQ,V_chargingStatus"
+ "TQ,V_currentStatus"
+ "TTE Fallback"
+ "TTE correction"
+ "TTE data Byte representation:\n%@"
+ "TTE idle"
+ "TTE is either not supported or disabled. Skipping"
+ "TTE monitor is nil, cannot record discharge session"
+ "TTE now disable. Resetting state."
+ "TTE now enabled. Triggering callback to enter idle state."
+ "TTE predicot is nil, cannot record discharge session"
+ "TTE prediction"
+ "TTE predictor is nil, cannot proceed with prediction"
+ "TTE state update from %lu to %lu (%@ --> %@); BatteryLevel %ld, PluggedIn %d"
+ "TTECategory"
+ "TTE_Model_SeB"
+ "TTE_Model_SeBInput"
+ "TTE_Model_SeBOutput"
+ "TTE_Model_SeS"
+ "TTE_Model_SeSInput"
+ "TTE_Model_SeSOutput"
+ "TTE_Model_SeriesB"
+ "TTE_Model_SeriesBInput"
+ "TTE_Model_SeriesBOutput"
+ "TTE_Model_SeriesS"
+ "TTE_Model_SeriesSInput"
+ "TTE_Model_SeriesSOutput"
+ "TTE_Model_Ultra"
+ "TTE_Model_UltraInput"
+ "TTE_Model_UltraOutput"
+ "TTE_Prediction_GBD"
+ "Td,N,V_prediction"
+ "Td,N,V_x1"
+ "Td,N,V_x2"
+ "Td,N,V_x3"
+ "Td,N,V_x4"
+ "Td,N,V_x5"
+ "Td,N,V_x6"
+ "Td,N,V_x7"
+ "Td,N,V_x8"
+ "Td,N,V_x9"
+ "Tf,N,V_averagePower"
+ "Tf,N,V_confidenceWidth"
+ "Tf,N,V_maxPower"
+ "Tf,N,V_minPower"
+ "Tf,V_correctedPower"
+ "Tf,V_remEnergyDischargeEnd"
+ "Tf,V_tteInMinutes"
+ "Ti,N,V_modelType"
+ "TimeToEmptyDbgData"
+ "Tq,N,V__tteMonitorStatus"
+ "Tq,N,V_ttePreResultsStatus"
+ "Tq,N,V_ttePredictionModelStatus"
+ "Tq,V_lastSOCValue"
+ "T{os_unfair_lock_s=I},N,V_learnTableLock"
+ "T{os_unfair_lock_s=I},N,V_modelLock"
+ "Unkown"
+ "Unsupported watch model type %d, using Ultra model as fallback"
+ "Updated power tables for %@/%@/%@ with Paverage: %.2f over %.2f hours. Tempo values: [%@]"
+ "VALIDE_REM_ENERGY(currentRemEnergy) && (startRemEnergy > 0)"
+ "Voltage"
+ "Willy"
+ "__tteMonitorStatus"
+ "_averagePower"
+ "_chargingStatus"
+ "_confidenceWidth"
+ "_correctedPower"
+ "_currentStatus"
+ "_inputFeatures"
+ "_lastNotificationTime"
+ "_lastSOCValue"
+ "_learnTableLock"
+ "_maxPower"
+ "_minPower"
+ "_modelLock"
+ "_modelName"
+ "_modelType"
+ "_name"
+ "_predictedFeatureNames"
+ "_prediction"
+ "_remEnergyDischargeEnd"
+ "_stateDescriptions"
+ "_tteFormatted"
+ "_tteInMinutes"
+ "_tteLearningTable"
+ "_tteMonitor"
+ "_tteMonitorStatus"
+ "_ttePreResultsStatus"
+ "_ttePredictionModel"
+ "_ttePredictionModelStatus"
+ "_ttePredictionParameters"
+ "_ttePredictions"
+ "_ttePredictor"
+ "_tteSessionID"
+ "_version"
+ "_x1"
+ "_x2"
+ "_x3"
+ "_x4"
+ "_x5"
+ "_x6"
+ "_x7"
+ "_x8"
+ "_x9"
+ "actualPower"
+ "appendFormat:"
+ "appendString:"
+ "averagePower"
+ "avgDischargePower"
+ "bytes"
+ "caculateInferredTTE"
+ "calculateActualPowerWithDefaults:withStartEnergy:withCurrentEnergy:"
+ "calculateAndUpdatePaverageOnPluginDetected"
+ "calculateTTEWithPower:"
+ "changeStateTo:"
+ "check if TTE is enabled. feature:%d, isInternalBuild:%d, isSupportedWatch:%d."
+ "clock"
+ "collectedPaverage"
+ "com.apple.powerui.tte"
+ "com.apple.powerui.tte.batterySocLevel"
+ "com.apple.powerui.tte.queue"
+ "com.apple.powerui.tte.unplug"
+ "com.apple.powerui.tteManager"
+ "com.apple.powerui.tte_prediction"
+ "com.apple.tte.evaluation.v1"
+ "com.apple.tte.monitor.v1"
+ "com.apple.tte.prediction.v1"
+ "componentsJoinedByString:"
+ "confidenceWidth"
+ "correctAveragePower:"
+ "correctedPower"
+ "currenSOC"
+ "currentRemEnergy"
+ "currentStatus"
+ "currentTTEDiff"
+ "currentTrueTTE"
+ "dataWithPropertyList:format:options:error:"
+ "detect unplug, entering prediction"
+ "device plugged in %@"
+ "device started in discharge, entering prediction"
+ "device unplugged %@"
+ "device, restarted, Last session was active and valid, reuse it"
+ "dischargeEndTTE"
+ "endRemEnergy"
+ "entered unsupported state"
+ "exportLearnTable"
+ "f"
+ "f16@0:8"
+ "f32@0:8@16@24"
+ "f40@0:8@16^f24^f32"
+ "fail to retrieve BatteryData"
+ "fail to retrieve BatteryData dictionary"
+ "fail to retrieve TimeToEmptyDbgData"
+ "failed to fetch SOC from SMC"
+ "failed to find Pmean"
+ "failed to find existing feature for "
+ "failed to find the learning table for "
+ "failed to find the time bucket for "
+ "failed to find time bucket"
+ "failed to load the tteTablePmean table"
+ "failed to load the tteTableTempo array"
+ "failed to predict tte"
+ "feature extraction failed"
+ "fetchLearningTable"
+ "fetchPresentRemEnergy"
+ "fetchPresentSOC"
+ "fetchPresentTemperature"
+ "fetchWatchModelType"
+ "fetchWatchModelType detected model: %d"
+ "fileURLWithPath:isDirectory:"
+ "filterPower"
+ "findTimeBuckets:"
+ "formatTTEToRightScale"
+ "getCorrectedPower"
+ "getInputFeaturesForTTEPrediction:"
+ "getModelVersion"
+ "getTTEDatafromSMC"
+ "handleIsEnabledChangeWithFlag:"
+ "hourRaw"
+ "hours"
+ "i32@0:8@16@24"
+ "illegal AlgoTemperature, value:%f"
+ "illegal StateOfCharge, value:%f"
+ "illegal remEnergy, value:%f"
+ "illegal time for update TTE monitor session, existing"
+ "in correction state, has SOC change?:%@"
+ "in fallback state"
+ "in idle state waiting for device unplug"
+ "initWithDefaultsDomain:withContextStore:"
+ "initWithPrediction:"
+ "initWithX1:x2:x3:x4:x5:x6:x7:x8:x9:"
+ "initialTrueTTE"
+ "inputFeatures"
+ "intialTTEDiff"
+ "invalid tempo value type"
+ "isValid"
+ "last session is invalid record a new session at %@"
+ "last time prediciton at %@, trying to update at %@"
+ "lastNotificationTime"
+ "lastSOCValue"
+ "learnTableLock"
+ "learning table is nil or not a dictionary"
+ "less than 30 Minutes"
+ "loadResultsWithDefaults:"
+ "loadTTELearningTable"
+ "loadTTEModelFromBundle:"
+ "maxPower"
+ "minPower"
+ "model inference failed"
+ "model name is null"
+ "modelLock"
+ "modelName"
+ "modelType"
+ "monitorUnpluggedChange"
+ "month"
+ "monthRaw"
+ "name"
+ "none"
+ "paverage > 0"
+ "plist"
+ "plug in detected, record session and switch back to sandby"
+ "plugged"
+ "post noitification for %@"
+ "postAnalyticsEventAtEnd:"
+ "postAnalyticsEventAtPrediction"
+ "postAnalyticsEventDurCorrection:"
+ "postPredictionNotification"
+ "postPredictionNotificationWithReason:"
+ "postTTEPredictionNotification:"
+ "predictTTEAt:withReason:"
+ "predicted time to empty in minutes: %f with power: %f"
+ "predictedFeatureNames"
+ "predictedPower"
+ "predictedTTE"
+ "predictedTTEWithStartTimeStamp:"
+ "prediction"
+ "prediction not found"
+ "prediction not successful, use default fallback"
+ "prediction successful, results is %ld"
+ "predictionFromX1:x2:x3:x4:x5:x6:x7:x8:x9:error:"
+ "predictionStatus"
+ "processModelInference:"
+ "readPlistToDictionary:"
+ "recordDischargeSessionAt:"
+ "remEnergy != POS_FLOAT_INVALID"
+ "remEnergy invalid and no session data available for fallback calculation"
+ "remEnergy invalid, using fallback TTE: original=%.2f - elapsed=%.2f = %.2f minutes"
+ "remEnergyDischargeEnd"
+ "remainingEnergy"
+ "remainingMinutes"
+ "removeAllNotificationsExceptFor:"
+ "reset"
+ "resetSessionForTTE"
+ "runModelInferenceforTTEPrediction"
+ "safeExtractDictionary:forKey:"
+ "safeExtractNumber:forKey:"
+ "safeFetchNumberFromDefaults:forKey:functionName:"
+ "safeFetchPosFloatFromDefaults"
+ "safeFetchPosFloatFromDefaults: Invalid float value %f for key %@"
+ "safeFetchPosFloatFromDefaults:forKey:"
+ "safeFetchPosIntFromDefaults"
+ "safeFetchPosIntFromDefaults: Invalid int value %d for key %@"
+ "safeFetchPosIntFromDefaults:forKey:"
+ "searchValueForPlist:withKeyArray:"
+ "sessionActive"
+ "sessionActiveNumber"
+ "sessionHours"
+ "sessionStartTime"
+ "sessionTimeElapsed"
+ "setAveragePower:"
+ "setChargingStatus:"
+ "setConfidenceWidth:"
+ "setCorrectedPower:"
+ "setCurrentStatus:"
+ "setInputFeatures:"
+ "setLastNotificationTime:"
+ "setLastSOCValue:"
+ "setLearnTableLock:"
+ "setMaxPower:"
+ "setMinPower:"
+ "setModelLock:"
+ "setModelName:"
+ "setModelType:"
+ "setName:"
+ "setPredictedFeatureNames:"
+ "setPrediction:"
+ "setRemEnergyDischargeEnd:"
+ "setStateDescriptions:"
+ "setTTE:"
+ "setTteFormatted:"
+ "setTteInMinutes:"
+ "setTteLearningTable:"
+ "setTteMonitor:"
+ "setTtePreResultsStatus:"
+ "setTtePredictionModel:"
+ "setTtePredictionModelStatus:"
+ "setTtePredictionParameters:"
+ "setTtePredictions:"
+ "setTtePredictor:"
+ "setTteSessionID:"
+ "setVersion:"
+ "setX1:"
+ "setX2:"
+ "setX3:"
+ "setX4:"
+ "setX5:"
+ "setX6:"
+ "setX7:"
+ "setX8:"
+ "setX9:"
+ "set_tteMonitorStatus:"
+ "startHour"
+ "startRemEnergy"
+ "startSeason"
+ "startTimeStamp"
+ "startWeekday"
+ "stateDescriptions"
+ "string"
+ "stringForTriggerReason:"
+ "timeBuckets"
+ "timegapHr is less than kminMonitoringGap, skip session update"
+ "totalSeconds>0"
+ "tte"
+ "tte format error"
+ "tte prediciton is not available currentFormattedTTE is nil"
+ "tteBatteryDataLogs %@"
+ "tteFormatted"
+ "tteInMinutes"
+ "tteLearningTable"
+ "tteManager"
+ "tteMonitor"
+ "ttePreResultsStatus"
+ "ttePrediction"
+ "ttePredictionModel"
+ "ttePredictionModelStatus"
+ "ttePredictionParameters"
+ "ttePredictionResultsStatus"
+ "ttePredictions"
+ "ttePredictor"
+ "tteSessionID"
+ "tteTableHarry"
+ "tteTableMolly"
+ "tteTablePeter"
+ "tteTableTempo"
+ "tteTableWilly"
+ "unplugged"
+ "updateFeatureEnable"
+ "updateLearningTable:"
+ "updateLearningTableEntry:withTimeBuckets:withPaverage:andHours:"
+ "updateTTEMonitorSession:"
+ "v20@0:8f16"
+ "v24@?0@\"NSMutableDictionary\"8@\"NSString\"16"
+ "v32@0:8^B16^B24"
+ "v40@0:8@16@24f32f36"
+ "valid predicted power and invalid actual power,use prediction power"
+ "validationLastPredSessionWithValidFlag:withActiveFlag:"
+ "version"
+ "watchType"
+ "weekdayRaw"
+ "writeDictionaryToPlist:withFilePath:"
+ "writeToURL:options:error:"
+ "x1"
+ "x2"
+ "x3"
+ "x4"
+ "x5"
+ "x6"
+ "x7"
+ "x8"
+ "x9"

```
