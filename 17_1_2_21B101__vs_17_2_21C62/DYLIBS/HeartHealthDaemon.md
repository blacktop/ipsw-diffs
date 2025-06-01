## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x42628
+4146.2.12.1.3
+  __TEXT.__text: 0x424d8
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x2af0
+  __TEXT.__objc_methlist: 0x2af8
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x54c
-  __TEXT.__cstring: 0x2e63
-  __TEXT.__oslogstring: 0x770e
-  __TEXT.__unwind_info: 0xf0c
-  __TEXT.__objc_classname: 0x1550
-  __TEXT.__objc_methname: 0xbf7a
+  __TEXT.__cstring: 0x2e24
+  __TEXT.__oslogstring: 0x76d1
+  __TEXT.__unwind_info: 0xf04
+  __TEXT.__objc_classname: 0x157c
+  __TEXT.__objc_methname: 0xbf3a
   __TEXT.__objc_methtype: 0x2d68
-  __TEXT.__objc_stubs: 0x77e0
+  __TEXT.__objc_stubs: 0x7760
   __DATA_CONST.__got: 0x540
   __DATA_CONST.__const: 0xe20
   __DATA_CONST.__objc_classlist: 0x220

   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x63d0
-  __DATA_CONST.__objc_selrefs: 0x22e0
-  __DATA_CONST.__objc_arraydata: 0x458
+  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_arraydata: 0x480
   __AUTH_CONST.__objc_const: 0x1880
-  __AUTH_CONST.__cfstring: 0x2920
+  __AUTH_CONST.__cfstring: 0x2900
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__objc_intobj: 0xbe8
+  __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_doubleobj: 0x3d0
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0x5f0
+  __AUTH.__objc_data: 0x640
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x620
   __DATA.__objc_superrefs: 0x1d0
   __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x1810
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0xf00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 661B6382-79C4-317B-BB2A-C7E11A9F16B4
-  Functions: 1360
-  Symbols:   5413
-  CStrings:  3035
+  UUID: 371BF6B5-2C95-3644-9A50-AF0277335BD0
+  Functions: 1359
+  Symbols:   5409
+  CStrings:  3028
 
