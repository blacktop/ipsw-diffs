## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

```diff

-749.36.0.0.0
-  __TEXT.__text: 0xa234
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0x7a8
-  __TEXT.__cstring: 0x22c3
-  __TEXT.__objc_classname: 0x254
-  __TEXT.__objc_methname: 0x23d2
-  __TEXT.__objc_methtype: 0xa77
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x1157
+749.40.0.0.0
+  __TEXT.__text: 0x95bc
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0x6e8
+  __TEXT.__cstring: 0x211f
+  __TEXT.__objc_classname: 0x20f
+  __TEXT.__objc_methname: 0x20f6
+  __TEXT.__objc_methtype: 0x97b
+  __TEXT.__const: 0x20
+  __TEXT.__oslogstring: 0xd77
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__unwind_info: 0x2dc
-  __DATA_CONST.__auth_got: 0x2f0
+  __TEXT.__unwind_info: 0x2ac
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xb00
-  __DATA_CONST.__cfstring: 0xa40
+  __DATA_CONST.__const: 0xac0
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x1a58
-  __DATA.__objc_selrefs: 0x7f8
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x17c0
+  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x540
+  __DATA.__data: 0x420
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4D462A7D-E01A-377F-82AD-438592E7DBD0
-  Functions: 234
-  Symbols:   181
-  CStrings:  710
+  UUID: 8A3E1F2B-639B-3A34-B40E-FFAA38C0B2AD
+  Functions: 216
+  Symbols:   165
+  CStrings:  629
 
Symbols:
+ _HKProductTypePrefixAppleWatch5SECellularBig
+ _HKProductTypePrefixAppleWatch5SECellularSmall
+ _HKProductTypePrefixAppleWatch5SENonCellularBig
+ _HKProductTypePrefixAppleWatch5SENonCellularSmall
+ _kWOConnectedGymDebugDisableGymKitNFCSwitchOnAllHardware
+ _kWOConnectedGymDisableGymKitNFCSwitchOnOldHardwareCompleted
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterRemoveEveryObserver
- _HDDiagnosticStringFromDate
- _HKCreateSerialUtilityDispatchQueue
- _OBJC_CLASS_$_HDPeriodicActivity
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSMutableString
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _kWOConnectedGymDebugPeriodicActivityInactivityIntervalInSeconds
- _kWOConnectedGymDebugPeriodicActivityIntervalInSeconds
- _kWOConnectedGymDebugPeriodicActivityOnAllHardware
- _kWOConnectedGymLastActivityDate
- _kWOInactivityIntervalInSeconds
- _kWOWorkoutGymKitNFCActivityName
- _objc_destroyWeak
- _objc_storeWeak
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_string
CStrings:
+ "\x02"
+ "ConnectedGymDebugDisableGymKitNFCSwitchOnAllHardware"
+ "ConnectedGymDisableGymKitNFCSwitchOnOldHardwareCompleted"
+ "[WorkoutGymKitNFC] Disable GymKit NFC Switch On Old Hardware Completed: %@, NFC All Day Enabled: %@"
+ "[WorkoutGymKitNFC] Initializing WOWorkoutGymKitNFCManager, disableGymKitNFCSwitch (oldHardware: %@ || allHardware: %@)"
+ "[WorkoutGymKitNFC] Not initializing WOWorkoutGymKitNFCManager, disableGymKitNFCSwitch (oldHardware: %@ || allHardware: %@), for testing on all hardware: defaults write %@ %@ 1"
+ "[WorkoutGymKitNFC] One time Disable GymKit NFC Switch On Old Hardware (all day support) already completed"
+ "[WorkoutGymKitNFC] One time Disable GymKit NFC Switch On Old Hardware (all day support), NFC All Day Enabled: %@"
+ "_isWorkoutNFCAllDayEnabledString"
+ "disableGymKitNFCSwitchOnOldHardwareIfNeeded"
+ "setBool:forKey:"
- "\x14"
- ", %@"
- ", InactivityIntervalInSeconds: %ld)"
- ", IntervalInSeconds: %ld"
- ", debugPeriodicActivity (OnAllHardware: %@"
- ", lastActivityDate: %@"
- "@\"HDPeriodicActivity\""
- "@\"NSDateFormatter\""
- "@\"NSUserDefaults\""
- "@\"WOWorkoutGymKitNFCManager\""
- "B24@0:8@\"HDPeriodicActivity\"16"
- "ConnectedGymDebugPeriodicActivityInactivityIntervalInSeconds"
- "ConnectedGymDebugPeriodicActivityIntervalInSeconds"
- "ConnectedGymDebugPeriodicActivityOnAllHardware"
- "ConnectedGymLastActivityDate"
- "ConnectedGymPreferencesChangedNotification"
- "FIUIIsWorkoutNFCAllDayEnabled: %@"
- "HDDiagnosticObject"
- "HDPeriodicActivityDelegate"
- "HDProfileReadyObserver"
- "Not waiting to run"
- "T@\"NSDate\",&,N"
- "T@\"NSString\",R,N"
- "T@\"WOWorkoutGymKitNFCManager\",&,N,V_gymKitNFCManager"
- "TB,R,N"
- "Tq,R,N"
- "Waiting to run"
- "[WorkoutGymKitNFC] (Auto Disable) Workout GymKit NFC All Day support (intervalSinceLastActivityDate %fs is greater then inactivityIntervalInSeconds %fs), WorkoutNFCAllDayEnabled: %@"
- "[WorkoutGymKitNFC] (Keep Current) Workout GymKit NFC All Day support (intervalSinceLastActivityDate %fs is less or equal to inactivityIntervalInSeconds %fs), WorkoutNFCAllDayEnabled: %@"
- "[WorkoutGymKitNFC] <<<< performPeriodicActivity: %@ (%@), elapsed time: %f seconds"
- "[WorkoutGymKitNFC] >>>> performPeriodicActivity: %@ (%@)"
- "[WorkoutGymKitNFC] Current Device Product Type: %@ (oldHardware: %@)"
- "[WorkoutGymKitNFC] Defaults %@ key found in %@ domain, current lastActivityDate: %@"
- "[WorkoutGymKitNFC] Initializing WOWorkoutGymKitNFCManager, periodicActivityOn (oldHardware: %@ || allHardware: %@)"
- "[WorkoutGymKitNFC] Last run: %@"
- "[WorkoutGymKitNFC] No defaults %@ key found in %@ domain, set lastActivityDate to now: %@"
- "[WorkoutGymKitNFC] Not initializing WOWorkoutGymKitNFCManager, periodicActivityOn (oldHardware: %@ || allHardware: %@), for testing on all hardware: defaults write %@ %@ 1"
- "[WorkoutGymKitNFC] Workout GymKit NFC All Day support is Disabled in Settings (WorkoutNFCAllDayEnabled: %@), skip (Auto Disable) checks"
- "[WorkoutGymKitNFC] connectedGymPreferencesChanged: Workout GymKit NFC All Day support is Disabled in Settings, keep current lastActivityDate: %@ (%@)"
- "[WorkoutGymKitNFC] connectedGymPreferencesChanged: Workout GymKit NFC All Day support is Enabled in Settings, set lastActivityDate to now: %@ (%@)"
- "[WorkoutGymKitNFC] dealloc"
- "[WorkoutGymKitNFC] initWithProfile: %@"
- "[WorkoutGymKitNFC] profileDidBecomeReady: scheduler created: %@ (%@)"
- "_connectedGymDefaults"
- "_dateFormatter"
- "_gymKitNFCManager"
- "_queue"
- "_scheduler"
- "appendFormat:"
- "com.apple.healthd.workout-gymkit-nfc"
- "debugPeriodicActivityInactivityIntervalInSeconds"
- "debugPeriodicActivityIntervalInSeconds"
- "debugPeriodicActivityOnAllHardware"
- "diagnosticDescription"
- "gymKitNFCManager"
- "initWithProfile:name:interval:delegate:loggingCategory:"
- "integerForKey:"
- "isWaitingToRun"
- "isWorkoutNFCAllDayEnabledString"
- "lastActivityDate"
- "lastActivityDateString"
- "lastSuccessfulRunDate"
- "now"
- "objectForKey:"
- "performPeriodicActivity:completion:"
- "periodicActivity:configureXPCActivityCriteria:"
- "periodicActivityRequiresProtectedData:"
- "profileDidBecomeReady:"
- "registerProfileReadyObserver:queue:"
- "setDateFormat:"
- "setGymKitNFCManager:"
- "setLastActivityDate:"
- "setObject:forKey:"
- "stringFromDate:"
- "v24@0:8@\"HDProfile\"16"
- "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
- "yyyy-MM-dd HH:mm:ss.SSSSSSZZZ"

```
