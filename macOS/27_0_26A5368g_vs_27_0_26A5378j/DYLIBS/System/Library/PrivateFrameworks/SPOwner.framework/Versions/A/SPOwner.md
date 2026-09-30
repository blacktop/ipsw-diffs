## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-  __TEXT.__text: 0x7b830
-  __TEXT.__objc_methlist: 0xbc3c
-  __TEXT.__const: 0x5b8
-  __TEXT.__gcc_except_tab: 0x144c
-  __TEXT.__cstring: 0x6999
-  __TEXT.__oslogstring: 0x7a98
+  __TEXT.__text: 0x7cfbc
+  __TEXT.__objc_methlist: 0xbd3c
+  __TEXT.__const: 0x5e8
+  __TEXT.__gcc_except_tab: 0x14f0
+  __TEXT.__cstring: 0x69c9
+  __TEXT.__oslogstring: 0x8298
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2478
+  __TEXT.__unwind_info: 0x24d0
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d98
+  __DATA_CONST.__objc_selrefs: 0x3e38
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x5d8
-  __AUTH_CONST.__const: 0x21e8
+  __DATA_CONST.__got: 0x608
+  __AUTH_CONST.__const: 0x2228
   __AUTH_CONST.__cfstring: 0x6000
-  __AUTH_CONST.__objc_const: 0x14610
+  __AUTH_CONST.__objc_const: 0x14738
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH.__objc_data: 0x1308
-  __DATA.__objc_ivar: 0xf3c
+  __DATA.__objc_ivar: 0xf54
   __DATA.__data: 0x15f8
   __DATA.__bss: 0x660
   __DATA_DIRTY.__objc_data: 0x1878

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4374
-  Symbols:   9206
-  CStrings:  2324
+  Functions: 4405
+  Symbols:   9261
+  CStrings:  2351
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[SPBeaconManager simpleBeaconSubscribersInfoWithCompletion:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface armDarwinReconnectObserver]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface armReconnectWatchdog_locked]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface buildSessionForServiceName:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface cancelReconnectWatchdog]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface isSPDCurrentlyRunning]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface machServiceName]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface performProbeGatedRecoveryWithReason:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface reconnectAttempt]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface reconnectGeneration]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface reconnectInProgress]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface reconnectWatchdogTimer]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setReconnectAttempt:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setReconnectGeneration:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setReconnectInProgress:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setReconnectWatchdogTimer:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setStopped:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface setSuppressNextInvalidation:]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface stopped]
+ -[SPBeaconManagerSimpleBeaconUpdateInterface suppressNextInvalidation]
+ GCC_except_table58
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._reconnectAttempt
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._reconnectGeneration
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._reconnectInProgress
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._reconnectWatchdogTimer
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._stopped
+ OBJC_IVAR_$_SPBeaconManagerSimpleBeaconUpdateInterface._suppressNextInvalidation
+ __64-[SPBeaconManagerSimpleBeaconUpdateInterface handleReconnection]_block_invoke
+ __66-[SPBeaconManagerSimpleBeaconUpdateInterface invalidationHandler:]_block_invoke
+ __73-[SPBeaconManagerSimpleBeaconUpdateInterface armReconnectWatchdog_locked]_block_invoke
+ __73-[SPBeaconManagerSimpleBeaconUpdateInterface buildSessionForServiceName:]_block_invoke
+ __95-[SPBeaconManagerSimpleBeaconUpdateInterface startUpdatingSimpleBeaconsWithContext:completion:]_block_invoke
+ ___61-[SPBeaconManager simpleBeaconSubscribersInfoWithCompletion:]_block_invoke
+ ___66-[SPBeaconManagerSimpleBeaconUpdateInterface invalidationHandler:]_block_invoke
+ ___72-[SPBeaconManagerSimpleBeaconUpdateInterface armDarwinReconnectObserver]_block_invoke
+ ___73-[SPBeaconManagerSimpleBeaconUpdateInterface armReconnectWatchdog_locked]_block_invoke
+ ___73-[SPBeaconManagerSimpleBeaconUpdateInterface buildSessionForServiceName:]_block_invoke
+ ___82-[SPBeaconManagerSimpleBeaconUpdateInterface performProbeGatedRecoveryWithReason:]_block_invoke
+ ___86-[SPBeaconManagerSimpleBeaconUpdateInterface stopUpdatingSimpleBeaconsWithCompletion:]_block_invoke_2
+ ___block_descriptor_48_e8_32w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_57_e8_32s40s_e5_v8?0l
+ _bootstrap_look_up3
+ _bootstrap_port
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_msgSend$armDarwinReconnectObserver
+ _objc_msgSend$armReconnectWatchdog_locked
+ _objc_msgSend$buildSessionForServiceName:
+ _objc_msgSend$cancelReconnectWatchdog
+ _objc_msgSend$handleReconnection
+ _objc_msgSend$isSPDCurrentlyRunning
+ _objc_msgSend$machServiceName
+ _objc_msgSend$performProbeGatedRecoveryWithReason:
+ _objc_msgSend$simpleBeaconSubscribersInfoWithCompletion:
- __51-[SPBeaconManagerSimpleBeaconUpdateInterface proxy]_block_invoke
- ___51-[SPBeaconManagerSimpleBeaconUpdateInterface proxy]_block_invoke
- ___66-[SPBeaconManagerSimpleBeaconUpdateInterface interruptionHandler:]_block_invoke
CStrings:
+ "#sbreconnect completion-ignored-stale self=%{public}p stale=%{public}lu current=%{public}lu"
+ "#sbreconnect handleReconnection begin self=%{public}p"
+ "#sbreconnect handleReconnection retry-failed self=%{public}p attempt=%{public}lu error=%@ (arming observer + one-shot reprobe)"
+ "#sbreconnect handleReconnection retry-success self=%{public}p attempt=%{public}lu"
+ "#sbreconnect interrupt-noop self=%{public}p (session already nil — no recovery scheduled)"
+ "#sbreconnect interrupted self=%{public}p connection=%{public}@ hasDiffBlock=%{public}d sessionNonNil=%{public}d willArmObserver=%{public}d"
+ "#sbreconnect invalidated self=%{public}p connection=%{public}@ (probe-gated recovery)"
+ "#sbreconnect invalidated-after-stop self=%{public}p (no recovery scheduled)"
+ "#sbreconnect invalidation-during-reconnect cleared in-progress latch self=%{public}p attempt=%{public}lu"
+ "#sbreconnect invalidation-suppressed self=%{public}p connection=%{public}@ (framework-initiated)"
+ "#sbreconnect observer-rearmed-for-attempt self=%{public}p attempt=%{public}lu"
+ "#sbreconnect probe self=%{public}p result=alive"
+ "#sbreconnect probe self=%{public}p result=dormant kr=%{public}d"
+ "#sbreconnect reconnect-skipped-already-in-progress self=%{public}p (handleReconnection)"
+ "#sbreconnect reconnect-skipped-stopped self=%{public}p (handleReconnection)"
+ "#sbreconnect reconnect-watchdog-armed self=%{public}p attempt=%{public}lu delay=%{public}.1f"
+ "#sbreconnect reconnect-watchdog-fired self=%{public}p attempt=%{public}lu (clearing latch + probing)"
+ "#sbreconnect recovery-decision self=%{public}p reason=%{public}s branch=reconnect-now (SPD alive)"
+ "#sbreconnect recovery-decision self=%{public}p reason=%{public}s branch=wait-for-darwin (SPD dormant)"
+ "#sbreconnect remove-observers self=%{public}p (typically handleReconnection success or dealloc)"
+ "#sbreconnect session-rebuilt self=%{public}p attempt=%{public}lu"
+ "#sbreconnect session-start completion self=%{public}p success=%{public}d"
+ "#sbreconnect session-start completion self=%{public}p success=%{public}d error=%@"
+ "#sbreconnect session-start self=%{public}p contextClass=%{public}@ sendInitial=%{public}d"
+ "error-retry"
+ "interrupt"
+ "invalidate"
+ "watchdog"
- "Failed reconnecting to daemon after retry: %@."

```
