## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-925.0.4.0.0
-  __TEXT.__text: 0x1670c
+925.0.12.0.0
+  __TEXT.__text: 0x17f80
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x35bc
-  __TEXT.__oslogstring: 0x17fa
-  __TEXT.__const: 0x398
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__cstring: 0x38db
+  __TEXT.__oslogstring: 0x1942
+  __TEXT.__const: 0x3a8
+  __TEXT.__unwind_info: 0x940
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1948
+  __DATA_CONST.__const: 0x1a38
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__const: 0x348
+  __AUTH_CONST.__cfstring: 0x17e0
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 619
-  Symbols:   978
-  CStrings:  634
+  Functions: 652
+  Symbols:   1010
+  CStrings:  665
 
Symbols:
+ ____tcc_indirect_auth_cache_max_size_block_invoke
+ ____tcc_server_send_get_fine_grained_status_block_invoke
+ ____tcc_server_send_get_fine_grained_status_block_invoke_2
+ ___tcc_authorization_get_fine_grained_status_block_invoke
+ __tcc_indirect_auth_cache_entry_release
+ __tcc_indirect_auth_cache_max_size.large_max_size
+ __tcc_indirect_auth_cache_max_size.once
+ __tcc_indirect_auth_cache_service_release
+ __xpc_type_bool
+ _kTCCIndirectAuthCacheEntryValueCallBacks
+ _kTCCIndirectAuthCacheServiceValueCallBacks
+ _sysctlbyname
+ _tcc_authorization_cache_indirect_auth_clear
+ _tcc_authorization_cache_indirect_auth_copy
+ _tcc_authorization_cache_indirect_auth_get_generation
+ _tcc_authorization_cache_indirect_auth_set
+ _tcc_authorization_get_fine_grained_status
+ _tcc_credential_get_audit_token
+ _tcc_indirect_object_create_with_target_app_audit_token
+ _tcc_indirect_object_create_with_target_app_bundle_identifier
+ _tcc_indirect_object_get_indirect_object_bundle_path
+ _tcc_indirect_object_get_indirect_object_identity_type
+ _tcc_indirect_object_get_target_app_attribution_method
+ _tcc_indirect_object_get_target_app_audit_token
+ _tcc_indirect_object_set_indirect_object_bundle_path
+ _tcc_indirect_object_set_indirect_object_identity_type
+ _tcc_indirect_object_set_target_app_attribution_method
+ _tcc_server_message_get_fine_grained_status
+ _tcc_service_get_indirect_auth_cache_max_size
+ _xpc_bool_get_value
+ _xpc_copy_entitlement_for_self
+ _xpc_dictionary_get_dictionary
CStrings:
+ "%s: CFDataCreate failed"
+ "%s: calloc failed"
+ "%{public}s(%{public}s) fails: %{public}@"
+ "(audit token)"
+ "Allowed For Session Time"
+ "GET: (%{public}s, subject pid %d, target pid %d) -> %{public}s"
+ "REMOVE: least recently used entry of %{public}s"
+ "SET: (%{public}s, subject pid %d, target pid %d)"
+ "SET: dropped for %{public}s, generation moved"
+ "TCCAccessGetFineGrainedStatus"
+ "TCCD_MSG_HAS_FINE_GRAINED_RECORD_KEY"
+ "TCCD_MSG_HAS_MAIN_RECORD_KEY"
+ "TCCD_MSG_HAS_RECORD_WITH_RIGHT_KEY"
+ "TCCD_MSG_QUERY_AUTHORIZATION_RIGHT_KEY"
+ "_tcc_authorization_cache_locked_indirect_auth_set"
+ "_tcc_server_send_get_fine_grained_status_block_invoke_2"
+ "authorization_indirect_object"
+ "com.apple.private.tcc.large-indirect-auth-cache"
+ "hit"
+ "indirect_object_audit_token"
+ "indirect_object_bundle_path"
+ "indirect_object_target_app_attribution_method"
+ "kern.maxproc"
+ "miss"
+ "tcc_authorization_cache_indirect_auth_copy"
+ "tcc_authorization_cache_indirect_auth_set"
+ "tcc_authorization_get_fine_grained_status_block_invoke"
+ "tcc_send_get_fine_grained_status() IPC"
+ "tccd could not answer the request"
+ "tccd did not say which subject it evaluated"
+ "v48@?0{?=BBBQ^{tcc_service_s}^{tcc_identity_s}}8^{__CFError=}40"
```
