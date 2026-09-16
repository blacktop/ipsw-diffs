## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
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

-1966.2.1.0.0
-  __TEXT.__text: 0x270ec
-  __TEXT.__auth_stubs: 0x1bc0
+1966.40.15.502.2
+  __TEXT.__text: 0x273d4
+  __TEXT.__auth_stubs: 0x1bd0
   __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x4a0a
+  __TEXT.__cstring: 0x4b02
   __TEXT.__objc_methname: 0x428
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xde8
+  __DATA_CONST.__auth_got: 0xdf0
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x120

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 515
-  Symbols:   500
-  CStrings:  633
+  Functions: 516
+  Symbols:   501
+  CStrings:  641
 
Symbols:
+ _getenv_copy_np
CStrings:
+ "%s.%s"
+ "Client attempted realtime logging connection but was not trusted. PID: %d"
+ "LIBTRACE_DEBUG_LOGD_SERVICE"
+ "admin"
+ "com.apple.private.logging.realtime"
+ "events"
+ "failed to check in to %s (0x%x)"
+ "logd_session_service_name: per-session service name too long"
+ "realtime"
+ "unprivileged logd: LIBTRACE_DEBUG_LOGD_SERVICE not set"
- "failed to allocate mach port"
- "failed to checkin to com.apple.logd"
```
