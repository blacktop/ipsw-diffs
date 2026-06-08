## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x25edc
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x12ac
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x4f21
-  __TEXT.__gcc_except_tab: 0xbdc
+1655.0.0.0.0
+  __TEXT.__text: 0x27564
+  __TEXT.__objc_methlist: 0x13b4
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x50d6
+  __TEXT.__gcc_except_tab: 0xc74
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0xc80
-  __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methname: 0x4412
-  __TEXT.__objc_methtype: 0x13e2
-  __TEXT.__objc_stubs: 0x2ca0
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__unwind_info: 0xd30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x29e0
-  __AUTH_CONST.__objc_const: 0x1900
+  __AUTH_CONST.__cfstring: 0x2b00
+  __AUTH_CONST.__objc_const: 0x19f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x118
   __DATA.__data: 0x240
   __DATA.__bss: 0x60
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32D5B2C9-1F64-3A74-BBAC-E7FDFBA7C10A
-  Functions: 791
-  Symbols:   2418
-  CStrings:  1572
+  UUID: 5E97C4F2-87D9-3B49-BB29-B1CFD7060B6D
+  Functions: 845
+  Symbols:   2543
+  CStrings:  867
 
Symbols:
+ +[MIInstallerClient installerWithAppBundleRecordEnumerator:]
+ -[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]
+ -[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]
+ -[MIInstallOptions bundleDirectoryName]
+ -[MIInstallOptions preserveTargetBundleName]
+ -[MIInstallOptions setBundleDirectoryName:]
+ -[MIInstallOptions setPreserveTargetBundleName:]
+ -[MIInstallerClient addPersona:toApp:inDomain:withCompletion:]
+ -[MIInstallerClient appBundleRecordEnumBlock]
+ -[MIInstallerClient enrollPersona:forApps:inDomain:withCompletion:]
+ -[MIInstallerClient enumerateAppBundleRecord:error:]
+ -[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]
+ -[MIInstallerClient removePersona:fromApp:inDomain:withCompletion:]
+ -[MIInstallerClient reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]
+ -[MIInstallerClient setAppBundleRecordEnumBlock:]
+ -[MIInstallerClient setPersonas:forApp:inDomain:withCompletion:]
+ GCC_except_table296
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table312
+ GCC_except_table315
+ GCC_except_table321
+ GCC_except_table341
+ GCC_except_table348
+ GCC_except_table350
+ GCC_except_table356
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table377
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table385
+ GCC_except_table387
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table398
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table408
+ GCC_except_table418
+ GCC_except_table425
+ GCC_except_table438
+ GCC_except_table442
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table469
+ GCC_except_table480
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table498
+ GCC_except_table500
+ GCC_except_table502
+ _MICopyPlugInKitPersonaEntitlement
+ _MIHasCriticalAlertsEntitlement
+ _MIHasExtensionKitAnyPersonaEntitlement
+ _MIHasExtensionKitSystemPersonaEntitlement
+ _MIHasWrapperBundleEntitlement
+ _MIIsValidPersonaLifecycleEventType
+ _MIStringForPersonaLifecycleEventType
+ _MobileInstallationAddPersonaToApp
+ _MobileInstallationEnrollPersonaForApps
+ _MobileInstallationEnumerateAllInstalledItemBundleRecords
+ _MobileInstallationRemovePersonaFromApp
+ _MobileInstallationReportPersonaLifecycleEvent
+ _MobileInstallationSetPersonasForApp
+ _OBJC_IVAR_$_MIInstallOptions._bundleDirectoryName
+ _OBJC_IVAR_$_MIInstallOptions._preserveTargetBundleName
+ _OBJC_IVAR_$_MIInstallerClient._appBundleRecordEnumBlock
+ __CopySafeHarborsForContainerClass
+ ___101-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
+ ___101-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]_block_invoke_2
+ ___113-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
+ ___113-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]_block_invoke_2
+ ___52-[MIInstallerClient enumerateAppBundleRecord:error:]_block_invoke
+ ___62-[MIInstallerClient addPersona:toApp:inDomain:withCompletion:]_block_invoke
+ ___62-[MIInstallerClient addPersona:toApp:inDomain:withCompletion:]_block_invoke_2
+ ___62-[MIInstallerClient addPersona:toApp:inDomain:withCompletion:]_block_invoke_3
+ ___62-[MIInstallerClient addPersona:toApp:inDomain:withCompletion:]_block_invoke_4
+ ___64-[MIInstallerClient setPersonas:forApp:inDomain:withCompletion:]_block_invoke
+ ___64-[MIInstallerClient setPersonas:forApp:inDomain:withCompletion:]_block_invoke_2
+ ___64-[MIInstallerClient setPersonas:forApp:inDomain:withCompletion:]_block_invoke_3
+ ___64-[MIInstallerClient setPersonas:forApp:inDomain:withCompletion:]_block_invoke_4
+ ___67-[MIInstallerClient enrollPersona:forApps:inDomain:withCompletion:]_block_invoke
+ ___67-[MIInstallerClient enrollPersona:forApps:inDomain:withCompletion:]_block_invoke_2
+ ___67-[MIInstallerClient enrollPersona:forApps:inDomain:withCompletion:]_block_invoke_3
+ ___67-[MIInstallerClient enrollPersona:forApps:inDomain:withCompletion:]_block_invoke_4
+ ___67-[MIInstallerClient removePersona:fromApp:inDomain:withCompletion:]_block_invoke
+ ___67-[MIInstallerClient removePersona:fromApp:inDomain:withCompletion:]_block_invoke_2
+ ___67-[MIInstallerClient removePersona:fromApp:inDomain:withCompletion:]_block_invoke_3
+ ___67-[MIInstallerClient removePersona:fromApp:inDomain:withCompletion:]_block_invoke_4
+ ___88-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke
+ ___88-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_2
+ ___88-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_3
+ ___88-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_4
+ ___89-[MIInstallerClient reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]_block_invoke
+ ___89-[MIInstallerClient reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]_block_invoke_2
+ ___89-[MIInstallerClient reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]_block_invoke_3
+ ___89-[MIInstallerClient reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:]_block_invoke_4
+ ___MobileInstallationAddPersonaToApp_block_invoke
+ ___MobileInstallationEnrollPersonaForApps_block_invoke
+ ___MobileInstallationEnumerateAllInstalledItemBundleRecords_block_invoke
+ ___MobileInstallationRemovePersonaFromApp_block_invoke
+ ___MobileInstallationReportPersonaLifecycleEvent_block_invoke
+ ___MobileInstallationSetPersonasForApp_block_invoke
+ ____CopySafeHarborsForContainerClass_block_invoke
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addPersona:toApp:inDomain:withCompletion:
+ _objc_msgSend$appBundleRecordEnumBlock
+ _objc_msgSend$enrollPersona:forApps:inDomain:withCompletion:
+ _objc_msgSend$enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:
+ _objc_msgSend$installerWithAppBundleRecordEnumerator:
+ _objc_msgSend$removePersona:fromApp:inDomain:withCompletion:
+ _objc_msgSend$reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:
+ _objc_msgSend$setAppBundleRecordEnumBlock:
+ _objc_msgSend$setPersonas:forApp:inDomain:withCompletion:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:
+ _objc_msgSend$stagingLocationForURL:withinStagingSubsystem:usingUniqueName:completion:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
- -[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]
- -[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]
- -[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]
- GCC_except_table268
- GCC_except_table273
- GCC_except_table278
- GCC_except_table281
- GCC_except_table284
- GCC_except_table287
- GCC_except_table290
- GCC_except_table293
- GCC_except_table311
- GCC_except_table320
- GCC_except_table326
- GCC_except_table332
- GCC_except_table334
- GCC_except_table336
- GCC_except_table340
- GCC_except_table347
- GCC_except_table351
- GCC_except_table353
- GCC_except_table355
- GCC_except_table357
- GCC_except_table359
- GCC_except_table361
- GCC_except_table363
- GCC_except_table365
- GCC_except_table368
- GCC_except_table372
- GCC_except_table374
- GCC_except_table376
- GCC_except_table378
- GCC_except_table380
- GCC_except_table382
- GCC_except_table384
- GCC_except_table386
- GCC_except_table388
- GCC_except_table390
- GCC_except_table424
- GCC_except_table428
- GCC_except_table430
- GCC_except_table437
- GCC_except_table450
- GCC_except_table458
- ___100-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke
- ___100-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke_2
- ___112-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke
- ___112-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke_2
- ___66-[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]_block_invoke
- ___66-[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]_block_invoke_2
- ___66-[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]_block_invoke_3
- ___66-[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]_block_invoke_4
- ___MobileInstallationCopySafeHarborsForContainerClass_block_invoke
- _objc_msgSend$enumerateInstalledAppsWithOptions:completion:
- _objc_msgSend$primaryPersonaString
- _objc_msgSend$stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:
- _objc_msgSend$stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:
CStrings:
+ "-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]_block_invoke"
+ "-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_3"
+ "Construction"
+ "Destruction"
+ "Invalid MIPersonaLifecycleEventType %@ when reporting persona lifecycle event"
+ "MIIsValidPersonaLifecycleEventType"
+ "Unknown: %ld"
+ "_CopySafeHarborsForContainerClass"
+ "_CopySafeHarborsForContainerClass_block_invoke"
+ "com.apple.developer.usernotifications.critical-alerts"
+ "com.apple.developer.wrapper-bundle"
+ "com.apple.private.extensionkit.builtinanypersona"
+ "com.apple.private.extensionkit.builtinsystempersona"
+ "com.apple.private.pluginkit.persona"
+ "\xf7"
- "-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke"
- "-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke"
- "-[MIInstallerClient enumerateInstalledAppsWithOptions:completion:]_block_invoke_3"
- ".cxx_destruct"
- "@\"MIAppIdentity\""
- "@\"MIPlaceholderConstructor\""
- "@\"MIStoreMetadata\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@?16@?24"
- "@32@0:8Q16^@24"
- "@36@0:8@16B24^@28"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24Q32I40"
- "@44@0:8@16B24Q28^@36"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16Q24@32^@40"
- "@88@0:8@16@24@32@40{?=[8I]}48^@80"
- "@96@0:8@16@24@32@40@48{?=[8I]}56^@88"
- "@?"
- "@?16@0:8"
- "AITransactionLog"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "B32@0:8@16^@24"
- "B32@0:8Q16^@24"
- "B32@0:8^B16^@24"
- "B36@0:8@16B24^@28"
- "B40@0:8@16@24^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^@24^@32"
- "B44@0:8@16S24I28I32^@36"
- "B48@0:8@16@24^@32@?40"
- "B48@0:8@16Q24@32^@40"
- "B48@0:8@16S24I28I32i36^@40"
- "B52@0:8@16S24I28I32i36B40^@44"
- "B56@0:8@16@24@32Q40^@48"
- "B56@0:8@16^{_BOMCopier=}24^Q32^Q40^@48"
- "I"
- "I16@0:8"
- "MIAppReference"
- "MIBOMWrapper"
- "MICandidateAppContainer"
- "MICandidateContainer"
- "MIHelperServiceFrameworkClient"
- "MIInstallOptions"
- "MIInstallerClient"
- "MIPlaceholderConstructor"
- "MIStagedUpdateMetadata"
- "MI_URLByAppendingPathComponents:lastIsDirectory:"
- "MI_dictionaryWithContentsOfURL:options:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:error:"
- "MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:"
- "MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:"
- "MI_writeAtomicallyToURLMatchingCurrentFileMetadata:format:error:"
- "MI_writeToURL:format:options:error:"
- "MobileInstallationAdditions"
- "MobileInstallationCopySafeHarborsForContainerClass_block_invoke"
- "MobileInstallationHelperServiceProtocol"
- "MobileInstallerDelegateProtocol"
- "MobileInstallerProtocol"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q16@0:8"
- "T@\"MIAppIdentity\",R,N,V_identity"
- "T@\"MIPlaceholderConstructor\",&,N,V_watchKitExtensionPlaceholderConstructor"
- "T@\"MIPlaceholderConstructor\",R,N"
- "T@\"MIStoreMetadata\",C,N,V_iTunesMetadata"
- "T@\"NSArray\",C,N,V_appExtensionPlaceholderConstructors"
- "T@\"NSArray\",C,N,V_embeddedAppClipPlaceholderConstructors"
- "T@\"NSArray\",C,N,V_embeddedWatchAppPlaceholderConstructors"
- "T@\"NSArray\",C,N,V_provisioningProfiles"
- "T@\"NSData\",&,N,V_installSessionUUID"
- "T@\"NSData\",&,N,V_installUUID"
- "T@\"NSData\",C,N,V_geoJSONData"
- "T@\"NSData\",C,N,V_iTunesArtworkData"
- "T@\"NSData\",C,N,V_sinfData"
- "T@\"NSDictionary\",&,N,V_infoPlistContent"
- "T@\"NSDictionary\",C,N,V_entitlements"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSDictionary\",R,C,N,V_metadata"
- "T@\"NSError\",&,N,V_delegatesCompleteError"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",C,N,V_alternateIconName"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_linkedParentBundleID"
- "T@\"NSString\",C,N,V_personaUniqueString"
- "T@\"NSString\",C,N,V_stagedIdentifier"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",&,N,V_appURL"
- "T@\"NSURL\",&,N,V_bundleURL"
- "T@\"NSURL\",R,N,V_rootURL"
- "T@\"NSUUID\",R,N,V_referenceUUID"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@?,C,N,V_appDictionaryEnumBlock"
- "T@?,C,N,V_progressBlock"
- "T@?,C,N,V_releaseTerminationAssertBlock"
- "TB,N,GisDeveloperInstall,V_developerInstall"
- "TB,N,GisSystemAppInstall,V_systemAppInstall"
- "TB,N,GisUserInitiated,V_userInitiated"
- "TB,N,V_allowDistributorChange"
- "TB,N,V_allowLocalProvisioned"
- "TB,N,V_basicIOSPlaceholderForWatchOSLessThanSix"
- "TB,N,V_delegatesComplete"
- "TB,N,V_includeAppClipPlaceholders"
- "TB,N,V_includeWatchAppPlaceholders"
- "TB,N,V_installForMigrator"
- "TB,N,V_isWatchKitExtension"
- "TB,N,V_performAPFSClone"
- "TB,N,V_performPlaceholderInstallActions"
- "TB,N,V_preserveFullInfoPlist"
- "TB,N,V_preservePlaceholderAsParallel"
- "TB,N,V_provisioningProfileInstallFailureIsFatal"
- "TB,N,V_skipBlacklist"
- "TB,N,V_skipWatchAppInstall"
- "TB,N,V_waitForDeletion"
- "TB,R"
- "TB,R,N"
- "TI,N,V_sinfDataType"
- "TI,R,N,V_uid"
- "TQ,N,V_autoInstallOverride"
- "TQ,N,V_installIntent"
- "TQ,N,V_installLocation"
- "TQ,N,V_installTargetType"
- "TQ,N,V_lsInstallType"
- "TQ,N,V_placeholderType"
- "TQ,N,V_stagedDiskUsage"
- "TQ,N,V_stashMode"
- "TQ,R,N,V_domain"
- "T^{?=[8I]},N,V_installationRequestorAuditToken"
- "Tq,R,N"
- "URLByAppendingPathComponent:isDirectory:"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "^{?=[8I]}"
- "^{?=[8I]}16@0:8"
- "_allowDistributorChange"
- "_allowLocalProvisioned"
- "_alternateIconName"
- "_appDictionaryEnumBlock"
- "_appExtensionPlaceholderConstructors"
- "_appURL"
- "_autoInstallOverride"
- "_basicIOSPlaceholderForWatchOSLessThanSix"
- "_bundleIdentifier"
- "_bundleURL"
- "_connection"
- "_constructPlaceholdersForDirectory:itemsWithPathExtension:appendingToArray:bundleType:error:"
- "_copyInfoPlistLoctableToPlaceholder:error:"
- "_copyStringsToPlaceholder:onlyDirectories:error:"
- "_countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:"
- "_defaultLog"
- "_delegatesComplete"
- "_delegatesCompleteCond"
- "_delegatesCompleteCondMutex"
- "_delegatesCompleteError"
- "_developerInstall"
- "_domain"
- "_embeddedAppClipPlaceholderConstructors"
- "_embeddedWatchAppPlaceholderConstructors"
- "_entitlements"
- "_entitlementsForPath:error:"
- "_geoJSONData"
- "_iTunesArtworkData"
- "_iTunesMetadata"
- "_identifier"
- "_identity"
- "_includeAppClipPlaceholders"
- "_includeWatchAppPlaceholders"
- "_infoPlistContent"
- "_infoPlistKeysToLoad"
- "_initWithLog:"
- "_initWithSource:byPreservingFullInfoPlist:forBundleType:error:"
- "_installForMigrator"
- "_installIntent"
- "_installLocation"
- "_installSessionUUID"
- "_installTargetType"
- "_installUUID"
- "_installationRequestorAuditToken"
- "_introspectWithError:"
- "_invalidateObject"
- "_isWatchKitExtension"
- "_linkedParentBundleID"
- "_loadInfoPlistContentWithError:"
- "_log"
- "_logScenario:step:success:forBundleID:persona:description:"
- "_lsInstallType"
- "_materializeConstructors:intoBundle:error:"
- "_metadata"
- "_performAPFSClone"
- "_performPlaceholderInstallActions"
- "_personaUniqueString"
- "_placeholderType"
- "_populateAppExtensionPlaceholderConstructorsWithError:"
- "_populateEmbeddedAppClipPlaceholderConstructorsWithError:"
- "_populateEmbeddedWatchAppPlaceholderConstructorsWithError:"
- "_preserveFullInfoPlist"
- "_preservePlaceholderAsParallel"
- "_progressBlock"
- "_provisioningProfileInstallFailureIsFatal"
- "_provisioningProfiles"
- "_queue"
- "_referenceUUID"
- "_releaseTerminationAssertBlock"
- "_remoteObjectProxyWithErrorHandler:"
- "_rootURL"
- "_sharedConnection"
- "_sinfData"
- "_sinfDataType"
- "_skipBlacklist"
- "_skipWatchAppInstall"
- "_stagedDiskUsage"
- "_stagedIdentifier"
- "_stashMode"
- "_synchronousRemoteObjectProxyWithErrorHandler:"
- "_systemAppInstall"
- "_transferAndUpdateInstallSessionIDsToPlaceholder:error:"
- "_uid"
- "_userInitiated"
- "_waitForDeletion"
- "_waitForPendingDelegateMessages"
- "_watchKitExtensionPlaceholderConstructor"
- "_writeIconToPlaceholder:infoPlistIconContent:error:"
- "_writeInfoPlistToPlaceholder:substitutingIconContent:withError:"
- "_xpcConnection"
- "acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:completion:"
- "acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:withCompletion:"
- "addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:"
- "addEntriesFromDictionary:"
- "addObject:"
- "allObjects"
- "allStagedUpdatesWithCompletion:"
- "allStagingLocationsWithinSubsystem:completion:"
- "allStagingLocationsWithinSubsystem:error:"
- "allocWithZone:"
- "altDSID"
- "appDictionaryEnumBlock"
- "appExtensionPlaceholderConstructors"
- "appURL"
- "appleID"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "basicIOSPlaceholderForWatchOSLessThanSix"
- "boolValue"
- "bundleAtURLIsPlaceholder:"
- "bundleID"
- "bundleRecordArrayToInfoDictionaryArray:"
- "bundleURL"
- "bytes"
- "cancelUpdateForStagedIdentifiers:completion:"
- "characterSetWithRange:"
- "checkCapabilities:withOptions:completion:"
- "clearTestFlags:withCompletion:"
- "clearTestFlags:withError:"
- "clearUninstalledIdentifiers:withOptions:completion:"
- "cloneItemAtURL:toURL:onBehalfOf:completion:"
- "cloneSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:"
- "code"
- "compare:"
- "connection"
- "containsObject:"
- "copy"
- "copyItemAtURL:toURL:error:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAppSnapshotWithBundleID:snapshotToURL:onlyV1AppIfPresent:placeholderOnly:completion:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:class:error:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:error:"
- "createSafeHarborWithIdentifier:forPersona:containerType:andMigrateDataFrom:completion:"
- "createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:"
- "createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:"
- "currentHandler"
- "dataForExtendedAttributeNamed:length:fromURL:error:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dealloc"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "defaultWorkspace"
- "delegateMessageDeliveryCompleteWithError:"
- "delegatesComplete"
- "delegatesCompleteError"
- "description"
- "deviceBasedVPP"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfURL:error:"
- "dieForTesting"
- "diskUsageForLaunchServicesWithBundleIDs:options:withError:"
- "diskUsageForURL:"
- "embeddedAppClipPlaceholderConstructors"
- "embeddedWatchAppPlaceholderConstructors"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endTestMode:"
- "endTestModeWithCompletion:"
- "entitlements"
- "enumerateAppDictionary:error:"
- "enumerateInstalledAppsWithOptions:completion:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:"
- "errorWithDomain:code:userInfo:"
- "estimatedSize"
- "extractZipArchiveAtURL:toURL:withError:"
- "extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:"
- "fetchDiskUsageForIdentifiers:withOptions:completion:"
- "fetchInfoForContainerizedAppWithBundleID:options:completion:"
- "fetchInfoForContainerizedAppWithIdentity:inDomain:options:completion:"
- "fetchInfoForFrameworkAtURL:options:completion:"
- "fetchListOfAppsRequiringPreInstallConsent:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "finalizeReference:completion:"
- "finalizeReference:withCompletion:"
- "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
- "firstNetworkExtension"
- "getAppMetadataForApp:completion:"
- "getPidForTestingWithCompletion:"
- "getTestModeEnabled:outError:"
- "getTestModeWithCompletion:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasPrefix:"
- "hash"
- "i16@0:8"
- "identifier"
- "includeAppClipPlaceholders"
- "includeWatchAppPlaceholders"
- "infoPlistContent"
- "init"
- "initForStagedIdentifier:diskUsage:"
- "initWithBundleID:"
- "initWithCoder:"
- "initWithContainerURL:identifier:metadata:"
- "initWithEmbeddedWatchAppSource:byPreservingFullInfoPlist:error:"
- "initWithFormat:arguments:"
- "initWithLegacyOptionsDictionary:"
- "initWithMachServiceName:options:"
- "initWithReferenceUUID:identity:domain:uid:"
- "initWithServiceName:"
- "initWithSource:byPreservingFullInfoPlist:error:"
- "initializeWithLog:"
- "installForMigrator"
- "installLocation"
- "installMacDeveloperAppAtURL:toURL:targetURLType:error:"
- "installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:"
- "installSessionUUID"
- "installTypeSummaryString"
- "installURL:identity:targetingDomain:options:returningResultInfo:completion:"
- "installURL:identity:targetingDomain:withOptions:returningResultInfo:completion:"
- "installUUID"
- "installerWithAppDictionaryEnumerator:"
- "installerWithProgressBlock:"
- "installerWithProgressBlock:releaseTerminationAssertionBlock:"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidateReference:completion:"
- "invalidateReference:withCompletion:"
- "isAppleApp"
- "isDataContainerEmpty:ofContainerType:completion:"
- "isEqual:"
- "isEqualToString:"
- "isLaunchProhibited"
- "isPlaceholder"
- "isWatchKitExtension"
- "itemDoesNotExistAtURL:"
- "itemExistsAtURL:"
- "itemExistsAtURL:error:"
- "itemID"
- "lastPathComponent"
- "legacyOptionsDictionary"
- "length"
- "linkedBundleIDsForAppIdentity:withCompletion:"
- "listSafeHarborsOfType:forPersona:withOptions:completion:"
- "logScenario:step:success:forBundleID:description:"
- "logStep:byParty:phase:success:forBundleID:description:"
- "logStep:byParty:phase:success:forBundleID:persona:description:"
- "longLongValue"
- "lookupSystemAppStateWithOptions:completion:"
- "lookupUninstalledWithOptions:completion:"
- "makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:"
- "markBundleAsPlaceholder:withError:"
- "materializeIntoBundleDirectory:error:"
- "metadata"
- "metadataFromPlistAtURL:error:"
- "metadataFromPlistData:error:"
- "metadataFromURL:error:"
- "migrateMobileContentWithCompletion:"
- "migrationPlistURL"
- "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:"
- "mutableCopy"
- "now"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "path"
- "pathExtension"
- "performPlaceholderInstallActions"
- "pidForTesting"
- "placeholderType"
- "preserveFullInfoPlist"
- "primaryPersonaString"
- "progressBlock"
- "propertyListDataWithError:"
- "purchaserID"
- "purgeInstallCoordinationPromiseStagingDirectoryForUUID:keepStagingDirectory:error:"
- "q16@0:8"
- "queue"
- "raiseException"
- "raiseExceptionWithCompletion:"
- "reconcileContentsOnKnownOSModules:completion:"
- "referencesForBundleWithIdentifier:inDomain:completion:"
- "referencesForBundleWithIdentifier:inDomain:withCompletion:"
- "registerContentsForDiskImageAtURL:completion:"
- "registerContentsOnOSModuleAtURL:completion:"
- "registerContentsOnRoot:deferUntilNextBoot:completion:"
- "registerPlaceholderForReference:completion:"
- "registerSafeHarborAtPath:forIdentity:ofType:withOptions:completion:"
- "releaseTerminationAssertBlock"
- "releaseTerminationAssertion"
- "remoteObjectProxyWithErrorHandler:"
- "removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:"
- "removeDeveloperAppAtURL:error:"
- "removeItemAtURL:error:"
- "removeMacAppWithBundleID:atURL:error:"
- "removeObjectForKey:"
- "removeSafeHarborForIdentity:ofType:withOptions:completion:"
- "reportProgress:"
- "resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:"
- "resume"
- "revertForLSWithIdentifier:withOptions:completion:"
- "revertIdentity:withOptions:completion:"
- "rootURL"
- "scanCharactersFromSet:intoString:"
- "scanInt:"
- "scannerWithString:"
- "serializeToURL:error:"
- "serviceName"
- "setAllowDistributorChange:"
- "setAllowLocalProvisioned:"
- "setAlternateIconName:"
- "setAppDictionaryEnumBlock:"
- "setAppExtensionPlaceholderConstructors:"
- "setAppURL:"
- "setAutoInstallOverride:"
- "setBasicIOSPlaceholderForWatchOSLessThanSix:"
- "setBundleIdentifier:"
- "setBundleURL:"
- "setByAddingObject:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setData:forExtendedAttributeNamed:onURL:error:"
- "setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:"
- "setDelegatesComplete:"
- "setDelegatesCompleteError:"
- "setDeveloperInstall:"
- "setEligibilityTestOverrides:withCompletion:"
- "setEligibilityTestOverrides:withError:"
- "setEmbeddedAppClipPlaceholderConstructors:"
- "setEmbeddedWatchAppPlaceholderConstructors:"
- "setEntitlements:"
- "setExportedInterface:"
- "setExportedObject:"
- "setGeoJSONData:"
- "setITunesArtworkData:"
- "setITunesMetadata:"
- "setIncludeAppClipPlaceholders:"
- "setIncludeWatchAppPlaceholders:"
- "setInfoPlistContent:"
- "setInstallBuildVersion:"
- "setInstallDate:"
- "setInstallForMigrator:"
- "setInstallIntent:"
- "setInstallLocation:"
- "setInstallSessionUUID:"
- "setInstallTargetType:"
- "setInstallType:"
- "setInstallUUID:"
- "setInstallationRequestorAuditToken:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsWatchKitExtension:"
- "setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:"
- "setLinkedParentBundleID:"
- "setLsInstallType:"
- "setObject:forKeyedSubscript:"
- "setPerformAPFSClone:"
- "setPerformPlaceholderInstallActions:"
- "setPersonaUniqueString:"
- "setPlaceholderType:"
- "setPreserveFullInfoPlist:"
- "setPreservePlaceholderAsParallel:"
- "setProgressBlock:"
- "setProvisioningProfileInstallFailureIsFatal:"
- "setProvisioningProfiles:"
- "setQueue:"
- "setReleaseTerminationAssertBlock:"
- "setRemoteObjectInterface:"
- "setSinfData:"
- "setSinfDataType:"
- "setSkipBlacklist:"
- "setSkipWatchAppInstall:"
- "setStagedDiskUsage:"
- "setStagedIdentifier:"
- "setStashMode:"
- "setSystemAppInstall:"
- "setSystemAppMigrationComplete:"
- "setTestFlags:withCompletion:"
- "setTestFlags:withError:"
- "setTestMode:"
- "setTestModeForIdentifierPrefix:testMode:error:"
- "setTestModeForIdentifierPrefix:testMode:validationData:"
- "setTestModeForIdentifierPrefix:testMode:validationData:error:"
- "setTestModeWithCompletion:"
- "setTestingEnabled:"
- "setTestingEnabled:error:"
- "setUserInitiated:"
- "setWaitForDeletion:"
- "setWatchKitExtensionPlaceholderConstructor:"
- "setWithArray:"
- "setWithObjects:"
- "setXpcConnection:"
- "sharedInstance"
- "sideLoadedDeviceBasedVPP"
- "skipBlacklist"
- "snapshotWKAppInCompanionAppID:toURL:options:completion:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "stageInstallURL:identity:targetingDomain:withOptions:completion:"
- "stageItemAtURL:toStagingLocation:options:completion:"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
- "stagingLocationForSystemContentWithinSubsystem:completion:"
- "stagingLocationForSystemContentWithinSubsystem:error:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:"
- "stagingLocationForUserContentWithinSubsystem:completion:"
- "stagingLocationForUserContentWithinSubsystem:error:"
- "stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:"
- "stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:"
- "storeListOfAppsRequiringPreInstallConsent:completion:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemAppMigratorHasCompleted:"
- "triggerRegistrationForContainerizedContentForOptions:withCompletion:"
- "triggerRegistrationForDiskImageContentForOptions:withCompletion:"
- "uninstallIdentifiers:withOptions:completion:"
- "uninstallIdentity:withOptions:completion:"
- "uninstallRecordArrayToDictionary:"
- "unregisterContentsForDiskImageAtURL:completion:"
- "unregisterContentsOnOSModuleAtURL:completion:"
- "unregisterContentsOnRoot:deferUntilNextBoot:completion:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updatePlaceholderMetadataForApp:installType:failureReason:underlyingError:failureSource:completion:"
- "updateSinfForIXWithIdentifier:withOptions:sinfData:completion:"
- "updateSystemAppStateForIdentifier:appState:completion:"
- "updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:"
- "updateiTunesMetadataForIXWithIdentifier:metadata:completion:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?i>16"
- "v24@0:8Q16"
- "v24@0:8^{?=[8I]}16"
- "v32@0:8@\"ICLRegistrationOptions\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8@\"MIAppReference\"16@?<v@?@\"LSRecordPromise\"@\"NSError\">24"
- "v32@0:8@\"MIAppReference\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@\"NSError\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"MIBundleMetadata\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24"
- "v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
- "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSObject\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v44@0:8@\"NSString\"16@\"NSURL\"24B32@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSData\"32@?<v@?@\"MIAppReference\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"ICLSinfInfo\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40"
- "v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24B32B36@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8Q16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8Q16@24@32@?40"
- "v52@0:8@16Q24B32@36@44"
- "v56@0:8@\"NSString\"16@\"MIAppIdentity\"24Q32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24Q32@\"NSURL\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"MIStagedUpdateMetadata\"@\"NSError\">48"
- "v56@0:8@16@24Q32@40@?48"
- "v60@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40B48@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">52"
- "v60@0:8@16@24Q32@40B48@?52"
- "v60@0:8@16Q24B32@36@44@52"
- "v60@0:8Q16Q24Q32B40@44@52"
- "v64@0:8@\"NSString\"16Q24Q32@\"NSError\"40Q48@?<v@?@\"NSError\">56"
- "v64@0:8@16Q24Q32@40Q48@?56"
- "v68@0:8Q16Q24Q32B40@44@52@60"
- "v72@0:8@\"NSURL\"16@\"NSURL\"24{?=[8I]}32@?<v@?@\"NSError\">64"
- "v72@0:8@16@24{?=[8I]}32@?64"
- "v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
- "v80@0:8@16@24@32{?=[8I]}40@?72"
- "validateAppIdentity:withError:"
- "validateAppReference:withError:"
- "volumeUUIDForURL:completion:"
- "waitForSystemAppMigratorToComplete:"
- "waitForSystemAppMigratorWithCompletion:"
- "watchKitExtensionPlaceholderConstructor"
- "wipeStagingRootAndSetUpPerUserDataDirWithCompletion:"
- "xpcConnection"
- "{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
- "\xf6"

```
