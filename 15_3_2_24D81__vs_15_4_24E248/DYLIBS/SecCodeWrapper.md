## SecCodeWrapper

> `/System/Library/PrivateFrameworks/SecCodeWrapper.framework/Versions/A/SecCodeWrapper`

```diff

-738.60.3.0.0
-  __TEXT.__text: 0x1e0c
+738.100.25.0.0
+  __TEXT.__text: 0x1e14
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_methlist: 0x360
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x11c
   __TEXT.__oslogstring: 0x87
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x48
   __TEXT.__objc_methname: 0x5e8
   __TEXT.__objc_methtype: 0x1dd

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9DBCC59-48D1-3C42-A7B3-E192D88B4961
-  Functions: 72
-  Symbols:   225
+  UUID: F3790A35-F6CF-31BB-88DA-DDB14B7A61DB
+  Functions: 73
+  Symbols:   226
   CStrings:  136
 
Symbols:
+ +[DynamicCodeIdentity signingRoot].cold.1
Functions:
~ -[StaticCodeIdentity initWithURL:error:] : 196 -> 200
~ +[DynamicCodeIdentity signingRoot] : 84 -> 68
~ -[CodeIdentity getSigningInformation:error:].cold.1 : 72 -> 160
~ -[CodeIdentity getSigningInformation:error:].cold.3 : 160 -> 72

```
