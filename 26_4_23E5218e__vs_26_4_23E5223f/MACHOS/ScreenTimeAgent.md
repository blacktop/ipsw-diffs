## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-605.4.16.0.0
-  __TEXT.__text: 0x12ff10
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_stubs: 0x12bc0
-  __TEXT.__objc_methlist: 0xa2c4
-  __TEXT.__const: 0x4dd8
+605.4.17.0.0
+  __TEXT.__text: 0x134050
+  __TEXT.__auth_stubs: 0x23f0
+  __TEXT.__objc_stubs: 0x12ea0
+  __TEXT.__objc_methlist: 0xa2fc
+  __TEXT.__const: 0x5098
   __TEXT.__gcc_except_tab: 0x22d8
-  __TEXT.__cstring: 0xabee
-  __TEXT.__oslogstring: 0x14320
-  __TEXT.__objc_methname: 0x1d997
-  __TEXT.__objc_classname: 0x2cc2
-  __TEXT.__objc_methtype: 0x5e02
-  __TEXT.__constg_swiftt: 0x3290
-  __TEXT.__swift5_typeref: 0x2920
+  __TEXT.__cstring: 0xac2e
+  __TEXT.__oslogstring: 0x14820
+  __TEXT.__objc_methname: 0x1dbe7
+  __TEXT.__objc_classname: 0x2d02
+  __TEXT.__objc_methtype: 0x5e22
+  __TEXT.__constg_swiftt: 0x35f0
+  __TEXT.__swift5_typeref: 0x2d52
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x2059
-  __TEXT.__swift5_fieldmd: 0x1550
-  __TEXT.__swift5_assocty: 0x250
-  __TEXT.__swift5_proto: 0x264
-  __TEXT.__swift5_types: 0x18c
-  __TEXT.__swift5_capture: 0x21f0
+  __TEXT.__swift5_reflstr: 0x2109
+  __TEXT.__swift5_fieldmd: 0x1640
+  __TEXT.__swift5_assocty: 0x2e8
+  __TEXT.__swift5_proto: 0x288
+  __TEXT.__swift5_types: 0x190
+  __TEXT.__swift5_capture: 0x2200
   __TEXT.__swift_as_entry: 0x264
   __TEXT.__swift_as_ret: 0x198
-  __TEXT.__swift5_protos: 0xa8
+  __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x47c8
-  __TEXT.__eh_frame: 0x6198
-  __DATA_CONST.__auth_got: 0x1200
-  __DATA_CONST.__got: 0x1390
-  __DATA_CONST.__auth_ptr: 0x6b0
-  __DATA_CONST.__const: 0x9b60
+  __TEXT.__unwind_info: 0x4838
+  __TEXT.__eh_frame: 0x61d0
+  __DATA_CONST.__auth_got: 0x1208
+  __DATA_CONST.__got: 0x13a0
+  __DATA_CONST.__auth_ptr: 0x6b8
+  __DATA_CONST.__const: 0x9cb0
   __DATA_CONST.__cfstring: 0x4ca0
-  __DATA_CONST.__objc_classlist: 0x6a0
+  __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1eb70
-  __DATA.__objc_selrefs: 0x5768
+  __DATA.__objc_const: 0x1ecc0
+  __DATA.__objc_selrefs: 0x5820
   __DATA.__objc_ivar: 0x814
-  __DATA.__objc_data: 0x4cf8
-  __DATA.__data: 0x7340
+  __DATA.__objc_data: 0x4de8
+  __DATA.__data: 0x7548
   __DATA.__bss: 0x37c0
-  __DATA.__common: 0xd0
+  __DATA.__common: 0xe8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95135138-C4E2-3E18-87EE-66B89322F11D
-  Functions: 6207
-  Symbols:   1351
-  CStrings:  8046
+  UUID: 420EEA7F-39EC-336F-9977-3ECDAE168438
+  Functions: 6269
+  Symbols:   1354
+  CStrings:  8093
 
Symbols:
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ _OBJC_CLASS_$_MOApplication
+ _STBlueprintConfigurationTypeLegacyAppRestrictions
CStrings:
+ "AllowedAppsStore"
+ "Computed blockedApplications: %ld apps"
+ "Computed feature restrictions - iMessage: %{bool}d, iTunes: %{bool}d, News: %{bool}d, Podcasts: %{bool}d, Safari: %{bool}d, FaceTime: %{bool}d, SharePlay: %{bool}d"
+ "Failed to get declarations from blueprint %{public}@: %{public}@"
+ "Finished applying allowed apps & features via ManagedSettings"
+ "Found %ld Allowed Apps & Features configurations in blueprint %s. Expected at most 1. Using merge semantics (union for apps, OR for deny flags), but this may not match UI behavior."
+ "Found %{public}ld Web Content Filter configurations in blueprint %s. Expected at most 1. Using all configurations, but this may not match UI behavior."
+ "Found %{public}lu restrictions blueprints - Agent may be applying more blueprints than shown in the UI"
+ "No Allowed Apps & Features data provided"
+ "Not updating allowed apps data from %s because it does not have any configurations"
+ "Not updating allowed apps data from %s because it is not a restrictions blueprint"
+ "Processing Allowed Apps & Features declaration from configuration %s"
+ "Updated allowed apps data: %ld blocked apps, deny flags - iMessage:%ld iTunes:%ld News:%ld Podcasts:%ld Safari:%ld FaceTime:%ld SharePlay:%ld"
+ "_TtC15ScreenTimeAgent28STAllowedAppsAndFeaturesData"
+ "allowedAppsAndFeatures"
+ "application"
+ "applyAllowedAppsAndFeaturesWithData:"
+ "batchUpdate:"
+ "blockedAppBundleIDs"
+ "declarationsExcludingConfigurationTypes:error:"
+ "denyFaceTime"
+ "denyNews"
+ "denyPodcasts"
+ "denySafari"
+ "denySharePlay"
+ "denyiMessage"
+ "denyiTunes"
+ "faceTime"
+ "media"
+ "news"
+ "payloadAllowChat"
+ "payloadAllowGroupActivity"
+ "payloadAllowNews"
+ "payloadAllowPodcasts"
+ "payloadAllowSafari"
+ "payloadAllowVideoConferencing"
+ "payloadAllowiTunes"
+ "payloadBlacklistedAppBundleIDs"
+ "setBlockedApplications:"
+ "setDenyFaceTime:"
+ "setDenyNews:"
+ "setDenyPodcasts:"
+ "setDenySafari:"
+ "setDenySharePlay:"
+ "setDenyiMessage:"
+ "setDenyiTunes:"
+ "updateFrom:"
+ "v16@?0@\"MOBatchSettingsStore\"8"
- "declarationsWithError:"

```
