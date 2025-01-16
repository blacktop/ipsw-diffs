## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3403.7.2.0.0
-  __TEXT.__text: 0x156e70
-  __TEXT.__auth_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0x13140
+3403.7.3.0.0
+  __TEXT.__text: 0x1590b8
+  __TEXT.__auth_stubs: 0x1c10
+  __TEXT.__objc_methlist: 0x13348
   __TEXT.__const: 0x5c0
-  __TEXT.__gcc_except_tab: 0x37a4
-  __TEXT.__cstring: 0x26ef6
-  __TEXT.__oslogstring: 0x1f86f
+  __TEXT.__gcc_except_tab: 0x3848
+  __TEXT.__cstring: 0x27382
+  __TEXT.__oslogstring: 0x1f9da
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__unwind_info: 0x4ec8
-  __TEXT.__objc_classname: 0x2ebd
-  __TEXT.__objc_methname: 0x38217
+  __TEXT.__unwind_info: 0x4f40
+  __TEXT.__objc_classname: 0x2ee4
+  __TEXT.__objc_methname: 0x38547
   __TEXT.__objc_methtype: 0x7cca
-  __TEXT.__objc_stubs: 0x1c300
-  __DATA_CONST.__got: 0x1ab8
-  __DATA_CONST.__const: 0x4130
-  __DATA_CONST.__objc_classlist: 0x858
+  __TEXT.__objc_stubs: 0x1c460
+  __DATA_CONST.__got: 0x1ac0
+  __DATA_CONST.__const: 0x4158
+  __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x498
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7c0
+  __DATA_CONST.__objc_selrefs: 0xa860
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xe18
+  __AUTH_CONST.__auth_got: 0xe20
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e40
   __AUTH_CONST.__cfstring: 0x8f80
-  __AUTH_CONST.__objc_const: 0x25648
+  __AUTH_CONST.__objc_const: 0x25958
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1a6c
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x1a98
   __DATA.__data: 0x36b0
   __DATA.__bss: 0x660
   __DATA.__common: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8258
-  Symbols:   10050
-  CStrings:  14537
+  Functions: 8317
+  Symbols:   10112
+  CStrings:  14592
 
Symbols:
+ _OBJC_CLASS_$_CSContinuousAudioFingerprintProvider
+ _OBJC_METACLASS_$_CSContinuousAudioFingerprintProvider
+ _dispatch_queue_attr_make_with_autorelease_frequency
CStrings:
+ "\x17"
+ "%s Siri enabled : %{public}d"
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
