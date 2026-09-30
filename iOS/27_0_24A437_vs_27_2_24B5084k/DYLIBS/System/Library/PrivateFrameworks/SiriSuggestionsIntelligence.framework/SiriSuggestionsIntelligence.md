## SiriSuggestionsIntelligence

> `/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence`

```diff

-3600.11.7.0.0
-  __TEXT.__text: 0x7fca0
+3605.5.1.0.0
+  __TEXT.__text: 0x7fec0
   __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0x9100
+  __TEXT.__const: 0x9110
   __TEXT.__swift5_typeref: 0x2d7f
-  __TEXT.__oslogstring: 0x20b3
-  __TEXT.__constg_swiftt: 0x28bc
+  __TEXT.__oslogstring: 0x2133
+  __TEXT.__constg_swiftt: 0x28c8
   __TEXT.__swift5_reflstr: 0x149c
   __TEXT.__swift5_fieldmd: 0x2158
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__cstring: 0xd1c
+  __TEXT.__cstring: 0xd3c
   __TEXT.__swift5_proto: 0x794
   __TEXT.__swift5_types: 0x2e0
   __TEXT.__swift_as_entry: 0x1d4

   __TEXT.__swift5_capture: 0x8f8
   __TEXT.__swift5_protos: 0x8c
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x33b8
+  __TEXT.__unwind_info: 0x33c0
   __TEXT.__eh_frame: 0x5284
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5b18
   __AUTH_CONST.__objc_const: 0x4150
-  __AUTH_CONST.__auth_got: 0x1038
+  __AUTH_CONST.__auth_got: 0x1050
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x578
   __DATA.__data: 0x1458

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4213
-  Symbols:   1793
-  CStrings:  256
+  Functions: 4219
+  Symbols:   1794
+  CStrings:  258
 
Symbols:
+ _TCCAccessCopyBundleIdentifiersDisabledForService
CStrings:
+ "AppIdValidator: AppExclusions FF disabled, no LFTA preference found"
+ "AppIdValidator: AppExclusions FF enabled, got %ld disabled apps from TCC"
+ "AppIdValidator: LFTA fallback, got %ld disabled apps"
+ "kTCCServiceSiriAccess"
- "Got disabledApps blocklist as: %s"
- "Unable to get disabledApps blocklist"
```
