## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1939.3.0.0.0
-  __TEXT.__text: 0x1716d8
+1950.2.0.0.0
+  __TEXT.__text: 0x171ac8
   __TEXT.__auth_stubs: 0x2790
-  __TEXT.__objc_stubs: 0x21920
+  __TEXT.__objc_stubs: 0x219c0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x11cac
+  __TEXT.__objc_methlist: 0x11cec
   __TEXT.__const: 0x11f10
-  __TEXT.__gcc_except_tab: 0x65a0
-  __TEXT.__cstring: 0x5a831
-  __TEXT.__objc_methname: 0x347ee
+  __TEXT.__gcc_except_tab: 0x65b0
+  __TEXT.__cstring: 0x5aa2f
+  __TEXT.__objc_methname: 0x34893
   __TEXT.__objc_classname: 0x11e2
   __TEXT.__objc_methtype: 0x8bea
   __TEXT.__dlopen_cstrs: 0x43e
   __TEXT.__oslogstring: 0x109
-  __TEXT.__unwind_info: 0x6078
+  __TEXT.__unwind_info: 0x6088
   __DATA_CONST.__const: 0x59f8
-  __DATA_CONST.__cfstring: 0x33400
+  __DATA_CONST.__cfstring: 0x334c0
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x13e0
   __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1d038
-  __DATA.__objc_selrefs: 0xa080
-  __DATA.__objc_ivar: 0x1e9c
+  __DATA.__objc_const: 0x1d068
+  __DATA.__objc_selrefs: 0xa0a8
+  __DATA.__objc_ivar: 0x1ea0
   __DATA.__objc_data: 0x3430
   __DATA.__data: 0x838
   __DATA.__common: 0x63a

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7862
+  Functions: 7867
   Symbols:   890
-  CStrings:  16934
+  CStrings:  16949
 
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
