## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0x291990
-  __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_methlist: 0x1298c
+1837.160.11.0.0
+  __TEXT.__text: 0x292750
+  __TEXT.__auth_stubs: 0x22d0
+  __TEXT.__objc_methlist: 0x129c4
   __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3ed8d
-  __TEXT.__oslogstring: 0x5e116
+  __TEXT.__cstring: 0x3eded
+  __TEXT.__oslogstring: 0x5e1a6
   __TEXT.__gcc_except_tab: 0xeb94
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x55b8
+  __TEXT.__unwind_info: 0x55c8
   __TEXT.__eh_frame: 0x90
-  __TEXT.__objc_classname: 0x116e
-  __TEXT.__objc_methname: 0x472a9
-  __TEXT.__objc_methtype: 0x4824
-  __TEXT.__objc_stubs: 0x27380
-  __DATA_CONST.__got: 0x1008
-  __DATA_CONST.__const: 0x3268
-  __DATA_CONST.__objc_classlist: 0x470
+  __TEXT.__objc_classname: 0x117e
+  __TEXT.__objc_methname: 0x4731c
+  __TEXT.__objc_methtype: 0x4844
+  __TEXT.__objc_stubs: 0x273c0
+  __DATA_CONST.__got: 0x1048
+  __DATA_CONST.__const: 0x3298
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad98
+  __DATA_CONST.__objc_selrefs: 0xadb0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
-  __AUTH_CONST.__auth_got: 0x1108
+  __AUTH_CONST.__auth_got: 0x1178
   __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x326c0
-  __AUTH_CONST.__objc_const: 0x18848
+  __AUTH_CONST.__cfstring: 0x32740
+  __AUTH_CONST.__objc_const: 0x18890
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0x2c98
-  __AUTH.__data: 0xe8
+  __AUTH.__objc_data: 0x2d08
+  __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0x17a4
-  __DATA.__data: 0x1158
+  __DATA.__data: 0x1170
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xa90
+  __DATA.__bss: 0xaa0
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B8D41430-41D2-3065-8E15-38362D2376C7
-  Functions: 7216
-  Symbols:   24158
-  CStrings:  26220
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 58B68ED8-D56A-3374-A10E-5407A3A8A724
+  Functions: 7224
+  Symbols:   24180
+  CStrings:  26239
 
Symbols:
+ -[SecureMobileAssetBundle _graftedContentsContainAppBundle]
+ -[SecureMobileAssetBundle ungraftOrUnmount:force:ungraftingError:]
+ -[SecureMobileAssetBundle ungraftWithForce:error:]
+ -[SecureMobileAssetBundle unmountWithForce:error:]
+ _OBJC_CLASS_$_MAHRSwiftUtils
+ _OBJC_METACLASS_$_MAHRSwiftUtils
+ __CLASS_METHODS_MAHRSwiftUtils
+ __DATA_MAHRSwiftUtils
+ __INSTANCE_METHODS_MAHRSwiftUtils
+ __METACLASS_DATA_MAHRSwiftUtils
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1327
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1373
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1442
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1344
+ ___block_literal_global.1324
+ ___block_literal_global.1326
+ ___block_literal_global.1489
+ ___block_literal_global.1836
+ ___block_literal_global.2417
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_MobileAssetDaemon
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_MobileAssetDaemon
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MobileAssetDaemon
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_MobileAssetDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_MobileAssetDaemon
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_MobileAssetDaemon
+ _objc_msgSend$_graftedContentsContainAppBundle
+ _objc_msgSend$extendEventWithGenerativeModelsInfo:
+ _objc_msgSend$ungraftOrUnmount:force:ungraftingError:
+ _objc_msgSend$ungraftWithForce:error:
+ _objc_msgSend$unmountWithForce:error:
- -[SecureMobileAssetBundle ungraft:]
- -[SecureMobileAssetBundle ungraftOrUnmount:ungraftingError:]
- -[SecureMobileAssetBundle unmount:]
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1324
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1370
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1439
- ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1341
- ___block_literal_global.1321
- ___block_literal_global.1323
- ___block_literal_global.1486
- ___block_literal_global.1821
- _objc_msgSend$ungraft:
- _objc_msgSend$ungraftOrUnmount:ungraftingError:
- _objc_msgSend$unmount:
CStrings:
+ "Applications"
+ "B28@0:8B16^@20"
+ "B36@0:8^q16B24^@28"
+ "Loaded built-in MobileAssetDaemon_Framework May 16 2026 00:10:14"
+ "LuckGSeed"
+ "MAHRSwiftUtils"
+ "RegionCode"
+ "[SMA] Checked %@ for .app bundles: found=%@"
+ "[SMA] Failed to list contents of %@: %@"
+ "[SMA] Ungrafting %@ with force=%@"
+ "[SMA] Unmounting %@ with force=%@"
+ "_graftedContentsContainAppBundle"
+ "app"
+ "com.apple.MobileAsset.HealthReport"
+ "extendEventWithGenerativeModelsInfo:"
+ "ungraftOrUnmount:force:ungraftingError:"
+ "ungraftWithForce:error:"
+ "unmountFlags"
+ "unmountWithForce:error:"
- "Loaded built-in MobileAssetDaemon_Framework Apr 22 2026 22:30:35"
- "LuckF"
- "ungraftOrUnmount:ungraftingError:"
- "unmount:"

```
