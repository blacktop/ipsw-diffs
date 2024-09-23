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
+ _objc_opt_class
+ _objc_release_x26
+ _OBJC_CLASS_$_NSURL
+ ___NSArray0__struct
+ _dispatch_source_create
+ _CFPreferencesAppSynchronize
+ _HKFeatureIdentifierHearingProtection
+ _OBJC_METACLASS_$_HMOcclusionNotification
+ _objc_release_x27
+ _OBJC_CLASS_$_HKSampleQuery
+ _OBJC_CLASS_$_HMDeviceConfigurations
+ _objc_release_x28
+ _CFPrefs_SetCString
+ _dispatch_activate
+ _OBJC_CLASS_$_NSSet
+ _dispatch_source_cancel
+ _CFPrefs_GetCString
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _HKFeatureAvailabilityContextAdvertisableFeature
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _OBJC_CLASS_$_HMOcclusionNotification
+ _CUPrintFlags32
+ _OBJC_CLASS_$_HUAccessoryHearingSettings
+ _OBJC_CLASS_$_NSCalendar
+ _objc_retainAutoreleasedReturnValue
+ _CUDispatchTimerSet
+ _objc_retain_x9
+ _OBJC_CLASS_$_HKUnit
+ _HKFeatureIdentifierHearingAid
+ _OBJC_CLASS_$_CUUserNotificationSession
+ _OBJC_CLASS_$_HKAudiogramSample
+ _OBJC_CLASS_$_HKObjectType
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSString
+ __dispatch_source_type_timer
+ _HKFeatureIdentifierHearingTest
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_NSDateFormatter
+ _CULocalizedStringEx
+ _OBJC_CLASS_$_HKHealthStore
+ _dispatch_source_set_event_handler
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_HMDeviceCloudRecordInfo
+ _OBJC_CLASS_$_NSMutableArray
CStrings:
+ "-[HMDeviceManager _saveCloudRecordForDevice:withConfig:]_block_invoke"
+ "v36@0:8@16i24@?28"
+ "-[HMDeviceManager _checkForOcclusionInDiagnosticRecord:forDevice:]"
+ "_occlusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "setEnableHearingAssist:"
+ "C24@0:8@16"
+ "activeHearingProtectionEnabledForAddress:"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]_block_invoke"
+ "setActionHandler:"
+ "_deviceUpdateRegionStatus:"
+ "components:fromDate:toDate:options:"
+ "sending settings: leftGain: %!l(MISSING)f, rightGain: %!l(MISSING)f, tone: %!l(MISSING)f, amplification: %!l(MISSING)f, balance: %!l(MISSING)f, beamFormer: %!l(MISSING)f, noiseSuppression: %!l(MISSING)f"
+ "settingsUpdateHandler"
+ "HEARING_PROTECTION_TITLE"
+ "computeOcclusionResultForHearingTest"
+ "### Unable to set occlusionIndicationShown, device record not found for address: %!@(MISSING)"
+ "-[HMDeviceManager _throttleUpdatesForHearingAidConfig:identifier:completion:]"
+ "AHPS connection manager: nothing to update: %!@(MISSING)"
+ "Invalid"
+ "fileURLWithPath:"
+ "-[HMHealthKitUtilities getRegionSupportStatusForFeatureID:]"
+ "Fetching region status for UUID: %!@(MISSING)"
+ "updateWithHearingProtectionValue:"
+ "yyyy-MM-dd HH:mm:ss"
+ "Unable to update HearingAid config: %!@(MISSING), device record not found for identifier: %!@(MISSING)"
+ "enrollHearingAssist"
+ "hearingProtectionRegionStatus"
+ "NotificationAudioTone"
+ "numberWithUnsignedChar:"
+ "setHearingProtectionRegionStatus:"
+ "_audiogramsQueryHandler:results:error:"
+ "setHearingAssistRegionStatus:"
+ "HMDeviceRecord with identifier: %!@(MISSING), set default for AllowListeningMode: %!s(MISSING), LsnM: %!s(MISSING), lsMc: %!@(MISSING)"
+ "Timeout"
+ "### Unable to update HearingAid config: %!@(MISSING), device record not found for identifier: %!@(MISSING)"
+ "/System/Library/UserNotifications/Bundles/com.apple.HearingModeUserNotifications.bundle"
+ "AHPS connection manager not found"
+ "setAudiogramEnrolledTimestamp:"
+ "beamFormer"
+ "setEnableSwipeGain:"
+ "@\"HMOcclusionNotification\""
+ "_retrieveHearingProtectionSettingsForDevice:"
+ "Region support changed for identifier %!@(MISSING): %!s(MISSING) --> %!s(MISSING), whyNotVisible: %!@(MISSING), whyWeCantUse: %!@(MISSING)"
+ "_updateCloudRecords:"
+ "-[HMDeviceManager _cloudServicesClientEnsureStarted]_block_invoke_3"
+ "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]"
+ "CleaningAlertSubsequentAttempt"
+ "HearingMode"
+ "setSettingsUpdateHandler:"
+ "a48fec08-3921-43db-82aa-afbce8ebb4fb"
+ "_hearingProtectionValueReceived:identifier:"
+ "Internal: Saved diagnostics data in HMDeviceCloudRecordInfo, with error %!@(MISSING)"
+ "_settingsUpdateHandler"
+ "setHearingAidToggle:"
+ "setIsNewPairing:"
+ "wav"
+ "-[HMDeviceManager _resetFaultCountForDevice:]"
+ "executeQuery:"
+ "_setHearingProtectionEnabledForDevice:withConfig:"
+ "balance"
+ "invalid audiogram"
+ "registerUpdateBlock:forRetrieveSelector:withListener:"
+ "writeHMSettingsConfigsData:completion:"
+ "unregisterObserver:"
+ "-[HMDeviceManager _triggerHearingProtectionOcclusionNotificationIfNeeded:]"
+ "Internal: Failed to find diagnostic record for UUID: %!@(MISSING)"
+ "_loadCloudRecordForDevice:"
+ "day"
+ "com.apple.HearingModeUserNotifications"
+ "setHpRegionStatus:"
+ "interpolating sensitivity point at 3000Hz, leftEar: %!f(MISSING) dbHL, rightEar: %!f(MISSING) dbHL"
+ "setIconName:"
+ "computeOcclusionResultForHearingProtection"
+ "override-occlusion-result"
+ "T@?,C,N,V_hearingProtectionUpdateHandler"
+ "_throttleTimerMap"
+ "No"
+ "NoIndication"
+ "Settings updated for unknown identifier: %!@(MISSING)"
+ "HMDeviceCloudRecordInfo found from persistent storage %!@(MISSING)"
+ "Transparency"
+ "_resetFaultCountForDevice:"
+ "sensitivityPoints"
+ "setEnableMediaAssist:"
+ "_startAudiogramQuery"
+ "bundleWithPath:"
+ "highestPriorityUnsatisfiedRequirement"
+ "Previous shown date %!@(MISSING) current Date: %!@(MISSING) Difference in date components: days %!i(MISSING) months %!i(MISSING) years %!i(MISSING)"
+ "invalidateHearingProtectionOcclusionNotification"
+ "CleaningAlert"
+ "Feature rescind, failed to modify device config: %!@(MISSING)"
+ "earLossArrayLeft"
+ "shouldShowHearingProtectionOcclusionNotification"
+ "v32@?0@\"HKAudiogramSensitivityPoint\"8Q16^B24"
+ "_diagnosticRecordCheckForOcclusion: missing cloud record"
+ "v20@?0@\"NSString\"8C16"
+ "-[HMDeviceManager _saveCloudRecordForDevice:withConfig:]"
+ "_validAudiograms"
+ "frequencyToHearingDecibelLevelMapFromAudiogram:"
+ "PassWithGainTableUpdateBoth"
+ "failed to process audiogram"
+ "setBundleID:"
+ "clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "enableHearingAid"
+ "-[HMDeviceManager _retrieveHearingProtectionSettingsForDevice:]"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:]_block_invoke"
+ "_audiogramsReported"
+ "### fetch audiograms failed: %!{(MISSING)error}"
+ "interpolating sensitivity point at 6000Hz, leftEar: %!f(MISSING) dbHL, rightEar: %!f(MISSING) dbHL"
+ "frequencyBins"
+ "HealthKit audiogram query error: %!@(MISSING)"
+ "_getHMRegionStatusFromFeatureStatus:featureIdentifier:"
+ "### Set OcclusionIndicationShown failed: %!{(MISSING)error}"
+ "Saved HMDeviceCloudRecordInfo, with error %!@(MISSING), record: %!@(MISSING)"
+ "v28@0:8C16@20"
+ "-[HMServiceXPCConnection clientFetchOcclusionResultForDeviceIdentifier:featureID:completion:]_block_invoke"
+ "setEnableHearingAidGainSwipe:"
+ "Yes"
+ "audiogramSampleType"
+ "Localizable"
+ "fetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "occlusion-test"
+ "setFeatureStatusChangedHandler:"
+ "setEnablePMEMedia:"
+ "_registerForHearingAccessibilitySettingsUpdate"
+ "Saved diagnostics data in HMDeviceCloudRecordInfo, with error %!@(MISSING)"
+ "_deviceSetOffListeningModeAllowedIfNeeded:"
+ "\x02"
+ "v20@?0i8@\"NSError\"12"
+ "isOcclusionDetectionSupported"
+ "activeHearingProtectionEnabled"
+ "-[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:]_block_invoke_2"
+ "setHearingAidEnrolled:"
+ "_reportValidAudiograms:invalidAudiograms:error:"
+ "featureStatusWithError:"
+ "T@?,C,N,V_settingsUpdateHandler"
+ "TB,N,V_audiogramsReported"
+ "Unable to fetch occlusion result, device record not found for identifier: %!@(MISSING)"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "invokePendingOcclusionCompletionsWithError:"
+ "setDateFormat:"
+ "stringWithUTF8String:"
+ "-[HMHealthKitUtilities updateHMSettingsStruct:fromAudiogram:]"
+ "Placard"
+ "backend converted tone: %!l(MISSING)f, balance: %!l(MISSING)f, amplification: %!l(MISSING)f"
+ "initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:"
+ "v16@?0@\"NSArray\"8"
+ "Feature rescinded, modified device config: %!@(MISSING)"
+ "Internal: HMDeviceRecord updated with occlusion result: %!@(MISSING)"
+ "v36@0:8@16i24i28i32"
+ "## peripheral device not found for identifier: %!@(MISSING)"
+ "Cancel"
+ "CleaningPerformed"
+ "aaDevice"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "_featureStatusChangedHandler"
+ "setMediaAssistEnabled:"
+ "HearingAid"
+ "-[HMHealthKitUtilities _audiogramsQueryHandler:results:error:]"
+ "Unable to query feature status with error: %!@(MISSING)"
+ "reset-occlusion-counts"
+ "-[HMDeviceManager _resetFaultCountForDevice:]_block_invoke"
+ "_fetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "hearingAssistEnabled"
+ "HearingProtection"
+ "_occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "_latestConfigsMap"
+ "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]_block_invoke"
+ "initWithObjects:"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceAddress:featureID:type:action:]"
+ "Triggering on-demand diagnostic check for device UUID: %!@(MISSING), with reason: %!@(MISSING)"
+ "_sendHearingAidConfigOverAHPSConnection:identifier:completion:"
+ "objectForKey:"
+ "T@?,C,N,V_featureStatusChangedHandler"
+ "_hearingProtectionUpdateHandler"
+ "clientTriggerFetchAudiograms:completion:"
+ "reportValidAudiograms:invalidAudiograms:error:"
+ "-[HMDeviceManager _computeOcclusionResultFromFaultCountsInRecord:forDevice:]"
+ "_hearingAidConfigDataReceived:identifier:"
+ "HMDeviceRecord updated with Hearing Protection settings value: %!d(MISSING), %!@(MISSING)"
+ "enableHearingAssist"
+ "hearingProtectionCapability"
+ "startAudiogramQuery"
+ "_throttleUpdatesForHearingAidConfig:identifier:completion:"
+ "occlusionIndicationShownForFeatureID:type:action:"
+ "setHaRegionStatus:"
+ "Normal"
+ "ConnectedAudio"
+ "HMDeviceRecord updated with Hearing Protection enable value: %!d(MISSING), %!@(MISSING)"
+ "swipeGainEnabled"
+ "soundWithAlertType:"
+ "fetchHMDeviceCloudRecordInfoWithAddress:completion:"
+ "HearingAssist"
+ "_computeOcclusionResultFromFaultCountsInRecord:forDevice:"
+ "HMDeviceCloudRecordInfo init %!@(MISSING)"
+ "date"
+ "selectedAudiogram"
+ "ActiveNotification"
+ "occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "numberWithInt:"
+ "setOcclusionResultReady:"
+ "initWithCalendarIdentifier:"
+ "source"
+ "-[HMDeviceManager _hearingProtectionValueReceived:identifier:]"
+ "_isAudiogramValid:"
+ "UTF8String"
+ "enableMediaAssist"
+ "intValue"
+ "setFlags:"
+ "setPmeMediaEnabled:"
+ "year"
+ "hearingProtectionUpdateHandler"
+ "HMDeviceCloudRecordInfo init for saving config %!@(MISSING)"
+ "PassWithGainTableUpdateRight"
+ "Device identifier: %!@(MISSING), updating tone %!f(MISSING) --> %!f(MISSING)"
+ "occlusionIndicationShownForDeviceAddress:featureID:type:action:"
+ "v36@0:8@\"NSString\"16i24i28i32"
+ "_invalidAudiograms"
+ "clientReportValidAudiograms:invalidAudiograms:error:"
+ "registerObserver:"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
+ "v32@?0@\"HKAudiogramSensitivityTest\"8Q16^B24"
+ "productID"
+ "### write HA characteristic UUID: %!@(MISSING) not found for identifier %!@(MISSING)"
+ "frequency"
+ "\x01\x15\x14"
+ "setLabel:"
+ "HMDeviceCloudRecordInfo not found from persistent storage for address %!@(MISSING), error %!@(MISSING)"
+ "OcclusionIndicationShown with address: %!@(MISSING), type: %!s(MISSING), feature: %!s(MISSING), action: %!s(MISSING)"
+ "initWithHMDeviceRecord:isNewPairing:"
+ "Saving diagnostics data in HMDeviceCloudRecordInfo record: %!@(MISSING)"
+ "setToneFileURL:"
+ "\x16"
+ "HMDeviceRecord with UUID %!@(MISSING) used for <3 months, override occlusion to pass"
+ "earLossArrayRight"
+ "setCategoryID:"
+ "dateFromString:"
+ "shouldShowHearingProtectionOcclusionNotification %!d(MISSING)"
+ "AACloudServicesClient: received hmDeviceCloudRecordUpdateHandler"
+ "featureStatusChangedHandler"
+ "hearingAidEnabled"
+ "### Unable to set occlusionIndicationShown, device record not found for identifier: %!@(MISSING)"
+ "-[HMDeviceManager _setHearingProtectionEnabledForDevice:withConfig:]"
+ "Internal: Saving diagnostics data in HMDeviceCloudRecordInfo record: %!@(MISSING)"
+ "setSound:"
+ "HMDeviceRecord updated from HearingAid config: %!@(MISSING)"
+ "clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:"
+ "sourceRevision"
+ "peripheral device not found for identifier: %!@(MISSING)"
+ "airpodspro"
+ "needsUpdateToAHPSConnectionManagerForDevice:"
+ "-[HMDeviceManager _sendHearingAidConfigOverAHPSConnection:identifier:completion:]"
+ "_registerForRegionStatusUpdates"
+ "hearingProtectionOcclusionResult"
+ "occlusionResultReady"
+ "### Unable to fetch occlusion result, device record not found for identifier: %!@(MISSING)"
+ "-[HMDeviceAHPSConnectionManager _writeHMSettingsConfigsData:completion:]"
+ "AutoANC"
+ "Pass"
+ "enableSwipeGain"
+ "setActiveHearingProtectionEnabled:forAddress:"
+ "v32@?0@\"HKSampleQuery\"8@\"NSArray\"16@\"NSError\"24"
+ "Fetch occlusion result: missing device UUID"
+ "HMDeviceRecord updated with occlusion result: %!@(MISSING)"
+ "listeningMode"
+ "feature-ID"
+ "HearingTest"
+ "enableHearingProtection"
+ "-[HMDeviceManager _occlusionIndicationShownForDeviceAddress:featureID:type:action:]"
+ "C32@0:8@16@24"
+ "Device identifier: %!@(MISSING), updating amplification %!f(MISSING) --> %!f(MISSING)"
+ "-[HMDeviceManager _deviceSetOffListeningModeAllowedIfNeeded:]"
+ "-[HMDeviceManager _throttleUpdatesForHearingAidConfig:identifier:completion:]_block_invoke"
+ "AllowListeningModeOff"
+ "v24@?0@\"HMDeviceCloudRecordInfo\"8@\"NSError\"16"
+ "showHearingProtectionOcclusionNotification:"
+ "-[HMDeviceManager _loadCloudRecordForDevice:]_block_invoke"
+ "FailOnSubsequentAttempt"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "Device identifier: %!@(MISSING), cancelling throttle timer %!@(MISSING)"
+ "numberWithDouble:"
+ "_getSystemIconName:"
+ "updateWithHearingAidConfigData:"
+ "-[HMDeviceManager _deviceUpdateRegionStatus:]"
+ "HMDeviceRecord updated locally: %!@(MISSING)"
+ "_featureIDRegionStatusMap"
+ "listeningModeOffAllowed"
+ "setPmeVoiceEnabled:"
+ "tone"
+ "HearingModeUserNotifications"
+ "doubleValueForUnit:"
+ "_writeHMSettingsConfigsData:completion:"
+ "Default"
+ "Device identifier: %!@(MISSING), updating beamFormer %!f(MISSING) --> %!f(MISSING)"
+ "-[HMServiceXPCConnection clientTriggerFetchAudiograms:completion:]_block_invoke"
+ "### AHPS connection manager not found"
+ "-[HMDeviceManager _fetchOcclusionResultForDeviceIdentifier:featureID:completion:]"
+ "configDataHearingAid"
+ "name"
+ "HEARING_PROTECTION_SUBTITLE"
+ "_unregisterFromRegionStatusUpdates"
+ "audiogramsReported"
+ "_deviceRescindHearingAssist:"
+ "fetch occlusion result for UUID: %!@(MISSING), feature ID: %!s(MISSING), result: %!s(MISSING)"
+ "setObject:forKey:"
+ "v20@0:8I16"
+ "measurementInvalidReason"
+ "v36@0:8@\"NSString\"16i24@?<v@?i@\"NSError\">28"
+ "HearingAid config data not found, creating new config"
+ "secondaryPlacement"
+ "-[HMDeviceManager _deviceRescindHearingAssist:]"
+ "-[HMHealthKitUtilities _getHMRegionStatusFromFeatureStatus:featureIdentifier:]"
+ "setBodyKey:"
+ "listeningModeConfigs"
+ "tests"
+ "Feature rescinded but device not enrolled: %!@(MISSING)"
+ "HP characteristic updated from peripheral: %!@(MISSING)"
+ "setHearingProtectionUpdateHandler:"
+ "hearingAssistRegionStatus"
+ "side"
+ "_getStringPreferencesForKey:"
+ "InsufficientMeasurements"
+ "CleaningInfoViewed"
+ "audiogram: %!@(MISSING), invalid ear sensitivity points found"
+ "startDate"
+ "+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke_2"
+ "@20@0:8I16"
+ "_unregisterFromHearingAccessibilitySettingsUpdate"
+ "hearingProtectionEnabled"
+ "@\"NSArray\""
+ "setEnableHearingAid:"
+ "Rescinded"
+ "Error"
+ "coreBluetoothDevice"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "requiredFrequencyBins"
+ "initWithBluetoothAddress:"
+ "updateWithCloudRecordInfo:"
+ "HP value update for unknown identifier: %!@(MISSING)"
+ "### Hearing Mode Client fetch occlusion result: %!{(MISSING)error}"
+ "_hasOcclusionNotificationsThresholdMet"
+ "hpRegionStatus"
+ "clientFetchOcclusionResultForDeviceIdentifier:featureID:completion:"
+ "areAllRequirementsSatisfied"
+ "writing HA characteristics to peripheral %!@(MISSING)"
+ "-[HMDeviceManager _deviceSetOffListeningModeAllowedIfNeeded:]_block_invoke"
+ "Device identifier: %!@(MISSING), updating noiseSuppression %!f(MISSING) --> %!f(MISSING)"
+ "HMDeviceRecord UUID %!@(MISSING), set Hearing Protection settings value: %!d(MISSING)"
+ "getRegionSupportStatusForFeatureID:"
+ "right"
+ "Device identifier: %!@(MISSING), throttling updates for Hearing Aid Config with timer %!@(MISSING)"
+ "clampedSensitivity"
+ "PassWithGainTableUpdateLeft"
+ "noiseSuppression"
+ "-[HMDeviceManager _occlusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
+ "setPendingOcclusionCompletionsMap:"
+ "_occlusionNotification"
+ "setTitleKey:"
+ "HA characteristic updated from peripheral: %!@(MISSING)"
+ "initWithFeatureIdentifier:healthStore:countryCodeSource:"
+ "isDeviceUsedFor3MonthsOrLess"
+ "### Unable to set occlusionIndicationShown, diagnostic record not found for address: %!@(MISSING)"
+ "left"
+ "decibelHearingLevelUnit"
+ "@\"CUUserNotificationSession\""
+ "_uiNotificationSessionHearingProtection"
+ "setHearingTestRegionStatus:"
+ "Saving HMDeviceCloudRecordInfo for cloud sync %!@(MISSING)"
+ "HMDeviceRecord updated from cloud push: %!@(MISSING)"
+ "containsObject:"
+ "getOnDemandRetestReason"
+ "### Unable fetch occlusion result, no completion handler for identifier: %!@(MISSING)"
+ "v32@0:8^{?=CCS{?=ffffffffffff}{?=ffffffffffff}}16@24"
+ "HMDeviceRecord updated from cloud record: %!@(MISSING)"
+ "caching occlusion result handler %!@(MISSING) for device identifier %!@(MISSING)"
+ "setEnablePMEVoice:"
+ "a4120005-95c5-4d6f-9098-0f0b41457e0a"
+ "updateFaultCountsFromCloudRecord:"
+ "modifyHMDeviceCloudRecordInfo:completion:"
+ "hearingAssistEnrolled"
+ "pendingOcclusionCompletionsMap"
+ "_checkForOcclusionInDiagnosticRecord:forDevice:"
+ "updateHMSettingsStruct:fromAudiogram:"
+ "-[HMDeviceManager _checkForOcclusionInDiagnosticRecord:forDevice:]_block_invoke"
+ "placementMode"
+ "getCloudRecordForCurrentFaultCount"
+ "hearingTestRegionStatus"
+ "Device identifier: %!@(MISSING), updating balance %!f(MISSING) --> %!f(MISSING)"
+ "occlusion-result"
+ "OcclusionIndicationShown with UUID: %!@(MISSING), type: %!s(MISSING), feature: %!s(MISSING), action: %!s(MISSING)"
+ "cloudRecord"
+ "setAudiogramsReported:"
+ "setHmDeviceCloudRecordUpdateHandler:"
+ "-[HMDeviceManager _updateCloudRecords:]_block_invoke"
+ "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
+ "resetFaultCounts"
+ "Dismiss"
+ "HearingModeUserNotifications UINotificationSession action: %!s(MISSING), %!{(MISSING)error}"
+ "getOcclusionResultForFeatureID:"
+ "HKFeatureStatusProvidingObserver"
+ "_setPreferencesForKey:withStringValue:"
+ "amplification"
+ "primaryPlacement"
+ "sensitivity"
+ "OcclusionNotificationShownDate"
+ "Unsupported"
+ "v32@?0@\"NSString\"8@\"HKFeatureStatusManager\"16^B24"
+ "Unable to fetch occlusion result, diagnostic record not found for identifier: %!@(MISSING)"
+ "month"
+ "-[HMDeviceManager _deviceRescindHearingAssist:]_block_invoke"
+ "HMOcclusionNotification"
+ "setOcclusionResult:forFeatureID:"
+ "haRegionStatus"
+ "setSwipeGainEnabled:"
+ "stringFromDate:"
+ "write HA characteristic UUID: %!@(MISSING) not found on %!@(MISSING)"
+ "ANC"
+ "-[HMOcclusionNotification _hasOcclusionNotificationsThresholdMet]"
+ "Supported"
+ "-[HMHealthKitUtilities _isAudiogramValid:]"
+ "bundleForClass:"
+ "mediaAssistEnabled"
+ "\x14\x14"
+ "Hearing Protection Occlusion Notification shown at: %!@(MISSING)"
+ "DiagnosticCheckNeeded"
+ "Fail"
+ "_triggerHearingProtectionOcclusionNotificationIfNeeded:"
+ "hertzUnit"
+ "sending loss for RIGHT ear: loss_01_dBHL: %!l(MISSING)f"
+ "-[HMDeviceManager _hearingAidConfigDataReceived:identifier:]"
+ "hideOffListeningModeCapability"
+ "pathForResource:ofType:"
+ "clientHMAvailableAudiograms:invalidAudiograms:error:"
+ "audioStreamState"
+ "_saveCloudRecordForDevice:withConfig:"
+ "sending loss for LEFT ear: loss_01_dBHL: %!l(MISSING)f"
+ "_featureManagerMap"
- "updateWithHMDeviceRecord:"
- "\x01\x15\x11"
- "\x14\x12"
- "-[HMDeviceManager _distributedNotificationReceived:]_block_invoke_2"
- "\x11"

```
