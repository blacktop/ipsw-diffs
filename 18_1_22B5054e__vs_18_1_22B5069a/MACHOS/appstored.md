## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-11.1.14.0.0
-  __TEXT.__text: 0x410228
-  __TEXT.__auth_stubs: 0x3c40
-  __TEXT.__objc_stubs: 0x127e0
-  __TEXT.__objc_methlist: 0xb2f4
-  __TEXT.__cstring: 0x21348
-  __TEXT.__objc_methname: 0x1ad14
-  __TEXT.__const: 0x19a18
-  __TEXT.__constg_swiftt: 0x21f4
-  __TEXT.__swift5_typeref: 0x20ca
-  __TEXT.__swift5_fieldmd: 0x1fe8
+11.1.17.2.1
+  __TEXT.__text: 0x4136e8
+  __TEXT.__auth_stubs: 0x3c50
+  __TEXT.__objc_stubs: 0x12820
+  __TEXT.__objc_methlist: 0xb354
+  __TEXT.__cstring: 0x21489
+  __TEXT.__objc_methname: 0x1adb5
+  __TEXT.__const: 0x19d48
+  __TEXT.__constg_swiftt: 0x22a0
+  __TEXT.__swift5_typeref: 0x2154
+  __TEXT.__swift5_fieldmd: 0x20e0
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x165d
-  __TEXT.__swift5_assocty: 0x390
-  __TEXT.__swift5_proto: 0x344
-  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift5_reflstr: 0x16dd
+  __TEXT.__swift5_assocty: 0x3c0
+  __TEXT.__swift5_proto: 0x37c
+  __TEXT.__swift5_types: 0x230
   __TEXT.__objc_classname: 0x42a4
   __TEXT.__objc_methtype: 0x78c7
-  __TEXT.__swift5_capture: 0x1594
+  __TEXT.__swift5_capture: 0x15b0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__oslogstring: 0x36b55
+  __TEXT.__oslogstring: 0x36cd7
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__gcc_except_tab: 0xab08
+  __TEXT.__gcc_except_tab: 0xaa9c
   __TEXT.__dlopen_cstrs: 0x4b8
-  __TEXT.__unwind_info: 0x9d08
-  __TEXT.__eh_frame: 0x75c4
-  __DATA_CONST.__auth_got: 0x1e30
-  __DATA_CONST.__got: 0x16d8
-  __DATA_CONST.__auth_ptr: 0x7f8
-  __DATA_CONST.__const: 0x1d0d0
-  __DATA_CONST.__cfstring: 0x1ae00
-  __DATA_CONST.__objc_classlist: 0x1628
+  __TEXT.__unwind_info: 0x9e48
+  __TEXT.__eh_frame: 0x776c
+  __DATA_CONST.__auth_got: 0x1e38
+  __DATA_CONST.__got: 0x16e8
+  __DATA_CONST.__auth_ptr: 0x818
+  __DATA_CONST.__const: 0x1d400
+  __DATA_CONST.__cfstring: 0x1ae20
+  __DATA_CONST.__objc_classlist: 0x1630
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x518
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x498
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x3aa58
-  __DATA.__objc_selrefs: 0x5ce8
-  __DATA.__objc_ivar: 0x24e0
-  __DATA.__objc_data: 0x10020
-  __DATA.__data: 0x6aa8
-  __DATA.__bss: 0x70a8
-  __DATA.__common: 0xb6c
+  __DATA.__objc_const: 0x3ab28
+  __DATA.__objc_selrefs: 0x5d00
+  __DATA.__objc_ivar: 0x24e4
+  __DATA.__objc_data: 0x100e8
+  __DATA.__data: 0x6b78
+  __DATA.__bss: 0x77a8
+  __DATA.__common: 0xb74
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11822
-  Symbols:   1903
-  CStrings:  14863
+  Functions: 11921
+  Symbols:   1906
+  CStrings:  14883
 
Symbols:
+ _$s2os6LoggerV14AppStoreDaemonE8storeKitACvgZ
+ _$sSdN
+ _OBJC_CLASS_$_ASDStoreKitService
CStrings:
+ "/\x0f\x03\x17"
+ "03:14:29"
+ "APPSTORE_ENGAGEMENT"
+ "Failed to encode ExternalPurchaseTokenV2Family for %!s(MISSING): %!@(MISSING)"
+ "Failed to extract token family information from %!s(MISSING) buy response"
+ "Failed to hand off new token family for %!s(MISSING)"
+ "Handing off external purchase token family info for %!s(MISSING)"
+ "Sep 30 2024"
+ "T@\"_TtC9appstored23StoreKitExternalGateway\",N,R"
+ "[%!@(MISSING)] Authentication is required to perform authorization"
+ "[%!@(MISSING)] Authentication not required to perform authorization"
+ "[FP/%!{(MISSING)public}@] Will not attempt fairplay recovery do to launchable fairplayStatus: %!d(MISSING)"
+ "_TtC9appstored23StoreKitExternalGateway"
+ "_externalPurchaseLinkOutTokenInfo"
+ "cacheExpirationDate"
+ "client"
+ "externalPurchaseLinkOutTokenInfo"
+ "externalPurchaseToken"
+ "handleExternalPurchaseTokenInfoDictionary:bundleID:"
+ "handleNewTokenFamily:bundleID:withReply:"
+ "hasActiveToken"
+ "initWithItemIDs:additionalBuyParams:client:logKey:"
+ "initWithItemMetadata:additionalBuyParams:client:logKey:"
+ "setSendBlindedData:"
+ "tokenEntries"
+ "tokenFamilyId"
+ "tokenType"
- "/\x0f\x03\x16"
- "17:39:05"
- "Sep 17 2024"
- "[%!@(MISSING)] Performing authorization for accountID: %!{(MISSING)public}@"
- "initWithItemIDs:additionalBuyParams:logKey:"
- "initWithItemMetadata:additionalBuyParams:logKey:"
- "metricsData"

```
