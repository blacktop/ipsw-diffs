## libCoreEntitlements_V2.dylib

> `/usr/lib/libCoreEntitlements_V2.dylib`

```diff

-69.100.2.0.0
-  __TEXT.__text: 0x30f0
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__cstring: 0xcb
-  __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_methname: 0x91
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x88
+80.0.0.0.0
+  __TEXT.__text: 0x52f8
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0xe7
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_methname: 0x166
+  __TEXT.__objc_stubs: 0x240
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__objc_selrefs: 0x98
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x50
+  __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__data: 0x4
   __DATA.__bss: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ADF71C22-296B-3E9B-80DD-39B3B270CE5A
-  Functions: 92
-  Symbols:   209
-  CStrings:  30
+  UUID: B68E96BE-2B55-3E8B-9533-5A6B1182A155
+  Functions: 114
+  Symbols:   290
+  CStrings:  44
 
Symbols:
+ _CECFDictionaryCreateAsDER
+ _CEContextCreateAsCFDictionary
+ _CEElementCreateAsCFObject
+ _CENSDictionaryCreateAsDER
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _DERDecodeItem
+ _DERDecodeItemPartialBufferGetLength
+ _DERDecodeSeqContentInit
+ _DERDecodeSeqNext
+ _DEREncodeItemSized
+ _DEREncodeLengthSized
+ _DEREncodeTag
+ _DERLengthOfItem
+ _DERParseBoolean
+ _DERParseInteger64Signed
+ _DERParseSequenceContentToObject
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _bzero
+ _memmove
+ _objc_autorelease
+ _objc_enumerationMutation
+ _objc_msgSend$UTF8String
+ _objc_msgSend$allKeys
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bytes
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$length
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _serializeAsArrayLength
+ _serializeAsIntegerLength
+ _serializeSequence
+ _validateSpec
+ _validateSpecForApplication
+ _validateSpecForDictionary
+ _validateSpecForElement
CStrings:
+ "UTF8String"
+ "allKeys"
+ "arrayWithObjects:count:"
+ "boolValue"
+ "bytes"
+ "compare:"
+ "countByEnumeratingWithState:objects:count:"
+ "dataWithBytes:length:"
+ "duplicate key | %.*s\n"
+ "i"
+ "length"
+ "objectForKeyedSubscript:"
+ "sortedArrayUsingSelector:"
+ "unsignedLongLongValue"
+ "validation | %.*s: 0x%04X\n"
- "%.*s | duplicated key\n"

```
