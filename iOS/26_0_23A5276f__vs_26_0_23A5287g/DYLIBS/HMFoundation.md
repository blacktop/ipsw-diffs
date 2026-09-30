## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-880.0.0.0.0
-  __TEXT.__text: 0x83ff4
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0x7644
-  __TEXT.__const: 0x25d8
+883.0.0.0.0
+  __TEXT.__text: 0x85fc4
+  __TEXT.__auth_stubs: 0x21a0
+  __TEXT.__objc_methlist: 0x7774
+  __TEXT.__const: 0x25e8
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x3181
-  __TEXT.__swift5_typeref: 0x9d5
-  __TEXT.__swift5_capture: 0x5f0
+  __TEXT.__cstring: 0x31a0
+  __TEXT.__swift5_typeref: 0x9e5
+  __TEXT.__swift5_capture: 0x600
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x194
   __TEXT.__constg_swiftt: 0xd38
-  __TEXT.__swift5_reflstr: 0x367
+  __TEXT.__swift5_reflstr: 0x373
   __TEXT.__swift5_fieldmd: 0x670
   __TEXT.__swift5_types: 0x9c
-  __TEXT.__oslogstring: 0x418e
-  __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__oslogstring: 0x418e
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__gcc_except_tab: 0x1c00
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2da8
-  __TEXT.__eh_frame: 0x2e60
-  __TEXT.__objc_classname: 0x10e0
-  __TEXT.__objc_methname: 0xc230
-  __TEXT.__objc_methtype: 0x26df
-  __TEXT.__objc_stubs: 0x8b00
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0x1560
+  __TEXT.__unwind_info: 0x2e70
+  __TEXT.__eh_frame: 0x2e98
+  __TEXT.__objc_classname: 0x10ed
+  __TEXT.__objc_methname: 0xc50c
+  __TEXT.__objc_methtype: 0x276e
+  __TEXT.__objc_stubs: 0x8fe0
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0x15d8
   __DATA_CONST.__objc_classlist: 0x458
-  __DATA_CONST.__objc_catlist: 0xa0
+  __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f10
+  __DATA_CONST.__objc_selrefs: 0x3018
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1080
-  __AUTH_CONST.__const: 0x1f90
+  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__const: 0x1fb8
   __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xe280
+  __AUTH_CONST.__objc_const: 0xe2c0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1130

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x2400
+  __DATA.__data: 0x2430
   __DATA.__bss: 0x514
   __DATA_DIRTY.__objc_ivar: 0x5ac
   __DATA_DIRTY.__objc_data: 0x19f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 047BFAD4-0E3D-3977-ACCB-95017013E4B1
-  Functions: 3365
-  Symbols:   9168
-  CStrings:  4545
+  UUID: 343D0D72-5679-3C86-AE60-1CE6FA9DC748
+  Functions: 3407
+  Symbols:   9278
+  CStrings:  4591
 
