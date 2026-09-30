## CoreGEM.dylib

> `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`

```diff

-10.0.3.0.0
-  __TEXT.__text: 0xdb4ec
+10.0.4.0.0
+  __TEXT.__text: 0xdb514
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xade0
+  __TEXT.__const: 0xadf0
   __TEXT.__gcc_except_tab: 0x39d4
   __TEXT.__cstring: 0x5e28
-  __TEXT.__oslogstring: 0x7dac
+  __TEXT.__oslogstring: 0x7e14
   __TEXT.__unwind_info: 0x3c28
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0xd4
CStrings:
+ "#gpsd,#supl,#out, Lat,%{sensitive}.6f,Long,%{sensitive}.6f,Alt,%{sensitive}.2f,SemMaj,%{private}.f,SemMin,%{private}.f,UncAlt,%{private}.f,PosMethod,%u,Status,%u,SessionId,%u,endCause,%u,HACC,%f,ephProvided,%c,refTimeProvided,%c,refLocProvided,%c"
+ "#gpsd,#supl,#out,posReport,sessionId,%u,posProtocol,%u,gpsWeek,%u,gpsTow,%u,gpsTimeUncertainty,%u,gpsTODPresent,%d,gpsTODMsec,%u,gpsTODFrac,%u,gpsTODUnc,%u,shapeType,%{private}u,latitude,%{sensitive}u,longitude,%{sensitive}u,Majoraxis,%{private}u,Minoraxis,%{private}u,altitude,%{sensitive}u,uncertainAltitude,%{private}u,confidence,%u,orientationAngle,%{private}u,technologySource,%u"
+ "#gpsd,#supl,#posp,#pdu,%{sensitive}zu,of,%{sensitive}zu,%{sensitive}s"
+ "#gpsd,#supl,#process,sendSuplStatusReport, RefLocLat,%{sensitive}.7lf,Long,%{sensitive}.7lf,Alt,%{sensitive}.2lf,HorUnc,%{private}.f,VerUnc,%{private}.f,conf,%{private}.d"
+ "#gpsd,#supl,#process,sendSuplStatusReport,Lat,%{sensitive}.7f,Long,%{sensitive}.7f,Alt,%{sensitive}.2f,SemMaj,%{private}.f,SemMin,%{private}.f,UncAlt,%{private}.f,PosMethod,%u,Status,%u,SessionId,%u,endCause,%u,HACC,%f,ephProvided,%c,refTimeProvided,%c,refLocProvided,%c"
+ "#heloFix,%s,lat,%{sensitive}.8f,lon,%{sensitive}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,alt,%{sensitive}.2f,vunc,%{private}.2f,vrel,%{private}s"
+ "#heloInputFix,%s,%s,ts,%llu,lat,%{sensitive}.8f,lon,%{sensitive}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,alt,%{sensitive}.2f,vunc,%{private}.2f,vrel,%{private}s"
+ "#heloOutputFix,%s,xy.source,%s,xy.ts,%llu,lat,%{sensitive}.8f,lon,%{sensitive}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,z.source,%{private}s,z.ts,%llu,alt,%{sensitive}.2f,vunc,%{private}.2f,vrel,%{private}s,week,%{private}u,tow,%{private}u"
+ "#input,#nilr,handleDeviceIndication, lat,%{sensitive}.6f,lon,%{sensitive}.6f,alt,%{sensitive}.2f,semiMajor,%{private}.2f,semiMinor,%{private}.2f,vertUncert,%{private}.2f"
+ "#input,#nilr,injectAssistancePosition,received tightly coupling pos,lat,%{sensitive}.4f,lon,%{sensitive}.4f,alt,%{sensitive}.4f,type,%{public}d,altValid,%{public}d,vertUncM,%{public}.1f,semiMajUncM,%{public}.1f,semiMinUncM,%{public}.1f,source,%{public}d,reliability,%{public}d,delayMachMs,%{public}.2f,"
+ "#input,#nilr,injectReflocationToGnssDevice refLat,%{sensitive}u,refLon,%{sensitive}u,refAlt,%{sensitive}u,conf,%{private}u,semiMajor,%{private}f,semiMinor,%{private}f,altUncertainty,%f"
+ "#input,#nilr,injectReflocationToGnssDevice,refLat,%{sensitive}u,refLon,%{sensitive}u,original uncertainties, %{private}f,semiMinor,%{private}f,%{private}u"
+ "#lpp,#pdu,%{sensitive}zu,of,%{sensitive}zu,%{sensitive}s"
+ "#process,#nilr,handleDeviceIndication,#nilr,get the latest altitude, alt,%{sensitive}.2f,vunc,%{private}.2f"
+ "#process,#nilr,handleDeviceIndication,fix in emergency mode, lat,%{sensitive}.6f,lon,%{sensitive}.6f,alt,%{sensitive}.2f,"
+ "#supl,#pdu,%{sensitive}zu,of,%{sensitive}zu,%{sensitive}s,%{sensitive}s"
+ "/AppleInternal/Library/BuildRoots/7d2a62ca-bb83-11ef-9317-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "SessionHandler,#out,posReport,result,%u,sessionId,%u,posProtocol,%u,gpsWeek,%u,gpsTow,%u,gpsTimeUncertainty,%u,gpsTODPresent,%d,gpsTODMsec,%u,gpsTODFrac,%u,gpsTODUnc,%u,shapeType,%u,latitude,%{sensitive}u,longitude,%{sensitive}u,Major axis,%{private}u,Minor axis,%{private}u,altitude,%{sensitive}u,uncertainAltitude,%{private}u,confidence,%{private}u,orientationAngle,%u,velocityType,%u,technologySource,%u,fixType,%u"
+ "v_ShapeType,%{private}u,v_SignOfLat,%{private}u,v_Latitude,%{sensitive}u,v_Longitude,%{sensitive}u,v_Altitude,%{sensitive}u,v_UncertSemiMajor,%{private}u,v_UncertSemiMinor,%{private}u,v_AxisBearing,%{private}u,v_DirectOfAlt,%{private}u,v_UncertAltitude,%{private}u,v_Confidence,%{private}u"
- "#gpsd,#supl,#out, Lat,%{private}.6f,Long,%{private}.6f,Alt,%{private}.2f,SemMaj,%{private}.f,SemMin,%{private}.f,UncAlt,%{private}.f,PosMethod,%u,Status,%u,SessionId,%u,endCause,%u,HACC,%f,ephProvided,%c,refTimeProvided,%c,refLocProvided,%c"
- "#gpsd,#supl,#out,posReport,sessionId,%u,posProtocol,%u,gpsWeek,%u,gpsTow,%u,gpsTimeUncertainty,%u,gpsTODPresent,%d,gpsTODMsec,%u,gpsTODFrac,%u,gpsTODUnc,%u,shapeType,%{private}u,latitude,%{private}u,longitude,%{private}u,Majoraxis,%{private}u,Minoraxis,%{private}u,altitude,%{private}u,uncertainAltitude,%{private}u,confidence,%u,orientationAngle,%{private}u,technologySource,%u"
- "#gpsd,#supl,#posp,#pdu,%{private}zu,of,%{private}zu,%{private}s"
- "#gpsd,#supl,#process,sendSuplStatusReport, RefLocLat,%{private}.7lf,Long,%{private}.7lf,Alt,%{private}.2lf,HorUnc,%{private}.f,VerUnc,%{private}.f,conf,%{private}.d"
- "#gpsd,#supl,#process,sendSuplStatusReport,Lat,%{private}.7f,Long,%{private}.7f,Alt,%{private}.2f,SemMaj,%{private}.f,SemMin,%{private}.f,UncAlt,%{private}.f,PosMethod,%u,Status,%u,SessionId,%u,endCause,%u,HACC,%f,ephProvided,%c,refTimeProvided,%c,refLocProvided,%c"
- "#heloFix,%s,lat,%{private}.8f,lon,%{private}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,alt,%{private}.2f,vunc,%{private}.2f,vrel,%{private}s"
- "#heloInputFix,%s,%s,ts,%llu,lat,%{private}.8f,lon,%{private}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,alt,%{private}.2f,vunc,%{private}.2f,vrel,%{private}s"
- "#heloOutputFix,%s,xy.source,%s,xy.ts,%llu,lat,%{private}.8f,lon,%{private}.8f,hunc,%{private}.2f,smj,%{private}.2f,smn,%{private}.2f,hrel,%{private}s,z.source,%{private}s,z.ts,%llu,alt,%{private}.2f,vunc,%{private}.2f,vrel,%{private}s,week,%{private}u,tow,%{private}u"
- "#input,#nilr,handleDeviceIndication, lat,%{private}.6f,lon,%{private}.6f,alt,%{private}.2f,semiMajor,%{private}.2f,semiMinor,%{private}.2f,vertUncert,%{private}.2f"
- "#input,#nilr,injectAssistancePosition,received tightly coupling pos,lat,%{private}.4f,lon,%{private}.4f,alt,%{private}.4f,type,%{public}d,altValid,%{public}d,vertUncM,%{public}.1f,semiMajUncM,%{public}.1f,semiMinUncM,%{public}.1f,source,%{public}d,reliability,%{public}d,delayMachMs,%{public}.2f,"
- "#input,#nilr,injectReflocationToGnssDevice refLat,%{private}u,refLon,%{private}u,refAlt,%{private}u,conf,%{private}u,semiMajor,%{private}f,semiMinor,%{private}f,altUncertainty,%f"
- "#input,#nilr,injectReflocationToGnssDevice,refLat,%{private}u,refLon,%{private}u,original uncertainties, %{private}f,semiMinor,%{private}f,%{private}u"
- "#lpp,#pdu,%{private}zu,of,%{private}zu,%{private}s"
- "#process,#nilr,handleDeviceIndication,#nilr,get the latest altitude, alt,%{private}.2f,vunc,%{private}.2f"
- "#process,#nilr,handleDeviceIndication,fix in emergency mode, lat,%{private}.6f,lon,%{private}.6f,alt,%{private}.2f,"
- "#supl,#pdu,%{private}zu,of,%{private}zu,%{private}s,%{private}s"
- "/AppleInternal/Library/BuildRoots/602d817d-b298-11ef-8387-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "SessionHandler,#out,posReport,result,%u,sessionId,%u,posProtocol,%u,gpsWeek,%u,gpsTow,%u,gpsTimeUncertainty,%u,gpsTODPresent,%d,gpsTODMsec,%u,gpsTODFrac,%u,gpsTODUnc,%u,shapeType,%u,latitude,%{private}u,longitude,%{private}u,Major axis,%{private}u,Minor axis,%{private}u,altitude,%{private}u,uncertainAltitude,%{private}u,confidence,%{private}u,orientationAngle,%u,velocityType,%u,technologySource,%u,fixType,%u"
- "v_ShapeType,%{private}u,v_SignOfLat,%{private}u,v_Latitude,%{private}u,v_Longitude,%{private}u,v_Altitude,%{private}u,v_UncertSemiMajor,%{private}u,v_UncertSemiMinor,%{private}u,v_AxisBearing,%{private}u,v_DirectOfAlt,%{private}u,v_UncertAltitude,%{private}u,v_Confidence,%{private}u"

```
