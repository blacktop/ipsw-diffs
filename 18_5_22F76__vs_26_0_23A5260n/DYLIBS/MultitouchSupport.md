## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-8140.4.0.0.0
-  __TEXT.__text: 0x1e200
+9100.23.0.0.0
+  __TEXT.__text: 0x1e30c
   __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0x2010
-  __TEXT.__cstring: 0x16ba
-  __TEXT.__oslogstring: 0x10ca
+  __TEXT.__const: 0x2008
+  __TEXT.__cstring: 0x1679
+  __TEXT.__oslogstring: 0x10b8
   __TEXT.__tpad_act_plist: 0xe22d
-  __TEXT.__unwind_info: 0x6d0
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0x682
-  __TEXT.__objc_methtype: 0x591
-  __TEXT.__objc_stubs: 0x560
+  __TEXT.__objc_methname: 0x677
+  __TEXT.__objc_methtype: 0x596
+  __TEXT.__objc_stubs: 0x540
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x740
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__cfstring: 0x1120
   __AUTH_CONST.__objc_const: 0x868
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x1c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20792C69-DF14-30A0-BDA8-82685D61EEF7
-  Functions: 661
-  Symbols:   1420
-  CStrings:  627
+  UUID: 771A1725-5CE2-3743-9063-E273047B95AA
+  Functions: 664
+  Symbols:   1422
+  CStrings:  616
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorReallocateTyped
+ _MTActuatorGetProductionPlist
+ _MTRegisterWorkIntervalCallback
+ _MTUnregisterWorkIntervalCallback
+ _mt_PostWorkIntervalEvent
- _CFAllocatorAllocate
- _CFAllocatorReallocate
- _objc_msgSend$floatValue
- _resetPathLifeCycle
CStrings:
+ "@32@0:8@16^{__MTDevice={__CFRuntimeBase=QAQ}IIB^{__MTActuator}BBBBIIIIQIIIIIIII^{__CFString}{?=BB}BBBBBBIIBBBBBBBB*d^{__ALGLibraryState}IQCIqIIIISBii[20{MTSensorRegion=CCCCCC(?=CC)}]{MTSensorRegionThresholds=sss}{MTSensorSurfaceDescriptor=IIssss}I^{MTParsedMultitouchFrameRep_t}{__MTDeviceCallbacksStruct=[21{__MTDeviceCallbackRecord=(?=[4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?]^?[4^?])C[4^v]}]i[4S]f[4S]f[4{ImageCallbackFilter=II}][5f][5{MTStatisticParameters=ff}][5*]B{?=iII}}^{__CFMachPort}^{__CFString}^{__CFRunLoopSource}B^{__CFRunLoop}[3I]CiiBIBIB@i^{__CFData}QQQCBB[5I][5I]^vQB^vB{?=i*I{MTBinaryFrameHeader={MTBinaryHeader=CCCCI}{MTImagePathContentOptions=CCCC}SSCCsSsC}I[32{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}]I[32^{?}]{?=*IS}}[7C]CQ^{work_interval}IBC^{__CFDictionary}}24"
+ "Sensor Surface dimensions not provided. Using defaults or getting from descriptor (%lu x %lu)"
- "@32@0:8@16^{__MTDevice={__CFRuntimeBase=QAQ}IIB^{__MTActuator}BBBBIIIIQIIIIIIII^{__CFString}{?=BB}BBBBBBIIBBBBBBBB*d^{__ALGLibraryState}IQCIqIIIISBii[20{MTSensorRegion=CCCCCC(?=CC)}]{MTSensorRegionThresholds=sss}{MTSensorSurfaceDescriptor=IIssss}I^{MTParsedMultitouchFrameRep_t}{__MTDeviceCallbacksStruct=[20{__MTDeviceCallbackRecord=(?=[4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?]^?)C[4^v]}]i[4S]f[4S]f[4{ImageCallbackFilter=II}][5f][5{MTStatisticParameters=ff}][5*]B{?=iII}}^{__CFMachPort}^{__CFString}^{__CFRunLoopSource}B^{__CFRunLoop}[3I]CiiBIBIB@i^{__CFData}QQQCBB[5I][5I]^vQB^vB{?=i*I{MTBinaryFrameHeader={MTBinaryHeader=CCCCI}{MTImagePathContentOptions=CCCC}SSCCsSsC}I[32{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}]I[32^{?}]{?=*IS}}[7C]CQ^{work_interval}IBC^{__CFDictionary}}24"
- "ActuatorLimits"
- "AmplitudeMax"
- "AmplitudeMin"
- "DurationMax"
- "DurationMin"
- "Sensor Surface dimensions not provided. Using defaults or getting from descriptor (%lu x %lu) (deviceID 0x%llX)"
- "floatValue"

```
