## timed

> `/usr/libexec/timed`

```diff

-334.0.16.3.0
-  __TEXT.__text: 0x176d8
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x2560
+340.0.8.0.0
+  __TEXT.__text: 0x17500
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_stubs: 0x26c0
   __TEXT.__objc_methlist: 0xd6c
   __TEXT.__const: 0x280
-  __TEXT.__objc_methname: 0x2397
-  __TEXT.__cstring: 0x1fd0
-  __TEXT.__objc_classname: 0x11d
-  __TEXT.__objc_methtype: 0x53e
-  __TEXT.__oslogstring: 0x2ae2
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__unwind_info: 0x610
-  __DATA_CONST.__auth_got: 0x5e0
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__cfstring: 0x2a40
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__objc_methname: 0x2550
+  __TEXT.__cstring: 0x20a1
+  __TEXT.__objc_classname: 0x111
+  __TEXT.__objc_methtype: 0x554
+  __TEXT.__oslogstring: 0x2c1b
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__unwind_info: 0x5e8
+  __DATA_CONST.__const: 0xe48
+  __DATA_CONST.__cfstring: 0x2b20
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_intobj: 0x5b8
+  __DATA_CONST.__objc_intobj: 0x5d0
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__objc_arraydata: 0x78
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1e10
-  __DATA.__objc_selrefs: 0xad8
-  __DATA.__objc_ivar: 0x170
-  __DATA.__objc_data: 0x370
+  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__got: 0x1c8
+  __DATA.__objc_const: 0x1da0
+  __DATA.__objc_selrefs: 0xb40
+  __DATA.__objc_ivar: 0x174
+  __DATA.__objc_data: 0x320
   __DATA.__data: 0x310
   __DATA.__bss: 0x140
   __DATA.__common: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7C179308-BB8D-3ACA-9267-166836A931E2
-  Functions: 602
-  Symbols:   254
-  CStrings:  1627
+  UUID: 925FF1B9-48CF-3B8F-BE08-5691A67AE575
+  Functions: 615
+  Symbols:   257
+  CStrings:  1664
 
Symbols:
+ _NSInvalidArgumentException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_TMTimeZone
+ _objc_retain_x20
- _OBJC_CLASS_$_NSConstantArray
CStrings:
+ "%@: source %@ has been rejected by Secure Filter, incrementing count (+%lu points, total: %lu)"
+ "340.0.8"
+ "BasebandAPTimeSync"
+ "Calling didFinishSetup"
+ "Calling startPeerSyncClient"
+ "Calling startPeerSyncServerWithCompletionHandler"
+ "Q24@0:8@16"
+ "Reset threshold reached: %lu >= %lu total reject points"
+ "Returning async reference time to client"
+ "SynthesizerMonitorThresholds"
+ "T@\"NSDictionary\",R"
+ "T@\"NSMutableDictionary\",&,N,V_sourceRejects"
+ "TMAutoSetTimeNotification"
+ "TMDidFinishSetupCommand"
+ "TMGetReferenceTimeAsync"
+ "TMReferenceTimeSuccessful"
+ "TMStartPeerClientCommand"
+ "TMStartPeerServerCommand"
+ "TQ,N,V_totalRejectPoints"
+ "_lastReferenceTimeTMLogAnalytics"
+ "_monitor"
+ "_totalRejectPoints"
+ "calculatePointsForSource:"
+ "defaultSynthesizerMonitorThresholdsForAppleTV"
+ "defaultSynthesizerMonitorThresholdsForDefaultPlatform"
+ "defaultSynthesizerMonitorThresholdsForMacOS"
+ "defaultSynthesizerMonitorThresholdsForVisionOS"
+ "dictionaryForKey:"
+ "didFinishSetup"
+ "didFinishSetupWithCompletionHandler:"
+ "error calling didFinishSetup: %@"
+ "error staring PeerTime client: %@"
+ "error staring PeerTime server: %@"
+ "initWithPrefs:"
+ "initializing synthesizer monitor: %@"
+ "raise:format:"
+ "referenceTime called with nil handler"
+ "resetThresholdReached"
+ "resetting reject counts (total points: %lu)"
+ "setTotalRejectPoints:"
+ "sources parameter cannot be nil"
+ "startPeerSyncClientWithCompletionHandler:"
+ "startPeerSyncServerWithCompletionHandler:"
+ "synthesizerMonitorThresholds"
+ "thresholdForSource:"
+ "totalRejectPoints"
+ "total_reject_points"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8Q16"
- "334.0.16.3"
- "<%@: %p (%@: %@)>"
- "HXTqT3UXOKuTEklxz+wMAA"
- "LocationBorder"
- "T@\"NSMutableDictionary\",V_sourceRejects"
- "T@\"NSString\",C,V_olsonName"
- "T@\"NSString\",C,V_source"
- "_olsonName"
- "_source"
- "initWithOlsonName:fromSource:"
- "monitor"
- "not recomputing because %@ source is not fetchable"
- "resetThreshholdReached"
- "resetting reject counts"
- "setOlsonName:"
- "source %@ has been rejected by Secure Filter, incrementing count"
- "source %@ is not being tracked by TMTimeSynthesizerMonitor"
- "timeZoneWithOlsonName:fromSource:"

```
