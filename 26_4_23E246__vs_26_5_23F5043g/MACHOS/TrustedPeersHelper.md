## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.102.2.0.0
-  __TEXT.__text: 0x254190
+61901.120.36.0.3
+  __TEXT.__text: 0x24992c
   __TEXT.__auth_stubs: 0x1f90
-  __TEXT.__objc_stubs: 0x5aa0
-  __TEXT.__objc_methlist: 0x2818
-  __TEXT.__const: 0xb2f8
-  __TEXT.__cstring: 0x168cb
-  __TEXT.__oslogstring: 0xad1a
+  __TEXT.__objc_stubs: 0x5ac0
+  __TEXT.__objc_methlist: 0x2830
+  __TEXT.__const: 0xce50
+  __TEXT.__cstring: 0x153f1
+  __TEXT.__oslogstring: 0xae0a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x142f
-  __TEXT.__objc_methname: 0x86f1
+  __TEXT.__objc_methname: 0x8731
   __TEXT.__objc_methtype: 0x246c
-  __TEXT.__constg_swiftt: 0x39a8
-  __TEXT.__swift5_typeref: 0x39f6
-  __TEXT.__swift5_fieldmd: 0x291c
-  __TEXT.__swift5_reflstr: 0x2387
+  __TEXT.__constg_swiftt: 0x39c4
+  __TEXT.__swift5_typeref: 0x3a16
+  __TEXT.__swift5_fieldmd: 0x29c8
+  __TEXT.__swift5_reflstr: 0x2427
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0x940
-  __TEXT.__swift5_types: 0x2ac
+  __TEXT.__swift5_assocty: 0x420
+  __TEXT.__swift5_proto: 0x958
+  __TEXT.__swift5_types: 0x2b0
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__swift5_capture: 0x475c
   __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x4d08
-  __TEXT.__eh_frame: 0x7ae0
+  __TEXT.__unwind_info: 0x4b00
+  __TEXT.__eh_frame: 0x7b10
   __DATA_CONST.__auth_got: 0xfd8
   __DATA_CONST.__got: 0x938
-  __DATA_CONST.__auth_ptr: 0x6c0
-  __DATA_CONST.__const: 0x138f8
-  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__auth_ptr: 0x6b8
+  __DATA_CONST.__const: 0x13a40
+  __DATA_CONST.__cfstring: 0x17e0
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA.__objc_const: 0x6ac8
-  __DATA.__objc_selrefs: 0x1d28
-  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_const: 0x6af8
+  __DATA.__objc_selrefs: 0x1d38
+  __DATA.__objc_ivar: 0x1f0
   __DATA.__objc_data: 0x2b28
-  __DATA.__data: 0x8018
+  __DATA.__data: 0x8048
   __DATA.__objc_stublist: 0xa8
-  __DATA.__bss: 0x12498
-  __DATA.__common: 0x9b0
+  __DATA.__bss: 0x12798
+  __DATA.__common: 0x9c8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6DC3DB1F-D8A0-3B55-8AAD-6A7ED453CBC6
-  Functions: 8467
+  UUID: B7BB6571-3E1A-3D68-899B-C32773732DA6
+  Functions: 8496
   Symbols:   510
-  CStrings:  3395
+  CStrings:  3182
 
