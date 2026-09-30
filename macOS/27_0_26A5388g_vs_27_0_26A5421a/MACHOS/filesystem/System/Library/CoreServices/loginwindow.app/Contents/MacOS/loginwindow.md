## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3106.100.0.0.0
-  __TEXT.__text: 0xca464
+3109.0.0.0.0
+  __TEXT.__text: 0xca7d4
   __TEXT.__auth_stubs: 0x2ce0
-  __TEXT.__objc_stubs: 0xfee0
-  __TEXT.__objc_methlist: 0x6b34
+  __TEXT.__objc_stubs: 0xff60
+  __TEXT.__objc_methlist: 0x6b64
   __TEXT.__const: 0x2e8
   __TEXT.__gcc_except_tab: 0x1064
-  __TEXT.__objc_methname: 0x12268
-  __TEXT.__oslogstring: 0x299bc
-  __TEXT.__cstring: 0x12ba8
+  __TEXT.__objc_methname: 0x1232d
+  __TEXT.__oslogstring: 0x29a9c
+  __TEXT.__cstring: 0x12c88
   __TEXT.__objc_classname: 0x87a
   __TEXT.__objc_methtype: 0x21af
   __TEXT.__ustring: 0x1c

   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0x53
-  __TEXT.__unwind_info: 0x1df8
-  __DATA_CONST.__const: 0x21d8
+  __TEXT.__unwind_info: 0x1de8
+  __DATA_CONST.__const: 0x2188
   __DATA_CONST.__cfstring: 0x6e60
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__auth_got: 0x1680
   __DATA_CONST.__got: 0xac8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x8d08
-  __DATA.__objc_selrefs: 0x4ef0
-  __DATA.__objc_ivar: 0x860
+  __DATA.__objc_const: 0x8d58
+  __DATA.__objc_selrefs: 0x4f18
+  __DATA.__objc_ivar: 0x868
   __DATA.__objc_data: 0x1a70
   __DATA.__data: 0x990
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x88
-  __DATA.__bss: 0x6c8
+  __DATA.__bss: 0x6d8
   __CGPreLoginApp.__cgpreloginapp: 0x0
   __RESTRICT.__restrict: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2608
+  Functions: 2613
   Symbols:   1065
-  CStrings:  9040
+  CStrings:  9051
 
Symbols:
+ _DASessionKeepAlive
+ _DASessionSetDispatchQueue
- _DAApprovalSessionScheduleWithRunLoop
- _DAApprovalSessionUnscheduleFromRunLoop
CStrings:
+ "%s | \t notifying delegate that screen lock UI finished closing"
+ "%s | \t teardown still in flight, leaving screenLockUIDidFinishClosing to it"
+ "%s |      Clearing _unlockInProgress (result = %ld, mode = %ld, awaitingUITeardown = %d)"
+ "%s |      Deferring _unlockInProgress clear until UI teardown completes (result = %ld, mode = %ld)"
+ "%s |      DisableScreenLockDiskPolicy "
+ "%s |      Do not EnableScreenLockDiskPolicy lock delay = INT_MAX"
+ "%s |      EnableScreenLockDiskPolicy to block disk mounts during screen lock"
+ "%s |      superseded teardown completed late, not notifying delegate"
+ "%s | DiskArb - screen locked; blocking removable disk mounts"
+ "%s | DiskArb - screen unlocked; allowing removable disk mounts"
+ "%s | DiskArb - screen-lock mount-approval session registered"
+ "%s | ERROR | CFDictionaryCreateMutable for diskarb failed"
+ "%s | ERROR | DAApprovalSessionCreate failed"
+ "%s | ERROR | screen lock UI teardown did not complete within %.0f seconds, clearing pending teardown and notifying delegate"
+ "%s | Minibuddy exiting with desktop already drawn, expediting dock desktop ready transition"
+ "%s | PSSO re-activation failed, falling back to user list"
+ "-[LWDefaultScreenLockUI _notifyDelegateOfCloseCompletionIfNoTeardownPending]"
+ "-[LWDefaultScreenLockUI _startTeardownWatchdogForGeneration:]_block_invoke"
+ "DisableScreenLockDiskPolicy"
+ "EnableScreenLockDiskPolicy"
+ "TB,V_hasPendingTeardown"
+ "_hasPendingTeardown"
+ "_notifyDelegateOfCloseCompletionIfNoTeardownPending"
+ "_startTeardownWatchdogForGeneration:"
+ "_teardownGeneration"
+ "com.apple.loginwindow.screenlock.diskarbitration"
+ "ensureDiskArbApprovalSession_block_invoke"
+ "hasPendingTeardown"
+ "markSessionAsLoggingOut"
+ "setHasPendingTeardown:"
+ "singleUserLayoutOnly"
- "%s |      Do not UnregisterDiskArbCallbacks lock delay was = INT_MAX"
- "%s |      Do not register DiskArbCallbacks lock delay = INT_MAX"
- "%s |      RegisterDiskArbCallbacks to block disk mounts during screen lock"
- "%s |      Unlock failed, clearing _unlockInProgress"
- "%s |      UnregisterDiskArbCallbacks "
- "%s | DiskArb - CFDictionaryCreateMutable for diskarb failed"
- "%s | DiskArb - DAApprovalSessionCreate failed"
- "%s | DiskArb - Enter - NOT main thread, dispatch to main thread"
- "%s | DiskArb - Enter - already exists so signal semaphore and exit"
- "%s | DiskArb - Enter - but doesnt exist so just signal semaphore and exit"
- "%s | DiskArb - Mount and unmount callbacks put on run loop"
- "%s | DiskArb - Removed diskarb callbacks"
- "%s | DiskArb - create access semaphore"
- "%s | ERROR | Semaphore wait of 10 seconds exceeded, continuing: %ld"
- "ERROR | Failed os_log_create, use default"
- "ERROR | Too many categories defined, use default"
- "RegisterDiskArbCallbacks"
- "UnregisterDiskArbCallbacks"
- "_markSessionAsLoggingOut"
- "diskArbAccessSemaphore_block_invoke"
```
