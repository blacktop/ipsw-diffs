## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-288.40.3.0.0
-  __TEXT.__text: 0x1cbbc
-  __TEXT.__objc_methlist: 0x2590
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x1d26
-  __TEXT.__oslogstring: 0x2c5d
+288.40.6.0.0
+  __TEXT.__text: 0x1db14
+  __TEXT.__objc_methlist: 0x25f0
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0x1f11
+  __TEXT.__oslogstring: 0x2ccc
   __TEXT.__gcc_except_tab: 0x730
-  __TEXT.__unwind_info: 0xe08
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__const: 0x990
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1410
+  __DATA_CONST.__objc_selrefs: 0x1458
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x208
-  __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x18c0
-  __AUTH_CONST.__objc_const: 0x3488
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x34b8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x224
+  __DATA.__objc_ivar: 0x228
   __DATA.__data: 0x5a0
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x98

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1016
-  Symbols:   1939
-  CStrings:  505
+  Functions: 1030
+  Symbols:   1962
+  CStrings:  523
 
Symbols:
+ +[_OSIBLMAnalyticsHandler allNotificationAnalyticsKeys]
+ +[_OSIBLMAnalyticsHandler analyticsKeyForNotificationDecision:]
+ -[_OSIBLMAnalyticsHandler historicalNotificationDataForDate:]
+ -[_OSIBLMAnalyticsHandler recordNotificationDecision:]
+ -[_OSIBLMAnalyticsHandler windowedNotificationSumsEndingDate:days:suffix:]
+ -[_OSIBLManager analyticsHandler]
+ -[_OSIBLManager isCurrentDrainUnusualWithDecision:]
+ -[_OSIBLManager setAnalyticsHandler:]
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table64
+ _OBJC_IVAR_$__OSIBLManager._analyticsHandler
+ ___54-[_OSIBLMAnalyticsHandler recordNotificationDecision:]_block_invoke
+ ___55+[_OSIBLMAnalyticsHandler allNotificationAnalyticsKeys]_block_invoke
+ ___61-[_OSIBLMAnalyticsHandler historicalNotificationDataForDate:]_block_invoke
+ ___74-[_OSIBLMAnalyticsHandler windowedNotificationSumsEndingDate:days:suffix:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8s56l8
+ _allNotificationAnalyticsKeys.keys
+ _allNotificationAnalyticsKeys.onceToken
+ _objc_msgSend$allNotificationAnalyticsKeys
+ _objc_msgSend$analyticsHandler
+ _objc_msgSend$analyticsKeyForNotificationDecision:
+ _objc_msgSend$historicalNotificationDataForDate:
+ _objc_msgSend$isCurrentDrainUnusualWithDecision:
+ _objc_msgSend$recordNotificationDecision:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$windowedNotificationSumsEndingDate:days:suffix:
- GCC_except_table55
- GCC_except_table58
- GCC_except_table62
- _objc_msgSend$isCurrentDrainUnusual
CStrings:
+ "IBLMNotificationDecision"
+ "Last30Days"
+ "Last7Days"
+ "NotificationDecision"
+ "Recorded notification decision %{public}@ for %@ (now %ld)"
+ "Unsupported notification decision for analytics %ld"
+ "com.apple.osintelligence.iblm.recordNotificationDecision"
+ "historicalIBLMNotificationCounts"
+ "notificationEvaluationCount"
+ "notificationSuppressedByBackstop"
+ "notificationSuppressedByCooldown"
+ "notificationSuppressedByDisabled"
+ "notificationSuppressedByInsufficientData"
+ "notificationSuppressedByNotUnusual"
+ "notificationSuppressedBySlotOutOfRange"
+ "notificationSuppressedByStartHour"
+ "onboardingNotificationCount"
+ "unusualDrainNotificationCount"
```
