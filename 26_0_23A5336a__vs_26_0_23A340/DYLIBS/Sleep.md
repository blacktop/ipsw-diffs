## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

 6106.1.2.11.0
-  __TEXT.__text: 0x58cf8
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x736c
+  __TEXT.__text: 0x59274
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x73b4
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0x49a4
+  __TEXT.__cstring: 0x4b87
   __TEXT.__gcc_except_tab: 0x8dc
   __TEXT.__oslogstring: 0x4306
   __TEXT.__unwind_info: 0x1c10
-  __TEXT.__objc_classname: 0xf0e
-  __TEXT.__objc_methname: 0x11427
+  __TEXT.__objc_classname: 0xf0f
+  __TEXT.__objc_methname: 0x11612
   __TEXT.__objc_methtype: 0x2549
-  __TEXT.__objc_stubs: 0xa580
+  __TEXT.__objc_stubs: 0xa5e0
   __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x2b38
+  __DATA_CONST.__const: 0x2b88
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37c0
+  __DATA_CONST.__objc_selrefs: 0x37e8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x5020
-  __AUTH_CONST.__objc_const: 0xbcc8
+  __AUTH_CONST.__cfstring: 0x51a0
+  __AUTH_CONST.__objc_const: 0xbd48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_ivar: 0x5e4
   __DATA.__data: 0x14a0
   __DATA_DIRTY.__objc_ivar: 0x64
   __DATA_DIRTY.__objc_data: 0x14f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E153665-12CD-3F4C-A783-83F3FC5DF9B3
-  Functions: 2699
-  Symbols:   8940
-  CStrings:  4748
+  UUID: 3B80D667-AE52-3EA9-83E2-EFF0206D4289
+  Functions: 2706
+  Symbols:   8968
+  CStrings:  4781
 
Symbols:
+ -[HKSPMutableSleepEventRecord lastWakeUpResultsIntroductionNotificationVersionSentDate]
+ -[HKSPMutableSleepEventRecord lastWakeUpResultsIntroductionNotificationVersionSent]
+ -[HKSPMutableSleepEventRecord setLastWakeUpResultsIntroductionNotificationVersionSent:]
+ -[HKSPMutableSleepEventRecord setLastWakeUpResultsIntroductionNotificationVersionSentDate:]
+ -[HKSPSleepEventRecord lastWakeUpResultsIntroductionNotificationVersionSentDate]
+ -[HKSPSleepEventRecord lastWakeUpResultsIntroductionNotificationVersionSent]
+ _HKSHSleepScoreResultsNotificationEventIdentifier
+ _HKSPLastWakeUpResultsIntroductionNotificationVersionSentDateKey
+ _HKSPLastWakeUpResultsIntroductionNotificationVersionSentKey
+ _HKSPProvenancePresentationSleepScoreRoom
+ _HKSPSleepEventIdentifierSleepScoreResultsNotification
+ _HKSPSleepLaunchURLRouteOpenSleepScoreRoom
+ _HKSPSleepScoreIntroductionCategory
+ _HKSPSleepScoreResultsCategory
+ _HKSPSleepScoreResultsIdentifier
+ _HKSPSleepScoreWidgetIdentifier
+ _HKSPTurnOffSleepScoreResultsNotificationsAction
+ _OBJC_IVAR_$_HKSPSleepEventRecord._lastWakeUpResultsIntroductionNotificationVersionSent
+ _OBJC_IVAR_$_HKSPSleepEventRecord._lastWakeUpResultsIntroductionNotificationVersionSentDate
+ ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.323
+ ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.320
+ _objc_msgSend$lastWakeUpResultsIntroductionNotificationVersionSent
+ _objc_msgSend$lastWakeUpResultsIntroductionNotificationVersionSentDate
+ _objc_msgSend$sleepDetails
- ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.319
- ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.316
CStrings:
+ "HKSPAnalyticsLaunchSourceSleepScoreRoom"
+ "HKSPLastWakeUpResultsIntroductionNotificationVersionSent"
+ "HKSPLastWakeUpResultsIntroductionNotificationVersionSentDate"
+ "SleepHealthAppPlugin.SleepScoreIntroduction"
+ "SleepHealthAppPlugin.SleepScoreResults"
+ "SleepScoreResultsIdentifier"
+ "SleepScoreRoomForeground"
+ "T@\"NSDate\",R,C,N,V_lastWakeUpResultsIntroductionNotificationVersionSentDate"
+ "Tq,R,N,V_lastWakeUpResultsIntroductionNotificationVersionSent"
+ "TurnOffScoreNotifications"
+ "_lastWakeUpResultsIntroductionNotificationVersionSent"
+ "_lastWakeUpResultsIntroductionNotificationVersionSentDate"
+ "com.apple.health.SleepScoreWidget"
+ "lastWakeUpResultsIntroductionNotificationVersionSent"
+ "lastWakeUpResultsIntroductionNotificationVersionSentDate"
+ "openSleepScoreRoom"
+ "setLastWakeUpResultsIntroductionNotificationVersionSent:"
+ "setLastWakeUpResultsIntroductionNotificationVersionSentDate:"
+ "sleepDetails"

```
