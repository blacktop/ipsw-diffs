## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

```diff

-749.20.0.1.0
-  __TEXT.__text: 0x90bc
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x16a0
-  __TEXT.__objc_methlist: 0x6ac
-  __TEXT.__cstring: 0x20b1
-  __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x2020
-  __TEXT.__objc_methtype: 0x97b
-  __TEXT.__const: 0x20
-  __TEXT.__oslogstring: 0xb11
+749.36.0.0.0
+  __TEXT.__text: 0xa234
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__objc_methlist: 0x7a8
+  __TEXT.__cstring: 0x22c3
+  __TEXT.__objc_classname: 0x254
+  __TEXT.__objc_methname: 0x23d2
+  __TEXT.__objc_methtype: 0xa77
+  __TEXT.__const: 0x30
+  __TEXT.__oslogstring: 0x1157
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__unwind_info: 0x2a8
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0xab0
-  __DATA_CONST.__cfstring: 0x840
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__unwind_info: 0x2dc
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__cfstring: 0xa40
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x1730
-  __DATA.__objc_selrefs: 0x6f8
-  __DATA.__objc_classrefs: 0xf8
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x420
+  __DATA.__objc_const: 0x1a58
+  __DATA.__objc_selrefs: 0x7f8
+  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x540
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 213
-  Symbols:   147
-  CStrings:  543
+  Functions: 234
+  Symbols:   181
+  CStrings:  628
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveEveryObserver
+ _FIUIIsWorkoutNFCAllDayEnabled
+ _FIUISetWorkoutNFCAllDayEnabled
+ _HDDiagnosticStringFromDate
+ _HKCreateSerialUtilityDispatchQueue
+ _HKProductTypePrefixAppleWatchFirstGeneration
+ _HKProductTypePrefixAppleWatchSeries1Series2
+ _HKProductTypePrefixAppleWatchSeries3
+ _HKProductTypePrefixAppleWatchSeries4
+ _HKProductTypePrefixAppleWatchSeries5
+ _OBJC_CLASS_$_HDPeriodicActivity
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_WOWorkoutGymKitNFCManager
+ _OBJC_CLASS_$__HKBehavior
+ _OBJC_METACLASS_$_WOWorkoutGymKitNFCManager
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _kHKConnectedGymPreferencesDomain
+ _kWOConnectedGymDebugPeriodicActivityInactivityIntervalInSeconds
+ _kWOConnectedGymDebugPeriodicActivityIntervalInSeconds
+ _kWOConnectedGymDebugPeriodicActivityOnAllHardware
+ _kWOConnectedGymLastActivityDate
+ _kWOInactivityIntervalInSeconds
+ _kWOWorkoutGymKitNFCActivityName
+ _objc_destroyWeak
+ _objc_storeWeak
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_string
CStrings:
+ "\x14"
+ ", %@"
+ ", InactivityIntervalInSeconds: %ld)"
+ ", IntervalInSeconds: %ld"
+ ", debugPeriodicActivity (OnAllHardware: %@"
+ ", lastActivityDate: %@"
+ "@\"HDPeriodicActivity\""
+ "@\"NSDateFormatter\""
+ "@\"NSUserDefaults\""
+ "@\"WOWorkoutGymKitNFCManager\""
+ "B24@0:8@\"HDPeriodicActivity\"16"
+ "ConnectedGymDebugPeriodicActivityInactivityIntervalInSeconds"
+ "ConnectedGymDebugPeriodicActivityIntervalInSeconds"
+ "ConnectedGymDebugPeriodicActivityOnAllHardware"
+ "ConnectedGymLastActivityDate"
+ "ConnectedGymPreferencesChangedNotification"
+ "FIUIIsWorkoutNFCAllDayEnabled: %@"
+ "HDDiagnosticObject"
+ "HDPeriodicActivityDelegate"
+ "HDProfileReadyObserver"
+ "Not waiting to run"
+ "T@\"NSDate\",&,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N"
+ "T@\"WOWorkoutGymKitNFCManager\",&,N,V_gymKitNFCManager"
+ "TB,R,N"
+ "Tq,R,N"
+ "WOWorkoutGymKitNFCManager"
+ "Waiting to run"
+ "[WorkoutGymKitNFC] (Auto Disable) Workout GymKit NFC All Day support (intervalSinceLastActivityDate %fs is greater then inactivityIntervalInSeconds %fs), WorkoutNFCAllDayEnabled: %@"
+ "[WorkoutGymKitNFC] (Keep Current) Workout GymKit NFC All Day support (intervalSinceLastActivityDate %fs is less or equal to inactivityIntervalInSeconds %fs), WorkoutNFCAllDayEnabled: %@"
+ "[WorkoutGymKitNFC] <<<< performPeriodicActivity: %@ (%@), elapsed time: %f seconds"
+ "[WorkoutGymKitNFC] >>>> performPeriodicActivity: %@ (%@)"
+ "[WorkoutGymKitNFC] Current Device Product Type: %@ (oldHardware: %@)"
+ "[WorkoutGymKitNFC] Defaults %@ key found in %@ domain, current lastActivityDate: %@"
+ "[WorkoutGymKitNFC] Initializing WOWorkoutGymKitNFCManager, periodicActivityOn (oldHardware: %@ || allHardware: %@)"
+ "[WorkoutGymKitNFC] Last run: %@"
+ "[WorkoutGymKitNFC] No defaults %@ key found in %@ domain, set lastActivityDate to now: %@"
+ "[WorkoutGymKitNFC] Not initializing WOWorkoutGymKitNFCManager, periodicActivityOn (oldHardware: %@ || allHardware: %@), for testing on all hardware: defaults write %@ %@ 1"
+ "[WorkoutGymKitNFC] Workout GymKit NFC All Day support is Disabled in Settings (WorkoutNFCAllDayEnabled: %@), skip (Auto Disable) checks"
+ "[WorkoutGymKitNFC] connectedGymPreferencesChanged: Workout GymKit NFC All Day support is Disabled in Settings, keep current lastActivityDate: %@ (%@)"
+ "[WorkoutGymKitNFC] connectedGymPreferencesChanged: Workout GymKit NFC All Day support is Enabled in Settings, set lastActivityDate to now: %@ (%@)"
+ "[WorkoutGymKitNFC] dealloc"
+ "[WorkoutGymKitNFC] initWithProfile: %@"
+ "[WorkoutGymKitNFC] profileDidBecomeReady: scheduler created: %@ (%@)"
+ "_connectedGymDefaults"
+ "_dateFormatter"
+ "_gymKitNFCManager"
+ "_isOldWatchSeries:"
+ "_queue"
+ "_scheduler"
+ "appendFormat:"
+ "boolForKey:"
+ "com.apple.healthd.workout-gymkit-nfc"
+ "currentDeviceProductType"
+ "debugPeriodicActivityInactivityIntervalInSeconds"
+ "debugPeriodicActivityIntervalInSeconds"
+ "debugPeriodicActivityOnAllHardware"
+ "diagnosticDescription"
+ "gymKitNFCManager"
+ "hasPrefix:"
+ "initWithProfile:name:interval:delegate:loggingCategory:"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "isWaitingToRun"
+ "isWorkoutNFCAllDayEnabledString"
+ "lastActivityDate"
+ "lastActivityDateString"
+ "lastSuccessfulRunDate"
+ "now"
+ "objectForKey:"
+ "performPeriodicActivity:completion:"
+ "periodicActivity:configureXPCActivityCriteria:"
+ "periodicActivityRequiresProtectedData:"
+ "profileDidBecomeReady:"
+ "registerProfileReadyObserver:queue:"
+ "setDateFormat:"
+ "setGymKitNFCManager:"
+ "setLastActivityDate:"
+ "setObject:forKey:"
+ "sharedBehavior"
+ "stringFromDate:"
+ "v24@0:8@\"HDProfile\"16"
+ "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
+ "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
+ "yyyy-MM-dd HH:mm:ss.SSSSSSZZZ"
- "\x02"

```
