## AAIDMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin`

```diff

-973.1.1.3.0
-  __TEXT.__text: 0x168c
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_methlist: 0xd0
+981.1.1.0.0
+  __TEXT.__text: 0xef8
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_methlist: 0x5c
   __TEXT.__const: 0x8
-  __TEXT.__oslogstring: 0x69a
-  __TEXT.__cstring: 0x4d
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0x78e
-  __TEXT.__objc_methtype: 0x316
-  __TEXT.__objc_stubs: 0x400
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x98
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+  __TEXT.__oslogstring: 0x469
+  __TEXT.__cstring: 0x34
+  __TEXT.__unwind_info: 0x7c
+  __TEXT.__objc_classname: 0x46
+  __TEXT.__objc_methname: 0x538
+  __TEXT.__objc_methtype: 0x223
+  __TEXT.__objc_stubs: 0x320
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x938
-  __DATA_CONST.__objc_selrefs: 0x150
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x100
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x38
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_const: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0xd8
+  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__auth_got: 0xc8
+  __DATA.__objc_classrefs: 0x20
+  __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD088AD8-D6A1-3E6E-BEE1-CE943F20A17A
-  Functions: 26
-  Symbols:   57
-  CStrings:  148
+  UUID: 0620620A-0A36-3ECD-8646-04F189EB1AEC
+  Functions: 14
+  Symbols:   41
+  CStrings:  103
 
Symbols:
- _OBJC_CLASS_$_AADaemonController
- _OBJC_CLASS_$_AASilentSignOutFlowControllerDelegate
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_AKFeatureManager
- _OBJC_METACLASS_$_AASilentSignOutFlowControllerDelegate
- __NSConcreteGlobalBlock
- ___CFConstantStringClassReference
- __dispatch_main_q
- _dispatch_assert_queue$V2
- _markedForSignOutAccountKey
- _objc_alloc_init
- _objc_msgSendSuper2
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_storeStrong
CStrings:
- "\x03"
- ".cxx_destruct"
- "@\"ACAccountStore\""
- "@\"AIDAAccountManager\""
- "@?"
- "AASignOutFlowControllerDelegate"
- "AASilentSignOutFlowControllerDelegate"
- "Attempting to sign out account %@ with dataclass actions (not used)."
- "Looking for Sign Out on account change"
- "Marked for Sign Out property: %@"
- "NO"
- "Not handling sign out since sign out is false, this shouldn't happen, only AuthKit sets it to explicitly to YES, but logging it in case it ever did."
- "Removal of account completed with success: %@, error: %@"
- "Sign out did not occur, error : %@"
- "Silent force sign out does not check for disableFindMyDevice for %@"
- "Silent force sign out does not check for walrus validation"
- "Silent force sign out showAlertWithTitle was called"
- "T@\"AIDAAccountManager\",&,N,V_accountManager"
- "YES"
- "_accountManager"
- "_accountStore"
- "_pendingSignOutCompletion"
- "_shouldSilentlySignOutAppleAccount:"
- "accountManager"
- "accountPropertyForKey:"
- "boolValue"
- "defaultStore"
- "handleMarkedForSignOutForAccount:completion:"
- "init"
- "isEnforceMDMPolicyEnabled"
- "removeAccount:withDataclassActions:completion:"
- "setAccountManager:"
- "signOutFlowController:disableFindMyDeviceForAccount:completion:"
- "signOutFlowController:performWalrusValidationForAccount:completion:"
- "signOutFlowController:showAlertWithTitle:message:completion:"
- "signOutFlowController:signOutAccount:completion:"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v24@0:8@16"
- "v40@0:8@\"AASignOutFlowController\"16@\"ACAccount\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"AASignOutFlowController\"16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
- "v48@0:8@16@24@32@?40"

```
