## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.0.36.0.1
-  __TEXT.__text: 0x4fee8
+2632.0.54.0.2
+  __TEXT.__text: 0x4fee0
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__const: 0x8410
   __TEXT.__cstring: 0xdde2

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: FC2EB705-8667-3428-98D1-F8E9025A0886
+  UUID: AB78A6B1-D8EF-35B0-B218-28FD886127CB
   Functions: 807
   Symbols:   1760
   CStrings:  1443
Functions:
~ _get_volume_io_object -> _get_apfs_io_object : 84 -> 124
~ _APFSVolumeRole -> _get_volume_io_object : 412 -> 84
~ _get_apfs_io_object -> _APFSVolumeRole : 124 -> 412
~ _obj_cache_perform_deferred_updates : 312 -> 304
CStrings:
+ "2632.0.54.0.2"
- "2632.0.36.0.1"

```
