## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-4146.1.11.3.0
+4146.2.12.1.3
   __TEXT.__text: 0x799a0
   __TEXT.__auth_stubs: 0xb50
   __TEXT.__objc_methlist: 0x7854

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DAAFB1D-B297-3F6D-B947-879F5064D892
+  UUID: F2770B70-3BF7-38DD-B5E8-DEAB464B5B8B
   Functions: 3066
   Symbols:   10779
   CStrings:  4747
Symbols:
+ -[HDSPWakeUpResultsNotificationManager sleepMetricsEngine]
+ _OBJC_CLASS_$_HKSHSleepMetricsEngine
+ _OBJC_IVAR_$_HDSPWakeUpResultsNotificationManager._sleepMetricsEngine
+ _objc_msgSend$sleepMetricsForDaySummaries:inMorningIndexRange:
- -[HDSPWakeUpResultsNotificationManager goalProgressEngine]
- _OBJC_CLASS_$_HKSHGoalProgressEngine
- _OBJC_IVAR_$_HDSPWakeUpResultsNotificationManager._goalProgressEngine
- _objc_msgSend$goalProgressForDaySummaries:inMorningIndexRange:
CStrings:
+ "@\"HKSHSleepMetricsEngine\""
+ "T@\"HKSHSleepMetricsEngine\",R,N,V_sleepMetricsEngine"
+ "_sleepMetricsEngine"
+ "sleepMetricsEngine"
+ "sleepMetricsForDaySummaries:inMorningIndexRange:"
- "@\"HKSHGoalProgressEngine\""
- "T@\"HKSHGoalProgressEngine\",R,N,V_goalProgressEngine"
- "_goalProgressEngine"
- "goalProgressEngine"
- "goalProgressForDaySummaries:inMorningIndexRange:"

```
