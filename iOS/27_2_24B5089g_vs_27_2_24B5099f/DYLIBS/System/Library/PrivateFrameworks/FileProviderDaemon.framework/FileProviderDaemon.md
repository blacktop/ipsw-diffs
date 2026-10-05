## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4838.40.92.502.1
-  __TEXT.__text: 0xa545e0
-  __TEXT.__objc_methlist: 0x99c4
-  __TEXT.__const: 0x2e570
-  __TEXT.__cstring: 0x4f8b5
-  __TEXT.__oslogstring: 0x210c2
-  __TEXT.__gcc_except_tab: 0xd80c
+4838.40.130.0.2
+  __TEXT.__text: 0xa62ff8
+  __TEXT.__objc_methlist: 0x9b54
+  __TEXT.__const: 0x2e640
+  __TEXT.__cstring: 0x500b5
+  __TEXT.__oslogstring: 0x21972
+  __TEXT.__gcc_except_tab: 0xd9d8
   __TEXT.__ustring: 0x1880
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__constg_swiftt: 0x14900
-  __TEXT.__swift5_typeref: 0x14d0e
-  __TEXT.__swift5_builtin: 0x8e8
-  __TEXT.__swift5_reflstr: 0xfa2d
-  __TEXT.__swift5_fieldmd: 0xd278
+  __TEXT.__constg_swiftt: 0x149cc
+  __TEXT.__swift5_typeref: 0x14d8a
+  __TEXT.__swift5_builtin: 0x8fc
+  __TEXT.__swift5_reflstr: 0xfa8d
+  __TEXT.__swift5_fieldmd: 0xd2ac
   __TEXT.__swift5_mpenum: 0x144
   __TEXT.__swift5_assocty: 0x29f0
-  __TEXT.__swift5_capture: 0x1aaa8
+  __TEXT.__swift5_capture: 0x1abe4
   __TEXT.__swift5_proto: 0x1cc4
-  __TEXT.__swift5_types: 0xc5c
+  __TEXT.__swift5_types: 0xc64
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift_as_entry: 0x1b4
   __TEXT.__swift_as_ret: 0x188
   __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x1b7b8
-  __TEXT.__eh_frame: 0x2dab0
+  __TEXT.__unwind_info: 0x1c108
+  __TEXT.__eh_frame: 0x2d098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x47a8
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__const: 0x4880
+  __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x2e8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6368
-  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x6438
+  __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2a8
-  __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__got: 0x1980
-  __AUTH_CONST.__const: 0x4c998
-  __AUTH_CONST.__cfstring: 0x7720
-  __AUTH_CONST.__objc_const: 0x28150
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x168
+  __DATA_CONST.__objc_arraydata: 0x128
+  __DATA_CONST.__got: 0x1940
+  __AUTH_CONST.__const: 0x4ccc8
+  __AUTH_CONST.__cfstring: 0x7860
+  __AUTH_CONST.__objc_const: 0x28320
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3150
-  __AUTH.__objc_data: 0x1b90
-  __AUTH.__data: 0x2878
-  __DATA.__objc_ivar: 0xbe8
-  __DATA.__data: 0x81f0
+  __AUTH_CONST.__auth_got: 0x3180
+  __AUTH.__objc_data: 0x1ca8
+  __AUTH.__data: 0x28a8
+  __DATA.__objc_ivar: 0xbf8
+  __DATA.__data: 0x82b0
   __DATA.__common: 0x21b
   __DATA_DIRTY.__objc_data: 0x34b0
-  __DATA_DIRTY.__data: 0x10e80
+  __DATA_DIRTY.__data: 0x10e70
   __DATA_DIRTY.__bss: 0x10198
   __DATA_DIRTY.__common: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31773
-  Symbols:   12677
-  CStrings:  8293
+  Functions: 31851
+  Symbols:   12742
+  CStrings:  8354
 
