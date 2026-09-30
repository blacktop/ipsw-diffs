## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-448.125.5.1.0
-  __TEXT.__text: 0x8d554
-  __TEXT.__objc_methlist: 0x5774
+448.125.5.2.0
+  __TEXT.__text: 0x8de40
+  __TEXT.__objc_methlist: 0x57ec
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x1503e
-  __TEXT.__cstring: 0xe5b5
+  __TEXT.__oslogstring: 0x1511e
+  __TEXT.__cstring: 0xe685
   __TEXT.__gcc_except_tab: 0xb68
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x2eb8
+  __TEXT.__unwind_info: 0x2ef0
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2608
-  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39b8
+  __DATA_CONST.__objc_selrefs: 0x3a00
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x1128
+  __DATA_CONST.__got: 0x1130
   __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x98a0
-  __AUTH_CONST.__objc_const: 0x100f0
+  __AUTH_CONST.__cfstring: 0x9940
+  __AUTH_CONST.__objc_const: 0x10260
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x968
-  __AUTH.__objc_data: 0x120
-  __DATA.__objc_ivar: 0x3b8
+  __AUTH.__objc_data: 0x170
+  __DATA.__objc_ivar: 0x3d0
   __DATA.__data: 0x1220
   __DATA_DIRTY.__objc_data: 0x19b0
   __DATA_DIRTY.__data: 0x200

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3196
-  Symbols:   5858
-  CStrings:  2855
+  Functions: 3209
+  Symbols:   5893
+  CStrings:  2862
 
Symbols:
+ -[CDPDAsyncSecureBackupEnableTracker .cxx_destruct]
+ -[CDPDAsyncSecureBackupEnableTracker _recordOutcomeWithReason:]
+ -[CDPDAsyncSecureBackupEnableTracker _timeOutCurrentWaiter]
+ -[CDPDAsyncSecureBackupEnableTracker awaitSettleWithTimeout:completionHandler:]
+ -[CDPDAsyncSecureBackupEnableTracker enableStarted]
+ -[CDPDAsyncSecureBackupEnableTracker recordDidEnable:error:]
+ -[CDPDAsyncSecureBackupEnableTracker recordEnableStarted]
+ -[CDPDStateMachine _afterAsyncSecureBackupEnableSettles:]
+ -[CDPDStateMachine initWithContext:uiProvider:asyncSecureBackupEnableTracker:]
+ GCC_except_table121
+ GCC_except_table35
+ _CDPDAsyncSecureBackupEnableTrackerErrorDomain
+ _OBJC_CLASS_$_CDPDAsyncSecureBackupEnableTracker
+ _OBJC_IVAR_$_CDPDAsyncSecureBackupEnableTracker._didRecordOutcome
+ _OBJC_IVAR_$_CDPDAsyncSecureBackupEnableTracker._enableStarted
+ _OBJC_IVAR_$_CDPDAsyncSecureBackupEnableTracker._lock
+ _OBJC_IVAR_$_CDPDAsyncSecureBackupEnableTracker._outcomeReason
+ _OBJC_IVAR_$_CDPDAsyncSecureBackupEnableTracker._waiter
+ _OBJC_IVAR_$_CDPDStateMachine._asyncSecureBackupEnableTracker
+ _OBJC_METACLASS_$_CDPDAsyncSecureBackupEnableTracker
+ __OBJC_$_INSTANCE_METHODS_CDPDAsyncSecureBackupEnableTracker
+ __OBJC_$_INSTANCE_VARIABLES_CDPDAsyncSecureBackupEnableTracker
+ __OBJC_$_PROP_LIST_CDPDAsyncSecureBackupEnableTracker
+ __OBJC_CLASS_RO_$_CDPDAsyncSecureBackupEnableTracker
+ __OBJC_METACLASS_RO_$_CDPDAsyncSecureBackupEnableTracker
+ ___54-[CDPDStateMachine _attemptPDPFallbackWithCompletion:]_block_invoke_2
+ ___57-[CDPDStateMachine _afterAsyncSecureBackupEnableSettles:]_block_invoke
+ ___79-[CDPDAsyncSecureBackupEnableTracker awaitSettleWithTimeout:completionHandler:]_block_invoke
+ _objc_msgSend$_afterAsyncSecureBackupEnableSettles:
+ _objc_msgSend$_recordOutcomeWithReason:
+ _objc_msgSend$_timeOutCurrentWaiter
+ _objc_msgSend$awaitSettleWithTimeout:completionHandler:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$enableStarted
+ _objc_msgSend$initWithContext:uiProvider:asyncSecureBackupEnableTracker:
+ _objc_msgSend$recordDidEnable:error:
+ _objc_msgSend$recordEnableStarted
- GCC_except_table120
- GCC_except_table34
CStrings:
+ "CDPDAsyncSecureBackupEnableTracker"
+ "CDPDStateMachine: asynchronous secure-backup enable did not deliver, skipping post-Octagon PDP setup: %@"
+ "CDPDStateMachine: waiting up to %@s for asynchronous secure-backup enable to settle before post-Octagon PDP setup"
+ "DBRAsyncEnableSettleTimeout"
+ "com.apple.corecdp.pdpRecordGenerationAhead"
+ "com.apple.corecdp.pdpRecordGenerationCheckSkipped"
+ "com.apple.corecdp.pdpWrappingKeyRepair"
```
