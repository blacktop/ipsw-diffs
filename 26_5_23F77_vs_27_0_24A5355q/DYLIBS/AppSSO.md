## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-483.120.4.0.0
-  __TEXT.__text: 0x2a278
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x1a94
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x1c84
-  __TEXT.__cstring: 0x313b
-  __TEXT.__dlopen_cstrs: 0x638
-  __TEXT.__oslogstring: 0x42f6
-  __TEXT.__unwind_info: 0xd90
-  __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x4b9e
-  __TEXT.__objc_methtype: 0xa91
-  __TEXT.__objc_stubs: 0x3a40
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0xcc8
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x88
+635.0.0.0.0
+  __TEXT.__text: 0x2bb40
+  __TEXT.__objc_methlist: 0x1c2c
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x1958
+  __TEXT.__oslogstring: 0x4bb8
+  __TEXT.__cstring: 0x37d9
+  __TEXT.__dlopen_cstrs: 0x6dc
+  __TEXT.__unwind_info: 0xe28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e0
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_selrefs: 0x12f8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x11e0
-  __AUTH_CONST.__objc_const: 0x40a8
+  __DATA_CONST.__got: 0x240
+  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__objc_const: 0x4900
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x670
-  __DATA.__bss: 0x210
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x174
+  __DATA.__data: 0x6d0
+  __DATA.__bss: 0x230
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43C41B79-121A-360C-8AD3-6407EB761564
-  Functions: 986
-  Symbols:   3555
-  CStrings:  1702
+  UUID: CBCAEA41-C55C-3147-BCAE-1601C0AFB01F
+  Functions: 1067
+  Symbols:   3820
+  CStrings:  885
 
