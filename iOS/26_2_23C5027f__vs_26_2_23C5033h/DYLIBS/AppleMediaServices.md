## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.2.16.0.0
-  __TEXT.__text: 0x768eb0
+9.2.21.0.0
+  __TEXT.__text: 0x76bdc8
   __TEXT.__auth_stubs: 0x4b30
   __TEXT.__objc_methlist: 0x22f7c
-  __TEXT.__const: 0x5d1b0
+  __TEXT.__const: 0x5d680
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2dd96
-  __TEXT.__swift5_typeref: 0x6899
-  __TEXT.__swift5_reflstr: 0x39d4
-  __TEXT.__swift5_assocty: 0xed0
-  __TEXT.__constg_swiftt: 0x52b4
-  __TEXT.__swift5_builtin: 0x30c
-  __TEXT.__swift5_fieldmd: 0x4cf8
-  __TEXT.__swift5_proto: 0x1100
-  __TEXT.__swift5_types: 0x610
-  __TEXT.__swift_as_entry: 0x720
-  __TEXT.__swift_as_ret: 0x88c
-  __TEXT.__swift5_capture: 0x3190
+  __TEXT.__cstring: 0x2df8b
+  __TEXT.__swift5_typeref: 0x697b
+  __TEXT.__swift5_reflstr: 0x3ab4
+  __TEXT.__swift5_assocty: 0xf00
+  __TEXT.__constg_swiftt: 0x53bc
+  __TEXT.__swift5_builtin: 0x320
+  __TEXT.__swift5_fieldmd: 0x4e0c
+  __TEXT.__swift5_proto: 0x1144
+  __TEXT.__swift5_types: 0x62c
+  __TEXT.__swift_as_entry: 0x734
+  __TEXT.__swift_as_ret: 0x8b4
+  __TEXT.__swift5_capture: 0x31c0
   __TEXT.__swift5_mpenum: 0x7c
   __TEXT.__swift5_protos: 0xf0
-  __TEXT.__oslogstring: 0x31048
+  __TEXT.__oslogstring: 0x3129b
   __TEXT.__gcc_except_tab: 0x5e88
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x11798
-  __TEXT.__eh_frame: 0x15970
+  __TEXT.__unwind_info: 0x118e8
+  __TEXT.__eh_frame: 0x15eb8
   __TEXT.__objc_classname: 0x40ba
-  __TEXT.__objc_methname: 0x45836
-  __TEXT.__objc_methtype: 0x79e9
-  __TEXT.__objc_stubs: 0x2eec0
+  __TEXT.__objc_methname: 0x458fb
+  __TEXT.__objc_methtype: 0x7a03
+  __TEXT.__objc_stubs: 0x2ef00
   __DATA_CONST.__got: 0x1a80
   __DATA_CONST.__const: 0xc6a8
-  __DATA_CONST.__objc_classlist: 0x14e0
+  __DATA_CONST.__objc_classlist: 0x14e8
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf418
+  __DATA_CONST.__objc_selrefs: 0xf428
   __DATA_CONST.__objc_protorefs: 0x218
   __DATA_CONST.__objc_superrefs: 0xce0
   __DATA_CONST.__objc_arraydata: 0x580
   __AUTH_CONST.__auth_got: 0x25b0
-  __AUTH_CONST.__const: 0x2d978
-  __AUTH_CONST.__cfstring: 0x22d20
-  __AUTH_CONST.__objc_const: 0x3d5d0
+  __AUTH_CONST.__const: 0x2dd88
+  __AUTH_CONST.__cfstring: 0x22d40
+  __AUTH_CONST.__objc_const: 0x3d658
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x98d0
-  __AUTH.__data: 0x26f8
-  __DATA.__objc_ivar: 0x18ec
-  __DATA.__data: 0x7828
-  __DATA.__bss: 0x1c489
+  __AUTH.__objc_data: 0x98c0
+  __AUTH.__data: 0x27d8
+  __DATA.__objc_ivar: 0x18f0
+  __DATA.__data: 0x7898
+  __DATA.__bss: 0x1cc89
   __DATA.__common: 0xb68
   __DATA_DIRTY.__objc_ivar: 0x718
   __DATA_DIRTY.__objc_data: 0x5ac0
