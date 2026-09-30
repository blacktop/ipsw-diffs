## AKAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/Contents/MacOS/AKAccountNotificationPlugin`

```diff

-493.230.1.0.0
-  __TEXT.__text: 0x29d4
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0x80
+493.462.0.0.0
+  __TEXT.__text: 0x2f24
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__objc_methlist: 0x2ec
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__oslogstring: 0x61c
+  __TEXT.__oslogstring: 0x75d
   __TEXT.__cstring: 0x70
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x7b
-  __TEXT.__objc_methname: 0xa77
+  __TEXT.__objc_methname: 0xb43
   __TEXT.__objc_methtype: 0x397
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_stubs: 0x920
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
-  __AUTH_CONST.__auth_got: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x350
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x978
+  __AUTH_CONST.__objc_const: 0x688
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46EE598D-4C44-3C86-A312-AA224599B105
-  Functions: 55
-  Symbols:   52
-  CStrings:  189
+  UUID: 5B17F046-1B6A-3251-9CBA-B2568E23BDCB
+  Functions: 59
+  Symbols:   55
+  CStrings:  202
 
Symbols:
+ _ACAccountTypeIdentifierDCA
+ _OBJC_CLASS_$_AKFeatureManager
+ _objc_enumerationMutation
CStrings:
+ "Deleted proto account: %@"
+ "Deleting proto account: %@"
+ "Failed to delete proto account: %@ with error: %@"
+ "Failed to fetch proto accounts from store: %@ with error: %@"
+ "Valid IdMS account has been added, removing all proto accounts in store: %@"
+ "Valid IdMS account is being added: %@, removing all proto accounts if applicable"
+ "_accountsWithAcountType:error:"
+ "_removeAllProtoAccountsInStore:"
+ "accountTypeWithIdentifier:"
+ "countByEnumeratingWithState:objects:count:"
+ "deleteAccountNoSave:error:"
+ "isAgeAttestationPhase1Enabled"
+ "sharedManager"

```