Symbols:
+ +[HKCountrySet(HKFeatureIdentifierElectrocardiogramRecordingV2) localAvailabilityForHKFeatureIdentifierElectrocardiogramRecordingV2]
+ -[HDHeartProfileExtension .cxx_destruct]
+ -[HDHeartProfileExtension _setupElectrocardiogramRecordingWithProfile:]
+ -[HDHeartProfileExtension aFibBurdenComponents]
+ -[HDHeartProfileExtension dailyHeartRateManager]
+ -[HDHeartProfileExtension featureAvailabilityExtensionForFeatureIdentifier:]
+ -[HDHeartProfileExtension healthLiteDataCollector]
+ -[HDHeartProfileExtension heartNotificationsUserDefaults]
+ -[HDHeartProfileExtension heartRateDataManager]
+ -[HDHeartProfileExtension heartRateNotificationManager]
+ -[HDHeartProfileExtension initWithProfile:heartNotificationsUserDefaults:]
+ -[HDHeartProfileExtension irregularRhythmNotificationsFeatureStatusManager]
+ -[HDHeartProfileExtension profileDidBecomeReady:]
+ -[HDHeartProfileExtension profile]
+ -[HDHeartProfileExtension setAFibBurdenComponents:]
+ -[HDHeartProfileExtension setDailyHeartRateManager:]
+ -[HDHeartProfileExtension setHealthLiteDataCollector:]
+ -[HDHeartProfileExtension setHeartNotificationsUserDefaults:]
+ -[HDHeartProfileExtension setHeartRateDataManager:]
+ -[HDHeartProfileExtension setHeartRateNotificationManager:]
+ _OBJC_CLASS_$_HDHeartProfileExtension
+ _OBJC_IVAR_$_HDHeartProfileExtension._aFibBurdenComponents
+ _OBJC_IVAR_$_HDHeartProfileExtension._cardioFitnessBackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._cardioFitnessFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._dailyAnalyticsActivity
+ _OBJC_IVAR_$_HDHeartProfileExtension._dailyHeartRateManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._electrocardiogramRecordingAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._electrocardiogramRecordingV2DeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._healthLiteDataCollector
+ _OBJC_IVAR_$_HDHeartProfileExtension._heartNotificationsUserDefaults
+ _OBJC_IVAR_$_HDHeartProfileExtension._heartRateDataManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._heartRateNotificationManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._heartbeatSeriesFeatureExclusivityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._highHeartRateNotificationsFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._irregularRhythmNotificationsAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._irregularRhythmNotificationsFeatureStatusManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._irregularRhythmNotificationsSettingMigrator
+ _OBJC_IVAR_$_HDHeartProfileExtension._irregularRhythmNotificationsV2DeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._lowHeartRateNotificationsFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._profile
+ _OBJC_METACLASS_$_HDHeartProfileExtension
+ __OBJC_$_CLASS_METHODS_HKCountrySet(IrregularRhythmNotificationsV2|HKFeatureIdentifierElectrocardiogramRecordingV2)
+ __OBJC_$_INSTANCE_METHODS_HDHeartProfileExtension
+ __OBJC_$_INSTANCE_VARIABLES_HDHeartProfileExtension
+ __OBJC_$_PROP_LIST_HDHeartProfileExtension
+ __OBJC_CLASS_PROTOCOLS_$_HDHeartProfileExtension
+ __OBJC_CLASS_RO_$_HDHeartProfileExtension
+ __OBJC_METACLASS_RO_$_HDHeartProfileExtension
+ _objc_msgSend$localAvailabilityForHKFeatureIdentifierElectrocardiogramRecordingV2
- -[HDHeartRateProfileExtension .cxx_destruct]
- -[HDHeartRateProfileExtension _setupElectrocardiogramRecordingWithProfile:]
- -[HDHeartRateProfileExtension aFibBurdenComponents]
- -[HDHeartRateProfileExtension dailyHeartRateManager]
- -[HDHeartRateProfileExtension featureAvailabilityExtensionForFeatureIdentifier:]
- -[HDHeartRateProfileExtension healthLiteDataCollector]
- -[HDHeartRateProfileExtension heartNotificationsUserDefaults]
- -[HDHeartRateProfileExtension heartRateDataManager]
- -[HDHeartRateProfileExtension heartRateNotificationManager]
- -[HDHeartRateProfileExtension initWithProfile:heartNotificationsUserDefaults:]
- -[HDHeartRateProfileExtension irregularRhythmNotificationsFeatureStatusManager]
- -[HDHeartRateProfileExtension profileDidBecomeReady:]
- -[HDHeartRateProfileExtension profile]
- -[HDHeartRateProfileExtension setAFibBurdenComponents:]
- -[HDHeartRateProfileExtension setDailyHeartRateManager:]
- -[HDHeartRateProfileExtension setHealthLiteDataCollector:]
- -[HDHeartRateProfileExtension setHeartNotificationsUserDefaults:]
- -[HDHeartRateProfileExtension setHeartRateDataManager:]
- -[HDHeartRateProfileExtension setHeartRateNotificationManager:]
- _HKHRElectrocardiogramRecordingV2AllowedCountrySet
- _HKHRElectrocardiogramRecordingV2AllowedCountrySet.cold.1
- _OBJC_CLASS_$_HDHeartRateProfileExtension
- _OBJC_IVAR_$_HDHeartRateProfileExtension._aFibBurdenComponents
- _OBJC_IVAR_$_HDHeartRateProfileExtension._cardioFitnessBackgroundFeatureDeliveryManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._cardioFitnessFeatureAvailabilityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._dailyAnalyticsActivity
- _OBJC_IVAR_$_HDHeartRateProfileExtension._dailyHeartRateManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._electrocardiogramRecordingAvailabilityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._electrocardiogramRecordingV2DeliveryManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._healthLiteDataCollector
- _OBJC_IVAR_$_HDHeartRateProfileExtension._heartNotificationsUserDefaults
- _OBJC_IVAR_$_HDHeartRateProfileExtension._heartRateDataManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._heartRateNotificationManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._heartbeatSeriesFeatureExclusivityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._highHeartRateNotificationsFeatureAvailabilityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._irregularRhythmNotificationsAvailabilityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._irregularRhythmNotificationsFeatureStatusManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._irregularRhythmNotificationsSettingMigrator
- _OBJC_IVAR_$_HDHeartRateProfileExtension._irregularRhythmNotificationsV2DeliveryManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._lowHeartRateNotificationsFeatureAvailabilityManager
- _OBJC_IVAR_$_HDHeartRateProfileExtension._profile
- _OBJC_METACLASS_$_HDHeartRateProfileExtension
- __OBJC_$_CLASS_METHODS_HKCountrySet(IrregularRhythmNotificationsV2)
- __OBJC_$_INSTANCE_METHODS_HDHeartRateProfileExtension
- __OBJC_$_INSTANCE_VARIABLES_HDHeartRateProfileExtension
- __OBJC_$_PROP_LIST_HDHeartRateProfileExtension
- __OBJC_CLASS_PROTOCOLS_$_HDHeartRateProfileExtension
- __OBJC_CLASS_RO_$_HDHeartRateProfileExtension
- __OBJC_METACLASS_RO_$_HDHeartRateProfileExtension
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$URLByAppendingPathExtension:
- _objc_msgSend$countrySetWithPlistURL:error:
- _objc_msgSend$emptyCountrySet
- _objc_msgSend$fileURLWithPath:isDirectory:
CStrings:
+ "HDHeartProfileExtension"
+ "HKCountrySet+HKFeatureIdentifierElectrocardiogramRecordingV2.m"
+ "HKFeatureIdentifierElectrocardiogramRecordingV2"
+ "localAvailabilityForHKFeatureIdentifierElectrocardiogramRecordingV2"
- "/System/Library/Health/AvailableRegions"
- "HDHeartRateProfileExtension"
- "HKCountrySet * _Nonnull HKHRElectrocardiogramRecordingV2AllowedCountrySet(void)"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "[%{public}s] Failed to load ECG2 country list with error: %@"
- "countrySetWithPlistURL:error:"
- "emptyCountrySet"
- "fileURLWithPath:isDirectory:"
- "plist"

```
