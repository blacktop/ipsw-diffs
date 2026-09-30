## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3056.0.20.0.2
-  __TEXT.__text: 0xbdd4
+3056.0.25.0.5
+  __TEXT.__text: 0xbe30
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x2b4
   __TEXT.__const: 0x40c
-  __TEXT.__gcc_except_tab: 0xea4
+  __TEXT.__gcc_except_tab: 0xea8
   __TEXT.__cstring: 0x129f
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xecd
   __TEXT.__objc_methtype: 0x50c
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x408
   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x3c0

   __DATA.__objc_selrefs: 0x400
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA.__data: 0x9d0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: F135BC14-0123-3A3F-B5A2-B4A847A6698C
+  UUID: D899C932-C80C-390F-BA70-5E93AF84DE81
   Functions: 182
   Symbols:   225
   CStrings:  463
Functions:
~ __ZN18CLFamiliarRoadData19addToFamiliarityMapERKyS1_S1_d : 200 -> 292
~ __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__13mapI12CLMapRoadKeyNS0_10shared_ptrI9CLMapRoadEENS0_4lessIS2_EENS0_9allocatorINS0_4pairIKS2_S5_EEEEEE -> __ZN18CLFamiliarRoadData21getFamiliarityDataForE12CLMapRoadKeyRKy : 208 -> 200
~ __ZN18CLFamiliarRoadData38isFamiliarRoadDataAvailableForThisRoadERK12CLMapRoadKey -> __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__13mapI12CLMapRoadKeyNS0_10shared_ptrI9CLMapRoadEENS0_4lessIS2_EENS0_9allocatorINS0_4pairIKS2_S5_EEEEEE : 140 -> 208
~ __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__16vectorINS0_10shared_ptrI9CLMapRoadEENS0_9allocatorIS4_EEEE -> __ZN18CLFamiliarRoadData38isFamiliarRoadDataAvailableForThisRoadERK12CLMapRoadKey : 172 -> 140
~ __ZN18CLFamiliarRoadData36trimNeighborsBasedOnFamiliarityIndexENSt3__110shared_ptrI9CLMapRoadEERNS0_6vectorIS3_NS0_9allocatorIS3_EEEE -> __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__16vectorINS0_10shared_ptrI9CLMapRoadEENS0_9allocatorIS4_EEEE : 556 -> 172
~ __ZN18CLFamiliarRoadData30getFamiliarRoadDataForThisRoadERK12CLMapRoadKeyRNSt3__16vectorINS3_10shared_ptrI17CLFamiliarityDataEENS3_9allocatorIS7_EEEE -> __ZN18CLFamiliarRoadData36trimNeighborsBasedOnFamiliarityIndexENSt3__110shared_ptrI9CLMapRoadEERNS0_6vectorIS3_NS0_9allocatorIS3_EEEE : 176 -> 556
~ __ZN18CLFamiliarRoadData21getFamiliarityDataForE12CLMapRoadKeyRKy -> __ZN18CLFamiliarRoadData30getFamiliarRoadDataForThisRoadERK12CLMapRoadKeyRNSt3__16vectorINS3_10shared_ptrI17CLFamiliarityDataEENS3_9allocatorIS7_EEEE : 200 -> 176

```
