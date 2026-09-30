## MiniSoftwareUpdate

> `/System/Library/PrivateFrameworks/MiniSoftwareUpdate.framework/Versions/A/MiniSoftwareUpdate`

```diff

 43.0.0.0.0
-  __TEXT.__text: 0x9e28
+  __TEXT.__text: 0x9dac
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x840
+  __TEXT.__objc_methlist: 0x9a4
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__gcc_except_tab: 0x150
   __TEXT.__cstring: 0xab1
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x102
   __TEXT.__objc_methname: 0x2252
   __TEXT.__objc_methtype: 0x49a
   __TEXT.__objc_stubs: 0x1a80
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x810
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__objc_const: 0x1840
+  __AUTH_CONST.__objc_const: 0x15c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x2d0

   - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1605E3E9-4B15-3838-B0CF-FBEC107B088F
-  Functions: 203
-  Symbols:   771
+  UUID: C7C3006A-675E-3F78-94E1-679F72952F24
+  Functions: 208
+  Symbols:   776
   CStrings:  689
 
Symbols:
+ +[MSUContentLocatorPackageSource _contentLocatorFunction].cold.1
+ +[MSUDataDownloader downloaderForCatalogURL:options:].cold.1
+ +[MSUDataDownloader downloaderForCatalogURL:options:].cold.2
+ -[MSUNSURLSessionDataDownloader initWithCatalogOptions:].cold.1
+ msu_qos_class_self.cold.1
Functions:
~ ___61-[MSUProductManager registerCatalogAtURL:options:completion:]_block_invoke : 1876 -> 1884
~ -[MSUProductManager __evaluateProduct:evaluationOptions:catalog:installable:error:] : 5880 -> 5876
~ ___60-[MSUProductManager evaluateProductsWithOptions:completion:]_block_invoke_2 : 328 -> 332
~ +[MSUProductManager _sendSynchronousRequest:catalogURL:options:error:] : 464 -> 460
~ +[MSUProductManager _downloadPKMForPackage:product:catalog:error:] : 1100 -> 1096
~ +[MSUDataDownloader downloaderForCatalogURL:options:] : 348 -> 316
~ -[MSUNSURLSessionDataDownloader initWithCatalogOptions:] : 316 -> 300
~ +[MSUNSURLSessionDataDownloader _checkForServerTrust:error:] : 100 -> 84
~ -[MSUNSURLConnectionDataDownloader sendSynchronousRequest:response:error:] : 752 -> 748
~ +[MSUContentLocatorPackageSource _contentLocatorFunction] : 140 -> 124
~ +[MSUContentLocatorPackageSource _modifiedPackageReferencesForPackages:] : 1248 -> 1252
~ -[MSUCatalog initWithLocalProductsDirectoryURL:options:error:] : 328 -> 324
~ -[MSUCatalog _parseFromDictionary:error:] : 1004 -> 996
~ _msu_qos_class_self : 96 -> 76
~ -[MSUProduct initWithProductKey:dictionaryRepresentation:error:] : 3800 -> 3668

```
