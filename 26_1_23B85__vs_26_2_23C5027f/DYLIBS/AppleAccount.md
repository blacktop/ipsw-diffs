## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1037.125.6.0.0
-  __TEXT.__text: 0xe9590
+1037.250.1.0.0
+  __TEXT.__text: 0xeb568
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xad94
-  __TEXT.__cstring: 0xee6c
+  __TEXT.__objc_methlist: 0xae84
   __TEXT.__const: 0x23e0
-  __TEXT.__gcc_except_tab: 0x249c
-  __TEXT.__oslogstring: 0xfcbd
+  __TEXT.__gcc_except_tab: 0x24cc
+  __TEXT.__oslogstring: 0xff6d
+  __TEXT.__cstring: 0xf1dc
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_typeref: 0x2ed

   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2f08
+  __TEXT.__unwind_info: 0x2f80
   __TEXT.__eh_frame: 0x3e8
-  __TEXT.__objc_classname: 0x1fae
-  __TEXT.__objc_methname: 0x158d2
-  __TEXT.__objc_methtype: 0x304f
-  __TEXT.__objc_stubs: 0xc140
+  __TEXT.__objc_classname: 0x1fc6
+  __TEXT.__objc_methname: 0x15c28
+  __TEXT.__objc_methtype: 0x30a0
+  __TEXT.__objc_stubs: 0xc380
   __DATA_CONST.__got: 0xd88
-  __DATA_CONST.__const: 0x3a78
-  __DATA_CONST.__objc_classlist: 0x7f0
+  __DATA_CONST.__const: 0x3aa8
+  __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4df0
+  __DATA_CONST.__objc_selrefs: 0x4e98
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x7160
-  __AUTH_CONST.__cfstring: 0xccc0
-  __AUTH_CONST.__objc_const: 0x237b8
+  __AUTH_CONST.__cfstring: 0xcee0
+  __AUTH_CONST.__objc_const: 0x23888
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0xb88
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0xba4
-  __DATA.__data: 0x1a50
-  __DATA.__bss: 0x1080
+  __AUTH.__objc_data: 0xbd8
+  __AUTH.__data: 0x1d8
+  __DATA.__objc_ivar: 0xba8
+  __DATA.__data: 0x1a80
+  __DATA.__bss: 0x10a0
   __DATA.__common: 0x91
   __DATA_DIRTY.__objc_data: 0x4600
   __DATA_DIRTY.__data: 0x90

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C3066B97-7CC3-3BAF-8C3E-0D972C64BC07
-  Functions: 4895
-  Symbols:   16181
-  CStrings:  8906
+  UUID: 34F27072-1982-387F-904A-FA0BB97F7B05
+  Functions: 4939
+  Symbols:   16320
+  CStrings:  8991
 
