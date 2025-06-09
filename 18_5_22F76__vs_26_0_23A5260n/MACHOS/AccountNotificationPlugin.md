## AccountNotificationPlugin

> `/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin`

```diff

-226.476.0.0.0
-  __TEXT.__text: 0xb64
+243.1.0.0.0
+  __TEXT.__text: 0xd88
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x1bc
   __TEXT.__const: 0x20
-  __TEXT.__oslogstring: 0x260
+  __TEXT.__oslogstring: 0x312
   __TEXT.__cstring: 0xf5
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x45f
+  __TEXT.__objc_methname: 0x4b2
   __TEXT.__objc_methtype: 0x214
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x108

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AFF3E21-7C05-30C0-9073-18E2B56DEF2F
-  Functions: 16
+  UUID: 92D37FAC-F6A9-3E88-9312-7DA6CD71E1F3
+  Functions: 17
   Symbols:   43
-  CStrings:  102
+  CStrings:  109
 
Symbols:
+ _objc_retain_x20
- _objc_retain_x21
CStrings:
+ "Account is being removed - remove restrictions"
+ "No pending DOB found - skip restrictions"
+ "Pending DOB found - apply restrictions"
+ "Pending DOB has been removed - remove restrictions"
+ "_updateAgeMigrationRestrictionsForAccount:oldAccount:"
+ "aa_pendingDOB"
+ "proto_ageRange"

```
