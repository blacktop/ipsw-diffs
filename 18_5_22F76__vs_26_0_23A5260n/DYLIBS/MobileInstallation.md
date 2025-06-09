## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1378.100.35.0.0
-  __TEXT.__text: 0x201b0
+1513.0.8.0.2
+  __TEXT.__text: 0x22418
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0xfd4
-  __TEXT.__cstring: 0x49c7
-  __TEXT.__gcc_except_tab: 0xa08
-  __TEXT.__const: 0x40
+  __TEXT.__objc_methlist: 0x1104
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x4cb2
+  __TEXT.__gcc_except_tab: 0xb04
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xb30
   __TEXT.__objc_classname: 0x166
-  __TEXT.__objc_methname: 0x3c35
-  __TEXT.__objc_methtype: 0x1030
-  __TEXT.__objc_stubs: 0x29e0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x930
+  __TEXT.__objc_methname: 0x3fe6
+  __TEXT.__objc_methtype: 0x127c
+  __TEXT.__objc_stubs: 0x2a80
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf8
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2860
-  __AUTH_CONST.__objc_const: 0x15c0
+  __AUTH_CONST.__cfstring: 0x2880
+  __AUTH_CONST.__objc_const: 0x1660
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x240
   __DATA.__bss: 0x60
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFE6752D-6860-3FE6-B852-5B2D6DA7F790
-  Functions: 680
-  Symbols:   2138
-  CStrings:  1467
+  UUID: 82527B2E-C3B2-355A-B078-D3DFAD4E9744
+  Functions: 720
+  Symbols:   2240
+  CStrings:  1504
 
