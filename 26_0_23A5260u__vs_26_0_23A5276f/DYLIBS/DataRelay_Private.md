## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-30.45.3.0.0
-  __TEXT.__text: 0xc204
-  __TEXT.__auth_stubs: 0x370
+30.48.2.1.2
+  __TEXT.__text: 0xc38c
+  __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x998
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x578
-  __TEXT.__cstring: 0x20a9
+  __TEXT.__gcc_except_tab: 0x58c
+  __TEXT.__cstring: 0x21c5
   __TEXT.__unwind_info: 0x420
   __TEXT.__objc_classname: 0xa5
   __TEXT.__objc_methname: 0x1b9f

   __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0xf78

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE6EF5AA-F97C-361A-94BE-C76FDDDB8A71
-  Functions: 339
-  Symbols:   1163
-  CStrings:  694
+  UUID: 99B0AA32-6C4C-32D0-B63D-21CBAB98DF75
+  Functions: 341
+  Symbols:   1169
+  CStrings:  699
 
Symbols:
+ -[DRClient routedWxDeviceChanged:].cold.1
+ -[DRHIDClient routedWxDeviceChanged:].cold.4
+ _dispatch_after
+ _dispatch_time
Functions:
~ -[DRClient routedWxDeviceChanged:] : 348 -> 404
~ ___48-[DRServer removeRequestedDataTypes:completion:]_block_invoke_2 : 212 -> 260
~ ___48-[DRServer removeRequestedDataTypes:completion:]_block_invoke_3 : 104 -> 64
~ -[DRHIDClient activate] : 1112 -> 1128
~ -[DRHIDClient routedWxDeviceChanged:] : 632 -> 688
~ -[DRPeer deviceFound:completion:] : 1040 -> 1168
+ -[DRClient routedWxDeviceChanged:].cold.1
~ -[DRHIDClient routedWxDeviceChanged:].cold.1 : 140 -> 64
~ -[DRHIDClient routedWxDeviceChanged:].cold.2 : 108 -> 140
+ -[DRHIDClient routedWxDeviceChanged:].cold.4
CStrings:
+ "-[DRClient routedWxDeviceChanged:]"
+ "DRClient: routedWxDeviceChanged, wxRoute=%@"
+ "DRHIDClient: routedWxDeviceChanged, wxRoute=%@"
+ "discoveryClient: desired device found, identifier: %@"
+ "discoveryClient: other device found, identifier: %@"
+ "not publishing serviceID %@ due to routing state: addr=%@, wxRoute=%@"
+ "publishing serviceID %@ due to routing state: addr=%@, wxRoute=%@"
- "discoveryClient: device found"
- "publishing serviceID %@ due to routing state: addr=%@"

```
