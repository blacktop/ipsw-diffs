## CompanionServices

> `/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices`

```diff

-156.50.26.0.0
-  __TEXT.__text: 0xd510
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x13ac
+276.0.2.1.2
+  __TEXT.__text: 0xdc68
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x153c
   __TEXT.__const: 0x532
-  __TEXT.__cstring: 0x144c
+  __TEXT.__cstring: 0x14ac
   __TEXT.__oslogstring: 0x1ef
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__dlopen_cstrs: 0x63

   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x548
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x40b
-  __TEXT.__objc_methname: 0x2954
-  __TEXT.__objc_methtype: 0x6e7
+  __TEXT.__objc_classname: 0x457
+  __TEXT.__objc_methname: 0x2b9a
+  __TEXT.__objc_methtype: 0x71c
   __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x910
+  __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x328
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0x2b70
-  __AUTH.__objc_data: 0x9b0
+  __AUTH_CONST.__cfstring: 0x1260
+  __AUTH_CONST.__objc_const: 0x2f20
+  __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0x480
   __DATA.__bss: 0x990
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6C88385C-896E-341C-B98D-E92D11B6BC2E
-  Functions: 524
-  Symbols:   1701
-  CStrings:  923
+  UUID: 7A4E6CEC-B045-3FE3-BE3C-6814F78666B3
+  Functions: 551
+  Symbols:   1779
+  CStrings:  964
 
Symbols:
+ +[CPSAmbientSetupRequest supportsSecureCoding]
+ +[CPSIncomingCallsRequest supportsSecureCoding]
+ +[CPSIncomingCallsResponse supportsSecureCoding]
+ -[CPSAmbientSetupRequest .cxx_destruct]
+ -[CPSAmbientSetupRequest authType]
+ -[CPSAmbientSetupRequest configurationURL]
+ -[CPSAmbientSetupRequest encodeWithCoder:]
+ -[CPSAmbientSetupRequest extensionToken]
+ -[CPSAmbientSetupRequest initWithCoder:]
+ -[CPSAmbientSetupRequest screensaverType]
+ -[CPSAmbientSetupRequest setConfigurationURL:]
+ -[CPSAmbientSetupRequest setExtensionToken:]
+ -[CPSAmbientSetupRequest setScreensaverType:]
+ -[CPSIncomingCallsRequest .cxx_destruct]
+ -[CPSIncomingCallsRequest appleAccountAltDSID]
+ -[CPSIncomingCallsRequest authType]
+ -[CPSIncomingCallsRequest description]
+ -[CPSIncomingCallsRequest deviceIdentifier]
+ -[CPSIncomingCallsRequest encodeWithCoder:]
+ -[CPSIncomingCallsRequest initWithCoder:]
+ -[CPSIncomingCallsRequest setAppleAccountAltDSID:]
+ -[CPSIncomingCallsRequest setDeviceIdentifier:]
+ -[CPSIncomingCallsResponse encodeWithCoder:]
+ -[CPSIncomingCallsResponse initWithCoder:]
+ -[CPSViewServicePresentationContext ambientSetupRequest]
+ -[CPSViewServicePresentationContext incomingCallsRequest]
+ -[CPSViewServicePresentationContext setAmbientSetupRequest:]
+ -[CPSViewServicePresentationContext setIncomingCallsRequest:]
+ _OBJC_CLASS_$_CPSAmbientSetupRequest
+ _OBJC_CLASS_$_CPSIncomingCallsRequest
+ _OBJC_CLASS_$_CPSIncomingCallsResponse
+ _OBJC_IVAR_$_CPSAmbientSetupRequest._configurationURL
+ _OBJC_IVAR_$_CPSAmbientSetupRequest._extensionToken
+ _OBJC_IVAR_$_CPSAmbientSetupRequest._screensaverType
+ _OBJC_IVAR_$_CPSIncomingCallsRequest._appleAccountAltDSID
+ _OBJC_IVAR_$_CPSIncomingCallsRequest._deviceIdentifier
+ _OBJC_IVAR_$_CPSViewServicePresentationContext._ambientSetupRequest
+ _OBJC_IVAR_$_CPSViewServicePresentationContext._incomingCallsRequest
+ _OBJC_METACLASS_$_CPSAmbientSetupRequest
+ _OBJC_METACLASS_$_CPSIncomingCallsRequest
+ _OBJC_METACLASS_$_CPSIncomingCallsResponse
+ __OBJC_$_CLASS_METHODS_CPSAmbientSetupRequest
+ __OBJC_$_CLASS_METHODS_CPSIncomingCallsRequest
+ __OBJC_$_CLASS_METHODS_CPSIncomingCallsResponse
+ __OBJC_$_CLASS_PROP_LIST_CPSAmbientSetupRequest
+ __OBJC_$_CLASS_PROP_LIST_CPSIncomingCallsRequest
+ __OBJC_$_CLASS_PROP_LIST_CPSIncomingCallsResponse
+ __OBJC_$_INSTANCE_METHODS_CPSAmbientSetupRequest
+ __OBJC_$_INSTANCE_METHODS_CPSIncomingCallsRequest
+ __OBJC_$_INSTANCE_METHODS_CPSIncomingCallsResponse
+ __OBJC_$_INSTANCE_VARIABLES_CPSAmbientSetupRequest
+ __OBJC_$_INSTANCE_VARIABLES_CPSIncomingCallsRequest
+ __OBJC_$_PROP_LIST_CPSAmbientSetupRequest
+ __OBJC_$_PROP_LIST_CPSIncomingCallsRequest
+ __OBJC_CLASS_PROTOCOLS_$_CPSAmbientSetupRequest
+ __OBJC_CLASS_PROTOCOLS_$_CPSIncomingCallsRequest
+ __OBJC_CLASS_PROTOCOLS_$_CPSIncomingCallsResponse
+ __OBJC_CLASS_RO_$_CPSAmbientSetupRequest
+ __OBJC_CLASS_RO_$_CPSIncomingCallsRequest
+ __OBJC_CLASS_RO_$_CPSIncomingCallsResponse
+ __OBJC_METACLASS_RO_$_CPSAmbientSetupRequest
+ __OBJC_METACLASS_RO_$_CPSIncomingCallsRequest
+ __OBJC_METACLASS_RO_$_CPSIncomingCallsResponse
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_CompanionServices
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CompanionServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CompanionServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CompanionServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CompanionServices
+ _swift_unknownObjectRelease
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_CompanionServices
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CompanionServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CompanionServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CompanionServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CompanionServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CompanionServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CompanionServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CompanionServices
CStrings:
+ "@\"CPSAmbientSetupRequest\""
+ "@\"CPSIncomingCallsRequest\""
+ "CPSAmbientSetupRequest"
+ "CPSIncomingCallsRequest"
+ "CPSIncomingCallsResponse"
+ "T@\"CPSAmbientSetupRequest\",&,N,V_ambientSetupRequest"
+ "T@\"CPSIncomingCallsRequest\",&,N,V_incomingCallsRequest"
+ "T@\"NSString\",&,N,V_deviceIdentifier"
+ "T@\"NSString\",&,N,V_extensionToken"
+ "T@\"NSURL\",&,N,V_configurationURL"
+ "Tq,N,V_screensaverType"
+ "_ambientSetupRequest"
+ "_configurationURL"
+ "_deviceIdentifier"
+ "_extensionToken"
+ "_incomingCallsRequest"
+ "_screensaverType"
+ "ambientSetupRequest"
+ "configurationURL"
+ "deviceIdentifier"
+ "extensionToken"
+ "incomingCallsRequest"
+ "screensaverType"
+ "setAmbientSetupRequest:"
+ "setConfigurationURL:"
+ "setDeviceIdentifier:"
+ "setExtensionToken:"
+ "setIncomingCallsRequest:"
+ "setScreensaverType:"

```
