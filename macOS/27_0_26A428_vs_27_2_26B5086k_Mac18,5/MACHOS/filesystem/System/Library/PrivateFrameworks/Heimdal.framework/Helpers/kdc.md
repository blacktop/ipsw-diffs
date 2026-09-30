## kdc

> `/System/Library/PrivateFrameworks/Heimdal.framework/Helpers/kdc`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-725.0.12.0.0
-  __TEXT.__text: 0x4d928
-  __TEXT.__auth_stubs: 0x1cd0
+725.40.6.0.0
+  __TEXT.__text: 0x4de74
+  __TEXT.__auth_stubs: 0x1d10
   __TEXT.__const: 0x720
-  __TEXT.__cstring: 0x5123
+  __TEXT.__cstring: 0x519a
   __TEXT.__oslogstring: 0x15
-  __TEXT.__unwind_info: 0xc30
-  __DATA_CONST.__const: 0x3dc0
+  __TEXT.__unwind_info: 0xc50
+  __DATA_CONST.__const: 0x3f90
   __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__auth_got: 0xe68
+  __DATA_CONST.__auth_got: 0xe88
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x80c
+  __DATA.__data: 0x8d8
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
-  Functions: 759
-  Symbols:   1849
-  CStrings:  805
+  Functions: 766
+  Symbols:   1883
+  CStrings:  811
 
Symbols:
+ ___kdc_pkinit_stat_report_block_invoke
+ _analytics_send_event_lazy
+ _asn1_ECParameters
+ _asn1_RSAPublicKey
+ _asn1_RSAPublicKey_tag__101
+ _asn1_choice_ECParameters_6
+ _asn1_heim_oid_seofTstruct_10
+ _asn1_oid_id_ecPublicKey
+ _asn1_oid_id_ec_group_secp160r1
+ _asn1_oid_id_ec_group_secp160r2
+ _asn1_oid_id_ec_group_secp192r1
+ _asn1_oid_id_ec_group_secp224r1
+ _asn1_oid_id_ec_group_secp256r1
+ _asn1_oid_id_ec_group_secp384r1
+ _asn1_oid_id_ec_group_secp521r1
+ _asn1_oid_id_pkcs1_rsaEncryption
+ _decode_ECParameters
+ _decode_RSAPublicKey
+ _free_ECParameters
+ _free_RSAPublicKey
+ _hx509_cert_get_SPKI
+ _kdc_pkinit_stat_curve
+ _kdc_pkinit_stat_report
+ _oid_id_ecPublicKey_variable_num
+ _oid_id_ec_group_secp160r1_variable_num
+ _oid_id_ec_group_secp160r2_variable_num
+ _oid_id_ec_group_secp192r1_variable_num
+ _oid_id_ec_group_secp224r1_variable_num
+ _oid_id_ec_group_secp256r1_variable_num
+ _oid_id_ec_group_secp384r1_variable_num
+ _oid_id_ec_group_secp521r1_variable_num
+ _oid_id_pkcs1_rsaEncryption_variable_num
+ _xpc_dictionary_create
+ _xpc_dictionary_set_int64
CStrings:
+ "KDCPKINIT_client_curve"
+ "KDCPKINIT_client_pk_alg"
+ "KDCPKINIT_client_pk_size"
+ "KDCPKINIT_keyex"
+ "^v8@?0"
+ "com.apple.GSS.KDCPKINIT"
```