Symbols:
+ -[HMFActivity initWithName:options:]
+ -[HMFObject attributeDescriptions]
+ -[NSData(FastEncoding) hmf_bytesAtOffset:length:]
+ -[NSData(FastEncoding) hmf_objectAtIndex:forArrayAtOffset:]
+ -[NSData(FastEncoding) hmf_objectForKey:forDictionaryAtOffset:]
+ -[NSData(FastEncoding) hmf_readAndCheckTag:offset:]
+ -[NSData(FastEncoding) hmf_readArrayAtOffset:]
+ -[NSData(FastEncoding) hmf_readBytesAtOffset:length:]
+ -[NSData(FastEncoding) hmf_readDataNoCopyAtOffset:]
+ -[NSData(FastEncoding) hmf_readDictionaryAtOffset:]
+ -[NSData(FastEncoding) hmf_readLengthAtOffset:]
+ -[NSData(FastEncoding) hmf_readObjectAtOffset:]
+ -[NSData(FastEncoding) hmf_readStringAtOffset:]
+ -[NSData(FastEncoding) hmf_readTableAtOffset:length:]
+ -[NSData(FastEncoding) hmf_tableLookupWithIndex:offset:]
+ -[NSMutableData(FastEncoding) hmf_appendArray:]
+ -[NSMutableData(FastEncoding) hmf_appendData:]
+ -[NSMutableData(FastEncoding) hmf_appendDictionary:]
+ -[NSMutableData(FastEncoding) hmf_appendNil]
+ -[NSMutableData(FastEncoding) hmf_appendNumber:]
+ -[NSMutableData(FastEncoding) hmf_appendObject:]
+ -[NSMutableData(FastEncoding) hmf_appendOffsetTable:block:]
+ -[NSMutableData(FastEncoding) hmf_appendUInt32:]
+ -[NSMutableData(FastEncoding) hmf_appendUInt8:]
+ -[NSMutableData(FastEncoding) hmf_appendUTF8String:]
+ GCC_except_table41
+ GCC_except_table45
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableData_$_FastEncoding
+ __OBJC_$_CATEGORY_NSMutableData_$_FastEncoding
+ __OBJC_$_CLASS_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
+ __OBJC_$_INSTANCE_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
+ __OBJC_CLASS_PROTOCOLS_$_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
+ ___47-[NSMutableData(FastEncoding) hmf_appendArray:]_block_invoke
+ ___52-[NSMutableData(FastEncoding) hmf_appendDictionary:]_block_invoke
+ ___63-[NSData(FastEncoding) hmf_objectForKey:forDictionaryAtOffset:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e15_i24?0r^v8r^v16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e8_v16?0Q8ls32l8s40l8s48l8
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ _bsearch_b
+ _objc_msgSend$charValue
+ _objc_msgSend$hmf_appendArray:
+ _objc_msgSend$hmf_appendData:
+ _objc_msgSend$hmf_appendDictionary:
+ _objc_msgSend$hmf_appendNil
+ _objc_msgSend$hmf_appendNumber:
+ _objc_msgSend$hmf_appendObject:
+ _objc_msgSend$hmf_appendOffsetTable:block:
+ _objc_msgSend$hmf_appendUInt32:
+ _objc_msgSend$hmf_appendUInt8:
+ _objc_msgSend$hmf_appendUTF8String:
+ _objc_msgSend$hmf_bytesAtOffset:length:
+ _objc_msgSend$hmf_readAndCheckTag:offset:
+ _objc_msgSend$hmf_readArrayAtOffset:
+ _objc_msgSend$hmf_readBytesAtOffset:length:
+ _objc_msgSend$hmf_readDataNoCopyAtOffset:
+ _objc_msgSend$hmf_readDictionaryAtOffset:
+ _objc_msgSend$hmf_readLengthAtOffset:
+ _objc_msgSend$hmf_readObjectAtOffset:
+ _objc_msgSend$hmf_readStringAtOffset:
+ _objc_msgSend$hmf_readTableAtOffset:length:
+ _objc_msgSend$hmf_tableLookupWithIndex:offset:
+ _objc_msgSend$increaseLengthBy:
+ _objc_msgSend$intValue
+ _objc_msgSend$longLongValue
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objCType
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shortValue
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedShortValue
+ _symbolic Say_____G s5UInt8V
- GCC_except_table39
- GCC_except_table44
- __OBJC_$_CLASS_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|HMFTimeZoneCreation)
- __OBJC_$_INSTANCE_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|HMFTimeZoneCreation)
- __OBJC_CLASS_PROTOCOLS_$_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|HMFTimeZoneCreation)
CStrings:
+ "@24@0:8I16I20"
+ "@24@0:8^I16"
+ "@28@0:8@16I24"
+ "B28@0:8C16^I20"
+ "FastEncoding"
+ "I24@0:8I16I20"
+ "I24@0:8^I16"
+ "hmf_appendArray:"
+ "hmf_appendData:"
+ "hmf_appendDictionary:"
+ "hmf_appendNil"
+ "hmf_appendNumber:"
+ "hmf_appendObject:"
+ "hmf_appendOffsetTable:block:"
+ "hmf_appendUInt32:"
+ "hmf_appendUInt8:"
+ "hmf_appendUTF8String:"
+ "hmf_bytesAtOffset:length:"
+ "hmf_objectAtIndex:forArrayAtOffset:"
+ "hmf_objectForKey:forDictionaryAtOffset:"
+ "hmf_readAndCheckTag:offset:"
+ "hmf_readArrayAtOffset:"
+ "hmf_readBytesAtOffset:length:"
+ "hmf_readDataNoCopyAtOffset:"
+ "hmf_readDictionaryAtOffset:"
+ "hmf_readLengthAtOffset:"
+ "hmf_readObjectAtOffset:"
+ "hmf_readStringAtOffset:"
+ "hmf_readTableAtOffset:length:"
+ "hmf_tableLookupWithIndex:offset:"
+ "i24@?0r^v8r^v16"
+ "increaseLengthBy:"
+ "initWithName:options:"
+ "intValue"
+ "longLongValue"
+ "r^I32@0:8^I16^I24"
+ "r^v28@0:8I16Q20"
+ "r^v32@0:8^I16Q24"
+ "setValue:forKey:"
+ "shortValue"
+ "unsignedCharValue"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "unsignedShortValue"
+ "v16@?0Q8"
+ "v20@0:8C16"

```
