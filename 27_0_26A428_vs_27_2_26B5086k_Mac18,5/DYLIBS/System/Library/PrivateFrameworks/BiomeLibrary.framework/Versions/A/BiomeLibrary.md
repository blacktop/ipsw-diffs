## BiomeLibrary

> `/System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary`

```diff

-436.6.0.0.0
-  __TEXT.__text: 0x786508
-  __TEXT.__objc_methlist: 0x4ffc4
-  __TEXT.__const: 0x47d0
+441.22.0.1.0
+  __TEXT.__text: 0x7887e0
+  __TEXT.__objc_methlist: 0x50034
+  __TEXT.__const: 0x4860
   __TEXT.__swift5_typeref: 0x17e
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__cstring: 0x4e30b
+  __TEXT.__cstring: 0x4e618
   __TEXT.__constg_swiftt: 0x5b8
   __TEXT.__swift5_fieldmd: 0x210
   __TEXT.__swift5_types: 0x84
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x12378
+  __TEXT.__unwind_info: 0x123b0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ebd0
+  __DATA_CONST.__const: 0x1ee90
   __DATA_CONST.__objc_classlist: 0x2320
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x126a0
+  __DATA_CONST.__objc_selrefs: 0x12700
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1b40
-  __DATA_CONST.__objc_arraydata: 0xb188
+  __DATA_CONST.__objc_arraydata: 0xb1c0
   __DATA_CONST.__got: 0x1c10
-  __AUTH_CONST.__const: 0x9b38
-  __AUTH_CONST.__cfstring: 0x4ada0
-  __AUTH_CONST.__objc_const: 0xa2f50
+  __AUTH_CONST.__const: 0x9b78
+  __AUTH_CONST.__cfstring: 0x4b220
+  __AUTH_CONST.__objc_const: 0xa30a0
   __AUTH_CONST.__objc_arrayobj: 0x65e8
   __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH.__objc_data: 0xaba8
+  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH.__objc_data: 0xabf8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8220
+  __DATA.__objc_ivar: 0x823c
   __DATA.__data: 0x328
-  __DATA_DIRTY.__objc_data: 0xbff8
+  __DATA_DIRTY.__objc_data: 0xbfa8
   __DATA_DIRTY.__data: 0x4f8
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 28605
-  Symbols:   60458
-  CStrings:  9713
+  Functions: 28629
+  Symbols:   60515
+  CStrings:  9749
 
Symbols:
+ +[BMSafariSearchEngine columns]
+ +[BMSafariSearchEngine eventWithData:dataVersion:]
+ +[BMSafariSearchEngine latestDataVersion]
+ +[BMSafariSearchEngine protoFields]
+ +[BMSafariSearchEngine validKeyPaths]
+ +[_BMSafariLibraryNode SearchEngine]
+ +[_BMSafariLibraryNode configurationForSearchEngine]
+ +[_BMSafariLibraryNode storeConfigurationForSearchEngine]
+ +[_BMSafariLibraryNode syncPolicyForSearchEngine]
+ -[BMAppInFocus initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:transitionReason:]
+ -[BMAppInFocus transitionReason]
+ -[BMAppInFocus(Deprecation) initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:]
+ -[BMCarKeyProvisioningData initWithOwnerPairingUrl:carBrand:alreadyProvisioned:carModel:carIdentifier:pairingCode:userIdentifier:provisioningCodeExpiration:spotlightUniqueIdentifier:spotlightDomainIdentifier:spotlightBundleIdentifier:dateSent:cccManufacturer:cccBrand:supportedTransports:sourceLanguage:messageIdentifier:]
+ -[BMCarKeyProvisioningData messageIdentifier]
+ -[BMCarKeyProvisioningData(Deprecation) initWithOwnerPairingUrl:carBrand:alreadyProvisioned:carModel:carIdentifier:pairingCode:userIdentifier:provisioningCodeExpiration:spotlightUniqueIdentifier:spotlightDomainIdentifier:spotlightBundleIdentifier:dateSent:cccManufacturer:cccBrand:supportedTransports:sourceLanguage:]
+ -[BMGeneratedImageFailureReason blockingSafetyModel]
+ -[BMGeneratedImageFailureReason blocklistCategory]
+ -[BMGeneratedImageFailureReason failureReason]
+ -[BMGeneratedImageFailureReason initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:userPrompt:rewrittenPrompt:safetyCategory:blocklistCategory:blockingSafetyModel:failureReason:]
+ -[BMGeneratedImageFailureReason rewrittenPrompt]
+ -[BMGeneratedImageFailureReason safetyCategory]
+ -[BMGeneratedImageFailureReason userPrompt]
+ -[BMGeneratedImageFailureReason(Deprecation) initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:]
+ -[BMSafariSearchEngine .cxx_destruct]
+ -[BMSafariSearchEngine dataVersion]
+ -[BMSafariSearchEngine description]
+ -[BMSafariSearchEngine initByReadFrom:]
+ -[BMSafariSearchEngine initWithJSONDictionary:error:]
+ -[BMSafariSearchEngine initWithSearchEngineIdentifier:]
+ -[BMSafariSearchEngine isEqual:]
+ -[BMSafariSearchEngine jsonDictionary]
+ -[BMSafariSearchEngine searchEngineIdentifier]
+ -[BMSafariSearchEngine serialize]
+ -[BMSafariSearchEngine writeTo:]
+ BMGeneratedImageFailureReasonBlockingSafetyModelFromString.sortedStrings
+ BMGeneratedImageFailureReasonBlocklistCategoryFromString.sortedEnums
+ BMGeneratedImageFailureReasonBlocklistCategoryFromString.sortedStrings
+ BMGeneratedImageFailureReasonFailureReasonFromString.sortedEnums
+ BMGeneratedImageFailureReasonFailureReasonFromString.sortedStrings
+ BMGeneratedImageFailureReasonSafetyCategoryFromString.sortedEnums
+ BMGeneratedImageFailureReasonSafetyCategoryFromString.sortedStrings
+ OBJC_IVAR_$_BMAppInFocus._transitionReason
+ OBJC_IVAR_$_BMCarKeyProvisioningData._messageIdentifier
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._blockingSafetyModel
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._blocklistCategory
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._failureReason
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._rewrittenPrompt
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._safetyCategory
+ OBJC_IVAR_$_BMGeneratedImageFailureReason._userPrompt
+ OBJC_IVAR_$_BMSafariSearchEngine._dataVersion
+ OBJC_IVAR_$_BMSafariSearchEngine._searchEngineIdentifier
+ _BMAppInFocusTransitionReasonColumn
+ _BMCarKeyProvisioningDataMessageIdentifierColumn
+ _BMGeneratedImageFailureReasonBlockingSafetyModelAsString
+ _BMGeneratedImageFailureReasonBlockingSafetyModelColumn
+ _BMGeneratedImageFailureReasonBlockingSafetyModelDecode
+ _BMGeneratedImageFailureReasonBlockingSafetyModelFromString
+ _BMGeneratedImageFailureReasonBlocklistCategoryAsString
+ _BMGeneratedImageFailureReasonBlocklistCategoryColumn
+ _BMGeneratedImageFailureReasonBlocklistCategoryDecode
+ _BMGeneratedImageFailureReasonBlocklistCategoryFromString
+ _BMGeneratedImageFailureReasonFailureReasonAsString
+ _BMGeneratedImageFailureReasonFailureReasonColumn
+ _BMGeneratedImageFailureReasonFailureReasonDecode
+ _BMGeneratedImageFailureReasonFailureReasonFromString
+ _BMGeneratedImageFailureReasonRewrittenPromptColumn
+ _BMGeneratedImageFailureReasonSafetyCategoryAsString
+ _BMGeneratedImageFailureReasonSafetyCategoryColumn
+ _BMGeneratedImageFailureReasonSafetyCategoryDecode
+ _BMGeneratedImageFailureReasonSafetyCategoryFromString
+ _BMGeneratedImageFailureReasonUserPromptColumn
+ _BMSafariSearchEngineIdentifier
+ _BMSafariSearchEngineSearchEngineIdentifierColumn
+ _NSSelectorFromString
+ _OBJC_CLASS_$_BMSafariSearchEngine
+ _OBJC_METACLASS_$_BMSafariSearchEngine
+ __OBJC_$_CLASS_METHODS_BMSafariSearchEngine
+ __OBJC_$_CLASS_PROP_LIST_BMSafariSearchEngine
+ __OBJC_$_INSTANCE_METHODS_BMGeneratedImageFailureReason(Deprecation)
+ __OBJC_$_INSTANCE_METHODS_BMSafariSearchEngine
+ __OBJC_$_INSTANCE_VARIABLES_BMSafariSearchEngine
+ __OBJC_$_PROP_LIST_BMSafariSearchEngine
+ __OBJC_CLASS_PROTOCOLS_$_BMSafariSearchEngine
+ __OBJC_CLASS_RO_$_BMSafariSearchEngine
+ __OBJC_METACLASS_RO_$_BMSafariSearchEngine
+ ___BMGeneratedImageFailureReasonBlockingSafetyModelFromString_block_invoke
+ ___BMGeneratedImageFailureReasonBlocklistCategoryFromString_block_invoke
+ ___BMGeneratedImageFailureReasonFailureReasonFromString_block_invoke
+ ___BMGeneratedImageFailureReasonSafetyCategoryFromString_block_invoke
+ _objc_msgSend$SearchEngine
+ _objc_msgSend$blockingSafetyModel
+ _objc_msgSend$blocklistCategory
+ _objc_msgSend$configurationForSearchEngine
+ _objc_msgSend$initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:transitionReason:
+ _objc_msgSend$initWithOwnerPairingUrl:carBrand:alreadyProvisioned:carModel:carIdentifier:pairingCode:userIdentifier:provisioningCodeExpiration:spotlightUniqueIdentifier:spotlightDomainIdentifier:spotlightBundleIdentifier:dateSent:cccManufacturer:cccBrand:supportedTransports:sourceLanguage:messageIdentifier:
+ _objc_msgSend$initWithSearchEngineIdentifier:
+ _objc_msgSend$initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:userPrompt:rewrittenPrompt:safetyCategory:blocklistCategory:blockingSafetyModel:failureReason:
+ _objc_msgSend$rewrittenPrompt
+ _objc_msgSend$safetyCategory
+ _objc_msgSend$searchEngineIdentifier
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$storeConfigurationForSearchEngine
+ _objc_msgSend$syncPolicyForSearchEngine
+ _objc_msgSend$transitionReason
+ _objc_msgSend$userPrompt
+ _objc_opt_respondsToSelector
- +[BMSiriHomeHistory columns]
- +[BMSiriHomeHistory eventWithData:dataVersion:]
- +[BMSiriHomeHistory latestDataVersion]
- +[BMSiriHomeHistory protoFields]
- +[BMSiriHomeHistory validKeyPaths]
- +[_BMSiriRemembersLibraryNode HomeHistory]
- +[_BMSiriRemembersLibraryNode configurationForHomeHistory]
- +[_BMSiriRemembersLibraryNode storeConfigurationForHomeHistory]
- +[_BMSiriRemembersLibraryNode syncPolicyForHomeHistory]
- -[BMAppInFocus initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:]
- -[BMCarKeyProvisioningData initWithOwnerPairingUrl:carBrand:alreadyProvisioned:carModel:carIdentifier:pairingCode:userIdentifier:provisioningCodeExpiration:spotlightUniqueIdentifier:spotlightDomainIdentifier:spotlightBundleIdentifier:dateSent:cccManufacturer:cccBrand:supportedTransports:sourceLanguage:]
- -[BMGeneratedImageFailureReason initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:]
- -[BMSiriHomeHistory .cxx_destruct]
- -[BMSiriHomeHistory _entitiesJSONArray]
- -[BMSiriHomeHistory dataVersion]
- -[BMSiriHomeHistory description]
- -[BMSiriHomeHistory entities]
- -[BMSiriHomeHistory initByReadFrom:]
- -[BMSiriHomeHistory initWithInteraction:entities:]
- -[BMSiriHomeHistory initWithJSONDictionary:error:]
- -[BMSiriHomeHistory interaction]
- -[BMSiriHomeHistory isEqual:]
- -[BMSiriHomeHistory jsonDictionary]
- -[BMSiriHomeHistory serialize]
- -[BMSiriHomeHistory writeTo:]
- OBJC_IVAR_$_BMSiriHomeHistory._dataVersion
- OBJC_IVAR_$_BMSiriHomeHistory._entities
- OBJC_IVAR_$_BMSiriHomeHistory._interaction
- _BMSiriHomeHistoryEntitiesColumn
- _BMSiriHomeHistoryInteractionColumn
- _BMSiriRemembersHomeHistoryIdentifier
- _OBJC_CLASS_$_BMSiriHomeHistory
- _OBJC_METACLASS_$_BMSiriHomeHistory
- __OBJC_$_CLASS_METHODS_BMSiriHomeHistory
- __OBJC_$_CLASS_PROP_LIST_BMSiriHomeHistory
- __OBJC_$_INSTANCE_METHODS_BMGeneratedImageFailureReason
- __OBJC_$_INSTANCE_METHODS_BMSiriHomeHistory
- __OBJC_$_INSTANCE_VARIABLES_BMSiriHomeHistory
- __OBJC_$_PROP_LIST_BMSiriHomeHistory
- __OBJC_CLASS_PROTOCOLS_$_BMSiriHomeHistory
- __OBJC_CLASS_RO_$_BMSiriHomeHistory
- __OBJC_METACLASS_RO_$_BMSiriHomeHistory
- ___28+[BMSiriHomeHistory columns]_block_invoke
- ___28+[BMSiriHomeHistory columns]_block_invoke_2
- _objc_msgSend$HomeHistory
- _objc_msgSend$configurationForHomeHistory
- _objc_msgSend$initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:
- _objc_msgSend$storeConfigurationForHomeHistory
- _objc_msgSend$syncPolicyForHomeHistory
CStrings:
+ "!D"
+ "AppleProducts"
+ "BMAppInFocus with launchReason: %@, type: %@, starting: %@, absoluteTimestamp: %@, bundleID: %@, parentBundleID: %@, extensionHostID: %@, shortVersionString: %@, exactVersionString: %@, dyldPlatform: %@, isNativeArchitecture: %@, displayType: %@, transitionReason: %@"
+ "BMCarKeyProvisioningData with ownerPairingUrl: %@, carBrand: %@, alreadyProvisioned: %@, carModel: %@, carIdentifier: %@, pairingCode: %@, userIdentifier: %@, provisioningCodeExpiration: %@, spotlightUniqueIdentifier: %@, spotlightDomainIdentifier: %@, spotlightBundleIdentifier: %@, dateSent: %@, cccManufacturer: %@, cccBrand: %@, supportedTransports: %@, sourceLanguage: %@, messageIdentifier: %@"
+ "BMGeneratedImageFailureReason with timestamp: %@, identifier: %@, userInterfaceLanguage: %@, userSetRegionFormat: %@, reason: %@, feature: %@, userPrompt: %@, rewrittenPrompt: %@, safetyCategory: %@, blocklistCategory: %@, blockingSafetyModel: %@, failureReason: %@"
+ "BMSafariSearchEngine with searchEngineIdentifier: %@"
+ "CustomWords"
+ "Desecration"
+ "Drugs"
+ "E701EAE3-5E66-458A-84C1-A611E4B3C2E3"
+ "ErrorUnableToSignInWithUserName"
+ "ExternalGeneratorNetworkFailure"
+ "ExternalGeneratorRateLimited"
+ "Harassment"
+ "Hate"
+ "IdentityEditing"
+ "MapsAndFlags"
+ "Minor"
+ "ModelsDownloading"
+ "MultimodalGuardrail"
+ "NOT ALL {bundleID, parentBundleID, extensionHostID} IN $installed"
+ "Offensive"
+ "PCCNoNodesAvailable"
+ "Photorealism"
+ "PixelGuardrail"
+ "PublicFigure"
+ "Racy"
+ "Safari.SearchEngine"
+ "SearchEngine"
+ "SelfHarm"
+ "Suggestive"
+ "Terrorism"
+ "TextGuardrail"
+ "Toxic"
+ "ViolenceAndGore"
+ "blockingSafetyModel"
+ "blocklistCategory"
+ "recoversFromFutureDatedEvents"
+ "rewrittenPrompt"
+ "safetyCategory"
+ "searchEngineIdentifier"
+ "setRecoversFromFutureDatedEvents:"
+ "transitionReason"
+ "userPrompt"
- "!\""
- "2A547182-AF14-4DCE-BF23-C42E38DBEC9B"
- "BMAppInFocus with launchReason: %@, type: %@, starting: %@, absoluteTimestamp: %@, bundleID: %@, parentBundleID: %@, extensionHostID: %@, shortVersionString: %@, exactVersionString: %@, dyldPlatform: %@, isNativeArchitecture: %@, displayType: %@"
- "BMCarKeyProvisioningData with ownerPairingUrl: %@, carBrand: %@, alreadyProvisioned: %@, carModel: %@, carIdentifier: %@, pairingCode: %@, userIdentifier: %@, provisioningCodeExpiration: %@, spotlightUniqueIdentifier: %@, spotlightDomainIdentifier: %@, spotlightBundleIdentifier: %@, dateSent: %@, cccManufacturer: %@, cccBrand: %@, supportedTransports: %@, sourceLanguage: %@"
- "BMGeneratedImageFailureReason with timestamp: %@, identifier: %@, userInterfaceLanguage: %@, userSetRegionFormat: %@, reason: %@, feature: %@"
- "BMSiriHomeHistory with interaction: %@, entities: %@"
- "HomeHistory"
- "Siri.Remembers.HomeHistory"
```