Symbols:
+ +[SOConfigurationHost _loadProfilesFromArray:]
+ +[SOConfigurationHost _loadProfilesFromArray:].cold.1
+ +[SOConfigurationHost _loadProfilesFromArray:].cold.2
+ +[SOConfigurationHost _loadProfilesFromArray:].cold.3
+ -[SOConfigurationHost _configurationsChangedWithSuccess:]
+ -[SOConfigurationHost _configurationsChangedWithSuccess:].cold.1
+ -[SOConfigurationHost _loadConfigForFirstTime].cold.1
+ -[SOConfigurationHost _mergeDDMProfiles:mdmProfiles:]
+ -[SOConfigurationHost _reloadConfigWithReason:].cold.2
+ -[SOConfigurationHost _reloadConfigWithReason:].cold.3
+ -[SOConfigurationHost _reloadConfigWithReason:].cold.4
+ -[SOConfigurationHost ddmConfigurationsChanged]
+ -[SOConfigurationHost hasAnyMDMProfileForExtension:].cold.4
+ -[SOConfigurationHost hasAnyMDMProfileForExtension:].cold.5
+ -[SOConfigurationHost platformSSOProfile].cold.4
+ -[SOConfigurationHost platformSSOProfile].cold.5
+ -[SOConfigurationHost systemMDMProfileForExtension:].cold.4
+ -[SOConfigurationHost systemMDMProfileForExtension:].cold.5
+ -[SOConfigurationManager _createDDMConfigurationXPCConnection]
+ -[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]
+ -[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]
+ -[SOConfigurationManager removeDDMConfiguration:completion:]
+ -[SODDMConfigurationHost _configurationFileForCurrentContext:]
+ -[SODDMConfigurationHost _defaultConfigurationPath]
+ -[SODDMConfigurationHost _defaultDDMConfigurationFile]
+ -[SODDMConfigurationHost _initDataVaultIfNeededWithError:]
+ -[SODDMConfigurationHost _initDataVaultIfNeededWithError:].cold.1
+ -[SODDMConfigurationHost _initDataVaultIfNeededWithError:].cold.2
+ -[SODDMConfigurationHost _initDataVaultIfNeededWithError:].cold.3
+ -[SODDMConfigurationHost _loadDDMConfigurationFromDisk:]
+ -[SODDMConfigurationHost _loadDDMConfigurationFromDisk:].cold.1
+ -[SODDMConfigurationHost _loadDDMConfigurationFromDisk:].cold.2
+ -[SODDMConfigurationHost _saveDDMConfigurationToDisk:error:]
+ -[SODDMConfigurationHost _saveDDMConfigurationToDisk:error:].cold.1
+ -[SODDMConfigurationHost _saveDDMConfigurationToDisk:error:].cold.2
+ -[SODDMConfigurationHost _saveDDMConfigurationToDisk:error:].cold.3
+ -[SODDMConfigurationHost allDeclarationKeysWithError:]
+ -[SODDMConfigurationHost allDeclarationKeysWithError:].cold.1
+ -[SODDMConfigurationHost applyConfiguration:replaceKey:error:]
+ -[SODDMConfigurationHost applyConfiguration:replaceKey:error:].cold.1
+ -[SODDMConfigurationHost applyConfiguration:replaceKey:error:].cold.2
+ -[SODDMConfigurationHost loadDDMConfigurationsWithError:]
+ -[SODDMConfigurationHost loadDDMConfigurationsWithError:].cold.1
+ -[SODDMConfigurationHost loadDDMSystemConfigurationsWithError:]
+ -[SODDMConfigurationHost loadDDMSystemConfigurationsWithError:].cold.1
+ -[SODDMConfigurationHost loadDDMSystemConfigurationsWithError:].cold.2
+ -[SODDMConfigurationHost loadDDMSystemConfigurationsWithError:].cold.3
+ -[SODDMConfigurationHost removeConfiguration:error:]
+ -[SODDMConfigurationHost removeConfiguration:error:].cold.1
+ -[SODDMConfigurationService .cxx_destruct]
+ -[SODDMConfigurationService _verifyEntitlement]
+ -[SODDMConfigurationService _verifyEntitlement].cold.1
+ -[SODDMConfigurationService _verifyEntitlement].cold.2
+ -[SODDMConfigurationService allDeclarationKeysWithCompletion:]
+ -[SODDMConfigurationService allDeclarationKeysWithCompletion:].cold.1
+ -[SODDMConfigurationService allDeclarationKeysWithCompletion:].cold.2
+ -[SODDMConfigurationService applyConfiguration:replaceKey:completion:]
+ -[SODDMConfigurationService applyConfiguration:replaceKey:completion:].cold.1
+ -[SODDMConfigurationService applyConfiguration:replaceKey:completion:].cold.2
+ -[SODDMConfigurationService connectionInvalidated]
+ -[SODDMConfigurationService dealloc]
+ -[SODDMConfigurationService initWithXPCConnection:]
+ -[SODDMConfigurationService invalidationHandler]
+ -[SODDMConfigurationService removeConfiguration:completion:]
+ -[SODDMConfigurationService removeConfiguration:completion:].cold.1
+ -[SODDMConfigurationService removeConfiguration:completion:].cold.2
+ -[SODDMConfigurationService setInvalidationHandler:]
+ -[SOExtension dealloc].cold.1
+ GCC_except_table24
+ GCC_except_table35
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table53
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_SODDMConfigurationHost
+ _OBJC_CLASS_$_SODDMConfigurationService
+ _OBJC_IVAR_$_SODDMConfigurationService._configHost
+ _OBJC_IVAR_$_SODDMConfigurationService._invalidationHandler
+ _OBJC_IVAR_$_SODDMConfigurationService._xpcConnection
+ _OBJC_METACLASS_$_SODDMConfigurationHost
+ _OBJC_METACLASS_$_SODDMConfigurationService
+ _SO_LOG_SODDMConfigurationHost
+ _SO_LOG_SODDMConfigurationHost.cold.1
+ _SO_LOG_SODDMConfigurationHost.log
+ _SO_LOG_SODDMConfigurationHost.once
+ _SO_LOG_SODDMConfigurationService
+ _SO_LOG_SODDMConfigurationService.cold.1
+ _SO_LOG_SODDMConfigurationService.log
+ _SO_LOG_SODDMConfigurationService.once
+ __OBJC_$_INSTANCE_METHODS_SODDMConfigurationHost
+ __OBJC_$_INSTANCE_METHODS_SODDMConfigurationService
+ __OBJC_$_INSTANCE_VARIABLES_SODDMConfigurationService
+ __OBJC_$_PROP_LIST_SODDMConfigurationService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SODDMConfigurationServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SODDMConfigurationServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_SODDMConfigurationServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SODDMConfigurationService
+ __OBJC_CLASS_RO_$_SODDMConfigurationHost
+ __OBJC_CLASS_RO_$_SODDMConfigurationService
+ __OBJC_LABEL_PROTOCOL_$_SODDMConfigurationServiceProtocol
+ __OBJC_METACLASS_RO_$_SODDMConfigurationHost
+ __OBJC_METACLASS_RO_$_SODDMConfigurationService
+ __OBJC_PROTOCOL_$_SODDMConfigurationServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SODDMConfigurationServiceProtocol
+ ___60-[SOConfigurationManager removeDDMConfiguration:completion:]_block_invoke
+ ___60-[SOConfigurationManager removeDDMConfiguration:completion:]_block_invoke.64
+ ___60-[SOConfigurationManager removeDDMConfiguration:completion:]_block_invoke_2
+ ___60-[SOConfigurationManager removeDDMConfiguration:completion:]_block_invoke_2.cold.1
+ ___62-[SOConfigurationManager _createDDMConfigurationXPCConnection]_block_invoke
+ ___62-[SOConfigurationManager _createDDMConfigurationXPCConnection]_block_invoke.57
+ ___62-[SOConfigurationManager _createDDMConfigurationXPCConnection]_block_invoke.57.cold.1
+ ___62-[SOConfigurationManager _createDDMConfigurationXPCConnection]_block_invoke.cold.1
+ ___62-[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]_block_invoke
+ ___62-[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]_block_invoke.61
+ ___62-[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]_block_invoke_2
+ ___62-[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]_block_invoke_2.cold.1
+ ___62-[SODDMConfigurationHost applyConfiguration:replaceKey:error:]_block_invoke
+ ___70-[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]_block_invoke
+ ___70-[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]_block_invoke.63
+ ___70-[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]_block_invoke_2
+ ___70-[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]_block_invoke_2.cold.1
+ ___SO_LOG_SODDMConfigurationHost_block_invoke
+ ___SO_LOG_SODDMConfigurationService_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.120
+ ___block_literal_global.192
+ ___block_literal_global.222
+ ___block_literal_global.36
+ ___block_literal_global.56
+ ___block_literal_global.59
+ ___block_literal_global.74
+ ___block_literal_global.76
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_configurationFileForCurrentContext:
+ _objc_msgSend$_configurationsChangedWithSuccess:
+ _objc_msgSend$_createDDMConfigurationXPCConnection
+ _objc_msgSend$_defaultDDMConfigurationFile
+ _objc_msgSend$_loadDDMConfigurationFromDisk:
+ _objc_msgSend$_loadProfilesFromArray:
+ _objc_msgSend$_mergeDDMProfiles:mdmProfiles:
+ _objc_msgSend$_saveDDMConfigurationToDisk:error:
+ _objc_msgSend$_verifyEntitlement
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allDeclarationKeysWithCompletion:
+ _objc_msgSend$allDeclarationKeysWithError:
+ _objc_msgSend$applyConfiguration:replaceKey:completion:
+ _objc_msgSend$applyConfiguration:replaceKey:error:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$checkEntitlementFromXPC:entitlement:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$ddmConfigurationsChanged
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$loadDDMConfigurationsWithError:
+ _objc_msgSend$loadDDMSystemConfigurationsWithError:
+ _objc_msgSend$missingEntitlementError:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$removeConfiguration:completion:
+ _objc_msgSend$removeConfiguration:error:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x9
- +[SOConfigurationHost _loadProfilesFromDict:].cold.2
- +[SOConfigurationHost _loadProfilesFromDict:].cold.3
- +[SOConfigurationHost _loadProfilesFromDict:].cold.4
- -[SOConfigurationHost saveConfiguration:error:].cold.2
- GCC_except_table114
- GCC_except_table115
- GCC_except_table25
- GCC_except_table37
- GCC_except_table43
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- ___block_literal_global.121
- ___block_literal_global.193
- ___block_literal_global.215
- ___block_literal_global.37
- ___block_literal_global.7
- ___block_literal_global.77
CStrings:
+ "%s Configurations changed on %@"
+ "%s DDM configurations changed on %@"
+ "%s applying configuration on %@"
+ "%s applying configuration: %{private}@ on %@"
+ "%s ddmProfiles = %{public}@, mdmProfiles = %{public}@ on %@"
+ "%s removing configuration with declarationKey: %{public}@ on %@"
+ "%s removing configuration: %{public}@ on %@"
+ "+[SOConfigurationHost _loadProfilesFromArray:]"
+ "-[SOConfigurationHost _configurationsChangedWithSuccess:]"
+ "-[SOConfigurationHost _mergeDDMProfiles:mdmProfiles:]"
+ "-[SOConfigurationHost ddmConfigurationsChanged]"
+ "-[SOConfigurationManager allDDMDeclarationKeysWithCompletion:]"
+ "-[SOConfigurationManager applyDDMConfiguration:replaceKey:completion:]"
+ "-[SOConfigurationManager removeDDMConfiguration:completion:]"
+ "-[SODDMConfigurationHost _initDataVaultIfNeededWithError:]"
+ "-[SODDMConfigurationHost _loadDDMConfigurationFromDisk:]"
+ "-[SODDMConfigurationHost _saveDDMConfigurationToDisk:error:]"
+ "-[SODDMConfigurationHost allDeclarationKeysWithError:]"
+ "-[SODDMConfigurationHost applyConfiguration:replaceKey:error:]"
+ "-[SODDMConfigurationHost loadDDMConfigurationsWithError:]"
+ "-[SODDMConfigurationHost loadDDMSystemConfigurationsWithError:]"
+ "-[SODDMConfigurationHost removeConfiguration:error:]"
+ "-[SODDMConfigurationService allDeclarationKeysWithCompletion:]"
+ "-[SODDMConfigurationService applyConfiguration:replaceKey:completion:]"
+ "-[SODDMConfigurationService connectionInvalidated]"
+ "-[SODDMConfigurationService dealloc]"
+ "-[SODDMConfigurationService initWithXPCConnection:]"
+ "-[SODDMConfigurationService removeConfiguration:completion:]"
+ "Added configuration for key: %{public}@"
+ "Checking DDM profiles"
+ "Checking DDM system profiles"
+ "Client does not have required entitlement: %{public}@"
+ "Client missing required entitlement"
+ "Configuration missing declarationKey"
+ "Configuration must contain a non-empty declarationKey"
+ "Configuration with replaceKey %{public}@ not found; appending new configuration for key: %{public}@"
+ "DDM config written to file: %{public}@"
+ "DDM configuration XPC connection interrupted"
+ "DDM configuration XPC connection invalidated"
+ "DDM configuration file doesn't exist yet: %{public}@"
+ "DDM configurations inored"
+ "DDMConfigurations"
+ "Error loading DDM configuration from %{public}@: %{public}@"
+ "Error loading system DDM configuration: %{public}@"
+ "ExtensibleSSOConfiguration"
+ "Extension found but config missing profile -- forcing immediate reload"
+ "Failed to apply configuration: %{public}@"
+ "Failed to get declaration keys: %{public}@"
+ "Failed to get remote object proxy: %{public}@"
+ "Failed to load DDM configurations: %{public}@"
+ "Failed to remove configuration: %{public}@"
+ "Found %lu declaration keys"
+ "Invalid declarationKey"
+ "Loaded %lu DDM configurations from system path: %{public}@"
+ "Loaded %lu DDM profiles"
+ "Loaded DDM config from: %{public}@"
+ "Loaded total of %lu DDM configurations"
+ "No DDM configurations found"
+ "No XPC connection"
+ "No configuration found with declarationKey: %{public}@"
+ "No configurations array found"
+ "No system DDM configurations from system path: %{public}@"
+ "RemoteManagement"
+ "Removed configuration for declarationKey: %{public}@"
+ "Replaced configuration at key: %{public}@ (previously: %{public}@)"
+ "Returning %lu declaration keys"
+ "SODDMConfigurationHost"
+ "SODDMConfigurationService"
+ "SOExtension deallocated with active sessionID — unload was not called"
+ "Successfully applied configuration"
+ "Successfully removed configuration"
+ "Total profiles after DDM merge: %lu"
+ "com.apple.AppSSO.DDMConfigurationChanged"
+ "com.apple.AppSSO.ddm-configuration-xpc"
+ "com.apple.AppSSO.ddm.plist"
+ "com.apple.private.AppSSO.configuration"
+ "configuration cannot be nil"
+ "datavault re-initialized on startup, retrying config load"
+ "datavault recovery on startup failed: %{public}@"
+ "declarationKey"
+ "declarationKey cannot be empty"
+ "declarationKey cannot be nil or empty"
+ "failed to save DDM config to file: %{public}@, error: %{public}@"
+ "failed to serialize property list, error: %{public}@"
+ "found DDM system profile for extension: %{public}@"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<ASAuthorizationProviderExtensionAuthorizationRequestHandler><POExtensionRegistrationProtocol>\""
- "@\"<SOAuthorizationDelegate>\""
- "@\"<SOQueueItem>\""
- "@\"<SORemoteExtensionViewControllerDelegate>\""
- "@\"<SOServiceProtocol>\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSExtension\""
- "@\"NSHTTPURLResponse\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@\"POLoginManager\""
- "@\"SOAuthorizationCore\""
- "@\"SOAuthorizationCredential\""
- "@\"SOAuthorizationParametersCore\""
- "@\"SOAuthorizationRequestParameters\""
- "@\"SOAuthorizationRequestParameters\"16@0:8"
- "@\"SOAuthorizationResultCore\""
- "@\"SOConfiguration\""
- "@\"SOConfigurationVersion\""
- "@\"SOExtension\""
- "@\"SOExtensionFinder\""
- "@\"SOExtensionServiceConnection\""
- "@\"SOExtensionViewService\""
- "@\"SORemoteExtensionContext\""
- "@\"SORemoteExtensionViewController\""
- "@\"SOUIAuthorizationViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURL\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8^{__CFString=}16B24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16q24"
- "B36@0:8@16q24B32"
- "B44@0:8@16q24@32B40"
- "Internal"
- "JSONObjectWithData:options:error:"
- "Kerberos"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "POExtensionRegistrationHostProtocol"
- "Process"
- "Q16@0:8"
- "SOAuthorizationHints"
- "SOAuthorizationParameters"
- "SOAuthorizationRequestParameters"
- "SOAuthorizationResult"
- "SODebugHints"
- "SOExtensionContext"
- "SOExtensionContextProtocol"
- "SOExtensionDelegate"
- "SOExtensionServiceProtocol"
- "SOExtensionViewProtocol"
- "SOHostExtensionContextProtocol"
- "SOHostExtensionViewProtocol"
- "SOQueueItem"
- "SORemoteExtensionContextProtocol"
- "SORemoteExtensionServiceProtocol"
- "SORemoteExtensionViewControllerDelegate"
- "SORemoteExtensionViewProtocol"
- "SORequestQueueItem"
- "SOUIAuthorizationViewControllerDelegate"
- "T#,R"
- "T@\"<ASAuthorizationProviderExtensionAuthorizationRequestHandler>\",R,N"
- "T@\"<SOAuthorizationDelegate>\",W,V_delegate"
- "T@\"<SORemoteExtensionViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<SOServiceProtocol>\",R,N,V_service"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_associatedDomains"
- "T@\"NSArray\",&,N,V_secKeyProxies"
- "T@\"NSArray\",&,N,V_secKeyProxyEndpoints"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_loadedExtensions"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_auditTokenData"
- "T@\"NSData\",&,N,V_httpBody"
- "T@\"NSData\",C,N,V_httpBody"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,V_authorizationOptions"
- "T@\"NSDictionary\",&,N,V_httpAuthorizationHeaders"
- "T@\"NSDictionary\",C,N,V_extensionData"
- "T@\"NSDictionary\",C,N,V_httpHeaders"
- "T@\"NSError\",&,N,V_canceledAuthorizationError"
- "T@\"NSExtension\",&,N,V_extension"
- "T@\"NSHTTPURLResponse\",C,N"
- "T@\"NSHTTPURLResponse\",C,N,V_httpResponse"
- "T@\"NSMutableDictionary\",&,V_associatedDomainCache"
- "T@\"NSObject\",&,N,V_cancelLock"
- "T@\"NSObject\",&,V_associatedDomainLock"
- "T@\"NSObject\",&,V_configurationPendingLock"
- "T@\"NSObject\",&,V_extensionDelegatesLock"
- "T@\"NSObject\",&,V_requestCountLock"
- "T@\"NSObject\",&,V_sessionIDLock"
- "T@\"NSObject<OS_dispatch_queue>\",&"
- "T@\"NSString\",&"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_callerBundleIdentifier"
- "T@\"NSString\",C,N,V_callerTeamIdentifier"
- "T@\"NSString\",C,N,V_impersonationBundleIdentifier"
- "T@\"NSString\",C,N,V_localizedCallerDisplayName"
- "T@\"NSString\",C,N,V_realm"
- "T@\"NSString\",C,N,V_requestedOperation"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_localizedExtensionBundleDisplayName"
- "T@\"NSURL\",&,N"
- "T@\"NSURL\",C,N,V_url"
- "T@\"NSUUID\",R,N"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"NSXPCListenerEndpoint\",&,V_serviceXpcEndpoint"
- "T@\"POLoginManager\",R,N,V_loginManager"
- "T@\"SOAuthorizationCredential\",&,N,V_canceledAuthorizationCredential"
- "T@\"SOAuthorizationParametersCore\",R,N"
- "T@\"SOAuthorizationRequestParameters\",R,N"
- "T@\"SOAuthorizationRequestParameters\",R,N,V_requestParameters"
- "T@\"SOExtension\",W,V_contextExtension"
- "T@\"SOExtensionViewService\",W,V_viewService"
- "T@\"SORemoteExtensionContext\",W,V_extensionContext"
- "T@?,C,N,V_processItemBlock"
- "T@?,C,V_groupsCompletion"
- "T@?,C,V_pictureCompletion"
- "T@?,C,V_registrationCompletion"
- "T@?,C,V_rotationCompletion"
- "T@?,R,C,N,V_completionBlock"
- "TB"
- "TB,N"
- "TB,N,GcanShowOnCoverScreen"
- "TB,N,GcanShowOnCoverScreen,V_showOnCoverScreen"
- "TB,N,GisAuthorizationCanceled,V_authorizationCanceled"
- "TB,N,GisCFNetworkInterception,SsetCFNetworkInterception:"
- "TB,N,GisCFNetworkInterception,V_cfNetworkInterception"
- "TB,N,GisCallerManaged"
- "TB,N,GisCallerManaged,V_callerManaged"
- "TB,N,GisUserInteractionEnabled"
- "TB,N,GisUserInteractionEnabled,V_enableUserInteraction"
- "TB,N,V_cancelled"
- "TB,N,V_enableEmbeddedAuthorizationViewController"
- "TB,N,V_useInternalExtensions"
- "TB,R"
- "TB,R,N"
- "TB,V_configurationPending"
- "TB,V_isRunning"
- "TQ,R"
- "Ti,N,V_secKeyProxiesConnectedClients"
- "Ti,R,N,V_requestCount"
- "Tq,N"
- "Tq,N,V_pssoAuthenticationMethod"
- "Tq,N,V_responseCode"
- "Tq,R,N"
- "URLPrefix"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UUID"
- "_applicationActivationWithTimeout:"
- "_associatedDomainCache"
- "_associatedDomainLock"
- "_associatedDomains"
- "_auditTokenData"
- "_authorizationCanceled"
- "_authorizationCore"
- "_authorizationOptions"
- "_authorizationParametersCore"
- "_authorizationResultCore"
- "_authorizationViewController"
- "_auxiliaryConnection"
- "_beginAuthorizationWithRequestParameters:completion:"
- "_beginAuthorizationWithServiceXPCEndpoint:completion:"
- "_callerBundleIdentifier"
- "_callerManaged"
- "_callerTeamIdentifier"
- "_cancelAuthorization"
- "_cancelLock"
- "_canceledAuthorizationCredential"
- "_canceledAuthorizationError"
- "_cancelled"
- "_cfNetworkInterception"
- "_checkAssociatedDomainForProfiles:"
- "_checkExtensionsExistenceForProfiles:"
- "_checkNewVersion"
- "_completeFinishAuthorizationWithRequestIdentifier:error:"
- "_completionBlock"
- "_configuration"
- "_configurationLoadedWithReason:"
- "_configurationPending"
- "_configurationPendingLock"
- "_configurationVersion"
- "_connectChildView"
- "_connectContextToSessionWithRequestIdentifier:completion:"
- "_connectToService"
- "_contextExtension"
- "_contextForSession"
- "_createSecKeyProxiesForSecKeys:error:"
- "_defaultCacheFile"
- "_defaultConfigurationFile"
- "_defaultConfigurationPath"
- "_delegate"
- "_disableAppSSO"
- "_disableAppSSOInCFNetwork"
- "_doBeginMatchingExtensions"
- "_doEndMatchingExtensions"
- "_doLoadExtensions"
- "_enableEmbeddedAuthorizationViewController"
- "_enableUserInteraction"
- "_exportedInterface"
- "_extension"
- "_extensionAuthorizationRequestHandler"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionBundle"
- "_extensionCleanup"
- "_extensionContext"
- "_extensionContextForUUID:"
- "_extensionData"
- "_extensionDelegates"
- "_extensionDelegatesLock"
- "_extensionFinder"
- "_extensionFinderQueue"
- "_extensionManagerQueue"
- "_extensionServiceConnection"
- "_extensionViewController"
- "_extensionsLoaded:"
- "_finishAuthorization:completion:"
- "_finishAuthorization:withCompletion:"
- "_finishAuthorizationCompletion"
- "_finishAuthorizationWithCredential:error:"
- "_finishedSettingUpSession:"
- "_groupsCompletion"
- "_hostExtensionContext"
- "_httpAuthorizationHeaders"
- "_httpBody"
- "_httpHeaders"
- "_httpResponse"
- "_identifier"
- "_impersonationBundleIdentifier"
- "_initCachePath:ifNeededWithError:"
- "_initDataVaultIfNeededWithError:"
- "_invalidateLoginManager"
- "_isConfigFileAvailable"
- "_isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:"
- "_isMatchedExtension:forBundleIdentifier:"
- "_isRunning"
- "_isUserInterfaceAllowed"
- "_itemCompleted"
- "_loadCacheFromDisk"
- "_loadConfigForFirstTime"
- "_loadProfilesFromDict:"
- "_loadProfilesFromURL:logFileError:"
- "_loadedExtensions"
- "_localizedCallerDisplayName"
- "_localizedExtensionBundleDisplayName"
- "_loginManager"
- "_matchingContext"
- "_mergeProfile:userProfiles:"
- "_otherVersionError:"
- "_pendingFinishAuthorizationBlock"
- "_pictureCompletion"
- "_plugIn"
- "_principalObject"
- "_processItem:"
- "_processItemBlock"
- "_processingItem"
- "_pssoAuthenticationMethod"
- "_pssoQueue"
- "_queue"
- "_realm"
- "_registrationCompletion"
- "_reloadConfigWithReason:"
- "_remoteExtensionContext"
- "_remoteViewController"
- "_remoteViewControllerInterface"
- "_removeNotSupportedUserProfiles:"
- "_removedProfiles"
- "_requestCount"
- "_requestCountLock"
- "_requestParameters"
- "_requestedOperation"
- "_requests"
- "_responseCode"
- "_rotationCompletion"
- "_saveCacheToFile:error:"
- "_saveConfigToFile:error:"
- "_secKeyProxies"
- "_secKeyProxiesConnectedClients"
- "_secKeyProxyEndpoints"
- "_sendNotificationsLoadedExtensions:new:removed:"
- "_service"
- "_serviceXpcEndpoint"
- "_sessionID"
- "_sessionIDLock"
- "_setPrincipalObject:forUUID:"
- "_setupExtension"
- "_setupNonUISessionIfNecessaryWithCompletion:"
- "_setupNonUISessionWithCompletion:"
- "_setupSessionHelperForIOSWithCompletion:"
- "_setupSessionIfNecessaryWithCompletion:"
- "_setupSessionWithCompletion:"
- "_sharedExtensionContextVendor"
- "_showOnCoverScreen"
- "_soExtensionsForExtensions:"
- "_startKeyBagObserverForReloadingConfiguration"
- "_stringWithReason:"
- "_url"
- "_useInternalExtensions"
- "_viewService"
- "_xpcConnection"
- "activateConstraints:"
- "addChildViewController:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "allKeys"
- "analyticsForMDMProfiles:reason:"
- "applicationDidBecomeActive:"
- "applicationState"
- "array"
- "arrayByAddingObject:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "associatedDomainCache"
- "associatedDomainLock"
- "associatedDomains"
- "auditToken"
- "auditTokenData"
- "auditTokenForSession"
- "authMethodWithString:"
- "authenticationMethods"
- "authorization:didCompleteWithAuthorizationResult:"
- "authorization:didCompleteWithCredential:error:"
- "authorization:didCompleteWithError:"
- "authorization:didCompleteWithHTTPAuthorizationHeaders:"
- "authorization:didCompleteWithHTTPResponse:httpBody:"
- "authorization:presentViewController:withCompletion:"
- "authorizationCanceled"
- "authorizationDidCancel:"
- "authorizationDidComplete:"
- "authorizationDidFailWithOtherVersionError:"
- "authorizationDidNotHandle:"
- "authorizationEnabled"
- "authorizationOptions"
- "authorizationParametersCore"
- "authorizationRequest"
- "authorizationRequestHandlerWithRequestParameters:error:"
- "autorelease"
- "beginAuthorizationWithCompletion:"
- "beginAuthorizationWithOperation:url:httpHeaders:httpBody:"
- "beginAuthorizationWithParameters:"
- "beginAuthorizationWithParameters:completion:"
- "beginAuthorizationWithRequest:"
- "beginAuthorizationWithRequestParameters:completion:"
- "beginAuthorizationWithServiceXPCEndpoint:completion:"
- "beginAuthorizationWithURL:httpHeaders:httpBody:"
- "beginDeviceRegistrationUsingOptions:extensionData:completion:"
- "beginExtensionRequestWithInputItems:error:"
- "beginMatchingExtensions"
- "beginMatchingExtensionsWithAttributes:completion:"
- "beginMatchingExtensionsWithCompletion:"
- "beginUserRegistrationUsingUserName:authenticationMethod:options:extensionData:completion:"
- "boolValue"
- "boolValueForKey:defaultValue:"
- "bottomAnchor"
- "bundleURL"
- "bundleWithPath:"
- "cStringUsingEncoding:"
- "callerBundleIdentifier"
- "callerManaged"
- "callerTeamIdentifier"
- "canOpenURL:"
- "canOpenURL:completionHandler:"
- "canPerformAuthorizationWithURL:responseCode:"
- "canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:"
- "canPerformAuthorizationWithURL:responseCode:callerBundleIdentifier:useInternalExtensions:completion:"
- "canPerformAuthorizationWithURL:responseCode:useInternalExtensions:"
- "canPerformRegistrationCompletion:"
- "canShowOnCoverScreen"
- "cancel"
- "cancelAuthorization:completion:"
- "cancelAuthorizationWithRequest:"
- "cancelExtensionRequestWithIdentifier:"
- "cancelLock"
- "canceledAuthorizationCredential"
- "canceledAuthorizationError"
- "cancelled"
- "cfNetworkInterception"
- "checkAssociatedDomainsWithCache:"
- "checkAssociatedDomainsWithCompletion:"
- "checkVersion"
- "class"
- "code"
- "complete"
- "completeFinishAuthorization:error:"
- "completeWithAuthorizationResult:"
- "completeWithError:"
- "completeWithHTTPAuthorizationHeaders:"
- "completeWithHTTPResponse:httpBody:"
- "completionBlock"
- "configVersion"
- "configurationForClientWithError:"
- "configurationPending"
- "configurationPendingLock"
- "configurationWithCompletion:"
- "conformsToProtocol:"
- "connectToContextWithSessionID:completion:"
- "constraintEqualToAnchor:"
- "containerAppBundleIdentifier"
- "containerAppPath"
- "containingBundle"
- "containingUrl"
- "containsObject:"
- "contextExtension"
- "copy"
- "copyProfile"
- "copyProfileForClient"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createFirstUserDuringSetupEnabled"
- "createSecKeysFromSecKeyProxyEndpoints:error:"
- "dataWithContentsOfURL:options:error:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "debugHintsWithCompletion:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decrementRequestCount"
- "defaultCenter"
- "defaultClient"
- "defaultManager"
- "defaultWorkspace"
- "delegate"
- "delegateDispatchQueue"
- "description"
- "dictionary"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "displayNamesForGroups:extensionData:completion:"
- "doNotHandle"
- "domain"
- "domainHost"
- "domainPort"
- "doubleValue"
- "empty"
- "enableEmbeddedAuthorizationViewController"
- "enableUserInteraction"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endMatchingExtensions"
- "endMatchingExtensions:"
- "endpoint"
- "enqueueRequest:"
- "entitlementValueForKey:ofClass:"
- "error:hasCode:"
- "errorWithCode:"
- "errorWithCode:message:"
- "errorWithCode:message:suberror:"
- "errorWithDomain:code:userInfo:"
- "exportedInterface"
- "extension"
- "extensionAuthorizationRequestHandlerWithError:"
- "extensionBundleIdentifier"
- "extensionContext"
- "extensionData"
- "extensionDelegatesLock"
- "extensionRequestsMode"
- "extensionViewController"
- "extensionsWithMatchingAttributes:error:"
- "fileExistsAtPath:isDirectory:"
- "fileURLWithPath:"
- "findDelegateForIdentifier:"
- "findExtensionWithBundleIdentifier:completion:"
- "findExtensionsWithCompletion:"
- "findPlatformSSOProfile:"
- "findProfileForExtension:profiles:"
- "findRequestForIdentifier:"
- "finishAuthorization:completion:"
- "firstObject"
- "getAuthorizationHintsWithURL:responseCode:completion:"
- "groupsCompletion"
- "hasAnyMDMProfileForExtension:"
- "hasAssociatedDomainsApproved"
- "hasURLApprovedAssociatedDomain:cache:"
- "hash"
- "host"
- "hostContextWithError:"
- "httpAuthorizationHeaders"
- "httpBody"
- "httpHeaders"
- "httpResponse"
- "i16@0:8"
- "identifier"
- "impersonationBundleIdentifier"
- "increaseVersionWithMessage:"
- "incrementRequestCount"
- "infoDictionary"
- "init"
- "initWithAuthorizationCredential:"
- "initWithAuthorizationHintsCore:"
- "initWithAuthorizationParametersCore:"
- "initWithAuthorizationRequest:"
- "initWithAuthorizationRequestParametersCore:"
- "initWithAuthorizationResult:"
- "initWithCoder:"
- "initWithExtension:"
- "initWithExtensionViewController:hints:"
- "initWithHTTPAuthorizationHeaders:"
- "initWithHTTPResponse:httpBody:"
- "initWithIdentifier:"
- "initWithKey:"
- "initWithListenerEndpoint:"
- "initWithMode:"
- "initWithProfile:"
- "initWithProfileData:"
- "initWithProfiles:"
- "initWithRequestParameters:remoteExtensionContext:"
- "initWithService:requestParameters:completionBlock:"
- "initWithServiceType:applicationIdentifier:domain:"
- "instantiateInitialViewController"
- "instantiateViewControllerWithInputItems:listenerEndpoint:connectionHandler:"
- "intValue"
- "integerValue"
- "interfaceWithInternalProtocol:"
- "interfaceWithProtocol:"
- "internalErrorWithMessage:"
- "internalExtensionBundleIdentifier"
- "internalExtensionsBundleIdentifiers"
- "invalidate"
- "isAppleConnectExtensionBundleIdentifier:"
- "isApplicationAvailableToOpenURL:error:"
- "isApproved"
- "isAssociatedDomainValidated"
- "isAuthorizationCanceled"
- "isCFNetworkInterception"
- "isCallerManaged"
- "isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:"
- "isEqual:"
- "isEqualToExtension:"
- "isEqualToString:"
- "isExtensionProcessWithAuditToken:completion:"
- "isExtensionSignatureValidated"
- "isInternalBuild"
- "isInternalExtensionBundleIdentifier:"
- "isKindOfClass:"
- "isLoadedExtensionWithBundleIdentifier:"
- "isMemberOfClass:"
- "isPlatformSSOProfile:"
- "isProxy"
- "isRunning"
- "isTiburonExtensionBundleIdentifier:"
- "isUpdating"
- "isUserInteractionEnabled"
- "kerberosProfiles"
- "keyWillRotateForKeyType:keyProxyEndpoint:extensionData:completion:"
- "leadingAnchor"
- "length"
- "loadExtensionWithBundleIdentifier:"
- "loadExtensionWithBundleIdentifier:completion:"
- "loadExtensions"
- "loadInternalExtension"
- "loadView"
- "loadedExtensionWithBundleIdentifier:"
- "loadedExtensions"
- "loadedInternalExtension"
- "localizedCallerDisplayName"
- "localizedExtensionDisplayName"
- "loginManager"
- "lowercaseString"
- "mainBundle"
- "mapArray:usingBlock:"
- "maskRegistrationTokenInConfigurationData:"
- "maskRegistrationTokenInProfileList:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openSensitiveURL:withOptions:error:"
- "openURL:completionHandler:"
- "operation"
- "originatorBundleIdentifier"
- "parameterErrorWithMessage:"
- "path"
- "performBlockOnDelegateQueue:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pictureCompletion"
- "platformSSO"
- "platformSSOProfile"
- "pluginKitProxyForURL:"
- "port"
- "postNotificationName:object:userInfo:"
- "postNotificationName:object:userInfo:options:"
- "presentAuthorizationViewControllerWithCompletion:"
- "presentAuthorizationViewControllerWithHints:completion:"
- "presentAuthorizationViewControllerWithHints:requestIdentifier:completion:"
- "presentRegistrationViewControllerWithCompletion:"
- "privateKeys"
- "processItemBlock"
- "processNextRequest"
- "profileForURL:responseCode:"
- "profilePictureForUserUsingExtensionData:completion:"
- "profiles"
- "profilesWithExtensionBundleIdentifier:"
- "protocolVersionCompletion:"
- "pssoAuthenticationMethod"
- "pssoRegistrationToken"
- "q16@0:8"
- "q40@0:8@16q24@32"
- "queueCount"
- "rangeOfString:"
- "realm"
- "realms"
- "registrationCompletion"
- "registrationDidCancelWithCompletion:"
- "registrationDidCompleteWithCompletion:"
- "release"
- "remoteContextWithError:"
- "remoteObjectProxyWithErrorHandler:"
- "remoteViewControllerInterface"
- "removeAllRequestsWithBlock:"
- "removeDelegateForRequestIdentifier:"
- "removeExpiredEntriesFromCache:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeQueueWithIdentifier:"
- "removeRequestForIdentifier:"
- "removeRequestWithIdentifier:block:"
- "removeURLPrefix:"
- "removedProfileForExtensionBundleIdentifier:"
- "requestAuthorizationViewControllerWithCompletion:"
- "requestCount"
- "requestCountLock"
- "requestParameters"
- "requestParametersCore"
- "requestQueueWithIdentifier:"
- "requestReauthenticationWithCompletion:"
- "requestReauthenticationWithRequestIdentifier:completion:"
- "requestedOperation"
- "requireAuthGracePeriod"
- "respondsToSelector:"
- "responseCode"
- "resume"
- "retain"
- "retainCount"
- "rotationCompletion"
- "saveConfiguration:error:"
- "saveConfigurationData:completion:"
- "saveConfigurationData:error:"
- "saveDelegate:forRequestIdentifier:"
- "saveRequest:forIdentifier:"
- "scheme"
- "secKeyProxies"
- "secKeyProxiesConnectedClients"
- "secKeyProxyEndpoints"
- "self"
- "service"
- "serviceDetailsWithServiceSpecifier:error:"
- "serviceSpecifier"
- "serviceViewControllerInterface"
- "serviceViewControllerProxyWithErrorHandler:"
- "serviceXpcEndpoint"
- "sessionID"
- "sessionIDLock"
- "setAppSSOUnavailable"
- "setAssociatedDomainCache:"
- "setAssociatedDomainLock:"
- "setAssociatedDomains:"
- "setAttributes:ofItemAtPath:error:"
- "setAuditTokenData:"
- "setAuthorizationCanceled:"
- "setAuthorizationOptions:"
- "setCFNetworkInterception:"
- "setCallerBundleIdentifier:"
- "setCallerManaged:"
- "setCallerTeamIdentifier:"
- "setCancelLock:"
- "setCanceledAuthorizationCredential:"
- "setCanceledAuthorizationError:"
- "setCancelled:"
- "setCfNetworkInterception:"
- "setClientConnectionHandler:"
- "setClientDisconnectionHandler:"
- "setConfigurationPending:"
- "setConfigurationPendingLock:"
- "setContextExtension:"
- "setDelegate:"
- "setDelegateDispatchQueue:"
- "setEnableEmbeddedAuthorizationViewController:"
- "setEnableUserInteraction:"
- "setExtension:"
- "setExtensionContext:"
- "setExtensionData:"
- "setExtensionDelegatesLock:"
- "setGroupsCompletion:"
- "setHostExtensionContext:"
- "setHttpAuthorizationHeaders:"
- "setHttpBody:"
- "setHttpHeaders:"
- "setHttpResponse:"
- "setIdentifier:"
- "setImpersonationBundleIdentifier:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsRunning:"
- "setLocalizedCallerDisplayName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOperation:"
- "setOriginatorBundleIdentifier:"
- "setPictureCompletion:"
- "setPrivateKeys:"
- "setProcessItemBlock:"
- "setPssoAuthenticationMethod:"
- "setPssoRegistrationToken:"
- "setRealm:"
- "setRegistrationCompletion:"
- "setRemoteObjectInterface:"
- "setRequestCountLock:"
- "setRequestIdentifier:"
- "setRequestInterruptionBlock:"
- "setRequestParametersCore:"
- "setRequestedOperation:"
- "setResponseCode:"
- "setRotationCompletion:"
- "setSecKeyProxies:"
- "setSecKeyProxiesConnectedClients:"
- "setSecKeyProxyEndpoints:"
- "setServiceXpcEndpoint:"
- "setSessionIDLock:"
- "setShowOnCoverScreen:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUrl:"
- "setUseInternalExtensions:"
- "setView:"
- "setViewService:"
- "setWithObjects:"
- "setXpcConnection:"
- "setupNonUISessionWithCompletion:"
- "sharedApplication"
- "sharedInstance"
- "showOnCoverScreen"
- "silentInternalErrorWithMessage:"
- "sleepForTimeInterval:"
- "storyboardWithName:bundle:"
- "stringByAppendingFormat:"
- "stringByDeletingLastPathComponent"
- "stringWithFormat:"
- "stringWithHandleResult:"
- "stringWithProfileType:"
- "strongToStrongObjectsMapTable"
- "strongToWeakObjectsMapTable"
- "superclass"
- "supportedDeviceEncryptionAlgorithmsCompletion:"
- "supportedDeviceSigningAlgorithmsCompletion:"
- "supportedGrantTypesCompletion:"
- "supportedUserSecureEnclaveKeySigningAlgorithmsCompletion:"
- "supportsSecureCoding"
- "synchronousHostContextWithError:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemMDMProfileForExtension:"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "topAnchor"
- "trailingAnchor"
- "unload"
- "unloadExtensions"
- "url"
- "useInternalExtensions"
- "useSharedDeviceKeys"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"SOUIAuthorizationViewController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"SOAuthorizationRequestParameters\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q>16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8q16"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"SOAuthorizationCredential\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q>24"
- "v32@0:8@\"NSURL\"16@?<v@?B>24"
- "v32@0:8@\"NSUUID\"16@?<v@?>24"
- "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"SOAuthorizationRequestParameters\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"SOAuthorizationCredential\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8q16@\"NSDictionary\"24@?<v@?q>32"
- "v40@0:8q16@24@?32"
- "v48@0:8@16@24@32@40"
- "v48@0:8q16@\"NSXPCListenerEndpoint\"24@\"NSDictionary\"32@?<v@?q>40"
- "v48@0:8q16@24@32@?40"
- "v52@0:8@\"NSString\"16i24q28@\"NSDictionary\"36@?<v@?q>44"
- "v52@0:8@16i24q28@36@?44"
- "v52@0:8@16q24@32B40@?44"
- "v56@0:8{?=[8I]}16@?48"
- "validatedProfileForPlatformSSO"
- "version"
- "view"
- "viewControllerDidCancel:"
- "viewService"
- "viewServiceDidTerminateWithError:"
- "waitForSiteApprovalWithCompletionHandler:"
- "willHandleURL:responseCode:callerBundleIdentifier:"
- "willHandleURL:responseCode:callerBundleIdentifier:profile:"
- "writeToURL:error:"
- "writeToURL:options:error:"
- "xpcConnection"
- "zone"
- "{?=[8I]}16@0:8"

```
