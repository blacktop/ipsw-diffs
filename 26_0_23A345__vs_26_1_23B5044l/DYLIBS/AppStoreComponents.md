## AppStoreComponents

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`

```diff

-8.0.36.0.0
-  __TEXT.__text: 0x8c070
+8.1.3.0.0
+  __TEXT.__text: 0x8c4b4
   __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_methlist: 0x8434
+  __TEXT.__objc_methlist: 0x846c
   __TEXT.__const: 0x1eb4
   __TEXT.__gcc_except_tab: 0x99c
-  __TEXT.__cstring: 0x3bc2
+  __TEXT.__cstring: 0x3c32
   __TEXT.__dlopen_cstrs: 0x14f
   __TEXT.__oslogstring: 0x2fdd
   __TEXT.__constg_swiftt: 0x700

   __TEXT.__swift5_protos: 0xc
   __TEXT.__unwind_info: 0x2530
   __TEXT.__objc_classname: 0x110d
-  __TEXT.__objc_methname: 0x11a22
-  __TEXT.__objc_methtype: 0x32fd
-  __TEXT.__objc_stubs: 0xc680
+  __TEXT.__objc_methname: 0x11adc
+  __TEXT.__objc_methtype: 0x3300
+  __TEXT.__objc_stubs: 0xc6e0
   __DATA_CONST.__got: 0x830
   __DATA_CONST.__const: 0x1880
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_selrefs: 0x3bf8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0xc68
   __AUTH_CONST.__const: 0x1d90
-  __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0xe9e8
+  __AUTH_CONST.__cfstring: 0x48e0
+  __AUTH_CONST.__objc_const: 0xea48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x560
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x7e0
+  __DATA.__objc_ivar: 0x7e8
   __DATA.__data: 0x1be8
   __DATA.__bss: 0x1b10
   __DATA.__common: 0x160

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BD32BB52-66CD-38A4-9263-988E6BA8CAF7
-  Functions: 3610
-  Symbols:   10594
-  CStrings:  4925
+  UUID: 042B59E3-9CBE-340A-87EA-8B1F8E1B06E7
+  Functions: 3614
+  Symbols:   10607
+  CStrings:  4935
 
Symbols:
+ -[ASCLockupBatchRequest _initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:]
+ -[ASCLockupBatchRequest countryCodeOverride]
+ -[ASCLockupRequest _lockupRequestWithCountryCodeOverride:]
+ -[ASCLockupRequest countryCodeOverride]
+ -[ASCLockupRequest(AppDistributionInstall) lockupRequestWithCountryCodeOverride:]
+ _OBJC_IVAR_$_ASCLockupBatchRequest._countryCodeOverride
+ _OBJC_IVAR_$_ASCLockupRequest._countryCodeOverride
+ ___block_descriptor_73_e8_32s40s48s56s64s_e38_v32?0"ASCPair"8"NSMutableSet"16^B24ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:
+ _objc_msgSend$_lockupRequestWithCountryCodeOverride:
+ _objc_msgSend$countryCodeOverride
+ _objc_msgSend$screen
- -[ASCLockupBatchRequest _initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:]
- ___block_descriptor_65_e8_32s40s48s56s_e38_v32?0"ASCPair"8"NSMutableSet"16^B24ls32l8s40l8s48l8s56l8
- _objc_msgSend$_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:
CStrings:
+ "@76@0:8@16@24@32@40B48@52@60@68"
+ "Requests with different countryCodeOverride options cannot be included in batch request: %@ != %@"
+ "T@\"NSString\",R,C,N,V_countryCodeOverride"
+ "_countryCodeOverride"
+ "_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:countryCodeOverride:"
+ "_lockupRequestWithCountryCodeOverride:"
+ "countryCodeOverride"
+ "lockupRequestWithCountryCodeOverride:"
+ "screen"
- "@68@0:8@16@24@32@40B48@52@60"
- "_initWithIDs:kind:context:clientID:enableAppDistribution:mediaQueryParams:platformOverride:"

```
