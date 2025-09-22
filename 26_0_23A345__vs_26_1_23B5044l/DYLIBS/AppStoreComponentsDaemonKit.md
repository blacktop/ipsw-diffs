## AppStoreComponentsDaemonKit

> `/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit`

```diff

-8.0.36.0.0
-  __TEXT.__text: 0x105eac
+8.1.3.0.0
+  __TEXT.__text: 0x106da0
   __TEXT.__auth_stubs: 0x3ae0
-  __TEXT.__objc_methlist: 0x4600
-  __TEXT.__const: 0x5d10
-  __TEXT.__cstring: 0x955c
+  __TEXT.__objc_methlist: 0x4658
+  __TEXT.__const: 0x5d20
+  __TEXT.__cstring: 0x95fc
   __TEXT.__oslogstring: 0x1c74
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__dlopen_cstrs: 0x8e

   __TEXT.__swift5_assocty: 0x6c8
   __TEXT.__swift5_proto: 0x418
   __TEXT.__swift5_types: 0x21c
-  __TEXT.__swift_as_entry: 0x1d4
-  __TEXT.__swift_as_ret: 0x278
-  __TEXT.__swift5_capture: 0x1794
+  __TEXT.__swift_as_entry: 0x1d8
+  __TEXT.__swift_as_ret: 0x27c
+  __TEXT.__swift5_capture: 0x17a4
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x3820
-  __TEXT.__eh_frame: 0x7dac
+  __TEXT.__unwind_info: 0x3850
+  __TEXT.__eh_frame: 0x7e3c
   __TEXT.__objc_classname: 0x83b
-  __TEXT.__objc_methname: 0x7a5d
-  __TEXT.__objc_methtype: 0x122a
-  __TEXT.__objc_stubs: 0x3880
+  __TEXT.__objc_methname: 0x7bd1
+  __TEXT.__objc_methtype: 0x1244
+  __TEXT.__objc_stubs: 0x3900
   __DATA_CONST.__got: 0xd10
-  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de8
+  __DATA_CONST.__objc_selrefs: 0x1e20
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x1e8
   __AUTH_CONST.__auth_got: 0x1d80
   __AUTH_CONST.__const: 0x5798
-  __AUTH_CONST.__cfstring: 0x33c0
-  __AUTH_CONST.__objc_const: 0x9dd0
+  __AUTH_CONST.__cfstring: 0x34e0
+  __AUTH_CONST.__objc_const: 0x9e30
   __AUTH.__objc_data: 0x1750
   __AUTH.__data: 0x3b8
-  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x1ad0
   __DATA.__bss: 0x5330
   __DATA.__common: 0x80

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F73943C-7DE8-3D35-A9E5-8D2910067739
-  Functions: 4443
-  Symbols:   5990
-  CStrings:  3290
+  UUID: D85ABB55-D150-3496-8F59-61305EA59D42
+  Functions: 4457
+  Symbols:   6008
+  CStrings:  3317
 
Symbols:
+ +[ASCLockupRequest(AppDistributionInstall) _requestWithID:kind:context:appVersionId:distributorId:]
+ -[ASCLockupBatchRequest _initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:]
+ -[ASCLockupBatchRequest countryCodeOverride]
+ -[ASCLockupRequest _lockupRequestWithCountryCodeOverride:]
+ -[ASCLockupRequest countryCodeOverride]
+ -[ASCLockupRequest(AppDistributionInstall) _initWithID:kind:context:appVersionId:distributorId:]
+ -[ASCLockupRequest(AppDistributionInstall) lockupRequestWithAppVersionId:distributorId:]
+ -[ASCLockupRequest(AppDistributionInstall) lockupRequestWithCountryCodeOverride:]
+ _OBJC_IVAR_$_ASCLockupBatchRequest._countryCodeOverride
+ _OBJC_IVAR_$_ASCLockupRequest._countryCodeOverride
+ __OBJC_$_CLASS_METHODS_ASCLockupRequest(AppDistribution|AppDistributionInstall|ForOverlaysOnly|MediaClientID|PlatformOverride)
+ __OBJC_$_INSTANCE_METHODS_ASCLockupRequest(AppDistribution|AppDistributionInstall|ForOverlaysOnly|MediaClientID|PlatformOverride)
+ ___block_descriptor_73_e8_32s40s48s56s64s_e38_v32?0"ASCPair"8"NSMutableSet"16^B24ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_initWithID:kind:context:appVersionId:distributorId:
+ _objc_msgSend$_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:
+ _objc_msgSend$_lockupRequestWithCountryCodeOverride:
+ _objc_msgSend$countryCodeOverride
+ _objc_msgSend$lockupRequestWithAppVersionId:distributorId:
- -[ASCLockupBatchRequest _initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:]
- __OBJC_$_CLASS_METHODS_ASCLockupRequest(AppDistribution|ForOverlaysOnly|MediaClientID|PlatformOverride)
- __OBJC_$_INSTANCE_METHODS_ASCLockupRequest(AppDistribution|ForOverlaysOnly|MediaClientID|PlatformOverride)
- ___block_descriptor_65_e8_32s40s48s56s_e38_v32?0"ASCPair"8"NSMutableSet"16^B24ls32l8s40l8s48l8s56l8
- __swift_FORCE_LOAD_$_swiftSpatial
- __swift_FORCE_LOAD_$_swiftSpatial_$_AppStoreComponentsDaemonKit
- _objc_msgSend$_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:
CStrings:
+ "@56@0:8@16@24@32@40@48"
+ "@76@0:8@16@24@32@40B48@52@60@68"
+ "Requests with different countryCodeOverride options cannot be included in batch request: %@ != %@"
+ "T@\"NSString\",R,C,N,V_countryCodeOverride"
+ "_countryCodeOverride"
+ "_initWithID:kind:context:appVersionId:distributorId:"
+ "_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:"
+ "_lockupRequestWithCountryCodeOverride:"
+ "_requestWithID:kind:context:appVersionId:distributorId:"
+ "countryCodeOverride"
+ "distributionChannel"
+ "extend"
+ "lockupRequestWithAppVersionId:distributorId:"
+ "lockupRequestWithCountryCodeOverride:"
+ "native"
+ "seed"
+ "setAppDistributionCountryCodeOverride:"
+ "version"
+ "web"
+ "with"
- "@68@0:8@16@24@32@40B48@52@60"
- "_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:"
- "production"

```
