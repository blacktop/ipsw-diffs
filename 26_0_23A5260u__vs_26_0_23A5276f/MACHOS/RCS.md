## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1436.100.6.2.12
-  __TEXT.__text: 0xd56cc
-  __TEXT.__auth_stubs: 0x1ad0
+1440.100.7.2.5
+  __TEXT.__text: 0xd461c
+  __TEXT.__auth_stubs: 0x1ab0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0x844
-  __TEXT.__const: 0x4ec0
+  __TEXT.__const: 0x4e60
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x488b
+  __TEXT.__objc_methname: 0x48c4
   __TEXT.__objc_methtype: 0xe70
-  __TEXT.__cstring: 0x3145
-  __TEXT.__constg_swiftt: 0x1d60
-  __TEXT.__swift5_typeref: 0x1d4f
+  __TEXT.__cstring: 0x3135
+  __TEXT.__constg_swiftt: 0x1d24
+  __TEXT.__swift5_typeref: 0x1d21
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x117c
+  __TEXT.__swift5_reflstr: 0x116c
   __TEXT.__swift5_assocty: 0x2c0
-  __TEXT.__oslogstring: 0x5639
-  __TEXT.__swift5_fieldmd: 0x15f4
+  __TEXT.__oslogstring: 0x5689
+  __TEXT.__swift5_fieldmd: 0x15d0
   __TEXT.__swift5_proto: 0x2e4
   __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift_as_entry: 0x230
-  __TEXT.__swift_as_ret: 0x288
-  __TEXT.__swift5_capture: 0x8f0
+  __TEXT.__swift_as_entry: 0x228
+  __TEXT.__swift_as_ret: 0x284
+  __TEXT.__swift5_capture: 0x884
   __TEXT.__swift5_mpenum: 0xbc
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x30d0
-  __TEXT.__eh_frame: 0x81a0
-  __DATA_CONST.__auth_got: 0xd70
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__auth_ptr: 0x548
-  __DATA_CONST.__const: 0x4e88
+  __TEXT.__unwind_info: 0x3050
+  __TEXT.__eh_frame: 0x80a8
+  __DATA_CONST.__auth_got: 0xd60
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__auth_ptr: 0x540
+  __DATA_CONST.__const: 0x4db8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1e90
-  __DATA.__objc_selrefs: 0x14b8
-  __DATA.__objc_data: 0x438
-  __DATA.__data: 0x32e8
+  __DATA.__objc_const: 0x1e78
+  __DATA.__objc_selrefs: 0x14c8
+  __DATA.__objc_data: 0x3e8
+  __DATA.__data: 0x3288
   __DATA.__bss: 0x4880
-  __DATA.__common: 0xb8
+  __DATA.__common: 0x98
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7BC082FD-87C7-31A5-A4B9-04BB555083C9
-  Functions: 3167
-  Symbols:   402
+  UUID: EBFCD802-573D-39D5-8036-93A0B820E421
+  Functions: 3134
+  Symbols:   399
   CStrings:  1442
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _swift_deletedAsyncMethodErrorTu
CStrings:
+ "Found chatbot sip uri: %s for original uri: %s"
+ "Sending RCS send message metric with subtype %s, messageSize %llu, originalServiceName %s, receiverType %s, receiverGroupType %s, duration %f, error %u"
+ "__im_isSipHandle"
+ "originalServiceName"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"
- "Sending RCS send message metric with subtype %s, messageSize %llu, receiverType %s, reciverGroupType %s, duration %f, error %u"
- "block"
- "interval"
- "priority"
- "trackSentMessageEventOfType:subtype:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"

```
