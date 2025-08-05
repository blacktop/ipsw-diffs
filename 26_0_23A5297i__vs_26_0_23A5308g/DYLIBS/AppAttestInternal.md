## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-125.0.0.0.0
-  __TEXT.__text: 0x6a458
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x6ac
-  __TEXT.__const: 0x31c0
-  __TEXT.__cstring: 0x5b48
+127.0.0.0.0
+  __TEXT.__text: 0x6b2b8
+  __TEXT.__auth_stubs: 0x16c0
+  __TEXT.__objc_methlist: 0x6c4
+  __TEXT.__const: 0x3220
+  __TEXT.__cstring: 0x5cd8
   __TEXT.__oslogstring: 0x38da
   __TEXT.__gcc_except_tab: 0x8f8
-  __TEXT.__swift5_typeref: 0xa1e
-  __TEXT.__swift5_reflstr: 0xec3
+  __TEXT.__swift5_typeref: 0xa56
+  __TEXT.__swift5_reflstr: 0xf33
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__constg_swiftt: 0xd58
-  __TEXT.__swift5_fieldmd: 0xf90
+  __TEXT.__swift5_fieldmd: 0xf9c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x238
+  __TEXT.__swift5_proto: 0x23c
   __TEXT.__swift5_types: 0x178
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x208
-  __TEXT.__unwind_info: 0xf40
+  __TEXT.__unwind_info: 0xf60
   __TEXT.__eh_frame: 0xd08
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x126a
+  __TEXT.__objc_methname: 0x133f
   __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__objc_stubs: 0x1320
+  __TEXT.__objc_stubs: 0x1340
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x26c0
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x17a8
+  __DATA_CONST.__objc_arraydata: 0xe0
+  __AUTH_CONST.__auth_got: 0xb70
+  __AUTH_CONST.__const: 0x26f8
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x17f8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x4d8
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH.__objc_data: 0x3b8
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x3250
-  __DATA.__common: 0x50
-  __DATA_DIRTY.__objc_data: 0x668
-  __DATA_DIRTY.__data: 0xa90
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x32c0
+  __DATA.__common: 0x48
+  __DATA_DIRTY.__objc_data: 0x788
+  __DATA_DIRTY.__data: 0xaa0
   __DATA_DIRTY.__bss: 0x11f0
-  __DATA_DIRTY.__common: 0x118
+  __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CC86149-B250-3E1D-ACAD-884CC84ADC0F
-  Functions: 1348
-  Symbols:   1944
-  CStrings:  1343
+  UUID: 64602D5C-D78F-3F7B-AF2A-789F7BEC3EFD
+  Functions: 1358
+  Symbols:   1955
+  CStrings:  1353
 
Symbols:
+ +[FeatureFlagsManager isExtensionAttestationEnabled]
+ -[AppAttestEligibilityManager allowlistedFirstPartyExtensions]
+ -[AppAttestEligibilityManager allowlistedThirdPartyExtensions]
+ -[AppAttestEligibilityManager setAllowlistedFirstPartyExtensions:]
+ -[AppAttestEligibilityManager setAllowlistedThirdPartyExtensions:]
+ GCC_except_table13
+ GCC_except_table17
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table6
+ _OBJC_IVAR_$_AppAttestEligibilityManager._allowlistedFirstPartyExtensions
+ _OBJC_IVAR_$_AppAttestEligibilityManager._allowlistedThirdPartyExtensions
+ ___52+[FeatureFlagsManager isExtensionAttestationEnabled]_block_invoke
+ ___52+[FeatureFlagsManager isExtensionAttestationEnabled]_block_invoke.cold.1
+ ___swift_memcpy73_8
+ _associated conformance 17AppAttestInternal18SecurityControllerC06DeviceD5StateOSHAASQ
+ _associated conformance 17AppAttestInternal22BundleRecordControllerC0E4TypeOSHAASQ
+ _isExtensionAttestationEnabled.onceToken
+ _objc_msgSend$allowlistedFirstPartyExtensions
+ _objc_msgSend$allowlistedThirdPartyExtensions
+ _objc_msgSend$isExtensionAttestationEnabled
+ _symbolic SDySS_____GSg 17AppAttestInternal22BundleRecordControllerC0E4TypeO
+ _symbolic SS______t 17AppAttestInternal22BundleRecordControllerC0E4TypeO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC06DeviceD5StateO
+ _symbolic _____Sg 17AppAttestInternal18SecurityControllerC06DeviceD5StateO
+ _symbolic _____ySS_____G s18_DictionaryStorageC 17AppAttestInternal22BundleRecordControllerC0G4TypeO
- +[FeatureFlagsManager isActionExtensionAttestationEnabled]
- -[AppAttestEligibilityManager allowlistedExtensions]
- -[AppAttestEligibilityManager setAllowlistedExtensions:]
- GCC_except_table12
- GCC_except_table16
- GCC_except_table20
- GCC_except_table22
- _OBJC_IVAR_$_AppAttestEligibilityManager._allowlistedExtensions
- ___58+[FeatureFlagsManager isActionExtensionAttestationEnabled]_block_invoke
- ___58+[FeatureFlagsManager isActionExtensionAttestationEnabled]_block_invoke.cold.1
- ___swift_memcpy72_8
- _associated conformance 17AppAttestInternal18SecurityControllerC18ValidationCategoryOSHAASQ
- _isActionExtensionAttestationEnabled.onceToken
- _objc_msgSend$allowlistedExtensions
- _objc_msgSend$isActionExtensionAttestationEnabled
- _symbolic _____ 17AppAttestInternal18SecurityControllerC18ValidationCategoryO
CStrings:
+ "$__lazy_storage_$_allowlistedThirdPartyAppExtensionTypes"
+ "%25s:%-5d App Attest Extension Support feature flag enabled { enabled=%d }."
+ ", deviceSecurityState="
+ "/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/AssertionUtility.swift"
+ "AppAttest (%@-127) - %@"
+ "Extension Attestation Feature Flag is not enabled."
+ "Failed to access attestation CBOR object."
+ "T@\"NSArray\",&,N,V_allowlistedFirstPartyExtensions"
+ "T@\"NSArray\",&,N,V_allowlistedThirdPartyExtensions"
+ "Unexpected type for extension record. { expected=LSApplicationExtensionRecord"
+ "_allowlistedFirstPartyExtensions"
+ "_allowlistedThirdPartyExtensions"
+ "addTestFirstPartyExtensionToAllowlist"
+ "allowlistedFirstPartyExtensions"
+ "allowlistedThirdPartyExtensions"
+ "cborWithInteger:"
+ "com.apple.AppSSO.idp-extension"
+ "deviceSecurityState"
+ "dictionary"
+ "extensionAttestation"
+ "isExtensionAttestationEnabled"
+ "setAllowlistedFirstPartyExtensions:"
+ "setAllowlistedThirdPartyExtensions:"
- "%25s:%-5d App Attest Action Extension feature flag enabled { enabled=%d }."
- "Action Extension not enabled."
- "AppAttest (%@-125) - %@"
- "T@\"NSArray\",&,N,V_allowlistedExtensions"
- "_allowlistedExtensions"
- "actionExtensionAttestation"
- "addTestExtensionToAllowlist"
- "allowlistedExtensions"
- "appStore"
- "developerID"
- "isActionExtensionAttestationEnabled"
- "platform"
- "setAllowlistedExtensions:"
- "unknown"

```
