## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x5a038
-  __TEXT.__auth_stubs: 0x1210
+485.3.0.0.0
+  __TEXT.__text: 0x530d8
+  __TEXT.__auth_stubs: 0x11f0
   __TEXT.__objc_methlist: 0x273c
-  __TEXT.__const: 0x930
+  __TEXT.__const: 0x980
   __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__oslogstring: 0x58eb
-  __TEXT.__cstring: 0x1c07
+  __TEXT.__oslogstring: 0x5954
+  __TEXT.__cstring: 0x1c37
   __TEXT.__dlopen_cstrs: 0x1a8
-  __TEXT.__swift5_typeref: 0x75e
+  __TEXT.__swift5_typeref: 0x750
   __TEXT.__swift5_capture: 0x2d8
   __TEXT.__constg_swiftt: 0x81c
   __TEXT.__swift5_reflstr: 0x301

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x1310
-  __TEXT.__eh_frame: 0x858
+  __TEXT.__unwind_info: 0x12a8
+  __TEXT.__eh_frame: 0x908
   __TEXT.__objc_classname: 0x482
-  __TEXT.__objc_methname: 0x5274
+  __TEXT.__objc_methname: 0x52ae
   __TEXT.__objc_methtype: 0xe36
-  __TEXT.__objc_stubs: 0x4880
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x8b0
+  __TEXT.__objc_stubs: 0x48e0
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1700
+  __DATA_CONST.__objc_selrefs: 0x1710
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x918
-  __AUTH_CONST.__const: 0x1080
+  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__const: 0x10a8
   __AUTH_CONST.__cfstring: 0x1120
   __AUTH_CONST.__objc_const: 0x3938
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x15b8
   __AUTH.__data: 0x300
   __DATA.__objc_ivar: 0x1c8
-  __DATA.__data: 0xb00
+  __DATA.__data: 0xaa0
   __DATA.__bss: 0x930
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BBD79A3F-CFE4-3971-8577-01FE8D1EF33F
-  Functions: 1736
-  Symbols:   3776
-  CStrings:  1905
+  UUID: DD6487BF-38AD-3E87-840C-6699DF843C65
+  Functions: 1741
+  Symbols:   3749
+  CStrings:  1911
 
Symbols:
+ -[AXSDRingBuffer .cxx_destruct]
+ -[AXSDRingBuffer addObject:]
+ -[AXSDRingBuffer content]
+ -[AXSDRingBuffer count]
+ -[AXSDRingBuffer initWithCount:]
+ -[AXSDRingBuffer reset]
+ _AVAudioSessionCategoryRecord
+ _BiomeLibrary
+ _OBJC_CLASS_$_AXSDRingBuffer
+ _OBJC_CLASS_$_BMAccessibilitySoundDetection
+ _OBJC_IVAR_$_AXSDRingBuffer._bufferArray
+ _OBJC_IVAR_$_AXSDRingBuffer._head
+ _OBJC_IVAR_$_AXSDRingBuffer._size
+ _OBJC_METACLASS_$_AXSDRingBuffer
+ __OBJC_$_INSTANCE_METHODS_AXSDRingBuffer
+ __OBJC_$_INSTANCE_VARIABLES_AXSDRingBuffer
+ __OBJC_$_PROP_LIST_AXSDRingBuffer
+ __OBJC_CLASS_RO_$_AXSDRingBuffer
+ __OBJC_METACLASS_RO_$_AXSDRingBuffer
+ ___38-[AXSDListenEngine _interruptCarPlay:]_block_invoke.105
+ ___44-[AXUltronModelAssetManager downloadAssets:]_block_invoke.290
+ ___block_literal_global.293
+ ___block_literal_global.297
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AXSoundDetectionUI
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_AXSoundDetectionUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AXSoundDetectionUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AXSoundDetectionUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AXSoundDetectionUI
+ _block_copy_helper.11
+ _block_copy_helper.25
+ _block_copy_helper.32
+ _block_copy_helper.39
+ _block_copy_helper.46
+ _block_copy_helper.5
+ _block_descriptor.13
+ _block_descriptor.27
+ _block_descriptor.34
+ _block_descriptor.41
+ _block_descriptor.48
+ _block_descriptor.7
+ _block_destroy_helper.12
+ _block_destroy_helper.26
+ _block_destroy_helper.33
+ _block_destroy_helper.40
+ _block_destroy_helper.47
+ _block_destroy_helper.6
+ _objc_msgSend$Accessibility
+ _objc_msgSend$SoundDetection
+ _objc_msgSend$initSessionForIndependentInputRoute
+ _objc_msgSend$initWithAbsoluteTimestamp:soundDetectionType:name:
+ _objc_msgSend$setAudioSession:
+ _objectdestroy.23Tm
- -[AXHARingBuffer .cxx_destruct]
- -[AXHARingBuffer addObject:]
- -[AXHARingBuffer content]
- -[AXHARingBuffer count]
- -[AXHARingBuffer initWithCount:]
- -[AXHARingBuffer reset]
- _AVAudioSessionInterruptionOptionKey
- _OBJC_CLASS_$_AXHARingBuffer
- _OBJC_CLASS_$_BMSoundDetectionEvent
- _OBJC_CLASS_$_BMStreams
- _OBJC_IVAR_$_AXHARingBuffer._bufferArray
- _OBJC_IVAR_$_AXHARingBuffer._head
- _OBJC_IVAR_$_AXHARingBuffer._size
- _OBJC_METACLASS_$_AXHARingBuffer
- __OBJC_$_INSTANCE_METHODS_AXHARingBuffer
- __OBJC_$_INSTANCE_VARIABLES_AXHARingBuffer
- __OBJC_$_PROP_LIST_AXHARingBuffer
- __OBJC_CLASS_RO_$_AXHARingBuffer
- __OBJC_METACLASS_RO_$_AXHARingBuffer
- ___38-[AXSDListenEngine _interruptCarPlay:]_block_invoke.103
- ___44-[AXUltronModelAssetManager downloadAssets:]_block_invoke.287
- ___block_literal_global.290
- ___block_literal_global.294
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AXSoundDetectionUI
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AXSoundDetectionUI
- _block_copy_helper.24
- _block_copy_helper.31
- _block_copy_helper.38
- _block_copy_helper.45
- _block_descriptor.26
- _block_descriptor.33
- _block_descriptor.40
- _block_descriptor.47
- _block_destroy_helper.25
- _block_destroy_helper.32
- _block_destroy_helper.39
- _block_destroy_helper.46
- _objc_msgSend$initWithAbsoluteTimestamp:type:customName:
- _objc_msgSend$soundDetection
- _objectdestroy.22Tm
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
- _swift_retain_n
- _symbolic _____Sg 13SoundAnalysis013AccessibilityA11RecognitionV18DetectorIdentifierO
- _symbolic ypSg
CStrings:
+ "@\"AXSDRingBuffer\""
+ "AXSDRingBuffer"
+ "Accessibility"
+ "InputAudioCoexistenceSupport"
+ "MediaExperience"
+ "SoundDetection"
+ "Using Default Mode for Audio Session."
+ "[%s]: Detector: %s. FATAL ERROR - result is unknown and not handled. Result: %s"
+ "initSessionForIndependentInputRoute"
+ "initWithAbsoluteTimestamp:soundDetectionType:name:"
- "@\"AXHARingBuffer\""
- "AXHARingBuffer"
- "initWithAbsoluteTimestamp:type:customName:"
- "soundDetection"

```
