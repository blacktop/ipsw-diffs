## AutoFillCore

> `/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore`

```diff

-27.202.0.0.0
-  __TEXT.__text: 0xa0e0
+27.302.0.0.0
+  __TEXT.__text: 0xa164
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x384
+  __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x16c7
+  __TEXT.__cstring: 0x16da
   __TEXT.__gcc_except_tab: 0x390
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x3aa
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0x1a09
+  __TEXT.__objc_methname: 0x1a4d
   __TEXT.__objc_methtype: 0x3ae
-  __TEXT.__objc_stubs: 0x13a0
+  __TEXT.__objc_stubs: 0x13e0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x850
-  __DATA_CONST.__objc_selrefs: 0x570
+  __DATA_CONST.__objc_const: 0x860
+  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_classrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1060
+  __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__auth_got: 0x288
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd0
   __DATA.__bss: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DD2F9D5-5066-35AA-84AA-B2E7D562C487
-  Functions: 209
-  Symbols:   931
-  CStrings:  619
+  UUID: 15143823-C83D-3C46-A500-6E865DA6B5C2
+  Functions: 213
+  Symbols:   943
+  CStrings:  626
 
Symbols:
+ -[AFCredentialManager oneTimeCodeProvider]
+ -[AFSuggestionGenerationManager inputContextPredictionManager]
+ -[AFSuggestionGenerationManager laContext]
+ -[AFSuggestionGenerationManager setLaContext:]
+ GCC_except_table22
+ GCC_except_table39
+ _AFTextContentTypeCellularEID
+ _AFTextContentTypeCellularIMEI
+ ___block_literal_global.276
+ _objc_msgSend$inputContextPredictionManager
+ _objc_msgSend$oneTimeCodeProvider
- GCC_except_table11
- GCC_except_table20
- GCC_except_table37
- GCC_except_table6
- ___block_literal_global.274
CStrings:
+ "T@\"NSString\",?,R,C"
+ "esim-eid"
+ "esim-imei"
+ "inputContextPredictionManager"
+ "oneTimeCodeProvider"

```
