## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-699.100.10.0.0
-  __TEXT.__text: 0x9a814
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0xa7a0
-  __TEXT.__objc_methlist: 0x5854
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x17866
-  __TEXT.__objc_methname: 0x10072
-  __TEXT.__objc_classname: 0x9d4
-  __TEXT.__objc_methtype: 0x224b
-  __TEXT.__oslogstring: 0xd3dd
-  __TEXT.__gcc_except_tab: 0x28c4
+755.0.0.0.0
+  __TEXT.__text: 0xa1ab8
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0xad20
+  __TEXT.__objc_methlist: 0x5c24
+  __TEXT.__const: 0x208
+  __TEXT.__cstring: 0x1888b
+  __TEXT.__objc_methname: 0x10b97
+  __TEXT.__objc_classname: 0x9ed
+  __TEXT.__objc_methtype: 0x2329
+  __TEXT.__oslogstring: 0xdb76
+  __TEXT.__gcc_except_tab: 0x2aa8
   __TEXT.__ustring: 0x1a64
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x2358
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x410
+  __TEXT.__unwind_info: 0x2478
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2a40
-  __DATA_CONST.__cfstring: 0x9500
-  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__const: 0x2b28
+  __DATA_CONST.__cfstring: 0x9c40
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xbce0
-  __DATA.__objc_selrefs: 0x3138
-  __DATA.__objc_ivar: 0x470
-  __DATA.__objc_data: 0x1680
+  __DATA.__objc_const: 0xc398
+  __DATA.__objc_selrefs: 0x3310
+  __DATA.__objc_ivar: 0x4ac
+  __DATA.__objc_data: 0x16d0
   __DATA.__data: 0x650
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x260
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 753F0A8A-7E67-335F-BCDD-40D8788E97B7
-  Functions: 3141
-  Symbols:   412
-  CStrings:  6490
+  UUID: 8AAFDDF2-6BDF-323F-BBBE-73174968B5F5
+  Functions: 3269
+  Symbols:   424
+  CStrings:  6751
 
