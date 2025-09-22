## ndp

> `/usr/sbin/ndp`

```diff

-726.0.0.0.0
-  __TEXT.__text: 0x3878
-  __TEXT.__auth_stubs: 0x300
+728.0.0.0.0
+  __TEXT.__text: 0x39b0
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xae7
+  __TEXT.__cstring: 0xb27
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x58
   __DATA.__data: 0x50
   __DATA.__bss: 0x25e8
   __DATA.__common: 0x298
   - /usr/lib/libSystem.B.dylib
-  UUID: F7E8DA31-72E2-36AC-A5F5-B07A55524DC5
-  Functions: 48
+  UUID: 0C29032D-3334-34A2-B6BD-1DAAAA326B19
+  Functions: 47
   Symbols:   136
-  CStrings:  191
+  CStrings:  194
 
Symbols:
+ _freeifaddrs
+ _getifaddrs
- ifinfo.cold.2
- ifinfo.cold.3
CStrings:
+ "\n%s:\n"
+ "getifaddrs"
+ "ndp: cannpt apply flag '%s' to all interfaces\n"

```
