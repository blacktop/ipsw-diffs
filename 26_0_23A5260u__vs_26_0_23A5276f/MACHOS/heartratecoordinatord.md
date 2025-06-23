## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

-15.1.1.0.0
-  __TEXT.__text: 0x1bf10
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0x149c
+17.0.0.0.0
+  __TEXT.__text: 0x1b728
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x2de0
+  __TEXT.__objc_methlist: 0x1414
   __TEXT.__const: 0x330
-  __TEXT.__oslogstring: 0x2e79
-  __TEXT.__cstring: 0xce5
-  __TEXT.__gcc_except_tab: 0x2674
-  __TEXT.__objc_methname: 0x3c42
-  __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methtype: 0x153a
-  __TEXT.__unwind_info: 0xd48
+  __TEXT.__oslogstring: 0x2f03
+  __TEXT.__cstring: 0xd51
+  __TEXT.__gcc_except_tab: 0x2528
+  __TEXT.__objc_methname: 0x3cbd
+  __TEXT.__objc_classname: 0x387
+  __TEXT.__objc_methtype: 0x1541
+  __TEXT.__unwind_info: 0xd78
   __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x9c0
-  __DATA_CONST.__cfstring: 0x960
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x26a8
-  __DATA.__objc_selrefs: 0xd48
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__objc_data: 0x640
+  __DATA.__objc_const: 0x24c0
+  __DATA.__objc_selrefs: 0xd50
+  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DC12B29-A0E6-3EBC-9EB7-4F8635EBE12B
-  Functions: 732
-  Symbols:   195
-  CStrings:  1150
+  UUID: D420D4DA-DABD-3B29-9751-9E40C60EE432
+  Functions: 721
+  Symbols:   192
+  CStrings:  1154
 
Symbols:
+ _objc_opt_isKindOfClass
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSSet
- ___NSArray0__struct
- ___objc_personality_v0
CStrings:
+ "@68@0:8@16@24@32@40@48@56B64"
+ "Got fit notification parameter update: %f %d (was %f %d)"
+ "HRArbOut timestamp: %llu, index: %hu, HR: %{sensitive}f, Conf: %f, Flags: %u, SensorLocation: %u, deviceId: %s, hrId: %s"
+ "Ignoring threshold update because default override is set"
+ "Logging client added count: %u"
+ "Logging client removed count: %u"
+ "Updating fit notification parameters to %{public}f %{public}u"
+ "Writing analytics to log, logging started: %{BOOL}u"
+ "_aacpSource"
+ "_enableWatchSource:enableAacpSource:"
+ "_handleFitNotificationUpdateThreshold:minimumPacketCount:"
+ "_handleFlushNotification"
+ "_notificationThresholdOverride"
+ "_setupAppleSource:"
+ "_watchSource"
+ "com.apple.HeartRateCoordinator.logFlushNotNeeded"
+ "com.apple.heartratecoordinator.spi.heartrate"
+ "enableWatchSource:enableAacpSource:"
+ "handleFitNotificationUpdateThreshold:minimumPacketCount:"
+ "initWithDelegate:watchSource:aacpSource:bleSource:onQueue:analyticsReporter:internalVariant:"
+ "missing entitlement: rejecting connection from PID %d"
+ "setFitNotificationParamUpdateHandler:"
+ "started"
+ "v16@?0f8I12"
+ "v16@?0r^{HRCSourceUpdate=@q@@CCBB}8"
+ "v24@0:8@?<v@?^{HRCSourceUpdate=@q@@CCBB}>16"
+ "v24@0:8@?<v@?fI>16"
+ "v24@0:8B16B20"
+ "v24@0:8f16I20"
+ "v32@0:8r^{HRCSourceUpdate=@q@@CCBB}16Q24"
+ "valueForEntitlement:"
+ "\x91"
- "%@, count : %lu"
- "@\"NSUUID\""
- "@60@0:8@16@24@32@40@48B56"
- "HRArbOut timestamp: %llu, index: %hu, HR: %f, Conf: %f, Flags: %u, SensorLocation: %u, deviceId: %s, hrId: %s"
- "HRCDummySource"
- "T@\"<HRCSource>\",&,N,V_bleSource"
- "T@\"NSSet\",&,N,V_appleSources"
- "_appleSources"
- "_device"
- "_deviceUuid"
- "_dummyHeartRateTimer"
- "_generateDummyHeartRates"
- "adding dummy source"
- "appleSources"
- "bleSource"
- "discoveryEnabled"
- "generated dummy HR with uuid : %@, bpm : %f, confidence : %f, context : %ld, date : %@"
- "init of HRDummySource"
- "initWithArray:"
- "initWithDelegate:appleSources:bleSource:onQueue:analyticsReporter:internalVariant:"
- "initWithQueue:"
- "request received for updated streaming mode : %lu"
- "setAppleSources:"
- "setBleSource:"
- "starting dummy streaming"
- "v24@0:8@?<v@?{HRCSourceUpdate=@q@@CCBB}>16"
- "v48@?0{HRCSourceUpdate=@q@@CCBB}8"
- "v56@0:8{HRCSourceUpdate=@q@@CCBB}16"
- "v64@0:8{HRCSourceUpdate=@q@@CCBB}16Q56"

```
