## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService`

```diff

-1965.3.7.0.0
-  __TEXT.__text: 0x243c
-  __TEXT.__auth_stubs: 0x430
+1965.4.2.0.0
+  __TEXT.__text: 0x2430
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x364
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x4b8
+  __TEXT.__gcc_except_tab: 0x4b0
   __TEXT.__objc_methname: 0x47b
-  __TEXT.__cstring: 0x34a
+  __TEXT.__cstring: 0x47d
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0x42f
   __TEXT.__oslogstring: 0x25
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x228
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B1C0AA1-D576-37E2-860F-F952FEEC7E3D
+  UUID: 237B2ABC-E906-3B9F-8741-29EFE5E100DA
   Functions: 61
-  Symbols:   289
-  CStrings:  154
+  Symbols:   286
+  CStrings:  155
 
Symbols:
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ _objc_release_x22
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[CGPDFPageImpl initWithCGPDFPage:requestQueue:] : 200 -> 196
~ -[CGPDFPageImpl getIdentifier:] : 176 -> 184
~ -[CGPDFPageImpl getRotation:] : 176 -> 184
~ ___29-[CGPDFPageImpl getRotation:]_block_invoke : 244 -> 236
~ ___39-[CGPDFPageImpl getBoxRect:completion:]_block_invoke : 304 -> 296
~ -[CGPDFPageImpl drawWithBox:size:colorSpace:options:completion:] : 316 -> 296
~ -[CGPDFPageImpl getPageText:] : 176 -> 184
~ ___29-[CGPDFPageImpl getPageText:]_block_invoke : 284 -> 276
~ -[CGPDFServiceListener initWithListener:] : 128 -> 120
~ -[CGPDFServiceListener initForXPCService] : 76 -> 80
~ -[CGPDFServiceListener initForLoopback] : 76 -> 80
~ -[CGPDFServiceListener run] : 100 -> 108
~ -[CGPDFServiceListener listener:shouldAcceptNewConnection:] : 124 -> 128
~ -[CGPDFDocumentImpl initWithData:requestQueue:] : 408 -> 396
~ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE6resizeEmRU8__strongKS2_ : 136 -> 140
~ -[CGPDFDocumentImpl getPageAtIndex:] : 212 -> 244
~ -[CGPDFDocumentImpl getInfo:] : 176 -> 184
~ ___29-[CGPDFDocumentImpl getInfo:]_block_invoke : 260 -> 252
~ -[CGPDFDocumentImpl getVersion:] : 176 -> 184
~ ___32-[CGPDFDocumentImpl getVersion:]_block_invoke : 252 -> 244
~ -[CGPDFDocumentImpl getIsUnlocked:] : 176 -> 184
~ ___35-[CGPDFDocumentImpl getIsUnlocked:]_block_invoke : 248 -> 240
~ -[CGPDFDocumentImpl getIsEncrypted:] : 176 -> 184
~ ___36-[CGPDFDocumentImpl getIsEncrypted:]_block_invoke : 248 -> 240
~ -[CGPDFDocumentImpl getPageCount:] : 176 -> 184
~ ___34-[CGPDFDocumentImpl getPageCount:]_block_invoke : 248 -> 240
~ ___47-[CGPDFDocumentImpl getPageAtIndex:completion:]_block_invoke : 288 -> 284
~ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE8__appendEmRU8__strongKS2_ : 296 -> 292
~ -[CGPDFService newPDFDocumentWithData:withReply:] : 232 -> 224
~ ___49-[CGPDFService newPDFDocumentWithData:withReply:]_block_invoke : 296 -> 288
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugCCGc1W6KBohgN7srzeLbMFrlwQ_utZ79Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
