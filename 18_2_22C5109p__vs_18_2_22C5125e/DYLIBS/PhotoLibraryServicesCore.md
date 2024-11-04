## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0xc00dc
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0x6540
+720.4.101.0.0
+  __TEXT.__text: 0xc19d4
+  __TEXT.__auth_stubs: 0x1c80
+  __TEXT.__objc_methlist: 0x6578
   __TEXT.__const: 0x2484
-  __TEXT.__gcc_except_tab: 0x6ea4
-  __TEXT.__cstring: 0x138ce
-  __TEXT.__oslogstring: 0x9ad1
+  __TEXT.__gcc_except_tab: 0x6fdc
+  __TEXT.__cstring: 0x13c2c
+  __TEXT.__oslogstring: 0x9c8e
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2fa0
+  __TEXT.__unwind_info: 0x2ff8
   __TEXT.__objc_classname: 0x104f
-  __TEXT.__objc_methname: 0x1504e
-  __TEXT.__objc_methtype: 0x4af6
-  __TEXT.__objc_stubs: 0xb660
+  __TEXT.__objc_methname: 0x151c1
+  __TEXT.__objc_methtype: 0x4b5e
+  __TEXT.__objc_stubs: 0xb740
   __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0x3838
+  __DATA_CONST.__const: 0x3860
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4830
+  __DATA_CONST.__objc_selrefs: 0x4870
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x418
-  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x32b0
-  __AUTH_CONST.__cfstring: 0x10920
-  __AUTH_CONST.__objc_const: 0xcdb0
+  __AUTH_CONST.__cfstring: 0x10a20
+  __AUTH_CONST.__objc_const: 0xce10
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x62c
   __DATA.__data: 0x1020
-  __DATA.__bss: 0xbd0
-  __DATA_DIRTY.__objc_data: 0x2490
+  __DATA.__bss: 0xb90
+  __DATA_DIRTY.__objc_data: 0x24e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x4f0
+  __DATA_DIRTY.__bss: 0x530
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3674
-  Symbols:   5477
-  CStrings:  7070
+  Functions: 3686
+  Symbols:   5490
+  CStrings:  7100
 
Symbols:
+ _CGImageSourceGetPrimaryImageIndex
+ _os_transaction_get_description
- _PFFigCopyImageDataWithProperties
CStrings:
+ "%!{(MISSING)public}@, backtrace:\n%!@(MISSING)"
+ "-[PLAssetsdPhotoKitClient cancelReservedCloudIdentifiersWithEntityName:error:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient reserveCloudIdentifiersWithEntityName:count:error:]_block_invoke"
+ "-[PLAssetsdPhotoKitClient reservedCloudIdentifiersWithEntityName:error:]_block_invoke"
+ "@40@0:8@16Q24^@32"
+ "AppPrivateData invalid bundle root. Error: %!@(MISSING)"
+ "PLPhotosErrorIdentifierReservationLimitExceeded"
+ "PLPhotosErrorUnsupportedIdentifier"
+ "PLXPC Client: cancelReservedCloudIdentifiersWithEntityName:error:"
+ "PLXPC Client: reserveCloudIdentifiersWithEntityName:count:error:"
+ "PLXPC Client: reservedCloudIdentifiersWithEntityName:error:"
+ "PLXPCTransaction: NULL identifier passed as argument."
+ "PLXPCTransaction: created NULL os_transaction (identifier: %!s(MISSING), transactionDescription: %!@(MISSING))."
+ "PLXPCTransaction: created nil transaction description (identifier: %!s(MISSING))."
+ "PLXPCTransaction: identifier passed as empty string argument."
+ "PLXPCTransaction: os_transaction has a NULL description (identifier: %!s(MISSING), transactionDescription: %!@(MISSING))."
+ "PLXPCTransaction: os_transaction has an empty description (identifier: %!s(MISSING), transactionDescription: %!@(MISSING))."
+ "Received error cancelling reserved cloud identifiers, error: %!@(MISSING)"
+ "Received error reserving cloud identifiers, error: %!@(MISSING)"
+ "Received error retrieving reserved cloud identifiers, error: %!@(MISSING)"
+ "_validateBundleRootWithPathManager:"
+ "arrayWithArray:"
+ "cancelReservedCloudIdentifiersWithEntityName:error:"
+ "cancelReservedCloudIdentifiersWithEntityName:reply:"
+ "internalValidateCreationRequestWithError:"
+ "reserveCloudIdentifiersWithEntityName:count:error:"
+ "reserveCloudIdentifiersWithEntityName:count:reply:"
+ "reservedCloudIdentifiersWithEntityName:error:"
+ "reservedCloudIdentifiersWithEntityName:reply:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@?0@\"NSUUID\"8Q16^B24"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "writeableDataForImage:previewImage:imageData:imageUTIType:imageSource:primaryImageProperties:imageOrientation:thumbnailDataOut:imageUTITypeOut:primaryImagePropertiesOut:isJPEGOut:imageDataOut:"
+ "writeableDataForImageData:imageUTIType:imageSource:thumbnailDataOut:imageUTITypeOut:primaryImagePropertiesOut:imageDataOut:"
- "copyPrimaryFormatImageData:toURL:properties:"
- "i40@0:8@16@24@32"
- "writeableDataForImage:previewImage:imageData:imageUTIType:imageSource:exifProperties:imageOrientation:thumbnailDataOut:imageUTITypeOut:exifPropertiesOut:isJPEGOut:imageDataOut:"
- "writeableDataForImageData:imageUTIType:imageSource:thumbnailDataOut:imageUTITypeOut:exifPropertiesOut:imageDataOut:"

```
