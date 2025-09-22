## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.0.80.0.0
-  __TEXT.__text: 0xa5364
+2422.40.19.502.1
+  __TEXT.__text: 0xa5450
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x79d4
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x15366
+  __TEXT.__cstring: 0x15381
   __TEXT.__oslogstring: 0xc570
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x1770
   __TEXT.__objc_classname: 0x71c
-  __TEXT.__objc_methname: 0x158f6
+  __TEXT.__objc_methname: 0x15911
   __TEXT.__objc_methtype: 0xfcc
-  __TEXT.__objc_stubs: 0xe960
+  __TEXT.__objc_stubs: 0xe9a0
   __DATA_CONST.__got: 0x928
   __DATA_CONST.__const: 0x2310
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4430
+  __DATA_CONST.__objc_selrefs: 0x4438
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12b80
+  __AUTH_CONST.__cfstring: 0x12be0
   __AUTH_CONST.__objc_const: 0xa710
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A05D92B8-8E4A-3A6E-80DA-1EF8C0B0031B
+  UUID: E6C6C805-A452-3ED6-B175-312A2FC86B7E
   Functions: 3020
-  Symbols:   10236
-  CStrings:  9000
+  Symbols:   10238
+  CStrings:  9007
 
Symbols:
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.563
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.564
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.473
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.526
+ _objc_msgSend$checkedDescription
+ _objc_msgSend$requireSameAssetTypeAndDownloadContent
+ _objc_msgSend$setUpdateMetricEventFieldsFromDictionary:
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.554
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.555
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.463
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.517
- _objc_msgSend$requireSameAssetTypeAndAssetId
Functions:
~ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke_2 : 920 -> 1156
CStrings:
+ "%@.%ld"
+ "checkedDescription"
+ "psusOutcome"
+ "requireSameAssetTypeAndDownloadContent"
+ "success"
- "requireSameAssetTypeAndAssetId"

```
