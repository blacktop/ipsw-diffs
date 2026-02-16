## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

-56.0.7.0.0
-  __TEXT.__text: 0x3390
-  __TEXT.__auth_stubs: 0x440
+56.100.1.0.0
+  __TEXT.__text: 0x3174
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__gcc_except_tab: 0x220
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0x157
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__cstring: 0xdd
+  __TEXT.__unwind_info: 0x278
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e
   __TEXT.__objc_methtype: 0x11

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 8CA158F1-2A0C-3C03-BD3D-E0D246DBDF9A
-  Functions: 143
-  Symbols:   398
-  CStrings:  28
+  UUID: C11B81A4-E29C-3E2B-8C4F-7CBD91972441
+  Functions: 148
+  Symbols:   399
+  CStrings:  25
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
- GCC_except_table1
- GCC_except_table15
- GCC_except_table16
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x8
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
CStrings:
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"

```
