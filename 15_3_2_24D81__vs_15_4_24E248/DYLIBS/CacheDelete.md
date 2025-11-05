## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete`

```diff

-742.80.2.0.0
-  __TEXT.__text: 0x377f0
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x13d8
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x212d
-  __TEXT.__oslogstring: 0x5528
-  __TEXT.__gcc_except_tab: 0xe34
+747.100.15.0.0
+  __TEXT.__text: 0x37a44
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x16f4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0x216f
+  __TEXT.__oslogstring: 0x555f
+  __TEXT.__gcc_except_tab: 0xe10
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x282
-  __TEXT.__objc_methname: 0x38eb
-  __TEXT.__objc_methtype: 0xa54
-  __TEXT.__objc_stubs: 0x34c0
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__objc_methname: 0x3993
+  __TEXT.__objc_methtype: 0xa5a
+  __TEXT.__objc_stubs: 0x3480
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa8
+  __DATA_CONST.__objc_selrefs: 0x1040
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x580
-  __AUTH_CONST.__const: 0x1110
-  __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0x2690
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__const: 0x1130
+  __AUTH_CONST.__cfstring: 0x1d20
+  __AUTH_CONST.__objc_const: 0x2138
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0x4a0
-  __DATA.__bss: 0x1c0
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x4a8
+  __DATA.__bss: 0x1c8
   __DATA.__common: 0x9
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D309CE0C-EE10-32F4-891A-5E4AEA92BFA4
-  Functions: 774
-  Symbols:   1896
-  CStrings:  1885
+  UUID: AFD70C45-3735-3852-ACE9-72956E6111CE
+  Functions: 782
+  Symbols:   1911
+  CStrings:  1894
 
Symbols:
+ +[AppCache appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:]
+ +[AppCache appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:]
+ -[AppCache bundleIdentifiers]
+ -[AppCache groupContainerIdentifiers]
+ -[AppCache initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:]
+ -[AppCache setBundleIdentifiers:]
+ -[AppCache setGroupContainerIdentifiers:]
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table64
+ GCC_except_table74
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table96
+ OBJC_IVAR_$_AppCache._bundleIdentifiers
+ OBJC_IVAR_$_AppCache._groupContainerIdentifiers
+ _CFNumberGetValue
+ _CacheDeleteGetPendingStorageThreshold
+ _CallCacheDPrivate
+ _GetAPFSVolumeRole
+ _IOObjectConformsTo
+ _IORegistryEntryGetParentEntry
+ __24-[AppCache clearCaches:]_block_invoke.33
+ __CallBlockWithProxy_block_invoke.305
+ ___size_dir_block_invoke
+ __block_literal_global.125
+ __block_literal_global.52
+ __block_literal_global.97
+ _fgetattrlist
+ _isSpecialAPFSVolume
+ _isVolumeSpecial
+ _objc_msgSend$appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:
+ _objc_msgSend$bundleIdentifiers
+ _objc_msgSend$groupContainerIdentifiers
+ _objc_msgSend$initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:
+ _statfs_ext
+ _strrchr
+ _volumeSupportsEAPFS
+ initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:.cdVolFreespace
+ size_dir.onceToken
+ size_dir.set_extended
- +[AppCache appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:]
- +[AppCache appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:]
- -[AppCache bundleRecords]
- -[AppCache groupCache:]
- -[AppCache initWithBundleRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:]
- -[AppCache setBundleRecords:]
- GCC_except_table15
- GCC_except_table31
- GCC_except_table35
- GCC_except_table39
- GCC_except_table46
- GCC_except_table51
- GCC_except_table52
- GCC_except_table63
- GCC_except_table70
- GCC_except_table85
- GCC_except_table90
- GCC_except_table92
- OBJC_IVAR_$_AppCache._bundleRecords
- _APFSVolumeRole
- __24-[AppCache clearCaches:]_block_invoke.34
- __CallBlockWithProxy_block_invoke.299
- __block_literal_global.122
- __block_literal_global.62
- __block_literal_global.92
- __block_literal_global.94
- _objc_msgSend$appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:
- _objc_msgSend$bundleRecords
- _objc_msgSend$groupContainerURLs
- _objc_msgSend$initWithBundleRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:
- _objc_msgSend$lastKnownGroupCacheSize
- _objc_msgSend$setLastKnownGroupCacheSize:
- initWithBundleRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:.cdVolFreespace
CStrings:
+ "@92@0:8@16@24@32@40@48@56@64B72B76B80@84"
+ "AppleAPFSSnapshot"
+ "AppleAPFSVolume"
+ "GetAPFSVolumeRole error for %s"
+ "IOService"
+ "RoleValue"
+ "T@\"NSMutableSet\",&,N,V_bundleIdentifiers"
+ "T@\"NSMutableSet\",&,N,V_groupContainerIdentifiers"
+ "Unable to call fgetattrlist on %@: %d"
+ "_bundleIdentifiers"
+ "_groupContainerIdentifiers"
+ "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "appCacheWithRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "bundleIdentifiers"
+ "com.apple.imagent.cache-delete_fspurgeable"
+ "groupContainerIdentifiers"
+ "initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "setBundleIdentifiers:"
+ "setGroupContainerIdentifiers:"
+ "specialVolume && !AllowSpecialVolume"
+ "statfs %s (%s)"
+ "statfs_ext failed for %@ : %s"
- "@76@0:8@16@24@32@40@48B56B60B64@68"
- "APFSVolumeRole error for %s"
- "T@\"NSMutableSet\",&,N,V_bundleRecords"
- "_bundleRecords"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "bundleRecords"
- "com.apple.imagent.cache-delete"
- "groupCache:"
- "groupContainerURLs"
- "initWithBundleRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "mountPointFromPath %s (%s)"
- "queryVolumeProperties failed for %@ : %s"
- "setBundleRecords:"

```
