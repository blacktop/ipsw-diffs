## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3402.53.1.1.3
-  __TEXT.__text: 0x619d4
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x3024
+3402.62.2.1.1
+  __TEXT.__text: 0x6258c
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x30e0
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x10f4
-  __TEXT.__cstring: 0x9314
-  __TEXT.__oslogstring: 0xa83c
+  __TEXT.__gcc_except_tab: 0x1084
+  __TEXT.__cstring: 0x948e
+  __TEXT.__oslogstring: 0xab88
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0x1050
+  __TEXT.__unwind_info: 0x10d8
   __TEXT.__objc_classname: 0x411
-  __TEXT.__objc_methname: 0x96e3
+  __TEXT.__objc_methname: 0x98bb
   __TEXT.__objc_methtype: 0xeac
-  __TEXT.__objc_stubs: 0x7a00
+  __TEXT.__objc_stubs: 0x7b20
   __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x19c8
+  __DATA_CONST.__const: 0x1a18
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_selrefs: 0x24e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x3de0
-  __AUTH_CONST.__objc_const: 0x4460
+  __AUTH_CONST.__cfstring: 0x3e60
+  __AUTH_CONST.__objc_const: 0x44b0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x230
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xcd0
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA_DIRTY.__bss: 0x2e0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1339
-  Symbols:   1925
-  CStrings:  3396
+  Functions: 1354
+  Symbols:   1939
+  CStrings:  3436
 
