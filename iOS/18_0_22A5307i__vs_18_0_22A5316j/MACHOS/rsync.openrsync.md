## rsync.openrsync

> `/usr/libexec/rsync/rsync.openrsync`

```diff

-91.0.3.0.0
-  __TEXT.__text: 0x295e4
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__const: 0x5668
-  __TEXT.__cstring: 0x6768
-  __TEXT.__unwind_info: 0x548
+91.0.6.0.0
+  __TEXT.__text: 0x3d2cc
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__const: 0x56d8
+  __TEXT.__cstring: 0x678b
+  __TEXT.__oslogstring: 0x28ab
+  __TEXT.__unwind_info: 0x598
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x17a8
+  __DATA_CONST.__const: 0x17c8
   __DATA.__data: 0x760
   __DATA.__bss: 0x788
-  __DATA.__common: 0x18
+  __DATA.__common: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsbuf.dylib
   - /usr/lib/libutil.dylib
-  Functions: 625
-  Symbols:   210
-  CStrings:  1338
+  Functions: 996
+  Symbols:   216
+  CStrings:  1762
 
Symbols:
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ _os_log_create
+ _os_log_type_enabled
+ _os_variant_has_internal_content
CStrings:
+ "com.apple.rsync"
+ "syslog-trace"
+ "trace"

```
