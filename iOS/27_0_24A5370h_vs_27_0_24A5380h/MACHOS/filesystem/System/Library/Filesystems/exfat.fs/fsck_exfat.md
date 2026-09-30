## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

```diff

-  __TEXT.__text: 0xcc30
+  __TEXT.__text: 0xcc08
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x280
   __TEXT.__cstring: 0x35af
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001760 : 1736 -> 1732
~ sub_100002a70 -> sub_100002a6c : 384 -> 380
~ sub_100003dd0 -> sub_100003dc8 : 484 -> 480
~ sub_1000070a4 -> sub_100007098 : 296 -> 272
~ sub_10000c82c -> sub_10000c808 : 648 -> 644

```
