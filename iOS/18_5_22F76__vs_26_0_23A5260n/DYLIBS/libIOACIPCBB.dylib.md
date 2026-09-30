## libIOACIPCBB.dylib

> `/usr/lib/libIOACIPCBB.dylib`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x1c40
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__const: 0x4f
-  __TEXT.__cstring: 0x56
-  __TEXT.__oslogstring: 0x2e5
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x28
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x178
+274.0.0.0.0
+  __TEXT.__text: 0x2714
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__const: 0x57
+  __TEXT.__cstring: 0x176
+  __TEXT.__oslogstring: 0x5e0
+  __TEXT.__unwind_info: 0x120
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x48
+  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libIOACIPC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4425E6BE-A3A8-3F81-BA9F-0F07A981D4BB
-  Functions: 40
-  Symbols:   127
-  CStrings:  24
+  UUID: AE596210-D9E0-3EB6-B700-A457081FD4A4
+  Functions: 54
+  Symbols:   167
+  CStrings:  48
 
Symbols:
+ GCC_except_table4
+ GCC_except_table6
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOServiceAddInterestNotification
+ _IOServiceGetState
+ __NSConcreteGlobalBlock
+ __ZN20IOACIPCBBNetCfgClass11testOffloadEh
+ __ZN20IOACIPCBBNetCfgClass13getFilterRuleEjP36AppleCellularDataPlaneFilterRuleInfo
+ __ZN20IOACIPCBBNetCfgClass18completeFilterRuleEj
+ __ZN20IOACIPCBBNetCfgClass19setNotificationPortEv
+ __ZN20IOACIPCBBNetCfgClass19setNotificationPortEv.cold.1
+ __ZN20IOACIPCBBNetCfgClass21clearNotificationPortEv
+ __ZN20IOACIPCBBNetCfgClass26cancelFilterRuleCompletionEj
+ __ZN20IOACIPCBBNetCfgClass26registerFilterRuleCallBackEU13block_pointerFvP36AppleCellularDataPlaneFilterRuleInfoE
+ __ZN20IOACIPCBBNetCfgClass28unregisterFilterRuleCallBackEv
+ __ZN20IOACIPCBBNetCfgClass34AppleCellularDataPlaneNotificationEPvjjS0_
+ __ZN20IOACIPCBBNetCfgClass5startEPK14__CFDictionaryt.cold.1
+ __ZN20IOACIPCBBNetCfgClass5startEPK14__CFDictionaryt.cold.2
+ __ZN20IOACIPCBBNetCfgClass6isOpenEv
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZTISt13runtime_error
+ ____ZN20IOACIPCBBNetCfgClassD2Ev_block_invoke
+ ___assert_rtn
+ ___block_literal_global
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_sync
+ _pthread_mutexattr_init
+ _pthread_mutexattr_settype
- GCC_except_table2
CStrings:
+ "!fNotificationObject"
+ "AppleCellularDataPlaneNotification"
+ "IOACIPCBBNetCfgClass"
+ "IOACIPCBBNetCfgClass.cpp"
+ "IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane Notification received: 0x%x\n"
+ "IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane Offloading Request Received, rule-id: %u\n"
+ "IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane terminated\n"
+ "IOACIPCBBNetCfgClass::%s: Cancelling FilterRule Completion (rule-id = %u)\n"
+ "IOACIPCBBNetCfgClass::%s: Completing FilterRule (rule-id = %u)\n"
+ "IOACIPCBBNetCfgClass::%s: ERROR: AppleCellularDataPlane Offloading Request has no Data, rule-id: %u, result: 0x%x\n"
+ "IOACIPCBBNetCfgClass::%s: Requesting FilterRule data (rule-id = %u)\n"
+ "IOACIPCBBNetCfgClass::%s: Requesting FilterRule data failed (0x%x)\n"
+ "IOACIPCBBNetCfgClass::%s: Retrieving Filter Rule Data, rule-id: %u\n"
+ "IOACIPCBBNetCfgClass::%s: Testing Offload FilterRule (interface-id = %u)\n"
+ "IOGeneralInterest"
+ "Unable to allocate DispatchQueue"
+ "cancelFilterRuleCompletion"
+ "completeFilterRule"
+ "fNotificationPort"
+ "getFilterRule"
+ "kr == KERN_SUCCESS"
+ "setNotificationPort"
+ "testOffload"
+ "v8@?0"

```
