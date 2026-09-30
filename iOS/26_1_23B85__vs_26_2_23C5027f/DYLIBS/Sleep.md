## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-6200.2.14.2.5
-  __TEXT.__text: 0x59250
+6200.3.4.0.0
+  __TEXT.__text: 0x59310
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x73b4
+  __TEXT.__objc_methlist: 0x73e4
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0x4bcc
+  __TEXT.__cstring: 0x4c21
   __TEXT.__gcc_except_tab: 0x8dc
   __TEXT.__oslogstring: 0x4306
   __TEXT.__unwind_info: 0x1c10
   __TEXT.__objc_classname: 0xf0f
-  __TEXT.__objc_methname: 0x11612
+  __TEXT.__objc_methname: 0x1173e
   __TEXT.__objc_methtype: 0x2549
-  __TEXT.__objc_stubs: 0xa5c0
+  __TEXT.__objc_stubs: 0xa600
   __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x2b98
+  __DATA_CONST.__const: 0x2ba0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37e8
+  __DATA_CONST.__objc_selrefs: 0x3808
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x270
-  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x51e0
-  __AUTH_CONST.__objc_const: 0xbd48
+  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__objc_const: 0xbda8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x5e4
+  __DATA.__objc_ivar: 0x5ec
   __DATA.__data: 0x14a0
   __DATA_DIRTY.__objc_ivar: 0x64
   __DATA_DIRTY.__objc_data: 0x14f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E117BDF-06D0-346C-9868-ADBE6A75AB8D
-  Functions: 2706
-  Symbols:   8969
-  CStrings:  4785
+  UUID: BCF61701-CDA0-31E6-8836-35CD69D90A22
+  Functions: 2710
+  Symbols:   8982
+  CStrings:  4801
 
Symbols:
+ -[HKSPAnalyticsDailyReportEvent isSleepScoreNotificationEnabled]
+ -[HKSPAnalyticsDailyReportEvent setIsSleepScoreNotificationEnabled:]
+ -[HKSPAnalyticsDailyReportEvent setSleepScoreLastNight:]
+ -[HKSPAnalyticsDailyReportEvent setSleepScoreNotificationThreshold:]
+ -[HKSPAnalyticsDailyReportEvent sleepScoreLastNight]
+ -[HKSPAnalyticsDailyReportEvent sleepScoreNotificationThreshold]
+ _HKSPAnalyticsPayloadKeySleepNotificationSleepScore
+ _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._isSleepScoreNotificationEnabled
+ _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._sleepScoreLastNight
+ _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._sleepScoreNotificationThreshold
+ _objc_msgSend$isSleepScoreNotificationEnabled
+ _objc_msgSend$sleepScoreLastNight
+ _objc_msgSend$sleepScoreNotificationThreshold
- -[HKSPAnalyticsDailyReportEvent setWakeUpResultsEnabled:]
- -[HKSPAnalyticsDailyReportEvent wakeUpResultsEnabled]
- _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._wakeUpResultsEnabled
- _objc_msgSend$wakeUpResultsEnabled
CStrings:
+ "SleepScore"
+ "T@\"NSNumber\",C,N,V_sleepScoreLastNight"
+ "T@\"NSNumber\",C,N,V_sleepScoreNotificationThreshold"
+ "TB,N,V_isSleepScoreNotificationEnabled"
+ "_isSleepScoreNotificationEnabled"
+ "_sleepScoreLastNight"
+ "_sleepScoreNotificationThreshold"
+ "isSleepScoreNotificationEnabled"
+ "setIsSleepScoreNotificationEnabled:"
+ "setSleepScoreLastNight:"
+ "setSleepScoreNotificationThreshold:"
+ "sleepScore"
+ "sleepScoreLastNight"
+ "sleepScoreNotificationThreshold"
- "TB,N,V_wakeUpResultsEnabled"
- "_wakeUpResultsEnabled"
- "setWakeUpResultsEnabled:"
- "wakeUpResultsEnabled"

```
