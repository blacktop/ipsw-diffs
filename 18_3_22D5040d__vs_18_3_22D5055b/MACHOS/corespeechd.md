## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3403.7.2.0.0
-  __TEXT.__text: 0x17211c
+3403.7.3.0.0
+  __TEXT.__text: 0x174364
   __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_stubs: 0x1e9e0
-  __TEXT.__objc_methlist: 0x16ef8
+  __TEXT.__objc_stubs: 0x1eb40
+  __TEXT.__objc_methlist: 0x17100
   __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x3940
-  __TEXT.__cstring: 0x2a11f
-  __TEXT.__objc_methname: 0x3e913
-  __TEXT.__oslogstring: 0x21a6f
-  __TEXT.__objc_classname: 0x3541
+  __TEXT.__gcc_except_tab: 0x39e4
+  __TEXT.__cstring: 0x2a5ab
+  __TEXT.__objc_methname: 0x3ec43
+  __TEXT.__oslogstring: 0x21bbd
+  __TEXT.__objc_classname: 0x3566
   __TEXT.__objc_methtype: 0x8798
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x5620
+  __TEXT.__unwind_info: 0x56a0
   __DATA_CONST.__auth_got: 0xbc0
   __DATA_CONST.__got: 0x13e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5ca0
+  __DATA_CONST.__const: 0x5cc8
   __DATA_CONST.__cfstring: 0x83c0
-  __DATA_CONST.__objc_classlist: 0x980
+  __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x7c8
+  __DATA_CONST.__objc_superrefs: 0x7d0
   __DATA_CONST.__objc_intobj: 0xc90
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x270
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x2c3c8
-  __DATA.__objc_selrefs: 0xb7f0
-  __DATA.__objc_ivar: 0x1f1c
-  __DATA.__objc_data: 0x5f00
+  __DATA.__objc_const: 0x2c6d8
+  __DATA.__objc_selrefs: 0xb890
+  __DATA.__objc_ivar: 0x1f48
+  __DATA.__objc_data: 0x5f50
   __DATA.__data: 0x3ba0
   __DATA.__bss: 0x758
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9626
+  Functions: 9685
   Symbols:   1027
-  CStrings:  15745
+  CStrings:  15798
 
CStrings:
+ "%s Starting continuousFingerprintProvider"
+ "%s Stopping continuousFingerprintProvider"
+ "%s UUID was nil will not start fingerprint provider"
+ "%s UUID was nil will not stop fingerprint provider"
+ "%s Updated in use services for fingerprintProvider. %lu services in use"
+ "%s Updated in use services for fingerprintProvider. %lu services remaining"
+ "-[CSContinuousAudioFingerprintProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]"
+ "-[CSContinuousAudioFingerprintProvider _handleEnablePolicyEvent:]"
+ "-[CSContinuousAudioFingerprintProvider _startListenPollingWithInterval:completion:]"
+ "-[CSContinuousAudioFingerprintProvider _startListenPollingWithInterval:completion:]_block_invoke"
+ "-[CSContinuousAudioFingerprintProvider _startListenPolling]"
+ "-[CSContinuousAudioFingerprintProvider _startListenWithCompletion:]"
+ "-[CSContinuousAudioFingerprintProvider _startListenWithCompletion:]_block_invoke"
+ "-[CSContinuousAudioFingerprintProvider _startListenWithCompletion:]_block_invoke_3"
+ "-[CSContinuousAudioFingerprintProvider _stopListening]"
+ "-[CSContinuousAudioFingerprintProvider _stopListening]_block_invoke"
+ "-[CSContinuousAudioFingerprintProvider audioStreamProvider:didStopStreamUnexpectedly:]"
+ "-[CSContinuousAudioFingerprintProvider startWithUUID:withMaximumBufferSize:]"
+ "-[CSContinuousAudioFingerprintProvider startWithUUID:withMaximumBufferSize:]_block_invoke"
+ "-[CSContinuousAudioFingerprintProvider stopWithUUID:]"
+ "-[CSContinuousAudioFingerprintProvider stopWithUUID:]_block_invoke"
+ "CSContinuousAudioFingerprintProvider"
+ "T@\"CSAudioCircularBuffer\",&,N,V_audioLoggingBuffer"
+ "T@\"NSMutableDictionary\",&,N,V_inUseServices"
+ "TQ,N,V_frameSkipCounter"
+ "TQ,N,V_frameSkipRate"
+ "Tf,N,V_currentMaximumBufferSize"
+ "_audioLoggingBuffer"
+ "_currentMaximumBufferSize"
+ "_frameSkipCounter"
+ "_frameSkipRate"
+ "_handleEnablePolicyEvent:"
+ "_inUseServices"
+ "_setMaximumBufferSizeFromInUseServices"
+ "audioFingerprintProvider"
+ "audioLoggingBuffer"
+ "copyBufferWithNumSamplesCopiedIn:"
+ "createAudioFileWriterForAdBlockerWithInputFormat:outputFormat:withAccessoryID:"
+ "currentMaximumBufferSize"
+ "defaultContinuousFingerprintBufferDuration"
+ "frameSkipCounter"
+ "frameSkipRate"
+ "inUseServices"
+ "isAdBlockerAudioLoggingEnabled"
+ "overridingFrameSkipRate"
+ "setAudioLoggingBuffer:"
+ "setCurrentMaximumBufferSize:"
+ "setFrameSkipCounter:"
+ "setFrameSkipRate:"
+ "setInUseServices:"
+ "startWithUUID:withMaximumBufferSize:"
+ "stopWithUUID:"

```
