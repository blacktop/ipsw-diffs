## FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

-2624.120.12.0.0
+2877.0.0.0.0
   __TEXT.__text: 0x2e98
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1746
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x174d
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x50

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 826B3440-DCAA-3F8B-88AD-111B7240760F
+  UUID: 83E8862E-BB95-3469-AD54-1EC9394EAC70
   Functions: 42
   Symbols:   94
   CStrings:  269
Functions:
~ sub_100000f04 : 344 -> 340
~ sub_100002450 -> sub_10000244c : 384 -> 388
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"

```
