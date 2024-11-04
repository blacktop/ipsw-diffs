## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1329.60.89.502.4
-  __TEXT.__text: 0x26333c
+1329.60.100.502.2
+  __TEXT.__text: 0x2628f4
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_stubs: 0x1fbe0
-  __TEXT.__objc_methlist: 0xeff8
-  __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x374ca
-  __TEXT.__cstring: 0x4ceac
+  __TEXT.__objc_stubs: 0x1fc20
+  __TEXT.__objc_methlist: 0xf010
+  __TEXT.__const: 0x495e
+  __TEXT.__objc_methname: 0x374f8
+  __TEXT.__cstring: 0x4cfcc
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x357c
+  __TEXT.__objc_methtype: 0x3588
   __TEXT.__oslogstring: 0x310d5
   __TEXT.__gcc_except_tab: 0x2558
   __TEXT.__dlopen_cstrs: 0x5a

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4750
+  __TEXT.__unwind_info: 0x4860
   __TEXT.__eh_frame: 0x30c4
   __DATA_CONST.__auth_got: 0x11d8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6700
-  __DATA_CONST.__cfstring: 0x319c0
+  __DATA_CONST.__const: 0x6720
+  __DATA_CONST.__cfstring: 0x31aa0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ba0
+  __DATA_CONST.__objc_selrefs: 0x8bb0
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x998
   __DATA_CONST.__objc_arrayobj: 0x1e0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8290
-  Symbols:   14891
-  CStrings:  15821
+  Functions: 8304
+  Symbols:   14908
+  CStrings:  15831
 
Symbols:
+ -[SecureMobileAssetBundle isPersonalized:]
+ -[SecureMobileAssetBundle isPersonalizedManifestStaged:]
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table87
+ __block_literal_global.1775
+ _cc_cmp_safe_internal
+ _cc_disable_dit_with_sb
+ _cccbc_init_internal
+ _cccbc_one_shot_explicit_internal
+ _cccbc_set_iv_internal
+ _cccbc_update_internal
+ _ccchacha20_update_internal
+ _ccchacha20poly1305_decrypt_internal
+ _ccchacha20poly1305_encrypt_internal
+ _ccchacha20poly1305_finalize_internal
+ _ccchacha20poly1305_init_internal
+ _ccchacha20poly1305_setnonce_internal
+ _ccchacha20poly1305_verify_internal
+ _cccmac_final_generate_internal
+ _cccmac_init_internal
+ _cccmac_update_internal
+ _ccctr_init_internal
+ _ccctr_update_internal
+ _ccder_blob_decode_eckey_internal
+ _ccder_blob_encode_eckey_internal
+ _ccder_decode_eckey_internal
+ _ccder_encode_eckey_internal
+ _ccdigest_init_internal
+ _ccdigest_internal
+ _ccdigest_update_internal
+ _ccdrbg_df_bc_init_internal
+ _ccdrbg_init_internal
+ _ccec_export_affine_point_public_value
+ _ccec_import_pub_ws
+ _ccn_bitlen_internal
+ _ccn_bitlen_public_value
+ _ccn_cmp_internal
+ _ccn_cmp_public_value
+ _ccn_cmpn_internal
+ _ccn_cmpn_public_value
+ _ccn_read_uint_internal
+ _ccn_read_uint_public_value
+ _ccn_write_int_public_value
+ _ccn_write_int_size_public_value
+ _ccn_write_uint_padded_ct_internal
+ _ccn_write_uint_public_value
+ _ccn_write_uint_size_internal
+ _ccpoly1305_final_internal
+ _ccpoly1305_init_internal
+ _ccpoly1305_update_internal
+ _objc_msgSend$isPersonalized:
+ _objc_msgSend$isPersonalizedManifestStaged:
+ _sb
+ _timingsafe_enable_if_supported
+ _timingsafe_restore_if_supported
- GCC_except_table70
- GCC_except_table71
- GCC_except_table85
- __block_literal_global.1766
- _cc_disable_dit
- _cccbc_clear_iv
- _cccbc_copy_iv
- _cccbc_init
- _cccbc_one_shot
- _cccbc_one_shot_explicit
- _cccbc_set_iv
- _cccbc_update
- _ccchacha20_init
- _ccchacha20_reset
- _ccchacha20_setnonce
- _ccchacha20_update
- _ccchacha20poly1305_reset
- _ccctr_init
- _ccctr_update
- _ccder_blob_decode_eckey
- _ccder_blob_encode_eckey
- _ccder_decode_eckey
- _ccder_encode_eckey
- _ccdigest
- _ccdrbg_df_bc_init
- _ccdrbg_init
- _ccec_export_affine_point
- _ccec_make_pub_from_priv
- _ccn_bitlen
- _ccn_cmpn
- _ccn_read_uint
- _ccn_write_int
- _ccn_write_int_size
- _ccn_write_uint
- _ccn_write_uint_padded_ct
- _ccn_write_uint_size
- _ccpoly1305_final
- _ccpoly1305_init
- _ccpoly1305_update
CStrings:
+ " (%!@(MISSING))"
+ "2.2.21"
+ "B24@0:8^q16"
+ "Bundle is not personalized and committed for Exclaves"
+ "Cannot map an unpersonalized asset to Exclaves"
+ "Committed ticket data is nil"
+ "CrystalCSeed"
+ "Personalized bundle ticket data and committed ticket data do not match"
+ "Personalized bundle ticket data is nil"
+ "Starting built-in MobileAsset brain built Oct 28 2024 22:37:01"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 28 2024 22:37:01"
+ "cannot graft an unpersonalized cryptex"
+ "cannot mount an unpersonalized cryptex"
+ "isPersonalized:"
+ "isPersonalizedManifestStaged:"
- "2.2.20"
- "CrystalSeedUpdate"
- "Starting built-in MobileAsset brain built Oct 20 2024 22:11:52"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 20 2024 22:11:52"
- "cannot graft an unsigned asset"

```
