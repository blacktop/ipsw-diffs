## DADaemonCalDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x1419c
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x4000
-  __TEXT.__objc_methlist: 0x1224
+2690.0.0.0.0
+  __TEXT.__text: 0x15058
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x4240
+  __TEXT.__objc_methlist: 0x1324
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x96c
-  __TEXT.__objc_methname: 0x496f
-  __TEXT.__oslogstring: 0x245f
-  __TEXT.__cstring: 0x864
-  __TEXT.__objc_classname: 0x3c0
-  __TEXT.__objc_methtype: 0xaed
-  __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__auth_got: 0x3b8
+  __TEXT.__gcc_except_tab: 0x988
+  __TEXT.__objc_methname: 0x4b50
+  __TEXT.__oslogstring: 0x2579
+  __TEXT.__cstring: 0x87f
+  __TEXT.__objc_classname: 0x3f1
+  __TEXT.__objc_methtype: 0xb00
+  __TEXT.__unwind_info: 0x598
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__const: 0x520
-  __DATA_CONST.__cfstring: 0x900
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA.__objc_const: 0x2ae8
-  __DATA.__objc_selrefs: 0x1440
+  __DATA.__objc_const: 0x2d18
+  __DATA.__objc_selrefs: 0x14b0
   __DATA.__objc_ivar: 0x198
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x21
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2637F83-8FDD-33F2-9FBD-258276B85C2C
-  Functions: 330
+  UUID: B85A2447-F336-3ADF-92F8-9C259974A281
+  Functions: 348
   Symbols:   284
-  CStrings:  1207
+  CStrings:  1237
 
Symbols:
+ _OBJC_CLASS_$_ACAccount
+ _OBJC_CLASS_$_MobileCalDAVDAAccount
+ _OBJC_CLASS_$_MobileCalDAVDADaemonAccount
+ _OBJC_CLASS_$_MobileCalDAViCloudDADaemonAccount
+ _OBJC_METACLASS_$_MobileCalDAVDAAccount
+ _OBJC_METACLASS_$_MobileCalDAVDADaemonAccount
+ _OBJC_METACLASS_$_MobileCalDAViCloudDADaemonAccount
+ _kAccountAuthenticationTypeParent
- OBJC_IVAR_$_DAAccount._taskManager
- _CalStoreAllowsCalendarAddDeleteModify
- _CalStoreIsFacebook
- _CalStoreSetAllowsCalendarAddDeleteModify
- _CalStoreSetIsFacebook
- _OBJC_CLASS_$_CalDAVDBHelper
- _OBJC_CLASS_$_MobileCalDAVFacebookDaemonAccount
- _OBJC_METACLASS_$_MobileCalDAVFacebookDaemonAccount
CStrings:
+ "@\"MobileCalDAVDADaemonAccount\""
+ "Account \"%@\" (%{public}@) was told to refresh, but it has terms and conditions that have not been accepted for account. Skipping refresh."
+ "CompatibilityShims"
+ "Delegate with account ID %@ failed to be removed"
+ "Delegate with account ID %@ was successfully removed"
+ "Expected an ACAccount"
+ "MobileCalDAVDADaemonAccount"
+ "MobileCalDAVDADaemonAccount %p going away"
+ "MobileCalDAVDADaemonAccount.m"
+ "MobileCalDAViCloudDADaemonAccount"
+ "T@\"ACAccount\",R,N"
+ "T@\"MobileCalDAVDADaemonAccount\",R,D,N"
+ "T@\"MobileCalDAVDADaemonAccount\",R,W,N,V_account"
+ "T@\"MobileCalDAVDaemonAccount\",R,D,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSSet\",R,N"
+ "T@\"NSString\",R,N"
+ "TB,?,R,N"
+ "Tq,?,R,N"
+ "_shareResponseIsGoingAway"
+ "accountInfo"
+ "accountTypeWithAccountTypeIdentifier:"
+ "backingAccount"
+ "childAccountsWithAccountTypeIdentifier:"
+ "contextDictionary"
+ "createChildAccountWithAccountTypeIdentifier:"
+ "daAccount"
+ "dbHelper"
+ "initWithAccountType:"
+ "initWithBackingAccount:"
+ "mobileCalDAVAccount"
+ "mobileCalDAVAccountClass"
+ "needsToVerifyTerms"
+ "refreshWithContext:completion:"
+ "removeAccount:"
+ "removeAccount:withDeleteSync:completion:"
+ "setActive:"
+ "setAuthenticationType:"
+ "setParentAccount:"
- "B24@0:8^v16"
- "MobileCalDAVFacebookDaemonAccount"
- "T@\"MobileCalDAVDaemonAccount\",R,W,N,V_account"
- "_updateCalendarStoreProperties:"
- "refreshWithContext:"
- "setAccountProperty:forKey:"
- "shareResponseIsGoingAway:"
- "sharedInstance"
- "useThunderhillBetaServers"
- "webdav.beta.facebook.com"

```
