## LighthouseASRReplay

> `/System/Library/ExtensionKit/Extensions/LighthouseASRReplay.appex/LighthouseASRReplay`

```diff

-3404.71.4.1.1
-  __TEXT.__text: 0x2c24
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x27e
-  __TEXT.__swift5_typeref: 0xe1
+3404.79.2.0.0
+  __TEXT.__text: 0x3bcc
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x13c
+  __TEXT.__const: 0x2ae
+  __TEXT.__cstring: 0x95
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__swift5_typeref: 0x14b
   __TEXT.__constg_swiftt: 0x74
-  __TEXT.__swift5_reflstr: 0x3b
+  __TEXT.__swift5_reflstr: 0x43
   __TEXT.__swift5_fieldmd: 0x84
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x3e
-  __TEXT.__cstring: 0x15
+  __TEXT.__objc_methname: 0x209
+  __TEXT.__oslogstring: 0x79
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__eh_frame: 0x1c0
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x1f0
+  __TEXT.__objc_classname: 0x2c
+  __TEXT.__objc_methtype: 0xeb
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__eh_frame: 0x250
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_ptr: 0x140
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x4c0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA.__objc_const: 0x150
+  __DATA.__objc_selrefs: 0x108
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x4d0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 84
-  Symbols:   75
-  CStrings:  4
+  Functions: 104
+  Symbols:   101
+  CStrings:  68
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMASRContextualReplayRecord
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftImmortalRefCount
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release
+ _objc_release_x21
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x23
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_dynamicCastObjCClass
+ _swift_initStackObject
+ _swift_setDeallocating
+ _swift_unknownObjectRelease
- __swift_stdlib_bridgeErrorToNSError
- _swift_errorRetain
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "#16@0:8"
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "ASR"
+ "B16@0:8"
+ "B16@?0@8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "BMBookmark"
+ "ContextualReplayRecord"
+ "NSCoding"
+ "NSObject"
+ "NSSecureCoding"
+ "Q16@0:8"
+ "Record does not meet experiment record filter criteria, skipping replay for requestID %s"
+ "SearchOrMessaging"
+ "Siri"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "contextualReplayRecord"
+ "debugDescription"
+ "description"
+ "drivableSinkWithBookmark:completion:shouldContinue:"
+ "encodeWithCoder:"
+ "eventBody"
+ "hash"
+ "ids"
+ "initWithCoder:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "metadata"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "publisherWithUseCase:"
+ "release"
+ "requestId"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "superclass"
+ "supportsSecureCoding"
+ "task"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@16"
+ "v24@?0@\"BPSCompletion\"8@\"<BMBookmark>\"16"
+ "zone"
- "Exception thrown: %@"

```
