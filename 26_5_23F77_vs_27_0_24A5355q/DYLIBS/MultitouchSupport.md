## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0x1e3f8
-  __TEXT.__auth_stubs: 0xe50
+9170.34.1.0.0
+  __TEXT.__text: 0x1e350
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0x1ff8
-  __TEXT.__cstring: 0x169e
-  __TEXT.__oslogstring: 0x1136
+  __TEXT.__const: 0x2028
+  __TEXT.__cstring: 0x16b5
+  __TEXT.__oslogstring: 0x12b4
   __TEXT.__tpad_act_plist: 0xe22d
-  __TEXT.__unwind_info: 0x6e0
-  __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0x677
-  __TEXT.__objc_methtype: 0x596
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__cfstring: 0x1140
   __AUTH_CONST.__objc_const: 0x868
+  __AUTH_CONST.__auth_got: 0x780
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x1c0
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 340C64FE-2C92-3052-92EC-03EE6890188C
-  Functions: 668
-  Symbols:   1430
-  CStrings:  619
+  UUID: BD7617EF-5446-361C-9A90-9778FEF48A71
+  Functions: 663
+  Symbols:   1431
+  CStrings:  484
 
Symbols:
+ _GetHIDServiceForService
+ _IOHIDEventSystemClientCopyServices
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDServiceClientCopyProperty
+ _IOHIDServiceClientGetRegistryID
+ _IOHIDServiceClientSetProperty
+ ___block_descriptor_tmp.216
+ __os_log_default
+ __os_signpost_emit_with_name_impl
+ _mach_get_times
+ _mtalg_MaxContacts
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
+ _os_signpost_enabled
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __ZL22MTParse_SABinary_PathsRK19_SABinaryInjExtDataPKhP28MTParsedMultitouchFrameRep_tP10__MTDevice
- __ZL29MTParse_SABinary_FireflyPathsRK19_SABinaryInjExtDataPKhP28MTParsedMultitouchFrameRep_tP10__MTDevice
- __ZZ16MTParse_SABinaryEN3$_28__invokeEPvRK21_SABinaryInjExtPacketPKh
- ___block_descriptor_tmp.213
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "%{public, signpost.description:begin_time}llu, %{public, signpost.description:end_time}llu"
+ "%{public, signpost.description:begin_time}llu, %{public, signpost.description:end_time}llu, Finish? %{BOOL}d"
+ "Force sensor position(%d) calculation hit a critical error"
+ "Raw force sensor position(%d) calculation hit a critical error"
+ "SystemActuations"
+ "WorkIntervalTouchLegacyDeadline"
+ "WorkIntervalTouchLegacySpan"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"NSBundle\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@\"NSDictionary\"16@?<@\"NSData\"@?@\"NSString\">24"
- "@32@0:8@16@?24"
- "@32@0:8@16^{__MTDevice={__CFRuntimeBase=QAQ}IIB^{__MTActuator}BBBBIIIIQIIIIIIII^{__CFString}{?=BB}BBBBBBIIBBBBBBBB*d^{__ALGLibraryState}IQCIqIIIISBii[20{MTSensorRegion=CCCCCC(?=CC)}]{MTSensorRegionThresholds=sss}{MTSensorSurfaceDescriptor=IIssss}I^{MTParsedMultitouchFrameRep_t}{__MTDeviceCallbacksStruct=[21{__MTDeviceCallbackRecord=(?=[4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?][4^?]^?[4^?])C[4^v]}]i[4S]f[4S]f[4{ImageCallbackFilter=II}][5f][5{MTStatisticParameters=ff}][5*]B{?=iII}}^{__CFMachPort}^{__CFString}^{__CFRunLoopSource}B^{__CFRunLoop}[3I]CiiBIBIB@i^{__CFData}QQQCBB[5I][5I]^vQB^vB{?=i*I{MTBinaryFrameHeader={MTBinaryHeader=CCCCI}{MTImagePathContentOptions=CCCC}SSCCsSsC}I[32{?=qdiiii{MTPoint=ff}{MTPoint=ff}fffff{MTPoint=ff}{MTPoint=ff}S ff}]I[32^{?}]{?=*IS}}[7C]CQ^{work_interval}IBC^{__CFDictionary}}24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "I16@0:8"
- "MTAHTSupport"
- "MTBinaryFilterLegacy"
- "MTBinaryFilterProtocol"
- "NSObject"
- "Q16@0:8"
- "T#,&,N,V_AHTDevice"
- "T#,&,N,V_AHTInterface"
- "T#,R"
- "T@\"NSBundle\",&,V_bundle"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N,V_bundleURL"
- "T@,&,N,V_cfBundle"
- "T@,W,N,V_mtDevice"
- "TI,R,N"
- "TI,R,N,V_maxFrameSize"
- "TQ,R"
- "T^?,N,V_createBinaryFilter"
- "T^{_MTBinaryFilter=^?^?^?},N,V_legacyFilter"
- "Vv16@0:8"
- "^?"
- "^?16@0:8"
- "^{_MTBinaryFilter=^?^?^?}"
- "^{_MTBinaryFilter=^?^?^?}16@0:8"
- "^{_NSZone=}16@0:8"
- "_AHTDevice"
- "_AHTInterface"
- "_bundle"
- "_bundleURL"
- "_cfBundle"
- "_createBinaryFilter"
- "_legacyFilter"
- "_maxFrameSize"
- "_mtDevice"
- "addObject:"
- "allDevices"
- "allInterfaces"
- "autorelease"
- "bundle"
- "bundleURL"
- "cfBundle"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "classNamed:"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createBinaryFilter"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "filterFrame:size:maxSize:extraFrame:"
- "getBootLoader"
- "getDeviceInServiceTree:"
- "getInterfaceInServiceTree:"
- "getProperty:property:options:error:"
- "hash"
- "init"
- "initFileURLWithPath:isDirectory:"
- "initFromURL:device:"
- "initWithInfo:"
- "initWithInfo:getProperty:"
- "initWithPath:"
- "initWithString:relativeToURL:"
- "initWithURL:"
- "intValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "legacyFilter"
- "length"
- "load"
- "localizedDescription"
- "maxFrameSize"
- "mtDevice"
- "mutableCopy"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "objectForInfoDictionaryKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "principalClass"
- "registryID"
- "release"
- "reset"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAHTDevice:"
- "setAHTInterface:"
- "setBundle:"
- "setBundleURL:"
- "setCfBundle:"
- "setCreateBinaryFilter:"
- "setLegacyFilter:"
- "setMtDevice:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setProperty:withValue:"
- "sharedInstance"
- "stringWithFormat:"
- "superclass"
- "v16@0:8"
- "v24@0:8#16"
- "v24@0:8@16"
- "v24@0:8^?16"
- "v24@0:8^{_MTBinaryFilter=^?^?^?}16"
- "v32@0:8@\"NSString\"16@24"
- "v32@0:8@16@24"
- "v48@0:8^*16^I24^I32@?40"
- "v48@0:8^*16^I24^I32@?<v@?*II>40"
- "zone"

```