-  __DATA_DIRTY.__data: 0x1b28
+  __DATA_DIRTY.__data: 0x1b18
   __DATA_DIRTY.__bss: 0x40e0
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DA615808-A304-3CF5-856B-D4B1AA6C7821
-  Functions: 26641
-  Symbols:   52931
-  CStrings:  25924
+  UUID: D91F8575-B3DD-3F80-A282-42CECF867A25
+  Functions: 26768
+  Symbols:   53047
+  CStrings:  25947
 
Symbols:
+ +[AMSMetricsIdentifierStore _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:]
+ +[AMSMetricsIdentifierStoreConsumerID _identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:valueDidChange:error:]
+ +[AMSMetricsIdentifierStoreConsumerID _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:]
+ +[AMSMetricsIdentifierStoreConsumerID _setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:linkedClientInfo:linkedDomain:linkedResetInterval:linkedKey:]
+ -[AMSAuthenticateOptions setSimpleProfileCreated:]
+ -[AMSAuthenticateOptions simpleProfileCreated]
+ _OBJC_IVAR_$_AMSAuthenticateOptions._simpleProfileCreated
+ __DATA__TtCV18AppleMediaServices29SuggestedRatingsConfigurationP33_CA15A9948F8FE6F763BFB83B377B791313BagValueCache
+ __IVARS__TtCV18AppleMediaServices29SuggestedRatingsConfigurationP33_CA15A9948F8FE6F763BFB83B377B791313BagValueCache
+ __METACLASS_DATA__TtCV18AppleMediaServices29SuggestedRatingsConfigurationP33_CA15A9948F8FE6F763BFB83B377B791313BagValueCache
+ ___150+[AMSMetricsIdentifierStoreConsumerID _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:]_block_invoke
+ ___150+[AMSMetricsIdentifierStoreConsumerID _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:]_block_invoke.4
+ ___155+[AMSMetricsIdentifierStoreConsumerID _identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:valueDidChange:error:]_block_invoke
+ ___212+[AMSMetricsIdentifierStoreConsumerID _setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:linkedClientInfo:linkedDomain:linkedResetInterval:linkedKey:]_block_invoke
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r136r_e5_v8?0ls32l8s40l8s48l8s56l8r128l8s64l8s72l8s80l8s88l8s96l8r136l8s104l8s112l8s120l8
+ ___block_descriptor_96_e8_32s40s48s56s64s_e9_B16?0^8ls32l8s40l8s48l8s56l8s64l8
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 18AppleMediaServices0B22RestrictionsQRAuthFlowOSHAASQ
+ _associated conformance 18AppleMediaServices17QRCodeHandlerFlowOSHAASQ
+ _associated conformance 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysOSHAASQ
+ _associated conformance 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 18AppleMediaServices32SuggestedRatingsProviderBagModelVSHAASQ
+ _objc_msgSend$_identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:valueDidChange:error:
+ _objc_msgSend$_setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:
+ _objc_msgSend$_setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:linkedClientInfo:linkedDomain:linkedResetInterval:linkedKey:
+ _objc_msgSend$setSimpleProfileCreated:
+ _objc_msgSend$simpleProfileCreated
+ _symbolic Say_____G 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysO
+ _symbolic So31AMSSuggestedRatingsProviderTaskCSgXw
+ _symbolic So31AMSSuggestedRatingsProviderTaskCSgXwz_Xx
+ _symbolic _____ 18AppleMediaServices0B22RestrictionsQRAuthFlowO
+ _symbolic _____ 18AppleMediaServices17QRCodeHandlerFlowO
+ _symbolic _____ 18AppleMediaServices29SuggestedRatingsConfigurationV
+ _symbolic _____ 18AppleMediaServices29SuggestedRatingsConfigurationV13BagValueCache33_CA15A9948F8FE6F763BFB83B377B7913LLC
+ _symbolic _____ 18AppleMediaServices32SuggestedRatingsProviderBagModelV
+ _symbolic _____ 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysO
+ _symbolic _____ So40AMSSuggestedRatingsProviderTaskMediaTypeV
+ _symbolic _____Sg 18AppleMediaServices32SuggestedRatingsProviderBagModelV
+ _symbolic _____Sg 18AppleMediaServices5Glyph33_013537140E75CD412106440FFA511BA4LLV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18AppleMediaServices32SuggestedRatingsProviderBagModelV10CodingKeysO
+ _type_layout_string 18AppleMediaServices29SuggestedRatingsConfigurationV
+ _type_layout_string 18AppleMediaServices32SuggestedRatingsProviderBagModelV
- +[AMSMetricsIdentifierStore _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:]
- +[AMSMetricsIdentifierStoreConsumerID _identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:error:]
- +[AMSMetricsIdentifierStoreConsumerID _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:]
- +[AMSMetricsIdentifierStoreConsumerID _setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:]
- ___124+[AMSMetricsIdentifierStoreConsumerID _setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:]_block_invoke
- ___140+[AMSMetricsIdentifierStoreConsumerID _identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:error:]_block_invoke
- ___152+[AMSMetricsIdentifierStoreConsumerID _setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:]_block_invoke
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r_e5_v8?0ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_88_e8_32s40s48s56s64s_e9_B16?0^8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- _block_copy_helper.58
- _block_descriptor.60
- _block_destroy_helper.59
- _objc_msgSend$_identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:error:
- _objc_msgSend$_setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:
- _objc_msgSend$_setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:
- _symbolic SDySS_____GSg 18AppleMediaServices20RestrictionValueTypeO
CStrings:
+ "%{public}@: [%{public}@] Consumer ID value changed, but we could not find the linked store to rotate the ID for key %{public}@"
+ "%{public}@: [%{public}@] Linked Metrics Identifier Store found for namespace \"%{public}@\"; store: %{public}@"
+ "%{public}@: [%{public}@] Linked Metrics Identifier Store not found for namespace \"%{public}@\"; error: %{public}@"
+ "%{public}@Fetch profile lock promise handler updater: %{public}@"
+ "%{public}@Profile lock encountered error in promise handler: %{public}@ | error = %{public}@"
+ "%{public}@Profile lock is stale: %{public}@"
+ "%{public}@Profile lock is valid: %{public}@"
+ "@124@0:8@16@24@32@40@48@56@64d72@80B88@92@100d108@116"
+ "@88@0:8@16@24@32@40^B48@56d64^B72^@80"
+ "@92@0:8@16@24@32@40@48@56@64B72@76@84"
+ "AMSAuthenticateOptionsSimpleProfileCreated"
+ "AUTH_WITH_PROFILE_LOCK"
+ "Error updating cached data after request failure:"
+ "Missing bag value for videoAgeGroupContentPoliciesUrlTemplate"
+ "Refreshing Media Restrictions"
+ "Refreshing Profile Lock"
+ "T@\"<AMSBagProtocol>\",N,R"
+ "TB,N,V_simpleProfileCreated"
+ "Task reference was deallocated"
+ "Unable to locate URL"
+ "_TtCV18AppleMediaServices29SuggestedRatingsConfigurationP33_CA15A9948F8FE6F763BFB83B377B791313BagValueCache"
+ "_identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:valueDidChange:error:"
+ "_setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:linkedKey:linkedNamespace:"
+ "_setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:linkedClientInfo:linkedDomain:linkedResetInterval:linkedKey:"
+ "_simpleProfileCreated"
+ "cachedModel"
+ "setSimpleProfileCreated:"
+ "simpleProfileCreated"
+ "videoAgeGroupContentPoliciesUrlTemplate"
- "@76@0:8@16@24@32@40@48@56@64B72"
- "@80@0:8@16@24@32@40^B48@56d64^@72"
- "@92@0:8@16@24@32@40@48@56@64d72@80B88"
- "TQ,N,R,VmediaType"
- "_identifierInfoForKey:storeInfo:inDatabase:setValue:needsToSync:serverProvidedAt:resetInterval:error:"
- "_setConsumerIdentifier:forKey:inNamespace:accountID:bag:at:serverProvidedAt:skipSync:"
- "_setIdentifier:withStartedDate:forKey:database:account:clientInfo:domain:resetInterval:serverProvidedAt:skipSync:"

```
