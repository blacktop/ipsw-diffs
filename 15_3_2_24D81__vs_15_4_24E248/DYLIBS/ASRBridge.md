## ASRBridge

> `/System/Library/PrivateFrameworks/ASRBridge.framework/Versions/A/ASRBridge`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x4ea68
-  __TEXT.__auth_stubs: 0x2130
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0xbc8
-  __TEXT.__cstring: 0x1c85
-  __TEXT.__constg_swiftt: 0xee4
-  __TEXT.__swift5_typeref: 0x9b4
-  __TEXT.__swift5_reflstr: 0xa5d
-  __TEXT.__swift5_fieldmd: 0x750
-  __TEXT.__oslogstring: 0x453b
+3404.82.3.0.0
+  __TEXT.__text: 0x580b8
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__objc_methlist: 0xa98
+  __TEXT.__const: 0xbe8
+  __TEXT.__cstring: 0x19e5
+  __TEXT.__constg_swiftt: 0xf44
+  __TEXT.__swift5_typeref: 0x9c0
+  __TEXT.__swift5_reflstr: 0xb1d
+  __TEXT.__swift5_fieldmd: 0x78c
+  __TEXT.__oslogstring: 0x474b
   __TEXT.__swift5_capture: 0x664
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x64
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__eh_frame: 0x2f0
   __TEXT.__objc_classname: 0x18d
-  __TEXT.__objc_methname: 0x24d2
-  __TEXT.__objc_methtype: 0xec5
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x100
+  __TEXT.__objc_methname: 0x2551
+  __TEXT.__objc_methtype: 0xeeb
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x578
+  __DATA_CONST.__objc_selrefs: 0x838
   __DATA_CONST.__objc_protorefs: 0x98
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x1090
   __AUTH_CONST.__const: 0x14f0
-  __AUTH_CONST.__objc_const: 0x2930
+  __AUTH_CONST.__objc_const: 0x1aa8
   __AUTH.__objc_data: 0x9a0
   __AUTH.__data: 0x918
-  __DATA.__data: 0xde0
-  __DATA.__common: 0x280
+  __DATA.__data: 0xdd0
+  __DATA.__common: 0x288
   __DATA.__bss: 0xa00
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B493AAAD-D9D2-38DC-B8AC-C6E134C39D47
-  Functions: 939
-  Symbols:   655
-  CStrings:  820
+  UUID: E9B4E82A-707D-3D60-8596-E854E64BF905
+  Functions: 950
+  Symbols:   658
+  CStrings:  819
 
Symbols:
+ _OBJC_CLASS_$_SAHomeMemberInfo
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ _symbolic SbSg
+ _symbolic _____ 16SiriMessageTypes16UserSessionStateO
- _AFDeviceSupportsSAE
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_ASRBridge
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ASRBridge
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
