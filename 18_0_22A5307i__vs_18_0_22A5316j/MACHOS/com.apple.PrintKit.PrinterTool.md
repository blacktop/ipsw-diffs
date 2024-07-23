## com.apple.PrintKit.PrinterTool

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool`

```diff

-304.0.0.0.0
-  __TEXT.__text: 0x5e658
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x6800
-  __TEXT.__objc_methlist: 0x25f8
+305.1.0.0.0
+  __TEXT.__text: 0x5eb28
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_stubs: 0x6860
+  __TEXT.__objc_methlist: 0x2624
   __TEXT.__const: 0xa18
-  __TEXT.__gcc_except_tab: 0xb708
-  __TEXT.__oslogstring: 0x417d
-  __TEXT.__cstring: 0x94a0
-  __TEXT.__objc_methname: 0x69c8
-  __TEXT.__objc_classname: 0x4f2
-  __TEXT.__objc_methtype: 0x1f3a
+  __TEXT.__gcc_except_tab: 0xb75c
+  __TEXT.__oslogstring: 0x4199
+  __TEXT.__cstring: 0x94d1
+  __TEXT.__objc_methname: 0x6a1a
+  __TEXT.__objc_classname: 0x504
+  __TEXT.__objc_methtype: 0x1f5e
   __TEXT.__ustring: 0x66
-  __TEXT.__unwind_info: 0x2e48
-  __DATA_CONST.__auth_got: 0xc38
+  __TEXT.__unwind_info: 0x2e60
+  __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x578
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xed30
-  __DATA_CONST.__cfstring: 0xed00
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0xed58
+  __DATA_CONST.__cfstring: 0xed20
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x5ed0
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0xfc0
-  __DATA.__objc_const: 0x6740
-  __DATA.__objc_selrefs: 0x1d08
-  __DATA.__objc_ivar: 0x3dc
-  __DATA.__objc_data: 0xf50
+  __DATA.__objc_const: 0x6830
+  __DATA.__objc_selrefs: 0x1d18
+  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x3180
   __DATA.__bss: 0x188
   __DATA.__common: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1621
-  Symbols:   928
-  CStrings:  4227
+  Functions: 1626
+  Symbols:   931
+  CStrings:  4236
 
Symbols:
+ _CFGetRetainCount
+ _OBJC_CLASS_$_PKSecTrustWrapper
+ _OBJC_METACLASS_$_PKSecTrustWrapper
+ __Z21PKUserAllowsCertTrustP17PKSecTrustWrapperP8NSStringS2_
- __Z21PKUserAllowsCertTrustP10__SecTrustP8NSStringS2_
CStrings:
+ "\x02$\x13\x17"
+ "<%!@(MISSING)@%!p(MISSING)> { unretained trust %!p(MISSING) (%!d(MISSING)) }"
+ "@24@0:8^{__SecTrust=}16"
+ "B24@?0@\"device_http_t\"8@\"PKSecTrustWrapper\"16"
+ "PKSecTrustWrapper"
+ "T^{__SecTrust=},R,V_trustRef"
+ "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on account id missing error (%!@(MISSING))."
+ "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on authorization error (%!@(MISSING))."
+ "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on busy error (%!@(MISSING))."
+ "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on error response:%!d(MISSING) (%!@(MISSING))."
+ "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on lost connection error (%!@(MISSING))"
+ "^{__SecTrust=}"
+ "^{__SecTrust=}16@0:8"
+ "_taskQueue"
+ "_trustRef"
+ "finishedWriting0"
+ "initWithTrust:"
+ "trustRef"
+ "v24@?0@\"PKSecTrustWrapper\"8@?<v@?B>16"
+ "writeDocumentData0: failed after writing %!l(MISSING)d uncompressed"
+ "writeDocumentData0:length:"
+ "writeDocumentDataBlocking:length:"
- "\x02#\x13\x17"
- "B24@0:8^{__SecTrust=}16"
- "B24@?0@\"device_http_t\"8^{__SecTrust=}16"
- "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on account id missing error."
- "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on authorization error."
- "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on busy error."
- "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on error response."
- "[Job %!d(MISSING)][%!d(MISSING)] %!s(MISSING) job on lost connection error."
- "v24@?0^{__SecTrust=}8@?<v@?B>16"
- "writeDocumentData:"
- "writeDocumentData: failed after writing %!l(MISSING)d uncompressed"
- "writeDocumentData:length:"
- "writeIPPDocumentPayload:"

```
