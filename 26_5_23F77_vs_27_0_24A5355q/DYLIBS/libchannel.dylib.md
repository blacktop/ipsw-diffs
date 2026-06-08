## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

-56.100.3.0.0
-  __TEXT.__text: 0x3288
-  __TEXT.__auth_stubs: 0x420
+59.0.0.0.0
+  __TEXT.__text: 0x3090
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x2c0
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0x157
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x1e
-  __TEXT.__objc_methtype: 0x11
-  __DATA_CONST.__got: 0x40
+  __TEXT.__gcc_except_tab: 0x1e0
+  __TEXT.__cstring: 0xde
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__objc_const: 0x240
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 7BF0E097-F245-3860-A88D-ED3B7586CEEB
-  Functions: 148
-  Symbols:   406
-  CStrings:  28
+  UUID: 1201C9C8-42DD-382D-9634-EF4E53807DDB
+  Functions: 144
+  Symbols:   391
+  CStrings:  16
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x8
- GCC_except_table1
- GCC_except_table12
- GCC_except_table14
- GCC_except_table15
- GCC_except_table16
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
CStrings:
- "OS_channel"
- "OS_channel_dispatch"
- "OS_channel_endpoint"
- "OS_channel_rt"
- "Vv16@0:8"
- "_xref_dispose"
- "dealloc"
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"
- "release"
- "v16@0:8"

```
