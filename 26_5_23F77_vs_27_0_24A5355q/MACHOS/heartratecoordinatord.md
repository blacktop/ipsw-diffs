## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

-31.2.0.0.0
-  __TEXT.__text: 0x27330
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x3be0
+38.0.0.0.0
+  __TEXT.__text: 0x25870
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x3ce0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x18ac
+  __TEXT.__objc_methlist: 0x190c
   __TEXT.__const: 0x369
-  __TEXT.__oslogstring: 0x3946
-  __TEXT.__cstring: 0x201f
-  __TEXT.__gcc_except_tab: 0x428c
-  __TEXT.__objc_methname: 0x4be9
-  __TEXT.__objc_classname: 0x3d0
-  __TEXT.__objc_methtype: 0x1b68
-  __TEXT.__unwind_info: 0x12b0
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xbe0
-  __DATA_CONST.__cfstring: 0x1d80
+  __TEXT.__oslogstring: 0x3a11
+  __TEXT.__cstring: 0x20fb
+  __TEXT.__gcc_except_tab: 0x4058
+  __TEXT.__objc_methname: 0x4d9a
+  __TEXT.__objc_classname: 0x38b
+  __TEXT.__objc_methtype: 0x1ba5
+  __TEXT.__unwind_info: 0x1180
+  __DATA_CONST.__const: 0xc18
+  __DATA_CONST.__cfstring: 0x1f60
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x150
-  __DATA_CONST.__objc_arraydata: 0x520
+  __DATA_CONST.__objc_intobj: 0x168
+  __DATA_CONST.__objc_arraydata: 0x570
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_const: 0x2b10
-  __DATA.__objc_selrefs: 0x10e8
-  __DATA.__objc_ivar: 0x274
+  __DATA_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__got: 0x210
+  __DATA.__objc_const: 0x2b90
+  __DATA.__objc_selrefs: 0x1130
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x600
   __DATA.__bss: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AB09598-AE0C-3922-83B1-B777E8CE737B
-  Functions: 892
-  Symbols:   199
-  CStrings:  1769
+  UUID: EA664B0F-336C-3DC5-BB18-6E9E1550175B
+  Functions: 896
+  Symbols:   206
+  CStrings:  1811
 
Symbols:
+ ___exp10
+ _log10
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"HRCHeartRateData\""
+ "@\"NSDate\""
+ "@24@0:8q16"
+ "@48@0:8@16@24@32@40"
+ "Background"
+ "BackgroundTachogram"
+ "Breathe"
+ "HR with bpm: %{sensitive}f"
+ "NotSet"
+ "OxygenSaturation"
+ "Sedentary"
+ "SleepModeSedentary"
+ "StreamingECG"
+ "StreamingPPG"
+ "T@\"HRCHeartRateData\",&,N,V_mostRecentHighConfidenceHeartRate"
+ "Unknown(%ld)"
+ "Walking"
+ "WheelchairMotion"
+ "Workout"
+ "_lastPublishedDateOnWatch"
+ "_mostRecentHighConfidenceHeartRate"
+ "_requestMostRecentHighConfidenceHeartRate"
+ "current Watch HR timestamp (%{public}@) is older than last published timestamp (%{public}@): writing as an individual sample instead"
+ "deliveryMode"
+ "failed to save heart rate as a sample: %{public}@"
+ "handleMostRecentHighConfidenceHeartRate:"
+ "initWithDelegate:remoteObjectProxy:onQueue:mostRecentHighConfidenceHR:"
+ "most recent high confidence HR requested by %{public}@, returning %@"
+ "mostRecentHighConfidenceHeartRate"
+ "nil"
+ "numberWithLong:"
+ "publishing HR sample to HK with UUID : %{public}@ , bpm : %{sensitive}f , context : %{public}@ , deliveryMode : 0x%02x"
+ "received hr from HRCSourceTypePlatinum but watchSourceCollector is nil, initialzing data collector"
+ "requestMostRecentHighConfidenceHeartRate"
+ "roundTo2SignificantFigures:"
+ "setMostRecentHighConfidenceHeartRate:"
+ "stringFromHRCHeartRateContext:"
+ "\x81"
- "a"
- "hrValue"
- "initWithDelegate:remoteObjectProxy:onQueue:"
- "location"
- "logHrOut"
- "mode"
- "publishing HR sample to HK with UUID : %{public}@ , bpm : %{sensitive}f , context : %{sensitive}ld , streamingThrottleStatus : %{public}d"
- "received hr from HRCSourceTypePlatinum but watchSourceCollector is nil"
- "saveObject completion handler :: success : %d, error : %@"

```
