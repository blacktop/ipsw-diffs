## PrintKit

> `/System/Library/PrivateFrameworks/PrintKit.framework/Versions/A/PrintKit`

```diff

-306.0.0.0.0
-  __TEXT.__text: 0x4d478
+306.2.0.0.0
+  __TEXT.__text: 0x4d3c0
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x2c40
-  __TEXT.__const: 0x408
-  __TEXT.__gcc_except_tab: 0x8e30
-  __TEXT.__cstring: 0x79df
-  __TEXT.__oslogstring: 0xed7
-  __TEXT.__unwind_info: 0x2c00
+  __TEXT.__objc_methlist: 0x3020
+  __TEXT.__const: 0x438
+  __TEXT.__gcc_except_tab: 0x8ea4
+  __TEXT.__cstring: 0x7a12
+  __TEXT.__oslogstring: 0xf03
+  __TEXT.__unwind_info: 0x2bf0
   __TEXT.__objc_classname: 0x467
-  __TEXT.__objc_methname: 0x6473
+  __TEXT.__objc_methname: 0x6516
   __TEXT.__objc_methtype: 0xff5
-  __TEXT.__objc_stubs: 0x4f80
-  __DATA_CONST.__got: 0x250
+  __TEXT.__objc_stubs: 0x5060
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0xcda8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b00
+  __DATA_CONST.__objc_selrefs: 0x1bb8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x6190
   __AUTH_CONST.__auth_got: 0x480
   __AUTH_CONST.__const: 0x21e8
-  __AUTH_CONST.__cfstring: 0xd800
-  __AUTH_CONST.__objc_const: 0x5ac0
+  __AUTH_CONST.__cfstring: 0xd880
+  __AUTH_CONST.__objc_const: 0x53b8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1350
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36006B1A-1BB0-3DF7-96CD-FEF72151D527
+  UUID: 44A3D039-7A92-37CB-8C6F-5C45503C7AA8
   Functions: 1563
-  Symbols:   4237
-  CStrings:  5299
+  Symbols:   4258
+  CStrings:  5316
 
Symbols:
+ +[PKDefaults startiCloudListening].cold.1
+ +[PKDefaults(PrintKitPrivate) urfIsOptional].cold.1
+ +[PKJob jobsCompletionHandler:].cold.1
+ +[PKPaper defaultGenericPaperForLocale:].cold.1
+ +[PKPrinterTool_Client sharedClient].cold.1
+ -[PKPrinter nearbyURL]
+ GCC_except_table109
+ GCC_except_table144
+ OBJC_IVAR_$_PKPrinterTool_Client._conn_needsLock
+ _OBJC_CLASS_$_NSCharacterSet
+ _PKLogCategory.cold.1
+ _Z12internStringP8NSString.cold.1
+ _Z20internUTF8ByteStringPKcm.cold.1
+ _Z29getPrintdRPCProtocolInterfacev.cold.1
+ _ZL11initNSColorv.cold.1
+ _ZL17findOrMakePrinterP19PKPrinterBrowseInfo.cold.1
+ __41-[PKCloudResolveContext _driveResolution]_block_invoke.353
+ __41-[PKCloudResolveContext _driveResolution]_block_invoke_2.354
+ __41-[PKPrinter unlockWithCompletionHandler:]_block_invoke.135
+ __53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.147
+ __53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.148
+ __57-[PKPrinter pollForPrinterStatusQueue:completionHandler:]_block_invoke.171
+ __Block_byref_object_copy_.396
+ __Block_byref_object_dispose_.397
+ ___ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.393
+ __block_literal_global.392
+ _objc_msgSend$URLHostAllowedCharacterSet
+ _objc_msgSend$setHost:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setQuery:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$stringByAddingPercentEncodingWithAllowedCharacters:
+ _objc_msgSend$stringByAppendingString:
- GCC_except_table108
- GCC_except_table145
- OBJC_IVAR_$_PKPrinterTool_Client._conn
- __41-[PKCloudResolveContext _driveResolution]_block_invoke.334
- __41-[PKCloudResolveContext _driveResolution]_block_invoke_2.335
- __41-[PKPrinter unlockWithCompletionHandler:]_block_invoke.118
- __53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.130
- __53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.131
- __57-[PKPrinter pollForPrinterStatusQueue:completionHandler:]_block_invoke.154
- __Block_byref_object_copy_.377
- __Block_byref_object_dispose_.378
- __ZL13isAsciiStringPKcm
- ___ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.374
- __block_literal_global.373
CStrings:
+ "._ipp._tcp.local."
+ "._ipps._tcp.local."
+ "Failed to generate a url from bonjour name\n"
+ "URLHostAllowedCharacterSet"
+ "_conn_needsLock"
+ "dnssd"
+ "nearbyURL"
+ "setHost:"
+ "setPath:"
+ "setQuery:"
+ "setScheme:"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "stringByAppendingString:"
+ "uuid=%@"
- "_conn"

```
