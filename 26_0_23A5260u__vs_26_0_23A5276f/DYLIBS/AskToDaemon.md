## AskToDaemon

> `/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon`

```diff

-57.2.1.1.0
-  __TEXT.__text: 0x54564
+59.1.0.0.0
+  __TEXT.__text: 0x54694
   __TEXT.__auth_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x5f8
   __TEXT.__const: 0x2fa8
   __TEXT.__cstring: 0x2c0a
   __TEXT.__swift5_typeref: 0x1589
-  __TEXT.__swift5_fieldmd: 0xe90
+  __TEXT.__swift5_fieldmd: 0xe9c
   __TEXT.__constg_swiftt: 0x10f8
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0xed7
-  __TEXT.__oslogstring: 0x4184
+  __TEXT.__swift5_reflstr: 0xef7
+  __TEXT.__oslogstring: 0x4154
   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_proto: 0x21c

   __TEXT.__swift5_capture: 0x564
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__unwind_info: 0x11d8
-  __TEXT.__eh_frame: 0x289c
+  __TEXT.__eh_frame: 0x28c4
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x1940
+  __TEXT.__objc_methname: 0x194f
   __TEXT.__objc_methtype: 0x936
   __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_protorefs: 0x68
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x2840
   __AUTH_CONST.__objc_const: 0x16e8
   __AUTH.__objc_data: 0x3c0
-  __AUTH.__data: 0xd28
-  __DATA.__data: 0xee0
+  __AUTH.__data: 0xd18
+  __DATA.__data: 0xef0
   __DATA.__bss: 0x3800
   __DATA.__common: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts

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
-  UUID: 179E2BEE-C5B0-3EA1-A764-D45024BE269D
+  UUID: C07C3DF4-7051-3DC9-A1FA-277D14A668D0
   Functions: 1384
-  Symbols:   1131
+  Symbols:   1127
   CStrings:  859
 
Symbols:
+ ___swift_memcpy113_8
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_AskToDaemon
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_AskToDaemon
- ___swift_memcpy112_8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AskToDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AskToDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AskToDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AskToDaemon
CStrings:
+ "Skipping validation of send destinations since `shouldValidateSendDestinations` is false"
+ "payloadForSendRequest(question:to:originatingClientMetadata:shouldValidateSendDestinations:)"
+ "payloadForSendRequestWithQuestion:recipientGroup:clientPayload:shouldValidateSendDestinations:completionHandler:"
+ "setCachePolicy:"
- "Platform didn't support presenting ask flow."
- "Skipping validation of send destinations since `shouldValidateSendDestionations` is false"
- "payloadForSendRequest(question:to:originatingClientMetadata:shouldValidateSendDestionations:)"
- "payloadForSendRequestWithQuestion:recipientGroup:clientPayload:shouldValidateSendDestionations:completionHandler:"

```
