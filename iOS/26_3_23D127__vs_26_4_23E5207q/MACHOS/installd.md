## installd

> `/usr/libexec/installd`

```diff

-1513.80.6.0.0
-  __TEXT.__text: 0x5a264
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x7e40
-  __TEXT.__objc_methlist: 0x3164
+1513.100.80.0.0
+  __TEXT.__text: 0x60dec
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__objc_methlist: 0x335c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x15651
-  __TEXT.__objc_classname: 0x5e3
-  __TEXT.__objc_methname: 0xb77c
-  __TEXT.__objc_methtype: 0x1f44
-  __TEXT.__gcc_except_tab: 0x3150
+  __TEXT.__cstring: 0x166dc
+  __TEXT.__objc_classname: 0x613
+  __TEXT.__objc_methtype: 0x1fe2
+  __TEXT.__objc_methname: 0xbfd7
+  __TEXT.__gcc_except_tab: 0x33a0
   __TEXT.__oslogstring: 0x11ac
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0xfc8
-  __DATA_CONST.__auth_got: 0x800
+  __TEXT.__unwind_info: 0x1208
+  __DATA_CONST.__auth_got: 0x7d0
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x10b0
-  __DATA_CONST.__cfstring: 0x9860
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__const: 0x1248
+  __DATA_CONST.__cfstring: 0x9c60
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x5d0
-  __DATA_CONST.__objc_dictobj: 0xe88
-  __DATA.__objc_const: 0x5b20
-  __DATA.__objc_selrefs: 0x2418
-  __DATA.__objc_ivar: 0x290
-  __DATA.__objc_data: 0xc30
+  __DATA_CONST.__objc_arraydata: 0x5f0
+  __DATA_CONST.__objc_dictobj: 0xed8
+  __DATA.__objc_const: 0x5e10
+  __DATA.__objc_selrefs: 0x2530
+  __DATA.__objc_ivar: 0x2a8
+  __DATA.__objc_data: 0xcd0
   __DATA.__data: 0xa18
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a8
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12C25BBD-7F50-30E5-9BC7-B92425647F16
-  Functions: 1226
-  Symbols:   377
-  CStrings:  4748
+  UUID: 3B878DB3-81D3-3528-AFFD-F23F27C82907
+  Functions: 1290
+  Symbols:   371
+  CStrings:  4885
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "%@ was not a valid dictionary"
+ "+[MIPreInstallConsentManager fetchAppListWithError:]"
+ "-[MIClientConnection fetchListOfAppsRequiringPreInstallConsent:]"
+ "-[MIClientConnection registerContentsOnRoot:deferUntilNextBoot:completion:]"
+ "-[MIClientConnection storeListOfAppsRequiringPreInstallConsent:completion:]"
+ "-[MIClientConnection unregisterContentsOnRoot:deferUntilNextBoot:completion:]"
+ "-[MILaunchServicesOperationManager _onQueue_registerApplicationInfo:onMountPoint:forAppBundleID:domain:personas:registrationType:resultingRecordPromise:error:]"
+ "-[MILaunchServicesOperationManager _onQueue_registerApplicationInfo:onMountPoint:forAppBundleID:domain:personas:registrationType:resultingRecordPromise:error:]_block_invoke"
+ "-[MILaunchServicesOperationManager _onQueue_unregisterAppForBundleID:domain:operationType:precondition:unregisterOpType:bundleURL:error:]_block_invoke"
+ "-[MILaunchServicesOperationManager _unregisterBundleOnRootAtURL:operationType:error:]_block_invoke"
+ "-[MIRootContentManager _initializeFromStorageWithError:]"
+ "-[MIRootContentManager _onQueue_invalidateDeferredBundles]"
+ "-[MIRootContentManager _onQueue_registerBundlesOnRoot:deferUntilNextBoot:completion:]"
+ "-[MIRootContentManager _onQueue_registerBundlesOnRoot:deferUntilNextBoot:completion:]_block_invoke"
+ "-[MIRootContentManager _onQueue_saveBundleOperations]"
+ "-[MIRootContentManager _onQueue_unregisterBundlesOnRoot:deferUntilNextBoot:completion:]"
+ "-[MIRootContentManager _onQueue_unregisterBundlesOnRoot:deferUntilNextBoot:completion:]_block_invoke"
+ "-[MIRootContentManager reconcileBundlesOnRootWithCompletion:]_block_invoke"
+ "-[MIRootContentManager reconcileBundlesOnRootWithCompletion:]_block_invoke_2"
+ "-[MIRootContentManager reconcileBundlesOnRoot]_block_invoke"
+ "@\"MILaunchServicesOperationManager\""
+ "@\"NSError\"32@?0@\"NSURL\"8@\"NSMutableDictionary\"16@?<v@?@\"MIExecutableBundle\"@\"NSString\">24"
+ "@40@0:8@16@24@?32"
+ "B68@0:8@16Q24I32@36Q44@52^@60"
+ "B80@0:8@16@24@32Q40@48Q56^@64^@72"
+ "Bundle URL is required for builtin app unregistration"
+ "BundleIDList"
+ "Deferring registration of bundles %@ until next boot"
+ "Deferring unregistration of bundles %@ until next boot"
+ "Expected valid LS operation type, instead found %ld"
+ "Failed to determine bundle identifier for bundle at %@"
+ "Failed to read pending operations cache at %@: %@"
+ "Failed to reconcile bundles on root, registerError: %@ unregisterError: %@"
+ "Failed to register bundles %@ with LS: %@"
+ "Failed to remove saved list of app bundles on root at %@: %@"
+ "Failed to unregister bundles %@ with LS: %@"
+ "Failed to write bundle paths to %@ : %@"
+ "Fetch list of apps requiring pre-install consent requested by client %@"
+ "FetchListOfAppsRequiringPreInstallConsent"
+ "Found invalid deferred operation type %ld for bundle at %@; skipping"
+ "LS failed to refresh standalone extension points: %@"
+ "LS failed to register item %@: %@"
+ "LS failed to unregister app at %@: %@"
+ "LS registered item %@"
+ "LS successfully refreshed standalone extension points"
+ "LS unregistered app at %@"
+ "List of bundle paths to register was not a set."
+ "List of bundle paths to unregister was not a set."
+ "MIConstructAppEntryForBundleAtURL"
+ "MIPreInstallConsentManager"
+ "MIRootContentManager"
+ "PendingRootOperations.plist"
+ "PreInstallConsentSet.plist"
+ "Process %@ tried to register contents on a root, but that operation can only be done by InstallCoordination."
+ "Registering contents on a darwinup root is not available on this build"
+ "Storage plist at %@ did not contain key %@ or its value was not an array of strings; found: %@"
+ "Store list of apps requiring pre-install consent requested by client %@"
+ "StoreListOfAppsRequiringPreInstallConsent"
+ "T@\"MILaunchServicesOperationManager\",R,N,V_lsOperationManager"
+ "T@\"NSMutableDictionary\",&,N,V_bundleOperationsMap"
+ "T@\"NSURL\",R,N,V_appBundleListCacheURL"
+ "T@?,R,C,N,V_bundleEntryConstructor"
+ "The Watch app contained within this app defines both %@ and %@ keys in its Info.plist and/or its WatchKit extension's Info.plist. Having both defined is ambiguous. Please remove one of these keys."
+ "The Watch app contained within this app has an incorrect value, \"%@\", for the WKCompanionAppBundleIdentifier key in the Watch app's Info.plist. Please set the WKCompanionAppBundleIdentifier key in the Watch app's Info.plist to the companion app's bundle identifier, \"%@\"."
+ "The Watch app contained within this app specifies WKWatchOnly = TRUE in its Info.plist. Watch-only apps cannot have a companion counterpart, so they cannot be contained within a companion app. Please either remove the WKWatchOnly key from the Watch app's Info.plist, or create a new Watch-only app."
+ "The Watch app within this app must specify the key WKCompanionAppBundleIdentifier in its Info.plist to indicate the identify of its companion counterpart. However, the value of the WKCompanionAppBundleIdentifier key in its Info.plist is missing or malformed. Please set WKCompanionAppBundleIdentifier in the Watch app's Info.plist to this app's bundle identifier, \"%@\"."
+ "The watch app contained within this app specifies a bundle identifier that does not start with this app's bundle identifier followed by a dot ('.') character. Please update the Watch app's bundle identifier (currently set to \"%@\") to begin with the prefix \"%@\"."
+ "Unregistering contents on a darwinup root is not available on this build"
+ "_appBundleListCacheURL"
+ "_bundleEntryConstructor"
+ "_bundleOperationsMap"
+ "_cacheURL"
+ "_initializeFromStorageWithError:"
+ "_lsOperationManager"
+ "_onQueue_constructAppEntriesForBundles:error:"
+ "_onQueue_invalidateDeferredBundles"
+ "_onQueue_registerApplicationInfo:onMountPoint:forAppBundleID:domain:personas:registrationType:resultingRecordPromise:error:"
+ "_onQueue_registerBundlesOnRoot:deferUntilNextBoot:completion:"
+ "_onQueue_saveBundleOperations"
+ "_onQueue_unregisterAppForBundleID:domain:operationType:precondition:unregisterOpType:bundleURL:error:"
+ "_onQueue_unregisterBundlesOnRoot:deferUntilNextBoot:completion:"
+ "_onQueue_updateBundleOperationsMapWithBundles:forOperationType:"
+ "_registerBundleOnRootUsingInstalledInfo:operationType:error:"
+ "_unregisterBundleOnRootAtURL:operationType:error:"
+ "appBundleListCacheURL"
+ "appex"
+ "bundleEntryConstructor"
+ "bundleIDSet did not contain valid strings"
+ "bundleIDSet parameter was not a valid set"
+ "bundleOperationsMap"
+ "com.apple.MobileInstallation.MIRootContentManager.internal"
+ "com.apple.MobileInstallation.MIRootContentManager.lsregister"
+ "fetchAppListWithError:"
+ "fetchListOfAppsRequiringPreInstallConsent:"
+ "initForTestingWithCacheURL:lsOperationManager:bundleEntryConstructor:"
+ "initWithCacheURL:lsOperationManager:bundleEntryConstructor:"
+ "installationDenylist"
+ "lsOperationManager"
+ "reconcileBundlesOnRoot"
+ "reconcileBundlesOnRootWithCompletion:"
+ "refreshStandaloneExtensionPointsWithError:"
+ "refreshUnbundledSystemExtensionPointsWithOperationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:"
+ "registerBundleOnRootUsingInstalledInfo:error:"
+ "registerBundlesOnRoot:deferUntilNextBoot:completion:"
+ "registerContentsOnRoot:deferUntilNextBoot:completion:"
+ "registerStandaloneExtensionOnRootUsingInstalledInfo:error:"
+ "root-content-register"
+ "root-content-unregister"
+ "setBundleOperationsMap:"
+ "storeAppList:error:"
+ "storeListOfAppsRequiringPreInstallConsent:completion:"
+ "unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterBuiltinStandaloneExtensionAtURL:operationUUID:requestContext:saveObserver:error:"
+ "unregisterBundleOnRootAtURL:error:"
+ "unregisterBundlesOnRoot:deferUntilNextBoot:completion:"
+ "unregisterContentsOnRoot:deferUntilNextBoot:completion:"
+ "unregisterStandaloneExtensionOnRootAtURL:error:"
+ "v24@?0@\"MIExecutableBundle\"8@\"NSString\"16"
+ "v24@?0@\"NSError\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"
- "%@: Missing WKCompanionAppBundleIdentifier key in WatchKit %@ app's Info.plist"
- "-[MIDiskImageManager _onQueue_scanApps:returnMapInfo:error:]_block_invoke"
- "-[MILaunchServicesOperationManager _onQueue_registerApplicationInfo:onMountPoint:forAppBundleID:domain:personas:error:]"
- "-[MILaunchServicesOperationManager _onQueue_unregisterAppForBundleID:domain:operationType:precondition:error:]"
- "Failed to create MIExecutableBundle instance for %@ : %@"
- "Failed to get entry for bundle %@ : %@"
- "Failed to scan app extensions in %@ : %@"
- "Invalid value of WKCompanionAppBundleIdentifier key in WatchKit %@ app's Info.plist: %@ (expected %@)"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
- "This app defines both %@ and %@ in its Info.plist and/or its WatchKit extension's Info.plist. Having both defined is not allowed."
- "Watch-only apps cannot be contained in companion apps installed on the companion."
- "WatchKit %@ app's bundle ID %@ is not prefixed by the parent app's bundle ID followed by a '.'; expected prefix %@"
- "_onQueue_registerApplicationInfo:onMountPoint:forAppBundleID:domain:personas:error:"
- "_onQueue_unregisterAppForBundleID:domain:operationType:precondition:error:"
- "installationBlacklist"
- "setInternalQueue:"
- "twoStageAppInstallEnabled"
- "v24@?0@\"NSString\"8@\"ICLBundleRecord\"16"

```
