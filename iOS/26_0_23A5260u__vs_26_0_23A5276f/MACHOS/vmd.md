## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-897.0.0.0.0
-  __TEXT.__text: 0x92e14
-  __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_stubs: 0xb680
+898.0.0.0.0
+  __TEXT.__text: 0x94548
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_stubs: 0xb780
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x627c
-  __TEXT.__cstring: 0x42aa
-  __TEXT.__objc_classname: 0xc54
-  __TEXT.__objc_methname: 0xed49
-  __TEXT.__objc_methtype: 0x2f69
-  __TEXT.__const: 0x596
-  __TEXT.__gcc_except_tab: 0x96d0
-  __TEXT.__oslogstring: 0xf237
+  __TEXT.__objc_methlist: 0x632c
+  __TEXT.__cstring: 0x428a
+  __TEXT.__objc_classname: 0xc52
+  __TEXT.__objc_methname: 0xedac
+  __TEXT.__objc_methtype: 0x2f68
+  __TEXT.__const: 0x5a6
+  __TEXT.__gcc_except_tab: 0x9678
+  __TEXT.__oslogstring: 0xf377
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2ce0
+  __TEXT.__unwind_info: 0x2d78
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0x7b8
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x2890
+  __DATA_CONST.__const: 0x28a8
   __DATA_CONST.__cfstring: 0x4e40
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x58

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xe350
-  __DATA.__objc_selrefs: 0x3b00
+  __DATA.__objc_const: 0xe3b8
+  __DATA.__objc_selrefs: 0x3b38
   __DATA.__objc_ivar: 0x5e4
   __DATA.__objc_data: 0x1870
   __DATA.__data: 0x1040

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30E6D3F1-87BE-3B88-945C-B54E1A35B13C
-  Functions: 2689
-  Symbols:   708
-  CStrings:  5371
+  UUID: B8D5E2EA-9226-3148-AF91-B4A4DD906676
+  Functions: 2718
+  Symbols:   702
+  CStrings:  5374
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _pthread_mutex_destroy
- _pthread_mutex_init
CStrings:
+ "%@ %p client [%s:%d] (conn=%p) requested transcription progress"
+ "%@ add delegate %@"
+ "%@ is handling TranscriptionProgressFractionCompletedChanged with fractionCompleted %f"
+ "%@ is handling transcriptionProgressTotalUnitCountChanged with totalUnitCount %lld"
+ "%@ is handling transcriptionStatusChanged with transcribing %@"
+ "%@ remove delegate %@"
+ "*"
+ "<%@ %p> Creating with Speech Recognizer %@"
+ "<%@ %p> Deleting"
+ "<%@ %p> for client [%s:%d] (conn=%p) Created"
+ "<%@ %p> for client [%s:%d] (conn=%p) Deleted"
+ "<%@ %p> observeValueForKeyPath: oldOperationCount %ld, newOperationCount %ld"
+ "<%@ %p> observeValueForKeyPath: transcribing is %@"
+ "<%@ %p> observeValueForKeyPath: transcription operation %@"
+ "<%@ %p> updating client [%s:%d] (conn=%p) transcribing status changed to %@"
+ "Error sending progress fraction completed back to client with error: %@"
+ "Error sending progress total unit count back to client with error: %@"
+ "RB"
+ "T@\"NSMapTable\",R,N,V_delegates"
+ "VMTranscriptionService.m"
+ "VMVoicemailTranscriptionController.m"
+ "_delegates"
+ "addTranscriptionProgressDelegate:queue:"
+ "cache_setTranscribing:"
+ "fCacheIsTranscribing"
+ "getTranscriptionProgress"
+ "notifyTranscriptionProgressFractionCompletedChanged:"
+ "notifyTranscriptionProgressTotalUnitCountChanged:"
+ "notifyTranscriptionStatusChanged:"
+ "removeTranscriptionProgressDelegate:"
+ "setProgressFractionCompleted:"
+ "setProgressTotalUnitCount:"
+ "setTranscribing:fractionCompleted:totalUnitCount:"
+ "transcriptionController:transcriptionStatusChanged:"
+ "v24@0:8@\"<VMTranscriptionProgressDelegate>\"16"
+ "v24@0:8@?<v@?B@\"NSNumber\"@\"NSNumber\">16"
+ "v28@0:8@\"VMVoicemailTranscriptionController\"16B24"
+ "v32@0:8@\"<VMTranscriptionProgressDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "{TranscriptionProgress_t=dq}16@0:8"
- "%@ %p for client [%s:%d] (conn=%p) Created"
- "%@ %p for client [%s:%d] (conn=%p) Deleted"
- "%@ Creating with Speech Recognizer %@"
- "%@ Deleting"
- "@\"NSProgress\"24@0:8@?<v@?B>16"
- "@\"VMVoicemailTranscriptionController\"16@0:8"
- "@\"VMVoicemailTranscriptionTask\"16@0:8"
- "Client %@ requested %@ for transcriptionProgress %@"
- "Client %@ requested %@ for transcriptionProgress, but we are not transcribing"
- "Executing existing reply block for connection %@"
- "Executing reply block for connection %@"
- "Posting notification that transcribing status has changed: %d"
- "RD"
- "Saving reply block for connection %@"
- "T@\"NSProgress\",&,N,V_progress"
- "T@\"VMVoicemailTranscriptionController\",&,N"
- "T@\"VMVoicemailTranscriptionTask\",&,N"
- "T@?,C,N,V_reportTranscriptionProgressReplyBlock"
- "Updating client with connection: %@ about transcribing changed to: %d"
- "VVVoicemailTranscribingStatusChangedNotification"
- "_handleTranscribingStatusChanged:"
- "_progress"
- "_reportTranscriptionProgressReplyBlock"
- "fCache_IsTranscribing"
- "fCache_lock"
- "kVMVoicemailTranscriptionInProgress"
- "oldOperationCount %ld, newOperationCount: %ld"
- "reportTranscriptionProgressReplyBlock"
- "setProgress:"
- "setReportTranscriptionProgressReplyBlock:"
- "setTranscribing:"
- "v24@0:8@\"VMVoicemailTranscriptionController\"16"
- "v24@0:8@\"VMVoicemailTranscriptionTask\"16"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
- "\x91"
- "\xaa"

```
