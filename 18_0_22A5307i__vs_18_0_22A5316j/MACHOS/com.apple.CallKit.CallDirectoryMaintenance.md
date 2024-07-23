## com.apple.CallKit.CallDirectoryMaintenance

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance`

```diff

-1266.100.1.0.0
-  __TEXT.__text: 0x19b44
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x1034
-  __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0xa97
-  __TEXT.__objc_methname: 0x34d1
-  __TEXT.__objc_classname: 0x398
-  __TEXT.__objc_methtype: 0xbde
+1268.100.11.0.0
+  __TEXT.__text: 0x1ce6c
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__objc_methlist: 0x10c4
+  __TEXT.__const: 0x2c8
+  __TEXT.__cstring: 0xba7
+  __TEXT.__objc_methname: 0x372d
+  __TEXT.__objc_classname: 0x3b9
+  __TEXT.__objc_methtype: 0xcaf
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__oslogstring: 0x21c0
-  __TEXT.__swift5_typeref: 0x10a
-  __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_reflstr: 0x72
-  __TEXT.__swift5_fieldmd: 0x5c
-  __TEXT.__swift5_capture: 0x54
-  __TEXT.__swift5_proto: 0x4
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x5d0
-  __TEXT.__eh_frame: 0x298
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__oslogstring: 0x23a0
+  __TEXT.__constg_swiftt: 0x110
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_typeref: 0x1c6
+  __TEXT.__swift5_reflstr: 0xa2
+  __TEXT.__swift5_fieldmd: 0xb0
+  __TEXT.__swift5_capture: 0x7c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__unwind_info: 0x678
+  __TEXT.__eh_frame: 0x500
+  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2a50
-  __DATA.__objc_selrefs: 0xb68
-  __DATA.__objc_ivar: 0x120
-  __DATA.__objc_data: 0x620
-  __DATA.__data: 0x648
-  __DATA.__bss: 0x90
+  __DATA.__objc_const: 0x2bb8
+  __DATA.__objc_selrefs: 0xbc0
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0x6e0
+  __DATA.__data: 0x738
+  __DATA.__bss: 0x110
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IdentityLookup.framework/IdentityLookup
+  - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
+  - /System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libBASupport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 617
-  Symbols:   217
-  CStrings:  901
+  Functions: 669
+  Symbols:   230
+  CStrings:  940
 
Symbols:
+ _BlastDoorInstanceTypeKnownSender
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$__TtC42com_apple_CallKit_CallDirectoryMaintenance21SecureImageTranscoder
+ _OBJC_METACLASS_$__TtC42com_apple_CallKit_CallDirectoryMaintenance21SecureImageTranscoder
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ _objc_retain_x6
+ _swift_deletedAsyncMethodErrorTu
+ _swift_deletedMethodError
+ _swift_dynamicCastClass
+ _swift_getForeignTypeMetadata
CStrings:
+ "\x03\x11"
+ "\x14s"
+ "/var/mobile/Library/CallDirectory/images"
+ "@\"<CXCallDirectoryUpdateDelegate>\""
+ "@\"_TtC42com_apple_CallKit_CallDirectoryMaintenance21SecureImageTranscoder\""
+ "@56@0:8@16@24@32@40@48"
+ "@72@0:8@16@24@32@40Q48@56@64"
+ "Attempting to generate preview of image after writing to URL: %!s(MISSING)"
+ "CXCallDirectoryUpdateDelegate"
+ "Error blastdooring image for handle: %!@(MISSING): %!@(MISSING)"
+ "Error creating temporary images directory: %!s(MISSING)"
+ "Generated preview with result: %!s(MISSING)"
+ "Generating preview from file: %!s(MISSING)"
+ "Received empty image result from BlastDoor"
+ "Received unsupported result type: %!s(MISSING)"
+ "T@\"<CXCallDirectoryUpdateDelegate>\",&,N,V_updateDelegate"
+ "T@\"_TtC42com_apple_CallKit_CallDirectoryMaintenance21SecureImageTranscoder\",&,N,V_imageTranscoder"
+ "Tq,N,V_lastInformationUpdate"
+ "_TtC42com_apple_CallKit_CallDirectoryMaintenance21SecureImageTranscoder"
+ "_imageTranscoder"
+ "_lastInformationUpdate"
+ "_updateDelegate"
+ "blastDoor"
+ "blastdoor successful, wrote image: %!@(MISSING)"
+ "callDirectoryHost:requestedLastUpdatedInfoWithCompletionHandler:"
+ "callDirectoryLastInformationUpdatedForPhoneNumber:"
+ "endpoint"
+ "generatePreview(forAttachmentWith:)"
+ "generatePreviewImageFrom:completionHandler:"
+ "imageTranscoder"
+ "initWithExtensionIdentifier:dataRequest:queue:store:lastUpdateDelegate:"
+ "initWithExtensionIdentifier:dataRequest:queue:store:maximumAllowedEntries:identificationEntriesChangedNotifier:lastUpdateDelegate:"
+ "lastInformationUpdate"
+ "networkConfig endpoint=%!s(MISSING) privacyProxyFailOpen=%!{(MISSING)bool}d"
+ "privacyProxyFailOpen"
+ "setImageTranscoder:"
+ "setLastInformationUpdate:"
+ "setUpdateDelegate:"
+ "updateDelegate"
+ "v16@?0@\"NSURL\"8"
+ "v32@0:8@\"CXCallDirectoryHost\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v48@0:8@16@24@32@?40"
+ "writeImageIfNecessary:extensionIdentifier:handle:completionHandler:"
- "\x14r"
- "@64@0:8@16@24@32@40Q48@56"
- "initWithExtensionIdentifier:dataRequest:queue:store:"
- "initWithExtensionIdentifier:dataRequest:queue:store:maximumAllowedEntries:identificationEntriesChangedNotifier:"
- "writeImageIfNecessary:extensionIdentifier:handle:"

```
