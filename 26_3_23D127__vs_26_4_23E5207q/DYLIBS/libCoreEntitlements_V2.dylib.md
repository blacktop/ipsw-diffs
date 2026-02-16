## libCoreEntitlements_V2.dylib

> `/usr/lib/libCoreEntitlements_V2.dylib`

```diff

-80.0.1.0.0
-  __TEXT.__text: 0x52f8
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xe7
-  __TEXT.__unwind_info: 0x190
+80.100.6.0.0
+  __TEXT.__text: 0x6594
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0xd1
+  __TEXT.__unwind_info: 0x1f0
   __TEXT.__objc_methname: 0x166
   __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x50
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__data: 0x4
-  __DATA.__bss: 0xc
+  __DATA.__common: 0x8
+  __DATA.__bss: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F4B804A-616F-34AD-AD3B-CD68B3D2FDDF
-  Functions: 114
-  Symbols:   290
+  UUID: F7DC7EFE-E51F-339F-BAED-1F38553FA42A
+  Functions: 139
+  Symbols:   277
   CStrings:  44
 
Symbols:
+ _CEContextCreateAsLegacyContext
+ _CEDictionaryCheckSubset
+ _CEElementCheckSubset
+ _CEEnvironmentAllocate
+ _CEEnvironmentFree
+ _DERContentLengthOfEncodedSequence
+ _DERDecodeItemPartialBuffer
+ _DERDecodeSeqInit
+ _DERDecodeSequenceContentWithBlock
+ _DERDecodeSequenceWithBlock
+ _DEREncodeItem
+ _DEREncodeLength
+ _DEREncodeSequence
+ _DEREncodeSequenceFromObject
+ _DERLengthOfEncodedSequence
+ _DERLengthOfEncodedSequenceFromObject
+ _DERLengthOfLength
+ _DERParseBitString
+ _DERParseBooleanWithDefault
+ _DERParseInteger
+ _DERParseInteger64
+ _DERParseIntegerSigned
+ _DERParseSequence
+ _DERParseSequenceContent
+ _DERParseSequenceToObject
+ ___keyValueLoop
+ ___matchLoop
+ _arrayIterate.54
+ _buildIndex
+ _dictionaryIterate.51
+ _dictionarySubsetIterate
+ _keyFromIndex
+ _mapTypeToConstraints
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _parseApplicationVN
+ _searchIndex
+ _sequenceSubsetIterate
+ _validateAuxiliary
+ _validateSpecForString
- _CEBuildIndexForContext
- _CEContextExecuteQuery
- _CEContextIsAccelerated
- _CEContextIsSubset
- _CEFreeIndexForContext
- _CEIndexSizeForContext
- _CESelectKeyOperation
- _CESelectValueOperation
- _arrayIterate.27
- _derVMIterateCallback
- _der_vm_CEType_from_context
- _der_vm_bool_from_context
- _der_vm_buffer_from_context
- _der_vm_container_from_context
- _der_vm_context_is_valid
- _der_vm_execute_nocopy
- _der_vm_execute_seq_nocopy
- _der_vm_integer_from_context
- _der_vm_iterate_count
- _der_vm_iterate_nocopy
- _der_vm_string_from_context
- _dictionaryIterate.24
- _mapToCEReturn.13
- _mapToCEReturn.6
- _objc_claimAutoreleasedReturnValue
- _objc_release_x22
- _objc_release_x8
- _objc_retain
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x8
- _validateContextWithType
- _validateDictionary
- _validateDuplicateKeys
- _validateDuplicateKeysSub
- _validateKeyValuePair
- _validateSingleType
- _validateSpecForApplication
- _validateString
- _validateValueTypePair
CStrings:
+ "*"
+ "subset | %.*s: 0x%04X\n"
- "%.*s | validate: 0x%04X\n"
- "duplicate key | %.*s\n"

```
