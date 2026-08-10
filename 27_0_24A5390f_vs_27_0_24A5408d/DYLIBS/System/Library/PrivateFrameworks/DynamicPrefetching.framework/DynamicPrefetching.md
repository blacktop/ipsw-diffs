## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-3.5.8.0.0
-  __TEXT.__text: 0x18abc
+3.6.0.0.0
+  __TEXT.__text: 0x1b2d0
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0x4b6
-  __TEXT.__gcc_except_tab: 0x12ec
-  __TEXT.__cstring: 0x87e
-  __TEXT.__oslogstring: 0x2774
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__const: 0x4f9
+  __TEXT.__gcc_except_tab: 0x1570
+  __TEXT.__cstring: 0x9e5
+  __TEXT.__oslogstring: 0x3019
+  __TEXT.__unwind_info: 0x978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0xb8
-  __AUTH_CONST.__const: 0x1e8
-  __AUTH_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__got: 0xf0
+  __AUTH_CONST.__const: 0x2a8
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xe0
-  __DATA.__bss: 0x248
+  __DATA.__bss: 0x2f8
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 492
-  Symbols:   175
-  CStrings:  266
+  Functions: 555
+  Symbols:   208
+  CStrings:  315
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFRelease
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IOObjectRelease
+ _IORegistryEntryCreateIterator
+ _IOServiceGetMatchingServices
+ __Block_object_dispose
+ __ZN11Prefetching26storage_controller_is_ans2Ev
+ __ZN11Prefetching32detected_storage_controller_nameEv
+ __ZN11Prefetching38detected_storage_controller_class_nameEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ _clock_gettime
+ _dispatch_async_and_wait
+ _dispatch_pthread_root_queue_create
+ _dispatch_queue_create_with_target$V2
+ _gmtime_r
+ _kCFAllocatorDefault
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMainPortDefault
+ _memset
+ _objc_retainBlock
+ _objc_retain_x4
+ _pthread_attr_destroy
+ _pthread_attr_init
+ _pthread_attr_setinheritsched
+ _pthread_attr_setschedparam
+ _setiopolicy_np
CStrings:
+ "%{public}s notification received"
+ ".powerlog_tasking"
+ "ANS2"
+ "ANS3"
+ "AppleANS2CGv2Controller"
+ "AppleANS2Controller"
+ "AppleANS2NVMeController"
+ "AppleANS3CGv2Controller"
+ "AppleANS3NVMeController"
+ "AppleS3ELabController"
+ "AppleS3XController"
+ "Failed to register for %{public}s notifications: %u"
+ "IOPropertyMatch"
+ "IOService"
+ "NVMe SMART Capable"
+ "PowerLog tasking"
+ "S3E"
+ "S3X"
+ "Trial update"
+ "com.apple.DynamicPrefetching.prefetching_root_queue"
+ "disabled"
+ "emit_powerlog_and_ca_telemetry: CA sampling (%u%%) dropped this event"
+ "emit_powerlog_and_ca_telemetry: PowerLog tasking active, skipping CA telemetry"
+ "emit_powerlog_and_ca_telemetry: clock_gettime failed, skipping CA telemetry"
+ "emit_powerlog_and_ca_telemetry: per-app CA daily cap reached, skipping CA telemetry"
+ "emit_powerlog_and_ca_telemetry: systemwide CA daily cap (%llu) reached, skipping CA telemetry"
+ "enabled"
+ "end_scenario_internal: clock_gettime failed, suppressing CA telemetry for bundleid %@"
+ "mmapped_profile: dispatch_pthread_root_queue_create returned nullptr (pool_size=%u); skipping prefetch"
+ "mmapped_profile: dispatch_queue_create_with_target returned nullptr (pool_size=%u); skipping prefetch"
+ "mmapped_profile: prefetch I/O queue not available (creation failed); skipping prefetch"
+ "mmapped_profile: pthread_attr_destroy failed (%{darwin.errno}d)"
+ "mmapped_profile: pthread_attr_init failed (%{darwin.errno}d), prefetch_io_queue will not be created"
+ "mmapped_profile: pthread_attr_setinheritsched(EXPLICIT) failed (%{darwin.errno}d); prefetch worker priority %d may be ignored"
+ "mmapped_profile: pthread_attr_setschedparam(prio=%d) failed (%{darwin.errno}d), continuing with default scheduling"
+ "mmapped_profile: setiopolicy_np(DISK, THREAD, STANDARD) failed on prefetch worker (%{darwin.errno}d)"
+ "mmapped_profile: storage controller generation ans2=%{BOOL}d (Tier-1 prefetch I/O %{public}s)"
+ "powerlog_tasking: clock_gettime failed: %{darwin.errno}d"
+ "powerlog_tasking: exception building marker path: %{public}s"
+ "powerlog_tasking: exception in note_tasking_started: %{public}s"
+ "powerlog_tasking: exception in tasking_active: %{public}s"
+ "powerlog_tasking: failed to create marker \"%s\": %{darwin.errno}d"
+ "powerlog_tasking: failed to remove expired marker \"%s\": %s"
+ "powerlog_tasking: tasking started — CA telemetry suppressed for the next %lld s"
+ "powerlog_tasking: tasking window elapsed, removed marker"
+ "powerlog_tasking: unknown exception in note_tasking_started"
+ "powerlog_tasking: unknown exception in tasking_active"
+ "storage_controller: detected generation=%{public}s"
+ "storage_controller: exception in detect_generation_uncached: %{public}s"
+ "storage_controller: no known NVMe controller generation matched; defaulting to unknown (Tier-1 prefetch disabled)"
+ "storage_controller: unknown exception in detect_generation_uncached"
+ "unknown"
+ "user defaults"
- "Failed to register for Trial update notifications: %d"
- "Failed to register for user defaults notifications: %d"
- "Notify notification received!"
- "Trial update notification received!"
```
