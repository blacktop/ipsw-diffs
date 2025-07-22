## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x39c64
+2632.0.68.0.3
+  __TEXT.__text: 0x39de4
   __TEXT.__auth_stubs: 0xcc0
   __TEXT.__const: 0x3c0
   __TEXT.__oslogstring: 0x1e12
-  __TEXT.__cstring: 0x74f9
+  __TEXT.__cstring: 0x74ff
   __TEXT.__unwind_info: 0x6f8
   __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0xc8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: E63E4948-5A9F-3D55-AC8A-D445F17CB01A
+  UUID: 7EC008C1-CB4B-3F7E-AF3E-3049429C5F5F
   Functions: 640
   Symbols:   233
   CStrings:  1093
Functions:
~ sub_10000fcd4 : 556 -> 564
~ sub_100017928 -> sub_100017930 : 1568 -> 1584
~ sub_10001834c -> sub_100018364 : 532 -> 528
~ sub_1000186d8 -> sub_1000186ec : 752 -> 760
~ sub_100018a48 -> sub_100018a64 : 1040 -> 1056
~ sub_10001ad24 -> sub_10001ad50 : 508 -> 496
~ sub_100024200 -> sub_100024220 : 1872 -> 1816
~ sub_10002498c -> sub_100024974 : 804 -> 832
~ sub_100024e4c -> sub_100024e50 : 2612 -> 2676
~ sub_100025880 -> sub_1000258c4 : 72 -> 64
~ sub_100025ff4 -> sub_100026030 : 3272 -> 3328
~ sub_1000275c8 -> sub_10002763c : 380 -> 448
~ sub_1000288a8 -> sub_100028960 : 308 -> 364
~ sub_1000289dc -> sub_100028acc : 116 -> 180
~ sub_10002e37c -> sub_10002e4ac : 5820 -> 5896
~ sub_1000347b8 -> sub_100034934 : 1388 -> 1392
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"

```