Symbols:
+ -[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]
+ -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:]
+ -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:]
+ -[MIHelperServiceFrameworkClient removeMacAppWithBundleID:atURL:error:]
+ -[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:error:]
+ -[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:validationData:error:]
+ -[MIHelperServiceFrameworkClient setTestingEnabled:error:]
+ -[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]
+ -[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]
+ -[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]
+ -[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]
+ -[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:]
+ -[MIInstallerClient addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]
+ -[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]
+ -[MIInstallerClient removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]
+ -[MIInstallerClient setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]
+ -[MIPlaceholderConstructor alternateIconName]
+ -[MIPlaceholderConstructor setAlternateIconName:]
+ GCC_except_table16
+ GCC_except_table233
+ GCC_except_table238
+ GCC_except_table24
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table258
+ GCC_except_table27
+ GCC_except_table285
+ GCC_except_table287
+ GCC_except_table293
+ GCC_except_table30
+ GCC_except_table301
+ GCC_except_table314
+ GCC_except_table318
+ GCC_except_table33
+ GCC_except_table337
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table345
+ GCC_except_table347
+ GCC_except_table35
+ GCC_except_table350
+ GCC_except_table357
+ GCC_except_table363
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table37
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table385
+ GCC_except_table401
+ GCC_except_table403
+ GCC_except_table405
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table413
+ _MobileInstallationVersionNumber
+ _MobileInstallationVersionString
+ _OBJC_CLASS_$_MILocationSystemDefinedBase
+ _OBJC_CLASS_$_MILocationSystemDefinedCommon
+ _OBJC_CLASS_$_MILocationUserDefined
+ _OBJC_CLASS_$_MILocationUserDefinedDirectory
+ _OBJC_CLASS_$_MIStagingLocation
+ _OBJC_IVAR_$_MIPlaceholderConstructor._alternateIconName
+ ___100-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke
+ ___100-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke_2
+ ___112-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke
+ ___112-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke_2
+ ___122-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]_block_invoke
+ ___122-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]_block_invoke_2
+ ___122-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]_block_invoke_3
+ ___122-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:]_block_invoke_4
+ ___58-[MIHelperServiceFrameworkClient setTestingEnabled:error:]_block_invoke
+ ___75-[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]_block_invoke
+ ___75-[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]_block_invoke_2
+ ___80-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:error:]_block_invoke
+ ___80-[MIInstallerClient addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]_block_invoke
+ ___80-[MIInstallerClient addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]_block_invoke_2
+ ___80-[MIInstallerClient addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]_block_invoke_3
+ ___80-[MIInstallerClient addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:]_block_invoke_4
+ ___82-[MIInstallerClient setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]_block_invoke
+ ___82-[MIInstallerClient setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]_block_invoke_2
+ ___82-[MIInstallerClient setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]_block_invoke_3
+ ___82-[MIInstallerClient setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:]_block_invoke_4
+ ___85-[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]_block_invoke
+ ___85-[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]_block_invoke_2
+ ___85-[MIInstallerClient removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]_block_invoke
+ ___85-[MIInstallerClient removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]_block_invoke_2
+ ___85-[MIInstallerClient removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]_block_invoke_3
+ ___85-[MIInstallerClient removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:]_block_invoke_4
+ ___87-[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]_block_invoke
+ ___87-[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]_block_invoke_2
+ ___95-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:validationData:error:]_block_invoke
+ ___MobileInstallationAddDataSeparatedAppsToPersona_block_invoke
+ ___MobileInstallationRemoveDataSeparatedAppsFromPersona_block_invoke
+ ___MobileInstallationSetPersonaForDataSeparatedApps_block_invoke
+ ___block_descriptor_48_e8_32r40r_e39_v24?0"MIStagingLocation"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr32l8
+ _objc_msgSend$_synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:
+ _objc_msgSend$allStagingLocationsWithinSubsystem:completion:
+ _objc_msgSend$createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:
+ _objc_msgSend$removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:
+ _objc_msgSend$setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:
+ _objc_msgSend$setTestModeForIdentifierPrefix:testMode:validationData:
+ _objc_msgSend$setTestingEnabled:
+ _objc_msgSend$stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:
+ _objc_msgSend$stagingLocationForSystemContentWithinSubsystem:completion:
+ _objc_msgSend$stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:
+ _objc_msgSend$stagingLocationForUserContentWithinSubsystem:completion:
- -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationInfo:onBehalfOf:error:]
- -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationRecords:onBehalfOf:error:]
- -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationInfo:onBehalfOf:error:]
- -[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationRecords:onBehalfOf:error:]
- -[MIHelperServiceFrameworkClient removeWrappedAppWithBundleID:atURL:error:]
- -[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:installationInfo:onBehalfOf:error:]
- -[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:installationRecords:onBehalfOf:error:]
- -[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]
- GCC_except_table218
- GCC_except_table223
- GCC_except_table228
- GCC_except_table231
- GCC_except_table234
- GCC_except_table237
- GCC_except_table240
- GCC_except_table263
- GCC_except_table270
- GCC_except_table272
- GCC_except_table284
- GCC_except_table286
- GCC_except_table288
- GCC_except_table292
- GCC_except_table305
- GCC_except_table309
- GCC_except_table311
- GCC_except_table313
- GCC_except_table315
- GCC_except_table317
- GCC_except_table342
- GCC_except_table348
- GCC_except_table352
- GCC_except_table354
- GCC_except_table356
- GCC_except_table358
- GCC_except_table362
- GCC_except_table364
- GCC_except_table366
- GCC_except_table370
- GCC_except_table375
- GCC_except_table386
- GCC_except_table388
- GCC_except_table395
- ___131-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]_block_invoke
- ___131-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]_block_invoke_2
- ___131-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]_block_invoke_3
- ___131-[MIInstallerClient createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:]_block_invoke_4
- ___block_descriptor_48_e8_32r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr32l8
- _objc_msgSend$createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:
- _objc_msgSend$createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationRecords:onBehalfOf:error:
- _objc_msgSend$createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationRecords:onBehalfOf:error:
- _objc_msgSend$deviceForURLOrFirstAvailableParent:error:
- _objc_msgSend$infoDictionaryArrayToBundleRecordArray:
- _objc_msgSend$objectForKey:
- _objc_msgSend$updateWrappedAppAt:forInstalledBundleIdentifier:installationRecords:onBehalfOf:error:
CStrings:
+ "-[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:]"
+ "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:]"
+ "-[MIHelperServiceFrameworkClient removeMacAppWithBundleID:atURL:error:]"
+ "-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:validationData:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient setTestingEnabled:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]_block_invoke"
+ "-[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:]"
+ "@32@0:8Q16^@24"
+ "@48@0:8@16Q24@32^@40"
+ "@88@0:8@16@24@32@40{?=[8I]}48^@80"
+ "B24@?0^{?=Qq*Q*QIIIIIIISBC}8^B16"
+ "B28@0:8B16^@20"
+ "B40@0:8@16Q24^@32"
+ "B48@0:8@16Q24@32^@40"
+ "Dictionary serialization of MIInstallOptions.installationRequestorAuditToken is not available; dropping this option."
+ "Proxy returned error: %@"
+ "addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:"
+ "allStagingLocationsWithinSubsystem:completion:"
+ "allStagingLocationsWithinSubsystem:error:"
+ "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:"
+ "createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:"
+ "createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:onBehalfOf:error:"
+ "moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:"
+ "removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:"
+ "removeMacAppWithBundleID:atURL:error:"
+ "resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:"
+ "setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:"
+ "setTestModeForIdentifierPrefix:testMode:error:"
+ "setTestModeForIdentifierPrefix:testMode:validationData:"
+ "setTestModeForIdentifierPrefix:testMode:validationData:error:"
+ "setTestingEnabled:"
+ "setTestingEnabled:error:"
+ "stageItemAtURL:toStagingLocation:options:completion:"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
+ "stagingLocationForSystemContentWithinSubsystem:completion:"
+ "stagingLocationForSystemContentWithinSubsystem:error:"
+ "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
+ "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:"
+ "stagingLocationForUserContentWithinSubsystem:completion:"
+ "stagingLocationForUserContentWithinSubsystem:error:"
+ "stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:"
+ "stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:"
+ "updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:"
+ "v24@?0@\"MIStagingLocation\"8@\"NSError\"16"
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
- "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationRecords:onBehalfOf:error:]"
- "-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationRecords:onBehalfOf:error:]"
- "-[MIHelperServiceFrameworkClient removeWrappedAppWithBundleID:atURL:error:]"
- "-[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:installationRecords:onBehalfOf:error:]"
- "@80@0:8@16@24@32{?=[8I]}40^@72"
- "B24@?0^{?=Qq*Q*QQIIIIIISBC}8^B16"
- "B80@0:8@16@24@32{?=[8I]}40^@72"
- "Converting install options with installationRequestorAuditToken set to a dictionary is not available; dropping this option."
- "MobileInstallationAddDataSeparatedAppsToPersona"
- "MobileInstallationRemoveDataSeparatedAppsFromPersona"
- "MobileInstallationSetPersonaForDataSeparatedApps"
- "createSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:onDevice:withCompletion:"
- "createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationInfo:onBehalfOf:error:"
- "createWrappedAppForInstalledBundleIdentifier:atTargetURL:installationRecords:onBehalfOf:error:"
- "createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationInfo:onBehalfOf:error:"
- "createWrappedAppForInstalledBundleIdentifier:inTargetDirectory:installationRecords:onBehalfOf:error:"
- "deviceForURLOrFirstAvailableParent:error:"
- "infoDictionaryArrayToBundleRecordArray:"
- "moveItemInStagingDirectory:atRelativePath:toDestinationURL:onBehalfOf:completion:"
- "objectForKey:"
- "removeWrappedAppWithBundleID:atURL:error:"
- "stageItemAtURL:options:completion:"
- "updateWrappedAppAt:forInstalledBundleIdentifier:installationInfo:onBehalfOf:error:"
- "updateWrappedAppAt:forInstalledBundleIdentifier:installationRecords:onBehalfOf:error:"
- "v40@0:8@\"NSURL\"16@\"MIInstallOptions\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24@32i40@?44"
- "v80@0:8Q16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72"
- "v80@0:8Q16@24@32{?=[8I]}40@?72"

```
