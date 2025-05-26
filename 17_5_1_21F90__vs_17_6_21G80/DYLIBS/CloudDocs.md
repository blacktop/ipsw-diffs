## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-2720.120.29.0.0
-  __TEXT.__text: 0x8ebb0
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x51b0
+2720.140.11.0.0
+  __TEXT.__text: 0x8eec8
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x51e0
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x42f8
-  __TEXT.__cstring: 0xb238
-  __TEXT.__oslogstring: 0x9731
+  __TEXT.__gcc_except_tab: 0x4360
+  __TEXT.__cstring: 0xb27e
+  __TEXT.__oslogstring: 0x97d8
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2438
-  __TEXT.__objc_classname: 0xdc2
-  __TEXT.__objc_methname: 0x109d5
-  __TEXT.__objc_methtype: 0x4149
-  __TEXT.__objc_stubs: 0xb0c0
+  __TEXT.__unwind_info: 0x2450
+  __TEXT.__objc_classname: 0xdd2
+  __TEXT.__objc_methname: 0x10a79
+  __TEXT.__objc_methtype: 0x4166
+  __TEXT.__objc_stubs: 0xb160
   __DATA_CONST.__got: 0x528
   __DATA_CONST.__const: 0x27f8
   __DATA_CONST.__objc_classlist: 0x2e0

   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xe290
-  __DATA_CONST.__objc_selrefs: 0x3b90
+  __DATA_CONST.__objc_selrefs: 0x3bb8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_classrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x248

   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x9d8
+  __AUTH_CONST.__auth_got: 0x9e0
   __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x624

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3197
-  Symbols:   10671
-  CStrings:  5471
+  Functions: 3203
+  Symbols:   10690
+  CStrings:  5482
 
