## aonsensed

> `/usr/libexec/aonsensed`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0x37de28
-  __TEXT.__auth_stubs: 0x20d0
+  __TEXT.__text: 0x391c00
+  __TEXT.__auth_stubs: 0x2590
   __TEXT.__objc_methlist: 0x44
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x2c4a0
-  __TEXT.__cstring: 0x15ca8
-  __TEXT.__constg_swiftt: 0x8fe8
-  __TEXT.__swift5_typeref: 0x661a
-  __TEXT.__swift5_reflstr: 0xa998
-  __TEXT.__swift5_fieldmd: 0xb094
-  __TEXT.__oslogstring: 0x1316
-  __TEXT.__swift5_types: 0x7f4
-  __TEXT.__swift5_assocty: 0x1950
-  __TEXT.__swift5_proto: 0x2920
+  __TEXT.__const: 0x2cab0
+  __TEXT.__cstring: 0x16608
+  __TEXT.__constg_swiftt: 0x98dc
+  __TEXT.__swift5_typeref: 0x6810
+  __TEXT.__swift5_reflstr: 0xae58
+  __TEXT.__swift5_fieldmd: 0xb534
+  __TEXT.__oslogstring: 0x1c36
+  __TEXT.__swift5_types: 0x848
+  __TEXT.__swift5_assocty: 0x1980
+  __TEXT.__swift5_proto: 0x2954
   __TEXT.__objc_methname: 0x6af
-  __TEXT.__swift5_capture: 0x230
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_capture: 0x298
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__unwind_info: 0xeb28
-  __TEXT.__eh_frame: 0xcad8
-  __DATA_CONST.__auth_got: 0x1068
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__auth_ptr: 0x708
-  __DATA_CONST.__const: 0x9070
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__unwind_info: 0xf048
+  __TEXT.__eh_frame: 0xd610
+  __DATA_CONST.__auth_got: 0x12d0
+  __DATA_CONST.__got: 0x660
+  __DATA_CONST.__auth_ptr: 0x7b0
+  __DATA_CONST.__const: 0x9770
+  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x7d90
+  __DATA.__objc_const: 0x8ca0
   __DATA.__objc_selrefs: 0x260
   __DATA.__objc_data: 0xe78
-  __DATA.__data: 0x18348
+  __DATA.__data: 0x190e0
   __DATA.__common: 0x2998
-  __DATA.__bss: 0x559e8
+  __DATA.__bss: 0x56028
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
   - /System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 23616
-  Symbols:   826
-  CStrings:  3509
+  Functions: 24045
+  Symbols:   930
+  CStrings:  3628
 
