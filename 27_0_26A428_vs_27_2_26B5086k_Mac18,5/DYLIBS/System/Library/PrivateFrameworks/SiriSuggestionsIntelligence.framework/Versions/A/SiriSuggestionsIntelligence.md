## SiriSuggestionsIntelligence

> `/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/Versions/A/SiriSuggestionsIntelligence`

```diff

-3600.11.7.0.0
-  __TEXT.__text: 0x80f6c
+3605.5.1.0.0
+  __TEXT.__text: 0x81198
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
-  __TEXT.__unwind_info: 0x33c8
+  __TEXT.__unwind_info: 0x33d8
   __TEXT.__eh_frame: 0x52a4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5b18
   __AUTH_CONST.__objc_const: 0x4150
-  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH_CONST.__auth_got: 0xed0
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x418
   __DATA.__data: 0x1448

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset

   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/Versions/A/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriUserSegments.framework/Versions/A/SiriUserSegments
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/Versions/A/SiriUtilities
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4217
-  Symbols:   1763
-  CStrings:  256
+  Functions: 4223
+  Symbols:   1764
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
