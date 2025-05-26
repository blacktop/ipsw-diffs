## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

```diff

-162.3.0.0.0
-  __TEXT.__text: 0x780
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0xe0
+176.0.0.0.0
+  __TEXT.__text: 0x40c
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0xa0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x12d
-  __TEXT.__oslogstring: 0x133
-  __TEXT.__objc_methname: 0x7c
-  __TEXT.__unwind_info: 0x64
-  __DATA.__auth_got: 0x160
-  __DATA.__got: 0x10
+  __TEXT.__cstring: 0x7a
+  __TEXT.__oslogstring: 0x16
+  __TEXT.__objc_methname: 0x5c
+  __TEXT.__unwind_info: 0x6c
+  __DATA.__auth_got: 0x110
+  __DATA.__got: 0x8
   __DATA.__const: 0x48
-  __DATA.__cfstring: 0x120
+  __DATA.__cfstring: 0x40
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x38
+  __DATA.__objc_selrefs: 0x28
   __DATA.__objc_classrefs: 0x10
+  __DATA.__data: 0x8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 7
-  Symbols:   55
-  CStrings:  31
+  Functions: 8
+  Symbols:   45
+  CStrings:  13
 
Symbols:
+ _tailspin_request_unique_id
- _CFDictionaryGetTypeID
- _CFGetTypeID
- _CFPreferencesCopyValue
- _CFPreferencesSetValue
- _CFRelease
- __os_log_impl
- _kCFPreferencesAnyHost
- _notify_post
- _objc_release_x23
- _strncmp
- _tailspin_buffer_size_get
CStrings:
- "%{public}s reset HangTracer + Bluetooth defaults"
- "%{public}s reset on-disk tailspin configuration. Apple-Internal: %{bool}d, Is Audio: %{bool}d"
- "Audio"
- "Did"
- "Didn't"
- "EnableTailspinLogging"
- "HangTracerEnableTailspin"
- "HangTracerEnabled"
- "Not audioanalyticsd, no on-disk config"
- "audioanalyticsd"
- "com.apple.MobileBluetooth.debug"
- "com.apple.da"
- "com.apple.da.tasking_changed"
- "is audioanalyticsd: %{bool}d, buffer size: %zu"
- "last build reset: %{public}@, current build: %{public}@"
- "mobile"
- "mutableCopy"
- "removeObjectForKey:"

```
