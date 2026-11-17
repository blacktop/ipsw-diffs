## TextToSpeech

> `/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech`

```diff

-727.3.12.0.0
-  __TEXT.__text: 0x32cbb4
-  __TEXT.__objc_methlist: 0x3ca8
-  __TEXT.__const: 0x3fca9
+727.3.22.0.0
+  __TEXT.__text: 0x343f44
+  __TEXT.__objc_methlist: 0x3d10
+  __TEXT.__const: 0x402e9
   __TEXT.__dlopen_cstrs: 0x150
-  __TEXT.__constg_swiftt: 0x86f8
-  __TEXT.__swift5_typeref: 0x7970
-  __TEXT.__swift5_fieldmd: 0x645c
-  __TEXT.__cstring: 0x854d
-  __TEXT.__swift5_types: 0x7bc
-  __TEXT.__swift5_capture: 0x3334
-  __TEXT.__swift5_reflstr: 0x5100
-  __TEXT.__swift5_assocty: 0x1690
-  __TEXT.__swift5_proto: 0x1354
-  __TEXT.__swift_as_entry: 0xca4
-  __TEXT.__swift_as_ret: 0xdd4
-  __TEXT.__swift_as_cont: 0x126c
-  __TEXT.__swift5_builtin: 0x4b0
-  __TEXT.__oslogstring: 0x30f4
+  __TEXT.__constg_swiftt: 0x8a40
+  __TEXT.__swift5_typeref: 0x7b5c
+  __TEXT.__swift5_fieldmd: 0x66c4
+  __TEXT.__cstring: 0x8731
+  __TEXT.__swift5_types: 0x7e4
+  __TEXT.__swift5_capture: 0x33f8
+  __TEXT.__swift5_reflstr: 0x5470
+  __TEXT.__swift5_assocty: 0x1750
+  __TEXT.__swift5_proto: 0x1380
+  __TEXT.__swift_as_entry: 0xcbc
+  __TEXT.__swift_as_ret: 0xdec
+  __TEXT.__swift_as_cont: 0x12a4
+  __TEXT.__swift5_builtin: 0x4c4
+  __TEXT.__oslogstring: 0x34b4
   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x144
   __TEXT.__gcc_except_tab: 0x1e24
   __TEXT.__ustring: 0x2c6
-  __TEXT.__unwind_info: 0xf178
-  __TEXT.__eh_frame: 0x17628
+  __TEXT.__unwind_info: 0xf4d8
+  __TEXT.__eh_frame: 0x17d10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19b0
+  __DATA_CONST.__const: 0x19d0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2978
+  __DATA_CONST.__objc_selrefs: 0x29c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x12d0
-  __DATA_CONST.__got: 0xda0
-  __AUTH_CONST.__const: 0x17ba8
-  __AUTH_CONST.__cfstring: 0x5f00
-  __AUTH_CONST.__objc_const: 0xacd8
+  __DATA_CONST.__got: 0xe68
+  __AUTH_CONST.__const: 0x18438
+  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__objc_const: 0xafb0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xed0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2b18
-  __AUTH.__objc_data: 0x3360
-  __AUTH.__data: 0x4198
+  __AUTH_CONST.__auth_got: 0x2c48
+  __AUTH.__objc_data: 0x3618
+  __AUTH.__data: 0x41a8
   __DATA.__objc_ivar: 0x32c
-  __DATA.__data: 0x3d80
-  __DATA.__common: 0x528
+  __DATA.__data: 0x3e48
+  __DATA.__common: 0x580
   __DATA_DIRTY.__objc_data: 0x520
   __DATA_DIRTY.__data: 0x12d0
   __DATA_DIRTY.__bss: 0xbc0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16149
-  Symbols:   1373
-  CStrings:  1663
+  Functions: 16387
+  Symbols:   1377
+  CStrings:  1686
 
Symbols:
+ _AVAudioSessionSilenceSecondaryAudioHintNotification
+ _AVAudioSessionSilenceSecondaryAudioHintTypeKey
+ _AudioQueueEnqueueBufferWithParameters
+ _dladdr
+ _swift_release_x11
- _AudioQueueEnqueueBuffer
CStrings:
+ "(?<![\\p{L}\\p{N}])\\((US\\$|CA\\$|A\\$|HK\\$|NZ\\$|S\\$|NT\\$|R\\$|Mex\\$|JP¥|[$€£¥₹₩₽₺₪₫฿₦₨₴₡₱])\\s?((?:\\d{1,3}(?:[,. \u202f ]\\d{3})+|\\d+)(?:[.,]\\d+)?|\\.\\d+)\\)(?![\\p{L}\\p{N}])"
+ "-[TTSSpeechManager handleAudioInterruptionBegan:]"
+ "Audio unit did not report end of request %{public}s within %{public}s; trailing markers may be dropped"
+ "AudioQueue %{public}s again within %.*fs of the last recycle (late by %.*fms); not recycling"
+ "AudioQueue diag [%ld refills, %.*fHz]: dispatchLatency avg=%.*fms max=%.*fms, maxWork=%.*fms, minInFlight=%ld, underflows=%ld, deadlineMisses=%ld, genSkips=%ld, lateEnqueues=%ld maxLate=%.*fms staleRecycles=%ld hintRecycles=%ld, poolReuse=%ld alloc=%ld sizeMiss=%ld freeDepth=%ld, ioCycle=%.*fms bufDur=%.*fms buffersPerIOCycle=%.*f"
+ "AudioQueue dispose: %.*fms"
+ "AudioQueue recycling (%{public}s): late by %.*fms, state=%{public}s, keeping %ld record(s) (%.*fms), cachedIOCycle=%.*fms"
+ "AudioQueue start: prime=%.*fms status=%d frames=%u/%u, start=%.*fms status=%d, ioBufferDuration=%.*fms, cancelled=%{bool}d"
+ "AudioQueue stop (%{public}s): %.*fms status=%d, ioBufferDuration=%.*fms"
+ "AudioQueue: another app began primary audio (secondary audio hint)"
+ "AudioQueueStop failed: %d; invalidating"
+ "Could not deactivate audio session after auto timeout: %{public}s"
+ "Detected audio session deactivation (state=%{public}s)."
+ "Failed to %{public}s audio queue (prime=%d, start=%d); invalidating"
+ "Ignoring non-interruption audio session deactivation, source: %ld"
+ "Instantiated audio unit for %{public}s, inProcess: %{bool}d"
+ "Not starting cancelled utterance with id %s"
+ "Stopping audio queue (%{public}s)"
+ "US\\$|CA\\$|A\\$|HK\\$|NZ\\$|S\\$|NT\\$|R\\$|Mex\\$|JP¥|[$€£¥₹₩₽₺₪₫฿₦₨₴₡₱]"
+ "UnspeakableCharacters"
+ "Using auxiliary audio session for WebKit speech"
+ "Will deactivate audio session after auto timeout. options=%lu"
+ "XCTestConfigurationFilePath"
+ "com.apple.Accessibility.TextToSpeech.AudioQueueControl"
+ "com.apple.TextToSpeech.diagnostics"
+ "com.apple.TextToSpeech.endOfRequest"
+ "loadedFromSharedCache"
+ "secondary audio hint"
+ "session deactivated"
+ "stale timeline"
+ "stop timeout"
+ "textToSpeechPath"
- "(?<![\\p{L}\\p{N}])\\((US\\$|CA\\$|A\\$|HK\\$|NZ\\$|S\\$|NT\\$|R\\$|Mex\\$|[$€£¥₹₩₽₺₪₫฿₦₨₴₡₱])\\s?((?:\\d{1,3}(?:[,. \u202f ]\\d{3})+|\\d+)(?:[.,]\\d+)?|\\.\\d+)\\)(?![\\p{L}\\p{N}])"
- "AudioQueue diag [%ld refills, %.*fHz]: dispatchLatency avg=%.*fms max=%.*fms, maxWork=%.*fms, minInFlight=%ld, underflows=%ld, deadlineMisses=%ld, genSkips=%ld, poolReuse=%ld alloc=%ld sizeMiss=%ld freeDepth=%ld, ioCycle=%.*fms bufDur=%.*fms buffersPerIOCycle=%.*f"
- "Could not deactivate audio session after auto timeout"
- "Detected audio session deactivation."
- "Failed to prime audio queue: %d"
- "Failed to start audio queue: %d"
- "Stop timeout reached, stopping queue"
- "US\\$|CA\\$|A\\$|HK\\$|NZ\\$|S\\$|NT\\$|R\\$|Mex\\$|[$€£¥₹₩₽₺₪₫฿₦₨₴₡₱]"
- "Will deactivate audio session after auto timeout"
```
