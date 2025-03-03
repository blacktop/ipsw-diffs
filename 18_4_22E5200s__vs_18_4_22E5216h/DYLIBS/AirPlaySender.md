## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-850.14.1.0.0
-  __TEXT.__text: 0x1e11e0
+850.17.1.0.0
+  __TEXT.__text: 0x1e0424
   __TEXT.__auth_stubs: 0x50e0
   __TEXT.__objc_methlist: 0x67c
-  __TEXT.__cstring: 0x74537
+  __TEXT.__cstring: 0x74136
   __TEXT.__const: 0xfd80
-  __TEXT.__gcc_except_tab: 0x970
+  __TEXT.__gcc_except_tab: 0x940
   __TEXT.__dlopen_cstrs: 0x61d
   __TEXT.__oslogstring: 0x6da
-  __TEXT.__unwind_info: 0x4a10
+  __TEXT.__unwind_info: 0x49e0
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
-  __TEXT.__objc_methname: 0x19ff
+  __TEXT.__objc_methname: 0x1a01
   __TEXT.__objc_methtype: 0xa56
   __TEXT.__objc_stubs: 0x17c0
-  __DATA_CONST.__got: 0x1d70
+  __DATA_CONST.__got: 0x1d68
   __DATA_CONST.__const: 0x6390
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x2880
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x7820
-  __AUTH_CONST.__cfstring: 0x10ec0
+  __AUTH_CONST.__const: 0x77e0
+  __AUTH_CONST.__cfstring: 0x10e20
   __AUTH_CONST.__objc_const: 0xb88
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x183c8
-  __DATA.__bss: 0x9f0
+  __DATA.__bss: 0x9c8
   __DATA.__common: 0xa08
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xc50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8777
-  Symbols:   12079
-  CStrings:  9925
+  Functions: 8759
+  Symbols:   12058
+  CStrings:  9901
 
Symbols:
+ _CFPropertyListAppendFormatted
- _kFigEndpointStreamAudioEngineNotification_FlushWithinSampleRangeFailed
- _objc_release_x24
CStrings:
+ "%kO=%i"
+ "850.17.1"
+ "BAE [%{ptr}] %s[0x%04X] Discarding sbuf with opts %1.3f for current flush time range: start = %1.3f, end = %1.3f \n"
+ "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, APPairingClientRef *)"
+ "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c%c.\n"
+ "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() failed: %m (encryptionContext = %@, remoteDataPort = %d)"
+ "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() with RemotePort = %d, LocalSendsWithReadKey = %d"
+ "[%{ptr}] Deactivation skipped - error %#m\n"
+ "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d, previousActivationSeed: %d\n"
+ "dictionaryWithDictionary:"
+ "{%kO=%O%kO=%D%kO=%D%kO=%s%kO=%.6a%kO=%.6a%kO=%i%kO=%O%kO=%.6a%kO=%i%kO=%O%kO=%O%kO=%O}"
- " with new value"
- "850.14.1"
- "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Failed. Time out. Posting FlushWithinTimeRageFailed.\n"
- "BAE [%{ptr}] %sflushWithinRangeLimitTime set to %1.1f seconds\n"
- "Boolean coreUtilsPairing_IsPeerKnown(APPairingClientRef)"
- "NSString *getkAVCMediaStreamOptionCallID(void)"
- "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, CFStringRef, APPairingClientRef *)"
- "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)"
- "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)_block_invoke_2"
- "Peer Cache"
- "PeerIdentifier"
- "PeerPublicKey"
- "Stored new"
- "Updated"
- "[%{ptr}] %s item in %s%s:\n\"%@\" :\n%@"
- "[%{ptr}] %s[%u]:\n%@ :\n%@"
- "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c%c%c.\n"
- "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() failed: %m (encryptionContext = %@, localPort = %d, remoteDataPort = %d)"
- "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() with localPort = %d, RemotePort = %d, LocalSendsWithReadKey = %d"
- "[%{ptr}] All items in %s:"
- "[%{ptr}] Forcing coreUtilsPairing_IsPeerKnown to return false\n"
- "[%{ptr}] Forcing coreUtilsPairing_IsPeerKnown to return true\n"
- "[%{ptr}] Is peer known: %d, peerIdentifier: %s (processing time: %llu ms, err: %d)\n"
- "[%{ptr}] Number of items in %s: %d"
- "[%{ptr}] PairingSessionCopyPeerIdentifier returned %s (err: %d) \n"
- "[%{ptr}] Removing random item from %s:\n\"%@\" :\n%@"
- "[%{ptr}] Using %s with size: %d\n"
- "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d \n"
- "bufferedAudio_flushForwardLimitSecs"
- "coreUtilsPairingPeerCache_SavePeer"
- "forcePeerKnown"
- "forcePeerUnknown"
- "initWithObjectsAndKeys:"
- "kAVCMediaStreamOptionCallID"
- "{%kO=%O%kO=%D%kO=%D%kO=%s%kO=%.6a%kO=%.6a%kO=%i%kO=%i%kO=%O%kO=%.6a%kO=%i%kO=%O%kO=%O%kO=%O}"

```
