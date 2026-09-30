## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.1.8.0
-  __TEXT.__text: 0x780f0
+301.23.2.1.0
+  __TEXT.__text: 0x784e4
   __TEXT.__auth_stubs: 0x1680
-  __TEXT.__objc_methlist: 0x57f4
-  __TEXT.__const: 0x1268
-  __TEXT.__cstring: 0x6541
-  __TEXT.__oslogstring: 0x7f69
+  __TEXT.__objc_methlist: 0x580c
+  __TEXT.__const: 0x1288
+  __TEXT.__cstring: 0x6771
+  __TEXT.__oslogstring: 0x8029
   __TEXT.__gcc_except_tab: 0x6b8
   __TEXT.__dlopen_cstrs: 0x2f1
-  __TEXT.__ustring: 0x136
+  __TEXT.__ustring: 0x152
   __TEXT.__swift5_typeref: 0x712
-  __TEXT.__swift5_capture: 0x2e0
+  __TEXT.__swift5_capture: 0x2f8
   __TEXT.__swift5_reflstr: 0x2c1
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__constg_swiftt: 0x6b0

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1cc0
-  __TEXT.__eh_frame: 0x11a8
-  __TEXT.__objc_classname: 0xa70
-  __TEXT.__objc_methname: 0xd521
-  __TEXT.__objc_methtype: 0xfe5
-  __TEXT.__objc_stubs: 0x8f80
+  __TEXT.__unwind_info: 0x1cd0
+  __TEXT.__eh_frame: 0x11d8
+  __TEXT.__objc_classname: 0xa79
+  __TEXT.__objc_methname: 0xd560
+  __TEXT.__objc_methtype: 0xfd7
+  __TEXT.__objc_stubs: 0x8fc0
   __DATA_CONST.__got: 0x7e8
   __DATA_CONST.__const: 0x1d00
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f28
+  __DATA_CONST.__objc_selrefs: 0x2f40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_arraydata: 0x20b0
+  __DATA_CONST.__objc_arraydata: 0x2328
   __AUTH_CONST.__auth_got: 0xb50
-  __AUTH_CONST.__const: 0x13a0
-  __AUTH_CONST.__cfstring: 0x7240
+  __AUTH_CONST.__const: 0x13c8
+  __AUTH_CONST.__cfstring: 0x7360
   __AUTH_CONST.__objc_const: 0xb010
-  __AUTH_CONST.__objc_intobj: 0xae0
-  __AUTH_CONST.__objc_dictobj: 0x1478
-  __AUTH_CONST.__objc_arrayobj: 0x528
+  __AUTH_CONST.__objc_intobj: 0xaf8
+  __AUTH_CONST.__objc_dictobj: 0x15e0
+  __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH.__objc_data: 0x14b0
   __AUTH.__data: 0x460
   __DATA.__objc_ivar: 0x680

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9A9F51F5-22F2-3E57-B1EB-47EDFCB5DA01
-  Functions: 2888
-  Symbols:   8034
-  CStrings:  5153
+  UUID: 69D075DA-D5B7-3E44-8248-863C6FC92D3E
+  Functions: 2895
+  Symbols:   8044
+  CStrings:  5176
 
Symbols:
+ +[ICQDaemonOfferConditions getLibrarySizesFromDB:]
+ +[ICQDaemonOfferConditions getLibrarySizesFromDB:].cold.1
+ +[ICQDaemonOfferConditions getLibrarySizesFromDB:].cold.2
+ +[ICQDaemonOfferConditions systemPhotoLibrary]
+ +[ICQOffer(Examples) debugPhotosOptimizeBannerOffer]
+ GCC_except_table18
+ __OBJC_$_CLASS_METHODS_ICQOffer(ICQDebugging|Internal|Examples)
+ __OBJC_$_INSTANCE_METHODS_ICQOffer(ICQDebugging|Internal|Examples)
+ _objc_msgSend$getLibrarySizesFromDB:
+ _objc_msgSend$isMultiLibraryModeEnabled
+ _objc_msgSend$systemPhotoLibrary
- +[ICQDaemonOfferConditions getLibrarySizesFromDB:photoLibrary:]
- +[ICQDaemonOfferConditions getLibrarySizesFromDB:photoLibrary:].cold.1
- GCC_except_table17
- __OBJC_$_CLASS_METHODS_ICQOffer(ICQDebugging|Internal)
- __OBJC_$_INSTANCE_METHODS_ICQOffer(ICQDebugging|Internal)
- _objc_msgSend$getLibrarySizesFromDB:photoLibrary:
CStrings:
+ "DEBUG_PHOTOS_OPTIMIZE_BANNER"
+ "Examples"
+ "ICQDaemonOfferConditions: Multi library mode detected, using system photo library"
+ "ICQDaemonOfferConditions: Using shared photo library"
+ "O"
+ "You do not have enough space to take more photos. Free up %$PhotoLibraryUploadSize of space on this iPhone by keeping your original photos in iCloud and smaller versions on this iPhone."
+ "You do not have enough space to take more photos. Free up space on this iPhone by keeping your original photos in iCloud and smaller versions on this iPhone."
+ "debug-account"
+ "debug-notification-banner"
+ "debugPhotosOptimizeBannerOffer"
+ "getLibrarySizesFromDB:"
+ "getLibrarySizesFromDB: photo libary usage is not available."
+ "iPhone storage is almost full. You can free up space by turning on Optimize iPhone Storage. %@"
+ "inlineAlertInfoCancelBtnId"
+ "inlineAlertInfoOkBtnId"
+ "isMultiLibraryModeEnabled"
+ "systemPhotoLibrary"
- "@28@0:8B16@20"
- "getLibrarySizesFromDB:photoLibrary:"

```
