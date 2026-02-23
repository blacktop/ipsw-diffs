## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-9140.1.0.0.0
-  __TEXT.__text: 0xc4614
-  __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_stubs: 0x61c0
-  __TEXT.__init_offsets: 0x1260
-  __TEXT.__objc_methlist: 0x49e8
-  __TEXT.__const: 0x3dbe
-  __TEXT.__gcc_except_tab: 0xd6f4
-  __TEXT.__cstring: 0xd229
-  __TEXT.__oslogstring: 0x3704
-  __TEXT.__objc_methname: 0x6e82
-  __TEXT.__objc_classname: 0xb7d
-  __TEXT.__objc_methtype: 0x54b4
-  __TEXT.__unwind_info: 0x4438
-  __DATA_CONST.__auth_got: 0xca8
+9140.3.0.0.0
+  __TEXT.__text: 0xc5494
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_stubs: 0x6260
+  __TEXT.__init_offsets: 0x1280
+  __TEXT.__objc_methlist: 0x4a78
+  __TEXT.__const: 0x3dde
+  __TEXT.__gcc_except_tab: 0xd7fc
+  __TEXT.__cstring: 0xd280
+  __TEXT.__oslogstring: 0x37c7
+  __TEXT.__objc_methname: 0x6f19
+  __TEXT.__objc_classname: 0xb9a
+  __TEXT.__objc_methtype: 0x59a6
+  __TEXT.__unwind_info: 0x44b8
+  __DATA_CONST.__auth_got: 0xcb0
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x1b48
-  __DATA_CONST.__cfstring: 0x6de0
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__const: 0x1b70
+  __DATA_CONST.__cfstring: 0x6e40
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_intobj: 0x600
+  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_intobj: 0x618
   __DATA_CONST.__objc_doubleobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x518
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA.__objc_const: 0x8920
-  __DATA.__objc_selrefs: 0x1d60
-  __DATA.__objc_ivar: 0x5bc
-  __DATA.__objc_data: 0x2300
+  __DATA.__objc_const: 0x8a38
+  __DATA.__objc_selrefs: 0x1d88
+  __DATA.__objc_ivar: 0x5cc
+  __DATA.__objc_data: 0x2350
   __DATA.__data: 0x1610
   __DATA.__bss: 0xc0
   __DATA.__common: 0x890

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A35837F6-B782-3824-8644-B64ACF9FB4C9
-  Functions: 4751
-  Symbols:   26400
-  CStrings:  4517
+  UUID: BEFF40F1-B64C-3639-A23B-3ABD5BF33FBE
+  Functions: 4774
+  Symbols:   26559
+  CStrings:  4539
 
