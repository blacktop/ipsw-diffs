## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-212.60.2.0.0
-  __TEXT.__text: 0x2d568
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x37ec
+212.100.2.0.0
+  __TEXT.__text: 0x30860
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x3824
   __TEXT.__const: 0x164
-  __TEXT.__cstring: 0x2b56
+  __TEXT.__cstring: 0x2b63
   __TEXT.__oslogstring: 0x215e
-  __TEXT.__gcc_except_tab: 0x13f4
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__gcc_except_tab: 0x1394
+  __TEXT.__unwind_info: 0xf80
   __TEXT.__objc_classname: 0x748
-  __TEXT.__objc_methname: 0x7665
-  __TEXT.__objc_methtype: 0x1ac1
-  __TEXT.__objc_stubs: 0x5aa0
+  __TEXT.__objc_methname: 0x772a
+  __TEXT.__objc_methtype: 0x1ad1
+  __TEXT.__objc_stubs: 0x5b00
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__const: 0xb80
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c40
+  __DATA_CONST.__objc_selrefs: 0x1c58
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2ba0
-  __AUTH_CONST.__objc_const: 0x6200
+  __AUTH_CONST.__cfstring: 0x2bc0
+  __AUTH_CONST.__objc_const: 0x6230
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x11f8
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x800
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A07D3924-4331-3182-BC2F-6B620ADD788B
-  Functions: 1230
-  Symbols:   4492
-  CStrings:  2625
+  UUID: F5DA785D-A53C-399B-A0F2-706F70D11968
+  Functions: 1243
+  Symbols:   4548
+  CStrings:  2631
 
Symbols:
+ +[ASTLocalization prepareLocalizedStringsForCountryCode:withCompletionHandler:]
+ +[ASTRemoteServerSession downloadAsset:serverURL:endpoint:countryCode:fileHandle:completionHandler:]
+ +[ASTSession requestAsset:serverURL:endpoint:countryCode:completionHandler:]
+ -[ASTConnectionAsset countryCode]
+ -[ASTConnectionAsset initWithServerURL:endpoint:countryCode:assetName:destinationFileHandle:]
+ -[ASTMaterializedConnection countryCode]
+ -[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:countryCode:destinationFileHandle:allowsCellularAccess:completion:]
+ -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:]
+ -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:].cold.1
+ -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:].cold.2
+ -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:].cold.3
+ -[ASTSession requestAsset:serverURL:endpoint:countryCode:completionHandler:]
+ GCC_except_table58
+ GCC_except_table62
+ _OBJC_IVAR_$_ASTConnectionAsset._countryCode
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___135-[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:countryCode:destinationFileHandle:allowsCellularAccess:completion:]_block_invoke
+ ___135-[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:countryCode:destinationFileHandle:allowsCellularAccess:completion:]_block_invoke.cold.1
+ ___79+[ASTLocalization prepareLocalizedStringsForCountryCode:withCompletionHandler:]_block_invoke
+ ___79+[ASTLocalization prepareLocalizedStringsForCountryCode:withCompletionHandler:]_block_invoke.cold.1
+ ___79+[ASTLocalization prepareLocalizedStringsForCountryCode:withCompletionHandler:]_block_invoke.cold.2
+ ___87-[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:]_block_invoke
+ ___87-[ASTSession fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:]_block_invoke.cold.1
+ _kASTHTTPHeaderCountryCode
+ _objc_msgSend$countryCode
+ _objc_msgSend$downloadAsset:serverURL:endpoint:countryCode:destinationFileHandle:allowsCellularAccess:completion:
+ _objc_msgSend$downloadAsset:serverURL:endpoint:countryCode:fileHandle:completionHandler:
+ _objc_msgSend$fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:
+ _objc_msgSend$initWithServerURL:endpoint:countryCode:assetName:destinationFileHandle:
+ _objc_msgSend$prepareLocalizedStringsForCountryCode:withCompletionHandler:
+ _objc_msgSend$requestAsset:serverURL:endpoint:countryCode:completionHandler:
- +[ASTRemoteServerSession downloadAsset:serverURL:endpoint:fileHandle:completionHandler:]
- -[ASTConnectionAsset initWithServerURL:endpoint:assetName:destinationFileHandle:]
- -[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:destinationFileHandle:allowsCellularAccess:completion:]
- -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:]
- -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:].cold.1
- -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:].cold.2
- -[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:].cold.3
- GCC_except_table56
- GCC_except_table60
- ___123-[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:destinationFileHandle:allowsCellularAccess:completion:]_block_invoke
- ___123-[ASTMaterializedConnectionManager downloadAsset:serverURL:endpoint:destinationFileHandle:allowsCellularAccess:completion:]_block_invoke.cold.1
- ___64+[ASTLocalization prepareLocalizedStringsWithCompletionHandler:]_block_invoke
- ___64+[ASTLocalization prepareLocalizedStringsWithCompletionHandler:]_block_invoke.cold.1
- ___64+[ASTLocalization prepareLocalizedStringsWithCompletionHandler:]_block_invoke.cold.2
- ___75-[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:]_block_invoke
- ___75-[ASTSession fetchAsset:sessionClass:serverURL:endpoint:completionHandler:]_block_invoke.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$downloadAsset:serverURL:endpoint:destinationFileHandle:allowsCellularAccess:completion:
- _objc_msgSend$downloadAsset:serverURL:endpoint:fileHandle:completionHandler:
- _objc_msgSend$fetchAsset:sessionClass:serverURL:endpoint:completionHandler:
- _objc_msgSend$initWithServerURL:endpoint:assetName:destinationFileHandle:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "Country-Code"
+ "_countryCode"
+ "countryCode"
+ "downloadAsset:serverURL:endpoint:countryCode:destinationFileHandle:allowsCellularAccess:completion:"
+ "downloadAsset:serverURL:endpoint:countryCode:fileHandle:completionHandler:"
+ "fetchAsset:sessionClass:serverURL:endpoint:countryCode:completionHandler:"
+ "initWithServerURL:endpoint:countryCode:assetName:destinationFileHandle:"
+ "prepareLocalizedStringsForCountryCode:withCompletionHandler:"
+ "requestAsset:serverURL:endpoint:countryCode:completionHandler:"
+ "v64@0:8@16#24@32@40@48@?56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v68@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40@\"NSFileHandle\"48B56@?<v@?B@\"NSError\">60"
- "downloadAsset:serverURL:endpoint:destinationFileHandle:allowsCellularAccess:completion:"
- "downloadAsset:serverURL:endpoint:fileHandle:completionHandler:"
- "fetchAsset:sessionClass:serverURL:endpoint:completionHandler:"
- "initWithServerURL:endpoint:assetName:destinationFileHandle:"
- "v56@0:8@16#24@32@40@?48"
- "v60@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSFileHandle\"40B48@?<v@?B@\"NSError\">52"
- "v60@0:8@16@24@32@40B48@?52"

```
