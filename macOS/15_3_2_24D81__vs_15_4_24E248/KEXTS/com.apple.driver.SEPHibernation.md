## com.apple.driver.SEPHibernation

> `com.apple.driver.SEPHibernation`

```diff

-842.60.8.0.0
+850.100.14.0.0
   __TEXT.__cstring: 0xa13
   __TEXT.__const: 0xc0
-  __TEXT_EXEC.__text: 0x21a4
+  __TEXT_EXEC.__text: 0x21c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc60
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 0861FB1A-EAB6-30A7-B82E-1B76590894CA
+  UUID: 5175CD61-E737-3BF4-87E4-D4A4B6289125
   Functions: 92
   Symbols:   430
   CStrings:  63
Functions:
~ __ZN10Hibernator4initEv : 28 -> 32
~ __ZN10Hibernator10hibernatorEP18HibernationService : 176 -> 196
~ __ZN18HibernationService14_setupEndpointEP21AppleSEPDeviceService : 716 -> 720
~ __ZN18HibernationService19_setPowerStateGatedEPm : 628 -> 636
~ __ZN18HibernationService24_prepareToHibernateGatedEP20sephib_wrapped_key_tP27sephib_seprom_hib_payload_t : 276 -> 272
~ __ZN18HibernationService20_startOperationGatedEv : 384 -> 388
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPHibernation/HibernationService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPHibernation/Hibernator.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPHibernation/HibernationService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSEPManager/SEPHibernation/Hibernator.cpp"

```
