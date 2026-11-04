## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2465.1.9.0.0
-  __TEXT.__text: 0x1795bc
-  __TEXT.__objc_methlist: 0x147d8
-  __TEXT.__const: 0xf08
-  __TEXT.__cstring: 0x2bedd
-  __TEXT.__gcc_except_tab: 0x9718
-  __TEXT.__oslogstring: 0xbfee
+2465.2.7.101.0
+  __TEXT.__text: 0x17aee4
+  __TEXT.__objc_methlist: 0x148d8
+  __TEXT.__const: 0xf38
+  __TEXT.__cstring: 0x2bf4b
+  __TEXT.__gcc_except_tab: 0x9758
+  __TEXT.__oslogstring: 0xc1b5
   __TEXT.__ustring: 0x218e
   __TEXT.__dlopen_cstrs: 0x4c4
   __TEXT.__constg_swiftt: 0x1bc

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7298
+  __TEXT.__unwind_info: 0x7310
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6718
-  __DATA_CONST.__objc_classlist: 0xab8
+  __DATA_CONST.__const: 0x67b8
+  __DATA_CONST.__objc_classlist: 0xac0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa620
+  __DATA_CONST.__objc_selrefs: 0xa6c8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x748
+  __DATA_CONST.__objc_superrefs: 0x750
   __DATA_CONST.__objc_arraydata: 0x11290
-  __DATA_CONST.__got: 0xe78
-  __AUTH_CONST.__const: 0x2430
-  __AUTH_CONST.__cfstring: 0x2e140
-  __AUTH_CONST.__objc_const: 0x20120
+  __DATA_CONST.__got: 0xe88
+  __AUTH_CONST.__const: 0x2450
+  __AUTH_CONST.__cfstring: 0x2e160
+  __AUTH_CONST.__objc_const: 0x20370
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3ae0
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1160
-  __AUTH.__objc_data: 0x57a8
+  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH.__objc_data: 0x57f8
   __AUTH.__data: 0x3a0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x146c
+  __DATA.__objc_ivar: 0x1498
   __DATA.__data: 0x1c60
   __DATA_DIRTY.__objc_data: 0x1388
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8959
-  Symbols:   14692
-  CStrings:  8107
+  Functions: 8993
+  Symbols:   14753
+  CStrings:  8117
 
