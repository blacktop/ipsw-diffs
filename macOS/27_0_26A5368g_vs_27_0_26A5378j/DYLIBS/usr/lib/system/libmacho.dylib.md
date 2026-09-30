## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-  __TEXT.__text: 0x2958
+  __TEXT.__text: 0x28dc
   __TEXT.__cstring: 0x492
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__unwind_info: 0xb8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7a0
   __DATA_CONST.__got: 0x0
Sections:
~ __DATA_CONST.__const : content changed
Functions:
~ _getsectiondata : 496 -> 512
~ _getsectbynamefromheader_64 : 236 -> 216
~ _NXGetArchInfoFromCpuType : 360 -> 344
~ _getsectbynamefromheader : 236 -> 216
~ _NXGetArchInfoFromName : 92 -> 76
~ _NXFreeArchInfo : 108 -> 96
~ _getsectbynamefromheaderwithswap : 328 -> 300
~ _getsectbynamefromheaderwithswap_64 : 328 -> 300

```
