## PerformanceTraceModule

> `/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule`

```diff

-655.10.5.3.0
-  __TEXT.__text: 0x31a4
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_methlist: 0x454
+696.0.1.0.0
+  __TEXT.__text: 0x2e80
+  __TEXT.__objc_methlist: 0x49c
   __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x2a2
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__cstring: 0x29e
   __TEXT.__oslogstring: 0x53b
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methname: 0xf65
-  __TEXT.__objc_methtype: 0x381
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x408
+  __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x608
+  __AUTH_CONST.__objc_const: 0x610
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA15723D-10FB-302C-8033-EB4DF89F0F07
-  Functions: 86
-  Symbols:   78
-  CStrings:  274
+  UUID: 1F5BCD34-B381-3EA9-BFE6-4B9C0720F2F0
+  Functions: 88
+  Symbols:   82
+  CStrings:  72
 
Symbols:
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CCUIContentModuleContext\""
- "@\"CCUIPerformanceTraceModuleViewController\""
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PTGlobalStateChangeMonitor\""
- "@\"PTTraceSession\""
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CCUIContentModule"
- "CCUIPerformanceTraceModule"
- "CCUIPerformanceTraceModuleViewController"
- "NSObject"
- "PTTraceSessionDelegate"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"CCUIPerformanceTraceModuleViewController\",&,N,V_viewController"
- "T@\"NSArray\",&,N,V_fgSceneIdentifiersAtTraceStart"
- "T@\"NSArray\",&,N,V_supportedTracePlanNames"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stateChangeQueue"
- "T@\"NSString\",&,N,V_selectedTracePlanName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"PTGlobalStateChangeMonitor\",R,N,V_stateChangeMonitor"
- "T@\"PTTraceSession\",&,N,V_performanceTraceSession"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "TB,?,R,N"
- "TB,N,V_selectedTracePlanIsPassive"
- "TB,N,V_selectedTracePlanIsPassivePowerMetrics"
- "TQ,?,R,N"
- "TQ,N,V_state"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_canShowWhileLocked"
- "_cleanupSessionAndUpdateState:"
- "_collectPassiveTrace"
- "_contentModuleContext"
- "_fgSceneIdentifiersAtTraceStart"
- "_getFGSceneIdentifiers"
- "_localizedString:"
- "_makeTracePlanNameMenuItem:"
- "_passiveTraceConfig"
- "_performanceTraceGlobalStateDidChange"
- "_performanceTraceSession"
- "_recreateMenu"
- "_selectedTracePlanIsPassive"
- "_selectedTracePlanIsPassivePowerMetrics"
- "_selectedTracePlanName"
- "_startRecording"
- "_startRecordingPowerMetricsPassiveTrace"
- "_startRecordingRegularTrace"
- "_state"
- "_stateChangeMonitor"
- "_stateChangeQueue"
- "_stopRecording"
- "_stopRecordingPowerMetricsPassiveTrace"
- "_stopRecordingRegularTrace"
- "_supportedTracePlanNames"
- "_updateGlyph"
- "_updatePlanNameConvenienceProperties"
- "_updateState:"
- "_updateSubtitle:"
- "_viewController"
- "addObject:"
- "applySetting:"
- "autorelease"
- "availableTracePlanNames"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "bundleForClass:"
- "buttonTapped:forEvent:"
- "buttonView"
- "ccui_bundleForModuleInstance:"
- "ccui_displayName"
- "class"
- "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:"
- "collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:"
- "configWithTracePlanName:"
- "conformsToProtocol:"
- "contentModuleContext"
- "contentViewController"
- "contentViewControllerForContext:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionary"
- "displayLayoutContextProvider"
- "displayNameForState:"
- "displayNameForTracePlanName:"
- "displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:"
- "enqueueStatusUpdate:"
- "expandsGridSizeClassesForAccessibility"
- "fgSceneIdentifiersAtTraceStart"
- "foregroundApplicationSceneBundleIdentifiers"
- "globalSettingsAreLocked"
- "hash"
- "init"
- "initWithConfig:"
- "initWithQueue:stateChangeBlock:"
- "initWithTitle:identifier:handler:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPassiveTracePlanName:"
- "isPowerMetricsPassiveTracePlanName:"
- "isProxy"
- "isSupported"
- "localizedStringForKey:value:table:"
- "moduleDescription"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "performanceTraceDidComplete:withToken:withError:"
- "performanceTraceDidStart:"
- "performanceTraceDidStop:"
- "performanceTraceSession"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "selectedTracePlanIsPassive"
- "selectedTracePlanIsPassivePowerMetrics"
- "selectedTracePlanName"
- "self"
- "setContentModuleContext:"
- "setDelegate:"
- "setEnabled:"
- "setFgSceneIdentifiersAtTraceStart:"
- "setGlyphImage:"
- "setIndentation:"
- "setMenuItems:"
- "setObject:forKeyedSubscript:"
- "setPerformanceTraceSession:"
- "setSelected:"
- "setSelectedGlyphColor:"
- "setSelectedTracePlanIsPassive:"
- "setSelectedTracePlanIsPassivePowerMetrics:"
- "setSelectedTracePlanName:"
- "setSelectedValueText:"
- "setState:"
- "setStateChangeQueue:"
- "setSupportedTracePlanNames:"
- "setSymbolicate:"
- "setTitle:"
- "setTraceDurationSecs:"
- "setTraceRecordArgs:"
- "setUserSelectedTracePlanName:"
- "setValueText:"
- "setViewController:"
- "sharedConfig:"
- "shouldBeginTransitionToExpandedContentModule"
- "startPerformanceTrace"
- "state"
- "stateChangeMonitor"
- "stateChangeQueue"
- "statusUpdateWithMessage:type:"
- "stopPerformanceTrace"
- "superclass"
- "supportedGridSizeClasses"
- "supportedTracePlanNames"
- "systemBlueColor"
- "systemImageNamed:"
- "userSelectedTracePlanName"
- "userSpecifiedCustomTracePlanArguments"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "viewController"
- "viewWillAppear:"
- "willTransitionToExpandedContentMode:"
- "zone"

```
