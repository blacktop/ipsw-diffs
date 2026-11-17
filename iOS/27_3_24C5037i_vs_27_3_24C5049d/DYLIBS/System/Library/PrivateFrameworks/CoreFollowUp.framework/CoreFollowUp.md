## CoreFollowUp

> `/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp`

```diff

-2027.2.2.0.0
-  __TEXT.__text: 0x21804
-  __TEXT.__objc_methlist: 0x16f4
+2027.2.4.0.0
+  __TEXT.__text: 0x23370
+  __TEXT.__objc_methlist: 0x1774
   __TEXT.__const: 0x10b0
-  __TEXT.__cstring: 0x20f4
+  __TEXT.__cstring: 0x24c4
   __TEXT.__gcc_except_tab: 0x2b0
   __TEXT.__oslogstring: 0x1330
   __TEXT.__swift5_typeref: 0x3cc

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0xd98
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_selrefs: 0xe58
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x2a0
-  __AUTH_CONST.__const: 0xaf8
-  __AUTH_CONST.__cfstring: 0x23c0
-  __AUTH_CONST.__objc_const: 0x5330
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __DATA_CONST.__got: 0x2b0
+  __AUTH_CONST.__const: 0xb18
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0x5338
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6d8
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x240
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1070
-  Symbols:   1312
-  CStrings:  431
+  Functions: 1090
+  Symbols:   1343
+  CStrings:  497
 
Symbols:
+ +[FLTelemetryAnalyticsSender isEventUsed:]
+ +[FLTelemetryProcessor sharedProcessor]
+ -[FLApprovedItemsFilter approvalStatusForItem:logging:]
+ -[FLTelemetryAnalyticsController _captureItem:event:source:extra:]
+ -[FLTelemetryAnalyticsController _payloadForItem:extra:]
+ -[FLTelemetryAnalyticsController captureItemPost:isNew:process:]
+ -[FLTelemetryAnalyticsController captureNotificationDelivery:reason:]
+ -[FLTelemetryAnalyticsController captureSnapshotWithItems:trigger:]
+ -[FLTelemetryProcessor _itemsExcludingTests:]
+ -[FLTelemetryProcessor processItemPost:isNew:process:]
+ -[FLTelemetryProcessor processNotificationDelivery:reason:]
+ -[FLTelemetryProcessor processSnapshotWithItems:trigger:]
+ _AnalyticsIsEventUsed
+ _FLTelemetryItemBadges
+ _FLTelemetrySnapshotTriggerDaily
+ _FLTelemetryZeroedSnapshotCounts
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __OBJC_$_CLASS_METHODS_FLTelemetryProcessor
+ ___34-[FLFollowUpAction _loadActionURL]_block_invoke
+ ___39+[FLTelemetryProcessor sharedProcessor]_block_invoke
+ ___45-[FLTelemetryProcessor _itemsExcludingTests:]_block_invoke
+ ___57-[FLTelemetryProcessor processSnapshotWithItems:trigger:]_block_invoke
+ ___66-[FLTelemetryAnalyticsController _captureItem:event:source:extra:]_block_invoke
+ ___67-[FLTelemetryAnalyticsController captureSnapshotWithItems:trigger:]_block_invoke
+ ___67-[FLTelemetryAnalyticsController captureSnapshotWithItems:trigger:]_block_invoke_2
+ ___67-[FLTelemetryAnalyticsController captureSnapshotWithItems:trigger:]_block_invoke_3
+ ___67-[FLTelemetryAnalyticsController captureSnapshotWithItems:trigger:]_block_invoke_4
+ ___69-[FLTelemetryAnalyticsController captureNotificationDelivery:reason:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e14_"NSArray"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ _objc_retain_x28
+ _sharedProcessor.onceToken
+ _sharedProcessor.processor
- -[FLTelemetryAnalyticsController _captureItem:event:source:]
- -[FLTelemetryAnalyticsController captureItemAddition:]
- -[FLTelemetryProcessor processItemAddition:]
- ___44-[FLTelemetryProcessor processCurrentItems:]_block_invoke
- ___60-[FLTelemetryAnalyticsController _captureItem:event:source:]_block_invoke
CStrings:
+ ","
+ "@\"NSArray\"8@?0"
+ "Priority"
+ "actionCount"
+ "alert"
+ "approval"
+ "approved"
+ "badgeOnly"
+ "badges"
+ "badging"
+ "clientUpdated"
+ "collection"
+ "com.apple.Health.MedicalID.familySetupReviewFollowUp"
+ "com.apple.followup.clientSnapshot"
+ "com.apple.followup.notificationPosted"
+ "com.apple.followup.snapshot"
+ "critical"
+ "criticalPriority"
+ "daily"
+ "default"
+ "defaultPriority"
+ "displayStyle"
+ "distinctClients"
+ "expired"
+ "firstNotificationDelaySeconds"
+ "forced"
+ "forcesDelivery"
+ "hasExpiration"
+ "hasExtension"
+ "hasNotification"
+ "high"
+ "highPriority"
+ "i"
+ "isExpired"
+ "isRepeat"
+ "localHour"
+ "maxItemsPerClient"
+ "notificationAgeSeconds"
+ "notificationFrequencySeconds"
+ "notificationOptions"
+ "notifiesAlert"
+ "notifiesBanner"
+ "notifiesLockScreen"
+ "notifiesNotificationCenter"
+ "offers"
+ "oldestNotificationAgeSeconds"
+ "priority"
+ "process"
+ "reason"
+ "rejected"
+ "repeatingNotification"
+ "repeatsNotification"
+ "required"
+ "scheduled"
+ "secondsSincePreviousDelivery"
+ "settingsTopLevel"
+ "suggested"
+ "targetBundle"
+ "total"
+ "trigger"
+ "typeIdentifier"
+ "unknown"
+ "update"
+ "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
+ "withNotification"
+ "zeroAction"
```
