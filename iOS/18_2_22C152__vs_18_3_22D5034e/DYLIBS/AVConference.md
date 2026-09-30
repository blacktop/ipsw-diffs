## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2090.17.2.0.0
-  __TEXT.__text: 0x6c2054
+2100.3.1.0.0
+  __TEXT.__text: 0x6c2484
   __TEXT.__auth_stubs: 0x5060
-  __TEXT.__objc_methlist: 0x2ddf0
-  __TEXT.__const: 0x7de0
-  __TEXT.__cstring: 0x8062a
-  __TEXT.__oslogstring: 0xedd02
-  __TEXT.__gcc_except_tab: 0x2560
+  __TEXT.__objc_methlist: 0x2de08
+  __TEXT.__const: 0x7e10
+  __TEXT.__cstring: 0x8072a
+  __TEXT.__oslogstring: 0xede2b
+  __TEXT.__gcc_except_tab: 0x2550
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd2f8
+  __TEXT.__unwind_info: 0xd2d0
   __TEXT.__objc_classname: 0x47d1
-  __TEXT.__objc_methname: 0x72780
-  __TEXT.__objc_methtype: 0x248aa
-  __TEXT.__objc_stubs: 0x48360
-  __DATA_CONST.__got: 0x18e8
+  __TEXT.__objc_methname: 0x728cb
+  __TEXT.__objc_methtype: 0x248b4
+  __TEXT.__objc_stubs: 0x483c0
+  __DATA_CONST.__got: 0x18d8
   __DATA_CONST.__const: 0x61d8
   __DATA_CONST.__objc_classlist: 0x1180
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14ab8
+  __DATA_CONST.__objc_selrefs: 0x14ac8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x25a0
   __AUTH_CONST.__auth_got: 0x2848
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__const: 0x3390
-  __AUTH_CONST.__cfstring: 0x22ba0
-  __AUTH_CONST.__objc_const: 0x61a88
+  __AUTH_CONST.__cfstring: 0x22be0
+  __AUTH_CONST.__objc_const: 0x61b28
   __AUTH_CONST.__objc_intobj: 0x45f0
   __AUTH_CONST.__objc_arrayobj: 0x1a58
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6408
+  __DATA.__objc_ivar: 0x6414
   __DATA.__data: 0x7490
   __DATA.__bss: 0xb68
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27940
+  Functions: 27939
   Symbols:   32675
-  CStrings:  47465
+  CStrings:  47488
 
CStrings:
+ " [%s] %s:%d %@(%p) image queue should not be nil if end point is set"
+ " [%s] %s:%d @:@ VCImageQueue-dealloc (%p)"
+ " [%s] %s:%d @:@ VCImageQueue-init (%p) frameRate=%d imageQueueProtected=%d"
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d image queue should not be nil if end point is set"
+ "-[VCImageQueue cleanupVideoTargetAndImageQueue]"
+ "-[VCImageQueue createAndCopyLatencyStatsDictionary:]"
+ "-[VCImageQueue createAndCopyPerformanceDictionary:]"
+ "-[VCRateControlMediaController updateBasebandDropPacketCountWithPayloadType:sequenceNumber:]"
+ "2100.3.1"
+ "@:@ VCImageQueue-dealloc"
+ "APBBD"
+ "BBNOTENW"
+ "Td,R,N,V_audioInterval"
+ "Ti,R,N,V_basebandDropAudioCount"
+ "Ti,R,N,V_basebandDropVideoCount"
+ "Ti,R,N,V_basebandNotificationType"
+ "VCRC [%s] %s:%d Baseband dropped media packet with payload type=%u, sequenceNumber=%u"
+ "VPBBD"
+ "_basebandDropAudioCount"
+ "_basebandDropVideoCount"
+ "_basebandNotificationType"
+ "_lastReportBasebandDropAudioPacketCount"
+ "_lastReportBasebandDropVideoPacketCount"
+ "audioInterval"
+ "basebandDropAudioCount"
+ "basebandDropVideoCount"
+ "basebandNotificationType"
+ "updateBasebandDropPacketCountWithPayloadType:sequenceNumber:"
+ "v22@0:8{tagVCVideoCaptureFeatureStatus=cccccc}16"
+ "v24@0:8C16S20"
+ "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
+ "v24@0:8^{tagVCVideoCaptureFeatureStatus=cccccc}16"
+ "{tagVCVideoCaptureFeatureStatus=cccccc}16@0:8"
- " [%s] %s:%d @:@ VCImageQueue-init frameRate=%d imageQueueProtected=%d"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- "2090.17.2"
- "BGRCCFENB"
- "setMaxBitrate:"
- "setMaxBitrateForBandwidthEstimator:"
- "setMaxBitrateForBandwidthEstimatorMap:"
- "v23@0:8{tagVCVideoCaptureFeatureStatus=ccccccc}16"
- "v24@0:8^{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
- "v24@0:8^{tagVCVideoCaptureFeatureStatus=ccccccc}16"
- "{tagVCVideoCaptureFeatureStatus=ccccccc}16@0:8"

```
