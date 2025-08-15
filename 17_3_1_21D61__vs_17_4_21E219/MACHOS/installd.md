## installd

> `/usr/libexec/installd`

```diff

-1270.80.2.0.0
-  __TEXT.__text: 0x4cd6c
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_stubs: 0x6d00
-  __TEXT.__objc_methlist: 0x2554
+1270.102.7.0.0
+  __TEXT.__text: 0x500e8
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_stubs: 0x72e0
+  __TEXT.__objc_methlist: 0x25ac
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x2430
-  __TEXT.__objc_methname: 0x9da3
-  __TEXT.__cstring: 0x115c4
+  __TEXT.__gcc_except_tab: 0x25d4
+  __TEXT.__objc_methname: 0xa283
+  __TEXT.__cstring: 0x130c1
   __TEXT.__objc_classname: 0x526
-  __TEXT.__objc_methtype: 0x1720
+  __TEXT.__objc_methtype: 0x1778
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x111e
-  __TEXT.__unwind_info: 0xe00
-  __DATA_CONST.__auth_got: 0x8d8
-  __DATA_CONST.__got: 0x168
+  __TEXT.__unwind_info: 0xe48
+  __DATA_CONST.__auth_got: 0x8f0
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__cfstring: 0x7f20
+  __DATA_CONST.__const: 0xe18
+  __DATA_CONST.__cfstring: 0x8880
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x520
-  __DATA_CONST.__objc_dictobj: 0xcd0
-  __DATA.__objc_const: 0x5a18
-  __DATA.__objc_selrefs: 0x1ec0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x310
-  __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x25c
+  __DATA_CONST.__objc_arraydata: 0x510
+  __DATA_CONST.__objc_dictobj: 0xca8
+  __DATA.__objc_const: 0x5a98
+  __DATA.__objc_selrefs: 0x2040
+  __DATA.__objc_ivar: 0x260
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x5f8
   __DATA.__bss: 0x178

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A882CC5-C8C3-3A70-846C-9E3FA784BB08
-  Functions: 1118
-  Symbols:   404
-  CStrings:  4059
+  UUID: 6E48B209-472E-3530-B211-A4CF4507B717
+  Functions: 1145
+  Symbols:   407
+  CStrings:  4277
 
Symbols:
+ _MIDistributorTypeIsThirdParty
+ _MIMachOFileIterateImageVersions
+ _OBJC_CLASS_$_MIStoreMetadata
+ _os_eligibility_get_domain_answer
- _kCFBundleIdentifierKey
CStrings:
+ "\x12\x15"
+ " %@"
+ "\"%@\" is not built for the ARM64e architecture. The ARM64e architecture is required for all components of a browser app."
+ "%@ has both the \"%@\" entitlement and the \"%@\" entitlement. Only one of these entitlements may be present at a time. Remove one of these entitlements to allow this app to be installed."
+ "%@ has the \"%@\" entitlement but must also have the \"%@\" entitlement."
+ "%@ has the \"%@\" entitlement so it may not also have the \"%@\" entitlement. Remove one of these entitlements to allow this app to be installed."
+ "%@ has the \"%@\" entitlement, but it does not have the \"%@\" entitlement. The \"%@\" entitlement is only available to apps with the \"%@\" entitlement."
+ "%@ is not allowed to be deleted"
+ "%@ patch supplied but install target type was placeholder or downgrade. This doesn't make sense."
+ "-[MIClientConnection setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:]"
+ "-[MIClientConnection updateiTunesMetadataForIXWithIdentifier:metadata:completion:]"
+ "-[MIInstallableBundle _checkEligibilityForEntitlements:withError:]"
+ "-[MIInstallableBundle _getMarketplaceEligibilityForWebDistribution:isMarketplace:operationType:isEligible:ineligibilityReason:error:]"
+ "-[MIInstallableBundle _performBrowserAppValidationForEntitlements:error:]"
+ "-[MIInstallableBundle _performBrowserAppValidationForEntitlements:error:]_block_invoke"
+ "-[MIInstallableBundle _setLaunchWarningDataWithError:]"
+ "-[MIInstallableBundle _validateiTunesMetadataWithError:]"
+ "-[MIInstallableBundle _writeData:toFile:inContainerAtURL:legacyErrorString:error:]"
+ "-[MIInstallableBundle _writeOptionsDataToBundle:orContainer:error:]"
+ "-[MIInstallableBundlePatch initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:error:]"
+ "Answer source was forced"
+ "App identity was nil or the wrong type for request to set launch warning"
+ "ApplicationSINFDataType"
+ "B16@?0@\"NSURL\"8"
+ "B28@?0i8i12I16I20I24"
+ "B56@0:8@16@24@32@40^@48"
+ "B56@0:8B16B20Q24^B32^@40^@48"
+ "Checking eligibility for initial install of %s %@"
+ "Checking eligibility for initial install of browser engine host app %@"
+ "Checking eligibility for initial install of embedded web engine app %@"
+ "Checking eligibility for initial install of web-distributed app %@"
+ "Checking eligibility for restore of %s %@"
+ "Checking eligibility for restore of browser engine host app %@"
+ "Checking eligibility for restore of embedded web engine app %@"
+ "Checking eligibility for restore of web-distributed app %@"
+ "Checking eligibility for update of %s %@"
+ "Checking eligibility for update of browser engine host app %@"
+ "Checking eligibility for update of embedded web engine app %@"
+ "Checking eligibility for update of web-distributed app %@"
+ "Clearing launch warning for %@"
+ "DataProtectionClass"
+ "Eligibility check for domain %llu returned ineligible value %llu, source %llu, status %@, context %@"
+ "Existing installed placeholder %@ did not have the application-identifier entitlement."
+ "Failed to check eligibility for browser engine app %@"
+ "Failed to check marketplace eligibility for %@"
+ "Failed to get app bundle in bundle container for %@"
+ "Failed to get installation identity for %@"
+ "Failed to locate app bundle in container for %@"
+ "Failed to read existing iTunesMetadata from %@ : %@"
+ "Failed to read iTunesMetadata from %@ : %@"
+ "Failed to revert Sinf data type to %u: %@"
+ "Failed to set new Sinf data type to %u: %@"
+ "Failed to write data to %@"
+ "Forcing SINF data type to ALD for non-Apple distributed app %@"
+ "Install Successful for (%@:%@) [Distributor: %@]; Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs; Overall: %.2fs"
+ "Install of \"%@\" type %@ (LSInstallType = %lu, Domain: %@) requested by %@"
+ "Installed app with identity %@ does not have supplied unique install identifier %@ (found %@)"
+ "LSApplicationLaunchProhibited"
+ "NULL os_eligibility status object"
+ "OS_ELIGIBILITY_INPUT_COUNTRY_BILLING"
+ "OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION"
+ "OS_ELIGIBILITY_INPUT_DEVICE_CLASS"
+ "Offloading is not allowed for the marketplace \"%@\"."
+ "Parameter validation failed: bundleIdentifier parameter was not a string"
+ "Parameter validation failed: metadata parameter was not MIStoreMetadata instance"
+ "SetLaunchWarning"
+ "Setting launch warning for %@"
+ "T@\"MIInstallOptions\",R,N,V_options"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_installedDistributorID"
+ "Test flag set to force marketplace eligibility to eligible"
+ "Test flag set to force marketplace eligibility to not eligible"
+ "The %@ at \"%@\" has the %@\" entitlement, which is only allowed on the app itself."
+ "The %@ at \"%@\" has the %@\" entitlement, which is only allowed on the browser app itself."
+ "The %@ at \"%@\" has the entitlement \"%@\", which is only allowed on app extensions targeting the extension point \"%@\"."
+ "The DriverKit extension at \"%@\" has the \"%@\" entitlement, which is not allowed on a DriverKit extension."
+ "The XPCService extension at \"%@\" has the \"%@\" entitlement, which is not allowed on an XPCService."
+ "The app being installed, \"%@\", is distributed by \"%@\" but its existing installation is distributed by \"%@\". An app cannot change its distribution source once installed, except to/from TestFlight. Uninstall this app, then try installing it again."
+ "The app being installed, \"%@\", is distributed by \"%@\" but its existing installation is distributed by \"%@\". An app cannot change its third party distribution source once installed. Uninstall this app, then try installing it again."
+ "The app being installed, \"%@\", is distributed by Apple (distributor ID \"%@\") but its existing installation is distributed by a third party (distributor ID \"%@\"). An app cannot change its distribution source from a third party to Apple once installed. Uninstall this app, then try installing it again."
+ "The app being installed, \"%@\", is distributed by a third party (distributor ID \"%@\") but its existing installation is distributed by Apple (distributor ID \"%@\"). An app cannot change its distribution source from Apple to a third party once installed. Uninstall this app, then try installing it again."
+ "The app extension at \"%@\" has the \"%@\" entitlement, which is not allowed on an app extension."
+ "The app extension at \"%@\" targets the extension point \"%@\", which is not allowed in a non-browser app. Either add the entitlement \"%@\" to the containing app, or remove this app extension."
+ "The marketplace \"%@\" has the key \"%@\" = TRUE in its Info.plist. This is not allowed."
+ "The marketplace \"%@\" may not be installed by the distributor ID \"%@\"."
+ "This device is not eligible based on the country or region it is located in and the country or region of the Apple ID signed in."
+ "This device is not eligible based on the country or region it is located in and without an Apple ID signed in."
+ "This device is not eligible based on the country or region it is located in."
+ "This device is not eligible based on the country or region of the Apple ID signed in."
+ "This device is not eligible to %s the app \"%@\" distributed by \"%@\".%@"
+ "This device is not eligible to %s the browser engine app \"%@\".%@"
+ "This device is not eligible to %s the marketplace \"%@\".%@"
+ "This device is not eligible without an Apple ID signed in."
+ "This device type is not eligible."
+ "Unexpectedly missing bundle signing information"
+ "Unique install identifier was nil or the wrong type for request to set launch warning for %@"
+ "Unknown ineligibility reason for source %llu status %@"
+ "Unknown os_eligibility_answer_source_t value %llu."
+ "Unknown validation operation %lu for %@"
+ "Unknown validation operation for %@"
+ "Update iTunesMetadata requested by client %@ for identifier %@"
+ "Validating %@ distributed by %@"
+ "Warning data was of the wrong type for request to set launch warning for %@"
+ "Wrote %ld bytes of data from options to %@"
+ "_IneligibilityReasonStringForSourceAndStatus"
+ "_ValidateBundleDoesNotHaveBrowserAppEntitlements"
+ "_ValidateBundleDoesNotHaveBrowserExtensionEntitlements"
+ "_checkEligibilityForEntitlements:withError:"
+ "_getMarketplaceEligibilityForWebDistribution:isMarketplace:operationType:isEligible:ineligibilityReason:error:"
+ "_installedDistributorID"
+ "_performBrowserAppValidationForEntitlements:error:"
+ "_setLaunchWarningDataWithError:"
+ "_validateiTunesMetadataWithError:"
+ "_writeData:toFile:inContainerAtURL:legacyErrorString:error:"
+ "allowDeletableSystemApps"
+ "alternateIconName"
+ "autoInstallOverride"
+ "bundleTypeDescription"
+ "captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:"
+ "com.apple.developer.browser.app-installation"
+ "com.apple.developer.cs.allow-jit"
+ "com.apple.developer.default-data-protection"
+ "com.apple.developer.default-data-protection-if-available"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.marketplace.app-installation"
+ "com.apple.developer.memory.transfer-accept"
+ "com.apple.developer.memory.transfer-send"
+ "com.apple.developer.web-browser"
+ "com.apple.developer.web-browser-engine.host"
+ "com.apple.developer.web-browser-engine.networking"
+ "com.apple.developer.web-browser-engine.rendering"
+ "com.apple.developer.web-browser-engine.webcontent"
+ "com.apple.web-browser-engine.content"
+ "com.apple.web-browser-engine.networking"
+ "com.apple.web-browser-engine.rendering"
+ "data-protection-class"
+ "dictionaryRepresentation"
+ "displayName"
+ "distributorID"
+ "distributorInfo"
+ "distributorIsFirstPartyApple"
+ "distributorNameForCurrentLocale"
+ "distributorType"
+ "eligibilityOperationType"
+ "enumerateDylibsWithBlock:"
+ "executableExistsWithError:"
+ "geoJSONData"
+ "getSinfDataType:withError:"
+ "hasExecutableSliceForCPUType:subtype:error:"
+ "iTunesArtworkData"
+ "iTunesMetadataWithError:"
+ "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:error:"
+ "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:existingBundleContainer:error:"
+ "initWithBundle:inStagingRoot:packageFormat:identity:domain:installOptions:manifestURL:existingBundleContainer:patchType:error:"
+ "install"
+ "installIntent"
+ "installTypeSummaryString"
+ "installedDistributorID"
+ "isDeveloperInstall"
+ "isLaunchProhibited"
+ "isSystemAppInstall"
+ "launchWarningData"
+ "marketplace"
+ "marketplace-distributed app"
+ "os_eligibility status was nil or not a dictionary; found: %@"
+ "os_eligibility_get_domain_answer failed"
+ "preservePlaceholderAsParallel"
+ "provisioningProfileInstallFailureIsFatal"
+ "provisioningProfiles"
+ "relativePath"
+ "restore"
+ "setDistributorInfo:"
+ "setInstalledDistributorID:"
+ "setLaunchWarningData:withError:"
+ "setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:"
+ "setSinfDataType:"
+ "setSinfDataType:withError:"
+ "sinfData"
+ "sinfDataType"
+ "stashMode"
+ "systemAppPlaceholderBundleIDs"
+ "targetsBrowserExtensionPoint"
+ "uniqueInstallID"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "update"
+ "updateAndValidateSinf:error:"
+ "updateiTunesMetadataForIXWithIdentifier:metadata:completion:"
+ "v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"MIInstallOptions\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
+ "v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40"
+ "validateHasCorrespondingEntitlements:error:"
+ "writeiTunesMetadata:error:"
- "\x12\x14"
- "%@ patch supplied with kPackageTypeKey = kPackageTypePlaceholder. This doesn't make sense."
- "-[MIClientConnection _updateSinfWithIdentifier:withOptions:sinfData:methodName:entitlement:completion:]"
- "-[MIClientConnection _updateiTunesMetadataWithIdentifier:options:plistData:methodName:entitlement:completion:]"
- "-[MIClientConnection updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:]"
- "-[MIInstallableBundle _writeOptionsDataToBundle:orContainer:error:]_block_invoke"
- "-[MIInstallableBundlePatch initWithBundle:inStagingRoot:packageFormat:identity:domain:userOptions:manifestURL:existingBundleContainer:patchType:error:]"
- "AllowInstallLocalProvisioned"
- "AlternateIconName"
- "ApplicationSINF"
- "AutoInstallWatchApp"
- "Customer"
- "Developer"
- "DowngradeToPlaceholder"
- "Failed to deserialize iTunesMetadata to dictionary"
- "Failed to write %@ data to %@ : %@"
- "File"
- "Install Successful for (%@:%@); Staging: %.2fs; Waiting: %.2fs; Preflight/Patch: %.2fs, Verifying: %.2fs; Overall: %.2fs"
- "Install of \"%@\" type %@ (LSInstallType = %@, Domain: %@) requested by %@"
- "InvalidiTunesMetadataPlist"
- "LSInstallType"
- "PackageType"
- "PreservePlaceholderAsParallel"
- "ProvisioningProfileInstallFailureIsFatal"
- "SkipWatchAppInstall"
- "StashMode"
- "System"
- "T@\"NSDictionary\",R,N,V_userOptions"
- "Unable to deserialize iTunesMetadata.plist data"
- "Update iTunesMetadata requested by client %@ for identifier %@ with options %@"
- "Wrote %ld bytes of data from options key %@ to %@"
- "_updateSinfWithIdentifier:withOptions:sinfData:methodName:entitlement:completion:"
- "_updateiTunesMetadataWithIdentifier:options:plistData:methodName:entitlement:completion:"
- "_userOptions"
- "captureStoreDataFromDirectory:doCopy:failureIsFatal:withError:"
- "iTunesMetadataCaptureFailed"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:userOptions:error:"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:userOptions:existingBundleContainer:error:"
- "initWithBundle:inStagingRoot:packageFormat:identity:domain:userOptions:manifestURL:existingBundleContainer:patchType:error:"
- "initWithLegacyOptionsDictionary:"
- "kInstallOptionDowngradeToPlaceholder doesn't make sense if the value of kPackageTypeKey is not kPackageTypePlaceholder (was %@)"
- "legacyOptionsDictionary"
- "updateSinfDataForAppWithIdentifier:sinfData:error:"
- "updateiTunesMetadataForAppWithIdentifier:plistData:error:"
- "updateiTunesMetadataForIXWithIdentifier:options:plistData:completion:"
- "userOptions"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"NSError\">40"
- "v64@0:8@16@24@32r*40@48@?56"

```
