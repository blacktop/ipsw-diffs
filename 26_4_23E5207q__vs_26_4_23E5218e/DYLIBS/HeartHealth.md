## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

```diff

-6200.5.77.2.6
-  __TEXT.__text: 0x2a8d0
+6200.5.81.2.2
+  __TEXT.__text: 0x2a028
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x2fbc
+  __TEXT.__objc_methlist: 0x2fa4
   __TEXT.__const: 0x272
-  __TEXT.__cstring: 0x365e
+  __TEXT.__cstring: 0x350e
   __TEXT.__oslogstring: 0x1894
   __TEXT.__gcc_except_tab: 0x27c
   __TEXT.__swift5_typeref: 0x23

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xd08
+  __TEXT.__unwind_info: 0xcf8
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0xc9d
-  __TEXT.__objc_methname: 0x8ca2
-  __TEXT.__objc_methtype: 0x1099
-  __TEXT.__objc_stubs: 0x4de0
+  __TEXT.__objc_methname: 0x89b3
+  __TEXT.__objc_methtype: 0x1088
+  __TEXT.__objc_stubs: 0x4ca0
   __DATA_CONST.__got: 0x618
   __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c90
+  __DATA_CONST.__objc_selrefs: 0x1c38
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x370
-  __AUTH_CONST.__cfstring: 0x2d60
+  __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0x5d98
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf00
   __AUTH.__data: 0xa8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EF25A178-CCF1-3B41-8F3E-B0F0A58AA61A
-  Functions: 1228
-  Symbols:   4252
-  CStrings:  2346
+  UUID: 5290F864-3332-3CEA-808F-44497DB05453
+  Functions: 1225
+  Symbols:   4240
+  CStrings:  2304
 
Symbols:
+ _HKHRCardioFitnessAnalyticsActiveWatchProductTypeKey
+ _HKHRCardioFitnessAnalyticsAgeKey
+ _HKHRCardioFitnessAnalyticsBiologicalSexKey
+ _HKHRCardioFitnessAnalyticsFeatureVersionKey
+ _HKHRCardioFitnessAnalyticsIsImproveHealthAndActivityAllowedKey
- -[HKHRCardioFitnessAnalyticsManager _setKey:value:onPayloadIfPresent:]
- -[HKHRCardioFitnessAnalyticsManager submitDailyEventWithSource:deviceContextsDict:]
- ___83-[HKHRCardioFitnessAnalyticsManager submitDailyEventWithSource:deviceContextsDict:]_block_invoke
- ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- _objc_msgSend$_setKey:value:onPayloadIfPresent:
- _objc_msgSend$determineDaysSinceLastLowNotificationWithCurrentDate:isImproveHealthAndActivityAllowed:error:
- _objc_msgSend$determineDaysSinceLastVO2MaxSampleWithCurrentDate:isImproveHealthAndActivityAllowed:error:
- _objc_msgSend$determineIsBlockersEnabledWithIsImproveHealthAndActivityAllowed:error:
- _objc_msgSend$determineIsHeartRateEnabledWithIsImproveHealthAndActivityAllowed:
- _objc_msgSend$determineIsNotificationsEnabled
- _objc_msgSend$determineIsWristDetectionEnabledWithIsImproveHealthAndActivityAllowed:
- _objc_msgSend$determineNumberOfLowNotificationsInPastYearWithCurrentDate:isImproveHealthAndActivityAllowed:error:
- _objc_msgSend$determineWeeksSinceOnboardingWithCurrentDate:error:
- _objc_msgSend$latestClassificationWithIsOnboarded:isImproveHealthAndActivityAllowed:error:
CStrings:
+ "253f2ed0-ffc6-4d36-a387-b6965c9e4682"
+ "a0a8cbbd-8f56-46ed-a36b-446d452c0515"
- "253F2ED0-332F-481C-B7DE-7E80973B07BF"
- "A0A8CBBD-332F-481C-B7DE-7E80973B07BF"
- "_setKey:value:onPayloadIfPresent:"
- "assignedClassification"
- "com.apple.Health.Cardio.Fitness.Daily"
- "countPairedVisionPro"
- "countPairedWatch"
- "countPairediPad"
- "countPairediPhone"
- "daysSinceLastLowNotification"
- "daysSinceLastVO2MaxSample"
- "determineDaysSinceLastLowNotificationWithCurrentDate:isImproveHealthAndActivityAllowed:error:"
- "determineDaysSinceLastVO2MaxSampleWithCurrentDate:isImproveHealthAndActivityAllowed:error:"
- "determineIsBlockersEnabledWithIsImproveHealthAndActivityAllowed:error:"
- "determineIsHeartRateEnabledWithIsImproveHealthAndActivityAllowed:"
- "determineIsNotificationsEnabled"
- "determineIsWristDetectionEnabledWithIsImproveHealthAndActivityAllowed:"
- "determineNumberOfLowNotificationsInPastYearWithCurrentDate:isImproveHealthAndActivityAllowed:error:"
- "determineWeeksSinceOnboardingWithCurrentDate:error:"
- "isBlockersEnabled"
- "latestClassificationWithIsOnboarded:isImproveHealthAndActivityAllowed:error:"
- "notificationsEnabled"
- "numberOfLowNotificationsInPastYear"
- "onboardedVersion"
- "submitDailyEventWithSource:deviceContextsDict:"
- "v40@0:8@16@24@32"
- "weeksSinceOnboarding"

```
