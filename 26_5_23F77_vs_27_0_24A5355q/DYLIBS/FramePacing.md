## FramePacing

> `/System/Library/PrivateFrameworks/FramePacing.framework/FramePacing`

```diff

-4.1.8.0.0
-  __TEXT.__text: 0x64d0
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x180
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x332
-  __TEXT.__oslogstring: 0x3c8b
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x7bd
-  __TEXT.__objc_methtype: 0xc7
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__objc_classlist: 0x28
+5.0.18.0.0
+  __TEXT.__text: 0x26260
+  __TEXT.__objc_methlist: 0x1588
+  __TEXT.__const: 0x1d8
+  __TEXT.__gcc_except_tab: 0xb88
+  __TEXT.__cstring: 0x2fae
+  __TEXT.__oslogstring: 0xd675
+  __TEXT.__unwind_info: 0xb48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x190
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0xb60
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x28
-  __DATA.__common: 0x38
-  __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x140
-  __DATA_DIRTY.__common: 0x68
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__got: 0x158
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__objc_const: 0x2fb0
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x328
+  __DATA.__data: 0x288
+  __DATA.__bss: 0x18
+  __DATA.__common: 0x40
+  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__data: 0x4
+  __DATA_DIRTY.__bss: 0x270
+  __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD48779C-A2BF-3776-B79A-49464BCB232E
-  Functions: 138
-  Symbols:   528
-  CStrings:  239
+  UUID: A8C1C6CB-7863-316B-9EC2-FF0420C26D25
+  Functions: 732
+  Symbols:   2466
+  CStrings:  738
 
Symbols:
+ +[FPCAMetalLayerState drawableLifetimeComposited:drawableID:surfaceID:compositedTime:detachCode:]
+ +[FPCAMetalLayerState metal4CommandBufferBegin:beginMAT:]
+ +[FPCAMetalLayerState metal4CommandBufferCommited:queueAddress:generation:commitMAT:]
+ +[FPCAMetalLayerState metal4CommandBufferCompleted:queueAddress:generation:gpuStartMAT:gpuEndMAT:]
+ +[FPCAMetalLayerState metal4CommandBufferCreated:creationMAT:]
+ +[FPCAMetalLayerState metal4CommandBufferDeallocated:]
+ +[FPCAMetalLayerState metal4CommandBufferEnd:endMAT:allocatorId:allocatedSize:]
+ +[FPMTLMetricsMTLLayerTracking deallocTrackerForLayer:]
+ +[FPMTLMetricsMTLLayerTracking enumerateTrackers:]
+ +[FPMTLMetricsMTLLayerTracking mainTracker]
+ +[FPMTLMetricsMTLLayerTracking numTrackers]
+ +[FPMTLMetricsMTLLayerTracking setMainTracker:]
+ +[FPMTLMetricsMTLLayerTracking trackerForLayer:]
+ +[FPMTLMetricsServiceInternal instance]
+ +[_CADeveloperHUDProperties instance]
+ -[FPCAMetalLayerAggregatedStats .cxx_destruct]
+ -[FPCAMetalLayerAggregatedStats addGPTkMetrics:]
+ -[FPCAMetalLayerAggregatedStats addMetalFXMetrics:]
+ -[FPCAMetalLayerAggregatedStats addShaderCompilerStatMetrics:]
+ -[FPCAMetalLayerAggregatedStats emitSignpost:log:intervalBegin:intervalEnd:]
+ -[FPCAMetalLayerAggregatedStats init]
+ -[FPCAMetalLayerAggregatedStats resetStats]
+ -[FPCAMetalLayerAggregatedStats setCommandBufferCount:]
+ -[FPCAMetalLayerAggregatedStats setDetachCount:]
+ -[FPCAMetalLayerAggregatedStats setMetalFXAutoExposureEnabledCount:]
+ -[FPCAMetalLayerAggregatedStats setMetalFXEnabledCount:]
+ -[FPCAMetalLayerAggregatedStats setMetalFXFrameInterpolatorEnabledCount:]
+ -[FPCAMetalLayerAggregatedStatsGPTK .cxx_destruct]
+ -[FPCAMetalLayerAggregatedStatsGPTK emitSignpost:log:intervalBegin:intervalEnd:numFrames:isSkippedFrameStats:]
+ -[FPCAMetalLayerAggregatedStatsGPTK init]
+ -[FPCAMetalLayerAggregatedStatsGPTK resetStats]
+ -[FPCAMetalLayerAggregatedStatsShaderCompiler emitSignpost:log:intervalBegin:intervalEnd:numFrames:isSkippedFrameStats:]
+ -[FPCAMetalLayerAggregatedStatsShaderCompiler init]
+ -[FPCAMetalLayerState finishDrawableLifetimeWithImageQueueID:drawableID:drawableFinishedTime:wasPresented:targetCPUDeadline:targetPresentationTime:]
+ -[FPMTLMetricsClientInsight .cxx_construct]
+ -[FPMTLMetricsClientInsight .cxx_destruct]
+ -[FPMTLMetricsClientInsight additionalContext]
+ -[FPMTLMetricsClientInsight category]
+ -[FPMTLMetricsClientInsight component]
+ -[FPMTLMetricsClientInsight context]
+ -[FPMTLMetricsClientInsight descriptor]
+ -[FPMTLMetricsClientInsight documentationLinks]
+ -[FPMTLMetricsClientInsight documentationTitles]
+ -[FPMTLMetricsClientInsight enabled]
+ -[FPMTLMetricsClientInsight identifier]
+ -[FPMTLMetricsClientInsight initWithDescriptor:isPrototype:]
+ -[FPMTLMetricsClientInsight message]
+ -[FPMTLMetricsClientInsight name]
+ -[FPMTLMetricsClientInsight numInstances]
+ -[FPMTLMetricsClientInsight setEnabled:]
+ -[FPMTLMetricsClientInsight supportedAPI]
+ -[FPMTLMetricsClientInsight timeCreated]
+ -[FPMTLMetricsClientInsight timeOut]
+ -[FPMTLMetricsClientInsight timeUpdated]
+ -[FPMTLMetricsClientInsight update:]
+ -[FPMTLMetricsClientInsightGroup .cxx_destruct]
+ -[FPMTLMetricsClientInsightGroup category]
+ -[FPMTLMetricsClientInsightGroup enabled]
+ -[FPMTLMetricsClientInsightGroup initWithCategory:]
+ -[FPMTLMetricsClientInsightGroup insights]
+ -[FPMTLMetricsClientInsightGroup setEnabled:]
+ -[FPMTLMetricsClientMetricCollection .cxx_destruct]
+ -[FPMTLMetricsClientMetricCollection addMetric:]
+ -[FPMTLMetricsClientMetricCollection getMetric:]
+ -[FPMTLMetricsClientMetricCollection init]
+ -[FPMTLMetricsClientMetricCollection removeMetrics:]
+ -[FPMTLMetricsClientMetricCollection requestAllMetrics]
+ -[FPMTLMetricsClientMetricCollection resetAllMetrics]
+ -[FPMTLMetricsClientMetricCollection resetMetric:]
+ -[FPMTLMetricsClientMetricCollection resetMetricAtIndex:]
+ -[FPMTLMetricsClientMetricCollection updateMetric:value:]
+ -[FPMTLMetricsClientMetricCollection updateMetricAtIndex:value:]
+ -[FPMTLMetricsClientMetricCollection updateMetricInt:value:]
+ -[FPMTLMetricsClientMetricCollection updateMetricIntAtIndex:value:]
+ -[FPMTLMetricsClientMetricCollection updateStringMetric:value:]
+ -[FPMTLMetricsClientMetricCollection updateStringMetricAtIndex:value:]
+ -[FPMTLMetricsClientMetricDescriptor .cxx_destruct]
+ -[FPMTLMetricsClientMetricDescriptor component]
+ -[FPMTLMetricsClientMetricDescriptor descriptorIndex]
+ -[FPMTLMetricsClientMetricDescriptor identifier]
+ -[FPMTLMetricsClientMetricDescriptor initWithName:identifier:unit:nameColor:valueColor:visualType:options:]
+ -[FPMTLMetricsClientMetricDescriptor initWithName:identifier:unit:options:unitType:nameColor:valueColor:visualType:minvalueAllowed:maxValueAllowed:component:]
+ -[FPMTLMetricsClientMetricDescriptor maxValueAllowed]
+ -[FPMTLMetricsClientMetricDescriptor metadataFormat]
+ -[FPMTLMetricsClientMetricDescriptor minValueAllowed]
+ -[FPMTLMetricsClientMetricDescriptor nameColor]
+ -[FPMTLMetricsClientMetricDescriptor name]
+ -[FPMTLMetricsClientMetricDescriptor options]
+ -[FPMTLMetricsClientMetricDescriptor setDescriptorIndex:]
+ -[FPMTLMetricsClientMetricDescriptor setMaxValueAllowed:]
+ -[FPMTLMetricsClientMetricDescriptor setMinValueAllowed:]
+ -[FPMTLMetricsClientMetricDescriptor setName:]
+ -[FPMTLMetricsClientMetricDescriptor setNameColor:]
+ -[FPMTLMetricsClientMetricDescriptor setOptions:]
+ -[FPMTLMetricsClientMetricDescriptor setUnit:]
+ -[FPMTLMetricsClientMetricDescriptor setUnitType:]
+ -[FPMTLMetricsClientMetricDescriptor setValueColor:]
+ -[FPMTLMetricsClientMetricDescriptor setValueIndex:]
+ -[FPMTLMetricsClientMetricDescriptor setVisualType:]
+ -[FPMTLMetricsClientMetricDescriptor unitType]
+ -[FPMTLMetricsClientMetricDescriptor unit]
+ -[FPMTLMetricsClientMetricDescriptor valueColor]
+ -[FPMTLMetricsClientMetricDescriptor valueIndex]
+ -[FPMTLMetricsClientMetricDescriptor visualType]
+ -[FPMTLMetricsClientMetricDescriptorGroup .cxx_destruct]
+ -[FPMTLMetricsClientMetricDescriptorGroup component]
+ -[FPMTLMetricsClientMetricDescriptorGroup descriptors]
+ -[FPMTLMetricsClientMetricDescriptorGroup initWithComponent:]
+ -[FPMTLMetricsClientMetricDescriptorGroup mutableDescriptors]
+ -[FPMTLMetricsClientMetricValue .cxx_destruct]
+ -[FPMTLMetricsClientMetricValue component]
+ -[FPMTLMetricsClientMetricValue descriptor]
+ -[FPMTLMetricsClientMetricValue doublevalue]
+ -[FPMTLMetricsClientMetricValue enabled]
+ -[FPMTLMetricsClientMetricValue hidden]
+ -[FPMTLMetricsClientMetricValue initWithDescriptor:]
+ -[FPMTLMetricsClientMetricValue intValue]
+ -[FPMTLMetricsClientMetricValue lastUpdateTime]
+ -[FPMTLMetricsClientMetricValue setDoublevalue:]
+ -[FPMTLMetricsClientMetricValue setEnabled:]
+ -[FPMTLMetricsClientMetricValue setHidden:]
+ -[FPMTLMetricsClientMetricValue setIntValue:]
+ -[FPMTLMetricsClientMetricValue setStringValue:]
+ -[FPMTLMetricsClientMetricValue stringValue]
+ -[FPMTLMetricsClientMetricValue valueAverage]
+ -[FPMTLMetricsClientMetricValue valueMax]
+ -[FPMTLMetricsClientMetricValue valueMin]
+ -[FPMTLMetricsClientMetricValue valueStddev]
+ -[FPMTLMetricsClientMetricValue valueType]
+ -[FPMTLMetricsGPUTimingListenerObjectInternal .cxx_destruct]
+ -[FPMTLMetricsGPUTimingListenerObjectInternal init:]
+ -[FPMTLMetricsGPUTimingListenerObjectInternal listener]
+ -[FPMTLMetricsGPUTimingListenerObjectInternal setListener:]
+ -[FPMTLMetricsHUDFeatureDescriptor .cxx_destruct]
+ -[FPMTLMetricsHUDFeatureDescriptor component]
+ -[FPMTLMetricsHUDFeatureDescriptor defaultValue]
+ -[FPMTLMetricsHUDFeatureDescriptor didChange]
+ -[FPMTLMetricsHUDFeatureDescriptor documentationLinks]
+ -[FPMTLMetricsHUDFeatureDescriptor documentationTitles]
+ -[FPMTLMetricsHUDFeatureDescriptor envVar]
+ -[FPMTLMetricsHUDFeatureDescriptor featureDescription]
+ -[FPMTLMetricsHUDFeatureDescriptor identifier]
+ -[FPMTLMetricsHUDFeatureDescriptor initButton:title:description:documtationTitles:documentLinks:options:didChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor initCommon:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:]
+ -[FPMTLMetricsHUDFeatureDescriptor initPopover:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:items:selectedIndex:didChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor initSlider:title:envVar:description:documtationTitles:documentLinks:options:minValue:maxValue:defaultValue:numberOfTicks:didChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor initTextbox:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:didChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor initToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:didChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor initToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:valueRef:]
+ -[FPMTLMetricsHUDFeatureDescriptor items]
+ -[FPMTLMetricsHUDFeatureDescriptor maxValue]
+ -[FPMTLMetricsHUDFeatureDescriptor minValue]
+ -[FPMTLMetricsHUDFeatureDescriptor numberOfTicks]
+ -[FPMTLMetricsHUDFeatureDescriptor options]
+ -[FPMTLMetricsHUDFeatureDescriptor selectedIndex]
+ -[FPMTLMetricsHUDFeatureDescriptor setComponent:]
+ -[FPMTLMetricsHUDFeatureDescriptor setDefaultValue:]
+ -[FPMTLMetricsHUDFeatureDescriptor setDidChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor setDocumentationLinks:]
+ -[FPMTLMetricsHUDFeatureDescriptor setDocumentationTitles:]
+ -[FPMTLMetricsHUDFeatureDescriptor setEnvVar:]
+ -[FPMTLMetricsHUDFeatureDescriptor setFeatureDescription:]
+ -[FPMTLMetricsHUDFeatureDescriptor setIdentifier:]
+ -[FPMTLMetricsHUDFeatureDescriptor setItems:]
+ -[FPMTLMetricsHUDFeatureDescriptor setMaxValue:]
+ -[FPMTLMetricsHUDFeatureDescriptor setMinValue:]
+ -[FPMTLMetricsHUDFeatureDescriptor setNumberOfTicks:]
+ -[FPMTLMetricsHUDFeatureDescriptor setOptions:]
+ -[FPMTLMetricsHUDFeatureDescriptor setSelectedIndex:]
+ -[FPMTLMetricsHUDFeatureDescriptor setState:]
+ -[FPMTLMetricsHUDFeatureDescriptor setStringDidChange:]
+ -[FPMTLMetricsHUDFeatureDescriptor setTitle:]
+ -[FPMTLMetricsHUDFeatureDescriptor setValueRef:]
+ -[FPMTLMetricsHUDFeatureDescriptor state]
+ -[FPMTLMetricsHUDFeatureDescriptor stringDidChange]
+ -[FPMTLMetricsHUDFeatureDescriptor title]
+ -[FPMTLMetricsHUDFeatureDescriptor type]
+ -[FPMTLMetricsHUDFeatureDescriptor valueRef]
+ -[FPMTLMetricsMTLLayerDrawableStateObj .cxx_destruct]
+ -[FPMTLMetricsMTLLayerDrawableStateObj drawableState]
+ -[FPMTLMetricsMTLLayerDrawableStateObj init]
+ -[FPMTLMetricsMTLLayerDrawableStateObj metrics]
+ -[FPMTLMetricsMTLLayerDrawableStateObj setSurface:]
+ -[FPMTLMetricsMTLLayerDrawableStateObj surface]
+ -[FPMTLMetricsMTLLayerTracking .cxx_destruct]
+ -[FPMTLMetricsMTLLayerTracking _drawableDidComposite:surfaceID:compositedTime:detachCode:]
+ -[FPMTLMetricsMTLLayerTracking _drawableDidPresent:presentedDrawableTime:hasMetalFXFrameInterpolator:]
+ -[FPMTLMetricsMTLLayerTracking _handleFrameBoundary:]
+ -[FPMTLMetricsMTLLayerTracking _initCommon]
+ -[FPMTLMetricsMTLLayerTracking _snapshotDrawable:imageQueueID:presentedTime:surface:state:]
+ -[FPMTLMetricsMTLLayerTracking _updateDetachState:detachCode:]
+ -[FPMTLMetricsMTLLayerTracking drawableComposited:surfaceID:compositedTime:detachCode:]
+ -[FPMTLMetricsMTLLayerTracking drawableFinish:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:]
+ -[FPMTLMetricsMTLLayerTracking drawablePresented:presentedDrawableTime:hasMetalFXFrameInterpolator:]
+ -[FPMTLMetricsMTLLayerTracking drawableStart:surfaceID:startTime:acquiredTime:]
+ -[FPMTLMetricsMTLLayerTracking drawableStateForDrawable:]
+ -[FPMTLMetricsMTLLayerTracking estimatedRecentAverageFrameInterval]
+ -[FPMTLMetricsMTLLayerTracking initWithLayer:frameNumber:]
+ -[FPMTLMetricsMTLLayerTracking isMainLayer]
+ -[FPMTLMetricsMTLLayerTracking layerAddress]
+ -[FPMTLMetricsMTLLayerTracking layerState]
+ -[FPMTLMetricsMTLLayerTracking setIsMainLayer:]
+ -[FPMTLMetricsMTLLayerTracking setName:]
+ -[FPMTLMetricsMTLLayerTracking setPixelFormat:]
+ -[FPMTLMetricsMTLLayerTracking setWidth:height:]
+ -[FPMTLMetricsMetricListenerObjectInternal .cxx_destruct]
+ -[FPMTLMetricsMetricListenerObjectInternal init:]
+ -[FPMTLMetricsMetricListenerObjectInternal listener]
+ -[FPMTLMetricsMetricListenerObjectInternal setListener:]
+ -[FPMTLMetricsMetricsBundleInternal copy]
+ -[FPMTLMetricsMetricsBundleInternal enabledFacets]
+ -[FPMTLMetricsMetricsBundleInternal encoderMetrics]
+ -[FPMTLMetricsMetricsBundleInternal gptkMetrics]
+ -[FPMTLMetricsMetricsBundleInternal gpuCounterMetrics]
+ -[FPMTLMetricsMetricsBundleInternal ioReportMetrics]
+ -[FPMTLMetricsMetricsBundleInternal isFacetEnabled:]
+ -[FPMTLMetricsMetricsBundleInternal metalFXMetrics]
+ -[FPMTLMetricsMetricsBundleInternal metalLayerMetrics]
+ -[FPMTLMetricsMetricsBundleInternal performanceInsightsMetrics]
+ -[FPMTLMetricsMetricsBundleInternal setEnabledFacets:]
+ -[FPMTLMetricsMetricsBundleInternal setEncoderMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setGptkMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setGpuCounterMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setIoReportMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setMetalFXMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setMetalLayerMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setPerformanceInsightsMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal setShaderCompilerMetrics:]
+ -[FPMTLMetricsMetricsBundleInternal shaderCompilerMetrics]
+ -[FPMTLMetricsMetricsBundleInternal updateWithFrameTiming:]
+ -[FPMTLMetricsServiceInternal .cxx_destruct]
+ -[FPMTLMetricsServiceInternal SEMEnabled]
+ -[FPMTLMetricsServiceInternal UTF8StringForName:]
+ -[FPMTLMetricsServiceInternal _canLoadHUD]
+ -[FPMTLMetricsServiceInternal _createMetalFXMetricsIfNeeded]
+ -[FPMTLMetricsServiceInternal _interposeSyncState]
+ -[FPMTLMetricsServiceInternal _parseScalingMethodForMetrics:metrics:]
+ -[FPMTLMetricsServiceInternal _registerHUDLoaderIfNeeded]
+ -[FPMTLMetricsServiceInternal _shouldEnableTracking]
+ -[FPMTLMetricsServiceInternal _updateGPTKState:]
+ -[FPMTLMetricsServiceInternal _updateMetalFXState:]
+ -[FPMTLMetricsServiceInternal addGPUTimingListener:]
+ -[FPMTLMetricsServiceInternal addGraph:after:min:max:]
+ -[FPMTLMetricsServiceInternal addInsight:isPrototype:]
+ -[FPMTLMetricsServiceInternal addInsight:name:category:message:documtationTitles:documentLinks:supportedAPI:options:isPrototype:]
+ -[FPMTLMetricsServiceInternal addInsightGroup:]
+ -[FPMTLMetricsServiceInternal addLabel:after:]
+ -[FPMTLMetricsServiceInternal addMetric:name:unit:nameColor:valueColor:visualType:options:]
+ -[FPMTLMetricsServiceInternal addMetricsListener:]
+ -[FPMTLMetricsServiceInternal addStatistic:after:color:tolerance:graph:]
+ -[FPMTLMetricsServiceInternal config]
+ -[FPMTLMetricsServiceInternal disableExplicitFrameBoundary]
+ -[FPMTLMetricsServiceInternal enableFacet:enabled:]
+ -[FPMTLMetricsServiceInternal enableInsight:enabled:]
+ -[FPMTLMetricsServiceInternal enabledFacets]
+ -[FPMTLMetricsServiceInternal enumerateTopCommandBuffersWithLabel:]
+ -[FPMTLMetricsServiceInternal enumerateTopEncodersWithLabel:]
+ -[FPMTLMetricsServiceInternal featureRegisterButton:title:description:documtationTitles:documentLinks:options:didChange:]
+ -[FPMTLMetricsServiceInternal featureRegisterPopover:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:items:selectedIndex:didChange:]
+ -[FPMTLMetricsServiceInternal featureRegisterSlider:title:envVar:description:documtationTitles:documentLinks:options:minValue:maxValue:defaultValue:numberOfTicks:didChange:]
+ -[FPMTLMetricsServiceInternal featureRegisterTextbox:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:didChange:]
+ -[FPMTLMetricsServiceInternal featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:didChange:]
+ -[FPMTLMetricsServiceInternal featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:valueRef:]
+ -[FPMTLMetricsServiceInternal gameModeEnabled]
+ -[FPMTLMetricsServiceInternal gameModeSupportState]
+ -[FPMTLMetricsServiceInternal getInsight:]
+ -[FPMTLMetricsServiceInternal getMetric:]
+ -[FPMTLMetricsServiceInternal globalMetrics]
+ -[FPMTLMetricsServiceInternal gptkDeviceCreated:graphicsAPI:]
+ -[FPMTLMetricsServiceInternal gptkExecName]
+ -[FPMTLMetricsServiceInternal gptkFeatureFlags]
+ -[FPMTLMetricsServiceInternal graphicsAPI]
+ -[FPMTLMetricsServiceInternal hasMainLayer]
+ -[FPMTLMetricsServiceInternal hasMetal4APIUsage]
+ -[FPMTLMetricsServiceInternal hasMetalMetrics]
+ -[FPMTLMetricsServiceInternal hudService]
+ -[FPMTLMetricsServiceInternal incrementStatistic:value:]
+ -[FPMTLMetricsServiceInternal init]
+ -[FPMTLMetricsServiceInternal insertMetric:after:name:unit:nameColor:valueColor:visualType:options:]
+ -[FPMTLMetricsServiceInternal insightGroups]
+ -[FPMTLMetricsServiceInternal interposeEnableCompilerStats:]
+ -[FPMTLMetricsServiceInternal interposeEnableEncoderCPU:]
+ -[FPMTLMetricsServiceInternal interposeEnableEncoderGPUTimeSampling:]
+ -[FPMTLMetricsServiceInternal interposeEnableIOReport:]
+ -[FPMTLMetricsServiceInternal interposeGetCompilerStatsDict]
+ -[FPMTLMetricsServiceInternal interposeGetDetachCode:]
+ -[FPMTLMetricsServiceInternal interposeGetMTLAllocatedSize]
+ -[FPMTLMetricsServiceInternal isFacetEnabled:]
+ -[FPMTLMetricsServiceInternal isHUDElementEnabled:]
+ -[FPMTLMetricsServiceInternal isInGPTk]
+ -[FPMTLMetricsServiceInternal isInsightEnabled:]
+ -[FPMTLMetricsServiceInternal isInternalInstall]
+ -[FPMTLMetricsServiceInternal isMetricEnabled:]
+ -[FPMTLMetricsServiceInternal isSideLoaded]
+ -[FPMTLMetricsServiceInternal isTranslated]
+ -[FPMTLMetricsServiceInternal lastTargetRebindingInsightContext]
+ -[FPMTLMetricsServiceInternal loadHUDIfNeeded]
+ -[FPMTLMetricsServiceInternal mainLayer]
+ -[FPMTLMetricsServiceInternal markAccelerationStructureEncoder:component:]
+ -[FPMTLMetricsServiceInternal markBlitEncoder:component:]
+ -[FPMTLMetricsServiceInternal markCommandBuffer:component:]
+ -[FPMTLMetricsServiceInternal markComputeEncoder:component:]
+ -[FPMTLMetricsServiceInternal markExplicitFrameBoundary]
+ -[FPMTLMetricsServiceInternal markMainLayer:]
+ -[FPMTLMetricsServiceInternal markRenderEncoder:component:]
+ -[FPMTLMetricsServiceInternal markResourceStateEncoder:component:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferBegin:beginTimeInSec:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferCommited:queueAddress:generation:commitTimeInSec:label:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferCompleted:queueAddress:generation:gpuStartTimeInSec:gpuEndTimeInSec:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferCreated:creationTimeInSec:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferDeallocated:]
+ -[FPMTLMetricsServiceInternal metal4CommandBufferEnd:endTimeInSec:allocatorId:allocatedSize:]
+ -[FPMTLMetricsServiceInternal metalAddEncoder:encoderTraceId:encoderType:counterSampleOffset:timeMAT:metadata:]
+ -[FPMTLMetricsServiceInternal metalCommandBufferCommited:commitTimeInSec:]
+ -[FPMTLMetricsServiceInternal metalCommandBufferCompleted:gpuStartTimeInSec:gpuEndTimeInSec:]
+ -[FPMTLMetricsServiceInternal metalCommandBufferCreated:creationTimeInSec:]
+ -[FPMTLMetricsServiceInternal metalCommandBufferScheduled:kernelStartTimeInSec:kernelEndTimeInSec:]
+ -[FPMTLMetricsServiceInternal metalCompilerFunctionCompiled:functionType:async:wasCached:compileTimeMAT:performanceStatistics:]
+ -[FPMTLMetricsServiceInternal metalCompilerPipelineStateCreated:async:compileTimeMAT:performanceStatistics:]
+ -[FPMTLMetricsServiceInternal metalDeviceCreatedWithFramePacingVersion:]
+ -[FPMTLMetricsServiceInternal metalEncoderEnd:encoderTraceId:timeMAT:label:commandBufferLabel:]
+ -[FPMTLMetricsServiceInternal metalFXFrameInterpolatorEncoded:commandBufferAddress:deltaTime:]
+ -[FPMTLMetricsServiceInternal metalFXFrameInterpolatorEncodingEnd:]
+ -[FPMTLMetricsServiceInternal metalFXInterpolatorPerformance:]
+ -[FPMTLMetricsServiceInternal metalFXScalerEncoded:commandBufferAddress:scalingMethod:version:scalingDevice:inputWidth:inputHeight:targetWidth:targetHeight:exposure:autoExposureEnabled:]
+ -[FPMTLMetricsServiceInternal metalFXScalingPerformance:]
+ -[FPMTLMetricsServiceInternal metalGetEncoderCounterOffset:encoderTraceId:]
+ -[FPMTLMetricsServiceInternal metalLayerAlloc:]
+ -[FPMTLMetricsServiceInternal metalLayerDealloc:]
+ -[FPMTLMetricsServiceInternal metalLayerDrawableDidComposite:drawableID:surfaceID:compositedTime:detachCode:]
+ -[FPMTLMetricsServiceInternal metalLayerDrawableDidPresent:drawableID:presentedDrawableTime:]
+ -[FPMTLMetricsServiceInternal metalLayerDrawableFinish:imageQueueID:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:]
+ -[FPMTLMetricsServiceInternal metalLayerDrawableStart:surfaceID:drawableID:acquisitionWaitStartTime:acquiredTime:]
+ -[FPMTLMetricsServiceInternal metalLayerSetName:name:]
+ -[FPMTLMetricsServiceInternal metalLayerSetPixelFormat:pixelFormat:]
+ -[FPMTLMetricsServiceInternal metalLayerSetSize:width:height:]
+ -[FPMTLMetricsServiceInternal metalSetEncoderTimestampResolver:]
+ -[FPMTLMetricsServiceInternal numberOfTopLabeledCommandBuffers]
+ -[FPMTLMetricsServiceInternal numberOfTopLabeledEncoders]
+ -[FPMTLMetricsServiceInternal progName]
+ -[FPMTLMetricsServiceInternal remove:]
+ -[FPMTLMetricsServiceInternal removeGPUTimingListener:]
+ -[FPMTLMetricsServiceInternal removeMetric:]
+ -[FPMTLMetricsServiceInternal removeMetricsListener:]
+ -[FPMTLMetricsServiceInternal removeRegisteredFeature:]
+ -[FPMTLMetricsServiceInternal requestGroupedMetrics]
+ -[FPMTLMetricsServiceInternal resetMetricHistory:]
+ -[FPMTLMetricsServiceInternal setGlobalMetrics:]
+ -[FPMTLMetricsServiceInternal setGraphicsAPI:]
+ -[FPMTLMetricsServiceInternal setHUDElementEnabled:flag:]
+ -[FPMTLMetricsServiceInternal setHasMainLayer:]
+ -[FPMTLMetricsServiceInternal setHudService:]
+ -[FPMTLMetricsServiceInternal setMainLayer:]
+ -[FPMTLMetricsServiceInternal setMetricEnabled:enabled:]
+ -[FPMTLMetricsServiceInternal setMetricProcessingQueue:]
+ -[FPMTLMetricsServiceInternal setShaderCompiledHandler:]
+ -[FPMTLMetricsServiceInternal setStatistic:value:]
+ -[FPMTLMetricsServiceInternal shaderCompiledHandler]
+ -[FPMTLMetricsServiceInternal totalCompilerStatistics]
+ -[FPMTLMetricsServiceInternal updateFloatMetric:value:]
+ -[FPMTLMetricsServiceInternal updateIntegerMetric:value:]
+ -[FPMTLMetricsServiceInternal updateLabel:value:]
+ -[FPMTLMetricsServiceInternal updateLabelMetric:label:]
+ -[FPMTLMetricsServiceInternal updateMetricColor:nameColor:valueColor:]
+ -[FPMTLMetricsServiceInternal updateMetricName:name:]
+ -[FPMTLMetricsServiceInternal updateMetricOptions:options:]
+ -[FPMTLMetricsServiceInternal version]
+ -[_CADeveloperHUDProperties init]
+ GCC_except_table101
+ GCC_except_table102
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table12
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table200
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table3
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table7
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table9
+ GCC_except_table90
+ GCC_except_table97
+ GCC_except_table98
+ _.str.105
+ _.str.247
+ _CFBundleGetIdentifier
+ _CFBundleGetMainBundle
+ _CFStringCompare
+ _FPDrawableLifetimeMarkComposited
+ _FPGPTkDeviceCreated
+ _FPMTL4CommandBufferBegin
+ _FPMTL4CommandBufferCommitted
+ _FPMTL4CommandBufferCompleted
+ _FPMTL4CommandBufferCreated
+ _FPMTL4CommandBufferDealloc
+ _FPMTL4CommandBufferEnd
+ _FPMTLCompilerFunctionCompiled
+ _FPMTLCompilerPipelineStateCreated
+ _FPMTLDeviceCreatedWithFramePacingVersion
+ _FPMTLMetricsAbsoluteTimeInNs
+ _FPMTLMetricsBarrierInsightCheck
+ _FPMTLMetricsCompilerInsightHandleCompilerStatistics
+ _FPMTLMetricsDispatchQueueAsync
+ _FPMTLMetricsEncoderTypeName.names
+ _FPMTLMetricsGPUTimeTrackerCommandBufferCommit
+ _FPMTLMetricsGPUTimeTrackerCommandBufferCreate
+ _FPMTLMetricsGPUTimeTrackerEnableCompilerStatsReporting
+ _FPMTLMetricsGPUTimeTrackerEnableEncoderGPUTimeSampling
+ _FPMTLMetricsGPUTimeTrackerEncoderEnd
+ _FPMTLMetricsGPUTimeTrackerEnumerateTopCommandBufferRecords
+ _FPMTLMetricsGPUTimeTrackerEnumerateTopEncoderRecords
+ _FPMTLMetricsGPUTimeTrackerFramePresented
+ _FPMTLMetricsGPUTimeTrackerGetEncoderCounterOffset
+ _FPMTLMetricsGPUTimeTrackerGetGlobalInstance
+ _FPMTLMetricsGPUTimeTrackerMTL4CommandBufferBegin
+ _FPMTLMetricsGPUTimeTrackerMTL4CommandBufferCommit
+ _FPMTLMetricsGPUTimeTrackerMTL4CommandBufferCreate
+ _FPMTLMetricsGPUTimeTrackerMTL4CommandBufferDealloc
+ _FPMTLMetricsGPUTimeTrackerMTL4CommandBufferEnd
+ _FPMTLMetricsGPUTimeTrackerMTLCompilerFunctionCompiled
+ _FPMTLMetricsGPUTimeTrackerMTLCompilerPipelineStateCreated
+ _FPMTLMetricsGPUTimeTrackerMarkCommandBuffer
+ _FPMTLMetricsGPUTimeTrackerMarkFrameBoundary
+ _FPMTLMetricsGPUTimeTrackerReset
+ _FPMTLMetricsGPUTimeTrackerSetEncoderTimestampResolver
+ _FPMTLMetricsGPUTimeTrackerSetInsightsEnabled
+ _FPMTLMetricsGPUTimeTrackerSetShaderCompiledHandler
+ _FPMTLMetricsGameModeEnabled
+ _FPMTLMetricsGameModeInsightCheck
+ _FPMTLMetricsGameModeInsightCheck.lastReportTime
+ _FPMTLMetricsGetGameModeKeyState
+ _FPMTLMetricsGetGameModeKeyState.onceToken
+ _FPMTLMetricsGetGameModeKeyState.state
+ _FPMTLMetricsInsightsCreatePrototypes
+ _FPMTLMetricsInsightsCreatePrototypes.onceToken
+ _FPMTLMetricsIsDebuggerAttached
+ _FPMTLMetricsIsExcluded
+ _FPMTLMetricsIsInternalInstall
+ _FPMTLMetricsIsProcessTranslated
+ _FPMTLMetricsIsProcessTranslated.onceToken
+ _FPMTLMetricsIsSideLoadedApp
+ _FPMTLMetricsMTLPixelFormatName
+ _FPMTLMetricsMetricValueAddValue
+ _FPMTLMetricsNotificationQueueAsync
+ _FPMTLMetricsSEMEnabled
+ _FPMTLMetricsTargetRebindingInsightContextBeginFrame
+ _FPMTLMetricsTargetRebindingInsightContextInit
+ _FPMTLMetricsTargetRebindingInsightContextNextFrame
+ _FPMTLMetricsTargetRebindingInsightContextProcessCommandBuffer
+ _FPMTLMetricsTargetRebindingInsightContextProcessEncoder
+ _FPMTLMetricsTessellationInsightCheck
+ _FPMetalFXFrameInterpolatorEncoded
+ _FPMetalFXReportInterpolatorPerformance
+ _FPMetalFXReportScalingPerformance
+ _FPMetalFXScalingEncoded
+ _FPRUsageTimestampToTimeInterval
+ _FPRUsageTimestampToTimeInterval.onceToken
+ _FP_MTL_METRICS_MTLCompileTimeStatisticsKeyPipelinesCompute
+ _FP_MTL_METRICS_MTLCompileTimeStatisticsKeyPipelinesRender
+ _MGGetBoolAnswer
+ _MetalMetricsInterposeDylibOpen
+ _NSLog
+ _OBJC_CLASS_$_FPCAMetalLayerAggregatedStats
+ _OBJC_CLASS_$_FPCAMetalLayerAggregatedStatsGPTK
+ _OBJC_CLASS_$_FPCAMetalLayerAggregatedStatsShaderCompiler
+ _OBJC_CLASS_$_FPMTLMetricsClientInsight
+ _OBJC_CLASS_$_FPMTLMetricsClientInsightGroup
+ _OBJC_CLASS_$_FPMTLMetricsClientMetricCollection
+ _OBJC_CLASS_$_FPMTLMetricsClientMetricDescriptor
+ _OBJC_CLASS_$_FPMTLMetricsClientMetricDescriptorGroup
+ _OBJC_CLASS_$_FPMTLMetricsClientMetricValue
+ _OBJC_CLASS_$_FPMTLMetricsGPUTimingListenerObjectInternal
+ _OBJC_CLASS_$_FPMTLMetricsHUDFeatureDescriptor
+ _OBJC_CLASS_$_FPMTLMetricsMTLLayerDrawableStateObj
+ _OBJC_CLASS_$_FPMTLMetricsMTLLayerTracking
+ _OBJC_CLASS_$_FPMTLMetricsMetricListenerObjectInternal
+ _OBJC_CLASS_$_FPMTLMetricsMetricsBundleInternal
+ _OBJC_CLASS_$_FPMTLMetricsServiceInternal
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$__CADeveloperHUDProperties
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._commandBufferCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._cpuWalltimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._detachCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._endToEndDrawableLifetimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._gptkMetrics
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._gpuFinishToPresentLatencyStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._gpuWalltimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._hasMetalFXMetrics
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._isSkippedFrameStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXAutoExposureEnabledCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXDenoisingScalingCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXEnabledCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXExposureStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXFrameInterpolatorDeltaTimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXFrameInterpolatorEnabledCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXScalingDeviceCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXScalingMethodCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXScalingOnANECount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXScalingOnGPUCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXScalingRatioStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXSpatialScalingCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._metalFXTemporalScalingCount
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._nextDrawableWaitTimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._onGPUTimeStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._onScreenStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStats._shaderCompilerStatMetrics
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkAccelerationEncoderCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkBlitEncoderCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkBuildBVHCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkClearCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkCommandBufferCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkComputeEncoderCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkCopyCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkDispatchCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkDispatchMeshCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkDispatchRaysCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkExecuteIndirectCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkFragmentDrawCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkGeometryDrawCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkGeometryTessDrawCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkRayQueryCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkRefitBVHCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkRenderEncoderCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsGPTK._gptkTessellationDrawCountStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._numCachedCompilations
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._numCompilations
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._numPipelineStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._shaderCompilationTime
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._totalNumCachedCompilations
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._totalNumCompilations
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._totalNumPipelineStats
+ _OBJC_IVAR_$_FPCAMetalLayerAggregatedStatsShaderCompiler._totalShaderCompilationTime
+ _OBJC_IVAR_$_FPCAMetalLayerState._presentedStats
+ _OBJC_IVAR_$_FPCAMetalLayerState._skippedStats
+ _OBJC_IVAR_$_FPInFlightDrawableLifetime._compositedTime
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._component
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._descriptor
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._enabled
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._numInstances
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._timeCreated
+ _OBJC_IVAR_$_FPMTLMetricsClientInsight._timeUpdated
+ _OBJC_IVAR_$_FPMTLMetricsClientInsightGroup._category
+ _OBJC_IVAR_$_FPMTLMetricsClientInsightGroup._enabled
+ _OBJC_IVAR_$_FPMTLMetricsClientInsightGroup._insights
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricCollection._descriptorGroups
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricCollection._valueMap
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricCollection._values
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._descriptorIndex
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._identifier
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._maxValueAllowed
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._minValueAllowed
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._name
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._nameColor
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._options
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._reportingComponent
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._unit
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._unitType
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._valueColor
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._valueIndex
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptor._visualType
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptorGroup._component
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricDescriptorGroup._descriptorIndexes
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._component
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._descriptor
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._enabled
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._hidden
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._lastUpdateTime
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._stringValueBacking
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._valueBacking
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._valueHistory
+ _OBJC_IVAR_$_FPMTLMetricsClientMetricValue._valueType
+ _OBJC_IVAR_$_FPMTLMetricsGPUTimingListenerObjectInternal._listener
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._component
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._defaultValue
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._didChange
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._documentationLinks
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._documentationTitles
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._envVar
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._featureDescription
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._identifier
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._items
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._maxValue
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._minValue
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._numberOfTicks
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._options
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._selectedIndex
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._state
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._stringDidChange
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._title
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._type
+ _OBJC_IVAR_$_FPMTLMetricsHUDFeatureDescriptor._valueRef
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerDrawableStateObj._drawableState
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerDrawableStateObj._metrics
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerDrawableStateObj._surface
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._currentDrawableStateIndex
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._drawableIDToStateIndex
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._drawableStates
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._layerAddress
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._layerState
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._metalFXFrameInterpolatorWaitCounter
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._recentPresentFrameNumber
+ _OBJC_IVAR_$_FPMTLMetricsMTLLayerTracking._recentPresentTime
+ _OBJC_IVAR_$_FPMTLMetricsMetricListenerObjectInternal._listener
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._caMetalLayerMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._enabledFacets
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._encoderMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._gptkMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._gpuCounterMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._ioReportMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._metalFXMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._perfInsightsMetrics
+ _OBJC_IVAR_$_FPMTLMetricsMetricsBundleInternal._shaderCompilerMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._canEnableIOReport
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._enabledFacets
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._featureDescriptors
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._globalMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._gptkExecName
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._gptkFeatureFlags
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._gptkMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._gptkNameToMetricOffset
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._gpuTiminglisteners
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._graphicsAPI
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasFPGPTk
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasFPMetalFX
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasHUDNotificationHandler
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasIOReportMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasMainLayer
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hasMetal4APIUsage
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._hudService
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._insightGroupMap
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._insightGroups
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._insightMap
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._ioReportMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._isInGPTk
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._listeners
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._metalFXStat
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._perLayerMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._perfInsightMetrics
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._presentCount
+ _OBJC_IVAR_$_FPMTLMetricsServiceInternal._shaderCompiledHandler
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._detached
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._drawableID
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._gptkMetrics
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._hasGPTKMetrics
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._hasMetalFXMetrics
+ _OBJC_IVAR_$_FPOnGlassCAMetalLayerDrawableInterval._metalFXMetrics
+ _OBJC_METACLASS_$_FPCAMetalLayerAggregatedStats
+ _OBJC_METACLASS_$_FPCAMetalLayerAggregatedStatsGPTK
+ _OBJC_METACLASS_$_FPCAMetalLayerAggregatedStatsShaderCompiler
+ _OBJC_METACLASS_$_FPMTLMetricsClientInsight
+ _OBJC_METACLASS_$_FPMTLMetricsClientInsightGroup
+ _OBJC_METACLASS_$_FPMTLMetricsClientMetricCollection
+ _OBJC_METACLASS_$_FPMTLMetricsClientMetricDescriptor
+ _OBJC_METACLASS_$_FPMTLMetricsClientMetricDescriptorGroup
+ _OBJC_METACLASS_$_FPMTLMetricsClientMetricValue
+ _OBJC_METACLASS_$_FPMTLMetricsGPUTimingListenerObjectInternal
+ _OBJC_METACLASS_$_FPMTLMetricsHUDFeatureDescriptor
+ _OBJC_METACLASS_$_FPMTLMetricsMTLLayerDrawableStateObj
+ _OBJC_METACLASS_$_FPMTLMetricsMTLLayerTracking
+ _OBJC_METACLASS_$_FPMTLMetricsMetricListenerObjectInternal
+ _OBJC_METACLASS_$_FPMTLMetricsMetricsBundleInternal
+ _OBJC_METACLASS_$_FPMTLMetricsServiceInternal
+ _OBJC_METACLASS_$__CADeveloperHUDProperties
+ __FPGetCurrentShaderCompilerStatSignpostsEnabled
+ __FPMTLMetricsBarrierInsightReport
+ __FPMTLMetricsCompilerStatInsightReport
+ __FPMTLMetricsDispatchQueueGet
+ __FPMTLMetricsDispatchQueueGet.onceToken
+ __FPMTLMetricsGameModeInsightReport
+ __FPMTLMetricsMetal3To4EfficientEncoderInsightReport
+ __FPMTLMetricsNotificationQueueGet
+ __FPMTLMetricsNotificationQueueGet.onceToken
+ __FPMTLMetricsTargetBlitInsightReport
+ __FPMTLMetricsTargetRebindCheckRenderEncoderGroup
+ __FPMTLMetricsTargetRebindingInsightReport
+ __FPMTLMetricsTessellationInsightReport
+ __FPSetCurrentShaderCompilerStatSignpostsEnabled
+ __OBJC_$_CLASS_METHODS_FPMTLMetricsMTLLayerTracking
+ __OBJC_$_CLASS_METHODS_FPMTLMetricsServiceInternal
+ __OBJC_$_CLASS_METHODS__CADeveloperHUDProperties
+ __OBJC_$_INSTANCE_METHODS_FPCAMetalLayerAggregatedStats
+ __OBJC_$_INSTANCE_METHODS_FPCAMetalLayerAggregatedStatsGPTK
+ __OBJC_$_INSTANCE_METHODS_FPCAMetalLayerAggregatedStatsShaderCompiler
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientInsight
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientInsightGroup
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientMetricCollection
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientMetricDescriptor
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientMetricDescriptorGroup
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsClientMetricValue
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsGPUTimingListenerObjectInternal
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsHUDFeatureDescriptor
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsMTLLayerDrawableStateObj
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsMTLLayerTracking
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsMetricListenerObjectInternal
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsMetricsBundleInternal
+ __OBJC_$_INSTANCE_METHODS_FPMTLMetricsServiceInternal
+ __OBJC_$_INSTANCE_METHODS__CADeveloperHUDProperties
+ __OBJC_$_INSTANCE_VARIABLES_FPCAMetalLayerAggregatedStats
+ __OBJC_$_INSTANCE_VARIABLES_FPCAMetalLayerAggregatedStatsGPTK
+ __OBJC_$_INSTANCE_VARIABLES_FPCAMetalLayerAggregatedStatsShaderCompiler
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientInsight
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientInsightGroup
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientMetricCollection
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientMetricDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientMetricDescriptorGroup
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsClientMetricValue
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsGPUTimingListenerObjectInternal
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsHUDFeatureDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsMTLLayerDrawableStateObj
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsMTLLayerTracking
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsMetricListenerObjectInternal
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsMetricsBundleInternal
+ __OBJC_$_INSTANCE_VARIABLES_FPMTLMetricsServiceInternal
+ __OBJC_$_PROP_LIST_FPMTLMetricsClientInsight
+ __OBJC_$_PROP_LIST_FPMTLMetricsClientInsightGroup
+ __OBJC_$_PROP_LIST_FPMTLMetricsClientMetricDescriptor
+ __OBJC_$_PROP_LIST_FPMTLMetricsClientMetricDescriptorGroup
+ __OBJC_$_PROP_LIST_FPMTLMetricsClientMetricValue
+ __OBJC_$_PROP_LIST_FPMTLMetricsGPUTimingListenerObjectInternal
+ __OBJC_$_PROP_LIST_FPMTLMetricsHUDFeatureDescriptor
+ __OBJC_$_PROP_LIST_FPMTLMetricsMTLLayerDrawableStateObj
+ __OBJC_$_PROP_LIST_FPMTLMetricsMTLLayerTracking
+ __OBJC_$_PROP_LIST_FPMTLMetricsMetricListenerObjectInternal
+ __OBJC_$_PROP_LIST_FPMTLMetricsMetricsBundleInternal
+ __OBJC_$_PROP_LIST_FPMTLMetricsServiceInternal
+ __OBJC_$_PROP_LIST_FPMTLMetricsServiceInternalGPTk
+ __OBJC_$_PROP_LIST_FPMTLMetricsServiceInternalHUD
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMTLMetricsServiceInternalFP
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMTLMetricsServiceInternalGPTk
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMTLMetricsServiceInternalHUD
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMTLMetricsServiceInternalInterposer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMTLMetricsServiceInternalMetalFX
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMTLMetricsServiceInternalFP
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMTLMetricsServiceInternalGPTk
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMTLMetricsServiceInternalHUD
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMTLMetricsServiceInternalInterposer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMTLMetricsServiceInternalMetalFX
+ __OBJC_CLASS_PROTOCOLS_$_FPMTLMetricsServiceInternal
+ __OBJC_CLASS_RO_$_FPCAMetalLayerAggregatedStats
+ __OBJC_CLASS_RO_$_FPCAMetalLayerAggregatedStatsGPTK
+ __OBJC_CLASS_RO_$_FPCAMetalLayerAggregatedStatsShaderCompiler
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientInsight
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientInsightGroup
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientMetricCollection
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientMetricDescriptor
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientMetricDescriptorGroup
+ __OBJC_CLASS_RO_$_FPMTLMetricsClientMetricValue
+ __OBJC_CLASS_RO_$_FPMTLMetricsGPUTimingListenerObjectInternal
+ __OBJC_CLASS_RO_$_FPMTLMetricsHUDFeatureDescriptor
+ __OBJC_CLASS_RO_$_FPMTLMetricsMTLLayerDrawableStateObj
+ __OBJC_CLASS_RO_$_FPMTLMetricsMTLLayerTracking
+ __OBJC_CLASS_RO_$_FPMTLMetricsMetricListenerObjectInternal
+ __OBJC_CLASS_RO_$_FPMTLMetricsMetricsBundleInternal
+ __OBJC_CLASS_RO_$_FPMTLMetricsServiceInternal
+ __OBJC_CLASS_RO_$__CADeveloperHUDProperties
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsService
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsServiceInternalFP
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsServiceInternalGPTk
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsServiceInternalHUD
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsServiceInternalInterposer
+ __OBJC_LABEL_PROTOCOL_$_FPMTLMetricsServiceInternalMetalFX
+ __OBJC_METACLASS_RO_$_FPCAMetalLayerAggregatedStats
+ __OBJC_METACLASS_RO_$_FPCAMetalLayerAggregatedStatsGPTK
+ __OBJC_METACLASS_RO_$_FPCAMetalLayerAggregatedStatsShaderCompiler
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientInsight
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientInsightGroup
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientMetricCollection
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientMetricDescriptor
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientMetricDescriptorGroup
+ __OBJC_METACLASS_RO_$_FPMTLMetricsClientMetricValue
+ __OBJC_METACLASS_RO_$_FPMTLMetricsGPUTimingListenerObjectInternal
+ __OBJC_METACLASS_RO_$_FPMTLMetricsHUDFeatureDescriptor
+ __OBJC_METACLASS_RO_$_FPMTLMetricsMTLLayerDrawableStateObj
+ __OBJC_METACLASS_RO_$_FPMTLMetricsMTLLayerTracking
+ __OBJC_METACLASS_RO_$_FPMTLMetricsMetricListenerObjectInternal
+ __OBJC_METACLASS_RO_$_FPMTLMetricsMetricsBundleInternal
+ __OBJC_METACLASS_RO_$_FPMTLMetricsServiceInternal
+ __OBJC_METACLASS_RO_$__CADeveloperHUDProperties
+ __OBJC_PROTOCOL_$_FPMTLMetricsService
+ __OBJC_PROTOCOL_$_FPMTLMetricsServiceInternalFP
+ __OBJC_PROTOCOL_$_FPMTLMetricsServiceInternalGPTk
+ __OBJC_PROTOCOL_$_FPMTLMetricsServiceInternalHUD
+ __OBJC_PROTOCOL_$_FPMTLMetricsServiceInternalInterposer
+ __OBJC_PROTOCOL_$_FPMTLMetricsServiceInternalMetalFX
+ __Unwind_Resume
+ __Z20_HUDTimeRangeComparePKvS0_
+ __Z35_FPMTLMetricsGPUTimeTrackerAddLabelP26FPMTLMetricsGPUTimeTrackeryP8NSStringm36FPMTLMetricsGPUTimeTrackerObjectType
+ __Z37_FPMTLMetricsGPUTimeTrackerAddEncoderP26FPMTLMetricsGPUTimeTrackeryy23FPMTLMetricsEncoderTypemdP27FPMTLMetricsEncoderMetadata
+ __Z37_FPMTLMetricsGPUTimeTrackerEndEncoderP26FPMTLMetricsGPUTimeTrackeryydP8NSStringS2_
+ __Z40_FPMTLMetricsCompilerStatisticsParseDictP12NSDictionaryP8NSStringP30FPMTLMetricsCompilerStatisticsU13block_pointerFvP22FPMTLMetricsShaderInfoE
+ __Z44_FPMTLMetricsGPUTimeTrackerPushTopObjectHeapP39FPMTLMetricsGPUTimeTrackerTopObjectHeapP44FPMTLMetricsGPUTimeTrackerTopObjectHeapValue
+ __Z46_FPMTLMetricsGPUTimeTrackerTopObjectHeapAssignP26FPMTLMetricsGPUTimeTrackerP39FPMTLMetricsGPUTimeTrackerTopObjectHeapPym
+ __Z48_FPMTLMetricsGPUTimeTrackerCommandBufferCompleteP26FPMTLMetricsGPUTimeTrackerydd
+ __Z48_FPMTLMetricsGPUTimeTrackerCommandBufferSnapshotP39FPMTLMetricsGPUTimeTrackerCommandBufferS0_
+ __Z49_FPMTLMetricsGPUTimeTrackerCommandBufferScheduledP26FPMTLMetricsGPUTimeTrackerydd
+ __Z52_FPMTLMetricsGPUTimeTrackerMTL4CommandBufferCompleteP26FPMTLMetricsGPUTimeTrackerddyy
+ __Z55_FPMTLMetricsGPUTimeTrackerEnumerateCommonObjectRecordsP26FPMTLMetricsGPUTimeTracker36FPMTLMetricsGPUTimeTrackerObjectTypeU13block_pointerFvP8NSStringjP44FPMTLMetricsGPUTimeTrackerCommonObjectRecordE
+ __Z58_FPMTLMetricsGPUTimeTrackerWrapupFrameForPresentedDrawableP26FPMTLMetricsGPUTimeTrackermyU13block_pointerFvP41FPMTLMetricsGPUTimeTrackerFrameTimingDataE
+ __ZL54_FPMTLMetricsGPUTimeTrackerMTLCompilerFunctionCompiledP30FPMTLMetricsCompilerStatisticsP8NSStringmbbP8NSNumberP12NSDictionary
+ __ZL56FPMTLMetricsClientMetricReportingComponentFromIdentifierP8NSString
+ __ZL58_FPMTLMetricsGPUTimeTrackerMTLCompilerPipelineStateCreatedP30FPMTLMetricsCompilerStatisticsP8NSStringbP8NSNumberP12NSDictionary
+ __ZN35FPMTLMetricsClientInsightDescriptoraSERKS_
+ __ZN39FPMTLMetricsGPUTimeTrackerCommandBufferD1Ev
+ __ZN46FPMTLMetricsGPUTimeTrackerFrameTimingDataStoreD2Ev
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIy31FPMTLMetricsGPUTimeTrackerLabelEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B9fqe220100Ev
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ46_FPMTLMetricsGPUTimeTrackerTopObjectHeapAssignP26FPMTLMetricsGPUTimeTrackerP39FPMTLMetricsGPUTimeTrackerTopObjectHeapPymE3$_0P44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueLb0EEEvT1_SB_T0_NS_15iterator_traitsISB_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ58_FPMTLMetricsGPUTimeTrackerWrapupFrameForPresentedDrawableP26FPMTLMetricsGPUTimeTrackermyU13block_pointerFvP41FPMTLMetricsGPUTimeTrackerFrameTimingDataEE3$_0P39FPMTLMetricsGPUTimeTrackerCommandBufferLb0EEEvT1_SC_T0_NS_15iterator_traitsISC_E15difference_typeEb
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy31FPMTLMetricsGPUTimeTrackerLabelEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE13__move_assignERSH_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEESO_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE21__construct_node_hashIJRS7_EEENS_10unique_ptrINS_11__hash_nodeIS3_PvEENS_22__hash_node_destructorINSF_ISN_EEEEEEmDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE22__deallocate_node_listB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEEC2EOSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEEC2ERKSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEEaSERKSH_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy44FPMTLMetricsGPUTimeTrackerCommonObjectRecordEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE13__move_assignERSG_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS2_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE16__copy_constructB9fqe220100EPNS_16__hash_node_baseIPNS_11__hash_nodeIS2_PvEEEESN_m
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEEC2EOSG_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEEC2ERKSG_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIymEENS_22__unordered_map_hasherIyNS_4pairIKymEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEEaSERKSG_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyyEENS_22__unordered_map_hasherIyNS_4pairIKyyEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIyPvEEEERKT_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__114__split_bufferI39FPMTLMetricsGPUTimeTrackerCommandBufferRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__116__if_likely_elseB9fqe220100IZNS_6vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS2_EEE12emplace_backIJRKS2_EEERS2_DpOT_EUlvE_ZNS6_IJS8_EEES9_SC_EUlvE0_EEvbT_T0_
+ __ZNSt3__116allocator_traitsINS_9allocatorI39FPMTLMetricsGPUTimeTrackerCommandBufferEEE7destroyB9fqe220100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorI21FPMTLMetricsTimeRangeEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorI33FPMTLMetricsGPUTimeTrackerEncoderEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEEPvEEEEEclB9fqe220100EPS7_
+ __ZNSt3__127__insertion_sort_incompleteB9fqe220100INS_17_ClassicAlgPolicyERZ46_FPMTLMetricsGPUTimeTrackerTopObjectHeapAssignP26FPMTLMetricsGPUTimeTrackerP39FPMTLMetricsGPUTimeTrackerTopObjectHeapPymE3$_0P44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueEEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9fqe220100INS_17_ClassicAlgPolicyERZ58_FPMTLMetricsGPUTimeTrackerWrapupFrameForPresentedDrawableP26FPMTLMetricsGPUTimeTrackermyU13block_pointerFvP41FPMTLMetricsGPUTimeTrackerFrameTimingDataEE3$_0P39FPMTLMetricsGPUTimeTrackerCommandBufferEEbT1_SC_T0_
+ __ZNSt3__14pairIy39FPMTLMetricsGPUTimeTrackerCommandBufferED2Ev
+ __ZNSt3__14swapB9fqe220100I39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS3_EE5valueEvE4typeERS3_S6_
+ __ZNSt3__16vectorI21FPMTLMetricsTimeRangeNS_9allocatorIS1_EEE18__insert_with_sizeB9fqe220100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l
+ __ZNSt3__16vectorI21FPMTLMetricsTimeRangeNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI21FPMTLMetricsTimeRangeNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE11__vallocateB9fqe220100Em
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE13__move_assignERS4_NS_17integral_constantIbLb1EEE
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE16__init_with_sizeB9fqe220100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE18__assign_with_sizeB9fqe220100INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI33FPMTLMetricsGPUTimeTrackerEncoderNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJEEEPS1_DpOT_
+ __ZNSt3__16vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS1_EEE30__emplace_back_assume_capacityB9fqe220100IJRKS1_EEEvDpOT_
+ __ZNSt3__16vectorI39FPMTLMetricsGPUTimeTrackerCommandBufferNS_9allocatorIS1_EEE9push_backB9fqe220100ERKS1_
+ __ZNSt3__17__sort3B9fqe220100INS_17_ClassicAlgPolicyERZ46_FPMTLMetricsGPUTimeTrackerTopObjectHeapAssignP26FPMTLMetricsGPUTimeTrackerP39FPMTLMetricsGPUTimeTrackerTopObjectHeapPymE3$_0P44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueLi0EEEbT1_SB_SB_T0_
+ __ZNSt3__17__sort4B9fqe220100INS_17_ClassicAlgPolicyERZ58_FPMTLMetricsGPUTimeTrackerWrapupFrameForPresentedDrawableP26FPMTLMetricsGPUTimeTrackermyU13block_pointerFvP41FPMTLMetricsGPUTimeTrackerFrameTimingDataEE3$_0P39FPMTLMetricsGPUTimeTrackerCommandBufferLi0EEEvT1_SC_SC_SC_T0_
+ __ZNSt3__17__sort5B9fqe220100INS_17_ClassicAlgPolicyERZ46_FPMTLMetricsGPUTimeTrackerTopObjectHeapAssignP26FPMTLMetricsGPUTimeTrackerP39FPMTLMetricsGPUTimeTrackerTopObjectHeapPymE3$_0P44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueLi0EEEvT1_SB_SB_SB_SB_T0_
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIy39FPMTLMetricsGPUTimeTrackerCommandBufferEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS6_EEENSM_IJEEEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlSN_SL_OSO_OSP_E_clESN_SL_S10_S11_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIy44FPMTLMetricsGPUTimeTrackerTopObjectHeapValueEENS_22__unordered_map_hasherIyNS_4pairIKyS2_EENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS7_SB_S9_EENS_9allocatorIS7_EEE16__emplace_uniqueB9fqe220100IJNS5_IyS2_EEEEENS5_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEEDpOT_ENKUlRS6_OSJ_E_clESU_SV_
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIyyEENS_22__unordered_map_hasherIyNS_4pairIKyyEENS_4hashIyEENS_8equal_toIyEEEENS_21__unordered_map_equalIyS6_SA_S8_EENS_9allocatorIS6_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEEDpOT_ENKUlSM_SK_OSN_OSO_E_clESM_SK_SZ_S10_
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___100-[FPMTLMetricsServiceInternal insertMetric:after:name:unit:nameColor:valueColor:visualType:options:]_block_invoke
+ ___105-[FPMTLMetricsServiceInternal metal4CommandBufferCommited:queueAddress:generation:commitTimeInSec:label:]_block_invoke
+ ___108-[FPMTLMetricsServiceInternal metalCompilerPipelineStateCreated:async:compileTimeMAT:performanceStatistics:]_block_invoke
+ ___111-[FPMTLMetricsServiceInternal metalAddEncoder:encoderTraceId:encoderType:counterSampleOffset:timeMAT:metadata:]_block_invoke
+ ___118-[FPMTLMetricsServiceInternal metal4CommandBufferCompleted:queueAddress:generation:gpuStartTimeInSec:gpuEndTimeInSec:]_block_invoke
+ ___121-[FPMTLMetricsServiceInternal featureRegisterButton:title:description:documtationTitles:documentLinks:options:didChange:]_block_invoke
+ ___127-[FPMTLMetricsServiceInternal metalCompilerFunctionCompiled:functionType:async:wasCached:compileTimeMAT:performanceStatistics:]_block_invoke
+ ___142-[FPMTLMetricsServiceInternal featureRegisterTextbox:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:didChange:]_block_invoke
+ ___146-[FPMTLMetricsServiceInternal featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:valueRef:]_block_invoke
+ ___147-[FPMTLMetricsServiceInternal featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:didChange:]_block_invoke
+ ___151-[FPMTLMetricsServiceInternal metalLayerDrawableFinish:imageQueueID:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:]_block_invoke
+ ___151-[FPMTLMetricsServiceInternal metalLayerDrawableFinish:imageQueueID:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:]_block_invoke_2
+ ___162-[FPMTLMetricsServiceInternal featureRegisterPopover:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:items:selectedIndex:didChange:]_block_invoke
+ ___173-[FPMTLMetricsServiceInternal featureRegisterSlider:title:envVar:description:documtationTitles:documentLinks:options:minValue:maxValue:defaultValue:numberOfTicks:didChange:]_block_invoke
+ ___186-[FPMTLMetricsServiceInternal metalFXScalerEncoded:commandBufferAddress:scalingMethod:version:scalingDevice:inputWidth:inputHeight:targetWidth:targetHeight:exposure:autoExposureEnabled:]_block_invoke
+ ___37+[_CADeveloperHUDProperties instance]_block_invoke
+ ___38-[FPMTLMetricsServiceInternal remove:]_block_invoke
+ ___46-[FPMTLMetricsServiceInternal addLabel:after:]_block_invoke
+ ___49+[FPCAMetalLayerState _reportBundleInfoIfNeeded:]_block_invoke_2
+ ___49-[FPMTLMetricsServiceInternal updateLabel:value:]_block_invoke
+ ___49-[FPMTLMetricsServiceInternal updateLabel:value:]_block_invoke_2
+ ___50-[FPMTLMetricsServiceInternal addMetricsListener:]_block_invoke
+ ___50-[FPMTLMetricsServiceInternal resetMetricHistory:]_block_invoke
+ ___52-[FPMTLMetricsServiceInternal addGPUTimingListener:]_block_invoke
+ ___53-[FPMTLMetricsServiceInternal enableInsight:enabled:]_block_invoke
+ ___53-[FPMTLMetricsServiceInternal removeMetricsListener:]_block_invoke
+ ___53-[FPMTLMetricsServiceInternal updateMetricName:name:]_block_invoke
+ ___55-[FPMTLMetricsServiceInternal interposeEnableIOReport:]_block_invoke
+ ___55-[FPMTLMetricsServiceInternal removeGPUTimingListener:]_block_invoke
+ ___55-[FPMTLMetricsServiceInternal removeRegisteredFeature:]_block_invoke
+ ___55-[FPMTLMetricsServiceInternal updateFloatMetric:value:]_block_invoke
+ ___55-[FPMTLMetricsServiceInternal updateLabelMetric:label:]_block_invoke
+ ___56-[FPMTLMetricsServiceInternal setMetricEnabled:enabled:]_block_invoke
+ ___56-[FPMTLMetricsServiceInternal setShaderCompiledHandler:]_block_invoke
+ ___56-[FPMTLMetricsServiceInternal setShaderCompiledHandler:]_block_invoke_2
+ ___56-[FPMTLMetricsServiceInternal setShaderCompiledHandler:]_block_invoke_3
+ ___57-[FPMTLMetricsServiceInternal _registerHUDLoaderIfNeeded]_block_invoke
+ ___57-[FPMTLMetricsServiceInternal _registerHUDLoaderIfNeeded]_block_invoke_2
+ ___57-[FPMTLMetricsServiceInternal _registerHUDLoaderIfNeeded]_block_invoke_3
+ ___57-[FPMTLMetricsServiceInternal metalFXScalingPerformance:]_block_invoke
+ ___57-[FPMTLMetricsServiceInternal updateIntegerMetric:value:]_block_invoke
+ ___59-[FPMTLMetricsServiceInternal markCommandBuffer:component:]_block_invoke
+ ___59-[FPMTLMetricsServiceInternal updateMetricOptions:options:]_block_invoke
+ ___61-[FPMTLMetricsServiceInternal enumerateTopEncodersWithLabel:]_block_invoke
+ ___61-[FPMTLMetricsServiceInternal gptkDeviceCreated:graphicsAPI:]_block_invoke
+ ___62-[FPMTLMetricsServiceInternal metal4CommandBufferDeallocated:]_block_invoke
+ ___62-[FPMTLMetricsServiceInternal metalFXInterpolatorPerformance:]_block_invoke
+ ___64-[FPMTLMetricsServiceInternal metalSetEncoderTimestampResolver:]_block_invoke
+ ___67-[FPMTLMetricsServiceInternal enumerateTopCommandBuffersWithLabel:]_block_invoke
+ ___67-[FPMTLMetricsServiceInternal metalFXFrameInterpolatorEncodingEnd:]_block_invoke
+ ___70-[FPMTLMetricsServiceInternal updateMetricColor:nameColor:valueColor:]_block_invoke
+ ___71-[FPMTLMetricsServiceInternal metal4CommandBufferBegin:beginTimeInSec:]_block_invoke
+ ___74-[FPMTLMetricsServiceInternal metalCommandBufferCommited:commitTimeInSec:]_block_invoke
+ ___75-[FPMTLMetricsServiceInternal metalCommandBufferCreated:creationTimeInSec:]_block_invoke
+ ___76-[FPMTLMetricsServiceInternal metal4CommandBufferCreated:creationTimeInSec:]_block_invoke
+ ___79-[FPMTLMetricsMTLLayerTracking drawableStart:surfaceID:startTime:acquiredTime:]_block_invoke
+ ___93-[FPMTLMetricsServiceInternal metal4CommandBufferEnd:endTimeInSec:allocatorId:allocatedSize:]_block_invoke
+ ___93-[FPMTLMetricsServiceInternal metalCommandBufferCompleted:gpuStartTimeInSec:gpuEndTimeInSec:]_block_invoke
+ ___94-[FPMTLMetricsServiceInternal metalFXFrameInterpolatorEncoded:commandBufferAddress:deltaTime:]_block_invoke
+ ___95-[FPMTLMetricsServiceInternal metalEncoderEnd:encoderTraceId:timeMAT:label:commandBufferLabel:]_block_invoke
+ ___97+[FPCAMetalLayerState drawableLifetimeComposited:drawableID:surfaceID:compositedTime:detachCode:]_block_invoke
+ ___99-[FPMTLMetricsServiceInternal metalCommandBufferScheduled:kernelStartTimeInSec:kernelEndTimeInSec:]_block_invoke
+ ___FPMTLMetricsGPUTimeTrackerEnableCompilerStatsReporting_block_invoke
+ ___FPMTLMetricsGPUTimeTrackerEnableEncoderGPUTimeSampling_block_invoke
+ ___FPMTLMetricsGPUTimeTrackerReset_block_invoke
+ ___FPMTLMetricsGPUTimeTrackerSetInsightsEnabled_block_invoke
+ ___FPMTLMetricsGameModeEnabled_block_invoke
+ ___FPMTLMetricsGameModeEnabled_block_invoke_2
+ ___FPMTLMetricsGetGameModeKeyState_block_invoke
+ ___FPMTLMetricsInsightsCreatePrototypes_block_invoke
+ ___FPMTLMetricsIsDebuggerAttached_block_invoke
+ ___FPMTLMetricsIsExcluded_block_invoke
+ ___FPMTLMetricsIsInternalInstall_block_invoke
+ ___FPMTLMetricsIsProcessTranslated_block_invoke
+ ___FPMTLMetricsIsSideLoadedApp_block_invoke
+ ___FPMTLMetricsMachAbsoluteToNs_block_invoke
+ ___FPMTLMetricsSEMEnabled_block_invoke
+ ___FPMTLMetricsSEMEnabled_block_invoke_2
+ ___FPRUsageTimestampToTimeInterval_block_invoke
+ ___MetalMetricsInterposeDylibOpen_block_invoke
+ ___NSArray0__struct
+ ____FPGetCurrentShaderCompilerStatSignpostsEnabled_block_invoke
+ ____FPMTLMetricsDispatchQueueGet_block_invoke
+ ____FPMTLMetricsNotificationQueueGet_block_invoke
+ ____FPSetCurrentShaderCompilerStatSignpostsEnabled_block_invoke
+ ____GPUToolsTelemetryMTLLayerTrackingGetTrackers_block_invoke
+ ____Z38_FPMTLMetricsGPUTimeTrackerGetInstancev_block_invoke
+ ____Z58_FPMTLMetricsGPUTimeTrackerWrapupFrameForPresentedDrawableP26FPMTLMetricsGPUTimeTrackermyU13block_pointerFvP41FPMTLMetricsGPUTimeTrackerFrameTimingDataE_block_invoke
+ ___assert_rtn
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e42_v16?0^{FPMTLMetricsShaderInfo=QBB[128c]}8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e154_v28?0"NSString"8I16^{FPMTLMetricsGPUTimeTrackerCommonObjectRecord={FPMTLMetricsMetricValue=(?=d*)dddddQddQ}{FPMTLMetricsMetricValue=(?=d*)dddddQddQ}Q}20ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e60_v16?0^{FPMTLMetricsIOReportMetricsBacking=dddddddd[24d]IQ}8ls32l8
+ ___block_descriptor_40_e8_32w_e11_v20?0I8Q12lw32l8
+ ___block_descriptor_40_e8_32w_e42_v16?0^{FPMTLMetricsShaderInfo=QBB[128c]}8lw32l8
+ ___block_descriptor_41_e5_v8?0l
+ ___block_descriptor_44_e5_v8?0l
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e621_v16?0^{FPMTLMetricsGPUTimeTrackerFrameTimingData=^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ[7^{FPMTLMetricsTimeRange}][7^{FPMTLMetricsTimeRange}][7Q][7Q]QQQQQBB}8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e29_v16?0"FPCAMetalLayerState"8ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e29_v16?0"FPCAMetalLayerState"8l
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_66_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_76_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_77_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_92_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.103
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.17
+ ___block_literal_global.23
+ ___block_literal_global.26
+ ___block_literal_global.270
+ ___block_literal_global.3
+ ___block_literal_global.353
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.39
+ ___block_literal_global.41
+ ___block_literal_global.47
+ ___block_literal_global.50
+ ___block_literal_global.6
+ ___block_literal_global.631
+ ___block_literal_global.86
+ ___block_literal_global.9
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___destructor_8_s0_s8_s16_s24_s32_s40_s48_s56
+ ___gxx_personality_v0
+ ___objc_personality_v0
+ ___strncpy_chk
+ __createMetalFXMetricsIfNeeded.created
+ __dispatch_main_q
+ __registerHUDLoaderIfNeeded.onceToken
+ __snapshotDrawable:imageQueueID:presentedTime:surface:state:.everHadPresentedTime
+ _bzero
+ _dispatch_after
+ _dispatch_time
+ _dlopen
+ _dlsym
+ _gFPShaderCompilerStatsSignpostingIsEnabled
+ _kCFAbsoluteTimeIntervalSince1970
+ _kFPEnableShaderCompilerStatSignpostsDefaultsVariableName
+ _kFPEnableShaderCompilerStatSignpostsEnvironmentVariableName
+ _loadHUDIfNeeded.hudHandle
+ _memcpy
+ _memmove
+ _notificationQueue
+ _notify_get_state
+ _notify_register_dispatch
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UTF8StringForName:
+ _objc_msgSend$_canLoadHUD
+ _objc_msgSend$_createMetalFXMetricsIfNeeded
+ _objc_msgSend$_drawableDidComposite:surfaceID:compositedTime:detachCode:
+ _objc_msgSend$_drawableDidPresent:presentedDrawableTime:hasMetalFXFrameInterpolator:
+ _objc_msgSend$_handleFrameBoundary:
+ _objc_msgSend$_initCommon
+ _objc_msgSend$_interposeSyncState
+ _objc_msgSend$_parseScalingMethodForMetrics:metrics:
+ _objc_msgSend$_registerHUDLoaderIfNeeded
+ _objc_msgSend$_shouldEnableTracking
+ _objc_msgSend$_snapshotDrawable:imageQueueID:presentedTime:surface:state:
+ _objc_msgSend$_updateDetachState:detachCode:
+ _objc_msgSend$_updateGPTKState:
+ _objc_msgSend$_updateMetalFXState:
+ _objc_msgSend$addGraph:after:min:max:
+ _objc_msgSend$addInsight:isPrototype:
+ _objc_msgSend$addInsightGroup:
+ _objc_msgSend$addLabel:after:
+ _objc_msgSend$addMetric:
+ _objc_msgSend$addMetric:name:unit:nameColor:valueColor:visualType:options:
+ _objc_msgSend$addStatistic:after:color:tolerance:graph:
+ _objc_msgSend$appStoreReceiptURL
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$component
+ _objc_msgSend$config
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$deallocTrackerForLayer:
+ _objc_msgSend$defaultValue
+ _objc_msgSend$deltaTime
+ _objc_msgSend$descriptor
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didChange
+ _objc_msgSend$disableExplicitFrameBoundary
+ _objc_msgSend$documentationLinks
+ _objc_msgSend$documentationTitles
+ _objc_msgSend$drawableComposited:surfaceID:compositedTime:detachCode:
+ _objc_msgSend$drawableFinish:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:
+ _objc_msgSend$drawablePresented:presentedDrawableTime:hasMetalFXFrameInterpolator:
+ _objc_msgSend$drawableStart:surfaceID:startTime:acquiredTime:
+ _objc_msgSend$drawableState
+ _objc_msgSend$drawableStateForDrawable:
+ _objc_msgSend$emitSignpost:log:intervalBegin:intervalEnd:
+ _objc_msgSend$emitSignpost:log:intervalBegin:intervalEnd:numFrames:isSkippedFrameStats:
+ _objc_msgSend$enableFacet:enabled:
+ _objc_msgSend$enableInsight:enabled:
+ _objc_msgSend$enabled
+ _objc_msgSend$enabledFacets
+ _objc_msgSend$envVar
+ _objc_msgSend$estimatedRecentAverageFrameInterval
+ _objc_msgSend$featureDescription
+ _objc_msgSend$featureRegisterButton:title:description:documtationTitles:documentLinks:options:didChange:
+ _objc_msgSend$featureRegisterPopover:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:items:selectedIndex:didChange:
+ _objc_msgSend$featureRegisterSlider:title:envVar:description:documtationTitles:documentLinks:options:minValue:maxValue:defaultValue:numberOfTicks:didChange:
+ _objc_msgSend$featureRegisterTextbox:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:didChange:
+ _objc_msgSend$featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:didChange:
+ _objc_msgSend$featureRegisterToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:valueRef:
+ _objc_msgSend$floatValue
+ _objc_msgSend$gameModeSupportState
+ _objc_msgSend$getMetric:
+ _objc_msgSend$globalMetrics
+ _objc_msgSend$gptkDeviceCreated:graphicsAPI:
+ _objc_msgSend$gptkExecName
+ _objc_msgSend$gptkFeatureFlags
+ _objc_msgSend$gptkMetrics
+ _objc_msgSend$gpuTimingUpdatedForFrame:onScreenTime:timingSnapshot:
+ _objc_msgSend$graphicsAPI
+ _objc_msgSend$hasMetal4APIUsage
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hash
+ _objc_msgSend$identifier
+ _objc_msgSend$increaseLengthBy:
+ _objc_msgSend$incrementStatistic:value:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$init:
+ _objc_msgSend$initButton:title:description:documtationTitles:documentLinks:options:didChange:
+ _objc_msgSend$initCommon:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:
+ _objc_msgSend$initPopover:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:items:selectedIndex:didChange:
+ _objc_msgSend$initSlider:title:envVar:description:documtationTitles:documentLinks:options:minValue:maxValue:defaultValue:numberOfTicks:didChange:
+ _objc_msgSend$initTextbox:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:didChange:
+ _objc_msgSend$initToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:didChange:
+ _objc_msgSend$initToggle:title:envVar:description:documtationTitles:documentLinks:options:defaultValue:state:valueRef:
+ _objc_msgSend$initWithCategory:
+ _objc_msgSend$initWithComponent:
+ _objc_msgSend$initWithDescriptor:
+ _objc_msgSend$initWithDescriptor:isPrototype:
+ _objc_msgSend$initWithLayer:frameNumber:
+ _objc_msgSend$initWithName:identifier:unit:nameColor:valueColor:visualType:options:
+ _objc_msgSend$insertMetric:after:name:unit:nameColor:valueColor:visualType:options:
+ _objc_msgSend$insights
+ _objc_msgSend$instance
+ _objc_msgSend$intValue
+ _objc_msgSend$interposeEnableCompilerStats:
+ _objc_msgSend$interposeEnableEncoderCPU:
+ _objc_msgSend$interposeEnableEncoderGPUTimeSampling:
+ _objc_msgSend$interposeEnableIOReport:
+ _objc_msgSend$interposeGetCompilerStatsDict
+ _objc_msgSend$interposeGetDetachCode:
+ _objc_msgSend$interposeGetMTLAllocatedSize
+ _objc_msgSend$ioReportMetrics
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isFacetEnabled:
+ _objc_msgSend$isHUDElementEnabled:
+ _objc_msgSend$isInGPTk
+ _objc_msgSend$isMainLayer
+ _objc_msgSend$isMetricEnabled:
+ _objc_msgSend$items
+ _objc_msgSend$layerAddress
+ _objc_msgSend$layerState
+ _objc_msgSend$length
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$listener
+ _objc_msgSend$loadHUDIfNeeded
+ _objc_msgSend$longLongValue
+ _objc_msgSend$mainLayer
+ _objc_msgSend$mainTracker
+ _objc_msgSend$markExplicitFrameBoundary
+ _objc_msgSend$markMainLayer:
+ _objc_msgSend$maxValue
+ _objc_msgSend$maxValueAllowed
+ _objc_msgSend$metal4CommandBufferBegin:beginTimeInSec:
+ _objc_msgSend$metal4CommandBufferCommited:queueAddress:generation:commitTimeInSec:label:
+ _objc_msgSend$metal4CommandBufferCompleted:queueAddress:generation:gpuStartTimeInSec:gpuEndTimeInSec:
+ _objc_msgSend$metal4CommandBufferCreated:creationTimeInSec:
+ _objc_msgSend$metal4CommandBufferDeallocated:
+ _objc_msgSend$metal4CommandBufferEnd:endTimeInSec:allocatorId:allocatedSize:
+ _objc_msgSend$metalCommandBufferCommited:commitTimeInSec:
+ _objc_msgSend$metalCommandBufferCompleted:gpuStartTimeInSec:gpuEndTimeInSec:
+ _objc_msgSend$metalCommandBufferCreated:creationTimeInSec:
+ _objc_msgSend$metalCommandBufferScheduled:kernelStartTimeInSec:kernelEndTimeInSec:
+ _objc_msgSend$metalCompilerFunctionCompiled:functionType:async:wasCached:compileTimeMAT:performanceStatistics:
+ _objc_msgSend$metalCompilerPipelineStateCreated:async:compileTimeMAT:performanceStatistics:
+ _objc_msgSend$metalDeviceCreatedWithFramePacingVersion:
+ _objc_msgSend$metalFXFrameInterpolatorEncoded:commandBufferAddress:deltaTime:
+ _objc_msgSend$metalFXFrameInterpolatorEncodingEndNoDirectObject:
+ _objc_msgSend$metalFXInterpolatorPerformance:
+ _objc_msgSend$metalFXMetrics
+ _objc_msgSend$metalFXScalerEncoded:commandBufferAddress:scalingMethod:version:scalingDevice:inputWidth:inputHeight:targetWidth:targetHeight:exposure:autoExposureEnabled:
+ _objc_msgSend$metalFXScalingPerformance:
+ _objc_msgSend$metalLayerAlloc:
+ _objc_msgSend$metalLayerDealloc:
+ _objc_msgSend$metalLayerDrawableDidComposite:drawableID:surfaceID:compositedTime:detachCode:
+ _objc_msgSend$metalLayerDrawableDidPresent:drawableID:presentedDrawableTime:
+ _objc_msgSend$metalLayerDrawableFinish:imageQueueID:drawableID:finishedTime:wasPresented:clientPresentLateness:onGlassPresentLateness:
+ _objc_msgSend$metalLayerDrawableStart:surfaceID:drawableID:acquisitionWaitStartTime:acquiredTime:
+ _objc_msgSend$metalLayerMetrics
+ _objc_msgSend$metalLayerSetName:name:
+ _objc_msgSend$metalLayerSetPixelFormat:pixelFormat:
+ _objc_msgSend$metalLayerSetSize:width:height:
+ _objc_msgSend$metrics
+ _objc_msgSend$metricsUpdatedForLayer:metrics:
+ _objc_msgSend$minValue
+ _objc_msgSend$minValueAllowed
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableDescriptors
+ _objc_msgSend$name
+ _objc_msgSend$nameColor
+ _objc_msgSend$numTrackers
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberOfTicks
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$options
+ _objc_msgSend$path
+ _objc_msgSend$performanceInsightsMetrics
+ _objc_msgSend$progName
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$removeMetric:
+ _objc_msgSend$removeMetrics:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeRegisteredFeature:
+ _objc_msgSend$requestAllMetrics
+ _objc_msgSend$resetMetric:
+ _objc_msgSend$resetMetricHistory:
+ _objc_msgSend$selectedIndex
+ _objc_msgSend$setCommandBufferCount:
+ _objc_msgSend$setDefaultValue:
+ _objc_msgSend$setDescriptorIndex:
+ _objc_msgSend$setDetachCount:
+ _objc_msgSend$setDocumentationLinks:
+ _objc_msgSend$setDocumentationTitles:
+ _objc_msgSend$setDoublevalue:
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$setEnabledFacets:
+ _objc_msgSend$setEnvVar:
+ _objc_msgSend$setFeatureDescription:
+ _objc_msgSend$setGraphicsAPI:
+ _objc_msgSend$setHUDElementEnabled:flag:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setIntValue:
+ _objc_msgSend$setIsMainLayer:
+ _objc_msgSend$setMainTracker:
+ _objc_msgSend$setMetricEnabled:enabled:
+ _objc_msgSend$setMetricProcessingQueue:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNameColor:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setPixelFormat:
+ _objc_msgSend$setStatistic:value:
+ _objc_msgSend$setStringValue:
+ _objc_msgSend$setSurface:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setWidth:height:
+ _objc_msgSend$shaderCompilerMetrics
+ _objc_msgSend$state
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringDidChange
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$surface
+ _objc_msgSend$title
+ _objc_msgSend$trackerForLayer:
+ _objc_msgSend$type
+ _objc_msgSend$unit
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$update:
+ _objc_msgSend$updateFloatMetric:value:
+ _objc_msgSend$updateIntegerMetric:value:
+ _objc_msgSend$updateLabel:value:
+ _objc_msgSend$updateLabelMetric:label:
+ _objc_msgSend$updateMetric:value:
+ _objc_msgSend$updateMetricColor:nameColor:valueColor:
+ _objc_msgSend$updateMetricInt:value:
+ _objc_msgSend$updateMetricName:name:
+ _objc_msgSend$updateMetricOptions:options:
+ _objc_msgSend$updateStringMetric:value:
+ _objc_msgSend$updateWithFrameTiming:
+ _objc_msgSend$valueColor
+ _objc_msgSend$valueRef
+ _objc_msgSend$version
+ _objc_msgSend$visualType
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_opt_new
+ _objc_opt_respondsToSelector
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_setProperty_nonatomic_copy
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _qsort
+ _queue
+ _setenv
+ _strncpy
+ _sysctl
- +[FPCAMetalLayerState _commandBufferForAddress:]
- +[FPCAMetalLayerState _globalScheduledCommandBuffers]
- +[FPCAMetalLayerState _updateCommandBufferState:block:]
- -[FPInFlightCommandBuffer dealloc]
- -[FPInFlightCommandBuffer initWithAddress:creationTime:]
- -[FPInFlightDrawableLifetime .cxx_destruct]
- _.str.97
- _OBJC_CLASS_$_FPInFlightCommandBuffer
- _OBJC_IVAR_$_FPCAMetalLayerState._onScreenStats
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedCPUWalltimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedCommandBufferCount
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedEndToEndDrawableLifetimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedGPUFinishToPresentLatency
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedGPUWalltimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._presentedOnGPUTimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedCPUWalltimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedCommandBufferCount
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedEndToEndDrawableLifetimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedGPUFinishToPresentLatency
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedGPUWalltimeStats
- _OBJC_IVAR_$_FPCAMetalLayerState._skippedOnGPUTimeStats
- _OBJC_IVAR_$_FPInFlightCommandBuffer._address
- _OBJC_IVAR_$_FPInFlightCommandBuffer._commitTime
- _OBJC_IVAR_$_FPInFlightCommandBuffer._creationTime
- _OBJC_IVAR_$_FPInFlightCommandBuffer._gpuEnd
- _OBJC_IVAR_$_FPInFlightCommandBuffer._gpuStart
- _OBJC_IVAR_$_FPInFlightCommandBuffer._intersectsMultipleLayers
- _OBJC_IVAR_$_FPInFlightCommandBuffer._kernelSchedulingEnd
- _OBJC_IVAR_$_FPInFlightCommandBuffer._kernelSchedulingStart
- _OBJC_IVAR_$_FPInFlightDrawableLifetime._attributedCommandBuffers
- _OBJC_METACLASS_$_FPInFlightCommandBuffer
- __FPGlobalInFlightCommandBufferDictionary
- __OBJC_$_INSTANCE_METHODS_FPInFlightCommandBuffer
- __OBJC_$_INSTANCE_VARIABLES_FPInFlightCommandBuffer
- __OBJC_CLASS_RO_$_FPInFlightCommandBuffer
- __OBJC_METACLASS_RO_$_FPInFlightCommandBuffer
- ___53+[FPCAMetalLayerState _globalScheduledCommandBuffers]_block_invoke
- ___54+[FPCAMetalLayerState commandBufferCommit:commitTime:]_block_invoke
- ___55+[FPCAMetalLayerState _updateCommandBufferState:block:]_block_invoke
- ___56+[FPCAMetalLayerState commandBufferCreate:creationTime:]_block_invoke
- ___70+[FPCAMetalLayerState commandBufferCompleted:gpuStartTime:gpuEndTime:]_block_invoke
- ___76+[FPCAMetalLayerState commandBufferScheduled:kernelStartTime:kernelEndTime:]_block_invoke
- ____FPGlobalInFlightCommandBufferDictionary_block_invoke
- ____accumulatedGPUTime_block_invoke
- ___block_descriptor_32_e61_q24?0"FPInFlightCommandBuffer"8"FPInFlightCommandBuffer"16l
- ___block_descriptor_40_e29_v16?0"FPCAMetalLayerState"8l
- ___block_descriptor_40_e33_v16?0"FPInFlightCommandBuffer"8l
- ___block_descriptor_40_e8_32s_e29_v16?0"FPCAMetalLayerState"8ls32l8
- ___block_descriptor_56_e33_v16?0"FPInFlightCommandBuffer"8l
- ___block_descriptor_64_e33_v16?0"FPInFlightCommandBuffer"8l
- ___block_literal_global.148
- ___block_literal_global.15
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.32
- ___block_literal_global.35
- ___block_literal_global.54
- ___block_literal_global.82
- ___block_literal_global.94
- _gFPInFlightCommandBufferCount
- _gHasRecentActiveDrawables
- _objc_msgSend$firstObject
- _objc_msgSend$initWithAddress:creationTime:
- _objc_msgSend$sortUsingComparator:
CStrings:
+ ""
+ "\tComparing last %d render passes, same attachment %d, total attachment %d, ratio = %f"
+ "\nTotal instructions: \t\t%{public, name=ri_instructions}llu instr\nTotal P-core instructions: \t%{public, name=ri_pinstructions}llu pinstr\nTotal cycles:               %{public, name=ri_cycles}llu cycles\nTotal P-core cycles:        %{public, name=ri_pcycles}llu cycles\nTotal system time:          %{public, name=ri_sys_time}.4fs\nTotal P-core system time:   %{public, name=ri_sys_ptime}.4fs\nTotal user time:            %{public, name=ri_user_time}.4fs\nTotal P-core user time:     %{public, name=ri_user_ptime}.4fs\nPhysical footprint: \t\t%{public, name=ri_phys_footprint}.2fMiB\nPeak Physical footprint: \t%{public, name=ri_lifetime_max_phys_footprint}.2fMiB\nMemory limit headroom:\t\t%{public, name=os_proc_available_memory}.2fMiB\nDiskIO - Reads: \t\t%{public, name=ri_diskio_bytesread}.2fMiB\nDiskIO - Writes: \t\t%{public, name=ri_diskio_byteswritten}.2fMiB\nDiskIO - Logical Writes: \t%{public, name=ri_logical_writes}.2fMiB\nMetal Device Allocated Size:     %{public, name=metal_device_allocated_size}.2fMiB\n"
+ " "
+ "    <====== Consecutive %d render encoders, %d unique color attachments, %d total color attachments, ratio = %f ("
+ "    <====== Num unique attachments: %lu, total attachments: %u"
+ "%@ (%s)\n"
+ "%@ Color Attachments: "
+ "%s\n"
+ "%s %f"
+ "%ux%u"
+ "(content size)"
+ ")"
+ ", Depth: 0x%llx, Stencil: 0x%llx\n"
+ "-[FPMTLMetricsServiceInternal setGlobalMetrics:]"
+ "/System/Library/PrivateFrameworks/GPUToolsHUD.framework/GPUToolsHUD"
+ "/usr/lib/libMTLHud.dylib"
+ "/usr/lib/libMetalMetricsInterpose.dylib"
+ "0x%llx | "
+ "1"
+ ":"
+ "====== Frame %zu Encoding ======"
+ "A1BGR5Unorm"
+ "A8Unorm"
+ "ABGR4Unorm"
+ "ANE"
+ "API Usage Patterns"
+ "ARGB8Unorm"
+ "ARGB8Unorm_sRGB"
+ "ASTC_10x10_HDR"
+ "ASTC_10x10_LDR"
+ "ASTC_10x10_sRGB"
+ "ASTC_10x5_HDR"
+ "ASTC_10x5_LDR"
+ "ASTC_10x5_sRGB"
+ "ASTC_10x6_HDR"
+ "ASTC_10x6_LDR"
+ "ASTC_10x6_sRGB"
+ "ASTC_10x8_HDR"
+ "ASTC_10x8_LDR"
+ "ASTC_10x8_sRGB"
+ "ASTC_12x10_HDR"
+ "ASTC_12x10_LDR"
+ "ASTC_12x10_sRGB"
+ "ASTC_12x12_HDR"
+ "ASTC_12x12_LDR"
+ "ASTC_12x12_sRGB"
+ "ASTC_4x2_HDR"
+ "ASTC_4x2_LDR"
+ "ASTC_4x2_sRGB"
+ "ASTC_4x4_HDR"
+ "ASTC_4x4_LDR"
+ "ASTC_4x4_sRGB"
+ "ASTC_5x4_HDR"
+ "ASTC_5x4_LDR"
+ "ASTC_5x4_sRGB"
+ "ASTC_5x5_HDR"
+ "ASTC_5x5_LDR"
+ "ASTC_5x5_sRGB"
+ "ASTC_6x5_HDR"
+ "ASTC_6x5_LDR"
+ "ASTC_6x5_sRGB"
+ "ASTC_6x6_HDR"
+ "ASTC_6x6_LDR"
+ "ASTC_6x6_sRGB"
+ "ASTC_8x4_HDR"
+ "ASTC_8x4_LDR"
+ "ASTC_8x4_sRGB"
+ "ASTC_8x5_HDR"
+ "ASTC_8x5_LDR"
+ "ASTC_8x5_sRGB"
+ "ASTC_8x6_HDR"
+ "ASTC_8x6_LDR"
+ "ASTC_8x6_sRGB"
+ "ASTC_8x8_HDR"
+ "ASTC_8x8_LDR"
+ "ASTC_8x8_sRGB"
+ "AccelerationStructure Encoder"
+ "Auto"
+ "B!"
+ "B5G6R5Unorm"
+ "BC1_RGBA"
+ "BC1_RGBA_sRGB"
+ "BC2_RGBA"
+ "BC2_RGBA_sRGB"
+ "BC3_RGBA"
+ "BC3_RGBA_sRGB"
+ "BC4_RSnorm"
+ "BC4_RUnorm"
+ "BC5_RGSnorm"
+ "BC5_RGUnorm"
+ "BC6H_RGBFloat"
+ "BC6H_RGBUfloat"
+ "BC7_RGBAUnorm"
+ "BC7_RGBAUnorm_sRGB"
+ "BGR10A2Unorm"
+ "BGR10A2Unorm_PQ"
+ "BGR10A2Unorm_sRGB"
+ "BGR10_XR"
+ "BGR10_XR_sRGB"
+ "BGR5A1Unorm"
+ "BGRA10Uint"
+ "BGRA10Uint_PACKED"
+ "BGRA10Unorm"
+ "BGRA10Unorm_HLG"
+ "BGRA10Unorm_PACKED"
+ "BGRA10Unorm_PACKED_HLG"
+ "BGRA10Unorm_PACKED_PQ"
+ "BGRA10Unorm_PACKED_sRGB"
+ "BGRA10Unorm_PQ"
+ "BGRA10Unorm_sRGB"
+ "BGRA10_XR"
+ "BGRA10_XR_PACKED"
+ "BGRA10_XR_PACKED_sRGB"
+ "BGRA10_XR_sRGB"
+ "BGRA4Unorm"
+ "BGRA8Unorm"
+ "BGRA8Unorm_sRGB"
+ "BGRG422"
+ "Blit Encoder"
+ "Bundle Info:\nBundleID: '%{public, name=BundleID}@'\nBundle Short Version: '%{public, name=BundleShortVersion}@'\nBundle Version: '%{public, name=BundleVersion}@'\nGame Mode Supported: '%{public, name=game_mode_supported}d'\nUses Metal4: '%{public, name=uses_metal4}d'\nProcess Translated: '%{public, name=process_translated}d'\n"
+ "Bundle Info:\nBundleID: '%{public, name=BundleID}@'\nBundle Short Version: '%{public, name=BundleShortVersion}@'\nBundle Version: '%{public, name=BundleVersion}@'\nGame Mode Supported: '%{public, name=game_mode_supported}d'\nUses Metal4: '%{public, name=uses_metal4}d'\nProcess Translated: '%{public, name=process_translated}d'\nGPTk Exec Name: '%{public, name=gptk_exec_name}@'\nGPTk Bundle Version: '%{public, name=gptk_bundle_version}@'\nGPTk MPL Bundle Version: '%{public, name=gptk_mpl_bundle_version}@'\nGPTk Graphics API: '%{public, name=gptk_graphics_api}@'\nGPTk Feature Flags: '%{public, name=gptk_feature_flags}d'\n"
+ "Client attempted to present a composite without acquiring it. ID is signpost ID"
+ "Coarse D3D Barrier Usage"
+ "Compiled %llu shaders. Total compilation time is %.2fms."
+ "Compiled %llu shaders. Total compilation time is %.2fms. Consider adopting MTL4Compiler for more fine grained compilations."
+ "Compute"
+ "Compute Encoder"
+ "Compute Pipelines"
+ "CoreSimulator"
+ "Creating Binary Archives"
+ "D3D11"
+ "D3D12"
+ "Denoising"
+ "Denoising | ANE"
+ "Denoising | GPU"
+ "Depth16Unorm"
+ "Depth24Unorm_Stencil8"
+ "Depth32Float"
+ "Depth32Float_Stencil8"
+ "Detected frequent change of similar render targets in between render commands, in Metal each change represents a new render pass. Consider merging similar render targets."
+ "Detected frequent resource copies interleaved with regular GPU commands. Consider batching resource updates."
+ "Detected high CPU encoding cost with encoders spending an average of %.2f%% of frame time encoding. Consider migrating to MTL4CommandBuffer."
+ "Detected high number of interleaved blit command encoder and other types of encoders. Consider batching resource updates or adopting MTL4ComputeCommandEncoder."
+ "Detected high number of render passes with similar attachments. Render passes are expensive on Apple GPUs, consider merging them or adopting color attachment mapping."
+ "Detected tessellation / geometry stage usage. Tessellation stage has a high cost of emulation on Apple GPUs. Consider use or transpile to Mesh shaders instead."
+ "EAC_R11Snorm"
+ "EAC_R11Unorm"
+ "EAC_RG11Snorm"
+ "EAC_RG11Unorm"
+ "EAC_RGBA8"
+ "EAC_RGBA8_sRGB"
+ "ETC2_RGB8"
+ "ETC2_RGB8A1"
+ "ETC2_RGB8A1_sRGB"
+ "ETC2_RGB8_sRGB"
+ "Exposure"
+ "FPMTLMetricsEnableIOReport"
+ "FPMTLMetricsEncoderTypeName"
+ "FPMTLMetricsInterposeEnableCompilerStats"
+ "FPMTLMetricsInterposeEnableEncoderCPU"
+ "FPMTLMetricsInterposeEnableEncoderGPUTimeSampling"
+ "FPMTLMetricsInterposeGetCompilerStatsDict"
+ "FPMTLMetricsInterposeGetDetachCode"
+ "FPMTLMetricsInterposeGetMTLAllocatedSize"
+ "FPMTLMetricsInterposeHasMainLayer"
+ "FPMTLMetricsInterposeSetGlobalNotificationHandler"
+ "FPMTLMetricsInterposeSetHasFPMetal4"
+ "FPMTLMetricsInterposeSetHasMainLayer"
+ "FPMTLMetricsInterposeSetQueue"
+ "FPMetalMetricsInsights.m"
+ "FPMetalMetricsServiceInternal.m"
+ "Fragment Shader"
+ "Frequent Render Target Change"
+ "Function Name"
+ "Function was cached"
+ "GBGR422"
+ "GPTk (count, frames) =%{public, signpost.aggregation:count, group=GPTk, unit=frames}u\nGPTk_GPTkRenderEncoderCount (GPTkRenderEncoderCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkRenderEncoderCount, measure_unit=count}.3f\nGPTk_GPTkRenderEncoderCount (GPTkRenderEncoderCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkRenderEncoderCount, measure_unit=count}.3f\nGPTk_GPTkRenderEncoderCount (GPTkRenderEncoderCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkRenderEncoderCount, measure_unit=count}.3f\nGPTk_GPTkRenderEncoderCount (GPTkRenderEncoderCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkRenderEncoderCount, measure_unit=count}.3f\nGPTk_GPTkComputeEncoderCount (GPTkComputeEncoderCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkComputeEncoderCount, measure_unit=count}.3f\nGPTk_GPTkComputeEncoderCount (GPTkComputeEncoderCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkComputeEncoderCount, measure_unit=count}.3f\nGPTk_GPTkComputeEncoderCount (GPTkComputeEncoderCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkComputeEncoderCount, measure_unit=count}.3f\nGPTk_GPTkComputeEncoderCount (GPTkComputeEncoderCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkComputeEncoderCount, measure_unit=count}.3f\nGPTk_GPTkBlitEncoderCount (GPTkBlitEncoderCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkBlitEncoderCount, measure_unit=count}.3f\nGPTk_GPTkBlitEncoderCount (GPTkBlitEncoderCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkBlitEncoderCount, measure_unit=count}.3f\nGPTk_GPTkBlitEncoderCount (GPTkBlitEncoderCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkBlitEncoderCount, measure_unit=count}.3f\nGPTk_GPTkBlitEncoderCount (GPTkBlitEncoderCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkBlitEncoderCount, measure_unit=count}.3f\nGPTk_GPTkCommandBufferCount (GPTkCommandBufferCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkCommandBufferCount, measure_unit=count}.3f\nGPTk_GPTkCommandBufferCount (GPTkCommandBufferCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkCommandBufferCount, measure_unit=count}.3f\nGPTk_GPTkCommandBufferCount (GPTkCommandBufferCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkCommandBufferCount, measure_unit=count}.3f\nGPTk_GPTkCommandBufferCount (GPTkCommandBufferCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkCommandBufferCount, measure_unit=count}.3f\nGPTk_GPTkDispatchCount (GPTkDispatchCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkDispatchCount, measure_unit=count}.3f\nGPTk_GPTkDispatchCount (GPTkDispatchCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkDispatchCount, measure_unit=count}.3f\nGPTk_GPTkDispatchCount (GPTkDispatchCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkDispatchCount, measure_unit=count}.3f\nGPTk_GPTkDispatchCount (GPTkDispatchCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkDispatchCount, measure_unit=count}.3f\nGPTk_GPTkDispatchMeshCount (GPTkDispatchMeshCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkDispatchMeshCount, measure_unit=count}.3f\nGPTk_GPTkDispatchMeshCount (GPTkDispatchMeshCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkDispatchMeshCount, measure_unit=count}.3f\nGPTk_GPTkDispatchMeshCount (GPTkDispatchMeshCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkDispatchMeshCount, measure_unit=count}.3f\nGPTk_GPTkDispatchMeshCount (GPTkDispatchMeshCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkDispatchMeshCount, measure_unit=count}.3f\nGPTk_GPTkFragmentDrawCount (GPTkFragmentDrawCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkFragmentDrawCount, measure_unit=count}.3f\nGPTk_GPTkFragmentDrawCount (GPTkFragmentDrawCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkFragmentDrawCount, measure_unit=count}.3f\nGPTk_GPTkFragmentDrawCount (GPTkFragmentDrawCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkFragmentDrawCount, measure_unit=count}.3f\nGPTk_GPTkFragmentDrawCount (GPTkFragmentDrawCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkFragmentDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryDrawCount (GPTkGeometryDrawCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkGeometryDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryDrawCount (GPTkGeometryDrawCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkGeometryDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryDrawCount (GPTkGeometryDrawCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkGeometryDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryDrawCount (GPTkGeometryDrawCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkGeometryDrawCount, measure_unit=count}.3f\nGPTk_GPTkTessellationDrawCount (GPTkTessellationDrawCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkTessellationDrawCount, measure_unit=count}.3f\nGPTk_GPTkTessellationDrawCount (GPTkTessellationDrawCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkTessellationDrawCount, measure_unit=count}.3f\nGPTk_GPTkTessellationDrawCount (GPTkTessellationDrawCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkTessellationDrawCount, measure_unit=count}.3f\nGPTk_GPTkTessellationDrawCount (GPTkTessellationDrawCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkTessellationDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryTessDrawCount (GPTkGeometryTessDrawCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkGeometryTessDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryTessDrawCount (GPTkGeometryTessDrawCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkGeometryTessDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryTessDrawCount (GPTkGeometryTessDrawCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkGeometryTessDrawCount, measure_unit=count}.3f\nGPTk_GPTkGeometryTessDrawCount (GPTkGeometryTessDrawCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkGeometryTessDrawCount, measure_unit=count}.3f\nGPTk_GPTkClearCount (GPTkClearCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkClearCount, measure_unit=count}.3f\nGPTk_GPTkClearCount (GPTkClearCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkClearCount, measure_unit=count}.3f\nGPTk_GPTkClearCount (GPTkClearCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkClearCount, measure_unit=count}.3f\nGPTk_GPTkClearCount (GPTkClearCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkClearCount, measure_unit=count}.3f\nGPTk_GPTkCopyCount (GPTkCopyCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkCopyCount, measure_unit=count}.3f\nGPTk_GPTkCopyCount (GPTkCopyCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkCopyCount, measure_unit=count}.3f\nGPTk_GPTkCopyCount (GPTkCopyCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkCopyCount, measure_unit=count}.3f\nGPTk_GPTkCopyCount (GPTkCopyCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkCopyCount, measure_unit=count}.3f\nGPTk_GPTkExecuteIndirectCount (GPTkExecuteIndirectCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkExecuteIndirectCount, measure_unit=count}.3f\nGPTk_GPTkExecuteIndirectCount (GPTkExecuteIndirectCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkExecuteIndirectCount, measure_unit=count}.3f\nGPTk_GPTkExecuteIndirectCount (GPTkExecuteIndirectCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkExecuteIndirectCount, measure_unit=count}.3f\nGPTk_GPTkExecuteIndirectCount (GPTkExecuteIndirectCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkExecuteIndirectCount, measure_unit=count}.3f\nGPTk_GPTkAccelerationEncoderCount (GPTkAccelerationEncoderCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkAccelerationEncoderCount, measure_unit=count}.3f\nGPTk_GPTkAccelerationEncoderCount (GPTkAccelerationEncoderCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkAccelerationEncoderCount, measure_unit=count}.3f\nGPTk_GPTkAccelerationEncoderCount (GPTkAccelerationEncoderCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkAccelerationEncoderCount, measure_unit=count}.3f\nGPTk_GPTkAccelerationEncoderCount (GPTkAccelerationEncoderCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkAccelerationEncoderCount, measure_unit=count}.3f\nGPTk_GPTkDispatchRaysCount (GPTkDispatchRaysCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkDispatchRaysCount, measure_unit=count}.3f\nGPTk_GPTkDispatchRaysCount (GPTkDispatchRaysCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkDispatchRaysCount, measure_unit=count}.3f\nGPTk_GPTkDispatchRaysCount (GPTkDispatchRaysCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkDispatchRaysCount, measure_unit=count}.3f\nGPTk_GPTkDispatchRaysCount (GPTkDispatchRaysCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkDispatchRaysCount, measure_unit=count}.3f\nGPTk_GPTkRayQueryCount (GPTkRayQueryCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkRayQueryCount, measure_unit=count}.3f\nGPTk_GPTkRayQueryCount (GPTkRayQueryCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkRayQueryCount, measure_unit=count}.3f\nGPTk_GPTkRayQueryCount (GPTkRayQueryCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkRayQueryCount, measure_unit=count}.3f\nGPTk_GPTkRayQueryCount (GPTkRayQueryCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkRayQueryCount, measure_unit=count}.3f\nGPTk_GPTkBuildBVHCount (GPTkBuildBVHCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkBuildBVHCount, measure_unit=count}.3f\nGPTk_GPTkBuildBVHCount (GPTkBuildBVHCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkBuildBVHCount, measure_unit=count}.3f\nGPTk_GPTkBuildBVHCount (GPTkBuildBVHCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkBuildBVHCount, measure_unit=count}.3f\nGPTk_GPTkBuildBVHCount (GPTkBuildBVHCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkBuildBVHCount, measure_unit=count}.3f\nGPTk_GPTkRefitBVHCount (GPTkRefitBVHCount average, count) =%{public, signpost.aggregation:measure_average, group=GPTk, type=GPTkRefitBVHCount, measure_unit=count}.3f\nGPTk_GPTkRefitBVHCount (GPTkRefitBVHCount min, count) =%{public, signpost.aggregation:measure_min, group=GPTk, type=GPTkRefitBVHCount, measure_unit=count}.3f\nGPTk_GPTkRefitBVHCount (GPTkRefitBVHCount max, count) =%{public, signpost.aggregation:measure_max, group=GPTk, type=GPTkRefitBVHCount, measure_unit=count}.3f\nGPTk_GPTkRefitBVHCount (GPTkRefitBVHCount stddev, count) =%{public, signpost.aggregation:measure_stddev, group=GPTk, type=GPTkRefitBVHCount, measure_unit=count}.3f\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "GPU"
+ "GPU Command Encoding - MTL4CommandBuffer"
+ "Game Mode Support"
+ "Game Porting Toolkit detected over synchronization due to coarse barrier usage. Consider using fine grained synchronization primitives when porting to Metal."
+ "Inherited"
+ "Interleaved Blit Command Encoders"
+ "Interleaved Resource Copy"
+ "Invalid"
+ "Invalid default value type: %{public, name=shader_compiler_stats_signpost_enabled}@"
+ "LSSupportsGameMode"
+ "LSSupportsGameMode key not found in Info.plist. This key will become required to be eligible for Game Mode in a future OS release."
+ "Layer 0x%llx"
+ "METAL_PERFORMANCE_SHADER_COMPILER_STATS_SIGNPOSTS"
+ "MTL_HUD_ENABLED"
+ "Machine Learning Encoder"
+ "Mesh Shader"
+ "Metal"
+ "Metal 4 Recommendations"
+ "MetalFX GPU"
+ "MetalPerformanceShaderCompilerStatsSignposts"
+ "Object Shader"
+ "Optimize high-end games for Apple GPUs"
+ "Other Insights"
+ "PVRTC_RGBA_2BPP"
+ "PVRTC_RGBA_2BPP_sRGB"
+ "PVRTC_RGBA_4BPP"
+ "PVRTC_RGBA_4BPP_sRGB"
+ "PVRTC_RGB_2BPP"
+ "PVRTC_RGB_2BPP_sRGB"
+ "PVRTC_RGB_4BPP"
+ "PVRTC_RGB_4BPP_sRGB"
+ "Pipelines"
+ "PresentedFrameStatsGPTk"
+ "PresentedFrameStatsShaderCompiler"
+ "R10Uint_PACKED"
+ "R10Uint_X6"
+ "R10Unorm_PACKED"
+ "R10Unorm_X6"
+ "R10Unorm_X6_HLG"
+ "R10Unorm_X6_PQ"
+ "R10Unorm_X6_sRGB"
+ "R12Uint_PACKED"
+ "R12Uint_X4"
+ "R12Unorm_X4"
+ "R12Unorm_X4_HLG"
+ "R12Unorm_X4_PQ"
+ "R16Bfloat"
+ "R16Float"
+ "R16Sint"
+ "R16Snorm"
+ "R16Uint"
+ "R16Unorm"
+ "R32Float"
+ "R32Sint"
+ "R32Uint"
+ "R8Sint"
+ "R8Snorm"
+ "R8Uint"
+ "R8Unorm"
+ "R8Unorm_sRGB"
+ "RG10Uint_PACKED"
+ "RG10Uint_X12"
+ "RG10Unorm_PACKED"
+ "RG10Unorm_X12"
+ "RG10Unorm_X12_sRGB"
+ "RG11B10Float"
+ "RG12Uint_PACKED"
+ "RG12Uint_X8"
+ "RG12Unorm_X8"
+ "RG16Bfloat"
+ "RG16Float"
+ "RG16Sint"
+ "RG16Snorm"
+ "RG16Uint"
+ "RG16Unorm"
+ "RG32Float"
+ "RG32Sint"
+ "RG32Uint"
+ "RG8Sint"
+ "RG8Snorm"
+ "RG8Uint"
+ "RG8Unorm"
+ "RG8Unorm_sRGB"
+ "RGB10A2Uint"
+ "RGB10A2Unorm"
+ "RGB10A2Unorm_HLG"
+ "RGB10A2Unorm_PQ"
+ "RGB10A2Unorm_sRGB"
+ "RGB10A8Uint_2P"
+ "RGB10A8_2P"
+ "RGB10A8_2P_HLG"
+ "RGB10A8_2P_PQ"
+ "RGB10A8_2P_XR10"
+ "RGB10A8_2P_XR10_sRGB"
+ "RGB10A8_2P_sRGB"
+ "RGB10_420_2P"
+ "RGB10_420_2P_PACKED"
+ "RGB10_422_2P"
+ "RGB10_422_2P_PACKED"
+ "RGB10_444_2P"
+ "RGB10_444_2P_PACKED"
+ "RGB8_420_2P"
+ "RGB8_422_2P"
+ "RGB8_444_2P"
+ "RGB9E5Float"
+ "RGBA16Bfloat"
+ "RGBA16Float"
+ "RGBA16Float_XR"
+ "RGBA16Sint"
+ "RGBA16Snorm"
+ "RGBA16Uint"
+ "RGBA16Unorm"
+ "RGBA32Float"
+ "RGBA32Sint"
+ "RGBA32Uint"
+ "RGBA8Sint"
+ "RGBA8Snorm"
+ "RGBA8Uint"
+ "RGBA8Unorm"
+ "RGBA8Unorm_sRGB"
+ "RGBX16Float"
+ "RGBX16Sint"
+ "RGBX16Uint"
+ "RGBX32Float"
+ "RGBX32Sint"
+ "RGBX32Uint"
+ "RGBX8Sint"
+ "RGBX8Snorm"
+ "RGBX8Uint"
+ "RGBX8Unorm"
+ "RGBX8Unorm_sRGB"
+ "Render Command Encoder"
+ "Render Encoder Color Attachments: "
+ "Render Pipelines"
+ "Resource Synchronizaation"
+ "Resource Synchronization"
+ "ResourceState Encoder"
+ "Scaling"
+ "Scaling Input Res"
+ "Scaling Target Res"
+ "Shader Compilation Time = %{public, name=shader_compilation_time}.4f\nShader Compilation Compilation Count = %{public, name=shader_compilation_shader_count}d\nShader Compilation Pipeline State Count = %{public, name=shader_compilation_pipeline_state_count}d\nShader Compilation Cached Compilation Count = %{public, name=shader_compilation_cached_shader_count}d\nTotal Shader Compilation Time = %{public, name=total_shader_compilation_time}.4f\nTotal Shader Compilation Compilation Count = %{public, name=total_shader_compilation_shader_count}d\nTotal Shader Compilation Pipeline State Count = %{public, name=total_shader_compilation_pipeline_state_count}d\nTotal Shader Compilation Cached Compilation Count = %{public, name=total_shader_compilation_cached_shader_count}d\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Shader Compiler Activity"
+ "Shader compiler stats signpost configured via 'FramePacingPerDrawableSignposts' default: %{public, name=shader_compiler_stats_signpost_enabled}u"
+ "Shader compiler stats signpost configured via environment variable: %{public, name=shader_compiler_stats_signpost_enabled}u"
+ "ShaderCompilerStatSignpostConfiguration"
+ "ShaderCompilerStatSignpostConfigurationError"
+ "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\nDetached = %{public, name=detached}d\nNextDrawable Wait = %{public, name=next_drawable_wait}.3fms\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\nDetached = %{public, name=detached}d\nNextDrawable Wait = %{public, name=next_drawable_wait}.3fms\nGPTk Num Render Encoder = %{public, name=gptk_num_RenderEncoder}d\nGPTk Num Compute Encoder = %{public, name=gptk_num_ComputeEncoder}d\nGPTk Num Blit Encoder = %{public, name=gptk_num_BlitEncoder}d\nGPTk Num Command Buffer = %{public, name=gptk_num_CommandBuffer}d\nGPTk Num Dispatch = %{public, name=gptk_num_Dispatch}d\nGPTk Num Dispatch Mesh = %{public, name=gptk_num_DispatchMesh}d\nGPTk Num Fragment Draw = %{public, name=gptk_num_FragmentDraw}d\nGPTk Num Geometry Draw = %{public, name=gptk_num_GeometryDraw}d\nGPTk Num Tessellation Draw = %{public, name=gptk_num_TessellationDraw}d\nGPTk Num GeometryTess Draw = %{public, name=gptk_num_GeometryTessDraw}d\nGPTk Num Clear = %{public, name=gptk_num_Clear}d\nGPTk Num Copy = %{public, name=gptk_num_Copy}d\nGPTk Num Execute Indirect = %{public, name=gptk_num_ExecuteIndirect}d\nGPTk Num Acceleration Encoder = %{public, name=gptk_num_AccelerationEncoder}d\nGPTk Num Dispatch Rays = %{public, name=gptk_num_DispatchRays}d\nGPTk Num Ray Query = %{public, name=gptk_num_RayQuery}d\nGPTk Num Build BVH = %{public, name=gptk_num_BuildBVH}d\nGPTk Num RefitB VH = %{public, name=gptk_num_RefitBVH}d\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\nDetached = %{public, name=detached}d\nNextDrawable Wait = %{public, name=next_drawable_wait}.3fms\nMetalFX Enabled = %{public, name=metal_fx_enabled}d\nMetalFX Auto Exposure Enabled = %{public, name=metal_fx_auto_exposure_enabled}d\nMetalFX Frame Interpolator Enabled = %{public, name=metal_fx_frame_interpolator_enabled}d\nMetalFX Exposure = %{public, name=metal_fx_exposure}.3f\nMetalFX Scaling Ratio = %{public, name=metal_fx_scaling_ratio}.3f\nMetalFX Scaling Method = %{public, name=metal_fx_scaling_method}d\nMetalFX Input Width (pixels) = %{public, name=metal_fx_input_pixels_width}d\nMetalFX Input Height (pixels) = %{public, name=metal_fx_input_pixels_height}d\nMetalFX Target Width (pixels) = %{public, name=metal_fx_target_pixels_width}d\nMetalFX Target Height (pixels) = %{public, name=metal_fx_target_pixels_height}d\nMetalFX Frame Interpolator Delta Time = %{public, name=metal_fx_frame_interpolator_delta_time}.3fms\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\nDetached = %{public, name=detached}d\nNextDrawable Wait = %{public, name=next_drawable_wait}.3fms\nMetalFX Enabled = %{public, name=metal_fx_enabled}d\nMetalFX Auto Exposure Enabled = %{public, name=metal_fx_auto_exposure_enabled}d\nMetalFX Frame Interpolator Enabled = %{public, name=metal_fx_frame_interpolator_enabled}d\nMetalFX Exposure = %{public, name=metal_fx_exposure}.3f\nMetalFX Scaling Ratio = %{public, name=metal_fx_scaling_ratio}.3f\nMetalFX Scaling Method = %{public, name=metal_fx_scaling_method}d\nMetalFX Input Width (pixels) = %{public, name=metal_fx_input_pixels_width}d\nMetalFX Input Height (pixels) = %{public, name=metal_fx_input_pixels_height}d\nMetalFX Target Width (pixels) = %{public, name=metal_fx_target_pixels_width}d\nMetalFX Target Height (pixels) = %{public, name=metal_fx_target_pixels_height}d\nMetalFX Frame Interpolator Delta Time = %{public, name=metal_fx_frame_interpolator_delta_time}.3fms\nGPTk Num Render Encoder = %{public, name=gptk_num_RenderEncoder}d\nGPTk Num Compute Encoder = %{public, name=gptk_num_ComputeEncoder}d\nGPTk Num Blit Encoder = %{public, name=gptk_num_BlitEncoder}d\nGPTk Num Command Buffer = %{public, name=gptk_num_CommandBuffer}d\nGPTk Num Dispatch = %{public, name=gptk_num_Dispatch}d\nGPTk Num Dispatch Mesh = %{public, name=gptk_num_DispatchMesh}d\nGPTk Num Fragment Draw = %{public, name=gptk_num_FragmentDraw}d\nGPTk Num Geometry Draw = %{public, name=gptk_num_GeometryDraw}d\nGPTk Num Tessellation Draw = %{public, name=gptk_num_TessellationDraw}d\nGPTk Num GeometryTess Draw = %{public, name=gptk_num_GeometryTessDraw}d\nGPTk Num Clear = %{public, name=gptk_num_Clear}d\nGPTk Num Copy = %{public, name=gptk_num_Copy}d\nGPTk Num Execute Indirect = %{public, name=gptk_num_ExecuteIndirect}d\nGPTk Num Acceleration Encoder = %{public, name=gptk_num_AccelerationEncoder}d\nGPTk Num Dispatch Rays = %{public, name=gptk_num_DispatchRays}d\nGPTk Num Ray Query = %{public, name=gptk_num_RayQuery}d\nGPTk Num Build BVH = %{public, name=gptk_num_BuildBVH}d\nGPTk Num RefitB VH = %{public, name=gptk_num_RefitBVH}d\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\nFrameDetachments (count, detach_count) =%{public, signpost.aggregation:count, group=FrameDetachments, unit=detach_count}u\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\nFrameDetachments (count, detach_count) =%{public, signpost.aggregation:count, group=FrameDetachments, unit=detach_count}u\nMetalFX (count, MetalFXEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFX, unit=MetalFXEnabledFrames}u\nMetalFXTemporalScaling (count, MetalFXTemporalScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXTemporalScaling, unit=MetalFXTemporalScalingFrames}u\nMetalFXSpatialScaling (count, MetalFXSpatialScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXSpatialScaling, unit=MetalFXSpatialScalingFrames}u\nMetalFXDenoisingScaling (count, MetalFXDenoisingScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXDenoisingScaling, unit=MetalFXDenoisingScalingFrames}u\nMetalFXFrameInterpolator (count, MetalFXFrameInterpolatorEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFXFrameInterpolator, unit=MetalFXFrameInterpolatorEnabledFrames}u\nMetalFXExposure (count, MetalFXAutoExposureEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFXExposure, unit=MetalFXAutoExposureEnabledFrames}u\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio average, count) =%{public, signpost.aggregation:measure_average, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio min, count) =%{public, signpost.aggregation:measure_min, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio max, count) =%{public, signpost.aggregation:measure_max, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio stddev, count) =%{public, signpost.aggregation:measure_stddev, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure average, count) =%{public, signpost.aggregation:measure_average, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure min, count) =%{public, signpost.aggregation:measure_min, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure max, count) =%{public, signpost.aggregation:measure_max, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure stddev, count) =%{public, signpost.aggregation:measure_stddev, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime average, ms) =%{public, signpost.aggregation:measure_average, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime min, ms) =%{public, signpost.aggregation:measure_min, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime max, ms) =%{public, signpost.aggregation:measure_max, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\nFrameDetachments (count, detach_count) =%{public, signpost.aggregation:count, group=FrameDetachments, unit=detach_count}u\nPresentedFrameIntervals (count, frame-on-glass_intervals) =%{public, signpost.aggregation:count, group=PresentedFrameIntervals, unit=frame-on-glass_intervals}u\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass average, ms) =%{public, signpost.aggregation:measure_average, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass min, ms) =%{public, signpost.aggregation:measure_min, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass max, ms) =%{public, signpost.aggregation:measure_max, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrames_NextDrawableWaitWaltime (NextDrawableWaitWaltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=NextDrawableWaitWaltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\nFrameDetachments (count, detach_count) =%{public, signpost.aggregation:count, group=FrameDetachments, unit=detach_count}u\nPresentedFrameIntervals (count, frame-on-glass_intervals) =%{public, signpost.aggregation:count, group=PresentedFrameIntervals, unit=frame-on-glass_intervals}u\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass average, ms) =%{public, signpost.aggregation:measure_average, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass min, ms) =%{public, signpost.aggregation:measure_min, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass max, ms) =%{public, signpost.aggregation:measure_max, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nMetalFX (count, MetalFXEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFX, unit=MetalFXEnabledFrames}u\nMetalFXTemporalScaling (count, MetalFXTemporalScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXTemporalScaling, unit=MetalFXTemporalScalingFrames}u\nMetalFXSpatialScaling (count, MetalFXSpatialScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXSpatialScaling, unit=MetalFXSpatialScalingFrames}u\nMetalFXDenoisingScaling (count, MetalFXDenoisingScalingFrames) =%{public, signpost.aggregation:count, group=MetalFXDenoisingScaling, unit=MetalFXDenoisingScalingFrames}u\nMetalFXFrameInterpolator (count, MetalFXFrameInterpolatorEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFXFrameInterpolator, unit=MetalFXFrameInterpolatorEnabledFrames}u\nMetalFXExposure (count, MetalFXAutoExposureEnabledFrames) =%{public, signpost.aggregation:count, group=MetalFXExposure, unit=MetalFXAutoExposureEnabledFrames}u\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio average, count) =%{public, signpost.aggregation:measure_average, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio min, count) =%{public, signpost.aggregation:measure_min, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio max, count) =%{public, signpost.aggregation:measure_max, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXScalingRatio (MetalFXScalingRatio stddev, count) =%{public, signpost.aggregation:measure_stddev, group=MetalFX, type=MetalFXScalingRatio, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure average, count) =%{public, signpost.aggregation:measure_average, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure min, count) =%{public, signpost.aggregation:measure_min, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure max, count) =%{public, signpost.aggregation:measure_max, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFX_MetalFXExposure (MetalFXExposure stddev, count) =%{public, signpost.aggregation:measure_stddev, group=MetalFX, type=MetalFXExposure, measure_unit=count}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime average, ms) =%{public, signpost.aggregation:measure_average, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime min, ms) =%{public, signpost.aggregation:measure_min, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime max, ms) =%{public, signpost.aggregation:measure_max, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\nMetalFXFrameInterpolator_MetalFXInterpolatorDeltaTime (MetalFXInterpolatorDeltaTime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=MetalFXFrameInterpolator, type=MetalFXInterpolatorDeltaTime, measure_unit=ms}.3f\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Signpost ID is Shared Image Queue ID\nName: '%{public, name=name}@'\nHeight (points): %{public, name=Height, units=pixels}llu\nWidth: (points): %{public, name=Width, units=pixels}llu\nPixel format: %{public, name=PixelFormat}#llx\nPixel format name: %{public, name=PixelFormatName}@\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
+ "Spatial"
+ "Spatial | ANE"
+ "Spatial | GPU"
+ "Stencil8"
+ "TAAUv%d | %@"
+ "TAAUv3"
+ "TAAUv4"
+ "Temporal"
+ "Tessellation or Geometry Stage"
+ "Total compile time in ns"
+ "Understanding the Metal 4 core API"
+ "Unknown | ANE"
+ "Unknown | GPU"
+ "Unspecialized"
+ "Updated shader compiler stats signposting: %{public, name=previous_shader_compiler_stats_signposts_enabled}s -> %{public, name=updated_shader_compiler_stats_signposts_enabled}s"
+ "UpdatedShaderCompilerStatsSignpostingEnabled"
+ "Using Metal mesh shaders"
+ "Vertex Shader"
+ "X24_Stencil8"
+ "X32_Stencil8"
+ "YCBCR10_420_2P"
+ "YCBCR10_420_2P_HLG"
+ "YCBCR10_420_2P_PACKED"
+ "YCBCR10_420_2P_PACKED_HLG"
+ "YCBCR10_420_2P_PACKED_PQ"
+ "YCBCR10_420_2P_PACKED_XR"
+ "YCBCR10_420_2P_PACKED_sRGB"
+ "YCBCR10_420_2P_PQ"
+ "YCBCR10_420_2P_XR"
+ "YCBCR10_420_2P_sRGB"
+ "YCBCR10_422_2P"
+ "YCBCR10_422_2P_HLG"
+ "YCBCR10_422_2P_PACKED"
+ "YCBCR10_422_2P_PACKED_HLG"
+ "YCBCR10_422_2P_PACKED_PQ"
+ "YCBCR10_422_2P_PACKED_XR"
+ "YCBCR10_422_2P_PACKED_sRGB"
+ "YCBCR10_422_2P_PQ"
+ "YCBCR10_422_2P_XR"
+ "YCBCR10_422_2P_sRGB"
+ "YCBCR10_444_1P"
+ "YCBCR10_444_1P_HLG"
+ "YCBCR10_444_1P_PQ"
+ "YCBCR10_444_1P_XR"
+ "YCBCR10_444_1P_sRGB"
+ "YCBCR10_444_2P"
+ "YCBCR10_444_2P_HLG"
+ "YCBCR10_444_2P_PACKED"
+ "YCBCR10_444_2P_PACKED_HLG"
+ "YCBCR10_444_2P_PACKED_PQ"
+ "YCBCR10_444_2P_PACKED_XR"
+ "YCBCR10_444_2P_PACKED_sRGB"
+ "YCBCR10_444_2P_PQ"
+ "YCBCR10_444_2P_XR"
+ "YCBCR10_444_2P_sRGB"
+ "YCBCR12_420_2P"
+ "YCBCR12_420_2P_HLG"
+ "YCBCR12_420_2P_PACKED"
+ "YCBCR12_420_2P_PACKED_HLG"
+ "YCBCR12_420_2P_PACKED_PQ"
+ "YCBCR12_420_2P_PACKED_XR"
+ "YCBCR12_420_2P_PQ"
+ "YCBCR12_420_2P_XR"
+ "YCBCR12_422_2P"
+ "YCBCR12_422_2P_HLG"
+ "YCBCR12_422_2P_PACKED"
+ "YCBCR12_422_2P_PACKED_HLG"
+ "YCBCR12_422_2P_PACKED_PQ"
+ "YCBCR12_422_2P_PACKED_XR"
+ "YCBCR12_422_2P_PQ"
+ "YCBCR12_422_2P_XR"
+ "YCBCR12_444_2P"
+ "YCBCR12_444_2P_HLG"
+ "YCBCR12_444_2P_PACKED"
+ "YCBCR12_444_2P_PACKED_HLG"
+ "YCBCR12_444_2P_PACKED_PQ"
+ "YCBCR12_444_2P_PACKED_XR"
+ "YCBCR12_444_2P_PQ"
+ "YCBCR12_444_2P_XR"
+ "YCBCR8_420_2P"
+ "YCBCR8_420_2P_sRGB"
+ "YCBCR8_422_1P"
+ "YCBCR8_422_1P_REV"
+ "YCBCR8_422_1P_sRGB"
+ "YCBCR8_422_2P"
+ "YCBCR8_422_2P_sRGB"
+ "YCBCR8_444_2P"
+ "YCBCR8_444_2P_sRGB"
+ "YCBCRA8_444_1P"
+ "["
+ "[libMTLHud] %@"
+ "apple-internal-install"
+ "com.apple.D3DMetal"
+ "com.apple.FPMTLMetrics.insights.3to4.efficientencoding"
+ "com.apple.FPMTLMetrics.insights.barrier-usage"
+ "com.apple.FPMTLMetrics.insights.blitswap"
+ "com.apple.FPMTLMetrics.insights.compiler"
+ "com.apple.FPMTLMetrics.insights.gamemode"
+ "com.apple.FPMTLMetrics.insights.rebinding"
+ "com.apple.FPMTLMetrics.insights.tessellation"
+ "com.apple.MPL"
+ "com.apple.MessagesAirlockService"
+ "com.apple.MessagesBlastDoorService"
+ "com.apple.MetalMetrics"
+ "com.apple.MetalMetricsNotification"
+ "com.apple.d3dmetal"
+ "com.apple.d3dmetal.ae-count"
+ "com.apple.d3dmetal.be-count"
+ "com.apple.d3dmetal.buildbvh-count"
+ "com.apple.d3dmetal.cb-count"
+ "com.apple.d3dmetal.ce-count"
+ "com.apple.d3dmetal.clear-count"
+ "com.apple.d3dmetal.copy-count"
+ "com.apple.d3dmetal.disp-count"
+ "com.apple.d3dmetal.dispgraph-count"
+ "com.apple.d3dmetal.dispmesh-count"
+ "com.apple.d3dmetal.dispray-count"
+ "com.apple.d3dmetal.ei-count"
+ "com.apple.d3dmetal.event-signals"
+ "com.apple.d3dmetal.event-waits"
+ "com.apple.d3dmetal.fence-updates"
+ "com.apple.d3dmetal.fence-waits"
+ "com.apple.d3dmetal.fragdraw-count"
+ "com.apple.d3dmetal.geom-count"
+ "com.apple.d3dmetal.geomtess-count"
+ "com.apple.d3dmetal.global-barrier-count"
+ "com.apple.d3dmetal.icb-count"
+ "com.apple.d3dmetal.ie-count"
+ "com.apple.d3dmetal.rayquery-count"
+ "com.apple.d3dmetal.re-count"
+ "com.apple.d3dmetal.refitbfh-count"
+ "com.apple.d3dmetal.skipped-global-barrier-count"
+ "com.apple.d3dmetal.tess-count"
+ "com.apple.d3dmetal.texture-view-count"
+ "com.apple.dock"
+ "com.apple.gputoolsserviced"
+ "com.apple.hud-label.hud"
+ "com.apple.hud-label.metalfx"
+ "com.apple.hud-label.metalfx.content_resolution"
+ "com.apple.hud-label.metalfx.resolution"
+ "com.apple.hud-label.metalfx.timing"
+ "com.apple.hud-label.metalfx.v2.exposure"
+ "com.apple.hud-label.metalfx.v2.input_resolution"
+ "com.apple.hud-label.metalfx.v2.scaling"
+ "com.apple.hud-label.metalfx.v2.target_resolution"
+ "com.apple.hud-stat.rosetta"
+ "com.apple.system.console_mode_changed"
+ "com.apple.system.sustained_execution_mode_changed"
+ "globalMetrics"
+ "https://developer.apple.com/documentation/metal/resource_synchronization?language=objc"
+ "https://developer.apple.com/documentation/metal/shader_libraries/metal_binary_archives/creating_binary_archives_from_device-built_pipeline_state_objects?language=objc"
+ "https://developer.apple.com/documentation/metal/understanding-the-metal-4-core-api?language=objc"
+ "https://developer.apple.com/videos/play/wwdc2021/10148/"
+ "https://developer.apple.com/videos/play/wwdc2022/10162/"
+ "i"
+ "identifier=%@, group=%d, unit=%d"
+ "libMTLHud"
+ "sandboxReceipt"
+ "type < FP_MTL_METRICS_ARRAY_LENGTH(names)"
+ "v12@?0i8"
+ "v16@?0^{FPMTLMetricsGPUTimeTrackerFrameTimingData=^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ^{FPMTLMetricsTimeRange}^{FPMTLMetricsTimeRange}QQ[7^{FPMTLMetricsTimeRange}][7^{FPMTLMetricsTimeRange}][7Q][7Q]QQQQQBB}8"
+ "v16@?0^{FPMTLMetricsIOReportMetricsBacking=dddddddd[24d]IQ}8"
+ "v16@?0^{FPMTLMetricsShaderInfo=QBB[128c]}8"
+ "v20@?0I8Q12"
+ "v28@?0@\"NSString\"8I16^{FPMTLMetricsGPUTimeTrackerCommonObjectRecord={FPMTLMetricsMetricValue=(?=d*)dddddQddQ}{FPMTLMetricsMetricValue=(?=d*)dddddQddQ}Q}20"
+ "vector"
+ "x"
+ "\x9c"
+ "\xf1"
- "\nTotal instructions: \t\t%{public, name=ri_instructions}llu instr\nTotal P-core instructions: \t%{public, name=ri_pinstructions}llu pinstr\nPhysical footprint: \t\t%{public, name=ri_phys_footprint}.2fMiB\nPeak Physical footprint: \t%{public, name=ri_lifetime_max_phys_footprint}.2fMiB\nMemory limit headroom:\t\t%{public, name=os_proc_available_memory}.2fMiB\nDiskIO - Reads: \t\t%{public, name=ri_diskio_bytesread}.2fMiB\nDiskIO - Writes: \t\t%{public, name=ri_diskio_byteswritten}.2fMiB\nDiskIO - Logical Writes: \t%{public, name=ri_logical_writes}.2fMiB\n"
- ".cxx_destruct"
- "@\"FPDurationStatistics\""
- "@\"FPOnGlassCAMetalLayerDrawableInterval\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@16@0:8"
- "@32@0:8^v16d24"
- "B"
- "Bundle Info:\nBundleID: '%{public, name=BundleID}@'\nBundle Short Version: '%{public, name=BundleShortVersion}@'\nBundle Version: '%{public, name=BundleVersion}@'\n"
- "Could not find command buffer state (Signpost ID is from pointer)"
- "Encountered a NULL command buffer address when starting to track new command buffer"
- "FPCAMetalLayerState"
- "FPDurationStatistics"
- "FPInFlightCommandBuffer"
- "FPInFlightDrawableLifetime"
- "FPOnGlassCAMetalLayerDrawableInterval"
- "I"
- "I16@0:8"
- "MissingCommandBufferState"
- "NullCommandBufferAddress"
- "Overwriting command buffer. (Signpost ID is from pointer)"
- "OverwritingCommandBuffer"
- "Q"
- "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
- "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
- "Signpost ID is Shared Image Queue ID\nFrames (count, frames) =%{public, signpost.aggregation:count, group=Frames, unit=frames}u\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalEndToEndWalltime (TotalEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_CPUEndToEndWalltime (CPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=CPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_GPUEndToEndWalltime (GPUEndToEndWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUEndToEndWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_TotalOnGPUWalltime (TotalOnGPUWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=TotalOnGPUWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime average, ms) =%{public, signpost.aggregation:measure_average, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime min, ms) =%{public, signpost.aggregation:measure_min, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime max, ms) =%{public, signpost.aggregation:measure_max, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrames_GPUDoneToCompletedWalltime (GPUDoneToCompletedWalltime stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=Frames, type=GPUDoneToCompletedWalltime, measure_unit=ms}.3f\nFrameCommandBuffers (count, command_buffers) =%{public, signpost.aggregation:count, group=FrameCommandBuffers, unit=command_buffers}u\nPresentedFrameIntervals (count, frame-on-glass_intervals) =%{public, signpost.aggregation:count, group=PresentedFrameIntervals, unit=frame-on-glass_intervals}u\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass average, ms) =%{public, signpost.aggregation:measure_average, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass min, ms) =%{public, signpost.aggregation:measure_min, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass max, ms) =%{public, signpost.aggregation:measure_max, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\nPresentedFrameIntervals_TimeOnGlass (TimeOnGlass stddev, ms) =%{public, signpost.aggregation:measure_stddev, group=PresentedFrameIntervals, type=TimeOnGlass, measure_unit=ms}.3f\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
- "Signpost ID is Shared Image Queue ID\nName: '%{public, name=name}@'\nHeight (points): %{public, name=Height, units=pixels}llu\nWidth: (points): %{public, name=Width, units=pixels}llu\nPixel format: %{public, name=PixelFormat}#llx\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
- "TI,R,N,V_count"
- "Td,N,V_totalDurationSec"
- "Td,N,V_totalDurationSecSquared"
- "Td,R,N"
- "Td,R,N,V_internalMinSec"
- "Td,R,N,V_maxSec"
- "^v"
- "_acquiredInFlightDrawables"
- "_acquiredTime"
- "_address"
- "_attributedCommandBuffers"
- "_clientPresentationLatenessStats"
- "_clientPresentedInFlightDrawables"
- "_commandBufferCount"
- "_commitTime"
- "_count"
- "_creationTime"
- "_drawableID"
- "_gpuEnd"
- "_gpuStart"
- "_hasTargets"
- "_hasUpdatedMetadata"
- "_height"
- "_imageQueueID"
- "_inFlightStart"
- "_internalMinSec"
- "_intersectsMultipleLayers"
- "_kernelSchedulingEnd"
- "_kernelSchedulingStart"
- "_layerAddress"
- "_maxSec"
- "_name"
- "_needsReport"
- "_onGPUEnd"
- "_onGPUStart"
- "_onGPUTime"
- "_onGlassPresentationLatenessStats"
- "_onGlassStart"
- "_onScreenStats"
- "_pixelFormat"
- "_presentCalledTime"
- "_presentedCPUWalltimeStats"
- "_presentedCommandBufferCount"
- "_presentedEndToEndDrawableLifetimeStats"
- "_presentedGPUFinishToPresentLatency"
- "_presentedGPUWalltimeStats"
- "_presentedOnGPUTimeStats"
- "_previousDrawableOnGlassDrawable"
- "_previousMetadataReportedMCTR"
- "_signpostID"
- "_skippedCPUWalltimeStats"
- "_skippedCommandBufferCount"
- "_skippedEndToEndDrawableLifetimeStats"
- "_skippedGPUFinishToPresentLatency"
- "_skippedGPUWalltimeStats"
- "_skippedOnGPUTimeStats"
- "_surfaceID"
- "_timeCreatedMCTR"
- "_totalDurationSec"
- "_totalDurationSecSquared"
- "_waitStartTime"
- "_width"
- "addDurationSec:"
- "addObject:"
- "allValues"
- "averageMs"
- "averageNs"
- "averageSec"
- "boolValue"
- "bundleIdentifier"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dealloc"
- "doubleValue"
- "firstObject"
- "init"
- "initWithAddress:creationTime:"
- "internalMinSec"
- "mainBundle"
- "maxMs"
- "maxNs"
- "maxSec"
- "minMs"
- "minNs"
- "minSec"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "q24@?0@\"FPInFlightCommandBuffer\"8@\"FPInFlightCommandBuffer\"16"
- "removeAllObjects"
- "removeObjectForKey:"
- "reset"
- "setObject:forKeyedSubscript:"
- "setTotalDurationSec:"
- "setTotalDurationSecSquared:"
- "sortUsingComparator:"
- "standardUserDefaults"
- "stddevMs"
- "stddevNs"
- "stddevSec"
- "timeIntervalSinceReferenceDate"
- "totalDurationMs"
- "totalDurationNs"
- "totalDurationSec"
- "totalDurationSecSquared"
- "unsignedLongLongValue"
- "v16@0:8"
- "v16@?0@\"FPInFlightCommandBuffer\"8"
- "v24@0:8d16"

```
