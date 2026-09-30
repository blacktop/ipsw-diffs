## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-1030.6.2.0.0
+1030.6.3.0.0
   __TEXT.__text: 0x28a0
   __TEXT.__auth_stubs: 0xe0
-  __TEXT.__cstring: 0x443
+  __TEXT.__cstring: 0x492
   __TEXT.__const: 0x20
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__const: 0x7a0
   __AUTH_CONST.__auth_got: 0x70
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
-  UUID: 31EF0479-4100-3DF5-BF58-1B0DB74B36C5
+  UUID: A8F9BD3E-49A0-37EA-86CB-3C683DE22BD8
   Functions: 91
   Symbols:   108
-  CStrings:  116
+  CStrings:  122
 
Functions:
~ _getsegmentdata -> _getsegbyname : 180 -> 112
~ _getsectiondata -> _getsegmentdata : 444 -> 180
~ _getsegbyname -> _getsectbyname : 112 -> 64
~ _getsectdatafromheader_64 -> _getsectiondata : 60 -> 444
~ _getsectbyname -> _getsectdatafromheader_64 : 64 -> 60
~ _NXGetArchInfoFromCpuType -> _NXGetAllArchInfos : 344 -> 12
~ _NXGetAllArchInfos -> _NXGetLocalArchInfo : 12 -> 212
~ _NXGetLocalArchInfo -> _NXGetArchInfoFromCpuType : 212 -> 344
CStrings:
+ "arm v8.1m.main"
+ "arm v8m.base"
+ "arm v8m.main"
+ "armv8.1m.main"
+ "armv8m.base"
+ "armv8m.main"

```
