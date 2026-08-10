## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0x1db4c
-  __TEXT.__objc_methlist: 0x256c
+3600.70.47.0.0
+  __TEXT.__text: 0x1dd64
+  __TEXT.__objc_methlist: 0x25a4
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x4acc
-  __TEXT.__oslogstring: 0x2d14
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__cstring: 0x4b44
+  __TEXT.__oslogstring: 0x2d90
+  __TEXT.__unwind_info: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1318
+  __DATA_CONST.__objc_selrefs: 0x1350
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0xc0
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

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 749
-  Symbols:   1876
-  CStrings:  611
+  Functions: 754
+  Symbols:   1890
+  CStrings:  615
 
Symbols:
+ -[LBAudioStreamInfo initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:originatingDeviceInvocationType:]
+ -[LBAudioStreamInfo originatingDeviceInvocationType]
+ -[LBAudioStreamInfo originatingDeviceSupportsAlwaysListeningHeySiri]
+ -[LBAudioStreamInfo setOriginatingDeviceInvocationType:]
+ -[LBAudioStreamInfo setOriginatingDeviceSupportsAlwaysListeningHeySiri:]
+ GCC_except_table314
+ GCC_except_table328
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table461
+ GCC_except_table468
+ GCC_except_table561
+ GCC_except_table677
+ GCC_except_table722
+ _OBJC_IVAR_$_LBAudioStreamInfo._originatingDeviceInvocationType
+ _OBJC_IVAR_$_LBAudioStreamInfo._originatingDeviceSupportsAlwaysListeningHeySiri
+ _objc_msgSend$initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:originatingDeviceInvocationType:
+ _objc_msgSend$integerValue
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$originatingDeviceInvocationType
+ _objc_msgSend$originatingDeviceSupportsAlwaysListeningHeySiri
+ _objc_msgSend$setOriginatingDeviceInvocationType:
+ _objc_msgSend$setOriginatingDeviceSupportsAlwaysListeningHeySiri:
- GCC_except_table309
- GCC_except_table323
- GCC_except_table446
- GCC_except_table450
- GCC_except_table456
- GCC_except_table463
- GCC_except_table556
- GCC_except_table672
- GCC_except_table707
CStrings:
+ "%s Failed to decode `originatingDeviceInvocationType`"
+ "%s Failed to decode `originatingDeviceSupportsAlwaysListeningHeySiri`"
+ "LBAudioStreamInfo:::originatingDeviceInvocationType"
+ "LBAudioStreamInfo:::originatingDeviceSupportsAlwaysListeningHeySiri"
```
