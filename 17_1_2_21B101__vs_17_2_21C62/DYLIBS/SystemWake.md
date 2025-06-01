## SystemWake

> `/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake`

```diff

-651.3.0.0.0
-  __TEXT.__text: 0x9350
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x498
+651.5.0.0.0
+  __TEXT.__text: 0x96f4
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x4a8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__gcc_except_tab: 0xc18
   __TEXT.__cstring: 0x96c
-  __TEXT.__oslogstring: 0x109c
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__oslogstring: 0x11f8
+  __TEXT.__unwind_info: 0x458
   __TEXT.__objc_classname: 0x20b
-  __TEXT.__objc_methname: 0x117b
+  __TEXT.__objc_methname: 0x11a7
   __TEXT.__objc_methtype: 0x548
-  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__objc_stubs: 0xae0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1720
-  __DATA_CONST.__objc_selrefs: 0x340
+  __DATA_CONST.__objc_const: 0x16b0
+  __DATA_CONST.__objc_selrefs: 0x348
   __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2c8
   __DATA.__objc_classrefs: 0xc8
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x3c0
   __DATA.__common: 0x10
   __DATA_DIRTY.__const: 0xa0

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60B08BE2-2ECA-3A33-82DB-341AE7910E62
-  Functions: 137
-  Symbols:   769
-  CStrings:  513
+  UUID: 40940AD8-8B90-31FA-97C1-23E414FB8F37
+  Functions: 140
+  Symbols:   778
+  CStrings:  516
 
Symbols:
+ -[SWSystemActivityAssertion _queue_declareSystemActivityWithRetryCount:]
+ -[SWSystemActivityAssertion isPreventingSleep]
+ GCC_except_table16
+ GCC_except_table20
+ __OBJC_$_PROP_LIST_SWSystemActivityAcquisitionDetails.182
+ ___72-[SWSystemActivityAssertion _queue_declareSystemActivityWithRetryCount:]_block_invoke
+ ___72-[SWSystemActivityAssertion _queue_declareSystemActivityWithRetryCount:]_block_invoke.39
+ ___block_descriptor_60_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$aggregateState
+ _objc_msgSend$sentinelWithSignalCount:signalHandler:
+ _objc_msgSend$sleepMonitorState
+ _objc_msgSend$sleepMonitorStateTimestamp
- GCC_except_table22
- _OBJC_IVAR_$_SWSystemSleepMonitorAggregateState._phase
- _OBJC_IVAR_$_SWSystemSleepMonitorAggregateState._phaseTimestamp
- _OBJC_IVAR_$_SWSystemSleepMonitorAggregateState._state
- _OBJC_IVAR_$_SWSystemSleepMonitorAggregateState._stateTimestamp
- __OBJC_$_PROP_LIST_SWSystemActivityAcquisitionDetails.178
- ___57-[SWSystemActivityAssertion _queue_declareSystemActivity]_block_invoke
- _objc_msgSend$sentinelWithQueue:signalCount:signalHandler:
CStrings:
+ "%p created system activity assertion too late, will wait for next system wake, id:%{public}@ err:%ld wasSleepImminent:%{BOOL}u retry:%u"
+ "%p created system activity assertion; id:%{public}@ systemState:%u assertionID:%lu wasSleepImminent:%{BOOL}u retry:%u"
+ "%p created system activity unable to revert sleep - possible race with powerd - no more retries allowed, id:%{public}@ err:%ld wasSleepImminent:%{BOOL}u retry:%u"
+ "%p created system activity unable to revert sleep - possible race with powerd - will wait 500ms and try again, id:%{public}@ err:%ld wasSleepImminent:%{BOOL}u retry:%u"
+ "TB,R,N,GisPreventingSleep"
+ "_queue_declareSystemActivityWithRetryCount:"
+ "isPreventingSleep"
+ "preventingSleep"
+ "sentinelWithSignalCount:signalHandler:"
- "%p created system activity assertion too late, will wait for next system wake, id:%{public}@ err:%ld wasSleepImminent:%{BOOL}u"
- "%p created system activity assertion; id:%{public}@ systemState:%u assertionID:%lu wasSleepImminent:%{BOOL}u"
- "_phase"
- "_phaseTimestamp"
- "_queue_declareSystemActivity"
- "sentinelWithQueue:signalCount:signalHandler:"

```
