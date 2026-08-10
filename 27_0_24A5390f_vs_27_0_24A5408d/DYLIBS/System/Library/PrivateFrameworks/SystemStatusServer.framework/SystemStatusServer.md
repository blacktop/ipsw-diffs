## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-284.1.0.0.0
-  __TEXT.__text: 0x20774
-  __TEXT.__objc_methlist: 0x1e98
-  __TEXT.__const: 0xd8
+286.101.0.0.0
+  __TEXT.__text: 0x21038
+  __TEXT.__objc_methlist: 0x1ef8
+  __TEXT.__const: 0xe0
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__cstring: 0x1d3b
-  __TEXT.__gcc_except_tab: 0x33c
-  __TEXT.__oslogstring: 0xe55
-  __TEXT.__unwind_info: 0x8a0
+  __TEXT.__cstring: 0x1dd5
+  __TEXT.__gcc_except_tab: 0x35c
+  __TEXT.__oslogstring: 0x1001
+  __TEXT.__unwind_info: 0x8c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1418
+  __DATA_CONST.__objc_selrefs: 0x1490
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__got: 0x438
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x44f8
+  __DATA_CONST.__got: 0x450
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x1840
+  __AUTH_CONST.__objc_const: 0x4528
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_ivar: 0x2cc
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 766
-  Symbols:   2230
-  CStrings:  303
+  Functions: 777
+  Symbols:   2261
+  CStrings:  314
 
Symbols:
+ +[STStatusDomainXPCClientWakeUpAssertion _watchdogQueue]
+ -[STStatusDomainXPCClientWakeUpAssertion _cancelWatchdogTimer]
+ -[STStatusDomainXPCClientWakeUpAssertion _startNewWatchdogTimer]
+ -[STStatusDomainXPCClientWakeUpAssertion _terminateClient]
+ -[STStatusDomainXPCClientWakeUpAssertion _watchdogQueue_cancelWatchdogTimer]
+ -[STStatusDomainXPCClientWakeUpAssertion setWatchdogTimer:]
+ -[STStatusDomainXPCClientWakeUpAssertion watchdogTimer]
+ GCC_except_table12
+ _BSStringFromBOOL
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSTerminateContext
+ _OBJC_CLASS_$_RBSTerminateRequest
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._watchdogTimer
+ __OBJC_$_CLASS_METHODS_STStatusDomainXPCClientWakeUpAssertion
+ ___56+[STStatusDomainXPCClientWakeUpAssertion _watchdogQueue]_block_invoke
+ ___62-[STStatusDomainXPCClientWakeUpAssertion _cancelWatchdogTimer]_block_invoke
+ ___64-[STStatusDomainXPCClientWakeUpAssertion _startNewWatchdogTimer]_block_invoke
+ _objc_msgSend$_cancelWatchdogTimer
+ _objc_msgSend$_startNewWatchdogTimer
+ _objc_msgSend$_terminateClient
+ _objc_msgSend$_watchdogQueue
+ _objc_msgSend$_watchdogQueue_cancelWatchdogTimer
+ _objc_msgSend$execute:
+ _objc_msgSend$initWithExplanation:
+ _objc_msgSend$initWithPredicate:context:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$predicateMatching:
+ _objc_msgSend$setExceptionCode:
+ _objc_msgSend$setMaximumTerminationResistance:
+ _objc_msgSend$setReportType:
+ _objc_msgSend$setWatchdogTimer:
CStrings:
+ "STStatusDomainXPCClientWakeUpAssertion-Watchdog:%d"
+ "SystemStatus observer watchdog - unresponsive client: %d"
+ "cancelling watchdog timer for client: %d"
+ "com.apple.systemstatus.observer.watchdogqueue"
+ "initialized wake up assertion for client: %d - RunningBoard managed: %@"
+ "invalidating wake up assertion for client: %d"
+ "starting new watchdog timer for client: %d"
+ "wake up assertion failed to create process handle for client: %d"
+ "wake up assertion failed to create process handle for client: %d - error: %@"
+ "watchdog failed to terminate client: %d - error: %@"
+ "watchdog terminating client: %d"
```
