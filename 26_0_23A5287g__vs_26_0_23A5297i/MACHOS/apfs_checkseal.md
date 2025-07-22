## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x4ed4c
+2632.0.68.0.3
+  __TEXT.__text: 0x4ef08
   __TEXT.__auth_stubs: 0x750
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0xff5c
+  __TEXT.__cstring: 0xff62
   __TEXT.__unwind_info: 0x8b8
   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x50

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E7A4C10F-B37B-3D63-91AF-888CAE33BB15
+  UUID: A49197E1-C394-34FE-9317-8BDFD64105C5
   Functions: 722
   Symbols:   131
   CStrings:  1301
Functions:
~ sub_10000afb0 : 556 -> 564
~ sub_100013510 -> sub_100013518 : 1568 -> 1584
~ sub_1000148e4 -> sub_1000148fc : 532 -> 528
~ sub_100014c70 -> sub_100014c84 : 752 -> 760
~ sub_100015c80 -> sub_100015c9c : 1040 -> 1056
~ sub_10001d3a4 -> sub_10001d3d0 : 508 -> 496
~ sub_1000299ac -> sub_1000299cc : 320 -> 324
~ sub_100031e28 -> sub_100031e4c : 1112 -> 1108
~ sub_100033b88 -> sub_100033ba8 : 712 -> 768
~ sub_1000369d8 -> sub_100036a30 : 1872 -> 1816
~ sub_100037164 -> sub_100037184 : 804 -> 832
~ sub_100037624 -> sub_100037660 : 2612 -> 2676
~ sub_100038058 -> sub_1000380d4 : 72 -> 64
~ sub_1000387cc -> sub_100038840 : 3272 -> 3328
~ sub_100039da0 -> sub_100039e4c : 380 -> 448
~ sub_10003a77c -> sub_10003a86c : 1004 -> 1008
~ sub_10003bb40 -> sub_10003bc34 : 308 -> 364
~ sub_10003bc74 -> sub_10003bda0 : 116 -> 180
~ sub_100041d18 -> sub_100041e84 : 5820 -> 5896
~ sub_100048500 -> sub_1000486b8 : 1388 -> 1392
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"

```
