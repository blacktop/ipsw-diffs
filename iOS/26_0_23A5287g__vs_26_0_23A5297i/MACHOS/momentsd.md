## momentsd

> `/usr/libexec/momentsd`

```diff

-269.0.0.0.0
-  __TEXT.__text: 0x246290
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_stubs: 0x1cd80
-  __TEXT.__objc_methlist: 0x10a50
-  __TEXT.__cstring: 0x2542f
+277.0.0.0.0
+  __TEXT.__text: 0x24b0d8
+  __TEXT.__auth_stubs: 0x1ae0
+  __TEXT.__objc_stubs: 0x1d200
+  __TEXT.__objc_methlist: 0x111e0
+  __TEXT.__cstring: 0x2618f
   __TEXT.__objc_classname: 0x1b58
-  __TEXT.__objc_methtype: 0x308d
-  __TEXT.__objc_methname: 0x33858
-  __TEXT.__oslogstring: 0x2e67b
-  __TEXT.__const: 0x1141
-  __TEXT.__gcc_except_tab: 0x7dec
+  __TEXT.__objc_methtype: 0x315e
+  __TEXT.__objc_methname: 0x36c94
+  __TEXT.__oslogstring: 0x2ee9b
+  __TEXT.__const: 0x1231
+  __TEXT.__gcc_except_tab: 0x7e04
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x5ec
-  __TEXT.__swift5_typeref: 0x440
-  __TEXT.__swift5_reflstr: 0x144
-  __TEXT.__swift5_fieldmd: 0x22c
+  __TEXT.__swift5_typeref: 0x456
+  __TEXT.__swift5_reflstr: 0x149
+  __TEXT.__swift5_fieldmd: 0x238
   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_capture: 0x300
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x4e50
-  __TEXT.__eh_frame: 0xa38
-  __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0xb98
+  __TEXT.__unwind_info: 0x4e68
+  __TEXT.__eh_frame: 0xa68
+  __DATA_CONST.__auth_got: 0xd88
+  __DATA_CONST.__got: 0xba8
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0xb348
-  __DATA_CONST.__cfstring: 0x243a0
+  __DATA_CONST.__const: 0xb4c8
+  __DATA_CONST.__cfstring: 0x24ee0
   __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_intobj: 0x3df8
-  __DATA_CONST.__objc_arraydata: 0x15a8
-  __DATA_CONST.__objc_arrayobj: 0xa98
+  __DATA_CONST.__objc_intobj: 0x3ea0
+  __DATA_CONST.__objc_arraydata: 0x16b8
+  __DATA_CONST.__objc_arrayobj: 0xac8
   __DATA_CONST.__objc_doubleobj: 0x4c0
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_floatobj: 0x250
-  __DATA.__objc_const: 0x1c420
-  __DATA.__objc_selrefs: 0x8d90
-  __DATA.__objc_ivar: 0x1594
-  __DATA.__objc_data: 0x55b0
-  __DATA.__data: 0x18b8
-  __DATA.__common: 0x2cc
+  __DATA.__objc_const: 0x1d2b0
+  __DATA.__objc_selrefs: 0x92b0
+  __DATA.__objc_ivar: 0x16c8
+  __DATA.__objc_data: 0x55c0
+  __DATA.__data: 0x18c8
+  __DATA.__common: 0x2e4
   __DATA.__bss: 0x3a0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
   - /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 129D960C-7389-3079-8168-DE563A5B5D9D
-  Functions: 8234
-  Symbols:   58552
-  CStrings:  20112
+  UUID: BD488A65-2823-3A66-8DEF-FBDF58AFEA5D
+  Functions: 8405
+  Symbols:   59636
+  CStrings:  20618
 
Symbols:
+ +[MOAvailabilityPredictionManager calculateOverlapPercentageForPredictionWindowStartHour:predictionWindowEndHour:eventStartHour:eventEndHour:]
+ +[MOAvailabilityPredictionManager getWeekday:]
+ +[availabilityPredict061725 URLOfModelInThisBundle]
+ +[availabilityPredict061725 URLOfModelInThisBundle].cold.1
+ +[availabilityPredict061725 loadContentsOfURL:configuration:completionHandler:]
+ +[availabilityPredict061725 loadWithConfiguration:completionHandler:]
+ -[MOAvailabilityPredictionManager atHomeCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager atHomeCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager atHomeCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager atHomeCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager atWorkCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager atWorkCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager atWorkCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager atWorkCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager atWorkSameWeekdayProbabilityFeatureScaleMean]
+ -[MOAvailabilityPredictionManager atWorkSameWeekdayProbabilityFeatureScaleStd]
+ -[MOAvailabilityPredictionManager availabilityPredictionProbabilityInsufficientScreentimeThreshold]
+ -[MOAvailabilityPredictionManager callCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager callCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager checkNonzeroMedianScreentimeUsagePerHour:]
+ -[MOAvailabilityPredictionManager checkNonzeroMedianScreentimeUsagePerHour:].cold.1
+ -[MOAvailabilityPredictionManager copyAndTrim:toWindowStartDate:returnAsMOEvent:]
+ -[MOAvailabilityPredictionManager countOccurenceOfEvents:forWindow:windowSize:checkTime:checkWeekday:addBuffer:checkOverlapPercentage:forFeature:]
+ -[MOAvailabilityPredictionManager countOccurenceOfEvents:forWindow:windowSize:checkTime:checkWeekday:addBuffer:checkOverlapPercentage:forFeature:].cold.1
+ -[MOAvailabilityPredictionManager downtimeDetectionDefaultSleepEndHour]
+ -[MOAvailabilityPredictionManager downtimeEndHourFeatureScaleMean]
+ -[MOAvailabilityPredictionManager downtimeEndHourFeatureScaleStd]
+ -[MOAvailabilityPredictionManager engagementCountBin1MidLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager engagementCountBin1MidLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager engagementCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager engagementCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager engagementCountMidLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager engagementCountMidLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:andDowntimeWindowEndHour:]
+ -[MOAvailabilityPredictionManager findOptimalDateWithPrediction:withPredictionProbabilityThreshold:]
+ -[MOAvailabilityPredictionManager firstScreentimeOfDayFeatureScaleMean]
+ -[MOAvailabilityPredictionManager firstScreentimeOfDayFeatureScaleStd]
+ -[MOAvailabilityPredictionManager getMediaPlaySessionStartDates:]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountMidLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountMidLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager healthandfitnessScreentimeCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager isAfternoonFeatureScaleMean]
+ -[MOAvailabilityPredictionManager isAfternoonFeatureScaleStd]
+ -[MOAvailabilityPredictionManager isEveningFeatureScaleMean]
+ -[MOAvailabilityPredictionManager isEveningFeatureScaleStd]
+ -[MOAvailabilityPredictionManager isNightFeatureScaleMean]
+ -[MOAvailabilityPredictionManager isNightFeatureScaleStd]
+ -[MOAvailabilityPredictionManager lastScreentimeOfDayFeatureScaleMean]
+ -[MOAvailabilityPredictionManager lastScreentimeOfDayFeatureScaleStd]
+ -[MOAvailabilityPredictionManager motionActivityCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager motionActivityCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager motionActivityCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager motionActivityCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager motionActivityOverlapCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager motionActivityOverlapCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager musicCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager musicCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager musicCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager musicCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager over20MinScreentimeCountMidLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager over20MinScreentimeCountMidLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager screentimeCountFeatureScaleMean]
+ -[MOAvailabilityPredictionManager screentimeCountFeatureScaleStd]
+ -[MOAvailabilityPredictionManager screentimeCountShortLookbackFeatureScaleMean]
+ -[MOAvailabilityPredictionManager screentimeCountShortLookbackFeatureScaleStd]
+ -[MOAvailabilityPredictionManager screentimeSameWeekdayProbabilityFeatureScaleMean]
+ -[MOAvailabilityPredictionManager screentimeSameWeekdayProbabilityFeatureScaleStd]
+ -[MOAvailabilityPredictionManager setAtHomeCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setAtHomeCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setAtHomeCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setAtHomeCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setAtWorkCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setAtWorkCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setAtWorkCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setAtWorkCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setAtWorkSameWeekdayProbabilityFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setAtWorkSameWeekdayProbabilityFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setAvailabilityPredictionProbabilityInsufficientScreentimeThreshold:]
+ -[MOAvailabilityPredictionManager setCallCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setCallCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setDowntimeDetectionDefaultSleepEndHour:]
+ -[MOAvailabilityPredictionManager setDowntimeEndHourFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setDowntimeEndHourFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setEngagementCountBin1MidLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setEngagementCountBin1MidLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setEngagementCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setEngagementCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setEngagementCountMidLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setEngagementCountMidLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setFirstScreentimeOfDayFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setFirstScreentimeOfDayFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountMidLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountMidLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setHealthandfitnessScreentimeCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setIsAfternoonFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setIsAfternoonFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setIsEveningFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setIsEveningFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setIsNightFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setIsNightFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setLastScreentimeOfDayFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setLastScreentimeOfDayFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setMotionActivityCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setMotionActivityCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setMotionActivityCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setMotionActivityCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setMotionActivityOverlapCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setMotionActivityOverlapCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setMusicCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setMusicCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setMusicCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setMusicCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setOver20MinScreentimeCountMidLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setOver20MinScreentimeCountMidLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setScreentimeCountFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setScreentimeCountFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setScreentimeCountShortLookbackFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setScreentimeCountShortLookbackFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setScreentimeSameWeekdayProbabilityFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setScreentimeSameWeekdayProbabilityFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager setWeekdayFeatureScaleMean:]
+ -[MOAvailabilityPredictionManager setWeekdayFeatureScaleStd:]
+ -[MOAvailabilityPredictionManager weekdayFeatureScaleMean]
+ -[MOAvailabilityPredictionManager weekdayFeatureScaleStd]
+ -[MOEngagementHistoryManager writeEngagementLightStreamForRemoteDevicesWithHandler:].cold.1
+ -[MOMultiDeviceEngagementManager latestViewedEngagmentDateFrom:to:]
+ -[MOScreenTimeManager _registerForDeviceActivity]
+ -[availabilityPredict061725 .cxx_destruct]
+ -[availabilityPredict061725 initWithConfiguration:error:]
+ -[availabilityPredict061725 initWithContentsOfURL:configuration:error:]
+ -[availabilityPredict061725 initWithContentsOfURL:error:]
+ -[availabilityPredict061725 initWithMLModel:]
+ -[availabilityPredict061725 init]
+ -[availabilityPredict061725 model]
+ -[availabilityPredict061725 predictionFromDowntimeStartHour:downtimeEndHour:hour:weekday:motionActivityCount:motionActivityCountShortLookback:motionActivityOverlapCountShortLookback:engagementCount:engagementCountMidLookback:engagementCountBin1MidLookback:healthandfitnessScreentimeCount:healthandfitnessScreentimeCountMidLookback:healthandfitnessScreentimeCountShortLookback:screentimeCount:screentimeSameWeekdayProbability:screentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:overMedianScreentimeSameWeekdayProbabilityShortLookback:over20MinScreentimeSameWeekdayProbability:over20MinScreentimeCountMidLookback:callCount:musicCount:musicCountShortLookback:atHomeCount:atHomeCountShortLookback:atWorkCount:atWorkSameWeekdayProbability:atWorkCountShortLookback:weekdayPrevScreentimeCount:firstScreentimeOfDay:lastScreentimeOfDay:isAfternoon:isEvening:isMorning:isNight:error:]
+ -[availabilityPredict061725 predictionFromFeatures:completionHandler:]
+ -[availabilityPredict061725 predictionFromFeatures:error:]
+ -[availabilityPredict061725 predictionFromFeatures:options:completionHandler:]
+ -[availabilityPredict061725 predictionFromFeatures:options:error:]
+ -[availabilityPredict061725 predictionsFromInputs:options:error:]
+ -[availabilityPredict061725Input atHomeCountShortLookback]
+ -[availabilityPredict061725Input atHomeCount]
+ -[availabilityPredict061725Input atWorkCountShortLookback]
+ -[availabilityPredict061725Input atWorkCount]
+ -[availabilityPredict061725Input atWorkSameWeekdayProbability]
+ -[availabilityPredict061725Input callCount]
+ -[availabilityPredict061725Input downtimeEndHour]
+ -[availabilityPredict061725Input downtimeStartHour]
+ -[availabilityPredict061725Input engagementCountBin1MidLookback]
+ -[availabilityPredict061725Input engagementCountMidLookback]
+ -[availabilityPredict061725Input engagementCount]
+ -[availabilityPredict061725Input featureNames]
+ -[availabilityPredict061725Input featureValueForName:]
+ -[availabilityPredict061725Input firstScreentimeOfDay]
+ -[availabilityPredict061725Input healthandfitnessScreentimeCountMidLookback]
+ -[availabilityPredict061725Input healthandfitnessScreentimeCountShortLookback]
+ -[availabilityPredict061725Input healthandfitnessScreentimeCount]
+ -[availabilityPredict061725Input hour]
+ -[availabilityPredict061725Input initWithDowntimeStartHour:downtimeEndHour:hour:weekday:motionActivityCount:motionActivityCountShortLookback:motionActivityOverlapCountShortLookback:engagementCount:engagementCountMidLookback:engagementCountBin1MidLookback:healthandfitnessScreentimeCount:healthandfitnessScreentimeCountMidLookback:healthandfitnessScreentimeCountShortLookback:screentimeCount:screentimeSameWeekdayProbability:screentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:overMedianScreentimeSameWeekdayProbabilityShortLookback:over20MinScreentimeSameWeekdayProbability:over20MinScreentimeCountMidLookback:callCount:musicCount:musicCountShortLookback:atHomeCount:atHomeCountShortLookback:atWorkCount:atWorkSameWeekdayProbability:atWorkCountShortLookback:weekdayPrevScreentimeCount:firstScreentimeOfDay:lastScreentimeOfDay:isAfternoon:isEvening:isMorning:isNight:]
+ -[availabilityPredict061725Input isAfternoon]
+ -[availabilityPredict061725Input isEvening]
+ -[availabilityPredict061725Input isMorning]
+ -[availabilityPredict061725Input isNight]
+ -[availabilityPredict061725Input lastScreentimeOfDay]
+ -[availabilityPredict061725Input motionActivityCountShortLookback]
+ -[availabilityPredict061725Input motionActivityCount]
+ -[availabilityPredict061725Input motionActivityOverlapCountShortLookback]
+ -[availabilityPredict061725Input musicCountShortLookback]
+ -[availabilityPredict061725Input musicCount]
+ -[availabilityPredict061725Input over20MinScreentimeCountMidLookback]
+ -[availabilityPredict061725Input over20MinScreentimeSameWeekdayProbability]
+ -[availabilityPredict061725Input overMedianScreentimeSameWeekdayProbabilityShortLookback]
+ -[availabilityPredict061725Input overMedianScreentimeSameWeekdayProbability]
+ -[availabilityPredict061725Input screentimeCountShortLookback]
+ -[availabilityPredict061725Input screentimeCount]
+ -[availabilityPredict061725Input screentimeSameWeekdayProbability]
+ -[availabilityPredict061725Input setAtHomeCount:]
+ -[availabilityPredict061725Input setAtHomeCountShortLookback:]
+ -[availabilityPredict061725Input setAtWorkCount:]
+ -[availabilityPredict061725Input setAtWorkCountShortLookback:]
+ -[availabilityPredict061725Input setAtWorkSameWeekdayProbability:]
+ -[availabilityPredict061725Input setCallCount:]
+ -[availabilityPredict061725Input setDowntimeEndHour:]
+ -[availabilityPredict061725Input setDowntimeStartHour:]
+ -[availabilityPredict061725Input setEngagementCount:]
+ -[availabilityPredict061725Input setEngagementCountBin1MidLookback:]
+ -[availabilityPredict061725Input setEngagementCountMidLookback:]
+ -[availabilityPredict061725Input setFirstScreentimeOfDay:]
+ -[availabilityPredict061725Input setHealthandfitnessScreentimeCount:]
+ -[availabilityPredict061725Input setHealthandfitnessScreentimeCountMidLookback:]
+ -[availabilityPredict061725Input setHealthandfitnessScreentimeCountShortLookback:]
+ -[availabilityPredict061725Input setHour:]
+ -[availabilityPredict061725Input setIsAfternoon:]
+ -[availabilityPredict061725Input setIsEvening:]
+ -[availabilityPredict061725Input setIsMorning:]
+ -[availabilityPredict061725Input setIsNight:]
+ -[availabilityPredict061725Input setLastScreentimeOfDay:]
+ -[availabilityPredict061725Input setMotionActivityCount:]
+ -[availabilityPredict061725Input setMotionActivityCountShortLookback:]
+ -[availabilityPredict061725Input setMotionActivityOverlapCountShortLookback:]
+ -[availabilityPredict061725Input setMusicCount:]
+ -[availabilityPredict061725Input setMusicCountShortLookback:]
+ -[availabilityPredict061725Input setOver20MinScreentimeCountMidLookback:]
+ -[availabilityPredict061725Input setOver20MinScreentimeSameWeekdayProbability:]
+ -[availabilityPredict061725Input setOverMedianScreentimeSameWeekdayProbability:]
+ -[availabilityPredict061725Input setOverMedianScreentimeSameWeekdayProbabilityShortLookback:]
+ -[availabilityPredict061725Input setScreentimeCount:]
+ -[availabilityPredict061725Input setScreentimeCountShortLookback:]
+ -[availabilityPredict061725Input setScreentimeSameWeekdayProbability:]
+ -[availabilityPredict061725Input setWeekday:]
+ -[availabilityPredict061725Input setWeekdayPrevScreentimeCount:]
+ -[availabilityPredict061725Input weekdayPrevScreentimeCount]
+ -[availabilityPredict061725Input weekday]
+ -[availabilityPredict061725Output .cxx_destruct]
+ -[availabilityPredict061725Output classProbability]
+ -[availabilityPredict061725Output featureNames]
+ -[availabilityPredict061725Output featureValueForName:]
+ -[availabilityPredict061725Output initWithTarget:classProbability:]
+ -[availabilityPredict061725Output setClassProbability:]
+ -[availabilityPredict061725Output setTarget:]
+ -[availabilityPredict061725Output target]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/DerivedSources/CoreMLGenerated/availabilityPredict061725/
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/availabilityPredict061725.o
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atHomeCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atHomeCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atHomeCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atHomeCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkSameWeekdayProbabilityFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._atWorkSameWeekdayProbabilityFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._availabilityPredictionProbabilityInsufficientScreentimeThreshold
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._callCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._callCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._downtimeDetectionDefaultSleepEndHour
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._downtimeEndHourFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._downtimeEndHourFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountBin1MidLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountBin1MidLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountMidLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._engagementCountMidLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._firstScreentimeOfDayFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._firstScreentimeOfDayFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountMidLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountMidLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._healthandfitnessScreentimeCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isAfternoonFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isAfternoonFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isEveningFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isEveningFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isNightFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._isNightFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._lastScreentimeOfDayFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._lastScreentimeOfDayFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityOverlapCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._motionActivityOverlapCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._musicCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._musicCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._musicCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._musicCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._over20MinScreentimeCountMidLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._over20MinScreentimeCountMidLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeCountFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeCountFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeCountShortLookbackFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeCountShortLookbackFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeSameWeekdayProbabilityFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._screentimeSameWeekdayProbabilityFeatureScaleStd
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._weekdayFeatureScaleMean
+ OBJC_IVAR_$_MOAvailabilityPredictionManager._weekdayFeatureScaleStd
+ OBJC_IVAR_$_availabilityPredict061725._model
+ OBJC_IVAR_$_availabilityPredict061725Input._atHomeCount
+ OBJC_IVAR_$_availabilityPredict061725Input._atHomeCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._atWorkCount
+ OBJC_IVAR_$_availabilityPredict061725Input._atWorkCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._atWorkSameWeekdayProbability
+ OBJC_IVAR_$_availabilityPredict061725Input._callCount
+ OBJC_IVAR_$_availabilityPredict061725Input._downtimeEndHour
+ OBJC_IVAR_$_availabilityPredict061725Input._downtimeStartHour
+ OBJC_IVAR_$_availabilityPredict061725Input._engagementCount
+ OBJC_IVAR_$_availabilityPredict061725Input._engagementCountBin1MidLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._engagementCountMidLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._firstScreentimeOfDay
+ OBJC_IVAR_$_availabilityPredict061725Input._healthandfitnessScreentimeCount
+ OBJC_IVAR_$_availabilityPredict061725Input._healthandfitnessScreentimeCountMidLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._healthandfitnessScreentimeCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._hour
+ OBJC_IVAR_$_availabilityPredict061725Input._isAfternoon
+ OBJC_IVAR_$_availabilityPredict061725Input._isEvening
+ OBJC_IVAR_$_availabilityPredict061725Input._isMorning
+ OBJC_IVAR_$_availabilityPredict061725Input._isNight
+ OBJC_IVAR_$_availabilityPredict061725Input._lastScreentimeOfDay
+ OBJC_IVAR_$_availabilityPredict061725Input._motionActivityCount
+ OBJC_IVAR_$_availabilityPredict061725Input._motionActivityCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._motionActivityOverlapCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._musicCount
+ OBJC_IVAR_$_availabilityPredict061725Input._musicCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._over20MinScreentimeCountMidLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._over20MinScreentimeSameWeekdayProbability
+ OBJC_IVAR_$_availabilityPredict061725Input._overMedianScreentimeSameWeekdayProbability
+ OBJC_IVAR_$_availabilityPredict061725Input._overMedianScreentimeSameWeekdayProbabilityShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._screentimeCount
+ OBJC_IVAR_$_availabilityPredict061725Input._screentimeCountShortLookback
+ OBJC_IVAR_$_availabilityPredict061725Input._screentimeSameWeekdayProbability
+ OBJC_IVAR_$_availabilityPredict061725Input._weekday
+ OBJC_IVAR_$_availabilityPredict061725Input._weekdayPrevScreentimeCount
+ OBJC_IVAR_$_availabilityPredict061725Output._classProbability
+ OBJC_IVAR_$_availabilityPredict061725Output._target
+ _$s7ToolKit10TypedValueO09PrimitiveD0O6stringyAESScAEmFWC
+ _$s8momentsd12CommonLoggerC4tips2os0C0Vvau
+ _$s8momentsd12CommonLoggerC4tips2os0C0VvgZ
+ _$s8momentsd12CommonLoggerC4tips2os0C0VvpZ
+ _$s8momentsd12CommonLoggerC4tips2os0C0VvpZMV
+ _$s8momentsd12CommonLoggerC4tips_WZ
+ _$s8momentsd12CommonLoggerC4tips_Wz
+ _$s8momentsd16ServerConnectionC4lockSo15NSRecursiveLockCvg
+ _$s8momentsd16ServerConnectionC4lockSo15NSRecursiveLockCvpMV
+ _$s8momentsd16ServerConnectionC4lockSo15NSRecursiveLockCvpWvd
+ _$s8momentsd16ServerConnectionC4lockSo15NSRecursiveLockCvpfi
+ _$s8momentsd30ProcessingServerCoreConnectionC12remoteTargetAA0bcD0_pSgvgyyXEfU_Tf0nsn_n
+ _OBJC_CLASS_$_MOApplication
+ _OBJC_CLASS_$_MOLocalSettingsStore
+ _OBJC_CLASS_$_availabilityPredict061725
+ _OBJC_CLASS_$_availabilityPredict061725Input
+ _OBJC_CLASS_$_availabilityPredict061725Output
+ _OBJC_METACLASS_$_availabilityPredict061725
+ _OBJC_METACLASS_$_availabilityPredict061725Input
+ _OBJC_METACLASS_$_availabilityPredict061725Output
+ __101-[MOEngagementHistoryManager writeEngagementLightStreamForDevices:storedBookmarks:completionHandler:]_block_invoke.508
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.230
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.230.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.248
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.248.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.254
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.254.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.260
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.260.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.266
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.266.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.266.cold.2
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.270
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.271
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.275
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.282
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.282.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.288
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.288.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.294
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.294.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.303
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.303.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.304
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.304.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.308
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.308.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.231
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.237
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.243
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.249
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.255
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.261
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.276
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.283
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.289
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.295
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.301
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.232
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.238
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.244
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.250
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.256
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.262
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.277
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.284
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.290
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.296
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.302
+ __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1928
+ __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.603
+ __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.352
+ __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.665
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.442
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.442.cold.1
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.443
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.453
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.454
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.454.cold.1
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.445
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.445.cold.1
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.446
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.359
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.363
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.367
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.377
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.387
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.391
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.395
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.399
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.403
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.407
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.411
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.415
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.419
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.335
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337.cold.1
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.321
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.323
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.325
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.466
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.482
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.482.cold.1
+ __61-[MOAvailabilityPredictionManager saveEligiblePOICategories:]_block_invoke.2131
+ __61-[MOAvailabilityPredictionManager saveEligiblePOICategories:]_block_invoke.2131.cold.1
+ __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.683
+ __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.685
+ __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.649
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.435
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.435.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.442
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.442.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.449
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.449.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.453.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.454
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.454.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.456
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.200
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.200.cold.1
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.202
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.679
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.689
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.704
+ __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.451
+ __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.669
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.666
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.666.cold.1
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.667
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.667.cold.1
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.672
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.673
+ __84-[MOEngagementHistoryManager updateEngagementLightStreamWithRefreshVariant:handler:]_block_invoke.541
+ __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.331
+ __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.479
+ __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.480
+ __OBJC_$_CLASS_METHODS_MOAvailabilityPredictionManager
+ __OBJC_$_CLASS_METHODS_availabilityPredict061725
+ __OBJC_$_INSTANCE_METHODS_availabilityPredict061725
+ __OBJC_$_INSTANCE_METHODS_availabilityPredict061725Input
+ __OBJC_$_INSTANCE_METHODS_availabilityPredict061725Output
+ __OBJC_$_INSTANCE_VARIABLES_availabilityPredict061725
+ __OBJC_$_INSTANCE_VARIABLES_availabilityPredict061725Input
+ __OBJC_$_INSTANCE_VARIABLES_availabilityPredict061725Output
+ __OBJC_$_PROP_LIST_availabilityPredict061725
+ __OBJC_$_PROP_LIST_availabilityPredict061725Input
+ __OBJC_$_PROP_LIST_availabilityPredict061725Output
+ __OBJC_CLASS_PROTOCOLS_$_availabilityPredict061725Input
+ __OBJC_CLASS_PROTOCOLS_$_availabilityPredict061725Output
+ __OBJC_CLASS_RO_$_availabilityPredict061725
+ __OBJC_CLASS_RO_$_availabilityPredict061725Input
+ __OBJC_CLASS_RO_$_availabilityPredict061725Output
+ __OBJC_METACLASS_RO_$_availabilityPredict061725
+ __OBJC_METACLASS_RO_$_availabilityPredict061725Input
+ __OBJC_METACLASS_RO_$_availabilityPredict061725Output
+ ___67-[MOMultiDeviceEngagementManager latestViewedEngagmentDateFrom:to:]_block_invoke
+ ___67-[MOMultiDeviceEngagementManager latestViewedEngagmentDateFrom:to:]_block_invoke_2
+ ___70-[availabilityPredict061725 predictionFromFeatures:completionHandler:]_block_invoke
+ ___78-[availabilityPredict061725 predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___79+[availabilityPredict061725 loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ __block_literal_global.333
+ __block_literal_global.425
+ __block_literal_global.427
+ __block_literal_global.429
+ __block_literal_global.431
+ __block_literal_global.490
+ __block_literal_global.495
+ __block_literal_global.535
+ __block_literal_global.537
+ __block_literal_global.597
+ _kAPMAtHomeCountFeatureScaleMeanKey
+ _kAPMAtHomeCountFeatureScaleStdKey
+ _kAPMAtHomeCountShortLookbackFeatureScaleMeanKey
+ _kAPMAtHomeCountShortLookbackFeatureScaleStdKey
+ _kAPMAtWorkCountFeatureScaleMeanKey
+ _kAPMAtWorkCountFeatureScaleStdKey
+ _kAPMAtWorkCountShortLookbackFeatureScaleMeanKey
+ _kAPMAtWorkCountShortLookbackFeatureScaleStdKey
+ _kAPMAtWorkSameWeekdayProbabilityFeatureScaleMeanKey
+ _kAPMAtWorkSameWeekdayProbabilityFeatureScaleStdKey
+ _kAPMCallCountFeatureScaleMeanKey
+ _kAPMCallCountFeatureScaleStdKey
+ _kAPMDowntimeEndHourFeatureScaleMeanKey
+ _kAPMDowntimeEndHourFeatureScaleStdKey
+ _kAPMEngagementCountBin1MidLookbackFeatureScaleMeanKey
+ _kAPMEngagementCountBin1MidLookbackFeatureScaleStdKey
+ _kAPMEngagementCountFeatureScaleMeanKey
+ _kAPMEngagementCountFeatureScaleStdKey
+ _kAPMEngagementCountMidLookbackFeatureScaleMeanKey
+ _kAPMEngagementCountMidLookbackFeatureScaleStdKey
+ _kAPMFirstScreentimeOfDayFeatureScaleMeanKey
+ _kAPMFirstScreentimeOfDayFeatureScaleStdKey
+ _kAPMHealthandfitnessScreentimeCountFeatureScaleMeanKey
+ _kAPMHealthandfitnessScreentimeCountFeatureScaleStdKey
+ _kAPMHealthandfitnessScreentimeCountMidLookbackFeatureScaleMeanKey
+ _kAPMHealthandfitnessScreentimeCountMidLookbackFeatureScaleStdKey
+ _kAPMHealthandfitnessScreentimeCountShortLookbackFeatureScaleMeanKey
+ _kAPMHealthandfitnessScreentimeCountShortLookbackFeatureScaleStdKey
+ _kAPMIsAfternoonFeatureScaleMeanKey
+ _kAPMIsAfternoonFeatureScaleStdKey
+ _kAPMIsEveningFeatureScaleMeanKey
+ _kAPMIsEveningFeatureScaleStdKey
+ _kAPMIsNightFeatureScaleMeanKey
+ _kAPMIsNightFeatureScaleStdKey
+ _kAPMLastScreentimeOfDayFeatureScaleMeanKey
+ _kAPMLastScreentimeOfDayFeatureScaleStdKey
+ _kAPMMotionActivityCountFeatureScaleMeanKey
+ _kAPMMotionActivityCountFeatureScaleStdKey
+ _kAPMMotionActivityCountShortLookbackFeatureScaleMeanKey
+ _kAPMMotionActivityCountShortLookbackFeatureScaleStdKey
+ _kAPMMotionActivityOverlapCountShortLookbackFeatureScaleMeanKey
+ _kAPMMotionActivityOverlapCountShortLookbackFeatureScaleStdKey
+ _kAPMMusicCountFeatureScaleMeanKey
+ _kAPMMusicCountFeatureScaleStdKey
+ _kAPMMusicCountShortLookbackFeatureScaleMeanKey
+ _kAPMMusicCountShortLookbackFeatureScaleStdKey
+ _kAPMOver20MinScreentimeCountMidLookbackFeatureScaleMeanKey
+ _kAPMOver20MinScreentimeCountMidLookbackFeatureScaleStdKey
+ _kAPMOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMeanKey
+ _kAPMOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStdKey
+ _kAPMScreentimeCountFeatureScaleMeanKey
+ _kAPMScreentimeCountFeatureScaleStdKey
+ _kAPMScreentimeCountShortLookbackFeatureScaleMeanKey
+ _kAPMScreentimeCountShortLookbackFeatureScaleStdKey
+ _kAPMScreentimeSameWeekdayProbabilityFeatureScaleMeanKey
+ _kAPMScreentimeSameWeekdayProbabilityFeatureScaleStdKey
+ _kAPMWeekdayFeatureScaleMeanKey
+ _kAPMWeekdayFeatureScaleStdKey
+ _kAvailabilityPredictionProbabilityInsufficientScreentimeThresholdKey
+ _kDowntimeDetectionDefaultSleepEndHourKey
+ _objc_msgSend$_registerForDeviceActivity
+ _objc_msgSend$allowedClients
+ _objc_msgSend$atHomeCount
+ _objc_msgSend$atHomeCountShortLookback
+ _objc_msgSend$atWorkCount
+ _objc_msgSend$atWorkCountShortLookback
+ _objc_msgSend$atWorkSameWeekdayProbability
+ _objc_msgSend$calculateOverlapPercentageForPredictionWindowStartHour:predictionWindowEndHour:eventStartHour:eventEndHour:
+ _objc_msgSend$callCount
+ _objc_msgSend$checkNonzeroMedianScreentimeUsagePerHour:
+ _objc_msgSend$copyAndTrim:toWindowStartDate:returnAsMOEvent:
+ _objc_msgSend$countOccurenceOfEvents:forWindow:windowSize:checkTime:checkWeekday:addBuffer:checkOverlapPercentage:forFeature:
+ _objc_msgSend$deviceActivity
+ _objc_msgSend$downtimeEndHour
+ _objc_msgSend$downtimeStartHour
+ _objc_msgSend$engagementCount
+ _objc_msgSend$engagementCountBin1MidLookback
+ _objc_msgSend$engagementCountMidLookback
+ _objc_msgSend$extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:andDowntimeWindowEndHour:
+ _objc_msgSend$findOptimalDateWithPrediction:withPredictionProbabilityThreshold:
+ _objc_msgSend$firstScreentimeOfDay
+ _objc_msgSend$getCallStartDates:
+ _objc_msgSend$getMediaPlaySessionStartDates:
+ _objc_msgSend$getWeekday:
+ _objc_msgSend$healthandfitnessScreentimeCount
+ _objc_msgSend$healthandfitnessScreentimeCountMidLookback
+ _objc_msgSend$healthandfitnessScreentimeCountShortLookback
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithDowntimeStartHour:downtimeEndHour:hour:weekday:motionActivityCount:motionActivityCountShortLookback:motionActivityOverlapCountShortLookback:engagementCount:engagementCountMidLookback:engagementCountBin1MidLookback:healthandfitnessScreentimeCount:healthandfitnessScreentimeCountMidLookback:healthandfitnessScreentimeCountShortLookback:screentimeCount:screentimeSameWeekdayProbability:screentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:overMedianScreentimeSameWeekdayProbabilityShortLookback:over20MinScreentimeSameWeekdayProbability:over20MinScreentimeCountMidLookback:callCount:musicCount:musicCountShortLookback:atHomeCount:atHomeCountShortLookback:atWorkCount:atWorkSameWeekdayProbability:atWorkCountShortLookback:weekdayPrevScreentimeCount:firstScreentimeOfDay:lastScreentimeOfDay:isAfternoon:isEvening:isMorning:isNight:
+ _objc_msgSend$initWithName:sharedContainer:
+ _objc_msgSend$isAfternoon
+ _objc_msgSend$isEvening
+ _objc_msgSend$isNight
+ _objc_msgSend$lastScreentimeOfDay
+ _objc_msgSend$motionActivityCount
+ _objc_msgSend$motionActivityCountShortLookback
+ _objc_msgSend$motionActivityOverlapCountShortLookback
+ _objc_msgSend$musicCount
+ _objc_msgSend$musicCountShortLookback
+ _objc_msgSend$over20MinScreentimeCountMidLookback
+ _objc_msgSend$overMedianScreentimeSameWeekdayProbabilityShortLookback
+ _objc_msgSend$screentimeCount
+ _objc_msgSend$screentimeCountShortLookback
+ _objc_msgSend$screentimeSameWeekdayProbability
+ _objc_msgSend$setAllowedClients:
+ _symbolic So15NSRecursiveLockC
+ availabilityPredict061725.m
- +[availabilityPredict042425 URLOfModelInThisBundle]
- +[availabilityPredict042425 URLOfModelInThisBundle].cold.1
- +[availabilityPredict042425 loadContentsOfURL:configuration:completionHandler:]
- +[availabilityPredict042425 loadWithConfiguration:completionHandler:]
- -[MOAvailabilityPredictionManager countOccurenceOfEvents:forWindow:checkTime:checkWeekday:addBuffer:forFeature:]
- -[MOAvailabilityPredictionManager countOccurenceOfEvents:forWindow:checkTime:checkWeekday:addBuffer:forFeature:].cold.1
- -[MOAvailabilityPredictionManager extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:]
- -[MOAvailabilityPredictionManager findOptimalDateWithPrediction:]
- -[MOAvailabilityPredictionManager prevEngagementCountBin1FeatureScaleMean]
- -[MOAvailabilityPredictionManager prevEngagementCountBin1FeatureScaleStd]
- -[MOAvailabilityPredictionManager prevEngagementCountFeatureScaleMean]
- -[MOAvailabilityPredictionManager prevEngagementCountFeatureScaleStd]
- -[MOAvailabilityPredictionManager prevScreentimeCountFeatureScaleMean]
- -[MOAvailabilityPredictionManager prevScreentimeCountFeatureScaleStd]
- -[MOAvailabilityPredictionManager prevScreentimeCountShortLookbackFeatureScaleMean]
- -[MOAvailabilityPredictionManager prevScreentimeCountShortLookbackFeatureScaleStd]
- -[MOAvailabilityPredictionManager setPrevEngagementCountBin1FeatureScaleMean:]
- -[MOAvailabilityPredictionManager setPrevEngagementCountBin1FeatureScaleStd:]
- -[MOAvailabilityPredictionManager setPrevEngagementCountFeatureScaleMean:]
- -[MOAvailabilityPredictionManager setPrevEngagementCountFeatureScaleStd:]
- -[MOAvailabilityPredictionManager setPrevScreentimeCountFeatureScaleMean:]
- -[MOAvailabilityPredictionManager setPrevScreentimeCountFeatureScaleStd:]
- -[MOAvailabilityPredictionManager setPrevScreentimeCountShortLookbackFeatureScaleMean:]
- -[MOAvailabilityPredictionManager setPrevScreentimeCountShortLookbackFeatureScaleStd:]
- -[availabilityPredict042425 .cxx_destruct]
- -[availabilityPredict042425 initWithConfiguration:error:]
- -[availabilityPredict042425 initWithContentsOfURL:configuration:error:]
- -[availabilityPredict042425 initWithContentsOfURL:error:]
- -[availabilityPredict042425 initWithMLModel:]
- -[availabilityPredict042425 init]
- -[availabilityPredict042425 model]
- -[availabilityPredict042425 predictionFromFeatures:completionHandler:]
- -[availabilityPredict042425 predictionFromFeatures:error:]
- -[availabilityPredict042425 predictionFromFeatures:options:completionHandler:]
- -[availabilityPredict042425 predictionFromFeatures:options:error:]
- -[availabilityPredict042425 predictionFromSleepStartHour:hour:prevEngagementCount:prevEngagementCountBin1:prevScreentimeCount:prevScreentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:over20MinScreentimeSameWeekdayProbability:weekdayPrevScreentimeCount:isMorning:error:]
- -[availabilityPredict042425 predictionsFromInputs:options:error:]
- -[availabilityPredict042425Input featureNames]
- -[availabilityPredict042425Input featureValueForName:]
- -[availabilityPredict042425Input hour]
- -[availabilityPredict042425Input initWithSleepStartHour:hour:prevEngagementCount:prevEngagementCountBin1:prevScreentimeCount:prevScreentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:over20MinScreentimeSameWeekdayProbability:weekdayPrevScreentimeCount:isMorning:]
- -[availabilityPredict042425Input isMorning]
- -[availabilityPredict042425Input over20MinScreentimeSameWeekdayProbability]
- -[availabilityPredict042425Input overMedianScreentimeSameWeekdayProbability]
- -[availabilityPredict042425Input prevEngagementCountBin1]
- -[availabilityPredict042425Input prevEngagementCount]
- -[availabilityPredict042425Input prevScreentimeCountShortLookback]
- -[availabilityPredict042425Input prevScreentimeCount]
- -[availabilityPredict042425Input setHour:]
- -[availabilityPredict042425Input setIsMorning:]
- -[availabilityPredict042425Input setOver20MinScreentimeSameWeekdayProbability:]
- -[availabilityPredict042425Input setOverMedianScreentimeSameWeekdayProbability:]
- -[availabilityPredict042425Input setPrevEngagementCount:]
- -[availabilityPredict042425Input setPrevEngagementCountBin1:]
- -[availabilityPredict042425Input setPrevScreentimeCount:]
- -[availabilityPredict042425Input setPrevScreentimeCountShortLookback:]
- -[availabilityPredict042425Input setSleepStartHour:]
- -[availabilityPredict042425Input setWeekdayPrevScreentimeCount:]
- -[availabilityPredict042425Input sleepStartHour]
- -[availabilityPredict042425Input weekdayPrevScreentimeCount]
- -[availabilityPredict042425Output .cxx_destruct]
- -[availabilityPredict042425Output classProbability]
- -[availabilityPredict042425Output featureNames]
- -[availabilityPredict042425Output featureValueForName:]
- -[availabilityPredict042425Output initWithTarget:classProbability:]
- -[availabilityPredict042425Output setClassProbability:]
- -[availabilityPredict042425Output setTarget:]
- -[availabilityPredict042425Output target]
- /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/DerivedSources/CoreMLGenerated/availabilityPredict042425/
- /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/availabilityPredict042425.o
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevEngagementCountBin1FeatureScaleMean
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevEngagementCountBin1FeatureScaleStd
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevEngagementCountFeatureScaleMean
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevEngagementCountFeatureScaleStd
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevScreentimeCountFeatureScaleMean
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevScreentimeCountFeatureScaleStd
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevScreentimeCountShortLookbackFeatureScaleMean
- OBJC_IVAR_$_MOAvailabilityPredictionManager._prevScreentimeCountShortLookbackFeatureScaleStd
- OBJC_IVAR_$_availabilityPredict042425._model
- OBJC_IVAR_$_availabilityPredict042425Input._hour
- OBJC_IVAR_$_availabilityPredict042425Input._isMorning
- OBJC_IVAR_$_availabilityPredict042425Input._over20MinScreentimeSameWeekdayProbability
- OBJC_IVAR_$_availabilityPredict042425Input._overMedianScreentimeSameWeekdayProbability
- OBJC_IVAR_$_availabilityPredict042425Input._prevEngagementCount
- OBJC_IVAR_$_availabilityPredict042425Input._prevEngagementCountBin1
- OBJC_IVAR_$_availabilityPredict042425Input._prevScreentimeCount
- OBJC_IVAR_$_availabilityPredict042425Input._prevScreentimeCountShortLookback
- OBJC_IVAR_$_availabilityPredict042425Input._sleepStartHour
- OBJC_IVAR_$_availabilityPredict042425Input._weekdayPrevScreentimeCount
- OBJC_IVAR_$_availabilityPredict042425Output._classProbability
- OBJC_IVAR_$_availabilityPredict042425Output._target
- _CFRunLoopRun
- _OBJC_CLASS_$_availabilityPredict042425
- _OBJC_CLASS_$_availabilityPredict042425Input
- _OBJC_CLASS_$_availabilityPredict042425Output
- _OBJC_METACLASS_$_availabilityPredict042425
- _OBJC_METACLASS_$_availabilityPredict042425Input
- _OBJC_METACLASS_$_availabilityPredict042425Output
- __101-[MOEngagementHistoryManager writeEngagementLightStreamForDevices:storedBookmarks:completionHandler:]_block_invoke.505
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.227
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.227.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.233
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.233.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.245
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.245.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.251
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.251.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.257
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.257.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.263
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.263.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.263.cold.2
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.267
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.268
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.272
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.279
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.279.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.285
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.285.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.291
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.291.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.297
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.297.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.301
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.301.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.305
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.305.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.228
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.234
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.240
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.246
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.252
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.258
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.273
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.280
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.286
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.292
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.298
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.229
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.235
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.241
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.247
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.253
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.259
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.274
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.281
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.287
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.293
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.299
- __23-[MODaemonUniverse run]_block_invoke.23
- __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1931
- __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.606
- __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.349
- __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.668
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.445
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.445.cold.1
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.446
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.456
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.457
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.457.cold.1
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.448
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.448.cold.1
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.449
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.356
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.360
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.364
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.374
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.384
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.388
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.392
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.396
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.400
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.404
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.408
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.412
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.416
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.503
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.505
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.505.cold.1
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.318
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.319
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.320
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.463
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.479
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.479.cold.1
- __61-[MOAvailabilityPredictionManager saveEligiblePOICategories:]_block_invoke.441
- __61-[MOAvailabilityPredictionManager saveEligiblePOICategories:]_block_invoke.441.cold.1
- __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.675
- __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.677
- __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.652
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.432
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.432.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.439
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.439.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.446
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.446.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.450
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.450.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.451
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.451.cold.1
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.197
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.197.cold.1
- __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.199
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.682
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.692
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.707
- __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.454
- __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.672
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.658
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.658.cold.1
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.659
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.659.cold.1
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.675
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.676
- __84-[MOEngagementHistoryManager updateEngagementLightStreamWithRefreshVariant:handler:]_block_invoke.538
- __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.328
- __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.482
- __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.483
- __OBJC_$_CLASS_METHODS_availabilityPredict042425
- __OBJC_$_INSTANCE_METHODS_availabilityPredict042425
- __OBJC_$_INSTANCE_METHODS_availabilityPredict042425Input
- __OBJC_$_INSTANCE_METHODS_availabilityPredict042425Output
- __OBJC_$_INSTANCE_VARIABLES_availabilityPredict042425
- __OBJC_$_INSTANCE_VARIABLES_availabilityPredict042425Input
- __OBJC_$_INSTANCE_VARIABLES_availabilityPredict042425Output
- __OBJC_$_PROP_LIST_availabilityPredict042425
- __OBJC_$_PROP_LIST_availabilityPredict042425Input
- __OBJC_$_PROP_LIST_availabilityPredict042425Output
- __OBJC_CLASS_PROTOCOLS_$_availabilityPredict042425Input
- __OBJC_CLASS_PROTOCOLS_$_availabilityPredict042425Output
- __OBJC_CLASS_RO_$_availabilityPredict042425
- __OBJC_CLASS_RO_$_availabilityPredict042425Input
- __OBJC_CLASS_RO_$_availabilityPredict042425Output
- __OBJC_METACLASS_RO_$_availabilityPredict042425
- __OBJC_METACLASS_RO_$_availabilityPredict042425Input
- __OBJC_METACLASS_RO_$_availabilityPredict042425Output
- ___70-[availabilityPredict042425 predictionFromFeatures:completionHandler:]_block_invoke
- ___78-[availabilityPredict042425 predictionFromFeatures:options:completionHandler:]_block_invoke
- ___79+[availabilityPredict042425 loadContentsOfURL:configuration:completionHandler:]_block_invoke
- __block_literal_global.25
- __block_literal_global.428
- __block_literal_global.430
- __block_literal_global.432
- __block_literal_global.434
- __block_literal_global.493
- __block_literal_global.498
- __block_literal_global.501
- __block_literal_global.522
- __block_literal_global.526
- __block_literal_global.534
- __block_literal_global.600
- __dispatch_main_q
- _kAPMPrevEngagementCountBin1FeatureScaleMeanKey
- _kAPMPrevEngagementCountBin1FeatureScaleStdKey
- _kAPMPrevEngagementCountFeatureScaleMeanKey
- _kAPMPrevEngagementCountFeatureScaleStdKey
- _kAPMPrevScreentimeCountFeatureScaleMeanKey
- _kAPMPrevScreentimeCountFeatureScaleStdKey
- _kAPMPrevScreentimeCountShortLookbackFeatureScaleMeanKey
- _kAPMPrevScreentimeCountShortLookbackFeatureScaleStdKey
- _objc_msgSend$countOccurenceOfEvents:forWindow:checkTime:checkWeekday:addBuffer:forFeature:
- _objc_msgSend$extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:
- _objc_msgSend$findOptimalDateWithPrediction:
- _objc_msgSend$initWithSleepStartHour:hour:prevEngagementCount:prevEngagementCountBin1:prevScreentimeCount:prevScreentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:over20MinScreentimeSameWeekdayProbability:weekdayPrevScreentimeCount:isMorning:
- _objc_msgSend$prevEngagementCount
- _objc_msgSend$prevEngagementCountBin1
- _objc_msgSend$prevScreentimeCount
- _objc_msgSend$prevScreentimeCountShortLookback
- _objc_msgSend$sleepStartHour
- availabilityPredict042425.m
CStrings:
+ " hour %@: %@"
+ "(category == %d) AND (placeUserType == %d) AND (provider == %d)"
+ "(provider != %d)"
+ "@296@0:8d16d24d32d40d48d56d64d72d80d88d96d104d112d120d128d136d144d152d160d168d176d184d192d200d208d216d224d232d240d248d256d264d272d280d288"
+ "@304@0:8d16d24d32d40d48d56d64d72d80d88d96d104d112d120d128d136d144d152d160d168d176d184d192d200d208d216d224d232d240d248d256d264d272d280d288^@296"
+ "@72@0:8@16@24@32@40@48d56d64"
+ "@distinctUnionOfObjects.hour"
+ "ANY screenTimeEvent.appCategoryUsages.appCategory == %d"
+ "APMAtHomeCountFeatureScaleMeanKey"
+ "APMAtHomeCountFeatureScaleStdKey"
+ "APMAtHomeCountShortLookbackFeatureScaleMeanKey"
+ "APMAtHomeCountShortLookbackFeatureScaleStdKey"
+ "APMAtWorkCountFeatureScaleMeanKey"
+ "APMAtWorkCountFeatureScaleStdKey"
+ "APMAtWorkCountShortLookbackFeatureScaleMeanKey"
+ "APMAtWorkCountShortLookbackFeatureScaleStdKey"
+ "APMAtWorkSameWeekdayProbabilityFeatureScaleMeanKey"
+ "APMAtWorkSameWeekdayProbabilityFeatureScaleStdKey"
+ "APMCallCountFeatureScaleMeanKey"
+ "APMCallCountFeatureScaleStdKey"
+ "APMDowntimeEndHourFeatureScaleMeanKey"
+ "APMDowntimeEndHourFeatureScaleStdKey"
+ "APMEngagementCountBin1MidLookbackFeatureScaleMeanKey"
+ "APMEngagementCountBin1MidLookbackFeatureScaleStdKey"
+ "APMEngagementCountFeatureScaleMeanKey"
+ "APMEngagementCountFeatureScaleStdKey"
+ "APMEngagementCountMidLookbackFeatureScaleMeanKey"
+ "APMEngagementCountMidLookbackFeatureScaleStdKey"
+ "APMFirstScreentimeOfDayFeatureScaleMeanKey"
+ "APMFirstScreentimeOfDayFeatureScaleStdKey"
+ "APMHealthandfitnessScreentimeCountFeatureScaleMeanKey"
+ "APMHealthandfitnessScreentimeCountFeatureScaleStdKey"
+ "APMHealthandfitnessScreentimeCountMidLookbackFeatureScaleMeanKey"
+ "APMHealthandfitnessScreentimeCountMidLookbackFeatureScaleStdKey"
+ "APMHealthandfitnessScreentimeCountShortLookbackFeatureScaleMeanKey"
+ "APMHealthandfitnessScreentimeCountShortLookbackFeatureScaleStdKey"
+ "APMIsAfternoonFeatureScaleMeanKey"
+ "APMIsAfternoonFeatureScaleStdKey"
+ "APMIsEveningFeatureScaleMeanKey"
+ "APMIsEveningFeatureScaleStdKey"
+ "APMIsNightFeatureScaleMeanKey"
+ "APMIsNightFeatureScaleStdKey"
+ "APMLastScreentimeOfDayFeatureScaleMeanKey"
+ "APMLastScreentimeOfDayFeatureScaleStdKey"
+ "APMMotionActivityCountFeatureScaleMeanKey"
+ "APMMotionActivityCountFeatureScaleStdKey"
+ "APMMotionActivityCountShortLookbackFeatureScaleMeanKey"
+ "APMMotionActivityCountShortLookbackFeatureScaleStdKey"
+ "APMMotionActivityOverlapCountShortLookbackFeatureScaleMeanKey"
+ "APMMotionActivityOverlapCountShortLookbackFeatureScaleStdKey"
+ "APMMusicCountFeatureScaleMeanKey"
+ "APMMusicCountFeatureScaleStdKey"
+ "APMMusicCountShortLookbackFeatureScaleMeanKey"
+ "APMMusicCountShortLookbackFeatureScaleStdKey"
+ "APMOver20MinScreentimeCountMidLookbackFeatureScaleMeanKey"
+ "APMOver20MinScreentimeCountMidLookbackFeatureScaleStdKey"
+ "APMOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMeanKey"
+ "APMOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStdKey"
+ "APMScreentimeCountFeatureScaleMeanKey"
+ "APMScreentimeCountFeatureScaleStdKey"
+ "APMScreentimeCountShortLookbackFeatureScaleMeanKey"
+ "APMScreentimeCountShortLookbackFeatureScaleStdKey"
+ "APMScreentimeSameWeekdayProbabilityFeatureScaleMeanKey"
+ "APMScreentimeSameWeekdayProbabilityFeatureScaleStdKey"
+ "APMWeekdayFeatureScaleMeanKey"
+ "APMWeekdayFeatureScaleStdKey"
+ "AvailabilityPredictionProbabilityInsufficientScreentimeThresholdKey"
+ "Could not load availabilityPredict061725.mlmodelc in the bundle resource"
+ "Device activity in ManagedSettings is already registered for %@"
+ "DeviceActivityStore"
+ "DowntimeDetectionDefaultSleepEndHourKey"
+ "DowntimeDetectionWindowEndHourUserHistoricalDefault"
+ "ManagedSettings store device activity is not registered for: %@, updating allow list"
+ "ProcessingLastSuccessfulRunDate"
+ "SpotlightEventIntegrationEnablement"
+ "SubAdministrativeArea"
+ "Td,N,V_atHomeCount"
+ "Td,N,V_atHomeCountFeatureScaleMean"
+ "Td,N,V_atHomeCountFeatureScaleStd"
+ "Td,N,V_atHomeCountShortLookback"
+ "Td,N,V_atHomeCountShortLookbackFeatureScaleMean"
+ "Td,N,V_atHomeCountShortLookbackFeatureScaleStd"
+ "Td,N,V_atWorkCount"
+ "Td,N,V_atWorkCountFeatureScaleMean"
+ "Td,N,V_atWorkCountFeatureScaleStd"
+ "Td,N,V_atWorkCountShortLookback"
+ "Td,N,V_atWorkCountShortLookbackFeatureScaleMean"
+ "Td,N,V_atWorkCountShortLookbackFeatureScaleStd"
+ "Td,N,V_atWorkSameWeekdayProbability"
+ "Td,N,V_atWorkSameWeekdayProbabilityFeatureScaleMean"
+ "Td,N,V_atWorkSameWeekdayProbabilityFeatureScaleStd"
+ "Td,N,V_availabilityPredictionProbabilityInsufficientScreentimeThreshold"
+ "Td,N,V_callCount"
+ "Td,N,V_callCountFeatureScaleMean"
+ "Td,N,V_callCountFeatureScaleStd"
+ "Td,N,V_downtimeDetectionDefaultSleepEndHour"
+ "Td,N,V_downtimeEndHour"
+ "Td,N,V_downtimeEndHourFeatureScaleMean"
+ "Td,N,V_downtimeEndHourFeatureScaleStd"
+ "Td,N,V_downtimeStartHour"
+ "Td,N,V_engagementCount"
+ "Td,N,V_engagementCountBin1MidLookback"
+ "Td,N,V_engagementCountBin1MidLookbackFeatureScaleMean"
+ "Td,N,V_engagementCountBin1MidLookbackFeatureScaleStd"
+ "Td,N,V_engagementCountFeatureScaleMean"
+ "Td,N,V_engagementCountFeatureScaleStd"
+ "Td,N,V_engagementCountMidLookback"
+ "Td,N,V_engagementCountMidLookbackFeatureScaleMean"
+ "Td,N,V_engagementCountMidLookbackFeatureScaleStd"
+ "Td,N,V_firstScreentimeOfDay"
+ "Td,N,V_firstScreentimeOfDayFeatureScaleMean"
+ "Td,N,V_firstScreentimeOfDayFeatureScaleStd"
+ "Td,N,V_healthandfitnessScreentimeCount"
+ "Td,N,V_healthandfitnessScreentimeCountFeatureScaleMean"
+ "Td,N,V_healthandfitnessScreentimeCountFeatureScaleStd"
+ "Td,N,V_healthandfitnessScreentimeCountMidLookback"
+ "Td,N,V_healthandfitnessScreentimeCountMidLookbackFeatureScaleMean"
+ "Td,N,V_healthandfitnessScreentimeCountMidLookbackFeatureScaleStd"
+ "Td,N,V_healthandfitnessScreentimeCountShortLookback"
+ "Td,N,V_healthandfitnessScreentimeCountShortLookbackFeatureScaleMean"
+ "Td,N,V_healthandfitnessScreentimeCountShortLookbackFeatureScaleStd"
+ "Td,N,V_isAfternoon"
+ "Td,N,V_isAfternoonFeatureScaleMean"
+ "Td,N,V_isAfternoonFeatureScaleStd"
+ "Td,N,V_isEvening"
+ "Td,N,V_isEveningFeatureScaleMean"
+ "Td,N,V_isEveningFeatureScaleStd"
+ "Td,N,V_isNight"
+ "Td,N,V_isNightFeatureScaleMean"
+ "Td,N,V_isNightFeatureScaleStd"
+ "Td,N,V_lastScreentimeOfDay"
+ "Td,N,V_lastScreentimeOfDayFeatureScaleMean"
+ "Td,N,V_lastScreentimeOfDayFeatureScaleStd"
+ "Td,N,V_motionActivityCount"
+ "Td,N,V_motionActivityCountFeatureScaleMean"
+ "Td,N,V_motionActivityCountFeatureScaleStd"
+ "Td,N,V_motionActivityCountShortLookback"
+ "Td,N,V_motionActivityCountShortLookbackFeatureScaleMean"
+ "Td,N,V_motionActivityCountShortLookbackFeatureScaleStd"
+ "Td,N,V_motionActivityOverlapCountShortLookback"
+ "Td,N,V_motionActivityOverlapCountShortLookbackFeatureScaleMean"
+ "Td,N,V_motionActivityOverlapCountShortLookbackFeatureScaleStd"
+ "Td,N,V_musicCount"
+ "Td,N,V_musicCountFeatureScaleMean"
+ "Td,N,V_musicCountFeatureScaleStd"
+ "Td,N,V_musicCountShortLookback"
+ "Td,N,V_musicCountShortLookbackFeatureScaleMean"
+ "Td,N,V_musicCountShortLookbackFeatureScaleStd"
+ "Td,N,V_over20MinScreentimeCountMidLookback"
+ "Td,N,V_over20MinScreentimeCountMidLookbackFeatureScaleMean"
+ "Td,N,V_over20MinScreentimeCountMidLookbackFeatureScaleStd"
+ "Td,N,V_overMedianScreentimeSameWeekdayProbabilityShortLookback"
+ "Td,N,V_overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean"
+ "Td,N,V_overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd"
+ "Td,N,V_screentimeCount"
+ "Td,N,V_screentimeCountFeatureScaleMean"
+ "Td,N,V_screentimeCountFeatureScaleStd"
+ "Td,N,V_screentimeCountShortLookback"
+ "Td,N,V_screentimeCountShortLookbackFeatureScaleMean"
+ "Td,N,V_screentimeCountShortLookbackFeatureScaleStd"
+ "Td,N,V_screentimeSameWeekdayProbability"
+ "Td,N,V_screentimeSameWeekdayProbabilityFeatureScaleMean"
+ "Td,N,V_screentimeSameWeekdayProbabilityFeatureScaleStd"
+ "Td,N,V_weekday"
+ "Td,N,V_weekdayFeatureScaleMean"
+ "Td,N,V_weekdayFeatureScaleStd"
+ "[APM] %@: found significant time overlap (above 50%% threshold) with event with startDate %@ endDate %@ for window %@; checkHour %d, checkWeekday %d, addBuffer %d"
+ "[APM] Downtime detection using personalized default end hour: %f"
+ "[APM] Downtime detection using population default end hour: %f"
+ "[APM] Extracted feature array after scaling: [downtimeStartHour:%.5f, downtimeEndHour:%.5f, hour:%.5f, weekday:%.5f, motionActivityCount:%.5f, motionActivityCountShortLookback:%.5f, motionActivityOverlapCountShortLookback:%.5f, engagementCount:%.5f, engagementCountMidLookback:%.5f, engagementCountBin1MidLookback:%.5f, healthandfitnessScreentimeCount:%.5f, healthandfitnessScreentimeCountMidLookback:%.5f, healthandfitnessScreentimeCountShortLookback:%.5f, screentimeCount:%.5f, screentimeSameWeekdayProbability:%.5f, screentimeCountShortLookback:%.5f, overMedianScreentimeSameWeekdayProbability:%.5f, overMedianScreentimeSameWeekdayProbabilityShortLookback:%.5f, over20MinScreentimeSameWeekdayProbability:%.5f, over20MinScreentimeCountMidLookback:%.5f, callCount:%.5f, musicCount:%.5f, musicCountShortLookback:%.5f, atHomeCount:%.5f, atHomeCountShortLookback:%.5f, atWorkCount:%.5f, atWorkSameWeekdayProbability:%.5f, atWorkCountShortLookback:%.5f, weekdayPrevScreentimeCount:%.5f, firstScreentimeOfDay:%.5f, lastScreentimeOfDay:%.5f, isAfternoon:%.5f, isEvening:%.5f, isMorning:%.5f, isNight:%.5f] for window %@"
+ "[APM] Extracted feature array before scaling: [downtimeStartHour:%.5f, downtimeEndHour:%.5f, hour:%.5f, weekday:%.5f, motionActivityCount:%.5f, motionActivityCountShortLookback:%.5f, motionActivityOverlapCountShortLookback:%.5f, engagementCount:%.5f, engagementCountMidLookback:%.5f, engagementCountBin1MidLookback:%.5f, healthandfitnessScreentimeCount:%.5f, healthandfitnessScreentimeCountMidLookback:%.5f, healthandfitnessScreentimeCountShortLookback:%.5f, screentimeCount:%.5f, screentimeSameWeekdayProbability:%.5f, screentimeCountShortLookback:%.5f, overMedianScreentimeSameWeekdayProbability:%.5f, overMedianScreentimeSameWeekdayProbabilityShortLookback:%.5f, over20MinScreentimeSameWeekdayProbability:%.5f, over20MinScreentimeCountMidLookback:%.5f, callCount:%.5f, musicCount:%.5f, musicCountShortLookback:%.5f, atHomeCount:%.5f, atHomeCountShortLookback:%.5f, atWorkCount:%.5f, atWorkSameWeekdayProbability:%.5f, atWorkCountShortLookback:%.5f, weekdayPrevScreentimeCount:%.5f, firstScreentimeOfDay:%.5f, lastScreentimeOfDay:%.5f, isAfternoon:%.5f, isEvening:%.5f, isMorning:%.5f, isNight:%.5f] for window %@"
+ "[APM] Screentime usage nonzero median check: %@"
+ "_atHomeCount"
+ "_atHomeCountFeatureScaleMean"
+ "_atHomeCountFeatureScaleStd"
+ "_atHomeCountShortLookback"
+ "_atHomeCountShortLookbackFeatureScaleMean"
+ "_atHomeCountShortLookbackFeatureScaleStd"
+ "_atWorkCount"
+ "_atWorkCountFeatureScaleMean"
+ "_atWorkCountFeatureScaleStd"
+ "_atWorkCountShortLookback"
+ "_atWorkCountShortLookbackFeatureScaleMean"
+ "_atWorkCountShortLookbackFeatureScaleStd"
+ "_atWorkSameWeekdayProbability"
+ "_atWorkSameWeekdayProbabilityFeatureScaleMean"
+ "_atWorkSameWeekdayProbabilityFeatureScaleStd"
+ "_availabilityPredictionProbabilityInsufficientScreentimeThreshold"
+ "_callCount"
+ "_callCountFeatureScaleMean"
+ "_callCountFeatureScaleStd"
+ "_downtimeDetectionDefaultSleepEndHour"
+ "_downtimeEndHour"
+ "_downtimeEndHourFeatureScaleMean"
+ "_downtimeEndHourFeatureScaleStd"
+ "_downtimeStartHour"
+ "_engagementCount"
+ "_engagementCountBin1MidLookback"
+ "_engagementCountBin1MidLookbackFeatureScaleMean"
+ "_engagementCountBin1MidLookbackFeatureScaleStd"
+ "_engagementCountFeatureScaleMean"
+ "_engagementCountFeatureScaleStd"
+ "_engagementCountMidLookback"
+ "_engagementCountMidLookbackFeatureScaleMean"
+ "_engagementCountMidLookbackFeatureScaleStd"
+ "_firstScreentimeOfDay"
+ "_firstScreentimeOfDayFeatureScaleMean"
+ "_firstScreentimeOfDayFeatureScaleStd"
+ "_healthandfitnessScreentimeCount"
+ "_healthandfitnessScreentimeCountFeatureScaleMean"
+ "_healthandfitnessScreentimeCountFeatureScaleStd"
+ "_healthandfitnessScreentimeCountMidLookback"
+ "_healthandfitnessScreentimeCountMidLookbackFeatureScaleMean"
+ "_healthandfitnessScreentimeCountMidLookbackFeatureScaleStd"
+ "_healthandfitnessScreentimeCountShortLookback"
+ "_healthandfitnessScreentimeCountShortLookbackFeatureScaleMean"
+ "_healthandfitnessScreentimeCountShortLookbackFeatureScaleStd"
+ "_isAfternoon"
+ "_isAfternoonFeatureScaleMean"
+ "_isAfternoonFeatureScaleStd"
+ "_isEvening"
+ "_isEveningFeatureScaleMean"
+ "_isEveningFeatureScaleStd"
+ "_isNight"
+ "_isNightFeatureScaleMean"
+ "_isNightFeatureScaleStd"
+ "_lastScreentimeOfDay"
+ "_lastScreentimeOfDayFeatureScaleMean"
+ "_lastScreentimeOfDayFeatureScaleStd"
+ "_motionActivityCount"
+ "_motionActivityCountFeatureScaleMean"
+ "_motionActivityCountFeatureScaleStd"
+ "_motionActivityCountShortLookback"
+ "_motionActivityCountShortLookbackFeatureScaleMean"
+ "_motionActivityCountShortLookbackFeatureScaleStd"
+ "_motionActivityOverlapCountShortLookback"
+ "_motionActivityOverlapCountShortLookbackFeatureScaleMean"
+ "_motionActivityOverlapCountShortLookbackFeatureScaleStd"
+ "_musicCount"
+ "_musicCountFeatureScaleMean"
+ "_musicCountFeatureScaleStd"
+ "_musicCountShortLookback"
+ "_musicCountShortLookbackFeatureScaleMean"
+ "_musicCountShortLookbackFeatureScaleStd"
+ "_over20MinScreentimeCountMidLookback"
+ "_over20MinScreentimeCountMidLookbackFeatureScaleMean"
+ "_over20MinScreentimeCountMidLookbackFeatureScaleStd"
+ "_overMedianScreentimeSameWeekdayProbabilityShortLookback"
+ "_overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean"
+ "_overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd"
+ "_registerForDeviceActivity"
+ "_screentimeCount"
+ "_screentimeCountFeatureScaleMean"
+ "_screentimeCountFeatureScaleStd"
+ "_screentimeCountShortLookback"
+ "_screentimeCountShortLookbackFeatureScaleMean"
+ "_screentimeCountShortLookbackFeatureScaleStd"
+ "_screentimeSameWeekdayProbability"
+ "_screentimeSameWeekdayProbabilityFeatureScaleMean"
+ "_screentimeSameWeekdayProbabilityFeatureScaleStd"
+ "_weekday"
+ "_weekdayFeatureScaleMean"
+ "_weekdayFeatureScaleStd"
+ "allowedClients"
+ "atHomeCount"
+ "atHomeCountFeatureScaleMean"
+ "atHomeCountFeatureScaleStd"
+ "atHomeCountShortLookback"
+ "atHomeCountShortLookbackFeatureScaleMean"
+ "atHomeCountShortLookbackFeatureScaleStd"
+ "atWorkCount"
+ "atWorkCountFeatureScaleMean"
+ "atWorkCountFeatureScaleStd"
+ "atWorkCountShortLookback"
+ "atWorkCountShortLookbackFeatureScaleMean"
+ "atWorkCountShortLookbackFeatureScaleStd"
+ "atWorkSameWeekdayProbability"
+ "atWorkSameWeekdayProbabilityFeatureScaleMean"
+ "atWorkSameWeekdayProbabilityFeatureScaleStd"
+ "availabilityPredict061725"
+ "availabilityPredict061725Input"
+ "availabilityPredict061725Output"
+ "availabilityPredictionProbabilityInsufficientScreentimeThreshold"
+ "bookmark database is not available"
+ "calculateOverlapPercentageForPredictionWindowStartHour:predictionWindowEndHour:eventStartHour:eventEndHour:"
+ "callCountFeatureScaleMean"
+ "callCountFeatureScaleStd"
+ "checkNonzeroMedianScreentimeUsagePerHour:"
+ "copyAndTrim:toWindowStartDate:returnAsMOEvent:"
+ "countOccurenceOfEvents:forWindow:windowSize:checkTime:checkWeekday:addBuffer:checkOverlapPercentage:forFeature:"
+ "d60@0:8@16@24i32B36B40B44B48@52"
+ "deviceActivity"
+ "downtimeDetectionDefaultSleepEndHour"
+ "downtimeEndHour"
+ "downtimeEndHourFeatureScaleMean"
+ "downtimeEndHourFeatureScaleStd"
+ "downtimeStartHour"
+ "engagementCount"
+ "engagementCountBin1MidLookback"
+ "engagementCountBin1MidLookbackFeatureScaleMean"
+ "engagementCountBin1MidLookbackFeatureScaleStd"
+ "engagementCountFeatureScaleMean"
+ "engagementCountFeatureScaleStd"
+ "engagementCountMidLookback"
+ "engagementCountMidLookbackFeatureScaleMean"
+ "engagementCountMidLookbackFeatureScaleStd"
+ "extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:andDowntimeWindowEndHour:"
+ "findOptimalDateWithPrediction:withPredictionProbabilityThreshold:"
+ "firstScreentimeOfDay"
+ "firstScreentimeOfDayFeatureScaleMean"
+ "firstScreentimeOfDayFeatureScaleStd"
+ "getMediaPlaySessionStartDates:"
+ "getWeekday:"
+ "healthandfitnessScreentimeCount"
+ "healthandfitnessScreentimeCountFeatureScaleMean"
+ "healthandfitnessScreentimeCountFeatureScaleStd"
+ "healthandfitnessScreentimeCountMidLookback"
+ "healthandfitnessScreentimeCountMidLookbackFeatureScaleMean"
+ "healthandfitnessScreentimeCountMidLookbackFeatureScaleStd"
+ "healthandfitnessScreentimeCountShortLookback"
+ "healthandfitnessScreentimeCountShortLookbackFeatureScaleMean"
+ "healthandfitnessScreentimeCountShortLookbackFeatureScaleStd"
+ "initWithBundleIdentifier:"
+ "initWithDowntimeStartHour:downtimeEndHour:hour:weekday:motionActivityCount:motionActivityCountShortLookback:motionActivityOverlapCountShortLookback:engagementCount:engagementCountMidLookback:engagementCountBin1MidLookback:healthandfitnessScreentimeCount:healthandfitnessScreentimeCountMidLookback:healthandfitnessScreentimeCountShortLookback:screentimeCount:screentimeSameWeekdayProbability:screentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:overMedianScreentimeSameWeekdayProbabilityShortLookback:over20MinScreentimeSameWeekdayProbability:over20MinScreentimeCountMidLookback:callCount:musicCount:musicCountShortLookback:atHomeCount:atHomeCountShortLookback:atWorkCount:atWorkSameWeekdayProbability:atWorkCountShortLookback:weekdayPrevScreentimeCount:firstScreentimeOfDay:lastScreentimeOfDay:isAfternoon:isEvening:isMorning:isNight:"
+ "initWithName:sharedContainer:"
+ "isAfternoon"
+ "isAfternoonFeatureScaleMean"
+ "isAfternoonFeatureScaleStd"
+ "isEvening"
+ "isEveningFeatureScaleMean"
+ "isEveningFeatureScaleStd"
+ "isNight"
+ "isNightFeatureScaleMean"
+ "isNightFeatureScaleStd"
+ "lastScreentimeOfDay"
+ "lastScreentimeOfDayFeatureScaleMean"
+ "lastScreentimeOfDayFeatureScaleStd"
+ "latestViewedEngagmentDateFrom:to:"
+ "motionActivityCount"
+ "motionActivityCountFeatureScaleMean"
+ "motionActivityCountFeatureScaleStd"
+ "motionActivityCountShortLookback"
+ "motionActivityCountShortLookbackFeatureScaleMean"
+ "motionActivityCountShortLookbackFeatureScaleStd"
+ "motionActivityOverlapCountShortLookback"
+ "motionActivityOverlapCountShortLookbackFeatureScaleMean"
+ "motionActivityOverlapCountShortLookbackFeatureScaleStd"
+ "musicCount"
+ "musicCountFeatureScaleMean"
+ "musicCountFeatureScaleStd"
+ "musicCountShortLookback"
+ "musicCountShortLookbackFeatureScaleMean"
+ "musicCountShortLookbackFeatureScaleStd"
+ "nonzeroMedianCheck"
+ "nonzeroMedianCheck == YES"
+ "over20MinScreentimeCountMidLookback"
+ "over20MinScreentimeCountMidLookbackFeatureScaleMean"
+ "over20MinScreentimeCountMidLookbackFeatureScaleStd"
+ "overMedianScreentimeSameWeekdayProbabilityShortLookback"
+ "overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean"
+ "overMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd"
+ "predictionFromDowntimeStartHour:downtimeEndHour:hour:weekday:motionActivityCount:motionActivityCountShortLookback:motionActivityOverlapCountShortLookback:engagementCount:engagementCountMidLookback:engagementCountBin1MidLookback:healthandfitnessScreentimeCount:healthandfitnessScreentimeCountMidLookback:healthandfitnessScreentimeCountShortLookback:screentimeCount:screentimeSameWeekdayProbability:screentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:overMedianScreentimeSameWeekdayProbabilityShortLookback:over20MinScreentimeSameWeekdayProbability:over20MinScreentimeCountMidLookback:callCount:musicCount:musicCountShortLookback:atHomeCount:atHomeCountShortLookback:atWorkCount:atWorkSameWeekdayProbability:atWorkCountShortLookback:weekdayPrevScreentimeCount:firstScreentimeOfDay:lastScreentimeOfDay:isAfternoon:isEvening:isMorning:isNight:error:"
+ "screentimeCount"
+ "screentimeCountFeatureScaleMean"
+ "screentimeCountFeatureScaleStd"
+ "screentimeCountShortLookback"
+ "screentimeCountShortLookbackFeatureScaleMean"
+ "screentimeCountShortLookbackFeatureScaleStd"
+ "screentimeSameWeekdayProbability"
+ "screentimeSameWeekdayProbabilityFeatureScaleMean"
+ "screentimeSameWeekdayProbabilityFeatureScaleStd"
+ "setAllowedClients:"
+ "setAtHomeCount:"
+ "setAtHomeCountFeatureScaleMean:"
+ "setAtHomeCountFeatureScaleStd:"
+ "setAtHomeCountShortLookback:"
+ "setAtHomeCountShortLookbackFeatureScaleMean:"
+ "setAtHomeCountShortLookbackFeatureScaleStd:"
+ "setAtWorkCount:"
+ "setAtWorkCountFeatureScaleMean:"
+ "setAtWorkCountFeatureScaleStd:"
+ "setAtWorkCountShortLookback:"
+ "setAtWorkCountShortLookbackFeatureScaleMean:"
+ "setAtWorkCountShortLookbackFeatureScaleStd:"
+ "setAtWorkSameWeekdayProbability:"
+ "setAtWorkSameWeekdayProbabilityFeatureScaleMean:"
+ "setAtWorkSameWeekdayProbabilityFeatureScaleStd:"
+ "setAvailabilityPredictionProbabilityInsufficientScreentimeThreshold:"
+ "setCallCount:"
+ "setCallCountFeatureScaleMean:"
+ "setCallCountFeatureScaleStd:"
+ "setDowntimeDetectionDefaultSleepEndHour:"
+ "setDowntimeEndHour:"
+ "setDowntimeEndHourFeatureScaleMean:"
+ "setDowntimeEndHourFeatureScaleStd:"
+ "setDowntimeStartHour:"
+ "setEngagementCount:"
+ "setEngagementCountBin1MidLookback:"
+ "setEngagementCountBin1MidLookbackFeatureScaleMean:"
+ "setEngagementCountBin1MidLookbackFeatureScaleStd:"
+ "setEngagementCountFeatureScaleMean:"
+ "setEngagementCountFeatureScaleStd:"
+ "setEngagementCountMidLookback:"
+ "setEngagementCountMidLookbackFeatureScaleMean:"
+ "setEngagementCountMidLookbackFeatureScaleStd:"
+ "setFirstScreentimeOfDay:"
+ "setFirstScreentimeOfDayFeatureScaleMean:"
+ "setFirstScreentimeOfDayFeatureScaleStd:"
+ "setHealthandfitnessScreentimeCount:"
+ "setHealthandfitnessScreentimeCountFeatureScaleMean:"
+ "setHealthandfitnessScreentimeCountFeatureScaleStd:"
+ "setHealthandfitnessScreentimeCountMidLookback:"
+ "setHealthandfitnessScreentimeCountMidLookbackFeatureScaleMean:"
+ "setHealthandfitnessScreentimeCountMidLookbackFeatureScaleStd:"
+ "setHealthandfitnessScreentimeCountShortLookback:"
+ "setHealthandfitnessScreentimeCountShortLookbackFeatureScaleMean:"
+ "setHealthandfitnessScreentimeCountShortLookbackFeatureScaleStd:"
+ "setIsAfternoon:"
+ "setIsAfternoonFeatureScaleMean:"
+ "setIsAfternoonFeatureScaleStd:"
+ "setIsEvening:"
+ "setIsEveningFeatureScaleMean:"
+ "setIsEveningFeatureScaleStd:"
+ "setIsNight:"
+ "setIsNightFeatureScaleMean:"
+ "setIsNightFeatureScaleStd:"
+ "setLastScreentimeOfDay:"
+ "setLastScreentimeOfDayFeatureScaleMean:"
+ "setLastScreentimeOfDayFeatureScaleStd:"
+ "setMotionActivityCount:"
+ "setMotionActivityCountFeatureScaleMean:"
+ "setMotionActivityCountFeatureScaleStd:"
+ "setMotionActivityCountShortLookback:"
+ "setMotionActivityCountShortLookbackFeatureScaleMean:"
+ "setMotionActivityCountShortLookbackFeatureScaleStd:"
+ "setMotionActivityOverlapCountShortLookback:"
+ "setMotionActivityOverlapCountShortLookbackFeatureScaleMean:"
+ "setMotionActivityOverlapCountShortLookbackFeatureScaleStd:"
+ "setMusicCount:"
+ "setMusicCountFeatureScaleMean:"
+ "setMusicCountFeatureScaleStd:"
+ "setMusicCountShortLookback:"
+ "setMusicCountShortLookbackFeatureScaleMean:"
+ "setMusicCountShortLookbackFeatureScaleStd:"
+ "setOver20MinScreentimeCountMidLookback:"
+ "setOver20MinScreentimeCountMidLookbackFeatureScaleMean:"
+ "setOver20MinScreentimeCountMidLookbackFeatureScaleStd:"
+ "setOverMedianScreentimeSameWeekdayProbabilityShortLookback:"
+ "setOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleMean:"
+ "setOverMedianScreentimeSameWeekdayProbabilityShortLookbackFeatureScaleStd:"
+ "setScreentimeCount:"
+ "setScreentimeCountFeatureScaleMean:"
+ "setScreentimeCountFeatureScaleStd:"
+ "setScreentimeCountShortLookback:"
+ "setScreentimeCountShortLookbackFeatureScaleMean:"
+ "setScreentimeCountShortLookbackFeatureScaleStd:"
+ "setScreentimeSameWeekdayProbability:"
+ "setScreentimeSameWeekdayProbabilityFeatureScaleMean:"
+ "setScreentimeSameWeekdayProbabilityFeatureScaleStd:"
+ "setWeekdayFeatureScaleMean:"
+ "setWeekdayFeatureScaleStd:"
+ "suggestionEvent.type IN %@"
+ "unable to write engagment light stream since bookmark datastore is not available"
+ "weekdayFeatureScaleMean"
+ "weekdayFeatureScaleStd"
- "(category == %d) AND (placeUserType == %d)"
- "@104@0:8d16d24d32d40d48d56d64d72d80d88^@96"
- "@64@0:8@16@24@32@40@48d56"
- "@96@0:8d16d24d32d40d48d56d64d72d80d88"
- "APMPrevEngagementCountBin1FeatureScaleMeanKey"
- "APMPrevEngagementCountBin1FeatureScaleStdKey"
- "APMPrevEngagementCountFeatureScaleMeanKey"
- "APMPrevEngagementCountFeatureScaleStdKey"
- "APMPrevScreentimeCountFeatureScaleMeanKey"
- "APMPrevScreentimeCountFeatureScaleStdKey"
- "APMPrevScreentimeCountShortLookbackFeatureScaleMeanKey"
- "APMPrevScreentimeCountShortLookbackFeatureScaleStdKey"
- "Could not load availabilityPredict042425.mlmodelc in the bundle resource"
- "Td,N,V_prevEngagementCount"
- "Td,N,V_prevEngagementCountBin1"
- "Td,N,V_prevEngagementCountBin1FeatureScaleMean"
- "Td,N,V_prevEngagementCountBin1FeatureScaleStd"
- "Td,N,V_prevEngagementCountFeatureScaleMean"
- "Td,N,V_prevEngagementCountFeatureScaleStd"
- "Td,N,V_prevScreentimeCount"
- "Td,N,V_prevScreentimeCountFeatureScaleMean"
- "Td,N,V_prevScreentimeCountFeatureScaleStd"
- "Td,N,V_prevScreentimeCountShortLookback"
- "Td,N,V_prevScreentimeCountShortLookbackFeatureScaleMean"
- "Td,N,V_prevScreentimeCountShortLookbackFeatureScaleStd"
- "Td,N,V_sleepStartHour"
- "[APM] Extracted feature array after scaling: [downtimeStartHour:%.5f, hour:%.5f, prevEngagementCount:%.5f, prevEngagementCountBin1:%.5f, prevScreentimeCount:%.5f, prevScreentimeCountShortLookback:%.5f, overMedianScreentimeSameWeekdayProbability:%.5f, over20MinScreentimeSameWeekdayProbability:%.5f, weekdayPrevScreentimeCount:%.5f, isMorning:%.5f] for window %@"
- "[APM] Extracted feature array before scaling: [downtimeStartHour:%.5f, hour:%.5f, prevEngagementCount:%.5f, prevEngagementCountBin1:%.5f, prevScreentimeCount:%.5f, prevScreentimeCountShortLookback:%.5f, overMedianScreentimeSameWeekdayProbability:%.5f, over20MinScreentimeSameWeekdayProbability:%.5f, weekdayPrevScreentimeCount:%.5f, isMorning:%.5f] for window %@"
- "_prevEngagementCount"
- "_prevEngagementCountBin1"
- "_prevEngagementCountBin1FeatureScaleMean"
- "_prevEngagementCountBin1FeatureScaleStd"
- "_prevEngagementCountFeatureScaleMean"
- "_prevEngagementCountFeatureScaleStd"
- "_prevScreentimeCount"
- "_prevScreentimeCountFeatureScaleMean"
- "_prevScreentimeCountFeatureScaleStd"
- "_prevScreentimeCountShortLookback"
- "_prevScreentimeCountShortLookbackFeatureScaleMean"
- "_prevScreentimeCountShortLookbackFeatureScaleStd"
- "_sleepStartHour"
- "availabilityPredict042425"
- "availabilityPredict042425Input"
- "availabilityPredict042425Output"
- "countOccurenceOfEvents:forWindow:checkTime:checkWeekday:addBuffer:forFeature:"
- "d52@0:8@16@24B32B36B40@44"
- "extractFeaturesWithEvents:andBundles:andHourlyEngagement:andHourlyWritingEngagement:forWindow:withDowntimeWindowStartHour:"
- "findOptimalDateWithPrediction:"
- "initWithSleepStartHour:hour:prevEngagementCount:prevEngagementCountBin1:prevScreentimeCount:prevScreentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:over20MinScreentimeSameWeekdayProbability:weekdayPrevScreentimeCount:isMorning:"
- "predictionFromSleepStartHour:hour:prevEngagementCount:prevEngagementCountBin1:prevScreentimeCount:prevScreentimeCountShortLookback:overMedianScreentimeSameWeekdayProbability:over20MinScreentimeSameWeekdayProbability:weekdayPrevScreentimeCount:isMorning:error:"
- "prevEngagementCount"
- "prevEngagementCountBin1"
- "prevEngagementCountBin1FeatureScaleMean"
- "prevEngagementCountBin1FeatureScaleStd"
- "prevEngagementCountFeatureScaleMean"
- "prevEngagementCountFeatureScaleStd"
- "prevScreentimeCount"
- "prevScreentimeCountFeatureScaleMean"
- "prevScreentimeCountFeatureScaleStd"
- "prevScreentimeCountShortLookback"
- "prevScreentimeCountShortLookbackFeatureScaleMean"
- "prevScreentimeCountShortLookbackFeatureScaleStd"
- "setPrevEngagementCount:"
- "setPrevEngagementCountBin1:"
- "setPrevEngagementCountBin1FeatureScaleMean:"
- "setPrevEngagementCountBin1FeatureScaleStd:"
- "setPrevEngagementCountFeatureScaleMean:"
- "setPrevEngagementCountFeatureScaleStd:"
- "setPrevScreentimeCount:"
- "setPrevScreentimeCountFeatureScaleMean:"
- "setPrevScreentimeCountFeatureScaleStd:"
- "setPrevScreentimeCountShortLookback:"
- "setPrevScreentimeCountShortLookbackFeatureScaleMean:"
- "setPrevScreentimeCountShortLookbackFeatureScaleStd:"
- "setSleepStartHour:"
- "sleepStartHour"

```
