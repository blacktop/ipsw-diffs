## GenerativeAssistantSettingsExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/GenerativeAssistantSettingsExtension`

```diff

-3405.28.1.0.0
-  __TEXT.__text: 0x11154
-  __TEXT.__auth_stubs: 0x860
+3406.9.1.0.0
+  __TEXT.__text: 0x12ea0
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__cstring: 0xc40
-  __TEXT.__const: 0x25f6
-  __TEXT.__swift5_typeref: 0x98c
-  __TEXT.__constg_swiftt: 0x3c8
-  __TEXT.__swift5_reflstr: 0x232
-  __TEXT.__swift5_fieldmd: 0x338
+  __TEXT.__cstring: 0xbc0
+  __TEXT.__const: 0x27a8
+  __TEXT.__swift5_typeref: 0x94a
+  __TEXT.__constg_swiftt: 0x388
+  __TEXT.__swift5_reflstr: 0x252
+  __TEXT.__swift5_fieldmd: 0x328
   __TEXT.__swift5_proto: 0x234
   __TEXT.__swift5_types: 0x64
-  __TEXT.__objc_methname: 0x5a
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift_as_entry: 0xc0
-  __TEXT.__swift_as_ret: 0x94
+  __TEXT.__objc_methname: 0x1b
+  __TEXT.__oslogstring: 0x7a
   __TEXT.__swift5_assocty: 0x4a0
+  __TEXT.__swift_as_entry: 0xb8
+  __TEXT.__swift_as_ret: 0x8c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x778
-  __TEXT.__eh_frame: 0x7c0
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__auth_ptr: 0x500
-  __DATA_CONST.__const: 0xb90
+  __TEXT.__unwind_info: 0x740
+  __TEXT.__eh_frame: 0x730
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x520
+  __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0x28
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x9a0
-  __DATA.__bss: 0x4600
-  __DATA.__common: 0x120
+  __DATA.__objc_selrefs: 0x18
+  __DATA.__objc_data: 0xe0
+  __DATA.__data: 0x870
+  __DATA.__bss: 0x4680
+  __DATA.__common: 0x130
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions
   - /System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
+  - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E8F5FD6F-D6CF-3D25-A72F-EBC08447244F
-  Functions: 623
-  Symbols:   103
-  CStrings:  67
+  UUID: DDB9CC94-919A-3424-8D74-6E6FF2B8D4FE
+  Functions: 615
+  Symbols:   102
+  CStrings:  64
 
Symbols:
+ __os_log_impl
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retain
+ _objc_retain_x8
+ _os_log_type_enabled
+ _swift_arrayDestroy
+ _swift_getObjectType
+ _swift_setDeallocating
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
- _OBJC_CLASS_$_CSFAvailability
- __NSConcreteStackBlock
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_stdlib_reportUnimplementedInitializer
- _objc_release_x20
- _objc_release_x25
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x25
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_resume
CStrings:
+ "%s.%s GM availability: %s"
+ "%s.%s GM restricted with info: %s"
+ "%s.%s GM unavailable with info: %s"
+ "_$observationRegistrar"
- "GenerativeAssistantSettingsExtension.GMAvailabilityProvider"
- "com.apple.Settings.AppleIntelligence"
- "currentAvailabilityWithCompletionHandler:"
- "init()"
- "provider"
- "unavailabiltyReasons"
- "v16@?0@\"CSFAvailability\"8"

```
