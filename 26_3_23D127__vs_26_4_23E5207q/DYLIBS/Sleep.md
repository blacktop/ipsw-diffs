## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x59310
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x73e4
-  __TEXT.__const: 0x250
+6200.5.77.2.6
+  __TEXT.__text: 0x5d598
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x754c
+  __TEXT.__const: 0x260
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0x4c21
-  __TEXT.__gcc_except_tab: 0x8dc
-  __TEXT.__oslogstring: 0x4306
-  __TEXT.__unwind_info: 0x1c10
-  __TEXT.__objc_classname: 0xf0f
-  __TEXT.__objc_methname: 0x1173e
-  __TEXT.__objc_methtype: 0x2549
-  __TEXT.__objc_stubs: 0xa600
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x2ba0
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__cstring: 0x4d4b
+  __TEXT.__gcc_except_tab: 0x8f0
+  __TEXT.__oslogstring: 0x4445
+  __TEXT.__unwind_info: 0x1d10
+  __TEXT.__objc_classname: 0xf3a
+  __TEXT.__objc_methname: 0x11982
+  __TEXT.__objc_methtype: 0x2589
+  __TEXT.__objc_stubs: 0xa700
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x2c88
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3808
+  __DATA_CONST.__objc_selrefs: 0x3868
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0xbda8
+  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x5380
+  __AUTH_CONST.__objc_const: 0xc018
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x5ec
+  __DATA.__objc_ivar: 0x62c
   __DATA.__data: 0x14a0
-  __DATA_DIRTY.__objc_ivar: 0x64
-  __DATA_DIRTY.__objc_data: 0x14f0
+  __DATA_DIRTY.__objc_ivar: 0x34
+  __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__bss: 0x128
-  __DATA_DIRTY.__common: 0xb8
+  __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E217B06-6485-34EF-BAE5-8D29E3780D5A
-  Functions: 2710
-  Symbols:   8982
-  CStrings:  4801
+  UUID: D5655902-2990-36CC-B3DF-17DDE1504D42
+  Functions: 2745
+  Symbols:   9074
+  CStrings:  4850
 
