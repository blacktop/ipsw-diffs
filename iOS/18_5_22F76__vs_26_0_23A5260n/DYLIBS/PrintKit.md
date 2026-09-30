## PrintKit

> `/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit`

```diff

-306.3.0.0.0
-  __TEXT.__text: 0x481e0
+318.0.0.0.0
+  __TEXT.__text: 0x48570
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x3020
-  __TEXT.__const: 0x430
-  __TEXT.__gcc_except_tab: 0x8ff0
-  __TEXT.__cstring: 0x7c9b
-  __TEXT.__oslogstring: 0xf03
-  __TEXT.__unwind_info: 0x2c78
+  __TEXT.__objc_methlist: 0x303c
+  __TEXT.__const: 0x440
+  __TEXT.__gcc_except_tab: 0x9050
+  __TEXT.__cstring: 0x7cac
+  __TEXT.__oslogstring: 0xef2
+  __TEXT.__unwind_info: 0x2c90
   __TEXT.__objc_classname: 0x467
-  __TEXT.__objc_methname: 0x66ce
-  __TEXT.__objc_methtype: 0xff5
-  __TEXT.__objc_stubs: 0x52c0
+  __TEXT.__objc_methname: 0x6744
+  __TEXT.__objc_methtype: 0x1002
+  __TEXT.__objc_stubs: 0x5320
   __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0xdf50
+  __DATA_CONST.__const: 0xdf68
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c48
+  __DATA_CONST.__objc_selrefs: 0x1c68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x6190
   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0xe08
-  __AUTH_CONST.__cfstring: 0xd940
-  __AUTH_CONST.__objc_const: 0x53b8
+  __AUTH_CONST.__cfstring: 0xd960
+  __AUTH_CONST.__objc_const: 0x53d0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1350
   __AUTH_CONST.__objc_arrayobj: 0x228
+  __AUTH.__objc_data: 0xf50
+  __AUTH.__data: 0x38
   __DATA.__objc_ivar: 0x324
   __DATA.__data: 0x2f34
   __DATA.__bss: 0x174
-  __DATA_DIRTY.__objc_data: 0xf50
-  __DATA_DIRTY.__data: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CA3C11D-4DD1-3445-8A22-5E6DBD0B6482
-  Functions: 1568
-  Symbols:   5957
-  CStrings:  5350
+  UUID: FB46B981-0A68-3289-AF3E-97DE815CB64F
+  Functions: 1573
+  Symbols:   5973
+  CStrings:  5355
 
Symbols:
+ +[PKDefaults updateiCloudPrinterCustomLocation:customLocation:]
+ +[PKDefaults updateiCloudPrinterCustomName:customName:]
+ -[PKPrinter updateiCloudPrinterInfo]
+ -[PKPrinterTool_Client updateiCloudPrinter:withInfo:forInfoKey:]
+ -[PKiCloudPrinter customLocation]
+ -[PKiCloudPrinter customName]
+ GCC_except_table101
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table97
+ _PKPrinterCustomLocationKey
+ _PKPrinterCustomNameKey
+ _PrinterTooliCloudPrintersChangedNotification
+ __ZL12writeStringsR11IPPIOWriterP18PK_ipp_attribute_tm
+ __ZN16XDriverSetupInfoD2Ev
+ ___36-[PKPrinter updateiCloudPrinterInfo]_block_invoke
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke.320
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.321
+ ___53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.129
+ ___57-[PKPrinter pollForPrinterStatusQueue:completionHandler:]_block_invoke.151
+ ___Block_byref_object_copy_.127
+ ___Block_byref_object_dispose_.128
+ ____ZL12writeStringsR11IPPIOWriterP18PK_ipp_attribute_tm_block_invoke
+ ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.376
+ ___block_descriptor_40_ea8_32bs_e29_v16?0"PKPrinterBrowseInfo"8ls32l8
+ ___block_descriptor_56_ea8_32s_e31_v32?0Q8"PK_ipp_value_t"16^B24ls32l8
+ ___block_literal_global.103
+ ___block_literal_global.24
+ ___block_literal_global.357
+ ___block_literal_global.56
+ ___block_literal_global.64
+ ___block_literal_global.66
+ _objc_msgSend$customLocation
+ _objc_msgSend$customName
+ _objc_msgSend$updateiCloudPrinter:withInfo:forInfoKey:
+ _objc_msgSend$updateiCloudPrinterCustomLocation:customLocation:
+ _objc_msgSend$updateiCloudPrinterCustomName:customName:
+ _objc_msgSend$updateiCloudPrinterInfo
+ _objc_msgSend$updateiCloudPrinterInfo:withNewInfo:forInfoKey:
- -[PKPrinter _updateiCloudPrinterInfo]
- -[PKPrinterTool_Client updateiCloudPrinterDisplayName:newDisplayName:]
- -[PKPrinterTool_Client updateiCloudPrinterLocation:location:]
- GCC_except_table119
- GCC_except_table120
- GCC_except_table145
- GCC_except_table147
- GCC_except_table98
- __ZN16XDriverSetupInfoD1Ev
- ___37-[PKPrinter _updateiCloudPrinterInfo]_block_invoke
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke.319
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.320
- ___53-[PKPrinter _checkAvailable:queue:completionHandler:]_block_invoke.128
- ___57-[PKPrinter pollForPrinterStatusQueue:completionHandler:]_block_invoke.150
- ___Block_byref_object_copy_.384
- ___Block_byref_object_dispose_.385
- ____ZL12writeStringsR11IPPIOWriterP18PK_ipp_attribute_t_block_invoke
- ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.375
- ___block_descriptor_48_ea8_32s40bs_e29_v16?0"PKPrinterBrowseInfo"8ls40l8s32l8
- ___block_descriptor_56_ea8_32s_e26_v16?0?<v?"PKPrinter">8ls32l8
- ___block_literal_global.107
- ___block_literal_global.359
- ___block_literal_global.367
- ___block_literal_global.60
- ___block_literal_global.70
- ___block_literal_global.72
- _objc_msgSend$_updateiCloudPrinterInfo
- _objc_msgSend$updateiCloudPrinterDisplayName:newDisplayName:
- _objc_msgSend$updateiCloudPrinterLocation:location:
- _objc_msgSend$updateiCloudPrinterLocation:newLocation:
CStrings:
+ "%s: truncating \"%@\" to %u octets"
+ "Invalid Bonjour service: %{public}@"
+ "com.apple.printkit.printer-custom-location"
+ "com.apple.printkit.printer-custom-name"
+ "customLocation"
+ "customName"
+ "self.txtRecord != nil"
+ "updateiCloudPrinter:withInfo:forInfoKey:"
+ "updateiCloudPrinterCustomLocation:customLocation:"
+ "updateiCloudPrinterCustomName:customName:"
+ "updateiCloudPrinterInfo"
+ "updateiCloudPrinterInfo:withNewInfo:forInfoKey:"
+ "v40@0:8@\"NSDictionary\"16@\"NSObject\"24@\"NSString\"32"
+ "writeStrings_block_invoke"
- "%@ resolved as %@"
- "+[PKPrinter printerWithName:discoveryTimeout:]"
- "Invalid Bonjour service: %@{public}"
- "PRINTERTOOL_ICLOUDPRINTERS_CHANGED_NOTIFICATION"
- "_txtRecord != nil"
- "_updateiCloudPrinterInfo"
- "existing info %@ resolved as %@"
- "updateiCloudPrinterDisplayName:newDisplayName:"
- "updateiCloudPrinterLocation:newLocation:"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"

```
