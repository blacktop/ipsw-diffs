## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2349.0.31.0.2
-  __TEXT.__text: 0x42e14
+2349.40.6.0.9
+  __TEXT.__text: 0x3a010
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x4a14
-  __TEXT.__const: 0x630
-  __TEXT.__cstring: 0xab31
-  __TEXT.__oslogstring: 0x3ef0
-  __TEXT.__gcc_except_tab: 0x1958
-  __TEXT.__unwind_info: 0x1510
-  __TEXT.__objc_classname: 0x4a1
-  __TEXT.__objc_methname: 0xc0bf
-  __TEXT.__objc_methtype: 0x1552
-  __TEXT.__objc_stubs: 0x61e0
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__objc_methlist: 0x429c
+  __TEXT.__const: 0x610
+  __TEXT.__cstring: 0x9c53
+  __TEXT.__gcc_except_tab: 0x164c
+  __TEXT.__oslogstring: 0x37c5
+  __TEXT.__unwind_info: 0x1330
+  __TEXT.__objc_classname: 0x44a
+  __TEXT.__objc_methname: 0xb230
+  __TEXT.__objc_methtype: 0x1504
+  __TEXT.__objc_stubs: 0x54c0
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a08
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x2610
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6c00
-  __AUTH_CONST.__objc_const: 0x6cd8
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x6280
+  __AUTH_CONST.__objc_const: 0x6478
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x40c
+  __DATA.__objc_ivar: 0x3e4
   __DATA.__data: 0x368
-  __DATA.__bss: 0x258
-  __DATA_DIRTY.__objc_data: 0x10e0
+  __DATA.__bss: 0x190
+  __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xf8
   __DATA_DIRTY.__common: 0x1
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1924
-  Symbols:   2388
-  CStrings:  3994
+  Functions: 1740
+  Symbols:   2188
+  CStrings:  3672
 
