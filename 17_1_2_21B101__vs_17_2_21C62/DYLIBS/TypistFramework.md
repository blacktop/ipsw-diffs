## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-408.0.0.0.0
-  __TEXT.__text: 0x3be64
+413.1.0.0.0
+  __TEXT.__text: 0x3c2a8
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x2cd4
+  __TEXT.__objc_methlist: 0x2d0c
   __TEXT.__const: 0x270
   __TEXT.__gcc_except_tab: 0x9f0
-  __TEXT.__cstring: 0x42be
+  __TEXT.__cstring: 0x42b3
   __TEXT.__ustring: 0xcc2
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xcf4
-  __TEXT.__objc_classname: 0x44c
-  __TEXT.__objc_methname: 0x743f
+  __TEXT.__unwind_info: 0xd00
+  __TEXT.__objc_classname: 0x460
+  __TEXT.__objc_methname: 0x74ab
   __TEXT.__objc_methtype: 0xf74
-  __TEXT.__objc_stubs: 0x6e80
+  __TEXT.__objc_stubs: 0x6ec0
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3028
-  __DATA_CONST.__objc_selrefs: 0x1fb8
-  __DATA_CONST.__objc_arraydata: 0x1ca0
+  __DATA_CONST.__objc_const: 0x30a0
+  __DATA_CONST.__objc_selrefs: 0x1fc0
+  __DATA_CONST.__objc_arraydata: 0x1a40
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_const: 0xe28
-  __AUTH_CONST.__cfstring: 0x9be0
+  __AUTH_CONST.__objc_const: 0xe70
+  __AUTH_CONST.__cfstring: 0x9b40
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0xa50
   __DATA.__objc_classrefs: 0x308
-  __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x1f0
+  __DATA.__objc_superrefs: 0xd8
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0x181
-  __DATA.__bss: 0x221
+  __DATA.__bss: 0x231
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1081
-  Symbols:   3997
-  CStrings:  2372
+  Functions: 1085
+  Symbols:   4010
+  CStrings:  2371
 
Symbols:
+ -[TypistHWKeyboard keyboardLanguageString]
+ -[TypistHWKeyboard setKeyboardLanguageString:]
+ -[TypistKeyboardFarsi init:options:]
+ -[TypistKeyboardFarsi isSwitchedToCapitalPlane:previous:currentPlane:context:]
+ GCC_except_table16
+ _OBJC_CLASS_$_TypistKeyboardFarsi
+ _OBJC_IVAR_$_TypistHWKeyboard._keyboardLanguageString
+ _OBJC_METACLASS_$_TypistKeyboardFarsi
+ __OBJC_$_INSTANCE_METHODS_TypistKeyboardFarsi
+ __OBJC_CLASS_RO_$_TypistKeyboardFarsi
+ __OBJC_METACLASS_RO_$_TypistKeyboardFarsi
+ ___38-[TypistKeyboard generateSwipeStream:]_block_invoke.440
+ ___44+[TypistHWKeyboard keyboardLanguageValueMap]_block_invoke_2
+ ___block_descriptor_32_e35_v32?0"NSNumber"8"NSString"16^B24l
+ ___block_literal_global.206
+ ___block_literal_global.366
+ ___block_literal_global.380
+ __unnamed_array_storage.506
+ __unnamed_array_storage.507
+ _keyboardLanguageValueMap.layoutMap
+ _keyboardLayoutValueMap.countryCodeMap
+ _objc_msgSend$detachHardwareKeyboard
+ _objc_msgSend$keyboardLanguageString
+ _objc_msgSend$setKeyboardLanguageString:
- GCC_except_table15
- _OBJC_CLASS_$_NSNull
- ___38-[TypistKeyboard generateSwipeStream:]_block_invoke.436
- ___42+[TypistHWKeyboard keyboardLayoutValueMap]_block_invoke_2
- ___block_descriptor_32_e35_v32?0"NSString"8"NSNumber"16^B24l
- ___block_literal_global.204
- ___block_literal_global.393
- ___block_literal_global.409
- __unnamed_array_storage.391
- __unnamed_array_storage.502
- __unnamed_array_storage.503
- _keyboardLanguageValueMap.countryCodeMap
- _keyboardLayoutValueMap.layoutMap
- _objc_msgSend$null
CStrings:
+ "ABC"
+ "An existing hardware keyboard was found to be attached. Detaching prior to attaching new keyboard (%@)..."
+ "Canadian"
+ "G"
+ "Spanish"
+ "Swedish"
+ "T@\"NSString\",&,N,V_keyboardLanguageString"
+ "Turkish-QWERTY"
+ "TypistKeyboardFarsi"
+ "_keyboardLanguageString"
+ "fa"
+ "keyboardLanguageString"
+ "setKeyboardLanguageString:"
+ "v32@?0@\"NSNumber\"8@\"NSString\"16^B24"
- "2SetHangul"
- "Canadian - CSA"
- "F"
- "Hebrew"
- "Italian - Pro"
- "Japanese Keyboard"
- "Latin America"
- "Persian"
- "Simplified Chinese Keyboard"
- "Spanish - ISO"
- "Swedish - Pro"
- "Thai"
- "Zhuyin Bopomofo"
- "null"
- "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"

```
