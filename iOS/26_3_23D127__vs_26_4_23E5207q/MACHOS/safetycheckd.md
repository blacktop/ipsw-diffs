## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-595.0.2.0.0
-  __TEXT.__text: 0x89b0
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x510
-  __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0xe8f
-  __TEXT.__oslogstring: 0xb51
-  __TEXT.__objc_classname: 0xeb
-  __TEXT.__objc_methtype: 0x373
+618.0.0.0.0
+  __TEXT.__text: 0x8c90
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x500
+  __TEXT.__const: 0x58
+  __TEXT.__objc_methname: 0xe49
+  __TEXT.__oslogstring: 0xb5c
+  __TEXT.__objc_classname: 0xe8
+  __TEXT.__objc_methtype: 0x322
   __TEXT.__cstring: 0x394
-  __TEXT.__gcc_except_tab: 0x558
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x168
+  __TEXT.__gcc_except_tab: 0x574
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x8b0
-  __DATA.__objc_selrefs: 0x490
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_const: 0x870
+  __DATA.__objc_selrefs: 0x478
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29845C54-B293-35B6-A04A-57886586937E
-  Functions: 111
-  Symbols:   139
-  CStrings:  365
+  UUID: DF29E0AA-F673-3E31-9866-633A3041E9F8
+  Functions: 122
+  Symbols:   132
+  CStrings:  358
 
Symbols:
+ __Block_object_dispose
+ _dispatch_async
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _DSErrorDomain
- _clock_gettime_nsec_np
- _dispatch_group_wait
- _dispatch_queue_attr_make_with_qos_class
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x28
- _objc_retain_x3
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
CStrings:
+ "Source %@ failed to complete fetch within timeout interval"
+ "com.apple.safetycheckd.SCPermissionsService.fetchCompletionQueue"
+ "errorWithException:"
+ "fetchPermissionsFromSource:withName:completion:"
- "@\"NSObject<OS_dispatch_queue_attr>\""
- "Failed to fetch shared resources due to timeout"
- "_permissionsLock"
- "_priorityAttribute"
- "com.apple.safetycheckd.SCPermissionsService.stopSharingWorkQueue"
- "fetchCompletedForSource:"
- "fetchStartedForSource:"
- "numberWithUnsignedLongLong:"
- "setValue:forKey:"
- "userInfo"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
