## gpsd

> `/usr/libexec/gpsd`

```diff

 293.0.2.0.0
-  __TEXT.__text: 0xda990
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_stubs: 0x5a0
+  __TEXT.__text: 0xdd8ac
+  __TEXT.__auth_stubs: 0x1640
+  __TEXT.__objc_stubs: 0x600
   __TEXT.__init_offsets: 0x24
-  __TEXT.__const: 0x8051
-  __TEXT.__oslogstring: 0x99c4
-  __TEXT.__cstring: 0x6ae8
-  __TEXT.__gcc_except_tab: 0x453c
+  __TEXT.__const: 0x8681
+  __TEXT.__oslogstring: 0xa12a
+  __TEXT.__cstring: 0x6dea
+  __TEXT.__gcc_except_tab: 0x46c4
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x3e4
-  __TEXT.__unwind_info: 0x38a0
-  __DATA_CONST.__auth_got: 0xb00
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0xa9a8
-  __DATA_CONST.__cfstring: 0xe00
+  __TEXT.__objc_methname: 0x424
+  __TEXT.__unwind_info: 0x3980
+  __DATA_CONST.__auth_got: 0xb30
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0xae10
+  __DATA_CONST.__cfstring: 0xec0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_selrefs: 0x188
   __DATA.__data: 0x48
   __DATA.__common: 0x261
   __DATA.__bss: 0x670

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 4074
-  Symbols:   442
-  CStrings:  1728
+  Functions: 4160
+  Symbols:   460
+  CStrings:  1792
 
Symbols:
+ _TelephonyBasebandPCITransportDeregisterTimeEvent
+ _TelephonyBasebandPCITransportRegisterTimeEvent
+ __ZN3abm15kKeyTraceActionE
+ __ZN3abm19kKeyTimestampStringE
+ __ZN3abm21kKeyBasebandBootStateE
+ __ZN3abm21kKeyBasebandResetTypeE
+ __ZN3abm23kKeyBasebandResetReasonE
+ __ZN3abm24kKeyBasebandResetSubTypeE
+ __ZN3abm25kEventTraceDumpStateBeginE
+ __ZN3abm26kBasebandBootStateDidResetE
+ __ZN3abm27kBasebandBootStateWillResetE
+ __ZN3abm29kEventBasebandBootStateChangeE
+ __ZN3abm33kCollectTelephonyLogsWithCoredumpE
+ __ZN3abm44kKeyTraceDumpStateMobileBasebandServicesPathE
+ __ZN3abm6client13CreateManagerERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEP16dispatch_queue_s
+ __ZN3abm6client20RegisterEventHandlerENSt3__110shared_ptrINS0_7ManagerEEERKNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEU13block_pointerFvPvP16dispatch_group_sE
+ __ZN3abm6client8EventsOnENSt3__110shared_ptrINS0_7ManagerEEE
+ _strcasecmp
CStrings:
+ "#bbReset,extensionsIndus,%{public}d,%{private}s"
+ "#gdm,decodeCoexConfig,coexConfigPostOverride,0x%{public}llx,coexConfigDefault,0x%{public}llx,isCLOverride,%s,coexConfigCLOverride,0x%{public}llx"
+ "#gpsdAbm, Abm Manager Created, Notifications registered"
+ "#gpsdAbm, DumpStateMobileBasebandServicesPath is null"
+ "#gpsdAbm, EventBasebandBootStateChange received"
+ "#gpsdAbm, EventTraceDumpStateBegin received"
+ "#gpsdAbm, dumpLogsCallback not registered"
+ "#gpsdAbm, gpsdLogPath for coredump,%{public}s"
+ "#gpsdAbm,BBBootStateChange, BootState,%{public}s"
+ "#gpsdAbm,BBBootStateChange, BootState,%{public}s, ResetType,%{public}s, ResetSubType,%{public}s, ResetReason,%{private}s"
+ "#gpsdAbm,EventBasebandBootStateChange, BasebandBootState not provided"
+ "#gpsdAbm,EventTraceDumpStateBegin, DumpStateMobileBasebandServicesPath,%{public}s"
+ "#gpsdAbm,EventTraceDumpStateBegin, timestamp,%{public}s"
+ "#gpsdAbm,EventTraceDumpStateBegin, traceAction,%{public}s"
+ "#gpsdAbm,abmManager,null,com.apple.gpsd.Abm"
+ "#gpsdAbm,ctor begin"
+ "#gpsdAbm,nullattr,%{public}s"
+ "#gpsdAbm,queue,null,%{public}s"
+ "#isbsr,answer,%{public}d"
+ "#isbsr,null"
+ "#pcie,#tt,completion success"
+ "-gpsd"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/Sources/CoreGPS/Sources/Daemon/GpsdAbmUtil.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreGPS/Sources/Daemon/GpsdPlatformInfo.mm"
+ "/usr/lib/libindus.dylib"
+ "13:59:25"
+ "CREnableCoexBlanking2G"
+ "CREnableCoexBlankingNR"
+ "CREnableCoexEnhancedAssistance"
+ "CREnableCoexLTEB13"
+ "CREnableCoexLTEB14"
+ "CREnableSTWMitigation"
+ "Feb 21 2025"
+ "Feb 21 2025 13:52:45"
+ "GpsdAbmUtil"
+ "GpsdAbmUtil.cpp"
+ "GpsdPlatformInfo,conflicting vendor libs"
+ "GpsdPlatformInfo.mm"
+ "No"
+ "VendorLogger,copyFile,error:%{public}s"
+ "VendorLogger,copyLatestLogsToPath, Copied,%d, RequestedMax,%d"
+ "VendorLogger,copyLatestLogsToPath, copied %{public}s"
+ "VendorLogger,copyLatestLogsToPath, failed src,%{public}s, dest,%{public}s"
+ "VendorLogger,copyLatestLogsToPath, null destination dirpath, cannot copy latest logs"
+ "VendorLogger,copyLatestLogsToPath, null source dirpath, cannot copy latest logs"
+ "VendorLogger,copyLatestLogsToPath, skipped file,%{public}s"
+ "VendorLogger,copyLatestLogsToPath,chmod failed,%{public}d"
+ "VendorLogger,copyLatestLogsToPath,could not create directory,%{public}s, error,%{public}d"
+ "VendorLogger,copyLatestLogsToPath,created directory,%{public}s,permissions,%x"
+ "VendorLogger,copyLatestLogsToPath,directory exists,permissions,%x"
+ "Yes"
+ "checkVendorLibs"
+ "com.apple.gpsd.Abm"
+ "com.apple.gpsd.AbmQueue"
+ "copyItemAtPath:toPath:error:"
+ "false && \"#gpsdAbm,abmManager,null,com.apple.gpsd.Abm\""
+ "false && \"#gpsdAbm,queue,null,%{public}s\""
+ "false && \"GpsdPlatformInfo,conflicting vendor libs\""
+ "localizedDescription"
+ "log-bb-"
+ "no-timestamp"
+ "not-provided"
+ "objectForKey:"
+ "v24@?0^v8^{dispatch_group_s=}16"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "04:37:14"
- "Feb 16 2025"
- "Feb 16 2025 04:32:08"

```
