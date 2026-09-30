## iCloud

> `/Applications/iCloud.app/iCloud`

```diff

-2260.10.3.0.0
-  __TEXT.__text: 0x13f84
+2300.138.2.0.0
+  __TEXT.__text: 0x15d58
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x2d20
-  __TEXT.__objc_methlist: 0xe30
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__objc_methname: 0x3cfc
-  __TEXT.__cstring: 0x2680
-  __TEXT.__oslogstring: 0x19e1
+  __TEXT.__objc_stubs: 0x3100
+  __TEXT.__objc_methlist: 0xf18
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x6c4
+  __TEXT.__objc_methname: 0x40c0
+  __TEXT.__cstring: 0x2953
+  __TEXT.__oslogstring: 0x1bad
   __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methtype: 0xd51
-  __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__objc_methtype: 0xd94
+  __TEXT.__ustring: 0xc
+  __TEXT.__unwind_info: 0x408
   __DATA_CONST.__auth_got: 0x2e8
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x650
-  __DATA_CONST.__cfstring: 0x1e60
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__cfstring: 0x2020
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xf90
-  __DATA.__objc_selrefs: 0xe40
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_const: 0xff0
+  __DATA.__objc_selrefs: 0xf38
+  __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x180
   __DATA.__bss: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42BB0E71-B99A-3E86-9262-C3A489555EA9
-  Functions: 263
-  Symbols:   217
-  CStrings:  1310
+  UUID: F85A12C8-3B6E-3AA7-ACA1-440228F64E97
+  Functions: 286
+  Symbols:   219
+  CStrings:  1384
 
Symbols:
+ _CKPhotosSharedCollectionsShareType
+ _OBJC_CLASS_$_CKPersona
+ _OBJC_CLASS_$_NSPredicate
+ _kCKPhotosSharedCollectionsShareURLSlug
+ _objc_retain_x4
- _ACAccountPropertyPersonaIdentifier
- _ACAccountTypeIdentifierAppleAccount
- _CKAdoptPersonaID
CStrings:
+ "@\"ACAccount\""
+ "ASK_OWNER_TO_SHARE"
+ "B24@0:8^B16"
+ "CKBladerunnerShareURLSlugBasedVettingKeySuffix"
+ "CLOUDKIT_VETTING_ACCESS_CANT_SEND_REQUEST_TITLE"
+ "CLOUDKIT_VETTING_ACCESS_REQUEST_SENT_MESSAGE"
+ "CLOUDKIT_VETTING_ACCESS_REQUEST_SENT_TITLE"
+ "CLOUDKIT_VETTING_ACCESS_TRY_AGAIN_LATER"
+ "Failed to adopt persona %@ with error: %@"
+ "Fallback flow: Share cannot be accepted by the account, due to: %@"
+ "Got a nil vettingKeySuffix for URL: %@"
+ "ITEM_UNAVAILABLE_FAILURE_ALERT_BODY_EMAIL"
+ "ITEM_UNAVAILABLE_REQUEST_ACCESS_BODY_%@"
+ "ITEM_UNAVAILABLE_UNPROVISIONED_DATACLASS_ALERT_BODY"
+ "No primary iCloud account is signed in."
+ "SELF MATCHES %@"
+ "SEND_REQUEST"
+ "Selected account is not provisioned for the underlying dataclass."
+ "Share access request for share %@ completed with error: %@"
+ "Share cannot be accepted by the selected account with unprovisioned dataclass for sharing URL: %@"
+ "ShareAcceptorStateFallbackShareAccessRequest"
+ "ShareAcceptorStateFallbackWarnUnprovisionedDataclass"
+ "SharedCollections"
+ "T@\"ACAccount\",C,N,V_selectedAccount"
+ "T@\"NSString\",C,N,V_failedAccountEmail"
+ "Unable to request access to share %@ because the device has no primary Apple account."
+ "User cancelled request access flow."
+ "User cancelled request‐access flow for share URL %@"
+ "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}"
+ "[Share] showRequestAccess=%@ (callingParticipant=%@, accessRequestsEnabled=%@, outOfNetworkMatches=%@, primaryAccountSupportsShareAccess=%@, forced=%@)"
+ "_actuallyRequestAccessWithCompletion:"
+ "_checkDataclassEnabledAndProvisioned:"
+ "_checkRepresentativeDataclassEnabled:"
+ "_failedAccountEmail"
+ "_fallbackFlowShareAccessRequest:"
+ "_fallbackFlowWarnUnprovisionedDataclass:"
+ "_getContainerForAccountID:"
+ "_selectedAccount"
+ "aa_appleAccounts"
+ "aa_formattedUsername"
+ "aa_isManagedAppleID"
+ "aa_primaryAppleAccount"
+ "aa_primaryEmail"
+ "accessRequestsEnabled"
+ "adopt:"
+ "alertContentForRequestAccessConfirmation"
+ "alertContentForRequestAccessFailure"
+ "alertContentForRequestAccessWithHandle:"
+ "alertContentForShareMetadataErrorWithURL:email:"
+ "alertContentForUnprovisionedDataclassWithURL:email:"
+ "alwaysShowShareAccessRequestUI"
+ "callingParticipant"
+ "ckShortDescription"
+ "ck_getPersona:error:"
+ "dictionaryWithDictionary:"
+ "evaluateWithObject:"
+ "failedAccountEmail"
+ "isCKAuthenticationUserCancelled"
+ "isCKVettedToSelfError"
+ "isEmail:"
+ "isSupported"
+ "predicateWithFormat:"
+ "primaryAppleAccount"
+ "q20@0:8B16"
+ "representativeDataclass"
+ "requestAccessToShareURLs:completionHandler:"
+ "selectedAccount"
+ "setFailedAccountEmail:"
+ "setSelectedAccount:"
+ "settings-navigation://com.apple.Settings"
+ "settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE"
+ "shouldShowRequestAccess"
+ "showAlertWithContent:isSourceICS:additionalOptions:responseHandler:"
+ "showICloudAccountSettingAlert:appName:previewRequested:isSourceICS:maid:"
+ "showRequestAccessAlert:isSourceICS:requestAccessHandler:cancelHandler:"
+ "showRequestAccessResultAlert:isSourceICS:"
+ "v12@?0i8"
+ "v44@0:8@16B24@28@?36"
+ "v44@0:8@16B24@?28@?36"
+ "v48@0:8@16@24^B32B40B44"
+ "\xfc\xff"
+ "\xfd\xff"
- "CKBladerunnerShareURLSlugBasedApplicationBundleID"
- "Error while querying if our dataclass is enabled"
- "Got nil bundle id for URL: %@"
- "_checkDataclassError:"
- "_checkRepresentativeDataclassEnabled:appCandidatesPresent:"
- "accountPropertyForKey:"
- "accountTypeWithAccountTypeIdentifier:"
- "accountWithIdentifier:"
- "alertContentForShareMetadataErrorWithURL:"
- "com.apple.Keynote"
- "com.apple.Numbers"
- "com.apple.Pages"
- "isAuthenticationUserCancelled"
- "isVettedToSelfError"
- "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE"
- "q28@0:8^@16B24"
- "representativeDataclassEnabledWithCompletionHandler:"
- "showICloudAccountSettingAlert:appName:previewRequested:isSourceICS:"
- "v20@?0B8@\"NSError\"12"
- "v44@0:8@16@24^B32B40"

```
