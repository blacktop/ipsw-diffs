## libbootpolicy.dylib

> `/usr/lib/libbootpolicy.dylib`

```diff

-  __TEXT.__text: 0x3c430
+  __TEXT.__text: 0x3ca90
   __TEXT.__const: 0x2818
   __TEXT.__cstring: 0x5be3
   __TEXT.__oslogstring: 0x14e3
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _bootpolicy_os_type_to_string : 68 -> 76
~ _bootpolicy_get_current_os_type : 996 -> 1028
~ _bootpolicy_error_to_string : 68 -> 76
~ _bootpolicy_get_current_os_type_restrictions_override_status : 912 -> 928
~ _bootpolicy_get_local_policy_pairing_status : 848 -> 864
~ _bootpolicy_update_local_policy_nonce_begin : 520 -> 536
~ __update_policy_nonce : 736 -> 752
~ _bootpolicy_update_local_policy_nonce_start_interruptible : 684 -> 700
~ _bootpolicy_update_local_policy_nonce_stop_interruptible : 684 -> 700
~ _bootpolicy_update_local_policy_finalize_filesystem_and_sidp : 560 -> 576
~ __update_local_policy_finalize_filesystem_and_sidp : 636 -> 652
~ _bootpolicy_update_local_policy_nonce_end : 644 -> 660
~ _bootpolicy_update_local_policy_nonce_reset : 540 -> 556
~ _bootpolicy_update_remote_policy_nonce_begin : 532 -> 548
~ _bootpolicy_update_remote_policy_nonce_end : 1088 -> 1120
~ _bootpolicy_update_remote_policy_nonce_reset : 540 -> 556
~ _bootpolicy_update_recoveryos_policy_nonce_begin : 520 -> 536
~ _bootpolicy_update_recoveryos_policy_finalize_filesystem_and_sidp : 556 -> 572
~ __unified_finalize : 24488 -> 24520
~ _bootpolicy_update_recoveryos_policy_nonce_end : 520 -> 536
~ _bootpolicy_update_recoveryos_policy_nonce_reset : 520 -> 536
~ _bootpolicy_disable_local_policies : 520 -> 536
~ _bootpolicy_get_local_policy_count : 1016 -> 1032
~ _bootpolicy_get_blessed_recoveryos_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_blessed_local_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_proposed_local_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_proposed_remote_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_proposed_recoveryos_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_blessed_remote_policy_nonce_digest : 516 -> 532
~ _bootpolicy_get_oic : 768 -> 784
~ _bootpolicy_store_oic : 800 -> 816
~ _bootpolicy_get_linked_manifest : 564 -> 580
~ _bootpolicy_get_linked_manifest_ex : 1584 -> 1600
~ _bootpolicy_create_linked_manifest : 1508 -> 1524
~ _bootpolicy_delete_linked_manifest : 968 -> 984
~ _bootpolicy_volume_has_auxkc_manifest : 840 -> 856
~ _bootpolicy_get_booted_local_policy : 776 -> 792
~ _bootpolicy_volume_has_local_policy : 540 -> 556
~ _bootpolicy_volume_has_local_policy_ex : 812 -> 828
~ _bootpolicy_get_local_policy_ex : 764 -> 780
~ _bootpolicy_get_local_policy : 548 -> 564
~ _bootpolicy_get_security_mode : 540 -> 556
~ _bootpolicy_get_security_mode_ex : 836 -> 852
~ _bootpolicy_get_nsih : 548 -> 564
~ _bootpolicy_get_nsih_ex : 652 -> 668
~ _bootpolicy_get_local_policy_digest_tag_ex2 : 1292 -> 1308
~ _bootpolicy_get_spih : 652 -> 668
~ _bootpolicy_verify_local_policy_uakl : 564 -> 580
~ _bootpolicy_verify_local_policy_uakl_ex : 884 -> 900
~ _bootpolicy_get_sip_flags : 540 -> 556
~ _bootpolicy_get_sip_flags_ex : 1064 -> 1080
~ _bootpolicy_get_sip_flags_ex2 : 552 -> 568
~ _bootpolicy_get_local_policy_integer_tag_ex : 1056 -> 1072
~ _bootpolicy_get_local_policy_integer_tag : 548 -> 564
~ _bootpolicy_get_local_policy_digest_tag : 568 -> 584
~ _bootpolicy_get_local_policy_digest_tag_ex : 572 -> 588
~ _bootpolicy_get_local_policy_uuid_tag : 1196 -> 1212
~ _bootpolicy_get_local_policy_boolean_tag : 548 -> 564
~ _bootpolicy_get_local_policy_boolean_tag_ex : 1076 -> 1092
~ _bootpolicy_create_paired_recoveryos_local_policy : 1520 -> 1536
~ _bootpolicy_create_local_policy_ex : 572 -> 588
~ _bootpolicy_create_local_policy_ex2 : 1940 -> 1956
~ _bootpolicy_create_local_policy_with_splat : 5688 -> 5704
~ _bootpolicy_update_paired_recoveryos_local_policy_for_software_update : 1704 -> 1720
~ _bootpolicy_update_local_policy_for_software_update_ex : 5436 -> 5452
~ _bootpolicy_update_local_policy_for_splat_update : 1704 -> 1720
~ _bootpolicy_update_local_policy_for_post_software_update_fixups : 1004 -> 1020
~ _bootpolicy_update_local_policy_uakl : 996 -> 1012
~ _bootpolicy_update_local_policy_boolean_tag : 984 -> 1000
~ _bootpolicy_update_sip_flags : 552 -> 568
~ _bootpolicy_update_sip_flags_ex : 552 -> 568
~ _bootpolicy_remove_sip_flags : 548 -> 564
~ _bootpolicy_update_local_policy_for_kcos : 1964 -> 1980
~ _bootpolicy_update_local_policy_for_custom_os : 540 -> 556
~ _bootpolicy_update_local_policy_for_custom_os_ex : 1980 -> 1996
~ _bootpolicy_revert_local_policy_to_defaults : 1112 -> 1128
~ _bootpolicy_create_kcos_auth_token_ex : 844 -> 860
~ _bootpolicy_consume_kcos_auth_token : 728 -> 744
~ _bootpolicy_mdm_is_managed : 540 -> 556
~ _bootpolicy_mdm_is_managed_ex : 844 -> 860
~ _bootpolicy_mdm_is_dep_managed : 844 -> 860
~ _bootpolicy_mdm_update_user_enrolled_mode : 972 -> 988
~ _bootpolicy_mdm_update_dep_mode : 968 -> 984
~ _bootpolicy_mdm_update_kexts_mode : 968 -> 984
~ _bootpolicy_mdm_reduce_security_mode : 1704 -> 1720
~ _bootpolicy_mdm_reduce_security_mode_with_splat : 5208 -> 5224
~ _bootpolicy_sidp_measure_all : 548 -> 564
~ _bootpolicy_get_root_volume_uuid : 548 -> 564
~ _bootpolicy_verify_baa_signing : 728 -> 744
~ _bootpolicy_verify_local_policy_pairing : 1200 -> 1216
~ _bootpolicy_set_debug_flags : 812 -> 828
~ _bootpolicy_clear_nvram : 664 -> 680
~ _bootpolicy_get_linked_manifest_tag_list : 848 -> 864
~ _bootpolicy_prepare_for_hibernation : 816 -> 832
~ __create_system_recoveryos_sidp_measurements : 1276 -> 1292
~ __create_sidp_measurement : 1244 -> 1260
~ __update_local_policy_for_new_local_and_remote_nonces : 840 -> 856
~ __update_local_policy_for_new_local_nonce : 844 -> 860
~ __finalize_sidp_measurements : 740 -> 756
~ _bootpolicy_update_local_policy_for_post_software_update_fixups_with_splat : 3372 -> 3388
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/dylib/backend.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/dylib/dylib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/shared/der.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/shared/env_data.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/shared/file_utility.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/shared/image4.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ic9P4w/Sources/BootPolicy/shared/platform_user.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/dylib/backend.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/dylib/dylib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/shared/der.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/shared/env_data.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/shared/file_utility.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/shared/image4.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKldKd/Sources/BootPolicy/shared/platform_user.c"

```
