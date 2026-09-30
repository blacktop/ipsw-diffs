## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4024.440.1.0.0
-  __TEXT.__text: 0x6f138
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0xa520
-  __TEXT.__objc_methlist: 0x4e60
-  __TEXT.__const: 0x258
-  __TEXT.__gcc_except_tab: 0xb24
-  __TEXT.__objc_classname: 0x1470
-  __TEXT.__objc_methname: 0x10fc6
-  __TEXT.__objc_methtype: 0x3258
-  __TEXT.__cstring: 0x5bff
-  __TEXT.__oslogstring: 0xd77e
+4024.540.1.0.0
+  __TEXT.__text: 0x6df34
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_stubs: 0xa500
+  __TEXT.__objc_methlist: 0x5be4
+  __TEXT.__const: 0x248
+  __TEXT.__gcc_except_tab: 0xae0
+  __TEXT.__objc_classname: 0x146d
+  __TEXT.__objc_methname: 0x10f3d
+  __TEXT.__objc_methtype: 0x32a0
+  __TEXT.__cstring: 0x5b5f
+  __TEXT.__oslogstring: 0xd2ee
   __TEXT.__dlopen_cstrs: 0xe7
-  __TEXT.__unwind_info: 0x1488
+  __TEXT.__unwind_info: 0x13f8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__const: 0x2bc8
-  __DATA_CONST.__cfstring: 0x4c20
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x760
+  __DATA_CONST.__const: 0x2b68
+  __DATA_CONST.__cfstring: 0x4c40
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x118

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xca00
-  __DATA.__objc_selrefs: 0x3640
-  __DATA.__objc_ivar: 0x620
+  __DATA.__objc_const: 0xb028
+  __DATA.__objc_selrefs: 0x3850
+  __DATA.__objc_ivar: 0x614
   __DATA.__objc_data: 0x28f0
   __DATA.__data: 0xd30
   __DATA.__bss: 0x110

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1818C220-2783-3767-9C6F-E3D7B4610A4D
-  Functions: 2060
-  Symbols:   487
-  CStrings:  4957
+  UUID: FE4B1CFC-BB9D-3805-83CD-3C25B5EE5825
+  Functions: 2022
+  Symbols:   463
+  CStrings:  4937
 
Symbols:
+ _OBJC_CLASS_$_ICBackgroundTaskScheduler
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_15_MIN
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_7_DAYS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- _xpc_activity_copy_criteria
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_criteria
- _xpc_activity_set_state
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_get_double
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_double
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "%{public}@ Failed to load the bag - will use default frequency"
+ "%{public}@ No pending events - canceling any previously scheduled task"
+ "%{public}@ Not scheduling a flush because one is already scheduled"
+ "%{public}@ Retrieved flush frequency from bag value: %f"
+ "%{public}@ starting operation to flush play activity events"
+ "@\"NSDictionary\"32@0:8@\"AMSPushPayload\"16@\"NSString\"24"
+ "ICDBackgroundTaskManager %p - startPeriodicPolling - Setting timer to perform periodic poll for %llds"
+ "_scheduleNextPlayActivityFlushOperationReplacingExisting:"
+ "authenticationProvider"
+ "cancelTask:"
+ "com.apple.itunescloud.ICPlayActivityServer.flush_task"
+ "hasScheduledTask:"
+ "importContainerArtworkForSagaID:artworkVariantType:configuration:completion:"
+ "pushPayload:metricsOverlayForType:"
+ "registerForTask:handler:"
+ "sagaPushNotificationTimes"
+ "scheduleRecurringTask:withInterval:afterDelay:withUserData:"
+ "scheduleTask:afterDelay:withUserData:"
+ "setSagaPushNotificationTimes:"
+ "sharedTaskScheduler"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v48@0:8Q16q24@\"ICConnectionConfiguration\"32@?<v@?@\"NSError\">40"
+ "v48@0:8Q16q24@32@?40"
- "%{public}@ Creating new criteria to fire on %{public}@ with grace period till %{public}@"
- "%{public}@ Did not find postFrequency from bag using default value (%f)"
- "%{public}@ Found existing activity to flush play activity events on %{public}@"
- "%{public}@ Found postFrequency %f from bag"
- "%{public}@ Have pending play activity events to flush"
- "%{public}@ Loading default nextFlushPlayActivityFireSyncInterval to %f"
- "%{public}@ Loading next play activity flush event to fire on %{public}@"
- "%{public}@ No active user identity - using default value (%f) to update the criteria to flush play activity events"
- "%{public}@ Not creating a new criteria for flush play activity events nextFlushPlayActivityFireSyncInterval (%f), testNextFlushPlayActivityFireSyncInterval (%f)"
- "%{public}@ Setting criteria to fire the next play activity event on %{public}@"
- "%{public}@ Unknown state"
- "%{public}@ starting operation for flush play activity events pendingOperationCount %lld, nextFlushPlayActivityFireSyncInterval %f, _testNextFlushPlayActivityFireSyncInterval %f "
- "%{public}@ starting xpc activity to flush play activity events"
- "%{public}@ updating current criteria to flush the next play activity event from %{public}@ to %{public}@"
- "@24@0:8d16"
- "@32@0:8q16q24"
- "@40@0:8@16q24q32"
- "B24@0:8d16"
- "CloudPlayActivityListenerNextFlushPlayActivityFireDateKey"
- "ICDBackgroundTaskManager %p - periodicPolling - Ignoring activity [State != Run]"
- "ICDBackgroundTaskManager %p - scheduleTask - Unable to force task termination [%{public}@]"
- "ICDBackgroundTaskManager %p - scheduleTask - Unable to perform asynchrounous work [%{public}@]"
- "ICDBackgroundTaskManager %p - startPeriodicPolling - Setting timer to perform periodic poll for %llds (+/- %llds)"
- "Invalid parameter not satisfying: %@"
- "_cellularDataAllowed"
- "_criteriaDictionaryWithPostFrequency:"
- "_deferredPushActivityCriteriaForTask:startTime:gracePeriod:"
- "_flushOperationCount"
- "_isValidTimeInterval:"
- "_nextFlushPlayActivityFireSyncInterval"
- "_periodicPollingActivityCriteriaWithRefreshInterval:gracePeriod:"
- "_pollingGracePeriodSecondsForRefreshInterval:"
- "_scheduleNextPlayActivityFlushOperationWithCriteria:"
- "_testNextFlushPlayActivityFireSyncInterval"
- "_timeIntervalForNextFlushOperationWithReplyBlock:"
- "activityCriteriaForTask:startTimeInSeconds:"
- "com.apple.itunescloudd.flushPlayactivityEventsBackgroundTask"
- "d"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSince1970:"
- "q24@0:8q16"
- "task.configuration.userIdentity.accountDSID != nil"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v16@?0d8"

```
