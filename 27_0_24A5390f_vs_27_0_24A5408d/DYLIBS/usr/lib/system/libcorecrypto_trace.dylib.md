## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__fips_hmacs`
- `__TEXT.__eh_frame`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-2109.0.17.0.0
-  __TEXT.__text: 0x8d054
-  __TEXT.__cstring: 0x5a8b
-  __TEXT.__const: 0x20498
+2109.0.22.0.0
+  __TEXT.__text: 0x8c4a0
+  __TEXT.__cstring: 0x5bb3
+  __TEXT.__const: 0x204b8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1d60
+  __TEXT.__unwind_info: 0x1d30
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
-  Functions: 2645
-  Symbols:   2981
-  CStrings:  553
+  Functions: 2633
+  Symbols:   2971
+  CStrings:  558
 
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
