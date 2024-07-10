## VoiceMemos

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceMemos.framework/Versions/A/VoiceMemos`

```diff

-1235.3.0.0.0
-  __TEXT.__text: 0x418b4
+1234.0.0.0.0
+  __TEXT.__text: 0x4170c
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x32a8
-  __TEXT.__gcc_except_tab: 0x1944
+  __TEXT.__objc_methlist: 0x3240
+  __TEXT.__gcc_except_tab: 0x1938
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x5b5b
+  __TEXT.__cstring: 0x5b40
   __TEXT.__oslogstring: 0x2525
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1728
-  __TEXT.__objc_classname: 0x793
-  __TEXT.__objc_methname: 0xa769
-  __TEXT.__objc_methtype: 0x140e
-  __TEXT.__objc_stubs: 0x7de0
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x1bb0
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__unwind_info: 0x1720
+  __TEXT.__objc_classname: 0x781
+  __TEXT.__objc_methname: 0xa698
+  __TEXT.__objc_methtype: 0x13f3
+  __TEXT.__objc_stubs: 0x7dc0
+  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__const: 0x1b88
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2828
+  __DATA_CONST.__objc_selrefs: 0x2808
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x3040
-  __AUTH_CONST.__objc_const: 0x5a00
+  __AUTH_CONST.__const: 0x680
+  __AUTH_CONST.__cfstring: 0x3020
+  __AUTH_CONST.__objc_const: 0x5908
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH.__objc_data: 0xff0
-  __DATA.__objc_ivar: 0x28c
+  __AUTH.__objc_data: 0xfa0
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0x798
-  __DATA.__bss: 0x288
+  __DATA.__bss: 0x278
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1672
-  Symbols:   4270
-  CStrings:  623
+  Functions: 1664
+  Symbols:   4247
+  CStrings:  622
 
Symbols:
+ -[RCDurationFormatter _onQueueStringFromDuration:byReplacingDigitsWithDigit:hideComponentOptions:style:]
+ -[RCDurationFormatter durationStringsFromDurationIntegers:hideComponentOptions:style:]
+ -[RCDurationFormatter stringFromDuration:hideComponentOptions:style:]
+ ___69-[RCDurationFormatter stringFromDuration:hideComponentOptions:style:]_block_invoke
+ _objc_msgSend$_onQueueStringFromDuration:byReplacingDigitsWithDigit:hideComponentOptions:style:
+ _objc_msgSend$durationStringsFromDurationIntegers:hideComponentOptions:style:
+ _objc_msgSend$stringFromDuration:hideComponentOptions:style:
- +[RCAppGroupStorage sharedInstance]
- -[RCAppGroupStorage .cxx_destruct]
- -[RCAppGroupStorage init]
- -[RCAppGroupStorage setTranscriptionIsSupported:]
- -[RCAppGroupStorage setUserDefaults:]
- -[RCAppGroupStorage transcriptionIsSupported]
- -[RCAppGroupStorage userDefaults]
- -[RCDurationFormatter _onQueueStringFromDuration:byReplacingDigitsWithDigit:hideComponentOptions:style:shouldPadMinute:]
- -[RCDurationFormatter durationStringsFromDurationIntegers:hideComponentOptions:style:shouldPadMinute:]
- -[RCDurationFormatter stringFromDuration:hideComponentOptions:style:shouldPadMinute:]
- OBJC_IVAR_$_RCAppGroupStorage._userDefaults
- _OBJC_CLASS_$_RCAppGroupStorage
- _OBJC_METACLASS_$_RCAppGroupStorage
- __OBJC_$_CLASS_METHODS_RCAppGroupStorage
- __OBJC_$_CLASS_PROP_LIST_RCAppGroupStorage
- __OBJC_$_INSTANCE_METHODS_RCAppGroupStorage
- __OBJC_$_INSTANCE_VARIABLES_RCAppGroupStorage
- __OBJC_$_PROP_LIST_RCAppGroupStorage
- __OBJC_CLASS_RO_$_RCAppGroupStorage
- __OBJC_METACLASS_RO_$_RCAppGroupStorage
- ___35+[RCAppGroupStorage sharedInstance]_block_invoke
- ___85-[RCDurationFormatter stringFromDuration:hideComponentOptions:style:shouldPadMinute:]_block_invoke
- ___block_descriptor_73_e8_32s40r_e5_v8?0lr40l8s32l8
- _objc_msgSend$_onQueueStringFromDuration:byReplacingDigitsWithDigit:hideComponentOptions:style:shouldPadMinute:
- _objc_msgSend$durationStringsFromDurationIntegers:hideComponentOptions:style:shouldPadMinute:
- _objc_msgSend$stringFromDuration:hideComponentOptions:style:shouldPadMinute:
- _objc_msgSend$transcriptionIsSupported
- sharedInstance.onceToken
- sharedInstance.sharedInstance
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformGenerator.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformSegment.mm"
- "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformGenerator.mm"
- "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformSegment.mm"
- "RCTranscriptionIsSupported"

```
