## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-140.26.102.0.0
-  __TEXT.__text: 0x4a268
+140.39.0.0.0
+  __TEXT.__text: 0x4af6c
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x2b14
+  __TEXT.__objc_methlist: 0x2bdc
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x4f95
-  __TEXT.__oslogstring: 0x2754
-  __TEXT.__gcc_except_tab: 0x43c
-  __TEXT.__dlopen_cstrs: 0x10b
-  __TEXT.__unwind_info: 0xe24
-  __TEXT.__objc_classname: 0x70f
-  __TEXT.__objc_methname: 0x83dd
-  __TEXT.__objc_methtype: 0x18bf
-  __TEXT.__objc_stubs: 0x5200
+  __TEXT.__cstring: 0x5047
+  __TEXT.__gcc_except_tab: 0x450
+  __TEXT.__oslogstring: 0x283a
+  __TEXT.__dlopen_cstrs: 0x161
+  __TEXT.__unwind_info: 0xe5c
+  __TEXT.__objc_classname: 0x76e
+  __TEXT.__objc_methname: 0x8549
+  __TEXT.__objc_methtype: 0x18d2
+  __TEXT.__objc_stubs: 0x5320
   __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0xf70
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__const: 0xf88
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8f48
-  __DATA_CONST.__objc_selrefs: 0x1a60
+  __DATA_CONST.__objc_const: 0x9468
+  __DATA_CONST.__objc_selrefs: 0x1ae8
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x3ce0
+  __AUTH_CONST.__cfstring: 0x3d40
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__objc_const: 0x1898
+  __AUTH_CONST.__objc_const: 0x1928
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH.__objc_data: 0x640
+  __AUTH.__objc_data: 0x6e0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x318
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x340
-  __DATA.__data: 0x5e0
-  __DATA.__bss: 0x40
+  __DATA.__objc_classrefs: 0x320
+  __DATA.__objc_superrefs: 0x160
+  __DATA.__objc_ivar: 0x348
+  __DATA.__data: 0x640
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x110
   __DATA_DIRTY.__common: 0xc

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4FE2CC5-7675-378D-B9A7-72758766D55F
-  Functions: 1636
-  Symbols:   5368
-  CStrings:  2762
+  UUID: 60756757-254C-302D-9D9E-74A64F4BDE61
+  Functions: 1663
+  Symbols:   5462
+  CStrings:  2798
 
