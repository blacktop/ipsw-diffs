## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService`

```diff

 1965.4.2.0.0
-  __TEXT.__text: 0x2430
-  __TEXT.__auth_stubs: 0x400
+  __TEXT.__text: 0x2410
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x364
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x4b0
   __TEXT.__objc_methname: 0x47b
-  __TEXT.__cstring: 0x47d
+  __TEXT.__cstring: 0x34a
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0x42f
   __TEXT.__oslogstring: 0x25
   __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6235CCFE-6F9E-3789-97FA-9EB4752C3164
+  UUID: D27F1F6A-4C14-398A-82C2-96B21F94F52F
   Functions: 61
-  Symbols:   286
-  CStrings:  155
+  Symbols:   285
+  CStrings:  154
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ -[CGPDFDocumentImpl getPageAtIndex:] : 244 -> 212
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIVugAcwFnYvr1rjfuGeyzvUblmylh3Hj1ra1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
