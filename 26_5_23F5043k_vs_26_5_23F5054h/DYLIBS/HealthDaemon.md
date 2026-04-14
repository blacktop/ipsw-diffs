## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.6.4.0.0
-  __TEXT.__text: 0x7e2f70
+6200.6.6.0.0
+  __TEXT.__text: 0x7e3130
   __TEXT.__auth_stubs: 0x4b20
   __TEXT.__objc_methlist: 0x441d4
   __TEXT.__const: 0x1fd38

   __TEXT.__swift5_capture: 0x7b8
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_proto: 0x1ac
-  __TEXT.__oslogstring: 0x42d57
+  __TEXT.__oslogstring: 0x42d8d
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__gcc_except_tab: 0x3a428
+  __TEXT.__gcc_except_tab: 0x3a448
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1e868
+  __TEXT.__unwind_info: 0x1e878
   __TEXT.__eh_frame: 0x17f0
   __TEXT.__objc_classname: 0xd10e
   __TEXT.__objc_methname: 0x90159

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2924F16A-9C4B-39F0-BBE6-BDE1673CDD89
-  Functions: 35439
-  Symbols:   105473
-  CStrings:  44523
+  UUID: F970985D-D2D0-3ACD-BD3B-52AD1ED3BF67
+  Functions: 35441
+  Symbols:   105478
+  CStrings:  44524
 
Symbols:
+ -[HDWorkoutManager _notifyForPostLaunchSessionRecovery]
+ ___57-[HDWorkoutObserverServer remote_startTaskServerIfNeeded]_block_invoke_2
Functions:
~ ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke : 2008 -> 2076
+ -[HDWorkoutManager _notifyForPostLaunchSessionRecovery]
~ ___60-[HDWorkoutManager _recoverCurrentWorkoutSessionAfterLaunch]_block_invoke : 236 -> 152
~ -[HDWorkoutManager profileDidBecomeReady:] : 376 -> 420
~ -[HDWorkoutObserverServer remote_startTaskServerIfNeeded] : 192 -> 340
+ ___57-[HDWorkoutObserverServer remote_startTaskServerIfNeeded]_block_invoke_2
CStrings:
+ "%{public}@: Recovering session server with identifier: %{public}@."
+ "%{public}@: Session server with identifier %{public}@ already exist. Skipping recovery."
- "%{public}@: Skipping automatic current workout recovery: session servers (%{public}@) already exist."

```
