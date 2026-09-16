## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`

```diff

-1427.100.1.0.0
-  __TEXT.__text: 0x95bcc
-  __TEXT.__objc_methlist: 0xab5c
-  __TEXT.__cstring: 0x7224
+1430.200.21.0.0
+  __TEXT.__text: 0x9675c
+  __TEXT.__objc_methlist: 0xac0c
+  __TEXT.__cstring: 0x7214
   __TEXT.__const: 0x1370
-  __TEXT.__oslogstring: 0x2818
-  __TEXT.__gcc_except_tab: 0x123c
-  __TEXT.__ustring: 0x2e2
-  __TEXT.__dlopen_cstrs: 0x167
+  __TEXT.__oslogstring: 0x28f8
+  __TEXT.__gcc_except_tab: 0x122c
+  __TEXT.__ustring: 0x514
+  __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__swift5_typeref: 0x84a
   __TEXT.__constg_swiftt: 0x7e8
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x388
+  __TEXT.__swift5_capture: 0x398
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4920
+  __TEXT.__unwind_info: 0x4960
   __TEXT.__eh_frame: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38c0
+  __DATA_CONST.__const: 0x38d8
   __DATA_CONST.__objc_classlist: 0xac0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x200

   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x9c90
   __DATA_CONST.__got: 0xed0
-  __AUTH_CONST.__const: 0x3328
-  __AUTH_CONST.__cfstring: 0xaf20
-  __AUTH_CONST.__objc_const: 0x16620
+  __AUTH_CONST.__const: 0x33a0
+  __AUTH_CONST.__cfstring: 0xaf60
+  __AUTH_CONST.__objc_const: 0x16628
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x11f0
+  __AUTH_CONST.__auth_got: 0x11f8
   __AUTH.__objc_data: 0x4190
   __AUTH.__data: 0x4c8
   __DATA.__objc_ivar: 0x7fc

   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2e68
   __DATA_DIRTY.__data: 0x2f8
-  __DATA_DIRTY.__bss: 0x5f8
+  __DATA_DIRTY.__bss: 0x5f0
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5236
-  Symbols:   10485
+  Functions: 5265
+  Symbols:   10506
   CStrings:  1913
 
Symbols:
+ -[CNBlockCountingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNCallStackRecordingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNCoalescingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNInhibitingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNQualityOfServiceSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNSuspendableSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNTimeProfilingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNVirtualScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNImmediateScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNInlineScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNJumpToMainQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNMainThreadScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNOffMainThreadScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNOperationQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[_CNSynchronousQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ _CNProcessSharedLockSandboxHintKey
+ ___36-[CNProcessSharedLock openLockFile:]_block_invoke_2
+ ___77-[_CNQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___77-[_CNQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke_2
+ ___78-[CNVirtualScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___78-[_CNInlineScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___78-[_CNInlineScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke_2
+ ___85-[_CNOffMainThreadScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___86-[_CNOperationQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___87-[_CNJumpToMainQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___88-[_CNSynchronousQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___89-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___89-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke_2
+ ___90-[CNCoalescingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___90-[CNInhibitingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___91-[CNSuspendableSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___91-[CNSuspendableSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke_2
+ ___93-[CNBlockCountingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___93-[CNTimeProfilingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___98-[CNCallStackRecordingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___block_descriptor_44_e8_32s_e14_"NSError"8?0ls32l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72w_e5_v8?0lw72l8s32l8r56l8r64l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80w_e5_v8?0ls32l8w80l8s40l8r64l8r72l8s48l8s56l8
+ _objc_msgSend$afterDelay:performBlock:delayTolerance:qualityOfService:
+ _strerror
- -[CNFeatureFlags isUIKitEnhancedLandscapeEnabled]
- _UIKitCoreLibraryCore.frameworkLibrary
- ___62-[_CNQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___62-[_CNQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke_2
- ___63-[CNVirtualScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___63-[_CNInlineScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___63-[_CNInlineScheduler afterDelay:performBlock:qualityOfService:]_block_invoke_2
- ___71-[_CNOperationQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___72-[_CNJumpToMainQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___73-[_CNSynchronousQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___74-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___74-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:qualityOfService:]_block_invoke_2
- ___76-[CNSuspendableSchedulerDecorator afterDelay:performBlock:qualityOfService:]_block_invoke
- ___76-[CNSuspendableSchedulerDecorator afterDelay:performBlock:qualityOfService:]_block_invoke_2
- ___UIKitCoreLibraryCore_block_invoke
- ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0lw64l8s32l8r56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64r72w_e5_v8?0ls32l8w72l8s40l8r64l8s48l8s56l8
- ___get_UIEnhancedLandscapeEnabledSymbolLoc_block_invoke
- _audit_stringUIKitCore
- _get_UIEnhancedLandscapeEnabledSymbolLoc.ptr
- _objc_msgSend$isUIKitEnhancedLandscapeEnabled
CStrings:
+ "CNProcessSharedLockSandboxHint"
+ "Failed to open shared lock file %{public}@ (errno=%d %{public}s). This is usually a client sandbox denial — the process's sandbox profile must grant the AddressBook locks directory (import contacts.sb). See rdar://147462310."
+ "The lock file could not be opened because of a permission denial (EPERM/EACCES). This is usually a client sandbox denial — the process's sandbox profile must grant the AddressBook locks directory (.AddressBookLocks), typically by importing contacts.sb and calling contacts-client."
- "_UIEnhancedLandscapeEnabled"
- "enhanced_landscape_contacts"
- "softlink:r:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"
```
