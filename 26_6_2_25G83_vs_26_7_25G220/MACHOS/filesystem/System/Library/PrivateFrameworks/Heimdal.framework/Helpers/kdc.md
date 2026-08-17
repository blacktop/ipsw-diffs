## kdc

> `System/Library/PrivateFrameworks/Heimdal.framework/Helpers/kdc`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-710.160.4.0.0
-  __TEXT.__text: 0x4d098
+710.160.4.701.2
+  __TEXT.__text: 0x4d218
   __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__const: 0x720
-  __TEXT.__cstring: 0x503e
+  __TEXT.__const: 0x728
+  __TEXT.__cstring: 0x5123
   __TEXT.__oslogstring: 0x15
   __TEXT.__unwind_info: 0x328
   __DATA_CONST.__auth_got: 0xe68
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3db0
+  __DATA_CONST.__const: 0x3dc0
   __DATA_CONST.__cfstring: 0x320
   __DATA.__data: 0x80c
   __DATA.__bss: 0x170

   - /usr/lib/libheimdal-asn1.dylib
   Functions: 759
   Symbols:   1849
-  CStrings:  800
+  CStrings:  805
 
Symbols:
+ _asn1_KDCFastCookie_tag__400
+ _asn1_KDCFastCookie_tag_realm_402
+ _asn1_KDCFastPAState_tag__391
+ _asn1_KDCFastPAState_tag_srp_392
+ _asn1_KDCFastState_tag__393
+ _asn1_KDCFastState_tag_expected_pa_types_398
+ _asn1_KDCFastState_tag_expiration_395
+ _asn1_KDCFastState_tag_flags_394
+ _asn1_KDCFastState_tag_pa_state_399
+ _asn1_KRB5_SRP_PA_ANNOUNCE_tag__465
+ _asn1_KRB5_SRP_PA_ANNOUNCE_tag_groups_467
+ _asn1_KRB5_SRP_PA_INIT_tag__470
+ _asn1_KRB5_SRP_PA_tag__460
+ _asn1_heim_utf8_string_tag_realm_403
- _asn1_KDCFastCookie_tag__399
- _asn1_KDCFastCookie_tag_realm_401
- _asn1_KDCFastPAState_tag__390
- _asn1_KDCFastPAState_tag_srp_391
- _asn1_KDCFastState_tag__392
- _asn1_KDCFastState_tag_expected_pa_types_396
- _asn1_KDCFastState_tag_expiration_394
- _asn1_KDCFastState_tag_flags_393
- _asn1_KDCFastState_tag_pa_state_398
- _asn1_KRB5_SRP_PA_ANNOUNCE_tag__464
- _asn1_KRB5_SRP_PA_ANNOUNCE_tag_groups_465
- _asn1_KRB5_SRP_PA_INIT_tag__468
- _asn1_KRB5_SRP_PA_tag__459
- _asn1_heim_utf8_string_tag_realm_402
Functions:
~ _pa_srp_validate : 3476 -> 3860
CStrings:
+ "(unbound)"
+ "(unknown)"
+ "SRP cookie principal mismatch: AS-REQ cname=%s cookie=%s"
+ "SRP requires a fetched client principal:r->client != NULL && r->client->entry.principal != NULL"
+ "have principal before expected:state->principal == NULL"
```
