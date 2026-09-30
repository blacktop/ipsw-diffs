## libAppletTranslationLibrary.dylib

> `/usr/lib/libAppletTranslationLibrary.dylib`

```diff

-55.1.0.0.0
-  __TEXT.__text: 0xb16a8
+55.2.0.0.0
+  __TEXT.__text: 0xb279c
   __TEXT.__auth_stubs: 0x14d0
-  __TEXT.__objc_methlist: 0x24e8
+  __TEXT.__objc_methlist: 0x2528
   __TEXT.__const: 0x3444
-  __TEXT.__cstring: 0x89c5
-  __TEXT.__oslogstring: 0x57f7
+  __TEXT.__cstring: 0x89f5
+  __TEXT.__oslogstring: 0x5837
   __TEXT.__gcc_except_tab: 0x1a04
   __TEXT.__swift5_typeref: 0x907
   __TEXT.__constg_swiftt: 0x84c

   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__ustring: 0xa
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1718
+  __TEXT.__unwind_info: 0x1730
   __TEXT.__eh_frame: 0x1944
   __TEXT.__objc_classname: 0x413
-  __TEXT.__objc_methname: 0x4dd9
+  __TEXT.__objc_methname: 0x4eb6
   __TEXT.__objc_methtype: 0xf45
-  __TEXT.__objc_stubs: 0x4b60
+  __TEXT.__objc_stubs: 0x4c20
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0xb88
+  __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c0
+  __DATA_CONST.__objc_selrefs: 0x14f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x1b10
   __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__auth_ptr: 0x340
+  __AUTH_CONST.__auth_ptr: 0x330
   __AUTH_CONST.__const: 0x2858
-  __AUTH_CONST.__cfstring: 0x97c0
+  __AUTH_CONST.__cfstring: 0x9840
   __AUTH_CONST.__objc_const: 0x37a8
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0x420

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1867
-  Symbols:   4197
-  CStrings:  3115
+  Functions: 1872
+  Symbols:   4213
+  CStrings:  3127
 
Symbols:
+ +[KramerMappings calculateTopupTransactionSN:withDifferentiator:withIpeId:]
+ +[KramerMappings convertTopupsToHistory:]
+ +[KramerMappings getMergedHistory:withDirectory:withIpeList:]
+ +[KramerMappings mergeTransitAndTopupHistory:withTopupHistory:]
+ +[KramerVCReader getTopupCredits:withIpeId:]
+ _objc_msgSend$calculateTopupTransactionSN:withDifferentiator:withIpeId:
+ _objc_msgSend$convertTopupsToHistory:
+ _objc_msgSend$getMergedHistory:withDirectory:withIpeList:
+ _objc_msgSend$getTopupCredits:withIpeId:
+ _objc_msgSend$mergeTransitAndTopupHistory:withTopupHistory:
+ _objc_msgSend$removeObjectsInArray:
CStrings:
+ "030000"
+ "Merged history: %@"
+ "Unexpected Enter / Exit Indicatorcode: %u (expected for topup transactions)"
+ "VGIpePointer"
+ "VGTopupCredit"
+ "VGTopups"
+ "calculateTopupTransactionSN:withDifferentiator:withIpeId:"
+ "convertTopupsToHistory:"
+ "getMergedHistory:withDirectory:withIpeList:"
+ "getTopupCredits:withIpeId:"
+ "historyEntries %@"
+ "mergeTransitAndTopupHistory:withTopupHistory:"
+ "removeObjectsInArray:"
- "Unexpected Enter / Exit Indicatorcode: %u"

```
