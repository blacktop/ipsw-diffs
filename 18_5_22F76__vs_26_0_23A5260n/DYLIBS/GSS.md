## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-693.100.10.0.0
-  __TEXT.__text: 0x27f38
+710.0.0.0.0
+  __TEXT.__text: 0x27efc
   __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__const: 0x44a
+  __TEXT.__const: 0x43a
   __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x728

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: C9E9310A-B3AA-3230-99F8-D7971673EBD4
-  Functions: 673
-  Symbols:   2163
+  UUID: B1FA204C-1F2B-3409-AB56-32536BC6C4D7
+  Functions: 671
+  Symbols:   2159
   CStrings:  660
 
Symbols:
- _free_key
- _get_int32
Functions:
~ __gssapi_wrap_cfx_iov : 1492 -> 1488
~ __gsskrb5_set_sec_context_option : 836 -> 832
- _get_int32
~ _gss_krb5_free_lucid_sec_context : 144 -> 204
- _free_key
~ __gss_mg_copy_debug_cred : 288 -> 292

```
