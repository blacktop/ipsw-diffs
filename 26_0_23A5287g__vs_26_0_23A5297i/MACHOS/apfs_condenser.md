## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x4c068
+2632.0.68.0.3
+  __TEXT.__text: 0x4c234
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf6bc
+  __TEXT.__cstring: 0xf6c2
   __TEXT.__const: 0x260
   __TEXT.__unwind_info: 0x7e8
   __DATA_CONST.__auth_got: 0x3c0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 485E2A5C-9641-3923-ADD2-AECADDC4820D
+  UUID: 6BF80240-AD87-34A6-8243-13905C008B0B
   Functions: 659
   Symbols:   134
   CStrings:  1273
Functions:
~ sub_10000eae4 : 320 -> 324
~ sub_10001ef9c -> sub_10001efa0 : 556 -> 564
~ sub_1000274fc -> sub_100027508 : 1568 -> 1584
~ sub_1000288d0 -> sub_1000288ec : 532 -> 528
~ sub_100028c5c -> sub_100028c74 : 752 -> 760
~ sub_100029c6c -> sub_100029c8c : 1040 -> 1056
~ sub_10002cd1c -> sub_10002cd4c : 1112 -> 1108
~ sub_10002e954 -> sub_10002e980 : 236 -> 240
~ sub_1000328e0 -> sub_100032910 : 712 -> 768
~ sub_100035730 -> sub_100035798 : 1872 -> 1816
~ sub_100035ebc -> sub_100035eec : 804 -> 832
~ sub_10003637c -> sub_1000363c8 : 2612 -> 2676
~ sub_100036db0 -> sub_100036e3c : 72 -> 64
~ sub_100037524 -> sub_1000375a8 : 3272 -> 3328
~ sub_100038af8 -> sub_100038bb4 : 380 -> 448
~ sub_1000394d4 -> sub_1000395d4 : 1004 -> 1008
~ sub_10003a898 -> sub_10003a99c : 308 -> 364
~ sub_10003a9cc -> sub_10003ab08 : 116 -> 180
~ sub_1000408dc -> sub_100040a58 : 5820 -> 5896
~ sub_1000470c4 -> sub_10004728c : 1388 -> 1392
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
