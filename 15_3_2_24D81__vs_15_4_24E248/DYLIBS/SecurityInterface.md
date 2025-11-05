## SecurityInterface

> `/System/Library/Frameworks/SecurityInterface.framework/Versions/A/SecurityInterface`

```diff

-55188.0.0.0.0
-  __TEXT.__text: 0x20180
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x24c0
+55206.0.0.0.0
+  __TEXT.__text: 0x20d30
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x2800
   __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x44c
-  __TEXT.__cstring: 0x271d
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__cstring: 0x2996
   __TEXT.__oslogstring: 0x108f
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__unwind_info: 0x968
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__objc_classname: 0x54a
-  __TEXT.__objc_methname: 0x5f5e
-  __TEXT.__objc_methtype: 0x1359
-  __TEXT.__objc_stubs: 0x6440
-  __DATA_CONST.__got: 0x440
+  __TEXT.__objc_methname: 0x619c
+  __TEXT.__objc_methtype: 0x1421
+  __TEXT.__objc_stubs: 0x6700
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f78
+  __DATA_CONST.__objc_selrefs: 0x2158
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0x2820
-  __AUTH_CONST.__objc_const: 0x5260
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x6b0
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x4dd0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x4e8
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x200
-  __DATA.__bss: 0x218
+  __DATA.__bss: 0x228
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 958F0F73-D69D-3152-9D6E-5B01775E1222
-  Functions: 958
-  Symbols:   2924
-  CStrings:  2371
+  UUID: D146BD93-9BB8-385D-917E-4B722F5585D1
+  Functions: 995
+  Symbols:   3138
+  CStrings:  2442
 
Symbols:
+ +[SFCertificateTrust isSMIMEPolicy:]
+ +[SFCertificateTrust isSSLPolicy:]
+ +[SFCertificateTrust issuerOrgName:]
+ +[SFCertificateTrust issuerSummaryName:]
+ +[SFCertificateTrust nameFromCertificate:fieldName:subFieldName:]
+ +[SFCertificateTrust sslPolicyNameForTrust:]
+ +[SFCertificateTrust subjectLocationName:]
+ +[SFCertificateTrust subjectOrgName:]
+ +[SFCertificateTrust subjectSummaryName:]
+ +[SFCertificateTrust trustStatementsEnabled]
+ +[SFCertificateTrust trustStatementsEnabled].cold.1
+ +[SFKeychainStorage isCloudKeychainSyncEnabled].cold.1
+ +[SheetSupport _loadLAUI].cold.2
+ +[SheetSupport _loadLAUI].cold.3
+ +[SheetSupport _loadSystemAdministrationFramework].cold.1
+ +[SheetSupport _loadSystemAdministrationFramework].cold.2
+ -[SFAuthorizationView(Private) setLAContext:].cold.1
+ -[SFCertificateTrustPanel(Private) _appendTrustStatements:toString:]
+ -[SFCertificateTrustPanel(Private) _binarySearchTruncateString:withEllipsis:maxRect:formatHandler:measurementBlock:]
+ -[SFCertificateTrustPanel(Private) _bulletIndentedAttributedString:]
+ -[SFCertificateTrustPanel(Private) _bundleIdentifier]
+ -[SFCertificateTrustPanel(Private) _localizedAppName]
+ -[SFCertificateTrustPanel(Private) _plainAttributedString:]
+ -[SFCertificateView _createViews].cold.1
+ -[SheetSupport _processRightProperties].cold.1
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.10
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.11
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.12
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.13
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.14
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.15
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.16
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.17
+ -[SheetSupport _processSheetCredentials:providedUid:].cold.9
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.10
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.11
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.12
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.13
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.14
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.6
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.7
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.8
+ -[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:].cold.9
+ -[SheetSupport init].cold.2
+ -[SheetSupport shouldUseSheet].cold.1
+ -[SheetSupport shouldUseSheet].cold.2
+ -[SheetSupport shouldUseSheet].cold.3
+ GCC_except_table59
+ OBJC_IVAR_$_SFCertificateTrustPanel_ivars._escButton
+ SFAuthorizationSheetWorker.cold.5
+ SFAuthorizationSheetWorker.cold.6
+ SFAuthorizationSheetWorker.cold.7
+ SFAuthorizationSheetWorker.cold.8
+ TKAddSecureToken.cold.10
+ TKAddSecureToken.cold.11
+ TKAddSecureToken.cold.12
+ TKAddSecureToken.cold.13
+ TKAddSecureToken.cold.14
+ TKAddSecureToken.cold.15
+ TKAddSecureToken.cold.8
+ TKAddSecureToken.cold.9
+ TKBindUser.cold.2
+ TKBindUserAm.cold.2
+ TKCopyAvailableTokensInfo.cold.3
+ TKCopyAvailableTokensInfo.cold.4
+ TKCopyAvailableTokensInfo.cold.5
+ TKCopyAvailableTokensInfo.cold.6
+ TKCopyLegacyBindings.cold.10
+ TKCopyLegacyBindings.cold.11
+ TKCopyLegacyBindings.cold.12
+ TKCopyLegacyBindings.cold.7
+ TKCopyLegacyBindings.cold.8
+ TKCopyLegacyBindings.cold.9
+ TKCopySmartCardConfiguration.cold.6
+ TKCopySmartCardConfiguration.cold.7
+ TKCopySmartCardConfiguration.cold.8
+ TKCopySmartCardConfiguration.cold.9
+ TKGetSmartcardSetting.cold.1
+ TKGetSmartcardSetting.cold.2
+ TKGetSmartcardSettingForUser.cold.1
+ TKGetSmartcardSettingForUser.cold.2
+ TKGetSmartcardSettingForUser.cold.3
+ TKGetSmartcardSettingForUser.cold.4
+ TKGetSmartcardSettingForUser.cold.5
+ TKGetSmartcardSettingForUser.cold.6
+ TKGetSmartcardSettingForUser.cold.7
+ TKGetSmartcardSettingForUser.cold.8
+ TKGetSmartcardSettingForUser.cold.9
+ TKGetSmartcardSettingWorker.cold.1
+ TKGetSmartcardSettingWorker.cold.2
+ TKGetSmartcardSettingWorker.cold.3
+ TKGetSmartcardSettingWorker.cold.4
+ TKIsUserBound.cold.4
+ TKIsUserBound.cold.5
+ TKIsUserBound.cold.6
+ TKPerformLogin.cold.10
+ TKPerformLogin.cold.11
+ TKPerformLogin.cold.6
+ TKPerformLogin.cold.7
+ TKPerformLogin.cold.8
+ TKPerformLogin.cold.9
+ TKReadSecureTokenData.cold.10
+ TKReadSecureTokenData.cold.11
+ TKReadSecureTokenData.cold.6
+ TKReadSecureTokenData.cold.7
+ TKReadSecureTokenData.cold.8
+ TKReadSecureTokenData.cold.9
+ TKSmartCardSecureTokenRemove.cold.5
+ TKSmartCardSecureTokenRemove.cold.6
+ TKSmartCardSecureTokenRemove.cold.7
+ TKSmartCardSecureTokenRemove.cold.8
+ TKSmartCardSecureTokenRemove.cold.9
+ TKSmartCardSecureTokenStatus.cold.5
+ TKSmartCardSecureTokenStatus.cold.6
+ TKSmartCardSecureTokenStatus.cold.7
+ TKSmartCardSecureTokenStatus.cold.8
+ TKSmartCardSecureTokenStatus.cold.9
+ TKUnbindUser.cold.2
+ TKUnlockKeybag.cold.4
+ TKUnlockKeybag.cold.5
+ TKUnlockKeybag.cold.6
+ TKValidateAttributeMatchingConfig.cold.5
+ TKValidateAttributeMatchingConfig.cold.6
+ TKValidateAttributeMatchingConfig.cold.7
+ TKValidateAttributeMatchingConfig.cold.8
+ TKValidateAttributeMatchingConfig.cold.9
+ _OBJC_CLASS_$_NSURLComponents
+ _SecCertificateCopySubjectSummary
+ _SecCertificateCopyValues
+ _SecPolicyCopyProperties
+ _SecTrustCopyResult
+ __76-[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:]_block_invoke.75.cold.1
+ __76-[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:]_block_invoke.76.cold.1
+ __76-[SheetSupport doSheetAuthorization:environment:forWindow:authorizedRights:]_block_invoke.76.cold.2
+ __83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke.215
+ __83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke.228
+ __83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke.230
+ __83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke.231
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_SFCertificateTrust
+ ___44+[SFCertificateTrust trustStatementsEnabled]_block_invoke
+ ___83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke
+ ___83-[SFCertificateTrustPanel(Private) _truncatedAlwaysTrustCertString:forHostOrEmail:]_block_invoke_2
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32b_e18_d16?0"NSString"8l
+ ___block_descriptor_40_e8_32o_e18_d16?0"NSString"8l
+ ___block_descriptor_41_e8_32o_e41_"NSString"24?0"NSString"8"NSString"16l
+ ___block_descriptor_48_e8_32o40b_e28_"NSString"16?0"NSString"8l
+ ___copy_helper_block_e8_32o40b
+ ___destroy_helper_block_e8_32o40b
+ __getSystemVolumeUuid_block_invoke.cold.5
+ __getSystemVolumeUuid_block_invoke.cold.6
+ __getSystemVolumeUuid_block_invoke.cold.7
+ __getSystemVolumeUuid_block_invoke.cold.8
+ __getUidForAgent_block_invoke.cold.4
+ __getUidForAgent_block_invoke.cold.5
+ __os_feature_enabled_impl
+ _kSecOIDCommonName
+ _kSecOIDCountryName
+ _kSecOIDLocalityName
+ _kSecOIDOrganizationName
+ _kSecOIDStateProvinceName
+ _kSecOIDX509V1IssuerName
+ _kSecOIDX509V1SubjectName
+ _kSecPolicyName
+ _kSecPropertyKeyLabel
+ _kSecPropertyKeyType
+ _kSecPropertyKeyValue
+ _kSecPropertyTypeSection
+ _kSecPropertyTypeString
+ _objc_msgSend$_appendTrustStatements:toString:
+ _objc_msgSend$_binarySearchTruncateString:withEllipsis:maxRect:formatHandler:measurementBlock:
+ _objc_msgSend$_bulletIndentedAttributedString:
+ _objc_msgSend$_bundleIdentifier
+ _objc_msgSend$_localizedAppName
+ _objc_msgSend$_plainAttributedString:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$host
+ _objc_msgSend$isSSLPolicy:
+ _objc_msgSend$issuerOrgName:
+ _objc_msgSend$issuerSummaryName:
+ _objc_msgSend$nameFromCertificate:fieldName:subFieldName:
+ _objc_msgSend$scheme
+ _objc_msgSend$setDefaultTabInterval:
+ _objc_msgSend$setFirstLineHeadIndent:
+ _objc_msgSend$setHeadIndent:
+ _objc_msgSend$setTabStops:
+ _objc_msgSend$sslPolicyNameForTrust:
+ _objc_msgSend$subjectLocationName:
+ _objc_msgSend$subjectOrgName:
+ _objc_msgSend$trustStatementsEnabled
+ binderWorker.cold.5
+ binderWorker.cold.6
+ binderWorker.cold.7
+ binderWorker.cold.8
+ fvunlockPrefs.cold.2
+ fvunlockPrefs.cold.3
+ getOdCustomEnforcementAttribute.cold.13
+ getOdCustomEnforcementAttribute.cold.14
+ getOdCustomEnforcementAttribute.cold.15
+ getOdCustomEnforcementAttribute.cold.16
+ getOdCustomEnforcementAttribute.cold.17
+ getOdCustomEnforcementAttribute.cold.18
+ getOdCustomEnforcementAttribute.cold.19
+ getOdCustomEnforcementAttribute.cold.20
+ getSystemVolumeUuid.cold.1
+ getUidForAgent.cold.1
+ isEnforcementOverriden.cold.1
+ isEnforcementOverriden.cold.2
+ isMemberOfGroup.cold.5
+ isMemberOfGroup.cold.6
+ isMemberOfGroup.cold.7
+ isMemberOfGroup.cold.8
+ setupConnection.cold.2
+ setupConnection.cold.3
+ trustStatementsEnabled.onceToken
+ trustStatementsEnabled.trustStatementsEnabled
- GCC_except_table54
- TKCopyTokenEndpoints.cold.1
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _tk_log.log
- _tk_log.onceToken
CStrings:
+ "\t"
+ "\x1b"
+ "%@\n"
+ "%@\n\n"
+ "%@ has verified that:"
+ "%@, %@, %@"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@\"NSString\"24@?0@\"NSString\"8@\"NSString\"16"
+ "@24@0:8^{__SecCertificate=}16"
+ "@24@0:8^{__SecTrust=}16"
+ "@32@0:8^{__SecTrust=}16@24"
+ "@40@0:8^{__SecCertificate=}16^v24^v32"
+ "@80@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@?64@?72"
+ "B24@0:8^{__SecPolicy=}16"
+ "Encryption with a digital certificate keeps information private as it's sent to or from %@."
+ "Organization"
+ "QWACValidation"
+ "SFCertificatePanel:_helpClicked -> openHelpAnchor:%@ inBook:%@"
+ "Security"
+ "TrustQWACValidation"
+ "\\U2022 %@ has identified %@ as being owned by %@ in %@"
+ "\\U2022 %@ is using an EU Qualified Web Authentication certificate"
+ "\\U2022 %@ issued this website's certificate"
+ "_appendTrustStatements:toString:"
+ "_binarySearchTruncateString:withEllipsis:maxRect:formatHandler:measurementBlock:"
+ "_bulletIndentedAttributedString:"
+ "_bundleIdentifier"
+ "_escButton"
+ "_localizedAppName"
+ "_plainAttributedString:"
+ "_truncatedAlwaysTrustCertString (%d) = %@"
+ "bundleIdentifier"
+ "com.apple.Safari"
+ "com.apple.Safari.help"
+ "com.apple.keychainaccess.help"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "d16@?0@\"NSString\"8"
+ "host"
+ "ibrw1066"
+ "isSMIMEPolicy:"
+ "isSSLPolicy:"
+ "issuerOrgName:"
+ "issuerSummaryName:"
+ "nameFromCertificate:fieldName:subFieldName:"
+ "scheme"
+ "setDefaultTabInterval:"
+ "setFirstLineHeadIndent:"
+ "setHeadIndent:"
+ "setTabStops:"
+ "sslPolicyNameForTrust:"
+ "subjectLocationName:"
+ "subjectOrgName:"
+ "subjectSummaryName:"
+ "trustStatementsEnabled"

```
