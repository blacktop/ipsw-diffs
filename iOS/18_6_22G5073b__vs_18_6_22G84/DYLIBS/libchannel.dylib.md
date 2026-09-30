## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

 50.100.3.0.0
-  __TEXT.__text: 0x3214
-  __TEXT.__auth_stubs: 0x400
+  __TEXT.__text: 0x330c
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__gcc_except_tab: 0x2a0
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0xdd
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__cstring: 0x157
+  __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e
   __TEXT.__objc_methtype: 0x11

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 0CC103A4-55D4-3133-B17F-5F55D2F8B32D
+  UUID: 35CF1D5C-88A5-3A1C-A28D-4EBE9AE9A9BB
   Functions: 140
-  Symbols:   384
-  CStrings:  25
+  Symbols:   390
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
~ __ZN7Channel8msg_waitEj : 144 -> 220
~ __ZN7Channel27poll_dead_name_notificationEv : 184 -> 448
~ __ZN7Channel27poll_dead_name_notificationEv.cold.1 : 176 -> 4
CStrings:
+ "mach_msg with timeout=0 is RT safe"
+ "mach_port_mod_refs is RT safe here"
+ "os_crash is not realtime_safe, but crashing is okay"

```
