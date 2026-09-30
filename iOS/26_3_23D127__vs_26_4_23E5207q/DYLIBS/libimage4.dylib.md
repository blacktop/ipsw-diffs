## libimage4.dylib

> `/usr/lib/libimage4.dylib`

```diff

-349.60.2.0.0
-  __TEXT.__text: 0x2a374
+349.100.9.0.0
+  __TEXT.__text: 0x2a2d0
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x105e8
-  __TEXT.__cstring: 0x6527
+  __TEXT.__const: 0x103d8
+  __TEXT.__cstring: 0x65d1
   __TEXT.__oslogstring: 0x7e
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__unwind_info: 0xa08
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x8ab0
-  __DATA_CONST.__image4_chp: 0x140
+  __DATA_CONST.__const: 0x8e10
+  __DATA_CONST.__image4_chp: 0x150
   __DATA_CONST.__image4_coproc: 0x48
   __AUTH_CONST.__auth_got: 0x378
-  __AUTH_CONST.__const: 0x6c50
+  __AUTH_CONST.__const: 0x70a0
   __AUTH.__data: 0x120
-  __DATA.__data: 0x338
+  __DATA.__data: 0x358
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x3b0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: AAA7C9CD-16C0-3B94-93F0-E986AA958E20
-  Functions: 1071
-  Symbols:   3717
-  CStrings:  834
+  UUID: 57321E89-54FB-329D-96C6-289EDF50EFF1
+  Functions: 1120
+  Symbols:   3939
+  CStrings:  837
 
Symbols:
+ _CMSAttributeParseAppleHashAgilityV2
+ _CMSGetCertificateUsingIssuerSerialNumber
+ _CMSParseEncapsulatedContent
+ _CMSParseSignedData
+ _DEREncoderAddImage4Property.cold.1
+ _DEREncoderAddImage4Property.cold.2
+ _DEREncoderEncodeImage4Dictionary.cold.1
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___chpld_cryptex1_mobile_asset_dfu_vma2
+ ___chpld_cryptex1_mobile_asset_vma2
+ ___odometer_select_policy.cold.1
+ ___set___image4_chp_sym___chpld_cryptex1_mobile_asset_dfu_vma2
+ ___set___image4_chp_sym___chpld_cryptex1_mobile_asset_vma2
+ __boot_ephemeral_enforce.cold.1
+ __boot_ephemeral_enforceable.cold.1
+ __boot_flash_secondary_enforce.cold.1
+ __boot_flash_secondary_enforce.cold.2
+ __boot_live_enforce.cold.1
+ __boot_live_enforce.cold.2
+ __boot_sideload_enforce.cold.1
+ __boot_sideload_enforceable.cold.1
+ __boot_static_enforceable.cold.1
+ __chain_future_enforce.cold.1
+ __chain_manifest_enforce.cold.1
+ __chain_sideload_enforceable.cold.1
+ __chip_cryptex1_mobile_asset_dfu_vma2
+ __chip_cryptex1_mobile_asset_vma2
+ __chip_decode_select_static.cold.1
+ __closure_compute_internal.cold.1
+ __darwin_el0_init.cold.1
+ __darwin_el0_init.cold.2
+ __darwin_el0_init.cold.3
+ __darwin_el0_init.cold.4
+ __darwin_el0_query_property_bool.cold.1
+ __darwin_el0_query_property_digest.cold.1
+ __darwin_el0_query_property_uint32.cold.1
+ __darwin_el0_query_property_uint64.cold.1
+ __darwin_el0_query_property_version.cold.1
+ __expert_alloc_type.cold.1
+ __extract_payload.cold.1
+ __fd_dealloc.cold.1
+ __image4_environment_init.cold.1
+ __image4_trust_add_link.cold.1
+ __image4_trust_post_properties.cold.1
+ __image4_trust_violation.cold.1
+ __manifest_evaluate_trust_manifest.cold.1
+ __manifest_evaluate_trust_payload.cold.1
+ __manifest_impose_internal.cold.1
+ __manifest_validate_property.cold.1
+ __oidMldsa44EcdsaP256Sha256
+ __oidMldsa44Ed25519Sha512
+ __oidMldsa44Rsa2048Pkcs15Sha256
+ __oidMldsa44Rsa2048PssSha256
+ __oidMldsa65EcdsaBrainpoolP256r1Sha512
+ __oidMldsa65EcdsaP256Sha512
+ __oidMldsa65EcdsaP384Sha512
+ __oidMldsa65Ed25519Sha512
+ __oidMldsa65Rsa3072Pkcs15Sha512
+ __oidMldsa65Rsa3072PssSha512
+ __oidMldsa65Rsa4096Pkcs15Sha512
+ __oidMldsa65Rsa4096PssSha512
+ __oidMldsa87EcdsaBrainpoolP384r1Sha512
+ __oidMldsa87EcdsaP384Sha512
+ __oidMldsa87EcdsaP521Sha512
+ __oidMldsa87Ed448Shake256
+ __oidMldsa87Rsa3072PssSha512
+ __oidMldsa87Rsa4096PssSha512
+ __payload_bare_get_measured_bytes.cold.1
+ __payload_bare_measure.cold.1
+ __payload_img4_get_measured_bytes.cold.1
+ __restore_log_state_file_locked.cold.1
+ _closure_node_destroy.cold.1
+ _darwin_syscall_init.cold.1
+ _generic_expert_specialist.cold.1
+ _image4_auditor_destroy.cold.1
+ _image4_coprocessor_resolve_from_manifest.cold.1
+ _image4_environment_get_digest_info.cold.1
+ _image4_environment_get_nonce_domain.cold.1
+ _image4_environment_identify.cold.1
+ _image4_trust_destroy.cold.1
+ _image4_trust_evaluate.cold.1
+ _image4_trust_evaluate_audit.cold.1
+ _image4_trust_evaluate_boot.cold.1
+ _image4_trust_evaluate_leaf.cold.1
+ _image4_trust_evaluate_normalize.cold.1
+ _image4_trust_record_property_bool.cold.1
+ _image4_trust_record_property_data.cold.1
+ _image4_trust_record_property_integer.cold.1
+ _image4_trust_set_result_buffer.cold.1
+ _img4_chip_get_cryptex1_boot.cold.1
+ _img4_chip_get_cryptex1_boot_proposal.cold.1
+ _img4_chip_select_cryptex1_boot.cold.1
+ _img4_chip_select_cryptex1_preboot.cold.1
+ _img4_firmware_evaluate.cold.1
+ _img4_firmware_evaluate.cold.2
+ _img4_firmware_select_chip.cold.1
+ _img4_firmware_select_chip.cold.2
+ _manifest_destroy.cold.1
+ _manifest_get_restore_info.cold.1
+ _manifest_post_property_callback.cold.1
+ _odometer_update.cold.1
+ _oidMldsa44EcdsaP256Sha256
+ _oidMldsa44Ed25519Sha512
+ _oidMldsa44Rsa2048Pkcs15Sha256
+ _oidMldsa44Rsa2048PssSha256
+ _oidMldsa65EcdsaBrainpoolP256r1Sha512
+ _oidMldsa65EcdsaP256Sha512
+ _oidMldsa65EcdsaP384Sha512
+ _oidMldsa65Ed25519Sha512
+ _oidMldsa65Rsa3072Pkcs15Sha512
+ _oidMldsa65Rsa3072PssSha512
+ _oidMldsa65Rsa4096Pkcs15Sha512
+ _oidMldsa65Rsa4096PssSha512
+ _oidMldsa87EcdsaBrainpoolP384r1Sha512
+ _oidMldsa87EcdsaP384Sha512
+ _oidMldsa87EcdsaP521Sha512
+ _oidMldsa87Ed448Shake256
+ _oidMldsa87Rsa3072PssSha512
+ _oidMldsa87Rsa4096PssSha512
CStrings:
+ "/Library/Caches/com.apple.xbs/F10F55E8-269E-4A19-A935-A1F2C7974FD4/TemporaryDirectory.GwWXKI/Binaries/AppleImage4_libraries/install/Symbols/image4"
+ "349.100.9"
+ "@(#)VERSION:Darwin Image4 Library Version 7.0.0: Wed Feb  4 23:04:42 PST 2026; root:AppleImage4_libraries-349.100.9~1740/libimage4/RELEASE_ARM64E"
+ "CHIP_CRYPTEX1_MOBILE_ASSET_DFU_VMA2"
+ "CHIP_CRYPTEX1_MOBILE_ASSET_VMA2"
+ "Cryptex1 mobile asset [VMA2 host]"
+ "Darwin Image4 Library Version 7.0.0: Wed Feb  4 23:04:42 PST 2026; root:AppleImage4_libraries-349.100.9~1740/libimage4/RELEASE_ARM64E"
- "/Library/Caches/com.apple.xbs/Binaries/AppleImage4_libraries/install/Symbols/image4"
- "349.60.2"
- "@(#)VERSION:Darwin Image4 Library Version 7.0.0: Wed Jan 21 22:08:43 PST 2026; root:AppleImage4_libraries-349.60.2~1600/libimage4/RELEASE_ARM64E"
- "Darwin Image4 Library Version 7.0.0: Wed Jan 21 22:08:43 PST 2026; root:AppleImage4_libraries-349.60.2~1600/libimage4/RELEASE_ARM64E"

```
