## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2632.0.77.0.1
-  __TEXT.__text: 0x53bac
+2632.2.1.0.0
+  __TEXT.__text: 0x53e10
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__cstring: 0x19901
+  __TEXT.__cstring: 0x19a39
   __TEXT.__const: 0x85f8
   __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__auth_got: 0x5d0

   __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0xef0
-  __DATA.__bss: 0x1e1e9
+  __DATA.__bss: 0x1e1f1
   __DATA.__common: 0xac9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 808E26F1-E5A0-33C9-AA64-8BDDB93B50E4
-  Functions: 944
+  UUID: 799332A5-9F10-3FA6-A29F-1909937110C3
+  Functions: 946
   Symbols:   203
-  CStrings:  1958
+  CStrings:  1963
 
CStrings:
+ "%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than CLONEGROUP_ID_MIN (%u)\n"
+ "(oid 0x%llx) %s: object read was finished already\n"
+ "2632.2.1"
+ "Skipping clonegroup cross-check since INVALID flag is set\n"
+ "clone group tree (id %llu): invalid cookie key length (%u)\n"
+ "clone group tree (id %llu): invalid cookie val length (%u)\n"
+ "clone group tree: cookie group_id (%llu) or cookie_group_id (%llu) is invalid\n"
+ "clone group tree: mapping group_id (%llu) is invalid\n"
- "%s (id %llu): xf %u/%u: %s: invalid clonegroup_id (%llu), less than MIN_CLONEGROUP_ID (%u)\n"
- "2632.0.77.0.1"
- "clone group tree: group_id (%llu) is invalid\n"

```
