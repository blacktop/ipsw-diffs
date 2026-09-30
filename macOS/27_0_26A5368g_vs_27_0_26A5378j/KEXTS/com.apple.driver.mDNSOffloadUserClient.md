## com.apple.driver.mDNSOffloadUserClient

> `com.apple.driver.mDNSOffloadUserClient`

```diff

   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x123a
-  __TEXT_EXEC.__text: 0x3800
+  __TEXT_EXEC.__text: 0x37bc
   __TEXT_EXEC.__auth_stubs: 0x2b0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN11mDNSHandoff21getInfoFromInterfacesEP7__ifnet : 680 -> 660
~ __ZN11mDNSHandoff19getIpV4_AddressInfoEPP8__ifaddrbP7__ifneti : 332 -> 324
~ __ZN11mDNSHandoff19getIpV6_AddressInfoEPP8__ifaddrbP7__ifneti : 392 -> 372
~ __ZL10my_strnstrPcPKcm : 152 -> 132

```
