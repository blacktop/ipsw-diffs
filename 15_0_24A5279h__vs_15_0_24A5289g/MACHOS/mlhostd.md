## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.2.4.0.0
-  __TEXT.__text: 0x48bf0
-  __TEXT.__auth_stubs: 0x1920
+3.2.8.0.0
+  __TEXT.__text: 0x47108
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xfc4
-  __TEXT.__cstring: 0x9955
-  __TEXT.__swift5_typeref: 0x747
-  __TEXT.__oslogstring: 0x1c2a
+  __TEXT.__const: 0xbf4
+  __TEXT.__cstring: 0x98a5
+  __TEXT.__swift5_typeref: 0x68d
+  __TEXT.__oslogstring: 0x1c6a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x354
+  __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x2e5
-  __TEXT.__swift5_fieldmd: 0x35c
+  __TEXT.__swift5_reflstr: 0x2b5
+  __TEXT.__swift5_fieldmd: 0x2e0
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0xd4
-  __TEXT.__swift5_types: 0x50
+  __TEXT.__swift5_proto: 0x90
+  __TEXT.__swift5_types: 0x40
   __TEXT.__objc_methname: 0xabb
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
   __TEXT.__swift5_capture: 0x1c4
   __TEXT.__info_plist: 0x51a
-  __TEXT.__unwind_info: 0x870
-  __TEXT.__eh_frame: 0x1090
-  __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x5138
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__eh_frame: 0xff8
+  __DATA_CONST.__auth_got: 0xc30
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__auth_ptr: 0x420
+  __DATA_CONST.__const: 0x4f70
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xac8
   __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0xb48
-  __DATA.__bss: 0x1a80
+  __DATA.__data: 0xa80
+  __DATA.__bss: 0x1200
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 664
-  Symbols:   664
-  CStrings:  1220
+  Functions: 587
+  Symbols:   646
+  CStrings:  1216
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- _$s20LighthouseBackground19TaskValidationErrorO15invalidCriteriayACSScACmFWC
- _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
- _$ss13DecodingErrorO12typeMismatchyABypXp_AB7ContextVtcABmFWC
- _$ss13DecodingErrorO7ContextV10codingPath16debugDescription010underlyingB0ADSays9CodingKey_pG_SSs0B0_pSgtcfC
- _$ss13DecodingErrorO7ContextVMn
- _$ss13DecodingErrorOMa
- _$ss13DecodingErrorOs0B0sWP
- _$ss22KeyedDecodingContainerV06nestedC07keyedBy6forKeyAByqd__Gqd__m_xtKs06CodingH0Rd__lF
- _$ss22KeyedDecodingContainerV10codingPathSays9CodingKey_pGvg
- _$ss22KeyedDecodingContainerV6decode_6forKeyS2Sm_xtKF
- _$ss22KeyedDecodingContainerV7allKeysSayxGvg
- _$ss22KeyedEncodingContainerV06nestedC07keyedBy6forKeyAByqd__Gqd__m_xts06CodingH0Rd__lF
- _$ss22KeyedEncodingContainerV6encode_6forKeyySS_xtKF
- _$ss5ErrorPsE19_getEmbeddedNSErroryXlSgyF
- _$ss5ErrorPsE5_codeSivg
- _$ss5ErrorPsE7_domainSSvg
- _$ss8DurationV12millisecondsyABxSzRzlFZ
- _$ss8DurationV7secondsyABxSzRzlFZ
- _$sytWV
CStrings:
- "Invalid number of keys found, expected one."
- "The push message body must be a json dictionary with key "
- "cannot register task"
- "invalidJSONFormat"

```
