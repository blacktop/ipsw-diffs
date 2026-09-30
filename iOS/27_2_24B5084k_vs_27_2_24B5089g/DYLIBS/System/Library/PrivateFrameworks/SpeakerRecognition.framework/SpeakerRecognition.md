## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3605.23.1.0.0
-  __TEXT.__text: 0xb66d0
-  __TEXT.__objc_methlist: 0x6d90
+3605.25.1.0.0
+  __TEXT.__text: 0xb6ab8
+  __TEXT.__objc_methlist: 0x6dd0
   __TEXT.__const: 0xfa8
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__cstring: 0x10fa9
+  __TEXT.__cstring: 0x11068
   __TEXT.__swift5_typeref: 0x696
-  __TEXT.__oslogstring: 0xee41
+  __TEXT.__oslogstring: 0xef0c
   __TEXT.__swift5_capture: 0x230
   __TEXT.__constg_swiftt: 0x908
   __TEXT.__swift5_reflstr: 0x57f

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x30
   __TEXT.__gcc_except_tab: 0x29d0
-  __TEXT.__unwind_info: 0x29a8
+  __TEXT.__unwind_info: 0x29c0
   __TEXT.__eh_frame: 0x1368
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f18
+  __DATA_CONST.__objc_selrefs: 0x3f40
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x3e0
   __DATA_CONST.__got: 0xb30
   __AUTH_CONST.__const: 0xee0
   __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0xbc68
+  __AUTH_CONST.__objc_const: 0xbc88
   __AUTH_CONST.__objc_dictobj: 0x9b0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x50

   __AUTH_CONST.__auth_got: 0x1020
   __AUTH.__objc_data: 0x1b8
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x874
+  __DATA.__objc_ivar: 0x878
   __DATA.__data: 0x1448
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x2678
   __DATA_DIRTY.__data: 0x580
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x70
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3096
-  Symbols:   6434
-  CStrings:  2650
+  Functions: 3102
+  Symbols:   6446
+  CStrings:  2657
 
Symbols:
+ -[CSVTUITrainingSession hasLiveSpeechTranscriber]
+ -[CSVTUITrainingSession hasUsableRecognizer]
+ -[CSVTUITrainingSessionWithPayload _deferCloseForTranscriberFinal]
+ -[CSVTUITrainingSessionWithPayload _firedTranscriberFinalTimeout]
+ -[CSVTUITrainingSessionWithPayload _registerTranscriberFinalTimeout]
+ GCC_except_table1661
+ GCC_except_table1766
+ GCC_except_table1781
+ GCC_except_table1791
+ GCC_except_table1801
+ GCC_except_table1806
+ GCC_except_table1822
+ GCC_except_table1826
+ GCC_except_table1836
+ GCC_except_table1844
+ GCC_except_table1908
+ GCC_except_table1912
+ GCC_except_table1973
+ GCC_except_table2008
+ GCC_except_table2074
+ GCC_except_table2084
+ GCC_except_table2093
+ GCC_except_table2104
+ GCC_except_table2113
+ GCC_except_table2132
+ GCC_except_table2194
+ _OBJC_IVAR_$_CSVTUITrainingSessionWithPayload._awaitingTranscriberFinal
+ ___68-[CSVTUITrainingSessionWithPayload _registerTranscriberFinalTimeout]_block_invoke
+ _objc_msgSend$_deferCloseForTranscriberFinal
+ _objc_msgSend$_firedTranscriberFinalTimeout
+ _objc_msgSend$_registerTranscriberFinalTimeout
+ _objc_msgSend$hasLiveSpeechTranscriber
+ _objc_msgSend$hasUsableRecognizer
- GCC_except_table1657
- GCC_except_table1754
- GCC_except_table1775
- GCC_except_table1785
- GCC_except_table1795
- GCC_except_table1800
- GCC_except_table1816
- GCC_except_table1820
- GCC_except_table1824
- GCC_except_table1838
- GCC_except_table1902
- GCC_except_table1906
- GCC_except_table1967
- GCC_except_table2002
- GCC_except_table2068
- GCC_except_table2078
- GCC_except_table2087
- GCC_except_table2098
- GCC_except_table2107
- GCC_except_table2126
- GCC_except_table2188
CStrings:
+ "%s Finalizing speech transcriber; awaiting final result"
+ "%s No usable recognizer; using no-SpeechAPI EOS timeout"
+ "%s Transcriber final result did not arrive; closing session"
+ "%s Using SpeechAPI EOS timeout"
+ "-[CSVTUITrainingSessionWithPayload _deferCloseForTranscriberFinal]"
+ "-[CSVTUITrainingSessionWithPayload _firedTranscriberFinalTimeout]"
+ "-[CSVTUITrainingSessionWithPayload _getSessionEOSTimeout]"
```
