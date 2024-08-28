## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-5200.1.3.0.0
-  __TEXT.__text: 0x760608
+5200.1.5.4.0
+  __TEXT.__text: 0x76127c
   __TEXT.__auth_stubs: 0x3710
-  __TEXT.__objc_methlist: 0x3cd18
+  __TEXT.__objc_methlist: 0x3cd40
   __TEXT.__const: 0x1c39c
-  __TEXT.__oslogstring: 0x3ebe5
+  __TEXT.__oslogstring: 0x3ed17
   __TEXT.__swift5_typeref: 0x387
   __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__constg_swiftt: 0x4fc
-  __TEXT.__cstring: 0x760fe
+  __TEXT.__cstring: 0x7621c
   __TEXT.__swift5_reflstr: 0x1b0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_capture: 0xe0
-  __TEXT.__gcc_except_tab: 0x379cc
+  __TEXT.__gcc_except_tab: 0x37a84
   __TEXT.__dlopen_cstrs: 0x15b
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1c170
+  __TEXT.__unwind_info: 0x1c1c8
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0xc675
-  __TEXT.__objc_methname: 0x8ba64
-  __TEXT.__objc_methtype: 0x174df
-  __TEXT.__objc_stubs: 0x4efe0
-  __DATA_CONST.__got: 0x50b8
-  __DATA_CONST.__const: 0x1cc50
+  __TEXT.__objc_methname: 0x8bb34
+  __TEXT.__objc_methtype: 0x174ed
+  __TEXT.__objc_stubs: 0x4f060
+  __DATA_CONST.__got: 0x50c0
+  __DATA_CONST.__const: 0x1cc78
   __DATA_CONST.__objc_classlist: 0x2890
   __DATA_CONST.__objc_catlist: 0x488
   __DATA_CONST.__objc_protolist: 0x9a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19228
+  __DATA_CONST.__objc_selrefs: 0x19248
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x1d98
   __DATA_CONST.__objc_arraydata: 0x8708
   __AUTH_CONST.__auth_got: 0x1ba0
   __AUTH_CONST.__auth_ptr: 0xa8
   __AUTH_CONST.__const: 0xdc98
-  __AUTH_CONST.__cfstring: 0x3c420
-  __AUTH_CONST.__objc_const: 0x83a28
+  __AUTH_CONST.__cfstring: 0x3c460
+  __AUTH_CONST.__objc_const: 0x83ac8
   __AUTH_CONST.__objc_arrayobj: 0x1ec0
   __AUTH_CONST.__objc_intobj: 0x4410
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xb688
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x4294
+  __DATA.__objc_ivar: 0x429c
   __DATA.__data: 0x76c0
   __DATA.__bss: 0x2b0
   __DATA.__common: 0x24
-  __DATA_DIRTY.__objc_ivar: 0xe58
+  __DATA_DIRTY.__objc_ivar: 0xe5c
   __DATA_DIRTY.__objc_data: 0xe448
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x400

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 33344
-  Symbols:   39870
-  CStrings:  35697
+  Functions: 33356
+  Symbols:   39883
+  CStrings:  35711
 
