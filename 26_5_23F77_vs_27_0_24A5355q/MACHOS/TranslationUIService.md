## TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

```diff

-365.13.0.0.0
-  __TEXT.__text: 0x50714
-  __TEXT.__auth_stubs: 0x22b0
+380.1.0.0.0
+  __TEXT.__text: 0x50f24
+  __TEXT.__auth_stubs: 0x2490
   __TEXT.__objc_stubs: 0x1000
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x3558
-  __TEXT.__constg_swiftt: 0xfbc
-  __TEXT.__swift5_typeref: 0x5306
+  __TEXT.__const: 0x3740
+  __TEXT.__constg_swiftt: 0x1000
+  __TEXT.__swift5_typeref: 0x5450
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xf2a
-  __TEXT.__swift5_fieldmd: 0xb94
-  __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__cstring: 0x6d3
-  __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_reflstr: 0xfba
+  __TEXT.__swift5_fieldmd: 0xbd4
+  __TEXT.__swift5_assocty: 0x310
+  __TEXT.__swift5_proto: 0xc8
+  __TEXT.__swift5_types: 0xc0
   __TEXT.__objc_classname: 0x41a
-  __TEXT.__objc_methname: 0x159b
-  __TEXT.__objc_methtype: 0x3f2
+  __TEXT.__objc_methname: 0x161b
+  __TEXT.__objc_methtype: 0x3d2
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__oslogstring: 0xf59
-  __TEXT.__swift5_capture: 0x688
+  __TEXT.__oslogstring: 0x1249
+  __TEXT.__swift5_capture: 0x6f8
+  __TEXT.__cstring: 0x6c3
   __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_cont: 0xb4
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__unwind_info: 0xfe8
-  __TEXT.__eh_frame: 0x10d0
-  __DATA_CONST.__auth_got: 0x1160
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__auth_ptr: 0x928
-  __DATA_CONST.__const: 0x1668
+  __TEXT.__eh_frame: 0x1080
+  __DATA_CONST.__const: 0x1710
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0xf88
+  __DATA_CONST.__auth_got: 0x1250
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__auth_ptr: 0x950
+  __DATA.__objc_const: 0xfe8
   __DATA.__objc_selrefs: 0x548
   __DATA.__objc_data: 0xa20
-  __DATA.__data: 0x2558
-  __DATA.__bss: 0x1bb0
+  __DATA.__data: 0x25d8
+  __DATA.__bss: 0x1c70
   __DATA.__common: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D832C165-DCB3-3594-AF92-51336F60821E
-  Functions: 1398
-  Symbols:   232
-  CStrings:  423
+  UUID: AC43B633-F884-321B-8E75-5550929D2003
+  Functions: 1420
+  Symbols:   255
+  CStrings:  437
 
Symbols:
+ _objc_release_x10
+ _objc_retain_x3
+ _swift_release_x1
+ _swift_release_x10
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_retain_x9
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- _bzero
- _objc_retain_x9
- _swift_unknownObjectRetain_n
CStrings:
+ "%{public}s: traditional Translate pair not installed"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "Can play TTS? Source: %{bool}d, Target:  %{bool}d"
+ "Deferring translation until availableLanguages is populated"
+ "ExpandSheetAction"
+ "Optional<UserInterfaceSizeClass>"
+ "Retrying previously deferred translation: resolving target locale now that language models are available"
+ "Saved target locale %{public}s not compatible with source %{public}s, falling back to default selection"
+ "Selected on-device engine type: %s"
+ "Source can play TTS: %{bool}d"
+ "TTS was not active, skipping cancellation of in-flight translation requests"
+ "Target can play TTS: %{bool}d"
+ "_availableLanguages"
+ "_canPlayTTSForSourceLocale"
+ "_canPlayTTSForTargetLocale"
+ "languageNotRecognizedLabel"
+ "languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:"
+ "onDeviceEngineType"
+ "separatorColor"
+ "setOnDeviceEngineType:"
+ "translationDeferred"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "_availableLocales"
- "availableLocalePairsForTask:completion:"
- "languagesForText:usingModel:completion:"
- "sourceLocale"
- "targetLocale"
- "v16@?0@\"NSArray\"8"

```
