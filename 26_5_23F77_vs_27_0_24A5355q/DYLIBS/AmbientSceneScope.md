## AmbientSceneScope

> `/System/Library/PrivateFrameworks/AmbientSceneScope.framework/AmbientSceneScope`

```diff

-1.23.0.0.0
-  __TEXT.__text: 0x1c3e4
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__cstring: 0x8d6
-  __TEXT.__const: 0xbc0
-  __TEXT.__gcc_except_tab: 0x1790
-  __TEXT.__oslogstring: 0x12d
-  __TEXT.__unwind_info: 0x860
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x38
+9.26.4.12.0
+  __TEXT.__text: 0x51c9f0
+  __TEXT.__cstring: 0x1048a
+  __TEXT.__const: 0x498b0
+  __TEXT.__gcc_except_tab: 0x48658
+  __TEXT.__oslogstring: 0xfbc
+  __TEXT.__unwind_info: 0x122f8
+  __TEXT.__eh_frame: 0x50
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0x840
-  __DATA.__data: 0xc0
+  __DATA_CONST.__weak_got: 0x28
+  __DATA_CONST.__objc_selrefs: 0x18
+  __DATA_CONST.__got: 0x2f8
+  __AUTH_CONST.__const: 0x20548
+  __AUTH_CONST.__cfstring: 0x2a0
+  __AUTH_CONST.__weak_auth_got: 0x30
+  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH.__data: 0x18
+  __DATA.__data: 0x1e00
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2b0
-  __DATA.__common: 0x60
+  __DATA.__bss: 0xf20
+  __DATA.__common: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: DABB47CC-A1C9-3097-9A1B-B4BFF7F760B6
-  Functions: 289
-  Symbols:   171
-  CStrings:  80
+  - /usr/lib/libobjc.A.dylib
+  UUID: D832B23E-ED81-36BD-9502-F43C00CB3F73
+  Functions: 11095
+  Symbols:   625
+  CStrings:  1673
 
Symbols:
+ _AmbientSceneFrameBundleCreateWithHeadOrientation
+ _AmbientSceneFrameBundleCreateWithOrientation
+ _AmbientSceneFusionResultGetSectorSceneTypes
+ _AmbientSceneFusionResultGetSectorizedMetadata
+ _AmbientSceneFusionResultHasSectorizedData
+ _AmbientSceneHeadOrientationCreate
+ _AmbientSceneHeadOrientationRelease
+ _AmbientSceneLeakyIntegratorConfigGetDefaults
+ _AmbientSceneLoggingDisable
+ _AmbientSceneLoggingEnableLogger
+ _AmbientSceneLoggingEnableLoggingToDestination
+ _AmbientSceneLoggingEnableLoggingToFile
+ _AmbientSceneLoggingEnableLoggingToHost
+ _AmbientSceneLoggingSync
+ _AmbientSceneSectorizedConfigGetDefaults
+ _AmbientSceneSessionConfigCreateForStrategy
+ _AmbientSceneSessionConfigCreateWithAggregatorParams
+ _AmbientSceneSessionConfigCreateWithDefaults
+ _AmbientSceneSessionConfigCreateWithSectorizedParams
+ _AmbientSceneSpatioTemporalConfigGetDefaults
+ _CFAllocatorCreate
+ _CFArrayGetTypeID
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFBundleCopyBundleURL
+ _CFBundleCopyExecutableURL
+ _CFBundleGetMainBundle
+ _CFBundleGetTypeID
+ _CFCopyDescription
+ _CFDataCreateWithBytesNoCopy
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryContainsKey
+ _CFDictionaryCreate
+ _CFDictionaryCreateMutableCopy
+ _CFDictionaryGetCount
+ _CFDictionaryGetKeysAndValues
+ _CFEqual
+ _CFErrorCopyFailureReason
+ _CFErrorCopyUserInfo
+ _CFErrorGetCode
+ _CFErrorGetDomain
+ _CFNumberGetType
+ _CFStringCreateWithCString
+ _CFURLCopyFileSystemPath
+ _CFURLCopyScheme
+ _CFURLGetString
+ _CFURLGetTypeID
+ _CGColorSpaceCreateDeviceCMYK
+ _CGColorSpaceCreateDeviceGray
+ _CGColorSpaceCreateDeviceRGB
+ _CGColorSpaceGetModel
+ _CGColorSpaceGetNumberOfComponents
+ _CGColorSpaceGetTypeID
+ _CGDataConsumerCreate
+ _CGDataConsumerGetTypeID
+ _CGDataProviderCopyData
+ _CGDataProviderCreateSequential
+ _CGDataProviderCreateWithCFData
+ _CGDataProviderGetTypeID
+ _CGImageCreate
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithDataConsumer
+ _CGImageDestinationFinalize
+ _CGImageDestinationGetTypeID
+ _CGImageGetAlphaInfo
+ _CGImageGetBitmapInfo
+ _CGImageGetBitsPerComponent
+ _CGImageGetBitsPerPixel
+ _CGImageGetByteOrderInfo
+ _CGImageGetBytesPerRow
+ _CGImageGetColorSpace
+ _CGImageGetDataProvider
+ _CGImageGetHeight
+ _CGImageGetPixelFormatInfo
+ _CGImageGetTypeID
+ _CGImageGetWidth
+ _CGImageSourceCreateImageAtIndex
+ _CGImageSourceCreateWithDataProvider
+ _CGImageSourceGetTypeID
+ _CVPixelBufferCreate
+ _CVPixelBufferGetBaseAddressOfPlane
+ _CVPixelBufferGetBytesPerRow
+ _CVPixelBufferGetHeight
+ _CVPixelBufferGetIOSurface
+ _CVPixelBufferGetPlaneCount
+ _CVPixelBufferGetTypeID
+ _CVPixelBufferGetWidth
+ _CVPixelBufferLockBaseAddress
+ _CVPixelBufferUnlockBaseAddress
+ _IOSurfaceGetBaseAddressOfPlane
+ _IOSurfaceGetPlaneCount
+ _IOSurfaceGetTypeID
+ _MGCopyAnswer
+ _MGGetSInt32Answer
+ _MGGetSInt64Answer
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_NSProcessInfo
+ _VZBlobCreateWithBytes
+ _VZBlobCreateWithCFDataNoCopy
+ _VZCameraCreate
+ _VZCameraSetHeikkilaLensParametersD
+ _VZCameraSetHeikkilaLensParametersF
+ _VZCameraSetImageSize
+ _VZCameraSetPinholeLensParametersD
+ _VZCameraSetPinholeLensParametersF
+ _VZDataCreateWithBlob
+ _VZDataCreateWithCamera
+ _VZDataCreateWithDictionary
+ _VZDataCreateWithImage
+ _VZDataCreateWithLines2
+ _VZDataCreateWithLines3
+ _VZDataCreateWithMesh
+ _VZDataCreateWithNumber
+ _VZDataCreateWithNumbers
+ _VZDataCreateWithPoints2
+ _VZDataCreateWithPoints3
+ _VZDataCreateWithTransform3
+ _VZDataIOImportLogMessageFromBlob
+ _VZDataInfoAddReference
+ _VZDataInfoCreate
+ _VZDataInfoSetInstanceID
+ _VZDataInfoSetLogTimestampNanoseconds
+ _VZDataInfoSetName
+ _VZDataInfoSetSpace
+ _VZDataInfoSetTimestampChronologicalNanoseconds
+ _VZDataInfoSetTimestampMachContinuousNanoseconds
+ _VZDataInfoSetTimestampSteadyNanoseconds
+ _VZDictionaryCreateWithCFDictionary
+ _VZImageCreateCopy
+ _VZImageCreateDefault
+ _VZImageCreateWithBytes
+ _VZImageCreateWithCVPixelBuffer
+ _VZLines2Create
+ _VZLines3Create
+ _VZLogMessageCreateFromContextIDString
+ _VZLoggerAddDestination
+ _VZLoggerCreate
+ _VZLoggerLogMessage
+ _VZLoggerSetEnableState
+ _VZMeshCreate
+ _VZMeshSetFaceColors
+ _VZMeshSetFaceLabels
+ _VZMeshSetFaceNormals
+ _VZMeshSetFaces
+ _VZMeshSetVertexColors
+ _VZMeshSetVertexLabels
+ _VZMeshSetVertexNormals
+ _VZMeshSetVertices
+ _VZNumberCreate
+ _VZNumbersCreate
+ _VZPoints2Create
+ _VZPoints3Create
+ _VZReferenceIDCreateWithInstanceID
+ _VZRelease
+ _VZRetain
+ _VZSE3CreateWithAffine3x4D
+ _VZSE3CreateWithAffine3x4F
+ _VZSE3CreateWithAlgebraD
+ _VZSE3CreateWithAlgebraF
+ _VZTransform3Create
+ __DefaultRuneLocale
+ __ZNKSt13runtime_error4whatEv
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__123__match_any_but_newlineIcE6__execERNS_7__stateIcEE
+ __ZNKSt3__14__fs10filesystem18directory_iterator13__dereferenceEv
+ __ZNKSt3__14__fs10filesystem4path16__root_directoryEv
+ __ZNKSt3__14__fs10filesystem4path18lexically_relativeERKS2_
+ __ZNKSt3__14__fs10filesystem4path6__stemEv
+ __ZNKSt3__16locale4nameEv
+ __ZNKSt8bad_cast4whatEv
+ __ZNKSt9exception4whatEv
+ __ZNSt11logic_errorC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt11logic_errorC2ERKS_
+ __ZNSt12domain_errorD1Ev
+ __ZNSt13exception_ptr31__from_native_exception_pointerEPv
+ __ZNSt13exception_ptrC1ERKS_
+ __ZNSt13exception_ptrD1Ev
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt13runtime_errorC1ERKS_
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt13runtime_errorC2ERKS_
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt13runtime_errorD2Ev
+ __ZNSt14overflow_errorD1Ev
+ __ZNSt3__111__call_onceERVmPvPFvS2_E
+ __ZNSt3__111regex_errorC1ENS_15regex_constants10error_typeE
+ __ZNSt3__111regex_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ __ZNSt3__112future_errorC1ENS_10error_codeE
+ __ZNSt3__112future_errorD1Ev
+ __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEEC1Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE4peekEv
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE4readEPcl
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE5seekgExNS_8ios_base7seekdirE
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE5tellgEv
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED1Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERd
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERf
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERi
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERj
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERs
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERt
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERx
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERy
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEPKv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEb
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEl
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEs
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEt
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEy
+ __ZNSt3__113random_deviceC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZNSt3__113random_deviceD1Ev
+ __ZNSt3__113random_deviceclEv
+ __ZNSt3__114__shared_countD2Ev
+ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj
+ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj
+ __ZNSt3__115__get_classnameEPKcb
+ __ZNSt3__115__thread_structC1Ev
+ __ZNSt3__115__thread_structD1Ev
+ __ZNSt3__115future_categoryEv
+ __ZNSt3__115recursive_mutex4lockEv
+ __ZNSt3__115recursive_mutex6unlockEv
+ __ZNSt3__115recursive_mutexC1Ev
+ __ZNSt3__115recursive_mutexD1Ev
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__117__assoc_sub_state13set_exceptionESt13exception_ptr
+ __ZNSt3__117__assoc_sub_state4waitEv
+ __ZNSt3__117__assoc_sub_state9__executeEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__117iostream_categoryEv
+ __ZNSt3__118condition_variable10notify_allEv
+ __ZNSt3__118condition_variable10notify_oneEv
+ __ZNSt3__118condition_variable15__do_timed_waitERNS_11unique_lockINS_5mutexEEENS_6chrono10time_pointINS5_12system_clockENS5_8durationIxNS_5ratioILl1ELl1000000000EEEEEEE
+ __ZNSt3__118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__119__shared_mutex_base11lock_sharedEv
+ __ZNSt3__119__shared_mutex_base13unlock_sharedEv
+ __ZNSt3__119__shared_mutex_base4lockEv
+ __ZNSt3__119__shared_mutex_base6unlockEv
+ __ZNSt3__119__shared_mutex_baseC1Ev
+ __ZNSt3__119__shared_weak_count4lockEv
+ __ZNSt3__119__thread_local_dataEv
+ __ZNSt3__120__get_collation_nameEPKc
+ __ZNSt3__120__throw_system_errorEiPKc
+ __ZNSt3__14__fs10filesystem10__absoluteERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem11__canonicalERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem11__copy_fileERKNS1_4pathES4_NS1_12copy_optionsEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem11__file_sizeERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem12__equivalentERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem12__remove_allERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem13__fs_is_emptyERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem13__permissionsERKNS1_4pathENS1_5permsENS1_12perm_optionsEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem13__resize_fileERKNS1_4pathEmPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem14__copy_symlinkERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem14__current_pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem14__current_pathERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem14__read_symlinkERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem16_FilesystemClock3nowEv
+ __ZNSt3__14__fs10filesystem16__create_symlinkERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem16__symlink_statusERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem17__hard_link_countERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem17__last_write_timeERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18__create_directoryERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18__create_directoryERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18__create_hard_linkERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18directory_iterator11__incrementEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem18directory_iteratorC1ERKNS1_4pathEPNS_10error_codeENS1_17directory_optionsE
+ __ZNSt3__14__fs10filesystem20__create_directoriesERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem21__temp_directory_pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem26__create_directory_symlinkERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14__fs10filesystem6__copyERKNS1_4pathES4_NS1_12copy_optionsEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem7__spaceERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem8__removeERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem8__renameERKNS1_4pathES4_PNS_10error_codeE
+ __ZNSt3__14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm
+ __ZNSt3__14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm
+ __ZNSt3__14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ __ZNSt3__16futureIvED1Ev
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ __ZNSt3__16thread4joinEv
+ __ZNSt3__16threadD1Ev
+ __ZNSt3__17collateIcE2idE
+ __ZNSt3__17promiseIvE10get_futureEv
+ __ZNSt3__17promiseIvE13set_exceptionESt13exception_ptr
+ __ZNSt3__17promiseIvE9set_valueEv
+ __ZNSt3__17promiseIvEC1Ev
+ __ZNSt3__17promiseIvED1Ev
+ __ZNSt3__18ios_base4moveERS0_
+ __ZNSt3__18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
+ __ZNSt3__18ios_base7failureD1Ev
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ __ZNSt3__19to_stringEd
+ __ZNSt3__19to_stringEf
+ __ZNSt3__19to_stringEj
+ __ZNSt3__19to_stringEl
+ __ZNSt3__19to_stringEx
+ __ZNSt3__19to_stringEy
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZNSt8bad_castC2Ev
+ __ZNSt8bad_castD2Ev
+ __ZNSt9bad_allocC1Ev
+ __ZNSt9bad_allocD1Ev
+ __ZSt17current_exceptionv
+ __ZSt17rethrow_exceptionSt13exception_ptr
+ __ZTINSt3__111regex_errorE
+ __ZTINSt3__112future_errorE
+ __ZTINSt3__117__assoc_sub_stateE
+ __ZTINSt3__117bad_function_callE
+ __ZTINSt3__14__fs10filesystem16filesystem_errorE
+ __ZTINSt3__18ios_base7failureE
+ __ZTISt12domain_error
+ __ZTISt13runtime_error
+ __ZTISt14overflow_error
+ __ZTISt8bad_cast
+ __ZTISt9bad_alloc
+ __ZTISt9exception
+ __ZTTNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __ZTTNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__112future_errorE
+ __ZTVNSt3__113basic_istreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__113basic_ostreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__117__assoc_sub_stateE
+ __ZTVNSt3__117bad_function_callE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__19basic_iosIcNS_11char_traitsIcEEEE
+ __ZTVSt12domain_error
+ __ZTVSt14overflow_error
+ ___CFConstantStringClassReference
+ ___chkstk_darwin
+ ___cxa_atexit
+ ___cxa_init_primary_exception
+ ___cxa_pure_virtual
+ ___darwin_check_fd_set_overflow
+ ___dynamic_cast
+ ___error
+ ___exp10
+ ___maskrune
+ ___sincos_stret
+ ___sincosf_stret
+ ___tolower
+ ___udivti3
+ ___umodti3
+ _accept
+ _acos
+ _acosf
+ _asin
+ _asinf
+ _atan2f
+ _atoi
+ _close
+ _connect
+ _dispatch_activate
+ _dispatch_group_async_f
+ _dispatch_group_create
+ _dispatch_group_wait
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_set_target_queue
+ _dispatch_sync_f
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_os_workgroup
+ _dispatch_workloop_set_qos_class_floor
+ _dispatch_workloop_set_scheduler_priority
+ _fcntl
+ _freeaddrinfo
+ _getaddrinfo
+ _getpid
+ _getsockname
+ _getsockopt
+ _inet_ntop
+ _kCFAllocatorNull
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFErrorFilePathKey
+ _kCFErrorUnderlyingErrorKey
+ _kCFNull
+ _kCVPixelBufferBytesPerRowAlignmentKey
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPlaneAlignmentKey
+ _kCVPixelBufferWidthKey
+ _kVZArgOptionsDefault
+ _kVZMatrixLayoutColMajor
+ _kVZMeshLabelTypeConfidence
+ _kVZMeshLabelTypeMaterial
+ _kVZMeshLabelTypeSemantic
+ _kVZPixelOriginCenter
+ _kVZPixelOriginCorner
+ _kVZValueTypeF32
+ _kVZValueTypeU8
+ _localeconv
+ _mach_continuous_time
+ _mach_task_self_
+ _mach_timebase_info
+ _malloc_type_aligned_alloc
+ _malloc_type_malloc
+ _malloc_type_realloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_release_x19
+ _objc_release_x20
+ _objc_retainAutorelease
+ _os_log_pack_send
+ _pthread_create
+ _pthread_getname_np
+ _pthread_setname_np
+ _pthread_setspecific
+ _recv
+ _remainderf
+ _sched_yield
+ _select
+ _send
+ _setsockopt
+ _shutdown
+ _snprintf
+ _socket
+ _strerror
+ _strtod
+ _strtof
+ _strtol
+ _strtoll
+ _strtoull
+ _vm_allocate
+ _vm_deallocate
- _AmbientSceneFrameBundleCreateWithSceneTypesAndConfidences
- _AmbientSceneSessionGetIndoorOutdoorDynamicParams
- _AmbientSceneSessionGetScenesDynamicParams
CStrings:
+ "\n}"
+ " "
+ " \t\n\v\f\r"
+ "  "
+ "      back: base=%.4f, scale=%.4f, min=%.4f, max=%.4f"
+ "      front: base=%.4f, scale=%.4f, min=%.4f, max=%.4f"
+ "      left: base=%.4f, scale=%.4f, min=%.4f, max=%.4f"
+ "      right: base=%.4f, scale=%.4f, min=%.4f, max=%.4f"
+ "    Cone decay params:"
+ "    aggregator_output_top_k: %zu"
+ "    base_decay_rate: %.4f"
+ "    base_window_expiry_duration_secs: %.2f"
+ "    camera_fov_rad: %.4f"
+ "    decay_rate_scale: %.4f"
+ "    fill_rate_scale: %.4f"
+ "    left_camera_horizontal_angle_rad: %.4f"
+ "    max_decay_rate: %.4f"
+ "    max_window_expiry_duration_secs: %.2f"
+ "    min_bucket_output_threshold: %.4f"
+ "    min_decay_rate: %.4f"
+ "    min_window_expiry_duration_secs: %.2f"
+ "    right_camera_horizontal_angle_rad: %.4f"
+ "    sector_output_top_k: %zu"
+ "    smoothing_factor: %.4f"
+ "    strict_output_confidence_threshold: %.4f"
+ "    use_per_frame_calibration: %s"
+ "    window_shrink_scale: %.4f"
+ "   ]"
+ "  #"
+ "  %s:"
+ " (e.g. '10MB') but is '"
+ " (with port in [0,65535]) but is '"
+ " .\\/:*?|<>\""
+ " and size "
+ " and time "
+ " at line "
+ " before newest timestamp"
+ " but current sample version is "
+ " but file contains "
+ " but image is of color format "
+ " but must be 8-bit Gray or Rgb to save as pnm."
+ " but no specialization is available. "
+ " but pnm file contains "
+ " but should be "
+ " but the image is of incompatible format "
+ " bytes with alignment "
+ " can't be saved with CoreGraphics."
+ " cannot be created with default arguments"
+ " characters, but has "
+ " connected to server at "
+ " data."
+ " does not allow the "
+ " encountered during loading is unrecognized. A data type ID of 0 indicates a serialization error (e.g. invalid data in the stream)"
+ " encountered during loading is unrecognized. The loader's package version may be too old."
+ " error "
+ " for format "
+ " format, but file contains "
+ " formatting argument"
+ " from an "
+ " from stream with file format "
+ " heikkila parameters"
+ " in "
+ " incompatible with pnm."
+ " into Image of format "
+ " invalid. "
+ " is added to a logger "
+ " is incompatible with current version "
+ " is not a valid pnm format."
+ " is not serializable"
+ " is processing only the first encountered timestamp, which was '"
+ " not yet supported."
+ " pinhole parameters"
+ " received a command to update its "
+ " separator"
+ " to "
+ " was requested of `Number` containing "
+ " was requested of `Numbers` containing "
+ " which is not in the provided type list "
+ " with LimitedRecorder"
+ "!controlled_visuallogger.lock()"
+ "!internal_logger.get().hasLogLevel()"
+ "\""
+ "\"\""
+ "\":"
+ "\": "
+ "\"bytes\": ["
+ "\"subtype\": "
+ "#"
+ "%.2X"
+ "%020llu"
+ "%d"
+ "%s: Config string contains more than one file path; first path: '%s'; following path '%s' ignored"
+ "%s: Config string contains more than one recorder; first recorder: '%s'; following recorder '%s' ignored"
+ "%s: Config string contains more than one server address; first address: '%s'; following address '%s' ignored"
+ "%s: Enabling log contexts: %s"
+ "%s: Failed to start logging to file at '%s': %s"
+ "%s: Failed to start logging to file at '%s': another file exporter already exists at the same location"
+ "%s: Failed to start logging via network to server at '%s' : %s"
+ "%s: Invalid config string '%s': %s"
+ "%s: Not enabling any log contexts"
+ "%s: Not enabling any log contexts since logger has no destinations"
+ "%s: Starting logging to file at '%s'"
+ "%s: Starting logging to local server '%s'"
+ "%s: Starting logging to recorder with: maximum_message_age=%s, maximum_record_count=%s"
+ "%s: Starting logging to recorder without maximum data age/count limits"
+ "%s: Starting logging via network to server at '%s'"
+ "%s: Stopping logging to file at '%s'"
+ "%s: Stopping logging to recorder"
+ "%s: Stopping logging via network"
+ "'"
+ "' (="
+ "' data type id "
+ "' encountered during loading is unrecognized. An empty package name indicates a serialization error (e.g. invalid data in the stream)"
+ "' encountered during loading is unrecognized. To load data of this package, add the corresponding `Package` to the package-list in `SharedDataSample` or importer constructor or arguments by using the 'PackageList' function"
+ "' for fields and rows"
+ "' sequence protocol version "
+ "' since it is also used as "
+ "' too long. Must have at most "
+ "'\"'"
+ "', expected "
+ "', it already has an active configuration '"
+ "', must be '{int size}[kb|mb|gb]'"
+ "','"
+ "'."
+ "'. Expected pattern 'major.minor.revision'"
+ "'. Info file '"
+ "'. Reason: "
+ "'. Thread already has name '"
+ "'. Use allow_overwrite=true to replace name."
+ "':'"
+ "'['"
+ "'[', '{', or a literal"
+ "']'"
+ "'host:port'"
+ "'host[:port]'"
+ "'{'"
+ "'}'"
+ "("
+ "(\\d*) ?(kb|mb|gb)?"
+ "(bytes_per_row % bytes_per_pixel == 0)"
+ "(mesh.colors.empty() || mesh.colors.size() == mesh.vertices.size())"
+ "(mesh.colors_type == TriMeshMetadataType::PerVertex || mesh.colors_type == TriMeshMetadataType::Unknown)"
+ "(mesh.normals_type == TriMeshMetadataType::PerVertex || mesh.normals_type == TriMeshMetadataType::Unknown)"
+ "(mesh.tex_faces.empty())"
+ "(mesh.tex_faces.size() == mesh.faces.size())"
+ ")"
+ ") "
+ "), "
+ ")}"
+ ",\n"
+ ", "
+ ", Size: "
+ ", bits_per_component="
+ ", bits_per_pixel="
+ ", but contains "
+ ", but is not supported by "
+ ", column "
+ ", cx,cy: "
+ ", dst: "
+ ", error: "
+ ", expected "
+ ", expected [Algebra|Affine][F|D]"
+ ", expected [Center|Corner][Pinhole|Heikkila][F|D]"
+ ", expected [u|i|f][{size}]"
+ ", expected one of "
+ ", float_components="
+ ", forgotten: "
+ ", k1,..,k"
+ ", k1,k2,p1,p2,k3: "
+ ", max queue size "
+ ", min="
+ ", reason: "
+ ", server object has been destroyed"
+ ", transform:"
+ ", used attributes:\n"
+ ", values = {\n"
+ ",;"
+ "- "
+ "-inf"
+ ". Minimum version required is "
+ ".*"
+ ".csv"
+ ".json"
+ ".obj"
+ ".png"
+ ".tiff"
+ ".workloop"
+ "/"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Dispatch/src/DispatchQueue.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Dispatch/src/DispatchQueueTypeUtil.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Dispatch/src/GrandCentralDispatchUtil.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/IO/include/Essentials/IO/Archive.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Essentials/Log/src/APILogging.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/include/Kit/Concurrency/Channel/Node.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ChannelInputModel.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/Processor.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ProcessorInputMessageHandlingStrategy.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/src/Channel/NodeTaskScheduler.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Concurrency/src/Channel/NodeTaskSchedulerPool.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Container/src/Lines.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Container/src/Points.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreGraphics/src/ImageRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/BundleRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/DictionaryRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/ErrorRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/NumberRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/Ref.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Foundation/src/URLRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/src/ImageStorage.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Image/src/Size.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Apple.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/src/ImageIO.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Pnm.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/ImageIO/src/Serialization.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Mesh/src/TriMesh.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Mesh/src/TriMeshAllocator.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Mesh/src/TriMeshIO.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/include/Kit/Visualization/IData.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/Client.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/DataIO.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/DataType.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/FileIOPrivate.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/IData.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/NamedContext.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/NetworkData.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/Kit/Visualization/src/VisualLogger.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AmbientSceneScope/library/VL/Bridge/src/APIBridge.cpp"
+ "/dev/urandom"
+ "0 == mach_timebase_info(&timebase)"
+ "01"
+ "01234567"
+ "0123456789"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "127.0.0.1"
+ "128RGBAFloat"
+ "14Bayer_BGGR"
+ "14Bayer_GBRG"
+ "14Bayer_GRBG"
+ "14Bayer_RGGB"
+ "16BE555"
+ "16BE565"
+ "16Gray"
+ "16LE555"
+ "16LE5551"
+ "16LE565"
+ "16VersatileBayer"
+ "1IndexedGray_WhiteIsZero"
+ "1Monochrome"
+ "24BGR"
+ "24RGB"
+ "2Indexed"
+ "2IndexedGray_WhiteIsZero"
+ "30RGB"
+ "30RGBLEPackedWideGamut"
+ "32ABGR"
+ "32ARGB"
+ "32AlphaGray"
+ "32BGRA"
+ "32RGBA"
+ "40ARGBLEWideGamut"
+ "40ARGBLEWideGamutPremultiplied"
+ "420YpCbCr10BiPlanarFullRange"
+ "420YpCbCr10BiPlanarVideoRange"
+ "420YpCbCr8BiPlanarFullRange"
+ "420YpCbCr8BiPlanarVideoRange"
+ "420YpCbCr8Planar"
+ "420YpCbCr8PlanarFullRange"
+ "420YpCbCr8VideoRange_8A_TriPlanar"
+ "422YpCbCr10"
+ "422YpCbCr10BiPlanarFullRange"
+ "422YpCbCr10BiPlanarVideoRange"
+ "422YpCbCr16"
+ "422YpCbCr8"
+ "422YpCbCr8BiPlanarFullRange"
+ "422YpCbCr8BiPlanarVideoRange"
+ "422YpCbCr8FullRange"
+ "422YpCbCr8_yuvs"
+ "422YpCbCr_4A_8BiPlanar"
+ "4444AYpCbCr16"
+ "4444AYpCbCr8"
+ "4444YpCbCrA8"
+ "4444YpCbCrA8R"
+ "444YpCbCr10"
+ "444YpCbCr10BiPlanarFullRange"
+ "444YpCbCr10BiPlanarVideoRange"
+ "444YpCbCr8"
+ "444YpCbCr8BiPlanarFullRange"
+ "444YpCbCr8BiPlanarVideoRange"
+ "48RGB"
+ "4Indexed"
+ "4IndexedGray_WhiteIsZero"
+ "64ARGB"
+ "64RGBAHalf"
+ "64RGBALE"
+ "64RGBA_DownscaledProResRAW"
+ "8Indexed"
+ "8IndexedGray_WhiteIsZero"
+ ": 0x"
+ ": failed a TimeframeSync: "
+ ": received data of timestamp "
+ ";"
+ ";\n "
+ "; "
+ "; X/X"
+ "; caused by:\n"
+ "; expected "
+ "; last read: '"
+ "<"
+ "<U+%.4X>"
+ "<discarded>"
+ "<parse error>"
+ "<uninitialized>"
+ ">"
+ "ARGB2101010LEPacked"
+ "Abgr16f"
+ "Abgr16u"
+ "Abgr32f"
+ "Abgr8u"
+ "Access notification must only be done in debug."
+ "AffineD"
+ "AffineF"
+ "AlgebraD"
+ "AlgebraF"
+ "An argument index may not have a negative value"
+ "An error occurred while loading the image"
+ "Archive can't load BinaryBlob"
+ "Argb16f"
+ "Argb16u"
+ "Argb32f"
+ "Argb8u"
+ "Array"
+ "Asynchronous callback not set"
+ "Attempt to access an expired PixelBuffer. Note that an image buffer  created by an ImageView does not keep the buffer alive."
+ "Attempting to create an "
+ "Auto"
+ "Bgr16f"
+ "Bgr16u"
+ "Bgr32f"
+ "Bgr8u"
+ "Bgra16f"
+ "Bgra16u"
+ "Bgra32f"
+ "Bgra8u"
+ "Blob"
+ "Bool"
+ "BuildVersion"
+ "Byte order and bits per component do not correspond to a supported format."
+ "Byte order is incompatible."
+ "Byte order is inverted."
+ "Byte order size for non-8 bits per component does not match bits per component."
+ "CF ref argument for `DictionaryValueSample` must be Number, String, Bool, Array or Dictionary, but is "
+ "CFDictionary cannot be used to create dict::Dictionary. It must only hold trivially serializable types: Boolean, Number, String, Array or Dictionary values"
+ "CMYK"
+ "Camera"
+ "CameraIMUDistanceType"
+ "Camera{Type: "
+ "Can't append to sequence '"
+ "Can't reconfigure VisualLogger with config '"
+ "CanSerialize(to_serialize.RuntimeFormat(), *op_format)"
+ "Cannot convert DataInfo to VZDataInfo; unsupported clock type: "
+ "Cannot copy CGImage of format "
+ "Cannot receive. Connection not initialized"
+ "Cannot save data as '"
+ "Cannot send. Connection not initialized"
+ "Cannot set root context to inherit its enable-state"
+ "Cannot set thread name '"
+ "Cannot use field end marker '"
+ "Cannot use same separator '"
+ "Caught unexpected exception of type: "
+ "Center"
+ "CenterHeikkilaD"
+ "CenterHeikkilaF"
+ "CenterPinholeD"
+ "CenterPinholeF"
+ "ChipID"
+ "Chronological"
+ "Client "
+ "Client cannot receive. Server connection not established."
+ "Client cannot send packet. Server connection not established."
+ "Client failed to connect to server at '"
+ "Client failed to send packet to "
+ "Client received invalid sync command from server."
+ "Client received no configuration from server after connection. This might mean the server could be outdated. Make sure to update VisualLogger server to protocol version 1.3.0+ (or same or newer version as the client)."
+ "ClientSyncUpdate"
+ "Color space model "
+ "Color values are premultiplied with alpha."
+ "ComputerName"
+ "Connection already initialized"
+ "ConstImageView"
+ "ConstSharedImage"
+ "Context may not be nullptr"
+ "Corner"
+ "CornerHeikkilaD"
+ "CornerHeikkilaF"
+ "CornerPinholeD"
+ "CornerPinholeF"
+ "Could not accept new client %d: %s (%d)"
+ "D"
+ "Debug"
+ "DepthFloat16"
+ "DepthFloat32"
+ "Desired image format is "
+ "Destination was nil"
+ "Device: "
+ "DeviceN"
+ "Dictionary"
+ "Dictionary cannot be serialized. It must only hold Boolean, Number, String, Array or Dictionary values, but contains "
+ "Dictionary to convert to json must only contain Number, String, Bool, Array or Dictionary, but has "
+ "Disabled"
+ "DisparityFloat16"
+ "DisparityFloat32"
+ "Dynamic"
+ "Enabled"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Endianness conversion not implemented for this format"
+ "Error"
+ "Error closing socket %d: %s (%d)"
+ "Error connecting to %s:%d"
+ "Error connecting to %s:%d %s (%d)"
+ "Error connecting to socket %d: %s (%d)"
+ "Error creating socket: %s (%d)"
+ "Error getting host address %d: %s (%d)"
+ "Error sending data to %d: %s (%d)"
+ "Error setsockopt: %s (%d)"
+ "Error setting socket blocking: %s (%d)"
+ "Error setting socket non-blocking: %s (%d)"
+ "Error starting client socket for "
+ "Error stopping socket %d: %s (%d)"
+ "Error while reading from %s. %s"
+ "ExportImageData requires data to be ImageData"
+ "ExportMeshData requires data to be MeshData"
+ "F"
+ "F == format"
+ "Failed to add VZDestination"
+ "Failed to create CVPixelBuffer: "
+ "Failed to export data of type "
+ "Failed to export log message to blob. Reason: "
+ "Failed to load sample "
+ "Failed to record data of type "
+ "Failed to save image to destination."
+ "Failed to send command(s) to client "
+ "Failed to set VZCamera "
+ "Failed to set VZCamera image size"
+ "Failed to start new server socket %d (expected if connection was terminated)"
+ "Failed to write to file: "
+ "Failure during "
+ "Failure during recording of data of type "
+ "Falling back to serialization-based conversion, due to direct conversion not implemented: %s"
+ "Fatal"
+ "File"
+ "Fisheye lens model not supported for VZCamera conversion"
+ "Fisheye4"
+ "Fisheye7"
+ "Flag not supported for ExportLargeData"
+ "For channels="
+ "ForType called with ArithmeticType::"
+ "Format "
+ "Format is not serializable. Must be a non-dynamic format."
+ "Found file format of unsupported format signature byte '0x"
+ "Four16f"
+ "Four16u"
+ "Four32f"
+ "Four8u"
+ "Function should contain valid target"
+ "FusionEngine initialized with config:"
+ "FusionResult is NULL"
+ "FusionResult published for timestamp: %lf"
+ "Given `camera` cannot be serialized. It does not contain a Kit_Camera camera"
+ "Given data block is too big to be represented by uint32_t indexed ArrayView"
+ "GraphicsFeatureSetClass"
+ "GraphicsFeatureSetFallbacks"
+ "Gray16f"
+ "Gray16u"
+ "Gray32f"
+ "Gray8u"
+ "GroupD"
+ "GroupF"
+ "HWModelStr"
+ "HasAppleNeuralEngine"
+ "Heikkila"
+ "HighResolution"
+ "I/O error"
+ "INFO"
+ "IOSurfaceName"
+ "Illegal or non-allocated address specified."
+ "Image"
+ "Image is of format "
+ "ImageDestinationRef does not (yet) support format "
+ "ImageIO"
+ "ImageView"
+ "Include <Kit/Common/ArithmeticType_Half.h> to support half type."
+ "Indexed"
+ "Info"
+ "Inherit"
+ "Input stream not in good state, in "
+ "Integral value outside the range of the char type"
+ "InternalBuild"
+ "Invalid .csv "
+ "Invalid ArithmeticType value '"
+ "Invalid Format ("
+ "Invalid Value Type for Camera model"
+ "Invalid `Version` string '"
+ "Invalid argument "
+ "Invalid image format. Format "
+ "Invalid mode"
+ "Invalid operation. Interface is disabled for "
+ "Invalid operation. Processor is released."
+ "Invalid pnm file. Format magic number not recognized."
+ "Invalid pnm file. Unexpected end of file in header."
+ "Invalid sector index (must be 0-11)"
+ "Invalid serialization format type: "
+ "Invalid sync type value"
+ "Invalid("
+ "IsValid()"
+ "IsVirtualDevice"
+ "Jpeg"
+ "Lab"
+ "Lens model type could not be identified for VZCamera conversion"
+ "Lines2"
+ "Lines3"
+ "MachAbsolute"
+ "MachContinuous"
+ "MakePixelBuffer"
+ "Mesh IO"
+ "Message was dropped."
+ "MetadataType (per-face vs per-vertex) not specified for field: "
+ "Monochrome"
+ "Must at least have one separator."
+ "Must choose format to save."
+ "NONE"
+ "Name: "
+ "Named scheduler already exists."
+ "NetworkOutputNode_WorkQueue"
+ "NewDataCallback"
+ "No known common format"
+ "No known method to load file of "
+ "No sectorized data available"
+ "Non-native packages are not supported: "
+ "Not enough data to read"
+ "Not enough data to read binary blob"
+ "Not enough data to read span"
+ "Not enough data to read string"
+ "Not implemented"
+ "NotSyncing"
+ "Number"
+ "Number of keys must match number of values"
+ "Numbers"
+ "OS: "
+ "OSLogAppender"
+ "OneComponent10"
+ "OneComponent12"
+ "OneComponent16"
+ "OneComponent16Half"
+ "OneComponent32Float"
+ "OneComponent8"
+ "P2\n"
+ "P3"
+ "P3\n"
+ "P5"
+ "P5\n"
+ "P6"
+ "P6\n"
+ "Package '"
+ "Package id '"
+ "Pattern"
+ "PeerInfo"
+ "Pgm"
+ "Pinhole"
+ "Pixel format is not kCGImagePixelFormatPacked."
+ "Png"
+ "Points2"
+ "Points3"
+ "Ppm"
+ "Proceeding"
+ "ProceedingConditionally"
+ "Process: "
+ "Processor is no longer available."
+ "Product: "
+ "ProductVersion"
+ "Protocol: "
+ "RGB"
+ "Raw"
+ "RearCameraOffsetFromDisplayCenter"
+ "RearFacingCameraTimeOfFlightCameraCapability"
+ "Receive packets from "
+ "Received a different target destination context during 'update enabled loggers' command. Retargeting of visualized textual log messages is not yet implemented. Command ignored."
+ "Received invalid Sync update from client "
+ "Received invalid format compatibility information"
+ "Received outdated Sync from client. Update the client to protocol 1.3.0 to sync with the server."
+ "Recorder\\{((?:\\.\\s*[a-zA-Z_][a-zA-Z0-9_]*\\s*=\\s*[a-zA-Z0-9_.]+\\s*,?\\s*)*)\\}"
+ "Recorder\\{(.*)\\}"
+ "RefillBuffer"
+ "ReleaseType"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "Requested format "
+ "Requested io-format "
+ "Requested to load "
+ "Requested to load format "
+ "Rgb16f"
+ "Rgb16u"
+ "Rgb32f"
+ "Rgb8u"
+ "Rgba16f"
+ "Rgba16u"
+ "Rgba32f"
+ "Rgba8u"
+ "Runtime format not in given Formats list"
+ "SN: "
+ "SerialNumber"
+ "Should not happen"
+ "Skips first component."
+ "Skips last component."
+ "Span of value type "
+ "Steady"
+ "String"
+ "Sync"
+ "SyncCommand"
+ "Sync{"
+ "System"
+ "TextLog"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The buffer does not support the given format"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Thread name '"
+ "Three16f"
+ "Three16u"
+ "Three32f"
+ "Three8u"
+ "Tiff"
+ "Timeout connecting to %s:%d"
+ "Timeout while waiting for connection established"
+ "Trace"
+ "Transform3"
+ "Transform3{src: "
+ "TriMesh"
+ "TriMeshData has edge data that will not be preserved by conversion to VZMesh"
+ "TriMeshData has texture data that will not be preserved by conversion to VZMesh"
+ "TriMeshData has texture name that will not be preserved by conversion to VZMesh"
+ "TriMeshData{\n"
+ "Two16f"
+ "Two16u"
+ "Two32f"
+ "Two8u"
+ "TwoComponent16"
+ "TwoComponent16Half"
+ "TwoComponent32Float"
+ "TwoComponent8"
+ "UUID: "
+ "UniqueDeviceID"
+ "Unknown"
+ "Unknown field name: '"
+ "Unknown pixel format '"
+ "Unsupported Format"
+ "Unsupported alpha info "
+ "Unsupported datatype:"
+ "Unsupported format"
+ "Unsupported pnm format. Loader does not support Rgb16u (.pbm) loading yet."
+ "Unsupported pnm format. Loader does not support intensity scaling. File specifies maximum intensity "
+ "Unsupported type"
+ "UpdateEnabledContexts"
+ "UpdateEnabledLoggers"
+ "UpdateSyncConfiguration"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "Using sectorized scene aggregators (world-fixed sectors) for all 3 scene type categories"
+ "V1_2_RequestOrAck"
+ "VDataExporter"
+ "Value of type "
+ "Virtual channel %d not handled"
+ "VisualLogger"
+ "WARN"
+ "WARNING: Visualization client "
+ "Waiting"
+ "Warn"
+ "When syncing is disabled, the first sync point must not be deferred"
+ "While connecting a new client, failed to send configuration to client: "
+ "XYZ"
+ "["
+ "[\n"
+ "[%s] No buckets above threshold"
+ "[%s] No buckets with evidence available"
+ "[%s] Probabilites map was empty even though window had some inputs. Likely none of the inputs had any predicted scene types"
+ "[%s] Query timestamp is before the last item in the window"
+ "[%s] Query timestamp is before the last update time"
+ "[%s] Window is empty"
+ "[%s] camera_id=%u exceeds expected range [0, %zu). Ensure logical camera index (0=left, 1=right) is passed, not a hardware stream ID."
+ "[%s] dynamic_params: decay_rate=%.4f"
+ "[%s] dynamic_params: decay_rate=%.4f, window_expiry_duration_secs=%.2f"
+ "[%s] heading left=%.4f right=%.4f delta=%.4f"
+ "[]"
+ "[json.exception."
+ "[row byte stride "
+ "\\\""
+ "\\'"
+ "\\.\\s*([a-zA-Z_][a-zA-Z0-9_]*)\\s*=\\s*([a-zA-Z0-9_.]+)"
+ "\\;"
+ "\\\\"
+ "\\d+(\\.?\\d+)?"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u%04x"
+ "]"
+ "]\n"
+ "],\n"
+ "],\"subtype\":"
+ "_f"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "acknowledge_until"
+ "affine3x4"
+ "algebra_r"
+ "algebra_t"
+ "alternate form"
+ "ambient::AmbientVisualLogging"
+ "an integer"
+ "api_log_level == tlog::LEVEL_FATAL || api_log_level == tlog::LEVEL_TRACE"
+ "api_logger.get().getInfoTree().numAppenders == 0"
+ "array"
+ "array size overflow"
+ "atto"
+ "auto_timestamp"
+ "base_scene"
+ "base_scene_config"
+ "bbox={"
+ "bin size overflow"
+ "binary"
+ "blocking caller while waiting for space in queue"
+ "boolean"
+ "box"
+ "bundle_url"
+ "byte_size"
+ "bytes"
+ "bytes_per_row >= min_bytes_per_row"
+ "callable_"
+ "camera"
+ "camera_id"
+ "camera_type"
+ "cannot compare iterators of different containers"
+ "cannot create object from initializer list"
+ "cannot get value"
+ "cannot use erase() with "
+ "cannot use key() for non-object iterators"
+ "cannot use operator[] with a numeric argument with "
+ "cannot use operator[] with a string argument with "
+ "cannot use push_back() with "
+ "caught runtime exception"
+ "centi"
+ "chosen common I/O format is not supported for the data type"
+ "client"
+ "client Receive() threw exception"
+ "client can't reach server"
+ "client does not have syncing enabled"
+ "client is outdated"
+ "client not found"
+ "client receive exception"
+ "client send failure"
+ "client synchronization is disabled"
+ "clock_type"
+ "color"
+ "colors"
+ "colors={"
+ "colors_type"
+ "colors_type="
+ "compat.format.has_value()"
+ "confidences"
+ "confidences={"
+ "confidences_type"
+ "confidences_type="
+ "config == active_config_.lock()"
+ "configuration issue"
+ "connection status update"
+ "container size overflow"
+ "context"
+ "context != nullptr"
+ "context_enable_state_changes"
+ "contexts status update"
+ "cpp-to-vz"
+ "current"
+ "custom_timestamp"
+ "cv3d.ambient_scene_scope.algorithm.input"
+ "cv3d.ambient_scene_scope.algorithm.output"
+ "cv3d.cf"
+ "cv3d.function"
+ "cv3d.kit.net"
+ "cv3d.kit.viz"
+ "cv3d.kit.viz I/O"
+ "cv3d.kit.viz client/server"
+ "cv3d.net"
+ "cv3d.viz"
+ "cv3d.vl.bridge"
+ "cv3d::kit::img::"
+ "cv3dapi"
+ "d-slice #"
+ "data"
+ "data export queue full"
+ "data is invalid"
+ "data of type "
+ "data package unknown to serializer"
+ "data type unknown to package"
+ "data_"
+ "data_id"
+ "days"
+ "deca"
+ "deci"
+ "depth size overflow"
+ "detail"
+ "dictionary"
+ "discarded"
+ "dispatch_group_wait failed"
+ "dispatch_queue"
+ "distortion_coeff"
+ "dst"
+ "edges"
+ "edges={"
+ "enable states from its connected server, but the client was configured without access to a logger. Specify the logger instance to control as part of client options for client creation using `VZClientOptionsSetControlledLogger`."
+ "end of input"
+ "entries: "
+ "error == 0"
+ "exa"
+ "excessive array size: "
+ "excessive object size: "
+ "exporter"
+ "ext size overflow"
+ "f"
+ "f16"
+ "f32"
+ "f64"
+ "faces"
+ "faces={"
+ "failed to convert or assign to/from VZ object, possibly due to an unexpected exception"
+ "failed to create VZ object, possibly due to an unexpected exception"
+ "failed to create file "
+ "failed to load"
+ "failed to load data"
+ "failed to open file"
+ "failed to open stream"
+ "failed to read from stream"
+ "failed to write to stream"
+ "false"
+ "false literal"
+ "femto"
+ "field"
+ "field end marker"
+ "file contains different image format"
+ "file exporter"
+ "file is of a different than specified format"
+ "file.good()"
+ "file://"
+ "filepath"
+ "filesystem error"
+ "filesystem operation failed"
+ "float32"
+ "float64"
+ "focal_length"
+ "for meshes with texture coords, mesh's #tex_faces must be equal to #faces"
+ "for meshes without texture coords, mesh's #tex_faces must be zero"
+ "format != img::Format::Dynamic"
+ "format not implemented"
+ "format not supported"
+ "fused_result_indoor_outdoor_scene"
+ "fused_result_scenes"
+ "giga"
+ "given tcp address must be of pattern "
+ "grocery_aisle"
+ "grocery_aisle_config"
+ "hecto"
+ "hostname:port %s:%d not valid"
+ "hours"
+ "i16"
+ "i32"
+ "i64"
+ "i8"
+ "idx < p_->GetCachedBaseAddress().size()"
+ "idx < static_cast<uint32_t>(DataType::End)"
+ "idx < static_cast<uint32_t>(NetworkDataType::End)"
+ "ignoring data of timestamp "
+ "image format not supported by io format"
+ "image_data"
+ "image_data_ptr"
+ "image_dynamic.RuntimeFormat() == color_format"
+ "image_format"
+ "image_size"
+ "incomplete UTF-8 string; last byte: 0x"
+ "inconsistent mesh"
+ "inconsistent timestamp"
+ "index out of range"
+ "index overflow"
+ "indoor_outdoor"
+ "indoor_outdoor_config"
+ "infnanINFNAN"
+ "info"
+ "info.json"
+ "info_"
+ "information not available"
+ "initial_sync_command"
+ "input_base_scenes"
+ "input_grocery_scenes"
+ "input_moving_platform_scenes"
+ "instance after creation but has not been given control of the logger. This can cause the server to have an inconsistent representation of the client logger state. \nHOW TO RESOLVE: Use `VZClientOptionsSetControlledLogger` to give the client control over the logger (recommended), or use `VZClientOptionsDisableLogControl` to disable."
+ "instance_id"
+ "internal_logger.get().getInfoTree().numAppenders == 0"
+ "invalid BOM; must be 0xEF 0xBB 0xBF if given"
+ "invalid IOValueType string "
+ "invalid UTF-8 byte at index "
+ "invalid alpha"
+ "invalid argument"
+ "invalid arithmetic type string "
+ "invalid camera type"
+ "invalid camera type string "
+ "invalid clock_type "
+ "invalid comment; expecting '/' or '*' after '/'"
+ "invalid comment; missing closing '*/'"
+ "invalid data type"
+ "invalid enable-state string "
+ "invalid enable-state string '"
+ "invalid image format type string "
+ "invalid key"
+ "invalid literal"
+ "invalid load into const data"
+ "invalid null pointer argument"
+ "invalid number; expected '+', '-', or digit after exponent"
+ "invalid number; expected digit after '-'"
+ "invalid number; expected digit after '.'"
+ "invalid number; expected digit after exponent sign"
+ "invalid or unsupported file"
+ "invalid peer ID"
+ "invalid recorder argument string: '"
+ "invalid se3 type string "
+ "invalid serialization format type string "
+ "invalid size limit string '"
+ "invalid string: '\\u' must be followed by 4 hex digits"
+ "invalid string: control character U+0000 (NUL) must be escaped to \\u0000"
+ "invalid string: control character U+0001 (SOH) must be escaped to \\u0001"
+ "invalid string: control character U+0002 (STX) must be escaped to \\u0002"
+ "invalid string: control character U+0003 (ETX) must be escaped to \\u0003"
+ "invalid string: control character U+0004 (EOT) must be escaped to \\u0004"
+ "invalid string: control character U+0005 (ENQ) must be escaped to \\u0005"
+ "invalid string: control character U+0006 (ACK) must be escaped to \\u0006"
+ "invalid string: control character U+0007 (BEL) must be escaped to \\u0007"
+ "invalid string: control character U+0008 (BS) must be escaped to \\u0008 or \\b"
+ "invalid string: control character U+0009 (HT) must be escaped to \\u0009 or \\t"
+ "invalid string: control character U+000A (LF) must be escaped to \\u000A or \\n"
+ "invalid string: control character U+000B (VT) must be escaped to \\u000B"
+ "invalid string: control character U+000C (FF) must be escaped to \\u000C or \\f"
+ "invalid string: control character U+000D (CR) must be escaped to \\u000D or \\r"
+ "invalid string: control character U+000E (SO) must be escaped to \\u000E"
+ "invalid string: control character U+000F (SI) must be escaped to \\u000F"
+ "invalid string: control character U+0010 (DLE) must be escaped to \\u0010"
+ "invalid string: control character U+0011 (DC1) must be escaped to \\u0011"
+ "invalid string: control character U+0012 (DC2) must be escaped to \\u0012"
+ "invalid string: control character U+0013 (DC3) must be escaped to \\u0013"
+ "invalid string: control character U+0014 (DC4) must be escaped to \\u0014"
+ "invalid string: control character U+0015 (NAK) must be escaped to \\u0015"
+ "invalid string: control character U+0016 (SYN) must be escaped to \\u0016"
+ "invalid string: control character U+0017 (ETB) must be escaped to \\u0017"
+ "invalid string: control character U+0018 (CAN) must be escaped to \\u0018"
+ "invalid string: control character U+0019 (EM) must be escaped to \\u0019"
+ "invalid string: control character U+001A (SUB) must be escaped to \\u001A"
+ "invalid string: control character U+001B (ESC) must be escaped to \\u001B"
+ "invalid string: control character U+001C (FS) must be escaped to \\u001C"
+ "invalid string: control character U+001D (GS) must be escaped to \\u001D"
+ "invalid string: control character U+001E (RS) must be escaped to \\u001E"
+ "invalid string: control character U+001F (US) must be escaped to \\u001F"
+ "invalid string: forbidden character after backslash"
+ "invalid string: ill-formed UTF-8 byte"
+ "invalid string: missing closing quote"
+ "invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF"
+ "invalid string: surrogate U+DC00..U+DFFF must follow U+D800..U+DBFF"
+ "invalid sync status ("
+ "invalid sync type"
+ "invalid timestamp"
+ "invalid uuid string"
+ "invalid value type identifier"
+ "invalid_iterator"
+ "io_format"
+ "iterator does not fit current value"
+ "iterator out of range"
+ "kCGImageAlphaOnly"
+ "kCGImageAlphaPremultipliedFirst"
+ "kCVReturnAllocationFailed: The allocation for a buffer or buffer pool failed. Most likely because of lack of resources."
+ "kCVReturnDisplayLinkAlreadyRunning: The CVDisplayLink is already started and running."
+ "kCVReturnDisplayLinkCallbacksNotSet: The output callback is not set."
+ "kCVReturnDisplayLinkNotRunning: The CVDisplayLink has not been started."
+ "kCVReturnError: Function executed with unknown error."
+ "kCVReturnInvalidArgument: At least one of the arguments passed in is not valid. Either out of range or the wrong type."
+ "kCVReturnInvalidDisplay: A CVDisplayLink cannot be created for the given DisplayRef."
+ "kCVReturnInvalidPixelBufferAttributes: A CVBuffer cannot be created with the given attributes."
+ "kCVReturnInvalidPixelFormat: The requested pixelformat is not supported for the CVBuffer type."
+ "kCVReturnInvalidPoolAttributes: A CVBufferPool cannot be created with the given attributes."
+ "kCVReturnInvalidSize: The requested size (most likely too big) is not supported for the CVBuffer type."
+ "kCVReturnPixelBufferNotMetalCompatible: The Buffer cannot be used with Metal as either its size, pixelformat or attributes are not supported by Metal."
+ "kCVReturnPixelBufferNotOpenGLCompatible: The Buffer cannot be used with OpenGL as either its size, pixelformat or attributes are not supported by OpenGL."
+ "kCVReturnPoolAllocationFailed: The allocation for the buffer pool failed. Most likely because of lack of resources. Check if your parameters are in range."
+ "kCVReturnRetry: a scan hasn't completely traversed the CVBufferPool due to a concurrent operation. The client can retry the scan."
+ "kCVReturnSuccess: Function executed successfully without errors."
+ "kCVReturnUnsupported"
+ "kCVReturnWouldExceedAllocationThreshold: The allocation request failed because it would have exceeded a specified allocation threshold (see kCVPixelBufferPoolAllocationThresholdKey)."
+ "keys.size() == values.size()"
+ "kilo"
+ "limited recorder"
+ "limiting_buffer_"
+ "lines2"
+ "lines3"
+ "load"
+ "loaded binary data size does not match given data blob size"
+ "loader must specify the format to load as"
+ "locale-specific form"
+ "localhost"
+ "location"
+ "logger_enable_state_changes"
+ "map size overflow"
+ "marketing-name"
+ "materials"
+ "materials={"
+ "materials_type"
+ "materials_type="
+ "max"
+ "maximum_message_age"
+ "maximum_record_count"
+ "maximum_records_size"
+ "maybe_format"
+ "maybe_string"
+ "mega"
+ "mesh is required to have per-vertex colors and normals"
+ "mesh structure not supported"
+ "mesh's #colors must be either zero or equal to #vertices"
+ "mesh_data_ptr"
+ "message: "
+ "micro"
+ "milli"
+ "min"
+ "min_version"
+ "minutes"
+ "months"
+ "moving_platform"
+ "moving_platform_config"
+ "mtx_"
+ "multiple error causes"
+ "must be: 'Recorder{[arg_value[, ...]]}' or 'Recorder{.arg_name=arg_value, ...}', with following args:\n#0: maximum_message_age: positive float (or '0' to disable)\n#1: maximum_record_count: positive int (or '0' to disable)\n#2: maximum_records_size: size string '{size}[KB|MB|GB]', e.g. '10KB' (or '0' to disable)"
+ "mutex"
+ "name"
+ "nano"
+ "network configuration issue"
+ "no error"
+ "normals"
+ "normals={"
+ "normals_type"
+ "normals_type="
+ "not a seed sequence"
+ "not available"
+ "not implemented"
+ "not_available"
+ "ns"
+ "null"
+ "null literal"
+ "nullopt"
+ "nullptr"
+ "null}"
+ "number"
+ "number literal"
+ "number overflow parsing '"
+ "numbers"
+ "obj export requires per-vertex colors"
+ "obj export requires per-vertex normals"
+ "object"
+ "object key"
+ "object separator"
+ "operation has no effect"
+ "operation not supported"
+ "os_build_version"
+ "os_product_version"
+ "out_of_range"
+ "owned_contexts"
+ "p_"
+ "package_id"
+ "parse error"
+ "parse_error"
+ "per-face"
+ "per-vertex"
+ "peta"
+ "pico"
+ "points2"
+ "points3"
+ "precision"
+ "principal_point"
+ "priv().initialized_root_appenders_ == current_root_appenders"
+ "proceed_n"
+ "proceed_until"
+ "process_id"
+ "process_name"
+ "processing queue is full"
+ "processor_"
+ "product_name"
+ "protocol_info"
+ "ptr != nullptr"
+ "public.jpeg"
+ "public.png"
+ "public.tiff"
+ "queue_type has unexpected value."
+ "recorder string 'maximum_message_age' argument (#0) invalid: must be positive float but is '"
+ "recorder string 'maximum_record_count' argument (#1) invalid: must be positive int but is '"
+ "recorder string 'maximum_records_size' argument (#2) invalid: must be a size string of pattern "
+ "references"
+ "ret == elog::APILogging::Available()"
+ "ret == elog::APILogging::InternalAvailable()"
+ "root appenders have been illegally modified between Initialize() and Enable() of APILogging"
+ "root appenders have been illegally modified between Initialize() and EnableInternal() of APILogging"
+ "root logger cannot inherit its enable-state but must be either enabled or disabled"
+ "root_logger.get().hasLogLevel() && api_logger.get().hasLogLevel()"
+ "row"
+ "save"
+ "scene_types"
+ "scene_types_count"
+ "scheduler must be valid"
+ "scheduler_"
+ "scheduler_ != nullptr"
+ "se3_type"
+ "seconds"
+ "sectorized"
+ "sectorized_base"
+ "sectorized_base_config"
+ "sectorized_grocery"
+ "sectorized_grocery_config"
+ "sectorized_moving_platform"
+ "sectorized_moving_platform_config"
+ "semantics"
+ "semantics={"
+ "semantics_type"
+ "semantics_type="
+ "separator"
+ "sequence file must not be named 'info'"
+ "sequence i/o failure"
+ "sequence.csv"
+ "serial_number"
+ "server Receive() threw exception"
+ "server can't reach client"
+ "server cannot receive "
+ "server cannot serialize data of unknown package"
+ "server cannot serialize package data of unknown data type"
+ "server receive exception"
+ "server send failure"
+ "server serialization failed"
+ "shape.size() == value_stride.size()"
+ "should not be reached"
+ "sign"
+ "size"
+ "size == image.Size()"
+ "space"
+ "src"
+ "src_to_dst"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 10U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 11U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 12U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 13U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 1U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 2U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 3U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 4U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 5U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 6U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 7U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 8U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = 9U]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::Number]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::Camera]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<double, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 4, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::FisheyeCamera<float, 7, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::HeikkilaCamera<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PinholeCamera<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PixelOrigin::Center]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cam::PixelOrigin::Corner]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::CameraSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::HeikkilaCameraSample<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<double, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<double, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<float, cv3d::kit::cam::PixelOrigin::Center>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::camio::PinholeCameraSample<float, cv3d::kit::cam::PixelOrigin::Corner>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cfio::DictionaryRefSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cfio::DictionaryValueSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::commonio::NumberSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Blob]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Lines<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Lines<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Points<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Points<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::BlobSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::LinesSample<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::LinesSample<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::NumbersSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::PointsSample<2>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::conio::PointsSample<3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Argb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Argb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Bgra8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Gray8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgba16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Rgba32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::dict::Dictionary]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::dictio::DictionarySample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Abgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Argb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Bgra8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Four8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Gray8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Rgba8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Three8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::ArrayImageBuffer<cv3d::kit::img::Format::Two8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::DynamicBuffer]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Abgr8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Argb8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgr8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Bgra8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Dynamic]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Four8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Gray8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgb8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Rgba8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Three8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two16f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two16u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two32f]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::img::Format::Two8u]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::imgio::ImageSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::imgio::ImageStructureSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::kio::ProtocolInfoSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Mutability::Const]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Ownership::Shared]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Protection::Unprotected]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::mesh::TriMeshBoundingBoxSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::mesh::TriMeshDataSample<>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::timeio::TimestampSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ClientSyncUpdateSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::DataInfoSample<6>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ImageData]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::NetworkPackage]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::PeerInfoSample<2U>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::PeerInfo]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::SE3Sample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::SyncCommandSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::SyncSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Sync]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::TextLog]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Transform3Sample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::Transform3]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::TriMesh]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateEnabledContextsSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateEnabledContexts]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateEnabledLoggersSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateEnabledLoggers]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateSyncConfigurationSample]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UpdateSyncConfiguration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::Number>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::cam::Camera>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Blob>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Lines<2>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Lines<3>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Points<2>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Points<3>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::dict::Dictionary>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::img::SharedImage<cv3d::kit::img::Format::Dynamic, cv3d::kit::img::DynamicBuffer, cv3d::kit::img::Mutability::Const>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::PeerInfo>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::Sync>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::TextLog>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::Transform3>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::TriMesh>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::UpdateEnabledContexts>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::UpdateEnabledLoggers>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::viz::UpdateSyncConfiguration>]"
+ "status"
+ "std::"
+ "std::__1::"
+ "std::aligned_alloc failed to allocate "
+ "std::any owner for CFData backing store"
+ "str size overflow"
+ "stride must be multiple of pixel size"
+ "stride must not overlap internally"
+ "string"
+ "string literal"
+ "string_view::substr"
+ "structure"
+ "sync update"
+ "sync_command_id"
+ "sync_id"
+ "sync_type"
+ "syntax error "
+ "target_context"
+ "tera"
+ "tex0='"
+ "tex_coords"
+ "tex_coords={"
+ "tex_faces"
+ "tex_faces={"
+ "textures"
+ "this->numbers.Size() % (N * 2) == 0"
+ "this->numbers.Size() % N == 0"
+ "thread constructor failed"
+ "timeout waiting for peer response"
+ "timestamp is invalid"
+ "timestamping is inconsistent"
+ "total_size < std::numeric_limits<uint32_t>::max()"
+ "true"
+ "true literal"
+ "trying to cast camera"
+ "type"
+ "type must be array, but is "
+ "type must be boolean, but is "
+ "type must be number, but is "
+ "type must be string, but is "
+ "type_error"
+ "type_id"
+ "u16"
+ "u32"
+ "u64"
+ "u8"
+ "uint32"
+ "unexpected "
+ "unexpected runtime exception in VZ method"
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
+ "unique_lock::unlock: not locked"
+ "unknown"
+ "unknown allocator mode"
+ "unknown arithmetic type"
+ "unknown error"
+ "unknown token"
+ "unknown type id "
+ "unknown_package"
+ "unnamed"
+ "unsupported format"
+ "unsupported or invalid sequence"
+ "user_given_name"
+ "uuid"
+ "v "
+ "value"
+ "value_type"
+ "version"
+ "vertices"
+ "vertices={"
+ "viz::ContextStatistics"
+ "viz::LimitedRecorder"
+ "viz::Package"
+ "viz::PackageData"
+ "viz::Records"
+ "viz::SharedData"
+ "viz::UnlimitedRecorder"
+ "vn "
+ "vt "
+ "vz_data_info"
+ "weeks"
+ "while parsing "
+ "work_queue_"
+ "world"
+ "x"
+ "years"
+ "zero-padding"
+ "{"
+ "{\n"
+ "{\"bytes\":["
+ "{:.{}}"
+ "{:<{}}"
+ "{:>{}}"
+ "{:{}}"
+ "{Model: "
+ "{current="
+ "{error}"
+ "{fx,fy: "
+ "{unknown buffer type}"
+ "{}"
+ "}"
+ "}\n"
+ "�"
- "No buckets above threshold"
- "No buckets with evidence available"
- "Output parameter is NULL"
- "Probabilites map was empty even though window had some inputs. Likely none of the inputs had any predicted scene types"
- "Query timestamp is before the last item in the window"
- "Query timestamp is before the last update time"
- "Unequal scene_types and confidences counts"
- "Window is empty"

```
