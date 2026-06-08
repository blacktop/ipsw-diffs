## CoreGEM.dylib

> `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0xf3e64
-  __TEXT.__auth_stubs: 0xaf0
+36.0.0.0.0
+  __TEXT.__text: 0xf8248
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xb808
-  __TEXT.__gcc_except_tab: 0x46c8
-  __TEXT.__cstring: 0x7096
-  __TEXT.__oslogstring: 0x91de
-  __TEXT.__unwind_info: 0x40c0
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0xc6
-  __TEXT.__objc_methtype: 0x34
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x49678
+  __TEXT.__const: 0xbac4
+  __TEXT.__gcc_except_tab: 0x4424
+  __TEXT.__cstring: 0x7020
+  __TEXT.__oslogstring: 0x92a5
+  __TEXT.__unwind_info: 0x44a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x49588
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x588
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x9150
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__weak_auth_got: 0x38
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x10
-  __DATA.__common: 0x1061
+  __DATA.__common: 0x1069
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0xa00
+  __DATA_DIRTY.__bss: 0x9f8
   __DATA_DIRTY.__common: 0x580
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: B83B4697-E8F4-3DD7-B6C8-623C72000F93
-  Functions: 4096
-  Symbols:   227
-  CStrings:  1441
+  UUID: 0C5F674F-5688-37C0-AC3E-71FBF783DB23
+  Functions: 4111
+  Symbols:   226
+  CStrings:  1416
 
Symbols:
- _memchr
CStrings:
+ "#gem,#lpp,#%s,startPosRequest"
+ "#gem,handleEmergencyNilrAssistanceNeededReport,Failed to parse gem request"
+ "#gem,handleEmergencyNilrAssistanceNeededReport,assistance req missing"
+ "#gpsd,#%s,#posp calling injectNavModel"
+ "#gpsd,#%s,#posp calling injectRefLocation"
+ "#gpsd,#%s,#posp calling injectRefTime"
+ "#gpsd,#%s,#posp calling startPosRequest"
+ "#gpsd,#supl,#posp gpsTow,%u,GpsTowUncK,%u,GpsWeek,%u,GpsWeekCycleNumber,%u,NumTowAssist,%u"
+ "#nilr,sendRefTimeIndicationToCl, indication to CL, gpsTow=%u,gpsWeek=%u,gpsWeekCycleNumber=%u"
+ "/AppleInternal/Library/BuildRoots/4~CQCjugCIg0sAh5QSo8Ounc6nJX8_Rq2q7HfEXb8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "cplane"
+ "file,%s,line,%d"
+ "file,%s,line,%d,Code,%u"
+ "file,%s,line,%d,ErrCode,%u"
+ "handleEmergencyNilrAssistanceNeededReport"
+ "handleEmergencyNilrAssistanceNeededReport, aid request not supported"
+ "handleEmergencyNilrAssistanceNeededReport,sessionId,%d,aidMask,%d"
+ "supl"
- "#gem,#lpp,#cplane,startPosRequest"
- "#gpsd #supl gnssOsa_Calloc allocation failed Size,%lu,Fn,%s,Line,%d"
- "#gpsd,#cplane,#posp calling injectNavModel"
- "#gpsd,#cplane,#posp calling injectRefLocation"
- "#gpsd,#cplane,#posp calling injectRefTime"
- "#gpsd,#cplane,#posp calling startPosRequest"
- "#gpsd,#supl,#posp calling injectNavModel"
- "#gpsd,#supl,#posp calling injectRefLocation"
- "#gpsd,#supl,#posp calling injectRefTime"
- "#gpsd,#supl,#posp calling startPosRequest"
- "#gpsd,#supl,#posp gpsTow,%u,GpsTowUncK,%u,GpsWeek,%u,,NumTowAssist,%u"
- "#nilr,sendRefTimeIndicationToCl, indication to CL"
- "/AppleInternal/Library/BuildRoots/4~CNpuugBPkmxM8uWWI6pXQLFOKJ-nuZ3TaFTZrkQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "@40@0:8@?16@?24@32"
- "Cell"
- "CoreGnssEmergencyManager"
- "Gnss"
- "High"
- "Invalid"
- "LPP_IDLE"
- "Low"
- "Medium"
- "NotSet"
- "SendSuplMsgStatus"
- "Size,%lu,Fn,%s,Line,%d"
- "VeryLow"
- "Wifi"
- "\\/"
- "agpsmacosa.cpp"
- "dealloc"
- "getBytes:length:"
- "gnssOsa_Calloc"
- "handleDeviceIndication:"
- "handleRemoteRequest:machconttimens:"
- "init"
- "initForComm:sendIndicationToRemoteCallback:dispatch_queue_t:"
- "initWithBytes:length:"
- "length"
- "notset"
- "stringWithFormat:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16Q24"

```
