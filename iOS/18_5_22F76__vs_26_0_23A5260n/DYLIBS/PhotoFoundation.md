## PhotoFoundation

> `/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x8b68
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0xc24
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__cstring: 0x7c7
-  __TEXT.__oslogstring: 0x59f
-  __TEXT.__unwind_info: 0x330
+800.14.111.0.0
+  __TEXT.__text: 0x9f54
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0xc3c
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0xc7d
+  __TEXT.__swift5_typeref: 0xe
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_reflstr: 0x303
+  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0x114
+  __TEXT.__oslogstring: 0x5c1
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__objc_classname: 0x2ac
-  __TEXT.__objc_methname: 0x1b54
-  __TEXT.__objc_methtype: 0x535
-  __TEXT.__objc_stubs: 0x1520
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1e0
+  __TEXT.__objc_methname: 0x1c1e
+  __TEXT.__objc_methtype: 0x541
+  __TEXT.__objc_stubs: 0x1620
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d0
+  __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__const: 0x390
+  __AUTH_CONST.__cfstring: 0xce0
   __AUTH_CONST.__objc_const: 0x20d8
   __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0x240
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x58
+  __DATA.__data: 0x250
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x190
   __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2378758-3377-3CB4-850C-650F9C32E676
-  Functions: 305
-  Symbols:   1239
-  CStrings:  700
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: D63C7083-2096-387F-B9E3-F451C0174C40
+  Functions: 369
+  Symbols:   1366
+  CStrings:  783
 
Symbols:
+ -[PFStateCaptureEventDescription appendNumber:]
+ -[PFStateCaptureEventDescription appendPointer:]
+ GCC_except_table101
+ GCC_except_table130
+ GCC_except_table180
+ GCC_except_table288
+ GCC_except_table292
+ GCC_except_table85
+ GCC_except_table99
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateFormatter
+ _OUTLINED_FUNCTION_0
+ _PFBitmaskDescription
+ _PFDeviceIsVirtualMachine
+ _PFDeviceIsVirtualMachine.isVirtualMachine
+ _PFDeviceIsVirtualMachine.onceToken
+ _PFIsCamera
+ _PFIsCamera.isCamera
+ _PFIsCamera.onceToken
+ _PFIsCameraAppAnyPlatform
+ _PFIsCameraMessagesApp
+ _PFIsCameraMessagesApp.isPreferences
+ _PFIsCameraMessagesApp.onceToken
+ _PFIsLockScreenCamera
+ _PFIsLockScreenCamera.didCheck
+ _PFIsLockScreenCamera.isCamera
+ _PFIsMacPhotosApp
+ _PFIsPhotosAppAnyPlatform
+ _PFIsPhotosMessagesApp
+ _PFIsPhotosMessagesApp.isPhotosMessagesApp
+ _PFIsPhotosMessagesApp.onceToken
+ _PFIsPhotosPicker
+ _PFIsPhotosPicker.isPhotoPicker
+ _PFIsPhotosPicker.onceToken
+ _PFIsPreferences
+ _PFIsPreferences.isPreferences
+ _PFIsPreferences.onceToken
+ _PFIsSpotlight
+ _PFIsSpotlight.isSpotlight
+ _PFIsSpotlight.onceToken
+ _PFIsTVPhotosApp
+ _PFIsTVPhotosApp.didCheck
+ _PFIsTVPhotosApp.isTVPhotosApp
+ _PFIsVisionCameraApp
+ _PFIsVisionPhotosApp
+ _PFIsiOSPhotosApp
+ _PFIsiOSPhotosApp.didCheck
+ _PFIsiOSPhotosApp.isPhotos
+ _PFKTraceSpatialPhotoCameraTechniqueChanged
+ _PFKTraceSpatialPhotoCameraTransformsChanged
+ _PFKTraceSpatialPhotoInvalidateCamera
+ _PFKTraceSpatialPhotoRenderEnd
+ _PFKTraceSpatialPhotoRenderStart
+ _PFKTraceSpatialPhotoSetCameraTechnique
+ _PFKTraceSpatialPhotoSetNeedsRender
+ ___PFBitmaskDescription_block_invoke
+ ___PFDeviceIsVirtualMachine_block_invoke
+ ___PFIsCameraMessagesApp_block_invoke
+ ___PFIsCamera_block_invoke
+ ___PFIsLockScreenCamera_block_invoke
+ ___PFIsPhotosMessagesApp_block_invoke
+ ___PFIsPhotosPicker_block_invoke
+ ___PFIsPreferences_block_invoke
+ ___PFIsSpotlight_block_invoke
+ ___PFIsTVPhotosApp_block_invoke
+ ___PFIsiOSPhotosApp_block_invoke
+ ___block_descriptor_64_e8_32s40s48r_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8r48l8
+ ___block_literal_global.118
+ ___block_literal_global.12
+ ___block_literal_global.122
+ ___block_literal_global.16
+ ___block_literal_global.18
+ ___block_literal_global.19
+ ___block_literal_global.23
+ ___block_literal_global.285
+ ___block_literal_global.3.290
+ ___block_literal_global.3.440
+ ___block_literal_global.31
+ ___block_literal_global.338
+ ___block_literal_global.36
+ ___block_literal_global.393
+ ___block_literal_global.41
+ ___block_literal_global.435
+ ___block_literal_global.524
+ ___block_literal_global.60
+ ___block_literal_global.67
+ ___block_literal_global.8
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PhotoFoundation
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_PhotoFoundation
+ _associated conformance 15PhotoFoundation18PhotosFeatureFlagsOSHAASQ
+ _kdebug_trace
+ _modf
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$processName
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$unsignedIntegerValue
+ _swift_getWitnessTable
+ _swift_release
+ _symbolic _____ 15PhotoFoundation18PhotosFeatureFlagsO
+ _sysctlbyname
- GCC_except_table109
- GCC_except_table123
- GCC_except_table125
- GCC_except_table172
- GCC_except_table280
- GCC_except_table284
- _OBJC_CLASS_$_NSISO8601DateFormatter
- _OBJC_CLASS_$_NSTimeZone
- ___block_literal_global.116
- ___block_literal_global.120
- ___block_literal_global.3.395
- ___block_literal_global.308
- ___block_literal_global.347
- ___block_literal_global.390
- ___block_literal_global.4
- ___block_literal_global.475
- ___block_literal_global.63
- ___block_literal_global.70
- _objc_msgSend$localTimeZone
- _objc_msgSend$setFormatOptions:
- _objc_msgSend$setTimeZone:
CStrings:
+ "%@"
+ "%p"
+ "(null)"
+ ".%06ld"
+ ".000000"
+ "@24@0:8^v16"
+ "AlbumListEditing"
+ "AppleMusicExportRestrictionByPass"
+ "AssetResourceBackgroundUpload"
+ "Camera"
+ "CameraMessagesApp"
+ "Connections"
+ "Gyro1Up"
+ "GyroPoster"
+ "GyroWidget"
+ "Lemonade"
+ "LemonadeDocuments"
+ "LemonadeEventLabeling"
+ "LibraryUnderstanding"
+ "LockScreenCamera"
+ "MemoryCreationContextualPrompt"
+ "MemoryCreationGenericLocation"
+ "MemoryCreationInternationalization"
+ "MemoryCreationMini"
+ "MemoryCreationPersonalEventsBeyondMeanings"
+ "MemoryCreationPromptSuggestionDB"
+ "MemoryCreationQU"
+ "MemoryCreationTimeEventDisambiguation"
+ "MemoryCreationWhimsicalPrompt"
+ "NSString * _Nonnull PFBitmaskDescription(NSUInteger, NSArray<NSNumber *> *__strong _Nonnull, NSArray<NSString *> *__strong _Nonnull)"
+ "None"
+ "PFOptimization.m"
+ "PhotoPicker"
+ "Photos"
+ "PhotosMessagesApp"
+ "PhotosPicker"
+ "PhotosPosterBackdrop"
+ "Preferences"
+ "RetailExperience"
+ "SharedCollections"
+ "SharedStreamCollectionShareSupport"
+ "ShazamPublicEvents"
+ "Spotlight"
+ "TVPhotos"
+ "UNKNOWN(%lu)"
+ "Unknown bitmask description (%lu)"
+ "appendNumber:"
+ "appendPointer:"
+ "bits.count == names.count"
+ "calendarWithIdentifier:"
+ "en_US_POSIX"
+ "enumerateObjectsUsingBlock:"
+ "isEqualToString:"
+ "kern.hv_vmm_present"
+ "localeWithLocaleIdentifier:"
+ "processName"
+ "setCalendar:"
+ "setDateFormat:"
+ "setLocale:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "unsignedIntegerValue"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "yyyy-MM-dd HH:mm:ss.000000Z"
+ "|"
- "localTimeZone"
- "setFormatOptions:"
- "setTimeZone:"

```
