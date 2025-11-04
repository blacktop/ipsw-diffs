## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.1.7.0
-  __TEXT.__text: 0x77f9c
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x57c4
+301.23.1.8.0
+  __TEXT.__text: 0x780f0
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_methlist: 0x57f4
   __TEXT.__const: 0x1268
   __TEXT.__cstring: 0x6541
-  __TEXT.__oslogstring: 0x7f39
+  __TEXT.__oslogstring: 0x7f69
   __TEXT.__gcc_except_tab: 0x6b8
   __TEXT.__dlopen_cstrs: 0x2f1
   __TEXT.__ustring: 0x136

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1cb8
+  __TEXT.__unwind_info: 0x1cc0
   __TEXT.__eh_frame: 0x11a8
-  __TEXT.__objc_classname: 0xa5f
-  __TEXT.__objc_methname: 0xd4d0
-  __TEXT.__objc_methtype: 0xfd7
-  __TEXT.__objc_stubs: 0x8f20
-  __DATA_CONST.__got: 0x7e0
+  __TEXT.__objc_classname: 0xa70
+  __TEXT.__objc_methname: 0xd521
+  __TEXT.__objc_methtype: 0xfe5
+  __TEXT.__objc_stubs: 0x8f80
+  __DATA_CONST.__got: 0x7e8
   __DATA_CONST.__const: 0x1d00
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f10
+  __DATA_CONST.__objc_selrefs: 0x2f28
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x20b0
-  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__auth_got: 0xb50
   __AUTH_CONST.__const: 0x13a0
   __AUTH_CONST.__cfstring: 0x7240
-  __AUTH_CONST.__objc_const: 0xaf80
+  __AUTH_CONST.__objc_const: 0xb010
   __AUTH_CONST.__objc_intobj: 0xae0
   __AUTH_CONST.__objc_dictobj: 0x1478
   __AUTH_CONST.__objc_arrayobj: 0x528
-  __AUTH.__objc_data: 0x1460
+  __AUTH.__objc_data: 0x14b0
   __AUTH.__data: 0x460
   __DATA.__objc_ivar: 0x680
   __DATA.__data: 0x5c8

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2B6D751B-724A-3C3E-B16A-8C1D6939AF31
-  Functions: 2884
-  Symbols:   8017
-  CStrings:  5147
+  UUID: 9A9F51F5-22F2-3E57-B1EB-47EDFCB5DA01
+  Functions: 2888
+  Symbols:   8034
+  CStrings:  5153
 
Symbols:
+ +[ICQDaemonOfferConditions canUsePhotoLibrary]
+ +[ICQDaemonOfferConditions getLibrarySizesFromDB:photoLibrary:]
+ +[ICQDaemonOfferConditions getLibrarySizesFromDB:photoLibrary:].cold.1
+ +[_ICQMobileKeyBag isDeviceUnlockedSinceBoot]
+ GCC_except_table17
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$__ICQMobileKeyBag
+ _OBJC_METACLASS_$__ICQMobileKeyBag
+ __OBJC_$_CLASS_METHODS__ICQMobileKeyBag
+ __OBJC_CLASS_RO_$__ICQMobileKeyBag
+ __OBJC_METACLASS_RO_$__ICQMobileKeyBag
+ ___block_descriptor_56_e8_32s40s48r_e18_v16?0"NSNumber"8ls32l8r48l8s40l8
+ _objc_msgSend$canUsePhotoLibrary
+ _objc_msgSend$getLibrarySizesFromDB:photoLibrary:
+ _objc_msgSend$isDeviceUnlockedSinceBoot
- GCC_except_table15
- ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r48l8s40l8
CStrings:
+ "@28@0:8B16@20"
+ "Error from getLibrarySizesFromDB: %@"
+ "_ICQMobileKeyBag"
+ "canUsePhotoLibrary"
+ "getLibrarySizesFromDB:photoLibrary:"
+ "isDeviceUnlockedSinceBoot"

```
