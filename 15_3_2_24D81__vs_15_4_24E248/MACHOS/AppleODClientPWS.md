## AppleODClientPWS

> `/System/Library/OpenDirectory/Modules/AppleODClientPWS.bundle/Contents/MacOS/AppleODClientPWS`

```diff

 164.0.0.0.0
-  __TEXT.__text: 0x12f14
+  __TEXT.__text: 0x12eb4
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x3c67
+  __TEXT.__cstring: 0x3c64
   __TEXT.__unwind_info: 0x320
   __DATA_CONST.__auth_got: 0x6d0
   __DATA_CONST.__got: 0x130

   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: F27A6833-E579-379B-AF68-F4C058034800
-  Functions: 232
-  Symbols:   585
-  CStrings:  710
+  UUID: 9BE5BDBC-7292-3FF7-92A0-97D3076B46C1
+  Functions: 235
+  Symbols:   590
+  CStrings:  709
 
Symbols:
+ __pws_conn_send_cmd_read_resp_block_invoke.cold.1
+ aodc_log_cfarray_contents.cold.1
+ aodc_log_cfdict_contents.cold.1
+ pws_conn_get_odconnection.cold.1
+ pws_modcfg_copy_enabled_ext_auth_mechs.cold.1
Functions:
~ ___pws_conn_set_cast_key_block_invoke : 224 -> 228
~ ___pws_conn_send_cmd_read_resp_block_invoke : 2000 -> 1984
~ _pws_conn_get_odconnection : 548 -> 532
~ __pws_connect_to_server : 1336 -> 1332
~ ____pws_conn_send_command_block_invoke : 248 -> 236
~ __pws_modcfg_copy_kerberos_services_block_invoke.47 : 144 -> 152
~ _pws_modcfg_copy_enabled_ext_auth_mechs : 352 -> 336
~ _pws_copy_policies : 460 -> 456
~ _pws_pps_auth : 2076 -> 2068
~ __pws_verify_password_extended : 3848 -> 3836
~ _odm_RecordChangePassword : 4640 -> 4632
~ _odm_NodeVerifyCredentialsExtended : 824 -> 820
~ _GetRecordPrivileges : 660 -> 652
~ __pws_authitems_for_ntlmv2 : 536 -> 548
~ __pws_authitems_for_smb_nt_lm_key : 288 -> 292
~ _pws_sasl_auth : 820 -> 824
~ ___pws_sasl_auth_block_invoke : 5404 -> 5412
~ _pws_sasl_get_nthashhash : 1560 -> 1544
~ _pws_sasl_get_ntlmv2_session_key : 1764 -> 1756
~ _pws_sasl_get_mppe_master_keys : 1828 -> 1824
~ __pws_bin_to_hex : 284 -> 288
~ __pws_base64_to_bin : 400 -> 396
~ _aodc_policy_create_dictionary_with_cstring : 552 -> 544
~ _aodc_policy_create_string : 588 -> 596
~ _aodc_error_create : 108 -> 96
~ _aodc_log_cfarray_contents : 300 -> 284
~ _aodc_log_cfdict_contents : 492 -> 468
~ ___pws_auth_ctx_release_block_invoke : 160 -> 152
CStrings:
- "lo"

```
