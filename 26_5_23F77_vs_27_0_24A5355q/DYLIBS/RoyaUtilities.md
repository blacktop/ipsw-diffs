## RoyaUtilities

> `/System/Library/PrivateFrameworks/RoyaUtilities.framework/RoyaUtilities`

```diff

-14.100.20.0.1
-  __TEXT.__text: 0x5268
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x694
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x110
-  __TEXT.__gcc_except_tab: 0x904
-  __TEXT.__unwind_info: 0x518
-  __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0xb1d
-  __TEXT.__objc_methtype: 0x9a2
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x58
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x18
+47.0.0.500.2
+  __TEXT.__text: 0x7964
+  __TEXT.__objc_methlist: 0xb74
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0xce0
+  __TEXT.__cstring: 0x164
+  __TEXT.__unwind_info: 0x780
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e8
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0xa48
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_CONST.__weak_got: 0x10
+  __DATA_CONST.__objc_selrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x148
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0x1648
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__data: 0x300
+  __DATA_DIRTY.__objc_data: 0x640
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6578B60F-0067-322B-BB0C-0AAC06F8DC83
-  Functions: 163
-  Symbols:   711
-  CStrings:  256
+  UUID: 4779E9E7-F350-3F06-9143-0D6A7DADC8AC
+  Functions: 264
+  Symbols:   1117
+  CStrings:  41
 
Symbols:
+ +[NSError(initWithInvalidArgument) errorWithInvalidArgument:userInfo:]
+ +[NSException(NSInternalInconsistencyException) internalInconsistencyWithUserInfo:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithArgumentName:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithArgumentName:andValue:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithReason:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithReason:andArgumentName:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithReason:andArgumentName:andValue:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithReason:andUserInfo:]
+ +[NSException(NSInvalidArgumentException) invalidArgumentWithUserInfo:]
+ +[NSException(NSInvalidArgumentException) invalidArgument]
+ +[NSException(NSInvalidArgumentException) newUserInfoWithArgumentName:]
+ +[NSException(NSInvalidArgumentException) newUserInfoWithArgumentName:andValue:]
+ +[NSException(RoyaUtilities) exceptionWithName:]
+ -[AVAudioPCMBuffer(Roya) initFromByteBuffer:size:]
+ -[AVAudioPCMBuffer(Roya) initFromByteBufferNoCopy:size:deallocator:]
+ -[AVAudioPCMBuffer(Roya) initFromNSData:]
+ -[AVAudioPCMBuffer(Roya) toByteBuffer:size:]
+ -[AVAudioPCMBuffer(Roya) toNSMutableData:]
+ -[NSError(initWithInvalidArgument) initWithInvalidArgument:userInfo:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithArgumentName:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithArgumentName:andValue:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithReason:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithReason:andArgumentName:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithReason:andArgumentName:andValue:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithReason:andUserInfo:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgumentWithUserInfo:]
+ -[NSException(NSInvalidArgumentException) initInvalidArgument]
+ -[NSException(RoyaUtilities) initWithName:]
+ -[PoolOfNSObjectsWithCount_LF addPooledNSObject:]
+ -[PoolOfNSObjectsWithCount_LF count]
+ -[PoolOfNSObjectsWithCount_LF dealloc]
+ -[PoolOfNSObjectsWithCount_LF getPooledNSObject]
+ -[PoolOfNSObjectsWithCount_LF init]
+ -[PoolOfNSObjectsWithCount_SL addPooledNSObject:]
+ -[PoolOfNSObjectsWithCount_SL count]
+ -[PoolOfNSObjectsWithCount_SL getPooledNSObject]
+ -[PoolOfNSObjectsWithCount_SL init]
+ -[PoolOfNSObjectsWithCount_UL .cxx_construct]
+ -[PoolOfNSObjectsWithCount_UL .cxx_destruct]
+ -[PoolOfNSObjectsWithCount_UL addPooledNSObject:]
+ -[PoolOfNSObjectsWithCount_UL count]
+ -[PoolOfNSObjectsWithCount_UL getPooledNSObject]
+ -[PoolOfNSObjectsWithCount_UL init]
+ -[PoolOfNSObjects_LF addPooledNSObject:]
+ -[PoolOfNSObjects_LF dealloc]
+ -[PoolOfNSObjects_LF getPooledNSObject]
+ -[PoolOfNSObjects_LF init]
+ -[PoolOfNSObjects_SL addPooledNSObject:]
+ -[PoolOfNSObjects_SL getPooledNSObject]
+ -[PoolOfNSObjects_SL init]
+ -[PoolOfNSObjects_UL .cxx_construct]
+ -[PoolOfNSObjects_UL .cxx_destruct]
+ -[PoolOfNSObjects_UL addPooledNSObject:]
+ -[PoolOfNSObjects_UL getPooledNSObject]
+ -[PoolOfNSObjects_UL init]
+ -[PooledNSObject_LF .cxx_destruct]
+ -[PooledNSObject_LF autorelease]
+ -[PooledNSObject_LF dealloc]
+ -[PooledNSObject_LF init]
+ -[PooledNSObject_LF nextPooledNSObject]
+ -[PooledNSObject_LF poolOfNSObjects]
+ -[PooledNSObject_LF releaseIntoPoolOfNSObjects]
+ -[PooledNSObject_LF release]
+ -[PooledNSObject_LF retainCount]
+ -[PooledNSObject_LF retain]
+ -[PooledNSObject_LF setNextPooledNSObject:]
+ -[PooledNSObject_LF setPoolOfNSObjects:]
+ -[PooledNSObject_SL .cxx_destruct]
+ -[PooledNSObject_SL autorelease]
+ -[PooledNSObject_SL dealloc]
+ -[PooledNSObject_SL init]
+ -[PooledNSObject_SL poolOfNSObjects]
+ -[PooledNSObject_SL releaseIntoPoolOfNSObjects]
+ -[PooledNSObject_SL release]
+ -[PooledNSObject_SL retainCount]
+ -[PooledNSObject_SL retain]
+ -[PooledNSObject_SL setPoolOfNSObjects:]
+ -[PooledNSObject_UL .cxx_destruct]
+ -[PooledNSObject_UL autorelease]
+ -[PooledNSObject_UL dealloc]
+ -[PooledNSObject_UL init]
+ -[PooledNSObject_UL poolOfNSObjects]
+ -[PooledNSObject_UL releaseIntoPoolOfNSObjects]
+ -[PooledNSObject_UL release]
+ -[PooledNSObject_UL retainCount]
+ -[PooledNSObject_UL retain]
+ -[PooledNSObject_UL setPoolOfNSObjects:]
+ GCC_except_table14
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table81
+ _AudioBuffersAndFormatToByteBuffer
+ _AudioBuffersAndFormatToNSMutableData
+ _MGCopyAnswer
+ _MGCopyAnswerWithError
+ _OBJC_CLASS_$_AVAudioChannelLayout
+ _OBJC_CLASS_$_AVAudioFormat
+ _OBJC_CLASS_$_AVAudioPCMBuffer
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_PoolOfNSObjects
+ _OBJC_CLASS_$_PoolOfNSObjectsWithCount
+ _OBJC_CLASS_$_PoolOfNSObjectsWithCount_LF
+ _OBJC_CLASS_$_PoolOfNSObjectsWithCount_SL
+ _OBJC_CLASS_$_PoolOfNSObjectsWithCount_UL
+ _OBJC_CLASS_$_PoolOfNSObjects_LF
+ _OBJC_CLASS_$_PoolOfNSObjects_SL
+ _OBJC_CLASS_$_PoolOfNSObjects_UL
+ _OBJC_CLASS_$_PooledNSObject
+ _OBJC_CLASS_$_PooledNSObject_LF
+ _OBJC_CLASS_$_PooledNSObject_SL
+ _OBJC_CLASS_$_PooledNSObject_UL
+ _OBJC_IVAR_$_PoolOfNSObjectsWithCount_LF._count
+ _OBJC_IVAR_$_PoolOfNSObjectsWithCount_LF._head
+ _OBJC_IVAR_$_PoolOfNSObjectsWithCount_SL._pool
+ _OBJC_IVAR_$_PoolOfNSObjectsWithCount_UL._lock
+ _OBJC_IVAR_$_PoolOfNSObjectsWithCount_UL._pool
+ _OBJC_IVAR_$_PoolOfNSObjects_LF._head
+ _OBJC_IVAR_$_PoolOfNSObjects_SL._pool
+ _OBJC_IVAR_$_PoolOfNSObjects_UL._lock
+ _OBJC_IVAR_$_PoolOfNSObjects_UL._pool
+ _OBJC_IVAR_$_PooledNSObject_LF._nextPooledNSObject
+ _OBJC_IVAR_$_PooledNSObject_LF._pooledRetainCount
+ _OBJC_IVAR_$_PooledNSObject_LF.poolOfNSObjects
+ _OBJC_IVAR_$_PooledNSObject_SL._pooledRetainCount
+ _OBJC_IVAR_$_PooledNSObject_SL.poolOfNSObjects
+ _OBJC_IVAR_$_PooledNSObject_UL._pooledRetainCount
+ _OBJC_IVAR_$_PooledNSObject_UL.poolOfNSObjects
+ _OBJC_METACLASS_$_PoolOfNSObjects
+ _OBJC_METACLASS_$_PoolOfNSObjectsWithCount
+ _OBJC_METACLASS_$_PoolOfNSObjectsWithCount_LF
+ _OBJC_METACLASS_$_PoolOfNSObjectsWithCount_SL
+ _OBJC_METACLASS_$_PoolOfNSObjectsWithCount_UL
+ _OBJC_METACLASS_$_PoolOfNSObjects_LF
+ _OBJC_METACLASS_$_PoolOfNSObjects_SL
+ _OBJC_METACLASS_$_PoolOfNSObjects_UL
+ _OBJC_METACLASS_$_PooledNSObject
+ _OBJC_METACLASS_$_PooledNSObject_LF
+ _OBJC_METACLASS_$_PooledNSObject_SL
+ _OBJC_METACLASS_$_PooledNSObject_UL
+ __OBJC_$_CATEGORY_AVAudioPCMBuffer_$_Roya
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVAudioPCMBuffer_$_Roya
+ __OBJC_$_CLASS_METHODS_NSError(initWithCode|initWithException|initWithInvalidArgument)
+ __OBJC_$_CLASS_METHODS_NSException(initWithError|RoyaUtilities|NSInternalInconsistencyException|NSInvalidArgumentException)
+ __OBJC_$_INSTANCE_METHODS_NSError(initWithCode|initWithException|initWithInvalidArgument)
+ __OBJC_$_INSTANCE_METHODS_NSException(initWithError|RoyaUtilities|NSInternalInconsistencyException|NSInvalidArgumentException)
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjectsWithCount_LF
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjectsWithCount_SL
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjectsWithCount_UL
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjects_LF
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjects_SL
+ __OBJC_$_INSTANCE_METHODS_PoolOfNSObjects_UL
+ __OBJC_$_INSTANCE_METHODS_PooledNSObject_LF
+ __OBJC_$_INSTANCE_METHODS_PooledNSObject_SL
+ __OBJC_$_INSTANCE_METHODS_PooledNSObject_UL
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjectsWithCount_LF
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjectsWithCount_SL
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjectsWithCount_UL
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjects_LF
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjects_SL
+ __OBJC_$_INSTANCE_VARIABLES_PoolOfNSObjects_UL
+ __OBJC_$_INSTANCE_VARIABLES_PooledNSObject_LF
+ __OBJC_$_INSTANCE_VARIABLES_PooledNSObject_SL
+ __OBJC_$_INSTANCE_VARIABLES_PooledNSObject_UL
+ __OBJC_$_PROP_LIST_PooledNSObject
+ __OBJC_$_PROP_LIST_PooledNSObject.49
+ __OBJC_$_PROP_LIST_PooledNSObject_LF
+ __OBJC_$_PROP_LIST_PooledNSObject_LF.69
+ __OBJC_$_PROP_LIST_PooledNSObject_SL
+ __OBJC_$_PROP_LIST_PooledNSObject_UL
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PoolOfNSObjects
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PooledNSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PooledNSObject_LF
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PooledNSObject_SL
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PooledNSObject_UL
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PoolOfNSObjects
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PooledNSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PooledNSObject_LF
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PooledNSObject_SL
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PooledNSObject_UL
+ __OBJC_$_PROTOCOL_REFS_PooledNSObject
+ __OBJC_$_PROTOCOL_REFS_PooledNSObject_LF
+ __OBJC_$_PROTOCOL_REFS_PooledNSObject_SL
+ __OBJC_$_PROTOCOL_REFS_PooledNSObject_UL
+ __OBJC_CLASS_PROTOCOLS_$_PoolOfNSObjects
+ __OBJC_CLASS_PROTOCOLS_$_PooledNSObject
+ __OBJC_CLASS_PROTOCOLS_$_PooledNSObject_LF
+ __OBJC_CLASS_PROTOCOLS_$_PooledNSObject_SL
+ __OBJC_CLASS_PROTOCOLS_$_PooledNSObject_UL
+ __OBJC_CLASS_RO_$_PoolOfNSObjects
+ __OBJC_CLASS_RO_$_PoolOfNSObjectsWithCount
+ __OBJC_CLASS_RO_$_PoolOfNSObjectsWithCount_LF
+ __OBJC_CLASS_RO_$_PoolOfNSObjectsWithCount_SL
+ __OBJC_CLASS_RO_$_PoolOfNSObjectsWithCount_UL
+ __OBJC_CLASS_RO_$_PoolOfNSObjects_LF
+ __OBJC_CLASS_RO_$_PoolOfNSObjects_SL
+ __OBJC_CLASS_RO_$_PoolOfNSObjects_UL
+ __OBJC_CLASS_RO_$_PooledNSObject
+ __OBJC_CLASS_RO_$_PooledNSObject_LF
+ __OBJC_CLASS_RO_$_PooledNSObject_SL
+ __OBJC_CLASS_RO_$_PooledNSObject_UL
+ __OBJC_LABEL_PROTOCOL_$_PoolOfNSObjects
+ __OBJC_LABEL_PROTOCOL_$_PooledNSObject
+ __OBJC_LABEL_PROTOCOL_$_PooledNSObject_LF
+ __OBJC_LABEL_PROTOCOL_$_PooledNSObject_SL
+ __OBJC_LABEL_PROTOCOL_$_PooledNSObject_UL
+ __OBJC_METACLASS_RO_$_PoolOfNSObjects
+ __OBJC_METACLASS_RO_$_PoolOfNSObjectsWithCount
+ __OBJC_METACLASS_RO_$_PoolOfNSObjectsWithCount_LF
+ __OBJC_METACLASS_RO_$_PoolOfNSObjectsWithCount_SL
+ __OBJC_METACLASS_RO_$_PoolOfNSObjectsWithCount_UL
+ __OBJC_METACLASS_RO_$_PoolOfNSObjects_LF
+ __OBJC_METACLASS_RO_$_PoolOfNSObjects_SL
+ __OBJC_METACLASS_RO_$_PoolOfNSObjects_UL
+ __OBJC_METACLASS_RO_$_PooledNSObject
+ __OBJC_METACLASS_RO_$_PooledNSObject_LF
+ __OBJC_METACLASS_RO_$_PooledNSObject_SL
+ __OBJC_METACLASS_RO_$_PooledNSObject_UL
+ __OBJC_PROTOCOL_$_PoolOfNSObjects
+ __OBJC_PROTOCOL_$_PooledNSObject
+ __OBJC_PROTOCOL_$_PooledNSObject_LF
+ __OBJC_PROTOCOL_$_PooledNSObject_SL
+ __OBJC_PROTOCOL_$_PooledNSObject_UL
+ __ZN4roya13MobileGestalt10CopyAnswerEPK10__CFStringP12NSDictionary
+ __ZN4roya13MobileGestalt13HardwareModelEv
+ __ZN4roya13MobileGestalt15CopyAnswerOrNilEPK10__CFStringP12NSDictionary
+ __ZN4roya13MobileGestalt18HardwareModelOrNilEv
+ __ZN4roya16MGErrorExceptionD0Ev
+ __ZN4roya16MGErrorExceptionD1Ev
+ __ZN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS_10ref_strongEED1Ev
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt16invalid_argumentC1B9fqe220100EPKc
+ __ZNSt3__112__destroy_atB9fqe220100IN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEEEEvPT_
+ __ZNSt3__112construct_atB9fqe220100IN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEEJS6_EPS6_EEPT_S9_DpOT0_
+ __ZNSt3__114__split_bufferIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEERNS_9allocatorIS6_EEED2Ev
+ __ZNSt3__116allocator_traitsIN4roya18small_vector_allocINS1_11CVPlaneInfoELm4EEEE9constructB9fqe220100IS3_JRKP10__CVBufferRmRbELi0EEEvRS4_PT_DpOT0_
+ __ZNSt3__116allocator_traitsIN4roya18small_vector_allocINS1_11CVPlaneInfoELm4EEEE9constructB9fqe220100IS3_JRKP11__IOSurfaceRmRbELi0EEEvRS4_PT_DpOT0_
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220100INS_9allocatorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS2_10ref_strongEEEEEPS7_EEvRT_T0_SC_SC_
+ __ZNSt3__16vectorIN4roya11CVPlaneInfoENS1_18small_vector_allocIS2_Lm4EEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN4roya19CVPlaneInfoWithDataENS1_18small_vector_allocIS2_Lm4EEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEENS_9allocatorIS6_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEENS_9allocatorIS6_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEENS_9allocatorIS6_EEE9push_backB9fqe220100EOS6_
+ __ZNSt3__19allocatorIN4roya11CVPlaneInfoEE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorIN4roya19CVPlaneInfoWithDataEE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorIN4roya5idrefIPU25objcproto14PooledNSObject11objc_objectNS1_10ref_strongEEEE17allocate_at_leastB9fqe220100Em
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTIN4roya16MGErrorExceptionE
+ __ZTIN4roya19exception_with_codeINS_16MGErrorExceptionEiLi0EEE
+ __ZTSN4roya16MGErrorExceptionE
+ __ZTSN4roya19exception_with_codeINS_16MGErrorExceptionEiLi0EEE
+ __ZTVN4roya16MGErrorExceptionE
+ ___41-[AVAudioPCMBuffer(Roya) initFromNSData:]_block_invoke
+ ___68-[AVAudioPCMBuffer(Roya) initFromByteBufferNoCopy:size:deallocator:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e13_v24?0r^v8Q16ls32l8
+ ___block_descriptor_64_ea8_32s40bs_e49_v16?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8ls32l8s40l8
+ ___objc_personality_v0
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_loadWeak
+ _objc_msgSend$addPooledNSObject:
+ _objc_msgSend$audioBufferList
+ _objc_msgSend$bytes
+ _objc_msgSend$channelLayout
+ _objc_msgSend$errorWithOSStatus:reason:userInfo:
+ _objc_msgSend$format
+ _objc_msgSend$initFromByteBufferNoCopy:size:deallocator:
+ _objc_msgSend$initFromNSData:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithLayout:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithOSStatus:reason:userInfo:
+ _objc_msgSend$initWithPCMFormat:bufferListNoCopy:deallocator:
+ _objc_msgSend$initWithStreamDescription:channelLayout:
+ _objc_msgSend$lastObject
+ _objc_msgSend$layout
+ _objc_msgSend$newPooledNSObject
+ _objc_msgSend$newUserInfoWithArgumentName:
+ _objc_msgSend$newUserInfoWithArgumentName:andValue:
+ _objc_msgSend$nextPooledNSObject
+ _objc_msgSend$null
+ _objc_msgSend$poolOfNSObjects
+ _objc_msgSend$releaseIntoPoolOfNSObjects
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$setLength:
+ _objc_msgSend$setNextPooledNSObject:
+ _objc_msgSend$setPoolOfNSObjects:
+ _objc_msgSend$streamDescription
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_terminate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- +[NSException(NSInternalInconsistencyException) exceptionWithName:]
- +[NSException(NSInternalInconsistencyException) internalInconsistencyWitUserInfo:]
- -[NSException(NSInternalInconsistencyException) initWithName:]
- GCC_except_table20
- GCC_except_table21
- GCC_except_table22
- GCC_except_table35
- GCC_except_table36
- GCC_except_table37
- GCC_except_table40
- GCC_except_table46
- __OBJC_$_CLASS_METHODS_NSError(initWithCode|initWithException)
- __OBJC_$_CLASS_METHODS_NSException(initWithError|NSInternalInconsistencyException)
- __OBJC_$_INSTANCE_METHODS_NSError(initWithCode|initWithException)
- __OBJC_$_INSTANCE_METHODS_NSException(initWithError|NSInternalInconsistencyException)
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt16invalid_argumentC1B9nqe210106EPKc
- __ZNSt3__116allocator_traitsIN4roya18small_vector_allocINS1_11CVPlaneInfoELm4EEEE9constructB9nqe210106IS3_JRKP10__CVBufferRmRbELi0EEEvRS4_PT_DpOT0_
- __ZNSt3__116allocator_traitsIN4roya18small_vector_allocINS1_11CVPlaneInfoELm4EEEE9constructB9nqe210106IS3_JRKP11__IOSurfaceRmRbELi0EEEvRS4_PT_DpOT0_
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__16vectorIN4roya11CVPlaneInfoENS1_18small_vector_allocIS2_Lm4EEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIN4roya19CVPlaneInfoWithDataENS1_18small_vector_allocIS2_Lm4EEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__19allocatorIN4roya11CVPlaneInfoEE17allocate_at_leastB9nqe210106Em
- __ZNSt3__19allocatorIN4roya19CVPlaneInfoWithDataEE17allocate_at_leastB9nqe210106Em
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZZ20roya_os_log_instanceE8instance
- __ZZ20roya_os_log_instanceE9onceToken
- ___block_descriptor_tmp
- ___roya_os_log_instance_block_invoke
- _dispatch_once
- _objc_retainAutoreleasedReturnValue
- _os_log_create
- _roya_os_log_instance
CStrings:
+ "HWModelStr"
+ "v16@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8"
+ "v24@?0r^v8Q16"
+ "value"
- "#16@0:8"
- "*"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8*16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{__CVBuffer=}16"
- "@24@0:8^{__IOSurface=}16"
- "@24@0:8q16"
- "@28@0:8^{__IOSurface=}16I24"
- "@32@0:8:16@24"
- "@32@0:8@16*24"
- "@32@0:8@16@24"
- "@32@0:8^v16Q24"
- "@32@0:8^{__CVBuffer=}16Q24"
- "@32@0:8^{__IOSurface=}16Q24"
- "@36@0:8^v16Q24B32"
- "@36@0:8i16@20@28"
- "@40@0:8:16@24@32"
- "@40@0:8^v16Q24@?32"
- "@48@0:8@16@24@32@40"
- "@80@0:8@16@24@32@40@48@56Q64@?72"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CVPixelBufferInfo"
- "CVPixelBufferInfoWithCVPixelBuffer"
- "CVPixelBufferInfoWithIOSurface"
- "NSAutoCondition"
- "NSBoolAutoCondition"
- "NSDataWithIOSurface"
- "NSIntAutoCondition"
- "NSInternalInconsistencyException"
- "NSLocking"
- "NSMutableDataNoCopy"
- "NSMutableDataWithIOSurface"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSError\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,R,N,V_deallocator"
- "TB,R,N"
- "TQ,R"
- "TQ,R,N,V_capacity"
- "T^{__CVBuffer=},R,N"
- "T^{__IOSurface=},R,N"
- "Tq,R,N"
- "Tr^v,R,N"
- "Vv16@0:8"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CVBuffer=}16@0:8"
- "^{__IOSurface=}16@0:8"
- "_buffer"
- "_capacity"
- "_cvbuffer"
- "_data"
- "_deallocator"
- "_info"
- "_initWithBytesNoCopy:length:deallocator:"
- "_initWithBytesNoCopy:length:freeWhenDone:"
- "_initialStatus"
- "_iosurface"
- "_length"
- "_mutableBytes"
- "_signaled"
- "_status"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "autorelease"
- "broadcast"
- "broadcast:"
- "bytes"
- "capacity"
- "class"
- "clear"
- "conformsToProtocol:"
- "count"
- "data"
- "dealloc"
- "deallocator"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "doesNotRecognizeSelector:"
- "errorWithCocoaError:reason:userInfo:"
- "errorWithDomain:code:userInfo:"
- "errorWithErrno:reason:userInfo:"
- "errorWithException:"
- "errorWithException:userInfo:"
- "errorWithIOReturn:reason:userInfo:"
- "errorWithKernReturn:reason:userInfo:"
- "errorWithOSStatus:reason:userInfo:"
- "exceptionWithError:"
- "exceptionWithError:name:reason:userInfo:"
- "exceptionWithError:reason:"
- "exceptionWithName:"
- "exceptionWithName:reason:userInfo:"
- "hash"
- "indexOfObjectIdenticalTo:"
- "info"
- "init"
- "init:"
- "init:flags:"
- "init:options:"
- "initInternalInconsistency"
- "initInternalInconsistencyWithReason:"
- "initInternalInconsistencyWithReason:andUserInfo:"
- "initInternalInconsistencyWithUserInfo:"
- "initWithBytesNoCopy:length:"
- "initWithBytesNoCopy:length:deallocator:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCVDataBuffer:"
- "initWithCVPixelBuffer:"
- "initWithCapacity:"
- "initWithCocoaError:reason:userInfo:"
- "initWithCode"
- "initWithDictionaries"
- "initWithDictionaries:"
- "initWithDictionaries:V:"
- "initWithDictionariesA:"
- "initWithDictionariesV:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithErrno:reason:userInfo:"
- "initWithError"
- "initWithError:"
- "initWithError:name:reason:userInfo:"
- "initWithError:reason:"
- "initWithException"
- "initWithException:"
- "initWithException:userInfo:"
- "initWithIOReturn:reason:userInfo:"
- "initWithIOSurface:"
- "initWithIOSurface:length:"
- "initWithKernReturn:reason:userInfo:"
- "initWithName:"
- "initWithName:reason:userInfo:"
- "initWithOSStatus:reason:userInfo:"
- "insertObject:atIndex:"
- "internalInconsistency"
- "internalInconsistencyWitUserInfo:"
- "internalInconsistencyWithReason:"
- "internalInconsistencyWithReason:andUserInfo:"
- "iosurface"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "lock"
- "mutableBytes"
- "nextObject"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "r^v16@0:8"
- "reason"
- "release"
- "replaceBytesInRange:withBytes:"
- "replaceBytesInRange:withBytes:length:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setData:"
- "setLength:"
- "setObject:forKeyedSubscript:"
- "signal"
- "signal:"
- "signaled"
- "sortedArrayWithOptions:usingComparator:"
- "status"
- "stringWithFormat:"
- "superclass"
- "toStringSorted"
- "toStringSorted:ifNil:sep:bra:mid:ket:options:compare:"
- "underlyingError"
- "unlock"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8r^v16Q24"
- "v40@0:8{_NSRange=QQ}16r^v32"
- "v48@0:8{_NSRange=QQ}16r^v32Q40"
- "v8@?0"
- "wait"
- "waitUntilDate:"
- "zone"
- "{CVPixelBufferInfo=\"pixelFormat\"{_FourCharCode=\"value\"I}\"extendedPixels\"{CVMargins=\"top\"Q\"right\"Q\"bottom\"Q\"left\"Q}\"buffer\"{CVPlaneInfo=\"width\"Q\"height\"Q\"bytesPerRow\"Q}\"planes\"{small_vector<roya::CVPlaneInfo, 4UL>=\"__begin_\"^{CVPlaneInfo}\"__end_\"^{CVPlaneInfo}\"\"{?=\"__cap_\"^{CVPlaneInfo}\"__alloc_\"{small_vector_alloc<roya::CVPlaneInfo, 4UL>=\"a\"{array<roya::CVPlaneInfo, 4UL>=\"__elems_\"[4{CVPlaneInfo=\"width\"Q\"height\"Q\"bytesPerRow\"Q}]}}}\"a\"{small_vector_alloc<roya::CVPlaneInfo, 4UL>=\"a\"{array<roya::CVPlaneInfo, 4UL>=\"__elems_\"[4{CVPlaneInfo=\"width\"Q\"height\"Q\"bytesPerRow\"Q}]}}}}"
- "{CVPixelBufferInfoWithData=\"pixelFormat\"{_FourCharCode=\"value\"I}\"extendedPixels\"{CVMargins=\"top\"Q\"right\"Q\"bottom\"Q\"left\"Q}\"buffer\"{CVPlaneInfoWithData=\"width\"Q\"height\"Q\"bytesPerRow\"Q\"size\"Q\"data\"^v}\"planes\"{small_vector<roya::CVPlaneInfoWithData, 4UL>=\"__begin_\"^{CVPlaneInfoWithData}\"__end_\"^{CVPlaneInfoWithData}\"\"{?=\"__cap_\"^{CVPlaneInfoWithData}\"__alloc_\"{small_vector_alloc<roya::CVPlaneInfoWithData, 4UL>=\"a\"{array<roya::CVPlaneInfoWithData, 4UL>=\"__elems_\"[4{CVPlaneInfoWithData=\"width\"Q\"height\"Q\"bytesPerRow\"Q\"size\"Q\"data\"^v}]}}}\"a\"{small_vector_alloc<roya::CVPlaneInfoWithData, 4UL>=\"a\"{array<roya::CVPlaneInfoWithData, 4UL>=\"__elems_\"[4{CVPlaneInfoWithData=\"width\"Q\"height\"Q\"bytesPerRow\"Q\"size\"Q\"data\"^v}]}}}}"
- "{LockableSafeRef<roya::_IOSurfaceSafeRefHandler, 0U>=\"p\"{TaggedRef=\"_tagged\"^{__IOSurface}}}"
- "{LockableSafeRef<roya::_IOSurfaceSafeRefHandler, 1U>=\"p\"{TaggedRef=\"_tagged\"^{__IOSurface}}}"
- "{LockableSafeRefWithFlags<roya::_CVPixelBufferSafeRefHandler>=\"p\"{TaggedRef=\"_tagged\"^{__CVBuffer}}\"_flags\"Q}"
- "{LockableSafeRefWithFlags<roya::_IOSurfaceSafeRefHandler>=\"p\"{TaggedRef=\"_tagged\"^{__IOSurface}}\"_flags\"I}"
- "{cvref<roya::CVBuffer_, roya::CVBuffer_>=\"p\"^{__CVBuffer}}"

```
