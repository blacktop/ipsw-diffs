## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

 715.160.9.0.0
   __TEXT.__const: 0x1ab8
-  __TEXT.__cstring: 0xa8bd
-  __TEXT_EXEC.__text: 0x4e760
+  __TEXT.__cstring: 0xa909
+  __TEXT_EXEC.__text: 0x4e778
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x5f0
   Functions: 511
   Symbols:   1572
-  CStrings:  856
+  CStrings:  857
 
Functions:
~ _hfs_vnop_getxattr : 924 -> 920
~ _HeadTruncateFile : 864 -> 892
CStrings:
+ "hfs: HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
```
