## MailCore

> `/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0x81c7c
-  __TEXT.__objc_methlist: 0x81b4
-  __TEXT.__cstring: 0x801e
+3901.200.34.0.0
+  __TEXT.__text: 0x82a18
+  __TEXT.__objc_methlist: 0x826c
+  __TEXT.__cstring: 0x810c
   __TEXT.__gcc_except_tab: 0x1684
-  __TEXT.__const: 0x4b0
-  __TEXT.__oslogstring: 0x1e68
-  __TEXT.__unwind_info: 0x29b8
+  __TEXT.__const: 0x4b8
+  __TEXT.__oslogstring: 0x1f0e
+  __TEXT.__unwind_info: 0x2a00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1220
-  __DATA_CONST.__objc_classlist: 0x370
+  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5430
+  __DATA_CONST.__objc_selrefs: 0x54b8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __DATA_CONST.__got: 0x1100
-  __AUTH_CONST.__const: 0x1350
-  __AUTH_CONST.__cfstring: 0x91c0
-  __AUTH_CONST.__objc_const: 0xcc70
+  __DATA_CONST.__got: 0x1138
+  __AUTH_CONST.__const: 0x13c0
+  __AUTH_CONST.__cfstring: 0x92a0
+  __AUTH_CONST.__objc_const: 0xced0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x930
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x7a8
+  __AUTH_CONST.__auth_got: 0x948
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x7bc
   __DATA.__data: 0xda8
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0x1720
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x418
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2884
-  Symbols:   7612
-  CStrings:  1474
+  Functions: 2910
+  Symbols:   7668
+  CStrings:  1487
 
Symbols:
+ +[MCImageMetadataService log]
+ +[MCImageMetadataService metadataForImageData:webView:completionHandler:]
+ +[MCImageMetadataService metadataForImageData:webView:error:]
+ -[MCConnection setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
+ -[MCImageJunkMetadata initWithMetadataResult:name:type:]
+ -[MCImageMetadataResult dpiHeight]
+ -[MCImageMetadataResult dpiWidth]
+ -[MCImageMetadataResult initWithPixelWidth:pixelHeight:dpiWidth:dpiHeight:pageCount:]
+ -[MCImageMetadataResult isMultiPage]
+ -[MCImageMetadataResult isRetina]
+ -[MCImageMetadataResult pageCount]
+ -[MCImageMetadataResult pixelHeight]
+ -[MCImageMetadataResult pixelWidth]
+ -[MCImageMetadataResult retinaPointWidth]
+ -[MCImageMetadataResult sizeInPoints]
+ -[MCMessageHeaders appendHeaderData:recipients:recipientsByHeaderKey:expandGroups:includeComment:includeBCC:]
+ OBJC_IVAR_$_MCImageMetadataResult._dpiHeight
+ OBJC_IVAR_$_MCImageMetadataResult._dpiWidth
+ OBJC_IVAR_$_MCImageMetadataResult._pageCount
+ OBJC_IVAR_$_MCImageMetadataResult._pixelHeight
+ OBJC_IVAR_$_MCImageMetadataResult._pixelWidth
+ _OBJC_CLASS_$_MCImageMetadataResult
+ _OBJC_CLASS_$_MCImageMetadataService
+ _OBJC_METACLASS_$_MCImageMetadataResult
+ _OBJC_METACLASS_$_MCImageMetadataService
+ __73+[MCImageMetadataService metadataForImageData:webView:completionHandler:]_block_invoke
+ __OBJC_$_CLASS_METHODS_MCImageMetadataService
+ __OBJC_$_INSTANCE_METHODS_MCImageMetadataResult
+ __OBJC_$_INSTANCE_VARIABLES_MCImageMetadataResult
+ __OBJC_$_PROP_LIST_MCImageMetadataResult
+ __OBJC_CLASS_RO_$_MCImageMetadataResult
+ __OBJC_CLASS_RO_$_MCImageMetadataService
+ __OBJC_METACLASS_RO_$_MCImageMetadataResult
+ __OBJC_METACLASS_RO_$_MCImageMetadataService
+ ___29+[MCImageMetadataService log]_block_invoke
+ ___73+[MCImageMetadataService metadataForImageData:webView:completionHandler:]_block_invoke
+ ____ef_log_MCImageMetadataService_block_invoke
+ ___block_descriptor_48_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
+ __ef_log_MCImageMetadataService
+ __os_signpost_emit_with_name_impl
+ _ef_log_MCImageMetadataService
+ _ef_log_MCImageMetadataService.log
+ _ef_log_MCImageMetadataService.onceToken
+ _kCGImagePropertyDPIHeight
+ _kCGImagePropertyDPIWidth
+ _kCGImagePropertyImageCount
+ _kCGImagePropertyPixelHeight
+ _kCGImagePropertyPixelWidth
+ _objc_msgSend$_getImageMetadata:completionHandler:
+ _objc_msgSend$appendHeaderData:recipients:recipientsByHeaderKey:expandGroups:includeComment:includeBCC:
+ _objc_msgSend$completionHandlerAdapter
+ _objc_msgSend$ef_isTimeoutError
+ _objc_msgSend$floatValue
+ _objc_msgSend$initWithMetadataResult:name:type:
+ _objc_msgSend$initWithPixelWidth:pixelHeight:dpiWidth:dpiHeight:pageCount:
+ _objc_msgSend$isRetina
+ _objc_msgSend$metadataForImageData:webView:completionHandler:
+ _objc_msgSend$pageCount
+ _objc_msgSend$setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:
+ _objc_msgSend$sizeInPoints
+ _os_signpost_enabled
+ _os_signpost_id_generate
- +[NSString(MCMimeEnrichedReader) stringFromMimeEnrichedString:]
- -[MCConnection _setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:]
- _DefaultsKeyUserOptedIntoAttachmentSending
- _objc_msgSend$_setupConnectionErrorForMonitorWithPort:usingSSL:serverTrust:
- _objc_msgSend$convertEnrichedString:intoPlainOutputString:
- _objc_msgSend$initWithImage:name:type:
CStrings:
+ "%@ must not be called on the main thread"
+ "Empty image data"
+ "Image metadata SPI unavailable"
+ "Image metadata SPI unavailable on this WebKit build"
+ "Image metadata extraction failed: %{public}@"
+ "Image metadata extraction returned no data"
+ "Image metadata extraction timed out"
+ "ImageMetadataSPI"
+ "MCImageMetadataService"
+ "MCImageMetadataService.m"
+ "Missing WKWebView"
+ "bytes=%lu"
+ "ok=%d"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "UserOptedIntoAttachmentSending"
```