Symbols:
+ ___strlcpy_chk
+ _$s9Tightbeam0A7DecoderV7encoder5bytes12capabilitiesAA0A7EncoderVSi_SitKF
+ _strdup
+ _IOConnectMapMemory64
+ _kIOMainPortDefault
+ __Unwind_Resume
+ _$s11ALDataTypes27ALWiFiScanSingleAccessPointV7channels5Int32VSgvg
+ _CFRunLoopRun
+ _$ss6UInt64Vs23CustomStringConvertiblesWP
+ _$ss5NeverON
+ _pthread_mutex_lock
+ _$ss6MirrorV10reflectingAByp_tcfC
+ _$s9Tightbeam0A7EncoderV6encodeyys4Int8VF
+ _$s9Tightbeam0A7DecoderV6decode2ass5Int32VAGm_tF
+ _$s9Tightbeam15ServiceProtocolPAA013MessageDecodeC0Tb
+ _CFDictionarySetValue
+ _$sSzsE11descriptionSSvg
+ _CFDictionaryCreateMutableCopy
+ _CFRunLoopRemoveSource
+ _$s9Tightbeam0A7DecoderV7messageAcA0A7MessageC_tcfC
+ _$s9Tightbeam0A7MessageC11BufferUsageOMa
+ _$s9Tightbeam0A7MessageC17withBufferPointer3for__xAC0D5UsageO_Srys5UInt8VGxACKXEtKlFZ
+ _$s9Tightbeam0A7DecoderV6decode2ass5UInt8VAGm_tF
+ _$s9Tightbeam0A7EncoderV8completeAA0A7MessageCyF
+ _$s9Tightbeam16ClientConnectionCMa
+ _CFRunLoopGetCurrent
+ _$s9Tightbeam0A7MessageCMa
+ _$s9Tightbeam17ServiceConnectionC7serviceAA0B8Protocol_pSgvsTj
+ _malloc_type_malloc
+ _$s9Tightbeam0A7DecoderV6decode2ass6UInt64VAGm_tF
+ _IOServiceClose
+ _$ss6UInt32VN
+ _IONotificationPortCreate
+ _mach_task_self_
+ _pthread_mutex_unlock
+ _snprintf
+ _$s9Tightbeam0A8EndpointOMa
+ _$s9Tightbeam0A7DecoderVMa
+ _$s9Tightbeam16ClientConnectionC8endpointAcA0A8EndpointO_tcfc
+ _$s11ALDataTypes27ALWiFiScanSingleAccessPointV6rssidBs5Int32VSgvg
+ _$s9Tightbeam0A7MessageC7encoderAA0A7EncoderVyFTj
+ _sleep
+ _$ss5Int32VN
+ _$s9Tightbeam0A7EncoderV6encodeyys6UInt32VF
+ _$s9Tightbeam0A7DecoderV6decode2ass4Int8VAGm_tF
+ _kCFAllocatorDefault
+ _swift_willThrowTypedImpl
+ _IOServiceOpen
+ _$s9Tightbeam17ServiceConnectionC8endpointAcA0A8EndpointO_tcfc
+ _$s9Tightbeam0A7EncoderV6encodeyys5Int32VF
+ _$s9Tightbeam17ServiceConnectionCMn
+ _CFRelease
+ _strcmp
+ _$s9Tightbeam0A7DecoderV6decode2asS2bm_tF
+ _$s9Tightbeam16ClientConnectionC15allocateMessage4size12capabilitiesAA0aE0CSi_SitKF
+ _$ss6HasherV8_combineyys5UInt8VF
+ _IONotificationPortGetRunLoopSource
+ _$s9Tightbeam0A7EncoderVMa
+ _$s9Tightbeam17ServiceConnectionC5beginyyFTj
+ _$s9Tightbeam0A8EndpointO3afkyACs6UInt32V_tcACmFWC
+ _$s9Tightbeam15ServiceProtocolMp
+ ___CFConstantStringClassReference
+ _$s9Tightbeam0A7EncoderV6encodeyys5UInt8VF
+ _strlen
+ _$ss5UInt8Vs23CustomStringConvertiblesWP
+ __swift_exceptionPersonality
+ _$s9Tightbeam0A7EncoderV6encodeyys6UInt64VF
+ _$ss5Int32VSzsMc
+ _$s11ALDataTypes27ALWiFiScanSingleAccessPointV3macs6UInt64VSgvg
+ _$ss11_StringGutsV16_slowWithCStringyxxSPys4Int8VGKXEKlF
+ _kIOMasterPortDefault
+ _IONotificationPortDestroy
+ _kCFRunLoopDefaultMode
+ _$ss15_AnySequenceBoxC4_mapySayqd__Gqd__xKXEKlFTj
+ _swift_getForeignTypeMetadata
+ _$ss5UInt8Vs7CVarArgsWP
+ _$s9Tightbeam0A19ServiceInitProtocolMp
+ _$s9Tightbeam17ServiceConnectionCMa
+ _$ss6MirrorVMa
+ _$ss6MirrorV8childrens13AnyCollectionVySSSg5label_yp5valuetGvg
+ _CFRunLoopStop
+ _$sSa11descriptionSSvg
+ _CFStringCreateWithCString
+ _MobileGestalt_get_deviceSupportsAOP2
+ _$s9Tightbeam0A7DecoderV6decode2ass6UInt32VAGm_tF
+ _IOObjectRelease
+ _IOIteratorNext
+ _$s9Tightbeam0A7EncoderVMn
+ _$s9Tightbeam0A7MessageC11BufferUsageO7readingyA2EmFWC
+ _IOServiceAddMatchingNotification
+ _$s9Tightbeam16ClientConnectionC4send7messageAA0A7MessageCAG_tKF
+ _$sSb10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$s9Tightbeam0A7MessageC11BufferUsageO7writingyA2EmFWC
+ _$s9Tightbeam16ClientConnectionCMn
+ _$sSo17OS_dispatch_queueC8DispatchE10asyncAfter8deadline3qos5flags7executeyAC0D4TimeV_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _IOServiceMatching
+ _tb_endpoint_create_with_data
+ _$ss4Int8Vs23CustomStringConvertiblesWP
+ _$s9Tightbeam0A19ServiceInitProtocolP8endpointxAA0A8EndpointO_tcfCTq
+ _$s9Tightbeam21MessageDecodeProtocolMp
+ _$ss5NeverOs5ErrorsWP
+ _CFRunLoopAddSource
+ _$s9Tightbeam21MessageDecodeProtocolP6decodeyAA0aB0CSgAA0A7DecoderVKFTq
+ _$s9Tightbeam0A7EncoderV6encodeyySbF
CStrings:
+ "Tightbeam, getSamplesQueueSize error: %!{(MISSING)public}@."
+ "WifiAddedAop2Scans"
+ "com.apple.aop2.aonloc"
+ "_newBlockCallback"
+ "Tightbeam, enableWifiReception error: %!{(MISSING)public}@."
+ "#WiFi,fetchQueue,AOPSERVICETIMESTAMP,timestamp,%!{(MISSING)public}llu"
+ "_failedAOP2Pings"
+ "Tightbeam, mallocNBlocks error: %!{(MISSING)public}@."
+ "_lastTimeSinceAPLastSleptInUsecs"
+ "PRCclassTest"
+ "WifiBufferOverflows"
+ "#WiFi, got pong from watchdog id: %!{(MISSING)public}llu, last sent %!{(MISSING)public}llu"
+ "IOServiceFirstMatch"
+ "WifiAddedEpnoAps"
+ "_aonloc"
+ "_tbHandler"
+ "#WiFi, Leeching on AOP2"
+ "deinitSharedMemory(handle:)"
+ "Tightbeam, setAONLogLevel error: %!{(MISSING)public}@."
+ "timeSinceAPLastSleptInUsecs='%!{(MISSING)public}llu'"
+ "{\"msg\":\"AOP2 logs received\", \"log\":%!s(MISSING)}"
+ "aop2.gps-debug"
+ "PollingAOP2IntervalSec"
+ "aop2.gps-data"
+ "_TtC5ALRPC9ALRPCTest"
+ "Tightbeam, init success"
+ "#WiFi,fetchQueue,block.next,%!{(MISSING)public}ld,count,%!{(MISSING)public}ld"
+ "Tightbeam, nudgeDRAMMove error: %!{(MISSING)public}@."
+ "Failed to find RPC server: "
+ "_TtC8ALDaemon15ALWiFiLeechAOP2"
+ "_TtCC8ALRPCShm14aonloc_service6Server"
+ "invalid rawValue for aonloc_callback.Selector "
+ "#WiFi,fetchQueue,ASSOCIATEDBSSIDUPDATE,bssid:%!{(MISSING)private}llx"
+ "Not enough bits to represent the passed value"
+ "Tightbeam, getLargestFreeBlockBytes error: %!{(MISSING)public}@."
+ "_aonloc_cb"
+ "_idForWatchdog"
+ "/Library/Caches/com.apple.xbs/Sources/AONLoc/Interface/RPC/ALShmQueueHandler.swift"
+ "Shmem map failed to unmap: "
+ "_TtC8ALRPCShm15aonloc_callback"
+ "_onLocCompAnalytics"
+ "_pollsWithoutHearingBack"
+ "_TtC8ALRPCShm18ALTightbeamHandler"
+ "Tightbeam, hello error: %!{(MISSING)public}@."
+ "#WiFi, Enable AOP2 Wifi Reception"
+ "_aop2Ifc"
+ "Tightbeam, getBufferUsagePercentageData error: %!{(MISSING)public}@."
+ "_timestampOfLastPacketReceived"
+ "AFKEndpointInterface"
+ "IONameMatch"
+ "com.apple.aop2.aonloc.ap.client"
+ "Tightbeam, hello return: %!{(MISSING)public}llu"
+ "Can't nudge AOP2, reason: "
+ "BtBufferOverflows"
+ "_leechAOP2"
+ "_pollAOP2StatsIntervalSec"
+ "_TtC8ALRPCShm14aonloc_service"
+ "Shmem map failed to initialize: "
+ "_isAop2Device"
+ "AFKSharedMemoryRegion"
+ "Tightbeam, pingForDaemonWatchdog error: %!{(MISSING)public}@."
+ "_intervalForAOP2PingInSecs"
+ "Tightbeam, intermediate queue is full."
+ "Tightbeam, hello ack: %!l(MISSING)lu."
+ "Tightbeam, getPowerState error: %!{(MISSING)public}@."
+ "_shmLogsHandle"
+ "_shmQueue"
+ "numberOfWifiSamplesReceivedWhileAsleep='%!{(MISSING)public}llu'"
+ "Can't nudge AOP2, reason: communications failed."
+ "Tightbeam, enableCallbackMessages error: %!{(MISSING)public}@."
+ "handler"
+ "#WiFi, onData error: %!{(MISSING)public}@"
+ "_incompleteLogHeader"
+ "_shmLogsQueue"
+ "_TtC8ALRPCShm17ALShmQueueHandler"
+ "#WiFi, Got unrecognized special packet with broadcast BSSID: {bssid:%!s(MISSING), rssi:%!{(MISSING)public}hhd, channel:%!{(MISSING)public}hhu, flags:%!{(MISSING)public}hhu, timestamp:%!{(MISSING)public}llu})"
+ "_TtCC8ALRPCShm15aonloc_callback7Service"
+ "Tightbeam, got new block."
+ "invalid rawValue for aonloc_service.Selector "
+ "Polling interval is %!{(MISSING)public}f sec"
+ "ALRPCShm/aonloc.swift"
+ "_onWiFi"
+ "Tightbeam, enableCallbackMessages return: %!{(MISSING)bool,public}d"
+ "connection"
+ "#WiFi, got pong from lost watchdog id, daemon crashed recently or there was too many samples in intermediate queue"
+ "Can't ping AOP2."
+ ", failedAOP2Pings="
+ "#WiFi,fetchQueue,wifiscandata,%!s(MISSING)"
+ "%!s(MISSING)-%!s(MISSING)-fwd"
+ "_accessPoints"
+ "_nudgeDelay"
+ "initSharedMemory(name:)"
+ "_TtCC8ALRPCShm14aonloc_service7Service"
+ "fetchQueue()"
+ "_TtCC8ALRPCShm15aonloc_callback6Server"
+ "rpc_afk_interface_find failed."
+ "Tightbeam, enqueue wifi sample return: %!d(MISSING)"
+ "DRAMMove may be stuck, nudging and waiting %!{(MISSING)public}f seconds"
+ "Tightbeam, enableWifiReception %!{(MISSING)public}s -> %!{(MISSING)bool}d"
+ "_lastBundleMctSec"
+ "Tightbeam, error in apOff: %!{(MISSING)public}@"
+ "init(cb:)"
+ "_scanIntervalThresholdSec"
+ "Tightbeam, error in enqueue wifi sample: %!{(MISSING)public}@"
+ "#WiFi,fetchQueue,empty"
+ "#WiFi, AOP2 didn't pong back. samplesQueueSize="
+ "%!s(MISSING)-%!s(MISSING)-rev"
+ "_lastPollAOP2StatsMctSec"
+ "_haveAOP2"
+ "_incompleteLogSequence"
+ "#ShmQueue, _tbHandler is nil. Skip nudge"
+ "/Library/Caches/com.apple.xbs/Sources/AONLoc/Interface/RPC/AFKTightbeamEndpointsHelpers.swift"
+ "AOP2EnableWifiReception"
+ "Pinged AOP2, id: %!{(MISSING)public}llu"
+ "_shmHandle"
+ "_TtC8ALRPCShmP33_5C9CF5B0EE1E3CA893C978B6223E185410ackHandler"
+ "Tightbeam, error in apOn: %!{(MISSING)public}@"
+ "_TtC5ALRPC14ALRPCInterface"
+ "Tightbeam, setNumberOfAPsBeforeInterleavingSpecialTimestamp error: %!{(MISSING)public}@."

```
