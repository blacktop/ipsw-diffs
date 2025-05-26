## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1431.600.72.2.2
-  __TEXT.__text: 0x11aa80
+1431.700.81.2.1
+  __TEXT.__text: 0x11adc4
   __TEXT.__auth_stubs: 0x17b0
-  __TEXT.__objc_methlist: 0x1240c
-  __TEXT.__cstring: 0x100cd
-  __TEXT.__oslogstring: 0xdc01
+  __TEXT.__objc_methlist: 0x12464
+  __TEXT.__cstring: 0x1010d
+  __TEXT.__oslogstring: 0xdc41
   __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x124c
+  __TEXT.__gcc_except_tab: 0x1260
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x788
   __TEXT.__swift5_typeref: 0x1ee

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x465c
+  __TEXT.__unwind_info: 0x4674
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x20d4
-  __TEXT.__objc_methname: 0x30c77
-  __TEXT.__objc_methtype: 0x6c88
-  __TEXT.__objc_stubs: 0x1bc00
+  __TEXT.__objc_methname: 0x30dc1
+  __TEXT.__objc_methtype: 0x6cbb
+  __TEXT.__objc_stubs: 0x1bc80
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x2ec8
+  __DATA_CONST.__const: 0x2f00
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fc30
-  __DATA_CONST.__objc_selrefs: 0x8f88
+  __DATA_CONST.__objc_const: 0x1fc80
+  __DATA_CONST.__objc_selrefs: 0x8fb8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_classrefs: 0x7f8
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__cfstring: 0xe320
+  __AUTH_CONST.__cfstring: 0xe3a0
   __AUTH_CONST.__objc_const: 0x5e70
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH_CONST.__auth_got: 0xbe8
   __AUTH.__objc_data: 0x1d10
   __AUTH.__data: 0x2c8
-  __DATA.__objc_ivar: 0x1344
+  __DATA.__objc_ivar: 0x1348
   __DATA.__data: 0x33a0
   __DATA.__bss: 0x4d0
   __DATA.__common: 0x1

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7791
-  Symbols:   24399
-  CStrings:  11525
+  Functions: 7798
+  Symbols:   24422
+  CStrings:  11541
 
Symbols:
+ +[TUCallCenter isSimultaneousVoiceAndDataSupportedForDialRequest:]
+ +[TUCaption averageConfidenceOverCaptions:]
+ -[TUCall liveVoicemailUnavailableReason]
+ -[TUCall setLiveVoicemailUnavailableReason:]
+ -[TUCallCenter setLiveVoicemailUnavailableReason:forCall:]
+ -[TUCallServicesInterface setLiveVoicemailUnavailableReason:forCallWithUniqueProxyIdentifier:]
+ GCC_except_table125
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table157
+ GCC_except_table196
+ GCC_except_table217
+ GCC_except_table222
+ _OBJC_IVAR_$_TUCall._liveVoicemailUnavailableReason
+ _TUAudioRouteBluetoothProductIdentifierB463
+ _TUAudioRouteBluetoothProductIdentifierB487
+ ___43+[TUCaption averageConfidenceOverCaptions:]_block_invoke
+ ___block_descriptor_40_e8_32r_e26_v32?0"TUCaption"8Q16^B24lr32l8
+ ___block_literal_global.1510
+ ___block_literal_global.1516
+ ___block_literal_global.190
+ _objc_msgSend$isSimultaneousVoiceAndDataSupportedForDialRequest:
+ _objc_msgSend$liveVoicemailUnavailableReason
+ _objc_msgSend$setLiveVoicemailUnavailableReason:
+ _objc_msgSend$setLiveVoicemailUnavailableReason:forCallWithUniqueProxyIdentifier:
- GCC_except_table124
- GCC_except_table130
- GCC_except_table133
- GCC_except_table136
- GCC_except_table139
- GCC_except_table142
- GCC_except_table145
- GCC_except_table156
- GCC_except_table194
- GCC_except_table215
- GCC_except_table220
- ___block_literal_global.1499
- ___block_literal_global.1505
- ___block_literal_global.187
CStrings:
+ " lvmR=%ld"
+ "76,8218"
+ "76,8230"
+ "Proxying setLiveVoicemailUnavailableReason:forCall: through CSD"
+ "Tq,N,V_liveVoicemailUnavailableReason"
+ "Vv32@0:8q16@\"NSString\"24"
+ "Vv32@0:8q16@24"
+ "_liveVoicemailUnavailableReason"
+ "averageConfidenceOverCaptions:"
+ "d24@0:8@16"
+ "isSimultaneousVoiceAndDataSupportedForDialRequest:"
+ "liveVoicemailUnavailableReason"
+ "setLiveVoicemailUnavailableReason:"
+ "setLiveVoicemailUnavailableReason:forCall:"
+ "setLiveVoicemailUnavailableReason:forCallWithUniqueProxyIdentifier:"
+ "\x8e\x12&ABA"
- "\x8e\x12&AB1"

```
