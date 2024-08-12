## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-605.80.0.0.0
-  __TEXT.__text: 0x83158
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x8160
-  __TEXT.__objc_methlist: 0x2d70
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x127cc
-  __TEXT.__gcc_except_tab: 0x4cfc
-  __TEXT.__objc_methname: 0xc87d
-  __TEXT.__oslogstring: 0x1215c
-  __TEXT.__objc_classname: 0x33b
-  __TEXT.__objc_methtype: 0x1097
+605.84.0.0.0
+  __TEXT.__text: 0x85f08
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_stubs: 0x8400
+  __TEXT.__objc_methlist: 0x2f10
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x12cbd
+  __TEXT.__gcc_except_tab: 0x4d80
+  __TEXT.__objc_methname: 0xcea5
+  __TEXT.__oslogstring: 0x126ff
+  __TEXT.__objc_classname: 0x353
+  __TEXT.__objc_methtype: 0x10d0
   __TEXT.__dlopen_cstrs: 0x17a
-  __TEXT.__unwind_info: 0xd38
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x1198
-  __DATA_CONST.__cfstring: 0xfca0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0xda0
+  __DATA_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x12a0
+  __DATA_CONST.__cfstring: 0xfd60
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x1360
   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x4fb8
-  __DATA.__objc_selrefs: 0x2a48
-  __DATA.__objc_ivar: 0x4a4
-  __DATA.__objc_data: 0x730
+  __DATA.__objc_const: 0x52d8
+  __DATA.__objc_selrefs: 0x2b48
+  __DATA.__objc_ivar: 0x4e0
+  __DATA.__objc_data: 0x780
   __DATA.__data: 0x488
-  __DATA.__common: 0x40
-  __DATA.__bss: 0x178
+  __DATA.__common: 0x50
+  __DATA.__bss: 0x188
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1211
-  Symbols:   372
-  CStrings:  5798
+  Functions: 1257
+  Symbols:   377
+  CStrings:  5908
 
