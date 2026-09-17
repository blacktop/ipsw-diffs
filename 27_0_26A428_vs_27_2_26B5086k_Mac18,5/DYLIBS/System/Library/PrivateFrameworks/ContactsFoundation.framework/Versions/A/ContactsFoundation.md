## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation`

```diff

-1427.100.1.0.0
-  __TEXT.__text: 0x9acc4
-  __TEXT.__objc_methlist: 0xa95c
-  __TEXT.__cstring: 0x6e14
+1430.200.21.0.0
+  __TEXT.__text: 0x9bbc0
+  __TEXT.__objc_methlist: 0xaa1c
+  __TEXT.__cstring: 0x6e34
   __TEXT.__const: 0x1380
-  __TEXT.__oslogstring: 0x2298
+  __TEXT.__oslogstring: 0x2378
   __TEXT.__gcc_except_tab: 0x1240
-  __TEXT.__ustring: 0x2e2
+  __TEXT.__ustring: 0x514
   __TEXT.__dlopen_cstrs: 0xb5
   __TEXT.__swift5_typeref: 0x84a
   __TEXT.__constg_swiftt: 0x7e8

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x388
+  __TEXT.__swift5_capture: 0x398
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x48b8
+  __TEXT.__unwind_info: 0x4908
   __TEXT.__eh_frame: 0xa30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__const: 0x11d0
   __DATA_CONST.__objc_classlist: 0xac0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a98
+  __DATA_CONST.__objc_selrefs: 0x4aa0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x9c88
   __DATA_CONST.__got: 0xec8
-  __AUTH_CONST.__const: 0x5ed8
-  __AUTH_CONST.__cfstring: 0xace0
-  __AUTH_CONST.__objc_const: 0x16318
+  __AUTH_CONST.__const: 0x5f80
+  __AUTH_CONST.__cfstring: 0xad20
+  __AUTH_CONST.__objc_const: 0x16320
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x1068
+  __AUTH_CONST.__auth_got: 0x1070
   __AUTH.__objc_data: 0x3ec0
   __AUTH.__data: 0x4b0
   __DATA.__objc_ivar: 0x7bc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5222
-  Symbols:   10359
-  CStrings:  1857
+  Functions: 5254
+  Symbols:   10389
+  CStrings:  1860
 
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
+ __36-[CNProcessSharedLock openLockFile:]_block_invoke
+ __77-[_CNQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ __78-[_CNInlineScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ __85-[_CNOffMainThreadScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ __89-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ __93-[CNTimeProfilingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___77-[_CNQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___78-[CNVirtualScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___78-[_CNInlineScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___85-[_CNOffMainThreadScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___86-[_CNOperationQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___87-[_CNJumpToMainQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___88-[_CNSynchronousQueueScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___89-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___90-[CNCoalescingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___90-[CNInhibitingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___91-[CNSuspendableSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___91-[CNSuspendableSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke_2
+ ___93-[CNBlockCountingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___93-[CNTimeProfilingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___98-[CNCallStackRecordingSchedulerDecorator afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___block_descriptor_44_e8_32s_e14_"NSError"8?0l
+ ___block_descriptor_80_e8_32s40s48s56r64r72w_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56r64r72w
+ ___destroy_helper_block_e8_32s40s48s56r64r72w
+ _objc_msgSend$afterDelay:performBlock:delayTolerance:qualityOfService:
+ _strerror
- __62-[_CNQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- __63-[_CNInlineScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- __74-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___62-[_CNQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___63-[CNVirtualScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___63-[_CNInlineScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___71-[_CNOperationQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___72-[_CNJumpToMainQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___73-[_CNSynchronousQueueScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___74-[_CNJumpToMainRunLoopScheduler afterDelay:performBlock:qualityOfService:]_block_invoke
- ___76-[CNSuspendableSchedulerDecorator afterDelay:performBlock:qualityOfService:]_block_invoke
- ___76-[CNSuspendableSchedulerDecorator afterDelay:performBlock:qualityOfService:]_block_invoke_2
- ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64r72w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64r72w
- ___destroy_helper_block_e8_32s40s48s56s64r72w
CStrings:
+ "CNProcessSharedLockSandboxHint"
+ "Failed to open shared lock file %{public}@ (errno=%d %{public}s). This is usually a client sandbox denial — the process's sandbox profile must grant the AddressBook locks directory (import contacts.sb). See rdar://147462310."
+ "The lock file could not be opened because of a permission denial (EPERM/EACCES). This is usually a client sandbox denial — the process's sandbox profile must grant the AddressBook locks directory (.AddressBookLocks), typically by importing contacts.sb and calling contacts-client."
```
