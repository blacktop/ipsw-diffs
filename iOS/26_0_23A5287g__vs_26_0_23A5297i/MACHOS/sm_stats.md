## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x43468
+2632.0.68.0.3
+  __TEXT.__text: 0x43630
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcd6a
+  __TEXT.__cstring: 0xcd70
   __TEXT.__const: 0x218
   __TEXT.__unwind_info: 0x6e0
   __DATA_CONST.__auth_got: 0x390

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: DC0327A6-B307-370A-9BB1-A950DE4B2836
+  UUID: CC67D846-B6EE-3230-B2D0-91BA7416D327
   Functions: 573
   Symbols:   128
   CStrings:  1060
Functions:
~ sub_100004734 : 320 -> 324
~ sub_10000b384 -> sub_10000b388 : 5820 -> 5896
~ sub_100011d80 -> sub_100011dd0 : 1388 -> 1392
~ sub_1000162a8 -> sub_1000162fc : 556 -> 564
~ sub_10001e4d4 -> sub_10001e530 : 1568 -> 1584
~ sub_10001eef8 -> sub_10001ef64 : 532 -> 528
~ sub_10001f284 -> sub_10001f2ec : 752 -> 760
~ sub_100020294 -> sub_100020304 : 1040 -> 1056
~ sub_100031a78 -> sub_100031af8 : 1112 -> 1108
~ sub_1000337d8 -> sub_100033854 : 712 -> 768
~ sub_100036628 -> sub_1000366dc : 1872 -> 1816
~ sub_100036db4 -> sub_100036e30 : 804 -> 832
~ sub_100037274 -> sub_10003730c : 2612 -> 2676
~ sub_100037ca8 -> sub_100037d80 : 72 -> 64
~ sub_10003841c -> sub_1000384ec : 3272 -> 3328
~ sub_1000399f0 -> sub_100039af8 : 380 -> 448
~ sub_10003a3cc -> sub_10003a518 : 1004 -> 1008
~ sub_10003b790 -> sub_10003b8e0 : 308 -> 364
~ sub_10003b8c4 -> sub_10003ba4c : 116 -> 180
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"

```
