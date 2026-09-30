## SiriSuggestionsIntelligence

> `/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence`

```diff

-3401.8.1.0.0
-  __TEXT.__text: 0x839c4
-  __TEXT.__auth_stubs: 0x1e50
+3401.14.1.0.0
+  __TEXT.__text: 0x8873c
+  __TEXT.__auth_stubs: 0x1f00
   __TEXT.__objc_methlist: 0x17c
-  __TEXT.__const: 0x77b6
-  __TEXT.__cstring: 0x3151
-  __TEXT.__swift5_typeref: 0x2c03
-  __TEXT.__constg_swiftt: 0x2c2c
-  __TEXT.__swift5_reflstr: 0x167d
-  __TEXT.__swift5_fieldmd: 0x2250
+  __TEXT.__const: 0x7b26
+  __TEXT.__cstring: 0x31f1
+  __TEXT.__swift5_typeref: 0x2c6b
+  __TEXT.__oslogstring: 0x2063
+  __TEXT.__constg_swiftt: 0x2c94
+  __TEXT.__swift5_reflstr: 0x16cd
+  __TEXT.__swift5_fieldmd: 0x22f4
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__oslogstring: 0x1f7c
-  __TEXT.__swift5_proto: 0x74c
-  __TEXT.__swift5_types: 0x2e8
+  __TEXT.__swift5_proto: 0x78c
+  __TEXT.__swift5_types: 0x2f4
   __TEXT.__swift5_capture: 0x33c
   __TEXT.__swift5_protos: 0x88
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x2bb8
-  __TEXT.__eh_frame: 0x5328
+  __TEXT.__unwind_info: 0x2d30
+  __TEXT.__eh_frame: 0x5590
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xdcf
+  __TEXT.__objc_methname: 0xdd2
   __TEXT.__objc_methtype: 0x2c4
-  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__got: 0x660
   __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_protorefs: 0x48
-  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__auth_got: 0xf80
   __AUTH_CONST.__auth_ptr: 0x688
-  __AUTH_CONST.__const: 0x4dd8
-  __AUTH_CONST.__objc_const: 0x4c10
-  __AUTH.__objc_data: 0x448
-  __AUTH.__data: 0x1368
-  __DATA.__data: 0x1600
-  __DATA.__bss: 0x7e00
-  __DATA.__common: 0x60
+  __AUTH_CONST.__const: 0x4fb8
+  __AUTH_CONST.__objc_const: 0x4be8
+  __AUTH.__objc_data: 0x498
+  __AUTH.__data: 0x1488
+  __DATA.__data: 0x17d0
+  __DATA.__bss: 0x8580
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1c8
-  __DATA_DIRTY.__data: 0x27d0
+  __DATA_DIRTY.__data: 0x26f0
   __DATA_DIRTY.__bss: 0x5700
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3927
-  Symbols:   1053
-  CStrings:  642
+  Functions: 4064
+  Symbols:   1097
+  CStrings:  651
 
Symbols:
+ _kMRMediaRemoteMediaTypeVideo
+ _kMRMediaRemoteMediaTypeAudio
+ _kMRMediaRemoteMediaTypeMusic
+ _objc_release_x9
+ _objc_retain_x27
+ _kMRMediaRemoteMediaTypePodcast
+ _kMRMediaRemoteMediaTypeAudioBook
CStrings:
+ "Got disabledApps blocklist as: %!s(MISSING)"
+ "_TtCO27SiriSuggestionsIntelligence27SiriSuggestionsIntelligence32PreFetchedAccountDetailsProvider"
+ "Extracted account details as: %!s(MISSING)"
+ "BiomeLatestEventProcessor: Latest event: %!s(MISSING) at: %!f(MISSING)"
+ "music"
+ "iCloud account does not have a creation date"
+ "Apple Vision Pro"
+ "Unable to get disabledApps blocklist"
+ "LocationService:: Got Location as: %!s(MISSING)"
+ "accountCreatedDate"
+ "clockOverride"
+ "no OSVersion or PrerequisiteOSVersion found in assets"
+ "Successfully decoded payload as: \n\n%!s(MISSING)\n\n"
+ "AccountDetails{devices: "
+ "itemMediaSubtype"
+ "Unknown device model: %!s(MISSING)"
+ "[warning] DeviceFeatureExtractor: No OS version available. Assuming the latest build is already installed"
+ "[warning] No FeatureField for interaction"
+ "Created FeatureService with:\ncontextualExtractors: \n%!s(MISSING),\nsuggestionFeatureExtractors: \n%!s(MISSING),\nactionExtractors: \n%!s(MISSING)"
+ "Extracted features for engagement estimation"
+ "Using endTime as: %!s(MISSING) when querying %!s(MISSING)"
- "   Created FeatureService with: contextualExtractors: %!s(MISSING),\n   suggestionFeatureExtractors: %!s(MISSING),\n   actionExtractors: %!s(MISSING)"
- "Unable to get suggestions blocklist"
- "itemMediaType"
- "Decoded payload as: \n\n%!s(MISSING)\n\n"
- "_TtCO27SiriSuggestionsIntelligence27SiriSuggestionsIntelligence33PreFetechedAccountDetailsProvider"
- "BiomeLatestEventProcessor: Latest event: %!s(MISSING)"
- "No FeatureField for interaction"
- "no OSVersion found"
- "Successfully decoded"
- "Unknown model: %!s(MISSING)"
- "Got suggestions blocklist as: %!s(MISSING)"
- "DeviceFeatureExtractor: No update available. Assuming the latest build is already installed"

```