Symbols:
+ +[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]
+ +[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona].cold.1
+ +[NSString(BRPathAdditions) br_accountSessionOpenErrorInfoPath]
+ +[NSString(BRPathAdditions) br_badFilenameAlternativeName]
+ +[NSString(BRPathAdditions) br_corruptedDBInfoPath]
+ +[NSString(BRPathAdditions) br_currentHomeDir]
+ +[NSString(BRPathAdditions) br_currentHomeDir].cold.1
+ +[NSString(BRPathAdditions) br_currentPersonaIDWithIsDataSeparated:]
+ +[NSString(BRPathAdditions) br_currentSupportDir]
+ +[NSString(BRPathAdditions) br_emptyFilenameAlternativeName]
+ +[NSString(BRPathAdditions) br_pathForDirectory:]
+ +[NSString(BRPathAdditions) br_pathForDirectory:].cold.1
+ +[NSString(BRPathAdditions) br_pathForDirectory:].cold.2
+ +[NSString(BRPathAdditions) br_pathForDirectory:].cold.3
+ +[NSString(BRPathAdditions) br_pathWithDeviceID:fileID:]
+ +[NSString(BRPathAdditions) br_pathWithDeviceID:fileID:].cold.1
+ +[NSString(BRPathAdditions) br_pathWithDeviceID:fileID:].cold.2
+ +[NSString(BRPathAdditions) br_personaGroupDirForFPFS:]
+ +[NSString(BRPathAdditions) br_personaGroupDirForFPFS:].cold.1
+ +[NSString(BRPathAdditions) br_personaGroupDir]
+ +[NSString(BRPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:]
+ +[NSString(BRPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:].cold.1
+ +[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]
+ -[NSString(BRPathAdditions) _br_isExcludedWithMaximumDepth:inFPFS:isFile:]
+ -[NSString(BRPathAdditions) _br_nameWithAddedExtension:makeDotFile:]
+ -[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:]
+ -[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:].cold.1
+ -[NSString(BRPathAdditions) br_compareToStringForHFS:isCaseSensitive:]
+ -[NSString(BRPathAdditions) br_displayFilenameWithExtensionHidden:]
+ -[NSString(BRPathAdditions) br_fileSystemRepresentation]
+ -[NSString(BRPathAdditions) br_isAbsolutePath]
+ -[NSString(BRPathAdditions) br_isDocumentTooLargeForUpload:maxUploadDocumentSize:]
+ -[NSString(BRPathAdditions) br_isEqualToStringForHFS:isCaseSensitive:]
+ -[NSString(BRPathAdditions) br_isExcludedButPreservedAtLogOutWithFilenames:extensions:]
+ -[NSString(BRPathAdditions) br_isExcludedFromSyncInFPFSIsFile:]
+ -[NSString(BRPathAdditions) br_isExcludedWithMaximumDepth:]
+ -[NSString(BRPathAdditions) br_isInPackage]
+ -[NSString(BRPathAdditions) br_isPackageRoot]
+ -[NSString(BRPathAdditions) br_isSideFaultName]
+ -[NSString(BRPathAdditions) br_nameIsRepresentableOnHFS]
+ -[NSString(BRPathAdditions) br_pathExtension]
+ -[NSString(BRPathAdditions) br_pathOfPackageRoot]
+ -[NSString(BRPathAdditions) br_pathRelativeToDirectory:]
+ -[NSString(BRPathAdditions) br_pathRelativeToPackageRoot]
+ -[NSString(BRPathAdditions) br_pathRelativeToPath:]
+ -[NSString(BRPathAdditions) br_realpathKeepingLastSymlink]
+ -[NSString(BRPathAdditions) br_realpathKeepingLastSymlink].cold.1
+ -[NSString(BRPathAdditions) br_realpath]
+ -[NSString(BRPathAdditions) br_realpath].cold.1
+ -[NSString(BRPathAdditions) br_representableDirectoryName]
+ -[NSString(BRPathAdditions) br_representableHFSFileNameWithNumber:addedExtension:makeDotFile:]
+ -[NSString(BRPathAdditions) br_safeFileSystemRepresentation]
+ -[NSString(BRPathAdditions) br_sideFaultName]
+ -[NSString(BRPathAdditions) br_sideFaultPath]
+ -[NSString(BRPathAdditions) brc_representableHFSFileNameWithSuffix:addedExtension:makeDotFile:]
+ -[NSString(BRPathAdditions) brc_stringByDeletingPathExtension]
+ -[NSString(BRPathAdditions) removingROSPPrefix]
+ __OBJC_$_CATEGORY_NSString_$_BRPathAdditions
+ __OBJC_$_CLASS_METHODS_NSString(BRPathAdditions|BRCAdditions|CommonBRPathAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSString(BRPathAdditions|BRCAdditions|CommonBRPathAdditions)
+ ___46+[NSString(BRPathAdditions) br_currentHomeDir]_block_invoke
+ ___55+[NSString(BRPathAdditions) br_personaGroupDirForFPFS:]_block_invoke
+ ___67+[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]_block_invoke
+ ___69+[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]_block_invoke
+ _fpfs_path_is_safe_save_temp_file_ext
+ _objc_msgSend$_br_isExcludedWithMaximumDepth:inFPFS:isFile:
+ _objc_msgSend$_br_safeFileSystemRepresentationWithDefaultValue:
+ _objc_msgSend$br_badFilenameAlternativeName
+ _objc_msgSend$br_safeFileSystemRepresentation
+ _objc_msgSend$reason
- +[NSString(BRCPathAdditions) _br_containerPathForDataSeparatedPersona]
- +[NSString(BRCPathAdditions) _br_containerPathForDataSeparatedPersona].cold.1
- +[NSString(BRCPathAdditions) br_accountSessionOpenErrorInfoPath]
- +[NSString(BRCPathAdditions) br_badFilenameAlternativeName]
- +[NSString(BRCPathAdditions) br_corruptedDBInfoPath]
- +[NSString(BRCPathAdditions) br_currentHomeDir]
- +[NSString(BRCPathAdditions) br_currentHomeDir].cold.1
- +[NSString(BRCPathAdditions) br_currentPersonaIDWithIsDataSeparated:]
- +[NSString(BRCPathAdditions) br_currentSupportDir]
- +[NSString(BRCPathAdditions) br_emptyFilenameAlternativeName]
- +[NSString(BRCPathAdditions) br_pathForDirectory:]
- +[NSString(BRCPathAdditions) br_pathForDirectory:].cold.1
- +[NSString(BRCPathAdditions) br_pathForDirectory:].cold.2
- +[NSString(BRCPathAdditions) br_pathForDirectory:].cold.3
- +[NSString(BRCPathAdditions) br_pathWithDeviceID:fileID:]
- +[NSString(BRCPathAdditions) br_pathWithDeviceID:fileID:].cold.1
- +[NSString(BRCPathAdditions) br_pathWithDeviceID:fileID:].cold.2
- +[NSString(BRCPathAdditions) br_personaGroupDirForFPFS:]
- +[NSString(BRCPathAdditions) br_personaGroupDirForFPFS:].cold.1
- +[NSString(BRCPathAdditions) br_personaGroupDir]
- +[NSString(BRCPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:]
- +[NSString(BRCPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:].cold.1
- +[NSString(BRCPathAdditions) br_supportDirForPersona:dataSeparated:]
- -[NSString(BRCPathAdditions) _br_nameWithAddedExtension:makeDotFile:]
- -[NSString(BRCPathAdditions) br_compareToStringForHFS:isCaseSensitive:]
- -[NSString(BRCPathAdditions) br_displayFilenameWithExtensionHidden:]
- -[NSString(BRCPathAdditions) br_fileSystemRepresentation]
- -[NSString(BRCPathAdditions) br_isAbsolutePath]
- -[NSString(BRCPathAdditions) br_isDocumentTooLargeForUpload:maxUploadDocumentSize:]
- -[NSString(BRCPathAdditions) br_isEqualToStringForHFS:isCaseSensitive:]
- -[NSString(BRCPathAdditions) br_isExcludedButPreservedAtLogOutWithFilenames:extensions:]
- -[NSString(BRCPathAdditions) br_isExcludedWithMaximumDepth:]
- -[NSString(BRCPathAdditions) br_isInPackage]
- -[NSString(BRCPathAdditions) br_isPackageRoot]
- -[NSString(BRCPathAdditions) br_isSideFaultName]
- -[NSString(BRCPathAdditions) br_nameIsRepresentableOnHFS]
- -[NSString(BRCPathAdditions) br_pathExtension]
- -[NSString(BRCPathAdditions) br_pathOfPackageRoot]
- -[NSString(BRCPathAdditions) br_pathRelativeToDirectory:]
- -[NSString(BRCPathAdditions) br_pathRelativeToPackageRoot]
- -[NSString(BRCPathAdditions) br_pathRelativeToPath:]
- -[NSString(BRCPathAdditions) br_realpathKeepingLastSymlink]
- -[NSString(BRCPathAdditions) br_realpathKeepingLastSymlink].cold.1
- -[NSString(BRCPathAdditions) br_realpath]
- -[NSString(BRCPathAdditions) br_realpath].cold.1
- -[NSString(BRCPathAdditions) br_representableDirectoryName]
- -[NSString(BRCPathAdditions) br_representableHFSFileNameWithNumber:addedExtension:makeDotFile:]
- -[NSString(BRCPathAdditions) br_sideFaultName]
- -[NSString(BRCPathAdditions) br_sideFaultPath]
- -[NSString(BRCPathAdditions) brc_representableHFSFileNameWithSuffix:addedExtension:makeDotFile:]
- -[NSString(BRCPathAdditions) brc_stringByDeletingPathExtension]
- -[NSString(BRCPathAdditions) removingROSPPrefix]
- GCC_except_table34
- __OBJC_$_CATEGORY_NSString_$_BRCPathAdditions
- __OBJC_$_CLASS_METHODS_NSString(BRCPathAdditions|BRCAdditions|CommonBRPathAdditions)
- __OBJC_$_INSTANCE_METHODS_NSString(BRCPathAdditions|BRCAdditions|CommonBRPathAdditions)
- ___47+[NSString(BRCPathAdditions) br_currentHomeDir]_block_invoke
- ___56+[NSString(BRCPathAdditions) br_personaGroupDirForFPFS:]_block_invoke
- ___68+[NSString(BRCPathAdditions) br_supportDirForPersona:dataSeparated:]_block_invoke
- ___70+[NSString(BRCPathAdditions) _br_containerPathForDataSeparatedPersona]_block_invoke
CStrings:
+ "+[NSString(BRPathAdditions) _br_containerPathForDataSeparatedPersona]"
+ "+[NSString(BRPathAdditions) br_currentHomeDir]"
+ "+[NSString(BRPathAdditions) br_pathForDirectory:]"
+ "+[NSString(BRPathAdditions) br_pathWithDeviceID:fileID:]"
+ "+[NSString(BRPathAdditions) br_personaGroupDirForFPFS:]"
+ "+[NSString(BRPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:]"
+ "+[NSString(BRPathAdditions) br_supportDirForPersona:dataSeparated:]"
+ "-[NSString(BRPathAdditions) _br_safeFileSystemRepresentationWithDefaultValue:]"
+ "-[NSString(BRPathAdditions) br_realpathKeepingLastSymlink]"
+ "-[NSString(BRPathAdditions) br_realpath]"
+ "2720.140.11"
+ "B28@0:8I16B20B24"
+ "BRPathAdditions"
+ "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
+ "[DEBUG] Got unexpected exception %@. rethrow%@"
+ "_br_isExcludedWithMaximumDepth:inFPFS:isFile:"
+ "_br_safeFileSystemRepresentationWithDefaultValue:"
+ "br_isExcludedFromSyncInFPFSIsFile:"
+ "br_safeFileSystemRepresentation"
+ "r*24@0:8@16"
+ "reason"
- "+[NSString(BRCPathAdditions) _br_containerPathForDataSeparatedPersona]"
- "+[NSString(BRCPathAdditions) br_currentHomeDir]"
- "+[NSString(BRCPathAdditions) br_pathForDirectory:]"
- "+[NSString(BRCPathAdditions) br_pathWithDeviceID:fileID:]"
- "+[NSString(BRCPathAdditions) br_personaGroupDirForFPFS:]"
- "+[NSString(BRCPathAdditions) br_representableHFSFileNameWithBase:suffix:extension:makeDotFile:]"
- "+[NSString(BRCPathAdditions) br_supportDirForPersona:dataSeparated:]"
- "-[NSString(BRCPathAdditions) br_realpathKeepingLastSymlink]"
- "-[NSString(BRCPathAdditions) br_realpath]"
- "2720.120.29"

```
