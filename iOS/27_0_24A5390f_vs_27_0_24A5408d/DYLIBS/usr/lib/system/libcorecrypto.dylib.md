## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-2109.0.17.0.0
-  __TEXT.__text: 0x8c894
-  __TEXT.__cstring: 0x5818
-  __TEXT.__const: 0x20488
+2109.0.22.0.0
+  __TEXT.__text: 0x8bcf0
+  __TEXT.__cstring: 0x5940
+  __TEXT.__const: 0x204a8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__unwind_info: 0x1cc0
   __TEXT.__eh_frame: 0x3a0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x1ec8
+  __DATA_CONST.__const: 0x2108
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x23b8
   __AUTH_CONST.__auth_got: 0x118

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2640
-  Symbols:   2968
-  CStrings:  529
+  Functions: 2628
+  Symbols:   2958
+  CStrings:  534
 
Symbols:
+ _rej_rnd_kat
- _ccapsic_client_check_intersect_response
- _ccapsic_client_check_intersect_response_ws
- _ccapsic_client_generate_match_response
- _ccapsic_client_init
- _ccapsic_client_init_internal
- _ccapsic_client_state_sizeof
- _ccapsic_server_determine_intersection
- _ccapsic_server_encode_element
- _ccapsic_server_encode_element_ws
- _ccapsic_server_init
- _ccapsic_server_state_sizeof
CStrings:
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n"
+ "FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n"
+ "fipspost_post_mldsa_sign_rejection_kat"
```
