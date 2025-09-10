## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

 6106.1.2.11.0
-  __TEXT.__text: 0x7b244
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x8a8c
+  __TEXT.__text: 0x7bb04
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x8b0c
   __TEXT.__const: 0x238
   __TEXT.__swift5_typeref: 0x20
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__oslogstring: 0xb92c
+  __TEXT.__oslogstring: 0xb986
   __TEXT.__cstring: 0x2b30
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1244
-  __TEXT.__unwind_info: 0x21f8
-  __TEXT.__objc_classname: 0x1fad
-  __TEXT.__objc_methname: 0x11ad3
+  __TEXT.__gcc_except_tab: 0x1250
+  __TEXT.__unwind_info: 0x2220
+  __TEXT.__objc_classname: 0x1fc5
+  __TEXT.__objc_methname: 0x11c5b
   __TEXT.__objc_methtype: 0x36d5
-  __TEXT.__objc_stubs: 0xd580
-  __DATA_CONST.__got: 0xa98
+  __TEXT.__objc_stubs: 0xd740
+  __DATA_CONST.__got: 0xac0
   __DATA_CONST.__const: 0x24c0
-  __DATA_CONST.__objc_classlist: 0x548
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d58
+  __DATA_CONST.__objc_selrefs: 0x3dc0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x360
-  __AUTH_CONST.__auth_got: 0x730
+  __DATA_CONST.__objc_superrefs: 0x368
+  __AUTH_CONST.__auth_got: 0x740
   __AUTH_CONST.__const: 0xd30
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0x10270
+  __AUTH_CONST.__objc_const: 0x103a0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xd30
+  __AUTH.__objc_data: 0xd80
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0x2610
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_ivar: 0xd0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8E2BF3CE-FF78-3248-B46E-E2AFFF1B1AC5
-  Functions: 2996
-  Symbols:   10738
-  CStrings:  4832
+  UUID: 7F5B3DF1-F0D5-312F-968A-C60EFDB03B44
+  Functions: 3007
+  Symbols:   10790
+  CStrings:  4847
 
Symbols:
+ -[HDSPOrchestrationCenter .cxx_destruct]
+ -[HDSPOrchestrationCenter environmentDidBecomeReady:]
+ -[HDSPOrchestrationCenter environment]
+ -[HDSPOrchestrationCenter initWithEnvironment:]
+ -[HDSPOrchestrationCenter publishNotificationForEvent:]
+ -[HDSPOrchestrationCenter tearDownNotificationForEventIdentifier:]
+ -[HDSPOrchestrationCenter tearDownNotifications]
+ -[HDSPUserNotificationCenter _sleepScoreResultsContentWithUserInfo:]
+ -[HDSPWakeUpResultsNotificationManager lastWakeUpResultsIntroductionNotificationVersionSent]
+ -[HDSPWakeUpResultsNotificationManager needsSleepScoreIntroduction]
+ GCC_except_table34
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table63
+ _HKSHSleepScoreResultsNotificationEventIdentifier
+ _HKSPSleepEventIdentifierSleepScoreResultsNotification
+ _HKSPSleepScoreIntroductionCategory
+ _HKSPSleepScoreResultsCategory
+ _HKSPSleepScoreResultsIdentifier
+ _OBJC_CLASS_$_HDSPOrchestrationCenter
+ _OBJC_CLASS_$_HKSHSleepScoreResultsNotification
+ _OBJC_CLASS_$_HKSHSleepScoreResultsNotificationBuilder
+ _OBJC_IVAR_$_HDSPOrchestrationCenter._environment
+ _OBJC_METACLASS_$_HDSPOrchestrationCenter
+ __OBJC_$_INSTANCE_METHODS_HDSPOrchestrationCenter
+ __OBJC_$_INSTANCE_VARIABLES_HDSPOrchestrationCenter
+ __OBJC_$_PROP_LIST_HDSPOrchestrationCenter
+ __OBJC_CLASS_PROTOCOLS_$_HDSPOrchestrationCenter
+ __OBJC_CLASS_RO_$_HDSPOrchestrationCenter
+ __OBJC_METACLASS_RO_$_HDSPOrchestrationCenter
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.326
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.329
+ ___65-[HDSPUserNotificationCenter _recordSentUserNotificationRequest:]_block_invoke
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.330
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.333
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.338
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.341
+ ___block_literal_global.305
+ _objc_msgSend$_sleepScoreResultsContentWithUserInfo:
+ _objc_msgSend$body
+ _objc_msgSend$hk_copyNonEmptyString
+ _objc_msgSend$initWithDaySummaries:needsIntroduction:userFirstName:
+ _objc_msgSend$initWithUserInfo:
+ _objc_msgSend$isIntroduction
+ _objc_msgSend$kickOffBackgroundGeneration
+ _objc_msgSend$lastWakeUpResultsIntroductionNotificationVersionSent
+ _objc_msgSend$needsSleepScoreIntroduction
+ _objc_msgSend$notificationUserInfo
+ _objc_msgSend$setLastWakeUpResultsIntroductionNotificationVersionSent:
+ _objc_msgSend$setLastWakeUpResultsIntroductionNotificationVersionSentDate:
+ _objc_msgSend$sleepDetails
+ _objc_msgSend$title
- GCC_except_table53
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.324
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.325
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.328
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.331
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.336
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.339
CStrings:
+ "HDSPOrchestrationCenter"
+ "[%{public}@] Cannot create content for sleep score results without valid data: %{public}@"
+ "_sleepScoreResultsContentWithUserInfo:"
+ "body"
+ "hk_copyNonEmptyString"
+ "initWithDaySummaries:needsIntroduction:userFirstName:"
+ "initWithUserInfo:"
+ "isIntroduction"
+ "lastWakeUpResultsIntroductionNotificationVersionSent"
+ "needsSleepScoreIntroduction"
+ "notificationUserInfo"
+ "setLastWakeUpResultsIntroductionNotificationVersionSent:"
+ "setLastWakeUpResultsIntroductionNotificationVersionSentDate:"
+ "sleepDetails"
+ "title"

```
