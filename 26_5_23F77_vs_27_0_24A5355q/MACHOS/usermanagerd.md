## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0xaeb4c
-  __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0x1a18
-  __TEXT.__const: 0x141c
-  __TEXT.__gcc_except_tab: 0x16b4
-  __TEXT.__cstring: 0x73fa
-  __TEXT.__objc_classname: 0x39a
-  __TEXT.__objc_methname: 0x3885
-  __TEXT.__objc_methtype: 0x146e
-  __TEXT.__oslogstring: 0x119e2
-  __TEXT.__unwind_info: 0x1560
-  __DATA_CONST.__auth_got: 0xc50
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x2770
-  __DATA_CONST.__cfstring: 0x1ca0
+488.0.0.0.0
+  __TEXT.__text: 0xae070
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0x1a78
+  __TEXT.__const: 0x1434
+  __TEXT.__gcc_except_tab: 0x161c
+  __TEXT.__cstring: 0x7653
+  __TEXT.__objc_classname: 0x37a
+  __TEXT.__objc_methname: 0x396d
+  __TEXT.__objc_methtype: 0x14ab
+  __TEXT.__oslogstring: 0x12070
+  __TEXT.__unwind_info: 0x15d0
+  __DATA_CONST.__const: 0x27c0
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x46a8
-  __DATA.__objc_selrefs: 0xce8
+  __DATA_CONST.__auth_got: 0xc70
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA.__objc_const: 0x46c8
+  __DATA.__objc_selrefs: 0xd10
   __DATA.__objc_ivar: 0x1e4
   __DATA.__objc_data: 0xa00
-  __DATA.__data: 0x12b8
+  __DATA.__data: 0x12c0
   __DATA.__bss: 0x371
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 042F44D6-4FFC-3458-BDC2-9F154E7D8691
-  Functions: 2372
-  Symbols:   462
-  CStrings:  3587
+  UUID: 8AEAEA65-6BFE-3B4B-9644-E0487022789D
+  Functions: 2403
+  Symbols:   468
+  CStrings:  3632
 
Symbols:
+ ___NSArray0__struct
+ ___stderrp
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "Could not provision due to error..."
+ "Failed to get data protection class for given path %s with errno %s (%d)\n"
+ "Fetch persona BundleID Mapping failed with error:%@"
+ "Found bundleID mapping for %@"
+ "Found no existing bundleIDMapping, returning empty dict"
+ "Found persona Array, parsing bundleID mappings"
+ "In RDServer: PersonaBundleIDMigration FF set, fetchBundleIdentifiersForPersona not supported:%d"
+ "In RDServer: PersonaBundleIDMigration FF set, fetchMultiPersonaBundleIdentifiersforPid not supported:%d"
+ "In RDServer: PersonaBundleIDMigration FF set, setMultiPersonaBundlesIdentifiers not supported:%d"
+ "In RDServer: PersonaBundleIDMigration FF set, setSinglePersonaBundlesIdentifiers not supported:%d"
+ "In UMSyncServer: entitlement OK, calling fetchPersonaBundleMapping with with asid:%d"
+ "In UMSyncServer: entitlement OK, calling resetPersonaBundleMapping with with asid:%d"
+ "In UMSyncServer: personaBundleIDMigrationCompleteWithReply FF not enabled"
+ "In UMSyncServer: personaBundleIDMigrationCompleteWithReply entitlement failure"
+ "In UMSyncServer: personaBundleIDMigrationStartWithReply entitlement failure"
+ "In UMSyncServer: setBundlesIdentifiers entitlement OK, but invalid bundleArray"
+ "In UMSyncServer: setBundlesIdentifiers entitlement failure:%d"
+ "In UMSyncServer: setBundlesIdentifiers, entitlement OK, but invalid profileInfo"
+ "In UMSyncServer:PersonaBundleIDMigration FF set, bundleIdentifiersForPersona not supported:%d"
+ "In UMSyncServer:PersonaBundleIDMigration FF set, setBundlesIdentifiers not supported:%d"
+ "In fetchPersonaBundleMapping"
+ "In resetPersonaBundleMapping"
+ "Mapping reset completed"
+ "Mapping reset failed with error:%d"
+ "PersonaBundleIDMigration"
+ "Reset bundleID Mapping for persona:%@"
+ "Reset bundleID mapping, Saving persona with removed bunbdleID Mapping"
+ "Reset persona BundleID Mapping completed successfully"
+ "Reset persona BundleID Mapping failed with error:%@"
+ "Returning persona bundleIDMapping for migration:%@"
+ "SupportsEDUMU"
+ "_aks_remote_peer_drop"
+ "_aks_remote_peer_get_state"
+ "aks_pki_token_get_info"
+ "aks_pki_token_list"
+ "aks_pki_token_op_register"
+ "aks_pki_token_op_set_password"
+ "aks_pki_token_op_unlock"
+ "aks_pki_token_op_verify"
+ "aks_pki_token_register_internal"
+ "aks_pki_token_request_challenge"
+ "aks_pki_token_unregister"
+ "com.apple.usermanagerd.persona.bundlemap.migration"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
+ "fetchPersonaBundleMapping:%@"
+ "personaBundleIDMigrationCompleteWithReply:"
+ "personaBundleIDMigrationStartWithReply:"
+ "personaUserProfileCreateWithUserODuuid:withUid:completionHandler:"
+ "personaUserProfileDeleteWithUserODuuid:withUid:completionHandler:"
+ "setValue:forKey:"
+ "v36@0:8@\"NSString\"16I24@?<v@?@\"NSError\">28"
+ "v36@0:8@16I24@?28"
- "4fT83+9coO3VAUnlxuOOcw"
- "AKSGetKeyBagStats"
- "AKSGetStashStats"
- "In UMSyncServer: entitlement OK, but invalid bundleArray"
- "PERSONA LOGOUT for USER:%@, UID:%d"
- "aks_fv_new_sibling_vek"
- "aks_remote_peer_drop"
- "aks_remote_peer_get_state"
- "aks_smartcard_register"
- "aks_smartcard_request_unlock"
- "aks_smartcard_unlock"
- "aks_smartcard_unregister"
- "aks_stash_escrow"
- "unLoading All persona Success"
- "unLoading All persona failed"

```
