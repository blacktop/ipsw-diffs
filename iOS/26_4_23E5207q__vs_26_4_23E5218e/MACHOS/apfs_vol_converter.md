## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2811.100.177.0.1
-  __TEXT.__text: 0x58ff0
+2811.100.184.0.1
+  __TEXT.__text: 0x58fe0
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xc00
-  __TEXT.__cstring: 0x11fb0
-  __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__unwind_info: 0xbf0
+  __TEXT.__cstring: 0x12011
+  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__unwind_info: 0xbe8
   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 48891BD1-53C2-31A2-9295-BB23187C0A17
+  UUID: F19986C7-35F6-37FF-A014-F257F1A28972
   Functions: 868
   Symbols:   185
-  CStrings:  1706
+  CStrings:  1707
 
Functions:
~ sub_100014868 : 5048 -> 5284
~ sub_100015cf8 -> sub_100015de4 : 708 -> 120
~ sub_100015fbc -> sub_100015e5c : 108 -> 452
~ sub_100016028 -> sub_100016020 : 120 -> 108
~ sub_1000304d8 -> sub_1000304c4 : 504 -> 508
CStrings:
+ "%s container load\n"
+ "%s:%u Warn: apfs_container_iouc (%s) failed with status: 0x%x, %u, load locking would not be available\n"
+ "/Library/Caches/com.apple.xbs/2A7685AA-611D-4967-8EF7-A36283B6FFE5/TemporaryDirectory.PimCgm/Sources/apfs_executables/fscommon/purging.c"
+ "/Library/Caches/com.apple.xbs/2A7685AA-611D-4967-8EF7-A36283B6FFE5/TemporaryDirectory.PimCgm/Sources/apfs_executables/nx/jobj.c"
+ "/Library/Caches/com.apple.xbs/2A7685AA-611D-4967-8EF7-A36283B6FFE5/TemporaryDirectory.PimCgm/Sources/apfs_executables/nx/jobj_snap.c"
+ "/Library/Caches/com.apple.xbs/2A7685AA-611D-4967-8EF7-A36283B6FFE5/TemporaryDirectory.PimCgm/Sources/apfs_executables/nx/obj.c"
+ "2811.100.184.0.1"
- "%s container load for %s\n"
- "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/fscommon/purging.c"
- "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj.c"
- "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj_snap.c"
- "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/obj.c"
- "2811.100.177.0.1"

```
