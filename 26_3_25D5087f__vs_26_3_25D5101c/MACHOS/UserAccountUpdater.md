## UserAccountUpdater

> `/System/Library/CoreServices/UserAccountUpdater`

```diff

-534.0.0.0.0
-  __TEXT.__text: 0xa7c
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x3a0
+535.0.0.0.0
+  __TEXT.__text: 0xbe4
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0x278
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x324
   __TEXT.__oslogstring: 0x55
-  __TEXT.__objc_methname: 0x20e
+  __TEXT.__objc_methname: 0x284
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x30
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_selrefs: 0x108
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/Versions/A/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration
   - /System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4DF9F4E-D3B1-38CA-9BB9-6BC7B72DA876
+  UUID: 1D734691-1B16-36F5-94F6-529958EBEA91
   Functions: 6
-  Symbols:   41
-  CStrings:  76
+  Symbols:   45
+  CStrings:  86
 
Symbols:
+ _OBJC_CLASS_$_LACSExtractablePassword
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _objc_opt_class
Functions:
~ sub_100000bb0 -> sub_100000c50 : 2636 -> 2996
CStrings:
+ "UAU: Failed to deserialize LACSExtractablePassword with nil error"
+ "UAU: Failed to deserialize LACSExtractablePassword: %@"
+ "UAU: Invalid LACSExtractablePassword base64 string"
+ "UserAccountUpdater: login window passed the wrong number of arguments: %d. We require 8\n"
+ "initWithBase64EncodedString:options:"
+ "setPassword:"
+ "stringWithCString:encoding:"
+ "unarchivedObjectOfClass:fromData:error:"
- "UserAccountUpdater: login window passed the wrong number of arguments: %d. We require 7\n"

```