CStrings:
+ "<TPWalrusExtraArguments(isDBRv2:%@ pdpState:%d)>"
+ "Asking cuttlefish to disable walrus in dbr state: %s with pre-records: %s"
+ "Asking cuttlefish to enable walrus in dbr state: %s with pre-records: %s"
+ "DBR pre-record blob: %s"
+ "Ti,V_pdpState"
+ "_pdpState"
+ "cannot enable walrus in unknown PDP state %ld"
+ "com.apple.protectedcloudstorage.dbrv2.record"
+ "pdpState"
+ "setPdpState:"
- "<TPWalrusExtraArguments(isDBRv2:%@)>"
- "ACCOUNT_FLAGS_CDP"
- "ACCOUNT_FLAGS_DBR"
- "ACCOUNT_FLAGS_DEMO"
- "ACCOUNT_FLAGS_INTERNAL"
- "ACCOUNT_FLAGS_SA_OR_2FAFA"
- "ACCOUNT_FLAGS_UNKNOWN"
- "ESCROW_CHECK_GRAPH_NEEDS_REPAIR"
- "ESCROW_CHECK_NA"
- "ESCROW_CHECK_NOT_TRUSTED"
- "ESCROW_CHECK_OK"
- "ESCROW_CHECK_REPAIR_NEEDED"
- "ESCROW_CHECK_UNKNOWN"
- "FILTERING_REQUEST_BY_OCTAGON_ONLY"
- "FILTERING_REQUEST_UNKNOWN"
- "GRAPH_NEEDS_REPAIR"
- "GRAPH_OK"
- "GRAPH_STATUS_UNKNOWN"
- "IdmsTrustedDevicesVersionString"
- "NO_RECORD_MATCHING_PASSCODE_GENERATION"
- "NO_RECORD_MATCHING_PEER"
- "NO_RECORD_MATCHING_RECOVERABLE"
- "PEER_UNTRUSTED"
- "RECORD_NEEDS_MIGRATION"
- "RECORD_OK"
- "RECORD_REPAIR_REASON_UNKNOWN"
- "RECORD_STATUS_INVALID"
- "RECORD_STATUS_VALID"
- "REPAIR_ACTION_LEAVE_TRUST"
- "REPAIR_ACTION_NO_ACTION"
- "REPAIR_ACTION_POST_REPAIR_ACCOUNT"
- "REPAIR_ACTION_POST_REPAIR_ESCROW"
- "REPAIR_ACTION_REROLL"
- "REPAIR_ACTION_RESET_OCTAGON"
- "RESET_REASON_HEALTH_CHECK"
- "RESET_REASON_LEGACY_JOIN_CIRCLE"
- "RESET_REASON_NO_BOTTLE_DURING_ESCROW_RECOVERY"
- "RESET_REASON_RECOVERY_KEY"
- "RESET_REASON_SUPPORT_APP_INITIATED_RESET"
- "RESET_REASON_TEST_GENERATED"
- "RESET_REASON_UNKNOWN"
- "RESET_REASON_USER_INITIATED_RESET"
- "SOS_NOT_VIABLE"
- "SOS_VIABLE"
- "SOS_VIABLE_UNKNOWN"
- "SUPPORT_APP_DEVICE_STATUS_BROKEN"
- "SUPPORT_APP_DEVICE_STATUS_HEALTHY"
- "VIEW_KEY_CLASS_CLASS_A"
- "VIEW_KEY_CLASS_CLASS_C"
- "VIEW_KEY_CLASS_TLK"
- "accountInfo"
- "account_info"
- "add"
- "backup_keybag_digest"
- "bottle"
- "bottle_id"
- "caesar_peers"
- "caesar_peers_cleaned_up"
- "caesar_peers_cleanup_enabled"
- "change_token"
- "changes"
- "class_a"
- "class_c"
- "client_metadata"
- "collectable_device_state_records"
- "collectable_escrow_records"
- "collectable_tlk_shares"
- "collected_device_state_records"
- "collected_escrow_records"
- "collected_tlk_shares"
- "creation_date"
- "current_federation"
- "current_items"
- "custodian_recovery_key"
- "custodian_recovery_key_and_sig"
- "dangling_peers_cleaned_up"
- "dangling_peers_cleanup_enabled"
- "device_color"
- "device_enclosure_color"
- "device_mid"
- "device_model"
- "device_model_class"
- "device_model_version"
- "device_name"
- "device_platform"
- "device_session_id"
- "device_state_record_deletion_failed"
- "devices"
- "differences"
- "disable_repair"
- "disable_with_error"
- "duplicate_escrow_records"
- "dynamic_info_and_sig"
- "entries"
- "escrow"
- "escrowRecords"
- "escrow_check_result"
- "escrow_information_metadata"
- "escrow_record_garbage_collection_enabled"
- "escrow_record_id"
- "escrow_record_label"
- "escrow_record_move_request"
- "escrow_repair_reason"
- "escrowed_signing_spki"
- "escrowed_spki"
- "expected_federation_id"
- "federation_id"
- "filter_request"
- "flags"
- "flow_id"
- "fully_dangling_peer_count_validation_fails"
- "fully_dangling_peers"
- "graph_status"
- "idmsCuttlefishPassword"
- "idmsTargetContext"
- "idms_updated"
- "intended_federation"
- "is_background_check"
- "item_pointer_name"
- "item_specifier"
- "items"
- "key_uuid"
- "known_federations"
- "last_health_report"
- "last_report"
- "legacy_records"
- "metrics"
- "model_id"
- "more"
- "new_class_a"
- "new_class_c"
- "new_tlk"
- "old_tlk"
- "page"
- "paginationToken"
- "parentkey_uuid"
- "partial_bottles"
- "partially_dangling_peer_count_validation_fails"
- "partially_dangling_peers"
- "passcodeGeneration"
- "passcode_generation"
- "passwordKeychainItemCount"
- "pcs_service"
- "pcs_services"
- "peer"
- "peer_dynamic_info"
- "peer_id"
- "peer_info"
- "peer_permanent_info"
- "peer_stable_info"
- "peers_cleanedup"
- "perform_caesar_peer_cleanup"
- "perform_cleanup"
- "perform_dangling_peer_cleanup"
- "permanent_info_and_sig"
- "public_key"
- "rate_limited"
- "receiver_public_encryption_key"
- "record"
- "record_status"
- "recovery_encryption_pub_key"
- "recovery_signing_pub_key"
- "recovery_voucher"
- "remaining_attempts"
- "remove"
- "repair_action"
- "repair_disabled"
- "requires_escrow_check"
- "reset_reason"
- "secure_backup_metadata_timestamp"
- "secure_backup_numeric_passphrase_length"
- "secure_backup_timestamp"
- "secure_backup_uses_complex_passphrase"
- "secure_backup_uses_multiple_icscs"
- "secure_backup_uses_numeric_passphrase"
- "serial_number"
- "service_identifier"
- "signature_using_escrow_key"
- "signature_using_peer_key"
- "silent_attempt_allowed"
- "sos"
- "stable_info_and_sig"
- "superfluous_peers"
- "superfluous_peers_cleanup_enabled"
- "synckeys"
- "testingNotifyIdms"
- "timestamp"
- "tlk_share_deletion_failed"
- "tlk_share_garbage_collection_enabled"
- "tlk_shares"
- "totalDevices"
- "total_device_state_records"
- "total_escrow_records"
- "total_escrow_records_fully_viable"
- "total_escrow_records_legacy"
- "total_escrow_records_partially_viable"
- "total_peers"
- "total_tlk_shares"
- "trusted_devices_version"
- "trusted_peers"
- "unsetHMACpeers"
- "update"
- "update_idms"
- "updatedHMACpeers"
- "upload_os_version"
- "viability_status"
- "viable_bottles"
- "view"
- "view_keys"
- "views"
- "voucher"
- "wrappedkey_base64"
- "zone_key_hierarchy_records"

```
