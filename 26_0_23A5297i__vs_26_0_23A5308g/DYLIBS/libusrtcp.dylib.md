## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.0.219.0.1
-  __TEXT.__text: 0x5c704
+5569.0.275.0.6
+  __TEXT.__text: 0x5c8f4
   __TEXT.__auth_stubs: 0x1020
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe59c
-  __TEXT.__cstring: 0x1a11
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__oslogstring: 0xe78d
+  __TEXT.__cstring: 0x1a22
+  __TEXT.__unwind_info: 0x458
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x3e8
   __AUTH_CONST.__auth_got: 0x810
   __AUTH_CONST.__const: 0x1a8
   __AUTH.__data: 0x220
   __DATA.__data: 0x10
-  __DATA.__bss: 0x6d0
+  __DATA.__bss: 0x6c0
   __DATA_DIRTY.__data: 0x184
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FBCFD43A-A8E3-3D93-8138-0E87F6DF6B73
-  Functions: 325
-  Symbols:   1005
-  CStrings:  1113
+  UUID: 374CAA13-8713-309B-BDD6-542A968FA86F
+  Functions: 326
+  Symbols:   1007
+  CStrings:  1119
 
Symbols:
+ _tcp_remove_timer
Functions:
~ _tcp_check_timer_state : 1720 -> 1700
~ _tcp_process_timerlist : 3664 -> 3452
~ _tcp_garbage_collect : 4496 -> 4384
~ _tcp_canceltimers : 220 -> 108
~ _add_to_time_wait : 1136 -> 1024
~ _tcp_close : 3872 -> 3940
+ _tcp_remove_timer
CStrings:
+ "%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry"
+ "%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, backtrace limit exceeded"
+ "%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, dumping backtrace:%{public}s"
+ "%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, no backtrace"
+ "%{public}s %{public}s retiring defunct socket from the TCP timer list (wantcnt=%d)"
+ "tcp_remove_timer"

```
