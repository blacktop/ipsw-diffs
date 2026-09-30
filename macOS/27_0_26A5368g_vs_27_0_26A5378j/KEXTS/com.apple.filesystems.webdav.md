## com.apple.filesystems.webdav

> `com.apple.filesystems.webdav`

```diff

   __TEXT.__cstring: 0x878
   __TEXT.__const: 0xd0
-  __TEXT_EXEC.__text: 0x5c88
-  __TEXT_EXEC.__auth_stubs: 0x710
+  __TEXT_EXEC.__text: 0x5cd0
+  __TEXT_EXEC.__auth_stubs: 0x740
   __DATA.__data: 0x340
   __DATA.__common: 0x38
   __DATA.__bss: 0x818
-  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x30
   Functions: 66
-  Symbols:   229
+  Symbols:   232
   CStrings:  57
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _kauth_getgid
+ _kauth_getuid
+ _vfs_context_issuser
Functions:
~ _webdav_assign_ref : 372 -> 368
~ _webdav_mount : 1176 -> 1220
~ _webdav_vnop_setattr : 716 -> 748

```