Symbols:
+ +[PRSBehaviorAggregator shouldUseSharedDataStore]
+ +[PRSBehaviorAggregator supportsPosterCustomization]
+ -[PRSPosterConfigurationCacheProvider .cxx_destruct]
+ -[PRSPosterConfigurationCacheProvider _homeURL]
+ -[PRSPosterConfigurationCacheProvider _lockURL]
+ -[PRSPosterConfigurationCacheProvider _lock_readAtURL:]
+ -[PRSPosterConfigurationCacheProvider _lock_readAtURL:].cold.1
+ -[PRSPosterConfigurationCacheProvider _lock_readAtURL:].cold.2
+ -[PRSPosterConfigurationCacheProvider _lock_removeAtURL:]
+ -[PRSPosterConfigurationCacheProvider _lock_removeAtURL:].cold.1
+ -[PRSPosterConfigurationCacheProvider _lock_setupSharedWorkspaceIfNeeded]
+ -[PRSPosterConfigurationCacheProvider _lock_setupSharedWorkspaceIfNeeded].cold.1
+ -[PRSPosterConfigurationCacheProvider _lock_writeData:atURL:]
+ -[PRSPosterConfigurationCacheProvider _lock_writeData:atURL:].cold.1
+ -[PRSPosterConfigurationCacheProvider initWithCachingReason:]
+ -[PRSPosterConfigurationCacheProvider initWithCachingReason:].cold.1
+ -[PRSPosterConfigurationCacheProvider lastActiveHomePoster]
+ -[PRSPosterConfigurationCacheProvider lastActiveLockPoster]
+ -[PRSPosterConfigurationCacheProvider removeCaches]
+ -[PRSPosterConfigurationCacheProvider setLastActiveHomePoster:]
+ -[PRSPosterConfigurationCacheProvider setLastActiveLockPoster:]
+ _OBJC_CLASS_$_PRSBehaviorAggregator
+ _OBJC_CLASS_$_PRSPosterConfigurationCacheProvider
+ _OBJC_CLASS_$_UMUserManager
+ _OBJC_IVAR_$_PRSPosterConfigurationCacheProvider._baseURL
+ _OBJC_IVAR_$_PRSPosterConfigurationCacheProvider._lock
+ _OBJC_METACLASS_$_PRSBehaviorAggregator
+ _OBJC_METACLASS_$_PRSPosterConfigurationCacheProvider
+ __OBJC_$_CLASS_METHODS_PRSBehaviorAggregator
+ __OBJC_$_CLASS_PROP_LIST_PRSBehaviorAggregator
+ __OBJC_$_INSTANCE_METHODS_PRSPosterConfigurationCacheProvider
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterConfigurationCacheProvider
+ __OBJC_$_PROP_LIST_PRSPosterConfigurationCacheProvider
+ __OBJC_$_PROP_LIST_PRSPosterConfigurationCacheProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterConfigurationCacheProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterConfigurationCacheProviding
+ __OBJC_$_PROTOCOL_REFS_PRSPosterConfigurationCacheProviding
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterConfigurationCacheProvider
+ __OBJC_CLASS_RO_$_PRSBehaviorAggregator
+ __OBJC_CLASS_RO_$_PRSPosterConfigurationCacheProvider
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterConfigurationCacheProviding
+ __OBJC_METACLASS_RO_$_PRSBehaviorAggregator
+ __OBJC_METACLASS_RO_$_PRSPosterConfigurationCacheProvider
+ __OBJC_PROTOCOL_$_PRSPosterConfigurationCacheProviding
+ ___getPBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURLSymbolLoc_block_invoke
+ ___getPBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURLSymbolLoc_block_invoke.cold.1
+ _getPBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURLSymbolLoc.ptr
+ _objc_msgSend$_homeURL
+ _objc_msgSend$_lockURL
+ _objc_msgSend$_lock_readAtURL:
+ _objc_msgSend$_lock_removeAtURL:
+ _objc_msgSend$_lock_setupSharedWorkspaceIfNeeded
+ _objc_msgSend$_lock_writeData:atURL:
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$sharedManager
CStrings:
+ "Error reaching resource at URL. Error: %@, URL: %@"
+ "Error reading data from URL. Error: %@, URL: %@"
+ "Error removing item at URL. Error: %@, URL: %@"
+ "Error setting up shared workspace: %@"
+ "Error writing data to URL. Error: %@, URL: %@"
+ "NSURL *soft_PBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURL(void)"
+ "PBUIWallpaperSharedDirectoryDataStoreSharedDirectoryURL"
+ "PRSBehaviorAggregator"
+ "PRSPosterConfigurationCacheProvider"
+ "PRSPosterConfigurationCacheProvider.m"
+ "PRSPosterConfigurationCacheProviding"
+ "T@\"NSData\",&,N"
+ "_baseURL"
+ "_homeURL"
+ "_lockURL"
+ "_lock_readAtURL:"
+ "_lock_removeAtURL:"
+ "_lock_setupSharedWorkspaceIfNeeded"
+ "_lock_writeData:atURL:"
+ "home"
+ "initWithCachingReason:"
+ "isSharedIPad"
+ "lastActiveHomePoster"
+ "lastActiveLockPoster"
+ "localizedDescription"
+ "lock"
+ "removeCaches"
+ "setLastActiveHomePoster:"
+ "setLastActiveLockPoster:"
+ "sharedManager"
+ "shouldUseSharedDataStore"
+ "supportsPosterCustomization"
+ "v24@0:8@\"NSData\"16"

```
