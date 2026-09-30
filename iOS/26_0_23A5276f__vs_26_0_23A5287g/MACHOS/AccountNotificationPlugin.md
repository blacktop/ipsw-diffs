## AccountNotificationPlugin

> `/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin`

```diff

-245.0.0.0.0
-  __TEXT.__text: 0xd88
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x1bc
+247.1.0.0.0
+  __TEXT.__text: 0x8f4
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x20
-  __TEXT.__oslogstring: 0x312
+  __TEXT.__oslogstring: 0x1ce
   __TEXT.__cstring: 0xf5
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x4b2
+  __TEXT.__objc_methname: 0x424
   __TEXT.__objc_methtype: 0x214
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xe0
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x1a0
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F10777F-BAE2-3DA3-8D7F-36E192D70EC9
-  Functions: 17
-  Symbols:   43
-  CStrings:  109
+  UUID: 0BF8AE65-7923-3BAB-9C64-C5231EA31611
+  Functions: 12
+  Symbols:   41
+  CStrings:  99
 
Symbols:
+ _objc_retain_x21
- _objc_release_x23
- _objc_retain_x20
- _objc_retain_x22
CStrings:
- "Account is being removed - remove restrictions"
- "FAAccountNotificationPlugin: ProtoAccount was deleted ... removing restrictions"
- "No pending DOB found - skip restrictions"
- "Pending DOB found - apply restrictions"
- "Pending DOB has been removed - remove restrictions"
- "_clearRestrictionsOnProtoAccountRemoval"
- "_updateAgeMigrationRestrictionsForAccount:oldAccount:"
- "aa_pendingDOB"
- "failed to remove restrictions on proto account removal; error: %@"
- "removeRestrictionsWithCompletion:"

```
