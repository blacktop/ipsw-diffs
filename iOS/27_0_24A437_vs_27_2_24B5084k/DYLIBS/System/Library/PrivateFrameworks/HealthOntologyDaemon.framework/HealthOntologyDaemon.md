## HealthOntologyDaemon

> `/System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x2c6b8
-  __TEXT.__objc_methlist: 0x21ac
+7027.1.36.2.7
+  __TEXT.__text: 0x2e56c
+  __TEXT.__objc_methlist: 0x226c
   __TEXT.__const: 0x282
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__cstring: 0x33bc
-  __TEXT.__oslogstring: 0x1dda
+  __TEXT.__gcc_except_tab: 0x6e8
+  __TEXT.__cstring: 0x34ec
+  __TEXT.__oslogstring: 0x208a
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_typeref: 0xb1
   __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__constg_swiftt: 0xbc
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1128
+  __TEXT.__unwind_info: 0x11c0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19f0
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x1a20
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1828
+  __DATA_CONST.__objc_selrefs: 0x18e8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0x381
-  __AUTH_CONST.__cfstring: 0x2240
-  __AUTH_CONST.__objc_const: 0x3f40
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0x4010
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0xc90
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
-  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1099
-  Symbols:   2746
-  CStrings:  452
+  Functions: 1138
+  Symbols:   2821
+  CStrings:  476
 
Symbols:
+ +[HDOntologyManifestUpdater _getManifestEntryWithUpdateCoordinator:URL:respectsOverriddenEnvironment:error:]
+ +[HDOntologyMercuryZipTSVImporter _handleResourceExtractionForArchiveEntry:entry:updateCoordinator:]
+ +[HDOntologyResourceDirectoryManager _activeDirectoryNameForEntry:]
+ +[HDOntologyResourceDirectoryManager _attemptDeleteOrphanedDirectoryAtURL:directoryName:fileManager:deletionErrors:]
+ +[HDOntologyResourceDirectoryManager _finalizeDeletionResultsWithAttemptedCount:deletionErrors:error:]
+ +[HDOntologyResourceDirectoryManager _isDirectoryAtURL:]
+ +[HDOntologyResourceDirectoryManager _processDirectoryItem:activeDirectoryNames:fileManager:deletionErrors:]
+ +[HDOntologyResourceDirectoryManager _shouldPreserveDirectoryNamed:activeDirectoryNames:]
+ +[HDOntologyResourceDirectoryManager _stagedDirectoryNameForEntry:]
+ +[HDOntologyResourceDirectoryManager _writeInfoPlistToBundleURL:bundleName:error:]
+ +[HDOntologyResourceDirectoryManager activeResourceDirectoryURLForEntry:baseResourcesDirectoryURL:]
+ +[HDOntologyResourceDirectoryManager activeResourceDirectoryURLForEntry:updateCoordinator:]
+ +[HDOntologyResourceDirectoryManager baseResourcesDirectoryURLForUpdateCoordinator:]
+ +[HDOntologyResourceDirectoryManager cleanupOrphanedDirectoriesExcluding:updateCoordinator:fileManager:error:]
+ +[HDOntologyResourceDirectoryManager createResourceDirectoryForEntry:updateCoordinator:fileManager:error:]
+ +[HDOntologyResourceDirectoryManager deleteResourceDirectoryForEntry:updateCoordinator:fileManager:error:]
+ +[HDOntologyResourceDirectoryManager extractResourceEntry:entry:updateCoordinator:fileManager:error:]
+ +[HDOntologyResourceDirectoryManager stagedResourceDirectoryURLForEntry:updateCoordinator:]
+ -[HDOntologyManifestUpdater initWithOntologyUpdateCoordinator:defaults:]
+ -[HDOntologyMercuryZipTSVPruner _deleteResourceDirectoriesForEntries:]
+ -[HDOntologyResourceDirectoryManager init]
+ -[HDOntologyShardImporter _publishMedicalHistoryVersionIfNeeded:]
+ -[HDOntologyShardImporter initWithOntologyUpdateCoordinator:medicalHistoryDefaults:]
+ -[HDOntologyShardImporter reconcileMedicalHistoryDefaultsWithError:]
+ -[HDOntologyShardPruner _activeResourceDirectoryNamesInTransaction:error:]
+ -[HDOntologyShardPruner _cleanupOrphanedResourceDirectoriesWithError:]
+ -[HDOntologyShardPruner _cleanupOrphanedResourceDirectoriesWithTransaction:error:]
+ -[HDOntologyUpdateCoordinator _reconcileMedicalHistoryDefaults]
+ -[HDOntologyUpdateCoordinator initWithDaemon:medicalHistoryDefaults:]
+ -[HDOntologyUpdateCoordinator initWithDaemon:scheduler:medicalHistoryDefaults:]
+ GCC_except_table14
+ GCC_except_table23
+ GCC_except_table71
+ GCC_except_table84
+ _HDOntologyZipResourcesPrefix
+ _HKErrorDomain
+ _HKHealthServicesPlatformRespectsOverriddenEnvironmentKey
+ _HKOntologyShardIdentifierMedicalHistory
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_HDOntologyResourceDirectoryManager
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_IVAR_$_HDOntologyManifestUpdater._defaults
+ _OBJC_IVAR_$_HDOntologyShardImporter._medicalHistoryDefaults
+ _OBJC_METACLASS_$_HDOntologyResourceDirectoryManager
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ __OBJC_$_CLASS_METHODS_HDOntologyResourceDirectoryManager
+ __OBJC_$_INSTANCE_METHODS_HDOntologyResourceDirectoryManager
+ __OBJC_CLASS_RO_$_HDOntologyResourceDirectoryManager
+ __OBJC_METACLASS_RO_$_HDOntologyResourceDirectoryManager
+ ___110+[HDOntologyResourceDirectoryManager cleanupOrphanedDirectoriesExcluding:updateCoordinator:fileManager:error:]_block_invoke
+ ___52-[HDOntologyShardImporter _markImportedEntry:error:]_block_invoke_2
+ ___68-[HDOntologyShardImporter reconcileMedicalHistoryDefaultsWithError:]_block_invoke
+ ___70-[HDOntologyShardPruner _cleanupOrphanedResourceDirectoriesWithError:]_block_invoke
+ ___74-[HDOntologyShardPruner _activeResourceDirectoryNamesInTransaction:error:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56r_e19_q24?0"NSURL"8^16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e32_v24?0"_HKZipArchiveEntry"8^B16ls32l8s40l8s48l8r64l8s56l8r72l8
+ _objc_msgSend$activeResourceDirectoryURLForEntry:baseResourcesDirectoryURL:
+ _objc_msgSend$activeResourceDirectoryURLForEntry:updateCoordinator:
+ _objc_msgSend$array
+ _objc_msgSend$baseResourcesDirectoryURLForUpdateCoordinator:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$cleanupOrphanedDirectoriesExcluding:updateCoordinator:fileManager:error:
+ _objc_msgSend$containsString:
+ _objc_msgSend$createResourceDirectoryForEntry:updateCoordinator:fileManager:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$deleteResourceDirectoryForEntry:updateCoordinator:fileManager:error:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$extractEntryContentsToURL:error:
+ _objc_msgSend$extractResourceEntry:entry:updateCoordinator:fileManager:error:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hk_isCocoaFileExistsError
+ _objc_msgSend$initWithDaemon:medicalHistoryDefaults:
+ _objc_msgSend$initWithDaemon:scheduler:medicalHistoryDefaults:
+ _objc_msgSend$initWithOntologyUpdateCoordinator:defaults:
+ _objc_msgSend$initWithOntologyUpdateCoordinator:medicalHistoryDefaults:
+ _objc_msgSend$reconcileMedicalHistoryDefaultsWithError:
+ _objc_msgSend$set
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$stagedResourceDirectoryURLForEntry:updateCoordinator:
+ _objc_msgSend$writeToURL:options:error:
- +[HDOntologyManifestUpdater _getManifestEntryWithUpdateCoordinator:URL:error:]
- GCC_except_table16
- GCC_except_table68
- GCC_except_table81
- ___block_descriptor_80_e8_32s40s48s56r64r_e32_v24?0"_HKZipArchiveEntry"8^B16ls32l8r56l8s40l8s48l8r64l8
- _objc_msgSend$initWithDaemon:scheduler:
CStrings:
+ "%@_%@_%ld_%ld.bundle"
+ "%{public}@: Cleaned up orphaned resource directories attempted %ld"
+ "%{public}@: Cleared medical history version from defaults"
+ "%{public}@: Deleted orphaned resource directory: %{public}@"
+ "%{public}@: Error reconciling medical history defaults: %{public}@"
+ "%{public}@: Failed to cleanup orphaned resource directories: %{public}@"
+ "%{public}@: Failed to delete resource directory for entry %{public}@: %{public}@"
+ "%{public}@: Failed to extract resource: '%{public}@' - %{public}@"
+ "%{public}@: No medicalHistoryDefaults, dropping clear"
+ "%{public}@: No medicalHistoryDefaults, dropping publish of version %{public}ld for %{public}@"
+ "%{public}@: Published medical history version %{public}ld to defaults"
+ "6.0"
+ "BNDL"
+ "CFBundleDevelopmentRegion"
+ "CFBundleIdentifier"
+ "CFBundleInfoDictionaryVersion"
+ "CFBundleName"
+ "CFBundlePackageType"
+ "Failed to delete %ld of %ld orphaned resource directories"
+ "Info.plist"
+ "MedicalHistoryImportedShardVersion"
+ "Resources/"
+ "com.apple.health.ontology.%@"
+ "en"
+ "resources"
- "1"
```
