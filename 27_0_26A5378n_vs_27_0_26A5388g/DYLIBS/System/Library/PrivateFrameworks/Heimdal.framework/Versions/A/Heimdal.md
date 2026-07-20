## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-725.0.8.0.0
+725.0.10.0.0
   __TEXT.__text: 0xacd6c
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xe80

   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x6e58
+  __DATA_CONST.__const: 0x6e88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__got: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   Functions: 2759
-  Symbols:   4530
+  Symbols:   4531
   CStrings:  2360
 
Symbols:
+ _asn1_KDC_PROXY_MESSAGE_tag__405
+ _asn1_KERB_ARMOR_SERVICE_REPLY_tag__452
+ _asn1_KERB_TGS_REQ_OUT_tag__438
+ _asn1_KERB_TGS_REQ_OUT_tag_t_440
+ _asn1_KRB5_SRP_PA_ANNOUNCE_tag__465
+ _asn1_KRB5_SRP_PA_ANNOUNCE_tag_groups_467
+ _asn1_KRB5_SRP_PA_INIT_tag__470
+ _asn1_KRB5_SRP_PA_tag__460
+ _asn1_Principal_seofTstruct_1
- _asn1_KDC_PROXY_MESSAGE_tag__404
- _asn1_KERB_ARMOR_SERVICE_REPLY_tag__451
- _asn1_KERB_TGS_REQ_OUT_tag__437
- _asn1_KERB_TGS_REQ_OUT_tag_t_439
- _asn1_KRB5_SRP_PA_ANNOUNCE_tag__464
- _asn1_KRB5_SRP_PA_ANNOUNCE_tag_groups_465
- _asn1_KRB5_SRP_PA_INIT_tag__468
- _asn1_KRB5_SRP_PA_tag__459
```
