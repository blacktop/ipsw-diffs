## siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__info_plist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-3600.34.21.0.0
-  __TEXT.__text: 0x12404
-  __TEXT.__auth_stubs: 0x1050
+3605.20.1.0.0
+  __TEXT.__text: 0x12604
+  __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x2cc
-  __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0x59c
-  __TEXT.__oslogstring: 0xe1f
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0x5cc
+  __TEXT.__oslogstring: 0xdaf
   __TEXT.__objc_methtype: 0x4d9
   __TEXT.__swift5_typeref: 0x3a6
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__info_plist: 0x62f
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x568
   __TEXT.__eh_frame: 0x430
-  __DATA_CONST.__const: 0x830
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x830
-  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_got: 0x840
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x188
   __DATA.__objc_const: 0x8d0
   __DATA.__objc_selrefs: 0x258
   __DATA.__objc_data: 0x480
-  __DATA.__data: 0x8b8
-  __DATA.__common: 0xb0
+  __DATA.__data: 0x8a8
+  __DATA.__common: 0xb8
   __DATA.__bss: 0x180
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/Versions/A/AIMLExperimentationAnalytics

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 448
-  Symbols:   399
-  CStrings:  249
+  Functions: 452
+  Symbols:   398
+  CStrings:  248
 
Symbols:
+ _$s13SiriRemembers0aB20TranscriptForwardingO13stopObservingyyFZ
+ _$s13SiriRemembers0aB20TranscriptForwardingO14startObservingyyFZ
+ _$s13SiriRemembers16InteractionStoreV20purgeLegacyDatabasesyyFZ
+ _$sSo13os_log_type_ta0A0E7defaultABvgZ
- _$s12FeatureFlags0aB3KeyP13SiriRemembersAD0A6ToggleRzrlE9isEnabledSbvg
- _$s13SiriRemembers0aB8FeaturesO12FeatureFlags0dE3KeyAAMc
- _$s13SiriRemembers0aB8FeaturesO30allowTranscriptDonationForwardyA2CmFWC
- _$s13SiriRemembers0aB8FeaturesOAA13FeatureToggleAAWP
- _$s13SiriRemembers0aB8FeaturesOMa
CStrings:
+ "BackgroundManager: purging legacy databases on daemon launch"
+ "com.apple.siriinferenced.startup"
- "allow forward the transcript donation to app.intent"
- "cancelled BackgroundQueue ops, calling xpc_transaction_exit_clean"
- "got SIGTERM signal"
```