Symbols:
+ _MobileInstallationAddDataSeparatedAppsToPersona
+ _MobileInstallationRemoveDataSeparatedAppsFromPersona
+ _MobileInstallationSetPersonaForDataSeparatedApps
+ _OBJC_CLASS_$_MIHelperServiceFrameworkClient
+ _OBJC_CLASS_$_MILocation
+ _OBJC_CLASS_$_MILocationSystemDefinedBase
+ _OBJC_CLASS_$_MILocationSystemDefinedCommon
+ _OBJC_CLASS_$_MILocationUserDefined
+ _OBJC_CLASS_$_MILocationUserDefinedDirectory
+ _OBJC_CLASS_$_MIStagingLocation
+ __kCFBundleSupportedPlatformsKey
+ _lchown
CStrings:
+ "\t"
+ "%@ promise being set has different location, %@, than this placeholder, %@."
+ "%@.%@"
+ "%@: Failed to locate data import promise instance with UUID %@ after deserialization"
+ "%s: %@ : Data Import Promises set: %@"
+ "%s: %@ promise being set has different location, %@, than this placeholder, %@. : %@"
+ "%s: %@: Enabling post processing by default"
+ "%s: %@: Failed to find placeholder record for demoted app: %@"
+ "%s: %@: Failed to locate data import promise instance with UUID %@ after deserialization : %@"
+ "%s: %@: Unable to find app asset promise with UUID %@; proceeding because it's not needed"
+ "%s: %@: Unable to find placeholder promise with UUID %@; proceeding because it's not needed"
+ "%s: App extension placeholders array has extension %@ with the location %@, but the parent %@ has the location %@. These locations must match. : %@"
+ "%s: App extension placeholders array has multiple %@ placeholders with the same bundle directory name of %@ : %@"
+ "%s: App extension placeholders array has multiple placeholders with the same bundle ID of %@ : %@"
+ "%s: Cannot set app extension placeholder with bundle ID %@ on parent app %@ because this extension's bundle ID does not have required bundle ID prefix of \"%@\" : %@"
+ "%s: Client %@ adding bundleID %@ to persona: %@"
+ "%s: Client %@ associating persona %@ with bundle IDs: %@"
+ "%s: Client %@ is missing persona based multi user (associating bundleIDs with persona) operation entitlement. : %@"
+ "%s: Client %@ removing bundle IDs: %@ from persona %@"
+ "%s: Could not find data import promise with UUID %@ : %@"
+ "%s: Expected volume UUID for transfer path %@ to match the volume UUID corresponding to location %@ when creating promised transfer to path data promise with name: %@ client: %@ - %@"
+ "%s: Failed to fetch localized string for key %@ from bundle %@ within table %@"
+ "%s: Failed to find all existing promise staging directories: %@"
+ "%s: Failed to resolve URL from staging location %@: %@"
+ "%s: Failed to resolve promise staging URL from location %@: %@ : %@"
+ "%s: Failed to set %@ promise with location %@ on a coordinator for app identity %@ targeting location %@  : %@"
+ "%s: Placeholder with bundle ID %@ is not an app extension so cannot be set as an app extension placeholder on %@ : %@"
+ "%s: Plist key [%@] faled to decode; error = %@"
+ "%s: Plist key [%@] is missing or of the wrong type; expected = [NSDictionary], got = %@"
+ "%s: Plist key [%@] is missing or of the wrong type; expected = [NSString], got = %@"
+ "%s: Plist key is of the wrong type; expected = [NSString|NSDictionary], got = %@"
+ "%s: Switching personas is not available on this build : %@"
+ "%s: Switching personas is not available on this platform : %@"
+ "+[IXSPlaceholder _sanitizedFilesystemNameForName:fileExtension:fallingBackToName:]"
+ ", "
+ "-[IXApplicationIdentity initFromDelimitedString:]"
+ "-[IXApplicationIdentity initFromPlistDictionary:]"
+ "-[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]_block_invoke"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:getDataImportPromises:]"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:getDataImportPromises:]_block_invoke"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:hasDataImportPromises:]"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:hasDataImportPromises:]_block_invoke"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:setDataImportPromiseUUIDs:completion:]"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:setDataImportPromiseUUIDs:completion:]_block_invoke"
+ "-[IXSClientConnection _remote_addBundleIDs:toMappingsForPersona:completion:]"
+ "-[IXSClientConnection _remote_associateMultiPersonaAppsWithBundleIDs:withPersona:completion:]"
+ "-[IXSClientConnection _remote_refreshContainersWithOptions:forAppWithIdentity:completion:]"
+ "-[IXSClientConnection _remote_removeBundleIDs:fromMappingsForPersona:completion:]"
+ "-[IXSContainerRefreshManager _onQueue_terminateBundleID:withOptions:terminationAssertion:error:]"
+ "-[IXSContainerRefreshManager refreshContainerTypesWithOptions:forAppWithIdentity:completion:]_block_invoke"
+ "-[IXSCoordinatedAppInstall _internalInitWithSeed:scopedToConnection:error:]_block_invoke"
+ "-[IXSCoordinatedAppInstall setDataImportPromises:]"
+ "-[IXSCoordinatedAppInstall shouldEnablePostProcessingByDefault]"
+ "-[IXSCoordinatedAppInstall(IPCMethods) _remote_getDataImportPromises:]"
+ "-[IXSCoordinatedAppInstall(IPCMethods) _remote_hasDataImportPromises:]"
+ "-[IXSCoordinatedAppInstall(IPCMethods) _remote_setDataImportPromiseUUIDs:completion:]"
+ "-[IXSCoordinatedAppInstall(IPCMethods) _validateLocationForPromise:error:]"
+ "-[IXSPlaceholder(IXSPlaceholderIPCMethods) _checkLocationOfPromiseMatchesOurs:description:error:]"
+ "-[IXSUninstallAlert _localizedStringForKey:tableName:withFormatHint:]"
+ "04:44:52"
+ "<%@<%p> : %@ containerTypes=%lx allowRefreshDuringPostProcessing=%d forceTerminateApp=%d>"
+ "@\"<MILocationProtocol>\""
+ "@\"IXSCoordinatedAppInstall\"16@?0^@8"
+ "@\"MIStagingLocation\""
+ "@40@0:8@16@24@32"
+ "@72@0:8@16@24{?=[8I]}32^@64"
+ "App extension placeholders array has extension %@ with the location %@, but the parent %@ has the location %@. These locations must match."
+ "App extension placeholders array has multiple %@ placeholders with the same bundle directory name of %@"
+ "App extension placeholders array has multiple placeholders with the same bundle ID of %@"
+ "Assertion for associating persona %@ : %@"
+ "Assertion for disassociating persona %@ : %@"
+ "B40@0:8@16I24I28^@32"
+ "Cannot set app extension placeholder with bundle ID %@ on parent app %@ because this extension's bundle ID does not have required bundle ID prefix of \"%@\""
+ "Client %@ is missing persona based multi user (associating bundleIDs with persona) operation entitlement."
+ "Coordinator intent %@ doesn't support a post processing app extension"
+ "Could not find data import promise with UUID %@"
+ "Cross-platform Migration"
+ "DTPlatformName"
+ "Data Import Promise"
+ "Duplicate app extension bundle directory names."
+ "Entitlements"
+ "ExtensionKit"
+ "Failed to get promise staging directory for install location %@ with uniqueName %@: %@"
+ "Failed to lchown %s with uid/gid %d/%d : %s"
+ "Failed to resolve promise staging URL from location %@: %@"
+ "Failed to set %@ promise with location %@ on a coordinator for app identity %@ targeting location %@ "
+ "IXAppCoordinationStateDataImportPromisesIncomplete"
+ "IXAppCoordinationStateDataImportPromisesNotSet"
+ "IXRefreshContainerOptions"
+ "Icon Info.plist content"
+ "Icon resources"
+ "InfoPlist loctable"
+ "LSRequiresIPhoneOS"
+ "Localization"
+ "May 23 2025"
+ "Metadata"
+ "MigrationKit"
+ "Mismatched location."
+ "Not processing attempt to set data import promises because those that were set were already complete and this coordinator is past the point of waiting for them."
+ "OSMigration"
+ "Placeholder with bundle ID %@ is not an app extension so cannot be set as an app extension placeholder on %@"
+ "PlugInKit"
+ "Sinf"
+ "Switching personas is not available on this build"
+ "Switching personas is not available on this platform"
+ "T@\"<MILocationProtocol>\",&,N,V_location"
+ "T@\"<MILocationProtocol>\",R,N"
+ "T@\"MIStagingLocation\",&,N,V_stagingLocation"
+ "T@\"NSArray\",C,N,V_cfBundleSupportedPlatforms"
+ "T@\"NSArray\",C,N,V_dataImportPromiseUUIDs"
+ "T@\"NSArray\",C,N,V_dataImportPromises"
+ "T@\"NSNumber\",&,N,V_totalExpectedDataImportSizeInBytes"
+ "T@\"NSString\",C,N,V_bundleDirectoryName"
+ "T@\"NSString\",C,N,V_dtPlatformName"
+ "T@\"NSString\",R,N,V_reason"
+ "TB,N,V_allowRefreshDuringPostProcessing"
+ "TB,N,V_forceTerminateApp"
+ "TB,N,V_isMacPlatformApp"
+ "TB,N,V_lsRequiresIPhoneOS"
+ "TB,R,N,V_isMacPlatformApp"
+ "TQ,R,N,V_containerTypes"
+ "Target install volume has been unmounted."
+ "URLByDeletingLastPathComponent"
+ "Unknown IXPlaceholderType value %lu"
+ "_CheckTransferPathForSeed"
+ "_CleanStagingLocation"
+ "_DoFirstRunCleanup_block_invoke_2"
+ "_IsPersonaSwitchingSupported"
+ "_allowRefreshDuringPostProcessing"
+ "_bundleDirectoryName"
+ "_cfBundleSupportedPlatforms"
+ "_checkLocationOfPromiseMatchesOurs:description:error:"
+ "_containerTypes"
+ "_dataImportPromiseUUIDs"
+ "_dataImportPromises"
+ "_dtPlatformName"
+ "_forceTerminateApp"
+ "_internalInitWithSeed:scopedToConnection:error:"
+ "_isMacPlatformApp"
+ "_localizedStringForKey:tableName:withFormatHint:"
+ "_location"
+ "_locationClassCluster"
+ "_lsRequiresIPhoneOS"
+ "_onQueue_terminateBundleID:withOptions:terminationAssertion:error:"
+ "_preparedBundleDirectoryName"
+ "_remote_IXSCoordinatedAppInstall:getDataImportPromises:"
+ "_remote_IXSCoordinatedAppInstall:hasDataImportPromises:"
+ "_remote_IXSCoordinatedAppInstall:setDataImportPromiseUUIDs:completion:"
+ "_remote_addBundleIDs:toMappingsForPersona:completion:"
+ "_remote_associateMultiPersonaAppsWithBundleIDs:withPersona:completion:"
+ "_remote_getDataImportPromises:"
+ "_remote_hasDataImportPromises:"
+ "_remote_refreshContainersWithOptions:forAppWithIdentity:completion:"
+ "_remote_removeBundleIDs:fromMappingsForPersona:completion:"
+ "_remote_setDataImportPromiseUUIDs:completion:"
+ "_remote_stagingLocationForInstallLocation:completion:"
+ "_sanitizedFilesystemNameForName:fileExtension:fallingBackToName:"
+ "_shouldStageUpdate"
+ "_stagingLocation"
+ "_totalExpectedDataImportSizeInBytes"
+ "_validateLocationForPromise:error:"
+ "allStagingLocationsWithinSubsystem:error:"
+ "allowRefreshDuringPostProcessing"
+ "appex"
+ "b"
+ "bundleDirectoryName"
+ "cfBundleSupportedPlatforms"
+ "com.apple.app-migration"
+ "com.apple.private.InstallCoordination.personaBasedMultiUser"
+ "containerTypes"
+ "dataImportPromiseUUIDs"
+ "dataImportPromises"
+ "dtPlatformName"
+ "forceTerminateApp"
+ "inPostProcessingPhase"
+ "initFromDelimitedString:"
+ "initFromPlistDictionary:"
+ "initWithBundleID:"
+ "initWithBundleID:personaUniqueString:location:"
+ "initWithBundleIdentifier:personaUniqueString:location:"
+ "initWithReason:containerTypes:"
+ "initWithSeed:scopedToConnection:creatorAuditToken:error:"
+ "isMacPlatformApp"
+ "location"
+ "locationFromPlistDictionary:error:"
+ "locationType"
+ "lsRequiresIPhoneOS"
+ "osAppMigrationEnabled"
+ "personaString"
+ "promiseStagingRootAbortingOnErrorForInstallLocation:usingUniqueName:"
+ "promiseStagingRootForInstallLocation:usingUniqueName:error:"
+ "realPathForURL:"
+ "refreshContainerTypesWithOptions:forAppWithIdentity:completion:"
+ "resolveWithError:"
+ "setAllowRefreshDuringPostProcessing:"
+ "setBundleDirectoryName:"
+ "setCfBundleSupportedPlatforms:"
+ "setDataImportPromiseUUIDs:"
+ "setDataImportPromises:"
+ "setDtPlatformName:"
+ "setForceTerminateApp:"
+ "setIsMacPlatformApp:"
+ "setLocation:"
+ "setLsRequiresIPhoneOS:"
+ "setStagingLocation:"
+ "setTotalExpectedDataImportSizeInBytes:"
+ "shouldEnablePostProcessingByDefault"
+ "stagingLocation"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
+ "standardizeOwnershipAtURL:toUID:toGID:error:"
+ "supportsDataExport"
+ "switchingPersonasEnabled"
+ "totalExpectedDataImportSizeInBytes"
+ "v24@?0@\"MIStagingLocation\"8^B16"
+ "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v40@0:8@\"IXRefreshContainerOptions\"16@\"IXApplicationIdentity\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v48@0:8@\"NSArray\"16@\"NSError\"24Q32@?<v@?@\"NSSet\"@\"NSError\">40"
+ "validateURL:forLocation:error:"
+ "\xf0\x81"
- "%@.app"
- "%s: App extension placeholders array has multiple placeholders with the same bundleID of %@ : %@"
- "%s: Cannot complete attempt to set app extension placeholder with bundle ID %@ because it does not have the parent placeholder's required bundle ID prefix of %@ : %@"
- "%s: Failed to create promise staging directory : %@"
- "%s: Reason passed to %s was nil! : %@"
- "%s: Unable to find placeholder promise with UUID %@; proceeding because it's not needed"
- "%s: Unexpected app install state: %lu"
- "-[IXSClientConnection _remote_refreshContainerTypes:forAppWithIdentity:reason:completion:]"
- "-[IXSContainerRefreshManager _onQueue_terminateBundleID:reason:terminationAssertion:error:]"
- "-[IXSContainerRefreshManager refreshContainerTypes:forAppWithIdentity:reason:completion:]_block_invoke"
- "04:41:49"
- "@\"IXSCoordinatedAppInstall\"8@?0"
- "App extension placeholders array has multiple placeholders with the same bundleID of %@"
- "Apr 19 2025"
- "Cannot complete attempt to set app extension placeholder with bundle ID %@ because it does not have the parent placeholder's required bundle ID prefix of %@"
- "Failed to create promise staging directory"
- "Failed to create staging root at %@ : %@"
- "Failed to get promise staging directory: %@"
- "Failed to get staging root path: %@"
- "PromiseStaging"
- "Reason passed to %s was nil!"
- "_internalInitWithSeed:scopedToConnection:"
- "_isStagedUpdate"
- "_onQueue_terminateBundleID:reason:terminationAssertion:error:"
- "_remote_refreshContainerTypes:forAppWithIdentity:reason:completion:"
- "createTemporaryIconsDirectoryWithError:"
- "initWithSeed:scopedToConnection:"
- "promiseStagingRootDirectoryAbortingOnError"
- "promiseStagingRootDirectoryWithError:"
- "refreshContainerTypes:forAppWithIdentity:reason:completion:"
- "v48@0:8@\"NSArray\"16@\"NSError\"24Q32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16@\"IXApplicationIdentity\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8Q16@24@32@?40"
- "\xf0q"

```
