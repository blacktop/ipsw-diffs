## RemoteManagementAccountNotificationPlugin

> `/System/Library/Accounts/Notification/RemoteManagementAccountNotificationPlugin.bundle/RemoteManagementAccountNotificationPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`

```diff

-624.2.3.0.0
-  __TEXT.__text: 0x1cd8
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2bd
-  __TEXT.__objc_classname: 0x218
-  __TEXT.__objc_methname: 0x75f
-  __TEXT.__objc_methtype: 0x217
-  __TEXT.__oslogstring: 0x12d
-  __TEXT.__unwind_info: 0x140
+624.40.12.0.0
+  __TEXT.__text: 0x2238
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x474
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x309
+  __TEXT.__objc_classname: 0x2d5
+  __TEXT.__objc_methname: 0xa25
+  __TEXT.__objc_methtype: 0x2d8
+  __TEXT.__oslogstring: 0x158
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__cfstring: 0x160
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x138
-  __DATA.__objc_const: 0x788
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x148
+  __DATA.__objc_const: 0xb58
+  __DATA.__objc_selrefs: 0x2f8
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x3c0
+  __DATA.__data: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
+  - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DataAccess.framework/DataAccess
   - /System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP
   - /System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP

   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 65
-  Symbols:   100
-  CStrings:  144
+  Functions: 80
+  Symbols:   114
+  CStrings:  183
 
Symbols:
+ _OBJC_CLASS_$_DMCDeviceEligibility
+ _OBJC_CLASS_$_RMAccountStatusHandlerSignificanceEvaluator
+ _OBJC_CLASS_$_RMDarwinNotificationPoster
+ _OBJC_CLASS_$_RMUserAccountTypeChecker
+ _OBJC_METACLASS_$_RMAccountStatusHandlerSignificanceEvaluator
+ _OBJC_METACLASS_$_RMDarwinNotificationPoster
+ _OBJC_METACLASS_$_RMUserAccountTypeChecker
+ _RMModelStatusAccountListExchange_ProtocolType_EAS
+ _objc_msgSendSuper2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_storeStrong
CStrings:
+ ".cxx_destruct"
+ "@\"<RMAccountChangeSignificanceEvaluating>\""
+ "@\"<RMAccountNotificationPosting>\""
+ "@\"<RMUserAccountTypeChecking>\""
+ "@40@0:8@16@24@32"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@\"ACAccount\"16@\"ACAccount\"24"
+ "RMAccountChangeSignificanceEvaluating"
+ "RMAccountNotificationPosting"
+ "RMAccountStatusHandlerSignificanceEvaluator"
+ "RMDarwinNotificationPoster"
+ "RMUserAccountTypeChecker"
+ "RMUserAccountTypeChecking"
+ "T@\"<RMAccountChangeSignificanceEvaluating>\",&,N,V_significanceEvaluator"
+ "T@\"<RMAccountNotificationPosting>\",&,N,V_notifier"
+ "T@\"<RMUserAccountTypeChecking>\",&,N,V_userAccountTypeChecker"
+ "User account %{public}@ of type %{public}@"
+ "_notifier"
+ "_sendUserAccountChangeNotificationIfNeededForAccount:oldAccount:changeType:"
+ "_significanceEvaluator"
+ "_userAccountTypeChecker"
+ "accountType"
+ "added"
+ "changeIsSignificantForAccount:oldAccount:"
+ "com.apple.remotemanagement.status.user-account.notification"
+ "containsObject:"
+ "init"
+ "initWithNotifier:userAccountTypeChecker:significanceEvaluator:"
+ "isUserAccountType:"
+ "notifier"
+ "postAccountStatusDidChangeNotification"
+ "postUserAccountDidChangeNotification"
+ "removed"
+ "setNotifier:"
+ "setSignificanceEvaluator:"
+ "setStatusProtocolType:"
+ "setUserAccountTypeChecker:"
+ "significanceEvaluator"
+ "userAccountTypeChecker"
+ "userAccountTypeIdentifiersForNoninteractiveEnhancedLogCollection"
+ "v24@0:8@16"
- "_changeIsSignificantForAccount:oldAccount:"
- "_postNotification"
```
