## SiriIntentEvents

> `/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents`

```diff

-3401.15.1.11.2
-  __TEXT.__text: 0x161e0
-  __TEXT.__auth_stubs: 0x890
+3402.43.1.1.2
+  __TEXT.__text: 0x16510
+  __TEXT.__auth_stubs: 0x8a0
   __TEXT.__objc_methlist: 0x58
-  __TEXT.__cstring: 0x741
-  __TEXT.__const: 0x1d70
-  __TEXT.__swift5_typeref: 0x4a1
+  __TEXT.__const: 0x1d80
+  __TEXT.__cstring: 0x731
+  __TEXT.__swift5_typeref: 0x49d
   __TEXT.__constg_swiftt: 0x6cc
-  __TEXT.__swift5_reflstr: 0x557
+  __TEXT.__swift5_reflstr: 0x53c
   __TEXT.__swift5_fieldmd: 0x828
   __TEXT.__swift5_proto: 0x1a4
   __TEXT.__swift5_types: 0x80
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__oslogstring: 0x33
-  __TEXT.__unwind_info: 0xae0
+  __TEXT.__oslogstring: 0x2e
+  __TEXT.__unwind_info: 0xad8
   __TEXT.__eh_frame: 0x1298
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x289
+  __TEXT.__objc_methname: 0x2e2
   __TEXT.__objc_methtype: 0x46
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__auth_ptr: 0x1c0
+  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_ptr: 0x1c8
   __AUTH_CONST.__const: 0xfc0
   __AUTH_CONST.__objc_const: 0x818
   __AUTH.__objc_data: 0x308
   __AUTH.__data: 0x550
-  __DATA.__data: 0x528
-  __DATA.__bss: 0x3000
+  __DATA.__data: 0x540
   __DATA.__common: 0xa0
+  __DATA.__bss: 0x3000
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x3c0
-  __DATA_DIRTY.__common: 0x20
+  __DATA_DIRTY.__data: 0x3d0
   __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 902
-  Symbols:   258
-  CStrings:  120
+  Functions: 905
+  Symbols:   263
+  CStrings:  125
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BMSQLColumn
+ _OBJC_CLASS_$_BMSQLSchema
+ _OBJC_CLASS_$_BMSiriIntent
+ _OBJC_CLASS_$_BMStream
+ _OBJC_CLASS_$_BMStreamConfiguration
+ _objc_retain_x23
+ _swift_getObjCClassFromMetadata
- _OBJC_CLASS_$_BMSiriIntentEvent
- _OBJC_CLASS_$_BMStoreStream
- _objc_release_x27
CStrings:
+ "Intent"
+ "Remembers"
+ "Siri"
+ "found BMStoreEvent<BMSiriIntent> with no body"
+ "initWithIdentifier:schema:configuration:"
+ "initWithIntentID:eventType:eventData:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "initWithStreamIdentifier:eventClass:storeConfig:"
+ "initWithTableName:columns:"
+ "intentID"
+ "publisherWithOptions:"
- "found BMStoreEvent<BMSiriIntentEvent> with no body"
- "initWithIntentId:eventType:eventData:"
- "initWithPrivateStreamIdentifier:storeConfig:"
- "initWithPublicStream:"
- "publisherWithStartTime:endTime:maxEvents:lastN:reversed:"

```