Symbols:
+ +[CSFileProviderContainerCache _currentOSBuild]
+ +[CSFileProviderContainerCache _decodeSnapshot:osBuild:]
+ +[CSFileProviderContainerCache _encodeSnapshot:osBuild:]
+ +[CSFileProviderContainerCache _isRetriableRefreshError:]
+ +[CSFileProviderContainerCache _retryDelayForAttempt:]
+ -[CSBundleFilterEvaluationRequest fileProviderAllowedBundleIDs]
+ -[CSBundleFilterEvaluationRequest initWithFileProviderContainerGroups:fileProviderExcludedBundleIDs:fileProviderAllowedBundleIDs:needsAppProtectionBundleIDs:needsMDMRestrictedBundleIDs:needsExcludedAppBundleIDs:attributeBackfillGroups:]
+ -[CSFileProviderContainerCache _donationRefreshDelay]
+ -[CSFileProviderContainerCache _finishRefreshWithOIDsByBundleId:error:completionHandler:]
+ -[CSFileProviderContainerCache _refreshCacheWithRetriesRemaining:]
+ -[CSFileProviderContainerCache _scheduleDonationRefreshForGeneration:]
+ -[CSFileProviderContainerCache _writePersistedSnapshotLocked]
+ -[CSFileProviderContainerCache containerVisibilityForDisabledBundleIDs:allowedBundleIDs:]
+ -[CSFileProviderContainerCache noteContainerItemIndexed]
+ -[CSFileProviderContainerCache usePersistenceDirectory:]
+ -[CSFileProviderContainerVisibility .cxx_destruct]
+ -[CSFileProviderContainerVisibility cacheRefreshed]
+ -[CSFileProviderContainerVisibility filesHidden]
+ -[CSFileProviderContainerVisibility hiddenContainerOIDs]
+ -[CSFileProviderContainerVisibility initWithCacheRefreshed:filesHidden:hiddenContainerOIDs:visibleContainerOIDs:]
+ -[CSFileProviderContainerVisibility initWithCacheRefreshed:filesHidden:hiddenContainerOIDs:visibleContainerOIDs:disabledOwnerBundleIDs:allowedOwnerBundleIDs:]
+ -[CSFileProviderContainerVisibility ownerBundleIDIsHidden:]
+ -[CSFileProviderContainerVisibility visibleContainerOIDs]
+ _CSFPAppendString
+ _CSFPReadString
+ _CSFPRemoveFile
+ _OBJC_CLASS_$_CSFileProviderContainerVisibility
+ _OBJC_IVAR_$_CSBundleFilterEvaluationRequest._fileProviderAllowedBundleIDs
+ _OBJC_IVAR_$_CSFileProviderContainerCache._donationGeneration
+ _OBJC_IVAR_$_CSFileProviderContainerCache._donationRefreshScheduled
+ _OBJC_IVAR_$_CSFileProviderContainerCache._loadedFromDisk
+ _OBJC_IVAR_$_CSFileProviderContainerCache._persistenceDirectory
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._allowedOwnerBundleIDs
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._cacheRefreshed
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._disabledOwnerBundleIDs
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._filesHidden
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._hiddenContainerOIDs
+ _OBJC_IVAR_$_CSFileProviderContainerVisibility._visibleContainerOIDs
+ _OBJC_METACLASS_$_CSFileProviderContainerVisibility
+ __OBJC_$_INSTANCE_METHODS_CSFileProviderContainerVisibility
+ __OBJC_$_INSTANCE_VARIABLES_CSFileProviderContainerVisibility
+ __OBJC_$_PROP_LIST_CSFileProviderContainerVisibility
+ __OBJC_CLASS_RO_$_CSFileProviderContainerVisibility
+ __OBJC_METACLASS_RO_$_CSFileProviderContainerVisibility
+ ___47+[CSFileProviderContainerCache _currentOSBuild]_block_invoke
+ ___66-[CSFileProviderContainerCache _refreshCacheWithRetriesRemaining:]_block_invoke
+ ___70-[CSFileProviderContainerCache _scheduleDonationRefreshForGeneration:]_block_invoke
+ ___89-[CSFileProviderContainerCache containerVisibilityForDisabledBundleIDs:allowedBundleIDs:]_block_invoke
+ ___89-[CSFileProviderContainerCache containerVisibilityForDisabledBundleIDs:allowedBundleIDs:]_block_invoke_2
+ ___89-[CSFileProviderContainerCache containerVisibilityForDisabledBundleIDs:allowedBundleIDs:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40s_e18_B16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e35_v32?0"NSString"8"NSNumber"16^B24ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8r40l8
+ __currentOSBuild.onceToken
+ __currentOSBuild.sOSBuild
+ _kPersistedFileName
+ _kPersistedTempFileName
+ _openat
+ _read
+ _renameat
+ _sysctlbyname
+ _unlinkat
+ _write
- -[CSBundleFilterEvaluationRequest initWithFileProviderContainerGroups:fileProviderExcludedBundleIDs:needsAppProtectionBundleIDs:needsMDMRestrictedBundleIDs:needsExcludedAppBundleIDs:attributeBackfillGroups:]
- -[CSFileProviderContainerCache addAppContainerOID:forBundle:fpBundle:]
- -[CSFileProviderContainerCache isFPBundleIDLocked:]
- ___block_descriptor_57_e8_32s40r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8r40l8
CStrings:
+ "B16@?0@\"NSString\"8"
+ "[ProtectedApps] Could not write the FP app container cache file, removing it"
+ "[ProtectedApps] Failed refreshing FP app container oid cache, leaving it unchanged: %@"
+ "[ProtectedApps] Giving up refreshing FP app container oid cache: %@"
+ "[ProtectedApps] Ignoring an unreadable FP app container cache file, removing it"
+ "[ProtectedApps] Loaded the FP app container cache file"
+ "[ProtectedApps] Retrying FP app container oid cache refresh in %.0fs (%lu retries left)"
+ "fileProviderAllowedBundleIDs"
+ "kern.osversion"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
```
