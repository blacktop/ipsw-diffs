## cmp

> `/usr/bin/cmp`

```diff

-66.0.0.0.0
-  __TEXT.__text: 0xe84
-  __TEXT.__auth_stubs: 0x1c0
+70.0.0.0.0
+  __TEXT.__text: 0x1008
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__const: 0x62
-  __TEXT.__cstring: 0x25f
+  __TEXT.__cstring: 0x27d
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0xe0
-  __DATA.__common: 0x5
+  __DATA.__common: 0xc
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 32F0DDF4-E877-3523-9086-B2C66A765F3B
-  Functions: 11
-  Symbols:   34
-  CStrings:  28
+  UUID: 786498B7-7AD4-3BE3-AF5A-A6753461D90B
+  Functions: 12
+  Symbols:   37
+  CStrings:  29
 
Symbols:
+ ___stdoutp
+ _fflush
+ _setvbuf
+ _signal
- _strcmp
CStrings:
+ "%s %s char %zu line %zu\n"
+ "stdout"
- "-"

```
