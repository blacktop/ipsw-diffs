## videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

-561.40.17.0.0
-  __TEXT.__text: 0xa678
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x1f00
-  __TEXT.__objc_methlist: 0x640
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x300
-  __TEXT.__objc_methname: 0x1d80
-  __TEXT.__oslogstring: 0x10b3
-  __TEXT.__cstring: 0x6c0
+587.0.0.0.0
+  __TEXT.__text: 0xb26c
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methlist: 0x6c0
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x2d8
+  __TEXT.__objc_methname: 0x1f56
+  __TEXT.__oslogstring: 0x11ec
+  __TEXT.__cstring: 0x6d2
   __TEXT.__objc_classname: 0xc3
-  __TEXT.__objc_methtype: 0x513
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x220
+  __TEXT.__objc_methtype: 0x5ab
+  __TEXT.__unwind_info: 0x308
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xb20
-  __DATA.__objc_selrefs: 0x900
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0xb10
+  __DATA.__objc_selrefs: 0x978
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
-  - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5F684B8-18BD-36F0-88FE-775E6D485AC1
-  Functions: 209
-  Symbols:   163
-  CStrings:  559
+  UUID: BC4734D1-B4FF-3224-A470-F4924034D6BE
+  Functions: 232
+  Symbols:   167
+  CStrings:  580
 
Symbols:
+ _AMSAccountMediaTypeAppStoreBeta
+ _AMSAccountMediaTypeAppStoreSandbox
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_AMSDeveloperSilentAuthTokenConsentTask
+ _OBJC_CLASS_$_AMSDeveloperSilentAuthTokenFetchTask
+ _OBJC_CLASS_$_AMSDeveloperSilentAuthTokenUpdateTask
+ _OBJC_CLASS_$_AMSEphemeralDefaults
+ _OBJC_CLASS_$_VSAutoSignInToken
- _OBJC_CLASS_$_WLKChannelManager
- _OBJC_CLASS_$_WLKSettingsStore
- _WLKSettingsDidChangeNotification
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "("
+ "Failed to authorize auto sign in token. {bundleIdentifier=%{public}@, error=%@}"
+ "Failed to delete auto sign in token. {bundleIdentifier=%{public}@, error=%@}"
+ "Failed to fetch auto sign in token. {bundleIdentifier=%{public}@, error=%@}"
+ "Failed to update auto sign in token. {bundleIdentifier=%{public}@, error=%@}"
+ "Invalid For Auto Sign In - Entitlement Not Found"
+ "Invalid For Auto Sign In - Missing Bundle Identifier"
+ "Invalid For Auto Sign In - No Account"
+ "Successfully deleted auto sign in token. {bundleIdentifier=%{public}@}"
+ "Successfully updated auto sign in token. {bundleIdentifier=%{public}@}"
+ "_accountForAutoSignInWithClientAccountType:"
+ "_amsAccountStoreForAccountType:"
+ "_isAccountValidForAutoSignIn:"
+ "_isClientValidForAutoSignInForCurrentTask"
+ "_isValidForAutoSignInForCurrentTaskWithAccount:"
+ "_queryAutoSignInTokenWithAccount:bundleIdentifier:completion:"
+ "ams_activeiTunesAccount"
+ "ams_isLocalAccount"
+ "ams_sharedAccountStore"
+ "ams_sharedAccountStoreForMediaType:"
+ "consentStatus"
+ "deleteAutoSignInTokenWithClientAccountType:completion:"
+ "hasConsented"
+ "initWithAuthorization:value:"
+ "initWithBundleId:account:bag:"
+ "perform"
+ "performPresentation"
+ "performWithToken:"
+ "queryAutoSignInTokenWithClientAccountType:completion:"
+ "requestAutoSignInAuthorizationWithClientAccountType:completion:"
+ "resultWithCompletion:"
+ "setSuppressEngagement:"
+ "token"
+ "updateAutoSignInToken:clientAccountType:completion:"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"AMSDeveloperSilentAuthToken\"8@\"NSError\"16"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v32@0:8q16@?<v@?@\"VSAutoSignInToken\"@\"NSError\">24"
+ "v32@0:8q16@?<v@?q@\"NSError\">24"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16q24@?32"
- ")"
- "@\"WLKSettingsStore\""
- "Consented Bundle IDs: %@"
- "Could not fetch VPPA-Consented and Connected bundleIDs: %@"
- "Failed to delete signed out non-connected user account: %@ - error: %@"
- "Removing Signed Out User Account that is Not Connected: %@"
- "T@\"WLKSettingsStore\",&,N,V_sharedSettingsStore"
- "TV app settings changed, removing any disconnected user accounts"
- "_removeNonConnectedSignedOutUserAccounts"
- "_sharedSettingsStore"
- "addObserverForName:object:queue:usingBlock:"
- "containsObject:"
- "defaultChannelManager"
- "mainQueue"
- "setSharedSettingsStore:"
- "sharedSettings"
- "sharedSettingsStore"
- "v16@?0@\"NSNotification\"8"
- "v24@?0@\"NSSet\"8@\"NSError\"16"
- "vppaConsentedBundleIDsWithCompletion:"

```
