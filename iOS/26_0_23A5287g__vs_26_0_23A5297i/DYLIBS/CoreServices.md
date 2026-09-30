## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1434.0.0.0.0
-  __TEXT.__text: 0x1a69f8
+1439.0.0.0.0
+  __TEXT.__text: 0x1a5ea8
   __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__delay_stubs: 0x2c
-  __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0xcb24
+  __TEXT.__delay_helper: 0x16c
+  __TEXT.__objc_methlist: 0xcb1c
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x24093
-  __TEXT.__oslogstring: 0x1317f
-  __TEXT.__gcc_except_tab: 0x26890
+  __TEXT.__cstring: 0x240c6
+  __TEXT.__oslogstring: 0x130f8
+  __TEXT.__gcc_except_tab: 0x268ec
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xaf30
+  __TEXT.__unwind_info: 0xaea8
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1e6e
-  __TEXT.__objc_methname: 0x1cb1d
-  __TEXT.__objc_methtype: 0x9f7a
-  __TEXT.__objc_stubs: 0x10120
+  __TEXT.__objc_classname: 0x1e43
+  __TEXT.__objc_methname: 0x1cba9
+  __TEXT.__objc_methtype: 0x9f38
+  __TEXT.__objc_stubs: 0x101c0
   __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x6b58
-  __DATA_CONST.__objc_classlist: 0x6a0
+  __DATA_CONST.__const: 0x6ba8
+  __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5dd8
-  __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x548
-  __DATA_CONST.__objc_arraydata: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x5df8
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x1810
-  __AUTH_CONST.__const: 0x3680
-  __AUTH_CONST.__cfstring: 0x167c0
-  __AUTH_CONST.__objc_const: 0x12d38
+  __AUTH_CONST.__const: 0x35c0
+  __AUTH_CONST.__cfstring: 0x167a0
+  __AUTH_CONST.__objc_const: 0x12bd0
   __AUTH_CONST.__objc_intobj: 0x810
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x2b20
-  __AUTH.__data: 0x330
-  __DATA.__objc_ivar: 0xa60
-  __DATA.__data: 0x12b4
-  __DATA.__bss: 0xeb0
+  __AUTH.__objc_data: 0x2ad0
+  __AUTH.__data: 0x318
+  __DATA.__objc_ivar: 0xa70
+  __DATA.__data: 0x1260
+  __DATA.__bss: 0xe78
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0FD621A8-3140-31D6-B2B9-C2AAE3962D41
-  Functions: 8579
-  Symbols:   27848
-  CStrings:  13505
+  UUID: E6E2A9ED-4A2A-394A-A017-172A53898CC8
+  Functions: 8545
+  Symbols:   27776
+  CStrings:  13503
 
