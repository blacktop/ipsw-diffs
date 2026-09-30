## AccountNotificationPlugin

> `/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin`

```diff

-226.230.0.0.0
-  __TEXT.__text: 0x61c
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x2c
+226.457.1.0.0
+  __TEXT.__text: 0x8cc
+  __TEXT.__auth_stubs: 0x1b0
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
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xa8
+  __TEXT.__objc_methname: 0x41c
+  __TEXT.__objc_methtype: 0x214
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4e8
-  __DATA.__objc_selrefs: 0x58
+  __DATA.__objc_const: 0x230
+  __DATA.__objc_selrefs: 0x178
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   34
-  CStrings:  83
+  Functions: 12
+  Symbols:   43
+  CStrings:  98
 
Symbols:
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_AKFeatureManager
+ _OBJC_CLASS_$_FASettingProtoAccountRestrictionsRequest
+ __FAAgeAttestationLogSystem
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
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
