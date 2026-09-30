## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-1935.2.0.0.0
-  __TEXT.__text: 0x170d3c
-  __TEXT.__auth_stubs: 0x26e0
-  __TEXT.__objc_stubs: 0x216e0
+1937.1.0.0.0
+  __TEXT.__text: 0x1713d8
+  __TEXT.__auth_stubs: 0x26f0
+  __TEXT.__objc_stubs: 0x21720
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x11bdc
+  __TEXT.__objc_methlist: 0x11bf4
   __TEXT.__const: 0x11e08
   __TEXT.__gcc_except_tab: 0x6364
-  __TEXT.__cstring: 0x59fd1
-  __TEXT.__objc_methname: 0x34630
+  __TEXT.__cstring: 0x5a193
+  __TEXT.__objc_methname: 0x346a6
   __TEXT.__objc_classname: 0x11e2
-  __TEXT.__objc_methtype: 0x8afe
+  __TEXT.__objc_methtype: 0x8b16
   __TEXT.__dlopen_cstrs: 0x43e
   __TEXT.__oslogstring: 0x109
-  __TEXT.__unwind_info: 0x50e8
-  __DATA_CONST.__const: 0x5858
-  __DATA_CONST.__cfstring: 0x32e80
+  __TEXT.__unwind_info: 0x50f0
+  __DATA_CONST.__const: 0x5888
+  __DATA_CONST.__cfstring: 0x32f60
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x848
   __DATA_CONST.__objc_arrayobj: 0x6780
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1388
+  __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x8b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1cf18
-  __DATA.__objc_selrefs: 0xa028
-  __DATA.__objc_ivar: 0x1e7c
+  __DATA.__objc_const: 0x1cf78
+  __DATA.__objc_selrefs: 0xa038
+  __DATA.__objc_ivar: 0x1e88
   __DATA.__objc_data: 0x3430
-  __DATA.__data: 0x840
+  __DATA.__data: 0x838
   __DATA.__bss: 0x7e0
-  __DATA.__common: 0x642
+  __DATA.__common: 0x632
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7805
-  Symbols:   873
-  CStrings:  16861
+  Functions: 7810
+  Symbols:   874
+  CStrings:  16874
 
Symbols:
+ _WiFiDeviceClientRegisterPowerCallback
CStrings:
+ "%s Received RRC state: %d from BB"
+ "ON"
+ "WiFiS: callbackWiFiDeviceClientPower power is %s"
+ "^{WRMMetricsGenericCellularScore=dIQIdddIIIIIIBB}16@0:8"
+ "evaluateGenericCellularScore RRC idle with history: finalScore: %s"
+ "getForegroundApp app: %@, webkit streaming active: %s"
+ "handleGamingStateChange state=%d, appId=%@"
+ "handleVoIPStateChange state=%d, appId=%@"
+ "handleVoIPandStreamingStateChange state=%d, appId=%@"
+ "handleWebKitStateChange state=%d, appId=%@"
+ "mAudioAccessoryTkn"
+ "mPrevAudioBandMessage"
+ "mPrevAudioMessage"
+ "maybeNotifyStreamingStop"
+ "maybeNotifyStreamingStop: mStreamingConnectionReferenceCount: %llu, mWebkitStreamingActiveRefCnt: %d, mForegroundRunningVoipAndStreamingApps.count: %lu, mForegroundRunningStreamingApps.count: %lu"
+ "maybeNotifyStreamingStop: notify streaming stop"
+ "smartLQM"
+ "startMonitoringAppSessions %@ configuration status: %d, for app: %@"
+ "startMonitoringAppSessions %@ start monitoring for app: %@"
+ "updateWebkitStreamingActiveStatus"
+ "updateWebkitStreamingActiveStatus: resetting refcount from %d to 0"
+ "{WRMMetricsGenericCellularScore=\"timestamp\"d\"lastCellScore\"I\"lastCellScoreDuration\"Q\"currentCellScore\"I\"rsrp\"d\"rsrq\"d\"snr\"d\"dataLQM\"I\"voiceLQM\"I\"smartLQM\"I\"dlConf\"I\"dlBw\"I\"rrcState\"I\"wifiPrimary\"B\"historicalInfoGood\"B}"
- "WiFiS: callbackWiFiDeviceClientDeviceAvailable Power ON due to DextCrash recovery"
- "^{WRMMetricsGenericCellularScore=dIQIdddIIIIBB}16@0:8"
- "evaluateGenericCellularScore RRC idle with history: dataLQM: %d, finalScore: %s"
- "handleGamingStateChange state= %d, appId=%@"
- "handleVoIPStateChange state= %d, appId=%@"
- "handleVoIPandStreamingStateChange state= %d, appId=%@"
- "handleWebKitStateChange state= %d, appId=%@"
- "stats manager configuration status %d"
- "{WRMMetricsGenericCellularScore=\"timestamp\"d\"lastCellScore\"I\"lastCellScoreDuration\"Q\"currentCellScore\"I\"rsrp\"d\"rsrq\"d\"snr\"d\"dataLQM\"I\"dlConf\"I\"dlBw\"I\"rrcState\"I\"wifiPrimary\"B\"historicalInfoGood\"B}"
```