Symbols:
+ -[HSTTelemetryAnalyticsStage .cxx_construct]
+ -[HSTTelemetryAnalyticsStage .cxx_destruct]
+ -[HSTTelemetryAnalyticsStage _handleFrame:]
+ -[HSTTelemetryAnalyticsStage _initializeReportIdMap]
+ -[HSTTelemetryAnalyticsStage _logPathReports]
+ -[HSTTelemetryAnalyticsStage _sendAnalyticsEvent:payload:]
+ -[HSTTelemetryAnalyticsStage _setupPeriodicTimer]
+ -[HSTTelemetryAnalyticsStage _trackReportID:]
+ -[HSTTelemetryAnalyticsStage dealloc]
+ -[HSTTelemetryAnalyticsStage handleConsume:]
+ -[HSTTelemetryAnalyticsStage initWithQueue:]
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationManager.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/CoreAccessoryManager.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/FirmwareUtil.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTTelemetryAnalyticsStage.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/Managers/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/Plugin/
+ /Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/Plugin/Parser/
+ HSTTelemetryAnalyticsStage.mm
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._periodicTimer
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._queue
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._receivedMask
+ OBJC_IVAR_$_HSTTelemetryAnalyticsStage._reportIdToBitMap
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_HSTTelemetryAnalyticsStage
+ _OBJC_METACLASS_$_HSTTelemetryAnalyticsStage
+ __Block_byref_object_copy_.422
+ __Block_byref_object_dispose_.423
+ __OBJC_$_INSTANCE_METHODS_HSTTelemetryAnalyticsStage
+ __OBJC_$_INSTANCE_VARIABLES_HSTTelemetryAnalyticsStage
+ __OBJC_CLASS_RO_$_HSTTelemetryAnalyticsStage
+ __OBJC_METACLASS_RO_$_HSTTelemetryAnalyticsStage
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIhJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZZ52-[HSTTelemetryAnalyticsStage _initializeReportIdMap]E9reportIds
+ ___49-[HSTTelemetryAnalyticsStage _setupPeriodicTimer]_block_invoke
+ ___58-[HSTTelemetryAnalyticsStage _sendAnalyticsEvent:payload:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e19_"NSDictionary"8?0ls32l8
+ _objc_msgSend$_initializeReportIdMap
+ _objc_msgSend$_logPathReports
+ _objc_msgSend$_sendAnalyticsEvent:payload:
+ _objc_msgSend$_setupPeriodicTimer
+ _objc_msgSend$_trackReportID:
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationManager.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/CoreAccessoryManager.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/FirmwareUtil.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Binaries/Multitouch/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/Managers/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/Plugin/
- /Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/Plugin/Parser/
- __Block_byref_object_copy_.421
- __Block_byref_object_dispose_.422
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI66ugB88kjDnjGDyA3fNTY8uFU5XrbpCf8inos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI66ugB88kjDnjGDyA3fNTY8uFU5XrbpCf8inos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI66ugB88kjDnjGDyA3fNTY8uFU5XrbpCf8inos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI66ugB88kjDnjGDyA3fNTY8uFU5XrbpCf8inos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSMachPortListener.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPlaybackStage.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPreferenceStage.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingPlaybackStage.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingStage.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingTypes.h"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject+Additions.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServerStage.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServiceDirectory.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSSocketListener.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStage+Util.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStageProxy.mm"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingUtil/HSIOUtil.h"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingUtil/HSPortRight.h"
+ "/Library/Caches/com.apple.xbs/70B9655F-08F3-4A96-9EF8-E3B23050D00D/TemporaryDirectory.1DTGYD/Sources/HIDSensingPipeline/HIDSensingUtil/HSSocket.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Contact.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTBackboardBridge.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTContactStabilizer.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTEvent.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTFrame.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTFrameParser.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTHIDEventGenerator.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTHIDEvents.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTPencilVirtualService.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTRecordingManager.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTSensingAlgs.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTServerStage.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTTipOffsetFilter.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Types.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSMousePipelineCreation.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTFirmwareManager.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTPipelineCreation.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTSAPipelineCreation.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTouchHIDService.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTrackpadPipelineCreation.m"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/MTTrackpadUberAlg.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/MTForceManagement_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTChordCycling_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTGestureConfig_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTHandStatistics_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTPathStates_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTSurfaceDimensions_.hpp"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/TrackpadAlgStage.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/HSTrackpadDefs.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/EmbeddedTrackpadHIDEventProcessor.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/PointerHIDEventProcessor.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/PointerBridge.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/TrackpadBridge.mm"
+ "/Library/Caches/com.apple.xbs/C7CFE689-84AD-4BE8-B76A-9DAB65E811FA/TemporaryDirectory.e02Yid/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/PointerSettings.mm"
+ "9140.3"
+ "@\"NSDictionary\"8@?0"
+ "Deallocating telemetry analytics stage"
+ "HSTTelemetryAnalyticsStage"
+ "Sending analytics event: %{public}@"
+ "Telemetry analytics stage scheduling periodic 24h logging on dispatch queue"
+ "Telemetry reporter logging found report IDs"
+ "_initializeReportIdMap"
+ "_logPathReports"
+ "_periodicTimer"
+ "_receivedMask"
+ "_reportIdToBitMap"
+ "_sendAnalyticsEvent:payload:"
+ "_setupPeriodicTimer"
+ "_trackReportID:"
+ "b"
+ "com.apple.HID.multitouchPathsReportIDUsage"
+ "reportID"
+ "reportID_value"
+ "{unordered_map<unsigned char, unsigned char, std::hash<unsigned char>, std::equal_to<unsigned char>, std::allocator<std::pair<const unsigned char, unsigned char>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned char, unsigned char>, std::__unordered_map_hasher<unsigned char, std::pair<const unsigned char, unsigned char>, std::hash<unsigned char>, std::equal_to<unsigned char>>, std::__unordered_map_equal<unsigned char, std::pair<const unsigned char, unsigned char>, std::equal_to<unsigned char>, std::hash<unsigned char>>, std::allocator<std::pair<const unsigned char, unsigned char>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned char, unsigned char>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "/AppleInternal/Library/BuildRoots/4~CHoMugD4Gbt8PzFSYgDZL5TMGPPbHLpQT-Ip7tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHoMugD4Gbt8PzFSYgDZL5TMGPPbHLpQT-Ip7tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoMugD4Gbt8PzFSYgDZL5TMGPPbHLpQT-Ip7tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoMugD4Gbt8PzFSYgDZL5TMGPPbHLpQT-Ip7tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Contact.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTBackboardBridge.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTContactStabilizer.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTEvent.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTFrame.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTFrameParser.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTHIDEventGenerator.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTHIDEvents.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTPencilVirtualService.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTRecordingManager.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTSensingAlgs.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTServerStage.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/HSTTipOffsetFilter.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTPipeline/Types.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSMousePipelineCreation.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTFirmwareManager.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTPipelineCreation.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTSAPipelineCreation.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTouchHIDService.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/HIDSensingTouch/HSTouchHIDService/HSTrackpadPipelineCreation.m"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/MTTrackpadUberAlg.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/MTForceManagement_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTChordCycling_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTGestureConfig_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTHandStatistics_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTPathStates_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTSurfaceDimensions_.hpp"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/Alg/TrackpadAlgStage.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/HSTrackpadDefs.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/EmbeddedTrackpadHIDEventProcessor.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/PointerHIDEventProcessor.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/PointerBridge.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/TrackpadBridge.mm"
- "/Library/Caches/com.apple.xbs/842016E7-D76A-4FC3-8334-AA23DA47C5EF/TemporaryDirectory.rzc8SD/Sources/Multitouch/MT2TPHIDService/HSTrackpad/PreAlg/PointerSettings.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSMachPortListener.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPlaybackStage.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPreferenceStage.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingPlaybackStage.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingStage.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingTypes.h"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject+Additions.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServerStage.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServiceDirectory.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSSocketListener.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStage+Util.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStageProxy.mm"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingUtil/HSIOUtil.h"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingUtil/HSPortRight.h"
- "/Library/Caches/com.apple.xbs/87D66679-54FB-4847-A943-4236B447024A/TemporaryDirectory.lX8j6t/Sources/HIDSensingPipeline/HIDSensingUtil/HSSocket.mm"
- "9140.1"

```
