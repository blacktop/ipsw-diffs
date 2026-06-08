## CIBarcode

> `/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode`

```diff

-1592.120.2.0.0
-  __TEXT.__text: 0xf33c
-  __TEXT.__auth_stubs: 0x440
+1653.0.0.120.2
+  __TEXT.__text: 0x11d94
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x560
-  __TEXT.__cstring: 0x20ba
-  __TEXT.__const: 0x5fb0
+  __TEXT.__objc_methlist: 0x700
+  __TEXT.__cstring: 0x28f7
+  __TEXT.__const: 0x60a0
   __TEXT.__oslogstring: 0x77a
-  __TEXT.__objc_classname: 0xb7
+  __TEXT.__objc_classname: 0x119
   __TEXT.__objc_methname: 0xd7c
   __TEXT.__objc_methtype: 0x1ba
-  __TEXT.__gcc_except_tab: 0x408
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4b0
-  __DATA_CONST.__cfstring: 0x1320
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__const: 0x7f0
+  __DATA_CONST.__cfstring: 0x16a0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x240
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0xa48
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0xe48
   __DATA.__objc_selrefs: 0x460
-  __DATA.__objc_ivar: 0x78
-  __DATA.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x18
   __DATA.__bss: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28A5DA3C-8624-3D63-8FD6-623E86C1E48D
-  Functions: 291
-  Symbols:   131
-  CStrings:  607
+  UUID: B0BB7AED-EBB9-3025-92B1-6147A5BE4CA8
+  Functions: 331
+  Symbols:   136
+  CStrings:  754
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retain_x27
CStrings:
+ "0123456789-$:/.+ABCD"
+ "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%*"
+ "27"
+ "CICodabarBarcodeGenerator"
+ "CICodabarBarcodeGenerator could not generate an image"
+ "CICodabarBarcodeGenerator filter requires NSData for inputMessage"
+ "CICode39BarcodeGenerator"
+ "CICode39BarcodeGenerator could not generate an image"
+ "CICode39BarcodeGenerator filter requires NSData for inputMessage"
+ "CIEAN13BarcodeGenerator"
+ "CIEAN13BarcodeGenerator could not generate an image"
+ "CIEAN13BarcodeGenerator filter requires NSData for inputMessage"
+ "CIInterleaved2of5BarcodeGenerator"
+ "CIInterleaved2of5BarcodeGenerator could not generate an image"
+ "CIInterleaved2of5BarcodeGenerator filter requires NSData for inputMessage"
+ "Codabar barcode must end with A, B, C, or D."
+ "Codabar barcode must have at least a start and stop character."
+ "Codabar barcode must start with A, B, C, or D."
+ "EAN-13 barcode must contain exactly 12 or 13 digits."
+ "Invalid character '%c' at position %zu. Codabar supports 0-9, -$:/.+, and A-D for start/stop."
+ "Invalid character '%c' at position %zu. Code39 supports 0-9, A-Z, and -. $/+%%"
+ "Invalid check digit. Expected %d but got %d."
+ "LGGGLL"
+ "LGGLGL"
+ "LGGLLG"
+ "LGLGGL"
+ "LGLGLG"
+ "LGLLGG"
+ "LLGGGL"
+ "LLGGLG"
+ "LLGLGG"
+ "LLLLLL"
+ "The message is too long for a Codabar barcode."
+ "The message is too long for a Code39 barcode."
+ "The message is too long for an Interleaved 2 of 5 barcode."
+ "The message must contain only digits (0-9)."
+ "com.apple.codabar"
+ "com.apple.code39"
+ "com.apple.ean13"
+ "com.apple.i2of5"
+ "nnnnnnwww"
+ "nnnnnww"
+ "nnnnnwwnw"
+ "nnnnwnnww"
+ "nnnnwnwwn"
+ "nnnnwwn"
+ "nnnnwwnnw"
+ "nnnnwwwnn"
+ "nnnwnnw"
+ "nnnwnnwnw"
+ "nnnwnwnwn"
+ "nnnwnww"
+ "nnnww"
+ "nnnwwnn"
+ "nnnwwnnnw"
+ "nnnwwnwnn"
+ "nnnwwwn"
+ "nnwnnnnww"
+ "nnwnnnwwn"
+ "nnwnnwn"
+ "nnwnnwnnw"
+ "nnwnnwwnn"
+ "nnwnw"
+ "nnwnwnnwn"
+ "nnwnwwnnn"
+ "nnwwn"
+ "nnwwnnn"
+ "nnwwnnnnw"
+ "nnwwnnwnn"
+ "nnwwnwn"
+ "nnwwwnnnn"
+ "nwnnnnw"
+ "nwnnnnwnn"
+ "nwnnnwnwn"
+ "nwnnw"
+ "nwnnwnn"
+ "nwnnwnnnw"
+ "nwnnwnwnn"
+ "nwnwn"
+ "nwnwnnnwn"
+ "nwnwnnw"
+ "nwnwnwn"
+ "nwnwnwnnn"
+ "nwwnn"
+ "nwwnnnn"
+ "nwwnnnnnn"
+ "nwwnnnwnn"
+ "nwwnwnnnn"
+ "v16@?0i8B12"
+ "wnnnnnnww"
+ "wnnnnnwwn"
+ "wnnnnwn"
+ "wnnnnwnnw"
+ "wnnnnwwnn"
+ "wnnnw"
+ "wnnnwnnwn"
+ "wnnnwwnnn"
+ "wnnwn"
+ "wnnwnnn"
+ "wnnwnnnnw"
+ "wnnwnnwnn"
+ "wnnwnwn"
+ "wnnwwnnnn"
+ "wnwnn"
+ "wnwnnnnwn"
+ "wnwnnnw"
+ "wnwnnwnnn"
+ "wnwnwnn"
+ "wnwwnnnnn"
+ "wwnnn"
+ "wwnnnnn"
+ "wwnnnnnnn"
+ "wwnnnnwnn"
+ "wwnnwnnnn"
+ "wwwnnnnnn"

```
