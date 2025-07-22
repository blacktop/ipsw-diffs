## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x51330
+2632.0.68.0.3
+  __TEXT.__text: 0x514fc
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xfb8f
+  __TEXT.__cstring: 0xfb95
   __TEXT.__const: 0x8380
   __TEXT.__unwind_info: 0x840
   __DATA_CONST.__auth_got: 0x468

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 436DD2B5-32A3-30BF-A757-5E401CBE9B42
+  UUID: 0308128F-CBED-33BA-B96A-1E4D5BC88DDF
   Functions: 703
   Symbols:   156
   CStrings:  1343
Functions:
~ sub_10000e39c : 320 -> 324
~ sub_10001cf78 -> sub_10001cf7c : 556 -> 564
~ sub_1000254d8 -> sub_1000254e4 : 1568 -> 1584
~ sub_1000268ac -> sub_1000268c8 : 532 -> 528
~ sub_100026c38 -> sub_100026c50 : 752 -> 760
~ sub_100027c48 -> sub_100027c68 : 1040 -> 1056
~ sub_100032968 -> sub_100032998 : 1112 -> 1108
~ sub_100034494 -> sub_1000344c0 : 268 -> 272
~ sub_1000351d4 -> sub_100035204 : 712 -> 768
~ sub_100038024 -> sub_10003808c : 1872 -> 1816
~ sub_1000387b0 -> sub_1000387e0 : 804 -> 832
~ sub_100038c70 -> sub_100038cbc : 2612 -> 2676
~ sub_1000396a4 -> sub_100039730 : 72 -> 64
~ sub_100039e18 -> sub_100039e9c : 3272 -> 3328
~ sub_10003b3ec -> sub_10003b4a8 : 380 -> 448
~ sub_10003bdc8 -> sub_10003bec8 : 1004 -> 1008
~ sub_10003d18c -> sub_10003d290 : 308 -> 364
~ sub_10003d2c0 -> sub_10003d3fc : 116 -> 180
~ sub_100044200 -> sub_10004437c : 5820 -> 5896
~ sub_10004a9e8 -> sub_10004abb0 : 1388 -> 1392
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
+ "2632.0.68.0.3"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "2632.0.54.0.2"

```
