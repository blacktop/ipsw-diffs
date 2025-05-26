## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

```diff

-45.4.5.0.0
-  __TEXT.__text: 0x6a4a4
-  __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_methlist: 0x1ed0
-  __TEXT.__const: 0x3c60
-  __TEXT.__oslogstring: 0xb39
-  __TEXT.__cstring: 0x4608
-  __TEXT.__gcc_except_tab: 0x1290
-  __TEXT.__swift5_typeref: 0xf12
-  __TEXT.__swift5_reflstr: 0x44c
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__constg_swiftt: 0xa34
-  __TEXT.__swift5_fieldmd: 0xa80
-  __TEXT.__swift5_proto: 0x2d4
-  __TEXT.__swift5_types: 0xf0
-  __TEXT.__swift5_builtin: 0x3c
+46.4.1.0.0
+  __TEXT.__text: 0x6f8f0
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_methlist: 0x2168
+  __TEXT.__const: 0x3fa0
+  __TEXT.__cstring: 0x4d68
+  __TEXT.__oslogstring: 0xae4
+  __TEXT.__gcc_except_tab: 0x13a4
+  __TEXT.__swift5_typeref: 0xf9e
+  __TEXT.__swift5_reflstr: 0x46c
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__constg_swiftt: 0xb90
+  __TEXT.__swift5_fieldmd: 0xac8
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_proto: 0x2fc
+  __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x2a8
+  __TEXT.__swift5_capture: 0x2cc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x23c4
-  __TEXT.__eh_frame: 0x24a0
-  __TEXT.__objc_classname: 0x487
-  __TEXT.__objc_methname: 0x61ee
-  __TEXT.__objc_methtype: 0x21ab
-  __TEXT.__objc_stubs: 0x3280
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x198
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__unwind_info: 0x260c
+  __TEXT.__eh_frame: 0x2560
+  __TEXT.__objc_classname: 0x4cb
+  __TEXT.__objc_methname: 0x68cc
+  __TEXT.__objc_methtype: 0x220a
+  __TEXT.__objc_stubs: 0x3640
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0xa48
+  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x47c8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_const: 0x4c38
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_classrefs: 0x200
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0x2dc0
-  __AUTH_CONST.__objc_const: 0x88
+  __AUTH_CONST.__cfstring: 0x2f60
+  __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__const: 0x1b68
+  __AUTH_CONST.__const: 0x1d20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__auth_got: 0xa60
-  __AUTH.__objc_data: 0x128
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2ac
+  __AUTH_CONST.__auth_ptr: 0x68
+  __AUTH_CONST.__auth_got: 0xb58
+  __AUTH.__objc_data: 0x3e8
+  __AUTH.__data: 0xa0
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x1b10
-  __DATA.__bss: 0x5aa0
-  __DATA.__common: 0x80
-  __DATA_DIRTY.__const: 0x740
+  __DATA.__data: 0x1c58
+  __DATA.__bss: 0x5fb0
+  __DATA.__common: 0x88
+  __DATA_DIRTY.__const: 0x788
   __DATA_DIRTY.__objc_const: 0x1488
   __DATA_DIRTY.__objc_data: 0x13d8
   __DATA_DIRTY.__data: 0x298

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSESShared.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2587
-  Symbols:   3629
-  CStrings:  1840
+  Functions: 2733
+  Symbols:   3856
+  CStrings:  1973
 
Symbols:
+ +[SESNFCAppSettingsContext contextWithBundleId:onChange:]
+ -[LSPropertyList(Entitlements) ses_isEntitled:]
+ -[SESDefaultNFCApplication .cxx_destruct]
+ -[SESDefaultNFCApplication bundleId]
+ -[SESDefaultNFCApplication domain]
+ -[SESDefaultNFCApplication initWithBundleId:displayName:rawDomain:]
+ -[SESDefaultNFCApplication localizedDisplayName]
+ -[SESNFCAppSettingsContext .cxx_destruct]
+ -[SESNFCAppSettingsContext alertMessageForDefaultAppChangeTo:]
+ -[SESNFCAppSettingsContext bundleId]
+ -[SESNFCAppSettingsContext dealloc]
+ -[SESNFCAppSettingsContext defaultAppCandidates]
+ -[SESNFCAppSettingsContext doubleClickToggleVisibilityType]
+ -[SESNFCAppSettingsContext getDefaultNFCApplication]
+ -[SESNFCAppSettingsContext initWithBundleId:onChange:]
+ -[SESNFCAppSettingsContext invalidateInternal]
+ -[SESNFCAppSettingsContext invalidate]
+ -[SESNFCAppSettingsContext isApplicationInstalledOrPlaceholder:]
+ -[SESNFCAppSettingsContext isContactlessTCCServiceEligible]
+ -[SESNFCAppSettingsContext isDefaultAppEligibleForService:]
+ -[SESNFCAppSettingsContext isDefaultAppTheOnlyCandidate]
+ -[SESNFCAppSettingsContext isDefaultApp]
+ -[SESNFCAppSettingsContext isDoubleClickEnabled]
+ -[SESNFCAppSettingsContext isExpressModeEnabled]
+ -[SESNFCAppSettingsContext isPassbookDefault]
+ -[SESNFCAppSettingsContext isSecureElementTCCServiceEligible]
+ -[SESNFCAppSettingsContext localizedAppNameForBundleId:]
+ -[SESNFCAppSettingsContext observeDefaults]
+ -[SESNFCAppSettingsContext observeValueForKeyPath:ofObject:change:context:]
+ -[SESNFCAppSettingsContext readDefaultValues]
+ -[SESNFCAppSettingsContext reconcileWithRecord:]
+ -[SESNFCAppSettingsContext setDefaultNFCApplication:]
+ -[SESNFCAppSettingsContext setDoubleClickEnabled:]
+ -[SESNFCAppSettingsContext shouldShowDefaultNFCAppPicker]
+ -[SESNFCAppSettingsContext shouldShowDoubleButtonPressToggle]
+ -[SESNFCAppSettingsContext ud]
+ _MGGetBoolAnswer
+ _NSKeyValueChangeNewKey
+ _OBJC_CLASS_$_LSPropertyList
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_SESDefaultNFCApplication
+ _OBJC_CLASS_$_SESNFCAppSettingsContext
+ _OBJC_CLASS_$__TtC9SEService10TCCContext
+ _OBJC_CLASS_$__TtC9SEService33SESSettingsLocalizedStringFactory
+ _OBJC_IVAR_$_SESDefaultNFCApplication._bundleId
+ _OBJC_IVAR_$_SESDefaultNFCApplication._domain
+ _OBJC_IVAR_$_SESDefaultNFCApplication._localizedDisplayName
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._bundleId
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._currentDefaultBundleId
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._defaultAppCandidates
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._doubleClickToggleVisibilityType
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._invalidated
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._isContactlessTCCServiceEligible
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._isDomainAluminumEligible
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._isSecureElementTCCServiceEligible
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._lock
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._onChange
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._shouldShowDefaultNFCAppPicker
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._shouldShowHCEDefaultPane
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._shouldShowHCETCCPane
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._shouldShowSECDefaultPane
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._shouldShowSECTCCPane
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._supportsTouchID
+ _OBJC_IVAR_$_SESNFCAppSettingsContext._ud
+ _OBJC_METACLASS_$_SESDefaultNFCApplication
+ _OBJC_METACLASS_$_SESNFCAppSettingsContext
+ _OBJC_METACLASS_$__TtC9SEService10TCCContext
+ _OBJC_METACLASS_$__TtC9SEService33SESSettingsLocalizedStringFactory
+ _OBJC_METACLASS_$__TtC9SEServiceP33_DF7C6A441E5AB625BDF4896CC18BC9FD9FindClass
+ _TCCAccessCopyInformationForBundleId
+ _Transform
+ __CLASS_PROPERTIES__TtC9SEService33SESSettingsLocalizedStringFactory
+ __DATA__TtC9SEService10TCCContext
+ __DATA__TtC9SEService33SESSettingsLocalizedStringFactory
+ __DATA__TtC9SEServiceP33_DF7C6A441E5AB625BDF4896CC18BC9FD9FindClass
+ __IVARS__TtC9SEService10TCCContext
+ __METACLASS_DATA__TtC9SEService10TCCContext
+ __METACLASS_DATA__TtC9SEService33SESSettingsLocalizedStringFactory
+ __METACLASS_DATA__TtC9SEServiceP33_DF7C6A441E5AB625BDF4896CC18BC9FD9FindClass
+ __OBJC_$_CATEGORY_LSPropertyList_$_Entitlements
+ __OBJC_$_CLASS_METHODS_SESNFCAppSettingsContext
+ __OBJC_$_CLASS_METHODS__TtC9SEService10TCCContext
+ __OBJC_$_CLASS_METHODS__TtC9SEService33SESSettingsLocalizedStringFactory
+ __OBJC_$_INSTANCE_METHODS_LSPropertyList(Entitlements)
+ __OBJC_$_INSTANCE_METHODS_SESDefaultNFCApplication
+ __OBJC_$_INSTANCE_METHODS_SESNFCAppSettingsContext
+ __OBJC_$_INSTANCE_METHODS__TtC9SEService10TCCContext
+ __OBJC_$_INSTANCE_METHODS__TtC9SEService33SESSettingsLocalizedStringFactory
+ __OBJC_$_INSTANCE_METHODS__TtC9SEServiceP33_DF7C6A441E5AB625BDF4896CC18BC9FD9FindClass
+ __OBJC_$_INSTANCE_VARIABLES_SESDefaultNFCApplication
+ __OBJC_$_INSTANCE_VARIABLES_SESNFCAppSettingsContext
+ __OBJC_$_PROP_LIST_SESDefaultNFCApplication
+ __OBJC_$_PROP_LIST_SESNFCAppSettingsContext
+ __OBJC_CLASS_RO_$_SESDefaultNFCApplication
+ __OBJC_CLASS_RO_$_SESNFCAppSettingsContext
+ __OBJC_METACLASS_RO_$_SESDefaultNFCApplication
+ __OBJC_METACLASS_RO_$_SESNFCAppSettingsContext
+ ___45-[SESNFCAppSettingsContext readDefaultValues]_block_invoke
+ ___52-[SESNFCAppSettingsContext getDefaultNFCApplication]_block_invoke
+ ___53-[SESNFCAppSettingsContext setDefaultNFCApplication:]_block_invoke
+ ___56-[SESNFCAppSettingsContext localizedAppNameForBundleId:]_block_invoke
+ ___75-[SESNFCAppSettingsContext observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___block_descriptor_32_e22_16?0"NSDictionary"8l
+ ___block_descriptor_32_e8_16?08l
+ ___block_descriptor_40_e8_32s_e34_B16?0"SESDefaultNFCApplication"8ls32l8
+ ___block_literal_global.278
+ _associated conformance 9SEService10TCCContextC10TCCServiceOSHAASQ
+ _associated conformance 9SEService10TCCContextC9TCCAccessOSHAASQ
+ _associated conformance So11CFStringRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So11CFStringRefaSHSCSQ
+ _defaultAluminumEligbilityChangedContext
+ _defaultAppCandidatesChangedContext
+ _defaultAppChangedContext
+ _defaultHCEContext
+ _defaultSECContext
+ _kTCCInfoGranted
+ _kTCCInfoService
+ _kTCCServiceContactlessAccess
+ _kTCCServiceSecureElementAccess
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$bundleId
+ _objc_msgSend$checkTCCAccessWithoutLoadingTo:for:
+ _objc_msgSend$domain
+ _objc_msgSend$entitlements
+ _objc_msgSend$expressModeDefaultAlertMessagePostfix
+ _objc_msgSend$find:
+ _objc_msgSend$initWithBundleId:displayName:rawDomain:
+ _objc_msgSend$initWithBundleId:onChange:
+ _objc_msgSend$invalidateInternal
+ _objc_msgSend$isDefaultApp
+ _objc_msgSend$isDefaultAppEligibleForService:
+ _objc_msgSend$isDefaultAppTheOnlyCandidate
+ _objc_msgSend$isExpressModeEnabled
+ _objc_msgSend$isPassbookDefault
+ _objc_msgSend$localizedAppNameForBundleId:
+ _objc_msgSend$localizedDisplayName
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$observeDefaults
+ _objc_msgSend$passbookDefaultAlertMessage
+ _objc_msgSend$passbookNonTouchIDOnlyAlertMessagePrefix
+ _objc_msgSend$readDefaultValues
+ _objc_msgSend$reconcileWithRecord:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$ses_isEntitled:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shouldShowDoubleButtonPressToggle
+ _objc_msgSend$thirdPartyDefaultAlertMessage
+ _objc_msgSend$thirdPartyNonTouchIDOnlyAlertMessagePrefix
+ _objc_msgSend$ud
+ _objc_retainBlock
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_dynamicCastObjCClass
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_readAtKeyPath
+ _swift_setAtReferenceWritableKeyPath
+ _symbolic SDySS_____G 9SEService10TCCContextC9TCCAccessO
+ _symbolic SDySS_____GSg 9SEService10TCCContextC9TCCAccessO
+ _symbolic SDySS_____Gz_Xx 9SEService10TCCContextC9TCCAccessO
+ _symbolic SDy_____yXlG s11AnyHashableV
+ _symbolic _____ 9SEService10TCCContextC
+ _symbolic _____ 9SEService10TCCContextC10TCCServiceO
+ _symbolic _____ 9SEService10TCCContextC9TCCAccessO
+ _symbolic _____ 9SEService33SESSettingsLocalizedStringFactoryC
+ _symbolic _____ 9SEService9FindClass33_DF7C6A441E5AB625BDF4896CC18BC9FDLLC
+ _symbolic _____ So25tcc_authorization_right_ta
+ _symbolic _____ySS_____G s18_DictionaryStorageC 9SEService10TCCContextC9TCCAccessO
+ _tccHCEContext
+ _tccSECContext
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_subject_identity
+ _tcc_identity_get_identifier
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_service_singleton_for_CF_name
- +[SESSettingsEligiblity shouldShowLimitedContactlessPane]
- _isPassbookDefault
- _objc_msgSend$shouldShowLimitedContactlessPane
CStrings:
+ "\x01\x11!\x12"
+ "@\"NSUserDefaults\""
+ "@16@?0@\"NSDictionary\"8"
+ "@16@?0@8"
+ "B16@?0@\"SESDefaultNFCApplication\"8"
+ "B24@0:8Q16"
+ "Bundle ID %@ does not correspond to a record or error encountered %@"
+ "Bundle Id %@ is not a valid candidate"
+ "CHANGE_DEFAULT_CONTACTLESS_APP_ALERT_MESSAGE_3RD_PARTY"
+ "CHANGE_DEFAULT_CONTACTLESS_APP_ALERT_MESSAGE_PASSBOOK"
+ "Deallocating app settings context for bundle ID %@"
+ "EXPRESS_MODE_DEFAULT_APP_CHANGED_POSTFIX"
+ "Entitlements"
+ "Error %s while getting auth records for service %s"
+ "Failed to create tcc server"
+ "Found auth record for bundle ID %s with authorization %s for service %s"
+ "Invalidating app settings context for bundle ID %@"
+ "Key %@ changed, firing on visibility change for bundle Id %@"
+ "Loaded TCC information for service %s --> %s"
+ "Loading TCC information for %s"
+ "NON_TOUCH_ID_ONLY_DEFAULT_APP_CHANGE_PREFIX_3RD_PARTY"
+ "NON_TOUCH_ID_ONLY_DEFAULT_APP_CHANGE_PREFIX_PASSBOOK"
+ "No authorizationRecord / identity for tccService %s"
+ "No default app found in user defaults"
+ "Non-dictionary candidate found"
+ "Raw Express State 0x%llx"
+ "SESDefaultNFCApplication"
+ "SESNFCAppSettingsContext"
+ "SESSettings_Localizable"
+ "Successfully initialized app settings context for bundle ID %@"
+ "Successfully invalidated internally due to manual invalidation or dealloc"
+ "T@\"NSArray\",R,V_defaultAppCandidates"
+ "T@\"NSNumber\",R,V_domain"
+ "T@\"NSString\",R,V_bundleId"
+ "T@\"NSString\",R,V_localizedDisplayName"
+ "T@\"NSUserDefaults\",R,N,V_ud"
+ "TB,R,V_isContactlessTCCServiceEligible"
+ "TB,R,V_isSecureElementTCCServiceEligible"
+ "TB,R,V_shouldShowDefaultNFCAppPicker"
+ "TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED"
+ "TCC_AUTHORIZATION_RIGHT_ALLOWED"
+ "TCC_AUTHORIZATION_RIGHT_DENIED"
+ "TCC_AUTHORIZATION_RIGHT_LIMITED"
+ "TCC_AUTHORIZATION_RIGHT_SESSION_PID"
+ "TCC_AUTHORIZATION_RIGHT_UNKNOWN"
+ "TQ,R,V_doubleClickToggleVisibilityType"
+ "Unable to create tcc Service string %s"
+ "Unable to look up TCC for %{public}s"
+ "Unexpected data type for key %@, do not reconcile"
+ "_TtC9SEService10TCCContext"
+ "_TtC9SEService33SESSettingsLocalizedStringFactory"
+ "_TtC9SEServiceP33_DF7C6A441E5AB625BDF4896CC18BC9FD9FindClass"
+ "_bundleId"
+ "_currentDefaultBundleId"
+ "_defaultAppCandidates"
+ "_domain"
+ "_doubleClickToggleVisibilityType"
+ "_invalidated"
+ "_isContactlessTCCServiceEligible"
+ "_isDomainAluminumEligible"
+ "_isSecureElementTCCServiceEligible"
+ "_localizedDisplayName"
+ "_lock"
+ "_onChange"
+ "_shouldShowDefaultNFCAppPicker"
+ "_shouldShowHCEDefaultPane"
+ "_shouldShowHCETCCPane"
+ "_shouldShowSECDefaultPane"
+ "_shouldShowSECTCCPane"
+ "_supportsTouchID"
+ "_ud"
+ "addObserver:forKeyPath:options:context:"
+ "alertMessageForDefaultAppChangeTo:"
+ "aluminumEligibility"
+ "arrayForKey:"
+ "bundleForClass:"
+ "bundleId"
+ "checkTCCAccessTo:for:"
+ "checkTCCAccessWithoutLoadingTo:for:"
+ "com.apple.developer.nfc.hce"
+ "com.apple.developer.nfc.hce.default-contactless-app"
+ "com.apple.developer.secure-element-credential"
+ "com.apple.developer.secure-element-credential.default-contactless-app"
+ "com.apple.stockholm.express.state"
+ "contextWithBundleId:onChange:"
+ "contextWithBundleId:onChange: unable to initialize ud"
+ "defaultAppCandidates"
+ "defaultAppLocalizedName"
+ "displayName"
+ "domain"
+ "doubleClickEnabled"
+ "doubleClickToggleVisibilityType"
+ "entitlements"
+ "expressModeDefaultAlertMessagePostfix"
+ "find:"
+ "getDefaultNFCApplication"
+ "hceService"
+ "initWithBundleId:displayName:rawDomain:"
+ "initWithBundleId:onChange:"
+ "invalidateInternal"
+ "isDefaultApp"
+ "isDefaultAppEligibleForService:"
+ "isDefaultAppTheOnlyCandidate"
+ "isDoubleClickEnabled"
+ "isExpressModeEnabled"
+ "isPassbookDefault"
+ "localizedAppNameForBundleId:"
+ "localizedDisplayName"
+ "localizedStringForKey:value:table:"
+ "notify_cancel failed with status %d"
+ "notify_get_state failed with status %d"
+ "notify_register_check failed with status %d"
+ "objectForKey:ofClass:"
+ "observeDefaults"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "passbookDefaultAlertMessage"
+ "passbookNonTouchIDOnlyAlertMessagePrefix"
+ "q32@0:8q16@24"
+ "readDefaultValues"
+ "reconcileWithRecord:"
+ "removeObserver:forKeyPath:"
+ "secService"
+ "ses_isEntitled:"
+ "setDefaultNFCApplication:"
+ "setDoubleClickEnabled:"
+ "setValue:forKey:"
+ "shouldShowContactlessPane"
+ "shouldShowContactlessTcc"
+ "shouldShowDefaultNFCAppPicker"
+ "shouldShowDoubleButtonPressToggle"
+ "shouldShowSECPane"
+ "shouldShowSecureElementTcc"
+ "thirdPartyDefaultAlertMessage"
+ "thirdPartyNonTouchIDOnlyAlertMessagePrefix"
+ "touch-id"
+ "ud"
+ "v24@?0@\"<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "v48@0:8@16@24@32^v40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "Current default app bundle ID %@"
- "DefaultAppPane: %@ is default and passbook is isntalled when usable is ineligible, should show limited pane"
- "DefaultAppPane: Set Default eligible: %d, Use Default eligible: %d, Platform eligible: %d, Apps eligible: %d"
- "DefaultAppPane: Set Default ineligible -- default is %@, fell through?"
- "DefaultAppPane: no default when usable is ineligible, should not show limited pane"
- "DefaultAppPane: passbook is default when usable is ineligible, should not show limited pane"
- "Domain Silicon: isPassbookDefault returned error code %d -- Passbook is overriden as default"
- "Ineligible to use 3rd party default app -- Passbook is overriden as default"
- "SILICON returned %llu, ALUMINUM returned %llu"
- "Unable to initialize user default suite for isPassbookDefault -- Passbook is overriden as default"
- "should.show.contactless.pane"
- "should.show.contactless.tcc"
- "should.show.secure-element.tcc"
- "shouldShowLimitedContactlessPane"

```
