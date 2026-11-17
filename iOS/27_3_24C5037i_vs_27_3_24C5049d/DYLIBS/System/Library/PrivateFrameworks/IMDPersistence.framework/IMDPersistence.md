## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1491.300.43.0.0
-  __TEXT.__text: 0x2f7fa4
-  __TEXT.__objc_methlist: 0xaa5c
-  __TEXT.__const: 0xc3c0
-  __TEXT.__cstring: 0x5ef14
-  __TEXT.__oslogstring: 0x3c3a4
-  __TEXT.__gcc_except_tab: 0xc688
+1491.300.74.0.0
+  __TEXT.__text: 0x2f996c
+  __TEXT.__objc_methlist: 0xaa7c
+  __TEXT.__const: 0xc4c0
+  __TEXT.__cstring: 0x5ef64
+  __TEXT.__oslogstring: 0x3c4a4
+  __TEXT.__gcc_except_tab: 0xc690
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
-  __TEXT.__swift5_typeref: 0x52ca
-  __TEXT.__swift5_capture: 0x2064
-  __TEXT.__constg_swiftt: 0x59b8
+  __TEXT.__swift5_typeref: 0x5314
+  __TEXT.__swift5_capture: 0x2084
+  __TEXT.__constg_swiftt: 0x5a54
   __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_reflstr: 0x38f9
-  __TEXT.__swift5_fieldmd: 0x36e8
+  __TEXT.__swift5_reflstr: 0x3919
+  __TEXT.__swift5_fieldmd: 0x3738
   __TEXT.__swift5_assocty: 0x770
   __TEXT.__swift5_proto: 0x4c0
-  __TEXT.__swift5_types: 0x390
+  __TEXT.__swift5_types: 0x398
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift_as_entry: 0x168
-  __TEXT.__swift_as_ret: 0x184
-  __TEXT.__swift_as_cont: 0x3a8
+  __TEXT.__swift_as_entry: 0x17c
+  __TEXT.__swift_as_ret: 0x190
+  __TEXT.__swift_as_cont: 0x35c
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xd7f0
-  __TEXT.__eh_frame: 0x9e14
+  __TEXT.__unwind_info: 0xd858
+  __TEXT.__eh_frame: 0x9dec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x65c0
+  __DATA_CONST.__const: 0x65e8
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c98
+  __DATA_CONST.__objc_selrefs: 0x6cd0
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __DATA_CONST.__got: 0x1c68
-  __AUTH_CONST.__const: 0xe460
+  __DATA_CONST.__got: 0x1c70
+  __AUTH_CONST.__const: 0xe610
   __AUTH_CONST.__cfstring: 0x131e0
-  __AUTH_CONST.__objc_const: 0x14a40
+  __AUTH_CONST.__objc_const: 0x14a70
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2a18
+  __AUTH_CONST.__auth_got: 0x2a30
   __AUTH.__objc_data: 0x1240
   __AUTH.__data: 0x1ce0
   __DATA.__objc_ivar: 0x584
-  __DATA.__data: 0x3e60
+  __DATA.__data: 0x3f60
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x30b8
   __DATA_DIRTY.__data: 0x6560

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13929
-  Symbols:   2877
-  CStrings:  7574
+  Functions: 13961
+  Symbols:   2879
+  CStrings:  7578
 
Symbols:
+ _OBJC_CLASS_$_IMBusinessLogoManager
+ _strlen
CStrings:
+ "Business logo fetched for %@, calling interaction updated handler"
+ "Clearing payload data for message %{public}@, balloonBundleID %{public}@, forceReplace %{BOOL}d"
+ "Dropping retraction stamp for message %{public}@, balloonBundleID %{public}@, forceReplace %{BOOL}d"
+ "INInteraction updated, updating posted notification for message %@"
+ "Not a Check In message from a known chat, leaving the notification untouched"
+ "SELECT date FROM message WHERE date > 0 ORDER BY date ASC LIMIT 1;"
+ "v16@?0@\"IMBusinessLogoFile\"8"
+ "withDisconnectHandling(cancellable:_:)"
- "Not synthesizing notification content from intent, message is a business chat message"
- "Unable to extract URL from Message, supressing the notification"
- "withThrowUponDisconnect(_:)"
- "withThrowingQueryProviderUponDisconnect(_:_:)"
```
