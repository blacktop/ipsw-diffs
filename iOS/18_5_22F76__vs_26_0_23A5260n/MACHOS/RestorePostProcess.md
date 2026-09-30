## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2624.120.12.0.0
-  __TEXT.__text: 0x15754
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_stubs: 0x2700
-  __TEXT.__objc_methlist: 0xd24
-  __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x3c65
-  __TEXT.__objc_methname: 0x2f72
+2877.0.0.0.0
+  __TEXT.__text: 0x121e8
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x38b5
+  __TEXT.__objc_methname: 0x2d44
   __TEXT.__objc_classname: 0x128
-  __TEXT.__objc_methtype: 0x61f
-  __TEXT.__oslogstring: 0x25b7
+  __TEXT.__objc_methtype: 0x5f9
+  __TEXT.__oslogstring: 0x2466
   __TEXT.__gcc_except_tab: 0x314
-  __TEXT.__constg_swiftt: 0x18c
-  __TEXT.__swift5_typeref: 0xe4
-  __TEXT.__swift5_reflstr: 0x8c
-  __TEXT.__swift5_fieldmd: 0xf4
+  __TEXT.__constg_swiftt: 0x12c
+  __TEXT.__swift5_typeref: 0x78
+  __TEXT.__swift5_reflstr: 0x74
+  __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x28
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x490
-  __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__cfstring: 0x1000
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__cfstring: 0xf00
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1420
-  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_const: 0x1348
+  __DATA.__objc_selrefs: 0xc80
   __DATA.__objc_ivar: 0x6c
-  __DATA.__objc_data: 0x560
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x600
+  __DATA.__objc_data: 0x490
+  __DATA.__data: 0x298
+  __DATA.__bss: 0x200
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AEA801BC-752D-3A38-B053-7FD2A8F58B05
-  Functions: 391
-  Symbols:   318
-  CStrings:  1292
+  UUID: 9453EA7D-9490-3391-892F-2C5D56CEB3C1
+  Functions: 318
+  Symbols:   296
+  CStrings:  1227
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _CFPreferencesCopyAppValue
- _CFPreferencesGetAppBooleanValue
- _NSFileGroupOwnerAccountName
- _NSFileOwnerAccountName
- __swiftEmptySetSingleton
- __swiftImmortalRefCount
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _bzero
- _memmove
- _objc_allocWithZone
- _swift_allocObject
- _swift_beginAccess
- _swift_endAccess
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_isUniquelyReferenced_nonNull_native
- _swift_once
- _swift_release_n
- _swift_retain_n
- _swift_slowAlloc
CStrings:
+ "-[MBMobileInstallation _enumerateAppsWithEnumerationOptions:to:persona:]"
+ "B44@0:8@16@24B32Q36"
+ "Db"
+ "Df"
+ "E "
+ "F "
+ "I "
+ "_configurePlaceholderIPA:personaIdentifier:isDataSeparated:installType:"
+ "_enumerateAppsWithEnumerationOptions:to:persona:"
+ "_registerPlaceholdersForBackgroundRestore:personaIdentifier:isDataSeparated:demotedAppsPlist:"
+ "userAppsForPersona:error:"
+ "v40@0:8Q16@24@32"
+ "v44@0:8@16@24B32@36"
- "+[MBServiceAccount serviceAccountFromPreferences]"
- "-[MBMobileInstallation _enumerateAppsWithEnumerationOptions:to:persona:dataSeparatedBundleIDs:]"
- "-[RestorePostProcess _writeMigratorCache:config:error:]"
- "-migratorCache.plist"
- "/var/mobile/Library/Caches/com.apple.migrationpluginwrapper"
- "@20@0:8B16"
- "@40@0:8@16@24^@32"
- "AccountID"
- "B52@0:8@16@24B32Q36@44"
- "ChunkStoreURL"
- "DEBUG"
- "DEFAULT"
- "EMPTY"
- "ERROR"
- "FAULT"
- "Failed to create directory at %{public}@: %{public}@"
- "Failed to remove existing MigratorCache at %{public}@: %{public}@"
- "Failed to write MigratorCache at %{public}@: %{public}@"
- "INFO"
- "Loaded account properties from preferences, enabled:%d"
- "No Migrator cache at "
- "ServiceURL"
- "Skipping MigratorCache write for %{public}@"
- "T@\"NSSet\",N,C"
- "UseMockChunkStore"
- "Writing MigratorCache for %{public}@ at %{public}@: %{public}@"
- "_TtC18RestorePostProcess13MigratorCache"
- "_configurePlaceholderIPA:personaIdentifier:isDataSeparated:installType:migratorCache:"
- "_enumerateAppsWithEnumerationOptions:to:persona:dataSeparatedBundleIDs:"
- "_registerPlaceholdersForBackgroundRestore:personaIdentifier:isDataSeparated:migratorCache:demotedAppsPlist:"
- "_visitContainerDependenciesAndFilterDuplicates:"
- "_writeMigratorCache:config:error:"
- "accountID"
- "addBundleID:"
- "appWithBundleID:"
- "bundleIDs"
- "cacheFileNameWithPersonaIdentifier:"
- "chunkStorePath"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "handleFailureInFunction:file:lineNumber:description:"
- "initWithString:"
- "initWithUrl:error:"
- "isEmpty"
- "lock"
- "migratorCacheURL"
- "migratorCacheURLFor:"
- "mobile"
- "nil personal persona: %@"
- "personalPersonaWithError:"
- "removeItemAtURL:error:"
- "serviceAccountFromPreferences"
- "servicePath"
- "setBundleIDs:"
- "uniqueContainers"
- "userAppsForPersona:dataSeparatedBundleIDs:error:"
- "v48@0:8Q16@24@32@40"
- "v52@0:8@16@24B32@36@44"
- "writeTo:error:"

```
