## VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

-1247.0.0.0.0
-  __TEXT.__text: 0x168f44
+1247.3.0.0.0
+  __TEXT.__text: 0x169a9c
   __TEXT.__auth_stubs: 0x4620
-  __TEXT.__objc_stubs: 0x23960
+  __TEXT.__objc_stubs: 0x239e0
   __TEXT.__objc_methlist: 0x10d64
-  __TEXT.__objc_classname: 0x1cf5
-  __TEXT.__objc_methname: 0x335c9
-  __TEXT.__objc_methtype: 0x75bb
-  __TEXT.__cstring: 0xb3da
+  __TEXT.__objc_classname: 0x1cf4
+  __TEXT.__objc_methname: 0x335d5
+  __TEXT.__objc_methtype: 0x7582
+  __TEXT.__cstring: 0xb47a
   __TEXT.__const: 0x87c4
-  __TEXT.__oslogstring: 0x2a1d
-  __TEXT.__gcc_except_tab: 0x1c24
+  __TEXT.__oslogstring: 0x2bbd
+  __TEXT.__gcc_except_tab: 0x1bdc
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x7654
   __TEXT.__swift5_fieldmd: 0x26b0

   __TEXT.__swift5_types: 0x354
   __TEXT.__swift5_protos: 0xa0
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x6c48
+  __TEXT.__unwind_info: 0x6c78
   __TEXT.__eh_frame: 0x5c10
   __DATA_CONST.__auth_got: 0x2328
   __DATA_CONST.__got: 0x1668
-  __DATA_CONST.__auth_ptr: 0x1808
-  __DATA_CONST.__const: 0x7908
+  __DATA_CONST.__auth_ptr: 0x1830
+  __DATA_CONST.__const: 0x79e8
   __DATA_CONST.__cfstring: 0x39e0
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0x98

   __DATA_CONST.__objc_protolist: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x3d0
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0xb0
-  __DATA.__objc_const: 0x201d0
-  __DATA.__objc_selrefs: 0xadb0
+  __DATA.__objc_const: 0x201b0
+  __DATA.__objc_selrefs: 0xadc8
   __DATA.__objc_ivar: 0x120c
   __DATA.__objc_data: 0x6248
   __DATA.__data: 0x82f8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9834
+  Functions: 9849
   Symbols:   2408
-  CStrings:  10427
+  CStrings:  10441
 
CStrings:
+ "%s -- First overdub buffer received"
+ "%s -- Player started outside the range of a recorded buffer."
+ "%s -- could not allocate trimmed buffer"
+ "%s -- durationToSkip = %f, framesToSkip = %u"
+ "%s -- inputSampleRate = %g Hz"
+ "%s -- outputSampleRate = %g Hz"
+ "%s -- playerBegin = %f, bufferRange = [%f - %f]"
+ "%s -- session.inputLatency = %f seconds"
+ "%s -- session.outputLatency = %f seconds"
+ "%s -- voiceIsolationLatency = %f seconds"
+ "-[VMRecordingEngine _recordTrimmedAudioBuffer:time:]"
+ "-[VMRecordingEngine _startPlayback:time:]"
+ "@\"AVAudioUnitEffect\""
+ "B36@0:8@16@24B32"
+ "B36@0:8@16@24i32"
+ "_canSelectNewestRecording"
+ "_playerBuffers"
+ "_recordingBlock"
+ "_startRecording"
+ "_voiceIsolationNode"
+ "bufferWithAudioBuffer:audioTime:"
+ "initWithAudioBuffer:audioTime:"
+ "lastRenderTime"
+ "latency"
+ "mostRecentRecordingIsSelectable"
+ "prepareWithFrameCount:"
+ "rc_copyFromTimeStamp"
+ "v32@?0@\"VMRecordingEngine\"8@\"AVAudioPCMBuffer\"16@\"AVAudioTime\"24"
+ "y\x13A\x12"
+ "\xf0\x81"
- "@\"NSString\"20@0:8B16"
- "@36@0:8@16@24i32"
- "T@\"AVAudioPlayerNode\",&,N,V_playerNode"
- "T@\"NSEnumerator\",&,N,V_overdubBuffers"
- "_firstOverdubBuffer"
- "_inputLatencySamples"
- "_overdubState"
- "_playerStarted"
- "finishedEditingWithNewRecordingUUID:"
- "overdubBuffers"
- "playerNode"
- "setOverdubBuffers:"
- "setPlayerNode:"
- "t\x12\x13A\x14"
- "{VMAudioBuffer=\"audioTime\"@\"AVAudioTime\"\"audioBuffer\"@\"AVAudioPCMBuffer\"}"
- "\xf0a"

```
