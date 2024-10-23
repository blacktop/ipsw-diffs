## AppleIDSetup

> `/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x1bd948
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0xb80
-  __TEXT.__const: 0x186a8
-  __TEXT.__cstring: 0x36c1
-  __TEXT.__oslogstring: 0x3600
-  __TEXT.__swift5_typeref: 0x648e
-  __TEXT.__constg_swiftt: 0x6394
-  __TEXT.__swift5_builtin: 0x294
-  __TEXT.__swift5_reflstr: 0x32a9
-  __TEXT.__swift5_fieldmd: 0x55f0
-  __TEXT.__swift5_assocty: 0x718
-  __TEXT.__swift5_proto: 0x19c8
-  __TEXT.__swift5_types: 0x708
-  __TEXT.__swift5_capture: 0x1a48
-  __TEXT.__swift5_mpenum: 0xc8
+50.225.0.0.0
+  __TEXT.__text: 0x1de6ac
+  __TEXT.__auth_stubs: 0x24f0
+  __TEXT.__objc_methlist: 0xbb0
+  __TEXT.__const: 0x18bd8
+  __TEXT.__cstring: 0x36e1
+  __TEXT.__oslogstring: 0x3720
+  __TEXT.__swift5_typeref: 0x664e
+  __TEXT.__constg_swiftt: 0x6300
+  __TEXT.__swift5_builtin: 0x26c
+  __TEXT.__swift5_reflstr: 0x3499
+  __TEXT.__swift5_fieldmd: 0x5854
+  __TEXT.__swift5_assocty: 0x730
+  __TEXT.__swift5_proto: 0x1a44
+  __TEXT.__swift5_types: 0x720
+  __TEXT.__swift5_capture: 0x19c8
+  __TEXT.__swift5_mpenum: 0xbc
   __TEXT.__swift5_protos: 0x9c
-  __TEXT.__unwind_info: 0x83a8
-  __TEXT.__eh_frame: 0xc564
-  __TEXT.__objc_classname: 0x1be
-  __TEXT.__objc_methname: 0x223e
+  __TEXT.__unwind_info: 0x8300
+  __TEXT.__eh_frame: 0xc218
+  __TEXT.__objc_classname: 0x1bf
+  __TEXT.__objc_methname: 0x234e
   __TEXT.__objc_methtype: 0x68c
   __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0xbf0
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__const: 0xc10
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x880
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__auth_ptr: 0xbc8
-  __AUTH_CONST.__const: 0xec08
+  __AUTH_CONST.__auth_got: 0x1280
+  __AUTH_CONST.__auth_ptr: 0xb78
+  __AUTH_CONST.__const: 0xef90
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x5258
-  __AUTH.__objc_data: 0x21a8
-  __AUTH.__data: 0x23c0
-  __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x7978
-  __DATA.__bss: 0x316b0
+  __AUTH_CONST.__objc_const: 0x51e0
+  __AUTH.__objc_data: 0x2158
+  __AUTH.__data: 0x2528
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__data: 0x7c30
+  __DATA.__bss: 0x32520
   __DATA.__common: 0xc8
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x998
+  __DATA_DIRTY.__data: 0x7e8
   __DATA_DIRTY.__bss: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10930
-  Symbols:   653
-  CStrings:  1161
+  Functions: 10951
+  Symbols:   657
+  CStrings:  1177
 
Symbols:
+ _GestaltProductTypeStringToDeviceClass
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceClassNumber
- _objc_retain_x10
CStrings:
+ "$#\x11"
+ "Apple Vision Pro"
+ "Converting objc setup context with properties (relaxed: %!{(MISSING)bool}d): {\n  requiredServiceTypes:%!s(MISSING),\n  desiredServiceTypes:%!s(MISSING),\n  shouldBackgroundDesiredServices:%!{(MISSING)bool}d,\n  messageSessionTemplate:%!@(MISSING),\n  bleDevice:%!@(MISSING),\n  localRole:%!l(MISSING)u,\n  remoteRole:%!l(MISSING)u,\n  fixedPIN:%!s(MISSING),\n  targetAuthTag:%!s(MISSING),\n  pinType:%!d(MISSING),\n  deviceUserKind:%!l(MISSING)u,\n  shouldCreateDeviceUser:%!{(MISSING)bool}d,\n  shouldSkipConfirmation:%!{(MISSING)bool}d,\n  candidateAltDSID:%!s(MISSING),\n  candidateUserName:%!s(MISSING),\n  serverDeviceModel:%!s(MISSING)\n}"
+ "Finished registering the message session. Ready for sending/receiving messages!"
+ "GameCenter"
+ "Performing handshake (isKeepAlive: %!{(MISSING)bool}d) with request command: %!s(MISSING)"
+ "Registering the message session with identifier: %!s(MISSING)"
+ "Retrying another handshake, we failed to receive a response: %!@(MISSING)"
+ "Retrying another handshake, we failed to send request, handler not set up yet"
+ "Sending handshake request command: %!s(MISSING)"
+ "T@\"NSString\",C,N,V_serverDeviceModel"
+ "TB,N,V_isPreEstablishedClient"
+ "_isPreEstablishedClient"
+ "_serverDeviceModel"
+ "ak_isUserCancelError"
+ "ak_isUserSkippedError"
+ "auth_plugin_modernization"
+ "dismissBasicLoginUI"
+ "dismissSecondFactor"
+ "dismissServerProvidedUI"
+ "initWithRequest:requestType:"
+ "isPreEstablishedClient"
+ "secondFactorAlert"
+ "serverDeviceModel"
+ "setIsPreEstablishedClient:"
+ "setServerDeviceModel:"
- "\x14#"
- "Converting objc setup context with properties (relaxed: %!{(MISSING)bool}d): {\n  requiredServiceTypes:%!s(MISSING),\n  desiredServiceTypes:%!s(MISSING),\n  shouldBackgroundDesiredServices:%!{(MISSING)bool}d,\n  messageSessionTemplate:%!@(MISSING),\n  bleDevice:%!@(MISSING),\n  localRole:%!l(MISSING)u,\n  remoteRole:%!l(MISSING)u,\n  fixedPIN:%!s(MISSING),\n  targetAuthTag:%!s(MISSING),\n  pinType:%!d(MISSING),\n  deviceUserKind:%!l(MISSING)u,\n  shouldCreateDeviceUser:%!{(MISSING)bool}d,\n  shouldSkipConfirmation:%!{(MISSING)bool}d,\n  candidateAltDSID:%!s(MISSING),\n  candidateUserName:%!s(MISSING)\n}"
- "Failed to send request, handler not set up yet"
- "Performing handshake (isKeepAlive: %!{(MISSING)bool}d) with command: %!s(MISSING)"
- "SECOND_FACTOR_ALERT_MESSAGE"
- "SECOND_FACTOR_ALERT_TITLE"
- "Sending handshake command: %!s(MISSING)"
- "_TtC12AppleIDSetup10SetupModel"
- "_TtC12AppleIDSetup11RepairModel"
- "_lockedModelData"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"

```
