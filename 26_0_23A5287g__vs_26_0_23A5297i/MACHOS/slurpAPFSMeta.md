## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x36e64
+2632.0.68.0.3
+  __TEXT.__text: 0x3702c
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x9092
+  __TEXT.__cstring: 0x9098
   __TEXT.__const: 0x200
   __TEXT.__unwind_info: 0x678
   __DATA_CONST.__auth_got: 0x418

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 950D728C-0418-326D-8FAC-5AE28432455F
+  UUID: ECF2CF6E-59AE-3405-AEC9-B3D0D1465534
   Functions: 518
   Symbols:   144
   CStrings:  790
Functions:
~ sub_100009670 : 556 -> 564
~ sub_1000112c4 -> sub_1000112cc : 1568 -> 1584
~ sub_100011ce8 -> sub_100011d00 : 532 -> 528
~ sub_100012074 -> sub_100012088 : 752 -> 760
~ sub_100013084 -> sub_1000130a0 : 1040 -> 1056
~ sub_10001e318 -> sub_10001e344 : 5820 -> 5896
~ sub_100024740 -> sub_1000247b8 : 1388 -> 1392
~ sub_100025ef0 -> sub_100025f6c : 176 -> 180
~ sub_100028944 -> sub_1000289c4 : 712 -> 768
~ sub_10002a09c -> sub_10002a154 : 1872 -> 1816
~ sub_10002a828 -> sub_10002a8a8 : 804 -> 832
~ sub_10002ace8 -> sub_10002ad84 : 2612 -> 2676
~ sub_10002b71c -> sub_10002b7f8 : 72 -> 64
~ sub_10002be90 -> sub_10002bf64 : 3272 -> 3328
~ sub_10002d3f8 -> sub_10002d504 : 380 -> 448
~ sub_10002ddd4 -> sub_10002df24 : 1000 -> 1004
~ sub_10002ec10 -> sub_10002ed64 : 308 -> 364
~ sub_10002ed44 -> sub_10002eed0 : 116 -> 180
~ sub_100030448 -> sub_100030614 : 1112 -> 1108
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"

```