Symbols:
+ +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]
+ +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:].cold.1
+ -[LSAltIconManager .cxx_destruct]
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:]
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.1
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.2
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.3
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.4
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.5
+ -[LSIconAlertManager .cxx_destruct]
+ -[LSIconAlertManager _hasOutstandingTokenForIdentity:]
+ -[LSIconAlertManager _removeExtantToken:]
+ -[LSIconAlertManager iconChangeAlertTokenForIdentity:error:]
+ -[LSIconAlertManager iconChangeAlertTokenForIdentity:error:].cold.1
+ -[LSIconAlertManager init]
+ -[LSIconChangeAlertToken .cxx_destruct]
+ -[LSIconChangeAlertToken dealloc]
+ -[LSIconChangeAlertToken identity]
+ -[LSIconChangeAlertToken initWithIdentity:manager:]
+ -[LSIconChangeAlertToken presentWithCompletion:]
+ -[LSIconChangeAlertToken presentWithCompletion:].cold.1
+ -[_LSDIconClient setAlternateIconNameForCurrentApplication:completionHandler:]
+ GCC_except_table185
+ GCC_except_table251
+ GCC_except_table299
+ GCC_except_table306
+ GCC_except_table345
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table363
+ GCC_except_table377
+ GCC_except_table378
+ GCC_except_table431
+ GCC_except_table437
+ GCC_except_table441
+ GCC_except_table445
+ GCC_except_table447
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table484
+ GCC_except_table485
+ GCC_except_table488
+ GCC_except_table491
+ GCC_except_table493
+ GCC_except_table494
+ _LSGetCSUIAUpcallManager
+ _LSGetCSUIAUpcallManager.cold.1
+ _LSGetCSUIAUpcallManager.error
+ _LSGetCSUIAUpcallManager.manager
+ _LSGetCSUIAUpcallManager.onceToken
+ _OBJC_CLASS_$_LSIconAlertManager
+ _OBJC_CLASS_$_LSIconChangeAlertToken
+ _OBJC_IVAR_$_LSAltIconManager._alertManager
+ _OBJC_IVAR_$_LSIconAlertManager._extantTokens
+ _OBJC_IVAR_$_LSIconAlertManager._lock
+ _OBJC_IVAR_$_LSIconChangeAlertToken._hasBeenPresented
+ _OBJC_IVAR_$_LSIconChangeAlertToken._identity
+ _OBJC_IVAR_$_LSIconChangeAlertToken._manager
+ _OBJC_METACLASS_$_LSIconAlertManager
+ _OBJC_METACLASS_$_LSIconChangeAlertToken
+ _OUTLINED_FUNCTION_22
+ __LSUserActivityTypeBrowsingWebUnused
+ __OBJC_$_INSTANCE_METHODS_LSIconAlertManager
+ __OBJC_$_INSTANCE_METHODS_LSIconChangeAlertToken
+ __OBJC_$_INSTANCE_VARIABLES_LSAltIconManager
+ __OBJC_$_INSTANCE_VARIABLES_LSIconAlertManager
+ __OBJC_$_INSTANCE_VARIABLES_LSIconChangeAlertToken
+ __OBJC_CLASS_RO_$_LSIconAlertManager
+ __OBJC_CLASS_RO_$_LSIconChangeAlertToken
+ __OBJC_METACLASS_RO_$_LSIconAlertManager
+ __OBJC_METACLASS_RO_$_LSIconChangeAlertToken
+ ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke
+ ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke.142
+ ___107+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:]_block_invoke.144
+ ___113-[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:]_block_invoke
+ ___113-[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:]_block_invoke.cold.1
+ ___42-[LSDocumentProxy(Binding) _boundIconInfo]_block_invoke.161
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.189
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.192
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.203
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke.209
+ ___45-[LSApplicationWorkspace establishConnection]_block_invoke_2.200
+ ___48-[LSIconChangeAlertToken presentWithCompletion:]_block_invoke
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.373
+ ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.373.cold.1
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.399
+ ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.399.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.2
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.370
+ ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.370.cold.1
+ ___59-[_LSDModifyClient removeAllHandlersWithCompletionHandler:]_block_invoke.203
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.303
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.306
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.309
+ ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.382
+ ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.374
+ ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.754
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.377
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.378
+ ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.379
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.243
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.248
+ ___78-[_LSDIconClient setAlternateIconNameForCurrentApplication:completionHandler:]_block_invoke
+ ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.283
+ ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.394
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.316
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.316.cold.1
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.317
+ ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.317.cold.1
+ ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.302
+ ___99+[LSApplicationRecord setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:]_block_invoke.36
+ ___99+[LSApplicationRecord setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:]_block_invoke.40
+ ___Block_byref_object_copy_.1009
+ ___Block_byref_object_copy_.1191
+ ___Block_byref_object_copy_.132
+ ___Block_byref_object_copy_.198
+ ___Block_byref_object_copy_.382
+ ___Block_byref_object_copy_.686
+ ___Block_byref_object_dispose_.1010
+ ___Block_byref_object_dispose_.1192
+ ___Block_byref_object_dispose_.133
+ ___Block_byref_object_dispose_.199
+ ___Block_byref_object_dispose_.383
+ ___Block_byref_object_dispose_.687
+ ___LSGetCSUIAUpcallManager_block_invoke
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.937
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.937.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.941
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.941.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.943
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.944
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.939
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.942
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.946
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.946.cold.1
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1011
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1012
+ ____LSUnregisterBundle_block_invoke.186
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_77_e27_v16?0^{BindingResult=^^?}8l
+ ___block_descriptor_80_e8_32r40r_e42_v24?0"LSDBExecutionContext"8"NSError"16lr32l8r40l8
+ ___block_literal_global.1096
+ ___block_literal_global.1119
+ ___block_literal_global.1146
+ ___block_literal_global.1148
+ ___block_literal_global.1159
+ ___block_literal_global.146
+ ___block_literal_global.151
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.177
+ ___block_literal_global.181
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.212
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.265
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.292
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.329
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.57
+ ___block_literal_global.576
+ ___block_literal_global.642
+ ___block_literal_global.656
+ ___block_literal_global.673
+ ___block_literal_global.675
+ ___block_literal_global.916
+ ___block_literal_global.945
+ ___block_literal_global.984
+ _dlopenHelper$BaseBoard
+ _dlopenHelperFlag$BaseBoard
+ _gotLoadHelper_x8$_OBJC_CLASS_$_BSProcessHandle
+ _objc_msgSend$_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:
+ _objc_msgSend$_hasOutstandingTokenForIdentity:
+ _objc_msgSend$_removeExtantToken:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:
+ _objc_msgSend$iconChangeAlertTokenForIdentity:error:
+ _objc_msgSend$identity
+ _objc_msgSend$initWithIdentity:manager:
+ _objc_msgSend$presentWithCompletion:
+ _objc_msgSend$setAlternateIconNameForCurrentApplication:completionHandler:
+ _objc_msgSend$showIconChangeAlertForApplicationWithIdentity:completion:
- +[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:]
- +[_LSInstallationService beginListening]
- +[_LSInstallationService beginListening].cold.1
- +[_LSInstallerClient makeServerInstallerConnection]
- +[_LSInstallerClient makeServerInstallerConnection].cold.1
- +[_LSInstallerClient makeServerInstallerConnection].cold.2
- +[_LSInstallerClient makeServerInstallerConnection].cold.3
- +[_LSInstallerClient syncServerInstallerProxyForShim]
- -[_LSDModifyClient performShimmedInstallOfArtifact:options:completion:]
- -[_LSDModifyClient performShimmedUninstallOfApplicationWithIdentifier:options:completion:]
- -[_LSInstallationService .cxx_destruct]
- -[_LSInstallationService init]
- -[_LSInstallationService init].cold.1
- -[_LSInstallationService listener:shouldAcceptNewConnection:]
- -[_LSInstallationService serialQueue]
- -[_LSInstaller .cxx_destruct]
- -[_LSInstaller performShimmedInstallOfArtifact:options:completion:]
- -[_LSInstaller performShimmedUninstallOfApplicationWithIdentifier:options:completion:]
- -[_LSInstaller setXpcConnection:]
- -[_LSInstaller xpcConnection]
- GCC_except_table149
- GCC_except_table168
- GCC_except_table192
- GCC_except_table204
- GCC_except_table229
- GCC_except_table235
- GCC_except_table236
- GCC_except_table239
- GCC_except_table243
- GCC_except_table260
- GCC_except_table262
- GCC_except_table264
- GCC_except_table292
- GCC_except_table312
- GCC_except_table314
- GCC_except_table319
- GCC_except_table358
- GCC_except_table365
- GCC_except_table366
- GCC_except_table388
- GCC_except_table389
- GCC_except_table390
- GCC_except_table391
- GCC_except_table444
- GCC_except_table450
- GCC_except_table454
- GCC_except_table458
- GCC_except_table460
- GCC_except_table464
- GCC_except_table478
- GCC_except_table497
- GCC_except_table498
- GCC_except_table501
- GCC_except_table504
- GCC_except_table506
- GCC_except_table507
- _MIInstallOptionsFunction
- _OBJC_CLASS_$__LSInstallationService
- _OBJC_CLASS_$__LSInstaller
- _OBJC_CLASS_$__LSInstallerClient
- _OBJC_IVAR_$__LSInstallationService._serialQueue
- _OBJC_IVAR_$__LSInstaller._xpcConnection
- _OBJC_METACLASS_$__LSInstallationService
- _OBJC_METACLASS_$__LSInstaller
- _OBJC_METACLASS_$__LSInstallerClient
- __LSInvokeMIForShimmedInstall
- __LSInvokeMIForShimmedUninstall
- __LSValidateEntitlementsOfConnectionForUninstall
- __LSValidateEntitlementsOfConnectionForVanillaInstall
- __OBJC_$_CLASS_METHODS__LSInstallationService
- __OBJC_$_INSTANCE_METHODS__LSInstallationService
- __OBJC_$_INSTANCE_METHODS__LSInstaller
- __OBJC_$_INSTANCE_VARIABLES__LSInstallationService
- __OBJC_$_INSTANCE_VARIABLES__LSInstaller
- __OBJC_$_PROP_LIST__LSDModifyClient
- __OBJC_$_PROP_LIST__LSInstallationService
- __OBJC_$_PROP_LIST__LSInstaller
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LSInstallationServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSInstallationServiceProtocol
- __OBJC_$_PROTOCOL_REFS_LSInstallationServiceProtocol
- __OBJC_$_PROTOCOL_REFS__LSDModifyProtocol
- __OBJC_CLASS_PROTOCOLS_$__LSInstallationService
- __OBJC_CLASS_PROTOCOLS_$__LSInstaller
- __OBJC_CLASS_RO_$__LSInstallationService
- __OBJC_CLASS_RO_$__LSInstaller
- __OBJC_CLASS_RO_$__LSInstallerClient
- __OBJC_LABEL_PROTOCOL_$_LSInstallationServiceProtocol
- __OBJC_METACLASS_RO_$__LSInstallationService
- __OBJC_METACLASS_RO_$__LSInstaller
- __OBJC_METACLASS_RO_$__LSInstallerClient
- __OBJC_PROTOCOL_$_LSInstallationServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_LSInstallationServiceProtocol
- ___101+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:]_block_invoke
- ___101+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:]_block_invoke_2
- ___101+[LSDocumentProxy(Binding) _bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:]_block_invoke_3
- ___102-[LSApplicationWorkspace uninstallContainerizedApplicationWithIdentifier:options:error:progressBlock:]_block_invoke
- ___102-[LSApplicationWorkspace uninstallContainerizedApplicationWithIdentifier:options:error:progressBlock:]_block_invoke_2
- ___126-[LSApplicationWorkspace installContainerizedApplicationArtifactAtURL:withOptions:returningRecordPromise:error:progressBlock:]_block_invoke
- ___126-[LSApplicationWorkspace installContainerizedApplicationArtifactAtURL:withOptions:returningRecordPromise:error:progressBlock:]_block_invoke_2
- ___40+[_LSInstallationService beginListening]_block_invoke
- ___42-[LSDocumentProxy(Binding) _boundIconInfo]_block_invoke.159
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.200
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.205
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.211
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke.217
- ___45-[LSApplicationWorkspace establishConnection]_block_invoke_2.208
- ___51+[_LSInstallerClient makeServerInstallerConnection]_block_invoke
- ___51+[_LSInstallerClient makeServerInstallerConnection]_block_invoke.2
- ___51+[_LSInstallerClient makeServerInstallerConnection]_block_invoke.2.cold.1
- ___51+[_LSInstallerClient makeServerInstallerConnection]_block_invoke.cold.1
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.381
- ___51-[LSApplicationWorkspace deviceIdentifierForVendor]_block_invoke.381.cold.1
- ___53+[_LSInstallerClient syncServerInstallerProxyForShim]_block_invoke
- ___53+[_LSInstallerClient syncServerInstallerProxyForShim]_block_invoke.cold.1
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.407
- ___55-[LSApplicationWorkspace _LSPrivateNoteMigratorRunning]_block_invoke.407.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.638
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.638.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.639
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.639.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.639.cold.2
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.378
- ___56-[LSApplicationWorkspace deviceIdentifierForAdvertising]_block_invoke.378.cold.1
- ___59-[_LSDModifyClient removeAllHandlersWithCompletionHandler:]_block_invoke.247
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.347
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.350
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.353
- ___66-[LSApplicationWorkspace installProgressForApplication:withPhase:]_block_invoke.390
- ___67-[_LSInstaller performShimmedInstallOfArtifact:options:completion:]_block_invoke
- ___68-[LSApplicationWorkspace urlContainsDeviceIdentifierForAdvertising:]_block_invoke.382
- ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.762
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.385
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.386
- ___69-[LSApplicationWorkspace installProgressForBundleID:makeSynchronous:]_block_invoke.387
- ___71-[_LSDModifyClient performShimmedInstallOfArtifact:options:completion:]_block_invoke
- ___74-[LSApplicationWorkspace installApplication:withOptions:error:usingBlock:]_block_invoke
- ___74-[LSApplicationWorkspace installApplication:withOptions:error:usingBlock:]_block_invoke_2
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.287
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.292
- ___76-[LSApplicationWorkspace uninstallApplication:withOptions:error:usingBlock:]_block_invoke
- ___76-[LSApplicationWorkspace uninstallApplication:withOptions:error:usingBlock:]_block_invoke_2
- ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.327
- ___86-[_LSInstaller performShimmedUninstallOfApplicationWithIdentifier:options:completion:]_block_invoke
- ___90-[_LSDModifyClient performShimmedUninstallOfApplicationWithIdentifier:options:completion:]_block_invoke
- ___95-[LSApplicationWorkspace _LSPrivateRebuildApplicationDatabasesForSystemApps:internal:user:uid:]_block_invoke.402
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.323
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.323.cold.1
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.324
- ___98-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]_block_invoke.324.cold.1
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.346
- ___99+[LSApplicationRecord setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:]_block_invoke.35
- ___99+[LSApplicationRecord setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:]_block_invoke.39
- ___Block_byref_object_copy_.1017
- ___Block_byref_object_copy_.1205
- ___Block_byref_object_copy_.131
- ___Block_byref_object_copy_.197
- ___Block_byref_object_copy_.387
- ___Block_byref_object_copy_.683
- ___Block_byref_object_dispose_.1018
- ___Block_byref_object_dispose_.1206
- ___Block_byref_object_dispose_.132
- ___Block_byref_object_dispose_.198
- ___Block_byref_object_dispose_.388
- ___Block_byref_object_dispose_.684
- ____LSInvokeMIForShimmedInstall_block_invoke
- ____LSInvokeMIForShimmedInstall_block_invoke.cold.1
- ____LSInvokeMIForShimmedUninstall_block_invoke
- ____LSInvokeMIForShimmedUninstall_block_invoke.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.945
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.945.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.949.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.951
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.952
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.947
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.950
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.954
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.954.cold.1
- ____LSServer_SyncWithMobileInstallation_block_invoke.1019
- ____LSServer_SyncWithMobileInstallation_block_invoke_2.1020
- ____LSUnregisterBundle_block_invoke.185
- ___block_descriptor_69_e27_v16?0^{BindingResult=^^?}8l
- ___block_literal_global.1104
- ___block_literal_global.1110
- ___block_literal_global.1133
- ___block_literal_global.1160
- ___block_literal_global.1162
- ___block_literal_global.1173
- ___block_literal_global.145
- ___block_literal_global.150
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.185
- ___block_literal_global.204
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.222
- ___block_literal_global.273
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.291
- ___block_literal_global.316
- ___block_literal_global.349
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.372
- ___block_literal_global.4
- ___block_literal_global.406
- ___block_literal_global.409
- ___block_literal_global.575
- ___block_literal_global.59
- ___block_literal_global.650
- ___block_literal_global.664
- ___block_literal_global.681
- ___block_literal_global.683
- ___block_literal_global.924
- ___block_literal_global.942
- ___block_literal_global.981
- ___getShimInvokeQueue_block_invoke
- ___installationInterface_block_invoke
- ___serviceQueue_block_invoke
- _beginListening.installationServiceDelegate
- _classMIInstallOptions
- _getMIInstallOptionsClass
- _getShimInvokeQueue
- _getShimInvokeQueue.cold.1
- _getShimInvokeQueue.onceToken
- _getShimInvokeQueue.queue
- _initMIInstallOptions
- _initMobileInstallationInstallForInstallCoordinationWithError
- _initMobileInstallationUninstallForInstallCoordinationWithError
- _installationInterface
- _installationInterface.cold.1
- _installationInterface.interface
- _installationInterface.once
- _objc_msgSend$_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:
- _objc_msgSend$initWithLegacyOptionsDictionary:
- _objc_msgSend$performShimmedInstallOfArtifact:options:completion:
- _objc_msgSend$performShimmedUninstallOfApplicationWithIdentifier:options:completion:
- _objc_msgSend$setXpcConnection:
- _objc_msgSend$xpcConnection
- _serviceQueue.onceToken
- _serviceQueue.queue
- _softLinkMobileInstallationInstallForInstallCoordinationWithError
- _softLinkMobileInstallationUninstallForInstallCoordinationWithError
CStrings:
+ "#ChangeIconWithAlert begin for %@ to %@"
+ "#ChangeIconWithAlert couldn't make icon alert token for %@: %@"
+ "#ChangeIconWithAlert couldn't set alternate icon name for %@: %@"
+ "#ChangeIconWithAlert done for %@: %d %@"
+ "#ChangeIconWithAlert present for %@"
+ "#ChangeIconWithAlert send notification for %@"
+ "-[LSIconAlertManager iconChangeAlertTokenForIdentity:error:]"
+ "-[LSIconChangeAlertToken presentWithCompletion:]"
+ "-[_LSDIconClient setAlternateIconNameForCurrentApplication:completionHandler:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/CSUIUpcall/CoreServicesUIUpcallEmbedded.m"
+ "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSIconAlertManager.m"
+ "/System/Library/CoreServices/CSUIAUpcallBundle.bundle"
+ "/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard"
+ "@\"LSApplicationIdentity\""
+ "@\"LSIconAlertManager\""
+ "AlternateIconNameOOP"
+ "Couldn't get fresh node: %@"
+ "Couldn't get refreshed modification date: %@"
+ "Evaluating document proxy binding query for %{private}@"
+ "Filtered %zu original bundle IDs to %zu for %@ (managed? %d) (%@) -> (%@)"
+ "LSGetCSUIAUpcallManager_block_invoke"
+ "LSIconAlertManager"
+ "LSIconAlertManager.m"
+ "LSIconChangeAlertToken"
+ "_alertManager"
+ "_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:sourceAuditToken:"
+ "_extantTokens"
+ "_hasBeenPresented"
+ "_hasOutstandingTokenForIdentity:"
+ "_identity"
+ "_removeExtantToken:"
+ "bundle 0x%llx fresh node confirms mod date changed from %{public}@ to %{public}@"
+ "bundle 0x%llx fresh node shows no change, cached data was stale"
+ "bundle 0x%llx mod date went backwards from %{public}@ to %{public}@, verifying with fresh node"
+ "bundleWithPath:"
+ "calling process is not an application"
+ "changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:"
+ "couldn't instantiate upcall bundle principal class"
+ "couldn't load upcall bundle principal class"
+ "iconChangeAlertTokenForIdentity:error:"
+ "identity"
+ "initWithIdentity:manager:"
+ "must have completion"
+ "must provide identity"
+ "open in restriction in effect, binding %{private}@ source is %@"
+ "presentWithCompletion:"
+ "setAlternateIconNameForCurrentApplication:completionHandler:"
+ "showIconChangeAlertForApplicationWithIdentity:completion:"
+ "this process is using %{public}s to install applications, which is not supported. Use InstallCoordination to install and uninstall applications on this platform."
+ "this process is using %{public}s to uninstall applications, which is not supported. Use InstallCoordination to install and uninstall applications on this platform."
+ "warning: no source audit token provided when filtering bindings for a document proxy, which is suspicious"
- "/Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSInstallationInterface.m"
- "AllowInstallLocalProvisioned"
- "Checking if this process can access the com.apple.lsd.installation service name"
- "Connection interrupted to installationCallbackInterface"
- "Connection invalidated to installationCallbackInterface"
- "InstallForDataMigrator"
- "InstallLocalProvisioned"
- "LS installation serial queue"
- "LSInstallationServiceProtocol"
- "LS_AVOID_SHIM_FAULTS_TEMPORARILY"
- "MIInstallOptions"
- "Missing Entitlement"
- "MobileInstallationInstallForInstallCoordinationWithError"
- "MobileInstallationInstallForInstallCoordinationWithError returned NO but did not emit an error?"
- "MobileInstallationUninstallForInstallCoordinationWithError"
- "MobileInstallationUninstallForInstallCoordinationWithError returned NO but did not emit an error?"
- "Processing install of %@... later."
- "Processing uninstall of %@... later."
- "SkipBlacklist"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_serialQueue"
- "T@\"NSXPCConnection\",W,N,V_xpcConnection"
- "VerifyForMigrator"
- "_LSInstallationService"
- "_LSInstaller"
- "_LSInstallerClient"
- "_LSInvokeMIForShimmedInstall_block_invoke"
- "_LSInvokeMIForShimmedUninstall_block_invoke"
- "_LSValidateEntitlementsOfConnectionForUninstall"
- "_LSValidateEntitlementsOfConnectionForVanillaInstall"
- "_bindingEvaluatorResultFilterForBindingStyle:contentIsManaged:auditToken:"
- "_serialQueue"
- "com.apple.LaunchServices.InstallationShimInvoke"
- "error on sync server connection for install shimming: %@"
- "initWithLegacyOptionsDictionary:"
- "now processing install of %@ with options %@"
- "now processing uninstall of %@ with options %@"
- "performShimmedInstallOfArtifact:options:completion:"
- "performShimmedUninstallOfApplicationWithIdentifier:options:completion:"
- "sandbox_check returned NO for the com.apple.lsd.installation service name,using _LSDModifyService instead"
- "sandbox_check returned YES for the com.apple.lsd.installation service name, attempting to connect"
- "serialQueue"
- "setXpcConnection:"
- "shimmed install returned error %@"
- "shimming install of %@ with options %@"
- "this process is using %{public}s to install applications, which is deprecated. Use InstallCoordination to install and uninstall applications on this platform."
- "this process is using %{public}s to install applications, which is unsupported. Use InstallCoordination to install and uninstall applications on this platform."
- "this process is using %{public}s to uninstall applications, which is deprecated. Use InstallCoordination to install and uninstall applications on this platform."
- "unknown error installing via mobileinstallation"
- "unknown error uninstalling via mobileinstallation"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "xpcConnection"

```
