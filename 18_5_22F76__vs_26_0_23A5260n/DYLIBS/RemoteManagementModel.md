## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel`

```diff

-560.4.11.0.0
-  __TEXT.__text: 0x52964
+578.0.1.0.0
+  __TEXT.__text: 0x55418
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x7e3c
+  __TEXT.__objc_methlist: 0x832c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x48c2
+  __TEXT.__cstring: 0x4aa9
   __TEXT.__oslogstring: 0x528
-  __TEXT.__unwind_info: 0x1410
-  __TEXT.__objc_classname: 0x1924
-  __TEXT.__objc_methname: 0xda6b
-  __TEXT.__objc_methtype: 0xf5c
-  __TEXT.__objc_stubs: 0x6780
-  __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__objc_classlist: 0x510
+  __TEXT.__unwind_info: 0x14b0
+  __TEXT.__objc_classname: 0x1a04
+  __TEXT.__objc_methname: 0xe275
+  __TEXT.__objc_methtype: 0x1008
+  __TEXT.__objc_stubs: 0x6a00
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2120
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x31c0
+  __DATA_CONST.__objc_selrefs: 0x2218
+  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_arraydata: 0x3260
   __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x70e0
-  __AUTH_CONST.__objc_const: 0xe648
-  __AUTH_CONST.__objc_arrayobj: 0x4e90
-  __AUTH_CONST.__objc_intobj: 0x2988
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x828
+  __AUTH_CONST.__cfstring: 0x7460
+  __AUTH_CONST.__objc_const: 0xef60
+  __AUTH_CONST.__objc_arrayobj: 0x4fe0
+  __AUTH_CONST.__objc_intobj: 0x2aa8
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x884
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x190
-  __DATA_DIRTY.__objc_data: 0x30c0
+  __DATA_DIRTY.__objc_data: 0x3070
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4EFED0FE-F0FB-3F93-A97B-FBD26D708C40
-  Functions: 2617
-  Symbols:   8470
-  CStrings:  3913
+  UUID: 6161C0FB-4A8B-3F5D-B846-6D91A512C5F2
+  Functions: 2716
+  Symbols:   8780
+  CStrings:  4034
 
Symbols:
+ +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:appComposedIdentifier:iosApp:installBehavior:updateBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:]
+ +[RMModelAppManagedDeclaration_InstallBehavior buildWithInstall:license:version:allowDownloadsOverCellular:]
+ +[RMModelAppManagedDeclaration_UpdateBehavior allowedPayloadKeys]
+ +[RMModelAppManagedDeclaration_UpdateBehavior buildRequiredOnlyWithAutomaticAppUpdates:]
+ +[RMModelAppManagedDeclaration_UpdateBehavior buildWithAutomaticAppUpdates:]
+ +[RMModelPackageDeclaration allowedPayloadKeys]
+ +[RMModelPackageDeclaration assetTypes]
+ +[RMModelPackageDeclaration buildRequiredOnlyWithIdentifier:manifestURL:]
+ +[RMModelPackageDeclaration buildWithIdentifier:manifestURL:installBehavior:repairBehavior:uninstallBehavior:]
+ +[RMModelPackageDeclaration combineConfigurations:]
+ +[RMModelPackageDeclaration registeredClassName]
+ +[RMModelPackageDeclaration registeredIdentifier]
+ +[RMModelPackageDeclaration supportedOS]
+ +[RMModelPackageDeclaration_InstallBehavior allowedPayloadKeys]
+ +[RMModelPackageDeclaration_InstallBehavior buildRequiredOnly]
+ +[RMModelPackageDeclaration_InstallBehavior buildWithInstall:installScript:]
+ +[RMModelPackageDeclaration_RepairBehavior allowedPayloadKeys]
+ +[RMModelPackageDeclaration_RepairBehavior buildRequiredOnlyWithCheckScript:repairScript:]
+ +[RMModelPackageDeclaration_RepairBehavior buildWithCheckScript:repairScript:]
+ +[RMModelPackageDeclaration_UninstallBehavior allowedPayloadKeys]
+ +[RMModelPackageDeclaration_UninstallBehavior buildRequiredOnlyWithUninstallScript:]
+ +[RMModelPackageDeclaration_UninstallBehavior buildWithUninstallScript:]
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:]
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:].cold.1
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:].cold.2
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:].cold.3
+ +[RMModelSchemaParser loadSupportedOSFromDictionary:].cold.4
+ +[RMModelStatusPackageList allowedStatusKeys]
+ +[RMModelStatusPackageList buildRequiredOnlyWithIdentifier:]
+ +[RMModelStatusPackageList buildWithIdentifier:removed:declarationIdentifier:name:version:state:reasons:]
+ +[RMModelStatusPackageList statusItemType]
+ +[RMModelStatusPackageList supportedOS]
+ -[RMModelAppManagedDeclaration payloadAppComposedIdentifier]
+ -[RMModelAppManagedDeclaration payloadIOSApp]
+ -[RMModelAppManagedDeclaration payloadUpdateBehavior]
+ -[RMModelAppManagedDeclaration setPayloadAppComposedIdentifier:]
+ -[RMModelAppManagedDeclaration setPayloadIOSApp:]
+ -[RMModelAppManagedDeclaration setPayloadUpdateBehavior:]
+ -[RMModelAppManagedDeclaration_InstallBehavior payloadAllowDownloadsOverCellular]
+ -[RMModelAppManagedDeclaration_InstallBehavior payloadVersion]
+ -[RMModelAppManagedDeclaration_InstallBehavior setPayloadAllowDownloadsOverCellular:]
+ -[RMModelAppManagedDeclaration_InstallBehavior setPayloadVersion:]
+ -[RMModelAppManagedDeclaration_UpdateBehavior .cxx_destruct]
+ -[RMModelAppManagedDeclaration_UpdateBehavior copyWithZone:]
+ -[RMModelAppManagedDeclaration_UpdateBehavior loadFromDictionary:serializationType:error:]
+ -[RMModelAppManagedDeclaration_UpdateBehavior payloadAutomaticAppUpdates]
+ -[RMModelAppManagedDeclaration_UpdateBehavior serializeWithType:]
+ -[RMModelAppManagedDeclaration_UpdateBehavior setPayloadAutomaticAppUpdates:]
+ -[RMModelConfigurationSchemaManagedSetting initWithManagedSetting:keyPath:valueType:invertBoolean:managedSettingScope:supportedOSOverride:parentSchema:]
+ -[RMModelConfigurationSchemaManagedSetting managedSettingScope]
+ -[RMModelPackageDeclaration .cxx_destruct]
+ -[RMModelPackageDeclaration assetReferences]
+ -[RMModelPackageDeclaration copyWithZone:]
+ -[RMModelPackageDeclaration loadPayloadFromDictionary:serializationType:error:]
+ -[RMModelPackageDeclaration payloadInstallBehavior]
+ -[RMModelPackageDeclaration payloadManifestURL]
+ -[RMModelPackageDeclaration payloadRepairBehavior]
+ -[RMModelPackageDeclaration payloadUninstallBehavior]
+ -[RMModelPackageDeclaration serializePayloadWithType:]
+ -[RMModelPackageDeclaration setPayloadInstallBehavior:]
+ -[RMModelPackageDeclaration setPayloadManifestURL:]
+ -[RMModelPackageDeclaration setPayloadRepairBehavior:]
+ -[RMModelPackageDeclaration setPayloadUninstallBehavior:]
+ -[RMModelPackageDeclaration_InstallBehavior .cxx_destruct]
+ -[RMModelPackageDeclaration_InstallBehavior copyWithZone:]
+ -[RMModelPackageDeclaration_InstallBehavior loadFromDictionary:serializationType:error:]
+ -[RMModelPackageDeclaration_InstallBehavior payloadInstallScript]
+ -[RMModelPackageDeclaration_InstallBehavior payloadInstall]
+ -[RMModelPackageDeclaration_InstallBehavior serializeWithType:]
+ -[RMModelPackageDeclaration_InstallBehavior setPayloadInstall:]
+ -[RMModelPackageDeclaration_InstallBehavior setPayloadInstallScript:]
+ -[RMModelPackageDeclaration_RepairBehavior .cxx_destruct]
+ -[RMModelPackageDeclaration_RepairBehavior copyWithZone:]
+ -[RMModelPackageDeclaration_RepairBehavior loadFromDictionary:serializationType:error:]
+ -[RMModelPackageDeclaration_RepairBehavior payloadCheckScript]
+ -[RMModelPackageDeclaration_RepairBehavior payloadRepairScript]
+ -[RMModelPackageDeclaration_RepairBehavior serializeWithType:]
+ -[RMModelPackageDeclaration_RepairBehavior setPayloadCheckScript:]
+ -[RMModelPackageDeclaration_RepairBehavior setPayloadRepairScript:]
+ -[RMModelPackageDeclaration_UninstallBehavior .cxx_destruct]
+ -[RMModelPackageDeclaration_UninstallBehavior copyWithZone:]
+ -[RMModelPackageDeclaration_UninstallBehavior loadFromDictionary:serializationType:error:]
+ -[RMModelPackageDeclaration_UninstallBehavior payloadUninstallScript]
+ -[RMModelPackageDeclaration_UninstallBehavior serializeWithType:]
+ -[RMModelPackageDeclaration_UninstallBehavior setPayloadUninstallScript:]
+ -[RMModelStatusPackageList .cxx_destruct]
+ -[RMModelStatusPackageList copyWithZone:]
+ -[RMModelStatusPackageList isArrayValue]
+ -[RMModelStatusPackageList loadPayloadFromDictionary:serializationType:error:]
+ -[RMModelStatusPackageList serializePayloadWithType:]
+ -[RMModelStatusPackageList setStatusDeclarationIdentifier:]
+ -[RMModelStatusPackageList setStatusIdentifier:]
+ -[RMModelStatusPackageList setStatusName:]
+ -[RMModelStatusPackageList setStatusReasons:]
+ -[RMModelStatusPackageList setStatusRemoved:]
+ -[RMModelStatusPackageList setStatusState:]
+ -[RMModelStatusPackageList setStatusVersion:]
+ -[RMModelStatusPackageList statusDeclarationIdentifier]
+ -[RMModelStatusPackageList statusIdentifier]
+ -[RMModelStatusPackageList statusName]
+ -[RMModelStatusPackageList statusReasons]
+ -[RMModelStatusPackageList statusRemoved]
+ -[RMModelStatusPackageList statusState]
+ -[RMModelStatusPackageList statusVersion]
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration_UpdateBehavior
+ _OBJC_CLASS_$_RMModelPackageDeclaration
+ _OBJC_CLASS_$_RMModelPackageDeclaration_InstallBehavior
+ _OBJC_CLASS_$_RMModelPackageDeclaration_RepairBehavior
+ _OBJC_CLASS_$_RMModelPackageDeclaration_UninstallBehavior
+ _OBJC_CLASS_$_RMModelStatusPackageList
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadAppComposedIdentifier
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadIOSApp
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration._payloadUpdateBehavior
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration_InstallBehavior._payloadAllowDownloadsOverCellular
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration_InstallBehavior._payloadVersion
+ _OBJC_IVAR_$_RMModelAppManagedDeclaration_UpdateBehavior._payloadAutomaticAppUpdates
+ _OBJC_IVAR_$_RMModelConfigurationSchemaManagedSetting._managedSettingScope
+ _OBJC_IVAR_$_RMModelPackageDeclaration._payloadInstallBehavior
+ _OBJC_IVAR_$_RMModelPackageDeclaration._payloadManifestURL
+ _OBJC_IVAR_$_RMModelPackageDeclaration._payloadRepairBehavior
+ _OBJC_IVAR_$_RMModelPackageDeclaration._payloadUninstallBehavior
+ _OBJC_IVAR_$_RMModelPackageDeclaration_InstallBehavior._payloadInstall
+ _OBJC_IVAR_$_RMModelPackageDeclaration_InstallBehavior._payloadInstallScript
+ _OBJC_IVAR_$_RMModelPackageDeclaration_RepairBehavior._payloadCheckScript
+ _OBJC_IVAR_$_RMModelPackageDeclaration_RepairBehavior._payloadRepairScript
+ _OBJC_IVAR_$_RMModelPackageDeclaration_UninstallBehavior._payloadUninstallScript
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusDeclarationIdentifier
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusIdentifier
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusName
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusReasons
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusRemoved
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusState
+ _OBJC_IVAR_$_RMModelStatusPackageList._statusVersion
+ _OBJC_METACLASS_$_RMModelAppManagedDeclaration_UpdateBehavior
+ _OBJC_METACLASS_$_RMModelPackageDeclaration
+ _OBJC_METACLASS_$_RMModelPackageDeclaration_InstallBehavior
+ _OBJC_METACLASS_$_RMModelPackageDeclaration_RepairBehavior
+ _OBJC_METACLASS_$_RMModelPackageDeclaration_UninstallBehavior
+ _OBJC_METACLASS_$_RMModelStatusPackageList
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_alwaysOff
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_alwaysOn
+ _RMModelAppManagedDeclaration_InstallBehavior_AllowDownloadsOverCellular_storeSettings
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_alwaysOff
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_alwaysOn
+ _RMModelAppManagedDeclaration_UpdateBehavior_AutomaticAppUpdates_storeSettings
+ _RMModelPackageDeclaration_InstallBehavior_Install_optional
+ _RMModelPackageDeclaration_InstallBehavior_Install_required
+ _RMModelStatusAppManagedList_State_notPresent
+ _RMModelStatusItemPackageList
+ _RMModelStatusPackageList_State_downloading
+ _RMModelStatusPackageList_State_failed
+ _RMModelStatusPackageList_State_installed
+ _RMModelStatusPackageList_State_installing
+ _RMModelStatusPackageList_State_optional
+ _RMModelStatusPackageList_State_promptingForConsent
+ _RMModelStatusPackageList_State_queued
+ __OBJC_$_CLASS_METHODS_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_$_CLASS_METHODS_RMModelPackageDeclaration
+ __OBJC_$_CLASS_METHODS_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_$_CLASS_METHODS_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_$_CLASS_METHODS_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_$_CLASS_METHODS_RMModelStatusPackageList
+ __OBJC_$_CLASS_PROP_LIST_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_$_CLASS_PROP_LIST_RMModelPackageDeclaration
+ __OBJC_$_CLASS_PROP_LIST_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_$_CLASS_PROP_LIST_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_$_CLASS_PROP_LIST_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_$_CLASS_PROP_LIST_RMModelStatusPackageList
+ __OBJC_$_INSTANCE_METHODS_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_$_INSTANCE_METHODS_RMModelPackageDeclaration
+ __OBJC_$_INSTANCE_METHODS_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_$_INSTANCE_METHODS_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_$_INSTANCE_METHODS_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusPackageList
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_$_INSTANCE_VARIABLES_RMModelPackageDeclaration
+ __OBJC_$_INSTANCE_VARIABLES_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_$_INSTANCE_VARIABLES_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_$_INSTANCE_VARIABLES_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusPackageList
+ __OBJC_$_PROP_LIST_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_$_PROP_LIST_RMModelPackageDeclaration
+ __OBJC_$_PROP_LIST_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_$_PROP_LIST_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_$_PROP_LIST_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_$_PROP_LIST_RMModelStatusPackageList
+ __OBJC_CLASS_PROTOCOLS_$_RMModelPackageDeclaration
+ __OBJC_CLASS_RO_$_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_CLASS_RO_$_RMModelPackageDeclaration
+ __OBJC_CLASS_RO_$_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_CLASS_RO_$_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_CLASS_RO_$_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_CLASS_RO_$_RMModelStatusPackageList
+ __OBJC_METACLASS_RO_$_RMModelAppManagedDeclaration_UpdateBehavior
+ __OBJC_METACLASS_RO_$_RMModelPackageDeclaration
+ __OBJC_METACLASS_RO_$_RMModelPackageDeclaration_InstallBehavior
+ __OBJC_METACLASS_RO_$_RMModelPackageDeclaration_RepairBehavior
+ __OBJC_METACLASS_RO_$_RMModelPackageDeclaration_UninstallBehavior
+ __OBJC_METACLASS_RO_$_RMModelStatusPackageList
+ ___53-[RMModelStatusPackageList serializePayloadWithType:]_block_invoke
+ ___54-[RMModelPackageDeclaration serializePayloadWithType:]_block_invoke
+ ___54-[RMModelPackageDeclaration serializePayloadWithType:]_block_invoke_2
+ ___54-[RMModelPackageDeclaration serializePayloadWithType:]_block_invoke_3
+ ___57-[RMModelAppManagedDeclaration serializePayloadWithType:]_block_invoke_5
+ ___block_literal_global.104
+ ___block_literal_global.477
+ ___block_literal_global.508
+ ___block_literal_global.58
+ ___block_literal_global.95
+ _objc_msgSend$initWithManagedSetting:keyPath:valueType:invertBoolean:managedSettingScope:supportedOSOverride:parentSchema:
+ _objc_msgSend$loadSupportedOSFromDictionary:
+ _objc_msgSend$managedSettingScope
+ _objc_msgSend$payloadAllowDownloadsOverCellular
+ _objc_msgSend$payloadAppComposedIdentifier
+ _objc_msgSend$payloadAutomaticAppUpdates
+ _objc_msgSend$payloadCheckScript
+ _objc_msgSend$payloadIOSApp
+ _objc_msgSend$payloadInstallScript
+ _objc_msgSend$payloadRepairBehavior
+ _objc_msgSend$payloadRepairScript
+ _objc_msgSend$payloadUninstallBehavior
+ _objc_msgSend$payloadUninstallScript
+ _objc_msgSend$payloadUpdateBehavior
+ _objc_msgSend$setPayloadAllowDownloadsOverCellular:
+ _objc_msgSend$setPayloadAppComposedIdentifier:
+ _objc_msgSend$setPayloadAutomaticAppUpdates:
+ _objc_msgSend$setPayloadCheckScript:
+ _objc_msgSend$setPayloadIOSApp:
+ _objc_msgSend$setPayloadInstallScript:
+ _objc_msgSend$setPayloadRepairBehavior:
+ _objc_msgSend$setPayloadRepairScript:
+ _objc_msgSend$setPayloadUninstallBehavior:
+ _objc_msgSend$setPayloadUninstallScript:
+ _objc_msgSend$setPayloadUpdateBehavior:
- +[RMModelAppManagedDeclaration buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:]
- +[RMModelAppManagedDeclaration_InstallBehavior buildWithInstall:license:]
- +[RMModelPayloadUtilities effectiveSupportedOS:overriddenSupportedOS:]
- +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:]
- +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.1
- +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.2
- +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.3
- +[RMModelSchemaParser loadSupportedOSFromDictionary:allowEmptyOS:].cold.4
- -[RMModelConfigurationSchemaManagedSetting initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:]
- ___70+[RMModelPayloadUtilities effectiveSupportedOS:overriddenSupportedOS:]_block_invoke
- ___block_descriptor_40_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
- ___block_literal_global.395
- ___block_literal_global.426
- ___block_literal_global.47
- ___block_literal_global.50
- ___block_literal_global.93
- ___block_literal_global.96
- _objc_msgSend$effectiveSupportedOS:overriddenSupportedOS:
- _objc_msgSend$initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:
- _objc_msgSend$loadSupportedOSFromDictionary:allowEmptyOS:
- _objc_msgSend$parentSchema
- _objc_msgSend$removeObjectForKey:
CStrings:
+ "@\"RMModelAppManagedDeclaration_UpdateBehavior\""
+ "@\"RMModelPackageDeclaration_InstallBehavior\""
+ "@\"RMModelPackageDeclaration_RepairBehavior\""
+ "@\"RMModelPackageDeclaration_UninstallBehavior\""
+ "@68@0:8@16@24@32B40@44@52@60"
+ "AllowDownloadsOverCellular"
+ "AppComposedIdentifier"
+ "AutomaticAppUpdates"
+ "CheckScript"
+ "InstallScript"
+ "RMModelAppManagedDeclaration_UpdateBehavior"
+ "RMModelPackageDeclaration"
+ "RMModelPackageDeclaration_InstallBehavior"
+ "RMModelPackageDeclaration_RepairBehavior"
+ "RMModelPackageDeclaration_UninstallBehavior"
+ "RMModelStatusPackageList"
+ "RepairBehavior"
+ "RepairScript"
+ "StoreSettings"
+ "T@\"NSNumber\",C,N,V_payloadIOSApp"
+ "T@\"NSNumber\",C,N,V_payloadVersion"
+ "T@\"NSString\",C,N,V_payloadAllowDownloadsOverCellular"
+ "T@\"NSString\",C,N,V_payloadAppComposedIdentifier"
+ "T@\"NSString\",C,N,V_payloadAutomaticAppUpdates"
+ "T@\"NSString\",C,N,V_payloadCheckScript"
+ "T@\"NSString\",C,N,V_payloadInstallScript"
+ "T@\"NSString\",C,N,V_payloadRepairScript"
+ "T@\"NSString\",C,N,V_payloadUninstallScript"
+ "T@\"NSString\",R,C,N,V_managedSettingScope"
+ "T@\"RMModelAppManagedDeclaration_UpdateBehavior\",C,N,V_payloadUpdateBehavior"
+ "T@\"RMModelPackageDeclaration_InstallBehavior\",C,N,V_payloadInstallBehavior"
+ "T@\"RMModelPackageDeclaration_RepairBehavior\",C,N,V_payloadRepairBehavior"
+ "T@\"RMModelPackageDeclaration_UninstallBehavior\",C,N,V_payloadUninstallBehavior"
+ "UninstallBehavior"
+ "UninstallScript"
+ "UpdateBehavior"
+ "_managedSettingScope"
+ "_payloadAllowDownloadsOverCellular"
+ "_payloadAppComposedIdentifier"
+ "_payloadAutomaticAppUpdates"
+ "_payloadCheckScript"
+ "_payloadIOSApp"
+ "_payloadInstallScript"
+ "_payloadRepairBehavior"
+ "_payloadRepairScript"
+ "_payloadUninstallBehavior"
+ "_payloadUninstallScript"
+ "_payloadUpdateBehavior"
+ "a"
+ "buildRequiredOnlyWithAutomaticAppUpdates:"
+ "buildRequiredOnlyWithCheckScript:repairScript:"
+ "buildRequiredOnlyWithIdentifier:manifestURL:"
+ "buildRequiredOnlyWithUninstallScript:"
+ "buildWithAutomaticAppUpdates:"
+ "buildWithCheckScript:repairScript:"
+ "buildWithIdentifier:appStoreID:bundleID:manifestURL:appComposedIdentifier:iosApp:installBehavior:updateBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:"
+ "buildWithIdentifier:manifestURL:installBehavior:repairBehavior:uninstallBehavior:"
+ "buildWithIdentifier:removed:declarationIdentifier:name:version:state:reasons:"
+ "buildWithInstall:installScript:"
+ "buildWithInstall:license:version:allowDownloadsOverCellular:"
+ "buildWithUninstallScript:"
+ "com.apple.configuration.package"
+ "iOSApp"
+ "initWithManagedSetting:keyPath:valueType:invertBoolean:managedSettingScope:supportedOSOverride:parentSchema:"
+ "installed"
+ "loadSupportedOSFromDictionary:"
+ "managedSettingScope"
+ "not-present"
+ "package.list"
+ "payloadAllowDownloadsOverCellular"
+ "payloadAppComposedIdentifier"
+ "payloadAutomaticAppUpdates"
+ "payloadCheckScript"
+ "payloadIOSApp"
+ "payloadInstallScript"
+ "payloadRepairBehavior"
+ "payloadRepairScript"
+ "payloadUninstallBehavior"
+ "payloadUninstallScript"
+ "payloadUpdateBehavior"
+ "scope"
+ "setPayloadAllowDownloadsOverCellular:"
+ "setPayloadAppComposedIdentifier:"
+ "setPayloadAutomaticAppUpdates:"
+ "setPayloadCheckScript:"
+ "setPayloadIOSApp:"
+ "setPayloadInstallScript:"
+ "setPayloadRepairBehavior:"
+ "setPayloadRepairScript:"
+ "setPayloadUninstallBehavior:"
+ "setPayloadUninstallScript:"
+ "setPayloadUpdateBehavior:"
- "@28@0:8@16B24"
- "@60@0:8@16@24@32B40@44@52"
- "Q"
- "buildWithIdentifier:appStoreID:bundleID:manifestURL:installBehavior:includeInBackup:attributes:appConfig:extensionConfigs:legacyAppConfigAssetReference:"
- "buildWithInstall:license:"
- "effectiveSupportedOS:overriddenSupportedOS:"
- "initWithManagedSetting:keyPath:valueType:invertBoolean:supportedOSOverride:parentSchema:"
- "loadSupportedOSFromDictionary:allowEmptyOS:"
- "removeObjectForKey:"
- "v32@?0@\"NSNumber\"8@\"NSArray\"16^B24"

```
