## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.25.1.0
-  __TEXT.__text: 0xbe0c4
-  __TEXT.__auth_stubs: 0x2740
+6.3.25.3.0
+  __TEXT.__text: 0xbe264
+  __TEXT.__auth_stubs: 0x2750
   __TEXT.__objc_stubs: 0x3880
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1380
-  __TEXT.__const: 0x595f
-  __TEXT.__gcc_except_tab: 0x8158
-  __TEXT.__objc_methname: 0x4a6f
-  __TEXT.__cstring: 0x3e01
-  __TEXT.__oslogstring: 0x4b6b
+  __TEXT.__const: 0x596f
+  __TEXT.__gcc_except_tab: 0x813c
+  __TEXT.__objc_methname: 0x4a85
+  __TEXT.__cstring: 0x3e81
+  __TEXT.__oslogstring: 0x4b9b
   __TEXT.__objc_classname: 0x307
-  __TEXT.__objc_methtype: 0xf3d
+  __TEXT.__objc_methtype: 0xf40
+  __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x3ae
   __TEXT.__swift5_capture: 0x228
   __TEXT.__constg_swiftt: 0x5d4

   __TEXT.__swift5_fieldmd: 0x220
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x4020
+  __TEXT.__unwind_info: 0x4038
   __TEXT.__eh_frame: 0xa70
-  __DATA_CONST.__auth_got: 0x13b8
-  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__auth_got: 0x13c0
+  __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x69e8
-  __DATA_CONST.__cfstring: 0x1cc0
+  __DATA_CONST.__const: 0x6a00
+  __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0xf08
   __DATA.__data: 0xd78
-  __DATA.__bss: 0xb10
+  __DATA.__bss: 0xb20
   __DATA.__common: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Speech.framework/Speech
-  - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3524
-  Symbols:   1326
-  CStrings:  2183
+  Functions: 3532
+  Symbols:   1327
+  CStrings:  2185
 
Symbols:
+ __ZN11RDQSREngine23DidGetUtteranceBoundaryExxx
+ __ZN11RDQSREngine31DidGetUtteranceBoundaryCallbackEPvxxx
+ __ZN19RDQSRCircularBufferIsE18totalFramesWrittenEv
+ __ZN19RDQSRCircularBufferIsE8seekBackEm
- _OBJC_CLASS_$_AXSystemAppServer
- __ZN11RDQSREngine23DidGetUtteranceBoundaryExx
- __ZN11RDQSREngine31DidGetUtteranceBoundaryCallbackEPvxx
CStrings:
+ "AXSystemAppServer"
+ "Class getAXSystemAppServerClass(void)_block_invoke"
+ "RDSoundInputImpl_iOS_Shared.m"
+ "SpeechDonation ::totalSamplesSent =%!l(MISSING)ld ::newUtteranceBeginSampleNumber :: start = %!l(MISSING)ld :: newUtteranceEndSampleNumber = %!l(MISSING)ld"
+ "SpeechDonation: Start Sample Number = %!l(MISSING)ld, end Sample number = %!l(MISSING)ld, samples in the utterance = %!l(MISSING)ld, totalSamplesSentToASR = %!l(MISSING)ld,  totalSamplesWritten = %!z(MISSING)u, sample overwritten by next utterance = %!z(MISSING)u"
+ "SpeechDonation: donation utterance has been overwritten in the circular buffer, don't donate"
+ "didGetUtteranceBoundary:utteranceEndSampleNumber:totalSamplesSentToASR:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities"
+ "v40@0:8q16q24q32"
+ "void *AccessibilityUtilitiesLibrary(void)"
- "SpeechDonation : new utterance boundary = %!l(MISSING)ld"
- "SpeechDonation ::totalSamplesSent =%!l(MISSING)ld ::newUtteranceBeginSampleNumber = %!l(MISSING)ld:: start = %!l(MISSING)ld :: end = %!l(MISSING)ld"
- "SpeechDonation: Adjusted Start Sample Number = %!l(MISSING)ld, total samples to be read = %!l(MISSING)ld"
- "SpeechDonation: Samples discarded = %!z(MISSING)u"
- "SpeechDonation: Start Sample Number = %!l(MISSING)ld, end Sample number = %!l(MISSING)ld"
- "VoiceControl::SpeechDonation"
- "didGetUtteranceBoundary:utteranceEndSampleNumber:"
- "v32@0:8q16q24"

```
