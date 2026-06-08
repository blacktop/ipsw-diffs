## RemoteManagementUI

> `/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x76a8
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0xb60
+621.0.0.502.1
+  __TEXT.__text: 0x781c
+  __TEXT.__objc_methlist: 0xb80
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0x6c3
-  __TEXT.__oslogstring: 0x500
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__objc_classname: 0x205
-  __TEXT.__objc_methname: 0x1dbb
-  __TEXT.__objc_methtype: 0x288
-  __TEXT.__objc_stubs: 0x1620
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x2c8
+  __TEXT.__cstring: 0x7f6
+  __TEXT.__oslogstring: 0x67e
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x1820
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x1850
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0xc0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F676BA9-F32D-3737-BF94-62A7D95ECBD0
-  Functions: 281
-  Symbols:   1081
-  CStrings:  529
+  UUID: 88F51D11-15F5-35CB-9160-E7CC41629D08
+  Functions: 290
+  Symbols:   1129
+  CStrings:  185
 
Symbols:
+ +[RMUIError legacyProfilesInvalidDeclarationForDeclarationID:description:]
+ -[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:].cold.3
+ -[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:].cold.4
+ -[RMUIKeyValueViewModel descriptor]
+ -[RMUIKeyValueViewModel setDescriptor:]
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_RMAssetResolverController
+ _OBJC_CLASS_$_RMModelAssetBase
+ _OBJC_IVAR_$_RMUIKeyValueViewModel._descriptor
+ ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.95
+ ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.95.cold.1
+ ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.95.cold.2
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.67
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.67.cold.1
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.69
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.69.cold.1
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.69.cold.2
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.71
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.71.cold.1
+ ___85-[RMUIConfigurationInterface _activateConfiguration:observerStore:completionHandler:]_block_invoke.71.cold.2
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e20_v20?0B8"NSError"12ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e44_v24?0"RMModelDeclarationBase"8"NSError"16ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$declarationKeyForStore:declaration:assets:
+ _objc_msgSend$declarationWithIdentifier:completionHandler:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$descriptor
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$installProfileAtPath:store:declarationKey:completionHandler:
+ _objc_msgSend$legacyProfilesInvalidDeclarationForDeclarationID:description:
+ _objc_msgSend$path
+ _objc_msgSend$payloadProfileAssetReference
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:
+ _objc_msgSend$setDescriptor:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_9
- ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.87
- ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.87.cold.1
- ___82-[RMUIPluginViewModelProvider loadPluginsFromConfigurationsWithCompletionHandler:]_block_invoke.87.cold.2
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@.mobileconfig"
+ "Both profile URL and asset reference specified"
+ "Both profile URL and asset reference specified for declaration %{public}@"
+ "Download asset URL: %{public}@"
+ "Error downloading asset for declaration %{public}@: %{public}@"
+ "Error fetching asset %{public}@: %{public}@"
+ "Error installing profile from asset for declaration %{public}@: %{public}@"
+ "Error no asset %{public}@"
+ "Installed profile from asset for declaration %{public}@"
+ "Invalid declaration for declaration %@: %@"
+ "Missing both profile URL and asset reference"
+ "Missing both profile URL and asset reference for declaration %{public}@"
+ "RMUI_SECTION_NETWORK"
+ "com.apple.configuration.network."
+ "com.apple.configuration.package"
+ "description"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"RMModelDeclarationBase\"8@\"NSError\"16"
- ""
- ".cxx_destruct"
- "@\"ACAccount\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"RMModelDeclarationBase\""
- "@\"RMObserverStore\""
- "@\"RMUIInteractiveProfileFooterViewModel\""
- "@\"RMUIInteractiveProfileToggleViewModel\""
- "@\"RMUILegacyProfilesViewModelProvider\""
- "@\"RMUIPluginViewModelProvider\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@36@0:8@16q24B32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32B40B44"
- "@56@0:8@16@24@32@40@48"
- "B"
- "B16@0:8"
- "Missing profile URL for declaration %{public}@: %{public}@"
- "NSCoding"
- "NSSecureCoding"
- "RMUIConfigurationInterface"
- "RMUIConfigurationViewModels"
- "RMUIDeclarationInfo"
- "RMUIError"
- "RMUIInteractiveProfileErrorViewModel"
- "RMUIInteractiveProfileFooterViewModel"
- "RMUIInteractiveProfileToggleViewModel"
- "RMUIKeyValueDetailViewModel"
- "RMUIKeyValueViewModel"
- "RMUILegacyProfilesViewModelProvider"
- "RMUILocalizable"
- "RMUILog"
- "RMUIPluginSectionViewModel"
- "RMUIPluginViewModel"
- "RMUIPluginViewModelProvider"
- "RMUIProfileViewModel"
- "T@\"ACAccount\",R,N,V_rmAccount"
- "T@\"NSArray\",&,N,V_details"
- "T@\"NSArray\",&,N,V_privPluginSectionViewModels"
- "T@\"NSArray\",&,N,V_privPluginViewModels"
- "T@\"NSArray\",&,N,V_privProfileViewModels"
- "T@\"NSArray\",&,V_detailViewModels"
- "T@\"NSArray\",&,V_viewModels"
- "T@\"NSArray\",R,C,N,V_declarationsPayloadIdentifiers"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_pluginSectionViewModels"
- "T@\"NSArray\",R,N,V_pluginViewModels"
- "T@\"NSArray\",R,N,V_profileViewModels"
- "T@\"NSDictionary\",&,N,V_hiddenDetails"
- "T@\"NSDictionary\",&,V_hiddenDetails"
- "T@\"NSError\",&,V_error"
- "T@\"NSMutableArray\",&,N,V_pluginSectionViewModels"
- "T@\"NSMutableArray\",&,N,V_pluginViewModels"
- "T@\"NSMutableArray\",&,N,V_profileViewModels"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSSet\",&,N,V_filterDeclarationIdentifiers"
- "T@\"NSSet\",R,C,N,V_filterDeclarationIdentifiers"
- "T@\"NSString\",&,N,V_declarationIdentifier"
- "T@\"NSString\",&,N,V_declarationServerToken"
- "T@\"NSString\",&,N,V_declarationType"
- "T@\"NSString\",&,N,V_descriptor"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_profileIdentifier"
- "T@\"NSString\",&,V_declarationIdentifier"
- "T@\"NSString\",&,V_declarationServerToken"
- "T@\"NSString\",&,V_declarationType"
- "T@\"NSString\",&,V_heading"
- "T@\"NSString\",&,V_interactiveDetailsText"
- "T@\"NSString\",&,V_message"
- "T@\"NSString\",&,V_okText"
- "T@\"NSString\",&,V_profileIdentifier"
- "T@\"NSString\",&,V_title"
- "T@\"NSString\",&,V_value"
- "T@\"NSString\",R,C,N,V_mdmProfileIdentifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_passcodeDeclarationsHeading"
- "T@\"NSString\",R,V_viewID"
- "T@\"RMModelDeclarationBase\",&,N,V_declaration"
- "T@\"RMModelDeclarationBase\",&,V_declaration"
- "T@\"RMObserverStore\",&,N,V_observerStore"
- "T@\"RMObserverStore\",&,V_observerStore"
- "T@\"RMUIInteractiveProfileFooterViewModel\",&,V_footerViewModel"
- "T@\"RMUIInteractiveProfileToggleViewModel\",&,V_toggleViewModel"
- "T@\"RMUILegacyProfilesViewModelProvider\",&,N,V_legacyProfilesProvider"
- "T@\"RMUIPluginViewModelProvider\",&,N,V_pluginProvider"
- "TB,N,V_isActive"
- "TB,N,V_isRequired"
- "TB,R"
- "TB,V_isInteractiveProfile"
- "TB,V_toggleState"
- "Tq,R,N,V_scope"
- "Ts,V_symbol"
- "URL"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "_activateConfiguration:observerStore:completionHandler:"
- "_addModel:toSection:"
- "_bundle"
- "_deactivateConfiguration:observerStore:completionHandler:"
- "_declaration"
- "_declarationIdentifier"
- "_declarationServerToken"
- "_declarationType"
- "_declarationsPayloadIdentifiers"
- "_descriptor"
- "_detailViewModels"
- "_details"
- "_error"
- "_filterDeclarationIdentifiers"
- "_footerViewModel"
- "_heading"
- "_hiddenDetails"
- "_interactiveDetailsText"
- "_isActive"
- "_isInteractiveProfile"
- "_isRequired"
- "_label"
- "_legacyProfilesProvider"
- "_loadObserverStoreForDDMWithCompletion:"
- "_loadObserverStoreForDeclarationsPayloadWithCompletion:"
- "_loadObserverStoreWithCompletion:"
- "_mdmProfileIdentifier"
- "_message"
- "_modelForDeclarationInfo:"
- "_observerStore"
- "_okText"
- "_passcodeDeclarationsHeading"
- "_pluginProvider"
- "_pluginSectionViewModels"
- "_pluginViewModels"
- "_privPluginSectionViewModels"
- "_privPluginViewModels"
- "_privProfileViewModels"
- "_profileIdentifier"
- "_profileViewModels"
- "_reloadUIWithCompletion:"
- "_reloadViewModelsWithCompletion:"
- "_rmAccount"
- "_rmManagementScope"
- "_rmStoreScope"
- "_scope"
- "_sectionNameForDeclarationType:"
- "_symbol"
- "_symbolForDeclarationType:"
- "_title"
- "_toggleState"
- "_toggleViewModel"
- "_updateViewModelsWithDeclarations:"
- "_value"
- "_viewID"
- "_viewModels"
- "accountDeclarationsHeading"
- "addObject:"
- "addObserver:selector:name:object:"
- "allKeys"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "boolValue"
- "bundleForClass:"
- "caseInsensitiveCompare:"
- "clearModel"
- "com.apple.configuration.app.managed"
- "complete"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "declarationDetails"
- "declarationIdentifiersForProfilePayloadIdentifiers:completionHandler:"
- "declarationsPayloadIdentifiers"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "descriptionUI"
- "details"
- "detailsUI"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeValueForKey:"
- "displayPropertiesForConfigurationsWithCompletionHandler:"
- "displayableProfileConfigurationsWithCompletionHandler:"
- "dmc_managementProfileIdentifier"
- "downloadAndInstallProfileDeclaration:store:fromURL:completionHandler:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enrollmentURL"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "filterDeclarationIdentifiers"
- "filteredArrayUsingPredicate:"
- "hasPrefix:"
- "identifier"
- "init"
- "initForTest:"
- "initWithAccount:scope:"
- "initWithAccount:scope:initialLoad:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithDeclaration:label:descriptor:"
- "initWithDeclarationIdentifier:declarationServerToken:declarationType:label:descriptor:"
- "initWithDeclarationsPayloadIdentifier:scope:"
- "initWithDeclarationsPayloadIdentifier:scope:initialLoad:"
- "initWithDeclarationsPayloadIdentifiers:scope:initialLoad:"
- "initWithError:isActivating:"
- "initWithHeading:viewModels:"
- "initWithMDMProfileIdentifier:scope:"
- "initWithMDMProfileIdentifier:scope:initialLoad:"
- "initWithProfileDeclaration:label:profileIdentifier:isRequired:isActive:"
- "initWithProfileViewModels:pluginSectionViewModels:pluginViewModels:"
- "initWithScope:"
- "initWithStore:"
- "initWithTitle:value:"
- "installedProfileIdentifiers"
- "intValue"
- "integerValue"
- "isActive"
- "isActiveForScope:"
- "isEqual:"
- "isRequired"
- "label"
- "legacyProfilesInvalidURLForDeclarationID:urlString:"
- "legacyProfilesNoDeclarationToSetActivated:"
- "legacyProfilesNoObserverStoreForDeclarationID:"
- "legacyProfilesProvider"
- "loadPluginsFromConfigurationsWithCompletionHandler:"
- "loadProfilesFromConfigurationsWithCompletionHandler:"
- "localizedCaseInsensitiveCompare:"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "mdmProfileIdentifier"
- "newPluginSectionViewModelWithHeading:viewModels:"
- "newProfileControllerWithPrefix:scope:"
- "numberWithBool:"
- "numberWithShort:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "observerStore"
- "observerStoreWithCompletionHandler:"
- "passcodeDeclarationsHeading"
- "payloadProfileURL"
- "payloadVisibleName"
- "pluginDeclarationsHeading"
- "pluginProvider"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:options:"
- "predicateWithBlock:"
- "privPluginSectionViewModels"
- "privPluginViewModels"
- "privProfileViewModels"
- "profileDeclarationsHeading"
- "profileIdentifierForDeclaration:store:"
- "profileNameForProfileIdentifier:"
- "profileStoreForOwner:scope:"
- "q"
- "q16@0:8"
- "refreshWithCompletion:"
- "reloadNotificationPosted:"
- "removeAllObjects"
- "rmAccount"
- "s16@0:8"
- "s24@0:8@16"
- "scope"
- "scopeHeading"
- "setConfigurationActivated:forViewModel:completionHandler:"
- "setDeclaration:"
- "setDeclarationIdentifier:"
- "setDeclarationServerToken:"
- "setDeclarationType:"
- "setDescriptor:"
- "setDetailViewModels:"
- "setDetails:"
- "setError:"
- "setFilterDeclarationIdentifiers:"
- "setFooterViewModel:"
- "setHeading:"
- "setHiddenDetails:"
- "setInteractiveDetailsText:"
- "setInteractiveProfileActive:profileIdentifier:"
- "setIsActive:"
- "setIsInteractiveProfile:"
- "setIsRequired:"
- "setLabel:"
- "setLegacyProfilesProvider:"
- "setMessage:"
- "setObject:forKeyedSubscript:"
- "setObserverStore:"
- "setOkText:"
- "setPath:"
- "setPluginProvider:"
- "setPluginSectionViewModels:"
- "setPluginViewModels:"
- "setPrivPluginSectionViewModels:"
- "setPrivPluginViewModels:"
- "setPrivProfileViewModels:"
- "setProfileIdentifier:"
- "setProfileViewModels:"
- "setScheme:"
- "setSymbol:"
- "setTitle:"
- "setToggleState:"
- "setToggleViewModel:"
- "setValue:"
- "setViewModels:"
- "setWithObjects:"
- "sortDescriptorWithKey:ascending:"
- "sortDescriptorWithKey:ascending:selector:"
- "sortUsingDescriptors:"
- "sortedArrayUsingDescriptors:"
- "sortedArrayUsingSelector:"
- "storesWithScope:completionHandler:"
- "string:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "titleUI"
- "uninstallProfileWithIdentifier:store:completionHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8s16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8B16@20"
- "v32@0:8@16@24"
- "v36@0:8B16@20@?28"
- "v40@0:8@16@24@?32"
- "waitForCompletion"
- "willChangeValueForKey:"

```
