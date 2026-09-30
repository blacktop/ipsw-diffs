## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/Versions/A/RemoteManagementModel`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x57120
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x77ec
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x45a8
-  __TEXT.__oslogstring: 0x3ed
-  __TEXT.__unwind_info: 0x1380
-  __TEXT.__objc_classname: 0x17cd
-  __TEXT.__objc_methname: 0xd2fb
-  __TEXT.__objc_methtype: 0xdd4
-  __TEXT.__objc_stubs: 0x6360
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x760
-  __DATA_CONST.__objc_classlist: 0x4d8
+560.4.11.0.0
+  __TEXT.__text: 0x5ab3c
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_methlist: 0x7e3c
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x48c2
+  __TEXT.__oslogstring: 0x528
+  __TEXT.__unwind_info: 0x1460
+  __TEXT.__objc_classname: 0x1924
+  __TEXT.__objc_methname: 0xda5e
+  __TEXT.__objc_methtype: 0xf5c
+  __TEXT.__objc_stubs: 0x6760
+  __DATA_CONST.__got: 0x5e0
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f38
-  __DATA_CONST.__objc_superrefs: 0x3d0
-  __DATA_CONST.__objc_arraydata: 0x30b8
-  __AUTH_CONST.__auth_got: 0xd8
-  __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x6dc0
-  __AUTH_CONST.__objc_const: 0xe030
-  __AUTH_CONST.__objc_arrayobj: 0x4c98
-  __AUTH_CONST.__objc_intobj: 0x2958
-  __AUTH.__objc_data: 0x3070
-  __DATA.__objc_ivar: 0x7d8
+  __DATA_CONST.__objc_selrefs: 0x2118
+  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_arraydata: 0x31c0
+  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__const: 0xb30
+  __AUTH_CONST.__cfstring: 0x70e0
+  __AUTH_CONST.__objc_const: 0xe648
+  __AUTH_CONST.__objc_arrayobj: 0x4e90
+  __AUTH_CONST.__objc_intobj: 0x2988
+  __AUTH.__objc_data: 0x32a0
+  __DATA.__objc_ivar: 0x828
   __DATA.__data: 0x1f0
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84A47B26-79D9-386B-AF71-FE9493AA8B4A
-  Functions: 2474
-  Symbols:   5535
-  CStrings:  3768
+  UUID: 6C067F9F-0745-34B9-948D-A6A9C7789247
+  Functions: 2619
+  Symbols:   5816
+  CStrings:  3912
 
