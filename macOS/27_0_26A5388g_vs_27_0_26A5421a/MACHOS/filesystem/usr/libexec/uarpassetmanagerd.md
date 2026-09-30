## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x2ebbc
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x1494
-  __TEXT.__cstring: 0x3040
-  __TEXT.__oslogstring: 0x1acc
-  __TEXT.__objc_methname: 0x2ee8
+1587.1.3.0.0
+  __TEXT.__text: 0x2faa8
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x2920
+  __TEXT.__objc_methlist: 0x14dc
+  __TEXT.__cstring: 0x3181
+  __TEXT.__oslogstring: 0x1afb
+  __TEXT.__objc_methname: 0x3045
   __TEXT.__objc_classname: 0x341
-  __TEXT.__objc_methtype: 0x894
+  __TEXT.__objc_methtype: 0x897
   __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__unwind_info: 0x3f8
-  __DATA_CONST.__const: 0x2c58
-  __DATA_CONST.__cfstring: 0x2f60
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__const: 0x2cd8
+  __DATA_CONST.__cfstring: 0x3020
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x1a0
-  __DATA.__objc_const: 0x3090
-  __DATA.__objc_selrefs: 0xc08
-  __DATA.__objc_ivar: 0x19c
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x1a8
+  __DATA.__objc_const: 0x30c0
+  __DATA.__objc_selrefs: 0xc58
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x480
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 516
-  Symbols:   1725
-  CStrings:  1246
+  Functions: 522
+  Symbols:   1750
+  CStrings:  1266
 
Symbols:
+ +[UARPAssetSubscriptioniCloud cacheSubdirectoryForContainerID:developmentEnvironment:]
+ +[UARPAssetSubscriptioniCloud developmentEnvironmentForContainerID:]
+ +[UARPAssetSubscriptioniCloud resolvedContainerIDForContainerID:]
+ -[UARPAssetManagerServiceInstanceMobileAsset createSubscriptionForPrimeCache:]
+ -[UARPAssetSubscriptioniCloud developmentEnvironment]
+ -[UARPAssetSubscriptioniCloud initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:developmentEnvironment:domain:]
+ -[UARPAssetSubscriptioniCloud isEqualForAnyDomain:]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-0f055d05674cdcd26b806ef6aa4501f8.o
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._developmentEnvironment
+ _CFPreferencesGetAppBooleanValue
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING_EXT_PRERELEASE
+ _kUARPAssetSubscriptioniCloudEncoderKeyDevelopmentEnvironment
+ _kUARPiCloudCHIPContainerPrefix
+ _kUARPiCloudDefaultPublicContainer
+ _kUARPiCloudDevelopmentEnvironmentDirectory
+ _kUARPiCloudDevelopmentEnvironmentPrefKey
+ _kUARPiCloudManagedPreferencesPath
+ _kUARPiCloudPreferencesDomain
+ _objc_msgSend$containsString:
+ _objc_msgSend$developmentEnvironment
+ _objc_msgSend$developmentEnvironmentForContainerID:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:developmentEnvironment:domain:
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$resolvedContainerIDForContainerID:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$usePallas
- -[UARPAssetSubscriptioniCloud initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:]
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-0ed1b5d7411a1d267bbabd619b9cd5e8.o
- _objc_msgSend$initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:
CStrings:
+ "%s: Failed to read managedPrefs at %@ error %@"
+ "+[UARPAssetSubscriptioniCloud developmentEnvironmentForContainerID:]"
+ "+[UARPAssetSubscriptioniCloud resolvedContainerIDForContainerID:]"
+ "/Library/Managed Preferences/mobile/com.apple.UARPiCloud.plist"
+ "165413ff-a1b0-4e64-b0a0-25ca4fa99e4a"
+ "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ development=%@ domain=%@>"
+ "@60@0:8@16@24@32B40B44B48@52"
+ "TB,R,V_developmentEnvironment"
+ "_developmentEnvironment"
+ "cacheSubdirectoryForContainerID:developmentEnvironment:"
+ "com.apple.UARPiCloud"
+ "com.apple.chip"
+ "containsString:"
+ "development"
+ "developmentEnvironment"
+ "developmentEnvironmentForContainerID:"
+ "initWithContentsOfURL:error:"
+ "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:developmentEnvironment:domain:"
+ "pathWithComponents:"
+ "resolvedContainerIDForContainerID:"
+ "stringByAppendingString:"
+ "substringFromIndex:"
+ "usePallas"
- "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ domain=%@>"
- "@56@0:8@16@24@32B40B44@48"
- "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:"
```
