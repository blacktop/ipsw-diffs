## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x58000
+2632.0.68.0.3
+  __TEXT.__text: 0x581d0
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x11b24
+  __TEXT.__cstring: 0x11b2a
   __TEXT.__gcc_except_tab: 0x5cc
   __TEXT.__unwind_info: 0xbb0
   __DATA_CONST.__auth_got: 0x500

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 5DC35821-E60A-383D-A61C-924A9379109F
+  UUID: 33C14A33-5903-3AC8-8FFA-30ECE9E49349
   Functions: 847
   Symbols:   184
   CStrings:  1676
Functions:
~ sub_100002b9c : 712 -> 768
~ sub_100005b6c -> sub_100005ba4 : 1872 -> 1816
~ sub_1000062f8 : 804 -> 832
~ sub_1000067b8 -> sub_1000067d4 : 2612 -> 2676
~ sub_1000071ec -> sub_100007248 : 72 -> 64
~ sub_100007960 -> sub_1000079b4 : 3272 -> 3328
~ sub_100008f34 -> sub_100008fc0 : 380 -> 448
~ sub_100009910 -> sub_1000099e0 : 1004 -> 1008
~ sub_10000acd4 -> sub_10000ada8 : 308 -> 364
~ sub_10000ae08 -> sub_10000af14 : 116 -> 180
~ sub_10001dda0 -> sub_10001deec : 556 -> 564
~ sub_100026300 -> sub_100026454 : 1568 -> 1584
~ sub_1000276d4 -> sub_100027838 : 532 -> 528
~ sub_100027a60 -> sub_100027bc0 : 752 -> 760
~ sub_100028a70 -> sub_100028bd8 : 1040 -> 1056
~ sub_10002f67c -> sub_10002f7f4 : 500 -> 508
~ sub_10003b66c -> sub_10003b7ec : 320 -> 324
~ sub_100043ae8 -> sub_100043c6c : 1112 -> 1108
~ sub_10004b1e4 -> sub_10004b364 : 5820 -> 5896
~ sub_1000519cc -> sub_100051b98 : 1388 -> 1392
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
