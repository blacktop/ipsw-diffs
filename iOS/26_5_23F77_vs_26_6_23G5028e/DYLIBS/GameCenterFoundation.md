## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.5.18.0.0
-  __TEXT.__text: 0x180208
+820.6.4.0.0
+  __TEXT.__text: 0x1805b4
   __TEXT.__auth_stubs: 0x2890
-  __TEXT.__objc_methlist: 0x124b4
-  __TEXT.__cstring: 0x18de0
+  __TEXT.__objc_methlist: 0x124ac
+  __TEXT.__cstring: 0x18df0
   __TEXT.__const: 0x65d8
   __TEXT.__gcc_except_tab: 0x1410
-  __TEXT.__oslogstring: 0xdc5b
+  __TEXT.__oslogstring: 0xdcfb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x1f88

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x73e0
+  __TEXT.__unwind_info: 0x73d8
   __TEXT.__eh_frame: 0x5a40
   __TEXT.__objc_classname: 0x25ad
-  __TEXT.__objc_methname: 0x28a05
+  __TEXT.__objc_methname: 0x289d5
   __TEXT.__objc_methtype: 0x6b82
-  __TEXT.__objc_stubs: 0x158c0
+  __TEXT.__objc_stubs: 0x15880
   __DATA_CONST.__got: 0x1140
   __DATA_CONST.__const: 0x6118
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8660
+  __DATA_CONST.__objc_selrefs: 0x8658
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1458
   __AUTH_CONST.__const: 0x5a30
-  __AUTH_CONST.__cfstring: 0x11680
-  __AUTH_CONST.__objc_const: 0x24ff0
+  __AUTH_CONST.__cfstring: 0x116a0
+  __AUTH_CONST.__objc_const: 0x25020
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2cd0
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0x1068
+  __DATA.__objc_ivar: 0x106c
   __DATA.__data: 0x3b28
   __DATA.__bss: 0x8510
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3912E7D7-B698-3064-AC76-9ED792125FAF
-  Functions: 11048
-  Symbols:   25465
-  CStrings:  13719
+  UUID: E261F80B-CA9F-343B-9588-DA910419EE0C
+  Functions: 11051
+  Symbols:   25468
+  CStrings:  13723
 
Symbols:
+ -[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:].cold.1
+ -[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:].cold.2
+ -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:lastUpdateDate:]
+ -[GKAppMetadata lastUpdateDate]
+ _GKImageCachePathForSubdirectoryAndFilename.cold.1
+ _OBJC_IVAR_$_GKAppMetadata._lastUpdateDate
+ ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.28
+ ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.28.cold.1
+ ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.29
+ ___27-[GKDispatchGroup perform:]_block_invoke.4
+ ___27-[GKDispatchGroup perform:]_block_invoke.4.cold.1
+ ___27-[GKDispatchGroup perform:]_block_invoke.6
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.7
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.7.cold.1
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.8
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.82
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.92
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.92.cold.1
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.93
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.94
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.94.cold.1
+ ___block_literal_global.102
+ ___block_literal_global.202
+ _secureCodedPropertyKeys.onceToken.200
+ _secureCodedPropertyKeys.sSecureCodedKeys.199
- +[GKDispatchGroup waitUntilDone:]
- -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:]
- ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.31
- ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.31.cold.1
- ___107+[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:]_block_invoke.35
- ___27-[GKDispatchGroup perform:]_block_invoke.11
- ___27-[GKDispatchGroup perform:]_block_invoke.9
- ___27-[GKDispatchGroup perform:]_block_invoke.9.cold.1
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.12
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.12.cold.1
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.13
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.78
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.84
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.86
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.88.cold.1
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.89
- ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke.90.cold.1
- ___block_literal_global.193
- ___block_literal_global.21
- ___block_literal_global.29
- ___block_literal_global.98
- _objc_msgSend$containsString:
- _objc_msgSend$waitUntilDone:
- _secureCodedPropertyKeys.onceToken.191
- _secureCodedPropertyKeys.sSecureCodedKeys.190
CStrings:
+ "-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]"
+ ".."
+ "@208@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160@168@176@184@192@200"
+ "Blocked path traversal attempt in image cache filename: %@"
+ "Illegal file cache path for subdirectory: %@, filename: %@"
+ "T@\"NSDate\",R,N,V_lastUpdateDate"
+ "_gkMapAccountsWithBlock: timed out waiting for accountsd after %ds"
+ "_lastUpdateDate"
+ "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:lastUpdateDate:"
+ "lastUpdateDate"
- "+[GKDispatchGroup waitUntilDone:]"
- "../"
- "@200@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120@128@136@144@152@160@168@176@184@192"
- "GKDispatchGroup.m"
- "Illegal file cache path: %@"
- "containsString:"
- "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isVerifiedForAppleSiliconMac:runsOnIntel:isIOSBinaryMacOSCompatible:gameDisplayName:miniGamesDeepLink:isGameGenre:ageRating:gkGameGenres:sizeOnDeviceInBytes:"
- "waitUntilDone:"

```
