## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x1b0f0
+1371.0.1.0.0
+  __TEXT.__text: 0x1de68
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb8
-  __TEXT.__cstring: 0x1181
+  __TEXT.__cstring: 0x138c
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x310
-  __DATA_CONST.__got: 0x48
+  __TEXT.__unwind_info: 0x338
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xd0
   __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x80
-  __DATA.__data: 0x120
+  __DATA.__data: 0x130
   __DATA.__bss: 0x67
   __DATA.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 4C98C47A-A101-32DC-B6FC-EFB8A137D8D4
+  UUID: F7E7F6E6-4E87-3D97-970C-4267B5DE89C6
   Functions: 254
-  Symbols:   411
-  CStrings:  185
+  Symbols:   412
+  CStrings:  200
 
Symbols:
+ GCC_except_table13
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- GCC_except_table12
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
Functions:
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
~ _APPLIB_DIAG_AUDIO_PCM_14Bit_Start_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_PCM_14Bit_Stop_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_PCM_16Bit_Start_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_PCM_16Bit_Stop_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_I2S_Start_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_I2S_Stop_Loopback : 60 -> 708
~ _APPLIB_DIAG_AUDIO_PCM_I2S_PASSTHROUGH_Start : 60 -> 708
~ _APPLIB_DIAG_AUDIO_PCM_I2S_PASSTHROUGH_Stop : 60 -> 708
~ _APPLIB_DIAG_AUDIO_I2S_PCM_PASSTHROUGH_Start : 60 -> 708
~ _APPLIB_DIAG_AUDIO_I2S_PCM_PASSTHROUGH_Stop : 60 -> 708
~ __ETLDMCCreateFromFile : 1960 -> 1888
~ __ETLDMCParseLogCodesInternal : 1324 -> 1320
~ _APPLIB_DIAG_CreateICCID_EFS_File : 180 -> 1272
~ _APPLIB_DIAG_GetICCID : 184 -> 568
~ _APPLIB_DIAG_Read_Meid : 8 -> 372
~ _APPLIB_DIAG_Read_Msl : 8 -> 368
~ _APPLIB_DIAG_Read_Otksl : 8 -> 368
~ _APPLIB_DIAG_Read_BlueToothAddr : 8 -> 372
~ _APPLIB_DIAG_Read_WiFi_MAC_Addr : 8 -> 372
~ _APPLIB_DIAG_Read_WiFi_Cal_Data : 8 -> 372
~ _APPLIB_DIAG_Read_USB2ETHERNET_MAC_Addr : 8 -> 372
~ _ETLEVENTProcessEvent : 696 -> 468
~ _ETLEVENTProcessEventItemTSLength : 304 -> 500
~ _ETLEVENTProcessHeader : 60 -> 152
~ _ETLEVENTParseReport : 216 -> 336
~ _ETLEVENTParseEventReport : 468 -> 384
~ _ETLEVENTReportFree : 132 -> 164
~ _ETLDMCGetMatchingFileNameAndType : 836 -> 872
~ __Z26ETLDMCDebugGetMessageRangePK26ETLMESSAGESubsystemIDRange : 1040 -> 1060
~ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev -> __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev : 424 -> 540
~ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev : 260 -> 288
~ __Z24ETLDMCDebugGetEventRangePK13ETLEVENTRange : 1040 -> 1060
~ __Z26ETLDMCDebugGetMessageMasksP17__ETLDMCHandleTag10ETLDMCView : 1016 -> 1048
~ __Z22ETLDMCDebugGetLogCodesP17__ETLDMCHandleTag10ETLDMCViewb : 1512 -> 1532
~ __Z20ETLDMCDebugGetEventsP17__ETLDMCHandleTag10ETLDMCView : 856 -> 884
~ __Z21ETLDMCDebugGetQtracesP17__ETLDMCHandleTag10ETLDMCView : 1016 -> 1036
~ ___clang_call_terminate -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev : 20 -> 16
~ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m -> __ZNSt3__120__throw_length_errorB8ne200100EPKc : 856 -> 84
~ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev -> __ZNSt12length_errorC1B8ne200100EPKc : 16 -> 60
~ __ZNSt3__120__throw_length_errorB8ne190102EPKc -> ___clang_call_terminate : 84 -> 20
~ __ZNSt12length_errorC1B8ne190102EPKc -> __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 60 -> 856
~ _crc_32_calc : 132 -> 292
~ _ETLDMCViewLoadQTraces : 404 -> 500
~ _APPLIB_DIAG_FTM_ChangeFTM_BootMode : 48 -> 376
~ _APPLIB_DIAG_FTM_TX_RX_FREQ_CAL_SWEEP_PARSE : 380 -> 472
CStrings:
+ "Buffer Length %u for payload not enough for, need %zu\n"
+ "Buffer Length %u not enough, need %zu for full timestamp\n"
+ "Buffer Length %u not enough, need %zu for truncated timestamp\n"
+ "ETLEVENTParseReport"
+ "ETLEVENTProcessEventItemTSLength"
+ "ETLEVENTProcessHeader"
+ "ETLEVENTReportFree"
+ "ETLLOGParseLogHeader"
+ "Failed to process header\n"
+ "Freed %u, count was %u\n"
+ "Length %u\n"
+ "Length %u is greater than buffer size %u\n"
+ "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
+ "SNS"
+ "Warning: Buffer Length %u is greater than field length %u\n"

```
