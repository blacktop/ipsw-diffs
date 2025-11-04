## HomeSharing

> `/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing`

```diff

-4025.200.15.0.0
-  __TEXT.__text: 0x6a100
+4025.300.5.0.0
+  __TEXT.__text: 0x6a0ec
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__objc_methlist: 0x201c
   __TEXT.__const: 0xf62c
-  __TEXT.__gcc_except_tab: 0x2c4
+  __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__cstring: 0x2942
   __TEXT.__oslogstring: 0x12d1
   __TEXT.__unwind_info: 0x9e8
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x530
-  __TEXT.__objc_methname: 0x5a76
-  __TEXT.__objc_methtype: 0xbf5
-  __TEXT.__objc_stubs: 0x3fa0
+  __TEXT.__objc_methname: 0x5a61
+  __TEXT.__objc_methtype: 0xc03
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0xdd8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1490
+  __DATA_CONST.__objc_selrefs: 0x1488
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x480

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A795A66D-528E-36EB-9E68-A9AD29AC2B2E
+  UUID: 4084CB3E-503D-334F-B5FA-6C4DFA7A4BAA
   Functions: 895
-  Symbols:   2936
+  Symbols:   2935
   CStrings:  2013
 
Symbols:
+ -[HSFairPlayInfo _hexStringForData:length:]
+ ___Block_byref_object_copy_.1718
+ ___Block_byref_object_dispose_.1719
+ ___block_literal_global.2106
+ ___block_literal_global.2220
+ _objc_msgSend$_hexStringForData:length:
- -[HSFairPlayInfo _hexStringForData:]
- ___Block_byref_object_copy_.1717
- ___Block_byref_object_dispose_.1718
- ___block_literal_global.2105
- ___block_literal_global.2219
- _objc_msgSend$_hexStringForData:
- _objc_msgSend$dataWithBytesNoCopy:length:
Functions:
~ -[HSFairPlayInfo _hexStringForData:] -> -[HSFairPlayInfo _hexStringForData:length:] : 192 -> 140
~ -[HSFairPlayInfo securityInfoForURL:] : 804 -> 788
~ -[HSFairPlayInfo continueNegotationWithSAPVersion:data:isComplete:] : 676 -> 700
~ -[HSFairPlayInfo beginNegotiationWithSAPVersion:] : 584 -> 608
CStrings:
+ "@28@0:8*16I24"
+ "_hexStringForData:length:"
- "_hexStringForData:"
- "dataWithBytesNoCopy:length:"

```
