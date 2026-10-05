## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1696.2.5.0.0
-  __TEXT.__text: 0xfdcc
+1696.2.8.1.0
+  __TEXT.__text: 0xffb0
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x2f60
+  __TEXT.__objc_stubs: 0x2fa0
   __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__objc_methname: 0x4844
+  __TEXT.__objc_methname: 0x4887
   __TEXT.__cstring: 0x751
   __TEXT.__oslogstring: 0x53e
   __TEXT.__objc_classname: 0x150

   __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0x938
   __DATA.__objc_const: 0xb70
-  __DATA.__objc_selrefs: 0xfe8
+  __DATA.__objc_selrefs: 0xff8
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3c8

   - /usr/lib/libobjc.A.dylib
   Functions: 197
   Symbols:   405
-  CStrings:  789
+  CStrings:  791
 
Functions:
~ sub_100003468 : 14580 -> 14632
~ sub_1000078d0 -> sub_100007904 : 14872 -> 15304
CStrings:
+ "isNewToWalletUser"
+ "numberWithBool:"
+ "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:"
- "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:"
```
