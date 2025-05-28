## SensorKit

> `/System/Library/Frameworks/SensorKit.framework/SensorKit`

```diff

-707.0.38.0.0
-  __TEXT.__text: 0x2cae0
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x352c
+707.0.47.0.0
+  __TEXT.__text: 0x2d0b0
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x3544
   __TEXT.__const: 0x4c
   __TEXT.__constg_swiftt: 0x40
   __TEXT.__swift5_typeref: 0x5f
-  __TEXT.__gcc_except_tab: 0x72c
-  __TEXT.__cstring: 0x4297
-  __TEXT.__oslogstring: 0x3d9c
+  __TEXT.__gcc_except_tab: 0x770
+  __TEXT.__cstring: 0x42ea
+  __TEXT.__oslogstring: 0x3e74
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0xd44
+  __TEXT.__unwind_info: 0xd60
   __TEXT.__objc_classname: 0x82a
-  __TEXT.__objc_methname: 0x7b74
-  __TEXT.__objc_methtype: 0x1206
-  __TEXT.__objc_stubs: 0x4f20
+  __TEXT.__objc_methname: 0x7ca2
+  __TEXT.__objc_methtype: 0x1226
+  __TEXT.__objc_stubs: 0x5000
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x1088
+  __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x56f8
-  __DATA_CONST.__objc_selrefs: 0x1ad0
+  __DATA_CONST.__objc_const: 0x5728
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__const: 0x250
-  __AUTH_CONST.__cfstring: 0x4040
+  __AUTH_CONST.__const: 0x290
+  __AUTH_CONST.__cfstring: 0x4080
   __AUTH_CONST.__objc_const: 0x1e78
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_protorefs: 0x98
   __DATA.__objc_classrefs: 0x2f0
   __DATA.__objc_superrefs: 0x180
-  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_ivar: 0x444
   __DATA.__data: 0xd40
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x70
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/ARKit.framework/ARKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1282
-  Symbols:   4744
-  CStrings:  2421
+  Functions: 1286
+  Symbols:   4767
+  CStrings:  2437
 
Symbols:
+ -[SRSpeechMetrics initWithSessionIdentifier:sessionFlags:timestamp:timeSinceAudioStart:audioLevel:speechRecognition:soundClassification:speechExpression:]
+ -[SRSpeechMetrics timeSinceAudioStart]
+ _OBJC_IVAR_$_SRSpeechMetrics._timeSinceAudioStart
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
+ ___block_literal_global.250
+ ___cullOldSessions_block_invoke
+ ___sessionUUIDFromSessionIdentifier_block_invoke
+ _objc_msgSend$UUID
+ _objc_msgSend$initWithSessionIdentifier:sessionFlags:timestamp:timeSinceAudioStart:audioLevel:speechRecognition:soundClassification:speechExpression:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$speechRecognitionMetadata
+ _objc_msgSend$speechStartTimestamp
+ _objc_msgSend$timeSinceAudioStart
+ _os_unfair_lock_assert_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _SRLogSpeechMetrics
CStrings:
+ "%@ (%p): sessionIdentifier: %@, sessionFlags: %lu, timestamp: %@, timeSinceAudioStart: %f, audioLevel: %@, speechRecognition: %@, soundClassification: %@, speechExpression: %@"
+ "%@;%@"
+ "@80@0:8@16Q24d32d40@48@56@64@72"
+ "Detected a new audio session. Sessions in flight: %@, session times: %@"
+ "Removing session UUID %{public}@ from tracking"
+ "Td,R,N,V_timeSinceAudioStart"
+ "_timeSinceAudioStart"
+ "initWithSessionIdentifier:sessionFlags:timestamp:timeSinceAudioStart:audioLevel:speechRecognition:soundClassification:speechExpression:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "removeObjectsForKeys:"
+ "session UUID: %@, sessionStartTime: %.09f, timestamp: %.09f, speechstart: %.09f, computed; %.09f"
+ "sortUsingComparator:"
+ "speechRecognitionMetadata"
+ "speechStartTimestamp"
+ "timeSinceAudioStart"
- "%@ (%p): sessionIdentifier: %@, sessionFlags: %lu, timestamp: %@, audioLevel: %@, speechRecognition: %@, soundClassification: %@, speechExpression: %@"

```
