## HealthHearing

> `/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x40b4
-  __TEXT.__auth_stubs: 0x370
+7027.0.52.2.6
+  __TEXT.__text: 0x3e20
   __TEXT.__objc_methlist: 0x504
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x493
+  __TEXT.__cstring: 0x496
   __TEXT.__oslogstring: 0x1fd
-  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__gcc_except_tab: 0x94
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0x1216
-  __TEXT.__objc_methtype: 0x2bb
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x500
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x188
   __DATA.__bss: 0xa0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4E44A91-13C6-3A3F-8851-49FFC818D455
-  Functions: 108
-  Symbols:   516
-  CStrings:  287
+  UUID: CA3D8963-DDC6-3CAE-8C51-A94C198719FC
+  Functions: 106
+  Symbols:   514
+  CStrings:  79
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"HKProxyProvider\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCInterface\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@36@0:8@16B24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8d16d24^@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "B36@0:8@16B24@28"
- "B36@0:8@16B24^@28"
- "B40@0:8@16B24B28^@32"
- "HKHeadphoneAudioExposureControl"
- "HKHeadphoneAudioExposureControlClient"
- "HKHeadphoneAudioExposureControlServer"
- "HKHearingFeatures"
- "HeadphoneSevenDayDose"
- "HealthHearing"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_HKXPCExportable"
- "_adasPreferenceDidChange:"
- "_boolForPreferenceKey:defaultValue:fromValues:"
- "_isHeadphoneExposureDataTransient"
- "_isHeadphoneExposureDataTransientOnActiveWatchWithError:"
- "_isLocalDevice"
- "_isMeasureOtherHeadphonesEnabled"
- "_isMeasureOtherHeadphonesEnabledOnActiveWatchWithError:"
- "_numbersForPhonePreferenceKeys:"
- "_numbersForPreferenceKeys:error:"
- "_numbersForPreferenceKeys:fromActiveWatch:"
- "_numbersForWatchPreferenceKeys:"
- "_proxyProvider"
- "_setBoolForPhonePreferenceKey:newValue:error:"
- "_setBoolForPreferenceKey:newValue:error:"
- "_setBoolForWatchPreferenceKey:newValue:error:"
- "_setHeadphoneExposureMeasureLevelsEnabled:error:"
- "_setHeadphoneExposureMeasureLevelsEnabledOnActiveWatch:error:"
- "_setHeadphoneExposureNotificationsEnabled:error:"
- "_setHeadphoneExposureNotificationsEnabledOnActiveWatch:error:"
- "_sevenDayDoseWithExposureAverageQuantity:duration:error:"
- "_sharedAudioDataAnalysisManager"
- "_startObservingForChanges"
- "_startObservingForChangesOnActiveWatch"
- "_stopObservingForChanges"
- "_unit"
- "activePairedDevice"
- "areHeadphoneExposureNotificationsMandatory"
- "areHeadphoneExposureNotificationsMandatoryOnActiveWatchWithError:"
- "arrayWithObjects:count:"
- "autorelease"
- "averageQuantity"
- "boolValue"
- "categorySampleWithType:value:startDate:endDate:device:metadata:"
- "categoryType"
- "categoryTypeForIdentifier:"
- "class"
- "clientQueueActionHandlerWithCompletion:"
- "clientQueueObjectHandlerWithCompletion:"
- "code"
- "compare:"
- "conformsToProtocol:"
- "connectionConfigured"
- "connectionInterrupted"
- "connectionInvalidated"
- "containsObject:"
- "copyWithZone:"
- "currentHandler"
- "dateByAddingTimeInterval:"
- "dealloc"
- "debugDescription"
- "decibelAWeightedSoundPressureLevelUnit"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "doubleValueForUnit:"
- "duration"
- "endDate"
- "exportedInterface"
- "fetchDoseLimitInfoWithCompletion:"
- "fetchInfoWithCompletion:"
- "fetchProxyWithHandler:errorHandler:"
- "getActivePairedDevice"
- "getNanoPreferencesFor:"
- "getPreferencesFor:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasActivePairedDevice"
- "hash"
- "hearing_audioDSP_isHAENDisabled"
- "hearing_isExpectedError"
- "hk_assignError:code:description:"
- "hk_assignError:code:format:"
- "hk_canTriggerHeadphoneExposureNotification"
- "hk_hearingSevenDayDoseDateIntervalClampedToMaxDuration"
- "hk_hearingSevenDayDoseDateIntervalEndingBeforeDate:error:"
- "hk_hearingSevenDayDosePercentageWithError:"
- "hk_isDatabaseAccessibilityError"
- "hk_isFeatureDisabledError"
- "hk_isHealthStoreUnavailableError"
- "hk_isHearingSevenDayDoseNotification"
- "hk_safeValueForKeyPath:class:error:"
- "hk_sevenDayDoseWithExposureLevel:exposureDuration:error:"
- "init"
- "initWithBool:"
- "initWithHealthStore:"
- "initWithHealthStore:taskIdentifier:exportedObject:taskUUID:"
- "initWithStartDate:duration:"
- "initWithStartDate:endDate:"
- "initWithUUIDString:"
- "insertQuantityWithExposure:duration:startDate:includesNotificationSample:synced:completion:"
- "interfaceWithProtocol:"
- "intersectionWithDateInterval:"
- "isCompatibleWithUnit:"
- "isEqual:"
- "isEqualToString:"
- "isHAENFeatureEnabled"
- "isHeadphoneExposureMeasureLevelsEnabled"
- "isHeadphoneExposureMeasureLevelsEnabledOnActiveWatchWithError:"
- "isHeadphoneExposureNotificationsEnabled"
- "isHeadphoneExposureNotificationsEnabledOnActiveWatchWithError:"
- "isHeadphoneExposureNotificationsSupportedOnActiveWatch"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "maximumAllowedDuration"
- "maximumDurationInSecondsForLEQ:days:"
- "metadata"
- "numberWithBool:"
- "numberWithDouble:"
- "objectForKeyedSubscript:"
- "overrideDoseLimit:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:userInfo:"
- "quantityType"
- "quantityTypeForIdentifier:"
- "rebuildWithCompletion:"
- "release"
- "remoteInterface"
- "remote_fetchDoseLimitWithCompletion:"
- "remote_fetchInfoDictWithCompletion:"
- "remote_fetchInfoWithCompletion:"
- "remote_insertQuantityWithExposure:duration:startDate:includesNotificationSample:synced:completion:"
- "remote_overrideDoseLimit:completion:"
- "remote_rebuildWithCompletion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "secondUnit"
- "self"
- "setBoolForPreferenceKey:newValue:forPairedWatch:error:"
- "setNanoPreferenceFor:value:notify:"
- "setPreferenceFor:value:notify:"
- "setShouldRetryOnInterruption:"
- "sharedInstance"
- "source"
- "sourceRevision"
- "startDate"
- "startObservingForChanges"
- "stringWithUTF8String:"
- "superclass"
- "supportsCapability:"
- "swizzled_isHAENFeatureEnabled"
- "taskIdentifier"
- "unitTesting_forceDefaultHeadphoneDataCollectionInterval"
- "unitTesting_hearingSevenDayDoseCategorySampleWithNow:includesPrunableData:error:"
- "unitTesting_overrideForceDefaultHeadphoneDataCollectionInterval:"
- "unitTesting_overrideIsHeadphoneExposureNotificationsEnabled:"
- "unitTesting_overrideSimulateLocalHeadphonePlayback:"
- "unitTesting_simulateLocalHeadphonePlayback"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v32@0:8@\"NSNumber\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v56@0:8d16d24@\"NSDate\"32B40B44@?<v@?B@\"NSError\">48"
- "v56@0:8d16d24@32B40B44@?48"
- "value"
- "zone"

```
