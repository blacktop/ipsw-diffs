## dasd

> `/usr/libexec/dasd`

```diff

-2109.100.198.0.0
-  __TEXT.__text: 0x151050
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0x18c40
-  __TEXT.__objc_methlist: 0x11ce0
+2109.100.204.0.0
+  __TEXT.__text: 0x151794
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_stubs: 0x18c80
+  __TEXT.__objc_methlist: 0x11e20
   __TEXT.__const: 0x9e2
-  __TEXT.__objc_methname: 0x2a4e5
-  __TEXT.__cstring: 0xf1ed
-  __TEXT.__oslogstring: 0x12e99
-  __TEXT.__objc_classname: 0x19b1
-  __TEXT.__objc_methtype: 0x3c2c
+  __TEXT.__objc_methname: 0x2a675
+  __TEXT.__cstring: 0xf3fd
+  __TEXT.__oslogstring: 0x12f49
+  __TEXT.__objc_classname: 0x19d1
+  __TEXT.__objc_methtype: 0x3c4c
   __TEXT.__gcc_except_tab: 0x522c
   __TEXT.__dlopen_cstrs: 0x4e2
   __TEXT.__swift5_typeref: 0x54

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x8a
   __TEXT.__swift5_fieldmd: 0x4c
-  __TEXT.__unwind_info: 0x5ac0
-  __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0xad8
+  __TEXT.__unwind_info: 0x5b10
+  __DATA_CONST.__auth_got: 0xb50
+  __DATA_CONST.__got: 0xae8
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x40a0
-  __DATA_CONST.__cfstring: 0x10400
-  __DATA_CONST.__objc_classlist: 0x648
+  __DATA_CONST.__const: 0x4128
+  __DATA_CONST.__cfstring: 0x10580
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x560
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_intobj: 0x1590
   __DATA_CONST.__objc_arraydata: 0x338
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x1b8
-  __DATA.__objc_const: 0x304c0
-  __DATA.__objc_selrefs: 0x9148
-  __DATA.__objc_ivar: 0x1460
-  __DATA.__objc_data: 0x3f68
+  __DATA.__objc_const: 0x30c20
+  __DATA.__objc_selrefs: 0x9180
+  __DATA.__objc_ivar: 0x1480
+  __DATA.__objc_data: 0x3fb8
   __DATA.__data: 0x1760
-  __DATA.__bss: 0xc78
+  __DATA.__bss: 0xc90
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 25770FB8-7E61-3EEA-A14A-230ABFDDD4F5
-  Functions: 7341
-  Symbols:   734
-  CStrings:  13613
+  UUID: 8855E93C-0663-3B94-BA45-26F427EEAB16
+  Functions: 7362
+  Symbols:   739
+  CStrings:  13652
 
Symbols:
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _arc4random
+ _fmod
+ _sleep
CStrings:
+ "1149321"
+ "Activity '%@' temporarily deferred for battery optimization during device inactivity (backoffTime=%.0fs)"
+ "B40@0:8d16@24^d32"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Flushing PPS cache before TTR for IdleStack: %{public}@"
+ "IdleStack task '%@' was asked to run but failed to launch within %ld seconds.\n\nDebug Info:\n{\n    activityIdentifier = \"%@\";\n    activityName = \"%@\";\n    schedulingPriority = %ld;\n    timeoutDuration = %ld;\n    trigger = \"IdleStack activity failed to launch within timeout period\";\n}\n\nCustom Root Installed: %@"
+ "Implements progressive backoff for discretionary activities during device inactivity on battery"
+ "No"
+ "Progressive Backoff Policy"
+ "Progressive backoff cycle STARTED - device idle and unplugged"
+ "Progressive backoff: disabled"
+ "Progressive backoff: enabled=1, durations(min): ON=%.1f, OFF1=%.1f, OFF2=%.1f, OFF3=%.1f"
+ "ProgressiveBackoffPolicy"
+ "Reproducible"
+ "RootInstalled"
+ "Saved TTR timestamp to defaults"
+ "Serious Bug"
+ "Skipping TTR for IdleStack due to rate limiting (last filed: %.0f seconds ago)"
+ "Sometimes"
+ "T@\"NSArray\",&,N,V_inactivityBackoffDurations"
+ "T@\"NSDate\",&,V_progressiveBackoffStartTime"
+ "Tap to Radar. Background maintenance task was asked to launch but failed"
+ "Tap to file Radar. Background maintenance task was asked to launch but failed"
+ "Title"
+ "Triggered TTR notification for IdleStack activity launch timeout: %{public}@"
+ "URL"
+ "Waiting for ClientFailedToLaunch checkpoint to reach PPS for IdleStack: %{public}@"
+ "Yes"
+ "[Internal] Background Maintenance Task Launch Failure"
+ "_DASProgressiveBackoffPolicy"
+ "_inactivityBackoffDurations"
+ "_progressiveBackoffStartTime"
+ "all"
+ "calculateBackoffDurationsWithInitialOff:maxOff:"
+ "com.apple.dasd.idlestack"
+ "com.apple.idleStack"
+ "componentsWithString:"
+ "defaultInactivityBackoffDurations"
+ "handleIdleStackLaunchFailureTTR:"
+ "inactivityBackoffDurations"
+ "inactivityInitialOffDuration"
+ "inactivityMaxOffDuration"
+ "inactivityProgressiveBackoffEnabled"
+ "isPluggedIn == NO AND deviceCompletelyIdle == YES AND progressiveBackoffActive == YES"
+ "lastTTRTimestamp"
+ "progressiveBackoffStartTime"
+ "queryItemWithName:value:"
+ "setInactivityBackoffDurations:"
+ "setProgressiveBackoffStartTime:"
+ "setQueryItems:"
+ "shouldAllowTasksWithProgressiveBackoff:withDurations:"
+ "shouldAllowTasksWithProgressiveBackoff:withDurations:timeUntilNextOn:"
+ "tap-to-radar://new"
- "Background maintenance tasks (IdleStack) are experiencing failures over the last 15 days.\n\nAdditional details are available in the Debug Info section below.\n\n"
- "Core"
- "First IdleStack TTR criteria not met; Skipping TTR"
- "First IdleStack TTR: failedToLaunch=%lu, failureRate=%.2f%%"
- "High failure rate for IdleStack activities"
- "IdleStack checkpoint summary - Total attempts: %lu, Failed to launch: %lu, Canceled: %lu, Affected tasks: %lu"
- "Name LIKE %@"
- "No IdleStack failures detected; Skipping TTR"
- "Subsequent IdleStack TTR thresholds not met; Skipping TTR"
- "Subsequent IdleStack TTR: failedToLaunch=%lu, failureRate=%.2f%%"
- "Tap to file Radar. Background maintenance tasks are experiencing failures"
- "Triggering TTR for IdleStack launch failures"
- "[Internal] Daily Storage Maintenance Activity"
- "affectedTasks"
- "canceledCount"
- "checkProgressForIdleStack"
- "com.apple.idleStack%"
- "failedToLaunch"
- "failedToLaunchCount"
- "failureRate"
- "fetchIdleStackTaskNames"
- "generateIdleStackTTRWithMetrics:"
- "lastDateForIdleStackProgressTTR"
- "lookBackDays"
- "processIdleStackMetrics:"
- "shouldGenerateIdleStackTTRForMetrics:"
- "shouldSkipIdleStackCheck"
- "timeOfDetection"
- "totalAttempts"
- "totalIssues"

```
