## libfire9.dylib

> `/usr/lib/libfire9.dylib`

### Sections with Same Size but Changed Content

- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0x301f94
-  __TEXT.__const: 0x9f6e8
-  __TEXT.__cstring: 0x1bd44
-  __TEXT.__oslogstring: 0x1938e
+32.0.0.0.0
+  __TEXT.__text: 0x302628
+  __TEXT.__const: 0x9f758
+  __TEXT.__cstring: 0x1bd1a
+  __TEXT.__oslogstring: 0x1943e
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xaa00
+  __DATA_CONST.__const: 0xaa08
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xf728
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x220
   __DATA.__data: 0x148
   __DATA.__common: 0x640
-  __DATA.__bss: 0x26d8
+  __DATA.__bss: 0x26d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 7594
-  Symbols:   8823
-  CStrings:  5180
+  Functions: 7601
+  Symbols:   8827
+  CStrings:  5183
 
Symbols:
+ __ZN13FireDeviceLog13LoggingBuffer5ResetEv
+ __ZN15FireResourceMgr5resetEv
+ __ZN18FireMessageHandler11resetEngineEv
+ __ZN18FireMessageHandler14createGlEngineEv
+ __ZN18FireMessageHandler19ExclusiveEntryCheck10resetCountEv
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_670616EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_670616EPvs
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_670616EPvs
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_670616EPvs
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_670616EPvs
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_670616EPvs
+ __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEE7__cloneEPNS0_6__baseIS4_EE
+ __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEE7__cloneEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEED0Ev
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEED1Ev
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEEclEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEE7destroyEv
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEED0Ev
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEED1Ev
+ __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEEclEOS4_Om
+ __ZNSt3__15dequeIN18FireMessageHandler21GLRefPositionExtendedENS_9allocatorIS2_EEED2B9fqn220106Ev
+ __ZNSt3__15dequeIN7BlueFin13GlExtSensDataENS_9allocatorIS2_EEED2B9fqn220106Ev
+ __ZTVNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvvEEE
+ __ZTVNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_2FvPhmEEE
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_670616EPvs
- __Exit
- __ZN13FireDeviceLog24GlRestartFailureReportedE
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_669867EPvs
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_669867EPvs
- __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEE7__cloneEPNS0_6__baseIS7_EE
- __ZNKSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEE7__cloneEv
- __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEE7destroyEv
- __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEED0Ev
- __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEED1Ev
- __ZNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEEclEOS4_Om
- __ZNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEE7destroyEv
- __ZNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEED0Ev
- __ZNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEED1Ev
- __ZNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEEclEv
- __ZNSt3__16vectorIhNS_9allocatorIhEEE24__emplace_back_slow_pathIJRhEEEPhDpOT_
- __ZTVNSt3__110__function6__funcIZN18FireMessageHandler14createGlEngineEvE3$_1FvPhmEEE
- __ZTVNSt3__110__function6__funcIZN18FireMessageHandlerC1EPN7BlueFin8GlEngineEE4$_12FvvEEE
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_669867EPvs
CStrings:
+ "#fgd,reset"
+ "@(#)Broadcom GLL ver. 172.20.28 670616, 2026/Jul/16, 16:02:15, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
+ "Aug  3 2026, 21:35:14"
+ "ChipData_GRABSNQ_670616"
+ "ERROR: LTO/RTO mimatch. Expected %s, got %s\n"
+ "FIRE@32 GLL@670616"
+ "FireMessageHandler,resetEngine,state,%d,pending,%zu"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 670125 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 670125 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 670125 $"
+ "kReset"
+ "resetEngine,recreateGlEngine,done"
+ "send,message,%d,droppedInRecovery"
- "@(#)Broadcom GLL ver. 172.20.28 669867, 2026/Jul/01, 22:23:04, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
- "ChipData_GRABSNQ_669867"
- "FIRE@30 GLL@669867"
- "FireMessageHandler"
- "Jul 10 2026, 01:09:00"
- "abnormalStopCrash"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 669866 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 669866 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 669866 $"
- "readLtoFile"
```
