## AccountNotificationPlugin

> `/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/Contents/MacOS/AccountNotificationPlugin`

```diff

-226.228.0.0.0
-  __TEXT.__text: 0x6b0
-  __TEXT.__auth_stubs: 0xb0
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x2c
+226.459.0.0.0
+  __TEXT.__text: 0x9b0
+  __TEXT.__auth_stubs: 0xc0
+  __TEXT.__objc_stubs: 0x260
+  __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x20
-  __TEXT.__oslogstring: 0x107
-  __TEXT.__cstring: 0xe0
+  __TEXT.__oslogstring: 0x1cd
+  __TEXT.__cstring: 0xf5
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x35e
-  __TEXT.__objc_methtype: 0x20c
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x60
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__objc_methname: 0x41c
+  __TEXT.__objc_methtype: 0x214
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x68
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4e8
-  __DATA.__objc_selrefs: 0x58
+  __DATA.__objc_const: 0x230
+  __DATA.__objc_selrefs: 0x178
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon
+  - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A6BCFBC-A2A5-3595-944C-AE7D665DB54E
-  Functions: 11
-  Symbols:   24
-  CStrings:  83
+  UUID: 645CB0A1-2D4E-314F-9CFD-5631EE9A75CB
+  Functions: 14
+  Symbols:   28
+  CStrings:  98
 
Symbols:
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_AKFeatureManager
+ _OBJC_CLASS_$_FASettingProtoAccountRestrictionsRequest
+ __FAAgeAttestationLogSystem
CStrings:
+ "FAAccountNotificationPlugin: ProtoAccount was deleted ... removing restrictions"
+ "_clearRestrictionsOnProtoAccountRemoval"
+ "accountType"
+ "failed to remove restrictions on proto account error: %@"
+ "feature is not enabled..."
+ "identifier"
+ "isAgeAttestationPhase1Enabled"
+ "isEqualToString:"
+ "protoAccountType"
+ "removeRestrictionsWithCompletion:"
+ "removed proto account restrictions"
+ "sharedInstance"
+ "sharedManager"
+ "v16@0:8"
+ "v20@?0B8@\"NSError\"12"

```
