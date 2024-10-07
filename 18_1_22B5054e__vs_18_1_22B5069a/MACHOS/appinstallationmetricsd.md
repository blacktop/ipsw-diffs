## appinstallationmetricsd

> `/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd`

```diff

-2.1.9.0.0
-  __TEXT.__text: 0x28dd8
-  __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x1170
+2.1.10.0.0
+  __TEXT.__text: 0x2b4e0
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_methlist: 0xd0
+  __TEXT.__const: 0x1304
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xfa1
-  __TEXT.__constg_swiftt: 0x7e8
-  __TEXT.__swift5_typeref: 0x85f
-  __TEXT.__swift5_reflstr: 0x3a6
-  __TEXT.__swift5_fieldmd: 0x4f8
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__objc_methname: 0x8d4
-  __TEXT.__oslogstring: 0x890
-  __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x78
+  __TEXT.__cstring: 0x1061
+  __TEXT.__constg_swiftt: 0x848
+  __TEXT.__swift5_typeref: 0x85b
+  __TEXT.__swift5_reflstr: 0x3e9
+  __TEXT.__swift5_fieldmd: 0x560
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_assocty: 0x150
+  __TEXT.__objc_methname: 0x8e8
+  __TEXT.__oslogstring: 0x980
+  __TEXT.__swift5_proto: 0xd8
+  __TEXT.__swift5_types: 0x84
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0x1b4
-  __TEXT.__swift5_capture: 0x220
+  __TEXT.__swift5_capture: 0x214
+  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0xaa8
-  __TEXT.__eh_frame: 0x1db0
-  __DATA_CONST.__auth_got: 0xa40
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__auth_ptr: 0x408
-  __DATA_CONST.__const: 0x11d0
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__unwind_info: 0xb88
+  __TEXT.__eh_frame: 0x1ef0
+  __DATA_CONST.__auth_got: 0xaa0
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__auth_ptr: 0x410
+  __DATA_CONST.__const: 0x1368
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1090
-  __DATA.__objc_selrefs: 0x248
-  __DATA.__objc_data: 0x318
-  __DATA.__data: 0x1140
-  __DATA.__bss: 0x1640
+  __DATA.__objc_const: 0x1128
+  __DATA.__objc_selrefs: 0x258
+  __DATA.__objc_data: 0x3f8
+  __DATA.__data: 0x11a0
+  __DATA.__bss: 0x1a40
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 705
-  Symbols:   556
-  CStrings:  318
+  Functions: 766
+  Symbols:   573
+  CStrings:  328
 
Symbols:
+ _$sSS_5radix9uppercaseSSx_SiSbtcSzRzlufC
+ _$sSe4fromxs7Decoder_p_tKcfCTq
+ _$sSeMp
+ _$ss28SingleValueDecodingContainerP6decodeyS2SmKFTj
+ _$ss28SingleValueDecodingContainerP6decodeyqd__qd__mKSeRd__lFTj
+ _$ss28SingleValueEncodingContainerP6encodeyySSKFTj
+ _$ss28SingleValueEncodingContainerP6encodeyyqd__KSERd__lFTj
+ _$ss6UInt32VN
+ _$ss6UInt32VSzsMc
+ _$ss7DecoderP20singleValueContainers06Singlec8DecodingD0_pyKFTj
+ _$ss7EncoderP20singleValueContainers06Singlec8EncodingD0_pyFTj
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _objc_autoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_deallocPartialClassInstance
+ _swift_stdlib_random
- _$sSo13os_log_type_ta0A0E4infoABvgZ
CStrings:
+ "???"
+ "AppInstallationMetricsDaemon.LogKey"
+ "BEM"
+ "GEN"
+ "INT"
+ "T@\"NSString\",N,R"
+ "[%!@(MISSING)] Adding install for bundleID: %!s(MISSING)"
+ "[%!@(MISSING)] Building AMSMetricsEvent for topic: %!{(MISSING)public}s"
+ "[%!@(MISSING)] Enqueue complete"
+ "[%!@(MISSING)] Enqueueing %!{(MISSING)public}ld events"
+ "[%!@(MISSING)] Enqueuing event with bundleID: %!s(MISSING) clientEventID: %!s(MISSING)"
+ "[%!@(MISSING)] Error encoding %!{(MISSING)public}s: %!{(MISSING)public}s"
+ "[%!@(MISSING)] Failed to clear installation events due to error: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Failed to derezz event"
+ "[%!@(MISSING)] Failed to enqueue events due to error: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Failed to flush events due to error: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Failed to record installation event due to error: %!{(MISSING)public}@"
+ "[%!@(MISSING)] Falling back to lookup by DSID"
+ "[%!@(MISSING)] Flushed %!{(MISSING)public}@ event(s)"
+ "[%!@(MISSING)] Flushing events"
+ "[%!@(MISSING)] No AMSMetricsEvents to enqueue"
+ "[%!@(MISSING)] Preparing to enqueue %!{(MISSING)public}ld events"
+ "[%!@(MISSING)] Saving installation events to: %!{(MISSING)private}s"
+ "[%!@(MISSING)] Skipping immediate post of event for: %!{(MISSING)public}s"
+ "[%!@(MISSING)] Skipping installation event for bundleID: %!s(MISSING) with non valid installType: %!s(MISSING)"
+ "_TtC28AppInstallationMetricsDaemon6LogKey"
+ "redactedDescription"
+ "representation"
- "Adding install for bundleID: %!s(MISSING)"
- "Attempting to post %!l(MISSING)d event(s)"
- "Building AMSMetricsEvent for topic: %!{(MISSING)public}s"
- "Enqueueing %!{(MISSING)public}ld events"
- "Error encoding %!{(MISSING)public}s: %!{(MISSING)public}s"
- "Failed to clear installation events due to error: %!{(MISSING)public}@"
- "Failed to derezz event"
- "Failed to enqueue events due to error: %!{(MISSING)public}@"
- "Failed to flush events due to error: %!{(MISSING)public}@"
- "Failed to record installation event due to error: %!{(MISSING)public}@"
- "Falling back to lookup by DSID"
- "Flushed %!{(MISSING)public}@ event(s)"
- "Flushing events"
- "No AMSMetricsEvents to enqueue"
- "Post complete"
- "Preparing to enqueue %!{(MISSING)public}ld events"
- "Saving installation events to: %!{(MISSING)private}s"
- "Skipping immediate post of event for: %!{(MISSING)public}s"
- "Skipping installation event for bundleID: %!s(MISSING) with non valid installType: %!s(MISSING)"

```
