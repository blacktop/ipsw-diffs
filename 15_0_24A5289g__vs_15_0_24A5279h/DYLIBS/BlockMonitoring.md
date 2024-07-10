## BlockMonitoring

> `/System/Library/PrivateFrameworks/BlockMonitoring.framework/Versions/A/BlockMonitoring`

```diff

-378.0.0.0.0
-  __TEXT.__text: 0x2edc
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__cstring: 0x429
-  __TEXT.__oslogstring: 0x50d
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x6fa
-  __TEXT.__objc_methtype: 0x162
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0xb8
+377.0.0.0.0
+  __TEXT.__text: 0x26d8
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x1a0
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x3e1
+  __TEXT.__oslogstring: 0x45b
+  __TEXT.__unwind_info: 0xe8
+  __TEXT.__objc_classname: 0x20
+  __TEXT.__objc_methname: 0x5aa
+  __TEXT.__objc_methtype: 0x10b
+  __TEXT.__objc_stubs: 0x4a0
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
+  __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x2f8
+  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__objc_const: 0x2d8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__bss: 0x20
+  __DATA.__objc_ivar: 0x48
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 74
-  Symbols:   284
-  CStrings:  35
+  Functions: 61
+  Symbols:   244
+  CStrings:  32
 
Symbols:
+ +[BMBlockMonitoring(Testing) monitorForTesting]
+ -[BMBlockMonitoring initForTesting:]
+ -[BMBlockMonitoring initForTesting:].cold.1
+ -[BMBlockMonitoring initForTesting:].cold.2
+ -[BMBlockMonitoring initForTesting:].cold.3
+ -[BMBlockMonitoring initForTesting:].cold.4
+ -[BMBlockMonitoring initForTesting:].cold.5
+ -[BMBlockMonitoring initForTesting:].cold.6
+ -[BMBlockMonitoring initForTesting:].cold.7
+ __61-[BMBlockMonitoring executeBlockWithSignature:timeout:block:]_block_invoke.60
+ ___36-[BMBlockMonitoring initForTesting:]_block_invoke
+ __os_feature_enabled_impl
+ _objc_msgSend$initForTesting:
- +[BMBlockMonitoring(Testing) monitorForTestingWithBootArgs:]
- +[BMBlockMonitoring(Testing) readEntitlement:withBlock:]
- +[BMBlockMonitoring(Testing) sanitizedSignature:maxLength:]
- -[BMBlockMonitoring initForTesting:bootArgs:]
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.1
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.2
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.3
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.4
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.5
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.6
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.7
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.8
- -[BMBlockMonitoring initForTesting:bootArgs:].cold.9
- -[BMBlockMonitoring logPanicDeny:reason:].cold.1
- -[BMBlockMonitoring parseBootArgInt:where:]
- -[BMBlockMonitoring parseBootArgInt:where:].cold.1
- GCC_except_table2
- GCC_except_table52
- OBJC_IVAR_$_BMBlockMonitoring._test_bootArgs
- _CFArrayGetTypeID
- _OBJC_CLASS_$_NSMutableCharacterSet
- _OBJC_CLASS_$_NSNumber
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.39
- __45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.43
- __61-[BMBlockMonitoring executeBlockWithSignature:timeout:block:]_block_invoke.79
- __Block_object_assign
- __Block_object_dispose
- __Unwind_Resume
- ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke
- ___59+[BMBlockMonitoring(Testing) sanitizedSignature:maxLength:]_block_invoke
- ___block_descriptor_40_e8_32s_e24_v24?0^v8^{__CFError=}16l
- ___block_descriptor_48_e8_32s40r_e24_v24?0^v8^{__CFError=}16l
- ___copy_helper_block_e8_32s40r
- ___destroy_helper_block_e8_32s40r
- ___objc_personality_v0
- __block_literal_global.156
- _objc_msgSend$addCharactersInString:
- _objc_msgSend$alphanumericCharacterSet
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$componentsSeparatedByCharactersInSet:
- _objc_msgSend$initForTesting:bootArgs:
- _objc_msgSend$invertedSet
- _objc_msgSend$longLongValue
- _objc_msgSend$objectForKey:
- _objc_msgSend$parseBootArgInt:where:
- _objc_msgSend$readEntitlement:withBlock:
- _objc_msgSend$sanitizedSignature:maxLength:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$substringToIndex:
- sanitizedSignature:maxLength:.onceToken
- sanitizedSignature:maxLength:.removedCharacters
CStrings:
+ "BlockMonitoring"
+ "blockMonitoring"
- "_"
- "blockmonitoring"
- "com.apple.security.exception.sysctl.read-only"
- "kern.bootargs"
- "v24@?0^v8^{__CFError=}16"

```
