## libwebrtc.dylib

> `/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libwebrtc.dylib`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0xae1904
+625.1.29.11.25
+  __TEXT.__text: 0xae1cc0
   __TEXT.__objc_methlist: 0x14cc
   __TEXT.__const: 0x700f8
-  __TEXT.__cstring: 0x5ad8a
-  __TEXT.__gcc_except_tab: 0x1830
-  __TEXT.__unwind_info: 0x10dd0
+  __TEXT.__cstring: 0x5adf1
+  __TEXT.__gcc_except_tab: 0x1838
+  __TEXT.__unwind_info: 0x10de8
   __TEXT.__eh_frame: 0xc48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18531
-  Symbols:   23977
-  CStrings:  9068
+  Functions: 18537
+  Symbols:   23983
+  CStrings:  9070
 
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
