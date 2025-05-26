## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2008.60.8.0.0
-  __TEXT.__text: 0x12a2c
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0x790
+2125.102.2.0.0
+  __TEXT.__text: 0x12c14
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x2080
+  __TEXT.__objc_methlist: 0x7b0
   __TEXT.__const: 0x31c
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__objc_methname: 0x2635
-  __TEXT.__cstring: 0x4042
-  __TEXT.__oslogstring: 0x2486
+  __TEXT.__objc_methname: 0x2763
+  __TEXT.__cstring: 0x4152
+  __TEXT.__oslogstring: 0x24d9
   __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methtype: 0x533
-  __TEXT.__constg_swiftt: 0x1cc
+  __TEXT.__objc_methtype: 0x566
+  __TEXT.__constg_swiftt: 0x1d4
   __TEXT.__swift5_typeref: 0xe9
   __TEXT.__swift5_reflstr: 0x89
   __TEXT.__swift5_fieldmd: 0xcc

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x3b4
-  __TEXT.__eh_frame: 0x190
-  __DATA_CONST.__auth_got: 0x648
+  __TEXT.__unwind_info: 0x3c4
+  __TEXT.__eh_frame: 0x198
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x668

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x10e0
-  __DATA.__objc_selrefs: 0x9c8
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x10f0
+  __DATA.__objc_selrefs: 0xa00
   __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_data: 0x3c8
   __DATA.__data: 0x308
   __DATA.__bss: 0x550
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 291
-  Symbols:   266
-  CStrings:  1052
+  Functions: 296
+  Symbols:   269
+  CStrings:  1068
 
Symbols:
+ _objc_opt_respondsToSelector
+ _swift_release_n
+ _swift_retain_n
CStrings:
+ "+[MBMobileInstallation _defaultSubdirectoriesForMCMContainerType:withError:]"
+ "+[MBMobileInstallation defaultSubdirectoriesForMBContainerType:withNestedSubdirectories:]"
+ "-[RestorePostProcess _configureAndIXInstallPlaceholdersInDirectory:isDataSeparated:migratorCache:demotedAppsPlist:]"
+ "-[RestorePostProcess _configureAppPlaceholderAtPath:installType:isDataSeparated:migratorCache:]"
+ "-[RestorePostProcess _createInstallCoordinatorForPlaceholderAtPath:bundleID:installType:isDataSeparated:error:]"
+ "-[RestorePostProcess _installCoordinatorForPlaceholder:bundleID:installType:isDataSeparated:error:]"
+ "-[RestorePostProcess _placeholderAtPath:bundleID:installType:error:]"
+ "@48@0:8@16@24Q32^@40"
+ "@52@0:8@16@24Q32B40^@44"
+ "B44@0:8@16Q24B32@36"
+ "B52@0:8@16@24Q32B40^@44"
+ "IX: Failed to set app asset DRI for  %@: %@"
+ "IX: No placeholder metadata for %@:%@: %@"
+ "IX: Setting app asset DRI for %@ (%lu)"
+ "T@\"NSString\",?,R,C"
+ "_configureAndIXInstallPlaceholdersInDirectory:isDataSeparated:migratorCache:demotedAppsPlist:"
+ "_configureAppPlaceholderAtPath:installType:isDataSeparated:migratorCache:"
+ "_createInstallCoordinatorForPlaceholderAtPath:bundleID:installType:isDataSeparated:error:"
+ "_installCoordinatorForPlaceholder:bundleID:installType:isDataSeparated:error:"
+ "_placeholderAtPath:bundleID:installType:error:"
+ "distributorInfo"
+ "distributorIsThirdParty"
+ "isDataSeparated"
+ "metadataWithError:"
+ "setAppAssetPromiseResponsibleClient:error:"
+ "v44@0:8@16B24@28@36"
- "-[MBMobileInstallation _defaultSubdirectoriesForMCMContainerType:withError:]"
- "-[MBMobileInstallation defaultSubdirectoriesForMBContainerType:withNestedSubdirectories:]"
- "-[RestorePostProcess _configureAndIXInstallPlaceholdersInDirectory:migratorCache:demotedAppsPlist:]"
- "-[RestorePostProcess _configureAppPlaceholderAtPath:installType:migratorCache:]"
- "-[RestorePostProcess _createInstallCoordinatorForPlaceholderAtPath:bundleID:installType:migratorCache:error:]"
- "B40@0:8@16Q24@32"
- "B56@0:8@16@24Q32@40^@48"
- "Failed to fetch the app record for %@: %@"
- "MBExcludedAppTypeFromAppRecord"
- "_configureAndIXInstallPlaceholdersInDirectory:migratorCache:demotedAppsPlist:"
- "_configureAppPlaceholderAtPath:installType:migratorCache:"
- "_createInstallCoordinatorForPlaceholderAtPath:bundleID:installType:migratorCache:error:"
- "v40@0:8@16@24@32"

```
