## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3559.100.0.0.0
-  __TEXT.__text: 0x2221c8
+3562.0.0.0.0
+  __TEXT.__text: 0x2228b4
   __TEXT.__init_offsets: 0xc0
-  __TEXT.__objc_methlist: 0x10aa0
+  __TEXT.__objc_methlist: 0x10ae8
   __TEXT.__dlopen_cstrs: 0x781
-  __TEXT.__const: 0x2e60
-  __TEXT.__cstring: 0x1c939
-  __TEXT.__oslogstring: 0x43e8
+  __TEXT.__const: 0x2e40
+  __TEXT.__cstring: 0x1ca14
+  __TEXT.__oslogstring: 0x4479
   __TEXT.__ustring: 0x7d8
-  __TEXT.__unwind_info: 0x65f8
+  __TEXT.__unwind_info: 0x6600
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa048
+  __DATA_CONST.__objc_selrefs: 0xa078
   __DATA_CONST.__objc_superrefs: 0x728
-  __DATA_CONST.__objc_arraydata: 0x1050
-  __DATA_CONST.__got: 0x1868
-  __AUTH_CONST.__const: 0x8850
-  __AUTH_CONST.__cfstring: 0x13d60
-  __AUTH_CONST.__objc_const: 0x1a610
+  __DATA_CONST.__objc_arraydata: 0x10a0
+  __DATA_CONST.__got: 0x18b0
+  __AUTH_CONST.__const: 0x8870
+  __AUTH_CONST.__cfstring: 0x13e80
+  __AUTH_CONST.__objc_const: 0x1a6a0
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
+  __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1b00
+  __AUTH_CONST.__auth_got: 0x1af8
   __AUTH.__objc_data: 0x2080
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x12c0
+  __DATA.__objc_ivar: 0x12cc
   __DATA.__data: 0x22a8
-  __DATA.__bss: 0x1ed0
+  __DATA.__bss: 0x1ee0
   __DATA.__common: 0x408
   __DATA_DIRTY.__objc_data: 0x32f0
   __DATA_DIRTY.__data: 0xb0

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10533
-  Symbols:   21800
-  CStrings:  4076
+  Functions: 10540
+  Symbols:   21820
+  CStrings:  4086
 
Symbols:
+ -[CoreTelephonyMockObject cellularImei1]
+ -[CoreTelephonyMockObject cellularImei2]
+ -[CoreTelephonyMockObject cellularNal]
+ -[CoreTelephonyMockObject initWithCellularEid:cellularImei:cellularImei1:cellularImei2:cellularNal:]
+ -[CoreTelephonyMockObject setCellularImei1:]
+ -[CoreTelephonyMockObject setCellularImei2:]
+ -[CoreTelephonyMockObject setCellularNal:]
+ _OBJC_IVAR_$_CoreTelephonyMockObject._cellularImei1
+ _OBJC_IVAR_$_CoreTelephonyMockObject._cellularImei2
+ _OBJC_IVAR_$_CoreTelephonyMockObject._cellularNal
+ _TIKeyboardOutputInfoTypeCellularIMEI1Str
+ _TIKeyboardOutputInfoTypeCellularIMEI2Str
+ _TIKeyboardOutputInfoTypeCellularNALStr
+ _TIKeyboardSecureCandidateCellularIMEI1Str
+ _TIKeyboardSecureCandidateCellularIMEI2Str
+ _TIKeyboardSecureCandidateCellularNALStr
+ _TITextContentTypeCellularIMEI1
+ _TITextContentTypeCellularIMEI2
+ _TITextContentTypeCellularNAL
+ __ZZ61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]E25screenScrapingAllowedApps
+ __ZZ61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]E9onceToken
+ ___61-[TIKeyboardInputManagerMecabra onScreenContextForCandidates]_block_invoke
- -[CoreTelephonyMockObject initWithCellularEid:cellularImei:]
- __ZNSt3__19to_stringEd
CStrings:
+ "%s  most_probable_lexicon_for_context_and_stems returned lexicon %u that is not owned by any loaded model; skipping single-model prediction step"
+ "AUTOFILL_CELLULAR_IMEI1_TITLE"
+ "AUTOFILL_CELLULAR_IMEI2_TITLE"
+ "AUTOFILL_CELLULAR_NAL_TITLE"
+ "DELETE FROM shapes WHERE timestamp <= ?"
+ "SELECT COUNT(*) FROM shapes WHERE string_representation LIKE ?"
+ "com.alibaba.dingtalklit"
+ "com.sina.weibo"
+ "com.soulapp.cn"
+ "com.ss.iphone.ugc.Aweme"
+ "com.tencent.ww"
+ "com.xingin.discover"
+ "unified_predictions"
- "';"
- "DELETE From shapes WHERE timestamp <= "
- "SELECT COUNT(*) FROM shapes WHERE string_representation LIKE '"
```
