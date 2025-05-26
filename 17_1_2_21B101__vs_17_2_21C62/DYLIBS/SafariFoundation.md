## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x1b8d4
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x15a8
+617.1.17.10.9
+  __TEXT.__text: 0x1c7dc
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x15e8
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xb3c
-  __TEXT.__cstring: 0x1f00
-  __TEXT.__oslogstring: 0xd66
+  __TEXT.__gcc_except_tab: 0xbd8
+  __TEXT.__cstring: 0x2049
+  __TEXT.__oslogstring: 0xd82
   __TEXT.__ustring: 0xb8
   __TEXT.__dlopen_cstrs: 0x156
-  __TEXT.__unwind_info: 0xa44
+  __TEXT.__unwind_info: 0xa84
   __TEXT.__objc_classname: 0x44a
-  __TEXT.__objc_methname: 0x5cdd
-  __TEXT.__objc_methtype: 0xa14
-  __TEXT.__objc_stubs: 0x3ce0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xde0
+  __TEXT.__objc_methname: 0x5e4d
+  __TEXT.__objc_methtype: 0xa50
+  __TEXT.__objc_stubs: 0x3dc0
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0xea0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2338
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x3a8
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x278
   __DATA.__objc_superrefs: 0xb0
   __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x380
   __DATA.__bss: 0xa4
-  __DATA_DIRTY.__const: 0x2c0
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0xc58
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 699
-  Symbols:   2750
-  CStrings:  1267
+  Functions: 717
+  Symbols:   2798
+  CStrings:  1283
 
