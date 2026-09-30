## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-920.8.2.0.0
-  __TEXT.__text: 0x21395c
+920.9.1.0.0
+  __TEXT.__text: 0x213470
   __TEXT.__auth_stubs: 0x5610
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x83219
+  __TEXT.__cstring: 0x833c7
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x5248
+  __TEXT.__unwind_info: 0x5230
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2116
   __TEXT.__objc_methtype: 0xd78
   __TEXT.__objc_stubs: 0x1da0
   __DATA_CONST.__got: 0x1f80
-  __DATA_CONST.__const: 0x6bc0
+  __DATA_CONST.__const: 0x6bc8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x2b18
   __AUTH_CONST.__const: 0x7f00
-  __AUTH_CONST.__cfstring: 0x129c0
+  __AUTH_CONST.__cfstring: 0x129e0
   __AUTH_CONST.__objc_const: 0xec0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84A67423-8E52-349F-B60A-85B6A2BAA1B8
-  Functions: 9804
-  Symbols:   24660
-  CStrings:  13522
+  UUID: F43179A4-B8DA-3315-94E6-E7E3024C061B
+  Functions: 9774
+  Symbols:   24605
+  CStrings:  13530
 
Symbols:
+ _APSenderSessionCreateTransportStreamWithID
+ ___block_descriptor_48_e8_32o_e38_i24?0^{__CFString=}8r^^{__CFString}16ls32l8
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.162
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.172
+ ___carEndpoint_copyStateProperty_block_invoke.cold.16
+ _epp_Dissociate.cold.1
+ _kAPEndpointProperty_CurrentCarPlayModesAndStates
- ___block_descriptor_48_e8_32o_e38_v24?0^{__CFString=}8r^^{__CFString}16ls32l8
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.185
- ___carAudioStream_resume_block_invoke_2.cold.1
- ___carAudioStream_resume_block_invoke_2.cold.10
- ___carAudioStream_resume_block_invoke_2.cold.11
- ___carAudioStream_resume_block_invoke_2.cold.12
- ___carAudioStream_resume_block_invoke_2.cold.13
- ___carAudioStream_resume_block_invoke_2.cold.14
- ___carAudioStream_resume_block_invoke_2.cold.15
- ___carAudioStream_resume_block_invoke_2.cold.16
- ___carAudioStream_resume_block_invoke_2.cold.17
- ___carAudioStream_resume_block_invoke_2.cold.18
- ___carAudioStream_resume_block_invoke_2.cold.19
- ___carAudioStream_resume_block_invoke_2.cold.2
- ___carAudioStream_resume_block_invoke_2.cold.20
- ___carAudioStream_resume_block_invoke_2.cold.21
- ___carAudioStream_resume_block_invoke_2.cold.22
- ___carAudioStream_resume_block_invoke_2.cold.23
- ___carAudioStream_resume_block_invoke_2.cold.24
- ___carAudioStream_resume_block_invoke_2.cold.25
- ___carAudioStream_resume_block_invoke_2.cold.26
- ___carAudioStream_resume_block_invoke_2.cold.27
- ___carAudioStream_resume_block_invoke_2.cold.28
- ___carAudioStream_resume_block_invoke_2.cold.29
- ___carAudioStream_resume_block_invoke_2.cold.3
- ___carAudioStream_resume_block_invoke_2.cold.30
- ___carAudioStream_resume_block_invoke_2.cold.31
- ___carAudioStream_resume_block_invoke_2.cold.32
- ___carAudioStream_resume_block_invoke_2.cold.33
- ___carAudioStream_resume_block_invoke_2.cold.34
- ___carAudioStream_resume_block_invoke_2.cold.35
- ___carAudioStream_resume_block_invoke_2.cold.36
- ___carAudioStream_resume_block_invoke_2.cold.37
- ___carAudioStream_resume_block_invoke_2.cold.38
- ___carAudioStream_resume_block_invoke_2.cold.39
- ___carAudioStream_resume_block_invoke_2.cold.4
- ___carAudioStream_resume_block_invoke_2.cold.40
- ___carAudioStream_resume_block_invoke_2.cold.41
- ___carAudioStream_resume_block_invoke_2.cold.42
- ___carAudioStream_resume_block_invoke_2.cold.5
- ___carAudioStream_resume_block_invoke_2.cold.6
- ___carAudioStream_resume_block_invoke_2.cold.7
- ___carAudioStream_resume_block_invoke_2.cold.8
- ___carAudioStream_resume_block_invoke_2.cold.9
CStrings:
+ "920.9.1"
+ "CurrentCarPlayModesAndStates"
+ "OSStatus carAudioStream_ensureEndpointStateAllowsForStreamResumption(FigEndpointStreamRef, APCarPlayAudioFormatInfoRef)"
+ "OSStatus epp_Dissociate(FigEndpointRef)"
+ "[%{ptr}] Dissociating"
+ "[%{ptr}] Error: Cannot setup a Speech stream while Telephony state is active\n"
+ "[%{ptr}] The comm channel can't be created because the endpoint is dissociated.\n"
+ "carAudioStream_ensureEndpointStateAllowsForStreamResumption"
+ "i24@?0^{__CFString=}8r^^{__CFString}16"
- "920.8.2"
- "v24@?0^{__CFString=}8r^^{__CFString}16"

```
