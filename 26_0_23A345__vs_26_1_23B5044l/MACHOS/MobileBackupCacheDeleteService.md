## MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

-2899.0.11.0.0
-  __TEXT.__text: 0x12228
+2899.40.32.0.0
+  __TEXT.__text: 0x121d4
   __TEXT.__auth_stubs: 0x7d0
   __TEXT.__objc_stubs: 0x1f40
   __TEXT.__objc_methlist: 0x7d0
   __TEXT.__const: 0x1a0
   __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__cstring: 0x3bda
+  __TEXT.__cstring: 0x3b5f
   __TEXT.__oslogstring: 0x1f0d
-  __TEXT.__objc_methname: 0x244b
+  __TEXT.__objc_methname: 0x2463
   __TEXT.__objc_classname: 0xd8
   __TEXT.__objc_methtype: 0x3cd
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__unwind_info: 0x340
   __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__cfstring: 0xf60
+  __DATA_CONST.__cfstring: 0xf40
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B91FD12E-D908-35A0-9F4E-DBF663C31EFC
+  UUID: 46F76614-4FD9-3702-8613-41AAB210D72B
   Functions: 314
   Symbols:   180
-  CStrings:  1102
+  CStrings:  1099
 
Functions:
~ sub_100000fc8 : 148 -> 156
~ sub_10000105c -> sub_100001064 : 528 -> 420
~ sub_10000126c -> sub_100001208 : 148 -> 156
~ sub_100001300 -> sub_1000012a4 : 148 -> 156
~ sub_100001394 -> sub_100001340 : 248 -> 264
~ sub_1000031a8 -> sub_100003164 : 312 -> 360
~ sub_100003c44 -> sub_100003c30 : 124 -> 60
CStrings:
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:error:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:error:]"
+ "sharedTemporaryDirectoryForTest:error:"
+ "sharedTemporaryDirectoryIdentifiedBy:error:"
+ "userTemporaryDirectoryForPersona:identifiedBy:error:"
+ "userTemporaryDirectoryForTest:error:"
- "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
- "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:]"
- "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:]"
- "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
- "TempDir: Failed to create %s directory (mkdtemp error: %d)"
- "char * _Nullable _mkdtemp(const char *, NSString *__strong, NSError *__autoreleasing *)"
- "sharedTemporaryDirectoryForTest:"
- "sharedTemporaryDirectoryIdentifiedBy:"
- "userTemporaryDirectoryForPersona:identifiedBy:"
- "userTemporaryDirectoryForTest:"

```
