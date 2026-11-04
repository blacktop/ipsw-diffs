## SearchAds

> `/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds`

```diff

-557.2.14.0.0
-  __TEXT.__text: 0x144b4
-  __TEXT.__objc_methlist: 0xf7c
-  __TEXT.__const: 0x970
+557.3.10.0.0
+  __TEXT.__text: 0x15960
+  __TEXT.__objc_methlist: 0xfbc
+  __TEXT.__const: 0xba0
   __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__cstring: 0x1166
-  __TEXT.__oslogstring: 0x1102
-  __TEXT.__constg_swiftt: 0x4dc
-  __TEXT.__swift5_typeref: 0x262
-  __TEXT.__swift5_reflstr: 0x100
-  __TEXT.__swift5_fieldmd: 0x260
+  __TEXT.__cstring: 0x1216
+  __TEXT.__oslogstring: 0xfa2
+  __TEXT.__constg_swiftt: 0x588
+  __TEXT.__swift5_typeref: 0x2ea
+  __TEXT.__swift5_reflstr: 0x1f5
+  __TEXT.__swift5_fieldmd: 0x338
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_proto: 0x6c
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x6c8
-  __TEXT.__eh_frame: 0x48
+  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__eh_frame: 0x1a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x390
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x2f0
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x2688
+  __DATA_CONST.__got: 0x330
+  __AUTH_CONST.__const: 0x368
+  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__objc_const: 0x2878
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x808
-  __AUTH.__objc_data: 0x2a0
-  __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x17c
-  __DATA.__data: 0x150
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH.__objc_data: 0x460
+  __AUTH.__data: 0x1b8
+  __DATA.__objc_ivar: 0x178
+  __DATA.__data: 0x1f8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x740

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem
   - /System/Library/PrivateFrameworks/APFoundation.framework/APFoundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore
   - /System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 595
-  Symbols:   273
-  CStrings:  279
+  Functions: 667
+  Symbols:   277
+  CStrings:  267
 
Symbols:
+ _OBJC_CLASS_$_APAnalytics
+ _OBJC_CLASS_$__TtC9SearchAds22ADClientSettingsConfig
+ _OBJC_CLASS_$__TtC9SearchAds28ADClientSettingsBaseSettings
+ _OBJC_METACLASS_$__TtC9SearchAds22ADClientSettingsConfig
+ _OBJC_METACLASS_$__TtC9SearchAds28ADClientSettingsBaseSettings
+ _objc_retain_x27
+ _objc_retain_x9
+ _swift_allocBox
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
- _ADCopyDataFromKeychain
- _ADWriteDataToKeychain
- _OBJC_CLASS_$_ADClientSettingsRequest
- _OBJC_CLASS_$_ADClientSettingsResponse
- _objc_retain_x10
- _swift_bridgeObjectRelease_n
CStrings:
+ "ADClientSettingsConfig: no config found in ConfigurationNode.json, falling back to default settings"
+ "ADClientSettingsConfig: retrieved config from ConfigurationNode.json"
+ "ClientSettingsConfigInit"
+ "SearchAds.ADClientSettingsBaseSettings"
+ "SearchAdsSettingsInit"
+ "[%@]: Returning:"
+ "didLoadConfig"
+ "durationMilliseconds"
+ "searchads.clientSettingsLoad"
- "ADClientSettingsKeychainKey"
- "Client Settings has not expired. (%f < %f)"
- "Client Settings is being forced to expire"
- "ClientSettingsForceExpire"
- "ClientSettingsRetrieval"
- "ClientSettingsServerRetrieval"
- "Current Client Settings: %@"
- "Error saving Client Settings to keychain: %d"
- "Received response for ADClientSettingsRequest: %@"
- "[%@]: ADClientSettingsRequest failed with error: %@."
- "[%@]: After applyClientSettings:"
- "[%@]: Properties at init:"
- "cacheHit"
- "flora"
- "iris1"
- "iris2"
- "metis"
- "reason=%{public}s enableTelemetry=YES"
- "serverError"
- "serverSuccess"
- "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
```
