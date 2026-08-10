## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-625.1.24.10.1
-  __TEXT.__text: 0xaac6a4
+625.1.29.10.3
+  __TEXT.__text: 0xaaca98
   __TEXT.__objc_methlist: 0x14cc
   __TEXT.__const: 0x6fef8
-  __TEXT.__cstring: 0x55f47
-  __TEXT.__gcc_except_tab: 0x1880
-  __TEXT.__unwind_info: 0x10db0
+  __TEXT.__cstring: 0x55fae
+  __TEXT.__gcc_except_tab: 0x1888
+  __TEXT.__unwind_info: 0x10dc8
   __TEXT.__eh_frame: 0xc38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18368
-  Symbols:   23808
-  CStrings:  9078
+  Functions: 18374
+  Symbols:   23814
+  CStrings:  9080
 
Symbols:
+ _CFDictionaryGetValueIfPresent
+ __ZN4absl22internal_any_invocable12LocalInvokerILb0EbRZN6webrtc25WebRtcVideoReceiveChannel16OnPacketReceivedENS2_17RtpPacketReceivedEE3$_0JRKS4_EEET0_PNS0_15TypeErasedStateEDpNS0_18ForwardedParameterIT2_E4typeE
+ __ZN4absl22internal_any_invocable12LocalInvokerILb0EbRZN6webrtc25WebRtcVoiceReceiveChannel16OnPacketReceivedENS2_17RtpPacketReceivedEE3$_0JRKS4_EEET0_PNS0_15TypeErasedStateEDpNS0_18ForwardedParameterIT2_E4typeE
+ __ZN4absl22internal_any_invocable22LocalManagerNontrivialIZN6webrtc25WebRtcVideoReceiveChannel16OnPacketReceivedENS2_17RtpPacketReceivedEE3$_0EEvNS0_14FunctionToCallEPNS0_15TypeErasedStateES8_
+ __ZN4absl22internal_any_invocable22LocalManagerNontrivialIZN6webrtc25WebRtcVoiceReceiveChannel16OnPacketReceivedENS2_17RtpPacketReceivedEE3$_0EEvNS0_14FunctionToCallEPNS0_15TypeErasedStateES8_
+ __ZN6webrtc10I010Buffer12MutableDataUEv
+ __ZN6webrtc10I010Buffer12MutableDataVEv
+ __ZN6webrtc10I010Buffer12MutableDataYEv
+ __ZN6webrtc10I010Buffer6CreateEii
+ __ZN6webrtc10I420Buffer6CreateEii
+ __ZZN6webrtc5Event4WaitENS_9TimeDeltaES1_ENK3$_0clENSt3__18optionalI8timespecEE
- _CFDictionaryContainsKey
- __ZN4absl22internal_any_invocable13RemoteInvokerILb0EbRNSt3__114__bind_front_tIMN6webrtc25WebRtcVideoReceiveChannelEFbRKNS4_17RtpPacketReceivedEEJPS5_EEEJS8_EEET0_PNS0_15TypeErasedStateEDpNS0_18ForwardedParameterIT2_E4typeE
- __ZN4absl22internal_any_invocable13RemoteInvokerILb0EbRNSt3__114__bind_front_tIMN6webrtc25WebRtcVoiceReceiveChannelEFbRKNS4_17RtpPacketReceivedEEJPS5_EEEJS8_EEET0_PNS0_15TypeErasedStateEDpNS0_18ForwardedParameterIT2_E4typeE
- __ZN6webrtc25WebRtcVideoReceiveChannel31MaybeCreateDefaultReceiveStreamERKNS_17RtpPacketReceivedE
- __ZN6webrtc25WebRtcVoiceReceiveChannel31MaybeCreateDefaultReceiveStreamERKNS_17RtpPacketReceivedE
CStrings:
+ "Event::Wait pthread_cond_timedwait failed with error "
+ "Event::Wait pthread_cond_wait failed with error "
```
