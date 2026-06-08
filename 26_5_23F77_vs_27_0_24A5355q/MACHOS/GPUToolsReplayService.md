## GPUToolsReplayService

> `/System/Library/PrivateFrameworks/GPUToolsDeviceServices.framework/XPCServices/GPUToolsReplayService.xpc/GPUToolsReplayService`

```diff

-314.14.0.0.0
-  __TEXT.__text: 0xb30
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x60
-  __TEXT.__const: 0x60
-  __TEXT.__oslogstring: 0x65
-  __TEXT.__cstring: 0x1bc
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x33
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0x20
+2027.0.28.0.0
+  __TEXT.__text: 0x1180
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x80
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0xb8
+  __TEXT.__cstring: 0x32d
+  __TEXT.__objc_methname: 0x3e
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x24
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x48
+  __DATA.__objc_selrefs: 0x20
+  __DATA.__data: 0x278
+  __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFFB69E0-E3C6-37DF-BF2E-50885C308C51
-  Functions: 15
-  Symbols:   43
-  CStrings:  34
+  UUID: 9AA09AA8-0DE9-3C02-90BC-D7CC11BAAE6C
+  Functions: 38
+  Symbols:   72
+  CStrings:  46
 
Symbols:
+ _GTCoreAlloc
+ _GTCoreFree
+ _GTCoreLogUseOsLog
+ ___stderrp
+ __os_log_fault_impl
+ _apr_allocator_destroy
+ _apr_allocator_max_free_set
+ _apr_atomic_init
+ _apr_initialize
+ _apr_palloc
+ _apr_pcalloc
+ _apr_pcalloc_debug
+ _apr_pool_cleanup_null
+ _apr_pool_cleanup_register
+ _apr_pool_create_ex
+ _apr_pool_initialize
+ _apr_pool_tag
+ _apr_proc_mutex_unix_setup_lock
+ _apr_signal_init
+ _apr_thread_mutex_create
+ _apr_thread_mutex_lock
+ _apr_thread_mutex_unlock
+ _apr_unix_setup_time
+ _bzero
+ _fprintf
+ _gt_tagged_log
+ _mach_memory_entry_ownership
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_storeStrong
+ _pthread_mutexattr_destroy
+ _pthread_mutexattr_init
+ _pthread_mutexattr_settype
- _objc_autoreleaseReturnValue
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
CStrings:
+ "%s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
+ "Dump"
+ "MemWatch"
+ "UTF8String"
+ "fail: Invalid log tag: %u"
+ "warning: failed to create memory entry error 0x%x (%s)\n"
+ "warning: failed to map memory error 0x%x (%s)\n"
+ "warning: failed to mark memory(GRAPHICS) error 0x%x (%s)"
+ "warning: failed to mark memory(GRAPHICS) error 0x%x (%s)\n"

```
