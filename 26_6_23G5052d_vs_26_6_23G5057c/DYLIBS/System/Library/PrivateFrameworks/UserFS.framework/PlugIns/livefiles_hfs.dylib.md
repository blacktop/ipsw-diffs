## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-  __TEXT.__text: 0x3dcd8
+  __TEXT.__text: 0x3dd00
   __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x4e60
   __TEXT.__oslogstring: 0x5cc6
   __TEXT.__cstring: 0x26fb
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x6d0
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x238
   __AUTH.__data: 0x140

   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  Functions: 677
-  Symbols:   1163
+  Functions: 678
+  Symbols:   1165
   CStrings:  739
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ _hfs_set_summary
Functions:
~ _cat_lookupbykey : 1788 -> 1796
~ _ScanUnmapBlocks : 1180 -> 1116
~ _hfs_release_summary : 132 -> 136
~ _hfs_init_summary : 300 -> 316
~ _BlockFindAny : 960 -> 932
~ _BlockFindContiguous : 2048 -> 2028
~ _hfs_find_summary_free : 160 -> 172
+ _hfs_set_summary
~ _InsertKeyRecord : 400 -> 408

```
