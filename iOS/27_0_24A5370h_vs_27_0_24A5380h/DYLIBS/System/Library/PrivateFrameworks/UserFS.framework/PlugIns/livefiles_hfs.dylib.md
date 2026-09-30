## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-  __TEXT.__text: 0x3d388
+  __TEXT.__text: 0x3d360
   __TEXT.__const: 0x4e60
   __TEXT.__oslogstring: 0x5ecc
   __TEXT.__cstring: 0x26fb
-  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0

   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  Functions: 676
-  Symbols:   1141
+  Functions: 677
+  Symbols:   1143
   CStrings:  747
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ _hfs_set_summary
Functions:
~ _priortysort : 148 -> 156
~ _cat_lookupbykey : 1752 -> 1760
~ _AllocateNode : 440 -> 428
~ _ReadFile : 296 -> 320
~ _journal_open : 3768 -> 3816
~ _replay_journal : 6340 -> 6220
~ _write_journal_header : 672 -> 668
~ _journal_create : 1648 -> 1636
~ _end_transaction : 4508 -> 4504
~ _journal_is_clean : 1516 -> 1508
~ _FastUnicodeCompare : 224 -> 200
~ _ConvertUnicodeToUTF8Mangled : 456 -> 468
~ _ScanUnmapBlocks : 1136 -> 1072
~ _hfs_release_summary : 132 -> 136
~ _hfs_init_summary : 268 -> 284
~ _BlockFindAny : 960 -> 932
~ _BlockFindContiguous : 1992 -> 1984
~ _hfs_find_summary_free : 160 -> 172
+ _hfs_set_summary
~ _InsertKeyRecord : 412 -> 420

```
