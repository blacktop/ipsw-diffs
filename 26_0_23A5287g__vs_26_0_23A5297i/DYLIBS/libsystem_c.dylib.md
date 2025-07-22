## libsystem_c.dylib

> `/usr/lib/system/libsystem_c.dylib`

```diff

-1725.0.7.0.0
-  __TEXT.__text: 0x779a0
+1725.0.11.0.0
+  __TEXT.__text: 0x77910
   __TEXT.__auth_stubs: 0x1010
-  __TEXT.__const: 0x2720
-  __TEXT.__cstring: 0x3276
+  __TEXT.__const: 0x2740
+  __TEXT.__cstring: 0x325c
   __TEXT.__oslogstring: 0x5c
   __TEXT.__unwind_info: 0x13e8
   __DATA_CONST.__got: 0x40

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 0D701ED8-711C-304E-82C3-BAD797EA43BD
+  UUID: F65D2233-5A15-30F6-9B54-0ACDE7039BA1
   Functions: 1831
-  Symbols:   3066
-  CStrings:  882
+  Symbols:   3068
+  CStrings:  880
 
Symbols:
+ _execvPe_err_preamble
+ _execvPe_err_trailer
Functions:
~ _posix_spawnp : 812 -> 768
~ _openpty : 312 -> 316
~ _execvPe : 876 -> 780
~ _ptsname_r : 232 -> 224
CStrings:
- ": path too long\n"
- "execvP: "

```
