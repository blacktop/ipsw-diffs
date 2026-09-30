## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-742.80.2.0.0
-  __TEXT.__text: 0x32dac
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x13d8
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x217e
-  __TEXT.__oslogstring: 0x573b
-  __TEXT.__gcc_except_tab: 0xdc8
+747.100.14.0.1
+  __TEXT.__text: 0x3326c
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x170c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x9a0
-  __TEXT.__objc_classname: 0x282
-  __TEXT.__objc_methname: 0x3978
-  __TEXT.__objc_methtype: 0xa54
-  __TEXT.__objc_stubs: 0x35c0
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x222c
+  __TEXT.__oslogstring: 0x579e
+  __TEXT.__gcc_except_tab: 0xdb8
+  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__objc_classname: 0x2a3
+  __TEXT.__objc_methname: 0x3a4d
+  __TEXT.__objc_methtype: 0xa5a
+  __TEXT.__objc_stubs: 0x35a0
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__const: 0xcd8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe0
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0x2690
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__objc_const: 0x2158
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14c
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x10
+  __DATA.__objc_ivar: 0x150
+  __DATA.__data: 0x4f8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_ivar: 0x2c
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0xc

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 737
-  Symbols:   1039
-  CStrings:  1681
+  Functions: 748
+  Symbols:   1055
+  CStrings:  1695
 
Symbols:
+ _CFNumberGetValue
+ _CacheDeleteGetPendingStorageThreshold
+ _CallCacheDPrivate
+ _GetAPFSVolumeRole
+ _IOObjectConformsTo
+ _IORegistryEntryGetParentEntry
+ _fgetattrlist
+ _isSpecialAPFSVolume
+ _isVolumeSpecial
+ _statfs_ext
+ _strrchr
+ _volumeSupportsEAPFS
- _APFSVolumeRole
CStrings:
+ "\x1c\x11"
+ "@92@0:8@16@24@32@40@48@56@64B72B76B80@84"
+ "AppleAPFSSnapshot"
+ "AppleAPFSVolume"
+ "CacheDeletePrivateClientProtocol"
+ "Failed to get pending storage threshold: %@"
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
+ "clientGetPendingStorageThreshold:replyBlock:"
+ "com.apple.cache_delete.private"
+ "groupContainerIdentifiers"
+ "initWithBundleRecords:identifier:groupIdentifiers:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
+ "setBundleIdentifiers:"
+ "setGroupContainerIdentifiers:"
+ "specialVolume && !AllowSpecialVolume"
+ "statfs %s (%s)"
+ "statfs_ext failed for %@ : %s"
+ "v16@?0@\"<CacheDeletePrivateClientProtocol>\"8"
- "\x1b\x11"
- "@76@0:8@16@24@32@40@48B56B60B64@68"
- "APFSVolumeRole error for %s"
- "T@\"NSMutableSet\",&,N,V_bundleRecords"
- "_bundleRecords"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "appCacheWithRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "bundleRecords"
- "groupCache:"
- "groupContainerURLs"
- "initWithBundleRecords:identifier:dataContainerURL:userManagedAssetsURL:personaUniqueString:cacheDeleteVolume:isDataseparated:isPlaceholder:isPlugin:telemetry:"
- "mountPointFromPath %s (%s)"
- "queryVolumeProperties failed for %@ : %s"
- "setBundleRecords:"

```
