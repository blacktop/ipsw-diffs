## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2761.1.0.0.0
-  __TEXT.__text: 0x43945c
+2764.0.0.0.0
+  __TEXT.__text: 0x439738
   __TEXT.__init_offsets: 0x188
   __TEXT.__objc_methlist: 0xf9c
   __TEXT.__const: 0x1c070
-  __TEXT.__gcc_except_tab: 0x3b78c
-  __TEXT.__cstring: 0x129d9
-  __TEXT.__oslogstring: 0x454a8
-  __TEXT.__unwind_info: 0x15b50
+  __TEXT.__gcc_except_tab: 0x3b7b4
+  __TEXT.__cstring: 0x12969
+  __TEXT.__oslogstring: 0x455e3
+  __TEXT.__unwind_info: 0x15b58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2278
+  __DATA_CONST.__const: 0x2258
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0xa38
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__got: 0x370
-  __AUTH_CONST.__const: 0x2ff88
+  __AUTH_CONST.__const: 0x2ffb8
   __AUTH_CONST.__cfstring: 0x2d60
   __AUTH_CONST.__objc_const: 0x1e28
   __AUTH_CONST.__weak_auth_got: 0x28
Functions:
~ ___ZN9ImsSocket20attachDispatchSourceEN8dispatch5queueE_block_invoke.21 : 604 -> 552
~ __ZN10SipSession27handleInviteOrUpdateRequestENSt3__110shared_ptrIK10SipRequestEENS1_I20SipServerTransactionEE : 4944 -> 5000
~ __ZN10SipSession26parseBrandedCallingHeadersENSt3__110shared_ptrIK10SipRequestEE : 532 -> 708
~ __ZN7ImsCall23setTextMediaSessionModeEN3ims20TextMediaSessionModeE : 1892 -> 2224
~ __ZN12ImsTcpSocket16initializeSocketEiRKNSt3__110shared_ptrI9IpAddressEERKN8dispatch5queueERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEbN3ims14CFMutableArrayESH_i : 3368 -> 3424
~ ___ZN12ImsTcpSocket16initializeSocketEiRKNSt3__110shared_ptrI9IpAddressEERKN8dispatch5queueERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEbN3ims14CFMutableArrayESH_i_block_invoke.6 : 224 -> 288
~ __ZN14MessageSession10initializeENSt3__18weak_ptrI10SDPSessionEENS0_10shared_ptrI9SipDialogEEN3ims14CFMutableArrayERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 3448 -> 3440
~ ___51-[AVCRTTSessionDelegate textStream:didStart:error:]_block_invoke : 1056 -> 1060
~ __ZN10SDPSessionC2ENSt3__110shared_ptrI7ImsCallEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS1_I9IpAddressEEN3ims20TextMediaSessionModeENS1_I8SipStackEENS1_I10RTPManagerEE : 4132 -> 4196
~ __ZN10SDPSessionC2ENSt3__110shared_ptrI13LazuliSessionEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS1_I9IpAddressEEN3ims20TextMediaSessionModeENS1_I8SipStackEEb : 2804 -> 2828
~ __ZN13SDPTTYBuilder11adjustModelENSt3__110shared_ptrI8SDPModelEENS0_8optionalI21SDPMediaAudioSettingsEENS4_I19SDPMediaTTYSettingsEEb : 2432 -> 2448
CStrings:
+ "%{private, mask.hash}sImsSocket %p : invalidating socket fd=%d"
+ "%{private, mask.hash}sImsSocket: detached from read source. cancel handler is now Closing fd %d"
+ "%{private, mask.hash}ssetTextMediaSessionMode: declining pending RTT upgrade for call %{private, mask.hash}s"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jffAhC/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"
+ "[ERROR]  %{private, mask.hash}sBranded Calling header received : Invalid request"
- "%{private, mask.hash}s%s0x%lx%s%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nduWXU/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"
- ": invalidating socket fd="
- "ImsSocket "
- "ImsSocket: detached from read source. cancel handler is now Closing fd "
```