Symbols:
+ +[NSDateFormatter(RemoteManagementModel) rmmodel_sharedRFC3339DateFormatter].cold.1
+ +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:]
+ +[RMModelAppManagedDeclaration_AppConfigDictionary allowedPayloadKeys]
+ +[RMModelAppManagedDeclaration_AppConfigDictionary buildRequiredOnly]
+ +[RMModelAppManagedDeclaration_AppConfigDictionary buildWithDataAssetReference:passwords:identities:certificates:]
+ +[RMModelAppManagedDeclaration_Attributes buildWithAssociatedDomains:associatedDomainsEnableDirectDownloads:cellularSliceUUID:contentFilterUUID:dnsProxyUUID:hideable:lockable:relayUUID:tapToPayScreenLock:VPNUUID:]
+ +[RMModelAppManagedDeclaration_CredentialConfig allowedPayloadKeys]
+ +[RMModelAppManagedDeclaration_CredentialConfig buildRequiredOnlyWithIdentifier:assetReference:]
+ +[RMModelAppManagedDeclaration_CredentialConfig buildWithIdentifier:assetReference:]
+ +[RMModelAppManagedDeclaration_ExtensionConfigs allowedPayloadKeys]
+ +[RMModelAppManagedDeclaration_ExtensionConfigs buildRequiredOnly]
+ +[RMModelAppManagedDeclaration_ExtensionConfigs build]
+ +[RMModelClasses addClass:declarationType:]
+ +[RMModelClasses allActivationClasses].cold.1
+ +[RMModelClasses allAssetClasses].cold.1
+ +[RMModelClasses allConfigurationClasses].cold.1
+ +[RMModelClasses allManagementClasses].cold.1
+ +[RMModelClasses allStatusItemClasses].cold.1
+ +[RMModelClasses classForCommandType:].cold.1
+ +[RMModelClasses classForDeclarationType:].cold.1
+ +[RMModelClasses classForStatusItemType:].cold.1
+ +[RMModelConfigurationBase usesKeychainAssets].cold.1
+ +[RMModelConfigurationSchema _loadDynamicSchemaFromFile:into:].cold.2
+ +[RMModelConfigurationSchema _processManagedSettingsSchemas]
+ +[RMModelConfigurationSchema managedSettingsSchemas]
+ +[RMModelConfigurationSchemaAssetReference parseJSON:]
+ +[RMModelConfigurationSchemaAssetReference parseJSON:].cold.1
+ +[RMModelConfigurationSchemaAssetReference parseJSON:].cold.2
+ +[RMModelConfigurationSchemaManagedSetting parseJSON:parentSchema:]
+ +[RMModelConfigurationSchemaManagedSetting parseJSON:parentSchema:].cold.1
+ +[RMModelConfigurationSchemaManagedSetting parseJSON:parentSchema:].cold.2
+ +[RMModelPayloadUtilities _walkObject:keyPath:fullKeyPath:]
+ +[RMModelPayloadUtilities _walkObject:keyPath:fullKeyPath:].cold.1
+ +[RMModelPayloadUtilities effectiveSupportedOS:overriddenSupportedOS:]
+ +[RMModelPayloadUtilities valueFromKeyPath:payload:]
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:]
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.1
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.2
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.3
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.4
+ +[RMModelSharedDefinitions allowedValueType:]
+ +[RMModelSharedDefinitions allowedValueType:].cold.1
+ +[RMModelStatusAppManagedList buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:configState:reasons:]
+ +[RMModelStatusAppManagedList_ManagedConfiguration allowedStatusKeys]
+ +[RMModelStatusAppManagedList_ManagedConfiguration buildRequiredOnly]
+ +[RMModelStatusAppManagedList_ManagedConfiguration buildWithAppConfigState:extensionConfigState:]
+ +[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState allowedStatusKeys]
+ +[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState buildRequiredOnly]
+ +[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState build]
+ +[RMModelStatusAppManagedList_ManagedConfigurationState allowedStatusKeys]
+ +[RMModelStatusAppManagedList_ManagedConfigurationState buildRequiredOnlyWithState:]
+ +[RMModelStatusAppManagedList_ManagedConfigurationState buildWithState:]
+ +[RMModelStatusSchema _loadDynamicSchemaFromFile:into:].cold.2
+ +[RMModelStatusSchema _processManagedSettingsSchemas]
+ +[RMModelStatusSchema managedSettingsSchemas]
+ +[RMModelStatusSchemaManagedSetting parseJSON:]
+ +[RMModelStatusSchemaManagedSetting parseJSON:].cold.1
+ +[RMModelStatusSchemaManagedSetting parseJSON:].cold.2
+ -[RMModelAccountCalDAVDeclaration assetReferences].cold.1
+ -[RMModelAccountCardDAVDeclaration assetReferences].cold.1
+ -[RMModelAccountExchangeDeclaration assetReferences].cold.1
+ -[RMModelAccountGoogleDeclaration assetReferences].cold.1
+ -[RMModelAccountLDAPDeclaration assetReferences].cold.1
+ -[RMModelAccountMailDeclaration assetReferences].cold.1
+ -[RMModelAccountSubscribedCalendarDeclaration assetReferences].cold.1
+ -[RMModelAppManagedDeclaration assetReferences].cold.1
+ -[RMModelAppManagedDeclaration payloadAppConfig]
+ -[RMModelAppManagedDeclaration payloadExtensionConfigs]
+ -[RMModelAppManagedDeclaration payloadLegacyAppConfigAssetReference]
+ -[RMModelAppManagedDeclaration setPayloadAppConfig:]
+ -[RMModelAppManagedDeclaration setPayloadExtensionConfigs:]
+ -[RMModelAppManagedDeclaration setPayloadLegacyAppConfigAssetReference:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary .cxx_destruct]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary copyWithZone:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary loadFromDictionary:serializationType:error:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary payloadCertificates]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary payloadDataAssetReference]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary payloadIdentities]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary payloadPasswords]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary serializeWithType:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary setPayloadCertificates:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary setPayloadDataAssetReference:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary setPayloadIdentities:]
+ -[RMModelAppManagedDeclaration_AppConfigDictionary setPayloadPasswords:]
+ -[RMModelAppManagedDeclaration_CredentialConfig .cxx_destruct]
+ -[RMModelAppManagedDeclaration_CredentialConfig copyWithZone:]
+ -[RMModelAppManagedDeclaration_CredentialConfig loadFromDictionary:serializationType:error:]
+ -[RMModelAppManagedDeclaration_CredentialConfig payloadAssetReference]
+ -[RMModelAppManagedDeclaration_CredentialConfig payloadIdentifier]
+ -[RMModelAppManagedDeclaration_CredentialConfig serializeWithType:]
+ -[RMModelAppManagedDeclaration_CredentialConfig setPayloadAssetReference:]
+ -[RMModelAppManagedDeclaration_CredentialConfig setPayloadIdentifier:]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs .cxx_destruct]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs copyWithZone:]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs loadFromDictionary:serializationType:error:]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs payloadDictionary]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs serializeWithType:]
+ -[RMModelAppManagedDeclaration_ExtensionConfigs setPayloadDictionary:]
+ -[RMModelConfigurationDynamic enumerateManagedSettingsUsingBlock:]
+ -[RMModelConfigurationDynamic isSupportedForPlatform:scope:enrollmentType:]
+ -[RMModelConfigurationSchema _parseManagedSettings:]
+ -[RMModelConfigurationSchema _parseManagedSettings:].cold.1
+ -[RMModelConfigurationSchema _parseManagedSettings:].cold.2
+ -[RMModelConfigurationSchema managedSettings]
+ -[RMModelConfigurationSchemaManagedSetting .cxx_destruct]
+ -[RMModelConfigurationSchemaManagedSetting initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:]
+ -[RMModelConfigurationSchemaManagedSetting invertBoolean]
+ -[RMModelConfigurationSchemaManagedSetting isEqual:]
+ -[RMModelConfigurationSchemaManagedSetting isEqualToManagedSetting:]
+ -[RMModelConfigurationSchemaManagedSetting isSupportedForPlatform:scope:enrollmentType:]
+ -[RMModelConfigurationSchemaManagedSetting keyPath]
+ -[RMModelConfigurationSchemaManagedSetting managedSettingKey]
+ -[RMModelConfigurationSchemaManagedSetting parentSchema]
+ -[RMModelConfigurationSchemaManagedSetting setParentSchema:]
+ -[RMModelConfigurationSchemaManagedSetting setSupportedOS:]
+ -[RMModelConfigurationSchemaManagedSetting supportedOS]
+ -[RMModelConfigurationSchemaManagedSetting valueType]
+ -[RMModelManagementTestDeclaration assetReferences].cold.1
+ -[RMModelNetworkEAPDeclaration assetReferences].cold.1
+ -[RMModelNetworkWiFiDeclaration assetReferences].cold.1
+ -[RMModelPayloadBase isSupportedForPlatform:scope:enrollmentType:]
+ -[RMModelScreenSharingConnectionDeclaration assetReferences].cold.1
+ -[RMModelSecurityCertificateDeclaration assetReferences].cold.1
+ -[RMModelSecurityIdentityDeclaration assetReferences].cold.1
+ -[RMModelSecurityPasskeyAttestationDeclaration assetReferences].cold.1
+ -[RMModelServicesBackgroundTasksDeclaration assetReferences].cold.1
+ -[RMModelServicesConfigurationFilesDeclaration assetReferences].cold.1
+ -[RMModelStatusAppManagedList setStatusConfigState:]
+ -[RMModelStatusAppManagedList statusConfigState]
+ -[RMModelStatusAppManagedList_ManagedConfiguration .cxx_destruct]
+ -[RMModelStatusAppManagedList_ManagedConfiguration copyWithZone:]
+ -[RMModelStatusAppManagedList_ManagedConfiguration loadFromDictionary:serializationType:error:]
+ -[RMModelStatusAppManagedList_ManagedConfiguration serializeWithType:]
+ -[RMModelStatusAppManagedList_ManagedConfiguration setStatusAppConfigState:]
+ -[RMModelStatusAppManagedList_ManagedConfiguration setStatusExtensionConfigState:]
+ -[RMModelStatusAppManagedList_ManagedConfiguration statusAppConfigState]
+ -[RMModelStatusAppManagedList_ManagedConfiguration statusExtensionConfigState]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState .cxx_destruct]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState copyWithZone:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState loadFromDictionary:serializationType:error:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState serializeWithType:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState setStatusDictionary:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState statusDictionary]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState .cxx_destruct]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState copyWithZone:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState loadFromDictionary:serializationType:error:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState serializeWithType:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState setStatusState:]
+ -[RMModelStatusAppManagedList_ManagedConfigurationState statusState]
+ -[RMModelStatusDynamic isSupportedForPlatform:scope:enrollmentType:]
+ -[RMModelStatusSchema managedSetting]
+ -[RMModelStatusSchemaManagedSetting .cxx_destruct]
+ -[RMModelStatusSchemaManagedSetting initWithManagedSetting:valueType:invertBoolean:]
+ -[RMModelStatusSchemaManagedSetting invertBoolean]
+ -[RMModelStatusSchemaManagedSetting isEqual:]
+ -[RMModelStatusSchemaManagedSetting isEqualToManagedSetting:]
+ -[RMModelStatusSchemaManagedSetting managedSettingKey]
+ -[RMModelStatusSchemaManagedSetting valueType]
+ -[RMModelWatchEnrollmentDeclaration assetReferences].cold.1
+ OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadAppConfig
+ OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadExtensionConfigs
+ OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadLegacyAppConfigAssetReference
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_AppConfigDictionary._payloadCertificates
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_AppConfigDictionary._payloadDataAssetReference
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_AppConfigDictionary._payloadIdentities
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_AppConfigDictionary._payloadPasswords
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_CredentialConfig._payloadAssetReference
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_CredentialConfig._payloadIdentifier
+ OBJC_IVAR_$_RMModelAppManagedDeclaration_ExtensionConfigs._payloadDictionary
+ OBJC_IVAR_$_RMModelConfigurationSchema._managedSettings
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._invertBoolean
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._keyPath
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._managedSettingKey
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._parentSchema
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._supportedOS
+ OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._valueType
+ OBJC_IVAR_$_RMModelStatusAppManagedList._statusConfigState
+ OBJC_IVAR_$_RMModelStatusAppManagedList_ManagedConfiguration._statusAppConfigState
+ OBJC_IVAR_$_RMModelStatusAppManagedList_ManagedConfiguration._statusExtensionConfigState
+ OBJC_IVAR_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState._statusDictionary
+ OBJC_IVAR_$_RMModelStatusAppManagedList_ManagedConfigurationState._statusState
+ OBJC_IVAR_$_RMModelStatusSchema._managedSetting
+ OBJC_IVAR_$_RMModelStatusSchemaManagedSetting._invertBoolean
+ OBJC_IVAR_$_RMModelStatusSchemaManagedSetting._managedSettingKey
+ OBJC_IVAR_$_RMModelStatusSchemaManagedSetting._valueType
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_AppConfigDictionary
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_CredentialConfig
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_ExtensionConfigs
+ _OBJC_CLASS_$_RMModelConfigurationSchemaManagedSetting
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfiguration
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ _OBJC_CLASS_$_RMModelStatusAppManagedList_ManagedConfigurationState
+ _OBJC_CLASS_$_RMModelStatusSchemaManagedSetting
+ _OBJC_METACLASS_$_RMModelAppManagedDeclaration_AppConfigDictionary
+ _OBJC_METACLASS_$_RMModelAppManagedDeclaration_CredentialConfig
+ _OBJC_METACLASS_$_RMModelAppManagedDeclaration_ExtensionConfigs
+ _OBJC_METACLASS_$_RMModelConfigurationSchemaManagedSetting
+ _OBJC_METACLASS_$_RMModelStatusAppManagedList_ManagedConfiguration
+ _OBJC_METACLASS_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ _OBJC_METACLASS_$_RMModelStatusAppManagedList_ManagedConfigurationState
+ _OBJC_METACLASS_$_RMModelStatusSchemaManagedSetting
+ _RMModelStatusAppManagedList_ManagedConfigurationState_State_invalid
+ _RMModelStatusAppManagedList_ManagedConfigurationState_State_unknown
+ _RMModelStatusAppManagedList_ManagedConfigurationState_State_valid
+ _RMModelValueTypeArray
+ _RMModelValueTypeBoolean
+ _RMModelValueTypeDictionary
+ _RMModelValueTypeInteger
+ _RMModelValueTypeReal
+ _RMModelValueTypeString
+ __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_$_CLASS_METHODS_RMModelConfigurationSchemaAssetReference
+ __OBJC_$_CLASS_METHODS_RMModelConfigurationSchemaManagedSetting
+ __OBJC_$_CLASS_METHODS_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_$_CLASS_METHODS_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_$_CLASS_METHODS_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_$_CLASS_METHODS_RMModelStatusSchemaManagedSetting
+ __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_$_CLASS_PROP_LIST_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_$_CLASS_PROP_LIST_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_$_CLASS_PROP_LIST_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_$_INSTANCE_METHODS_RMModelConfigurationSchemaManagedSetting
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusSchemaManagedSetting
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_$_INSTANCE_VARIABLES_RMModelConfigurationSchemaManagedSetting
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusSchemaManagedSetting
+ __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_$_PROP_LIST_RMModelConfigurationSchemaManagedSetting
+ __OBJC_$_PROP_LIST_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_$_PROP_LIST_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_$_PROP_LIST_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_$_PROP_LIST_RMModelStatusSchemaManagedSetting
+ __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_CLASS_RO_$_RMModelConfigurationSchemaManagedSetting
+ __OBJC_CLASS_RO_$_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_CLASS_RO_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_CLASS_RO_$_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_CLASS_RO_$_RMModelStatusSchemaManagedSetting
+ __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_AppConfigDictionary
+ __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_CredentialConfig
+ __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_ExtensionConfigs
+ __OBJC_METACLASS_RO_$_RMModelConfigurationSchemaManagedSetting
+ __OBJC_METACLASS_RO_$_RMModelStatusAppManagedList_ManagedConfiguration
+ __OBJC_METACLASS_RO_$_RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState
+ __OBJC_METACLASS_RO_$_RMModelStatusAppManagedList_ManagedConfigurationState
+ __OBJC_METACLASS_RO_$_RMModelStatusSchemaManagedSetting
+ ___45+[RMModelSharedDefinitions allowedValueType:]_block_invoke
+ ___53+[RMModelStatusSchema _processManagedSettingsSchemas]_block_invoke
+ ___56-[RMModelStatusAppManagedList serializePayloadWithType:]_block_invoke_2
+ ___60+[RMModelConfigurationSchema _processManagedSettingsSchemas]_block_invoke
+ ___70+[RMModelPayloadUtilities effectiveSupportedOS:overriddenSupportedOS:]_block_invoke
+ ___70-[RMModelAppManagedDeclaration_AppConfigDictionary serializeWithType:]_block_invoke
+ ___70-[RMModelAppManagedDeclaration_AppConfigDictionary serializeWithType:]_block_invoke_2
+ ___70-[RMModelAppManagedDeclaration_AppConfigDictionary serializeWithType:]_block_invoke_3
+ ___70-[RMModelStatusAppManagedList_ManagedConfiguration serializeWithType:]_block_invoke
+ ___70-[RMModelStatusAppManagedList_ManagedConfiguration serializeWithType:]_block_invoke_2
+ ___block_descriptor_34_e69_"NSDictionary"16?0"RMModelAppManagedDeclaration_CredentialConfig"8l
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24l
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSString"8"RMModelStatusSchema"16^B24l
+ ___block_descriptor_40_e8_32s_e53_v32?0"NSString"8"RMModelConfigurationSchema"16^B24l
+ ___copy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s
+ __block_literal_global.395
+ __block_literal_global.426
+ __block_literal_global.50
+ __managedSettingsSchemas
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_parseManagedSettings:
+ _objc_msgSend$_processManagedSettingsSchemas
+ _objc_msgSend$_walkObject:keyPath:fullKeyPath:
+ _objc_msgSend$allValues
+ _objc_msgSend$allowedValueType:
+ _objc_msgSend$effectiveSupportedOS:overriddenSupportedOS:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:
+ _objc_msgSend$initWithManagedSetting:valueType:invertBoolean:
+ _objc_msgSend$invertBoolean
+ _objc_msgSend$isEqualToManagedSetting:
+ _objc_msgSend$isSupportedForPlatform:scope:enrollmentType:
+ _objc_msgSend$loadSupportedOSFromDictionary:allowEmptyOS:
+ _objc_msgSend$managedSetting
+ _objc_msgSend$managedSettingKey
+ _objc_msgSend$managedSettings
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$parentSchema
+ _objc_msgSend$parseJSON:
+ _objc_msgSend$parseJSON:parentSchema:
+ _objc_msgSend$payloadAppConfig
+ _objc_msgSend$payloadCertificates
+ _objc_msgSend$payloadExtensionConfigs
+ _objc_msgSend$payloadIdentifier
+ _objc_msgSend$payloadIdentities
+ _objc_msgSend$payloadLegacyAppConfigAssetReference
+ _objc_msgSend$payloadPasswords
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setPayloadAppConfig:
+ _objc_msgSend$setPayloadCertificates:
+ _objc_msgSend$setPayloadExtensionConfigs:
+ _objc_msgSend$setPayloadIdentifier:
+ _objc_msgSend$setPayloadIdentities:
+ _objc_msgSend$setPayloadLegacyAppConfigAssetReference:
+ _objc_msgSend$setPayloadPasswords:
+ _objc_msgSend$setStatusAppConfigState:
+ _objc_msgSend$setStatusConfigState:
+ _objc_msgSend$setStatusExtensionConfigState:
+ _objc_msgSend$statusAppConfigState
+ _objc_msgSend$statusConfigState
+ _objc_msgSend$statusDictionary
+ _objc_msgSend$statusExtensionConfigState
+ _objc_msgSend$valueFromKeyPath:payload:
+ _objc_msgSend$valueType
+ _objc_storeWeak
+ allowedValueType:.allowedValueTypes
+ allowedValueType:.onceToken
- +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfigAssetReference:passwordAppConfigs:identityAppConfigs:certificateAppConfigs:]
- +[RMModelAppManagedDeclaration_AppCredentialConfig allowedPayloadKeys]
- +[RMModelAppManagedDeclaration_AppCredentialConfig buildRequiredOnlyWithAppIdentifier:assetReference:]
- +[RMModelAppManagedDeclaration_AppCredentialConfig buildWithAppIdentifier:assetReference:]
- +[RMModelAppManagedDeclaration_Attributes buildWithHideable:lockable:associatedDomains:associatedDomainsEnableDirectDownloads:cellularSliceUUID:contentFilterUUID:dnsProxyUUID:relayUUID:tapToPayScreenLock:VPNUUID:]
- +[RMModelSchemaParser loadSupportedOSFromDictionary:]
- +[RMModelSchemaParser loadSupportedOSFromDictionary:].cold.1
- +[RMModelStatusAppManagedList buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:]
- -[RMModelAppManagedDeclaration payloadAppConfigAssetReference]
- -[RMModelAppManagedDeclaration payloadCertificateAppConfigs]
- -[RMModelAppManagedDeclaration payloadIdentityAppConfigs]
- -[RMModelAppManagedDeclaration payloadPasswordAppConfigs]
- -[RMModelAppManagedDeclaration setPayloadAppConfigAssetReference:]
- -[RMModelAppManagedDeclaration setPayloadCertificateAppConfigs:]
- -[RMModelAppManagedDeclaration setPayloadIdentityAppConfigs:]
- -[RMModelAppManagedDeclaration setPayloadPasswordAppConfigs:]
- -[RMModelAppManagedDeclaration_AppCredentialConfig .cxx_destruct]
- -[RMModelAppManagedDeclaration_AppCredentialConfig copyWithZone:]
- -[RMModelAppManagedDeclaration_AppCredentialConfig loadFromDictionary:serializationType:error:]
- -[RMModelAppManagedDeclaration_AppCredentialConfig payloadAppIdentifier]
- -[RMModelAppManagedDeclaration_AppCredentialConfig payloadAssetReference]
- -[RMModelAppManagedDeclaration_AppCredentialConfig serializeWithType:]
- -[RMModelAppManagedDeclaration_AppCredentialConfig setPayloadAppIdentifier:]
- -[RMModelAppManagedDeclaration_AppCredentialConfig setPayloadAssetReference:]
- OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadAppConfigAssetReference
- OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadCertificateAppConfigs
- OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadIdentityAppConfigs
- OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadPasswordAppConfigs
- OBJC_IVAR_$_RMModelAppManagedDeclaration_AppCredentialConfig._payloadAppIdentifier
- OBJC_IVAR_$_RMModelAppManagedDeclaration_AppCredentialConfig._payloadAssetReference
- _OBJC_CLASS_$_RMModelAppManagedDeclaration_AppCredentialConfig
- _OBJC_METACLASS_$_RMModelAppManagedDeclaration_AppCredentialConfig
- _OUTLINED_FUNCTION_2
- __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_AppCredentialConfig
- __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_AppCredentialConfig
- ___57-[RMModelAppManagedDeclaration serializePayloadWithType:]_block_invoke_5
- ___block_descriptor_34_e72_"NSDictionary"16?0"RMModelAppManagedDeclaration_AppCredentialConfig"8l
- __block_literal_global.374
- __block_literal_global.44
- _objc_msgSend$loadDateFromDictionary:usingKey:forKeyPath:isRequired:defaultValue:serializationType:error:
- _objc_msgSend$loadSupportedOSFromDictionary:
- _objc_msgSend$payloadAppConfigAssetReference
- _objc_msgSend$payloadAppIdentifier
- _objc_msgSend$payloadCertificateAppConfigs
- _objc_msgSend$payloadIdentityAppConfigs
- _objc_msgSend$payloadPasswordAppConfigs
- _objc_msgSend$setPayloadAppConfigAssetReference:
- _objc_msgSend$setPayloadAppIdentifier:
- _objc_msgSend$setPayloadCertificateAppConfigs:
- _objc_msgSend$setPayloadIdentityAppConfigs:
- _objc_msgSend$setPayloadPasswordAppConfigs:
CStrings:
+ "$.payloadAppConfig.payloadCertificates.*.payloadAssetReference"
+ "$.payloadAppConfig.payloadDataAssetReference"
+ "$.payloadAppConfig.payloadIdentities.*.payloadAssetReference"
+ "$.payloadAppConfig.payloadPasswords.*.payloadAssetReference"
+ "$.payloadExtensionConfigs.payloadDictionary.*.payloadCertificates.*.payloadAssetReference"
+ "$.payloadExtensionConfigs.payloadDictionary.*.payloadDataAssetReference"
+ "$.payloadExtensionConfigs.payloadDictionary.*.payloadIdentities.*.payloadAssetReference"
+ "$.payloadExtensionConfigs.payloadDictionary.*.payloadPasswords.*.payloadAssetReference"
+ "$.payloadLegacyAppConfigAssetReference"
+ "@\"NSDictionary\"16@?0@\"RMModelAppManagedDeclaration_CredentialConfig\"8"
+ "@\"RMModelAppManagedDeclaration_AppConfigDictionary\""
+ "@\"RMModelAppManagedDeclaration_ExtensionConfigs\""
+ "@\"RMModelStatusAppManagedList_ManagedConfiguration\""
+ "@\"RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState\""
+ "@\"RMModelStatusAppManagedList_ManagedConfigurationState\""
+ "@\"RMModelStatusSchemaManagedSetting\""
+ "@28@0:8@16B24"
+ "@36@0:8@16@24B32"
+ "@60@0:8@16@24@32B40@44@52"
+ "AppConfig"
+ "Certificates"
+ "Could not parse JSON data file: %{public}@ %{public}@"
+ "ExtensionConfigs"
+ "Identities"
+ "Invalid asset-reference"
+ "Invalid managed-setting"
+ "Invalid managed-settings"
+ "Invalid supported-os: %{public}@ allowed-enrollments"
+ "Invalid supported-os: %{public}@ allowed-scopes"
+ "Invalid supported-os: %{public}@ item"
+ "Key path lookup failed: %{public}@ at %{public}@"
+ "LegacyAppConfigAssetReference"
+ "Passwords"
+ "Q"
+ "RMModelAppManagedDeclaration_AppConfigDictionary"
+ "RMModelAppManagedDeclaration_CredentialConfig"
+ "RMModelAppManagedDeclaration_ExtensionConfigs"
+ "RMModelConfigurationSchemaManagedSetting"
+ "RMModelStatusAppManagedList_ManagedConfiguration"
+ "RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState"
+ "RMModelStatusAppManagedList_ManagedConfigurationState"
+ "RMModelStatusSchemaManagedSetting"
+ "T@\"NSArray\",C,N,V_payloadCertificates"
+ "T@\"NSArray\",C,N,V_payloadIdentities"
+ "T@\"NSArray\",C,N,V_payloadPasswords"
+ "T@\"NSArray\",R,C,N,V_managedSettings"
+ "T@\"NSDictionary\",C,N,V_statusDictionary"
+ "T@\"NSString\",C,N,V_payloadIdentifier"
+ "T@\"NSString\",C,N,V_payloadLegacyAppConfigAssetReference"
+ "T@\"NSString\",C,N,V_statusTargetLocalDateTime"
+ "T@\"NSString\",R,C,N,V_managedSettingKey"
+ "T@\"NSString\",R,C,N,V_valueType"
+ "T@\"RMModelAppManagedDeclaration_AppConfigDictionary\",C,N,V_payloadAppConfig"
+ "T@\"RMModelAppManagedDeclaration_ExtensionConfigs\",C,N,V_payloadExtensionConfigs"
+ "T@\"RMModelConfigurationSchema\",W,N,V_parentSchema"
+ "T@\"RMModelStatusAppManagedList_ManagedConfiguration\",C,N,V_statusConfigState"
+ "T@\"RMModelStatusAppManagedList_ManagedConfigurationExtensionConfigState\",C,N,V_statusExtensionConfigState"
+ "T@\"RMModelStatusAppManagedList_ManagedConfigurationState\",C,N,V_statusAppConfigState"
+ "T@\"RMModelStatusSchemaManagedSetting\",R,C,N,V_managedSetting"
+ "TB,R,V_invertBoolean"
+ "_invertBoolean"
+ "_managedSetting"
+ "_managedSettingKey"
+ "_managedSettings"
+ "_parentSchema"
+ "_parseManagedSettings:"
+ "_payloadAppConfig"
+ "_payloadCertificates"
+ "_payloadExtensionConfigs"
+ "_payloadIdentifier"
+ "_payloadIdentities"
+ "_payloadLegacyAppConfigAssetReference"
+ "_payloadPasswords"
+ "_processManagedSettingsSchemas"
+ "_statusAppConfigState"
+ "_statusConfigState"
+ "_statusDictionary"
+ "_statusExtensionConfigState"
+ "_valueType"
+ "_walkObject:keyPath:fullKeyPath:"
+ "addClass:declarationType:"
+ "allValues"
+ "allowedValueType:"
+ "app-config-state"
+ "array"
+ "boolean"
+ "buildRequiredOnlyWithIdentifier:assetReference:"
+ "buildRequiredOnlyWithState:"
+ "buildWithAppConfigState:extensionConfigState:"
+ "buildWithAssociatedDomains:associatedDomainsEnableDirectDownloads:cellularSliceUUID:contentFilterUUID:dnsProxyUUID:hideable:lockable:relayUUID:tapToPayScreenLock:VPNUUID:"
+ "buildWithDataAssetReference:passwords:identities:certificates:"
+ "buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:"
+ "buildWithIdentifier:assetReference:"
+ "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:configState:reasons:"
+ "buildWithState:"
+ "config-state"
+ "dictionary"
+ "effectiveSupportedOS:overriddenSupportedOS:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumerateManagedSettingsUsingBlock:"
+ "extension-config-state"
+ "initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:"
+ "initWithManagedSetting:valueType:invertBoolean:"
+ "integer"
+ "invert-boolean"
+ "invertBoolean"
+ "isEqualToManagedSetting:"
+ "loadSupportedOSFromDictionary:allowEmptyOS:"
+ "managed-setting"
+ "managed-settings"
+ "managedSetting"
+ "managedSettingKey"
+ "managedSettings"
+ "managedSettingsSchemas"
+ "numberWithInt:"
+ "parentSchema"
+ "parseJSON:"
+ "parseJSON:parentSchema:"
+ "payloadAppConfig"
+ "payloadCertificates"
+ "payloadExtensionConfigs"
+ "payloadIdentifier"
+ "payloadIdentities"
+ "payloadLegacyAppConfigAssetReference"
+ "payloadPasswords"
+ "real"
+ "removeObjectForKey:"
+ "setParentSchema:"
+ "setPayloadAppConfig:"
+ "setPayloadCertificates:"
+ "setPayloadExtensionConfigs:"
+ "setPayloadIdentifier:"
+ "setPayloadIdentities:"
+ "setPayloadLegacyAppConfigAssetReference:"
+ "setPayloadPasswords:"
+ "setStatusAppConfigState:"
+ "setStatusConfigState:"
+ "setStatusDictionary:"
+ "setStatusExtensionConfigState:"
+ "setting"
+ "statusAppConfigState"
+ "statusConfigState"
+ "statusDictionary"
+ "statusExtensionConfigState"
+ "string"
+ "v24@0:8@?16"
+ "v32@0:8#16@24"
+ "v32@?0@\"NSNumber\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8@\"RMModelConfigurationSchema\"16^B24"
+ "v32@?0@\"NSString\"8@\"RMModelStatusSchema\"16^B24"
+ "valueFromKeyPath:payload:"
+ "valueType"
- "$.payloadAppConfigAssetReference"
- "$.payloadCertificateAppConfigs.*.payloadAssetReference"
- "$.payloadIdentityAppConfigs.*.payloadAssetReference"
- "$.payloadPasswordAppConfigs.*.payloadAssetReference"
- "@\"NSDate\""
- "@\"NSDictionary\"16@?0@\"RMModelAppManagedDeclaration_AppCredentialConfig\"8"
- "AppConfigAssetReference"
- "AppIdentifier"
- "CertificateAppConfigs"
- "IdentityAppConfigs"
- "PasswordAppConfigs"
- "RMModelAppManagedDeclaration_AppCredentialConfig"
- "T@\"NSArray\",C,N,V_payloadCertificateAppConfigs"
- "T@\"NSArray\",C,N,V_payloadIdentityAppConfigs"
- "T@\"NSArray\",C,N,V_payloadPasswordAppConfigs"
- "T@\"NSDate\",C,N,V_statusTargetLocalDateTime"
- "T@\"NSString\",C,N,V_payloadAppConfigAssetReference"
- "T@\"NSString\",C,N,V_payloadAppIdentifier"
- "_payloadAppConfigAssetReference"
- "_payloadAppIdentifier"
- "_payloadCertificateAppConfigs"
- "_payloadIdentityAppConfigs"
- "_payloadPasswordAppConfigs"
- "buildRequiredOnlyWithAppIdentifier:assetReference:"
- "buildWithAppIdentifier:assetReference:"
- "buildWithHideable:lockable:associatedDomains:associatedDomainsEnableDirectDownloads:cellularSliceUUID:contentFilterUUID:dnsProxyUUID:relayUUID:tapToPayScreenLock:VPNUUID:"
- "buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfigAssetReference:passwordAppConfigs:identityAppConfigs:certificateAppConfigs:"
- "buildWithIdentifier:removed:declarationIdentifier:name:externalVersionId:version:shortVersion:state:updateState:reasons:"
- "loadSupportedOSFromDictionary:"
- "payloadAppConfigAssetReference"
- "payloadAppIdentifier"
- "payloadCertificateAppConfigs"
- "payloadIdentityAppConfigs"
- "payloadPasswordAppConfigs"
- "setPayloadAppConfigAssetReference:"
- "setPayloadAppIdentifier:"
- "setPayloadCertificateAppConfigs:"
- "setPayloadIdentityAppConfigs:"
- "setPayloadPasswordAppConfigs:"

```
