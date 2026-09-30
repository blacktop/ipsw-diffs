## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-710.7.140.0.0
-  __TEXT.__text: 0xbd924
-  __TEXT.__auth_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0x6478
+710.14.102.0.0
+  __TEXT.__text: 0xbe8dc
+  __TEXT.__auth_stubs: 0x1c70
+  __TEXT.__objc_methlist: 0x64c0
   __TEXT.__const: 0x2434
-  __TEXT.__gcc_except_tab: 0x6c98
-  __TEXT.__cstring: 0x13731
-  __TEXT.__oslogstring: 0x9721
+  __TEXT.__gcc_except_tab: 0x6d90
+  __TEXT.__cstring: 0x137d7
+  __TEXT.__oslogstring: 0x97d7
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2f28
-  __TEXT.__objc_classname: 0x1008
-  __TEXT.__objc_methname: 0x14d7c
-  __TEXT.__objc_methtype: 0x4a27
-  __TEXT.__objc_stubs: 0xb560
-  __DATA_CONST.__got: 0xa78
+  __TEXT.__unwind_info: 0x2f68
+  __TEXT.__objc_classname: 0x104f
+  __TEXT.__objc_methname: 0x14ea8
+  __TEXT.__objc_methtype: 0x4aca
+  __TEXT.__objc_stubs: 0xb5a0
+  __DATA_CONST.__got: 0xa88
   __DATA_CONST.__const: 0x3820
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47a0
-  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x47d8
+  __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x430
-  __AUTH_CONST.__auth_got: 0xe30
+  __DATA_CONST.__objc_arraydata: 0x418
+  __AUTH_CONST.__auth_got: 0xe48
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3290
-  __AUTH_CONST.__cfstring: 0x10880
-  __AUTH_CONST.__objc_const: 0xcbb8
-  __AUTH_CONST.__objc_intobj: 0x9a8
+  __AUTH_CONST.__const: 0x32b0
+  __AUTH_CONST.__cfstring: 0x108a0
+  __AUTH_CONST.__objc_const: 0xcd38
+  __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0xfc0
-  __DATA.__bss: 0xbd0
+  __AUTH_CONST.__objc_arrayobj: 0x258
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x628
+  __DATA.__data: 0x1020
+  __DATA.__bss: 0xbe0
   __DATA_DIRTY.__objc_data: 0x2490
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x4f0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3644
-  Symbols:   5436
-  CStrings:  7019
+  Functions: 3659
+  Symbols:   5457
+  CStrings:  7040
 
Symbols:
+ _PFErrorOrUnderlyingErrorMatchesCodesByDomain
+ _PFUnderlyingErrorThatMatchesCodesByDomain
+ _PFMaxPathComponentCountLimit
+ _PLPlatformCleanupRegionSupported
+ _PLPlatformSharedAlbumAndiCPLPrefetchSupported
+ _OBJC_CLASS_$_PLAssetsdNonBindingDebugClient
+ _PFIsErrorOrUnderlyingErrorFileNotFound
+ _OBJC_METACLASS_$_PLAssetsdNonBindingDebugClient
- _PLPlatformCloudPhotosPrefetchSupported
CStrings:
+ "\x0f\t"
+ "PLAssetsdNonBindingDebugServiceProtocol"
+ "PLAssetsdNonBindingDebugClient"
+ "getExistingPhotoLibraryIdentifierWithLibraryURL:reply:"
+ "Open XPC transactions: %!d(MISSING)"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "@40@0:8I16B20@24@32"
+ "PLXPC Client: existingPhotoLibraryIdentifierForPhotoLibraryURL:error:"
+ "statusDescription"
+ "v24@0:8@?<v@?@\"<PLAssetsdNonBindingDebugServiceProtocol>\"@\"NSError\">16"
+ "realURLForURL:error:"
+ "@32@0:8I16B20@24"
+ "-[PLAssetsdNonBindingDebugClient existingPhotoLibraryIdentifierForPhotoLibraryURL:error:]_block_invoke"
+ "PLXPC Client: boundServicesForLibrary:error:"
+ "PLPlatformCleanupRegionSupported"
+ "\a"
+ "nonBindingDebugClient"
+ "_nonBindingDebugClient"
+ "existingPhotoLibraryIdentifierForPhotoLibraryURL:error:"
+ "T@\"NSString\",R,C,N"
+ "I20@0:8B16"
+ "I80@0:8B16B20B24B28B32B36B40B44B48B52B56B60B64B68B72B76"
+ "@20@0:8I16"
+ "T@\"PLAssetsdNonBindingDebugClient\",R"
+ "fractionCompleted"
+ "PLPlatformCleanupRegionSupported is overridden to YES via defaults"
+ "boundServicesForLibrary:error:"
+ "-[PLAssetsdNonBindingDebugClient getPhotosXPCEndpoint:error:]_block_invoke"
+ "getNonBindingDebugServiceWithReply:"
+ "getBoundServicesForLibrary:reply:"
+ "_addDebugInterfaces:"
+ "'%!@(MISSING)' (progress=%!f(MISSING) units=%!l(MISSING)d req=%!@(MISSING) qos=%!@(MISSING))"
+ "@24@0:8I16B20"
+ "@\"PLAssetsdNonBindingDebugClient\""
- "S20@0:8B16"
- "S80@0:8B16B20B24B28B32B36B40B44B48B52B56B60B64B68B72B76"
- "*"
- "URLIsInTrash:"
- "Number of open XPC transactions: %!d(MISSING).\n"
- "@32@0:8S16B20@24"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "_addDebugInterface:"
- "-[PLAssetsdLibraryManagementClient getPhotosXPCEndpoint:error:]_block_invoke"
- "\x0f\b"
- "\x06"
- "@24@0:8S16B20"
- "@40@0:8S16B20@24@32"

```
