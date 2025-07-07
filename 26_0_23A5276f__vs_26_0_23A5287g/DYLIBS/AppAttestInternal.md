## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x692bc
-  __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x684
+123.0.0.0.0
+  __TEXT.__text: 0x69b90
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_methlist: 0x69c
   __TEXT.__const: 0x3170
-  __TEXT.__cstring: 0x5a68
-  __TEXT.__oslogstring: 0x37da
+  __TEXT.__cstring: 0x5ab8
+  __TEXT.__oslogstring: 0x388a
   __TEXT.__gcc_except_tab: 0x8f0
   __TEXT.__swift5_typeref: 0xa18
-  __TEXT.__swift5_reflstr: 0xe73
+  __TEXT.__swift5_reflstr: 0xec3
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__constg_swiftt: 0xd3c
-  __TEXT.__swift5_fieldmd: 0xf50
+  __TEXT.__swift5_fieldmd: 0xf68
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0x234

   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x208
-  __TEXT.__unwind_info: 0xf18
+  __TEXT.__unwind_info: 0xf28
   __TEXT.__eh_frame: 0xd08
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x1207
+  __TEXT.__objc_methname: 0x122c
   __TEXT.__objc_methtype: 0x2b6
   __TEXT.__objc_stubs: 0x12c0
   __DATA_CONST.__got: 0x4b0

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x678
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0xb30
+  __AUTH_CONST.__auth_got: 0xb38
   __AUTH_CONST.__const: 0x2630
-  __AUTH_CONST.__cfstring: 0x1ac0
-  __AUTH_CONST.__objc_const: 0x1788
+  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__objc_const: 0x17a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x4d0
+  __AUTH.__objc_data: 0x4d8
   __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x460
-  __DATA.__bss: 0x31c0
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x31d0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x668
-  __DATA_DIRTY.__data: 0xa98
+  __DATA_DIRTY.__data: 0xa90
   __DATA_DIRTY.__bss: 0x11f0
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B5ADFAA5-0BE5-3F43-91D4-5AF48CA0C71D
-  Functions: 1329
-  Symbols:   1918
-  CStrings:  1324
+  UUID: 25ED003D-9DD8-344E-98E5-D76C796BE3BD
+  Functions: 1337
+  Symbols:   1930
+  CStrings:  1334
 
Symbols:
+ +[FeatureFlagsManager isMacEnabled]
+ _AppAttest_AppAttestation_IsSupportedAndEligibleApplication
+ _AppAttest_AppAttestation_IsSupportedAndEligibleApplication.cold.1
+ _AppAttest_AppAttestation_IsSupportedAndEligibleApplication.cold.2
+ ___35+[FeatureFlagsManager isMacEnabled]_block_invoke
+ ___35+[FeatureFlagsManager isMacEnabled]_block_invoke.cold.1
+ ___fetchPublicKey_block_invoke.149
+ _isMacEnabled.onceToken
- GCC_except_table14
- ___fetchPublicKey_block_invoke.146
CStrings:
+ "%25s:%-5d App Attest is not supported."
+ "%25s:%-5d Client application is not eligible to use App Attest."
+ "%25s:%-5d Mac feature flag enabled { enabled=%d }."
+ "%25s:%-5d Signed data blob. { keyId=%@ , appUUID=%@, resolvedAppID=%@ }"
+ "AppAttest (%@-123) - %@"
+ "actionExtensionAttestation"
+ "bundleVersion"
+ "isMacEnabled"
+ "rcsStressTest.com.apple.coretelephony"
+ "supported"
+ "x-apple-client-appid"
- "%25s:%-5d Signed data blob. { keyId=%@ }"
- "AppAttest (%@-121) - %@"

```
