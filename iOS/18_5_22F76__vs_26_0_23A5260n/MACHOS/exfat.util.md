## exfat.util

> `/System/Library/Filesystems/exfat.fs/exfat.util`

```diff

-488.120.2.0.0
-  __TEXT.__text: 0x24b8
+522.0.0.0.0
+  __TEXT.__text: 0x24fc
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0xd44
+  __TEXT.__cstring: 0xd76
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x20

   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 78908C79-6BCF-315F-805E-7FBE5FF87029
+  UUID: F98C6C7B-CF40-3112-B9F6-13048F1DDFCA
   Functions: 36
   Symbols:   51
-  CStrings:  87
+  CStrings:  88
 
Functions:
~ sub_100000860 : 1040 -> 1036
~ sub_100001138 -> sub_100001134 : 1288 -> 1360
CStrings:
+ "Invalid ExFAT signature in alternate boot region\n"

```
