## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-625.100.7.0.0
-  __TEXT.__text: 0x1ba04
+625.120.3.0.0
+  __TEXT.__text: 0x1bcfc
   __TEXT.__auth_stubs: 0x1390
   __TEXT.__objc_methlist: 0x260
-  __TEXT.__cstring: 0x7aa7
+  __TEXT.__cstring: 0x7e6f
   __TEXT.__const: 0x4e6
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x620
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x874
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x14e9
   __TEXT.__objc_methtype: 0x9b0
   __TEXT.__objc_stubs: 0x10a0
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x120
+  __DATA.__data: 0x378
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29D0287F-09CB-37EA-9CD3-60A9C376593C
-  Functions: 536
-  Symbols:   1719
-  CStrings:  1904
+  UUID: 71D69049-16BC-321B-BBDE-940264FE6804
+  Functions: 538
+  Symbols:   1724
+  CStrings:  1927
 
Symbols:
+ ___analytics_send_fv_status_block_invoke
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.132
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.173
+ _analytics_send_fv_status
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.150
CStrings:
+ "AnalyticsEvent: fv_enabled: %llu, fv_users_count: %llu, icloud_recovery_key: %llu, institutional_recovery_key: %llu, personal_recovery_key: %llu, mdm_recovery_key: %llu, installer_user: %llu, icloud_recovery_user: %llu, institutional_recovery_user: %llu, vek_device_protected: %llu, vek_ephemeral: %llu, vek_is_owner: %llu, vek_boot_policy: %llu, vek_imported: %llu, kek_sidp_count: %llu, kek_ps_count: %llu, kek_last_count: %llu, kek_imported_count: %llu, kek_bad_sig_count: %llu, kek_xart_policy_missing_count: %llu, kek_ps_missing_count: %llu"
+ "analytics_send_fv_status"
+ "com.apple.mobile.keybagd.filevault.status"
+ "fv_enabled"
+ "fv_users_count"
+ "icloud_recovery_key"
+ "icloud_recovery_user"
+ "installer_user"
+ "institutional_recovery_key"
+ "institutional_recovery_user"
+ "kek_bad_sig_count"
+ "kek_imported_count"
+ "kek_last_count"
+ "kek_ps_count"
+ "kek_ps_missing_count"
+ "kek_sidp_count"
+ "kek_xart_policy_missing_count"
+ "mdm_recovery_key"
+ "personal_recovery_key"
+ "vek_boot_policy"
+ "vek_device_protected"
+ "vek_ephemeral"
+ "vek_imported"
+ "vek_is_owner"
- "AnalyticsEvent: status: %llu"

```