Symbols:
+ -[AAPrivacyConsentManager .cxx_destruct]
+ -[AAPrivacyConsentManager accountManager]
+ -[AAPrivacyConsentManager createAuthenticationController]
+ -[AAPrivacyConsentManager createConsentConfigurationWithVersion:]
+ -[AAPrivacyConsentManager createOBBundleWithError:]
+ -[AAPrivacyConsentManager createOBBundleWithError:].cold.1
+ -[AAPrivacyConsentManager createOBBundleWithError:].cold.2
+ -[AAPrivacyConsentManager createOBPrivacyFlowWithBundle:error:]
+ -[AAPrivacyConsentManager createOBPrivacyFlowWithBundle:error:].cold.1
+ -[AAPrivacyConsentManager extractVersionFromFlow:error:]
+ -[AAPrivacyConsentManager extractVersionFromFlow:error:].cold.1
+ -[AAPrivacyConsentManager getConsentStatusForAccount:completion:]
+ -[AAPrivacyConsentManager getConsentStatusForAccount:completion:].cold.1
+ -[AAPrivacyConsentManager getCurrentConsentVersionWithError:]
+ -[AAPrivacyConsentManager getStoredConsentVersionForAccount:]
+ -[AAPrivacyConsentManager getStoredConsentVersionForAccount:].cold.1
+ -[AAPrivacyConsentManager initWithAccountManager:]
+ -[AAPrivacyConsentManager init]
+ -[AAPrivacyConsentManager performConsentUpdateWithController:configInfo:altDSID:completion:]
+ -[AAPrivacyConsentManager recordConsentAcknowledgmentForAccount:completion:]
+ -[AAPrivacyConsentManager recordConsentAcknowledgmentForAccount:completion:].cold.1
+ -[AAPrivacyConsentManager setAccountManager:]
+ -[AAPrivacyConsentManager shouldPresentConsentForAccount:currentVersion:storedVersion:error:]
+ -[AAPrivacyConsentManager shouldPresentConsentUIForAccount:completion:]
+ -[AAPrivacyConsentManager shouldPresentConsentUIForAccount:completion:].cold.1
+ -[AAPrivacyConsentManager updateIdMSConsentVersion:forAccount:completion:]
+ -[AAPrivacyConsentManager updateLocalConsentVersion:forAccount:]
+ -[AAPrivacyConsentManager updateLocalConsentVersion:forAccount:].cold.1
+ -[AAPrivacyConsentManager updateLocalConsentVersion:forAccount:].cold.2
+ _AAPrivacyConsentErrorDomain
+ _OBJC_CLASS_$_AAPrivacyConsentManager
+ _OBJC_IVAR_$_AAPrivacyConsentManager._accountManager
+ _OBJC_METACLASS_$_AAPrivacyConsentManager
+ _OnBoardingKitLibrary
+ _OnBoardingKitLibrary.cold.1
+ _OnBoardingKitLibraryCore
+ _OnBoardingKitLibraryCore.frameworkLibrary
+ __OBJC_$_INSTANCE_METHODS_AAPrivacyConsentManager
+ __OBJC_$_INSTANCE_VARIABLES_AAPrivacyConsentManager
+ __OBJC_$_PROP_LIST_AAPrivacyConsentManager
+ __OBJC_CLASS_RO_$_AAPrivacyConsentManager
+ __OBJC_METACLASS_RO_$_AAPrivacyConsentManager
+ ___76-[AAPrivacyConsentManager recordConsentAcknowledgmentForAccount:completion:]_block_invoke
+ ___76-[AAPrivacyConsentManager recordConsentAcknowledgmentForAccount:completion:]_block_invoke.cold.1
+ ___92-[AAPrivacyConsentManager performConsentUpdateWithController:configInfo:altDSID:completion:]_block_invoke
+ ___92-[AAPrivacyConsentManager performConsentUpdateWithController:configInfo:altDSID:completion:]_block_invoke.cold.1
+ ___OnBoardingKitLibraryCore_block_invoke
+ ___getOBBundleClass_block_invoke
+ ___getOBBundleClass_block_invoke.cold.1
+ ___getOBPrivacyFlowClass_block_invoke
+ ___getOBPrivacyFlowClass_block_invoke.cold.1
+ _getOBBundleClass
+ _getOBBundleClass.softClass
+ _getOBPrivacyFlowClass
+ _getOBPrivacyFlowClass.softClass
+ _objc_msgSend$accountManager
+ _objc_msgSend$appleAccountConsentVersionForAccount:
+ _objc_msgSend$authKitAccountWithAltDSID:error:
+ _objc_msgSend$createAuthenticationController
+ _objc_msgSend$createConsentConfigurationWithVersion:
+ _objc_msgSend$createOBBundleWithError:
+ _objc_msgSend$createOBPrivacyFlowWithBundle:error:
+ _objc_msgSend$extractVersionFromFlow:error:
+ _objc_msgSend$flowWithBundle:
+ _objc_msgSend$getCurrentConsentVersionWithError:
+ _objc_msgSend$getStoredConsentVersionForAccount:
+ _objc_msgSend$initWithAccountManager:
+ _objc_msgSend$performConsentUpdateWithController:configInfo:altDSID:completion:
+ _objc_msgSend$setAppleAccountConsentVersion:forAccount:error:
+ _objc_msgSend$setConfigurationInfo:forIdentifier:forAltDSID:completion:
+ _objc_msgSend$shouldPresentConsentForAccount:currentVersion:storedVersion:error:
+ _objc_msgSend$updateIdMSConsentVersion:forAccount:completion:
+ _objc_msgSend$updateLocalConsentVersion:forAccount:
CStrings:
+ "/AppleInternal/Library/Frameworks/OnBoardingKit.framework/OnBoardingKit"
+ "/System/AppleInternal/Library/Frameworks/OnBoardingKit.framework/OnBoardingKit"
+ "/System/Library/Frameworks/OnBoardingKit.framework/OnBoardingKit"
+ "/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit"
+ "@\"AKAccountManager\""
+ "AAOBKitSoftLinks.m"
+ "AAPrivacyConsentErrorDomain"
+ "AAPrivacyConsentManager"
+ "Account parameter cannot be nil"
+ "Apple Account missing or invalid altDSID"
+ "B48@0:8@16^q24^q32^@40"
+ "Class getOBBundleClass(void)_block_invoke"
+ "Class getOBPrivacyFlowClass(void)_block_invoke"
+ "Consent decision: currentVersion=%ld, storedVersion=%ld, should present=%@"
+ "Error checking consent eligibility: %@"
+ "Error getting consent status: %@"
+ "Error recording consent acknowledgment: %@"
+ "Error when fetching the IdMS account with error=%@"
+ "Failed to create OBBundle"
+ "Failed to create OBBundle with identifier: %@"
+ "Failed to create OBPrivacyFlow"
+ "Failed to create OBPrivacyFlow with bundle"
+ "Failed to initialize AK client"
+ "Failed to set privacy consent for altDSID: %{private}@, error: %@"
+ "Failed to update local consent version: %@"
+ "IdMS update failed: %@"
+ "NIL"
+ "OBBundle"
+ "OBKit privacy flow contentVersion is 0"
+ "OBKit privacy flow contentVersion is 0, skipping consent UI"
+ "OBPrivacyFlow"
+ "OnBoardingKit classes not available"
+ "OnBoardingKit classes not available - bundleClass=%@, flowClass=%@"
+ "Privacy consent successfully set for altDSID: %{private}@"
+ "Successfully updated local consent version to %ld"
+ "T@\"AKAccountManager\",&,N,V_accountManager"
+ "Unknown error"
+ "X-Apple-I-PrivacyConsent-Value"
+ "X-Apple-I-PrivacyConsent-Version"
+ "accountManager"
+ "appleAccountConsentVersionForAccount:"
+ "authKitAccountWithAltDSID:error:"
+ "com.apple.idms.config.privacy.appleid.consent"
+ "com.apple.onboarding.appleid"
+ "contentVersion"
+ "createAuthenticationController"
+ "createConsentConfigurationWithVersion:"
+ "createOBBundleWithError:"
+ "createOBPrivacyFlowWithBundle:error:"
+ "extractVersionFromFlow:error:"
+ "flowWithBundle:"
+ "getConsentStatusForAccount:completion:"
+ "getCurrentConsentVersionWithError:"
+ "getStoredConsentVersionForAccount:"
+ "performConsentUpdateWithController:configInfo:altDSID:completion:"
+ "q24@0:8@16"
+ "q24@0:8^@16"
+ "q32@0:8@16^@24"
+ "recordConsentAcknowledgmentForAccount:completion:"
+ "setAccountManager:"
+ "setAppleAccountConsentVersion:forAccount:error:"
+ "setConfigurationInfo:forIdentifier:forAltDSID:completion:"
+ "shouldPresentConsentForAccount:currentVersion:storedVersion:error:"
+ "shouldPresentConsentUIForAccount:completion:"
+ "updateIdMSConsentVersion:forAccount:completion:"
+ "updateLocalConsentVersion:forAccount:"
+ "void *OnBoardingKitLibrary(void)"

```
