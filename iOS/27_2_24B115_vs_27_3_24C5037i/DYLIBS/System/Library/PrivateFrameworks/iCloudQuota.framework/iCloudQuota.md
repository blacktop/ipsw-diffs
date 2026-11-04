## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.24.1.5.0
-  __TEXT.__text: 0x794f8
-  __TEXT.__objc_methlist: 0x5a74
+301.24.2.4.2
+  __TEXT.__text: 0x7a79c
+  __TEXT.__objc_methlist: 0x5ad4
   __TEXT.__const: 0x1378
-  __TEXT.__cstring: 0x5080
-  __TEXT.__oslogstring: 0x8aa9
+  __TEXT.__cstring: 0x50d0
+  __TEXT.__oslogstring: 0x8c99
   __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__ustring: 0x4
+  __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x7f8
   __TEXT.__swift5_capture: 0x39c
   __TEXT.__swift5_reflstr: 0x2f1

   __TEXT.__swift_as_cont: 0xe0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x26b8
+  __TEXT.__unwind_info: 0x26d8
   __TEXT.__eh_frame: 0x1500
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e80
+  __DATA_CONST.__const: 0x1ea8
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30b8
+  __DATA_CONST.__objc_selrefs: 0x3118
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x730
   __DATA_CONST.__got: 0x820
-  __AUTH_CONST.__const: 0x1450
-  __AUTH_CONST.__cfstring: 0x66e0
+  __AUTH_CONST.__const: 0x1470
+  __AUTH_CONST.__cfstring: 0x6740
   __AUTH_CONST.__objc_const: 0xba10
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3053
-  Symbols:   4365
-  CStrings:  1652
+  Functions: 3062
+  Symbols:   4375
+  CStrings:  1661
 
Symbols:
+ +[_ICQDeviceInfo _canFillTemplate:words:]
+ +[_ICQDeviceInfo filledTemplate:itemCount:albumName:]
+ +[_ICQDeviceInfo filledTemplateForItemCount:albumName:lookup:]
+ +[_ICQDeviceInfo normalizedAlbumName:]
+ +[_ICQDeviceInfo wordsToReplaceForItemCount:albumName:]
+ +[_ICQHelperFunctions fillTemplate:words:]
+ -[ICQOffer exactMessageSpecificationForReason:bundleId:]
+ -[ICQOffer inAppAlertKeyForReason:placement:]
+ _ICQBannerSourceAppFeatureMessagingInfo
+ ___42+[_ICQHelperFunctions fillTemplate:words:]_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
- GCC_except_table35
CStrings:
+ "%$AlbumName"
+ "%{public}@ has no value, skipping the template"
+ "ICQBannerSourceAppFeatureMessagingInfo"
+ "No appFeatureMessagingInfo entry for reason: %{public}@, placement: %{public}@, bundleId: %{public}@ in offer %{public}@"
+ "albumName is empty or whitespace, treating as nil"
+ "appFeatureMessagingInfo entry for reason: %{public}@, placement: %{public}@ in offer %{public}@ has an alertKey of unexpected type %{public}@"
+ "appFeatureMessagingInfo entry for reason: %{public}@, placement: %{public}@ in offer %{public}@ has no SHOW_INLINE_ALERT link with an alertKey"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "\u2068%@\u2069"
```
