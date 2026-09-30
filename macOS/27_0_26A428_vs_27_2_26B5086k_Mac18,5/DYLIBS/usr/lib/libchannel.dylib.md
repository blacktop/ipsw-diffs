## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

 59.0.1.0.0
-  __TEXT.__text: 0x31d8
+  __TEXT.__text: 0x30d8
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__gcc_except_tab: 0x284
-  __TEXT.__cstring: 0x158
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__cstring: 0xde
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
   Functions: 144
-  Symbols:   260
-  CStrings:  19
+  Symbols:   254
+  CStrings:  16
 
Symbols:
- GCC_except_table1
- GCC_except_table12
- GCC_except_table15
- GCC_except_table16
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
Functions:
~ __ZN9RTChannel5closeEv : 168 -> 96
~ __ZN7Channel26advance_commit_assert_headEv : 300 -> 348
~ __ZN7Channel10msg_notifyEv : 152 -> 84
~ __ZN7Channel8msg_waitEj : 176 -> 104
~ __ZN7Channel27poll_dead_name_notificationEv : 444 -> 184
~ _ZN7Channel27poll_dead_name_notificationEv.cold.1 : 4 -> 172
CStrings:
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"
```
