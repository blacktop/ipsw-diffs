## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-800.61.1.0.0
-  __TEXT.__text: 0x1657f0
-  __TEXT.__auth_stubs: 0x4550
+800.65.1.0.0
+  __TEXT.__text: 0x165fb8
+  __TEXT.__auth_stubs: 0x45a0
   __TEXT.__objc_methlist: 0x258
-  __TEXT.__cstring: 0x57510
+  __TEXT.__cstring: 0x577be
   __TEXT.__const: 0xcde0
   __TEXT.__gcc_except_tab: 0x228
   __TEXT.__oslogstring: 0x303

   __TEXT.__objc_methname: 0x1448
   __TEXT.__objc_methtype: 0x8f1
   __TEXT.__objc_stubs: 0x1220
-  __DATA_CONST.__got: 0x17d8
-  __DATA_CONST.__const: 0x3300
+  __DATA_CONST.__got: 0x17e0
+  __DATA_CONST.__const: 0x3310
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x22b8
+  __AUTH_CONST.__auth_got: 0x22e0
   __AUTH_CONST.__const: 0x7050
   __AUTH_CONST.__cfstring: 0xccc0
   __AUTH_CONST.__objc_const: 0xc38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2463
-  Symbols:   5989
-  CStrings:  7140
+  Symbols:   5996
+  CStrings:  7148
 
Symbols:
+ _FigHALAudioConduitDeviceHALStartIO
+ _FigHALAudioConduitDeviceHALStartStream
+ _FigHALAudioConduitDeviceHALStopIO
+ _FigHALAudioConduitDeviceHALStopStream
+ _FigSimpleMutexCheckIsLockedOnThisThread
+ __block_descriptor_tmp.237
+ __block_descriptor_tmp.343
+ __block_descriptor_tmp.354
+ __block_literal_global.345
+ __block_literal_global.356
+ _kAPSenderSessionStreamKey_PacketFormatAPAP
+ _kFigPWDKeyExchangeSenderProperty_Encryptor
- __block_descriptor_tmp.236
- __block_descriptor_tmp.353
- __block_literal_global.344
- __block_literal_global.355
CStrings:
+ "%!s(MISSING) propertyKey: '%!@(MISSING)'\n"
+ "800.65.1"
+ "<PWDKeyExchange> [%!{(MISSING)ptr}] Processing IncomingData%!?(MISSING){end}=%!@(MISSING)"
+ "<PWDKeyExchange> [%!{(MISSING)ptr}] Sending outgoingData%!?(MISSING){end}=%!@(MISSING)"
+ "OSStatus audioEngineAVC_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus audioEngineAVC_suspendInternal(FigEndpointStreamAudioEngineRef)"
+ "[%!{(MISSING)ptr}] Allocating input buffer. Requested bytes=%!u(MISSING)"
+ "[%!{(MISSING)ptr}] Display capabilities in GetInfo response: %!@(MISSING)\n"
+ "[%!{(MISSING)ptr}] Finalizing\n"
+ "[%!{(MISSING)ptr}] Flush\n"
+ "[%!{(MISSING)ptr}] PWDKeyExchangeSender SendMessageAsyncCallback called%!?(MISSING){end} with data %!@(MISSING)"
+ "[%!{(MISSING)ptr}] Resetting write handler in audio source [%!{(MISSING)ptr}] failed. err=%!m(MISSING)\n"
+ "[%!{(MISSING)ptr}] Resume completed (err=%!m(MISSING)) total=%!f(MISSING) ms (sourceResume=%!f(MISSING) conduitStartIO=%!f(MISSING) conduitStartStream=%!f(MISSING))\n"
+ "[%!{(MISSING)ptr}] Resuming\n"
+ "[%!{(MISSING)ptr}] Resuming audio engine failed. err=%!m(MISSING)\n"
+ "[%!{(MISSING)ptr}] Set endpoint stream [%!{(MISSING)ptr}]\n"
+ "[%!{(MISSING)ptr}] Setting audio source [%!{(MISSING)ptr}]. Old audio source [%!{(MISSING)ptr}]\n"
+ "[%!{(MISSING)ptr}] Suspend completed (err=%!m(MISSING)) total=%!f(MISSING) ms\n"
+ "[%!{(MISSING)ptr}] Suspend internal completed (err=%!m(MISSING)) total=%!f(MISSING) ms (conduitStopStream=%!f(MISSING) conduitStopIO=%!f(MISSING))\n"
+ "[%!{(MISSING)ptr}] Suspending\n"
+ "[%!{(MISSING)ptr}] Suspending audio source [%!{(MISSING)ptr}] failed. err=%!m(MISSING)\n"
+ "audioEngineAVC_CopyProperty"
+ "packetFormatAPAP"
+ "void audioEngineAVC_Finalize(CMBaseObjectRef)"
- "800.61.1"
- "<PWDKeyExchange> [%!{(MISSING)ptr}] Processing IncomingData=%!@(MISSING)"
- "<PWDKeyExchange> [%!{(MISSING)ptr}] Sending outgoingData=%!@(MISSING)"
- "Boolean audioEngineAVC_suspendInternal(FigEndpointStreamAudioEngineRef)"
- "Error Suspending audio source. err=%!m(MISSING)\n"
- "Flush. \n"
- "PWDEncryptor"
- "Resuming\n"
- "Resuming audio engine failed with %!d(MISSING) \n"
- "Set endpoint stream. \n"
- "Setting audio source: %!{(MISSING)ptr}\n"
- "Suspending\n"
- "Suspending audio engine failed with %!@(MISSING) \n"
- "[%!{(MISSING)ptr}] Allocating bytesRequested=%!u(MISSING)"
- "[%!{(MISSING)ptr}] Display capabilities: %!@(MISSING)\n"
- "[%!{(MISSING)ptr}] PWDKeyExchangeSender SendMessageAsyncCallback called%!{(MISSING)end} with data %!@(MISSING)"

```
