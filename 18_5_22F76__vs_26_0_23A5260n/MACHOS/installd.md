## installd

> `/usr/libexec/installd`

```diff

-1378.100.35.0.0
-  __TEXT.__text: 0x57180
-  __TEXT.__auth_stubs: 0x11d0
+1513.0.8.0.2
+  __TEXT.__text: 0x566a4
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0x79c0
-  __TEXT.__objc_methlist: 0x2f94
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2d98
-  __TEXT.__objc_methname: 0xb0dd
-  __TEXT.__cstring: 0x14b1e
-  __TEXT.__objc_classname: 0x591
-  __TEXT.__objc_methtype: 0x1adb
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__oslogstring: 0x11ad
+  __TEXT.__objc_methlist: 0x2ef4
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x1477d
+  __TEXT.__objc_classname: 0x5b8
+  __TEXT.__objc_methname: 0xaf34
+  __TEXT.__objc_methtype: 0x1d5b
+  __TEXT.__gcc_except_tab: 0x2f34
+  __TEXT.__oslogstring: 0x11f3
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0xfb8
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0x328
+  __TEXT.__unwind_info: 0xf28
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xf88
-  __DATA_CONST.__cfstring: 0x9220
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__cfstring: 0x92c0
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x560
-  __DATA_CONST.__objc_dictobj: 0xd70
-  __DATA.__objc_const: 0x59b0
-  __DATA.__objc_selrefs: 0x2300
-  __DATA.__objc_ivar: 0x2a0
-  __DATA.__objc_data: 0xc80
-  __DATA.__data: 0x838
-  __DATA.__bss: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_intobj: 0x258
+  __DATA_CONST.__objc_arraydata: 0x5a0
+  __DATA_CONST.__objc_dictobj: 0xe10
+  __DATA.__objc_const: 0x5760
+  __DATA.__objc_selrefs: 0x22d0
+  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_data: 0xb90
+  __DATA.__data: 0xa18
+  __DATA.__bss: 0x188
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8FD2AF0-829F-3C0D-A78E-0C4321D37A60
-  Functions: 1221
-  Symbols:   400
-  CStrings:  4591
+  UUID: 67C6DAC3-228E-3815-96F6-F138E10383DB
+  Functions: 1167
+  Symbols:   369
+  CStrings:  4570
 
Symbols:
+ _CC_MD5_Final
+ _CC_MD5_Init
+ _CC_MD5_Update
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _OBJC_CLASS_$_MIHelperServiceFrameworkClient
+ _OBJC_CLASS_$_MILocationSystemDefinedBase
+ _OBJC_CLASS_$_MILocationSystemDefinedCommon
+ _OBJC_CLASS_$_MILocationUserDefined
+ _OBJC_CLASS_$_MILocationUserDefinedDirectory
+ _OBJC_CLASS_$_MIMCMContainer
+ _OBJC_CLASS_$_MIStagingLocation
+ _OBJC_CLASS_$_MIUserManagement
+ _OBJC_CLASS_$_NSMutableData
+ __os_log_error_impl
+ _fcntl
+ _getattrlist
+ _mkdtemp
+ _removefile
+ _strndup
- _MICreateSHA256Digest
- _NSFilePathErrorKey
- _OBJC_CLASS_$_MIPersonaAttributes
- _OBJC_CLASS_$_NSAssertionHandler
- __CFXPCCreateXPCObjectFromCFObject
- __sl_dlopen
- _container_copy_object
- _container_copy_unlocalized_description
- _container_delete_all_container_content
- _container_disk_usage
- _container_error_free
- _container_error_get_path
- _container_error_get_posix_errno
- _container_error_get_type
- _container_free_array_of_containers
- _container_free_object
- _container_get_class
- _container_get_error_description
- _container_get_identifier
- _container_get_info_value_for_key
- _container_get_path
- _container_get_persona_unique_string
- _container_is_equal
- _container_is_new
- _container_is_transient
- _container_operation_delete_array
- _container_operation_delete_reclaim_disk_space
- _container_query_create
- _container_query_create_from_container
- _container_query_free
- _container_query_get_last_error
- _container_query_get_single_result
- _container_query_iterate_results_sync
- _container_query_operation_set_flags
- _container_query_set_class
- _container_query_set_group_identifiers
- _container_query_set_identifiers
- _container_query_set_include_other_owners
- _container_query_set_persona_unique_string
- _container_query_set_transient
- _container_recreate_structure
- _container_regenerate_uuid
- _container_replace
- _container_serialize_copy_deserialized_reference
- _container_serialize_copy_serialized_reference
- _container_set_info_value
- _container_subdirectories_for_class
- _objc_getClass
- _objc_retain_x9
- _xpc_array_append_value
- _xpc_array_create
- _xpc_string_create
CStrings:
+ "%@.XXXXXX"
+ "+[MIPlaceholderSerializer serializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onBehalfOf:withError:]"
+ "-[MIClientConnection addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]"
+ "-[MIClientConnection createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]"
+ "-[MIClientConnection removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]"
+ "-[MIClientConnection setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]"
+ "-[MIHelperServiceClient moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:error:]_block_invoke"
+ "-[MIHelperServiceClient stageItemAtURL:toStagingLocation:options:containedSymlink:error:]_block_invoke"
+ "-[MIIPAPatcherFileManager createTempDirectoryWithPrefix:relativeToURL:mode:withError:]"
+ "-[MIIPAPatcherFileManager hashType:ofFileURL:chunkSize:withError:]"
+ "-[MIIPAPatcherFileManager moveSourceURL:toDestinationURL:fallBackToCopy:withError:]"
+ "-[MIIPAPatcherFileManager nodeTypeWithURL:withError:]"
+ "-[MIIPAPatcherFileManager realpathForURL:withError:]"
+ "-[MIIPAPatcherFileManager removeURL:withError:]"
+ "-[MIIPAPatcherFileManager syncEnumerateLinesFromFileURL:options:error:enumerator:]"
+ "-[MIIPAPatcherFileManager syncReadBytesFromFileURL:chunkSize:error:handler:]"
+ "-[MIInstallable _applyDeltaPatchWithError:]"
+ "-[MIInstallable _applyParallelPatchProcessingArchiveSection:withError:]"
+ "-[MIInstallable applyPatchWithError:]"
+ "-[MIInstallable initWithBundle:inStagingRoot:stagingLocation:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:operationType:error:]"
+ "-[MIInstallable performPreflightWithError:]"
+ "-[MIInstaller _bundleInDirectory:withBundleID:platformHint:error:]"
+ "-[MIInstaller _bundleInDirectory:withBundleID:platformHint:error:]_block_invoke"
+ "-[MIInstaller _existingBundleContainerForBundle:error:]"
+ "-[MIInstaller _patchUpdateInstallableForBundle:manifestPath:existingBundleContainer:patchType:error:]"
+ "0123456789ABCDEF"
+ "0123456789abcdef"
+ "@\"MIExecutableBundle\""
+ "@\"MIStagingLocation\""
+ "@\"NSData\"40@0:8@\"NSDictionary\"16Q24^@32"
+ "@\"NSString\"48@0:8Q16@\"NSURL\"24Q32^@40"
+ "@\"NSURL\"32@0:8@\"NSURL\"16^@24"
+ "@\"NSURL\"44@0:8@\"NSString\"16@\"NSURL\"24S32^@36"
+ "@104@0:8@16@24@32C40@44Q52@60@68@76C84Q88^@96"
+ "@36@0:8r*16Q24B32"
+ "@44@0:8@16@24I32^@36"
+ "@44@0:8@16@24S32^@36"
+ "@48@0:8Q16@24Q32^@40"
+ "@52@0:8@16@24@32C40^@44"
+ "@56@0:8@16@24@32^B40^@48"
+ "@84@0:8@16@24@32C40@44Q52@60Q68^@76"
+ "@92@0:8@16@24@32C40@44Q52@60@68Q76^@84"
+ "Attempted a patch update for %@ with an incompatible patch type"
+ "B32@?0Q8@\"NSData\"16^@24"
+ "B44@0:8@\"NSURL\"16@\"NSURL\"24B32^@36"
+ "B48@0:8@\"NSURL\"16Q24^@32@?<B@?Q@\"NSData\"^@>40"
+ "B48@0:8@\"NSURL\"16Q24^@32@?<B@?Q@\"NSString\"^@>40"
+ "B52@0:8@\"NSDictionary\"16Q24@\"NSURL\"32S40^@44"
+ "B52@0:8@16Q24@32S40^@44"
+ "B80@0:8@16@24@32{?=[8I]}40^@72"
+ "CFBundleIdentifier"
+ "CFBundleVersion"
+ "Could not allocate %lld bytes to read file [%@]"
+ "Could not chmod newly created temp directory at [%@]"
+ "Could not create temp directory at [%@]"
+ "Could not open file [%@] for reading."
+ "Could not read %lld bytes from file [%@]"
+ "Could not read file [%@]."
+ "Could not stat file [%@]"
+ "Could open file [%@] for reading"
+ "Deleted exisiting bundle container for %@ because it didn't contain a bundle"
+ "Failed to associate %@ with persona string in LS %@ : %@"
+ "Failed to find manifestURL when attempting a patch update for %@"
+ "Failed to get details about path [%@]"
+ "Failed to get staging root for system content: %@"
+ "Failed to lstat [%@]"
+ "Failed to move [%@] -> [%@]."
+ "Failed to re-fetch bundle during preflight"
+ "Failed to remove [%@]."
+ "Failed to rename [%@] -> [%@]."
+ "Failed to resolve staging location %@: %@"
+ "File [%@] was empty."
+ "File too large (%lld) to read into single buffer [%@]"
+ "Invalid hash selection (%lu)"
+ "MIBOMFileModeKey"
+ "MIBundlePlatform"
+ "MIIPAPatcherDeletes"
+ "MIIPAPatcherHashesFile"
+ "MIIPAPatcherMoves"
+ "MIIPAPatcherResolvesPath"
+ "MIIPAPatcherStats"
+ "MIRequiredCDHash"
+ "No installable items found at %@"
+ "None"
+ "Process %@ tried to set persona %@ for data separated apps %@, can only be done by InstallCoordination."
+ "Q32@0:8@\"NSURL\"16^@24"
+ "Q32@0:8@16^@24"
+ "Switching personas is not available on this build"
+ "Switching personas is not available on this platform"
+ "T@\"MIExecutableBundle\",&,N,V_bundle"
+ "T@\"MIStagingLocation\",&,N,V_stagingLocation"
+ "T@\"MIStagingLocation\",R,N,V_stagingLocation"
+ "Unable to set F_NOCACHE accessing file [%@]; error = %{darwin.errno}u"
+ "_IsPersonaSwitchingSupported"
+ "_bundleInDirectory:withBundleID:platformHint:error:"
+ "_existingBundleContainerForBundle:error:"
+ "_hexOfHashBuffer:length:upperCase:"
+ "_md5OfFileURL:chunkSize:withError:"
+ "_patchUpdateInstallableForBundle:manifestPath:existingBundleContainer:patchType:error:"
+ "_sha256OfFileURL:chunkSize:withError:"
+ "_stagingLocation"
+ "addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:"
+ "allStagingLocationsWithinSubsystem:completion:"
+ "bundleForURL:platformHint:forceAsPlaceholder:error:"
+ "characterSetWithCharactersInString:"
+ "checkExecutableExistsIfRequiredWithError:"
+ "com.apple.background-asset-downloader-extension"
+ "com.apple.installmetadata."
+ "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:"
+ "createTempDirectoryWithPrefix:relativeToURL:mode:withError:"
+ "dataFromPlistRepresentation:format:withError:"
+ "dataWithCapacity:"
+ "hashType:ofFileURL:chunkSize:withError:"
+ "infoPlistHashWithError:"
+ "initWithBundle:inStagingRoot:stagingLocation:packageFormat:identity:domain:installOptions:existingBundleContainer:operationType:error:"
+ "initWithBundle:inStagingRoot:stagingLocation:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:operationType:error:"
+ "initWithBundle:inStagingRoot:stagingLocation:packageFormat:identity:domain:installOptions:operationType:error:"
+ "initWithBundleIdentifier:personaUniqueString:"
+ "initWithUTF8String:"
+ "isPatchUpdate"
+ "location"
+ "macosx"
+ "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:"
+ "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:error:"
+ "moveSourceURL:toDestinationURL:fallBackToCopy:withError:"
+ "mutableBytes"
+ "nodeTypeWithURL:withError:"
+ "realpathForURL:withError:"
+ "removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:"
+ "removeURL:withError:"
+ "resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:"
+ "resolveWithError:"
+ "serializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onBehalfOf:withError:"
+ "setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:"
+ "setLength:"
+ "setStagingLocation:"
+ "setTestModeForIdentifierPrefix:testMode:validationData:"
+ "setTestingEnabled:"
+ "stageItemAtURL:toStagingLocation:options:completion:"
+ "stageItemAtURL:toStagingLocation:options:containedSymlink:error:"
+ "stagingLocation"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
+ "stagingLocationForSystemContentWithinSubsystem:completion:"
+ "stagingLocationForSystemContentWithinSubsystem:error:"
+ "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:"
+ "stagingLocationForUserContentWithinSubsystem:completion:"
+ "stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:"
+ "stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:"
+ "switchingPersonasEnabled"
+ "syncEnumerateLinesFromFileURL:options:error:enumerator:"
+ "syncReadBytesFromFileURL:chunkSize:error:handler:"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32"
+ "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16Q24@32"
+ "v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
+ "v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
+ "v80@0:8@16@24@32{?=[8I]}40@?72"
+ "volumeUUIDForURL:completion:"
+ "writePlistRepresentation:format:toFileURL:mode:withError:"
- "%s"
- "(container_get_error_description returned NULL)"
- "+[MIMCMContainer _containerForIdentifier:contentClass:forPersona:transient:create:error:]"
- "+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]"
- "+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]_block_invoke"
- "+[MIMCMContainer defaultDirectoriesForContainerType:error:]"
- "+[MIMCMContainer deleteContainers:waitForDeletion:error:]"
- "+[MIPlaceholderSerializer serializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:onBehalfOf:withError:]"
- "-[MIClientConnection createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]"
- "-[MIHelperServiceClient moveItemInStagingDirectory:atRelativePath:toDestinationURL:onBehalfOf:withError:]_block_invoke"
- "-[MIHelperServiceClient stageItemAtURL:options:containedSymlink:error:]_block_invoke"
- "-[MIInstallableBundlePatch _applyDeltaPatchWithError:]"
- "-[MIInstallableBundlePatch _applyParallelPatchProcessingArchiveSection:withError:]"
- "-[MIInstallableBundlePatch applyPatchWithError:]"
- "-[MIInstallableBundlePatch initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:operationType:error:]"
- "-[MIInstaller _bundleInDirectory:withBundleID:error:]"
- "-[MIInstaller _bundleInDirectory:withBundleID:error:]_block_invoke"
- "-[MIMCMContainer _doInitWithContainer:error:]"
- "-[MIMCMContainer _refreshContainerMetadataWithError:]"
- "-[MIMCMContainer diskUsage]"
- "-[MIMCMContainer infoValueForKey:error:]"
- "-[MIMCMContainer initWithSerializedContainer:matchingWithOptions:error:]"
- "-[MIMCMContainer purgeContentWithError:]"
- "-[MIMCMContainer reclaimDiskSpaceWithError:]"
- "-[MIMCMContainer recreateDefaultStructureWithError:]"
- "-[MIMCMContainer regenerateDirectoryUUIDWithError:]"
- "-[MIMCMContainer replaceExistingContainer:error:]"
- "-[MIMCMContainer setInfoValue:forKey:error:]"
- "-[MIUserManagement _onQueue_refreshPersonaInformationWithError:]"
- "-[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]_block_invoke"
- "-[MIUserManagement enterprisePersonaUniqueString]_block_invoke"
- "-[MIUserManagement isKnownPersonaUniqueString:error:]_block_invoke"
- "-[MIUserManagement personaForBundleID:error:]"
- "-[MIUserManagement personaForBundleID:error:]_block_invoke_2"
- "-[MIUserManagement primaryPersonaUniqueString]_block_invoke"
- "-[MIUserManagement setBundleIdentifiers:forPersonaUniqueString:error:]"
- "-[MIUserManagement systemPersonaUniqueString]_block_invoke"
- "<%@ container=%@ persona=%@ path=%@>"
- "<No container description>"
- "@\"MIBundle\""
- "@\"NSData\"32@0:8@\"NSDictionary\"16^@24"
- "@32@0:8Q16^@24"
- "@32@0:8^{container_object_s=}16^@24"
- "@44@0:8Q16@24B32^@36"
- "@48@0:8@16@24^B32^@40"
- "@52@0:8@16Q24@32B40^@44"
- "@56@0:8@16Q24@32B40B44^@48"
- "@60@0:8Q16@24B32@36@44@?52"
- "@64@0:8@16@24Q32@40B48B52^@56"
- "@64@0:8Q16@24B32@36@44B52@?56"
- "@76@0:8@16@24C32@36Q44@52Q60^@68"
- "@84@0:8@16@24C32@36Q44@52@60Q68^@76"
- "@96@0:8@16@24C32@36Q44@52@60@68C76Q80^@88"
- "B16@?0^{container_object_s=}8"
- "B32@0:8^{container_object_s=}16^@24"
- "B44@0:8@\"NSDictionary\"16@\"NSURL\"24S32^@36"
- "B80@0:8Q16@24@32{?=[8I]}40^@72"
- "B84@0:8@16@24@32i40{?=[8I]}44^@76"
- "BundleID %@ is associated with data separated persona %@"
- "Class getUMUserManagerClass(void)_block_invoke"
- "Client provided persona %@ is not among available personas on the system"
- "Container query for %@ create: %d transient: %d with nil persona"
- "Error getting disk usage for %@ (%ld): %@"
- "Exiting before replacing transient bundle container: %@"
- "Failed to allocate memory for deleting containers"
- "Failed to associate apps with persona %@ : %@"
- "Failed to construct MIMCMContainer instance with container %@ : %@"
- "Failed to create container query for querying containers for identifier %@"
- "Failed to create container query for querying containers for identifier: %@ groupIdentifiers: %@ containerType: %llu"
- "Failed to fetch container URL from %@"
- "Failed to find persona %@ when checking associated bundleIDs for it"
- "Failed to get identifier for the container"
- "Failed to get staging root path"
- "Failed to query enteprise persona string: %@"
- "Failed to query primary persona string: %@"
- "Failed to query system persona string: %@"
- "Failed to read UM's persona generation identifier when resolving persona"
- "Failed to read container error path"
- "Failed to read persona attributes from UM"
- "Failed to retrieve container subdirectories for class %llu"
- "Failed to retrieve value for key %@ from the underlying xpc object"
- "Failed to wipe container for identifier %@"
- "ICLSoftLinking.h"
- "Info.plist"
- "MIInstallableBundlePatch"
- "MIMCMContainer"
- "MIUserManagement"
- "Q24@0:8@16"
- "Querying persona from UserManagement: %@"
- "T@\"MIBundle\",&,N,V_bundle"
- "T@\"MIExecutableBundle\",&,D,N"
- "T@\"NSDictionary\",&,N,V_personaAttributesMap"
- "T@\"NSString\",&,N,V_systemPersonaUniqueString"
- "T@\"NSString\",C,N,V_enterprisePersonaUniqueString"
- "T@\"NSString\",C,N,V_primaryPersonaUniqueString"
- "T@\"NSString\",R,D,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_personaUniqueString"
- "T@\"NSURL\",R,N,V_containerURL"
- "TB,N,V_isTransient"
- "TB,R,N,V_isNew"
- "TQ,N,V_personaGenerationIdentifier"
- "TQ,R,N,V_containerClass"
- "T^{container_object_s=},R,N,V_mcmContainer"
- "UMUserManager"
- "Unable to find class %s"
- "Underlying errno set by container manager is %s"
- "^{container_object_s=}"
- "^{container_object_s=}16@0:8"
- "_ContainerURL"
- "_allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:"
- "_bundleInDirectory:withBundleID:error:"
- "_containerClass"
- "_containerForIdentifier:contentClass:forPersona:transient:create:error:"
- "_containerURL"
- "_doInitWithContainer:error:"
- "_enterprisePersonaUniqueString"
- "_enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:"
- "_identifier"
- "_isNew"
- "_isTransient"
- "_mcmContainer"
- "_onQueue_refreshPersonaInformationWithError:"
- "_personaAttributesMap"
- "_personaGenerationIdentifier"
- "_personaUniqueString"
- "_primaryPersonaUniqueString"
- "_refreshContainerMetadataWithError:"
- "_systemPersonaUniqueString"
- "bundleIDs"
- "com.apple.installd.umAccessQueue"
- "containerForIdentifier:contentClass:forPersona:create:error:"
- "container_operation_delete_array returned NULL but did not set an error"
- "containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:error:"
- "containersForContentClass:forPersona:fetchTransient:error:"
- "containersForGroupIdentifier:forPersona:create:fetchTransient:error:"
- "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:"
- "currentHandler"
- "dataFromPlistRepresentation:withError:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "defaultDirectoriesForContainerType:error:"
- "deleteContainers:waitForDeletion:error:"
- "enterprisePersonaUniqueString"
- "executableExistsWithError:"
- "handleFailureInFunction:file:lineNumber:description:"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:existingBundleContainer:operationType:error:"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:operationType:error:"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:operationType:error:"
- "initWithBundleID:persona:"
- "initWithContainer:error:"
- "initWithPersonaString:personaType:associatedBundleIDs:"
- "initWithSerializedContainer:matchingWithOptions:error:"
- "isEnterprisePersona"
- "isKnownPersonaUniqueString:error:"
- "isNew"
- "isPersonalPersona"
- "isSystemPersona"
- "mcmContainer"
- "moveItemInStagingDirectory:atRelativePath:toDestinationURL:onBehalfOf:completion:"
- "moveItemInStagingDirectory:atRelativePath:toDestinationURL:onBehalfOf:withError:"
- "personaAttributesMap"
- "personaForBundleID:error:"
- "personaGenerationIdentifier"
- "personaGenerationIdentifierWithError:"
- "personaType"
- "reclaimDiskSpaceWithError:"
- "recreateDefaultStructureWithError:"
- "replaceExistingContainer:error:"
- "serializedContainerRepresentation"
- "serializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:onBehalfOf:withError:"
- "setBundleIdentifiers:forPersonaWithPersonaUniqueString:withError:"
- "setEnterprisePersonaUniqueString:"
- "setInfoValue:forKey:error:"
- "setIsTransient:"
- "setPersonaAttributesMap:"
- "setPersonaGenerationIdentifier:"
- "setPrimaryPersonaUniqueString:"
- "setSystemPersonaUniqueString:"
- "softlink:o:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement"
- "stageItemAtURL:options:completion:"
- "stageItemAtURL:options:containedSymlink:error:"
- "stagingRootForDevice:url:identifier:error:"
- "stagingRootForSystemContent"
- "stringWithFileSystemRepresentation:"
- "systemPersonaUniqueString"
- "transientContainerForIdentifier:contentClass:forPersona:create:error:"
- "userPersonaType"
- "v32@?0@\"NSString\"8@\"MIPersonaAttributes\"16^B24"
- "v40@0:8@\"NSURL\"16@\"MIInstallOptions\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24@32i40@?44"
- "v80@0:8Q16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
- "v80@0:8Q16@24@32{?=[8I]}40@?72"
- "void *UserManagementLibrary(void)"
- "writePlistRepresentation:toFileURL:mode:withError:"

```
