## AAGKAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin`

```diff

-1037.575.5.0.0
-  __TEXT.__text: 0xb540
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x4bc
+1059.1.1.0.0
+  __TEXT.__text: 0x9c94
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__cstring: 0x9e8
-  __TEXT.__objc_methname: 0x1a45
-  __TEXT.__oslogstring: 0x1a6f
-  __TEXT.__objc_classname: 0x7e
+  __TEXT.__gcc_except_tab: 0x358
+  __TEXT.__cstring: 0x944
+  __TEXT.__objc_methname: 0x1909
+  __TEXT.__oslogstring: 0x1696
+  __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methtype: 0x645
-  __TEXT.__unwind_info: 0x2e8
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6b8
-  __DATA_CONST.__cfstring: 0x780
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__const: 0x618
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x1e0
   __DATA.__objc_const: 0x4b8
-  __DATA.__objc_selrefs: 0x7c0
+  __DATA.__objc_selrefs: 0x758
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C807CCCB-8FD1-3DC7-BE44-9DC6E52A30B3
-  Functions: 214
-  Symbols:   178
-  CStrings:  589
+  UUID: EFDFF915-77BD-3C66-8BCF-A370E6272640
+  Functions: 190
+  Symbols:   167
+  CStrings:  550
 
Symbols:
+ _OBJC_CLASS_$_AACompanionDeviceHelper
+ _OBJC_CLASS_$_AAGrayModeHelper
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- _CFUserNotificationCancel
- _CFUserNotificationCreate
- _OBJC_CLASS_$_AARequester
- _OBJC_CLASS_$_AAUpdateProvisioningRequest
- _OBJC_CLASS_$_NSBundle
- ___kCFBooleanTrue
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
- "initWithAccount:token:"
- "initWithRequest:handler:"
- "localizedStringForKey:value:table:"
- "remoteDeviceProxy"
- "sendCommand:withAccount:options:completion:"
- "v16@?0@\"AAResponse\"8"
- "v28@?0B8@\"NSObject<NSCoding>\"12@\"NSError\"20"

```
