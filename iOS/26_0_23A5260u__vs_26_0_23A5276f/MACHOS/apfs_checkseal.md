## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x4ecf4
-  __TEXT.__auth_stubs: 0x740
+2632.0.36.0.1
+  __TEXT.__text: 0x4ed54
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__const: 0x510
   __TEXT.__cstring: 0xff5c
   __TEXT.__unwind_info: 0x8b8
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x7b8

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: BBFA7405-F507-38F0-A79E-D0E34F36C74E
+  UUID: FA412934-AD63-364A-8F61-CFAA2A5CFF33
   Functions: 722
-  Symbols:   130
+  Symbols:   131
   CStrings:  1301
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_1000028ac : 484 -> 580

```
