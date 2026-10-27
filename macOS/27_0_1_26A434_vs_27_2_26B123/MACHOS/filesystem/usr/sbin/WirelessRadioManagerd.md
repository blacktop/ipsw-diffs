## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1786.19.0.0.0
-  __TEXT.__text: 0x93e30
+1786.21.0.0.0
+  __TEXT.__text: 0x941f4
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x14e40
-  __TEXT.__objc_methlist: 0xb634
+  __TEXT.__objc_stubs: 0x14ec0
+  __TEXT.__objc_methlist: 0xb674
   __TEXT.__const: 0x2ff0
-  __TEXT.__objc_methname: 0x25a4f
+  __TEXT.__objc_methname: 0x25af4
   __TEXT.__objc_classname: 0x7a3
   __TEXT.__objc_methtype: 0x567a
-  __TEXT.__cstring: 0x3193f
-  __TEXT.__gcc_except_tab: 0xd30
+  __TEXT.__cstring: 0x31b3d
+  __TEXT.__gcc_except_tab: 0xd40
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__oslogstring: 0xbd
-  __TEXT.__unwind_info: 0x1fb0
+  __TEXT.__unwind_info: 0x1fc8
   __DATA_CONST.__const: 0x2450
-  __DATA_CONST.__cfstring: 0x1cae0
+  __DATA_CONST.__cfstring: 0x1cba0
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x660
   __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0x530
-  __DATA.__objc_const: 0x11bb8
-  __DATA.__objc_selrefs: 0x6e70
-  __DATA.__objc_ivar: 0x14bc
+  __DATA.__objc_const: 0x11be8
+  __DATA.__objc_selrefs: 0x6e98
+  __DATA.__objc_ivar: 0x14c0
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0x2f0
   __DATA.__bss: 0x578

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3993
+  Functions: 3998
   Symbols:   358
-  CStrings:  10529
+  CStrings:  10544
 
CStrings:
+ "%s state:%d"
+ "-[WCM_BTController handleBTMusicHandoff:]"
+ "TB,N,V_musicHandoffState"
+ "_musicHandoffState"
+ "_now2c"
+ "evaluateActiveCallQuality: RTP metrics ignored on current SSID, dropping RTP loss and jitter buffer terms"
+ "handleBTMusicHandoff:"
+ "handleBTMusicHandoffState"
+ "isMovingAverageAudioQualityOfCurrentCallGood: RTP metrics ignored on current SSID, dropping moving average RTP loss terms"
+ "isRTPMetricsIgnoredOnCurrentSSID"
+ "isRTPMetricsIgnoredOnCurrentSSID: true"
+ "isWiFiVoIPQualityGoodEnough: RTP metrics ignored on current SSID, suppressing handover. Rx Pkt loss: %llu, rxSpeechPktLoss: %llu, nominal buffer delay: %llu"
+ "kWCMBTMusicHandoffActive"
+ "musicHandoffState"
+ "setMusicHandoffState:"
```
