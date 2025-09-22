## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0x3a440
+3774.300.61.2.4
+  __TEXT.__text: 0x3a5e4
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x3520
-  __TEXT.__gcc_except_tab: 0x8130
-  __TEXT.__cstring: 0x2b59
+  __TEXT.__objc_methlist: 0x3578
+  __TEXT.__gcc_except_tab: 0x8144
+  __TEXT.__cstring: 0x2ba8
   __TEXT.__ustring: 0x318
-  __TEXT.__const: 0x1546b
+  __TEXT.__const: 0x1546a
   __TEXT.__oslogstring: 0x19d2
-  __TEXT.__unwind_info: 0x2334
+  __TEXT.__unwind_info: 0x2360
   __TEXT.__objc_classname: 0xa2f
-  __TEXT.__objc_methname: 0x10960
-  __TEXT.__objc_methtype: 0x404a
-  __TEXT.__objc_stubs: 0xb440
+  __TEXT.__objc_methname: 0x10a38
+  __TEXT.__objc_methtype: 0x4058
+  __TEXT.__objc_stubs: 0xb540
   __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0x11c8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7b78
-  __DATA_CONST.__objc_selrefs: 0x35d0
+  __DATA_CONST.__objc_const: 0x7ba8
+  __DATA_CONST.__objc_selrefs: 0x3608
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__cfstring: 0x2da0
+  __AUTH_CONST.__cfstring: 0x2de0
   __AUTH_CONST.__objc_const: 0x1500
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x400

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x618
   __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_ivar: 0x444
   __DATA.__data: 0xf90
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xaf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ADDC1953-8311-35E5-8F3D-0BA0851CEE95
-  Functions: 1313
-  Symbols:   6314
-  CStrings:  3908
+  UUID: 9B7F0CF0-8D21-3810-A720-897FFC3A086D
+  Functions: 1321
+  Symbols:   6342
+  CStrings:  3921
 
Symbols:
+ -[MFBannerView _readLaterStringForDate:]
+ -[MFBannerView _updateBannerLabelTextWithReadLaterDate:]
+ -[MFHasMoreContentBannerView updateBannerWithRemainingBytes:error:]
+ -[MFMessageContentView _updateHasMoreContentBannerWithRemainingBytes:error:]
+ -[_MFPartiallyDownloadedBannerView _messageStringForBytes:isDownloading:hasError:]
+ -[_MFPartiallyDownloadedBannerView hasError]
+ -[_MFPartiallyDownloadedBannerView setHasError:]
+ -[_MFPartiallyDownloadedBannerView updateBannerWithRemainingBytes:error:]
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table223
+ GCC_except_table226
+ GCC_except_table231
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table263
+ GCC_except_table265
+ GCC_except_table338
+ GCC_except_table345
+ _OBJC_IVAR_$__MFPartiallyDownloadedBannerView._hasError
+ ___block_literal_global.1430
+ ___block_literal_global.1437
+ _objc_msgSend$_readLaterStringForDate:
+ _objc_msgSend$_updateBannerLabelTextWithReadLaterDate:
+ _objc_msgSend$_updateHasMoreContentBannerWithRemainingBytes:error:
+ _objc_msgSend$ef_isEarlierThanNow
+ _objc_msgSend$hasError
+ _objc_msgSend$setHasError:
+ _objc_msgSend$setRemainingBytes:
+ _objc_msgSend$updateBannerWithRemainingBytes:error:
- GCC_except_table208
- GCC_except_table212
- GCC_except_table216
- GCC_except_table220
- GCC_except_table225
- GCC_except_table227
- GCC_except_table232
- GCC_except_table242
- GCC_except_table244
- GCC_except_table247
- GCC_except_table250
- GCC_except_table255
- GCC_except_table259
- GCC_except_table262
- GCC_except_table264
- GCC_except_table336
- GCC_except_table344
- ___block_literal_global.1428
- ___block_literal_global.1435
CStrings:
+ "Download failed. Retry download of remaining %@"
+ "Download remaining %@"
+ "Downloading remaining %@"
+ "Mail reminded you"
+ "TB,V_hasError"
+ "_readLaterStringForDate:"
+ "_updateBannerLabelTextWithReadLaterDate:"
+ "_updateHasMoreContentBannerWithRemainingBytes:error:"
+ "ef_isEarlierThanNow"
+ "hasError"
+ "setHasError:"
+ "updateBannerWithRemainingBytes:error:"
+ "v32@0:8Q16@24"
- "BYTES_DOWNLOADING"
- "BYTES_REMAINING"

```
