## CloudKitNotificationPlugin

> `/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin`

```diff

-2130.14.1.0.0
-  __TEXT.__text: 0x1290
-  __TEXT.__auth_stubs: 0x240
+2150.34.1.0.0
+  __TEXT.__text: 0x132c
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0x2ff
-  __TEXT.__cstring: 0x12
-  __TEXT.__unwind_info: 0x58
+  __TEXT.__oslogstring: 0x388
+  __TEXT.__cstring: 0x18
+  __TEXT.__unwind_info: 0x5c
   __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methname: 0x55c
+  __TEXT.__objc_methname: 0x56e
   __TEXT.__objc_methtype: 0x204
   __TEXT.__objc_stubs: 0x440
   __DATA_CONST.__got: 0x58

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4a0
   __DATA_CONST.__objc_selrefs: 0x120
+  __DATA_CONST.__objc_classrefs: 0x20
+  __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x128
-  __DATA.__objc_classrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x120
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   Functions: 5
   Symbols:   55
-  CStrings:  106
+  CStrings:  108
 
Symbols:
+ ___CFConstantStringClassReference
- __os_log_debug_impl
CStrings:
+ "Changed account properties are %{public}@to CloudKit: account.dirtyProperties: %{public}@, account.dirthAccountProperties: %{public}@"
+ "Notifying cloudd of an add of account %{public}@. Authorized client: %{public}@. ContainerIDs: %{public}@ ="
+ "T@\"NSString\",?,R,C"
+ "not "
- "Changed account properties are not relevant to CloudKit"
- "Notifying cloudd of an add of account %{public}@"

```
