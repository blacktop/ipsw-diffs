## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/Versions/A/LocalSpeechRecognitionBridge`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0x1fc00
-  __TEXT.__objc_methlist: 0x256c
+3600.70.47.0.0
+  __TEXT.__text: 0x1fe24
+  __TEXT.__objc_methlist: 0x25a4
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x4b7a
-  __TEXT.__oslogstring: 0x2d14
+  __TEXT.__cstring: 0x4bf2
+  __TEXT.__oslogstring: 0x2d90
   __TEXT.__unwind_info: 0x760
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1318
+  __DATA_CONST.__objc_selrefs: 0x1350
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x1ac0
-  __AUTH_CONST.__objc_const: 0x3e68
+  __AUTH_CONST.__cfstring: 0x1b00
+  __AUTH_CONST.__objc_const: 0x3ec8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x8b0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x58

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 781
-  Symbols:   1896
-  CStrings:  613
+  Functions: 786
+  Symbols:   1910
+  CStrings:  617
 
Symbols:
+ -[LBAudioStreamInfo initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:originatingDeviceInvocationType:]
+ -[LBAudioStreamInfo originatingDeviceInvocationType]
+ -[LBAudioStreamInfo originatingDeviceSupportsAlwaysListeningHeySiri]
+ -[LBAudioStreamInfo setOriginatingDeviceInvocationType:]
+ -[LBAudioStreamInfo setOriginatingDeviceSupportsAlwaysListeningHeySiri:]
+ GCC_except_table334
+ GCC_except_table348
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table486
+ GCC_except_table496
+ GCC_except_table591
+ GCC_except_table709
+ GCC_except_table754
+ OBJC_IVAR_$_LBAudioStreamInfo._originatingDeviceInvocationType
+ OBJC_IVAR_$_LBAudioStreamInfo._originatingDeviceSupportsAlwaysListeningHeySiri
+ _objc_msgSend$initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:originatingDeviceInvocationType:
+ _objc_msgSend$integerValue
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$originatingDeviceInvocationType
+ _objc_msgSend$originatingDeviceSupportsAlwaysListeningHeySiri
+ _objc_msgSend$setOriginatingDeviceInvocationType:
+ _objc_msgSend$setOriginatingDeviceSupportsAlwaysListeningHeySiri:
- GCC_except_table329
- GCC_except_table343
- GCC_except_table468
- GCC_except_table472
- GCC_except_table481
- GCC_except_table491
- GCC_except_table586
- GCC_except_table704
- GCC_except_table739
CStrings:
+ "%s Failed to decode `originatingDeviceInvocationType`"
+ "%s Failed to decode `originatingDeviceSupportsAlwaysListeningHeySiri`"
+ "LBAudioStreamInfo:::originatingDeviceInvocationType"
+ "LBAudioStreamInfo:::originatingDeviceSupportsAlwaysListeningHeySiri"
```
