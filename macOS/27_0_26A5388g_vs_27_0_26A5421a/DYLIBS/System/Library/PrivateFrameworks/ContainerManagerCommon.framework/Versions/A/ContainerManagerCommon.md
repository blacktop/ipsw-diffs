## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon`

```diff

-833.0.3.0.0
-  __TEXT.__text: 0xf7a98
-  __TEXT.__objc_methlist: 0xab5c
-  __TEXT.__const: 0x1318
+833.0.8.0.1
+  __TEXT.__text: 0xf94c8
+  __TEXT.__objc_methlist: 0xad24
+  __TEXT.__const: 0x1378
   __TEXT.__swift5_typeref: 0x6bb
-  __TEXT.__oslogstring: 0xcdb1
-  __TEXT.__cstring: 0x9c62
+  __TEXT.__oslogstring: 0xd45c
+  __TEXT.__cstring: 0x9df4
   __TEXT.__constg_swiftt: 0x650
   __TEXT.__swift5_reflstr: 0x39a
   __TEXT.__swift5_fieldmd: 0x458

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x230c
+  __TEXT.__gcc_except_tab: 0x2348
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x22a8
+  __TEXT.__unwind_info: 0x2298
   __TEXT.__eh_frame: 0x5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x440
+  __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x530
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3668
+  __DATA_CONST.__objc_selrefs: 0x36b8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x500
-  __AUTH_CONST.__const: 0x2948
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0x16f18
+  __DATA_CONST.__got: 0x510
+  __AUTH_CONST.__const: 0x2918
+  __AUTH_CONST.__cfstring: 0x5640
+  __AUTH_CONST.__objc_const: 0x16f70
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH_CONST.__objc_intobj: 0x1560
+  __AUTH_CONST.__objc_intobj: 0x15c0
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x1128
+  __AUTH_CONST.__auth_got: 0x1120
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0xd0
   __DATA.__objc_ivar: 0xbfc
   __DATA.__data: 0x3bc0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xd58
+  __DATA.__bss: 0xd68
   __DATA_DIRTY.__objc_data: 0x3070
   __DATA_DIRTY.__data: 0x450
   __DATA_DIRTY.__bss: 0x850

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3635
-  Symbols:   8408
-  CStrings:  1978
+  Functions: 3651
+  Symbols:   8439
+  CStrings:  2009
 
Symbols:
+ +[MCMContainerMigrator sharedInstance]
+ -[MCMClientIdentity _descriptionRedacting:]
+ -[MCMClientIdentity redactedDescription]
+ -[MCMCodeSigningEntry _descriptionRedacting:]
+ -[MCMCodeSigningEntry redactedDescription]
+ -[MCMConcreteContainerIdentity _descriptionRedacting:]
+ -[MCMConcreteContainerIdentity redactedDescription]
+ -[MCMConcreteContainerIdentityForLibsystem _descriptionRedacting:]
+ -[MCMConcreteContainerIdentityForLibsystem redactedDescription]
+ -[MCMContainerClassPath _descriptionRedacting:]
+ -[MCMContainerClassPath redactedDescription]
+ -[MCMContainerConfiguration excludeFromBackupIdentifiers]
+ -[MCMContainerIdentity _descriptionRedacting:]
+ -[MCMContainerIdentity redactedDescription]
+ -[MCMContainerIdentityMinimal _descriptionRedacting:]
+ -[MCMContainerIdentityMinimal redactedDescription]
+ -[MCMContainerMigrator .cxx_destruct]
+ -[MCMContainerMigrator _excludeContainersFromBackupWithContext:containerConfig:]
+ -[MCMContainerMigrator _excludeFromBackupWithContainer:]
+ -[MCMContainerMigrator _fixParentsOnMigratedIdentitiesWithContext:]
+ -[MCMContainerMigrator _performEntitlementBypassListMigrationWithError:]
+ -[MCMContainerMigrator _updateMigratedContainerParentsFromMap:containerConfig:context:]
+ -[MCMContainerMigrator initWithUserIdentityCache:]
+ -[MCMContainerMigrator performSynchronousBuildUpgradeMigration:context:error:]
+ -[MCMContainerMigrator setUserIdentityCache:]
+ -[MCMContainerMigrator userIdentityCache]
+ -[MCMContainerPath _descriptionRedacting:]
+ -[MCMContainerPath redactedDescription]
+ -[MCMError _descriptionRedacting:]
+ -[MCMError redactedDescription]
+ -[MCMFileManager addExclusionFromBackupToURL:error:]
+ -[MCMManagedPath _descriptionRedacting:]
+ -[MCMManagedPath redactedDescription]
+ -[MCMMetadata _descriptionRedacting:]
+ -[MCMMetadata redactedDescription]
+ -[MCMMetadataMinimal _descriptionRedacting:]
+ -[MCMMetadataMinimal redactedDescription]
+ -[MCMPOSIXUser _descriptionRedacting:]
+ -[MCMPOSIXUser redactedDescription]
+ -[MCMUserIdentity _descriptionRedacting:]
+ -[MCMUserIdentity _shortDescriptionRedacting:]
+ -[MCMUserIdentity redactedDescription]
+ -[MCMUserIdentity redactedShortDescription]
+ GCC_except_table1012
+ GCC_except_table1023
+ GCC_except_table1066
+ GCC_except_table1075
+ GCC_except_table1081
+ GCC_except_table1130
+ GCC_except_table1131
+ GCC_except_table1147
+ GCC_except_table1154
+ GCC_except_table1160
+ GCC_except_table1171
+ GCC_except_table1173
+ GCC_except_table1176
+ GCC_except_table1181
+ GCC_except_table1183
+ GCC_except_table1191
+ GCC_except_table1194
+ GCC_except_table1196
+ GCC_except_table1206
+ GCC_except_table1225
+ GCC_except_table1227
+ GCC_except_table1282
+ GCC_except_table1292
+ GCC_except_table1323
+ GCC_except_table1561
+ GCC_except_table1708
+ GCC_except_table1712
+ GCC_except_table2388
+ GCC_except_table2402
+ GCC_except_table2423
+ GCC_except_table2492
+ GCC_except_table2504
+ GCC_except_table2570
+ GCC_except_table2582
+ GCC_except_table2607
+ GCC_except_table2634
+ GCC_except_table2657
+ GCC_except_table2659
+ GCC_except_table2662
+ GCC_except_table2669
+ GCC_except_table2717
+ GCC_except_table2721
+ GCC_except_table2891
+ GCC_except_table2894
+ GCC_except_table2971
+ GCC_except_table685
+ GCC_except_table768
+ GCC_except_table779
+ GCC_except_table931
+ GCC_except_table979
+ OBJC_IVAR_$_MCMContainerConfiguration._excludeFromBackupIdentifiers
+ OBJC_IVAR_$_MCMContainerMigrator._userIdentityCache
+ _MCMMigrationTypeExcludePSCFromBackup
+ _OBJC_CLASS_$_MCMContainerMigrator
+ _OBJC_METACLASS_$_MCMContainerMigrator
+ __52-[MCMFileManager addExclusionFromBackupToURL:error:]_block_invoke
+ __OBJC_$_CLASS_METHODS_MCMContainerMigrator
+ __OBJC_$_INSTANCE_METHODS_MCMContainerMigrator
+ __OBJC_$_INSTANCE_VARIABLES_MCMContainerMigrator
+ __OBJC_$_PROP_LIST_MCMContainerMigrator
+ __OBJC_CLASS_RO_$_MCMContainerMigrator
+ __OBJC_METACLASS_RO_$_MCMContainerMigrator
+ ___38+[MCMContainerMigrator sharedInstance]_block_invoke
+ ___72-[MCMContainerMigrator _performEntitlementBypassListMigrationWithError:]_block_invoke
+ ___78-[MCMContainerMigrator performSynchronousBuildUpgradeMigration:context:error:]_block_invoke
+ _kMCMXATTRMetadataBackupExcludeNameValue
+ _objc_msgSend$_descriptionRedacting:
+ _objc_msgSend$_excludeContainersFromBackupWithContext:containerConfig:
+ _objc_msgSend$_excludeFromBackupWithContainer:
+ _objc_msgSend$_regenerateContainerPaths
+ _objc_msgSend$_shortDescriptionRedacting:
+ _objc_msgSend$_updateMigratedContainerParentsFromMap:containerConfig:context:
+ _objc_msgSend$addExclusionFromBackupToURL:error:
+ _objc_msgSend$containerIdentityMigrationParents
+ _objc_msgSend$excludeFromBackupIdentifiers
+ _objc_msgSend$hasMigrationOccurredForType:
+ _objc_msgSend$isBuildUpgrade
+ _objc_msgSend$performSynchronousBuildUpgradeMigration:context:error:
+ _objc_msgSend$redactedShortDescription
+ _objc_msgSend$setMigrationCompleteForType:
+ _objc_msgSend$wellknownContainerForId:class:
+ _objc_msgSend$writeCurrentBuildInfoToDisk
+ _performEntitlementBypassListMigrationWithError:.possibleContainerClasses
- -[MCMLazyDescription .cxx_destruct]
- -[MCMLazyDescription characterAtIndex:]
- -[MCMLazyDescription description]
- -[MCMLazyDescription getCharacters:range:]
- -[MCMLazyDescription initWithDescriber:]
- -[MCMLazyDescription length]
- -[MCMLazyDescription redactedDescription]
- -[MCMPOSIXUser fullDescription]
- GCC_except_table1004
- GCC_except_table1019
- GCC_except_table1062
- GCC_except_table1071
- GCC_except_table1077
- GCC_except_table1126
- GCC_except_table1127
- GCC_except_table1143
- GCC_except_table1146
- GCC_except_table1156
- GCC_except_table1159
- GCC_except_table1165
- GCC_except_table1172
- GCC_except_table1175
- GCC_except_table1177
- GCC_except_table1187
- GCC_except_table1190
- GCC_except_table1192
- GCC_except_table1202
- GCC_except_table1217
- GCC_except_table1223
- GCC_except_table1278
- GCC_except_table1288
- GCC_except_table1319
- GCC_except_table1555
- GCC_except_table1702
- GCC_except_table1706
- GCC_except_table2387
- GCC_except_table2408
- GCC_except_table2477
- GCC_except_table2489
- GCC_except_table2555
- GCC_except_table2567
- GCC_except_table2592
- GCC_except_table2619
- GCC_except_table2642
- GCC_except_table2644
- GCC_except_table2647
- GCC_except_table2654
- GCC_except_table2702
- GCC_except_table2706
- GCC_except_table2875
- GCC_except_table2878
- GCC_except_table2955
- GCC_except_table682
- GCC_except_table765
- GCC_except_table776
- GCC_except_table927
- GCC_except_table975
- OBJC_IVAR_$_MCMLazyDescription._block
- OBJC_IVAR_$_MCMLazyDescription._value
- _OBJC_CLASS_$_MCMLazyDescription
- _OBJC_METACLASS_$_MCMLazyDescription
- _OBJC_METACLASS_$_NSString
- __OBJC_$_INSTANCE_METHODS_MCMLazyDescription
- __OBJC_$_INSTANCE_VARIABLES_MCMLazyDescription
- __OBJC_CLASS_RO_$_MCMLazyDescription
- __OBJC_METACLASS_RO_$_MCMLazyDescription
- ___23-[MCMError description]_block_invoke
- ___26-[MCMMetadata description]_block_invoke
- ___27-[MCMError fullDescription]_block_invoke
- ___27-[MCMPOSIXUser description]_block_invoke
- ___29-[MCMManagedPath description]_block_invoke
- ___30-[MCMUserIdentity description]_block_invoke
- ___31-[MCMContainerPath description]_block_invoke
- ___31-[MCMMetadata debugDescription]_block_invoke
- ___31-[MCMPOSIXUser fullDescription]_block_invoke
- ___32-[MCMClientIdentity description]_block_invoke
- ___33-[MCMMetadataMinimal description]_block_invoke
- ___34-[MCMCodeSigningEntry description]_block_invoke
- ___35-[MCMContainerIdentity description]_block_invoke
- ___35-[MCMUserIdentity shortDescription]_block_invoke
- ___36-[MCMContainerClassPath description]_block_invoke
- ___37-[MCMClientIdentity shortDescription]_block_invoke
- ___38-[MCMMetadataMinimal debugDescription]_block_invoke
- ___40-[MCMContainerIdentity debugDescription]_block_invoke
- ___42-[MCMContainerIdentityMinimal description]_block_invoke
- ___43-[MCMConcreteContainerIdentity description]_block_invoke
- ___47-[MCMContainerIdentityMinimal debugDescription]_block_invoke
- ___48-[MCMConcreteContainerIdentity debugDescription]_block_invoke
- ___55-[MCMConcreteContainerIdentityForLibsystem description]_block_invoke
- ___60-[MCMConcreteContainerIdentityForLibsystem debugDescription]_block_invoke
- ___block_descriptor_40_e8_32s_e18_"NSString"12?0B8l
- _objc_msgSend$fullDescription
- _objc_msgSend$getCharacters:range:
- _objc_msgSend$initWithDescriber:
- _removexattr
CStrings:
+ "%s: Failed to generate new metadata for listed container %@"
+ "%s: Failed to move system container %@ from %@ to listed location %@: (error= %@: %lld)"
+ "%s: Failed to remove cache for listed container %@: %@"
+ "%s: Failed to update cache for listed container %@: %@"
+ "-[MCMContainerMigrator _performEntitlementBypassListMigrationWithError:]"
+ "-[MCMContainerMigrator _performEntitlementBypassListMigrationWithError:]_block_invoke"
+ "-[MCMFileManager addExclusionFromBackupToURL:error:]_block_invoke"
+ "17:57:15"
+ "Ambiguous persona with identifier: [🔒%{private}s]"
+ "Attempt to create a container identity without a user identity when one is required; identifier = [🔒%{private}@], class = %{public}@"
+ "Aug  8 2026"
+ "Completed Container Identity Parent Fixup Migration on %@"
+ "Completed Performing Exclude From Backup Migration [%@] on %@; success = %d"
+ "Could not create app group symlink for [🔒%{private}@], falling back to realpath: %{public}@"
+ "Couldn't load metadata; container = %@, error = %@"
+ "Encountered container identity migration entry with unknown container class: %@"
+ "Error during entitlement bypass list migration: %@"
+ "Exclude from backup identifiers malformed"
+ "ExcludePSCFromBackup"
+ "Excluded [%@] from backup"
+ "Excluded container from backup; container = %@"
+ "Failed to add backup exclusion xattr at [%@]"
+ "Failed to exclude container from backup; error = %@"
+ "Failed to fchown(%@) %s: %s"
+ "Failed to fetch entries for [%@]; error = %@"
+ "Failed to get dirstats on 🔒%{private}s using fallback: (err %d) %s"
+ "Failed to get list of system containers for migration: %@"
+ "Failed to perform build upgrade migration : %@"
+ "Invalid app group identifier [🔒%{private}@]"
+ "Invalid size (%lld) from dirstats on 🔒%{private}s using fallback: (err %d) %s"
+ "Migrating well-known container %@ from %@ to %@"
+ "MobileContainerManager-833.0.8.0.1~210"
+ "POSIX permission [%{public}@] value is not in a recognizable format; expected = POSIX mode bit string, got = 🔒%{private}@, errno = %{darwin.errno}d"
+ "Performing Container Identity Parent Fixup Migration on %@"
+ "Performing Exclude From Backup Migration [%@] on %@"
+ "Read [🔒%{private}@], length = %{public}lu, options = 0x%{public}lx"
+ "Rejecting query with invalid partDomain [%{public}@]"
+ "Responding CA event 🔒%{private}s"
+ "Submitting CA event 🔒%{private}s"
+ "System container lookup failed, class = %@, identifier = 🔒%{private}@, error = (%llu)%{public}@, client = %{public}@"
+ "Unable to construct container identity for migration; identifier = [%@], userIdentity = %@, error = (%llu) %s"
+ "Unable to fetch container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to fetch metadata for container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Unable to write new metadata to container for migration; identifier = [%@], userIdentity = %@, error = %@"
+ "Updated [%@] parent key to [%@]"
+ "Using app group symlink for [🔒%{private}@]: 🔒%{private}@"
+ "Wrote [🔒%{private}@], length = %{public}lu, options = 0x%{public}lx, permissions = %@"
+ "[%{public}s] requesting [🔒%{private}s]: APPROVED. Requestor's signature allows it to access a TCC-protected group container"
+ "[%{public}s] requesting [🔒%{private}s]: DEVELOPER ACTION REQUIRED. Requestor's signature is given temporary compatibility affordance to access a TCC-protected group container. Group containers identifiers should be authorized by a provisioning profile."
+ "[%{public}s] requesting [🔒%{private}s]: REJECTED. Requestor's signature does not allow it to access a TCC-protected group container. Group containers identifiers should be prefixed by requestor's team ID to allow access on this platform."
+ "[%{public}s] requesting [🔒%{private}s]: The container IS NOT PROTECTED since it isn't prefixed by team ID. Group containers identifiers must be prefixed by requestor's team ID on this platform for container security to be enforced."
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Action [%@] failed; error = %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not fetch fsNode for [%@]: %{public}@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not form action [%@] with args: %@, error = %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), actions count = %{public}lu, error = %{public}@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), no actions available"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Read metadata from [%@]: %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Successfully updated schema from (%{public}@) → (%{public}@), actions count = %{public}lu"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Trying to target a version [%@] higher than available [%lu], capping to max"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Wrote metadata to [%@]: %@"
+ "[🔒%{private}@] is a plugin"
+ "[🔒%{private}s] Enabled APFSIOC_DIR_STATS_OP"
+ "[🔒%{private}s] Enabled APFSIOC_MAINTAIN_DIR_STATS"
+ "[🔒%{private}s] Enabling fast disk sizing failed: %@"
+ "[🔒%{private}s] Failed to get dirstats: %{darwin.errno}d"
+ "[🔒%{private}s] Failed to set maintain-dir-stats: %{darwin.errno}d"
+ "[🔒%{private}s] Fast disk sizing failed: %{darwin.errno}d"
+ "[🔒%{private}s] Invalid size (%lld) from dirstats: %{darwin.errno}d"
+ "[🔒%{private}s]: descendants: %llu, total size: %llu [ph%llu; cl%llu; pu%llu]"
+ "[🔒%{private}s]: descendants: %llu, total size: %llu, using fallback"
+ "com.apple.MobileInstallation.ParentBundleID"
+ "excludeFromBackupIdentifiers"
+ "nil path when trying to add backup exclusion"
+ "open(O_NOFOLLOW) of %s for chown failed: %s"
- "23:41:39"
- "<%@: %p; UID = %u, primaryGID = %u, name = [%@], homeDirectoryURL = [%@]>"
- "<cm-redacted>"
- "@\"NSString\"12@?0B8"
- "Ambiguous persona with identifier: [%s]"
- "Attempt to create a container identity without a user identity when one is required; identifier = [%{public}@], class = %{public}@"
- "Could not create app group symlink for [%{public}@], falling back to realpath: %{public}@"
- "Failed to chown(%@) %s: %s"
- "Failed to get dirstats on %{public}s using fallback: (err %d) %s"
- "Invalid app group identifier [%{public}@]"
- "Invalid size (%lld) from dirstats on %{public}s using fallback: (err %d) %s"
- "Jul  7 2026"
- "MobileContainerManager-833.0.3~125"
- "POSIX permission [%{public}@] value is not in a recognizable format; expected = POSIX mode bit string, got = %{public}@, errno = %{darwin.errno}d"
- "Read [%{public}@], length = %{public}lu, options = 0x%{public}lx"
- "Responding CA event %s"
- "Submitting CA event %s"
- "System container lookup failed, class = %@, identifier = %{public}@, error = (%llu)%{public}@, client = %{public}@"
- "Using app group symlink for [%{public}@]: %{public}@"
- "Wrote [%{public}@], length = %{public}lu, options = 0x%{public}lx, permissions = %@"
- "[%{public}@] is a plugin"
- "[%{public}s] Enabled APFSIOC_DIR_STATS_OP"
- "[%{public}s] Enabled APFSIOC_MAINTAIN_DIR_STATS"
- "[%{public}s] Enabling fast disk sizing failed: %@"
- "[%{public}s] Failed to get dirstats: %{darwin.errno}d"
- "[%{public}s] Failed to set maintain-dir-stats: %{darwin.errno}d"
- "[%{public}s] Fast disk sizing failed: %{darwin.errno}d"
- "[%{public}s] Invalid size (%lld) from dirstats: %{darwin.errno}d"
- "[%{public}s] requesting [%{public}s]: APPROVED. Requestor's signature allows it to access a TCC-protected group container"
- "[%{public}s] requesting [%{public}s]: DEVELOPER ACTION REQUIRED. Requestor's signature is given temporary compatibility affordance to access a TCC-protected group container. Group containers identifiers should be authorized by a provisioning profile."
- "[%{public}s] requesting [%{public}s]: REJECTED. Requestor's signature does not allow it to access a TCC-protected group container. Group containers identifiers should be prefixed by requestor's team ID to allow access on this platform."
- "[%{public}s] requesting [%{public}s]: The container IS NOT PROTECTED since it isn't prefixed by team ID. Group containers identifiers must be prefixed by requestor's team ID on this platform for container security to be enforced."
- "[%{public}s]: descendants: %llu, total size: %llu [ph%llu; cl%llu; pu%llu]"
- "[%{public}s]: descendants: %llu, total size: %llu, using fallback"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Action [%@] failed; error = %@"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Could not fetch fsNode for [%@]: %{public}@"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Could not form action [%@] with args: %@, error = %@"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), actions count = %{public}lu, error = %{public}@"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), no actions available"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Read metadata from [%@]: %@"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Successfully updated schema from (%{public}@) → (%{public}@), actions count = %{public}lu"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Trying to target a version [%@] higher than available [%lu], capping to max"
- "[u %{public}@:p %{public}@:c %@(%{public}@):i%llu] Wrote metadata to [%@]: %@"
```
