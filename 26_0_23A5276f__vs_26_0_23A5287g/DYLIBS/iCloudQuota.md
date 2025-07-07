## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.23.0.17.0
-  __TEXT.__text: 0x76c98
-  __TEXT.__auth_stubs: 0x1660
+301.23.0.19.0
+  __TEXT.__text: 0x76fd0
+  __TEXT.__auth_stubs: 0x1670
   __TEXT.__objc_methlist: 0x57c4
-  __TEXT.__const: 0x1080
-  __TEXT.__cstring: 0x6491
-  __TEXT.__oslogstring: 0x7ed9
-  __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__dlopen_cstrs: 0x35f
+  __TEXT.__const: 0x10a0
+  __TEXT.__cstring: 0x6481
+  __TEXT.__oslogstring: 0x7f39
+  __TEXT.__gcc_except_tab: 0x6b8
+  __TEXT.__dlopen_cstrs: 0x2f1
   __TEXT.__ustring: 0x136
   __TEXT.__swift5_typeref: 0x712
-  __TEXT.__swift5_capture: 0x2b8
+  __TEXT.__swift5_capture: 0x2e0
   __TEXT.__swift5_reflstr: 0x2c1
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__constg_swiftt: 0x6b0

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1cb8
-  __TEXT.__eh_frame: 0x11a0
+  __TEXT.__unwind_info: 0x1cd8
+  __TEXT.__eh_frame: 0x11a8
   __TEXT.__objc_classname: 0xa5f
-  __TEXT.__objc_methname: 0xd4e3
+  __TEXT.__objc_methname: 0xd4d0
   __TEXT.__objc_methtype: 0xfd7
-  __TEXT.__objc_stubs: 0x8ea0
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0x1d68
+  __TEXT.__objc_stubs: 0x8ee0
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__const: 0x1d00
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f18
+  __DATA_CONST.__objc_selrefs: 0x2f10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x20b0
-  __AUTH_CONST.__auth_got: 0xb40
-  __AUTH_CONST.__const: 0x12b8
+  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__const: 0x1330
   __AUTH_CONST.__cfstring: 0x7240
   __AUTH_CONST.__objc_const: 0xaf80
   __AUTH_CONST.__objc_intobj: 0xae0

   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1080
   __DATA_DIRTY.__data: 0x278
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__bss: 0x248
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BFD52F7A-3B1F-38B7-A4C8-95C42069BC45
-  Functions: 2888
-  Symbols:   8031
-  CStrings:  5143
+  UUID: E5177868-3D43-32F8-8466-126D0415847B
+  Functions: 2886
+  Symbols:   8016
+  CStrings:  5142
 
Symbols:
+ +[ICQDaemonOfferConditions getPhotosLibrarySizeWithCompletion:]
+ +[ICQDaemonOfferConditions getPhotosLibraryUploadSizeWithCompletion:].cold.1
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table35
+ ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.293
+ ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke_2.294
+ ___72-[ICQDaemonOfferManager _processOfferStub:account:offerType:completion:]_block_invoke.270
+ ___77-[ICQDaemonOfferManager _reconsiderLocalOffersWithReason:account:completion:]_block_invoke.269
+ ___block_literal_global.141
+ ___block_literal_global.363
+ _objc_msgSend$chooseDefaultStubForConditions:
+ _objc_msgSend$choosePremiumStubForConditions:
+ _objc_msgSend$chooseStubForConditions:
+ _objc_msgSend$getLibrarySizesFromDB:error:
- +[_ICQHelperFunctions getPhotosLibrarySizeWithCompletion:]
- GCC_except_table11
- GCC_except_table13
- GCC_except_table14
- GCC_except_table37
- _OBJC_CLASS_$_PLGatekeeperClient
- _PhotoLibraryServicesCoreLibraryCore.frameworkLibrary
- ___58+[_ICQHelperFunctions getPhotosLibrarySizeWithCompletion:]_block_invoke
- ___69+[ICQDaemonOfferConditions getPhotosLibraryUploadSizeWithCompletion:]_block_invoke
- ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke.291
- ___71-[ICQDaemonOfferManager _processPushNotificationDictionary:completion:]_block_invoke_2.293
- ___72-[ICQDaemonOfferManager _processOfferStub:account:offerType:completion:]_block_invoke.269
- ___77-[ICQDaemonOfferManager _reconsiderLocalOffersWithReason:account:completion:]_block_invoke.268
- ___PhotoLibraryServicesCoreLibraryCore_block_invoke
- ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
- ___block_descriptor_48_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
- ___block_literal_global.146
- ___block_literal_global.362
- ___getPLGatekeeperClientClass_block_invoke
- ___getPLGatekeeperClientClass_block_invoke.cold.1
- _audit_stringPhotoLibraryServicesCore
- _getPLGatekeeperClientClass.softClass
- _objc_msgSend$getLibrarySizes:
- _objc_msgSend$getLibrarySizesFromDB:handler:
CStrings:
+ "Requesting library size from PHPhotoLibrary"
+ "Requesting library size from PHPhotoLibrary using DB"
+ "getLibrarySizesFromDB:error:"
- "PLGatekeeperClient"
- "getLibrarySizes:"
- "getLibrarySizesFromDB:handler:"
- "softlink:r:path:/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore"

```
