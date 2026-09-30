## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-750.17.102.0.0
-  __TEXT.__text: 0xc2c7c
+752.0.105.0.0
+  __TEXT.__text: 0xc4b74
   __TEXT.__auth_stubs: 0x1c80
-  __TEXT.__objc_methlist: 0x7cd4
+  __TEXT.__objc_methlist: 0x7e74
   __TEXT.__const: 0x249c
-  __TEXT.__cstring: 0x13fec
+  __TEXT.__cstring: 0x1418b
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x7080
-  __TEXT.__oslogstring: 0x9db9
-  __TEXT.__unwind_info: 0x2ff8
-  __TEXT.__objc_classname: 0x107a
-  __TEXT.__objc_methname: 0x1524d
-  __TEXT.__objc_methtype: 0x4bed
-  __TEXT.__objc_stubs: 0xb9e0
-  __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0x39b0
-  __DATA_CONST.__objc_classlist: 0x400
+  __TEXT.__gcc_except_tab: 0x71dc
+  __TEXT.__oslogstring: 0x9e09
+  __TEXT.__unwind_info: 0x3068
+  __TEXT.__objc_classname: 0x1100
+  __TEXT.__objc_methname: 0x15488
+  __TEXT.__objc_methtype: 0x4c61
+  __TEXT.__objc_stubs: 0xbb00
+  __DATA_CONST.__got: 0xab0
+  __DATA_CONST.__const: 0x39c8
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4978
+  __DATA_CONST.__objc_selrefs: 0x49c0
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x408
   __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3310
-  __AUTH_CONST.__cfstring: 0x10ca0
-  __AUTH_CONST.__objc_const: 0xa5d0
+  __AUTH_CONST.__cfstring: 0x10da0
+  __AUTH_CONST.__objc_const: 0xaa40
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x640
-  __DATA.__data: 0x1020
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x678
+  __DATA.__data: 0x1080
   __DATA.__bss: 0xba8
   __DATA_DIRTY.__objc_data: 0x2580
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3688
-  Symbols:   5562
-  CStrings:  7133
+  Functions: 3730
+  Symbols:   5613
+  CStrings:  7173
 
Symbols:
+ _OBJC_CLASS_$_PLNonBindingAssetsdPhotoKitAddClient
+ _OBJC_CLASS_$_PLNonBindingAssetsdPhotoKitClient
+ _OBJC_CLASS_$_PLXPCLibraryToken
+ _OBJC_METACLASS_$_PLNonBindingAssetsdPhotoKitAddClient
+ _OBJC_METACLASS_$_PLNonBindingAssetsdPhotoKitClient
+ _OBJC_METACLASS_$_PLXPCLibraryToken
+ _PLVoidResultFromResultAndError
+ _sClientOptionsKey
+ _sSandboxExtensionKey
+ _sUrlKey
CStrings:
+ "\x04"
+ "\x0f\r"
+ "-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:reply:]_block_invoke"
+ "-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:reply:]_block_invoke"
+ "@\"PLNonBindingAssetsdPhotoKitAddClient\""
+ "@\"PLNonBindingAssetsdPhotoKitClient\""
+ "@\"PLXPCLibraryToken\""
+ "PLAssetsdNonBindingPhotoKitServiceProtocol"
+ "PLNonBindingAssetsdPhotoKitAddClient"
+ "PLNonBindingAssetsdPhotoKitClient"
+ "PLVoidResult * _Nonnull PLVoidResultFromResultAndError(BOOL, NSError * _Nullable __strong)"
+ "PLXPC Client: sendChangesRequest:error:"
+ "PLXPC Client: sendChangesRequest:reply:"
+ "PLXPCLibraryToken"
+ "PLXPCLibraryToken.m"
+ "PLXPCLibraryToken.url cannot be nil"
+ "PhotoKitAddService_applyChangesRequest:libraryToken:reply:"
+ "PhotoKitService_applyChangesRequest:libraryToken:reply:"
+ "T@\"NSData\",R,C,V_sandboxExtension"
+ "T@\"NSDictionary\",R,C,V_clientOptions"
+ "T@\"NSURL\",R,C,V_url"
+ "T@\"PLNonBindingAssetsdPhotoKitAddClient\",R"
+ "T@\"PLNonBindingAssetsdPhotoKitClient\",R"
+ "_clientOptions"
+ "_libraryToken"
+ "_nonBindingPhotoKitAddClient"
+ "_nonBindingPhotoKitClient"
+ "_sandboxExtension"
+ "clientOptions"
+ "decodeObjectOfClasses:forKey:"
+ "error == nil"
+ "initWithQueue:proxyCreating:libraryURL:"
+ "initWithURL:sandboxExtension:clientOptions:"
+ "non-binding PhotoKit client"
+ "non-binding PhotoKitAdd client"
+ "nonBindingPhotoKitAddClient"
+ "nonBindingPhotoKitClient"
+ "photosLibraryTombstoneExtension"
+ "sandboxExtension"
+ "tombstone"
+ "v40@0:8@\"PLXPCObject\"16@\"PLXPCLibraryToken\"24@?<v@?B@\"NSError\">32"
- "\x0f\n"
- "bindToPhotoLibraryURL:sandboxExtension:withReply:"
- "v40@0:8@\"NSURL\"16@\"NSData\"24@?<v@?@\"NSError\">32"

```
