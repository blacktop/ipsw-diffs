## AssetCacheServicesExtensions

> `/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/Versions/A/AssetCacheServicesExtensions`

```diff

-157.0.0.0.0
-  __TEXT.__text: 0xfe54
-  __TEXT.__objc_methlist: 0x10a4
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x141a
+157.40.2.0.0
+  __TEXT.__text: 0x13b70
+  __TEXT.__objc_methlist: 0x1314
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x1919
   __TEXT.__ustring: 0x20
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__oslogstring: 0x284
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__oslogstring: 0x6f1
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0xdb0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__got: 0x220
-  __AUTH_CONST.__const: 0x3f0
-  __AUTH_CONST.__cfstring: 0x2260
-  __AUTH_CONST.__objc_const: 0x1f08
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x124
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__got: 0x268
+  __AUTH_CONST.__const: 0x410
+  __AUTH_CONST.__cfstring: 0x2700
+  __AUTH_CONST.__objc_const: 0x2270
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/AssetCacheServices.framework/Versions/A/AssetCacheServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 439
-  Symbols:   1274
-  CStrings:  313
+  Functions: 511
+  Symbols:   1466
+  CStrings:  376
 
Symbols:
+ +[ACSDataPathValidator _canonicalPath:matchesWildcardRoot:]
+ +[ACSDataPathValidator _canonicalizePath:]
+ +[ACSDataPathValidator _canonicalizeRoot:]
+ +[ACSDataPathValidator _errorWithCode:description:path:component:]
+ +[ACSDataPathValidator _path:isSameFileAs:]
+ +[ACSDataPathValidator _path:matchesWildcardPattern:]
+ +[ACSDataPathValidator _validateAndResolvePath:allowedRoots:resolvedPath:matchedRoot:error:]
+ +[ACSDataPathValidator secureCreateDirectoryAtPath:allowedRoots:owner:group:leafMode:parentMode:error:]
+ +[ACSDataPathValidator validateAndResolvePath:allowedRoots:resolvedPath:error:]
+ +[ACSDataPathValidator validateSyntaxOfPath:error:]
+ +[AssetCacheConfiguration initialize]
+ +[AssetCacheConfiguration sharedConfiguration]
+ -[AssetCacheConfiguration .cxx_destruct]
+ -[AssetCacheConfiguration _applyAttributes:toItemAtPath:error:]
+ -[AssetCacheConfiguration _containerUnavailableError]
+ -[AssetCacheConfiguration _createContainerWithError:]
+ -[AssetCacheConfiguration _legacySettingsAreTrustworthy]
+ -[AssetCacheConfiguration _settings]
+ -[AssetCacheConfiguration _writeErrorForPath:posixError:]
+ -[AssetCacheConfiguration _writeSettings:error:]
+ -[AssetCacheConfiguration containerCreationDenied]
+ -[AssetCacheConfiguration containerPath]
+ -[AssetCacheConfiguration containerUnavailablePermanently]
+ -[AssetCacheConfiguration ddmConfigurationPath]
+ -[AssetCacheConfiguration ddmManagedKeys]
+ -[AssetCacheConfiguration defaultSettings]
+ -[AssetCacheConfiguration explicitContainerPath]
+ -[AssetCacheConfiguration exportSettingsToLegacyLocationWithError:]
+ -[AssetCacheConfiguration initWithContainerPath:legacySettingsPath:]
+ -[AssetCacheConfiguration isManagedKey:]
+ -[AssetCacheConfiguration legacySettingsPath]
+ -[AssetCacheConfiguration logHandle]
+ -[AssetCacheConfiguration managedByDDM]
+ -[AssetCacheConfiguration managedByMDM]
+ -[AssetCacheConfiguration managedValueForKey:]
+ -[AssetCacheConfiguration mdmManageableKeys]
+ -[AssetCacheConfiguration resolvedContainerPath]
+ -[AssetCacheConfiguration restrictedKeys]
+ -[AssetCacheConfiguration saveDDMConfiguration:error:]
+ -[AssetCacheConfiguration savedDDMConfiguration]
+ -[AssetCacheConfiguration setContainerCreationDenied:]
+ -[AssetCacheConfiguration setContainerUnavailablePermanently:]
+ -[AssetCacheConfiguration setExplicitContainerPath:]
+ -[AssetCacheConfiguration setLogHandle:]
+ -[AssetCacheConfiguration setResolvedContainerPath:]
+ -[AssetCacheConfiguration settingsPath]
+ -[AssetCacheConfiguration settings]
+ -[AssetCacheConfiguration updateSettingsWithBlock:error:]
+ -[AssetCacheServicesManager absorbCacheFrom:readOnly:]
+ GCC_except_table10
+ GCC_except_table2
+ GCC_except_table81
+ OBJC_IVAR_$_AssetCacheConfiguration._containerCreationDenied
+ OBJC_IVAR_$_AssetCacheConfiguration._containerUnavailablePermanently
+ OBJC_IVAR_$_AssetCacheConfiguration._explicitContainerPath
+ OBJC_IVAR_$_AssetCacheConfiguration._legacySettingsPath
+ OBJC_IVAR_$_AssetCacheConfiguration._logHandle
+ OBJC_IVAR_$_AssetCacheConfiguration._resolvedContainerPath
+ _ACSConfigurationQueryContainerPath
+ _ACSCopyPathBytes
+ _ACSDataPathValidatorErrorDomain
+ _CFPreferencesAppValueIsForced
+ _CFPreferencesCopyAppValue
+ _NSFileGroupOwnerAccountName
+ _NSFileOwnerAccountName
+ _NSFilePathErrorKey
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_ACSDataPathValidator
+ _OBJC_CLASS_$_AssetCacheConfiguration
+ _OBJC_CLASS_$_AssetCacheSettingsMissingAlert
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSSet
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_ACSDataPathValidator
+ _OBJC_METACLASS_$_AssetCacheConfiguration
+ _OBJC_METACLASS_$_AssetCacheSettingsMissingAlert
+ _OUTLINED_FUNCTION_3
+ __ACSConfigurationContainerDirectoryExists
+ __ACSConfigurationCopyContainerOwnerIDs
+ __ACSConfigurationQueryContainerPath
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_ACSDataPathValidator
+ __OBJC_$_CLASS_METHODS_AssetCacheConfiguration
+ __OBJC_$_INSTANCE_METHODS_AssetCacheConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AssetCacheConfiguration
+ __OBJC_$_PROP_LIST_AssetCacheConfiguration
+ __OBJC_CLASS_RO_$_ACSDataPathValidator
+ __OBJC_CLASS_RO_$_AssetCacheConfiguration
+ __OBJC_CLASS_RO_$_AssetCacheSettingsMissingAlert
+ __OBJC_METACLASS_RO_$_ACSDataPathValidator
+ __OBJC_METACLASS_RO_$_AssetCacheConfiguration
+ __OBJC_METACLASS_RO_$_AssetCacheSettingsMissingAlert
+ ___46+[AssetCacheConfiguration sharedConfiguration]_block_invoke
+ ___54-[AssetCacheServicesManager absorbCacheFrom:readOnly:]_block_invoke
+ ___54-[AssetCacheServicesManager absorbCacheFrom:readOnly:]_block_invoke_2
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ ___chkstk_darwin
+ ___error
+ __kACSConfigurationDDMFileName
+ __kACSConfigurationLegacySettingsPath
+ __kACSConfigurationSettingsFileName
+ _close
+ _container_copy_sandbox_token
+ _container_error_copy_unlocalized_description
+ _container_error_get_type
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_ownership
+ _fchmod
+ _fchown
+ _free
+ _geteuid
+ _getpwnam_r
+ _kacsConfigurationDDMManagedKeys
+ _kacsConfigurationDefaultSettings
+ _kacsConfigurationFileAttributes
+ _kacsConfigurationMDMManageableKeys
+ _lstat
+ _mkdirat
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_applyAttributes:toItemAtPath:error:
+ _objc_msgSend$_canonicalPath:matchesWildcardRoot:
+ _objc_msgSend$_canonicalizePath:
+ _objc_msgSend$_canonicalizeRoot:
+ _objc_msgSend$_containerUnavailableError
+ _objc_msgSend$_createContainerWithError:
+ _objc_msgSend$_errorWithCode:description:path:component:
+ _objc_msgSend$_legacySettingsAreTrustworthy
+ _objc_msgSend$_path:isSameFileAs:
+ _objc_msgSend$_path:matchesWildcardPattern:
+ _objc_msgSend$_settings
+ _objc_msgSend$_validateAndResolvePath:allowedRoots:resolvedPath:matchedRoot:error:
+ _objc_msgSend$_writeErrorForPath:posixError:
+ _objc_msgSend$_writeSettings:error:
+ _objc_msgSend$absorbCacheFrom:readOnly:withCallback:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$containerCreationDenied
+ _objc_msgSend$containerPath
+ _objc_msgSend$containerUnavailablePermanently
+ _objc_msgSend$copy
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$ddmConfigurationPath
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$explicitContainerPath
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$getFileSystemRepresentation:maxLength:
+ _objc_msgSend$initWithContainerPath:legacySettingsPath:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isManagedKey:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$legacySettingsPath
+ _objc_msgSend$managedByDDM
+ _objc_msgSend$manager:didStartAbsorbingCache:withError:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$resolvedContainerPath
+ _objc_msgSend$savedDDMConfiguration
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setContainerCreationDenied:
+ _objc_msgSend$setContainerUnavailablePermanently:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setResolvedContainerPath:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$settingsPath
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringWithFileSystemRepresentation:length:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$validateSyntaxOfPath:error:
+ _objc_msgSend$writeToFile:atomically:
+ _open
+ _openat
+ _realpath$DARWIN_EXTSN
+ _sandbox_extension_consume
+ _singleton
+ _singletonOnce
+ _stat
+ _strerror
+ _strlen
+ _unlinkat
+ _xpc_string_create
- GCC_except_table75
CStrings:
+ "%s DDM configuration"
+ "*"
+ ".."
+ "/"
+ "/*"
+ "/Library/Preferences/com.apple.AssetCache.plist"
+ "ACSDataPathValidatorComponent"
+ "ACSDataPathValidatorErrorDomain"
+ "Adopting the settings at %@ into the container"
+ "AssetCacheSettingsMissingAlert"
+ "Configuration"
+ "DataPath \"%@\" cannot be created: component \"%@\" of the allowed root \"%@\" is a symlink, or could not be checked"
+ "DataPath \"%@\" resolves to \"%@\", which is not in the allowed-roots list"
+ "DataPath contains a \".\" component"
+ "DataPath contains a \"..\" component"
+ "DataPath contains a NUL or control byte"
+ "DataPath contains an empty path component (e.g. \"//\")"
+ "DataPath could not be encoded as a filesystem path"
+ "DataPath is empty"
+ "DataPath is missing or is not a string"
+ "DataPath must be an absolute POSIX path"
+ "DataPath must have at least one intermediate component beneath /"
+ "DataPath must not end with a slash"
+ "No allowed roots were supplied to the DataPath validator"
+ "No sandbox extension was issued for the settings container; access to it will fail"
+ "No settings in the container or at %@; starting from the defaults"
+ "Not privileged to set the attributes of %@: %@"
+ "Not retrying the settings container lookup; this process cannot reach %{public}@"
+ "Not the owner of %{public}@, so it is not ours to create; waiting for it to appear"
+ "Path component could not be encoded as a filesystem name"
+ "Refusing to adopt %@ into the settings container: uid %u, mode 0%o"
+ "Removed the saved"
+ "ReservedVolumeSpace"
+ "Saved the"
+ "The settings container at %{public}@ is gone"
+ "The settings container moved from %{public}@ to %{public}@"
+ "The settings container resolved to %{public}@, which is not there either"
+ "The settings container still resolves to %{public}@, which is not there; treating it as unavailable"
+ "There is no %s account, so the settings container cannot be resolved"
+ "Unable to %{public}s the settings container %{public}@: %{public}s"
+ "Unable to consume the sandbox extension for the settings container"
+ "Unable to export settings to %@: %@"
+ "Unable to save the DDM configuration: %@"
+ "Unable to seed the settings container: %@"
+ "Unable to set the attributes of %@: %@"
+ "_assetcache"
+ "com.apple.AssetCache.DDM.plist"
+ "com.apple.AssetCache.plist"
+ "create"
+ "failed to update %@"
+ "fchmod(\"%@\") failed: %s"
+ "fchmod(%@) failed: %s"
+ "fchown(%@) failed: %s"
+ "leaf"
+ "look up"
+ "mkdirat(\"%@\") failed: %s"
+ "no description"
+ "open(\"/\") failed: %s"
+ "openat(\"%@\", O_NOFOLLOW) failed: %s"
+ "parent"
+ "q"
+ "realpath(3) failed for \"%@\": %s"
+ "the %@ settings container is unavailable"
```
