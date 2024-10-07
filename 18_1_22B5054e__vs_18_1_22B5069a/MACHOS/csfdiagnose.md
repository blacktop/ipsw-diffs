## csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

-301.22.1.8.0
-  __TEXT.__text: 0xda44
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__const: 0x296
-  __TEXT.__cstring: 0x133b
-  __TEXT.__swift5_typeref: 0x136
+301.22.1.9.2
+  __TEXT.__text: 0xbf08
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__const: 0x2b2
+  __TEXT.__cstring: 0x117b
+  __TEXT.__swift5_typeref: 0x132
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_fieldmd: 0xd8
+  __TEXT.__swift5_fieldmd: 0xc0
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_reflstr: 0xfc
+  __TEXT.__swift5_reflstr: 0x79
   __TEXT.__swift5_capture: 0x34
   __TEXT.__objc_methname: 0x107
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x288
-  __TEXT.__eh_frame: 0x520
-  __DATA_CONST.__auth_got: 0x518
+  __TEXT.__eh_frame: 0x510
+  __DATA_CONST.__auth_got: 0x4d8
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__auth_ptr: 0x178
-  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__auth_ptr: 0x170
+  __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x1e0
   __DATA.__common: 0x20
   __DATA.__bss: 0x480
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 145
-  Symbols:   263
-  CStrings:  97
+  Symbols:   255
+  CStrings:  88
 
Symbols:
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2bm_xtKF
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _objc_retain_x23
+ _objc_retain_x24
- _$s10Foundation4DateVMn
- _$s25CloudSubscriptionFeatures0A7FeatureC3ttl10Foundation4DateVSgvg
- _$s25CloudSubscriptionFeatures0A7FeatureC9featureIDSSvg
- _$s25CloudSubscriptionFeatures12FeatureCacheC03allC07forDSIDSayAA0aD0CGSSSg_tF
- _$s25CloudSubscriptionFeatures8GMBypassC19gmEligibilityBypassSbyFZ
- _$s25CloudSubscriptionFeatures8GMBypassCMa
- _$sSS10describingSSx_tclufC
- _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
- _$ss18_CocoaArrayWrapperV8endIndexSivg
- _objc_retain_x21
- _objc_retain_x27
- _objc_retain_x8
CStrings:
+ "--include-sensitive false"
- "--include-sensitive "
- ". (This command was run without --full so all asset checks will evaluate to true which may lead to false positives)"
- "Feature object: "
- "Features cache:\n"
- "GM Assets Bypass (csfctl gmAssets bypass)"
- "GM Bypass (csfctl gmBypass)"
- "Pass to include sensitive Apple Account information."
- "Pass to include sensitive information."
- "User has bypass enabled? "
- "includeSensitive"

```
