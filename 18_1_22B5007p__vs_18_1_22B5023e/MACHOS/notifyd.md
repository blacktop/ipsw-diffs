## notifyd

> `/usr/sbin/notifyd`

```diff

-327.0.4.0.0
-  __TEXT.__text: 0xb5e0
+327.0.5.0.0
+  __TEXT.__text: 0xb4f4
   __TEXT.__auth_stubs: 0x950
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1b81
+  __TEXT.__cstring: 0x1b5c
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x4a8
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xb50
+  __DATA_CONST.__const: 0xb30
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2c8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 141
+  Functions: 140
   Symbols:   167
-  CStrings:  283
+  CStrings:  282
 
Symbols:
+ _xpc_event_publisher_set_throttling
- _xpc_event_publisher_fire_barrier
CStrings:
+ "xpc event: %!l(MISSING)lu\n"
- "event-throttled,%!l(MISSING)lu\n"
- "xpc event: %!l(MISSING)lu (inflight: %!u(MISSING))\n"

```
