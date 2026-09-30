## CoreGPSTest.dylib

> `/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`

```diff

-326.0.2.0.0
-  __TEXT.__text: 0xd4f74
+326.0.3.0.0
+  __TEXT.__text: 0xd5028
   __TEXT.__auth_stubs: 0x1240
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x5fb7
-  __TEXT.__gcc_except_tab: 0x46cc
+  __TEXT.__const: 0x5f97
+  __TEXT.__gcc_except_tab: 0x46d0
   __TEXT.__cstring: 0x6923
-  __TEXT.__oslogstring: 0x53cc
-  __TEXT.__unwind_info: 0x4890
+  __TEXT.__oslogstring: 0x5791
+  __TEXT.__unwind_info: 0x4898
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methname: 0x931
   __TEXT.__objc_methtype: 0xd76

   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  UUID: 5319721B-0A06-3FB4-84B0-E80CAC5CAAFE
-  Functions: 6028
-  Symbols:   10332
-  CStrings:  1565
+  UUID: C11B7840-7529-3094-903D-872192C5BBAB
+  Functions: 6029
+  Symbols:   10333
+  CStrings:  1566
 
Symbols:
+ __ZN18GpsdSessionMonitor16setExplicitStateEb
Functions:
+ __ZN18GpsdSessionMonitor16setExplicitStateEb
~ ____ZN12VendorLogger20copyLatestLogsToPathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEij_block_invoke : 1372 -> 1368
~ __ZNK15GpsdPreferences14getPvtmTimeOutEv : 192 -> 188
~ __ZNK15GpsdPreferences16nmeaMaskOverrideEv : 292 -> 288
~ __ZN14GpsFactoryTest23deviceInterfaceCallbackEN4gnss6ResultE : 392 -> 388
CStrings:
+ "#comm,configure,IOSSIOSPEED,%{public}lu,standardSpeed,%{public}lu"
+ "#comm,open,%{public}s,flag,0x%{public}X"
+ "#gdm,decodeCoexConfig,coexConfigPostOverride,0x%{public}llx,coexConfigDefault,0x%{public}llx,isCLOverride,%{public}s,coexConfigCLOverride,0x%{public}llx"
+ "#gpsdUtil,CC_SHA256 failed on,%{public}p,%{public}zu"
+ "#gpsdUtil,Tick to ns info,Numerator,%{public}llu,Denominator,%{public}llu,PrecisionReductionBits,%{public}d"
+ "#spi,hal,write,size,%{public}zu,duration,us,%{public}.1f"
+ "#version,CoreGPS-326.0.3,machContSec,%{public}.3f,BuildTime,{Jun 26 2025,03:52:22}"
+ "%{public}s,%{public}zu,%{public}zu,%{private}s"
+ "/AppleInternal/Library/BuildRoots/4~B37jugCFX2ohDyXSK25xkm2PvNnJ5xJjpd-FZf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
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
+ "Pref: %{public}@ = %{public}@"
+ "Pref: kNmeaMaskOverride = 0x%{public}llx"
+ "Pref: kPvtmTimeOut = %{public}d"
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
+ "deviceInterfaceCallback,results,current:%{public}s,new:%{public}s"
+ "factoryTestJob,%{public}s"
+ "factoryTestXml,%{public}s"
+ "gpsd_plistpath: %{public}@ defaults %{public}@"
+ "readFileIntoVector,%{public}s,size,%{public}zu"
- "#comm,configure,IOSSIOSPEED,%lu,standardSpeed,%lu"
- "#comm,open,%s,flag,0x%{public}X"
- "#gdm,decodeCoexConfig,coexConfigPostOverride,0x%{public}llx,coexConfigDefault,0x%{public}llx,isCLOverride,%s,coexConfigCLOverride,0x%{public}llx"
- "#gpsdUtil,CC_SHA256 failed on,%p,%zu"
- "#gpsdUtil,Tick to ns info,Numerator,%llu,Denominator,%llu,PrecisionReductionBits,%d"
- "#spi,hal,write,size,%zu,duration,us,%.1f"
- "#version,CoreGPS-326.0.2,machContSec,%{public}.3f,BuildTime,{Jun 13 2025,05:56:20}"
- "%s,%zu,%zu,%s"
- "/AppleInternal/Library/BuildRoots/4~B2_BugAm1GzvXODY4Aja5x8PfgnMu26FfSBRIoc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
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
- "Pref: %@ = %@"
- "Pref: kNmeaMaskOverride = 0x%llx"
- "Pref: kPvtmTimeOut = %d"
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
- "deviceInterfaceCallback,results,curent:%{public}s,new:%{public}s"
- "factoryTestJob,%s"
- "factoryTestXml,%s"
- "gpsd_plistpath: %@ defaults %@"
- "readFileIntoVector,%s,size,%zu"

```
