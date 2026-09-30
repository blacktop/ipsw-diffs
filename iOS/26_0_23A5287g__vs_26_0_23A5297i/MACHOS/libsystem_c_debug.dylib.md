## libsystem_c_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib`

```diff

-1725.0.7.0.0
-  __TEXT.__text: 0xc00d4
+1725.0.11.0.0
+  __TEXT.__text: 0xc0098
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__const: 0x27c4
-  __TEXT.__cstring: 0x2ed5
+  __TEXT.__const: 0x27e4
+  __TEXT.__cstring: 0x2ebb
   __TEXT.__unwind_info: 0x9b0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x13a8

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: 7403E322-3C5C-3318-94C1-64428DA580E8
+  UUID: 48C535E7-169B-3A7B-AD93-DDAC81CA4E72
   Functions: 1707
-  Symbols:   2246
-  CStrings:  829
+  Symbols:   2248
+  CStrings:  827
 
Symbols:
+ _execvPe_err_preamble
+ _execvPe_err_trailer
Functions:
~ _posix_spawnp : 1232 -> 1220
~ _execvPe : 1280 -> 1252
~ _ptsname_r : 344 -> 324
CStrings:
- ": path too long\n"
- "execvP: "

```
