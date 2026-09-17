## AUHelperService

> `/System/Library/CoreServices/Applications/Archive Utility.app/Contents/XPCServices/AUHelperService.xpc/Contents/MacOS/AUHelperService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-183.0.0.0.0
-  __TEXT.__text: 0x3100
-  __TEXT.__auth_stubs: 0x290
+184.0.0.0.0
+  __TEXT.__text: 0x383c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0xa60
   __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__cstring: 0x257
+  __TEXT.__cstring: 0x41b
   __TEXT.__objc_classname: 0xb2
   __TEXT.__objc_methname: 0xb36
   __TEXT.__objc_methtype: 0x468
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__unwind_info: 0x138
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3f8
   __DATA.__objc_selrefs: 0x388
   __DATA.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 34
-  Symbols:   83
-  CStrings:  185
+  Functions: 37
+  Symbols:   95
+  CStrings:  192
 
Symbols:
+ _URLIsInsideAnotherUsersHome
+ ___chkstk_darwin
+ _close
+ _fstat
+ _fstatat
+ _geteuid
+ _getpwnam_r
+ _getpwuid_r
+ _objc_terminate
+ _open
+ _openat
+ _stat
CStrings:
+ ".."
+ "URLIsInsideAnotherUsersHome: cannot open a parent directory, errno %d"
+ "URLIsInsideAnotherUsersHome: cannot open the item or its parent directory, errno %d"
+ "URLIsInsideAnotherUsersHome: fstat failed, errno %d"
+ "URLIsInsideAnotherUsersHome: fstat of a parent directory failed, errno %d"
+ "removeItemWithWrapper: refusing to %s an item inside another user's home directory"
+ "renameWithUniquingFrom: refusing to move an item inside another user's home directory"
```