Symbols:
+ -[FPDAccessControlServicer transferAccessToAllItemsFromBundle:toBundle:completionHandler:]
+ -[FPDAccessControlStore getSupersededBundleIdentifier:installSessionIdentifier:forBundleIdentifier:installSession:]
+ -[FPDAccessControlStore transferAccessFromBundle:toBundle:error:]
+ -[FPDDomain migrationState]
+ -[FPDDomain setMigrationState:]
+ -[FPDExtensionManager _isProviderInMigration:]
+ -[FPDExtensionManager _resumePendingMigrationsForEachPersona]
+ -[FPDExtensionManager beginMigrationForProviderIdentifiers:]
+ -[FPDExtensionManager currentDomainForSupersededProviderDomainIdentifier:]
+ -[FPDExtensionManager endMigrationForProviderIdentifiers:]
+ -[FPDXPCServicer migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]
+ -[FPFSChangeMonitor didResumeHandler]
+ -[FPFSChangeMonitor isSuspended]
+ -[FPFSChangeMonitor setDidResumeHandler:]
+ GCC_except_table223
+ GCC_except_table241
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table297
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table312
+ GCC_except_table322
+ GCC_except_table329
+ GCC_except_table331
+ GCC_except_table333
+ GCC_except_table338
+ GCC_except_table352
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table409
+ GCC_except_table434
+ GCC_except_table441
+ GCC_except_table450
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table456
+ _FPDomainMigrationDestinationKey
+ _FPDomainMigrationKey
+ _FPDomainMigrationSourcesKey
+ _OBJC_CLASS_$_FPDDomainMigrationState
+ _OBJC_IVAR_$_FPDAccessControlStore._openError
+ _OBJC_IVAR_$_FPDDomain._migrationState
+ _OBJC_IVAR_$_FPDExtensionManager._providersInMigration
+ _OBJC_IVAR_$_FPFSChangeMonitor._didResumeHandler
+ _OBJC_METACLASS_$_FPDDomainMigrationState
+ __DATA_FPDDomainMigrationState
+ __INSTANCE_METHODS_FPDDomainMigrationState
+ __IVARS_FPDDomainMigrationState
+ __METACLASS_DATA_FPDDomainMigrationState
+ __OBJC_$_INSTANCE_METHODS_FPDExtensionManager(FileProviderDaemon)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSCopying
+ __PROPERTIES_FPDDomainMigrationState
+ __PROTOCOLS_FPDDomainMigrationState
+ __ZL27containingApplicationRecordP8NSString
+ ___115-[FPDAccessControlStore getSupersededBundleIdentifier:installSessionIdentifier:forBundleIdentifier:installSession:]_block_invoke
+ ___115-[FPDAccessControlStore getSupersededBundleIdentifier:installSessionIdentifier:forBundleIdentifier:installSession:]_block_invoke_2
+ ___61-[FPDExtensionManager _resumePendingMigrationsForEachPersona]_block_invoke
+ ___65-[FPDAccessControlStore transferAccessFromBundle:toBundle:error:]_block_invoke
+ ___65-[FPDAccessControlStore transferAccessFromBundle:toBundle:error:]_block_invoke_2
+ ___97-[FPDXPCServicer migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r56r_e23_B16?0"PQLConnection"8ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e35_v24?0"PQLConnection"8"NSError"16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e23_B16?0"PQLConnection"8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e35_v24?0"PQLConnection"8"NSError"16lr64l8r72l8s32l8s40l8s48l8s56l8
+ ___swift_assign_boxed_opaque_existential_0
+ ___swift_closure_destructor.1025Tm
+ ___swift_closure_destructor.1028Tm
+ ___swift_closure_destructor.1031Tm
+ ___swift_closure_destructor.1034Tm
+ ___swift_closure_destructor.111Tm
+ ___swift_closure_destructor.114Tm
+ ___swift_closure_destructor.1237Tm
+ ___swift_closure_destructor.1591Tm
+ ___swift_closure_destructor.1643Tm
+ ___swift_closure_destructor.1694Tm
+ ___swift_closure_destructor.1697Tm
+ ___swift_closure_destructor.1733Tm
+ ___swift_closure_destructor.1760Tm
+ ___swift_closure_destructor.176Tm
+ ___swift_closure_destructor.1776Tm
+ ___swift_closure_destructor.1784Tm
+ ___swift_closure_destructor.1883Tm
+ ___swift_closure_destructor.190Tm
+ ___swift_closure_destructor.1911Tm
+ ___swift_closure_destructor.1958Tm
+ ___swift_closure_destructor.234Tm
+ ___swift_closure_destructor.2518Tm
+ ___swift_closure_destructor.258Tm
+ ___swift_closure_destructor.261Tm
+ ___swift_closure_destructor.264Tm
+ ___swift_closure_destructor.267Tm
+ ___swift_closure_destructor.275Tm
+ ___swift_closure_destructor.2825Tm
+ ___swift_closure_destructor.287Tm
+ ___swift_closure_destructor.2938Tm
+ ___swift_closure_destructor.3075Tm
+ ___swift_closure_destructor.3082Tm
+ ___swift_closure_destructor.3092Tm
+ ___swift_closure_destructor.3095Tm
+ ___swift_closure_destructor.3169Tm
+ ___swift_closure_destructor.3200Tm
+ ___swift_closure_destructor.3306Tm
+ ___swift_closure_destructor.3444Tm
+ ___swift_closure_destructor.344Tm
+ ___swift_closure_destructor.3474Tm
+ ___swift_closure_destructor.351Tm
+ ___swift_closure_destructor.3550Tm
+ ___swift_closure_destructor.3560Tm
+ ___swift_closure_destructor.3563Tm
+ ___swift_closure_destructor.3566Tm
+ ___swift_closure_destructor.3642Tm
+ ___swift_closure_destructor.3648Tm
+ ___swift_closure_destructor.3657Tm
+ ___swift_closure_destructor.367Tm
+ ___swift_closure_destructor.376Tm
+ ___swift_closure_destructor.381Tm
+ ___swift_closure_destructor.38Tm
+ ___swift_closure_destructor.413Tm
+ ___swift_closure_destructor.4143Tm
+ ___swift_closure_destructor.4187Tm
+ ___swift_closure_destructor.4193Tm
+ ___swift_closure_destructor.4305Tm
+ ___swift_closure_destructor.439Tm
+ ___swift_closure_destructor.4518Tm
+ ___swift_closure_destructor.4521Tm
+ ___swift_closure_destructor.4525Tm
+ ___swift_closure_destructor.4528Tm
+ ___swift_closure_destructor.4609Tm
+ ___swift_closure_destructor.4635Tm
+ ___swift_closure_destructor.4674Tm
+ ___swift_closure_destructor.4790Tm
+ ___swift_closure_destructor.4796Tm
+ ___swift_closure_destructor.490Tm
+ ___swift_closure_destructor.5011Tm
+ ___swift_closure_destructor.513Tm
+ ___swift_closure_destructor.5199Tm
+ ___swift_closure_destructor.519Tm
+ ___swift_closure_destructor.525Tm
+ ___swift_closure_destructor.528Tm
+ ___swift_closure_destructor.534Tm
+ ___swift_closure_destructor.537Tm
+ ___swift_closure_destructor.5472Tm
+ ___swift_closure_destructor.5504Tm
+ ___swift_closure_destructor.556Tm
+ ___swift_closure_destructor.561Tm
+ ___swift_closure_destructor.572Tm
+ ___swift_closure_destructor.57Tm
+ ___swift_closure_destructor.5807Tm
+ ___swift_closure_destructor.590Tm
+ ___swift_closure_destructor.6018Tm
+ ___swift_closure_destructor.609Tm
+ ___swift_closure_destructor.615Tm
+ ___swift_closure_destructor.618Tm
+ ___swift_closure_destructor.6321Tm
+ ___swift_closure_destructor.6335Tm
+ ___swift_closure_destructor.6541Tm
+ ___swift_closure_destructor.6548Tm
+ ___swift_closure_destructor.6573Tm
+ ___swift_closure_destructor.657Tm
+ ___swift_closure_destructor.6693Tm
+ ___swift_closure_destructor.688Tm
+ ___swift_closure_destructor.699Tm
+ ___swift_closure_destructor.715Tm
+ ___swift_closure_destructor.752Tm
+ ___swift_closure_destructor.755Tm
+ ___swift_closure_destructor.768Tm
+ ___swift_closure_destructor.832Tm
+ ___swift_closure_destructor.841Tm
+ ___swift_closure_destructor.848Tm
+ ___swift_closure_destructor.84Tm
+ ___swift_closure_destructor.855Tm
+ ___swift_closure_destructor.899Tm
+ ___swift_closure_destructor.949Tm
+ ___unnamed_117
+ _errorInjectionDefaultsKeyForCategory
+ _errorInjectionMigrationCrashAfterMarkEnabled
+ _errorInjectionMigrationCrashAfterRenameEnabled
+ _errorInjectionMigrationCrashBeforeHandoverEnabled
+ _errorInjectionMigrationCrashBeforeMarkEnabled
+ _errorInjectionMigrationCrashBetweenDomainsEnabled
+ _errorInjectionMigrationCrashBetweenStorageKindsEnabled
+ _fpfs_supports_appDomainMigration
+ _kFileProviderSupersededAppReplacementEntitlement
+ _kill
+ _migrationDestinationIfUnfinished
+ _resolveInstallSessionIdentifier
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic Say_____G So12FPProviderIDa
+ _symbolic Sb_____yxq_GcSg 18FileProviderDaemon11SchedulableC
+ _symbolic _____ 18FileProviderDaemon23FPDDomainMigrationStateC
+ _symbolic _____ So30FPDVolumeDomainStorageLocationV
+ _symbolic _____3key_yp5valuet So30NSFileProviderDomainIdentifiera
+ _symbolic _____6source_AA11destinationt So12FPProviderIDa
+ _symbolic _____y_____6source_AB11destinationtG s23_ContiguousArrayStorageC So12FPProviderIDa
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So12FPProviderIDa
+ _symbolic _____y_____SgG s23_ContiguousArrayStorageC So28NSFileProviderItemIdentifiera
+ _symbolic _____y_____ypG s18_DictionaryStorageC So30NSFileProviderDomainIdentifiera
- GCC_except_table229
- GCC_except_table244
- GCC_except_table251
- GCC_except_table253
- GCC_except_table275
- GCC_except_table276
- GCC_except_table280
- GCC_except_table281
- GCC_except_table282
- GCC_except_table286
- GCC_except_table290
- GCC_except_table291
- GCC_except_table300
- GCC_except_table309
- GCC_except_table310
- GCC_except_table315
- GCC_except_table325
- GCC_except_table335
- GCC_except_table337
- GCC_except_table339
- GCC_except_table341
- GCC_except_table355
- GCC_except_table381
- GCC_except_table382
- GCC_except_table383
- GCC_except_table412
- GCC_except_table440
- GCC_except_table444
- GCC_except_table453
- __OBJC_$_INSTANCE_METHODS_FPDExtensionManager
- ___swift_closure_destructor.1023Tm
- ___swift_closure_destructor.1026Tm
- ___swift_closure_destructor.1029Tm
- ___swift_closure_destructor.1032Tm
- ___swift_closure_destructor.103Tm
- ___swift_closure_destructor.1235Tm
- ___swift_closure_destructor.143Tm
- ___swift_closure_destructor.1548Tm
- ___swift_closure_destructor.1641Tm
- ___swift_closure_destructor.1692Tm
- ___swift_closure_destructor.1695Tm
- ___swift_closure_destructor.1710Tm
- ___swift_closure_destructor.1730Tm
- ___swift_closure_destructor.1737Tm
- ___swift_closure_destructor.1782Tm
- ___swift_closure_destructor.180Tm
- ___swift_closure_destructor.1881Tm
- ___swift_closure_destructor.189Tm
- ___swift_closure_destructor.1909Tm
- ___swift_closure_destructor.1935Tm
- ___swift_closure_destructor.242Tm
- ___swift_closure_destructor.2457Tm
- ___swift_closure_destructor.262Tm
- ___swift_closure_destructor.263Tm
- ___swift_closure_destructor.265Tm
- ___swift_closure_destructor.266Tm
- ___swift_closure_destructor.274Tm
- ___swift_closure_destructor.2764Tm
- ___swift_closure_destructor.286Tm
- ___swift_closure_destructor.2877Tm
- ___swift_closure_destructor.289Tm
- ___swift_closure_destructor.3014Tm
- ___swift_closure_destructor.3021Tm
- ___swift_closure_destructor.3031Tm
- ___swift_closure_destructor.3034Tm
- ___swift_closure_destructor.3108Tm
- ___swift_closure_destructor.3139Tm
- ___swift_closure_destructor.3245Tm
- ___swift_closure_destructor.324Tm
- ___swift_closure_destructor.3383Tm
- ___swift_closure_destructor.33Tm
- ___swift_closure_destructor.3413Tm
- ___swift_closure_destructor.343Tm
- ___swift_closure_destructor.3489Tm
- ___swift_closure_destructor.3499Tm
- ___swift_closure_destructor.3502Tm
- ___swift_closure_destructor.3505Tm
- ___swift_closure_destructor.350Tm
- ___swift_closure_destructor.3581Tm
- ___swift_closure_destructor.3587Tm
- ___swift_closure_destructor.3596Tm
- ___swift_closure_destructor.366Tm
- ___swift_closure_destructor.375Tm
- ___swift_closure_destructor.380Tm
- ___swift_closure_destructor.4082Tm
- ___swift_closure_destructor.4126Tm
- ___swift_closure_destructor.412Tm
- ___swift_closure_destructor.4132Tm
- ___swift_closure_destructor.4244Tm
- ___swift_closure_destructor.432Tm
- ___swift_closure_destructor.438Tm
- ___swift_closure_destructor.441Tm
- ___swift_closure_destructor.4451Tm
- ___swift_closure_destructor.4454Tm
- ___swift_closure_destructor.4458Tm
- ___swift_closure_destructor.4461Tm
- ___swift_closure_destructor.4541Tm
- ___swift_closure_destructor.4567Tm
- ___swift_closure_destructor.4606Tm
- ___swift_closure_destructor.4722Tm
- ___swift_closure_destructor.4728Tm
- ___swift_closure_destructor.4943Tm
- ___swift_closure_destructor.494Tm
- ___swift_closure_destructor.5131Tm
- ___swift_closure_destructor.517Tm
- ___swift_closure_destructor.518Tm
- ___swift_closure_destructor.523Tm
- ___swift_closure_destructor.526Tm
- ___swift_closure_destructor.532Tm
- ___swift_closure_destructor.535Tm
- ___swift_closure_destructor.5404Tm
- ___swift_closure_destructor.5436Tm
- ___swift_closure_destructor.554Tm
- ___swift_closure_destructor.564Tm
- ___swift_closure_destructor.5739Tm
- ___swift_closure_destructor.576Tm
- ___swift_closure_destructor.58Tm
- ___swift_closure_destructor.5950Tm
- ___swift_closure_destructor.600Tm
- ___swift_closure_destructor.608Tm
- ___swift_closure_destructor.614Tm
- ___swift_closure_destructor.6252Tm
- ___swift_closure_destructor.6266Tm
- ___swift_closure_destructor.628Tm
- ___swift_closure_destructor.6472Tm
- ___swift_closure_destructor.6479Tm
- ___swift_closure_destructor.64Tm
- ___swift_closure_destructor.6504Tm
- ___swift_closure_destructor.6630Tm
- ___swift_closure_destructor.67Tm
- ___swift_closure_destructor.687Tm
- ___swift_closure_destructor.697Tm
- ___swift_closure_destructor.714Tm
- ___swift_closure_destructor.753Tm
- ___swift_closure_destructor.756Tm
- ___swift_closure_destructor.818Tm
- ___swift_closure_destructor.829Tm
- ___swift_closure_destructor.838Tm
- ___swift_closure_destructor.849Tm
- ___swift_closure_destructor.852Tm
- ___swift_closure_destructor.85Tm
- ___swift_closure_destructor.88Tm
- ___swift_closure_destructor.930Tm
- ___swift_closure_destructor.946Tm
- ___unnamed_115
CStrings:
+ "\r"
+ "%{public}s already has domains of its own"
+ "%{public}s has no domains to hand over"
+ "-[FPDXPCServicer migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]"
+ "-[FPDXPCServicer migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]_block_invoke"
+ "CREATE TABLE superseded_apps ( bundle_identifier TEXT NOT NULL, install_session_identifier BLOB NOT NULL, superseded_bundle_identifier TEXT NOT NULL, superseded_install_session_identifier BLOB NOT NULL, PRIMARY KEY (bundle_identifier, install_session_identifier) )"
+ "CREATE TRIGGER \"donation_status/fp_snapshot/app_container_bundle_identifier_arrival\"\n  AFTER UPDATE OF decoration_app_container_bundle_identifier ON fp_snapshot\n  WHEN (OLD.decoration_app_container_bundle_identifier IS NULL\n        OR length(OLD.decoration_app_container_bundle_identifier) = 0)\n    AND NEW.decoration_app_container_bundle_identifier IS NOT NULL\n    AND length(NEW.decoration_app_container_bundle_identifier) > 0\n    AND NEW.decoration_is_container = 1\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "Destination"
+ "FileProviderDaemon.FPDDomainMigrationState"
+ "INSERT OR REPLACE INTO superseded_apps (bundle_identifier, install_session_identifier, superseded_bundle_identifier, superseded_install_session_identifier) VALUES (%@, %@, %@, %@)"
+ "Migration"
+ "PRAGMA auto_vacuum = none"
+ "SELECT 1 FROM manifest LIMIT 1"
+ "SELECT superseded_bundle_identifier, superseded_install_session_identifier FROM superseded_apps WHERE bundle_identifier = %@ AND install_session_identifier = %@"
+ "Sources"
+ "UPDATE OR REPLACE bundle_keys SET identifier = %@ WHERE identifier = %@"
+ "[DEBUG] [incomplete migration] Initializing disconnected provider for %@"
+ "[DEBUG] itemID %@ predates the hand-over to %@"
+ "[NOTICE] %@: not starting the indexer (invalidated=%{bool}d indexerStopped=%{bool}d activeProvider=%{bool}d)"
+ "[NOTICE] Not registering %{public}@ while its domains are being migrated"
+ "[NOTICE] no access to transfer from %@ to %@"
+ "[NOTICE] refusing to migrate domains: the appDomainMigration feature flag is off"
+ "[NOTICE] transferred access from %@ (%@) to %@ (%@)"
+ "access control database is unavailable until first unlock"
+ "after marking the records"
+ "after-mark"
+ "after-rename"
+ "before marking the records"
+ "before-handover"
+ "before-mark"
+ "between-domains"
+ "between-storage-kinds"
+ "cannot hand %{public}s storage over to %{public}s: it owns one already"
+ "cannot look for unfinished migrations under %{public}s: %{public}@"
+ "cannot mark the record of %{public}s for hand-over: it is not a dictionary"
+ "cannot open access control database"
+ "cannot read the records of %{public}s: %{public}@"
+ "crash-injection: killing fileproviderd at %s"
+ "destinationProviderIdentifier"
+ "domains are being handed over to another provider"
+ "folder is being populated"
+ "found %ld unfinished hand-over(s) under %{public}s"
+ "handing %{public}s storage at %{public}s over to %{public}s"
+ "ignoring malformed migration state with keys %s"
+ "marked %ld record(s) of %{public}s; a later launch can finish this hand-over from here"
+ "marking %ld record(s) of %{public}s for hand-over to %{public}s"
+ "migrated %ld domain(s) from %{public}s to %{public}s; both providers are registered again"
+ "migrating %{public}s to %{public}s failed %{public}s: %{public}@"
+ "moved the records over to %{public}s, which is what finishes the hand-over"
+ "moving the records of %{public}s over to %{public}s"
+ "pre-flight passed, handing over %ld domain(s) from %{public}s to %{public}s"
+ "re-stamped the storage of %{public}s"
+ "re-stamping the storage of %{public}s from %{public}s to %{public}s"
+ "refusing to migrate %{public}s to %{public}s: %{public}@"
+ "removed the existing records of %{public}s"
+ "resumed migration of %{public}s to %{public}s"
+ "resuming migration of %{public}s to %{public}s"
+ "resuming migration of %{public}s to %{public}s failed: %{public}@"
+ "starting request to migrate %{public}s to %{public}s from %{public}s"
+ "stopped %{public}s for the duration of the hand-over"
+ "update_v13_6_appContainerBundleIdentifierArrivalTrigger(with:)"
+ "\xd1"
+ "\xf0\xb1"
- "\f"
- "\xf0\xa1"
```
