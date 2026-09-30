## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__os_assumes_log`

```diff

-1966.1.1.0.0
-  __TEXT.__text: 0x27964
-  __TEXT.__auth_stubs: 0x1a40
+1966.40.15.0.0
+  __TEXT.__text: 0x27c60
+  __TEXT.__auth_stubs: 0x1a50
   __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x288
-  __TEXT.__cstring: 0x4b1c
+  __TEXT.__cstring: 0x4c0e
   __TEXT.__objc_methname: 0x3e2
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__unwind_info: 0x8d8
   __DATA_CONST.__const: 0x26d8
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xd28
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x120

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 549
-  Symbols:   475
-  CStrings:  649
+  Functions: 550
+  Symbols:   476
+  CStrings:  656
 
Symbols:
+ _getenv_copy_np
CStrings:
+ "%s.%s"
+ "Client attempted realtime logging connection but was not trusted. PID: %d"
+ "LIBTRACE_DEBUG_LOGD_SERVICE"
+ "com.apple.private.logging.realtime"
+ "events"
+ "failed to check in to %s (0x%x)"
+ "logd_session_service_name: per-session service name too long"
+ "realtime"
+ "unprivileged logd: LIBTRACE_DEBUG_LOGD_SERVICE not set"
- "failed to allocate mach port"
- "failed to checkin to com.apple.logd"
```
