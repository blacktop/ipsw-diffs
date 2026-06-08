## AppleFlatBuffers

> `/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers`

```diff

 17.0.0.0.0
-  __TEXT.__text: 0x12894
-  __TEXT.__auth_stubs: 0x430
+  __TEXT.__text: 0x122ac
   __TEXT.__objc_methlist: 0x60c
   __TEXT.__const: 0x1a4
-  __TEXT.__gcc_except_tab: 0x3490
-  __TEXT.__cstring: 0x7d9
-  __TEXT.__unwind_info: 0x640
-  __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x11d8
-  __TEXT.__objc_methtype: 0x354
-  __TEXT.__objc_stubs: 0x960
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__gcc_except_tab: 0x3660
+  __TEXT.__cstring: 0x7e3
+  __TEXT.__unwind_info: 0x658
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x168
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x5a8
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x9
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59B22810-6493-38C4-8BF2-FD82F80A21FD
-  Functions: 238
-  Symbols:   847
-  CStrings:  311
+  UUID: D02FD34E-2812-3B99-8D72-329A659032B1
+  Functions: 241
+  Symbols:   861
+  CStrings:  88
 
Symbols:
+ GCC_except_table119
+ GCC_except_table130
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe220100ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEENS_16allocator_traitsIS8_EEEENS_19__allocation_resultINT0_7pointerENSC_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__16__treeIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS3_17FlatBufferBuilder19StringOffsetCompareENS_9allocatorIS6_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJRS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- GCC_except_table129
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
- "#"
- "(type=\"__data\"[96C])"
- ".cxx_destruct"
- "@\"AFBBufRef\""
- "@\"AFBDictionary\""
- "@\"NSData\""
- "@\"NSError\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8r*16"
- "@32@0:8@16Q24"
- "@32@0:8Q16@?24"
- "@32@0:8r*16Q24"
- "@32@0:8r^@16Q24"
- "@32@0:8r^B16Q24"
- "@32@0:8r^I16Q24"
- "@32@0:8r^Q16Q24"
- "@32@0:8r^S16Q24"
- "@32@0:8r^d16Q24"
- "@32@0:8r^f16Q24"
- "@32@0:8r^i16Q24"
- "@32@0:8r^q16Q24"
- "@32@0:8r^s16Q24"
- "@40@0:8@16Q24@?32"
- "@40@0:8@16Q24^@32"
- "@40@0:8Q16Q24@?32"
- "@40@0:8r*16Q24Q32"
- "@40@0:8r^@16r^@24Q32"
- "@40@0:8r^B16Q24Q32"
- "@40@0:8r^I16Q24Q32"
- "@40@0:8r^Q16Q24Q32"
- "@40@0:8r^S16Q24Q32"
- "@40@0:8r^d16Q24Q32"
- "@40@0:8r^f16Q24Q32"
- "@40@0:8r^i16Q24Q32"
- "@40@0:8r^q16Q24Q32"
- "@40@0:8r^s16Q24Q32"
- "@48@0:8@16@24Q32^@40"
- "@52@0:8r^{Config=iQiI}16@24i32Q36^@44"
- "@64@0:8@16Q24#32@?40@?48@?56"
- "@?"
- "AFBArray"
- "AFBBufRef"
- "AFBBufferBuilder"
- "AFBDictionary"
- "AFBDictionaryEnumerator"
- "B"
- "B24@0:8@16"
- "B48@0:8:16^v24Q32^@40"
- "Q"
- "Q16@0:8"
- "T@\"NSData\",R,N"
- "T@\"NSError\",R,N,V_firstError"
- "T@\"NSString\",R,N,V_path"
- "T^{__CFAllocator=},R,N"
- "UTF8String"
- "^v"
- "^v16@0:8"
- "^{__CFAllocator=}"
- "^{__CFAllocator=}16@0:8"
- "_bufRef"
- "_cfReleaseBackingDataDeallocator"
- "_count"
- "_data"
- "_dict"
- "_fbbStorage"
- "_fileAllocator"
- "_firstError"
- "_index"
- "_initOk"
- "_isFinalized"
- "_keyAtIndex"
- "_keyClass"
- "_objectAtIndex"
- "_objectForValidKey"
- "_path"
- "_tableAtIndex"
- "addObject:"
- "allKeys"
- "allKeysForObject:"
- "allValues"
- "boolValue"
- "bytes"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createString:"
- "createString:alignment:"
- "createStringWithCString:"
- "createStringWithCString:alignment:"
- "createStringWithData:"
- "createStringWithData:alignment:"
- "createVectorOfBoolWithArray:"
- "createVectorOfBoolWithArray:alignment:"
- "createVectorOfBoolWithCArray:count:"
- "createVectorOfBoolWithCArray:count:alignment:"
- "createVectorOfBoolWithCount:alignment:block:"
- "createVectorOfBoolWithCount:block:"
- "createVectorOfFloat32WithArray:"
- "createVectorOfFloat32WithArray:alignment:"
- "createVectorOfFloat32WithCArray:count:"
- "createVectorOfFloat32WithCArray:count:alignment:"
- "createVectorOfFloat32WithCount:alignment:block:"
- "createVectorOfFloat32WithCount:block:"
- "createVectorOfFloat64WithArray:"
- "createVectorOfFloat64WithArray:alignment:"
- "createVectorOfFloat64WithCArray:count:"
- "createVectorOfFloat64WithCArray:count:alignment:"
- "createVectorOfFloat64WithCount:alignment:block:"
- "createVectorOfFloat64WithCount:block:"
- "createVectorOfInt16WithArray:"
- "createVectorOfInt16WithArray:alignment:"
- "createVectorOfInt16WithCArray:count:"
- "createVectorOfInt16WithCArray:count:alignment:"
- "createVectorOfInt16WithCount:alignment:block:"
- "createVectorOfInt16WithCount:block:"
- "createVectorOfInt32WithArray:"
- "createVectorOfInt32WithArray:alignment:"
- "createVectorOfInt32WithCArray:count:"
- "createVectorOfInt32WithCArray:count:alignment:"
- "createVectorOfInt32WithCount:alignment:block:"
- "createVectorOfInt32WithCount:block:"
- "createVectorOfInt64WithArray:"
- "createVectorOfInt64WithArray:alignment:"
- "createVectorOfInt64WithCArray:count:"
- "createVectorOfInt64WithCArray:count:alignment:"
- "createVectorOfInt64WithCount:alignment:block:"
- "createVectorOfInt64WithCount:block:"
- "createVectorOfInt8WithArray:"
- "createVectorOfInt8WithArray:alignment:"
- "createVectorOfInt8WithCArray:count:"
- "createVectorOfInt8WithCArray:count:alignment:"
- "createVectorOfInt8WithCount:alignment:block:"
- "createVectorOfInt8WithCount:block:"
- "createVectorOfStringWithArray:"
- "createVectorOfStringWithArray:alignment:"
- "createVectorOfStringWithCount:alignment:block:"
- "createVectorOfStringWithCount:block:"
- "createVectorOfStringWithOffsets:"
- "createVectorOfUInt16WithArray:"
- "createVectorOfUInt16WithArray:alignment:"
- "createVectorOfUInt16WithCArray:count:"
- "createVectorOfUInt16WithCArray:count:alignment:"
- "createVectorOfUInt16WithCount:alignment:block:"
- "createVectorOfUInt16WithCount:block:"
- "createVectorOfUInt32WithArray:"
- "createVectorOfUInt32WithArray:alignment:"
- "createVectorOfUInt32WithCArray:count:"
- "createVectorOfUInt32WithCArray:count:alignment:"
- "createVectorOfUInt32WithCount:alignment:block:"
- "createVectorOfUInt32WithCount:block:"
- "createVectorOfUInt64WithArray:"
- "createVectorOfUInt64WithArray:alignment:"
- "createVectorOfUInt64WithCArray:count:"
- "createVectorOfUInt64WithCArray:count:alignment:"
- "createVectorOfUInt64WithCount:alignment:block:"
- "createVectorOfUInt64WithCount:block:"
- "createVectorOfUInt8WithArray:"
- "createVectorOfUInt8WithArray:alignment:"
- "createVectorOfUInt8WithCArray:count:"
- "createVectorOfUInt8WithCArray:count:alignment:"
- "createVectorOfUInt8WithCount:alignment:block:"
- "createVectorOfUInt8WithCount:block:"
- "createVectorOfUInt8WithData:"
- "createVectorOfUInt8WithData:alignment:"
- "dealloc"
- "deallocator"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateKeysAndObjectsWithOptions:usingBlock:"
- "exceptionWithName:reason:userInfo:"
- "fbb"
- "fileSystemRepresentation"
- "finalizeWithSelector:"
- "finalizeWithSelector:allocatorBufferAddr:size:error:"
- "firstError"
- "floatValue"
- "initWithBufRef:count:keyClass:keyAtIndex:tableAtIndex:objectForValidKey:"
- "initWithBufRef:count:objectAtIndex:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithConfig:path:protectionClass:capacity:error:"
- "initWithData:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFileAtPath:capacity:error:"
- "initWithFileAtPath:protection:capacity:error:"
- "initWithFormat:"
- "initWithObjects:count:"
- "initWithObjects:forKeys:count:"
- "initWithUTF8String:"
- "initWithUnsignedInt:"
- "intValue"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "keyEnumerator"
- "length"
- "longLongValue"
- "nextObject"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "path"
- "releaseBuf"
- "retainBuf"
- "reverseObjectEnumerator"
- "setError:"
- "throwIfFinalizedWithSelector:"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "v16@0:8"
- "v24@0:8:16"
- "v24@0:8@16"
- "v32@0:8Q16@?24"

```
