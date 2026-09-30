## nfcd

> `/usr/libexec/nfcd`

```diff

-360.38.0.0.0
-  __TEXT.__text: 0x2798e0
+360.39.2.0.0
+  __TEXT.__text: 0x27a1cc
   __TEXT.__auth_stubs: 0x1840
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0x120c
-  __TEXT.__objc_stubs: 0xd460
+  __TEXT.__objc_stubs: 0xd440
   __TEXT.__objc_methlist: 0x9c98
-  __TEXT.__const: 0x1390
-  __TEXT.__objc_methname: 0x17d9d
-  __TEXT.__cstring: 0x2f6d2
+  __TEXT.__const: 0x13c0
+  __TEXT.__objc_methname: 0x17d8c
+  __TEXT.__cstring: 0x2f82e
   __TEXT.__objc_classname: 0x1d5f
   __TEXT.__objc_methtype: 0x567d
-  __TEXT.__oslogstring: 0x2699a
+  __TEXT.__oslogstring: 0x269e4
   __TEXT.__unwind_info: 0x2c50
   __DATA_CONST.__auth_got: 0xcc8
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x83e0
-  __DATA_CONST.__cfstring: 0x110a0
+  __DATA_CONST.__cfstring: 0x11160
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390

   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xfa0
   __DATA.__objc_const: 0x14920
-  __DATA.__objc_selrefs: 0x55d8
+  __DATA.__objc_selrefs: 0x55d0
   __DATA.__objc_ivar: 0x10ac
   __DATA.__objc_data: 0x3d90
   __DATA.__data: 0x2b94

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF6EF938-FFE2-3B7C-BD99-3EF346DAD331
+  UUID: 6A9C6D78-B8BC-3F32-8189-7E6D8B4A0711
   Functions: 4155
   Symbols:   592
-  CStrings:  14592
+  CStrings:  14605
 
Functions:
~ sub_100004fa8 : 764 -> 772
~ sub_100007034 -> sub_10000703c : 1464 -> 1796
~ sub_10006c8e0 -> sub_10006ca34 : 1496 -> 1512
~ sub_1000aab78 -> sub_1000aacdc : 996 -> 1328
~ sub_100104c1c -> sub_100104ecc : 6424 -> 6448
~ sub_100182fb8 -> sub_100183280 : 704 -> 1040
~ sub_100183278 -> sub_100183690 : 704 -> 1864
~ sub_100191228 -> sub_100191ac8 : 2484 -> 2532
~ sub_1001cc73c -> sub_1001cd00c : 1920 -> 1940
~ sub_1001d63dc -> sub_1001d6cc0 : 584 -> 592
CStrings:
+ "%c[%{public}s %{public}s]:%i Presentation service is not available"
+ "%c[%{public}s %{public}s]:%i [PaymentReader] Prompting for bundle %@"
+ "Assertion Failure"
+ "NFCD built from (B&I) Stockholm_Base-360.39.2"
+ "Presentation service is not available"
+ "[NFAssertPKWalletForegroundPresentment onAssert]"
+ "[NFAssertPKWalletForegroundPresentment onDeassert]"
+ "[NFAssertSuppressPresentmentIntentToDefaultApp onAssert]"
+ "[NFAssertSuppressPresentmentIntentToDefaultApp onDeassert]"
- "%c[%{public}s %{public}s]:%i [PaymentReader] Prompting for %@"
- "NFCD built from (B&I) Stockholm_Base-360.38"
- "localizedAppName"

```
