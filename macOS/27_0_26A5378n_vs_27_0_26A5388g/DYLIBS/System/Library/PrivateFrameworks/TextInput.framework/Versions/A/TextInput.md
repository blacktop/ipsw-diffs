## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3559.0.0.0.0
-  __TEXT.__text: 0x84e48
-  __TEXT.__objc_methlist: 0xb560
+3562.0.0.0.0
+  __TEXT.__text: 0x84fb0
+  __TEXT.__objc_methlist: 0xb5a8
   __TEXT.__dlopen_cstrs: 0x1ea
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x490b0
+  __TEXT.__cstring: 0x491d6
   __TEXT.__ustring: 0xc8bc8
   __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x1ef0
+  __TEXT.__unwind_info: 0x1f00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1560
+  __DATA_CONST.__const: 0x15b0
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55b0
+  __DATA_CONST.__objc_selrefs: 0x55d8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0x101920
+  __DATA_CONST.__objc_arraydata: 0x101948
   __DATA_CONST.__got: 0x608
   __AUTH_CONST.__const: 0x1f50
-  __AUTH_CONST.__cfstring: 0x255920
-  __AUTH_CONST.__objc_const: 0x11ad0
+  __AUTH_CONST.__cfstring: 0x255ac0
+  __AUTH_CONST.__objc_const: 0x11b18
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x5040
+  __AUTH_CONST.__objc_arrayobj: 0x5058
   __AUTH_CONST.__objc_dictobj: 0xf190
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_doubleobj: 0xc0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4006
-  Symbols:   9223
-  CStrings:  76753
+  Functions: 4011
+  Symbols:   9240
+  CStrings:  76766
 
Symbols:
+ -[TIKeyboardState canInsertGenmoji]
+ -[TIKeyboardState setCanInsertGenmoji:]
+ -[TIKeyboardState setSupportsGenmojiCreation:]
+ -[TIKeyboardState supportsGenmojiCreation]
+ -[TIPreferencesController alwaysShowOnscreenKeyboardEnabled]
+ _TIAssistiveTouchMouseAlwaysShowSoftwareKeyboardPreference
+ _TIKeyboardOutputInfoTypeCellularIMEI1Str
+ _TIKeyboardOutputInfoTypeCellularIMEI2Str
+ _TIKeyboardOutputInfoTypeCellularNALStr
+ _TIKeyboardSecureCandidateCellularIMEI1Str
+ _TIKeyboardSecureCandidateCellularIMEI2Str
+ _TIKeyboardSecureCandidateCellularNALStr
+ _TITextContentTypeCellularIMEI1
+ _TITextContentTypeCellularIMEI2
+ _TITextContentTypeCellularNAL
+ _objc_msgSend$canInsertGenmoji
+ _objc_msgSend$supportsGenmojiCreation
CStrings:
+ ".notification"
+ "; canInsertGenmoji = %s"
+ "; supportsGenmojiCreation = %s"
+ "AssistiveTouchMouseAlwaysShowSoftwareKeyboard"
+ "AutofillCellularIMEI1"
+ "AutofillCellularIMEI2"
+ "AutofillCellularNAL"
+ "Insert Cellular IMEI1"
+ "Insert Cellular IMEI2"
+ "Insert Cellular NAL"
+ "com.apple.Accessibility"
+ "esim-imei1"
+ "esim-imei2"
+ "esim-nal"
- "ar_"
```
