## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2612.0.0.0.0
-  __TEXT.__text: 0x52cb28
+2613.2.0.0.0
+  __TEXT.__text: 0x52dbb8
   __TEXT.__auth_stubs: 0x2ee0
   __TEXT.__init_offsets: 0x15c
   __TEXT.__objc_methlist: 0x748
-  __TEXT.__const: 0x20afa
-  __TEXT.__cstring: 0x379a8
-  __TEXT.__gcc_except_tab: 0x4ec0c
-  __TEXT.__oslogstring: 0xf0f7
-  __TEXT.__unwind_info: 0x19230
+  __TEXT.__const: 0x20b4a
+  __TEXT.__cstring: 0x379e9
+  __TEXT.__gcc_except_tab: 0x4ecc8
+  __TEXT.__oslogstring: 0xf1e1
+  __TEXT.__unwind_info: 0x19278
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x1de8
   __TEXT.__objc_methtype: 0x1118

   __DATA_CONST.__objc_selrefs: 0x968
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1780
-  __AUTH_CONST.__const: 0x3c128
+  __AUTH_CONST.__const: 0x3c2c8
   __AUTH_CONST.__cfstring: 0x26e0
   __AUTH_CONST.__objc_const: 0xbf8
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 5308FBB5-5D35-3DB9-9CCF-FC5FF8FBE9FF
-  Functions: 17113
-  Symbols:   51420
-  CStrings:  9953
+  UUID: 521FA9AA-1BE4-347E-ACD2-41B9E3208A97
+  Functions: 17132
+  Symbols:   51468
+  CStrings:  9959
 
Symbols:
+ __ZN15SipCrlfResponseD0Ev
+ __ZN15SipCrlfResponseD1Ev
+ __ZN17SipTimerContainer10startTimerERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRS6_EEEjbd
+ __ZN21SipRegistrationPolicy22startingTransportRetryEv
+ __ZN33LazuliTransientRegistrationPolicy17retryRegistrationEv
+ __ZN33LazuliTransientRegistrationPolicy18onInterfaceChangedEv
+ __ZN33LazuliTransientRegistrationPolicy20startingRegistrationEv
+ __ZN33LazuliTransientRegistrationPolicy22startingTransportRetryEv
+ __ZN33LazuliTransientRegistrationPolicy26restorePrivateRelaySettingEv
+ __ZN33LazuliTransientRegistrationPolicy26setNextPrivateRelaySettingEb
+ __ZNK15SipCrlfResponse12longDebugStrEv
+ __ZNK15SipCrlfResponse13clone_virtualEv
+ __ZNK15SipCrlfResponse15encodeStartLineER12ImsOutStream
+ __ZNK15SipCrlfResponse7nextHopEv
+ __ZNK15SipCrlfResponse8debugStrEv
+ __ZNK15SipCrlfResponse9isRequestEv
+ __ZNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEED1Ev
+ __ZTI15SipCrlfResponse
+ __ZTINSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEEE
+ __ZTS15SipCrlfResponse
+ __ZTSNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEEE
+ __ZTV15SipCrlfResponse
+ __ZTVNSt3__120__shared_ptr_emplaceI15SipCrlfResponseNS_9allocatorIS1_EEEE
+ ____ZN12SipTimerInfo10initializeEP17SipTimerContainerbd_block_invoke
+ ___cxx_global_var_init.37
- __ZN17SipTimerContainer10startTimerERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRS6_EEEjb
- ____ZN12SipTimerInfo10initializeEP17SipTimerContainerb_block_invoke
- ___cxx_global_var_init.36
CStrings:
+ "#D %{private, mask.hash}sRegistration active using fallback setting PR=%{BOOL}d SD=%{BOOL}d"
+ "%{private, mask.hash}sFound CRLF pong among SIP messages"
+ "%{private, mask.hash}sims::RegistrationState=%s, clientState=%s SipRegistrationState=%s, regInterrupted=%s"
+ "%{private, mask.hash}snext retry usePrivateRelay=%{BOOL}d SD=%{BOOL}d"
+ "/AppleInternal/Library/BuildRoots/4~CGHougDSa5Sf3dZFfHbvss--iRJqqxvJl2ywTd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~CGHougDSa5Sf3dZFfHbvss--iRJqqxvJl2ywTd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "IsNSPDirect"
+ "found crlf response"
+ "pong interleaved in SIP messages"
- "%{private, mask.hash}sims::RegistrationState=%s, SipRegistrationState=%s, regInterrupted=%s"
- "/AppleInternal/Library/BuildRoots/4~CDy3ugCdzzRHV5TKEbYR18MdeVy-OzauHvdpCuw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CDy3ugCdzzRHV5TKEbYR18MdeVy-OzauHvdpCuw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"

```
