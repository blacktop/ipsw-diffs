## ManagedSettingsObjC

> `/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC`

```diff

-267.122.1.0.0
-  __TEXT.__text: 0x2e0fc
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x4104
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__cstring: 0x1372
+299.0.0.0.0
+  __TEXT.__text: 0x33b30
+  __TEXT.__objc_methlist: 0x488c
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x580
+  __TEXT.__cstring: 0x17cc
   __TEXT.__oslogstring: 0x1610
-  __TEXT.__unwind_info: 0xf28
-  __TEXT.__objc_classname: 0xd02
-  __TEXT.__objc_methname: 0x7255
-  __TEXT.__objc_methtype: 0x10cd
-  __TEXT.__objc_stubs: 0x24a0
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xa38
-  __DATA_CONST.__objc_classlist: 0x380
+  __TEXT.__unwind_info: 0x1218
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19b0
+  __DATA_CONST.__objc_selrefs: 0x1ca8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0x268
+  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__got: 0x418
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1f20
-  __AUTH_CONST.__objc_const: 0x8900
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x2f8
+  __AUTH_CONST.__cfstring: 0x25c0
+  __AUTH_CONST.__objc_const: 0x9620
+  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x36c
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x798
-  __DATA_DIRTY.__objc_data: 0x1ea0
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA.__bss: 0x8d0
+  __DATA_DIRTY.__objc_data: 0x1f40
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78E47E90-3CC5-3679-9280-E9A3750CE30E
-  Functions: 1457
-  Symbols:   5021
-  CStrings:  2059
+  UUID: D637F3E0-4183-3329-B705-B7FABEF9E488
+  Functions: 1616
+  Symbols:   5529
+  CStrings:  709
 
Symbols:
+ +[MOAppTCCDefaultsConfiguration convertDefaultsDictionaryToDictionary:]
+ +[MOAppTCCDefaultsConfiguration convertDictionaryToDefaultsDictionary:]
+ +[MOAppTCCDefaultsConfiguration(Persistence) initializeWithPersistableValue:]
+ +[MOAppTCCDefaultsConfiguration(Persistence) isValidPersistableRepresentation:]
+ +[MOApplicationSettingsGroup allowedApplicationsMetadata]
+ +[MOApplicationSettingsGroup allowedPartnerFinancingApplicationsMetadata]
+ +[MOApplicationSettingsGroup launchApplicationAllowlistMetadata]
+ +[MOApplicationSettingsGroup launchApplicationDenylistMetadata]
+ +[MOApplicationSettingsGroup launchRestrictedApplicationsMetadata]
+ +[MOApplicationSettingsGroup ratingExemptedApplicationsMetadata]
+ +[MOApplicationSettingsGroup unremovablePartnerFinancingApplicationsMetadata]
+ +[MOIntelligenceSettingsGroup denyPhotorealisticImageGenerationMetadata]
+ +[MOLaunchRestrictionRule(Persistence) initializeWithPersistableValue:]
+ +[MOLaunchRestrictionRule(Persistence) isValidPersistableRepresentation:]
+ +[MOPrivacySettingsGroup applicationTCCDefaultsMetadata]
+ +[MOSafariSettingsGroup websitePermissionDefaultsMetadata]
+ +[MOSiriSettingsGroup denySiri3489Metadata]
+ +[MOStandbySettingsGroup denyStandbyModeMetadata]
+ +[MOStandbySettingsGroup groupName]
+ +[MOWebContentFilterPolicy allWithTransitiveTrustPolicyWithExceptions:blockedDomains:]
+ +[MOWebContentFilterPolicy(Persistence) legacyPolicyFromAutoAllow:neverAllow:onlyAllow:]
+ +[MOWebContentFilterPolicy(Persistence) webDomainSetFromPersistedArray:]
+ +[MOWebContentSettingsGroup limitWebProxiesMetadata]
+ +[MOWebContentSettingsGroup overridePolicyMetadata]
+ +[MOWebsitePermissions convertDefaultsDictionaryToDictionary:]
+ +[MOWebsitePermissions convertDictionaryToDefaultsDictionary:]
+ +[MOWebsitePermissions(Persistence) initializeWithPersistableValue:]
+ +[MOWebsitePermissions(Persistence) isValidPersistableRepresentation:]
+ -[MOAppTCCDefaultsConfiguration .cxx_destruct]
+ -[MOAppTCCDefaultsConfiguration accessibility]
+ -[MOAppTCCDefaultsConfiguration bluetooth]
+ -[MOAppTCCDefaultsConfiguration camera]
+ -[MOAppTCCDefaultsConfiguration copyWithZone:]
+ -[MOAppTCCDefaultsConfiguration dictation]
+ -[MOAppTCCDefaultsConfiguration dictionaryRepresentation]
+ -[MOAppTCCDefaultsConfiguration hash]
+ -[MOAppTCCDefaultsConfiguration initWithAccessibility:bluetooth:camera:dictation:localNetwork:location:locationAccuracy:microphone:organizationJustification:]
+ -[MOAppTCCDefaultsConfiguration initWithDictionary:]
+ -[MOAppTCCDefaultsConfiguration isEqual:]
+ -[MOAppTCCDefaultsConfiguration localNetwork]
+ -[MOAppTCCDefaultsConfiguration locationAccuracy]
+ -[MOAppTCCDefaultsConfiguration location]
+ -[MOAppTCCDefaultsConfiguration microphone]
+ -[MOAppTCCDefaultsConfiguration organizationJustification]
+ -[MOAppTCCDefaultsConfiguration setAccessibility:]
+ -[MOAppTCCDefaultsConfiguration setBluetooth:]
+ -[MOAppTCCDefaultsConfiguration setCamera:]
+ -[MOAppTCCDefaultsConfiguration setDictation:]
+ -[MOAppTCCDefaultsConfiguration setLocalNetwork:]
+ -[MOAppTCCDefaultsConfiguration setLocation:]
+ -[MOAppTCCDefaultsConfiguration setLocationAccuracy:]
+ -[MOAppTCCDefaultsConfiguration setMicrophone:]
+ -[MOAppTCCDefaultsConfiguration setOrganizationJustification:]
+ -[MOAppTCCDefaultsConfiguration(Persistence) persistableValue]
+ -[MOApplicationSettingsGroup allowedApplications]
+ -[MOApplicationSettingsGroup allowedPartnerFinancingApplications]
+ -[MOApplicationSettingsGroup launchApplicationAllowlist]
+ -[MOApplicationSettingsGroup launchApplicationDenylist]
+ -[MOApplicationSettingsGroup launchRestrictedApplications]
+ -[MOApplicationSettingsGroup ratingExemptedApplications]
+ -[MOApplicationSettingsGroup setAllowedApplications:]
+ -[MOApplicationSettingsGroup setAllowedPartnerFinancingApplications:]
+ -[MOApplicationSettingsGroup setLaunchApplicationAllowlist:]
+ -[MOApplicationSettingsGroup setLaunchApplicationDenylist:]
+ -[MOApplicationSettingsGroup setLaunchRestrictedApplications:]
+ -[MOApplicationSettingsGroup setRatingExemptedApplications:]
+ -[MOApplicationSettingsGroup setUnremovablePartnerFinancingApplications:]
+ -[MOApplicationSettingsGroup unremovablePartnerFinancingApplications]
+ -[MOBatchSettingsStore commitChangesWithOutError:]
+ -[MOIntelligenceSettingsGroup denyPhotorealisticImageGeneration]
+ -[MOIntelligenceSettingsGroup setDenyPhotorealisticImageGeneration:]
+ -[MOInternalBatchSettingsStore commitChangesWithOutError:]
+ -[MOInternalLocalSettingsStore recordIdentifierLock]
+ -[MOInternalLocalSettingsStore recordIdentifier]
+ -[MOInternalLocalSettingsStore setRecordIdentifier:]
+ -[MOLaunchRestrictionRule .cxx_destruct]
+ -[MOLaunchRestrictionRule cdhash]
+ -[MOLaunchRestrictionRule copyWithZone:]
+ -[MOLaunchRestrictionRule hash]
+ -[MOLaunchRestrictionRule initWithCdhash:teamID:signingID:prefixPath:signingState:]
+ -[MOLaunchRestrictionRule isEqual:]
+ -[MOLaunchRestrictionRule isValidWithError:]
+ -[MOLaunchRestrictionRule prefixPath]
+ -[MOLaunchRestrictionRule signingID]
+ -[MOLaunchRestrictionRule signingState]
+ -[MOLaunchRestrictionRule teamID]
+ -[MOLaunchRestrictionRule(Persistence) persistableValue]
+ -[MOLaunchRestrictionRuleSetSettingMetadata defaultValue]
+ -[MOLaunchRestrictionRuleSetSettingMetadata persistableValueFromValue:]
+ -[MOLaunchRestrictionRuleSetSettingMetadata sanitizePersistableValue:]
+ -[MOLaunchRestrictionRuleSetSettingMetadata valueFromPersistableValue:]
+ -[MOLocalSettingsStore batchUpdate:outError:]
+ -[MOPrivacySettingsGroup applicationTCCDefaults]
+ -[MOPrivacySettingsGroup setApplicationTCCDefaults:]
+ -[MOSafariSettingsGroup setWebsitePermissionDefaults:]
+ -[MOSafariSettingsGroup websitePermissionDefaults]
+ -[MOSettingsStore standby]
+ -[MOSiriSettingsGroup denySiri3489]
+ -[MOSiriSettingsGroup setDenySiri3489:]
+ -[MOStandbySettingsGroup denyStandbyMode]
+ -[MOStandbySettingsGroup setDenyStandbyMode:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata .cxx_destruct]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _combine:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _combineAccuracyValue:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _combineConfiguration:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _combineGenericValue:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _combineLocationValue:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata _isAcceptablePersistedArrayElement:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata accuracyCombineOperator]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata combinePersistableValue:with:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata defaultValue]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata generalCombineOperator]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata initWithSettingName:defaultDictionary:generalCombineOperator:locationCombineOperator:accuracyCombineOperator:rankedGeneralValues:rankedLocationValues:rankedAccuracyValues:maximumCount:isPublic:scope:isPrivacySensitive:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata locationCombineOperator]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata maximumCount]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata persistableValueFromValue:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata rankedAccuracyValues]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata rankedGeneralValues]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata rankedLocationValues]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata sanitizePersistableValue:]
+ -[MOStringKeyAppTCCDefaultDictionarySettingMetadata valueFromPersistableValue:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata .cxx_destruct]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata _combine:with:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata _combineConfiguration:with:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata _combineGenericValue:with:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata _isAcceptablePersistedArrayElement:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata combinePersistableValue:with:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata defaultValue]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata generalCombineOperator]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata initWithSettingName:defaultDictionary:generalCombineOperator:rankedGeneralValues:maximumCount:isPublic:scope:isPrivacySensitive:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata maximumCount]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata persistableValueFromValue:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata rankedGeneralValues]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata sanitizePersistableValue:]
+ -[MOStringKeyWebsitePermissionsDictionarySettingMetadata valueFromPersistableValue:]
+ -[MOSystemBatchSettingsStore commitChangesWithOutError:]
+ -[MOSystemLocalSettingsStore batchUpdate:outError:]
+ -[MOWebContentFilterPolicy initWithPolicy:autoAllow:neverAllow:onlyAllow:]
+ -[MOWebContentSettingsGroup limitWebProxies]
+ -[MOWebContentSettingsGroup overridePolicy]
+ -[MOWebContentSettingsGroup setLimitWebProxies:]
+ -[MOWebContentSettingsGroup setOverridePolicy:]
+ -[MOWebsitePermissions .cxx_destruct]
+ -[MOWebsitePermissions camera]
+ -[MOWebsitePermissions copyWithZone:]
+ -[MOWebsitePermissions dictionaryRepresentation]
+ -[MOWebsitePermissions hash]
+ -[MOWebsitePermissions initWithCamera:microphone:organizationJustification:]
+ -[MOWebsitePermissions initWithDictionary:]
+ -[MOWebsitePermissions isEqual:]
+ -[MOWebsitePermissions microphone]
+ -[MOWebsitePermissions organizationJustification]
+ -[MOWebsitePermissions setCamera:]
+ -[MOWebsitePermissions setMicrophone:]
+ -[MOWebsitePermissions setOrganizationJustification:]
+ -[MOWebsitePermissions(Persistence) persistableValue]
+ GCC_except_table20
+ GCC_except_table29
+ GCC_except_table34
+ _MOGenericPermissionValueAllow
+ _MOGenericPermissionValueNone
+ _MOLaunchRestrictionRuleErrorDomain
+ _MOLocationAccuracyPermissionValueApproximate
+ _MOLocationAccuracyPermissionValueNone
+ _MOLocationAccuracyPermissionValuePrecise
+ _MOLocationPermissionValueAlways
+ _MOLocationPermissionValueNone
+ _MOLocationPermissionValueWhileUsing
+ _MOPermissionKeyAccessibility
+ _MOPermissionKeyBluetooth
+ _MOPermissionKeyCamera
+ _MOPermissionKeyDictation
+ _MOPermissionKeyLocalNetwork
+ _MOPermissionKeyLocation
+ _MOPermissionKeyLocationAccuracy
+ _MOPermissionKeyMicrophone
+ _MOPermissionKeyOrganizationJustification
+ _MOPersistenceKeyCDHash
+ _MOPersistenceKeyPrefixPath
+ _MOPersistenceKeySigningID
+ _MOPersistenceKeySigningState
+ _MOPersistenceKeyTeamID
+ _MOSettingsGroupNameStandby
+ _MOSigningStateAll
+ _MOSigningStateAppStore
+ _MOSigningStateApple
+ _MOSigningStateDeveloperID
+ _MOSigningStateEnterprise
+ _MOSigningStateTestFlight
+ _MOWebContentOverridePolicyAskForPermission
+ _MOWebContentOverridePolicyLocalApprovalOnly
+ _MOWebContentOverridePolicyNotAllowed
+ _MOWebContentOverridePolicyUnverifiedAdultLegacyScreenTime
+ _MOWebContentOverridePolicyUnverifiedAdultScreenTime
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_MOAppTCCDefaultsConfiguration
+ _OBJC_CLASS_$_MOLaunchRestrictionRule
+ _OBJC_CLASS_$_MOLaunchRestrictionRuleSetSettingMetadata
+ _OBJC_CLASS_$_MOStandbySettingsGroup
+ _OBJC_CLASS_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ _OBJC_CLASS_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ _OBJC_CLASS_$_MOWebsitePermissions
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._accessibility
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._bluetooth
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._camera
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._dictation
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._localNetwork
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._location
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._locationAccuracy
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._microphone
+ _OBJC_IVAR_$_MOAppTCCDefaultsConfiguration._organizationJustification
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._recordIdentifier
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._recordIdentifierLock
+ _OBJC_IVAR_$_MOLaunchRestrictionRule._cdhash
+ _OBJC_IVAR_$_MOLaunchRestrictionRule._prefixPath
+ _OBJC_IVAR_$_MOLaunchRestrictionRule._signingID
+ _OBJC_IVAR_$_MOLaunchRestrictionRule._signingState
+ _OBJC_IVAR_$_MOLaunchRestrictionRule._teamID
+ _OBJC_IVAR_$_MOSettingsStore._standby
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._accuracyCombineOperator
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._generalCombineOperator
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._locationCombineOperator
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._maximumCount
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._rankedAccuracyValues
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._rankedGeneralValues
+ _OBJC_IVAR_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata._rankedLocationValues
+ _OBJC_IVAR_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata._generalCombineOperator
+ _OBJC_IVAR_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata._maximumCount
+ _OBJC_IVAR_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata._rankedGeneralValues
+ _OBJC_IVAR_$_MOWebsitePermissions._camera
+ _OBJC_IVAR_$_MOWebsitePermissions._microphone
+ _OBJC_IVAR_$_MOWebsitePermissions._organizationJustification
+ _OBJC_METACLASS_$_MOAppTCCDefaultsConfiguration
+ _OBJC_METACLASS_$_MOLaunchRestrictionRule
+ _OBJC_METACLASS_$_MOLaunchRestrictionRuleSetSettingMetadata
+ _OBJC_METACLASS_$_MOStandbySettingsGroup
+ _OBJC_METACLASS_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ _OBJC_METACLASS_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ _OBJC_METACLASS_$_MOWebsitePermissions
+ __OBJC_$_CLASS_METHODS_MOAppTCCDefaultsConfiguration(Persistence)
+ __OBJC_$_CLASS_METHODS_MOLaunchRestrictionRule(Persistence)
+ __OBJC_$_CLASS_METHODS_MOStandbySettingsGroup
+ __OBJC_$_CLASS_METHODS_MOWebsitePermissions(Persistence)
+ __OBJC_$_CLASS_PROP_LIST_MOStandbySettingsGroup
+ __OBJC_$_INSTANCE_METHODS_MOAppTCCDefaultsConfiguration(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOLaunchRestrictionRule(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOLaunchRestrictionRuleSetSettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOStandbySettingsGroup
+ __OBJC_$_INSTANCE_METHODS_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOWebsitePermissions(Persistence)
+ __OBJC_$_INSTANCE_VARIABLES_MOAppTCCDefaultsConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_MOLaunchRestrictionRule
+ __OBJC_$_INSTANCE_VARIABLES_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOWebsitePermissions
+ __OBJC_$_PROP_LIST_MOLaunchRestrictionRuleSetSettingMetadata
+ __OBJC_$_PROP_LIST_MOStandbySettingsGroup
+ __OBJC_$_PROP_LIST_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ __OBJC_$_PROP_LIST_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ __OBJC_CLASS_PROTOCOLS_$_MOAppTCCDefaultsConfiguration(Persistence)
+ __OBJC_CLASS_PROTOCOLS_$_MOLaunchRestrictionRule(Persistence)
+ __OBJC_CLASS_PROTOCOLS_$_MOWebsitePermissions(Persistence)
+ __OBJC_CLASS_RO_$_MOAppTCCDefaultsConfiguration
+ __OBJC_CLASS_RO_$_MOLaunchRestrictionRule
+ __OBJC_CLASS_RO_$_MOLaunchRestrictionRuleSetSettingMetadata
+ __OBJC_CLASS_RO_$_MOStandbySettingsGroup
+ __OBJC_CLASS_RO_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ __OBJC_CLASS_RO_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ __OBJC_CLASS_RO_$_MOWebsitePermissions
+ __OBJC_METACLASS_RO_$_MOAppTCCDefaultsConfiguration
+ __OBJC_METACLASS_RO_$_MOLaunchRestrictionRule
+ __OBJC_METACLASS_RO_$_MOLaunchRestrictionRuleSetSettingMetadata
+ __OBJC_METACLASS_RO_$_MOStandbySettingsGroup
+ __OBJC_METACLASS_RO_$_MOStringKeyAppTCCDefaultDictionarySettingMetadata
+ __OBJC_METACLASS_RO_$_MOStringKeyWebsitePermissionsDictionarySettingMetadata
+ __OBJC_METACLASS_RO_$_MOWebsitePermissions
+ ___43+[MOSiriSettingsGroup denySiri3489Metadata]_block_invoke
+ ___49+[MOStandbySettingsGroup denyStandbyModeMetadata]_block_invoke
+ ___51+[MOWebContentSettingsGroup overridePolicyMetadata]_block_invoke
+ ___52+[MOWebContentSettingsGroup limitWebProxiesMetadata]_block_invoke
+ ___56+[MOPrivacySettingsGroup applicationTCCDefaultsMetadata]_block_invoke
+ ___57+[MOApplicationSettingsGroup allowedApplicationsMetadata]_block_invoke
+ ___58+[MOSafariSettingsGroup websitePermissionDefaultsMetadata]_block_invoke
+ ___58-[MOInternalBatchSettingsStore commitChangesWithOutError:]_block_invoke
+ ___58-[MOInternalBatchSettingsStore commitChangesWithOutError:]_block_invoke.16
+ ___58-[MOInternalBatchSettingsStore commitChangesWithOutError:]_block_invoke.16.cold.1
+ ___58-[MOInternalBatchSettingsStore commitChangesWithOutError:]_block_invoke.cold.1
+ ___63+[MOApplicationSettingsGroup launchApplicationDenylistMetadata]_block_invoke
+ ___64+[MOApplicationSettingsGroup launchApplicationAllowlistMetadata]_block_invoke
+ ___64+[MOApplicationSettingsGroup ratingExemptedApplicationsMetadata]_block_invoke
+ ___66+[MOApplicationSettingsGroup launchRestrictedApplicationsMetadata]_block_invoke
+ ___72+[MOIntelligenceSettingsGroup denyPhotorealisticImageGenerationMetadata]_block_invoke
+ ___73+[MOApplicationSettingsGroup allowedPartnerFinancingApplicationsMetadata]_block_invoke
+ ___77+[MOApplicationSettingsGroup unremovablePartnerFinancingApplicationsMetadata]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSUUID"8"NSError"16ls32l8r40l8
+ ___block_literal_global.86
+ _allowedApplicationsMetadata.metadata
+ _allowedApplicationsMetadata.onceToken
+ _allowedPartnerFinancingApplicationsMetadata.metadata
+ _allowedPartnerFinancingApplicationsMetadata.onceToken
+ _applicationTCCDefaultsMetadata.metadata
+ _applicationTCCDefaultsMetadata.onceToken
+ _denyPhotorealisticImageGenerationMetadata.metadata
+ _denyPhotorealisticImageGenerationMetadata.onceToken
+ _denySiri3489Metadata.metadata
+ _denySiri3489Metadata.onceToken
+ _denyStandbyModeMetadata.metadata
+ _denyStandbyModeMetadata.onceToken
+ _launchApplicationAllowlistMetadata.metadata
+ _launchApplicationAllowlistMetadata.onceToken
+ _launchApplicationDenylistMetadata.metadata
+ _launchApplicationDenylistMetadata.onceToken
+ _launchRestrictedApplicationsMetadata.metadata
+ _launchRestrictedApplicationsMetadata.onceToken
+ _limitWebProxiesMetadata.metadata
+ _limitWebProxiesMetadata.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_combineAccuracyValue:with:
+ _objc_msgSend$_combineConfiguration:with:
+ _objc_msgSend$_combineGenericValue:with:
+ _objc_msgSend$_combineLocationValue:with:
+ _objc_msgSend$accessibility
+ _objc_msgSend$batchUpdate:outError:
+ _objc_msgSend$bluetooth
+ _objc_msgSend$camera
+ _objc_msgSend$cdhash
+ _objc_msgSend$commitChangesWithOutError:
+ _objc_msgSend$dictation
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$initWithAccessibility:bluetooth:camera:dictation:localNetwork:location:locationAccuracy:microphone:organizationJustification:
+ _objc_msgSend$initWithCamera:microphone:organizationJustification:
+ _objc_msgSend$initWithCdhash:teamID:signingID:prefixPath:signingState:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithPolicy:autoAllow:neverAllow:onlyAllow:
+ _objc_msgSend$initWithSettingName:defaultDictionary:generalCombineOperator:locationCombineOperator:accuracyCombineOperator:rankedGeneralValues:rankedLocationValues:rankedAccuracyValues:maximumCount:isPublic:scope:isPrivacySensitive:
+ _objc_msgSend$initWithSettingName:defaultDictionary:generalCombineOperator:rankedGeneralValues:maximumCount:isPublic:scope:isPrivacySensitive:
+ _objc_msgSend$isAbsolutePath
+ _objc_msgSend$legacyPolicyFromAutoAllow:neverAllow:onlyAllow:
+ _objc_msgSend$localNetwork
+ _objc_msgSend$location
+ _objc_msgSend$locationAccuracy
+ _objc_msgSend$microphone
+ _objc_msgSend$organizationJustification
+ _objc_msgSend$prefixPath
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setAccessibility:
+ _objc_msgSend$setBluetooth:
+ _objc_msgSend$setCamera:
+ _objc_msgSend$setDictation:
+ _objc_msgSend$setLocalNetwork:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setLocationAccuracy:
+ _objc_msgSend$setMicrophone:
+ _objc_msgSend$setOrganizationJustification:
+ _objc_msgSend$signingID
+ _objc_msgSend$signingState
+ _objc_msgSend$teamID
+ _objc_msgSend$webDomainSetFromPersistedArray:
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_setProperty_atomic
+ _overridePolicyMetadata.metadata
+ _overridePolicyMetadata.onceToken
+ _ratingExemptedApplicationsMetadata.metadata
+ _ratingExemptedApplicationsMetadata.onceToken
+ _unremovablePartnerFinancingApplicationsMetadata.metadata
+ _unremovablePartnerFinancingApplicationsMetadata.onceToken
+ _websitePermissionDefaultsMetadata.metadata
+ _websitePermissionDefaultsMetadata.onceToken
- -[MOBatchSettingsStore commitChanges]
- -[MOInternalBatchSettingsStore commitChanges]
- -[MOSystemBatchSettingsStore commitChanges]
- -[MOWebContentFilterPolicy initWithAutoAllow:neverAllow:onlyAllow:]
- GCC_except_table32
- _OBJC_IVAR_$_MOInternalLocalSettingsStore._persistenceRecordIdentifier
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke
- ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.16
- ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.16.cold.1
- ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.cold.1
- ___block_literal_global.87
- _objc_msgSend$commitChanges
- _objc_msgSend$initWithAutoAllow:neverAllow:onlyAllow:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "3"
+ "Accessibility"
+ "Allow"
+ "Always"
+ "Approximate"
+ "Bluetooth"
+ "Camera"
+ "Dictation"
+ "LocalNetwork"
+ "Location"
+ "LocationAccuracy"
+ "MOLaunchRestrictionRuleErrorDomain"
+ "Microphone"
+ "None"
+ "OrganizationJustification"
+ "Precise"
+ "WhileUsing"
+ "^([A-Z0-9]{10,64})?$"
+ "^[0-9a-fA-F]{40}$"
+ "^[a-zA-Z0-9._-]{1,255}$"
+ "allowedApplications"
+ "allowedPartnerFinancingApplications"
+ "apple"
+ "applicationTCCDefaults"
+ "askForPermission"
+ "at least one of cdhash, teamID, or signingID must be specified"
+ "cdhash"
+ "cdhash must be 40-character hexadecimal"
+ "denyPhotorealisticImageGeneration"
+ "denySiri3489"
+ "denyStandbyMode"
+ "developerID"
+ "enterprise"
+ "launchApplicationAllowlist"
+ "launchApplicationDenylist"
+ "launchRestrictedApplications"
+ "limitWebProxies"
+ "localApprovalOnly"
+ "notAllowed"
+ "overridePolicy"
+ "prefixPath"
+ "prefixPath must be an absolute path"
+ "ratingExemptedApplications"
+ "signingID"
+ "signingID must be 1-255 alphanumeric, periods, or hyphens"
+ "signingState"
+ "standby"
+ "teamID"
+ "teamID must be 10-64 uppercase alphanumeric characters"
+ "testFlight"
+ "unremovablePartnerFinancingApplications"
+ "unverifiedAdultLegacyScreenTime"
+ "unverifiedAdultScreenTime"
+ "websitePermissionDefaults"
+ "\xf0\xf0\""
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<MOSettingsReader>\""
- "@\"<MOSettingsWriter>\""
- "@\"<MOSubscription>\""
- "@\"MOAccountSettingsGroup\""
- "@\"MOAirDropSettingsGroup\""
- "@\"MOAllowedClientSettingsGroup\""
- "@\"MOAppStoreSettingsGroup\""
- "@\"MOApplication\""
- "@\"MOApplicationSettingsGroup\""
- "@\"MOCalculatorSettingsGroup\""
- "@\"MOCameraSettingsGroup\""
- "@\"MOCarPlaySettingsGroup\""
- "@\"MOCategoryShieldPolicy\""
- "@\"MOCellularSettingsGroup\""
- "@\"MODateAndTimeSettingsGroup\""
- "@\"MODeviceActivitySettingsGroup\""
- "@\"MOEffectiveAccountSettings\""
- "@\"MOEffectiveAllowedClientSettings\""
- "@\"MOEffectiveSettingsStore\""
- "@\"MOEffectiveShieldSettings\""
- "@\"MOEffectiveUserSettings\""
- "@\"MOEyeReliefSettingsGroup\""
- "@\"MOFaceTimeSettingsGroup\""
- "@\"MOFindMySettingsGroup\""
- "@\"MOGameCenterSettingsGroup\""
- "@\"MOIntelligenceSettingsGroup\""
- "@\"MOInternalBatchSettingsStore\""
- "@\"MOInternalLocalSettingsStore\""
- "@\"MOKeyboardSettingsGroup\""
- "@\"MOManagedSettingsSettingsGroup\""
- "@\"MOMediaSettingsGroup\""
- "@\"MOMessagesSettingsGroup\""
- "@\"MONewsSettingsGroup\""
- "@\"MONotificationSettingsGroup\""
- "@\"MOPasscodeSettingsGroup\""
- "@\"MOPassthroughSubject\""
- "@\"MOPrivacySettingsGroup\""
- "@\"MOPublisher\""
- "@\"MOSafariSettingsGroup\""
- "@\"MOScreenTimeSettingsGroup\""
- "@\"MOSettingsPublisherBase\""
- "@\"MOShieldLabel\""
- "@\"MOShieldSettingsGroup\""
- "@\"MOSiriSettingsGroup\""
- "@\"MOSubscriber\""
- "@\"MOSystemAudioAccessorySettingsGroup\""
- "@\"MOUnpairingTime\""
- "@\"MOUserSafetySettingsGroup\""
- "@\"MOUserSettingsGroup\""
- "@\"MOWebContentFilterPolicy\""
- "@\"MOWebContentSettingsGroup\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUUID\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"NSXPCConnection\"16@0:8"
- "@\"NSXPCConnection\"24@0:8@\"<MOManagedSettingsSubscriberProxy>\"16"
- "@\"NSXPCInterface\"16@0:8"
- "@16@0:8"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@\"NSString\"16@\"NSString\"24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@?16@?24"
- "@32@0:8Q16@24"
- "@32@0:8q16@24"
- "@32@0:8q16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8q16@24@32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24@?32#40"
- "@48@0:8@16@24@?32@?40"
- "@48@0:8@16@24B32@36B44"
- "@52@0:8@16B24q28B36@40B48"
- "@56@0:8@16@24q32B40@44B52"
- "@64@0:8@16@24Q32Q40B48@52B60"
- "@64@0:8@16@24q32@40B48@52B60"
- "@64@0:8@16@24q32Q40B48@52B60"
- "@72@0:8@16@24Q32Q40Q48B56@60B68"
- "@72@0:8@16@24q32@40Q48B56@60B68"
- "@72@0:8@16q24q32q40q48B56@60B68"
- "@80@0:8@16@24#32q40@48Q56B64@68B76"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8B16B20"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@24^B32"
- "B40@0:8@16^@24^@32"
- "EventStream"
- "MOAccountSettingsGroup"
- "MOAirDropSettingsGroup"
- "MOAllowedClientSettingsGroup"
- "MOAppStoreSettingsGroup"
- "MOApplication"
- "MOApplicationCategoryShieldPolicy"
- "MOApplicationCategoryShieldPolicySettingMetadata"
- "MOApplicationSetSettingMetadata"
- "MOApplicationSettingMetadata"
- "MOApplicationSettingsGroup"
- "MOArraySettingMetadata"
- "MOAudioAccessoryTemporaryPairingConfiguration"
- "MOBatchSettingsStore"
- "MOBlameFinderProxy"
- "MOBookmark"
- "MOBookmarkSource"
- "MOBookmarkSourceArraySettingMetadata"
- "MOBoolSettingMetadata"
- "MOCalculatorSettingsGroup"
- "MOCameraSettingsGroup"
- "MOCancellable"
- "MOCarPlaySettingsGroup"
- "MOCategory"
- "MOCategoryShieldPolicy"
- "MOCellularSettingsGroup"
- "MOCompletion"
- "MODataSetSettingMetadata"
- "MODataSettingMetadata"
- "MODateAndTimeSettingsGroup"
- "MODeviceActivitySettingsGroup"
- "MODiagnosticsCollector"
- "MOEffectiveAccountSettings"
- "MOEffectiveAllowedClientSettings"
- "MOEffectiveApplicationSettings"
- "MOEffectiveApplicationSettingsProxy"
- "MOEffectiveArray"
- "MOEffectiveBool"
- "MOEffectiveCategoryShieldPolicy"
- "MOEffectiveData"
- "MOEffectiveInteger"
- "MOEffectiveOptionalApplication"
- "MOEffectivePublisher"
- "MOEffectiveSettings"
- "MOEffectiveSettingsStore"
- "MOEffectiveShieldSettings"
- "MOEffectiveShieldSettingsProxy"
- "MOEffectiveString"
- "MOEffectiveUserSettings"
- "MOEffectiveWebContentFilterPolicy"
- "MOEyeReliefSettingsGroup"
- "MOFaceTimeSettingsGroup"
- "MOFindMySettingsGroup"
- "MOGameCenterSettingsGroup"
- "MOIdentifiable"
- "MOIntegerSettingMetadata"
- "MOIntelligenceSettingsGroup"
- "MOInternalBatchSettingsStore"
- "MOInternalLocalSettingsStore"
- "MOKeyboardSettingsGroup"
- "MOLocalSettingsStore"
- "MOLocatable"
- "MOLocations"
- "MOLogger"
- "MOManagedSettingsAgent"
- "MOManagedSettingsAgentConnection"
- "MOManagedSettingsAgentPublisherConnection"
- "MOManagedSettingsConnection"
- "MOManagedSettingsProxy"
- "MOManagedSettingsPublisherConnection"
- "MOManagedSettingsPublisherProxy"
- "MOManagedSettingsSettingsGroup"
- "MOManagedSettingsSubscriberProxy"
- "MOManagedSettingsSystemAgent"
- "MOManagedSettingsSystemAgentConnection"
- "MOManagedSettingsSystemAgentPublisherConnection"
- "MOMediaSettingsGroup"
- "MOMessagesSettingsGroup"
- "MONewsSettingsGroup"
- "MONotificationSettingsGroup"
- "MOPasscodeSettingsGroup"
- "MOPassthroughSubject"
- "MOPassthroughSubjectConduit"
- "MOPersistable"
- "MOPersistableKeyStringDictionarySettingMetadata"
- "MOPrivacySettingsGroup"
- "MOPublisher"
- "MOSafariSettingsGroup"
- "MOScreenTimeSettingsGroup"
- "MOSetSettingMetadata"
- "MOSettingMetadata"
- "MOSettingsGroup"
- "MOSettingsPublisherBase"
- "MOSettingsPublisherConduit"
- "MOSettingsReader"
- "MOSettingsStore"
- "MOSettingsWriter"
- "MOShieldConfiguration"
- "MOShieldLabel"
- "MOShieldSettingsGroup"
- "MOSink"
- "MOSiriSettingsGroup"
- "MOStringSetSettingMetadata"
- "MOStringSettingMetadata"
- "MOSubject"
- "MOSubscriber"
- "MOSubscription"
- "MOSubscriptionCenter"
- "MOSystemAudioAccessorySettingsGroup"
- "MOSystemBatchSettingsStore"
- "MOSystemEffectiveSettingsStore"
- "MOSystemLocalSettingsStore"
- "MOSystemLocations"
- "MOSystemSettingsStore"
- "MOTemporaryPairingConfigurationSettingMetadata"
- "MOUnpairingTime"
- "MOUserSafetyScanningPolicy"
- "MOUserSafetyScanningPolicySettingMetadata"
- "MOUserSafetySettingsGroup"
- "MOUserSettingsGroup"
- "MOWebContentFilterPolicy"
- "MOWebContentFilterPolicySettingMetadata"
- "MOWebContentSettingsGroup"
- "MOWebDomain"
- "MOWebDomainCategoryShieldPolicy"
- "MOWebDomainCategoryShieldPolicySettingMetadata"
- "MOWebDomainSetSettingMetadata"
- "MOWebNewPage"
- "MOWebNewPageSettingMetadata"
- "MOXPCRemoteObjectProxy"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Persistence"
- "PersistenceInternal"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T#,R,N,V_connectionClass"
- "T#,R,N,V_persistableKeyClass"
- "T@\"<MOSettingsReader>\",R,W,V_settingsReader"
- "T@\"<MOSettingsReader>\",W,N,V_settingsReader"
- "T@\"<MOSettingsWriter>\",R,W,V_settingsWriter"
- "T@\"<MOSettingsWriter>\",W,N,V_settingsWriter"
- "T@\"<MOSubscription>\",R,N,V_subscription"
- "T@\"<MOSubscription>\",R,N,V_upstream"
- "T@\"MOAccountSettingsGroup\",R,N,V_account"
- "T@\"MOAirDropSettingsGroup\",R,N,V_airDrop"
- "T@\"MOAllowedClientSettingsGroup\",R,N,V_allowedClient"
- "T@\"MOAppStoreSettingsGroup\",R,N,V_appStore"
- "T@\"MOApplication\",&,N"
- "T@\"MOApplication\",R,N"
- "T@\"MOApplication\",R,V_defaultValue"
- "T@\"MOApplication\",R,V_value"
- "T@\"MOApplicationCategoryShieldPolicy\",&,N"
- "T@\"MOApplicationCategoryShieldPolicy\",R,N"
- "T@\"MOApplicationCategoryShieldPolicySettingMetadata\",R,N"
- "T@\"MOApplicationSetSettingMetadata\",R,N"
- "T@\"MOApplicationSettingMetadata\",R,N"
- "T@\"MOApplicationSettingsGroup\",R,N,V_application"
- "T@\"MOAudioAccessoryTemporaryPairingConfiguration\",&,N"
- "T@\"MOAudioAccessoryTemporaryPairingConfiguration\",R,N"
- "T@\"MOBookmarkSourceArraySettingMetadata\",R,N"
- "T@\"MOBoolSettingMetadata\",R,N"
- "T@\"MOCalculatorSettingsGroup\",R,N,V_calculator"
- "T@\"MOCameraSettingsGroup\",R,N,V_camera"
- "T@\"MOCarPlaySettingsGroup\",R,N,V_carPlay"
- "T@\"MOCategory\",R"
- "T@\"MOCategoryShieldPolicy\",R,V_defaultValue"
- "T@\"MOCategoryShieldPolicy\",R,V_value"
- "T@\"MOCellularSettingsGroup\",R,N,V_cellular"
- "T@\"MODataSetSettingMetadata\",R,N"
- "T@\"MODataSettingMetadata\",R,N"
- "T@\"MODateAndTimeSettingsGroup\",R,N,V_dateAndTime"
- "T@\"MODeviceActivitySettingsGroup\",R,N,V_deviceActivity"
- "T@\"MOEffectiveAccountSettings\",R,V_account"
- "T@\"MOEffectiveAllowedClientSettings\",R,V_allowedClient"
- "T@\"MOEffectiveArray\",R"
- "T@\"MOEffectiveBool\",R"
- "T@\"MOEffectiveCategoryShieldPolicy\",R"
- "T@\"MOEffectiveOptionalApplication\",R"
- "T@\"MOEffectiveSettingsStore\",R,V_store"
- "T@\"MOEffectiveShieldSettings\",R,V_shield"
- "T@\"MOEffectiveString\",R"
- "T@\"MOEffectiveUserSettings\",R,V_user"
- "T@\"MOEyeReliefSettingsGroup\",R,N,V_eyeRelief"
- "T@\"MOFaceTimeSettingsGroup\",R,N,V_faceTime"
- "T@\"MOFindMySettingsGroup\",R,N,V_findMy"
- "T@\"MOGameCenterSettingsGroup\",R,N,V_gameCenter"
- "T@\"MOIntegerSettingMetadata\",R,N"
- "T@\"MOIntelligenceSettingsGroup\",R,N,V_intelligence"
- "T@\"MOInternalBatchSettingsStore\",R,N,V_internalStore"
- "T@\"MOInternalLocalSettingsStore\",R,N,V_internalStore"
- "T@\"MOKeyboardSettingsGroup\",R,N,V_keyboard"
- "T@\"MOManagedSettingsSettingsGroup\",R,N,V_managedSettings"
- "T@\"MOMediaSettingsGroup\",R,N,V_media"
- "T@\"MOMessagesSettingsGroup\",R,N,V_messages"
- "T@\"MONewsSettingsGroup\",R,N,V_news"
- "T@\"MONotificationSettingsGroup\",R,N,V_notification"
- "T@\"MOPasscodeSettingsGroup\",R,N,V_passcode"
- "T@\"MOPassthroughSubject\",R,N,V_effectiveSubject"
- "T@\"MOPassthroughSubject\",R,W,N,V_parent"
- "T@\"MOPersistableKeyStringDictionarySettingMetadata\",R,N"
- "T@\"MOPrivacySettingsGroup\",R,N,V_privacy"
- "T@\"MOPublisher\",R,N,V_upstream"
- "T@\"MOSafariSettingsGroup\",R,N,V_safari"
- "T@\"MOScreenTimeSettingsGroup\",R,N,V_screenTime"
- "T@\"MOSettingsPublisherBase\",R,N,V_base"
- "T@\"MOShieldLabel\",R,V_primaryButtonLabel"
- "T@\"MOShieldLabel\",R,V_secondaryButtonLabel"
- "T@\"MOShieldLabel\",R,V_subtitle"
- "T@\"MOShieldLabel\",R,V_title"
- "T@\"MOShieldSettingsGroup\",R,N,V_shield"
- "T@\"MOSiriSettingsGroup\",R,N,V_siri"
- "T@\"MOStringSetSettingMetadata\",R,N"
- "T@\"MOStringSettingMetadata\",R,N"
- "T@\"MOSubscriber\",R,W,N,V_downstream"
- "T@\"MOSubscriptionCenter\",R,N"
- "T@\"MOSystemAudioAccessorySettingsGroup\",R,N,V_audioAccessory"
- "T@\"MOTemporaryPairingConfigurationSettingMetadata\",R,N"
- "T@\"MOUnpairingTime\",R,V_unpairingTime"
- "T@\"MOUserSafetyScanningPolicy\",&,N"
- "T@\"MOUserSafetyScanningPolicy\",R,N"
- "T@\"MOUserSafetyScanningPolicySettingMetadata\",R,N"
- "T@\"MOUserSafetySettingsGroup\",R,N,V_userSafety"
- "T@\"MOUserSettingsGroup\",R,N,V_user"
- "T@\"MOWebContentFilterPolicy\",&,N"
- "T@\"MOWebContentFilterPolicy\",R,N"
- "T@\"MOWebContentFilterPolicy\",R,V_defaultValue"
- "T@\"MOWebContentFilterPolicy\",R,V_value"
- "T@\"MOWebContentFilterPolicySettingMetadata\",R,N"
- "T@\"MOWebContentSettingsGroup\",R,N,V_webContent"
- "T@\"MOWebDomainCategoryShieldPolicy\",&,N"
- "T@\"MOWebDomainCategoryShieldPolicy\",R,N"
- "T@\"MOWebDomainCategoryShieldPolicySettingMetadata\",R,N"
- "T@\"MOWebDomainSetSettingMetadata\",R,N"
- "T@\"MOWebNewPage\",&,N"
- "T@\"MOWebNewPage\",R,N"
- "T@\"MOWebNewPageSettingMetadata\",R,N"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",R,C,V_secondaryButtonSubmenuItems"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,V_children"
- "T@\"NSArray\",R,V_defaultValue"
- "T@\"NSArray\",R,V_excludedContent"
- "T@\"NSArray\",R,V_specificCategories"
- "T@\"NSArray\",R,V_value"
- "T@\"NSData\",&,N"
- "T@\"NSData\",R,C,V_backgroundColorData"
- "T@\"NSData\",R,C,V_backgroundEffectData"
- "T@\"NSData\",R,C,V_colorData"
- "T@\"NSData\",R,C,V_iconData"
- "T@\"NSData\",R,C,V_primaryButtonColorData"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,V_defaultValue"
- "T@\"NSData\",R,V_value"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_rankedAllowedValues"
- "T@\"NSDictionary\",R,N,V_rankedInterventionTypes"
- "T@\"NSDictionary\",R,V_allApplications"
- "T@\"NSDictionary\",R,V_allServices"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSMutableArray\",R,V_children"
- "T@\"NSMutableDictionary\",&,N,V_updatedProperties"
- "T@\"NSMutableDictionary\",&,N,V_updatedSettings"
- "T@\"NSMutableDictionary\",R,N,V_downstreams"
- "T@\"NSMutableDictionary\",R,N,V_effectiveSubscriptions"
- "T@\"NSMutableSet\",&,N,V_removedSettings"
- "T@\"NSNumber\",&,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSNumber\",R,V_hour"
- "T@\"NSObject\",R,N,V_connectionLock"
- "T@\"NSObject\",R,N,V_lock"
- "T@\"NSObject\",R,N,V_settingsLock"
- "T@\"NSObject\",R,N,V_subscriptionLock"
- "T@\"NSObject<OS_os_log>\",R,N"
- "T@\"NSSet\",&,N"
- "T@\"NSSet\",R"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_interestedGroups"
- "T@\"NSSet\",R,V_autoAllow"
- "T@\"NSSet\",R,V_neverAllow"
- "T@\"NSSet\",R,V_onlyAllow"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_container"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,V_text"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_scope"
- "T@\"NSString\",R,N,V_settingName"
- "T@\"NSString\",R,V_bookmark"
- "T@\"NSString\",R,V_bundleIdentifier"
- "T@\"NSString\",R,V_defaultValue"
- "T@\"NSString\",R,V_domain"
- "T@\"NSString\",R,V_extensionIdentifier"
- "T@\"NSString\",R,V_homepageURL"
- "T@\"NSString\",R,V_identifier"
- "T@\"NSString\",R,V_interventionType"
- "T@\"NSString\",R,V_sourceIdentifier"
- "T@\"NSString\",R,V_title"
- "T@\"NSString\",R,V_url"
- "T@\"NSString\",R,V_value"
- "T@\"NSURL\",R"
- "T@\"NSUUID\",&,N,V_persistenceRecordIdentifier"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_identifier"
- "T@\"NSXPCConnection\",&,N,V_currentConnection"
- "T@\"NSXPCConnection\",R,N"
- "T@,R,N"
- "T@,R,N,V_defaultValue"
- "T@?,R,N,V_receiveCompletionBlock"
- "T@?,R,N,V_receiveInputBlock"
- "T@?,R,N,V_sensitivityChecker"
- "T@?,R,N,V_startBlock"
- "T@?,R,N,V_stopBlock"
- "TB,N"
- "TB,N,V_fullReplacement"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_active"
- "TB,R,N,V_isPrivacySensitive"
- "TB,R,N,V_isPublic"
- "TB,R,V_defaultValue"
- "TB,R,V_value"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_demand"
- "TQ,R,N,V_maximumActivityCount"
- "TQ,R,N,V_maximumApplicationCount"
- "TQ,R,N,V_maximumAutoAllowCount"
- "TQ,R,N,V_maximumCategoryCount"
- "TQ,R,N,V_maximumCount"
- "TQ,R,N,V_maximumNeverAllowCount"
- "TQ,R,N,V_maximumOnlyAllowCount"
- "TQ,R,N,V_state"
- "Tq,R,N,V_combineOperator"
- "Tq,R,N,V_interventionCombineOperator"
- "Tq,R,N,V_lowerBound"
- "Tq,R,N,V_upperBound"
- "Tq,R,V_defaultValue"
- "Tq,R,V_pageType"
- "Tq,R,V_policy"
- "Tq,R,V_value"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_account"
- "_active"
- "_airDrop"
- "_allApplications"
- "_allServices"
- "_allowedClient"
- "_appStore"
- "_application"
- "_audioAccessory"
- "_autoAllow"
- "_backgroundColorData"
- "_backgroundEffectData"
- "_base"
- "_bookmark"
- "_bundleIdentifier"
- "_calculator"
- "_camera"
- "_carPlay"
- "_cellular"
- "_children"
- "_colorData"
- "_combine:with:"
- "_combineInterventionType:with:"
- "_combineOperator"
- "_connectionClass"
- "_connectionLock"
- "_container"
- "_currentConnection"
- "_dateAndTime"
- "_defaultValue"
- "_demand"
- "_deviceActivity"
- "_domain"
- "_downstream"
- "_downstreams"
- "_effectiveSubject"
- "_effectiveSubscriptions"
- "_error"
- "_excludedContent"
- "_extensionIdentifier"
- "_eyeRelief"
- "_faceTime"
- "_findMy"
- "_fullReplacement"
- "_gameCenter"
- "_homepageURL"
- "_hour"
- "_iconData"
- "_identifier"
- "_intelligence"
- "_interestedGroups"
- "_internalStore"
- "_interventionCombineOperator"
- "_interventionType"
- "_isAcceptablePersistedArrayElement:"
- "_isAcceptableStringValue:"
- "_isPrivacySensitive"
- "_isPublic"
- "_keyboard"
- "_lock"
- "_lowerBound"
- "_managedSettings"
- "_maximumActivityCount"
- "_maximumApplicationCount"
- "_maximumAutoAllowCount"
- "_maximumCategoryCount"
- "_maximumCount"
- "_maximumNeverAllowCount"
- "_maximumOnlyAllowCount"
- "_media"
- "_messages"
- "_name"
- "_neverAllow"
- "_news"
- "_notification"
- "_onlyAllow"
- "_pageType"
- "_parent"
- "_passcode"
- "_persistableKeyClass"
- "_persistenceRecordIdentifier"
- "_policy"
- "_primaryButtonColorData"
- "_primaryButtonLabel"
- "_privacy"
- "_rankedAllowedValues"
- "_rankedInterventionTypes"
- "_receiveCompletionBlock"
- "_receiveInputBlock"
- "_removedSettings"
- "_safari"
- "_scope"
- "_screenTime"
- "_secondaryButtonLabel"
- "_secondaryButtonSubmenuItems"
- "_sensitivityChecker"
- "_settingName"
- "_settingsLock"
- "_settingsReader"
- "_settingsWriter"
- "_shield"
- "_siri"
- "_sourceIdentifier"
- "_specificCategories"
- "_startBlock"
- "_state"
- "_stopBlock"
- "_store"
- "_subscription"
- "_subscriptionLock"
- "_subtitle"
- "_text"
- "_title"
- "_unpairingTime"
- "_updatedProperties"
- "_updatedSettings"
- "_upperBound"
- "_upstream"
- "_url"
- "_user"
- "_userSafety"
- "_value"
- "_webContent"
- "_xpcConnection"
- "activate"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "allApplications"
- "allKeys"
- "allObjects"
- "allPolicyWithExceptions:"
- "allPolicyWithExcludedContent:"
- "allServices"
- "allValues"
- "allocWithZone:"
- "allowedClientMetadata"
- "allowedClientsMetadata"
- "allowedDataClientMetadata"
- "allowedExternalIntelligenceWorkspaceIDsMetadata"
- "allowedOtherPlayerTypesMetadata"
- "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:"
- "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:error:"
- "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:replyHandler:"
- "appResponsibleForShieldingCategoryIdentifier:completionHandler:"
- "appResponsibleForShieldingCategoryIdentifier:error:"
- "appResponsibleForShieldingCategoryIdentifier:replyHandler:"
- "appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:"
- "appResponsibleForShieldingWebDomain:categoryIdentifier:error:"
- "appResponsibleForShieldingWebDomain:categoryIdentifier:replyHandler:"
- "applicationCategoriesMetadata"
- "applicationCategoryPolicy"
- "applicationShieldPoliciesMetadata"
- "applicationsMetadata"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "askToOverrideUnremovabilityOfApplication:teamIdentifier:completionHandler:"
- "askToOverrideUnremovabilityOfApplication:teamIdentifier:replyHandler:"
- "autoPolicyWithDomains:exceptions:"
- "autorelease"
- "backgroundColorData"
- "backgroundEffectData"
- "base"
- "batchUpdate:"
- "blockedApplicationsMetadata"
- "blockedByFilterMetadata"
- "bookmarkSourceArrayFromPersistedArray:"
- "boolValue"
- "cancel"
- "caseInsensitiveCompare:"
- "categoryShieldPoliciesMetadata"
- "class"
- "clearAllSettings"
- "clearAllSettingsForRecordIdentifier:storeContainer:storeName:replyHandler:"
- "clearCurrentConnectionAndInvalidate:"
- "clearEffectiveSubscription:"
- "code"
- "collectDiagnosticsWithOneTimeConnection:outError:"
- "collectDiagnosticsWithOutError:"
- "collectDiagnosticsWithReplyHandler:"
- "colorData"
- "combineOperator"
- "combinePersistableValue:with:"
- "commitChanges"
- "communicationSafetyWithInterventionType:"
- "compareDomain:withDomainPattern:outExactMatch:"
- "componentsSeparatedByString:"
- "configurationForBundleIdentifier:categoryIdentifier:categoryName:error:"
- "configurationForCategoryIdentifier:categoryName:error:"
- "configurationForWebDomain:categoryIdentifier:categoryName:error:"
- "conformsToProtocol:"
- "connectionClass"
- "connectionLock"
- "container"
- "containsObject:"
- "cookiePolicyMetadata"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createSettingsStoreErrorWithCode:"
- "currentConnection"
- "currentDemand"
- "dataWithContentsOfURL:options:error:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeObjectOfClass:forKey:"
- "defaultValue"
- "deleteStore"
- "deleteStores:recordIdentifier:storeContainer:replyHandler:"
- "deleteStoresWithStoreNames:"
- "deleteStoresWithStoreNames:sharedContainer:"
- "deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:"
- "demand"
- "denyAddingFriendsMetadata"
- "denyAirDropMetadata"
- "denyAppClipsMetadata"
- "denyAppInstallationMetadata"
- "denyAppRemovalMetadata"
- "denyAppStoreAppInstallationMetadata"
- "denyAppleIntelligenceReportMetadata"
- "denyAutoCorrectionMetadata"
- "denyAutoFillMetadata"
- "denyBackgroundAppRefreshMetadata"
- "denyBookstoreEroticaMetadata"
- "denyBookstoreMetadata"
- "denyCameraMetadata"
- "denyCarPlayMetadata"
- "denyContinuousPathKeyboardMetadata"
- "denyDefinitionLookupMetadata"
- "denyDictationMetadata"
- "denyExplicitContentMetadata"
- "denyExternalIntelligenceIntegrationsMetadata"
- "denyExternalIntelligenceIntegrationsSignInMetadata"
- "denyFaceTimeMetadata"
- "denyFeature1Metadata"
- "denyGameCenterMetadata"
- "denyGenmojiMetadata"
- "denyHistoryClearingMetadata"
- "denyImagePlaygroundMetadata"
- "denyImageWandMetadata"
- "denyInAppPurchasesMetadata"
- "denyInputModeRPNMetadata"
- "denyInputModeUnitConversionMetadata"
- "denyJavaScriptMetadata"
- "denyKeyboardShortcutsMetadata"
- "denyMDMEnrollmentMetadata"
- "denyMailSmartRepliesMetadata"
- "denyMailSummaryMetadata"
- "denyMarketplaceAppInstallationMetadata"
- "denyMathPaperSolvingMetadata"
- "denyMathSolvingKeyboardMetadata"
- "denyMediaPurchaseMetadata"
- "denyModeMathPaperMetadata"
- "denyModeProgrammerMetadata"
- "denyModeScientificMetadata"
- "denyMultiplayerGamingMetadata"
- "denyMusicArtistActivityMetadata"
- "denyMusicServiceMetadata"
- "denyMusicVideosMetadata"
- "denyNearbyMultiplayerMetadata"
- "denyNewsMetadata"
- "denyNotesTranscriptionMetadata"
- "denyNotesTranscriptionSummaryMetadata"
- "denyPersonalizedHandwritingResultsMetadata"
- "denyPodcastsMetadata"
- "denyPopupsMetadata"
- "denyPredictiveKeyboardMetadata"
- "denyPrivateBrowsingMetadata"
- "denyPrivateMessagingMetadata"
- "denySafariMetadata"
- "denyScreenRecordingMetadata"
- "denySharePlayMetadata"
- "denySharedMediaLibrariesMetadata"
- "denySharingMetadata"
- "denySiriMetadata"
- "denySiriUserGeneratedContentMetadata"
- "denySiriWhileLockedMetadata"
- "denySpellCheckMetadata"
- "denySpotlightInternetResultsMetadata"
- "denySummaryMetadata"
- "denyTemporaryPairingMetadata"
- "denyUnrestrictedSharingMetadata"
- "denyVisualIntelligenceSummaryMetadata"
- "denyWebDistributionAppInstallationMetadata"
- "denyWritingToolsMetadata"
- "denyiCloudLogoutMetadata"
- "denyiMessageMetadata"
- "denyiTunesMetadata"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disassociate:"
- "downstream"
- "downstreams"
- "effectiveInterestedGroups"
- "effectiveSettingsChangedForGroups:"
- "effectiveSettingsDirectory"
- "effectiveSettingsPath"
- "effectiveSubject"
- "effectiveSubscriptions"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error"
- "errorWithDomain:code:userInfo:"
- "excludedContent"
- "extensionPageWithIdentifier:"
- "failureWithError:"
- "fetchConfigurationForBundleIdentifier:categoryIdentifier:categoryName:replyHandler:"
- "fetchConfigurationForCategoryIdentifier:categoryName:replyHandler:"
- "fetchConfigurationForWebDomain:categoryIdentifier:categoryName:replyHandler:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "finishWithCompletion:"
- "firstObject"
- "forceFraudWarningMetadata"
- "forceLimitAdTrackingMetadata"
- "forceOnDeviceOnlyDictationMetadata"
- "forceOnDeviceOnlyTranslationMetadata"
- "forceScreenDistanceOnMetadata"
- "forceSiriProfanityFilterMetadata"
- "forceSquareRootOnBasicCalculatorMetadata"
- "fullReplacement"
- "getAllSettingsForRecordIdentifier:storeContainer:storeName:replyHandler:"
- "getCurrentSettings"
- "getCurrentStoreProperties"
- "getStoreProperties"
- "getStorePropertiesForRecordIdentifier:storeContainer:storeName:replyHandler:"
- "getValuesForSettingNames:recordIdentifier:storeContainer:storeName:replyHandler:"
- "groupName"
- "handleAction:bundleIdentifier:categoryIdentifier:completionHandler:"
- "handleAction:bundleIdentifier:categoryIdentifier:replyHandler:"
- "handleAction:categoryIdentifier:completionHandler:"
- "handleAction:categoryIdentifier:replyHandler:"
- "handleAction:webDomain:categoryIdentifier:completionHandler:"
- "handleAction:webDomain:categoryIdentifier:replyHandler:"
- "hasDemand"
- "hasPrefix:"
- "hasSensitiveDataInSettings:"
- "hasSubscriptionWithIdentifier:"
- "hash"
- "homepageWithURL:"
- "hourPolicyWithHour:"
- "iconData"
- "indexOfObjectPassingTest:"
- "init"
- "initPublisher"
- "initSubject"
- "initSubscriber"
- "initWithAllServices:allApplications:interventionType:"
- "initWithArray:"
- "initWithAutoAllow:neverAllow:onlyAllow:"
- "initWithBackgroundColorData:backgroundEffectData:iconData:title:subtitle:primaryButtonLabel:primaryButtonColorData:secondaryButtonLabel:secondaryButtonSubmenuItems:"
- "initWithBundleIdentifier:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithCompletion:receiveInput:"
- "initWithConnectionClass:"
- "initWithDomain:"
- "initWithDomain:bookmark:"
- "initWithDownstream:interestedGroups:startBlock:stopBlock:"
- "initWithDownstream:parent:"
- "initWithIdentifier:"
- "initWithInterestedGroups:subscriptionCenter:"
- "initWithMachServiceName:options:"
- "initWithName:"
- "initWithName:sharedContainer:"
- "initWithName:sharedContainer:sensitivityChecker:connectionClass:"
- "initWithPageType:homepageURL:extensionIdentifier:"
- "initWithPolicy:hour:"
- "initWithPolicy:specificCategories:excludedContent:"
- "initWithReader:writer:"
- "initWithSettingName:defaultApplication:combineOperator:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultArray:combineOperator:maximumCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultBool:combineOperator:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultConfiguration:combineOperator:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultData:combineOperator:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultDictionary:persistableKeyClass:combineOperator:rankedAllowedValues:maximumCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultInt:combineOperator:lowerBound:upperBound:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultPolicy:interventionCombineOperator:rankedInterventionTypes:maximumApplicationCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultPolicy:maximumAutoAllowCount:maximumNeverAllowCount:maximumOnlyAllowCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultPolicy:maximumCategoryCount:maximumActivityCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultSet:combineOperator:maximumCount:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultString:combineOperator:rankedAllowedValues:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultValue:isPublic:scope:isPrivacySensitive:"
- "initWithSettingName:defaultWebNewPage:combineOperator:isPublic:scope:isPrivacySensitive:"
- "initWithSharedContainer:"
- "initWithSourceIdentifier:title:children:"
- "initWithState:error:"
- "initWithText:colorData:"
- "initWithTitle:children:"
- "initWithTitle:url:"
- "initWithUnpairingTime:"
- "initWithUpstream:interestedGroups:startBlock:stopBlock:"
- "initWithValue:defaultValue:"
- "initializeWithPersistableValue:"
- "intValue"
- "integerValue"
- "interestedGroups"
- "interfaceWithProtocol:"
- "internalStore"
- "intersectSet:"
- "interventionCombineOperator"
- "invalidate"
- "isDirectory"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToNumber:"
- "isEqualToSet:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPrivacySensitive"
- "isProxy"
- "isPublic"
- "isValidPersistableRepresentation:"
- "length"
- "loadDataAtURL:outError:"
- "loadEffectiveSettingsAtURL:"
- "lock"
- "lockAccountsMetadata"
- "lockAppCellularDataMetadata"
- "lockCellularPlanMetadata"
- "lockDriverDoNotDisturbMetadata"
- "lockESIMMetadata"
- "lockFindMyFriendsMetadata"
- "lockFriendsSharingMetadata"
- "lockPasscodeMetadata"
- "lockProfileMetadata"
- "lockProfilePrivacyMetadata"
- "lockSpeakerVolumeLimitMetadata"
- "lockTVProviderMetadata"
- "lowerBound"
- "managedBookmarksMetadata"
- "maximumActivityCount"
- "maximumApplicationCount"
- "maximumAutoAllowCount"
- "maximumCategoryCount"
- "maximumCount"
- "maximumMovieRatingMetadata"
- "maximumNeverAllowCount"
- "maximumOnlyAllowCount"
- "maximumRatingMetadata"
- "maximumTVShowRatingMetadata"
- "metadataForSetting:"
- "metadataForSettingKey:"
- "migrateSettingsIfNecessary:"
- "minusSet:"
- "mutableCopy"
- "name"
- "new"
- "newAgentInterface"
- "newClientInterface"
- "newConnection"
- "newConnectionWithExportedObject:"
- "newInterface"
- "newTabStartPageMetadata"
- "nonePolicy"
- "nudityDetectionPolicyWithAllServices:allApplications:"
- "nudityDetectionPolicyWithServices:applications:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "offerInput:"
- "oneTimeConnection"
- "parent"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistableArrayFromBookmarkSourceArray:"
- "persistableKeyClass"
- "persistableValue"
- "persistableValueForSetting:inGroup:"
- "persistableValueForSettingKey:"
- "persistableValueFromValue:"
- "persistenceRecordIdentifier"
- "primaryButtonColorData"
- "primaryButtonLabel"
- "processInfo"
- "processName"
- "propertyListWithData:options:format:error:"
- "proxyFromConnection:withRetryCount:proxyHandler:"
- "publisherForGroups:"
- "q"
- "q16@0:8"
- "q32@0:8q16q24"
- "rangeOfString:options:"
- "rankedAllowedValues"
- "rankedInterventionTypes"
- "receiveCompletion:"
- "receiveCompletionBlock"
- "receiveInput:"
- "receiveInputBlock"
- "receiveSubscription:"
- "reduceValues:intoExistingValues:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removePersistableValueForSetting:inGroup:"
- "removePersistableValueForSettingKey:"
- "removeValuesForSettingNames:recordIdentifier:storeContainer:storeName:replyHandler:"
- "removedSettings"
- "requestDemand:"
- "requireAutomaticDateAndTimeMetadata"
- "requirePasswordForPurchasesMetadata"
- "respondsToSelector:"
- "responsibleClients"
- "responsibleClientsForSetting:replyHandler:"
- "retain"
- "retainCount"
- "sanitizePersistableValue:"
- "scanningPolicyMetadata"
- "scope"
- "secondaryButtonLabel"
- "secondaryButtonSubmenuItems"
- "self"
- "sendCompletion:"
- "sendValue:"
- "sensitivityChecker"
- "serviceName"
- "services"
- "setActive:"
- "setAllowedClient:"
- "setAllowedClients:"
- "setAllowedDataClient:"
- "setAllowedExternalIntelligenceWorkspaceIDs:"
- "setAllowedOtherPlayerTypes:"
- "setApplicationCategories:"
- "setApplicationShieldPolicies:"
- "setApplications:"
- "setBlockedApplications:"
- "setBlockedByFilter:"
- "setByAddingObjectsFromSet:"
- "setCategoryShieldPolicies:"
- "setContainer:"
- "setCookiePolicy:"
- "setCurrentConnection:"
- "setDenyAddingFriends:"
- "setDenyAirDrop:"
- "setDenyAppClips:"
- "setDenyAppInstallation:"
- "setDenyAppRemoval:"
- "setDenyAppStoreAppInstallation:"
- "setDenyAppleIntelligenceReport:"
- "setDenyAutoCorrection:"
- "setDenyAutoFill:"
- "setDenyBackgroundAppRefresh:"
- "setDenyBookstore:"
- "setDenyBookstoreErotica:"
- "setDenyCamera:"
- "setDenyCarPlay:"
- "setDenyContinuousPathKeyboard:"
- "setDenyDefinitionLookup:"
- "setDenyDictation:"
- "setDenyExplicitContent:"
- "setDenyExternalIntelligenceIntegrations:"
- "setDenyExternalIntelligenceIntegrationsSignIn:"
- "setDenyFaceTime:"
- "setDenyFeature1:"
- "setDenyGameCenter:"
- "setDenyGenmoji:"
- "setDenyHistoryClearing:"
- "setDenyImagePlayground:"
- "setDenyImageWand:"
- "setDenyInAppPurchases:"
- "setDenyInputModeRPN:"
- "setDenyInputModeUnitConversion:"
- "setDenyJavaScript:"
- "setDenyKeyboardShortcuts:"
- "setDenyMDMEnrollment:"
- "setDenyMailSmartReplies:"
- "setDenyMailSummary:"
- "setDenyMarketplaceAppInstallation:"
- "setDenyMathPaperSolving:"
- "setDenyMathSolvingKeyboard:"
- "setDenyMediaPurchase:"
- "setDenyModeMathPaper:"
- "setDenyModeProgrammer:"
- "setDenyModeScientific:"
- "setDenyMultiplayerGaming:"
- "setDenyMusicArtistActivity:"
- "setDenyMusicService:"
- "setDenyMusicVideos:"
- "setDenyNearbyMultiplayer:"
- "setDenyNews:"
- "setDenyNotesTranscription:"
- "setDenyNotesTranscriptionSummary:"
- "setDenyPersonalizedHandwritingResults:"
- "setDenyPodcasts:"
- "setDenyPopups:"
- "setDenyPredictiveKeyboard:"
- "setDenyPrivateBrowsing:"
- "setDenyPrivateMessaging:"
- "setDenySafari:"
- "setDenyScreenRecording:"
- "setDenySharePlay:"
- "setDenySharedMediaLibraries:"
- "setDenySharing:"
- "setDenySiri:"
- "setDenySiriUserGeneratedContent:"
- "setDenySiriWhileLocked:"
- "setDenySpellCheck:"
- "setDenySpotlightInternetResults:"
- "setDenySummary:"
- "setDenyTemporaryPairing:"
- "setDenyUnrestrictedSharing:"
- "setDenyVisualIntelligenceSummary:"
- "setDenyWebDistributionAppInstallation:"
- "setDenyWritingTools:"
- "setDenyiCloudLogout:"
- "setDenyiMessage:"
- "setDenyiTunes:"
- "setExportedInterface:"
- "setExportedObject:"
- "setForceFraudWarning:"
- "setForceLimitAdTracking:"
- "setForceOnDeviceOnlyDictation:"
- "setForceOnDeviceOnlyTranslation:"
- "setForceScreenDistanceOn:"
- "setForceSiriProfanityFilter:"
- "setForceSquareRootOnBasicCalculator:"
- "setFullReplacement:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLockAccounts:"
- "setLockAppCellularData:"
- "setLockCellularPlan:"
- "setLockDriverDoNotDisturb:"
- "setLockESIM:"
- "setLockFindMyFriends:"
- "setLockFriendsSharing:"
- "setLockPasscode:"
- "setLockProfile:"
- "setLockProfilePrivacy:"
- "setLockSpeakerVolumeLimit:"
- "setLockTVProvider:"
- "setManagedBookmarks:"
- "setMaximumMovieRating:"
- "setMaximumRating:"
- "setMaximumTVShowRating:"
- "setName:"
- "setNewTabStartPage:"
- "setObject:forKeyedSubscript:"
- "setOfActiveRestrictionUUIDs"
- "setPersistableValue:forSetting:inGroup:"
- "setPersistableValue:forSettingKey:"
- "setPersistenceRecordIdentifier:"
- "setRemoteObjectInterface:"
- "setRemovedSettings:"
- "setRequireAutomaticDateAndTime:"
- "setRequirePasswordForPurchases:"
- "setScanningPolicy:"
- "setSettingsReader:"
- "setSettingsWriter:"
- "setShareAcrossDevices:"
- "setSharingAppleIDs:"
- "setSharingPolicy:"
- "setSyncToWatch:"
- "setTemporaryPairingConfiguration:"
- "setTokenDecodingKeys:"
- "setTokenEncodingKey:"
- "setTokenKeys:"
- "setUnremovableApplications:"
- "setUnshieldableApplications:"
- "setUnshieldableWebDomains:"
- "setUpdatedProperties:"
- "setUpdatedSettings:"
- "setValue:forSetting:"
- "setValue:forSettingKey:outError:"
- "setValues:recordIdentifier:storeContainer:storeName:replyHandler:"
- "setWebDomainCategories:"
- "setWebDomainShieldPolicies:"
- "setWebDomains:"
- "setWithArray:"
- "setWithObject:"
- "setWithSet:"
- "settingAndGroupStringsFromSettingKey:outGroup:outSetting:"
- "settingKeyFromSetting:group:"
- "settingName"
- "settingsLock"
- "settingsReader"
- "settingsWriter"
- "shareAcrossDevicesMetadata"
- "sharedDirectory"
- "sharingAppleIDsMetadata"
- "sharingPolicyMetadata"
- "sinkWithCompletion:receiveInput:"
- "sinkWithReceiveInput:"
- "sinkWithRecieveInput:"
- "specificCategories"
- "specificPolicyWithCategories:excludedContent:"
- "specificPolicyWithDomains:"
- "startBlock"
- "startObservingChangesWithHandler:"
- "startPage"
- "state"
- "stopBlock"
- "storeNamesForRecordIdentifier:storeContainer:replyHandler:"
- "storeWithName:sharedContainer:"
- "stores"
- "storesForSharedContainer:"
- "storesForSharedContainer:oneTimeConnection:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subscribe:"
- "subscribeForChangesInGroups:eventName:"
- "subscribeForEffectiveChanges:identifier:"
- "subscribeToEffectiveChangesForGroups:objC:"
- "subscriptionLock"
- "substringFromIndex:"
- "subtitle"
- "success"
- "superclass"
- "supportsSecureCoding"
- "synchronousProxyFromConnection:withRetryCount:proxyHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemCenter"
- "systemGroupContainerWithGroupIdentifier:"
- "temporaryPairingConfigurationMetadata"
- "text"
- "tokenDecodingKeysMetadata"
- "tokenEncodingKeyMetadata"
- "tokenKeysMetadata"
- "unarchivedObjectOfClass:fromData:error:"
- "unionSet:"
- "unremovableApplicationsMetadata"
- "unshieldableApplicationsMetadata"
- "unshieldableWebDomainsMetadata"
- "unsubscribeFromEffectiveChanges:"
- "updateStoreProperties:"
- "updateStoreProperties:recordIdentifier:storeContainer:storeName:replyHandler:"
- "updateStoreWithNewSettings:removedSettings:newProperties:fullReplacement:recordIdentifier:storeContainer:storeName:replyHandler:"
- "updateSubscription"
- "updatedProperties"
- "updatedSettings"
- "upperBound"
- "upstream"
- "userCenter"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
- "v24@0:8Q16"
- "v28@0:8@\"NSSet\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
- "v40@0:8@16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8q16@\"NSString\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v48@0:8@\"NSSet\"16@\"NSUUID\"24@\"NSString\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8q16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSNumber\"@\"NSError\">40"
- "v48@0:8q16@24@32@?40"
- "v56@0:8@\"NSDictionary\"16@\"NSUUID\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSUUID\"@\"NSError\">48"
- "v56@0:8@\"NSSet\"16@\"NSUUID\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@\"NSSet\"16@\"NSUUID\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSUUID\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v76@0:8@\"NSDictionary\"16@\"NSSet\"24@\"NSDictionary\"32B40@\"NSUUID\"44@\"NSString\"52@\"NSString\"60@?<v@?@\"NSUUID\"@\"NSError\">68"
- "v76@0:8@16@24@32B40@44@52@60@?68"
- "valueForKey:"
- "valueForSetting:"
- "valueForSettingKey:"
- "valueForUndefinedKey:"
- "valueFromPersistableValue:"
- "webDomainCategoriesMetadata"
- "webDomainCategoryPolicy"
- "webDomainShieldPoliciesMetadata"
- "webDomainsMetadata"
- "xpcConnection"
- "zone"

```
