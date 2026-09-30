## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Versions/A/Sleep`

```diff

-5200.3.6.0.0
-  __TEXT.__text: 0x60498
+5200.4.25.0.0
+  __TEXT.__text: 0x60c2c
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x654c
-  __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x4649
+  __TEXT.__objc_methlist: 0x718c
+  __TEXT.__const: 0x1b0
+  __TEXT.__cstring: 0x4741
   __TEXT.__gcc_except_tab: 0x898
   __TEXT.__oslogstring: 0x440e
   __TEXT.__unwind_info: 0x1c58
-  __TEXT.__objc_classname: 0xe1d
-  __TEXT.__objc_methname: 0x10c12
-  __TEXT.__objc_methtype: 0x23ce
-  __TEXT.__objc_stubs: 0xa1c0
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0xf40
-  __DATA_CONST.__objc_classlist: 0x2e8
+  __TEXT.__objc_classname: 0xe4e
+  __TEXT.__objc_methname: 0x10d75
+  __TEXT.__objc_methtype: 0x240b
+  __TEXT.__objc_stubs: 0xa280
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__const: 0xf68
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3590
+  __DATA_CONST.__objc_selrefs: 0x3650
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x26f0
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0xce10
+  __AUTH_CONST.__const: 0x2720
+  __AUTH_CONST.__cfstring: 0x4e80
+  __AUTH_CONST.__objc_const: 0xbad0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1d10
-  __DATA.__objc_ivar: 0x62c
+  __AUTH.__objc_data: 0x1d60
+  __DATA.__objc_ivar: 0x634
   __DATA.__data: 0x1328
-  __DATA.__bss: 0x100
   __DATA.__common: 0xc8
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF9C733C-4926-3360-BE9F-04F5083CC11F
-  Functions: 2701
-  Symbols:   6224
-  CStrings:  4622
+  UUID: 19546326-AFC0-3CA6-A076-5BFCFAA9FE1D
+  Functions: 2706
+  Symbols:   6254
+  CStrings:  4652
 
Symbols:
+ +[HKSPAnalyticsSleepRoomEntryEvent _payloadWithProvidenceInfo:isOnboarded:secondsSinceAlarmDismissed:]
+ -[HKSPAnalyticsSleepDataInteractionEvent .cxx_destruct]
+ -[HKSPAnalyticsSleepDataInteractionEvent description]
+ -[HKSPAnalyticsSleepDataInteractionEvent eventName]
+ -[HKSPAnalyticsSleepDataInteractionEvent eventPayload]
+ -[HKSPAnalyticsSleepDataInteractionEvent initWithType:secondsSinceAlarmDismissal:isSleepOnWatchOnboarded:isWatchSleepTrackingEnabled:isSleepScheduleEnabled:isOnboardedVitals:]
+ -[HKSPAnalyticsSleepDataInteractionEvent setEventName:]
+ -[HKSPAnalyticsSleepDataInteractionEvent setEventPayload:]
+ -[HKSPAnalyticsSleepRoomEntryEvent initWithProvenanceInfo:isOnboarded:secondsSinceAlarmDismissed:]
+ -[HKSPSleepEventRecord secondsSinceAlarmDismissalFromDate:]
+ -[HKSPSleepStore(Analytics) trackSleepDataInteractionEventWithType:isOnboardedVitals:completion:]
+ OBJC_IVAR_$_HKSPAnalyticsSleepDataInteractionEvent._eventName
+ OBJC_IVAR_$_HKSPAnalyticsSleepDataInteractionEvent._eventPayload
+ _HKSPAnalyticsEventNameSleepDataInteraction
+ _HKSPAnalyticsPayloadKeySecondsSinceAlarmDismissal
+ _OBJC_CLASS_$_HKSPAnalyticsSleepDataInteractionEvent
+ _OBJC_METACLASS_$_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_$_INSTANCE_METHODS_HKSPSleepStore(Analytics|Proactive)
+ __OBJC_$_INSTANCE_VARIABLES_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_$_PROP_LIST_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_CLASS_PROTOCOLS_$_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_CLASS_RO_$_HKSPAnalyticsSleepDataInteractionEvent
+ __OBJC_METACLASS_RO_$_HKSPAnalyticsSleepDataInteractionEvent
+ ___97-[HKSPSleepStore(Analytics) trackSleepDataInteractionEventWithType:isOnboardedVitals:completion:]_block_invoke
+ ___block_descriptor_57_e8_32s40bs_e44_v24?0"HKSPSleepScheduleModel"8"NSError"16l
+ _objc_msgSend$_payloadWithProvidenceInfo:isOnboarded:secondsSinceAlarmDismissed:
+ _objc_msgSend$analyticsManager
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$initWithProvenanceInfo:isOnboarded:secondsSinceAlarmDismissed:
+ _objc_msgSend$initWithType:secondsSinceAlarmDismissal:isSleepOnWatchOnboarded:isWatchSleepTrackingEnabled:isSleepScheduleEnabled:isOnboardedVitals:
+ _objc_msgSend$secondsSinceAlarmDismissalFromDate:
+ _objc_msgSend$sleepScheduleModelWithCompletion:
- +[HKSPAnalyticsSleepRoomEntryEvent _payloadWithProvidenceInfo:isOnboarded:]
- __OBJC_$_INSTANCE_METHODS_HKSPSleepStore(Proactive)
- _objc_msgSend$_payloadWithProvidenceInfo:isOnboarded:
CStrings:
+ "@36@0:8@16B24d28"
+ "@52@0:8Q16@24B32B36@40B48"
+ "Analytics"
+ "HKSPAnalyticsSleepDataInteractionEvent"
+ "HKSPAnalyticsSleepDataInteractionType-%@"
+ "Sleep App"
+ "Vitals App"
+ "Vitals Data Type Room"
+ "_payloadWithProvidenceInfo:isOnboarded:secondsSinceAlarmDismissed:"
+ "com.apple.health.sleepdata.interactions"
+ "dictionaryWithDictionary:"
+ "initWithProvenanceInfo:isOnboarded:secondsSinceAlarmDismissed:"
+ "initWithType:secondsSinceAlarmDismissal:isSleepOnWatchOnboarded:isWatchSleepTrackingEnabled:isSleepScheduleEnabled:isOnboardedVitals:"
+ "isOnboardedVitals"
+ "isSleepOnWatchOnboarded"
+ "isSleepScheduleEnabled"
+ "isWatchSleepTrackingEnabled"
+ "secondsSinceAlarmDismissalFromDate:"
+ "secondsSinceAlarmLastDismissed"
+ "trackSleepDataInteractionEventWithType:isOnboardedVitals:completion:"
+ "v36@0:8Q16B24@?28"
- "_payloadWithProvidenceInfo:isOnboarded:"

```
