## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Versions/A/MobileTimer`

```diff

-2257.4.0.0.0
-  __TEXT.__text: 0x8ffa0
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x81e8
-  __TEXT.__const: 0x378
+2258.5.10.0.0
+  __TEXT.__text: 0x900b0
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x93d4
+  __TEXT.__const: 0x340
   __TEXT.__oslogstring: 0x8355
-  __TEXT.__cstring: 0x688e
+  __TEXT.__cstring: 0x68c9
   __TEXT.__gcc_except_tab: 0xa84
   __TEXT.__dlopen_cstrs: 0x26f
   __TEXT.__ustring: 0x1a
-  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__unwind_info: 0x22f8
   __TEXT.__objc_classname: 0x10d4
-  __TEXT.__objc_methname: 0x10a84
+  __TEXT.__objc_methname: 0x10b15
   __TEXT.__objc_methtype: 0x2dab
-  __TEXT.__objc_stubs: 0xc960
+  __TEXT.__objc_stubs: 0xc9e0
   __DATA_CONST.__got: 0x728
-  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4360
+  __DATA_CONST.__objc_selrefs: 0x4460
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x2f50
-  __AUTH_CONST.__cfstring: 0x5b00
-  __AUTH_CONST.__objc_const: 0x1c320
+  __AUTH_CONST.__cfstring: 0x5b40
+  __AUTH_CONST.__objc_const: 0x1a468
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2da0
-  __DATA.__objc_ivar: 0x678
+  __DATA.__objc_ivar: 0x67c
   __DATA.__data: 0x1830
   __DATA.__common: 0x20
   __DATA.__bss: 0x450

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F9C4A7A-32BC-38B8-B9ED-FD52C7B7C26A
-  Functions: 3560
-  Symbols:   8652
-  CStrings:  5765
+  UUID: 1A80CE25-1FAA-339F-AFAA-A9E8CCD4C81C
+  Functions: 3614
+  Symbols:   8719
+  CStrings:  5775
 
Symbols:
+ +[MTAgent agent].cold.1
+ +[MTAlarm _isInternalBuild].cold.1
+ +[MTAlarm defaultSilentModeOptions]
+ +[MTAlarm(Properties) propertiesAffectingBedtime].cold.1
+ +[MTAlarm(Properties) propertiesAffectingNotification].cold.1
+ +[MTAlarm(Properties) propertiesAffectingSessions].cold.1
+ +[MTAlarm(Properties) propertiesAffectingSnooze].cold.1
+ +[MTAlarm(Properties) propertiesAffectingWaketime].cold.1
+ +[MTCFUserNotificationPoster sharedInstance].cold.1
+ +[MTDateFormatting sharedInstance].cold.1
+ +[MTDeviceListener sharedDeviceListener].cold.1
+ +[MTLegacyManager _numberFromString:].cold.1
+ +[MTLegacyManager sharedManager].cold.1
+ +[MTMetrics _sharedPublicMetrics].cold.1
+ +[MTScheduledList _sort:].cold.1
+ +[MTSpringboardStartMonitor sharedInstance].cold.1
+ +[MTTimer(Properties) propertiesAffectingSessions].cold.1
+ +[MTUserDefaults sharedUserDefaults].cold.1
+ +[MTUserNotificationCenter _durationComponentsFormatter].cold.1
+ +[MTUserNotificationCenter _timeFormatter].cold.1
+ +[MTUtilities widgetOverrideDate].cold.1
+ +[NSDateFormatter(MTUtilities) mtTimeOnlyFormatter].cold.1
+ +[NSNumberFormatter(MTUtilities) mtDecimalStyleNumberFormatter].cold.1
+ +[WorldClockManager sharedManager].cold.1
+ -[Alarm setSoundVolume:].cold.1
+ -[MTAlarm breaksThroughSilentModeOnThisDevice]
+ -[MTAlarm setSilentModeOptions:]
+ -[MTAlarm silentModeOptions]
+ -[MTAlarmManager alarmsSyncIncludingSleepAlarm:].cold.1
+ -[MTAlarmManager nextAlarmsForDateSync:maxCount:includeSleepAlarm:includeBedtimeNotification:].cold.1
+ -[MTAlarmManager nextAlarmsInRangeSync:maxCount:includeSleepAlarm:includeBedtimeNotification:].cold.1
+ -[MTObserverStore addObserver:wasFirst:].cold.1
+ -[MTObserverStore containsObserver:].cold.1
+ -[MTObserverStore removeObserver:wasLast:].cold.1
+ -[MTSensitiveUIMonitor _isVendorRelease].cold.1
+ -[MTTimer nextTriggerAfterDate:].cold.2
+ -[MTTimerManager _updateCurrentTimerWithState:].cold.1
+ -[MTTimerManager _updateCurrentTimerWithStateSync:].cold.1
+ -[MTTimerManager _updateTimer:doSynchronous:].cold.1
+ -[MTTimerManager addTimer:].cold.1
+ -[MTTimerScheduler _queue_scheduleTimers:withCompletion:].cold.1
+ -[NSDate(MTUtilities) mtIsAfterDate:].cold.1
+ -[NSDate(MTUtilities) mtIsAfterOrSameAsDate:].cold.1
+ -[NSDate(MTUtilities) mtIsBeforeDate:].cold.1
+ -[NSDate(MTUtilities) mtIsBeforeOrSameAsDate:].cold.1
+ -[NSString(Notification) mtStringByAppendingNotificationDate:].cold.1
+ GCC_except_table63
+ MTActivityForName.cold.1
+ MTAlarmClientInterface.cold.1
+ MTAlarmServerInterface.cold.1
+ MTAlarmStandardSort.cold.1
+ MTCurrentDateProvider.cold.1
+ MTIntegerIsPositive.cold.1
+ MTLogForCategory.cold.1
+ MTSessionClientInterface.cold.1
+ MTSessionServerInterface.cold.1
+ MTStopwatchClientInterface.cold.1
+ MTStopwatchServerInterface.cold.1
+ MTTimeIntervalIsPositive.cold.1
+ MTTimerClientInterface.cold.1
+ MTTimerServerInterface.cold.1
+ OBJC_IVAR_$_MTAlarm._silentModeOptions
+ _MTAlarmSilentModeOptionsKey
+ __block_literal_global.109
+ __block_literal_global.111
+ __block_literal_global.113
+ __block_literal_global.115
+ _kMTAlarmSilentModeOptionsEncodingKey
+ _objc_msgSend$breaksThroughSilentModeOnThisDevice
+ _objc_msgSend$defaultSilentModeOptions
+ _objc_msgSend$setSilentModeOptions:
+ _objc_msgSend$silentModeOptions
- GCC_except_table61
- _MTAlarmPlaysOnKey
- __block_literal_global.106
- __block_literal_global.108
- __block_literal_global.110
- __block_literal_global.112
- _fmod
- _fmodf
CStrings:
+ "MTAlarmSilentModeOptions"
+ "MTSilentModeOptions"
+ "TQ,N,V_silentModeOptions"
+ "_silentModeOptions"
+ "breaksThroughSilentMode"
+ "breaksThroughSilentModeOnThisDevice"
+ "defaultSilentModeOptions"
+ "setSilentModeOptions:"
+ "silentModeOptions"
- "MTPlaysOn"

```
