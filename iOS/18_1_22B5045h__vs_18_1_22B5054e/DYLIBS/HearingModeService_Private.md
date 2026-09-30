## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-21.9.1.0.0
-  __TEXT.__text: 0x7d50
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x514
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__cstring: 0x235b
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0xfc
-  __TEXT.__objc_methname: 0x18a0
-  __TEXT.__objc_methtype: 0x678
-  __TEXT.__objc_stubs: 0x1380
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+21.13.3.1.3
+  __TEXT.__text: 0x100b0
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_methlist: 0x848
+  __TEXT.__const: 0x86
+  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__cstring: 0x47c0
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__objc_classname: 0x137
+  __TEXT.__objc_methname: 0x3122
+  __TEXT.__objc_methtype: 0x804
+  __TEXT.__objc_stubs: 0x2c40
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0xc18
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x1228
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__objc_const: 0x18c8
+  __AUTH_CONST.__objc_doubleobj: 0x80
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__data: 0x380
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x150
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
+  - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 151
-  Symbols:   248
-  CStrings:  529
+  Functions: 260
+  Symbols:   403
+  CStrings:  962
 
Symbols:
+ _CULocalizedStringEx
+ _objc_release_x28
+ __dispatch_source_type_timer
+ _objc_release_x26
+ _OBJC_CLASS_$_NSMutableArray
+ _HKFeatureIdentifierHearingProtection
+ _OBJC_CLASS_$_CUUserNotificationSession
+ _OBJC_CLASS_$_HMOcclusionNotification
+ _CUDispatchTimerSet
+ _OBJC_CLASS_$_NSSet
+ ___NSArray0__struct
+ _OBJC_CLASS_$_NSDate
+ _OBJC_METACLASS_$_HMOcclusionNotification
+ _CFPrefs_SetCString
+ _OBJC_CLASS_$_HKObjectType
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_HKSampleQuery
+ _dispatch_activate
+ _OBJC_CLASS_$_HMDeviceCloudRecordInfo
+ _OBJC_CLASS_$_HUAccessoryHearingSettings
+ _HKFeatureIdentifierHearingTest
+ _CUPrintFlags32
+ _OBJC_CLASS_$_HKAudiogramSample
+ _OBJC_CLASS_$_HMDeviceConfigurations
+ _OBJC_CLASS_$_NSBundle
+ _objc_retainAutoreleasedReturnValue
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_HKHealthStore
+ _OBJC_CLASS_$_HKUnit
+ _HKFeatureAvailabilityContextAdvertisableFeature
+ _CFPrefs_GetCString
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _NSCalendarIdentifierGregorian
+ _objc_release_x27
+ _HKFeatureIdentifierHearingAid
+ _dispatch_source_create
+ _objc_opt_class
+ _objc_retain_x9
+ _CFPreferencesAppSynchronize
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _dispatch_source_cancel
+ _dispatch_source_set_event_handler
CStrings:
+ "### Unable to fetch occlusion result, device record not found for identifier: %!@(MISSING)"
+ "-[HMDeviceManager _computeOcclusionResultFromFaultCountsInRecord:forDevice:]"
+ "clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "setAudiogramsReported:"
+ "Supported"
+ "Yes"
+ "hearingProtectionEnabled"
+ "-[HMHealthKitUtilities _getHMRegionStatusFromFeatureStatus:featureIdentifier:]"
+ "Triggering on-demand diagnostic check for device UUID: %!@(MISSING), with reason: %!@(MISSING)"
+ "_retrieveHearingProtectionSettingsForDevice:"
+ "enableMediaAssist"
+ "HearingModeUserNotifications UINotificationSession action: %!s(MISSING), %!{(MISSING)error}"
+ "initWithHMDeviceRecord:isNewPairing:"
+ "fileURLWithPath:"
+ "Device identifier: %!@(MISSING), updating amplification %!f(MISSING) --> %!f(MISSING)"
+ "hertzUnit"
+ "setHearingAssistRegionStatus:"
+ "-[HMServiceXPCConnection clientTriggerFetchAudiograms:completion:]_block_invoke"
+ "HMDeviceCloudRecordInfo found from persistent storage %!@(MISSING)"
+ "@20@0:8I16"
+ "numberWithUnsignedChar:"
+ "clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "needsUpdateToAHPSConnectionManagerForDevice:"
+ "write HA characteristic UUID: %!@(MISSING) not found on %!@(MISSING)"
+ "AACloudServicesClient: received hmDeviceCloudRecordUpdateHandler"
+ "activeHearingProtectionEnabled"
+ "CleaningAlertSubsequentAttempt"
+ "cloudRecord"
+ "updateWithHearingProtectionValue:"
+ "### Unable to update HearingAid config: %!@(MISSING), device record not found for identifier: %!@(MISSING)"
+ "setIconName:"
+ "updateWithHearingAidConfigData:"
+ "occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "month"
+ "HearingAid"
+ "CleaningInfoViewed"
+ "_computeOcclusionResultFromFaultCountsInRecord:forDevice:"
+ "Hearing Protection Occlusion Notification shown at: %!@(MISSING)"
+ "_isAudiogramValid:"
+ "earLossArrayLeft"
+ "_hearingAidConfigDataReceived:identifier:"
+ "_updateCloudRecords:"
+ "audioStreamState"
+ "HA characteristic updated from peripheral: %!@(MISSING)"
+ "PassWithGainTableUpdateRight"
+ "-[HMDeviceManager _resetFaultCountForDevice:]"
+ "OcclusionNotificationShownDate"
+ "hpRegionStatus"
+ "setDateFormat:"
+ "InsufficientMeasurements"
+ "-[HMDeviceManager _throttleUpdatesForHearingAidConfig:identifier:completion:]"
+ "productID"
+ "_registerForHearingAccessibilitySettingsUpdate"
+ "getRegionSupportStatusForFeatureID:"
+ "-[HMDeviceManager _saveCloudRecordForDevice:withConfig:]_block_invoke"
+ "setEnablePMEMedia:"
+ "_throttleUpdatesForHearingAidConfig:identifier:completion:"
+ "setIsNewPairing:"
+ "-[HMDeviceManager _hearingProtectionValueReceived:identifier:]"
+ "setActionHandler:"
+ "setToneFileURL:"
+ "-[HMServiceXPCConnection clientFetchOcclusionResultForDeviceIdentifier:featureID:completion:]_block_invoke"
+ "/System/Library/UserNotifications/Bundles/com.apple.HearingModeUserNotifications.bundle"
+ "Device identifier: %!@(MISSING), throttling updates for Hearing Aid Config with timer %!@(MISSING)"
+ "setHearingTestRegionStatus:"
+ "setHearingAidToggle:"
+ "fetch occlusion result for UUID: %!@(MISSING), feature ID: %!s(MISSING), result: %!s(MISSING)"
+ "v36@0:8@16i24i28i32"
+ "featureStatusChangedHandler"
+ "getCloudRecordForCurrentFaultCount"
+ "hearingAssistRegionStatus"
+ "clampedSensitivity"
+ "startDate"
+ "listeningMode"
+ "sending loss for LEFT ear: loss_01_dBHL: %!l(MISSING)f"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]_block_invoke"
+ "_checkForOcclusionInDiagnosticRecord:forDevice:"
+ "sourceRevision"
+ "setEnablePMEVoice:"
+ "### Unable fetch occlusion result, no completion handler for identifier: %!@(MISSING)"
+ "decibelHearingLevelUnit"
+ "audiogram: %!@(MISSING), invalid ear sensitivity points found"
+ "setFlags:"
+ "Fetch occlusion result: missing device UUID"
+ "Fetching region status for UUID: %!@(MISSING)"
+ "setHearingAidEnrolled:"
+ "_featureIDRegionStatusMap"
+ "swipeGainEnabled"
+ "isOcclusionDetectionSupported"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:]"
+ "T@?,C,N,V_hearingProtectionUpdateHandler"
+ "dateFromString:"
+ "-[HMHealthKitUtilities _audiogramsQueryHandler:results:error:]"
+ "_reportValidAudiograms:invalidAudiograms:error:"
+ "setSound:"
+ "Saved HMDeviceCloudRecordInfo, with error %!@(MISSING), record: %!@(MISSING)"
+ "Unsupported"
+ "_hasOcclusionNotificationsThresholdMet"
+ "listeningModeConfigs"
+ "HearingModeUserNotifications"
+ "setEnableHearingAidGainSwipe:"
+ "-[HMDeviceManager _setHearingProtectionEnabledForDevice:withConfig:]"
+ "Region support changed for identifier %!@(MISSING): %!s(MISSING) --> %!s(MISSING), whyNotVisible: %!@(MISSING), whyWeCantUse: %!@(MISSING)"
+ "aaDevice"
+ "setHaRegionStatus:"
+ "Device identifier: %!@(MISSING), updating balance %!f(MISSING) --> %!f(MISSING)"
+ "frequencyToHearingDecibelLevelMapFromAudiogram:"
+ "@\"NSArray\""
+ "HMDeviceRecord updated with occlusion result: %!@(MISSING)"
+ "_occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "PassWithGainTableUpdateLeft"
+ "clientHMAvailableAudiograms:invalidAudiograms:error:"
+ "doubleValueForUnit:"
+ "v32@?0@\"HKAudiogramSensitivityTest\"8Q16^B24"
+ "reset-occlusion-counts"
+ "updateHMSettingsStruct:fromAudiogram:"
+ "featureStatusWithError:"
+ "setEnableHearingAid:"
+ "@\"HMOcclusionNotification\""
+ "writeHMSettingsConfigsData:completion:"
+ "invokePendingOcclusionCompletionsWithError:"
+ "resetFaultCounts"
+ "NoIndication"
+ "_deviceRescindHearingAssist:"
+ "_settingsUpdateHandler"
+ "settingsUpdateHandler"
+ "Localizable"
+ "date"
+ "enableHearingAssist"
+ "setHpRegionStatus:"
+ "FailOnSubsequentAttempt"
+ "OcclusionIndicationShown with address: %!@(MISSING), type: %!s(MISSING), feature: %!s(MISSING), action: %!s(MISSING)"
+ "### write HA characteristic UUID: %!@(MISSING) not found for identifier %!@(MISSING)"
+ "registerUpdateBlock:forRetrieveSelector:withListener:"
+ "numberWithDouble:"
+ "selectedAudiogram"
+ "setEnableSwipeGain:"
+ "PassWithGainTableUpdateBoth"
+ "audiogramsReported"
+ "-[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:]_block_invoke_2"
+ "placementMode"
+ "HearingProtection"
+ "initWithObjects:"
+ "earLossArrayRight"
+ "setTitleKey:"
+ "yyyy-MM-dd HH:mm:ss"
+ "_hearingProtectionValueReceived:identifier:"
+ "intValue"
+ "setBodyKey:"
+ "setSettingsUpdateHandler:"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
+ "_audiogramsQueryHandler:results:error:"
+ "fetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "Feature rescinded, modified device config: %!@(MISSING)"
+ "failed to process audiogram"
+ "v24@?0@\"HMDeviceCloudRecordInfo\"8@\"NSError\"16"
+ "v36@0:8@16i24@?28"
+ "bundleForClass:"
+ "com.apple.HearingModeUserNotifications"
+ "-[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:]"
+ "HMDeviceRecord with identifier: %!@(MISSING), set default for AllowListeningMode: %!s(MISSING), LsnM: %!s(MISSING), lsMc: %!@(MISSING)"
+ "-[HMDeviceManager _throttleUpdatesForHearingAidConfig:identifier:completion:]_block_invoke"
+ "HearingTest"
+ "v32@?0@\"HKAudiogramSensitivityPoint\"8Q16^B24"
+ "CleaningAlert"
+ "No"
+ "v36@0:8@\"NSString\"16i24i28i32"
+ "HearingAid config data not found, creating new config"
+ "Unable to query feature status with error: %!@(MISSING)"
+ "setPmeVoiceEnabled:"
+ "v28@0:8C16@20"
+ "setPendingOcclusionCompletionsMap:"
+ "setHmDeviceCloudRecordUpdateHandler:"
+ "_featureStatusChangedHandler"
+ "frequency"
+ "getOcclusionResultForFeatureID:"
+ "-[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:]"
+ "balance"
+ "occlusionIndicationShownForFeatureID:type:action:"
+ "### Unable to set occlusionIndicationShown, device record not found for identifier: %!@(MISSING)"
+ "OcclusionIndicationShown with UUID: %!@(MISSING), type: %!s(MISSING), feature: %!s(MISSING), action: %!s(MISSING)"
+ "_occlusionNotification"
+ "-[HMOcclusionNotification _hasOcclusionNotificationsThresholdMet]"
+ "unregisterObserver:"
+ "secondaryPlacement"
+ "setEnableMediaAssist:"
+ "tone"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "Dismiss"
+ "registerObserver:"
+ "-[HMDeviceManager _hearingAidConfigDataReceived:identifier:]"
+ "Device identifier: %!@(MISSING), updating noiseSuppression %!f(MISSING) --> %!f(MISSING)"
+ "left"
+ "computeOcclusionResultForHearingProtection"
+ "peripheral device not found for identifier: %!@(MISSING)"
+ "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]"
+ "Default"
+ "HMDeviceRecord with UUID %!@(MISSING) used for <3 months, override occlusion to pass"
+ "occlusion-test"
+ "ActiveNotification"
+ "### Hearing Mode Client fetch occlusion result: %!{(MISSING)error}"
+ "_loadCloudRecordForDevice:"
+ "setFeatureStatusChangedHandler:"
+ "-[HMDeviceManager _updateCloudRecords:]_block_invoke"
+ "_fetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "startAudiogramQuery"
+ "_deviceSetOffListeningModeAllowedIfNeeded:"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "HMDeviceRecord updated locally: %!@(MISSING)"
+ "_writeHMSettingsConfigsData:completion:"
+ "HMDeviceRecord updated from cloud record: %!@(MISSING)"
+ "### Set OcclusionIndicationShown failed: %!{(MISSING)error}"
+ "setActiveHearingProtectionEnabled:forAddress:"
+ "wav"
+ "Feature rescind, failed to modify device config: %!@(MISSING)"
+ "enableHearingProtection"
+ "occlusion-result"
+ "pathForResource:ofType:"
+ "\x01\x15\x14"
+ "hearingAssistEnrolled"
+ "v32@?0@\"HKSampleQuery\"8@\"NSArray\"16@\"NSError\"24"
+ "_setHearingProtectionEnabledForDevice:withConfig:"
+ "initWithCalendarIdentifier:"
+ "Cancel"
+ "Unable to update HearingAid config: %!@(MISSING), device record not found for identifier: %!@(MISSING)"
+ "stringFromDate:"
+ "modifyHMDeviceCloudRecordInfo:completion:"
+ "Pass"
+ "requiredFrequencyBins"
+ "enableHearingAid"
+ "setHearingProtectionRegionStatus:"
+ "HKFeatureStatusProvidingObserver"
+ "HMDeviceCloudRecordInfo init %!@(MISSING)"
+ "hideOffListeningModeCapability"
+ "setMediaAssistEnabled:"
+ "\x02"
+ "+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke_2"
+ "Saving HMDeviceCloudRecordInfo for cloud sync %!@(MISSING)"
+ "## peripheral device not found for identifier: %!@(MISSING)"
+ "HMDeviceCloudRecordInfo init for saving config %!@(MISSING)"
+ "TB,N,V_audiogramsReported"
+ "setHearingProtectionUpdateHandler:"
+ "-[HMDeviceManager _deviceUpdateRegionStatus:]"
+ "HP characteristic updated from peripheral: %!@(MISSING)"
+ "AllowListeningModeOff"
+ "setEnableHearingAssist:"
+ "-[HMDeviceManager _deviceRescindHearingAssist:]_block_invoke"
+ "-[HMDeviceManager _saveCloudRecordForDevice:withConfig:]"
+ "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]_block_invoke"
+ "sending loss for RIGHT ear: loss_01_dBHL: %!l(MISSING)f"
+ "Fail"
+ "side"
+ "v20@?0@\"NSString\"8C16"
+ "-[HMDeviceManager _deviceSetOffListeningModeAllowedIfNeeded:]_block_invoke"
+ "-[HMDeviceManager _resetFaultCountForDevice:]_block_invoke"
+ "updateWithCloudRecordInfo:"
+ "-[HMDeviceManager _retrieveHearingProtectionSettingsForDevice:]"
+ "AHPS connection manager: nothing to update: %!@(MISSING)"
+ "sensitivity"
+ "setBundleID:"
+ "_setPreferencesForKey:withStringValue:"
+ "frequencyBins"
+ "setAudiogramEnrolledTimestamp:"
+ "### AHPS connection manager not found"
+ "-[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:]"
+ "ANC"
+ "HMDeviceRecord updated with Hearing Protection enable value: %!d(MISSING), %!@(MISSING)"
+ "setOcclusionResult:forFeatureID:"
+ "### fetch audiograms failed: %!{(MISSING)error}"
+ "isDeviceUsedFor3MonthsOrLess"
+ "mediaAssistEnabled"
+ "HealthKit audiogram query error: %!@(MISSING)"
+ "Previous shown date %!@(MISSING) current Date: %!@(MISSING) Difference in date components: days %!i(MISSING) months %!i(MISSING) years %!i(MISSING)"
+ "v16@?0@\"NSArray\"8"
+ "_latestConfigsMap"
+ "updateFaultCountsFromCloudRecord:"
+ "-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke_3"
+ "T@?,C,N,V_settingsUpdateHandler"
+ "components:fromDate:toDate:options:"
+ "haRegionStatus"
+ "Unable to fetch occlusion result, device record not found for identifier: %!@(MISSING)"
+ "caching occlusion result handler %!@(MISSING) for device identifier %!@(MISSING)"
+ "listeningModeOffAllowed"
+ "_occlusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "noiseSuppression"
+ "hearingTestRegionStatus"
+ "-[HMDeviceManager _triggerHearingProtectionOcclusionNotificationIfNeeded:]"
+ "AHPS connection manager not found"
+ "HEARING_PROTECTION_TITLE"
+ "initWithFeatureIdentifier:healthStore:countryCodeSource:"
+ "Internal: HMDeviceRecord updated with occlusion result: %!@(MISSING)"
+ "name"
+ "override-occlusion-result"
+ "invalid audiogram"
+ "C32@0:8@16@24"
+ "HearingAssist"
+ "hearingProtectionRegionStatus"
+ "interpolating sensitivity point at 6000Hz, leftEar: %!f(MISSING) dbHL, rightEar: %!f(MISSING) dbHL"
+ "setOcclusionResultReady:"
+ "HMDeviceRecord updated from HearingAid config: %!@(MISSING)"
+ "setCategoryID:"
+ "CleaningPerformed"
+ "HP value update for unknown identifier: %!@(MISSING)"
+ "amplification"
+ "feature-ID"
+ "areAllRequirementsSatisfied"
+ "hearingAssistEnabled"
+ "v32@0:8^{?=CCS{?=ffffffffffff}{?=ffffffffffff}}16@24"
+ "_invalidAudiograms"
+ "activeHearingProtectionEnabledForAddress:"
+ "v20@0:8I16"
+ "HMDeviceRecord updated with Hearing Protection settings value: %!d(MISSING), %!@(MISSING)"
+ "-[HMHealthKitUtilities updateHMSettingsStruct:fromAudiogram:]"
+ "year"
+ "occlusionResultReady"
+ "_validAudiograms"
+ "Saved diagnostics data in HMDeviceCloudRecordInfo, with error %!@(MISSING)"
+ "interpolating sensitivity point at 3000Hz, leftEar: %!f(MISSING) dbHL, rightEar: %!f(MISSING) dbHL"
+ "a48fec08-3921-43db-82aa-afbce8ebb4fb"
+ "_unregisterFromHearingAccessibilitySettingsUpdate"
+ "-[HMHealthKitUtilities getRegionSupportStatusForFeatureID:]"
+ "getOnDemandRetestReason"
+ "hearingProtectionUpdateHandler"
+ "v36@0:8@\"NSString\"16i24@?<v@?i@\"NSError\">28"
+ "C24@0:8@16"
+ "HMDeviceRecord updated from cloud push: %!@(MISSING)"
+ "computeOcclusionResultForHearingTest"
+ "Placard"
+ "_uiNotificationSessionHearingProtection"
+ "-[HMHealthKitUtilities _isAudiogramValid:]"
+ "UTF8String"
+ "sending settings: leftGain: %!l(MISSING)f, rightGain: %!l(MISSING)f, tone: %!l(MISSING)f, amplification: %!l(MISSING)f, balance: %!l(MISSING)f, beamFormer: %!l(MISSING)f, noiseSuppression: %!l(MISSING)f"
+ "showHearingProtectionOcclusionNotification:"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "HearingMode"
+ "\x16"
+ "_registerForRegionStatusUpdates"
+ "executeQuery:"
+ "NotificationAudioTone"
+ "configDataHearingAid"
+ "DiagnosticCheckNeeded"
+ "Rescinded"
+ "-[HMDeviceManager _checkForOcclusionInDiagnosticRecord:forDevice:]"
+ "_getHMRegionStatusFromFeatureStatus:featureIdentifier:"
+ "initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:"
+ "-[HMDeviceManager _deviceRescindHearingAssist:]"
+ "Device identifier: %!@(MISSING), updating beamFormer %!f(MISSING) --> %!f(MISSING)"
+ "-[HMDeviceManager _occlusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
+ "shouldShowHearingProtectionOcclusionNotification %!d(MISSING)"
+ "occlusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "sensitivityPoints"
+ "containsObject:"
+ "pendingOcclusionCompletionsMap"
+ "HMDeviceCloudRecordInfo not found from persistent storage for address %!@(MISSING), error %!@(MISSING)"
+ "beamFormer"
+ "\x14\x14"
+ "-[HMDeviceManager _deviceSetOffListeningModeAllowedIfNeeded:]"
+ "setObject:forKey:"
+ "### Unable to set occlusionIndicationShown, diagnostic record not found for address: %!@(MISSING)"
+ "-[HMDeviceManager _checkForOcclusionInDiagnosticRecord:forDevice:]_block_invoke"
+ "airpodspro"
+ "clientTriggerFetchAudiograms:completion:"
+ "@\"CUUserNotificationSession\""
+ "_saveCloudRecordForDevice:withConfig:"
+ "soundWithAlertType:"
+ "day"
+ "_diagnosticRecordCheckForOcclusion: missing cloud record"
+ "audiogramSampleType"
+ "_startAudiogramQuery"
+ "hearingAidEnabled"
+ "numberWithInt:"
+ "AutoANC"
+ "invalidateHearingProtectionOcclusionNotification"
+ "Device identifier: %!@(MISSING), updating tone %!f(MISSING) --> %!f(MISSING)"
+ "fetchHMDeviceCloudRecordInfoWithAddress:completion:"
+ "Invalid"
+ "setSwipeGainEnabled:"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
+ "Internal: Saved diagnostics data in HMDeviceCloudRecordInfo, with error %!@(MISSING)"
+ "clientFetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "Settings updated for unknown identifier: %!@(MISSING)"
+ "setPmeMediaEnabled:"
+ "source"
+ "tests"
+ "Internal: Saving diagnostics data in HMDeviceCloudRecordInfo record: %!@(MISSING)"
+ "Device identifier: %!@(MISSING), cancelling throttle timer %!@(MISSING)"
+ "Normal"
+ "_featureManagerMap"
+ "_getStringPreferencesForKey:"
+ "a4120005-95c5-4d6f-9098-0f0b41457e0a"
+ "measurementInvalidReason"
+ "HMDeviceRecord UUID %!@(MISSING), set Hearing Protection settings value: %!d(MISSING)"
+ "enableSwipeGain"
+ "setLabel:"
+ "_triggerHearingProtectionOcclusionNotificationIfNeeded:"
+ "Transparency"
+ "Saving diagnostics data in HMDeviceCloudRecordInfo record: %!@(MISSING)"
+ "initWithBluetoothAddress:"
+ "shouldShowHearingProtectionOcclusionNotification"
+ "-[HMDeviceManager _occlusionIndicationShownForDeviceAddress:featureID:type:action:]"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:]_block_invoke"
+ "primaryPlacement"
+ "Feature rescinded but device not enrolled: %!@(MISSING)"
+ "HEARING_PROTECTION_SUBTITLE"
+ "stringWithUTF8String:"
+ "ConnectedAudio"
+ "_resetFaultCountForDevice:"
+ "### Unable to set occlusionIndicationShown, device record not found for address: %!@(MISSING)"
+ "_hearingProtectionUpdateHandler"
+ "writing HA characteristics to peripheral %!@(MISSING)"
+ "_sendHearingAidConfigOverAHPSConnection:identifier:completion:"
+ "hearingProtectionOcclusionResult"
+ "HMOcclusionNotification"
+ "-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke"
+ "Internal: Failed to find diagnostic record for UUID: %!@(MISSING)"
+ "_audiogramsReported"
+ "_deviceUpdateRegionStatus:"
+ "highestPriorityUnsatisfiedRequirement"
+ "right"
+ "_throttleTimerMap"
+ "T@?,C,N,V_featureStatusChangedHandler"
+ "coreBluetoothDevice"
+ "v20@?0i8@\"NSError\"12"
+ "v32@?0@\"NSString\"8@\"HKFeatureStatusManager\"16^B24"
+ "Error"
+ "objectForKey:"
+ "_getSystemIconName:"
+ "hearingProtectionCapability"
+ "enrollHearingAssist"
+ "reportValidAudiograms:invalidAudiograms:error:"
+ "Timeout"
+ "Unable to fetch occlusion result, diagnostic record not found for identifier: %!@(MISSING)"
+ "backend converted tone: %!l(MISSING)f, balance: %!l(MISSING)f, amplification: %!l(MISSING)f"
+ "clientReportValidAudiograms:invalidAudiograms:error:"
+ "_unregisterFromRegionStatusUpdates"
+ "bundleWithPath:"
- "-[HMDeviceManager _distributedNotificationReceived:]_block_invoke_2"
- "\x11"
- "updateWithHMDeviceRecord:"
- "\x14\x12"
- "\x01\x15\x11"

```
