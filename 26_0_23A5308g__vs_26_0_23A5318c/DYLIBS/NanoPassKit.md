## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1274.1.0.0.0
-  __TEXT.__text: 0x2555f8
+1276.0.0.0.0
+  __TEXT.__text: 0x256954
   __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0x25ab0
-  __TEXT.__cstring: 0x17c28
+  __TEXT.__objc_methlist: 0x25b58
+  __TEXT.__cstring: 0x18018
   __TEXT.__const: 0xd34
-  __TEXT.__oslogstring: 0x2c7d7
-  __TEXT.__gcc_except_tab: 0x6e10
+  __TEXT.__oslogstring: 0x2cae7
+  __TEXT.__gcc_except_tab: 0x6dc8
   __TEXT.__dlopen_cstrs: 0x260
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x294

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x8ed0
+  __TEXT.__unwind_info: 0x8f08
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x6b98
-  __TEXT.__objc_methname: 0x3f977
-  __TEXT.__objc_methtype: 0xa08b
-  __TEXT.__objc_stubs: 0x22040
-  __DATA_CONST.__got: 0x1e78
-  __DATA_CONST.__const: 0x6b08
+  __TEXT.__objc_methname: 0x3fcaa
+  __TEXT.__objc_methtype: 0xa108
+  __TEXT.__objc_stubs: 0x220a0
+  __DATA_CONST.__got: 0x1e80
+  __DATA_CONST.__const: 0x6b80
   __DATA_CONST.__objc_classlist: 0x1200
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc970
+  __DATA_CONST.__objc_selrefs: 0xc9d0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x1130
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0xf50
   __AUTH_CONST.__const: 0x1750
-  __AUTH_CONST.__cfstring: 0xe9a0
-  __AUTH_CONST.__objc_const: 0x45b38
+  __AUTH_CONST.__cfstring: 0xeac0
+  __AUTH_CONST.__objc_const: 0x45c50
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0xb3e0
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x1c50
+  __DATA.__objc_ivar: 0x1c64
   __DATA.__data: 0x1f48
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 626B8D4D-2063-39A9-BCFF-98A2B84254E5
-  Functions: 14485
-  Symbols:   42477
-  CStrings:  17018
+  UUID: BCB00421-E061-3449-B197-76C6E73554AB
+  Functions: 14500
+  Symbols:   42519
+  CStrings:  17063
 
