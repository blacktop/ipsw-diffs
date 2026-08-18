## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

 715.160.9.0.0
   __TEXT.__const: 0x1b50
-  __TEXT.__cstring: 0xa4fb
-  __TEXT_EXEC.__text: 0x52300
+  __TEXT.__cstring: 0xa547
+  __TEXT_EXEC.__text: 0x52318
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x690
   Functions: 533
   Symbols:   0
-  CStrings:  870
+  CStrings:  871
 
Functions:
~ sub_fffffe00099ba954 -> _hfs_vnop_removexattr : 928 -> 924
~ _HeadTruncateFile : 864 -> 892
CStrings:
+ "hfs: HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
```
