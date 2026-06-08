## PosterPlatformSupport

> `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport`

```diff

-304.5.4.102.0
-  __TEXT.__text: 0x2048
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x1c8
+341.0.3.0.0
+  __TEXT.__text: 0x1fbc
+  __TEXT.__objc_methlist: 0x1e0
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x1ff
+  __TEXT.__cstring: 0x202
   __TEXT.__oslogstring: 0x3fe
   __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x8b8
-  __TEXT.__objc_methtype: 0x198
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
+  __DATA_CONST.__objc_selrefs: 0x250
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x180
-  __AUTH_CONST.__const: 0x80
+  __DATA_CONST.__got: 0xb0
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x60
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B4C3328-B8B3-3F5E-98A2-EFFE2B1DC372
+  UUID: 087D9220-0BC3-32A7-BA69-C48D5151E8C0
   Functions: 66
-  Symbols:   312
-  CStrings:  155
+  Symbols:   325
+  CStrings:  47
 
Symbols:
+ +[PPSPlatformPolicyManager ambientPosterAutocreationSupportedForProvider:]
+ +[PPSPlatformPolicyManager defaultRoleForProactiveGallery]
+ +[PPSPlatformPolicyManager rolesRequiringProactiveGallery]
+ +[PPSPlatformPolicyManager rolesRequiringProactiveGallery].cold.1
+ _OBJC_CLASS_$_NSSet
+ _PFPosterRoleAmbient
+ ___58+[PPSPlatformPolicyManager rolesRequiringProactiveGallery]_block_invoke
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$boolValue
+ _objc_msgSend$setWithObjects:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _rolesRequiringProactiveGallery.onceToken
+ _rolesRequiringProactiveGallery.rolesRequiringProactiveGallery
- +[PPSPlatformPolicyManager ambientPosterAutocreationSupported]
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
Functions:
~ +[PPSHostConfigurationManager sharedHostConfigurationManager] : 176 -> 160
~ ___61+[PPSHostConfigurationManager sharedHostConfigurationManager]_block_invoke : 120 -> 116
~ -[PPSHostConfigurationManager initWithUserDefaults:] : 112 -> 120
~ -[PPSHostConfigurationManager setHostConfiguration:forRole:] : 108 -> 112
~ -[PPSHostConfigurationManager _lock_setHostConfiguration:forRole:] : 240 -> 232
~ -[PPSHostConfigurationManager hostConfigurationForRole:] : 432 -> 372
~ -[PPSHostConfigurationManager _lock_hostConfigurationForRole:outCacheHit:] : 580 -> 516
~ -[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:] : 592 -> 608
~ ___102-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]_block_invoke : 124 -> 120
~ -[PPSHostConfigurationManager _lock_deleteHostConfigurationForRole:] : 156 -> 148
~ -[PPSHostConfigurationManager updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:] : 568 -> 496
~ ___102-[PPSHostConfigurationManager updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:]_block_invoke : 152 -> 136
~ -[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:] : 592 -> 608
~ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke : 124 -> 120
~ -[PPSHostConfigurationManager _lock_bundleURLForRole:error:] : 276 -> 272
~ -[PPSHostConfigurationManager _lock_findBundleURLForRole:error:] : 1100 -> 1024
~ -[PPSHostConfigurationManager _lock_cachedHostConfigurationForRole:] : 316 -> 304
~ -[PPSHostConfigurationManager _connectionToBundleServiceForRole:outProxy:errorHandler:] : 184 -> 180
~ ___87-[PPSHostConfigurationManager _connectionToBundleServiceForRole:outProxy:errorHandler:]_block_invoke : 76 -> 72
~ -[PPSHostConfigurationManager setUserDefaults:] : 64 -> 12
~ _OUTLINED_FUNCTION_0 : 24 -> 32
~ _OUTLINED_FUNCTION_1 : 20 -> 24
~ _OUTLINED_FUNCTION_2 : 24 -> 32
~ _OUTLINED_FUNCTION_3 : 20 -> 12
~ _OUTLINED_FUNCTION_5 -> +[PPSPlatformPolicyManager platformSupportsDataMigrator] : 12 -> 8
~ _OUTLINED_FUNCTION_6 -> +[PPSPlatformPolicyManager snapshottingSupportedForRole:] : 12 -> 120
~ _OUTLINED_FUNCTION_7 -> +[PPSPlatformPolicyManager proactiveGallerySupportedForRole:] : 32 -> 120
~ _OUTLINED_FUNCTION_8 -> +[PPSPlatformPolicyManager ambientPosterAutocreationSupportedForProvider:] : 32 -> 28
~ +[PPSPlatformPolicyManager snapshottingSupportedForRole:] -> +[PPSPlatformPolicyManager defaultRoleForProactiveGallery] : 20 -> 52
~ +[PPSPlatformPolicyManager proactiveGallerySupportedForRole:] -> +[PPSPlatformPolicyManager rolesRequiringProactiveGallery] : 20 -> 68
~ +[PPSPlatformPolicyManager ambientPosterAutocreationSupported] -> ___58+[PPSPlatformPolicyManager rolesRequiringProactiveGallery]_block_invoke : 8 -> 116
~ -[PPSGalleryPrewarmPolicy setMaxTotalItemsToPrewarm:] -> _PPSLogCommon : 8 -> 68
~ _PPSLogCommon -> ___PPSLogCommon_block_invoke : 84 -> 68
~ _PPSLogHostConfiguration -> ___PPSLogHostConfiguration_block_invoke : 84 -> 68
~ ___PPSLogHostConfiguration_block_invoke -> -[PPSHostConfigurationManager _lock_setHostConfiguration:forRole:].cold.1 : 68 -> 52
~ -[PPSHostConfigurationManager _lock_hostConfigurationForRole:outCacheHit:].cold.1 -> -[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:].cold.1 : 84 -> 52
~ -[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:].cold.1 -> ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.cold.1 : 72 -> 64
~ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.cold.1 -> ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.16.cold.1 : 80 -> 132
~ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.16.cold.1 -> -[PPSHostConfigurationManager _lock_deleteHostConfigurationForRole:].cold.1 : 144 -> 72
~ -[PPSHostConfigurationManager _lock_deleteHostConfigurationForRole:].cold.1 -> -[PPSHostConfigurationManager _lock_findBundleURLForRole:error:].cold.1 : 84 -> 52
~ -[PPSHostConfigurationManager _lock_findBundleURLForRole:error:].cold.2 -> -[PPSHostConfigurationManager _lock_cachedHostConfigurationForRole:].cold.1 : 84 -> 52
~ -[PPSHostConfigurationManager _lock_cachedHostConfigurationForRole:].cold.1 -> -[PPSHostConfigurationManager _connectionToBundleServiceForRole:outProxy:errorHandler:].cold.1 : 72 -> 20
CStrings:
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@40@0:8@16@24^@32"
- "@40@0:8@16o^@24@?32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "PPSBundleServiceProtocol"
- "PPSGalleryPrewarmPolicy"
- "PPSHostConfigurationManager"
- "PPSPlatformPolicyManager"
- "Q"
- "Q16@0:8"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "TB,N,V_skipFirstSection"
- "TQ,N,V_maxPerSectionToPrewarm"
- "TQ,N,V_maxTotalItemsToPrewarm"
- "URLByAppendingPathComponent:"
- "URLsForDirectory:inDomains:"
- "_connectionToBundleServiceForRole:outProxy:errorHandler:"
- "_lock"
- "_lock_bundleURLByRoleIdentifier"
- "_lock_bundleURLForRole:error:"
- "_lock_cachedHostConfigurationForRole:"
- "_lock_deleteHostConfigurationForRole:"
- "_lock_findBundleURLForRole:error:"
- "_lock_hostConfigurationForRole:outCacheHit:"
- "_lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:"
- "_lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:"
- "_lock_rolesWithoutHostConfigurations"
- "_lock_setHostConfiguration:forRole:"
- "_maxPerSectionToPrewarm"
- "_maxTotalItemsToPrewarm"
- "_skipFirstSection"
- "_userDefaults"
- "addObject:"
- "ambientPosterAutocreationSupported"
- "ambientPosterDateCreatedOrderingSupported"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "bs_compactMap:"
- "bundleNameForRole:"
- "containsObject:"
- "count"
- "defaultManager"
- "defaultsKeyForRole:"
- "deleteHostConfigurationForRole:"
- "descriptorID"
- "dictionaryWithObjects:forKeys:count:"
- "entries"
- "entryWithExtensionID:descriptorID:"
- "errorWithDomain:code:userInfo:"
- "extensionID"
- "fileExistsAtPath:"
- "firstObject"
- "galleryPrewarmPolicy"
- "hostConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:"
- "hostConfigurationForRole:"
- "hostConfigurationWithConfigurationEntries:"
- "init"
- "initWithServiceName:"
- "initWithUserDefaults:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "localizedDescription"
- "maxPerSectionToPrewarm"
- "maxTotalItemsToPrewarm"
- "objectForKey:"
- "path"
- "platformSupportsDataMigrator"
- "proactiveGallerySupportedForRole:"
- "removeObject:"
- "removeObjectForKey:"
- "resume"
- "setHostConfiguration:forRole:"
- "setMaxPerSectionToPrewarm:"
- "setMaxTotalItemsToPrewarm:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "setSkipFirstSection:"
- "setUserDefaults:"
- "sharedHostConfigurationManager"
- "skipFirstSection"
- "snapshottingSupportedForRole:"
- "standardUserDefaults"
- "stringByAppendingString:"
- "stringWithFormat:"
- "switcherConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unarchivedObjectOfClass:fromData:error:"
- "updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:"
- "userDefaults"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v48@0:8@\"NSURL\"16@\"PRSHostConfiguration\"24@\"NSString\"32@?<v@?@\"PRSHostConfiguration\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
