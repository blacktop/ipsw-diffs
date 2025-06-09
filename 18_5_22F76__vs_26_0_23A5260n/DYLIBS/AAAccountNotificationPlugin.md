## AAAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin`

```diff

-1007.477.0.0.0
-  __TEXT.__text: 0x9734
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x4bc
+1025.0.0.0.0
+  __TEXT.__text: 0x9c9c
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0x4d4
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x9f5
-  __TEXT.__oslogstring: 0x16fc
+  __TEXT.__cstring: 0xa96
+  __TEXT.__oslogstring: 0x1825
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methname: 0x19a0
+  __TEXT.__objc_methname: 0x1a8b
   __TEXT.__objc_methtype: 0x34e
-  __TEXT.__objc_stubs: 0x1840
-  __DATA_CONST.__got: 0x2a0
+  __TEXT.__objc_stubs: 0x1900
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x7a8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x730
+  __AUTH_CONST.__objc_const: 0x750
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_ivar: 0x40
   __DATA.__data: 0xc0
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CEEC84E-5080-3C3F-BF5A-0AE8A863D2DA
-  Functions: 153
-  Symbols:   178
-  CStrings:  528
+  UUID: 29BC2A11-E9C2-3C41-B711-40D8617AD2FD
+  Functions: 161
+  Symbols:   182
+  CStrings:  543
 
Symbols:
+ _AAFollowUpIdentifierAgeMigration
+ _AAFollowUpIdentifierChildOrTeenProtoConnect
+ _OBJC_CLASS_$_AAAgeMigrationController
+ _OBJC_CLASS_$_AAAgeMigrationFeatureStateProvider
+ _objc_opt_new
- _AAFollowUpIdentifierChildProtoConnect
CStrings:
+ "A non-child or teen proto account was modified, but we don't care."
+ "Age migration CFU should already exist. Leaving it"
+ "AppleAccount is being removed - Remove follow ups."
+ "Dismissed child migration followup with error: %@"
+ "No need to post an age migration CFU."
+ "Pending DOB has been removed. Removing related follow ups"
+ "Posting an Age migration CFU."
+ "Proto account age range has been modified and is no longer a child or teen - Remove follow ups."
+ "Proto account is being removed - Remove follow ups."
+ "_ageMigrationCFURemovalQueue"
+ "_childOrTeenConnectRemovalQueue"
+ "_dismissAgeMigrationFollowUp"
+ "_dismissChildOrTeenProtoConnectFollowUp"
+ "aa_isTeenProtoAccount"
+ "aa_pendingDOB"
+ "ageMigrationFeatureEnabled"
+ "clearAgeMigrationFollowUpWithCompletion:"
+ "com.apple.AppleAccount.AAAccountNotificationFollowUp-removeAgeMigrationCFU.txn"
+ "com.apple.AppleAccount.AAAccountNotificationFollowUp-removeChildOrTeenConnect.txn"
+ "com.apple.AppleAccount.AAAccountNotificationFollowUp.RemoveChildMigationCFU"
+ "removeChildOrTeenConnectFollowUpWithCompletion:"
+ "updateAgeMigrationFollowUpForAccount:oldAccount:"
+ "updateChildOrTeenProtoConnectFollowupForAccountStore:account:oldAccount:"
- "A non-child protoaccount was modified, but we don't care."
- "Protoaccount age range has been modified and is no longer a child - Remove follow ups."
- "Protoaccount is being removed - Remove follow ups."
- "_childConnectRemovalQueue"
- "_dismissChildProtoConnectFollowUp"
- "com.apple.AppleAccount.AAAccountNotificationFollowUp-removeChildConnect.txn"
- "removeChildConnectFollowUpWithCompletion:"
- "updateChildProtoConnectFollowupForAccountStore:account:oldAccount:"

```
