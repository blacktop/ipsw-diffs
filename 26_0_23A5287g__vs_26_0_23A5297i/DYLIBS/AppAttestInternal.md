## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-123.0.0.0.0
-  __TEXT.__text: 0x69b90
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_methlist: 0x69c
-  __TEXT.__const: 0x3170
-  __TEXT.__cstring: 0x5ab8
-  __TEXT.__oslogstring: 0x388a
-  __TEXT.__gcc_except_tab: 0x8f0
-  __TEXT.__swift5_typeref: 0xa18
+125.0.0.0.0
+  __TEXT.__text: 0x6a458
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_methlist: 0x6ac
+  __TEXT.__const: 0x31c0
+  __TEXT.__cstring: 0x5b48
+  __TEXT.__oslogstring: 0x38da
+  __TEXT.__gcc_except_tab: 0x8f8
+  __TEXT.__swift5_typeref: 0xa1e
   __TEXT.__swift5_reflstr: 0xec3
   __TEXT.__swift5_assocty: 0x1e0
-  __TEXT.__constg_swiftt: 0xd3c
-  __TEXT.__swift5_fieldmd: 0xf68
+  __TEXT.__constg_swiftt: 0xd58
+  __TEXT.__swift5_fieldmd: 0xf90
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x234
-  __TEXT.__swift5_types: 0x174
+  __TEXT.__swift5_proto: 0x238
+  __TEXT.__swift5_types: 0x178
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x208
-  __TEXT.__unwind_info: 0xf28
+  __TEXT.__unwind_info: 0xf40
   __TEXT.__eh_frame: 0xd08
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x122c
+  __TEXT.__objc_methname: 0x126a
   __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__objc_stubs: 0x12c0
+  __TEXT.__objc_stubs: 0x1320
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0xb38
-  __AUTH_CONST.__const: 0x2630
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__const: 0x26c0
+  __AUTH_CONST.__cfstring: 0x1b00
   __AUTH_CONST.__objc_const: 0x17a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x4d8
   __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x480
-  __DATA.__bss: 0x31d0
-  __DATA.__common: 0x48
+  __DATA.__data: 0x490
+  __DATA.__bss: 0x3250
+  __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x668
   __DATA_DIRTY.__data: 0xa90
   __DATA_DIRTY.__bss: 0x11f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25ED003D-9DD8-344E-98E5-D76C796BE3BD
-  Functions: 1337
-  Symbols:   1930
-  CStrings:  1334
+  UUID: 1CC86149-B250-3E1D-ACAD-884CC84ADC0F
+  Functions: 1348
+  Symbols:   1944
+  CStrings:  1343
 
Symbols:
+ +[FeatureFlagsManager isActionExtensionAttestationEnabled]
+ -[AppAttestEligibilityManager isEligibleApplicationExtensionFor:].cold.8
+ _MobileGestalt_get_deviceClassNumber
+ ___58+[FeatureFlagsManager isActionExtensionAttestationEnabled]_block_invoke
+ ___58+[FeatureFlagsManager isActionExtensionAttestationEnabled]_block_invoke.cold.1
+ _associated conformance 17AppAttestInternal22BundleRecordControllerC0E4TypeO0a9ExtensionG0OSHAASQ
+ _isActionExtensionAttestationEnabled.onceToken
+ _objc_msgSend$extensionPointRecord
+ _objc_msgSend$isActionExtensionAttestationEnabled
+ _objc_msgSend$name
+ _symbolic _____ 17AppAttestInternal22BundleRecordControllerC0E4TypeO0a9ExtensionG0O
- _associated conformance 17AppAttestInternal22BundleRecordControllerC0E4TypeOSHAASQ
CStrings:
+ "%25s:%-5d App Attest Action Extension feature flag enabled { enabled=%d }."
+ "Action Extension not enabled."
+ "AppAttest (%@-125) - %@"
+ "Extension client is not allowlisted. { "
+ "Failed to fetch bundle ID. { "
+ "com.apple.ui-services"
+ "extensionPointRecord"
+ "isActionExtensionAttestationEnabled"
+ "name"
- "AppAttest (%@-123) - %@"

```
