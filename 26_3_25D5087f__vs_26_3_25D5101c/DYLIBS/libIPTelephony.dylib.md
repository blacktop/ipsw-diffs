## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2612.0.0.0.0
-  __TEXT.__text: 0x4a31cc
+2613.2.0.0.0
+  __TEXT.__text: 0x4a4270
   __TEXT.__auth_stubs: 0x2180
   __TEXT.__init_offsets: 0x144
   __TEXT.__objc_methlist: 0x6b8
-  __TEXT.__const: 0x1d242
-  __TEXT.__cstring: 0x30358
-  __TEXT.__gcc_except_tab: 0x46504
-  __TEXT.__oslogstring: 0xec57
-  __TEXT.__unwind_info: 0x16ad8
+  __TEXT.__const: 0x1d292
+  __TEXT.__cstring: 0x30399
+  __TEXT.__gcc_except_tab: 0x465bc
+  __TEXT.__oslogstring: 0xed47
+  __TEXT.__unwind_info: 0x16b20
   __TEXT.__objc_classname: 0x114
   __TEXT.__objc_methname: 0x1908
   __TEXT.__objc_methtype: 0x10bd

   __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x10d0
-  __AUTH_CONST.__const: 0x35b60
+  __AUTH_CONST.__const: 0x35d00
   __AUTH_CONST.__cfstring: 0x23a0
   __AUTH_CONST.__objc_const: 0xb08
   __AUTH.__objc_data: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 2A91D3CB-F566-32C8-9894-DEF2540ABBFB
-  Functions: 15195
-  Symbols:   29986
-  CStrings:  8799
+  UUID: 2BDECD2D-2BC0-3E3D-B69C-AF693F21590F
+  Functions: 15214
+  Symbols:   30015
+  CStrings:  8805
 
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
+ __cxx_global_var_init.37
- __ZN17SipTimerContainer10startTimerERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFvRS6_EEEjb
- ____ZN12SipTimerInfo10initializeEP17SipTimerContainerb_block_invoke
- __cxx_global_var_init.36
CStrings:
+ "%{private, mask.hash}sFound CRLF pong among SIP messages"
+ "%{private, mask.hash}sims::RegistrationState=%s, clientState=%s SipRegistrationState=%s, regInterrupted=%s"
+ "%{private, mask.hash}snext retry usePrivateRelay=%{BOOL}d SD=%{BOOL}d"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugC-dD3t4cfDSIu6Ashau-keTLoSNObt6ME/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugC-dD3t4cfDSIu6Ashau-keTLoSNObt6ME/Library/Caches/com.apple.xbs/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"
+ "IsNSPDirect"
+ "[DEBUG]  %{private, mask.hash}sRegistration active using fallback setting PR=%{BOOL}d SD=%{BOOL}d"
+ "found crlf response"
+ "pong interleaved in SIP messages"
- "%{private, mask.hash}sims::RegistrationState=%s, SipRegistrationState=%s, regInterrupted=%s"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugAhStwWZpOG5OWXpiROIfbB3JHdADZQEwI/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugAhStwWZpOG5OWXpiROIfbB3JHdADZQEwI/Library/Caches/com.apple.xbs/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"

```
