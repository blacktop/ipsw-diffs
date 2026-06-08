## SignalCompression

> `/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression`

```diff

-29.100.2.0.0
-  __TEXT.__text: 0x10008
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x1cc0
-  __TEXT.__gcc_except_tab: 0x320
+32.0.0.0.0
+  __TEXT.__text: 0xf3d8
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x1c80
+  __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__oslogstring: 0xf19
-  __TEXT.__cstring: 0x3bb
-  __TEXT.__swift5_typeref: 0x25c
-  __TEXT.__constg_swiftt: 0x2e0
-  __TEXT.__swift5_reflstr: 0x1b9
-  __TEXT.__swift5_fieldmd: 0x2b4
+  __TEXT.__cstring: 0x3eb
+  __TEXT.__swift5_typeref: 0x252
+  __TEXT.__constg_swiftt: 0x2a8
+  __TEXT.__swift5_reflstr: 0x169
+  __TEXT.__swift5_fieldmd: 0x278
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x88
   __TEXT.__swift5_types: 0x40
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__eh_frame: 0x294
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x39b
-  __TEXT.__objc_methtype: 0x1a9
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x80
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__eh_frame: 0x2c4
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x5b0
+  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x238
+  __AUTH.__data: 0x1d8
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x7d0
+  __DATA.__data: 0x7c0
   __DATA.__bss: 0x1120
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3B723F3C-2C6F-3B5B-9504-0C6B736E7726
-  Functions: 376
-  Symbols:   547
-  CStrings:  208
+  UUID: 1A82E74A-1F41-302E-ABA7-FD38AA03E9F5
+  Functions: 381
+  Symbols:   554
+  CStrings:  149
 
Symbols:
+ -[MotionDecoderWrapper .cxx_destruct]
+ -[MotionDecoderWrapper attributeCount]
+ -[MotionDecoderWrapper componentPerAttributeCount]
+ -[MotionDecoderWrapper decodeFrameInternal:outputDecodedBuffer:outputBufferLength:quantization:formatType:decodeError:]
+ -[MotionDecoderWrapper decodeFrameInternal:outputDecodedBuffer:outputBufferLength:quantization:formatType:decodeError:].cold.1
+ -[MotionDecoderWrapper initWithEncoderSeqParams:].cold.1
+ -[MotionDecoderWrapper maxDecodedCount]
+ -[MotionEncoderWrapper encodeFrameInternal:quantization:formatType:frameType:outputEncodedBuffer:outputBufferLength:encodeError:]
+ -[MotionEncoderWrapper initWithAttributeCount:componentCount:quantization:].cold.2
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table43
+ GCC_except_table46
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _SCFormatTypeSize
+ __MergedGlobals
+ __ZN3gcl6motion11DecoderImpl11decodeFrameEPKhmRmPviNS0_10FormatTypeE
+ __ZN3gcl6motion11EncoderImpl11encodeFrameEPKviNS0_10FormatTypeENS0_9FrameTypeEPhmRmRKNS0_7Encoder18EncodingParametersE
+ __ZN3gcl6motion7Decoder11decodeFrameEPKhmRmPviNS0_10FormatTypeE
+ __ZN3gcl6motion7Encoder11encodeFrameEPKviNS0_10FormatTypeENS0_9FrameTypeEPhmRmRKNS1_18EncodingParametersE
+ __ZN3gcl6motionL9_quantizeEPKviNS0_10FormatTypeEiRi
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIN3gcl17ArithmeticContextEEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIN3gcl6motion9SliceInfoEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIiEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN3gcl6motion9SliceInfoENS_9allocatorIS3_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN3gcl6motion9SliceInfoENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9fqe220100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE24__emplace_back_slow_pathIJhEEEPhDpOT_
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE6resizeEm
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9fqe220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9fqe220100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B9fqe220100EmRKi
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ ___swift__destructor
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retain_x1
+ _objc_retain_x8
+ _swift_deallocObject
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x25
+ _swift_retain_x27
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic _____y_____G s15EmptyCollectionV s5UInt8V
- -[MotionDecoderWrapper decodeFrameInternal:decodedFrame:decodeError:]
- -[MotionDecoderWrapper decodeFrameInternal:decodedFrame:decodeError:].cold.1
- -[MotionDecoderWrapper getAttributeCount]
- -[MotionDecoderWrapper getComponentPerAttributeCount]
- -[MotionDecoderWrapper getPointerToDataBuffer:]
- -[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance].cold.1
- -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:]
- -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.1
- -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.2
- -[MotionEncoderWrapper encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:].cold.3
- -[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance].cold.1
- GCC_except_table13
- GCC_except_table15
- GCC_except_table3
- GCC_except_table35
- GCC_except_table37
- GCC_except_table44
- GCC_except_table48
- GCC_except_table5
- GCC_except_table8
- __ZN16MSCDecoderObject15resizeBitstreamEm
- __ZN3gcl6motion11DecoderImpl11decodeFrameEPKhmRmPi
- __ZN3gcl6motion11EncoderImpl11encodeFrameEPKiNS0_9FrameTypeEPhmRmRKNS0_7Encoder18EncodingParametersE
- __ZN3gcl6motion7Decoder11decodeFrameEPKhmRmPi
- __ZN3gcl6motion7Encoder11encodeFrameEPKiNS0_9FrameTypeEPhmRmRKNS1_18EncodingParametersE
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN3gcl17ArithmeticContextEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN3gcl6motion9SliceInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN3gcl17ArithmeticContextENS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIN3gcl6motion9SliceInfoENS_9allocatorIS3_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN3gcl6motion9SliceInfoENS_9allocatorIS3_EEE9push_backB9nqe210106EOS3_
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB9nqe210106IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE8__appendEm
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB9nqe210106IPKiS6_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE8__appendEm
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B9nqe210106Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B9nqe210106EmRKi
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZZ61-[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]E14sharedInstance
- __ZZ61-[MotionDecoderWrapper motionDecoderWrapperLogSharedInstance]E9onceToken
- __ZZ61-[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]E14sharedInstance
- __ZZ61-[MotionEncoderWrapper motionEncoderWrapperLogSharedInstance]E9onceToken
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SignalCompression
- _objc_msgSend$decodeFrameInternal:decodedFrame:decodeError:
- _objc_msgSend$encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:
- _objc_msgSend$getAttributeCount
- _objc_msgSend$getComponentPerAttributeCount
- _objc_msgSend$getEncoderParams
- _objc_msgSend$getPointerToDataBuffer:
- _objc_msgSend$initWithAttributeCount:componentCount:quantization:
- _objc_msgSend$initWithEncoderSeqParams:
- _objc_msgSend$motionDecoderWrapperLogSharedInstance
- _objc_msgSend$motionEncoderWrapperLogSharedInstance
- _objc_release_x26
- _symbolic Say_____G s5Int32V
- _symbolic _____Sg s5UInt8V
- _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int32V
CStrings:
+ "Invalid output length for decode"
+ "output buffer (%ld) is less than required size: %ld"
- "*24@0:8@16"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"NSData\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8I16I20I24"
- "C"
- "MotionDecoderWrapper"
- "MotionEncoderWrapper"
- "Q"
- "Q56@0:8r^i16*24Q32^Q40^Q48"
- "^v"
- "_TtC17SignalCompression13SignalDecoder"
- "_TtC17SignalCompression13SignalEncoder"
- "_attributeCount"
- "_bitstream"
- "_componentsPerAttribute"
- "_encoderParamsData"
- "_frameCount"
- "_intraFramePeriod"
- "_quantization"
- "attributeCount"
- "buffer"
- "bytes"
- "componentsPerAttribute"
- "dataWithBytes:length:"
- "dealloc"
- "debugEnabled"
- "decodeFrameInternal:decodedFrame:decodeError:"
- "decoder"
- "encParametersLength"
- "encodeFrameInternal:outputEncodedBuffer:outputBufferLength:type:encodeError:"
- "encoder"
- "encoderInfo"
- "encoderParams"
- "estimatedEncodedFrameSizeInBytes"
- "formatDescriptor"
- "formatType"
- "getAttributeCount"
- "getComponentPerAttributeCount"
- "getEncoderParams"
- "getPointerToDataBuffer:"
- "i"
- "i16@0:8"
- "i40@0:8@16^i24^Q32"
- "init"
- "initWithAttributeCount:componentCount:quantization:"
- "initWithEncoderSeqParams:"
- "length"
- "logger"
- "motionDecoderWrapperLogSharedInstance"
- "motionEncoderWrapperLogSharedInstance"
- "outbuffer"
- "output buffer does not match requirements %ld %ld"
- "outputBuffer"
- "quantization"
- "signalEncoderParamsDecoder"
- "v16@0:8"
- "{AttributeInfo=\"apiVersion\"i\"version\"{Version=\"major\"C\"minor\"C\"revision\"S}\"attributeCount\"i\"componentsPerAttribute\"i\"componentCount\"i\"quatizationBits\"C\"seiDataSize\"I\"decompressedDataSize\"I\"rawSPS\"[1020C]}"
- "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"\"{?=\"__cap_\"*}}"

```
