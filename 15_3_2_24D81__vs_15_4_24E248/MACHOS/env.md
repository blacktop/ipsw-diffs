## env

> `/usr/bin/env`

```diff

-319.0.1.0.0
-  __TEXT.__text: 0xdec
+326.0.0.0.0
+  __TEXT.__text: 0xe14
   __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0x4c
-  __TEXT.__cstring: 0x2ba
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x323
   __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x38
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 3215C19B-1513-3FD6-8A10-D74B89AA2DC6
+  UUID: D7583833-CCD6-32F5-A4A2-2C014014FDB6
   Functions: 6
   Symbols:   38
-  CStrings:  29
+  CStrings:  32
 
Symbols:
+ _chdir
- _ferror
Functions:
~ sub_100002cc4 -> sub_100000588 : 968 -> 980
~ sub_10000308c -> sub_10000095c : 464 -> 52
~ sub_10000325c -> sub_100000990 : 2000 -> 464
~ sub_100003a2c -> sub_100000b60 : 36 -> 2012
CStrings:
+ "-0C:iP:S:u:v"
+ "cannot change directory to '%s'"
+ "must specify command with -C"
+ "must specify command with -P"
+ "usage: env [-0iv] [-C workdir] [-P utilpath] [-S string]\n           [-u name] [name=value ...] [utility [argument ...]]\n"
- "-0iP:S:u:v"
- "usage: env [-0iv] [-P utilpath] [-S string] [-u name]\n           [name=value ...] [utility [argument ...]]\n"

```