Symbols:
+ _MGGetProductType
+ _OBJC_CLASS_$_NSTimer
+ _objc_sync_enter
+ _objc_sync_exit
+ _xpc_transaction_try_exit_clean
CStrings:
+ "\x01\x11_\x01#\xf0\xaf\x06-\""
+ "\x02\x11\x13\x11"
+ "\"WiFiAnalytics_executables-605.84\""
+ "%!{(MISSING)public}s::%!d(MISSING):Attempting Daemon Eager Exit due to inactivity timeout of %!f(MISSING) seconds"
+ "%!{(MISSING)public}s::%!d(MISSING):Cannot eager exit, still outstanding transactions"
+ "%!{(MISSING)public}s::%!d(MISSING):Completed %!l(MISSING)u transactions within uptime of %!f(MISSING) seconds"
+ "%!{(MISSING)public}s::%!d(MISSING):Found preference value in domain: %!@(MISSING) key: %!@(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):Found preference value in domain: %!@(MISSING) key: %!@(MISSING) value: %!d(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager debugTimer already setup"
+ "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager init error!"
+ "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager is b520, setting isEagerExitEnabled"
+ "%!{(MISSING)public}s::%!d(MISSING):WAActivityManager is not b520, no isEagerExitEnabled"
+ "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, configuring eager exit timer in %!f(MISSING) seconds"
+ "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, eager exit timer disabled via defaults write"
+ "%!{(MISSING)public}s::%!d(MISSING):_active_transactions empty, extending running eager exit timer to %!f(MISSING) seconds"
+ "%!{(MISSING)public}s::%!d(MISSING):activeTransaction %!s(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):activeTransactions %!l(MISSING)u"
+ "%!{(MISSING)public}s::%!d(MISSING):configured _periodicActiveListTimer"
+ "%!{(MISSING)public}s::%!d(MISSING):configuring _periodicActiveListTimer"
+ "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete %!s(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete %!s(MISSING), TRANSACTION NOT FOUND, active count before completing %!l(MISSING)u"
+ "%!{(MISSING)public}s::%!d(MISSING):osTransactionComplete TRANSACTION NOT FOUND ASSERT"
+ "%!{(MISSING)public}s::%!d(MISSING):osTransactionCreate %!s(MISSING), active count is now %!l(MISSING)u, total started is now %!l(MISSING)u"
+ "%!{(MISSING)public}s::%!d(MISSING):osTransactionCreate, timer was running, invalidating and freeing"
+ "%!{(MISSING)public}s::%!d(MISSING):prepareToTerminate..."
+ "-[WAActivityManager debugTimerEnabled]"
+ "-[WAActivityManager debugTimer]"
+ "-[WAActivityManager debugTimer]_block_invoke"
+ "-[WAActivityManager debugTimer]_block_invoke_3"
+ "-[WAActivityManager init]"
+ "-[WAActivityManager osTransactionComplete:]"
+ "-[WAActivityManager osTransactionComplete:]_block_invoke"
+ "-[WAActivityManager osTransactionComplete:]_block_invoke_2"
+ "-[WAActivityManager osTransactionCreate:transaction:]_block_invoke"
+ "-[WAEngine _prepareToTerminateViaEagerExit]"
+ "-[WAEngine prepareToTerminateViaEagerExit]_block_invoke"
+ "-[WAEngine xpcConnection:clearMessageStoreAndReply:]_block_invoke"
+ "-[WAEngine xpcConnection:killDaemonAndReply:]_block_invoke"
+ "-[WAEngine xpcConnection:lqmCrashTracerNotifyForInterfaceWithName:andReply:]_block_invoke"
+ "-[WAEngine xpcConnection:lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:]_block_invoke"
+ "-[WAEngine xpcConnection:sendMemoryPressureRequestAndReply:]_block_invoke"
+ "-[WAEngine xpcConnection:trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:]_block_invoke"
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSTimer\""
+ "Activity"
+ "Aug  6 2024 09:07:28"
+ "D"
+ "T@\"NSDate\",&,V_dateFirstTransaction"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_dnsStudyTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_dpsStudyTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_megaProfileInstalledTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_slowwifiStudyTransaction"
+ "T@?,C,N,V_alternateExecutionBlockForCleanExit"
+ "T@?,C,N,V_executeBeforePossibleEagerExit"
+ "TQ,V_transactionsCompleted"
+ "TQ,V_transactionsStarted"
+ "Terminations - Try Eager Exit"
+ "WAActivityManager"
+ "WAActivityManager"
+ "WiFiAnalytics_executables-605.84"
+ "_active_transactions"
+ "_alternateExecutionBlockForCleanExit"
+ "_dateFirstTransaction"
+ "_dnsStudyTransaction"
+ "_dpsStudyTransaction"
+ "_eagerExitTimeout"
+ "_executeBeforePossibleEagerExit"
+ "_executeTimerBlock"
+ "_megaProfileInstalledTransaction"
+ "_periodicActiveListTimer"
+ "_prepareToTerminateViaEagerExit"
+ "_slowwifiStudyTransaction"
+ "_transactionsCompleted"
+ "_transactionsStarted"
+ "alternateExecutionBlockForCleanExit"
+ "com.apple.wifianalytics.DatapathMetricStream"
+ "com.apple.wifianalytics.dnsStudyTransaction"
+ "com.apple.wifianalytics.dpsStudyTransaction"
+ "com.apple.wifianalytics.migratestore"
+ "com.apple.wifianalytics.pid_%!d(MISSING).%!s(MISSING)"
+ "com.apple.wifianalytics.slowwifiStudyTransaction"
+ "com.apple.wifianalytics.triggerPeerDiagnosticsStudy"
+ "dateFirstTransaction"
+ "debugTimer"
+ "debugTimerEnabled"
+ "dnsStudyTransaction"
+ "dpsStudyTransaction"
+ "eager-exit-debug"
+ "eager-exit-enable"
+ "eager-exit-timeout"
+ "engine_TerminationTryEagerExit"
+ "executeBeforePossibleEagerExit"
+ "invalidate"
+ "isEagerExitEnabled"
+ "isValid"
+ "megaProfileInstalledTransaction"
+ "osTransactionComplete:"
+ "osTransactionCreate:transaction:"
+ "osTransactionsActive"
+ "prepareToTerminateViaEagerExit"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setAlternateExecutionBlockForCleanExit:"
+ "setDateFirstTransaction:"
+ "setDnsStudyTransaction:"
+ "setDpsStudyTransaction:"
+ "setExecuteBeforePossibleEagerExit:"
+ "setMegaProfileInstalledTransaction:"
+ "setSlowwifiStudyTransaction:"
+ "setTransactionsCompleted:"
+ "setTransactionsStarted:"
+ "sharedActivityManager"
+ "slowwifiStudyTransaction"
+ "transactionsCompleted"
+ "transactionsStarted"
+ "v16@?0@\"NSTimer\"8"
+ "v32@0:8r*16@24"
+ "waitingToInitDebugTimer"
- "\x01\x11_\x01\xf0\xcf\x06-\""
- "\"WiFiAnalytics_executables-605.80\""
- "-[WAEngine xpcConnection:issueIOReportManagementCommand:andReply:]_block_invoke_2"
- "Jul 22 2024 17:04:32"
- "WiFiAnalytics_executables-605.80"
- "com.apple.wifianalytics.triggerDatapathDiagnosticsAndCollectUpdates"
- "com.apple.wifianalytics.triggerQueryForNWActivity"

```
