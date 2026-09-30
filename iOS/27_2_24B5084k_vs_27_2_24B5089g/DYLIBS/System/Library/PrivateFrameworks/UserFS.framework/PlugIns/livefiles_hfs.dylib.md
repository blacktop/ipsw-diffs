## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-753.40.2.0.0
-  __TEXT.__text: 0x3d120
+753.40.3.0.0
+  __TEXT.__text: 0x3d380
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5ed7
+  __TEXT.__oslogstring: 0x5f0f
   __TEXT.__cstring: 0x270a
   __TEXT.__unwind_info: 0xa48
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   Functions: 677
   Symbols:   646
-  CStrings:  751
+  CStrings:  752
 
Functions:
~ _hfs_vnop_setxattr : 3008 -> 3616
CStrings:
+ "hfs_setxattr: orphan overflow attr record vol=%s %d,%s\n"
```