Symbols:
+ -[HKSPAlarmConfiguration coordinationPolicy]
+ -[HKSPAlarmConfiguration unknownProperties]
+ -[HKSPDictionaryDeserializer hksp_decodeUnknownPropertiesForObject:]
+ -[HKSPDictionarySerializer hksp_encodeUnknownPropertiesForObject:]
+ -[HKSPFeatureAvailabilityStore activePairedDeviceSupportsAlertCoordination]
+ -[HKSPFeatureAvailabilityStore activePairedDeviceSupportsSleep]
+ -[HKSPFeatureAvailabilityStore hasActivePairedDevice]
+ -[HKSPMutableAlarmConfiguration coordinationPolicy]
+ -[HKSPMutableAlarmConfiguration setCoordinationPolicy:]
+ -[HKSPMutableAlarmConfiguration unknownProperties]
+ -[HKSPMutableSleepScheduleDayOccurrence unknownProperties]
+ -[HKSPOverrideOccurrenceGenerationResult copyWithZone:]
+ -[HKSPOverrideOccurrenceGenerationResult date]
+ -[HKSPOverrideOccurrenceGenerationResult descriptionBuilderWithMultilinePrefix:]
+ -[HKSPOverrideOccurrenceGenerationResult descriptionWithMultilinePrefix:]
+ -[HKSPOverrideOccurrenceGenerationResult description]
+ -[HKSPOverrideOccurrenceGenerationResult generatedOccurrenceCouldBeEarlier]
+ -[HKSPOverrideOccurrenceGenerationResult generatedOccurrence]
+ -[HKSPOverrideOccurrenceGenerationResult gregorianCalendar]
+ -[HKSPOverrideOccurrenceGenerationResult hash]
+ -[HKSPOverrideOccurrenceGenerationResult initWithDate:gregorianCalendar:generatedOccurrence:upcomingOccurrence:]
+ -[HKSPOverrideOccurrenceGenerationResult isEqual:]
+ -[HKSPOverrideOccurrenceGenerationResult succinctDescriptionBuilder]
+ -[HKSPOverrideOccurrenceGenerationResult succinctDescription]
+ -[HKSPOverrideOccurrenceGenerationResult upcomingOccurrence]
+ -[HKSPOverrideOccurrenceGenerationResult wasGeneratedFromUpcomingOccurrence]
+ -[HKSPResolvedSleepScheduleOccurrence overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:]
+ -[HKSPSleepScheduleDayOccurrence unknownProperties]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceForCurrentDate:gregorianCalendar:]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceForCurrentDate:gregorianCalendar:schedule:]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceFromTemplateForCurrentDate:]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:mutableOccurrence:]
+ -[HKSPSleepScheduleModel(OverrideGeneration) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:schedule:]
+ -[NSCoder(HKSPSerialization) hksp_decodeUnknownPropertiesForObject:]
+ -[NSCoder(HKSPSerialization) hksp_encodeUnknownPropertiesForObject:]
+ -[_HKBehavior(HKSPSleep) hksp_activePairedDeviceSupportsAlertCoordination]
+ -[_HKSPUnknownProperties copyValueFromObject:toObject:]
+ -[_HKSPUnknownProperties decodeValueForObject:fromCoder:]
+ -[_HKSPUnknownProperties encodeValueForObject:fromCoder:]
+ -[_HKSPUnknownProperties init]
+ GCC_except_table54
+ _.str.340
+ _.str.352
+ _.str.364
+ _.str.365
+ _.str.376
+ _.str.377
+ _.str.445
+ _HKSPAlarmCoordinationPolicyKey
+ _HKSPSleepLogCategoryOverride
+ _NSSelectorFromString
+ _NSStringFromHKSPAlarmCoordinationPolicy
+ _OBJC_CLASS_$__HKSPUnknownProperties
+ _OBJC_IVAR_$_HKSPAlarmConfiguration._coordinationPolicy
+ _OBJC_IVAR_$_HKSPAlarmConfiguration._unknownProperties
+ _OBJC_IVAR_$_HKSPMutableAlarmConfiguration._changeSet
+ _OBJC_IVAR_$_HKSPMutableAlarmConfiguration._originalObject
+ _OBJC_IVAR_$_HKSPMutableSleepEventRecord._changeSet
+ _OBJC_IVAR_$_HKSPMutableSleepEventRecord._originalObject
+ _OBJC_IVAR_$_HKSPMutableSleepSchedule._changeSet
+ _OBJC_IVAR_$_HKSPMutableSleepSchedule._originalObject
+ _OBJC_IVAR_$_HKSPMutableSleepScheduleDayOccurrence._changeSet
+ _OBJC_IVAR_$_HKSPMutableSleepScheduleDayOccurrence._originalObject
+ _OBJC_IVAR_$_HKSPMutableSleepScheduleOccurrence._changeSet
+ _OBJC_IVAR_$_HKSPMutableSleepScheduleOccurrence._originalObject
+ _OBJC_IVAR_$_HKSPMutableSleepSettings._changeSet
+ _OBJC_IVAR_$_HKSPMutableSleepSettings._originalObject
+ _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._date
+ _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._generatedOccurrence
+ _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._gregorianCalendar
+ _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._upcomingOccurrence
+ _OBJC_IVAR_$_HKSPSleepScheduleDayOccurrence._unknownProperties
+ _OBJC_METACLASS_$__HKSPUnknownProperties
+ __OBJC_$_INSTANCE_METHODS_HKSPSleepScheduleModel(OverrideGeneration|EventRecord|Notifications)
+ __OBJC_$_INSTANCE_METHODS__HKSPUnknownProperties
+ __OBJC_CLASS_PROTOCOLS_$_HKSPOverrideOccurrenceGenerationResult
+ __OBJC_CLASS_RO_$__HKSPUnknownProperties
+ __OBJC_METACLASS_RO_$__HKSPUnknownProperties
+ ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.341
+ ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.342
+ ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.540
+ ___39-[HKSPXPCConnectionProvider connection]_block_invoke.354
+ ___40-[HKSPDiagnostics _registerStateHandler]_block_invoke.342
+ ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke.350
+ ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2.351
+ ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.542
+ ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.541
+ ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.550
+ ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.371
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.370
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.372
+ ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.538
+ ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.406
+ ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.545
+ ___50-[HKSPOverrideOccurrenceGenerationResult isEqual:]_block_invoke
+ ___50-[HKSPOverrideOccurrenceGenerationResult isEqual:]_block_invoke_2
+ ___50-[HKSPOverrideOccurrenceGenerationResult isEqual:]_block_invoke_3
+ ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.368
+ ___52-[HKSPSleepStore _getSleepScheduleFromServerDoSync:]_block_invoke.394
+ ___52-[HKSPSleepStore _getSleepSettingsFromServerDoSync:]_block_invoke.399
+ ___55-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:]_block_invoke.401
+ ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.411
+ ___57-[HKSPSleepStore _getSleepScheduleModelFromServerDoSync:]_block_invoke.403
+ ___57-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:]_block_invoke.413
+ ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.552
+ ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.549
+ ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.414
+ ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.437
+ ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.537
+ ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.543
+ ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.544
+ ___64-[HKSPXPCConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.344
+ ___68-[HKSPDictionaryDeserializer hksp_decodeUnknownPropertiesForObject:]_block_invoke
+ ___68-[HKSPDictionaryDeserializer hksp_decodeUnknownPropertiesForObject:]_block_invoke_2
+ ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.547
+ ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.548
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.343
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.348
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke_2.350
+ ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.355
+ ___block_descriptor_40_e8_32s_e41_"HKSPMutableSleepScheduleOccurrence"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e42_"HKSPResolvedSleepScheduleOccurrence"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e44_B24?0"NSString"8"<NSCopying><NSCoding>"16ls32l8
+ ___block_literal_global.342
+ ___block_literal_global.345
+ ___block_literal_global.348
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.357
+ ___block_literal_global.363
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.376
+ ___block_literal_global.378
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.409
+ ___block_literal_global.430
+ ___block_literal_global.448
+ ___block_literal_global.472
+ ___block_literal_global.612
+ ___block_literal_global.614
+ _objc_msgSend$coordinationPolicy
+ _objc_msgSend$generatedOccurrence
+ _objc_msgSend$generatedOccurrenceCouldBeEarlier
+ _objc_msgSend$hksp_decodeUnknownPropertiesForObject:
+ _objc_msgSend$hksp_encodeUnknownPropertiesForObject:
+ _objc_msgSend$initWithDate:gregorianCalendar:generatedOccurrence:upcomingOccurrence:
+ _objc_msgSend$isFeatureCapabilitySupportedOnActivePairedDeviceWithError:
+ _objc_msgSend$na_setByRemovingObjectsFromSet:
+ _objc_msgSend$overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:
+ _objc_msgSend$setCoordinationPolicy:
+ _objc_msgSend$unknownProperties
+ _objc_msgSend$upcomingOccurrence
- -[HKSPOverrideOccurrenceGenerationResult overrideOccurrence]
- -[HKSPOverrideOccurrenceGenerationResult setOverrideOccurrence:]
- -[HKSPOverrideOccurrenceGenerationResult setUpcomingOccurrenceWasOverride:]
- -[HKSPOverrideOccurrenceGenerationResult setWasGeneratedFromTemplate:]
- -[HKSPOverrideOccurrenceGenerationResult wasGeneratedFromTemplate]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceForCurrentDate:gregorianCalendar:]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceForCurrentDate:gregorianCalendar:schedule:]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceFromTemplateForCurrentDate:]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:mutableOccurrence:]
- -[HKSPSleepScheduleModel(EventRecord) generateOverrideOccurrenceFromTemplateForCurrentDate:gregorianCalendar:schedule:]
- -[HKSPSleepScheduleModel(EventRecord) overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:schedule:]
- GCC_except_table48
- _.str.301
- _.str.313
- _.str.324
- _.str.325
- _.str.337
- _.str.338
- _.str.402
- _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._overrideOccurrence
- _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._upcomingOccurrenceWasOverride
- _OBJC_IVAR_$_HKSPOverrideOccurrenceGenerationResult._wasGeneratedFromTemplate
- __OBJC_$_INSTANCE_METHODS_HKSPSleepScheduleModel(EventRecord|Notifications)
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.302
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.303
- ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.497
- ___39-[HKSPXPCConnectionProvider connection]_block_invoke.315
- ___40-[HKSPDiagnostics _registerStateHandler]_block_invoke.303
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke.311
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2.312
- ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.499
- ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.498
- ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.507
- ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.332
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.331
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.333
- ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.495
- ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.367
- ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.502
- ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.329
- ___52-[HKSPSleepStore _getSleepScheduleFromServerDoSync:]_block_invoke.355
- ___52-[HKSPSleepStore _getSleepSettingsFromServerDoSync:]_block_invoke.360
- ___55-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:]_block_invoke.362
- ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.372
- ___57-[HKSPSleepStore _getSleepScheduleModelFromServerDoSync:]_block_invoke.364
- ___57-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:]_block_invoke.374
- ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.509
- ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.506
- ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.375
- ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.398
- ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.494
- ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.500
- ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.501
- ___64-[HKSPXPCConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.305
- ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.504
- ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.505
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.304
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.309
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke_2.311
- ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.316
- ___block_literal_global.303
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.324
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.347
- ___block_literal_global.364
- ___block_literal_global.370
- ___block_literal_global.391
- ___block_literal_global.394
- ___block_literal_global.405
- ___block_literal_global.569
- ___block_literal_global.571
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:schedule:
- _objc_msgSend$setOverrideOccurrence:
- _objc_msgSend$setUpcomingOccurrenceWasOverride:
- _objc_msgSend$setWasGeneratedFromTemplate:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "!3"
+ "@\"HKSPMutableSleepScheduleOccurrence\"8@?0"
+ "@\"HKSPResolvedSleepScheduleOccurrence\"8@?0"
+ "@\"NSDictionary\"24@0:8@\"<HKSPObject>\"16"
+ "A70EA46D-332F-481C-B7DE-7E80973B07BF"
+ "B24@?0@\"NSString\"8@\"<NSCopying><NSCoding>\"16"
+ "C0F3C2C3-332F-481C-B7DE-7E80973B07BF"
+ "D0482616-332F-481C-B7DE-7E80973B07BF"
+ "E49AA0D4-332F-481C-B7DE-7E80973B07BF"
+ "FFDA9C57-332F-481C-B7DE-7E80973B07BF"
+ "HKSPAlarmCoordinationPolicy"
+ "OptIn"
+ "OptOut"
+ "OverrideGeneration"
+ "T@\"HKSPMutableSleepScheduleOccurrence\",R,C,N,V_generatedOccurrence"
+ "T@\"HKSPResolvedSleepScheduleOccurrence\",R,C,N,V_upcomingOccurrence"
+ "T@\"NSCalendar\",R,C,N,V_gregorianCalendar"
+ "T@\"NSDate\",R,C,N,V_date"
+ "T@\"NSDictionary\",?,R,C,N"
+ "T@\"NSDictionary\",?,R,C,N,V_unknownProperties"
+ "TQ,R,N,V_coordinationPolicy"
+ "[%{public}@] determining template date for override generation on date: %{public}@"
+ "[%{public}@] generated override occurrence: %{public}@"
+ "[%{public}@] generated result: %{public}@"
+ "[%{public}@] generating override occurrence from %{public}@ for current date %{public}@"
+ "[%{public}@] note: generated override potentially should have been earlier..."
+ "[%{public}@] using template date: %{public}@"
+ "_HKSPUnknownProperties"
+ "_coordinationPolicy"
+ "_generatedOccurrence"
+ "_gregorianCalendar"
+ "_unknownProperties"
+ "_upcomingOccurrence"
+ "activePairedDeviceSupportsAlertCoordination"
+ "activePairedDeviceSupportsSleep"
+ "coordinationPolicy"
+ "generatedOccurrence"
+ "generatedOccurrenceCouldBeEarlier"
+ "gregorianCalendar"
+ "hasActivePairedDevice"
+ "hksp_activePairedDeviceSupportsAlertCoordination"
+ "hksp_decodeUnknownPropertiesForObject:"
+ "hksp_encodeUnknownPropertiesForObject:"
+ "initWithDate:gregorianCalendar:generatedOccurrence:upcomingOccurrence:"
+ "na_setByRemovingObjectsFromSet:"
+ "override"
+ "overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:"
+ "setCoordinationPolicy:"
+ "unknownProperties"
+ "upcomingOccurrence"
+ "v24@0:8@\"<HKSPObject>\"16"
+ "wasGeneratedFromUpcomingOccurrence"
- "A70EA46D-407A-4723-A8EF-CFF5DFB423B4"
- "C"
- "C0F3C2C3-0CDE-4DF9-A95A-789AC9A0348B"
- "E49AA0D4-4AA5-47C3-9272-4644AF0E6FA9"
- "FFDA9C57-8508-4B50-B6D8-EEE862251FC0"
- "T@\"HKSPMutableSleepScheduleOccurrence\",&,N,V_overrideOccurrence"
- "TB,N,V_upcomingOccurrenceWasOverride"
- "TB,N,V_wasGeneratedFromTemplate"
- "[%{public}@] generating override occurrence for current date %{public}@"
- "_overrideOccurrence"
- "_upcomingOccurrenceWasOverride"
- "_wasGeneratedFromTemplate"
- "overrideOccurrenceGenerationResultForCurrentDate:gregorianCalendar:schedule:"
- "setOverrideOccurrence:"
- "setUpcomingOccurrenceWasOverride:"
- "setWasGeneratedFromTemplate:"
- "wasGeneratedFromTemplate"

```
