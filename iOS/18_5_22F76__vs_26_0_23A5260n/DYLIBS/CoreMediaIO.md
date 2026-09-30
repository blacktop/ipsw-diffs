## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

```diff

-5590.122.2.0.1
-  __TEXT.__text: 0x46954
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x1f9c
+5610.0.0.0.0
+  __TEXT.__text: 0x46dd4
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_methlist: 0x2014
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x16b8
-  __TEXT.__cstring: 0x8386
-  __TEXT.__oslogstring: 0x41f0
+  __TEXT.__cstring: 0x84e4
+  __TEXT.__oslogstring: 0x42ae
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__unwind_info: 0xc90
-  __TEXT.__objc_classname: 0x395
-  __TEXT.__objc_methname: 0x4ba9
+  __TEXT.__unwind_info: 0xca8
+  __TEXT.__objc_classname: 0x3bf
+  __TEXT.__objc_methname: 0x4c76
   __TEXT.__objc_methtype: 0x10e4
-  __TEXT.__objc_stubs: 0x30e0
+  __TEXT.__objc_stubs: 0x3180
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xd88
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfb0
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x708
+  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x3890
-  __DATA.__objc_ivar: 0x354
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x39f0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x364
   __DATA.__data: 0x4b0
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__bss: 0x70
-  __DATA_DIRTY.__common: 0x1d
+  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E32E674C-FC1D-3754-8105-D3E2AD8B4B73
-  Functions: 1315
-  Symbols:   4349
-  CStrings:  2187
+  UUID: 0F15476B-3499-3643-B6C3-3027818F6845
+  Functions: 1329
+  Symbols:   4398
+  CStrings:  2222
 
Symbols:
+ -[CMIOExtensionDiscoverySession completeRegistration:]
+ -[CMIOExtensionDiscoverySessionRegistration bundleID]
+ -[CMIOExtensionDiscoverySessionRegistration dealloc]
+ -[CMIOExtensionDiscoverySessionRegistration initWithBundleID:token:]
+ -[CMIOExtensionDiscoverySessionRegistration isRetryAllowed]
+ -[CMIOExtensionDiscoverySessionRegistration numOfRetryAttempts]
+ -[CMIOExtensionDiscoverySessionRegistration setBundleID:]
+ -[CMIOExtensionDiscoverySessionRegistration setNumOfRetryAttempts:]
+ -[CMIOExtensionDiscoverySessionRegistration setToken:]
+ -[CMIOExtensionDiscoverySessionRegistration token]
+ _CMIOExtensionPropertyStreamDeskViewCameraZoomFactor
+ _CMIOExtensionPropertyStreamHumanHandDetectionEnabled
+ _CMIOExtensionPropertyStreamHumanHeadDetectionEnabled
+ _OBJC_CLASS_$_CMIOExtensionDiscoverySessionRegistration
+ _OBJC_IVAR_$_CMIOExtensionDiscoverySessionRegistration._bundleID
+ _OBJC_IVAR_$_CMIOExtensionDiscoverySessionRegistration._numOfRetryAttempts
+ _OBJC_IVAR_$_CMIOExtensionDiscoverySessionRegistration._token
+ _OBJC_IVAR_$_CMIOExtensionStream._metadataSequenceNumber
+ _OBJC_METACLASS_$_CMIOExtensionDiscoverySessionRegistration
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ __OBJC_$_INSTANCE_METHODS_CMIOExtensionDiscoverySessionRegistration
+ __OBJC_$_INSTANCE_VARIABLES_CMIOExtensionDiscoverySessionRegistration
+ __OBJC_$_PROP_LIST_CMIOExtensionDiscoverySessionRegistration
+ __OBJC_CLASS_RO_$_CMIOExtensionDiscoverySessionRegistration
+ __OBJC_METACLASS_RO_$_CMIOExtensionDiscoverySessionRegistration
+ ___50-[CMIOExtensionDiscoverySession setUpRegistration]_block_invoke.61
+ ___50-[CMIOExtensionDiscoverySession setUpRegistration]_block_invoke.61.cold.1
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke.51
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke.52
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke.52.cold.1
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke.53
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke_2
+ ___54-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke_2.cold.1
+ ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.441
+ ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.443
+ ___67-[CMIOExtensionProvider consumeSampleBufferForStream:client:reply:]_block_invoke.457
+ ___81-[CMIOExtensionProvider setPluginPropertyValuesForClientID:propertyValues:reply:]_block_invoke.422
+ ___86-[CMIOExtensionProvider enqueueReactionEffectForClientID:streamID:reactionType:reply:]_block_invoke.451
+ ___90-[CMIOExtensionProvider setDevicePropertyValuesForClientID:deviceID:propertyValues:reply:]_block_invoke.433
+ ___90-[CMIOExtensionProvider setStreamPropertyValuesForClientID:streamID:propertyValues:reply:]_block_invoke.437
+ ___91-[CMIOExtensionProvider captureAsyncStillImageForClientID:streamID:uniqueID:options:reply:]_block_invoke.448
+ ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.444
+ ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.444.cold.1
+ ___block_descriptor_52_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.333
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.359
+ ___block_literal_global.42
+ ___block_literal_global.64
+ _cmio_clientApplicationIDIsXCTest
+ _cmio_clientApplicationIDIsXCTest.cold.1
+ _cmio_clientIsRunningInXCTest
+ _cmio_clientIsRunningInXCTestWithSecTask
+ _dispatch_after
+ _internalProperties.onceToken.246
+ _internalProperties.onceToken.331
+ _objc_msgSend$completeRegistration:
+ _objc_msgSend$initWithBundleID:token:
+ _objc_msgSend$isRetryAllowed
+ _objc_msgSend$numOfRetryAttempts
+ _objc_msgSend$setNumOfRetryAttempts:
+ _objc_msgSend$token
+ _objc_setProperty_nonatomic
- -[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]
- ___50-[CMIOExtensionDiscoverySession setUpRegistration]_block_invoke.25
- ___50-[CMIOExtensionDiscoverySession setUpRegistration]_block_invoke.25.cold.1
- ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.440
- ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.442
- ___67-[CMIOExtensionProvider consumeSampleBufferForStream:client:reply:]_block_invoke.456
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke.17
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke.17.cold.1
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke.18
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke_2
- ___71-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke_2.cold.1
- ___81-[CMIOExtensionProvider setPluginPropertyValuesForClientID:propertyValues:reply:]_block_invoke.421
- ___86-[CMIOExtensionProvider enqueueReactionEffectForClientID:streamID:reactionType:reply:]_block_invoke.450
- ___90-[CMIOExtensionProvider setDevicePropertyValuesForClientID:deviceID:propertyValues:reply:]_block_invoke.432
- ___90-[CMIOExtensionProvider setStreamPropertyValuesForClientID:streamID:propertyValues:reply:]_block_invoke.436
- ___91-[CMIOExtensionProvider captureAsyncStillImageForClientID:streamID:uniqueID:options:reply:]_block_invoke.447
- ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.443
- ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.443.cold.1
- ___block_descriptor_56_e8_32o40o_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32o40o48o_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.28
- ___block_literal_global.332
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.358
- ___block_literal_global.8
- _internalProperties.onceToken.245
- _internalProperties.onceToken.330
- _objc_msgSend$completeRegistrationForBundleID:token:
CStrings:
+ "%s:%d:%s Got invalid endpoint and the registration doesn't allow retry, retried attempts: %d"
+ "%s:%d:%s Valid endpoint not presented... retry attempt %d, will try again in %d seconds"
+ "%s:%d:%s clientApplicationID is nil"
+ "%s:%d:%s retry attempt %d now trying to complete the registration"
+ "-[CMIOExtensionDiscoverySession completeRegistration:]"
+ "-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke"
+ "-[CMIOExtensionDiscoverySession completeRegistration:]_block_invoke_2"
+ "@32@0:8@16Q24"
+ "CMIOExtensionDiscoverySessionRegistration"
+ "DeskViewCameraZoomFactor"
+ "HumanHandDetectionEnabled"
+ "HumanHeadDetectionEnabled"
+ "T@\"NSString\",&,N,V_bundleID"
+ "TB,R,N"
+ "TQ,N,V_token"
+ "Ti,N,V_numOfRetryAttempts"
+ "_metadataSequenceNumber"
+ "_numOfRetryAttempts"
+ "_token"
+ "cmio_clientApplicationIDIsXCTest"
+ "com.apple.avfoundation.AVFCaptureTests-Embedded-Runner.xctrunner"
+ "com.apple.avfoundation.AVFoundation-OSX-Capture-Unit-Tests.xctrunner"
+ "com.apple.avfoundation.AVFoundation-macCatalyst-Capture-Unit-Tests.xctrunner"
+ "com.apple.cmio.ContinuityCaptureAgent"
+ "com.apple.dt.xctest.tool"
+ "com.apple.xctest"
+ "completeRegistration:"
+ "initWithBundleID:token:"
+ "isRetryAllowed"
+ "numOfRetryAttempts"
+ "setNumOfRetryAttempts:"
+ "setToken:"
+ "token"
+ "\xf02"
- "%s:%d:%s SetProperty - %@"
- "%s:%d:%s returning early because a valid endpoint was not provided"
- "-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]"
- "-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke"
- "-[CMIOExtensionDiscoverySession completeRegistrationForBundleID:token:]_block_invoke_2"
- "completeRegistrationForBundleID:token:"
- "v32@0:8@16Q24"
- "\xf0\""

```