Symbols:
+ +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:shouldSuppressLiveActivity:]
+ -[NPKCompanionAgentConnection paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:]
+ -[NPKCompanionAgentConnection updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:]
+ -[NPKGizmoDatabase _removeSubcredentialsForPassWithUniqueIDLocked:]
+ -[NPKGizmoDatabase _setSubcredentialsLocked:forPassWithUniqueID:paymentApplicationIdentifier:]
+ -[NPKGizmoDatabase _subcredentialsForPassWithUniqueIDLocked:paymentApplicationIdentifier:]
+ -[NPKGizmoDatabase _updateSubcredentialsDuringMigration:]
+ -[NPKGizmoDatabase deleteAllSubcredentialsForPassUniqueIDStatement]
+ -[NPKGizmoDatabase deleteSubcredentialsStatement]
+ -[NPKGizmoDatabase insertSubcredentialsStatement]
+ -[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:]
+ -[NPKGizmoDatabase subcredentialsForPassWithUniqueID:paymentApplicationIdentifier:]
+ -[NPKProtoAddSecureElementPassWithPropertiesResponse hasPaymentApplicationID]
+ -[NPKProtoAddSecureElementPassWithPropertiesResponse paymentApplicationID]
+ -[NPKProtoAddSecureElementPassWithPropertiesResponse setPaymentApplicationID:]
+ -[NPKProtoHandleCredentialsChangeRequest hasPaymentApplicationID]
+ -[NPKProtoHandleCredentialsChangeRequest paymentApplicationID]
+ -[NPKProtoHandleCredentialsChangeRequest setPaymentApplicationID:]
+ -[NPKProtoRelevantPassTuple hasShouldSuppressLiveActivity]
+ -[NPKProtoRelevantPassTuple setHasShouldSuppressLiveActivity:]
+ -[NPKProtoRelevantPassTuple setShouldSuppressLiveActivity:]
+ -[NPKProtoRelevantPassTuple shouldSuppressLiveActivity]
+ -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:shouldSuppressLiveActivity:]
+ -[NPKRelevancyInformation setShouldSuppressLiveActivity:]
+ -[NPKRelevancyInformation shouldSuppressLiveActivity]
+ -[NPKSharedWebServiceProvider handleCredentialsUpdate:forUniqueID:paymentApplicationIdentifier:completion:]
+ -[NSDictionary(NPKRelevancy) npkRelevancyShouldSuppressLiveActivity]
+ GCC_except_table147
+ GCC_except_table226
+ GCC_except_table250
+ GCC_except_table268
+ GCC_except_table276
+ GCC_except_table278
+ GCC_except_table70
+ _OBJC_IVAR_$_NPKGizmoDatabase._deleteAllSubcredentialsForPassUniqueIDStatement
+ _OBJC_IVAR_$_NPKGizmoDatabase._deleteSubcredentialsStatement
+ _OBJC_IVAR_$_NPKGizmoDatabase._insertSubcredentialsStatement
+ _OBJC_IVAR_$_NPKProtoAddSecureElementPassWithPropertiesResponse._paymentApplicationID
+ _OBJC_IVAR_$_NPKProtoHandleCredentialsChangeRequest._paymentApplicationID
+ _OBJC_IVAR_$_NPKProtoRelevantPassTuple._has
+ _OBJC_IVAR_$_NPKProtoRelevantPassTuple._shouldSuppressLiveActivity
+ _OBJC_IVAR_$_NPKRelevancyInformation._shouldSuppressLiveActivity
+ _PKPassLibraryRelevantInfoSuppressLAAutoStart
+ ___101-[NPKCompanionAgentConnection updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:]_block_invoke
+ ___101-[NPKCompanionAgentConnection updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:]_block_invoke.176
+ ___120-[NPKCompanionAgentConnection paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:]_block_invoke
+ ___28-[NPKGizmoDatabase database]_block_invoke.273
+ ___41-[NPKGizmoDatabase savePass:isLocalPass:]_block_invoke.465
+ ___46-[NPKGizmoDatabase rebuildDatabaseWithPasses:]_block_invoke.467
+ ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke.472
+ ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke_2.473
+ ___59-[NPKGizmoDatabase _savePassLocked:locallyAdded:wasUpdate:]_block_invoke.477
+ ___60-[NPKGizmoDatabase _passForUniqueIDLocked:includeImageSets:]_block_invoke
+ ___61-[NPKGizmoDatabase _libraryHashLockedForWatchOSMajorVersion:]_block_invoke.587
+ ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.583
+ ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.584
+ ___69-[NPKGizmoDatabase _setLastAddValueAmountLocked:forPassWithUniqueID:]_block_invoke.481
+ ___69-[NPKGizmoDatabase _setTransitAppletStateLocked:forPassWithUniqueID:]_block_invoke.480
+ ___70-[NPKGizmoDatabase _setPendingAddValueDateLocked:forPassWithUniqueID:]_block_invoke.482
+ ___83-[NPKGizmoDatabase subcredentialsForPassWithUniqueID:paymentApplicationIdentifier:]_block_invoke
+ ___87-[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:]_block_invoke
+ ___87-[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:]_block_invoke.470
+ ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96s104s112s_e5_B8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_48_e8_32s40bs_e26_v20?0B8^{sqlite3_stmt=}12ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e31_v28?0B8"NSSet"12"NSString"20lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_B8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e17_v16?0"NSError"8lr56l8s32l8r64l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e26_v16?0"NPKGizmoDatabase"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e35_v32?0"NPKPassDescription"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e5_v8?0ls32l8s40l8s64l8s48l8s56l8r72l8r80l8
+ ___block_literal_global.240
+ _objc_msgSend$_removeSubcredentialsForPassWithUniqueIDLocked:
+ _objc_msgSend$_setSubcredentialsLocked:forPassWithUniqueID:paymentApplicationIdentifier:
+ _objc_msgSend$_subcredentialsForPassWithUniqueIDLocked:paymentApplicationIdentifier:
+ _objc_msgSend$_updateSubcredentialsDuringMigration:
+ _objc_msgSend$deleteAllSubcredentialsForPassUniqueIDStatement
+ _objc_msgSend$deleteSubcredentialsStatement
+ _objc_msgSend$handleCredentialsUpdate:forUniqueID:paymentApplicationIdentifier:completion:
+ _objc_msgSend$insertSubcredentialsStatement
+ _objc_msgSend$paymentApplicationID
+ _objc_msgSend$paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:
+ _objc_msgSend$setPaymentApplicationID:
+ _objc_msgSend$updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:
- +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:]
- -[NPKCompanionAgentConnection paymentPassWithUniqueIdentifier:didUpdateWithCredentials:]
- -[NPKCompanionAgentConnection updateCredentials:forUniqueID:completion:]
- -[NPKGizmoDatabase _setSubcredentialsLocked:forPassWithUniqueID:]
- -[NPKGizmoDatabase _subcredentialsForPassWithUniqueIDLocked:]
- -[NPKGizmoDatabase selectSubcredentialsForPassStatement]
- -[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:]
- -[NPKGizmoDatabase subcredentialsForPassWithUniqueID:]
- -[NPKGizmoDatabase updateSubcredentialsForPassStatement]
- -[NPKPassDescription setSubcredentials:]
- -[NPKPassDescription subcredentials]
- -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:]
- -[NPKSharedWebServiceProvider handleCredentialsUpdate:forUniqueID:completion:]
- GCC_except_table145
- GCC_except_table224
- GCC_except_table246
- GCC_except_table272
- GCC_except_table274
- _OBJC_IVAR_$_NPKGizmoDatabase._selectSubcredentialsForPassStatement
- _OBJC_IVAR_$_NPKGizmoDatabase._updateSubcredentialsForPassStatement
- _OBJC_IVAR_$_NPKPassDescription._subcredentials
- ___28-[NPKGizmoDatabase database]_block_invoke.267
- ___41-[NPKGizmoDatabase savePass:isLocalPass:]_block_invoke.456
- ___46-[NPKGizmoDatabase rebuildDatabaseWithPasses:]_block_invoke.458
- ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke.462
- ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke_2.463
- ___54-[NPKGizmoDatabase subcredentialsForPassWithUniqueID:]_block_invoke
- ___58-[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:]_block_invoke
- ___59-[NPKGizmoDatabase _savePassLocked:locallyAdded:wasUpdate:]_block_invoke.467
- ___61-[NPKGizmoDatabase _libraryHashLockedForWatchOSMajorVersion:]_block_invoke.560
- ___65-[NPKGizmoDatabase _setSubcredentialsLocked:forPassWithUniqueID:]_block_invoke
- ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.556
- ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.557
- ___69-[NPKGizmoDatabase _setLastAddValueAmountLocked:forPassWithUniqueID:]_block_invoke.471
- ___69-[NPKGizmoDatabase _setTransitAppletStateLocked:forPassWithUniqueID:]_block_invoke.470
- ___70-[NPKGizmoDatabase _setPendingAddValueDateLocked:forPassWithUniqueID:]_block_invoke.472
- ___72-[NPKCompanionAgentConnection updateCredentials:forUniqueID:completion:]_block_invoke
- ___72-[NPKCompanionAgentConnection updateCredentials:forUniqueID:completion:]_block_invoke.176
- ___88-[NPKCompanionAgentConnection paymentPassWithUniqueIdentifier:didUpdateWithCredentials:]_block_invoke
- ___block_descriptor_138_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e5_B8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_40_e8_32bs_e26_v20?0B8^{sqlite3_stmt=}12ls32l8
- ___block_descriptor_48_e8_32bs40r_e18_v20?0B8"NSSet"12lr40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8lr56l8s32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s64l8s48l8s56l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e26_v16?0"NPKGizmoDatabase"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e35_v32?0"NPKPassDescription"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.234
- _objc_msgSend$_setSubcredentialsLocked:forPassWithUniqueID:
- _objc_msgSend$_subcredentialsForPassWithUniqueIDLocked:
- _objc_msgSend$handleCredentialsUpdate:forUniqueID:completion:
- _objc_msgSend$paymentPassWithUniqueIdentifier:didUpdateWithCredentials:
- _objc_msgSend$selectSubcredentialsForPassStatement
- _objc_msgSend$setSubcredentials:forPassWithUniqueID:
- _objc_msgSend$subcredentialsForPassWithUniqueID:
- _objc_msgSend$updateCredentials:forUniqueID:completion:
- _objc_msgSend$updateSubcredentialsForPassStatement
CStrings:
+ "-[NPKGizmoDatabase _removeSubcredentialsForPassWithUniqueIDLocked:]"
+ "-[NPKGizmoDatabase _setSubcredentialsLocked:forPassWithUniqueID:paymentApplicationIdentifier:]"
+ "-[NPKGizmoDatabase _subcredentialsForPassWithUniqueIDLocked:paymentApplicationIdentifier:]"
+ "-[NPKGizmoDatabase deleteAllSubcredentialsForPassUniqueIDStatement]"
+ "-[NPKGizmoDatabase deleteSubcredentialsStatement]"
+ "-[NPKGizmoDatabase insertSubcredentialsStatement]"
+ "-[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:]_block_invoke"
+ "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n\tshouldSuppressLiveActivity: %@\n>"
+ "ALTER TABLE pass DROP COLUMN subcredentials"
+ "CREATE INDEX IF NOT EXISTS subcredentials_index ON subcredentials(pass_unique_id)"
+ "CREATE TABLE IF NOT EXISTS subcredentials (pass_unique_id TEXT, payment_application_id TEXT, encoded_subcredentials BLOB);"
+ "DELETE FROM subcredentials WHERE pass_unique_id = ?"
+ "DELETE FROM subcredentials WHERE pass_unique_id = ? AND payment_application_id = ?"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Delete subcredential sets failed: %s; %s)"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Insert subcredential set failed: %s; %s)"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare delete all subcredentials for pass statement)"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare delete subcredentials statement)"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare insert subcredentials statement)"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare select subcredentials statement: %s)"
+ "Error: Delete subcredentials from pass table failed. result %d, dbError: %s"
+ "Error: Error while updating credentials %@ for pass unique ID: %@, paymentApplicationIdentifier: %@. Error: %@"
+ "Error: Failed to prepare statements for subcredential migration. selectResult: %d, insertResult: %d, deleteResult: %d, dbError: %s"
+ "Error: Insert into subcredentials table failed for unique ID %@ paymentApplicationIdentifier %@ result %d, dbError: %s"
+ "Error: Missing unique ID in migration dictionary. Skipping this pass."
+ "Error: Select subcredentials from pass table failed for unique ID %@ paymentApplicationIdentifier %@ result %d, dbError: %s"
+ "INSERT INTO pass (unique_id, type_id, style, hash, encoded_pass, encoded_image_sets, encoded_diff, logo_text, logo_image, background_color, label_color, foreground_color, background_image, nfc_payload, private_label, cobranded, device_payment_applications, device_primary_payment_application, device_primary_contactless_payment_application, device_primary_in_app_payment_application, preferred_aid, preferred_payment_application, ingested_date, complete_hash, delete_pending, effective_payment_application_state, has_user_selectable_payment_applications, has_stored_value, settings, complete_hashes, issuer_country_code, available_actions, organization_name, felica_transit_applet_state, front_field_buckets, back_field_buckets, last_add_value_amount, localized_description, pending_add_value_date, express_pass_types_mask, complete_remote_hashes, supports_pp, balances) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "INSERT INTO subcredentials (pass_unique_id, payment_application_id, encoded_subcredentials) VALUES (?, ?, ?)"
+ "Notice: Did complete credentials update %@ for unique ID %@ paymentApplicationIdentifier %@. Error: %@"
+ "Notice: Got credentials update for unique ID %@ with %u credentials for paymentApplicationIdentifier %@"
+ "Notice: Handled credentials update %@ for unique ID %@ paymentApplicationIdentifier %@ with error: %@"
+ "Notice: Handling credentials update %@ for unique ID %@ paymentApplicationIdentifier %@"
+ "Notice: Handling credentials update %@ for unique ID: %@, paymentApplicationIdentifier: %@"
+ "Notice: NPKCompanionAgentConnection (%@): Payment pass with uniqueID: %@ did update credentials: %@, for paymentApplicationIdentifier %@"
+ "SELECT encoded_subcredentials FROM subcredentials WHERE pass_unique_id = ? AND payment_application_id = ?"
+ "SELECT encoded_subcredentials FROM subcredentials WHERE pass_unique_id = ? AND payment_application_id IS NULL"
+ "SELECT unique_id, type_id, style, hash, logo_text, logo_image, background_color, label_color, foreground_color, delete_pending, background_image, nfc_payload, private_label, cobranded, device_payment_applications, device_primary_payment_application, device_primary_contactless_payment_application, device_primary_in_app_payment_application, preferred_payment_application, ingested_date, complete_hash, effective_payment_application_state, has_user_selectable_payment_applications, has_stored_value, settings, complete_hashes, issuer_country_code, available_actions, organization_name, felica_transit_applet_state, front_field_buckets, back_field_buckets, last_add_value_amount, localized_description, pending_add_value_date, express_pass_types_mask, complete_remote_hashes, supports_pp FROM pass"
+ "T@\"NSString\",&,N,V_paymentApplicationID"
+ "TB,N,V_shouldSuppressLiveActivity"
+ "TB,V_shouldSuppressLiveActivity"
+ "_deleteAllSubcredentialsForPassUniqueIDStatement"
+ "_deleteSubcredentialsStatement"
+ "_insertSubcredentialsStatement"
+ "_paymentApplicationID"
+ "_removeSubcredentialsForPassWithUniqueIDLocked:"
+ "_setSubcredentialsLocked:forPassWithUniqueID:paymentApplicationIdentifier:"
+ "_shouldSuppressLiveActivity"
+ "_subcredentialsForPassWithUniqueIDLocked:paymentApplicationIdentifier:"
+ "_updateSubcredentialsDuringMigration:"
+ "deleteAllSubcredentialsForPassUniqueIDStatement"
+ "deleteSubcredentialsStatement"
+ "devicePrimaryPaymentApplicationIdentifier"
+ "fpanDescriptorAndCredentialForFPAN:descriptor:credential:error:"
+ "handleCredentialsUpdate:forUniqueID:paymentApplicationIdentifier:completion:"
+ "hasPaymentApplicationID"
+ "hasShouldSuppressLiveActivity"
+ "initWithPassUniqueID:groupID:relevantText:shouldSuppressLiveActivity:"
+ "insertSubcredentialsStatement"
+ "npkRelevancyShouldSuppressLiveActivity"
+ "npkRelevancyTupleWithUniqueID:relevantText:shouldSuppressLiveActivity:"
+ "paymentApplicationID"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:"
+ "setHasShouldSuppressLiveActivity:"
+ "setPaymentApplicationID:"
+ "setShouldSuppressLiveActivity:"
+ "setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:"
+ "shouldSuppressLiveActivity"
+ "subcredentialsForPassWithUniqueID:paymentApplicationIdentifier:"
+ "updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:"
+ "v28@?0B8@\"NSSet\"12@\"NSString\"20"
+ "v40@0:8@\"NSString\"16@\"NSSet\"24@\"NSString\"32"
+ "v48@0:8@\"NSSet\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16^@24^@32^@40"
+ "{?=\"shouldSuppressLiveActivity\"b1}"
- " ( subcredentials %@)"
- "-[NPKGizmoDatabase _setSubcredentialsLocked:forPassWithUniqueID:]"
- "-[NPKGizmoDatabase selectSubcredentialsForPassStatement]"
- "-[NPKGizmoDatabase setSubcredentials:forPassWithUniqueID:]_block_invoke"
- "-[NPKGizmoDatabase updateSubcredentialsForPassStatement]"
- "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n>"
- "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare \"select subcredentials state\" statement)"
- "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare \"update subcredentials state\" statement)"
- "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Updating subcredentials failed: %s; %s)"
- "Error: Error while updating credentials %@ for pass unique ID: %@. Error: %@"
- "INSERT INTO pass (unique_id, type_id, style, hash, encoded_pass, encoded_image_sets, encoded_diff, logo_text, logo_image, background_color, label_color, foreground_color, background_image, nfc_payload, private_label, cobranded, device_payment_applications, device_primary_payment_application, device_primary_contactless_payment_application, device_primary_in_app_payment_application, preferred_aid, preferred_payment_application, ingested_date, complete_hash, delete_pending, effective_payment_application_state, has_user_selectable_payment_applications, has_stored_value, settings, complete_hashes, issuer_country_code, available_actions, organization_name, felica_transit_applet_state, front_field_buckets, back_field_buckets, last_add_value_amount, localized_description, pending_add_value_date, express_pass_types_mask, complete_remote_hashes, supports_pp, balances, subcredentials) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "Notice: (PKAppletSubcredential restore) archiving old subcredentials for pass %@ %@ returned nil"
- "Notice: (PKAppletSubcredential restore) restoring old subcredentials for pass %@ %@"
- "Notice: Did complete credentials update %@ for unique ID %@. Error: %@"
- "Notice: Got credentials update for unique ID %@ with %u credentials"
- "Notice: Handled credentials update %@ for unique ID %@ with error: %@"
- "Notice: Handling credentials update %@ for unique ID %@"
- "Notice: NPKCompanionAgentConnection (%@): Payment pass did update credentials: %@, credentials %@"
- "Notice: Updating description %@ with new subcredentials %@"
- "SELECT unique_id, type_id, style, hash, logo_text, logo_image, background_color, label_color, foreground_color, delete_pending, background_image, nfc_payload, private_label, cobranded, device_payment_applications, device_primary_payment_application, device_primary_contactless_payment_application, device_primary_in_app_payment_application, preferred_payment_application, ingested_date, complete_hash, effective_payment_application_state, has_user_selectable_payment_applications, has_stored_value, settings, complete_hashes, issuer_country_code, available_actions, organization_name, felica_transit_applet_state, front_field_buckets, back_field_buckets, last_add_value_amount, localized_description, pending_add_value_date, express_pass_types_mask, complete_remote_hashes, supports_pp, subcredentials FROM pass"
- "T@\"NSSet\",&,N,V_subcredentials"
- "UPDATE pass SET subcredentials = ? WHERE unique_id = ?"
- "Warning: Assigning subcredentials to devicePrimaryPaymentApplication for pass with more than one devicePaymentApplications. Expect bad thing to happen."
- "_selectSubcredentialsForPassStatement"
- "_setSubcredentialsLocked:forPassWithUniqueID:"
- "_subcredentials"
- "_subcredentialsForPassWithUniqueIDLocked:"
- "_updateSubcredentialsForPassStatement"
- "handleCredentialsUpdate:forUniqueID:completion:"
- "initWithPassUniqueID:groupID:relevantText:"
- "npkRelevancyTupleWithUniqueID:relevantText:"
- "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:"
- "selectSubcredentialsForPassStatement"
- "setSubcredentials:forPassWithUniqueID:"
- "subcredentialsForPassWithUniqueID:"
- "updateCredentials:forUniqueID:completion:"
- "updateSubcredentialsForPassStatement"
- "v20@?0B8@\"NSSet\"12"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"

```
