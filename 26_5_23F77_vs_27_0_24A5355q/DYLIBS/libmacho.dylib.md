## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-1378.0.0.0.0
-  __TEXT.__text: 0x285c
-  __TEXT.__auth_stubs: 0xe0
+27050.4.0.0.0
+  __TEXT.__text: 0x2860
   __TEXT.__cstring: 0x492
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__got: 0x8
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7a0
-  __AUTH_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
-  UUID: 7E6E20B0-7267-3D97-A8E0-E056D08F5D2A
+  UUID: 29DD638B-0DCB-31AA-8A76-6279CC8618F1
   Functions: 91
   Symbols:   108
   CStrings:  122
Functions:
~ _getsegbyname -> _getsectbyname : 112 -> 64
~ _getsegmentdata -> _getsectdatafromheader_64 : 180 -> 60
~ _getsectbyname -> _getsegmentdata : 64 -> 180
~ _getsectiondata -> _getsegbyname : 444 -> 112
~ _getsectdatafromheader_64 -> _getsectiondata : 60 -> 444
~ _NXFindBestFatArch : 60 -> 64

```
