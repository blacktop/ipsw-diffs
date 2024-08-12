## PCSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin`

```diff

-1037.0.21.0.0
-  __TEXT.__text: 0x8b0
+1037.40.9.0.0
+  __TEXT.__text: 0x8c4
   __TEXT.__auth_stubs: 0x70
   __TEXT.__objc_methlist: 0x88
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0xb2
-  __TEXT.__oslogstring: 0x337
+  __TEXT.__oslogstring: 0x33f
   __TEXT.__unwind_info: 0x70
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x3f3
+  __TEXT.__objc_methname: 0x3fd
   __TEXT.__objc_methtype: 0x20f
-  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x300
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0xd0
   __AUTH_CONST.__auth_got: 0x40
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x528

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 10
   Symbols:   30
-  CStrings:  109
+  CStrings:  110
 
Symbols:
+ _PCSIdentityHaveiCloudIdentityLocally
- _PCSIdentityNeedsSetup
CStrings:
+ "account:willChangeWithType: update %!d(MISSING): for account %!@(MISSING) (password: %!@(MISSING), pcs dataclass: %!@(MISSING), gf: %!@(MISSING))"
+ "boolValue"
- "account:willChangeWithType: update %!d(MISSING): for account %!@(MISSING) (password: %!@(MISSING), pcs dataclass: %!@(MISSING))"

```
