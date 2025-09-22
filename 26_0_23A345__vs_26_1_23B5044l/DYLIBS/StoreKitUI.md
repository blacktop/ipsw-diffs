## StoreKitUI

> `/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI`

```diff

-815.0.48.0.0
-  __TEXT.__text: 0x356eac
-  __TEXT.__auth_stubs: 0x24b0
-  __TEXT.__objc_methlist: 0x33974
+815.1.6.0.0
+  __TEXT.__text: 0x357390
+  __TEXT.__auth_stubs: 0x24a0
+  __TEXT.__objc_methlist: 0x3399c
   __TEXT.__const: 0x23e4
   __TEXT.__gcc_except_tab: 0x5ff8
-  __TEXT.__cstring: 0x2e5ba
-  __TEXT.__oslogstring: 0xaf1
+  __TEXT.__cstring: 0x2e5da
+  __TEXT.__oslogstring: 0xc01
   __TEXT.__dlopen_cstrs: 0x26d
   __TEXT.__ustring: 0x62
   __TEXT.__constg_swiftt: 0x4b4

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xcf08
+  __TEXT.__unwind_info: 0xcf10
   __TEXT.__eh_frame: 0x358
   __TEXT.__objc_classname: 0x8e49
-  __TEXT.__objc_methname: 0x5d6d8
+  __TEXT.__objc_methname: 0x5d7e0
   __TEXT.__objc_methtype: 0x10773
-  __TEXT.__objc_stubs: 0x40a20
-  __DATA_CONST.__got: 0x1f10
-  __DATA_CONST.__const: 0x9098
+  __TEXT.__objc_stubs: 0x40ac0
+  __DATA_CONST.__got: 0x1f20
+  __DATA_CONST.__const: 0x90e8
   __DATA_CONST.__objc_classlist: 0x1f60
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x870
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13c38
+  __DATA_CONST.__objc_selrefs: 0x13c68
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x19c8
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x1270
+  __AUTH_CONST.__auth_got: 0x1268
   __AUTH_CONST.__const: 0x1b18
-  __AUTH_CONST.__cfstring: 0x151a0
-  __AUTH_CONST.__objc_const: 0xbdae0
+  __AUTH_CONST.__cfstring: 0x151e0
+  __AUTH_CONST.__objc_const: 0xbdb40
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x112d0
   __AUTH.__data: 0x418
-  __DATA.__objc_ivar: 0x49fc
+  __DATA.__objc_ivar: 0x4a04
   __DATA.__data: 0x6df8
   __DATA.__bss: 0x1148
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C1851BA2-B976-3ACD-8610-A84A23C6212D
-  Functions: 20351
-  Symbols:   68036
-  CStrings:  26116
+  UUID: 285E3BD0-8A36-316F-B1AB-927997CDB459
+  Functions: 20356
+  Symbols:   68057
+  CStrings:  26135
 
Symbols:
+ -[SKUIReviewConfiguration storeExternalVersionID]
+ -[SKUIReviewInAppConfiguration setStoreExternalVersionID:]
+ -[SKUIReviewInAppConfiguration storeExternalVersionID]
+ _OBJC_CLASS_$_AMSURLRequestEncoder
+ _OBJC_CLASS_$_AMSURLSession
+ _OBJC_IVAR_$_SKUIReviewConfiguration._storeExternalVersionID
+ _OBJC_IVAR_$_SKUIReviewInAppConfiguration._storeExternalVersionID
+ ___30-[SKUIPostRatingOperation run]_block_invoke
+ ___30-[SKUIPostRatingOperation run]_block_invoke.27
+ ___54-[SKUIReviewInAppController _submitRating:completion:]_block_invoke.34
+ ___block_descriptor_40_e8_32s_e34_v24?0"AMSURLResult"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e35_v24?0"AMSURLRequest"8"NSError"16ls32l8
+ _objc_msgSend$dataTaskPromiseWithRequest:
+ _objc_msgSend$defaultSession
+ _objc_msgSend$requestByEncodingRequest:parameters:
+ _objc_msgSend$requestWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$setRequestEncoding:
+ _objc_msgSend$storeExternalVersionID
- ___54-[SKUIReviewInAppController _submitRating:completion:]_block_invoke.31
- _objc_msgSend$setShouldProcessDialogsOutsideDaemon:
CStrings:
+ "Error fetching review URLs: "
+ "T@\"NSString\",C,N,V_storeExternalVersionID"
+ "T@\"NSString\",R,N,V_storeExternalVersionID"
+ "[SKUIPostRatingOperation] Error encoding request: %{public}@"
+ "[SKUIPostRatingOperation] Error receiving response: %{public}@"
+ "[SKUIPostRatingOperation] Failed to get app's storeExternalVersionID"
+ "[SKUIPostRatingOperation] Failed to get save-user-review key from bag"
+ "_storeExternalVersionID"
+ "appstored"
+ "dataTaskPromiseWithRequest:"
+ "defaultSession"
+ "https://userpub.itunes.apple.com/api/v1/saveUserReview?id=%@"
+ "requestByEncodingRequest:parameters:"
+ "requestWithURL:cachePolicy:timeoutInterval:"
+ "save-user-review"
+ "setRequestEncoding:"
+ "setStoreExternalVersionID:"
+ "storeExternalVersionID"
+ "v24@?0@\"AMSURLRequest\"8@\"NSError\"16"
+ "v24@?0@\"AMSURLResult\"8@\"NSError\"16"
- "Error fetching reivew URLs: "
- "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/userRateContent?displayable-kind=11&id=%@"
- "p2-application-user-rate-content"
- "setShouldProcessDialogsOutsideDaemon:"

```