Symbols:
+ -[SFAppAutoFillOneTimeCodeProvider _consumeOneTimeCode:]
+ -[SFAppAutoFillOneTimeCodeProvider _domainBindingForRecievedOneTimeCode:forAppWithIdentifier:websiteURL:hasDomainBinding:]
+ -[SFAppAutoFillOneTimeCodeProvider _domainBindingForRecievedOneTimeCode:forAppWithIdentifier:websiteURL:hasDomainBinding:].cold.1
+ -[SFAppAutoFillOneTimeCodeProvider _mostRecentlyReceivedOneTimeCode]
+ -[SFAppAutoFillOneTimeCodeProvider _processReceivedOneTimeCode:fromSource:]
+ -[SFAppAutoFillOneTimeCodeProvider _url:matchesURLFromOriginBoundCode:]
+ -[SFAppAutoFillOneTimeCodeProvider _validateCurrentOneTimeCodes]
+ -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAuditToken:website:usernameHint:fieldClassification:].cold.1
+ -[SFAppAutoFillOneTimeCodeProvider initWithOptions:]
+ -[SFAppAutoFillOneTimeCodeProvider test_deliverOneTimeCode:fromSource:]
+ -[SFAutoFillFeatureManager isAutoFillFromKeychainRestricted]
+ -[SFCredentialProviderExtensionState initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:]
+ _OBJC_IVAR_$_SFAppAutoFillOneTimeCodeProvider._currentReceivedOneTimeCodesBySource
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.55
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke_2.56
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke_3
+ ___119-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:inContext:]_block_invoke_2
+ ___119-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:inContext:]_block_invoke_3
+ ___122-[SFAppAutoFillOneTimeCodeProvider _domainBindingForRecievedOneTimeCode:forAppWithIdentifier:websiteURL:hasDomainBinding:]_block_invoke
+ ___52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke
+ ___52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke_2
+ ___52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke_3
+ ___52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke_4
+ ___55-[SFAppAutoFillOneTimeCodeProvider consumeOneTimeCode:]_block_invoke
+ ___61-[SFAppAutoFillOneTimeCodeProvider consumeCurrentOneTimeCode]_block_invoke
+ ___61-[SFAppAutoFillOneTimeCodeProvider consumeCurrentOneTimeCode]_block_invoke_2
+ ___64-[SFAppAutoFillOneTimeCodeProvider _validateCurrentOneTimeCodes]_block_invoke
+ ___68-[SFAppAutoFillOneTimeCodeProvider _mostRecentlyReceivedOneTimeCode]_block_invoke
+ ___71-[SFAppAutoFillOneTimeCodeProvider consumeMessagesOneTimeCodeWithGUID:]_block_invoke
+ ___block_descriptor_32_e80_"SFAutoFillOneTimeCode"24?0"SFAutoFillOneTimeCode"8"SFAutoFillOneTimeCode"16l
+ ___block_descriptor_40_e8_32s_e48_v32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e57_"WBSPair"32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e71_"SFAutoFillOneTimeCode"32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e68_"NSNumber"24?0"SFSharedWebCredentialsDatabaseEntry"8"NSNumber"16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e57_"WBSPair"32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.102
+ ___block_literal_global.115
+ ___block_literal_global.95
+ __os_activity_initiate
+ _objc_msgSend$_consumeOneTimeCode:
+ _objc_msgSend$_domainBindingForRecievedOneTimeCode:forAppWithIdentifier:websiteURL:hasDomainBinding:
+ _objc_msgSend$_processReceivedOneTimeCode:fromSource:
+ _objc_msgSend$_url:matchesURLFromOriginBoundCode:
+ _objc_msgSend$_validateCurrentOneTimeCodes
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$safari_isEarlierThanDate:
+ _objc_msgSend$safari_isLaterThanDate:
+ _objc_msgSend$safari_mapAndFilterKeysAndObjectsUsingBlock:
+ _objc_msgSend$safari_reduceObjectsUsingBlock:
+ _objc_msgSend$safari_stringByRemovingTopLevelDomainFromHost
+ _objc_msgSend$setExtension:isEnabled:
+ _objc_msgSend$setShouldAutoFillPasswordsFromKeychain:
- -[SFAppAutoFillOneTimeCodeProvider _validateCurrentOneTimeCode]
- -[SFAppAutoFillOneTimeCodeProvider _validateURL:withURLFromOriginBoundCode:]
- -[SFAppAutoFillOneTimeCodeProvider hasOneTimeCodeForAppWithAuditToken:]
- -[SFAppAutoFillOneTimeCodeProvider initWithMessagesOneTimeCodeSupport:]
- GCC_except_table48
- _OBJC_IVAR_$_SFAppAutoFillOneTimeCodeProvider._currentReceivedOneTimeCode
- ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.48
- ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.56
- ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.cold.1
- ___71-[SFAppAutoFillOneTimeCodeProvider initWithMessagesOneTimeCodeSupport:]_block_invoke
- ___71-[SFAppAutoFillOneTimeCodeProvider initWithMessagesOneTimeCodeSupport:]_block_invoke_2
- ___71-[SFAppAutoFillOneTimeCodeProvider initWithMessagesOneTimeCodeSupport:]_block_invoke_3
- ___71-[SFAppAutoFillOneTimeCodeProvider initWithMessagesOneTimeCodeSupport:]_block_invoke_4
- ___block_descriptor_48_e8_32s40s_e45_B16?0"SFSharedWebCredentialsDatabaseEntry"8ls32l8s40l8
- ___block_literal_global.113
- ___block_literal_global.20
- ___block_literal_global.91
- __os_activity_create
- __os_activity_current
- _objc_msgSend$_validateCurrentOneTimeCode
- _objc_msgSend$_validateURL:withURLFromOriginBoundCode:
- _objc_msgSend$consumeOneTimeCode:
- _objc_msgSend$initWithMessagesOneTimeCodeSupport:
- _objc_msgSend$safari_effectiveTopLevelDomainForHost
- _objc_msgSend$substringWithRange:
- _objc_msgSend$timeIntervalSinceNow
- _os_activity_apply
CStrings:
+ "\x03\x14\x11"
+ "%@ is expired; removing from cache"
+ "@\"NSMutableDictionary\""
+ "@\"NSNumber\"24@?0@\"SFSharedWebCredentialsDatabaseEntry\"8@\"NSNumber\"16"
+ "@\"SFAutoFillOneTimeCode\"24@?0@\"SFAutoFillOneTimeCode\"8@\"SFAutoFillOneTimeCode\"16"
+ "@\"SFAutoFillOneTimeCode\"32@?0@\"NSNumber\"8@\"SFAutoFillOneTimeCode\"16^B24"
+ "@\"WBSPair\"32@?0@\"NSNumber\"8@\"SFAutoFillOneTimeCode\"16^B24"
+ "@24@0:8Q16"
+ "@40@0:8B16B20@24@32"
+ "App %@ has web browser entitlement. Checking domain against website URL %{sensitive, mask.hash}@."
+ "App %@ has web browser entitlement. Getting passwords for website URL %{sensitive, mask.hash}@."
+ "Checking domain against associated domains for app %@."
+ "Couldn't get an app identifier for the given audit token"
+ "Current verification code is domain-bound to %{sensitive, mask.hash}@."
+ "Domain-bound verification code is %@valid for app %@."
+ "Missing app identifier. Domain validation is not possible."
+ "Received verification code from Mail: %{sensitive, mask.hash}@ and MessageID: %ld"
+ "Received verification code from Messages: %{sensitive, mask.hash}@"
+ "_consumeOneTimeCode:"
+ "_currentReceivedOneTimeCodesBySource"
+ "_domainBindingForRecievedOneTimeCode:forAppWithIdentifier:websiteURL:hasDomainBinding:"
+ "_mostRecentlyReceivedOneTimeCode"
+ "_processReceivedOneTimeCode:fromSource:"
+ "_url:matchesURLFromOriginBoundCode:"
+ "_validateCurrentOneTimeCodes"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:"
+ "initWithOptions:"
+ "isAutoFillFromKeychainRestricted"
+ "q32@0:8@16@24"
+ "q48@0:8@16@24@32^B40"
+ "safari_isEarlierThanDate:"
+ "safari_isLaterThanDate:"
+ "safari_mapAndFilterKeysAndObjectsUsingBlock:"
+ "safari_reduceObjectsUsingBlock:"
+ "safari_stringByRemovingTopLevelDomainFromHost"
+ "test_deliverOneTimeCode:fromSource:"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSNumber\"8@\"SFAutoFillOneTimeCode\"16^B24"
- "\x02\x15\x11"
- "@20@0:8B16"
- "App %{private}@ has web browser entitlement. Checking domain against website URL %{private}@."
- "App %{sensitive, mask.hash}@ has web browser entitlement. Getting passwords for website URL %{sensitive, mask.hash}@."
- "B32@0:8@16@24"
- "B48@0:8{?=[8I]}16"
- "Checking domain against associated domains for app %{private}@."
- "Current one time code message expired at %{public}@."
- "Current verification code is domain-bound to %{private}@."
- "Domain-bound verification code is %@valid for app %{private}@."
- "Invalid audit token for app. Domain validation is not possible."
- "Received verification code from Mail: %{private}@ and MessageID: %{private}ld"
- "Received verification code from Messages: %{private}@"
- "T@\"NSString\",&,D,N"
- "_currentReceivedOneTimeCode"
- "_validateCurrentOneTimeCode"
- "_validateURL:withURLFromOriginBoundCode:"
- "hasOneTimeCodeForAppWithAuditToken:"
- "initWithMessagesOneTimeCodeSupport:"
- "preferredCredentialProviderForSaving"
- "safari_effectiveTopLevelDomainForHost"
- "substringWithRange:"
- "timeIntervalSinceNow"

```
