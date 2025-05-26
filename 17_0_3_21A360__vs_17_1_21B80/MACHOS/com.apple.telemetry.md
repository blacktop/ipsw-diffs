## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-490.0.0.0.0
-  __TEXT.__text: 0x2a20
-  __TEXT.__auth_stubs: 0x330
+490.40.2.0.0
+  __TEXT.__text: 0x2bc4
+  __TEXT.__auth_stubs: 0x390
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x21d
-  __TEXT.__oslogstring: 0x27f7
+  __TEXT.__cstring: 0x2ce
+  __TEXT.__oslogstring: 0x2817
   __TEXT.__unwind_info: 0xac
-  __DATA.__auth_got: 0x198
+  __DATA.__auth_got: 0x1c8
   __DATA.__got: 0x38
   __DATA.__const: 0x1a8
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 45
-  Symbols:   62
-  CStrings:  47
+  Functions: 46
+  Symbols:   68
+  CStrings:  59
 
Symbols:
+ _analytics_send_event
+ _xpc_dictionary_create
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_release
CStrings:
+ "bytes_written"
+ "cleanup_quota"
+ "com.apple.microstackshots.diskQuota"
+ "default_interval"
+ "ending_interval"
+ "exceeded_quota"
+ "failed to allocate for %s event"
+ "interrupt"
+ "interrupt_sample_rate"
+ "pmi"
+ "time_since_last_cleanup"
+ "type"

```
