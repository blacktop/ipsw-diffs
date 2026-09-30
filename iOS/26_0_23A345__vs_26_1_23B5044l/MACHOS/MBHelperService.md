## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-2899.0.11.0.0
-  __TEXT.__text: 0x144d8
+2899.40.32.0.0
+  __TEXT.__text: 0x14500
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_stubs: 0x2060
   __TEXT.__objc_methlist: 0xc64
   __TEXT.__const: 0x220
-  __TEXT.__objc_methname: 0x2618
-  __TEXT.__cstring: 0x3aee
+  __TEXT.__objc_methname: 0x2630
+  __TEXT.__cstring: 0x3b06
   __TEXT.__objc_classname: 0x130
   __TEXT.__objc_methtype: 0x76d
   __TEXT.__oslogstring: 0x1f26

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1A7EA73B-8F05-38DE-8A2C-48F58C6788B4
+  UUID: 0D711835-9779-3655-82BB-26F3DE9ED467
   Functions: 393
   Symbols:   286
   CStrings:  1343
Functions:
~ sub_100006ef0 : 148 -> 156
~ sub_100007128 -> sub_100007130 : 148 -> 156
~ sub_1000071bc -> sub_1000071cc : 148 -> 156
~ sub_100007250 -> sub_100007268 : 248 -> 264
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
- "sharedTemporaryDirectoryForTest:"
- "sharedTemporaryDirectoryIdentifiedBy:"
- "userTemporaryDirectoryForPersona:identifiedBy:"
- "userTemporaryDirectoryForTest:"

```