Symbols:
+ _OBJC_CLASS_$_NSRegularExpression
- OBJC_IVAR_$_MBContainer._plist
- _MBStringForContainerType
- _MCMContainerContentClassForMBContainerType
- _OBJC_CLASS_$_MBApp
- _OBJC_CLASS_$_MBAppManager
- _OBJC_CLASS_$_MBContainer
- _OBJC_CLASS_$_MBProperties
- _OBJC_CLASS_$_NSPropertyListSerialization
- _OBJC_METACLASS_$_MBApp
- _OBJC_METACLASS_$_MBAppManager
- _OBJC_METACLASS_$_MBContainer
- _OBJC_METACLASS_$_MBProperties
- _kCFBundleIdentifierKey
- _kCFBundleVersionKey
- _kLockdownBuildVersionKey
- _kLockdownDeviceNameKey
- _kLockdownProductTypeKey
- _kLockdownSerialNumberKey
- _kLockdownUniqueDeviceIDKey
CStrings:
+ "-[MBDomain _initWithName:volumeMountPoint:volumeType:rootPath:]"
+ "-[NSFileManager(MobileBackup) mb_moveAsideAndMarkPurgeableDBFilesAtPath:error:]"
+ "=mbfm= Failed to mark DB %!@(MISSING) as purgeable: %!@(MISSING)"
+ "=mbfm= Failed to mark DB %!@(MISSING) as purgeable: %!@(MISSING)"
+ "=mbfm= Failed to move aside DB file %!@(MISSING): %!@(MISSING)"
+ "=mbfm= Failed to move aside DB file %!@(MISSING): %!@(MISSING)"
+ "=mbfm= Moved aside DB file %!@(MISSING) to %!@(MISSING)"
+ "=mbfm= Moved aside DB file %!@(MISSING) to %!@(MISSING)"
+ "BackupPathsToFailVerifyingRegex"
+ "DomainsToBackUpRegex"
+ "DomainsToSendInvalidChecksumRegex"
+ "Failed to compile regex: %!@(MISSING)"
+ "Failed to compile regex: %!@(MISSING)"
+ "MaxConcurrentRestoreDomainOperations"
+ "Removing domain %!@(MISSING) not matching regex (%!@(MISSING))"
+ "Removing domain %!@(MISSING) not matching regex (%!@(MISSING))"
+ "Removing domains not matching regex (%!@(MISSING))"
+ "Removing domains not matching regex (%!@(MISSING))"
+ "RestoreAssetIDsToFailFetchingRegex"
+ "RestorePathsToFailPlacingRegex"
+ "RestorePathsToFailVerifyingRegex"
+ "backupPathsToFailVerifyingRegex"
+ "dbPath"
+ "domainsToBackUpRegex"
+ "domainsToSendInvalidChecksumRegex"
+ "initWithPattern:options:error:"
+ "isAppDomainName:"
+ "maxConcurrentRestoreDomainOperations"
+ "mb_moveAsideAndMarkPurgeableDBFilesAtPath:error:"
+ "numberOfMatchesInString:options:range:"
+ "removeDomainsNotMatchingRegex:"
+ "restoreAssetIDsToFailFetchingRegex"
+ "restoreDomain:deviceUUID:snapshotUUID:intoPath:error:"
+ "restoreFailures.plist"
+ "restoreFailuresPlistPath"
+ "restorePathsToFailPlacingRegex"
+ "restorePathsToFailVerifyingRegex"
+ "setByAddingObject:"
- "\x11"
- "!accountClass || [accountClass isKindOfClass:NSNumber.class]"
- "!accountType || [accountType isKindOfClass:NSNumber.class]"
- "!requiredProductVersion || [requiredProductVersion isKindOfClass:NSString.class]"
- "%!f(MISSING)"
- "%!@(MISSING) is not a containerized app domain - not removing from the disabled domains list"
- "%!@(MISSING) is not a containerized app domain - not removing from the disabled domains list"
- "%!@(MISSING) lockdown value not an NSString"
- "%!@(MISSING) value not an NSData"
- "%!@(MISSING) value not an NSDictionary"
- "%!@(MISSING) value not an NSNumber"
- "+[MBAppManager _persistDisabledDomainNames:forPersona:]"
- "-[MBAppManager _copyAppsWithPlists:volumeMountPoints:safeHarbor:error:]"
- "-[MBAppManager createSafeHarbor:error:]"
- "-[MBProperties setAccountClass:]"
- "-[MBProperties setAccountType:]"
- "-[MBProperties setRequiredProductVersion:]"
- ".com.apple.mobile_container_manager.metadata.plist"
- "9A"
- "<%!@(MISSING): version=%!f(MISSING), systemDomainsVersion=%!f(MISSING), requiredProductVersion=%!@(MISSING), date=\"%!@(MISSING)\", encrypted=%!d(MISSING), passcodeSet=%!d(MISSING), lockdownKeys=%!@(MISSING)>"
- "@"
- "@\"MBSettingsContext\""
- "@36@0:8@16@24B32"
- "Account item %!@(MISSING) not a string"
- "AccountClass"
- "AccountType"
- "ActiveAppleID"
- "Adding appleID:%!@(MISSING), DSID:%!@(MISSING), altDSID:%!@(MISSING), dataClass:%!@(MISSING)"
- "Adding appleID:%!@(MISSING), DSID:%!@(MISSING), altDSID:%!@(MISSING), dataClass:%!@(MISSING)"
- "App %!@(MISSING) has no data container to move to safe harbor"
- "App %!@(MISSING) has no data container to move to safe harbor"
- "App: Found container %!@(MISSING) (%!@(MISSING)) at %!@(MISSING)"
- "App: Found container %!@(MISSING) (%!@(MISSING)) at %!@(MISSING)"
- "AppDomain-com.apple.Health"
- "AppDomain-com.apple.iBooks"
- "AppleIDs"
- "ApplicationType"
- "Applications"
- "B24@?0@8@\"NSDictionary\"16"
- "B44@0:8@16@24B32^@36"
- "BackupKeyBag"
- "BooksDomain"
- "BudyStashData"
- "ContainerContentClass"
- "Containers value not an NSDictionary"
- "Copying safe harbors"
- "Copying safe harbors"
- "Creating directory %!@(MISSING)"
- "Creating directory %!@(MISSING)"
- "Creating safe harbor for container %!@(MISSING) with type %!@(MISSING) at %!@(MISSING)"
- "Creating safe harbor for container %!@(MISSING) with type %!@(MISSING) at %!@(MISSING)"
- "DSID mismatch: existingDSID:%!@(MISSING) != DSID:%!@(MISSING)"
- "DSID mismatch: existingDSID:%!@(MISSING) != DSID:%!@(MISSING)"
- "Data/Application"
- "Data/PluginKitPlugin"
- "Date"
- "Date missing from safe harbor: %!@(MISSING)"
- "Date value not an NSDate"
- "DisabledDomains"
- "Documents"
- "Duplicate container ID: %!@(MISSING)"
- "Entitlements"
- "Enumerating apps for persona %!@(MISSING) with current persona %!@(MISSING)"
- "Enumerating apps for persona %!@(MISSING) with current persona %!@(MISSING)"
- "Error changing ownership of Safe Harbor Info.plist"
- "Error deserializing properties: %!@(MISSING)"
- "Error removing safe harbor: %!@(MISSING)"
- "Error removing safe harbor: %!@(MISSING)"
- "Error serializing properties: %!@(MISSING)"
- "Error writing Safe Harbor Info.plist"
- "Failed to copy system containers from generated plists, error:%!@(MISSING)"
- "Failed to copy system containers from generated plists, error:%!@(MISSING)"
- "Failed to copy system shared containers from generated plists, error:%!@(MISSING)"
- "Failed to copy system shared containers from generated plists, error:%!@(MISSING)"
- "Failed to create safe harbor for %!@(MISSING): %!@(MISSING)"
- "Failed to create safe harbor for %!@(MISSING): %!@(MISSING)"
- "Failed to enumerate contents of path at %!@(MISSING): %!@(MISSING)"
- "Failed to enumerate contents of path at %!@(MISSING): %!@(MISSING)"
- "Failed to fetch the contents of %!@(MISSING): %!@(MISSING)"
- "Failed to fetch the contents of %!@(MISSING): %!@(MISSING)"
- "Failed to find volume (%!@(MISSING)) for %!@(MISSING)"
- "Failed to find volume (%!@(MISSING)) for %!@(MISSING)"
- "Failed to move file in %!@(MISSING) to safe harbor"
- "Failed to move file in %!@(MISSING) to safe harbor"
- "Failed to move file to safe harbor"
- "Failed to parse system container plist"
- "Failed to parse system container plist: %!@(MISSING)"
- "Failed to parse system container plist: %!@(MISSING)"
- "Failed to refresh app info before moving to safe harbor: %!@(MISSING)"
- "Failed to refresh app info before moving to safe harbor: %!@(MISSING)"
- "Failed to remove the placeholder archive at %!@(MISSING): %!@(MISSING)"
- "Failed to remove the placeholder archive at %!@(MISSING): %!@(MISSING)"
- "Found empty app group container identifier for %!@(MISSING) (%!@(MISSING))"
- "Found empty app group container identifier for %!@(MISSING) (%!@(MISSING))"
- "Found installed app, bundleID:%!@(MISSING), isPlaceholder:%!d(MISSING), bundleDir:%!@(MISSING), containerDir:%!@(MISSING)"
- "Found installed app, bundleID:%!@(MISSING), isPlaceholder:%!d(MISSING), bundleDir:%!@(MISSING), containerDir:%!@(MISSING)"
- "Found nil bundleDir for %!@(MISSING): %!@(MISSING)"
- "Found nil bundleDir for %!@(MISSING): %!@(MISSING)"
- "Found nil bundleID: %!@(MISSING)"
- "Found nil bundleID: %!@(MISSING)"
- "GeoJSON"
- "GroupContainers"
- "HealthDomain"
- "Installed system plugin: %!@(MISSING)"
- "Installed system plugin: %!@(MISSING)"
- "Internal"
- "IsEncrypted"
- "IsPlaceholder"
- "IsUpdating"
- "Library"
- "Library/Caches"
- "Library/Caches/NeverRestore"
- "Library/Saved Application State"
- "Library/SplashBoard"
- "Library/SyncedPreferences"
- "Lockdown"
- "Looking up system containers"
- "Looking up system containers"
- "Looking up system plugins"
- "Looking up system plugins"
- "Looking up user apps"
- "Looking up user apps"
- "MBApp"
- "MBApp.m"
- "MBAppGroup"
- "MBAppManager"
- "MBAppManager.m"
- "MBAppPlugin"
- "MBContainer"
- "MBDisabledDomains"
- "MBProperties"
- "MBProperties.m"
- "MBSystemContainer"
- "Manifest key is not an NSData"
- "ManifestKey"
- "NewsstandArtwork"
- "Not a safe harbor"
- "Not moving file %!@(MISSING) into the safe harbor because it lies outside the default directory hierarchy"
- "Not moving file %!@(MISSING) into the safe harbor because it lies outside the default directory hierarchy"
- "Not removing safe harbor %!@(MISSING) created at %!@(MISSING)"
- "Not removing safe harbor %!@(MISSING) created at %!@(MISSING)"
- "Path"
- "PlaceholderEntitlements.plist"
- "PluginOwnerBundleID"
- "Plugins"
- "Removing %!@(MISSING) from disabled domains list - related app is no longer installed on the device"
- "Removing %!@(MISSING) from disabled domains list - related app is no longer installed on the device"
- "Removing old placeholder archive at %!@(MISSING)"
- "Removing old placeholder archive at %!@(MISSING)"
- "Removing safe harbor %!@(MISSING) created at %!@(MISSING)"
- "Removing safe harbor %!@(MISSING) created at %!@(MISSING)"
- "Removing safe harbors created before %!@(MISSING)"
- "Removing safe harbors created before %!@(MISSING)"
- "RequiredProductVersion"
- "RestrictedDomains"
- "SafeHarborDockingDate"
- "Shared/AppGroup"
- "Skipping app %!@(MISSING), because it's container path %!@(MISSING) is on the wrong volume"
- "Skipping app %!@(MISSING), because it's container path %!@(MISSING) is on the wrong volume"
- "Skipping system container %!@(MISSING), because it's path is on the wrong volume"
- "Skipping system container %!@(MISSING), because it's path is on the wrong volume"
- "Skipping system plugin %!@(MISSING), because it's container path is on the wrong volume"
- "Skipping system plugin %!@(MISSING), because it's container path is on the wrong volume"
- "System"
- "System Plugin: Found app group container %!@(MISSING) at %!@(MISSING) for %!@(MISSING)"
- "System Plugin: Found app group container %!@(MISSING) at %!@(MISSING) for %!@(MISSING)"
- "System Plugin: Found container %!@(MISSING) %!@(MISSING)"
- "System Plugin: Found container %!@(MISSING) %!@(MISSING)"
- "System container: %!@(MISSING)"
- "System container: %!@(MISSING)"
- "System/Data"
- "System/Shared"
- "SystemData/com.apple.AuthenticationServices"
- "SystemData/com.apple.chrono"
- "SystemDomainsVersion"
- "SystemDomainsVersion not an NSString"
- "T@\"NSData\",&,N"
- "T@\"NSData\",N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSNumber\",&,N"
- "T@\"NSString\",&,N"
- "T@,R,N,V_plist"
- "TB,N,GisProtected,V_protected"
- "TB,N,GwasPasscodeSet"
- "TB,R,N,GisSafeHarbor"
- "Td,N"
- "Unsupported properties version: %!f(MISSING)"
- "Unsupported system domains version: %!f(MISSING)"
- "Version value not an NSNumber or NSString"
- "WasPasscodeSet"
- "Writing %!@(MISSING)"
- "Writing %!@(MISSING)"
- "_allDisabledDomainNamesForPersona:"
- "_allPersistedDisabledDomainNamesForPersona:"
- "_boolForKey:"
- "_containersByID"
- "_copyAppsWithPlists:volumeMountPoints:safeHarbor:error:"
- "_copySafeHarborsWithVolumeMountPoints:error:"
- "_copySystemContainersWithPlists:volumeMountPoints:error:"
- "_copySystemContainersWithVolumeMountPoints:error:"
- "_copySystemPluginsForPersona:volumeMountPoints:error:"
- "_copySystemPluginsWithPlists:volumeMountPoints:error:"
- "_copyUserAppsForPersona:dataSeparatedBundleIDs:volumeMountPoints:error:"
- "_dataForKey:"
- "_dictionaryForKey:"
- "_isContainerizedAppDomain:"
- "_persistDisabledDomainNames:forPersona:"
- "_plist"
- "_protected"
- "_reconcileBooksAndHealthInDisabledDomainsList:"
- "_setBool:forKey:"
- "_setData:forKey:"
- "_setDictionary:forKey:"
- "_settingsContext"
- "_stringForLockdownKey:"
- "_subdomainNamesForAppDomainNames:"
- "_syncDisabledDomainsWithAllInstalledAppDomains:persona:"
- "_systemDataContainersByID"
- "_systemSharedContainersByID"
- "_volumeMountPointForPlist"
- "accountClass"
- "addAppleID:DSID:altDSID:dataClass:"
- "addAppleIDsFromSet:dataClass:"
- "addAssetDescriptionForAppleID:assetDescription:"
- "addContainer:"
- "addContainersFromArray:"
- "allAppGroupContainers"
- "allApps"
- "allContainers"
- "allDisabledDomainNames"
- "allDisabledDomainNamesForPersona:"
- "allObjects"
- "allPlugins"
- "allRestrictedDomainNames"
- "allRestrictedDomainNamesForPersona:"
- "allSystemContainers"
- "altDSID mismatch: existingAltDSID:%!@(MISSING) != altDSID:%!@(MISSING)"
- "altDSID mismatch: existingAltDSID:%!@(MISSING) != altDSID:%!@(MISSING)"
- "altDsid"
- "app"
- "appManager"
- "appManagerWithSettingsContext:"
- "appWithBundleID:"
- "appWithIdentifier:"
- "appWithPropertyList:"
- "appleID:%!@(MISSING), nil DSID&altDSID, dataClass:%!@(MISSING)"
- "appleID:%!@(MISSING), nil DSID&altDSID, dataClass:%!@(MISSING)"
- "assets"
- "buddyStashData"
- "bundleDir"
- "bundleVersion"
- "containerDir"
- "containerTypeString"
- "containerWithIdentifier:"
- "containerWithPropertyList:volumeMountPoint:"
- "containers"
- "copyPreferencesValueForKey:class:"
- "copyWithVolumeMountPoint:"
- "createSafeHarborForContainer:withPersona:error:"
- "createSafeHarborForContainer:withPersona:usingIntermediateRestoreDir:error:"
- "dataClasses"
- "dataFromPropertyList:format:errorDescription:"
- "dataWithContentsOfFile:options:error:"
- "dataWithError:"
- "dataWithPropertyList:format:options:error:"
- "datePlacedInSafeHarbor"
- "defaultSubdirectoriesForMBContainerType:withNestedSubdirectories:"
- "deviceID"
- "dictionaryWithContentsOfFile:"
- "doNotBackupAppIDs"
- "dsid"
- "encrypted"
- "entitlements"
- "entitlementsRelativePath"
- "groups"
- "hasCorruptSQLiteDBs"
- "hasEncryptedManifestDB"
- "hasManifestDB"
- "initWithData:error:"
- "initWithFile:error:"
- "initWithPropertyList:volumeMountPoint:"
- "initWithSettingsContext:"
- "initWithVersion:minVersion:maxVersion:"
- "ipa"
- "isAppUpdating"
- "isDomainNameEnabled:forPersona:"
- "isPlaceholder"
- "isProtected"
- "isSafeHarbor"
- "isSystemContainer"
- "isSystemSharedContainer"
- "keybagData"
- "loadAppsWithPersona:safeHarbors:dataSeparatedBundleIDs:error:"
- "loadAppsWithPersona:safeHarbors:error:"
- "lockdownKeys"
- "manifestEncryptionKey"
- "mobileInstallation"
- "moveAppDataToSafeHarborForContainer:withPersona:usingIntermediateRestoreDir:withError:"
- "moveAppDataToSafeHarborForContainer:withPersona:withError:"
- "mutableCopyWithZone:"
- "names"
- "nil appleID, DSID:%!@(MISSING), altDSID:%!@(MISSING), dataClass:%!@(MISSING)"
- "nil appleID, DSID:%!@(MISSING), altDSID:%!@(MISSING), dataClass:%!@(MISSING)"
- "ownerBundleID"
- "passcodeSet"
- "plugins"
- "properties"
- "propertiesWithFile:error:"
- "propertyList"
- "propertyListForBackupProperties"
- "propertyListForSafeHarborInfo"
- "propertyListFromData:mutabilityOption:format:errorDescription:"
- "protected"
- "q24@?0@\"NSString\"8@\"NSString\"16"
- "removeAllContainers"
- "removeAllDisabledDomainNamesForPersona:"
- "removeObject:"
- "removeOldSafeHarbors"
- "removeSafeHarborWithIdentifier:type:error:"
- "removeStaleStateForUninstalledAppsForPersona:"
- "restoreDomain:deviceUUID:commitID:intoPath:error:"
- "safeHarbor"
- "safeHarborDir"
- "safeHarborExpiration"
- "safeHarborWithPath:"
- "safeHarborsWithError:"
- "serialNumber"
- "set"
- "setAccountClass:"
- "setBuddyStashData:"
- "setBundleDir:"
- "setContainerDir:"
- "setDatePlacedInSafeHarbor:"
- "setEnabled:forDomainName:persona:"
- "setEncrypted:"
- "setKeybagData:"
- "setLockdownKeys:"
- "setManifestEncryptionKey:"
- "setObject:forKey:"
- "setPasscodeSet:"
- "setProtected:"
- "setSystemDomainsVersion:"
- "systemContainerWithDomainName:containerDir:isShared:"
- "systemContainersWithError:"
- "systemDataContainerWithIdentifier:"
- "systemDomainsVersion"
- "systemPluginsForPersona:error:"
- "systemSharedContainerWithIdentifier:"
- "systemSharedContainersWithError:"
- "uninstalledContainerWithDomainName:volumeMountPoint:"
- "unionSet:"
- "userAppWithBundleID:placeholder:persona:error:"
- "userAppsForPersona:dataSeparatedBundleIDs:error:"
- "v36@0:8B16@20@28"
- "wasPasscodeSet"
- "writeToFile:atomically:"
- "writeToFile:error:"
- "writeToFile:options:error:"
- "zip"

```
