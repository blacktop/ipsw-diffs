## ASRBridge

> `/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x4e6ec
-  __TEXT.__auth_stubs: 0x2380
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0xbc8
-  __TEXT.__cstring: 0x1ce5
-  __TEXT.__constg_swiftt: 0xee4
-  __TEXT.__swift5_typeref: 0x9ea
-  __TEXT.__swift5_reflstr: 0xa5d
-  __TEXT.__swift5_fieldmd: 0x750
-  __TEXT.__oslogstring: 0x45eb
+3404.71.4.1.1
+  __TEXT.__text: 0x4dca0
+  __TEXT.__auth_stubs: 0x2360
+  __TEXT.__objc_methlist: 0xaa0
+  __TEXT.__const: 0xc58
+  __TEXT.__cstring: 0x1a45
+  __TEXT.__constg_swiftt: 0xf44
+  __TEXT.__swift5_typeref: 0x9f0
+  __TEXT.__swift5_reflstr: 0xb1d
+  __TEXT.__swift5_fieldmd: 0x78c
+  __TEXT.__oslogstring: 0x47fb
   __TEXT.__swift5_capture: 0x6a0
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x64
-  __TEXT.__unwind_info: 0x828
+  __TEXT.__unwind_info: 0x820
   __TEXT.__eh_frame: 0x2f0
   __TEXT.__objc_classname: 0x18d
-  __TEXT.__objc_methname: 0x2518
-  __TEXT.__objc_methtype: 0xecd
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xf8
+  __TEXT.__objc_methname: 0x2597
+  __TEXT.__objc_methtype: 0xef3
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x850
   __DATA_CONST.__objc_protorefs: 0x98
-  __AUTH_CONST.__auth_got: 0x11c0
-  __AUTH_CONST.__auth_ptr: 0x3e0
+  __AUTH_CONST.__auth_got: 0x11b0
+  __AUTH_CONST.__auth_ptr: 0x3f0
   __AUTH_CONST.__const: 0x1590
-  __AUTH_CONST.__objc_const: 0x2950
+  __AUTH_CONST.__objc_const: 0x1ab0
   __AUTH.__objc_data: 0x278
-  __AUTH.__data: 0x2b8
+  __AUTH.__data: 0x2c8
   __DATA.__data: 0x990
   __DATA.__common: 0x68
   __DATA.__bss: 0x400
   __DATA_DIRTY.__objc_data: 0x728
-  __DATA_DIRTY.__data: 0xbe0
-  __DATA_DIRTY.__common: 0x230
+  __DATA_DIRTY.__data: 0xbb0
+  __DATA_DIRTY.__common: 0x238
   __DATA_DIRTY.__bss: 0x600
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 953
-  Symbols:   301
-  CStrings:  830
+  Functions: 949
+  Symbols:   309
+  CStrings:  829
 
Symbols:
+ _OBJC_CLASS_$_SAHomeMemberInfo
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _AFDeviceSupportsSAE
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x10
- _swift_initStructMetadata
CStrings:
+ "#user-session: final user session state: %s."
+ "#user-session: received message: %@"
+ "ActiveUserSessionDetectedMessage does not belong to current session id: %s"
+ "Setting userSessionState to ambient"
+ "Unable to find isSystemAssistantExperienceEnabled to pass to AsrRequestProcessor"
+ "activeUserInfo found matching home member"
+ "activeUserInfo sharedUserId: %s with loggableSharedUserId:  %s and persona ID: %s"
+ "activeUserInfo will look for matching home member from %s"
+ "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:"
+ "initWithSharedUserId:loggableSharedUserId:personaId:"
+ "isSystemAssistantExperienceEnabled"
+ "nil activePersonaId"
+ "nil loggableSharedUserId "
+ "nil sharedUserId"
+ "personaId"
+ "registerInternalGestureTestingHandler:"
+ "userSessionState"
+ "v24@0:8@?<v@?qB@?<v@?B@\"NSString\">>16"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "asrResultCandidateAcceptedMUX"
- "asrResultCandidateAcceptedMUXFailure"
- "asrResultCandidateAcceptedMessagePostedFailure"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:"
- "invalid Collection: less than 'count' elements in collection"
- "isAssistantEngineEnabled"

```
