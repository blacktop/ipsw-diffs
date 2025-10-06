## CBORLibrary

> `/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary`

```diff

-3.1.1.0.0
-  __TEXT.__text: 0x25664
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0x110a
-  __TEXT.__cstring: 0x93e
-  __TEXT.__swift5_typeref: 0x3c4
-  __TEXT.__swift5_reflstr: 0x1c4
+3.4.5.0.0
+  __TEXT.__text: 0x26c44
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x564
+  __TEXT.__const: 0x11ba
+  __TEXT.__cstring: 0xbf3
+  __TEXT.__swift5_typeref: 0x3ce
+  __TEXT.__swift5_reflstr: 0x234
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_fieldmd: 0x3c0
-  __TEXT.__constg_swiftt: 0x634
+  __TEXT.__swift5_fieldmd: 0x40c
+  __TEXT.__constg_swiftt: 0x6ac
   __TEXT.__swift5_capture: 0x100
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0xa0
-  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_proto: 0xac
+  __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__oslogstring: 0x20
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x1540
-  __TEXT.__eh_frame: 0x1ac0
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x1016
-  __TEXT.__objc_methtype: 0x221
-  __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0x200
+  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__eh_frame: 0x1bf0
+  __TEXT.__objc_classname: 0x4f
+  __TEXT.__objc_methname: 0x1120
+  __TEXT.__objc_methtype: 0x23d
+  __TEXT.__objc_stubs: 0xd00
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1038
-  __DATA_CONST.__objc_selrefs: 0x4f0
-  __AUTH_CONST.__const: 0x8e0
+  __DATA_CONST.__objc_const: 0x1068
+  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__const: 0x968
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH.__objc_data: 0x0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x98
-  __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x3d8
-  __DATA.__bss: 0x1400
-  __DATA_DIRTY.__const: 0x748
+  __DATA.__data: 0x460
+  __DATA.__bss: 0x1580
+  __DATA_DIRTY.__const: 0x728
   __DATA_DIRTY.__objc_const: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x278
-  __DATA_DIRTY.__data: 0x548
+  __DATA_DIRTY.__objc_data: 0x2a0
+  __DATA_DIRTY.__data: 0x558
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B2BC3965-E043-324F-A1E8-BC5EB82A22D6
-  Functions: 908
-  Symbols:   721
-  CStrings:  461
+  UUID: 3C113E19-7F60-363D-98BC-8795B9D19F19
+  Functions: 936
+  Symbols:   745
+  CStrings:  493
 
Symbols:
+ +[CBOR cborWithEmbeddedCBORData:]
+ +[CBOR decodeFromBytes:length:recursionLevel:keepKeyOrdering:]
+ +[CBOR decodeMajorType2And3FromBuffer:length:tag:indefiniteLenContainerType:]
+ +[CBOR decodeMajorType4FromBuffer:length:tag:recursionLevel:keepKeyOrdering:]
+ +[CBOR decodeMajorType5FromBuffer:length:tag:recursionLevel:keepKeyOrdering:]
+ +[CBOR(Decoder) decodeFromData:keepKeyOrdering:]
+ +[NSData(CBOR) dataWithCBOR:encodingKeyOrder:]
+ -[CBOR encodeToEmbeddedCBORData]
+ -[CBOR isEmbeddedCBORData]
+ ___51+[CBOR(Encoder) encodeMajorType5:encodingKeyOrder:]_block_invoke
+ ___block_descriptor_40_e23_q24?0"CBOR"8"CBOR"16l
+ ___strlcpy_chk
+ ___unnamed_22
+ __swift_stdlib_reportUnimplementedInitializer
+ _mktime
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$cborWithEmbeddedCBORData:
+ _objc_msgSend$dataWithCBOR:encodingKeyOrder:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$decodeFromData:keepKeyOrdering:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$unsignedIntValue
+ _strptime_l
+ _strtod
+ _swift_checkMetadataState
+ _swift_initStructMetadata
+ _symbolic Sb
+ _symbolic _____ So4CBORC11CBORLibraryE07EncodedA0V
+ _timegm
- +[CBOR decodeFromBytes:length:recursionLevel:]
- +[CBOR decodeMajorType2And3FromBuffer:length:tag:]
- +[CBOR decodeMajorType4FromBuffer:length:tag:recursionLevel:]
- +[CBOR decodeMajorType5FromBuffer:length:tag:recursionLevel:]
- __NSConcreteGlobalBlock
- ___34+[CBOR(Encoder) encodeMajorType5:]_block_invoke
- ___block_descriptor_32_e23_q24?0"CBOR"8"CBOR"16l
- ___block_literal_global
- ___swift_memcpy0_1
- ___unnamed_19
CStrings:
+ "%Y-%m-%dT%H:%M:%S"
+ "%Y-%m-%dT%H:%M:%S%z"
+ "+[CBOR(Decoder) decodeMajorType2And3FromBuffer:length:tag:indefiniteLenContainerType:]"
+ "+[CBOR(Decoder) decodeMajorType4FromBuffer:length:tag:recursionLevel:keepKeyOrdering:]"
+ "+[CBOR(Decoder) decodeMajorType5FromBuffer:length:tag:recursionLevel:keepKeyOrdering:]"
+ "@28@0:8@16B24"
+ "@32@0:8@16Q24"
+ "Bool value not found"
+ "CBORLibrary._CBORDictionary"
+ "Double value not found"
+ "Float value not found"
+ "Int value not found"
+ "Int16 value not found"
+ "Int32 value not found"
+ "Int64 value not found"
+ "Int8 value not found"
+ "String value not found"
+ "T@\"NSString\",?,R,C"
+ "The given data does not contain encoded CBOR data item"
+ "UInt value not found"
+ "UInt16 value not found"
+ "UInt32 value not found"
+ "UInt64 value not found"
+ "UInt8 value not found"
+ "cStringUsingEncoding:"
+ "cborWithEmbeddedCBORData:"
+ "dataWithCBOR:encodingKeyOrder:"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSince1970:"
+ "decodeFromData:keepKeyOrdering:"
+ "encodeToEmbeddedCBORData"
+ "init()"
+ "isEmbeddedCBORData"
+ "lengthOfBytesUsingEncoding:"
+ "maintainKeySetOrder"
- "+[CBOR(Decoder) decodeMajorType2And3FromBuffer:length:tag:]"
- "+[CBOR(Decoder) decodeMajorType4FromBuffer:length:tag:recursionLevel:]"
- "+[CBOR(Decoder) decodeMajorType5FromBuffer:length:tag:recursionLevel:]"

```
