## HeimODAdmin

> `/System/Library/PrivateFrameworks/HeimODAdmin.framework/Versions/A/HeimODAdmin`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0xae18
+693.100.10.0.0
+  __TEXT.__text: 0x9ba8
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x7b0

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
-  UUID: BD8B8CC6-C8E3-3F9A-AEE8-369E6DAADC8F
+  UUID: 72EE02D5-378D-354E-85B8-CD1EE647870E
   Functions: 98
   Symbols:   260
   CStrings:  175
Functions:
~ _HeimODCreateRealm : 60 -> 52
~ _HeimODCreatePrincipalData : 608 -> 524
~ _copyDataRecord : 420 -> 352
~ _flags2int : 336 -> 304
~ _createError : 332 -> 304
~ _HeimODRemovePrincipalData : 448 -> 412
~ _HeimODSetKerberosFlags : 252 -> 236
~ _flagop : 348 -> 324
~ _HeimODCopyKerberosFlags : 252 -> 224
~ _getflags : 304 -> 280
~ _CopyInt2flags : 208 -> 188
~ _HeimODClearKerberosFlags : 288 -> 272
~ _HeimODSetACL : 304 -> 280
~ _CopyReMapACL : 324 -> 296
~ _HeimODCopyACL : 252 -> 224
~ _HeimODClearACL : 308 -> 284
~ _HeimODAddServerAlias : 408 -> 348
~ _HeimODRemoveServerAlias : 256 -> 228
~ _HeimODCopyServerAliases : 184 -> 164
~ _HeimODSetKerberosMaxLife : 64 -> 56
~ _HeimODGetKerberosMaxLife : 60 -> 52
~ _HeimODSetKerberosMaxRenewable : 64 -> 56
~ _HeimODGetKerberosMaxRenewable : 64 -> 56
~ _HeimODCreateSRPKeys : 1216 -> 1076
~ _cfstring2cstring : 240 -> 216
~ _krb5_principalCreateFromString : 160 -> 144
~ _HeimODSetVerifiers : 336 -> 292
~ _HeimODSetKeys : 2152 -> 1880
~ _last_kvno_record : 168 -> 156
~ _get_lkdc_realm : 392 -> 324
~ _update_keys : 1108 -> 1004
~ _SetSRP : 348 -> 296
~ _HeimODModifyKeys : 1164 -> 988
~ _delete_enctypes : 1392 -> 1232
~ _last_kvno_array : 456 -> 388
~ _HeimODKeysetToString : 932 -> 832
~ _HeimODCopyDefaultEnctypes : 172 -> 164
~ _HeimODAddCertificate : 1372 -> 1152
~ _find_ta : 444 -> 368
~ _HeimODAddCertificateSubjectAndTrustAnchor : 720 -> 664
~ ___HeimODAddCertificateSubjectAndTrustAnchor_block_invoke : 152 -> 140
~ _HeimODRemoveCertificateSubjectAndTrustAnchor : 396 -> 348
~ _HeimODAddAppleIDAlias : 632 -> 584
~ _is_record_server : 96 -> 92
~ ___HeimODAddAppleIDAlias_block_invoke : 152 -> 140
~ _HeimODRemoveAppleIDAlias : 336 -> 296
~ _load_simple : 392 -> 352
~ _edump_principal : 156 -> 148
~ _edump_flags : 220 -> 208
~ _load_keys : 1372 -> 1192
~ _edump_keys : 464 -> 420
~ _HeimODDumpRecord : 720 -> 644
~ _HeimODLoadRecord : 864 -> 764
~ _HeimODDumpHdbEntry : 508 -> 448
~ _is_record_server_location : 280 -> 248
~ _force_server : 108 -> 104
~ ___force_server_block_invoke : 192 -> 168
~ _string2int : 144 -> 128
~ ___update_keys_block_invoke : 1048 -> 992
~ _find_enctype : 140 -> 128
~ _CFStringCreateWithkrb5_principal : 152 -> 144
~ _applier : 68 -> 64
~ _encode_Salt : 1344 -> 1240
~ _decode_Salt : 2776 -> 2468
~ _free_Salt : 112 -> 104
~ _length_Salt : 404 -> 380
~ _encode_Key : 1144 -> 1048
~ _decode_Key : 2260 -> 2024
~ _free_Key : 164 -> 148
~ _length_Key : 388 -> 356
~ _HDBFlags2int : 828 -> 592
~ _encode_Keys : 420 -> 388
~ _decode_Keys : 864 -> 776
~ _free_Keys : 132 -> 124
~ _length_Keys : 232 -> 216
~ _encode_hdb_keyset_aapl : 1112 -> 1024
~ _decode_hdb_keyset_aapl : 2160 -> 1932
~ _free_hdb_keyset_aapl : 112 -> 104
~ _length_hdb_keyset_aapl : 356 -> 332
~ _encode_hdb_srp : 828 -> 768
~ _length_hdb_srp : 248 -> 236
~ _hdb_set_srp_verifier : 320 -> 288

```
