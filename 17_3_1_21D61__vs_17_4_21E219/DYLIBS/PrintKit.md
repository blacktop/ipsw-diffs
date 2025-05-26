## PrintKit

> `/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit`

```diff

-288.3.0.0.0
-  __TEXT.__text: 0x3bdcc
+288.7.0.0.0
+  __TEXT.__text: 0x3c0a4
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x2170
-  __TEXT.__const: 0x3c8
-  __TEXT.__gcc_except_tab: 0x6af0
+  __TEXT.__objc_methlist: 0x2190
+  __TEXT.__const: 0x3c0
+  __TEXT.__gcc_except_tab: 0x6b4c
   __TEXT.__cstring: 0x687e
-  __TEXT.__oslogstring: 0xab1
-  __TEXT.__unwind_info: 0x2334
+  __TEXT.__oslogstring: 0xab3
+  __TEXT.__unwind_info: 0x2360
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x28a
-  __TEXT.__objc_methname: 0x5275
+  __TEXT.__objc_methname: 0x5305
   __TEXT.__objc_methtype: 0xdc7
-  __TEXT.__objc_stubs: 0x44c0
+  __TEXT.__objc_stubs: 0x44e0
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xc728
+  __DATA_CONST.__const: 0xc750
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2d68
-  __DATA_CONST.__objc_selrefs: 0x16b8
+  __DATA_CONST.__objc_const: 0x2d98
+  __DATA_CONST.__objc_selrefs: 0x16d8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x57c8
   __AUTH_CONST.__objc_const: 0xcf0
   __AUTH_CONST.__const: 0x8e0

   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0x8c0
   __AUTH.__data: 0x38
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0xc0
-  __DATA.__objc_ivar: 0x270
-  __DATA.__data: 0x2ae0
+  __DATA.__objc_ivar: 0x274
+  __DATA.__data: 0x2ae8
   __DATA.__bss: 0x140
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1260
-  Symbols:   4787
-  CStrings:  3025
+  Functions: 1266
+  Symbols:   4804
+  CStrings:  3032
 
Symbols:
+ +[PKPrinterDescription attributesRequiredForPKPaperList]
+ -[PKPrinterDescription(PrintertoolSideConstruction) replacePaperList:]
+ -[PKPrinterDescription(PrintertoolSideConstruction) wantsComprehensivePaperList]
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table110
+ _OBJC_IVAR_$_PKPrinterDescription._wantsComprehensivePaperList
+ __Z28liteFigureOutDriverSetupInfoP16XDriverSetupInfoP13lite_driver_sP12NSDictionaryIP8NSStringS5_E
+ __ZN17Printd_Parameters19keyMediaColDatabaseE
+ __ZNK21Printd_Job_Parameters13getFinishingsEv
+ ___34-[PKPrinter withDescriptionAsync:]_block_invoke_2
+ ___block_descriptor_40_ea8_32s_e54_v24?0"PKPrinterDescription"8"PKPrinterBrowseInfo"16ls32l8
+ __unnamed_array_storage.429
+ __unnamed_array_storage.445
+ __unnamed_array_storage.467
+ _objc_msgSend$addTimeInterval:
- __OBJC_$_PROP_LIST_PKPrinterDescription
- __unnamed_array_storage.427
- __unnamed_array_storage.443
- __unnamed_array_storage.465
- __unnamed_array_storage.638
CStrings:
+ "Force updating paper list: %@"
+ "T@\"NSString\",?,R,C"
+ "_wantsComprehensivePaperList"
+ "addTimeInterval:"
+ "attributesRequiredForPKPaperList"
+ "replacePaperList:"
+ "wantsComprehensivePaperList"
+ "would like lazily fetched paperlist"
- "Missing media-col-supported, haven't fetched media-col-database"

```
