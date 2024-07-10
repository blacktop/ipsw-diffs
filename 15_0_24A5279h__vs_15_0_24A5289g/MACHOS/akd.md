## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/Support/akd`

```diff

-486.0.0.0.0
-  __TEXT.__text: 0x189b28
-  __TEXT.__auth_stubs: 0x1b80
-  __TEXT.__objc_stubs: 0x16140
-  __TEXT.__objc_methlist: 0x846c
-  __TEXT.__const: 0x2c80
-  __TEXT.__objc_methname: 0x1f8e7
-  __TEXT.__objc_classname: 0x17b9
-  __TEXT.__objc_methtype: 0x5603
-  __TEXT.__oslogstring: 0x1e27b
-  __TEXT.__gcc_except_tab: 0x2538
-  __TEXT.__cstring: 0xa554
+488.2.0.0.0
+  __TEXT.__text: 0x18d38c
+  __TEXT.__auth_stubs: 0x1bc0
+  __TEXT.__objc_stubs: 0x163c0
+  __TEXT.__objc_methlist: 0x8634
+  __TEXT.__const: 0x2d10
+  __TEXT.__objc_methname: 0x1fce9
+  __TEXT.__objc_classname: 0x17ce
+  __TEXT.__objc_methtype: 0x5669
+  __TEXT.__oslogstring: 0x1e64b
+  __TEXT.__gcc_except_tab: 0x2244
+  __TEXT.__cstring: 0xa734
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__swift5_typeref: 0x15ef
-  __TEXT.__swift5_fieldmd: 0xb18
-  __TEXT.__constg_swiftt: 0x1100
-  __TEXT.__swift5_reflstr: 0xaa5
+  __TEXT.__swift5_typeref: 0x1651
+  __TEXT.__swift5_fieldmd: 0xb6c
+  __TEXT.__constg_swiftt: 0x1190
+  __TEXT.__swift5_reflstr: 0xae5
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_proto: 0x118
-  __TEXT.__swift5_types: 0xe4
-  __TEXT.__swift5_capture: 0x840
+  __TEXT.__swift5_types: 0xec
+  __TEXT.__swift5_capture: 0x86c
   __TEXT.__info_plist: 0x538
-  __TEXT.__unwind_info: 0x4d00
-  __TEXT.__eh_frame: 0x6ac8
-  __DATA_CONST.__auth_got: 0xdd0
-  __DATA_CONST.__got: 0x1450
-  __DATA_CONST.__auth_ptr: 0x440
-  __DATA_CONST.__const: 0xac48
-  __DATA_CONST.__cfstring: 0x62e0
-  __DATA_CONST.__objc_classlist: 0x6a8
+  __TEXT.__unwind_info: 0x4e28
+  __TEXT.__eh_frame: 0x6dc0
+  __DATA_CONST.__auth_got: 0xdf0
+  __DATA_CONST.__got: 0x1458
+  __DATA_CONST.__auth_ptr: 0x4a0
+  __DATA_CONST.__const: 0xad58
+  __DATA_CONST.__cfstring: 0x6300
+  __DATA_CONST.__objc_classlist: 0x6c0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x2a0
+  __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x3a0
+  __DATA_CONST.__objc_protorefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_intobj: 0x270
   __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x23f48
-  __DATA.__objc_selrefs: 0x6920
-  __DATA.__objc_ivar: 0x96c
-  __DATA.__objc_data: 0x5070
-  __DATA.__data: 0x39d0
+  __DATA.__objc_const: 0x246c0
+  __DATA.__objc_selrefs: 0x69d8
+  __DATA.__objc_ivar: 0x970
+  __DATA.__objc_data: 0x5298
+  __DATA.__data: 0x3a60
   __DATA.__bss: 0x21b0
   __DATA.__common: 0x114
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6415
-  Symbols:   1220
-  CStrings:  1368
+  Functions: 6493
+  Symbols:   1226
+  CStrings:  1378
 
Symbols:
+ _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
+ _$sSS10FoundationE8EncodingV4utf8ACvgZ
+ _$sSS10FoundationE8EncodingVMa
+ _AKMDMInfoRequiredHeaderKey
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ _swift_dynamicCastObjCClass
CStrings:
+ "-[AKAuthModeController fetchAuthModeWithContext:client:completion:]_block_invoke"
+ "AKApplicationMetadataRequestProvider"
+ "AKApplicationMetadataService"
+ "AKApplicationMetadataServiceProviding"
+ "SELECT client_id, app_name, app_developer_name FROM authorized_primary_applications"
+ "X-Apple-I-Client-Id"
+ "akd.ApplicationMetadataService"
+ "com.apple.authkit.urlbag.clearanceQueue"
+ "com.apple.authkit.urlbag.trafficQueue"
+ "metadataService"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@?0B8@\"NSError\"12@\"NSData\"20I28*32"
- "-[AKUserInfoController fetchAuthModeWithContext:client:completion:]_block_invoke"
- "AKBagFetchTrafficQueue"

```
