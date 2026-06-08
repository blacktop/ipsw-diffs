## AssistantCoreFollowupExtension

> `/System/Library/ExtensionKit/Extensions/AssistantCoreFollowupExtension.appex/AssistantCoreFollowupExtension`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x254
-  __TEXT.__auth_stubs: 0xc0
-  __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__cstring: 0xd6
-  __TEXT.__objc_methname: 0x63
+3600.49.31.1.6
+  __TEXT.__text: 0x18a0
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0xe0
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__const: 0x7a
+  __TEXT.__cstring: 0x1b3
+  __TEXT.__oslogstring: 0xe1
+  __TEXT.__objc_methname: 0xe9
   __TEXT.__objc_classname: 0x3d
-  __TEXT.__objc_methtype: 0x40
-  __TEXT.__const: 0x3a
+  __TEXT.__objc_methtype: 0x4e
   __TEXT.__constg_swiftt: 0x58
-  __TEXT.__swift5_typeref: 0x26
+  __TEXT.__swift5_typeref: 0x87
   __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x68
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x48
-  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_selrefs: 0x60
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x28
+  __DATA.__data: 0x68
+  __DATA.__bss: 0x8
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C97B682A-5EC3-37C4-A5F8-D70C19E6DD99
-  Functions: 9
-  Symbols:   48
-  CStrings:  15
+  UUID: BC7F62F1-3A3C-36DD-89FE-87B5CB5B98DF
+  Functions: 31
+  Symbols:   95
+  CStrings:  33
 
Symbols:
+ _LAStorageErrorDomain
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_OS_os_log
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_release
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x8
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_release
+ _swift_release_x1
+ _swift_release_x20
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x2
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrow
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftVideoToolbox
CStrings:
+ ".cxx_destruct"
+ "Error clearing followup item: %@"
+ "Failed to set protected variable: %@"
+ "Handling CFU for allow siri when face down"
+ "Handling CFU for sound enrollment preboard"
+ "Reboot required to set protected variable"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
+ "code"
+ "com.apple.securesettings.followup.allowCustomSoundRecognition"
+ "com.apple.securesettings.followup.alwaysAllowVoiceActivation"
+ "com.apple.securesettings.followup.restartaction"
+ "com.apple.securesettings.migration"
+ "domain"
+ "identifier"
+ "initWithClientIdentifier:"
+ "uniqueIdentifier"
+ "v16@0:8"
+ "v8@?0"

```
