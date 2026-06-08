## AAIDSAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin`

```diff

-1037.575.5.0.0
-  __TEXT.__text: 0x7b58
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x38c
+1059.1.1.0.0
+  __TEXT.__text: 0x65c8
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x354
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__cstring: 0x5f6
-  __TEXT.__objc_methname: 0x14db
-  __TEXT.__oslogstring: 0x14b8
-  __TEXT.__objc_classname: 0x64
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__cstring: 0x54e
+  __TEXT.__objc_methname: 0x1399
+  __TEXT.__oslogstring: 0x10df
+  __TEXT.__objc_classname: 0x62
   __TEXT.__objc_methtype: 0x58d
-  __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__cfstring: 0x360
+  __TEXT.__unwind_info: 0x1f0
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x208
   __DATA.__objc_const: 0x348
-  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_selrefs: 0x5c0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9591A21-072E-3694-92CB-B80D39DCE49A
-  Functions: 148
-  Symbols:   170
-  CStrings:  413
+  UUID: 673502A1-B73C-36D8-AEB0-A643AB2F7573
+  Functions: 123
+  Symbols:   157
+  CStrings:  372
 
Symbols:
+ _OBJC_CLASS_$_AACompanionDeviceHelper
+ _OBJC_CLASS_$_AAGrayModeHelper
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- _CFRelease
- _CFUserNotificationCancel
- _CFUserNotificationCreate
- _OBJC_CLASS_$_AARequester
- _OBJC_CLASS_$_AAUpdateProvisioningRequest
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSOperationQueue
- ___kCFBooleanTrue
- __dispatch_main_q
- __dispatch_source_type_timer
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _dispatch_time
- _kACIDServiceCommandPromptUser
- _kCFAllocatorDefault
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlertTopMostKey
- _kCFUserNotificationDefaultButtonTitleKey
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "doesRelyOnCompanionAccounts"
+ "getPasswordFromCompanionForAccount:store:options:completion:"
+ "isAccountInGrayMode:"
+ "isAccountReallyInGrayMode:accountStore:completion:"
+ "parametersForProxiedAuthentication"
- ""
- "ACRemoteDeviceProxy reports that renewCredentials succeeded, but no password is in the response!"
- "ACRemoteDeviceProxy reports that renewCredentials succeeded, but response is not a string! %@"
- "ACRemoteDeviceProxy successfully provided us with a password for %@"
- "Asking ACRemoteDeviceProxy to obtain password for account %@ with options: %@"
- "CFUserNotificationCreate in renewCredentials!"
- "Can't get password from companion, told to avoid UI"
- "Dismissing renew-credentials prompt."
- "Failed to encode AKDevice! Proxied auth is doomed."
- "Failed to obtain a password from ACRemoteDeviceProxy for account %@! Error: %@"
- "Failed to save account after marking it as not in gray mode anymore. %@"
- "Got an error, may still be in Gray Mode. %@"
- "Localizable"
- "Make a quick round-trip to the server to see if we really need to accept new terms"
- "PASSWORD_ENTRY_DISMISS_BUTTON"
- "PASSWORD_ENTRY_REQUIRED_MESSAGE"
- "PASSWORD_ENTRY_REQUIRED_TITLE"
- "Server auth was successful, not in Gray Mode anymore"
- "Showing renew-credentials prompt..."
- "Something went wrong and we couldn't contact the server. %@"
- "We timed out waiting on the server"
- "_doesRelyOnCompanionAccounts"
- "_getPasswordFromCompanionForAccount:store:options:completion:"
- "_isAccountInGrayMode:"
- "_isAccountReallyInGrayMode:accountStore:completion:"
- "_parametersForProxiedAuthentication"
- "aa_isSuspended"
- "aa_setNeedsToVerifyTerms:"
- "aa_updateWithProvisioningResponse:"
- "addEntriesFromDictionary:"
- "addOperation:"
- "bundleForClass:"
- "cancelAllOperations"
- "currentDevice"
- "error"
- "initWithAccount:token:"
- "initWithRequest:handler:"
- "localizedStringForKey:value:table:"
- "remoteDeviceProxy"
- "sendCommand:withAccount:options:completion:"
- "v16@?0@\"AAResponse\"8"
- "v28@?0B8@\"NSObject<NSCoding>\"12@\"NSError\"20"

```
