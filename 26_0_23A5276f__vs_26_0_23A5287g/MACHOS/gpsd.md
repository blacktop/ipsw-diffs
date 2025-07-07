## gpsd

> `/usr/libexec/gpsd`

```diff

-326.0.2.0.0
-  __TEXT.__text: 0x136974
+326.0.3.0.0
+  __TEXT.__text: 0x136ce4
   __TEXT.__auth_stubs: 0x1cc0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__init_offsets: 0x28
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__gcc_except_tab: 0x78d4
-  __TEXT.__const: 0xd1b8
+  __TEXT.__gcc_except_tab: 0x7900
+  __TEXT.__const: 0xd168
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2a8
   __TEXT.__swift5_typeref: 0x193
   __TEXT.__swift5_reflstr: 0x9c
   __TEXT.__swift5_fieldmd: 0x130
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0xcceb
+  __TEXT.__oslogstring: 0xd2b1
   __TEXT.__objc_methname: 0x6b3
   __TEXT.__swift5_types: 0x24
   __TEXT.__cstring: 0x88e8

   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methtype: 0xe9
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x69a8
+  __TEXT.__unwind_info: 0x6a00
   __TEXT.__eh_frame: 0x6b8
   __DATA_CONST.__auth_got: 0xe78
   __DATA_CONST.__got: 0x308

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 85C51FCA-BF72-3A87-AA40-7443BFA0BCFC
-  Functions: 8411
-  Symbols:   50376
-  CStrings:  2322
+  UUID: 43B2300E-3F33-33C9-A36E-08D5ABEA0FFA
+  Functions: 8412
+  Symbols:   50382
+  CStrings:  2324
 
Symbols:
+ __Z11getNmeaTypeRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERm
+ __ZN18GpsdSessionMonitor16setExplicitStateEb
- __Z11getNmeaTypeRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
CStrings:
+ "#comm,configure,IOSSIOSPEED,%{public}lu,standardSpeed,%{public}lu"
+ "#comm,open,%{public}s,flag,0x%{public}X"
+ "#gdm,#bps,createDevice failure,%{public}d"
+ "#gdm,Device remote interface version,%{public}d"
+ "#gdm,INJECT_ASSISTANCE_FILE,Injecting Assistance file,size,%{public}zu"
+ "#gdm,INJECT_RTI_FILE,Injecting RTI file,size,%{public}zu"
+ "#gdm,configureDevice,enabled PVTM,pvt,%{public}d,meas,%{public}d,extmeas,%{public}d,svinfo,%{public}d,rxcorr,%{public}d,timeinfo,%{public}d"
+ "#gdm,configureDevice,setConfigEnableGnssConstellations,0x%{public}x,succeeded"
+ "#gdm,decodeCoexConfig,coexConfigPostOverride,0x%{public}llx,coexConfigDefault,0x%{public}llx,isCLOverride,%{public}s,coexConfigCLOverride,0x%{public}llx"
+ "#gdm,destroyDevice,fDevice,%{public}p,fDeviceCtrAttempted,%{public}d,fDeviceCtrStatus,%{public}s,regSession,%{public}d,emergSession,%{public}d"
+ "#gdm,getNonAsicPowerAdder,base,%{public}.1f,osc,%{public}.1f,l1_lna,%{public}.1f,l5_lna,%{public}.1f"
+ "#gdm,powerReportCallback,adding non-asic power for platform, %{public}.1f"
+ "#gdm,pvtmCallback,hasFix,%{public}d,nMeas,%{public}d,nSvInfo,%{public}d,nBand,%{public}d,hasTimeInfo,%{public}d,hasKlob,%{public}d"
+ "#gdm,receivedRequest,%{public}s"
+ "#gdm,sendResponse,%{public}s,%{public}s"
+ "#gnssseeding,SAVING_ASSISTANCE_FILE,invalid file path,%{public}d"
+ "#gnssseeding,SAVING_ASSISTANCE_FILE,saving uncompressed assistance file,size,%{public}zu"
+ "#gnssseeding,Saving RTI file,size,%{public}zu"
+ "#gnssseeding,createAssistanceFileProto,file,%{public}s,doesn't exist"
+ "#gnssseeding,createAssistanceFileProto,requestType,%{public}s"
+ "#gnssseeding,handleRequest,invalid request type,%{public}d"
+ "#gpsdUtil,CC_SHA256 failed on,%{public}p,%{public}zu"
+ "#gpsdUtil,Tick to ns info,Numerator,%{public}llu,Denominator,%{public}llu,PrecisionReductionBits,%{public}d"
+ "#imag,fix is in week 0 with low uncertainty,%{public}f,%{public}f"
+ "#imag,set build week,%{public}d"
+ "#rxClockConv,out of range pulse unc,%{public}.9f,%{public}lu,%{public}lu"
+ "#rxClockConv,pulse,rxRtcMs,%{public}llu,rxRtcUnc,%{public}u,machAbsTicks,%{public}llu,%{public}llu,gpsNs,%{public}llu,gpsUncNs,%{public}.3f"
+ "#spi,hal,write,size,%{public}zu,duration,us,%{public}.1f"
+ "#tt,onCompleted,%{public}d"
+ "#tt,sendTimeTransferDataIndication,fromGpioSet,%{public}d,fromGnssVendorSet,%{public}d"
+ "#version,CoreGPS-326.0.3,machContSec,%{public}.3f,BuildTime,{Jun 26 2025,03:52:22}"
+ "%{public}c,NMEA:%{public}s%{private}s"
+ "%{public}c,NMEA:%{public}s%{public}s"
+ "%{public}c,NMEA:%{public}s%{sensitive}s"
+ "%{public}s,%{public}zu,%{public}zu,%{private}s"
+ "/AppleInternal/Library/BuildRoots/4~B37jugCFX2ohDyXSK25xkm2PvNnJ5xJjpd-FZf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "GpsdPerformanceSummary,timer interval,%{public}.2f"
+ "GpsdPlatformInfo,getNoiseFigure,band,%{public}d"
+ "GpsdPlatformInfo,hardware,%{public}d"
+ "GpsdSessionMonitor,setExplicitState,current,%{public}d,new,%{public}d"
+ "HalExtensions,getGpsCrossCorrelationMaxThreshold_dBHz,%{public}f"
+ "HalExtensions,getGpsCrossCorrelationMinThreshold_dBHz,%{public}f"
+ "Jun 26 2025 03:52:19"
+ "MlbSn,%{private}s"
+ "MlbSn,bornOnGpsWeek,%{public}d"
+ "MlbSn,dom,%{public}s,%{public}d"
+ "MlbSn,dom,bornOnGpsWeek,%{public}d"
+ "MlbSn,dom,unexpectedCh,%{public}c"
+ "MlbSn,dom,weekOutOfRange,mlb,%{public}d,earliest,%{public}d"
+ "MlbSn,invalid,ww,%{public}d"
+ "MlbSn,parse,%{private}s,sz,%{public}zu"
+ "MlbSn,sz,%{public}zu,yww,%{public}d"
+ "MlbSn,unexpectedSize,%{public}zu"
+ "MlbSn,weekOutOfRange,mlb,%{public}d"
+ "NvStore,Did not find dedicated file for NamedType,%{public}d,Converting to id,%{public}lld"
+ "NvStore,Failed to read from primary and backup files for,%{public}s, using an empty cache"
+ "NvStore,Needed to read from backup file, %{public}s, is corrupt"
+ "NvStore,clear,mach_cont_s,%{public}.3f,id,%{public}d"
+ "NvStore,clearNamed,mach_cont_s,%{public}.3f,id,%{public}d"
+ "NvStore,clearPermanent,mach_cont_s,%{public}.3f"
+ "NvStore,clearSession,mach_cont_s,%{public}.3f"
+ "NvStore,printState,begin,%{public}s"
+ "NvStore,printState,currentSize,%{public}lld,filePath,%{public}s"
+ "NvStore,printState,end,%{public}s"
+ "NvStore,printState,id,%{public}lld,size,%{public}zu,hash,%{public}x,createAgeSeconds,%{public}.1f,modAgeSeconds,%{public}.1f,modCount,%{public}lld"
+ "NvStore,readCacheFromFile,Could not open file,%{public}s"
+ "NvStore,readCacheFromFile,Could not parse message from file,%{public}s,parsed_ver,%{public}d,parsed_items_size,%{public}d"
+ "NvStore,readCacheFromFile,Empty file,%{public}s"
+ "NvStore,readCacheFromFile,filePath,%{public}s,size,%{public}d"
+ "NvStore,readCacheFromFile,numItems,%{public}d,totalSize,%{public}lld"
+ "NvStore,recall,mach_cont_s,%{public}.3f,id,%{public}d,size,%{public}zu,hash,%{public}x"
+ "NvStore,store,mach_cont_s,%{public}.3f,id,%{public}d,size,%{public}zu,hash,%{public}x"
+ "NvStore,storeNamed,mach_cont_s,%{public}.3f,id,%{public}d,size,%{public}zu,hash,%{public}x"
+ "NvStore,storeReturn,%{public}d"
+ "NvStore,storeToProtobuf,source_size,%{public}zu,dest_size,%{public}zu,hash,%{public}x,count,%{public}lld"
+ "NvStore: Clearing NamedType=%{public}d from dedicated file %{public}s"
+ "NvStore: Did not find dedicated file for NamedType=%{public}d, converting it to id=%{public}lld"
+ "NvStore: Reading NamedType=%{public}d from dedicated file %{public}s"
+ "PerfCpi,deltaNorth,%{public}.1f,deltaEast,%{public}.1f,deltaVert,%{public}.1f,deltaHorizNorm,%{public}.2f,deltaVertNorm,%{public}.2f,type,%{public}d"
+ "PerfDem,delta,%{public}.1f,deltaNorm,%{public}.2f"
+ "PerfWarning,spurious printSummary,%{public}.3f,%{public}.3f"
+ "Pref: %{public}@ = %{public}@"
+ "Pref: kNmeaMaskOverride = 0x%{public}llx"
+ "Pref: kPvtmTimeOut = %{public}d"
+ "Resource,user,%{public}.2f,sys,%{public}.2f,residentMB,%{public}.3f,footprintMB,%{public}.3f,interval,%{public}.2f"
+ "VendorLogger,closeLogFile,Archiving,Old name,%{public}s,New name,%{public}s"
+ "VendorLogger,closeLogFile,Could not archive,%{public}s"
+ "VendorLogger,copyLatestLogsToPath, Copied,%{public}d, RequestedMax,%{public}d"
+ "VendorLogger,copyLatestLogsToPath,created directory,%{public}s,permissions,%{public}x"
+ "VendorLogger,copyLatestLogsToPath,directory exists,permissions,%{public}x"
+ "VendorLogger,created directory,%{public}s,permissions,%{public}x"
+ "VendorLogger,directory exists,permissions,%{public}x"
+ "VendorLogger,flushCompression,after,%{public}p,%{public}zu,%{public}p,%{public}zu,status,%{public}d"
+ "VendorLogger,flushCompression,before,%{public}p,%{public}zu,%{public}p,%{public}zu"
+ "VendorLogger,flushCompression,flushed bytes,%{public}zu"
+ "VendorLogger,pruneLogFiles,deleted due to age,%{public}s,fileTime,%{public}ld,targetTime,%{public}ld"
+ "VendorLogger,pruneLogFiles,deleted due to num files,%{public}s,num files,%{public}d"
+ "VendorLogger,pruneLogFiles,deleted due to size,%{public}s"
+ "VendorLogger,pruneLogFiles,deleted due to zero size,%{public}s"
+ "VendorLogger,pruneLogFiles,looking at,%{public}s,modTime,%{public}ld,floorTime,%{public}ld,size,%{public}lld,new total,%{public}lld"
+ "debugFeaturesBitmask,0x%{public}llx"
+ "factoryTestJob,%{public}s"
+ "factoryTestXml,%{public}s"
+ "gpsd_plistpath: %{public}@ defaults %{public}@"
+ "readFileIntoVector,%{public}s,size,%{public}zu"
- "#comm,configure,IOSSIOSPEED,%lu,standardSpeed,%lu"
- "#comm,open,%s,flag,0x%{public}X"
- "#gdm,#bps,createDevice failure,%d"
- "#gdm,Device remote interface version,%d"
- "#gdm,INJECT_ASSISTANCE_FILE,Injecting Assistance file,size,%zu"
- "#gdm,INJECT_RTI_FILE,Injecting RTI file,size,%zu"
- "#gdm,configureDevice,enabled PVTM,pvt,%d,meas,%d,extmeas,%d,svinfo,%d,rxcorr,%d,timeinfo,%d"
- "#gdm,configureDevice,setConfigEnableGnssConstellations,0x%x,succeeded"
- "#gdm,decodeCoexConfig,coexConfigPostOverride,0x%{public}llx,coexConfigDefault,0x%{public}llx,isCLOverride,%s,coexConfigCLOverride,0x%{public}llx"
- "#gdm,destroyDevice,fDevice,%p,fDeviceCtrAttempted,%{public}d,fDeviceCtrStatus,%{public}s,regSession,%{public}d,emergSession,%{public}d"
- "#gdm,getNonAsicPowerAdder,base,%.1f,osc,%.1f,l1_lna,%.1f,l5_lna,%.1f"
- "#gdm,powerReportCallback,adding non-asic power for platform, %.1f"
- "#gdm,pvtmCallback,hasFix,%d,nMeas,%d,nSvInfo,%d,nBand,%d,hasTimeInfo,%d,hasKlob,%d"
- "#gdm,receivedRequest,%s"
- "#gdm,sendResponse,%s,%s"
- "#gnssseeding,SAVING_ASSISTANCE_FILE,invalid file path,%d"
- "#gnssseeding,SAVING_ASSISTANCE_FILE,saving uncompressed assistance file,size,%zu"
- "#gnssseeding,Saving RTI file,size,%zu"
- "#gnssseeding,createAssistanceFileProto,file,%s,doesn't exist"
- "#gnssseeding,createAssistanceFileProto,requestType,%s"
- "#gnssseeding,handleRequest,invalid request type,%d"
- "#gpsdUtil,CC_SHA256 failed on,%p,%zu"
- "#gpsdUtil,Tick to ns info,Numerator,%llu,Denominator,%llu,PrecisionReductionBits,%d"
- "#imag,fix is in week 0 with low uncertainty,%f,%f"
- "#imag,set build week,%d"
- "#rxClockConv,out of range pulse unc,%{public}.9f,%lu,%lu"
- "#rxClockConv,pulse,rxRtcMs,%{public}llu,rxRtcUnc,%{public}u,machAbsTicks,%{public}llu,%{public}llu,gpsNs,%llu,gpsUncNs,%{public}.3f"
- "#spi,hal,write,size,%zu,duration,us,%.1f"
- "#tt,onCompleted,%d"
- "#tt,sendTimeTransferDataIndication,fromGpioSet,%d,fromGnssVendorSet,%d"
- "#version,CoreGPS-326.0.2,machContSec,%{public}.3f,BuildTime,{Jun 13 2025,05:56:20}"
- "%s,%zu,%zu,%s"
- "%{public}c,NMEA:%{public}s"
- "%{public}c,NMEA:%{sensitive}s"
- "/AppleInternal/Library/BuildRoots/4~B2_BugAm1GzvXODY4Aja5x8PfgnMu26FfSBRIoc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "GpsdPerformanceSummary,timer interval,%.2f"
- "GpsdPlatformInfo,getNoiseFigure,band,%d"
- "GpsdPlatformInfo,hardware,%d"
- "HalExtensions,getGpsCrossCorrelationMaxThreshold_dBHz,%f"
- "HalExtensions,getGpsCrossCorrelationMinThreshold_dBHz,%f"
- "Jun 13 2025 05:56:17"
- "MlbSn,%s"
- "MlbSn,bornOnGpsWeek,%{private}d"
- "MlbSn,dom,%{private}s,%{private}d"
- "MlbSn,dom,bornOnGpsWeek,%{private}d"
- "MlbSn,dom,unexpectedCh,%{private}c"
- "MlbSn,dom,weekOutOfRange,mlb,%{private}d,earliest,%{public}d"
- "MlbSn,invalid,ww,%{private}d"
- "MlbSn,parse,%{private}s,sz,%{private}zu"
- "MlbSn,sz,%{private}zu,yww,%{private}d"
- "MlbSn,unexpectedSize,%{private}zu"
- "MlbSn,weekOutOfRange,mlb,%{private}d"
- "NvStore,Did not find dedicated file for NamedType,%d,Converting to id,%lld"
- "NvStore,Failed to read from primary and backup files for,%s, using an empty cache"
- "NvStore,Needed to read from backup file, %s, is corrupt"
- "NvStore,clear,mach_cont_s,%.3f,id,%d"
- "NvStore,clearNamed,mach_cont_s,%.3f,id,%d"
- "NvStore,clearPermanent,mach_cont_s,%.3f"
- "NvStore,clearSession,mach_cont_s,%.3f"
- "NvStore,printState,begin,%s"
- "NvStore,printState,currentSize,%lld,filePath,%s"
- "NvStore,printState,end,%s"
- "NvStore,printState,id,%lld,size,%zu,hash,%x,createAgeSeconds,%.1f,modAgeSeconds,%.1f,modCount,%lld"
- "NvStore,readCacheFromFile,Could not open file,%s"
- "NvStore,readCacheFromFile,Could not parse message from file,%s,parsed_ver,%d,parsed_items_size,%d"
- "NvStore,readCacheFromFile,Empty file,%s"
- "NvStore,readCacheFromFile,filePath,%s,size,%{public}d"
- "NvStore,readCacheFromFile,numItems,%d,totalSize,%lld"
- "NvStore,recall,mach_cont_s,%.3f,id,%d,size,%zu,hash,%x"
- "NvStore,store,mach_cont_s,%.3f,id,%d,size,%zu,hash,%x"
- "NvStore,storeNamed,mach_cont_s,%.3f,id,%d,size,%zu,hash,%x"
- "NvStore,storeReturn,%d"
- "NvStore,storeToProtobuf,source_size,%zu,dest_size,%zu,hash,%x,count,%lld"
- "NvStore: Clearing NamedType=%d from dedicated file %s"
- "NvStore: Did not find dedicated file for NamedType=%d, converting it to id=%lld"
- "NvStore: Reading NamedType=%d from dedicated file %s"
- "PerfCpi,deltaNorth,%.1f,deltaEast,%.1f,deltaVert,%.1f,deltaHorizNorm,%.2f,deltaVertNorm,%.2f,type,%d"
- "PerfDem,delta,%.1f,deltaNorm,%.2f"
- "PerfWarning,spurious printSummary,%.3f,%.3f"
- "Pref: %@ = %@"
- "Pref: kNmeaMaskOverride = 0x%llx"
- "Pref: kPvtmTimeOut = %d"
- "Resource,user,%.2f,sys,%.2f,residentMB,%.3f,footprintMB,%.3f,interval,%.2f"
- "VendorLogger,closeLogFile,Archiving,Old name,%s,New name,%s"
- "VendorLogger,closeLogFile,Could not archive,%s"
- "VendorLogger,copyLatestLogsToPath, Copied,%d, RequestedMax,%d"
- "VendorLogger,copyLatestLogsToPath,created directory,%{public}s,permissions,%x"
- "VendorLogger,copyLatestLogsToPath,directory exists,permissions,%x"
- "VendorLogger,created directory,%{public}s,permissions,%x"
- "VendorLogger,directory exists,permissions,%x"
- "VendorLogger,flushCompression,after,%p,%zu,%p,%zu,status,%d"
- "VendorLogger,flushCompression,before,%p,%zu,%p,%zu"
- "VendorLogger,flushCompression,flushed bytes,%zu"
- "VendorLogger,pruneLogFiles,deleted due to age,%s,fileTime,%ld,targetTime,%ld"
- "VendorLogger,pruneLogFiles,deleted due to num files,%s,num files,%d"
- "VendorLogger,pruneLogFiles,deleted due to size,%s"
- "VendorLogger,pruneLogFiles,deleted due to zero size,%s"
- "VendorLogger,pruneLogFiles,looking at,%s,modTime,%ld,floorTime,%ld,size,%lld,new total,%lld"
- "debugFeaturesBitmask,0x%llx"
- "factoryTestJob,%s"
- "factoryTestXml,%s"
- "gpsd_plistpath: %@ defaults %@"
- "readFileIntoVector,%s,size,%zu"

```