Symbols:
- _CFPreferencesCopyAppValue
CStrings:
+ "\x03\x12"
+ "%!s(MISSING) #settings NO returned for UOD"
+ "%!s(MISSING) #settings siriUODAvailabilityDidChange delegate available:%!d(MISSING)"
+ "%!s(MISSING) %!{(MISSING)public}@: No '%!{(MISSING)public}@' asset in asset set"
+ "%!s(MISSING) Altered auto asset set %!{(MISSING)public}@ with type %!{(MISSING)public}@ with expensive cellular: %!d(MISSING) and specifiers %!{(MISSING)public}@"
+ "%!s(MISSING) Assistant Subscription not allowed"
+ "%!s(MISSING) Assistant enablement changed to : %!{(MISSING)public}@"
+ "%!s(MISSING) Assistant language changed to : %!{(MISSING)public}@"
+ "%!s(MISSING) Auto asset set %!{(MISSING)public}@ newly created with expensive cellular policy: %!d(MISSING)"
+ "%!s(MISSING) Changing subscriptions for '%!{(MISSING)public}@': '%!{(MISSING)public}@'"
+ "%!s(MISSING) Dictation enablement changed to : %!{(MISSING)public}@"
+ "%!s(MISSING) GMS enablement changed to : %!{(MISSING)public}@"
+ "%!s(MISSING) Not updating Assistant enablement as it is unchanged from : %!{(MISSING)public}@"
+ "%!s(MISSING) Not updating Assistant language as value is unchanged from : %!{(MISSING)public}@"
+ "%!s(MISSING) Not updating Dictation enablement as it is unchanged from : %!{(MISSING)public}@"
+ "%!s(MISSING) Not updating GMS enablement as it is unchanged from : %!{(MISSING)public}@"
+ "%!s(MISSING) Not updating system language as value is unchanged from : %!{(MISSING)public}@"
+ "%!s(MISSING) Processing update to assistant language"
+ "%!s(MISSING) Processing update to assistant preferences"
+ "%!s(MISSING) Processing update to gms availability"
+ "%!s(MISSING) Processing update to system language"
+ "%!s(MISSING) Siri configured for: language %!{(MISSING)public}@, mode: %!{(MISSING)public}@"
+ "%!s(MISSING) failed to init assetSet with assetSetName '%!{(MISSING)public}@' and usages '%!{(MISSING)public}@'"
+ "%!s(MISSING) failed to init assetSetWithoutExperimentation with assetSetName '%!{(MISSING)public}@' and usages '%!{(MISSING)public}@'"
+ "+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke"
+ "+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke"
+ "-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke"
+ "-[UAFAssetUtilities assetsAreAvailableForLanguage:completion:]"
+ "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke_3"
+ "-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke"
+ "-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke_3"
+ "-[UAFXPCService _assistantEnabledChanged]"
+ "-[UAFXPCService _assistantLanguageChanged]"
+ "-[UAFXPCService _dictationEnabledChanged]"
+ "-[UAFXPCService _gmsEnabledChanged]"
+ "-[UAFXPCService _systemLanguageChanged]"
+ "-[UAFXPCService _updateAssistantSubscription]"
+ "-[UAFXPCService _updateGMSSiriLanguageSubscription]"
+ "Asset missing"
+ "T@\"NSString\",R,C,V_assistantLanguage"
+ "T@\"NSString\",R,C,V_systemLanguage"
+ "TB,N,V_enableExpensiveCellular"
+ "TB,R,N,V_assistantEnabled"
+ "TB,R,N,V_dictationEnabled"
+ "TB,R,N,V_gmsEnabled"
+ "UOD not supported"
+ "_assistantEnabledChanged"
+ "_assistantLanguage"
+ "_assistantLanguageChanged"
+ "_dictationEnabledChanged"
+ "_enableExpensiveCellular"
+ "_gmsEnabled"
+ "_gmsEnabledChanged"
+ "_isOnDemandAssetSubscriptionAllowed"
+ "_systemLanguage"
+ "_systemLanguageChanged"
+ "_updateAssetUtilitiesLanguage"
+ "_updateAssistantSubscription"
+ "_updateGMSSiriLanguageSubscription"
+ "_updateMorphunSystemLanguageSubscription"
+ "_updateNLSystemLanguageSubscription"
+ "allowCheckDownloadOverExpensive"
+ "assetsAreAvailableForLanguage:completion:"
+ "assistantLanguage"
+ "dictationEnabled"
+ "enableExpensiveCellular"
+ "gmsEnabled"
+ "self is nil"
+ "setEnableExpensiveCellular:"
+ "systemLanguage"
- "\x02\x13"
- "%!s(MISSING) #settings Failed to check assets availability due to timeout. Returning cached value:%!d(MISSING), language = %!{(MISSING)public}@"
- "%!s(MISSING) #settings Failed to refresh UAFAssetStatus due to timeout"
- "%!s(MISSING) Altered auto asset set %!{(MISSING)public}@ with type %!{(MISSING)public}@ with cellular: %!d(MISSING) and specifiers %!{(MISSING)public}@"
- "%!s(MISSING) Assistant preferences changed to : %!s(MISSING)"
- "%!s(MISSING) Auto asset set %!{(MISSING)public}@ newly created with cellular policy: %!d(MISSING)"
- "%!s(MISSING) Dictation preferences changed to : %!s(MISSING)"
- "%!s(MISSING) Ignoring notification Siri language unchanged from : %!{(MISSING)public}@"
- "%!s(MISSING) Siri language changed to : %!{(MISSING)public}@, mode: %!{(MISSING)public}@"
- "-[UAFAssetUtilities _assetsAreAvailableForLanguageSync:]"
- "-[UAFAssetUtilities _assistantPreferencesAndLanguageUpdate]_block_invoke"
- "-[UAFAssetUtilities _refreshUAFAssetStatusSync]"
- "-[UAFAssetUtilities _refreshUAFAssetStatusSync]_block_invoke"
- "-[UAFAssetUtilities _refreshUAFAssetStatusSync]_block_invoke_2"
- "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke"
- "TB,N,V_enableCellular"
- "_assetsAreAvailableForLanguageSync:"
- "_assistantPreferencesAndLanguageUpdate"
- "_enableCellular"
- "_languageCode"
- "_refreshUAFAssetStatusSync"
- "_systemLanguageCode"
- "_uodDelegateAvailable"
- "assetsAreAvailableForLanguageSync:"
- "en-US"
- "enableCellular"
- "kAFSessionLanguage"
- "kAssistantBackedUpDomain"
- "setEnableCellular:"
- "systemLanguageLocale"

```