Symbols:
+ _HKApplicationIdentifierEntitlement
CStrings:
+ "%!{(MISSING)public}@: Posting notification for Bluetooth to start collection"
+ "TB,R,N,V_isInForeground"
+ "@60@0:8q16@24q32Q40B48^@52"
+ "isInForeground"
+ "updateDataUploadRequestStatus:"
+ "com.apple"
+ "(isInForeground=%!@(MISSING), hasRunningWorkout=%!@(MISSING), hasBackgroundObserver=%!@(MISSING))"
+ "<%!@(MISSING):%!p(MISSING)> %!@(MISSING) (%!l(MISSING)fs, inForeground=%!@(MISSING), hasRunningWorkout=%!@(MISSING), hasBackgroundObserver=%!@(MISSING))"
+ "%!{(MISSING)public}@: Anchor is less then or equal to anchor returned in initial results. Skipping update"
+ "configurationWithLatency:interval:seriesDuration:activeWorkout:foregroundObserver:backgroundObserver:"
+ "%!{(MISSING)public}@: Entering running state and collection stopped. Will not take assertion."
+ "(%!l(MISSING)fs, latency %!l(MISSING)fs, series %!l(MISSING)fs, %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING))"
+ "_isInForeground"
+ "setHasBackgroundObserver:"
+ "<Interval: %!l(MISSING)fs, Latency: %!l(MISSING)fs, Duration: %!l(MISSING)fs, Workout: %!s(MISSING), Foreground: %!s(MISSING), Background: %!s(MISSING)>"
+ "objectsAssociatedWithObjectPID:subObjectReference:dataTypes:associationType:limit:sortDescending:profile:error:"
+ "hasBackgroundObserver"
+ "BACKGROUND RUNNING"
+ "setDataUploadRequestStatus:profileType:"
+ "TB,R,N,V_hasBackgroundObserver"
+ "@52@0:8d16d24d32B40B44B48"
+ "%!{(MISSING)public}@: Attempting to set samples types and collection already ended"
+ "dataCollectionObserverStateInForeground:hasRunningWorkout:hasBackgroundObserver:"
+ "[routes] [elevation] %!{(MISSING)public}@ Error  currentElevationGain: %!l(MISSING)u is less than previousGain:%!l(MISSING)u"
+ "TB,N,V_hasBackgroundObserver"
+ "WITH RECURSIVE generate_series(value) AS (SELECT 0 UNION ALL SELECT value+1 FROM generate_series WHERE value<%!l(MISSING)d) SELECT value, (SELECT MAX(%!@(MISSING)) FROM %!@(MISSING) WHERE %!@(MISSING)=value) as anchor FROM generate_series WHERE anchor IS NOT NULL;"
+ "%!{(MISSING)public}@ Successfully completed sync for Tinker data available for download notification"
+ "_fetchSamplesForWorkoutPID:activity:options:limit:sortDescending:error:"
+ "_hasBackgroundObserver"
+ "@28@0:8B16B20B24"
+ "%!{(MISSING)public}@ Error syncing Tinker data available for download notification %!{(MISSING)public}@"
- "<%!@(MISSING):%!p(MISSING)> %!@(MISSING) (%!l(MISSING)fs, inBackground=%!@(MISSING), hasRunningWorkout=%!@(MISSING))"
- "@76@0:8@16@24@32Q40Q48B56@60^@68"
- "latestObjectAssociatedWithObjectPID:subObjectReference:dataTypes:associationType:limit:sortDescending:profile:error:"
- "TB,R,N,V_isInBackground"
- "%!{(MISSING)publice}@: Anchor is less then or equal to anchor returned in initial results. Skipping update"
- "<Interval: %!l(MISSING)fs, Latency: %!l(MISSING)fs, Duration: %!l(MISSING)fs, Workout: %!s(MISSING), Foreground: %!s(MISSING)>"
- "latestObjectAssociatedWithObjectUUID:subObjectReference:dataTypes:associationType:limit:sortDescending:profile:error:"
- "SELECT %!@(MISSING), MAX(%!@(MISSING)) FROM %!@(MISSING) GROUP BY %!@(MISSING);"
- "(isInBackground=%!@(MISSING), hasRunningWorkout=%!@(MISSING))"
- "%!{(MISSING)public}@ Successfully triggered sync for Tinker data available for download notification"
- "_fetchSamplesForWorkoutPID:activity:error:"
- "@48@0:8d16d24d32B40B44"
- "configurationWithLatency:interval:seriesDuration:activeWorkout:foregroundObserver:"
- "_isInBackground"
- "isInBackground"
- "%!{(MISSING)public}@ Error triggering sync for Tinker data available for download notification %!{(MISSING)public}@"
- "(%!l(MISSING)fs, latency %!l(MISSING)fs, series %!l(MISSING)fs, %!@(MISSING), %!@(MISSING), %!@(MISSING))"

```
