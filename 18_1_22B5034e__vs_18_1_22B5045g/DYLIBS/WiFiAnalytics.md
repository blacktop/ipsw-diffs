## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-610.1.0.0.0
-  __TEXT.__text: 0xf1554
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0xc36c
+610.5.0.0.0
+  __TEXT.__text: 0xefc74
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0xc244
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0xe086
-  __TEXT.__oslogstring: 0xb5d9
+  __TEXT.__cstring: 0xde8c
+  __TEXT.__oslogstring: 0xb05b
   __TEXT.__swift5_typeref: 0x128
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_reflstr: 0x61
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x2c0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1154
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__gcc_except_tab: 0x1108
+  __TEXT.__unwind_info: 0x1c50
   __TEXT.__eh_frame: 0x670
-  __TEXT.__objc_classname: 0xac6
-  __TEXT.__objc_methname: 0x193ab
-  __TEXT.__objc_methtype: 0x34ab
-  __TEXT.__objc_stubs: 0x8f00
-  __DATA_CONST.__got: 0x650
-  __DATA_CONST.__const: 0x1a08
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__objc_classname: 0xaaf
+  __TEXT.__objc_methname: 0x19025
+  __TEXT.__objc_methtype: 0x3487
+  __TEXT.__objc_stubs: 0x8de0
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__const: 0x1968
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c30
+  __DATA_CONST.__objc_selrefs: 0x6b80
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x1370
-  __AUTH_CONST.__cfstring: 0xb180
-  __AUTH_CONST.__objc_const: 0x11028
+  __AUTH_CONST.__const: 0x1350
+  __AUTH_CONST.__cfstring: 0xb120
+  __AUTH_CONST.__objc_const: 0x10dc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH.__objc_data: 0x408
-  __DATA.__objc_ivar: 0xc9c
+  __AUTH.__objc_data: 0x3b8
+  __DATA.__objc_ivar: 0xc70
   __DATA.__data: 0x1f8
-  __DATA.__common: 0x11e0
+  __DATA.__common: 0x11d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0xa0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4613
-  Symbols:   5938
-  CStrings:  8304
+  Functions: 4581
+  Symbols:   5900
+  CStrings:  8229
 
Symbols:
- _os_transaction_get_description
- _OBJC_METACLASS_$_WAActivityManager
- __dispatch_main_q
- _OBJC_CLASS_$_NSTimer
- _OBJC_CLASS_$_WAActivityManager
- _xpc_transaction_try_exit_clean
CStrings:
- "%!{(MISSING)public}s::%!d(MISSING):Found preference value in domain: %!@(MISSING) key: %!@(MISSING)"
- "setAlternateExecutionBlockForCleanExit:"
- "%!{(MISSING)public}s::%!d(MISSING):Found preference value in domain: %!@(MISSING) key: %!@(MISSING) value: %!d(MISSING)"
- "T@\"NSDate\",&,V_dateFirstTransaction"
- "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager is b520, setting isEagerExitEnabled"
- "osTransactionsActive"
- "%!{(MISSING)public}s::%!d(MISSING):configuring _periodicActiveListTimer"
- "-[WAActivityManager debugTimer]_block_invoke_3"
- "WAActivityManager"
- "_dateFirstTransaction"
- "-[WAActivityManager osTransactionCreate:transaction:]_block_invoke"
- "debugTimerEnabled"
- "v16@?0@\"NSTimer\"8"
- "%!{(MISSING)public}s::%!d(MISSING):configured _periodicActiveListTimer"
- "osTransactionCreate:transaction:"
- "isValid"
- "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete TRANSACTION NOT FOUND ASSERT"
- "-[WAActivityManager debugTimerEnabled]"
- "@\"NSDate\""
- "isEagerExitEnabled"
- "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, extending running eager exit timer to %!f(MISSING) seconds"
- "osTransactionComplete:"
- "eager-exit-enable"
- "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager is not b520, no isEagerExitEnabled"
- "eager-exit-timeout"
- "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager debugTimer already setup"
- "\x02\x11\x13\x11"
- "%!{(MISSING)public}s::%!d(MISSING):osTransactionCreate, timer was running, invalidating and freeing"
- "alternateExecutionBlockForCleanExit"
- "dateFirstTransaction"
- "_transactionsStarted"
- "@\"NSTimer\""
- "-[WAActivityManager osTransactionComplete:]"
- "%!{(MISSING)public}s::%!d(MISSING):Completed %!l(MISSING)u transactions within uptime of %!f(MISSING) seconds"
- "setTransactionsCompleted:"
- "setExecuteBeforePossibleEagerExit:"
- "_eagerExitTimeout"
- "eager-exit-debug"
- "v32@0:8r*16@24"
- "T@?,C,N,V_executeBeforePossibleEagerExit"
- "%!{(MISSING)public}s::%!d(MISSING):Cannot eager exit, still outstanding transactions"
- "debugTimer"
- "setDateFirstTransaction:"
- "_transactionsCompleted"
- "_executeBeforePossibleEagerExit"
- "TQ,V_transactionsCompleted"
- "%!{(MISSING)public}s::%!d(MISSING):Attempting Daemon Eager Exit due to inactivity timeout of %!f(MISSING) seconds"
- "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, configuring eager exit timer in %!f(MISSING) seconds"
- "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete %!s(MISSING)"
- "_alternateExecutionBlockForCleanExit"
- "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete %!s(MISSING), TRANSACTION NOT FOUND, active count before completing %!l(MISSING)u"
- "%!{(MISSING)public}s::%!d(MISSING):osTransactionCreate %!s(MISSING), active count is now %!l(MISSING)u, total started is now %!l(MISSING)u"
- "executeBeforePossibleEagerExit"
- "-[WAActivityManager debugTimer]_block_invoke"
- "now"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "TQ,V_transactionsStarted"
- "-[WAActivityManager debugTimer]"
- "waitingToInitDebugTimer"
- "setTransactionsStarted:"
- "%!{(MISSING)public}s::%!d(MISSING):activeTransactions %!l(MISSING)u"
- "transactionsCompleted"
- "transactionsStarted"
- "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager init error!"
- "-[WAActivityManager init]"
- "_periodicActiveListTimer"
- "sharedActivityManager"
- "%!{(MISSING)public}s::%!d(MISSING):activeTransaction %!s(MISSING)"
- "T@?,C,N,V_alternateExecutionBlockForCleanExit"
- "_executeTimerBlock"
- "-[WAActivityManager osTransactionComplete:]_block_invoke_2"
- "_active_transactions"
- "-[WAActivityManager osTransactionComplete:]_block_invoke"
- "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, eager exit timer disabled via defaults write"

```
