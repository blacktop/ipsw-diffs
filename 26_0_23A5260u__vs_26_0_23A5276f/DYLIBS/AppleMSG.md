## AppleMSG

> `/System/Library/PrivateFrameworks/AppleMSG.framework/AppleMSG`

```diff

-101.0.15.0.0
-  __TEXT.__text: 0x13e6c
-  __TEXT.__auth_stubs: 0x370
+101.0.18.0.0
+  __TEXT.__text: 0x15264
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0xd8
-  __TEXT.__oslogstring: 0xa84
-  __TEXT.__cstring: 0x1b80
+  __TEXT.__oslogstring: 0xb7c
+  __TEXT.__cstring: 0x1d21
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__unwind_info: 0x3b0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x70
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x40
   __DATA.__common: 0x18

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D9F07F5A-306B-3C8F-BA2C-32D4C9D836E1
-  Functions: 450
-  Symbols:   847
-  CStrings:  229
+  UUID: 1F08B357-5FF7-348B-99AC-9646E05B9940
+  Functions: 475
+  Symbols:   909
+  CStrings:  242
 
Symbols:
+ _MSGConfigureBaseSync.cold.2
+ _MSGConfigureDerivedSync.cold.2
+ _MSGEnableSyncInterrupt.cold.2
+ _MSGGetCurrentSyncTiming
+ _MSGGetCurrentSyncTiming.cold.1
+ _MSGGetCurrentSyncTiming.cold.2
+ _MSGGetCurrentSyncTiming.cold.3
+ _MSGGetFutureSyncTiming
+ _MSGGetFutureSyncTiming.cold.1
+ _MSGGetFutureSyncTiming.cold.2
+ _MSGGetFutureSyncTiming.cold.3
+ _MSGGetSyncConfig.cold.2
+ _MSGGetSyncRunState
+ _MSGGetSyncRunState.cold.1
+ _MSGGetSyncRunState.cold.2
+ _MSGGetSystemState
+ _MSGInitBaseSync.cold.2
+ _MSGInitDerivedSync.cold.2
+ _MSGRegisterForEventTriggerTiming
+ _MSGRegisterForEventTriggerTiming.cold.1
+ _MSGRegisterForSyncTiming
+ _MSGRegisterForSyncTiming.cold.1
+ _MSGRegisterForSyncTiming.cold.2
+ _MSGResetSync.cold.2
+ _MSGStartSync.cold.2
+ _MSGUnregisterFromEventTriggerTiming
+ _MSGUnregisterFromEventTriggerTiming.cold.1
+ _MSGUnregisterFromSyncTiming
+ _MSGUnregisterFromSyncTiming.cold.1
+ _MSGUnregisterFromSyncTiming.cold.2
+ _controllerMutex
- _MSGRegisterForEventTriggerInfo
- _MSGRegisterForEventTriggerInfo.cold.1
- _MSGUnregisterForEventTriggerInfo
- _MSGUnregisterForEventTriggerInfo.cold.1
- __ZN13MSGController26SetCurrentDisplayFramerateEjjty
- _controller_mutex
- _kdebug_trace
CStrings:
+ "!syncHandle->remote"
+ "(syncHandle->id == 0)"
+ "Invalid sync handle passed in"
+ "MSGClientAPI_EventTriggers::%s: Error (%x) getting the event trigger interrupt status\n\n"
+ "MSGClientAPI_EventTriggers::%s: Error (%x) registering for the event trigger timing for id %d\n\n"
+ "MSGClientAPI_EventTriggers::%s: Error (%x) unregistering from the event trigger timing for id %d\n\n"
+ "MSGClientAPI_Syncs::%s: getNextNFrames failed with retcode: %#x\n\n"
+ "MSGGetCurrentSyncTiming is currently only supported for sync 0"
+ "MSGGetCurrentSyncTiming is not supported on the remote"
+ "MSGGetFutureSyncTiming"
+ "MSGGetFutureSyncTiming is currently only supported for sync 0"
+ "MSGGetFutureSyncTiming is not supported on the remote"
+ "MSGRegisterForEventTriggerTiming"
+ "MSGUnregisterFromEventTriggerTiming"
+ "Maximum subscription count reached!"
+ "Registering for sync timing information is not supported on the remote"
+ "controller"
+ "syncHandle"
- "Controller"
- "MSGClientAPI_EventTriggers::%s: Error (%x) registering for the event trigger information for id %d\n\n"
- "MSGRegisterForEventTriggerInfo"
- "MSGUnregisterForEventTriggerInfo"
- "Maximum subsciption count reached!"

```
