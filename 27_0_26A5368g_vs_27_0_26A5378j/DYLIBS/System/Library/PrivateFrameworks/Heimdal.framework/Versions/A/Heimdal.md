## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal`

```diff

-  __TEXT.__text: 0xac060
+  __TEXT.__text: 0xacd6c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0xe78
-  __TEXT.__cstring: 0xfbb2
+  __TEXT.__const: 0xe80
+  __TEXT.__cstring: 0xfc5b
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xb30
+  __TEXT.__unwind_info: 0xb38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x22f0
   __AUTH_CONST.__cfstring: 0xc40
-  __AUTH_CONST.__auth_got: 0xcf8
-  __AUTH.__data: 0x90
-  __DATA.__data: 0x3420
+  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH.__data: 0x1680
+  __DATA.__data: 0x3438
   __DATA.__bss: 0x6e9
   __DATA.__common: 0x18
-  __DATA_DIRTY.__data: 0x1548
+  __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2752
-  Symbols:   4707
-  CStrings:  2451
+  Functions: 2759
+  Symbols:   4721
+  CStrings:  2457
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Symbols:
+ _CCDesIsWeakKey
+ _CCDesSetOddParity
+ _DES3_prf
+ _DES3_random_key
+ _DES3_string_to_key_derived
+ __krb5_DES3_random_to_key
+ __krb5_checksum_hmac_sha1_des3
+ __krb5_des3_salt_derived
+ __krb5_enctype_des3_cbc_none
+ __krb5_enctype_des3_cbc_sha1
+ __krb5_evp_encrypt
+ __krb5_xor
+ _keytype_des3_derived
+ _krb5_string_to_key_derived
CStrings:
+ "KRB-CRED tickets count (%lu) does not match ticket-info count (%lu)"
+ "des3"
+ "des3-cbc-none"
+ "des3-cbc-sha1"
+ "hmac-sha1-des3"
+ "prfsize not same ?:prfsize == crypto->et->prf_length"

```
