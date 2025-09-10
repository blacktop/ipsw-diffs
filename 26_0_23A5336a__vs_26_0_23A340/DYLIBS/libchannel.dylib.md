## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

 56.0.7.0.0
-  __TEXT.__text: 0x329c
-  __TEXT.__auth_stubs: 0x420
+  __TEXT.__text: 0x3394
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__gcc_except_tab: 0x2c0
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0xdd
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__cstring: 0x157
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e
   __TEXT.__objc_methtype: 0x11

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 5313C74A-C82F-3AC2-AEE5-77E9140CA50D
+  UUID: 20C06621-4A02-313F-B687-03C5C69534AE
   Functions: 143
-  Symbols:   392
-  CStrings:  25
+  Symbols:   398
+  CStrings:  28
 
Symbols:
+ GCC_except_table1
+ GCC_except_table15
+ GCC_except_table16
+ _realtime_runtime_check_pop_authorization
+ _realtime_runtime_check_push_authorization
Functions:
~ __ZN9RTChannel5closeEv : 108 -> 168
~ __ZN7Channel26advance_commit_assert_headEv : 348 -> 300
~ __ZN7Channel10msg_notifyEv : 84 -> 152
~ __ZN7Channel8msg_waitEj : 176 -> 252
~ __ZN7Channel27poll_dead_name_notificationEv : 184 -> 448
~ __ZN7Channel27poll_dead_name_notificationEv.cold.1 : 176 -> 4
CStrings:
+ "mach_msg with timeout=0 is RT safe"
+ "mach_port_mod_refs is RT safe here"
+ "os_crash is not realtime_safe, but crashing is okay"

```
