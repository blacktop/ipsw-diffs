## com.apple.iokit.IOAudio2Family

> `com.apple.iokit.IOAudio2Family`

```diff

 420.2.0.0.0
   __TEXT.__cstring: 0x3af
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x698c
+  __TEXT_EXEC.__text: 0x6bdc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1b58
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 2E9BF56B-4B80-3320-AD46-AE5C366A785E
-  Functions: 352
-  Symbols:   728
+  UUID: 1BA0625E-B0B5-3B9F-990F-E5A3CE869AC5
+  Functions: 350
+  Symbols:   727
   CStrings:  63
 
Symbols:
- _ZN14IOAudio2Device21sendMultiNotificationEjPK20IOAudio2Notification.cold.1
Functions:
~ __Z29IOAudio2Dictionary_setBooleanP12OSDictionaryPKcb : 340 -> 356
~ __Z28IOAudio2Dictionary_setUInt32P12OSDictionaryPKcj : 340 -> 356
~ __Z28IOAudio2Dictionary_setUInt64P12OSDictionaryPKcy : 340 -> 356
~ __ZN25IOAudio2ControlDictionary29createLevelControlSimpleRangeEjjjjjjjxjxjbjP8OSString : 356 -> 380
~ __ZN25IOAudio2ControlDictionary33setSliderControlPropertySelectorsEP12OSDictionaryjj : 420 -> 476
~ __ZN25IOAudio2ControlDictionary26getLevelControlSimpleRangeEP12OSDictionaryRjRxS2_S3_ : 172 -> 188
~ __ZN25IOAudio2ControlDictionary26setLevelControlSimpleRangeEP12OSDictionaryjxjx : 316 -> 336
~ __ZN25IOAudio2ControlDictionary32setLevelControlPropertySelectorsEP12OSDictionaryjjjjjj : 908 -> 1044
~ __ZN25IOAudio2ControlDictionary34setBooleanControlPropertySelectorsEP12OSDictionaryj : 304 -> 340
~ __ZN25IOAudio2ControlDictionary35setSelectorControlPropertySelectorsEP12OSDictionaryjjj : 548 -> 624
~ __ZN25IOAudio2ControlDictionary36setStereoPanControlPropertySelectorsEP12OSDictionaryjj : 420 -> 476
~ __ZN25IOAudio2ControlDictionary32setBlockControlPropertySelectorsEP12OSDictionaryjj : 420 -> 476
~ __ZN14IOAudio2Device4freeEv : 168 -> 172
~ __ZN14IOAudio2Device17createIOReportersEv : 504 -> 512
~ __ZN14IOAudio2Device12stopIOEngineEv : 304 -> 308
~ __ZN14IOAudio2Device13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient : 756 -> 748
~ __ZN14IOAudio2Device22sendSingleNotificationEjjjjyy : 92 -> 108
~ __ZN14IOAudio2Device21sendMultiNotificationEjPK20IOAudio2Notification : 232 -> 244
~ __ZN14IOAudio2Device19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 416 -> 392
+ __ZN14IOAudio2Device15setControlValueEjjPj
- __ZN14IOAudio2Device15setControlValueEjjPj
- __ZN14IOAudio2Device20moveBlockControlDataEjjj
~ __ZN14IOAudio2Device12updateReportEP19IOReportChannelListjPvS2_ : 344 -> 332
~ __ZN24IOAudio2DeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary : 120 -> 128
~ __ZN24IOAudio2DeviceUserClient4freeEv : 120 -> 124
~ __ZN24IOAudio2DeviceUserClient5startEP9IOService : 440 -> 432
~ __ZN24IOAudio2DeviceUserClient4stopEP9IOService : 248 -> 256
~ __ZN24IOAudio2DeviceUserClient26getTargetAndMethodForIndexEPP9IOServicej : 112 -> 148
~ __ZN24IOAudio2DeviceUserClient24getTargetAndTrapForIndexEPP9IOServicej : 108 -> 144
~ __ZN24IOAudio2StreamDictionary16setCurrentFormatEP12OSDictionaryRK30IOAudio2StreamBasicDescription : 176 -> 192
~ __ZN30IOAudio2StreamFormatDictionary31createRangedWithSimpleLinearPCMExxjjjb : 104 -> 100

```
