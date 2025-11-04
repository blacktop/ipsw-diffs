## PrintKit

> `/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit`

```diff

-319.0.0.0.0
-  __TEXT.__text: 0x48570
+319.1.0.0.0
+  __TEXT.__text: 0x4901c
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x303c
+  __TEXT.__objc_methlist: 0x312c
   __TEXT.__const: 0x440
-  __TEXT.__gcc_except_tab: 0x9050
+  __TEXT.__gcc_except_tab: 0x92d4
   __TEXT.__cstring: 0x7cac
   __TEXT.__oslogstring: 0xef2
-  __TEXT.__unwind_info: 0x2c98
-  __TEXT.__objc_classname: 0x467
-  __TEXT.__objc_methname: 0x6744
+  __TEXT.__unwind_info: 0x2ce0
+  __TEXT.__objc_classname: 0x468
+  __TEXT.__objc_methname: 0x69ae
   __TEXT.__objc_methtype: 0x1002
-  __TEXT.__objc_stubs: 0x5320
+  __TEXT.__objc_stubs: 0x55c0
   __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0xdf68
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_selrefs: 0x1d00
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x6190
   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0xe08
   __AUTH_CONST.__cfstring: 0xd960
-  __AUTH_CONST.__objc_const: 0x53d0
+  __AUTH_CONST.__objc_const: 0x5478
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1350
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF9FB7CF-8469-36EC-9669-B4548197AC06
-  Functions: 1573
-  Symbols:   5973
-  CStrings:  5355
+  UUID: ACECFBB1-5338-3CA5-801E-AE6EC35A90AE
+  Functions: 1593
+  Symbols:   6042
+  CStrings:  5384
 
Symbols:
+ -[PKCloudResolveContext enumerator]
+ -[PKCloudResolveContext icloudPrinter]
+ -[PKCloudResolveContext queue]
+ -[PKCloudResolveContext setEnumerator:]
+ -[PKCloudResolveContext setIcloudPrinter:]
+ -[PKCloudResolveContext setQueue:]
+ -[PKCloudResolveContext setStartTime:]
+ -[PKCloudResolveContext setTag:]
+ -[PKCloudResolveContext setTimeout:]
+ -[PKCloudResolveContext startTime]
+ -[PKCloudResolveContext tag]
+ -[PKCloudResolveContext timeout]
+ -[PKPrinter iCloudPrinter]
+ -[PKPrinter job_request]
+ -[PKPrinter printerDescriptionTime]
+ -[PKPrinter printerDescription]
+ -[PKPrinter setICloudPrinter:]
+ -[PKPrinter setJob_request:]
+ -[PKPrinter setPrinterDescription:]
+ -[PKPrinter setPrinterDescriptionTime:]
+ GCC_except_table120
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table98
+ __OBJC_$_PROP_LIST_PKCloudResolveContext
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke.336
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.337
+ ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.418
+ ___block_literal_global.399
+ ___block_literal_global.402
+ ___block_literal_global.410
+ _objc_msgSend$accessState
+ _objc_msgSend$enumerator
+ _objc_msgSend$iCloudPrinter
+ _objc_msgSend$icloudPrinter
+ _objc_msgSend$job_request
+ _objc_msgSend$printerDescription
+ _objc_msgSend$printerDescriptionTime
+ _objc_msgSend$queue
+ _objc_msgSend$setEnumerator:
+ _objc_msgSend$setICloudPrinter:
+ _objc_msgSend$setIcloudPrinter:
+ _objc_msgSend$setJob_request:
+ _objc_msgSend$setPrinterDescription:
+ _objc_msgSend$setPrinterDescriptionTime:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setStartTime:
+ _objc_msgSend$setTag:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$startTime
+ _objc_msgSend$tag
+ _objc_msgSend$timeout
- GCC_except_table104
- GCC_except_table106
- GCC_except_table134
- GCC_except_table137
- GCC_except_table138
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke.320
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.321
- ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.376
- ___block_literal_global.357
CStrings:
+ "T@\"NSDate\",&,V_printerDescriptionTime"
+ "T@\"NSDate\",&,V_startTime"
+ "T@\"NSEnumerator\",&,V_enumerator"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSString\",&,V_tag"
+ "T@\"PKPrintJobRequest\",&,V_job_request"
+ "T@\"PKPrinterBrowseInfo\",R,V_browseInfo"
+ "T@\"PKPrinterDescription\",&,V_printerDescription"
+ "T@\"PKiCloudPrinter\",&,V_iCloudPrinter"
+ "T@\"PKiCloudPrinter\",&,V_icloudPrinter"
+ "Td,V_timeout"
+ "enumerator"
+ "iCloudPrinter"
+ "icloudPrinter"
+ "job_request"
+ "printerDescription"
+ "printerDescriptionTime"
+ "queue"
+ "setEnumerator:"
+ "setICloudPrinter:"
+ "setIcloudPrinter:"
+ "setJob_request:"
+ "setPrinterDescription:"
+ "setPrinterDescriptionTime:"
+ "setQueue:"
+ "setStartTime:"
+ "setTag:"
+ "setTimeout:"
+ "tag"
+ "timeout"
- "T@\"PKPrinterBrowseInfo\",R"

```
