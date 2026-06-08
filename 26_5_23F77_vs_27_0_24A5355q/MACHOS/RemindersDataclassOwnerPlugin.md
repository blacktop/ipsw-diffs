## RemindersDataclassOwnerPlugin

> `/System/Library/Accounts/DataclassOwners/RemindersDataclassOwnerPlugin.bundle/RemindersDataclassOwnerPlugin`

```diff

-3976.0.0.0.0
-  __TEXT.__text: 0x24f0
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x294
+4034.15.0.0.0
+  __TEXT.__text: 0x2544
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x88
-  __TEXT.__objc_methname: 0x7bd
-  __TEXT.__cstring: 0x2f
-  __TEXT.__oslogstring: 0xa1e
-  __TEXT.__objc_classname: 0x43
+  __TEXT.__objc_methname: 0x850
+  __TEXT.__cstring: 0x52
+  __TEXT.__oslogstring: 0xaa0
+  __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methtype: 0x231
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__const: 0x68
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0x280
-  __DATA.__objc_selrefs: 0x248
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DB4DEB1-8FC4-3DF0-8785-14AAB5EA2655
-  Functions: 42
+  UUID: 0487039C-B3B8-33F6-B74D-D61B942FB651
+  Functions: 44
   Symbols:   59
-  CStrings:  140
+  CStrings:  149
 
Symbols:
+ ___CFConstantStringClassReference
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _rem_feature_enabled
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "Reminders"
+ "RemindersDCO: Done requested to merge sync data into local data {identifier: %@}."
+ "RemindersDCO: Request to merge sync data into local data failed with error {identifier: %@, error: %@}."
+ "RemindersDCO: _isActiveCloudKitAccount: fetch failed {identifier: %@, error: %@}."
+ "_isActiveCloudKitAccount:"
+ "_performMergeSyncDataIntoLocalDataActionForAccount:"
+ "iCloudSignInAndSignOut"
+ "requestToMergeSyncDataIntoLocalDataWithAccountIdentifier:completion:"
- "RemindersDCO: Should not happen as ACDataclassActionMergeSyncDataIntoLocalData is disabled for now since CK accounts can't be downgraded."

```
