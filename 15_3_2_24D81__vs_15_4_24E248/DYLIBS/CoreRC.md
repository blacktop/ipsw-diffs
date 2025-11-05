## CoreRC

> `/System/Library/PrivateFrameworks/CoreRC.framework/Versions/A/CoreRC`

```diff

-249.80.2.0.0
-  __TEXT.__text: 0x46154
+254.100.6.0.0
+  __TEXT.__text: 0x49ee4
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x4558
-  __TEXT.__const: 0x3b8
-  __TEXT.__cstring: 0xf38e
+  __TEXT.__objc_methlist: 0x4d94
+  __TEXT.__const: 0x3f8
+  __TEXT.__cstring: 0xf5ae
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x1a5
-  __TEXT.__unwind_info: 0x11a8
-  __TEXT.__objc_classname: 0x5b8
-  __TEXT.__objc_methname: 0x955f
-  __TEXT.__objc_methtype: 0x27a9
-  __TEXT.__objc_stubs: 0x7c40
-  __DATA_CONST.__got: 0x248
+  __TEXT.__oslogstring: 0x1d1
+  __TEXT.__unwind_info: 0x1520
+  __TEXT.__objc_classname: 0x5ca
+  __TEXT.__objc_methname: 0x9785
+  __TEXT.__objc_methtype: 0x27f0
+  __TEXT.__objc_stubs: 0x7e00
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x1218
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2248
+  __DATA_CONST.__objc_selrefs: 0x2350
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x160
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_arraydata: 0x168
   __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0xc90
-  __AUTH_CONST.__cfstring: 0x3300
-  __AUTH_CONST.__objc_const: 0x92a0
+  __AUTH_CONST.__const: 0xcf0
+  __AUTH_CONST.__cfstring: 0x3440
+  __AUTH_CONST.__objc_const: 0x8a20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x2dc
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x1018
   __DATA.__bss: 0x380
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x380
   __DATA_DIRTY.__bss: 0x10
-  - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B957039-DC28-368B-812A-DB21322917C2
-  Functions: 1773
-  Symbols:   3903
-  CStrings:  3888
+  UUID: E6E261C5-CCB4-385F-868C-9F15F497F86A
+  Functions: 2327
+  Symbols:   4668
+  CStrings:  3964
 
Symbols:
+ +[CECEDIDAttributes supportsSecureCoding]
+ +[NSUserDefaults(CEC) cecUserDefaults].cold.1
+ -[AppleIRCommand getVendorSpecificHIDUsagePage:usageID:ignoreRepeats:].cold.1
+ -[AppleIRCommand getVendorSpecificHIDUsagePage:usageID:ignoreRepeats:].cold.2
+ -[AppleIRDeviceProvider _dispatchAppleVendorEventPage:usage:timestamp:toDevice:].cold.1
+ -[AppleIRDeviceProvider _dispatchAppleVendorEventPage:usage:timestamp:toDevice:].cold.2
+ -[AppleIRDeviceProvider _dispatchEventWithCommand:timestamp:toDevice:].cold.1
+ -[AppleIRDeviceProvider _dispatchEventWithCommand:timestamp:toDevice:].cold.2
+ -[AppleIRDeviceProvider _dispatchEventWithCommand:timestamp:toDevice:].cold.3
+ -[AppleIRDeviceProvider _dispatchEventWithCommand:timestamp:toDevice:].cold.4
+ -[AppleIRDeviceProvider _synthesizeButtonReleaseWithTimestamp:].cold.1
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.1
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.10
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.11
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.12
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.13
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.14
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.15
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.2
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.3
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.4
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.5
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.6
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.7
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.8
+ -[AppleIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.9
+ -[CECBusPollingOperation poll].cold.1
+ -[CECBusPollingOperation poll].cold.2
+ -[CECEDIDAttributes address]
+ -[CECEDIDAttributes copyWithZone:]
+ -[CECEDIDAttributes dealloc]
+ -[CECEDIDAttributes description]
+ -[CECEDIDAttributes encodeWithCoder:]
+ -[CECEDIDAttributes initWithAttributes:]
+ -[CECEDIDAttributes initWithCoder:]
+ -[CECEDIDAttributes initWithModelName:]
+ -[CECEDIDAttributes initWithVendorID:]
+ -[CECEDIDAttributes modelName]
+ -[CECEDIDAttributes productID]
+ -[CECEDIDAttributes setAddress:]
+ -[CECEDIDAttributes setModelName:]
+ -[CECEDIDAttributes setProductID:]
+ -[CECEDIDAttributes setUuid:]
+ -[CECEDIDAttributes setVendorID:]
+ -[CECEDIDAttributes setWeek:]
+ -[CECEDIDAttributes setYear:]
+ -[CECEDIDAttributes uuid]
+ -[CECEDIDAttributes vendorID]
+ -[CECEDIDAttributes week]
+ -[CECEDIDAttributes year]
+ -[CECFakeInterface receivedFrame:].cold.1
+ -[CECFakeInterface setBlockedMessages:]
+ -[CECFakeInterfaceListener createDeviceProvider:andFakeInterface:withPhysicalAddress:andLogicalAddress:].cold.1
+ -[CECFakeInterfaceListener createDeviceProvider:andFakeInterface:withPhysicalAddress:andLogicalAddress:].cold.2
+ -[CECFakeInterfaceListener createDeviceProvider:andFakeInterface:withPhysicalAddress:andLogicalAddress:].cold.3
+ -[CECInterface allocateCECAddress:forDeviceType:error:].cold.2
+ -[CECInterface allocateCECAddress:forDeviceType:error:].cold.3
+ -[CECInterface allocateCECAddress:forDeviceType:error:].cold.4
+ -[CECInterface allocateCECAddress:forDeviceType:error:].cold.5
+ -[CECInterface pingTo:acknowledged:error:].cold.1
+ -[CECRouterInterface receivedFrame:].cold.1
+ -[CoreCECBus activeSource].cold.1
+ -[CoreCECBus dealloc]
+ -[CoreCECBus didChangeLinkState:physicalAddress:].cold.1
+ -[CoreCECBus edidAttributes]
+ -[CoreCECBus notifyDelegateLinkStateUpdated].cold.1
+ -[CoreCECBus removeDeviceWithType:].cold.1
+ -[CoreCECBus removeDeviceWithType:].cold.2
+ -[CoreCECBus setEdidAttributes:]
+ -[CoreCECBus setOSDName:error:].cold.1
+ -[CoreCECBus setOSDName:error:].cold.2
+ -[CoreCECBus setOSDName:error:].cold.3
+ -[CoreCECBus setTvLanguageCode:error:].cold.1
+ -[CoreCECBus setTvLanguageCode:error:].cold.2
+ -[CoreCECBus setTvLanguageCode:error:].cold.3
+ -[CoreCECBusClient removeDeviceWithType:].cold.1
+ -[CoreCECBusClient removeDeviceWithType:].cold.2
+ -[CoreCECBusClient removeDeviceWithType:].cold.3
+ -[CoreCECBusClient setTvLanguageCode:error:].cold.1
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.1
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.2
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.3
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.4
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.5
+ -[CoreCECBusProvider _sendMessage:toDevice:withRetryCount:error:].cold.6
+ -[CoreCECBusProvider addDeviceWithLogicalAddress:message:reason:].cold.1
+ -[CoreCECBusProvider allocateCECAddressForDeviceType:withCECAddress:error:].cold.1
+ -[CoreCECBusProvider allocateCECAddressForDeviceType:withCECAddress:error:].cold.2
+ -[CoreCECBusProvider allocateCECAddressForDeviceType:withCECAddress:error:].cold.3
+ -[CoreCECBusProvider allocateCECAddressForDeviceType:withCECAddress:error:].cold.4
+ -[CoreCECBusProvider pollingOperation:deviceNotRespondingAtAddress:].cold.1
+ -[CoreCECBusProvider pollingOperation:shouldSkipAddress:].cold.1
+ -[CoreCECBusProvider reallocateAllCECAddresses:].cold.1
+ -[CoreCECBusProvider refreshDevicesWithInitiator:error:].cold.1
+ -[CoreCECBusProvider refreshDevicesWithInitiator:error:].cold.2
+ -[CoreCECBusProvider refreshDevicesWithInitiator:error:].cold.3
+ -[CoreCECBusProvider sendMessage:withRetryCount:error:].cold.1
+ -[CoreCECBusProvider sendMessage:withRetryCount:error:].cold.2
+ -[CoreCECBusProvider setLinkState:physicalAddress:].cold.1
+ -[CoreCECBusProvider setLinkState:physicalAddress:].cold.2
+ -[CoreCECBusProvider updateAllowHibernation].cold.1
+ -[CoreCECDevice deckControlCommandHasBeenReceived:fromDevice:].cold.1
+ -[CoreCECDevice deckControlPlayHasBeenReceived:fromDevice:].cold.1
+ -[CoreCECDevice deckControlSetDeckStatus:error:].cold.1
+ -[CoreCECDevice deckControlSetDeckStatus:error:].cold.2
+ -[CoreCECDevice deckControlStatusHasBeenUpdated:fromDevice:].cold.1
+ -[CoreCECDevice notifyDelegateActiveSourceStatusHasChanged].cold.1
+ -[CoreCECDevice notifyDelegateAudioStatusReceived:muteStatus:].cold.1
+ -[CoreCECDevice notifyDelegateDeckControlCommandHasBeenReceived:command:].cold.1
+ -[CoreCECDevice notifyDelegateDeckControlPlayHasBeenReceived:playMode:].cold.1
+ -[CoreCECDevice notifyDelegateDeckControlStatusHasBeenUpdated:deckInfo:].cold.1
+ -[CoreCECDevice notifyDelegateFeatureAbort:].cold.1
+ -[CoreCECDevice notifyDelegateReceivedRequestAudioReturnChannelStatusChangeTo:fromDevice:].cold.1
+ -[CoreCECDevice notifyDelegateReceivedRequestSystemAudioModeStatusChangeTo:fromDevice:].cold.1
+ -[CoreCECDevice notifyDelegateRequestSystemAudioModeStatusChangeTo:didFinishWithResult:error:].cold.1
+ -[CoreCECDevice notifyDelegateShouldAssertActiveSource].cold.1
+ -[CoreCECDevice notifyDelegateStandbyRequestHasBeenReceived:].cold.1
+ -[CoreCECDevice receivedRequestAudioReturnChannelStatusChangeTo:fromDevice:].cold.1
+ -[CoreCECDevice receivedRequestSystemAudioModeStatusChangeTo:fromDevice:].cold.1
+ -[CoreCECDevice removeFromBus]
+ -[CoreCECDevice removeFromBus].cold.1
+ -[CoreCECDevice setAudioMuteStatus:error:].cold.1
+ -[CoreCECDevice setAudioReturnChannelControlEnabled:error:].cold.1
+ -[CoreCECDevice setAudioVolumeStatus:error:].cold.1
+ -[CoreCECDevice setPowerStatus:error:].cold.1
+ -[CoreCECDevice setSupportedAudioFormats:error:].cold.1
+ -[CoreCECDevice setSupportedAudioFormats:error:].cold.2
+ -[CoreCECDevice setSystemAudioControlEnabled:error:].cold.1
+ -[CoreCECDevice standbyRequestHasBeenReceived:].cold.1
+ -[CoreCECDevice systemAudioModeRequest:error:].cold.1
+ -[CoreCECDevice(Analytics) sendAnalyticsForErrorString:vendorID:productID:serialNumber:week:year:monitorName:].cold.1
+ -[CoreCECDevice(Analytics) sendLogicalAddressErrorAnalyticsForMessage:].cold.1
+ -[CoreCECDeviceClient deckControlCommandWithMode:target:error:].cold.1
+ -[CoreCECDeviceClient deckControlPlayWithMode:target:error:].cold.1
+ -[CoreCECDeviceClient deckControlRefreshStatus:requestType:error:].cold.1
+ -[CoreCECDeviceClient deckControlSetDeckStatus:error:].cold.1
+ -[CoreCECDeviceClient makeActiveSourceWithTVMenus:error:].cold.1
+ -[CoreCECDeviceClient performStandbyWithTargetDevice:error:].cold.1
+ -[CoreCECDeviceClient refreshDevices:].cold.1
+ -[CoreCECDeviceClient refreshProperties:ofDevice:error:].cold.1
+ -[CoreCECDeviceClient removeFromBus]
+ -[CoreCECDeviceClient removeFromBus].cold.1
+ -[CoreCECDeviceClient removeFromBus].cold.2
+ -[CoreCECDeviceClient requestActiveSource:].cold.1
+ -[CoreCECDeviceClient requestAudioReturnChannelStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceClient requestAudioReturnChannelStatusChangeTo:error:].cold.2
+ -[CoreCECDeviceClient requestAudioStatus:].cold.1
+ -[CoreCECDeviceClient requestSystemAudioModeStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceClient requestSystemAudioModeStatusChangeTo:error:].cold.2
+ -[CoreCECDeviceClient resignActiveSource:].cold.1
+ -[CoreCECDeviceClient setAudioMuteStatus:error:].cold.1
+ -[CoreCECDeviceClient setAudioMuteStatus:error:].cold.2
+ -[CoreCECDeviceClient setAudioReturnChannelControlEnabled:error:].cold.1
+ -[CoreCECDeviceClient setAudioReturnChannelControlEnabled:error:].cold.2
+ -[CoreCECDeviceClient setAudioVolumeStatus:error:].cold.1
+ -[CoreCECDeviceClient setAudioVolumeStatus:error:].cold.2
+ -[CoreCECDeviceClient setSupportedAudioFormats:count:error:].cold.1
+ -[CoreCECDeviceClient setSupportedAudioFormats:count:error:].cold.2
+ -[CoreCECDeviceClient setSystemAudioControlEnabled:error:].cold.1
+ -[CoreCECDeviceClient setTrackAudioStatusEnabled:pressTimeout:pollInterval:error:].cold.1
+ -[CoreCECDeviceClient systemAudioModeRequest:error:].cold.1
+ -[CoreCECDeviceProvider arcStarting].cold.1
+ -[CoreCECDeviceProvider arcStarting].cold.2
+ -[CoreCECDeviceProvider arcStarting_handleFeatureAbortReceivedWithOpcode:reason:].cold.1
+ -[CoreCECDeviceProvider arcStarting_handleFeatureAbortReceivedWithOpcode:reason:].cold.2
+ -[CoreCECDeviceProvider arcStarting_handleReportARCInitiatedReceived].cold.1
+ -[CoreCECDeviceProvider arcStopping].cold.1
+ -[CoreCECDeviceProvider arcStopping].cold.2
+ -[CoreCECDeviceProvider arcStopping_handleFeatureAbortReceivedWithOpcode:reason:].cold.1
+ -[CoreCECDeviceProvider arcStopping_handleFeatureAbortReceivedWithOpcode:reason:].cold.2
+ -[CoreCECDeviceProvider arcStopping_handleReportARCTerminatedReceived].cold.1
+ -[CoreCECDeviceProvider audioStatusChanged].cold.1
+ -[CoreCECDeviceProvider audioStatusChanged].cold.2
+ -[CoreCECDeviceProvider audioStatusHandleUserControlReleased].cold.1
+ -[CoreCECDeviceProvider audioStatusHandleUserControlReleased].cold.2
+ -[CoreCECDeviceProvider audioSystemRequestSystemAudioModeStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceProvider deckControlCommandWithMode:target:error:].cold.1
+ -[CoreCECDeviceProvider deckControlCommandWithMode:target:error:].cold.2
+ -[CoreCECDeviceProvider deckControlCommandWithMode:target:error:].cold.3
+ -[CoreCECDeviceProvider deckControlPlayWithMode:target:error:].cold.1
+ -[CoreCECDeviceProvider deckControlPlayWithMode:target:error:].cold.2
+ -[CoreCECDeviceProvider deckControlPlayWithMode:target:error:].cold.3
+ -[CoreCECDeviceProvider deckControlRefreshStatus:requestType:error:].cold.1
+ -[CoreCECDeviceProvider deckControlRefreshStatus:requestType:error:].cold.2
+ -[CoreCECDeviceProvider deckControlRefreshStatus:requestType:error:].cold.3
+ -[CoreCECDeviceProvider deckControlRefreshStatus:requestType:error:].cold.4
+ -[CoreCECDeviceProvider deckControlWithMode:to:error:].cold.1
+ -[CoreCECDeviceProvider deckStatusWithInfo:to:error:].cold.1
+ -[CoreCECDeviceProvider deviceRequestSystemAudioModeStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceProvider deviceRequestSystemAudioModeStatusChangeTo:error:].cold.2
+ -[CoreCECDeviceProvider didAddToBus:].cold.1
+ -[CoreCECDeviceProvider didChangePowerStatus:].cold.1
+ -[CoreCECDeviceProvider didNotHandleMessage:unsupportedOperand:].cold.1
+ -[CoreCECDeviceProvider dsamStarting:].cold.1
+ -[CoreCECDeviceProvider dsamStartingWithPhysicalAddress:].cold.1
+ -[CoreCECDeviceProvider dsamStartingWithPhysicalAddress:].cold.2
+ -[CoreCECDeviceProvider dsamStarting_handleBroadcastSSAMOnResponseReceived].cold.1
+ -[CoreCECDeviceProvider dsamStarting_handleBroadcastSSAMOnResponseReceived].cold.2
+ -[CoreCECDeviceProvider dsamStarting_handleBroadcastSSAMOnResponseTimeout].cold.1
+ -[CoreCECDeviceProvider dsamStarting_handleBroadcastSSAMOnResponseTimeout].cold.2
+ -[CoreCECDeviceProvider dsamStarting_handleBroadcastSSAMOnResponseTimeout].cold.3
+ -[CoreCECDeviceProvider dsamStopping].cold.1
+ -[CoreCECDeviceProvider dsamStopping].cold.2
+ -[CoreCECDeviceProvider dsamStopping_handleBroadcastSSAMOffResponseReceived].cold.1
+ -[CoreCECDeviceProvider dsamStopping_handleBroadcastSSAMOffResponseReceived].cold.2
+ -[CoreCECDeviceProvider dsamStopping_handleBroadcastSSAMOffResponseTimeout].cold.1
+ -[CoreCECDeviceProvider dsamStopping_handleBroadcastSSAMOffResponseTimeout].cold.2
+ -[CoreCECDeviceProvider dsamStopping_handleBroadcastSSAMOffResponseTimeout].cold.3
+ -[CoreCECDeviceProvider filterActiveSourceMessage:].cold.1
+ -[CoreCECDeviceProvider filterCECVersionMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterDeckStatusMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterDeviceVendorIDMessage:].cold.1
+ -[CoreCECDeviceProvider filterInactiveSourceMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterReportPhysicalAddressMessage:].cold.1
+ -[CoreCECDeviceProvider filterReportPowerStatusMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterRoutingChangeMessage:].cold.1
+ -[CoreCECDeviceProvider filterRoutingChangeMessage:].cold.2
+ -[CoreCECDeviceProvider filterRoutingChangeMessage:].cold.3
+ -[CoreCECDeviceProvider filterRoutingInformationMessage:].cold.1
+ -[CoreCECDeviceProvider filterSetOSDNameMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterSetStreamPathMessage:].cold.1
+ -[CoreCECDeviceProvider filterSetStreamPathMessage:].cold.2
+ -[CoreCECDeviceProvider filterSetStreamPathMessage:].cold.3
+ -[CoreCECDeviceProvider filterSetSystemAudioModeMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterSetSystemAudioModeMessage:toDevice:].cold.2
+ -[CoreCECDeviceProvider filterSystemAudioModeStatusMessage:toDevice:].cold.1
+ -[CoreCECDeviceProvider filterSystemAudioModeStatusMessage:toDevice:].cold.2
+ -[CoreCECDeviceProvider getRemoteControlDestination:logicalAddress:forTargetDevice:command:error:].cold.1
+ -[CoreCECDeviceProvider getRemoteControlDestination:logicalAddress:forTargetDevice:command:error:].cold.2
+ -[CoreCECDeviceProvider getRemoteControlDestination:logicalAddress:forTargetDevice:command:error:].cold.3
+ -[CoreCECDeviceProvider getRemoteControlDestination:logicalAddress:forTargetDevice:command:error:].cold.4
+ -[CoreCECDeviceProvider getRemoteControlDestination:logicalAddress:forTargetDevice:command:error:].cold.5
+ -[CoreCECDeviceProvider handleFeatureAbortMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleGiveDeckStatusMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleGiveDeckStatusMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handleMessage:fromDevice:broadcast:].cold.1
+ -[CoreCECDeviceProvider handleReportAudioStatusMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleReportAudioStatusMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handleReportAudioStatusMessage:fromDevice:].cold.3
+ -[CoreCECDeviceProvider handleReportAudioStatusMessage:fromDevice:].cold.4
+ -[CoreCECDeviceProvider handleRequestARCInitiationMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleRequestARCTerminationMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleRequestShortAudioDescriptorMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleRequestShortAudioDescriptorMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handleRequestShortAudioDescriptorMessage:fromDevice:].cold.3
+ -[CoreCECDeviceProvider handleRequestShortAudioDescriptorMessage:fromDevice:].cold.4
+ -[CoreCECDeviceProvider handleRequestShortAudioDescriptorMessage:fromDevice:].cold.5
+ -[CoreCECDeviceProvider handleSetAudioVolumeLevelMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleSetAudioVolumeLevelMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handleSetSystemAudioModeMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleSystemAudioModeRequestMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleSystemAudioModeRequestMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handleSystemAudioModeRequestMessage:fromDevice:].cold.3
+ -[CoreCECDeviceProvider handleUserControl:pressed:fromDevice:abortReason:].cold.1
+ -[CoreCECDeviceProvider handleUserControl:pressed:fromDevice:abortReason:].cold.2
+ -[CoreCECDeviceProvider handleUserControlPressedMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleUserControlReleasedMessage:fromDevice:].cold.1
+ -[CoreCECDeviceProvider handleUserControlReleasedMessage:fromDevice:].cold.2
+ -[CoreCECDeviceProvider handlingRequiredForSystemAudioModeMessage:].cold.1
+ -[CoreCECDeviceProvider hibernationChanged:].cold.1
+ -[CoreCECDeviceProvider initiateARC:error:].cold.1
+ -[CoreCECDeviceProvider initiatorAddressErrorDetectedForMessage:].cold.1
+ -[CoreCECDeviceProvider oneTouchPlayWithMenu:to:error:].cold.1
+ -[CoreCECDeviceProvider performStandbyWithTargetDevice:error:].cold.1
+ -[CoreCECDeviceProvider performStandbyWithTargetDevice:error:].cold.2
+ -[CoreCECDeviceProvider performStandbyWithTargetDevice:error:].cold.3
+ -[CoreCECDeviceProvider playWithMode:to:error:].cold.1
+ -[CoreCECDeviceProvider probeAbsoluteVolumeControl_handleFeatureAbortReceivedFromDevice:withOpcode:reason:].cold.1
+ -[CoreCECDeviceProvider refreshActiveSource].cold.1
+ -[CoreCECDeviceProvider refreshProperties:ofDevice:error:].cold.1
+ -[CoreCECDeviceProvider refreshProperties:ofDevice:error:].cold.2
+ -[CoreCECDeviceProvider refreshProperties:ofDevice:error:].cold.3
+ -[CoreCECDeviceProvider refreshSystemAudioModeStatus].cold.1
+ -[CoreCECDeviceProvider reportFeatures:].cold.1
+ -[CoreCECDeviceProvider reportFeatures:].cold.2
+ -[CoreCECDeviceProvider reportFeatures:].cold.3
+ -[CoreCECDeviceProvider reportFeatures:].cold.4
+ -[CoreCECDeviceProvider reportPhysicalAddress:].cold.1
+ -[CoreCECDeviceProvider reportShortAudioDescriptorTo:error:].cold.1
+ -[CoreCECDeviceProvider requestAudioReturnChannelStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceProvider requestAudioReturnChannelStatusChangeTo:error:].cold.2
+ -[CoreCECDeviceProvider requestAudioReturnChannelStatusChangeTo:error:].cold.3
+ -[CoreCECDeviceProvider requestAudioStatus:].cold.1
+ -[CoreCECDeviceProvider requestShortAudioDescriptor:error:].cold.1
+ -[CoreCECDeviceProvider requestSystemAudioModeStatusChangeTo:error:].cold.1
+ -[CoreCECDeviceProvider requestSystemAudioModeStatusChangeTo:error:].cold.2
+ -[CoreCECDeviceProvider requestSystemAudioModeStatusChangeTo:error:].cold.3
+ -[CoreCECDeviceProvider requestSystemAudioModeStatusChangeTo:error:].cold.4
+ -[CoreCECDeviceProvider samStarting_broadcast_Req_Act_Src].cold.1
+ -[CoreCECDeviceProvider samStarting_broadcast_Req_Act_Src].cold.2
+ -[CoreCECDeviceProvider samStarting_broadcast_SSAM_ON].cold.1
+ -[CoreCECDeviceProvider samStarting_broadcast_SSAM_ON].cold.2
+ -[CoreCECDeviceProvider samStarting_broadcast_SSAM_ON].cold.3
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceReceived].cold.1
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceReceived].cold.2
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceReceived].cold.3
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceResponseTimeout].cold.1
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceResponseTimeout].cold.2
+ -[CoreCECDeviceProvider samStarting_handleActiveSourceResponseTimeout].cold.3
+ -[CoreCECDeviceProvider samStarting_handleFeatureAbortReceived].cold.1
+ -[CoreCECDeviceProvider samStarting_handleFeatureAbortReceived].cold.2
+ -[CoreCECDeviceProvider samStarting_handleFeatureAbortResponseTimeout].cold.1
+ -[CoreCECDeviceProvider samStarting_handleFeatureAbortResponseTimeout].cold.2
+ -[CoreCECDeviceProvider samStarting_send_SSAM_ON_to_TV].cold.1
+ -[CoreCECDeviceProvider samStarting_send_SSAM_ON_to_TV].cold.2
+ -[CoreCECDeviceProvider samStopping].cold.1
+ -[CoreCECDeviceProvider samStopping].cold.2
+ -[CoreCECDeviceProvider samStopping].cold.3
+ -[CoreCECDeviceProvider sendMessage:withRetryCount:error:].cold.1
+ -[CoreCECDeviceProvider sendMessage:withRetryCount:error:].cold.2
+ -[CoreCECDeviceProvider sendMessage:withRetryCount:error:].cold.3
+ -[CoreCECDeviceProvider serialQueue].cold.1
+ -[CoreCECDeviceProvider setAudioReturnChannelControlEnabled:error:].cold.1
+ -[CoreCECDeviceProvider setSystemAudioControlEnabled:error:].cold.1
+ -[CoreCECDeviceProvider setSystemAudioMode:to:error:].cold.1
+ -[CoreCECDeviceProvider setTrackAudioStatusEnabled:pressTimeout:pollInterval:error:].cold.1
+ -[CoreCECDeviceProvider setTrackAudioStatusEnabled:pressTimeout:pollInterval:error:].cold.2
+ -[CoreCECDeviceProvider systemAudioModeRequest:error:].cold.1
+ -[CoreCECDeviceProvider systemAudioModeRequest:error:].cold.2
+ -[CoreCECDeviceProvider systemAudioModeRequest:error:].cold.3
+ -[CoreCECDeviceProvider systemAudioModeRequest:error:].cold.4
+ -[CoreCECDeviceProvider systemAudioModeStatus:error:].cold.1
+ -[CoreCECDeviceProvider terminateARC:error:].cold.1
+ -[CoreCECDeviceProvider userControlFollowerSafetyTimeoutExpired].cold.1
+ -[CoreCECDeviceProvider userControlFollowerSynthesizeRelease].cold.1
+ -[CoreCECDeviceProvider userControlInitiatorTrackAudioStatusTimeoutExpired].cold.1
+ -[CoreCECDeviceProvider userControlInitiatorTrackAudioStatusTimeoutExpired].cold.2
+ -[CoreCECDeviceProvider userControlScheduleInitiatorTrackAudioStatusTimeout].cold.1
+ -[CoreCECDeviceProvider userControlScheduleInitiatorTrackAudioStatusTimeout].cold.2
+ -[CoreCECDeviceProvider willRemoveFromBus:].cold.1
+ -[CoreIRBusClient deleteDevice:error:].cold.1
+ -[CoreIRBusClient deleteDevice:error:].cold.2
+ -[CoreIRBusProvider _findAppleRemoteWithUID:].cold.1
+ -[CoreIRBusProvider _recreatePairedDeviceFromDefaults:key:].cold.1
+ -[CoreIRBusProvider _recreatePairedDeviceFromDefaults:key:].cold.2
+ -[CoreIRBusProvider addDeviceWithType:matching:learningSession:error:].cold.1
+ -[CoreIRBusProvider addDeviceWithType:matching:learningSession:error:].cold.2
+ -[CoreIRBusProvider addDeviceWithType:matching:learningSession:error:].cold.3
+ -[CoreIRBusProvider copyPrefsPropertyForUUID:UUIDKey:key:].cold.1
+ -[CoreIRBusProvider copyPrefsPropertyForUUID:UUIDKey:key:].cold.2
+ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.1
+ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.2
+ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.3
+ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.4
+ -[CoreIRBusProvider deleteDevicePrefsWithUUID:UUIDKey:].cold.5
+ -[CoreIRBusProvider getExistingDeviceWithType:matching:].cold.1
+ -[CoreIRBusProvider mergePersistentMappingsFromSession:ofDevice:].cold.1
+ -[CoreIRBusProvider mergePersistentMappingsFromSession:ofDevice:].cold.2
+ -[CoreIRBusProvider saveDevicePrefsWithDict:error:].cold.1
+ -[CoreIRBusProvider saveDevicePrefsWithDict:error:].cold.2
+ -[CoreIRBusProvider saveDevicePrefsWithDict:error:].cold.3
+ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.1
+ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.2
+ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.3
+ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.4
+ -[CoreIRBusProvider setPrefsPropertyForUUID:UUIDKey:object:key:].cold.5
+ -[CoreIRBusProvider updateAllowHibernation].cold.1
+ -[CoreIRBusProvider updateLearnedProtocols].cold.1
+ -[CoreIRBusProvider updateLearnedProtocols].cold.2
+ -[CoreIRBusProvider updatePersistentValue:forProperty:ofDevice:].cold.1
+ -[CoreIRBusProvider updatePersistentValue:forProperty:ofDevice:].cold.2
+ -[CoreIRBusProvider willAddToManager:].cold.1
+ -[CoreIRDevice setOSDName:error:].cold.1
+ -[CoreIRDevice setOSDName:error:].cold.2
+ -[CoreIRDeviceClient changeButtonCombination:delay:enabled:error:].cold.1
+ -[CoreIRDeviceClient clearAllStoredCommands:].cold.1
+ -[CoreIRDeviceClient clearAllStoredCommands:].cold.2
+ -[CoreIRDeviceClient disableButtonCombination:delay:error:].cold.1
+ -[CoreIRDeviceClient enableButtonCombination:delay:error:].cold.1
+ -[CoreIRDeviceClient sendCommand:error:].cold.1
+ -[CoreIRDeviceClient sendCommand:error:].cold.2
+ -[CoreIRDeviceClient setCommand:target:forButtonCombination:delay:error:].cold.1
+ -[CoreIRDeviceClient setCommand:target:forButtonCombination:delay:error:].cold.2
+ -[CoreIRDeviceClient updateMappingWithSession:error:].cold.1
+ -[CoreIRDeviceClient updateMappingWithSession:error:].cold.2
+ -[CoreIRDeviceProvider dispatchButtonEventWithCommand:pressed:timestamp:toDevice:].cold.1
+ -[CoreIRDeviceProvider dispatchEventForCommand:matchingButton:timestamp:toDevice:].cold.1
+ -[CoreIRDeviceProvider dispatchEventForCommand:matchingButton:timestamp:toDevice:].cold.2
+ -[CoreIRDeviceProvider dispatchEventForCommand:matchingButton:timestamp:toDevice:].cold.3
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.1
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.2
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.3
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.4
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.5
+ -[CoreIRDeviceProvider dispatchEventsForCommand:toDevice:].cold.6
+ -[CoreIRDeviceProvider findDuplicateIRCommand:forCommand:device:].cold.1
+ -[CoreIRDeviceProvider infraredCommandForCommand:].cold.1
+ -[CoreIRDeviceProvider infraredCommandForCommand:].cold.2
+ -[CoreIRDeviceProvider infraredCommandForCommand:].cold.3
+ -[CoreIRDeviceProvider sendCommand:error:].cold.1
+ -[CoreIRDeviceProvider sendCommand:target:withDuration:error:].cold.1
+ -[CoreIRDeviceProvider sendCommand:target:withDuration:error:].cold.2
+ -[CoreIRDeviceProvider sendHIDEvent:target:error:].cold.1
+ -[CoreIRDeviceProvider sendHIDEvent:target:error:].cold.2
+ -[CoreIRDeviceProvider sendHIDEvent:target:error:].cold.3
+ -[CoreIRDeviceProvider setCommand:target:forButtonCombination:delay:error:].cold.1
+ -[CoreIRDeviceProvider setInfraredCommand:forCommand:error:].cold.1
+ -[CoreIRDeviceProvider setOSDName:error:].cold.1
+ -[CoreIRDeviceProvider setOSDName:error:].cold.2
+ -[CoreIRDeviceProvider startLearningSessionWithReason:error:].cold.1
+ -[CoreIRDeviceProvider synthesizeButtonReleaseWithTimestamp:].cold.1
+ -[CoreIRLearningSessionClient endLearning].cold.1
+ -[CoreIRLearningSessionClient endLearning].cold.2
+ -[CoreIRLearningSessionClient startLearningCommand:].cold.1
+ -[CoreIRLearningSessionClient startLearningCommand:].cold.2
+ -[CoreIRLearningSessionProvider captureIRCommand:].cold.1
+ -[CoreIRLearningSessionProvider handleDone].cold.1
+ -[CoreIRLearningSessionProvider handleIdle].cold.1
+ -[CoreIRLearningSessionProvider handleIdle].cold.2
+ -[CoreIRLearningSessionProvider handleNoSignal].cold.1
+ -[CoreIRLearningSessionProvider handleNoSignal].cold.2
+ -[CoreIRLearningSessionProvider handleNoSignal].cold.3
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.1
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.2
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.3
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.4
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.5
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.6
+ -[CoreIRLearningSessionProvider processCapturedPattern].cold.7
+ -[CoreIRLearningSessionProvider processIRCommand:].cold.1
+ -[CoreIRLearningSessionProvider processIRCommand:].cold.2
+ -[CoreIRLearningSessionProvider setCaptureState:].cold.1
+ -[CoreIRLearningSessionProvider updateProgress].cold.1
+ -[CoreIRLearningSessionProvider waitForIdle].cold.1
+ -[CoreRCBus notifyDelegateAllDevicesRemoved:].cold.1
+ -[CoreRCBus notifyDelegateDeviceAdded:].cold.1
+ -[CoreRCBus notifyDelegateDeviceRemoved:].cold.1
+ -[CoreRCBus notifyDelegateDeviceUpdated:].cold.1
+ -[CoreRCBus serialQueue].cold.1
+ -[CoreRCDevice receivedHIDEvent:fromDevice:].cold.1
+ -[CoreRCDevice receivedHIDEvent:fromDevice:].cold.2
+ -[CoreRCDevice removeAllOwningClients]
+ -[CoreRCDevice removeAllOwningClients].cold.1
+ -[CoreRCHIDEvent initWithCommand:pressed:timestamp:].cold.1
+ -[CoreRCHIDEvent(CEC) initWithCECDeckControlMode:pressed:].cold.1
+ -[CoreRCHIDEvent(CEC) initWithCECPlayMode:pressed:].cold.1
+ -[CoreRCHIDEvent(CEC) initWithCECUserControl:pressed:].cold.1
+ -[CoreRCInterface doesNotImplement:error:].cold.1
+ -[CoreRCInterface propertyForKey:error:].cold.1
+ -[CoreRCInterfaceListener scheduleWithDispatchQueue:].cold.1
+ -[CoreRCInterfaceListener unscheduleFromDispatchQueue:].cold.1
+ -[CoreRCManager addBus:].cold.1
+ -[CoreRCManagerClient busHasBeenAdded:].cold.1
+ -[CoreRCManagerClient busHasBeenRemoved:].cold.1
+ -[CoreRCManagerClient busHasBeenUpdated:].cold.1
+ -[CoreRCManagerClient connectionInterrupted].cold.1
+ -[CoreRCManagerClient mergeBus:].cold.1
+ -[CoreRCManagerClient sendCommand:fromDevice:toDevice:withDuration:error:].cold.1
+ -[CoreRCManagerClient sendHIDEvent:fromDevice:toDevice:error:].cold.1
+ -[CoreRCManagerClient setLogging:].cold.1
+ -[CoreRCManagerClient synchBuses:].cold.1
+ -[CoreRCManagerClient(CEC) performRemoveFromBus:reply:]
+ -[CoreRCManagerProvider addDeviceWithBus:transportProperties:error:].cold.1
+ -[CoreRCManagerProvider extendedPropertyForKey:ofDevice:error:].cold.1
+ -[CoreRCManagerProvider initOverrides].cold.1
+ -[CoreRCManagerProvider interfaceController:didAddInterface:].cold.1
+ -[CoreRCManagerProvider interfaceController:didRemoveInterface:].cold.1
+ -[CoreRCManagerProvider propertyForKey:ofBus:error:].cold.1
+ -[CoreRCManagerProvider setExtendedProperty:forKey:ofDevice:error:].cold.1
+ -[CoreRCManagerProvider setProperty:forKey:ofBus:error:].cold.1
+ -[CoreRCXPCService _getExtendedPropertyAsyncForKey:ofDevice:reply:].cold.1
+ -[CoreRCXPCService _getPropertyAsyncForKey:ofBus:reply:].cold.1
+ -[CoreRCXPCService _queryBusesAsync:].cold.1
+ -[CoreRCXPCService _sendCommandAsync:fromDevice:toDevice:withDuration:reply:].cold.1
+ -[CoreRCXPCService _sendHIDEventAsync:fromDevice:toDevice:reply:].cold.1
+ -[CoreRCXPCService _setExtendedPropertyAsync:forKey:ofDevice:reply:].cold.1
+ -[CoreRCXPCService _setPropertyAsync:forKey:ofBus:reply:].cold.1
+ -[CoreRCXPCService checkEntitlement:].cold.1
+ -[CoreRCXPCService connectionInvalidated:].cold.1
+ -[CoreRCXPCService enumerateClientsHavingEntitlement:usingBlock:].cold.1
+ -[CoreRCXPCService getExtendedPropertyAsyncForKey:ofDevice:reply:].cold.1
+ -[CoreRCXPCService getPropertyAsyncForKey:ofBus:reply:].cold.1
+ -[CoreRCXPCService listener:shouldAcceptNewConnection:].cold.1
+ -[CoreRCXPCService manager:hasAdded:].cold.1
+ -[CoreRCXPCService manager:hasRemoved:].cold.1
+ -[CoreRCXPCService manager:hasUpdated:].cold.1
+ -[CoreRCXPCService queryBusesAsync:].cold.1
+ -[CoreRCXPCService sendCommandAsync:fromDevice:toDevice:withDuration:reply:].cold.1
+ -[CoreRCXPCService sendHIDEventAsync:fromDevice:toDevice:reply:].cold.1
+ -[CoreRCXPCService setExtendedPropertyAsync:forKey:ofDevice:reply:].cold.1
+ -[CoreRCXPCService setPropertyAsync:forKey:ofBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performActiveSourceAsync:withMenus:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performDeckControlSetDeckStatusAsync:forDevice:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performDeckControlSetDeckStatusAsync:forDevice:allowRemoteDevice:reply:].cold.2
+ -[CoreRCXPCService(CEC) _performDeckControlSetDeckStatusAsync:forDevice:allowRemoteDevice:reply:].cold.3
+ -[CoreRCXPCService(CEC) _performDeckControlSetDeckStatusAsync:forDevice:allowRemoteDevice:reply:].cold.4
+ -[CoreRCXPCService(CEC) _performInactiveSourceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRefreshDevicesAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRefreshProperties:ofDevice:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRemoveDeviceWithTypeAsync:bus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRemoveDeviceWithTypeAsync:bus:reply:].cold.2
+ -[CoreRCXPCService(CEC) _performRemoveFromBus:reply:]
+ -[CoreRCXPCService(CEC) _performRemoveFromBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRemoveFromBus:reply:].cold.2
+ -[CoreRCXPCService(CEC) _performRequestActiveSourceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRequestAudioReturnChannelStatusChangeTo:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRequestAudioStatusAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performRequestSystemAudioModeStatusChangeTo:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetAudioMuteStatus:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetAudioReturnChannelControlEnabled:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetAudioVolumeStatus:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetPowerStatus:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetSupportedAudioFormats:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetSystemAudioControlEnabled:withDeviceAsync:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSetTrackAudioStatusEnabled:pressTimeout:pollInterval:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) _performSystemAudioModeRequestAsync:withDesiredState:allowRemoteDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) _setOsdNameAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _setOsdNameAsync:forBus:reply:].cold.2
+ -[CoreRCXPCService(CEC) _setTvLanguageCodeAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _setTvLanguageCodeAsync:forBus:reply:].cold.2
+ -[CoreRCXPCService(CEC) cecBus:activeSourceHasChangedTo:fromDevice:].cold.1
+ -[CoreRCXPCService(CEC) cecDevice:audioStatusReceived:muteStatus:].cold.1
+ -[CoreRCXPCService(CEC) cecDevice:requestAudioReturnChannelStatusChangeTo:didFinishWithResult:error:].cold.1
+ -[CoreRCXPCService(CEC) cecDevice:requestSystemAudioModeStatusChangeTo:didFinishWithResult:error:].cold.1
+ -[CoreRCXPCService(CEC) cecDeviceShouldAssertActiveSource:].cold.1
+ -[CoreRCXPCService(CEC) performActiveSourceAsync:withMenus:reply:].cold.1
+ -[CoreRCXPCService(CEC) performDeckControlCommandAsync:controlMode:targetDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) performDeckControlPlayAsync:playMode:targetDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) performDeckControlRefreshStatusAsync:targetDevice:requestType:reply:].cold.1
+ -[CoreRCXPCService(CEC) performDeckControlSetDeckStatusAsync:forDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) performInactiveSourceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRefreshDevicesAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRefreshProperties:ofDevice:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRemoveDeviceWithTypeAsync:bus:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRemoveFromBus:reply:]
+ -[CoreRCXPCService(CEC) performRemoveFromBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRequestActiveSourceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRequestAudioReturnChannelStatusChangeTo:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRequestAudioStatusAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performRequestSystemAudioModeStatusChangeTo:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetAudioMuteStatus:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetAudioReturnChannelControlEnabled:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetAudioVolumeStatus:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetPowerStatus:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetSupportedAudioFormats:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetSystemAudioControlEnabled:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSetTrackAudioStatusEnabled:pressTimeout:pollInterval:withDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CEC) performStandbyAsync:targetDevice:reply:].cold.1
+ -[CoreRCXPCService(CEC) performSystemAudioModeRequestAsync:withDesiredState:reply:].cold.1
+ -[CoreRCXPCService(CEC) queryLocalInstanceAsync:bus:reply:].cold.1
+ -[CoreRCXPCService(CEC) setOsdNameAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) setTvLanguageCodeAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeCreateCECBusAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeCreateCECBusAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) _fakeCreateRemoteCECDeviceAsync:bus:logicalAddress:physicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeCreateRemoteCECDeviceAsync:bus:logicalAddress:physicalAddress:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) _fakeCreateRemoteCECDeviceAsync:bus:logicalAddress:physicalAddress:reply:].cold.3
+ -[CoreRCXPCService(CECPrivate) _fakeRemoveCECBusAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeRemoveCECBusAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) _fakeRemoveCECDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeRemoveCECDeviceAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) _fakeRemoveCECDeviceAsync:reply:].cold.3
+ -[CoreRCXPCService(CECPrivate) _fakeSetCECBusLinkStateAsync:linkState:physicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeSetCECDeviceLogicalAddressAsync:logicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) _fakeSetCECDeviceLogicalAddressAsync:logicalAddress:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) _fakeSetCECDeviceLogicalAddressAsync:logicalAddress:reply:].cold.3
+ -[CoreRCXPCService(CECPrivate) fakeCreateCECBusAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeCreateCECBusAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) fakeCreateRemoteCECDeviceAsync:bus:logicalAddress:physicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeCreateRemoteCECDeviceAsync:bus:logicalAddress:physicalAddress:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) fakeRemoveCECBusAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeRemoveCECBusAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) fakeRemoveCECDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeRemoveCECDeviceAsync:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) fakeSetCECBusLinkStateAsync:linkState:physicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeSetCECBusLinkStateAsync:linkState:physicalAddress:reply:].cold.2
+ -[CoreRCXPCService(CECPrivate) fakeSetCECDeviceLogicalAddressAsync:logicalAddress:reply:].cold.1
+ -[CoreRCXPCService(CECPrivate) fakeSetCECDeviceLogicalAddressAsync:logicalAddress:reply:].cold.2
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:reply:].cold.1
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:reply:].cold.2
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:reply:].cold.3
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:reply:].cold.4
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:withSessionOwningDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:withSessionOwningDevice:reply:].cold.2
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:withSessionOwningDevice:reply:].cold.3
+ -[CoreRCXPCService(IR) _addDeviceOnBusAsync:withType:matching:withSessionOwningDevice:reply:].cold.4
+ -[CoreRCXPCService(IR) _changeButtonCombinationAsync:delay:enabled:forDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) _changeButtonCombinationAsync:delay:enabled:forDevice:reply:].cold.2
+ -[CoreRCXPCService(IR) _clearAllStoredCommandsFromDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(IR) _deleteDeviceAsync:fromBus:reply:].cold.1
+ -[CoreRCXPCService(IR) _deleteDeviceAsync:fromBus:reply:].cold.2
+ -[CoreRCXPCService(IR) _deleteDeviceAsync:fromBus:reply:].cold.3
+ -[CoreRCXPCService(IR) _deleteDeviceAsync:fromBus:reply:].cold.4
+ -[CoreRCXPCService(IR) _endLearningWithDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(IR) _endLearningWithDeviceAsync:reply:].cold.2
+ -[CoreRCXPCService(IR) _endLearningWithDeviceAsync:reply:].cold.3
+ -[CoreRCXPCService(IR) _sendCommandAsync:fromDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) _setCommandAsync:target:source:forButtonCombination:delay:reply:].cold.1
+ -[CoreRCXPCService(IR) _setCommandAsync:target:source:forButtonCombination:delay:reply:].cold.2
+ -[CoreRCXPCService(IR) _setCommandAsync:target:source:forButtonCombination:delay:reply:].cold.3
+ -[CoreRCXPCService(IR) _setOSDNameAsync:forDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) _setOSDNameAsync:forDevice:reply:].cold.2
+ -[CoreRCXPCService(IR) _setPairStateAsync:forAppleRemote:reply:].cold.1
+ -[CoreRCXPCService(IR) _setPairStateAsync:forAppleRemote:reply:].cold.2
+ -[CoreRCXPCService(IR) _setPairStateAsync:forAppleRemote:reply:].cold.3
+ -[CoreRCXPCService(IR) _startLearningCommandAsync:withDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) _startLearningCommandAsync:withDevice:reply:].cold.2
+ -[CoreRCXPCService(IR) _startLearningCommandAsync:withDevice:reply:].cold.3
+ -[CoreRCXPCService(IR) addDeviceOnBusAsync:withType:matching:reply:].cold.1
+ -[CoreRCXPCService(IR) addDeviceOnBusAsync:withType:matching:withSessionOwningDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) changeButtonCombinationAsync:delay:enabled:forDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) clearAllStoredCommandsFromDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(IR) deleteDeviceAsync:fromBus:reply:].cold.1
+ -[CoreRCXPCService(IR) endLearningWithDeviceAsync:reply:].cold.1
+ -[CoreRCXPCService(IR) learningSessionForDevice:commandProgress:].cold.1
+ -[CoreRCXPCService(IR) learningSessionForDevice:status:].cold.1
+ -[CoreRCXPCService(IR) learningSessionForDeviceCommandDone:].cold.1
+ -[CoreRCXPCService(IR) sendCommandAsync:fromDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) setCommandAsync:target:source:forButtonCombination:delay:reply:].cold.1
+ -[CoreRCXPCService(IR) setOSDNameAsync:forDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) setPairStateAsync:forAppleRemote:reply:].cold.1
+ -[CoreRCXPCService(IR) startLearningCommandAsync:withDevice:reply:].cold.1
+ -[CoreRCXPCService(IR) startLearningSessionWithDeviceAsync:forReason:reply:].cold.1
+ -[CoreRCXPCService(IR) updateMappingWithSessionOwningDeviceAsync:forTargetDevice:reply:].cold.1
+ -[CoreRCXPCService(Private) queryLoggingAsync:].cold.1
+ -[CoreRCXPCService(Private) queryLoggingAsync:].cold.2
+ -[CoreRCXPCService(Private) setLoggingAsync:reply:].cold.1
+ -[CoreRCXPCService(Private) setLoggingAsync:reply:].cold.2
+ -[IRInterface setLearnedProtocolMask:error:].cold.1
+ OBJC_IVAR_$_CECEDIDAttributes._address
+ OBJC_IVAR_$_CECEDIDAttributes._modelName
+ OBJC_IVAR_$_CECEDIDAttributes._productID
+ OBJC_IVAR_$_CECEDIDAttributes._uuid
+ OBJC_IVAR_$_CECEDIDAttributes._vendorID
+ OBJC_IVAR_$_CECEDIDAttributes._week
+ OBJC_IVAR_$_CECEDIDAttributes._year
+ OBJC_IVAR_$_CECFakeInterface._blockedMessages
+ OBJC_IVAR_$_CoreCECBus._edidAttributes
+ _IRDecoder_Initialize.cold.1
+ _IRDecoder_Initialize.cold.2
+ _OBJC_CLASS_$_CECEDIDAttributes
+ _OBJC_METACLASS_$_CECEDIDAttributes
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __28-[CoreRCManagerClient buses]_block_invoke_2.cold.1
+ __30-[CECInterface receivedFrame:]_block_invoke.cold.1
+ __38-[CoreIRBusClient deleteDevice:error:]_block_invoke_2.cold.1
+ __39-[CoreRCManagerClient busHasBeenAdded:]_block_invoke.cold.1
+ __41-[CoreRCManagerClient busHasBeenRemoved:]_block_invoke.cold.1
+ __41-[CoreRCManagerClient busHasBeenUpdated:]_block_invoke.cold.1
+ __42-[CoreRCXPCService connectionInvalidated:]_block_invoke.cold.1
+ __45-[CoreIRDeviceClient clearAllStoredCommands:]_block_invoke_2.cold.1
+ __49-[CoreIRDeviceProvider schedulePressAndHoldTimer]_block_invoke.cold.1
+ __50-[CoreCECBusClient addDeviceWithAttributes:error:]_block_invoke_2.cold.1
+ __51-[AppleIRDeviceProvider _schedulePressAndHoldTimer]_block_invoke.cold.1
+ __52-[CoreIRBusClient addDeviceWithType:matching:error:]_block_invoke_2.cold.1
+ __52-[CoreIRDeviceProvider setMappingWithSession:error:]_block_invoke.cold.1
+ __52-[CoreIRLearningSessionClient startLearningCommand:]_block_invoke_2.cold.1
+ __53-[CoreIRDeviceClient updateMappingWithSession:error:]_block_invoke_2.cold.1
+ __59-[CoreIRDeviceClient startLearningSessionWithReason:error:]_block_invoke_2.cold.1
+ __66-[CoreIRDeviceClient changeButtonCombination:delay:enabled:error:]_block_invoke_2.cold.1
+ __68-[CoreIRBusClient addDeviceWithType:matching:learningSession:error:]_block_invoke_2.cold.1
+ __73-[CoreIRDeviceClient setCommand:target:forButtonCombination:delay:error:]_block_invoke_2.cold.1
+ __76-[CoreCECDeviceProvider userControlScheduleInitiatorTrackAudioStatusTimeout]_block_invoke.cold.1
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_CECEDIDAttributes
+ __OBJC_$_CLASS_PROP_LIST_CECEDIDAttributes
+ __OBJC_$_INSTANCE_METHODS_CECEDIDAttributes
+ __OBJC_$_INSTANCE_VARIABLES_CECEDIDAttributes
+ __OBJC_$_PROP_LIST_CECEDIDAttributes
+ __OBJC_CLASS_PROTOCOLS_$_CECEDIDAttributes
+ __OBJC_CLASS_RO_$_CECEDIDAttributes
+ __OBJC_METACLASS_RO_$_CECEDIDAttributes
+ ___36-[CoreCECDeviceClient removeFromBus]_block_invoke
+ ___52-[CoreRCXPCService(CEC) performRemoveFromBus:reply:]_block_invoke
+ ___block_descriptor_50_e8_32o40b_e5_v8?0l
+ ___block_descriptor_59_e8_32o40o48b_e5_v8?0l
+ ___block_descriptor_67_e8_32o40o48o56b_e5_v8?0l
+ _kCECInterfacePropertyEDIDAttributes
+ _objc_msgSend$_performRemoveFromBus:reply:
+ _objc_msgSend$address
+ _objc_msgSend$edidAttributes
+ _objc_msgSend$initWithAttributes:
+ _objc_msgSend$modelName
+ _objc_msgSend$performRemoveFromBus:reply:
+ _objc_msgSend$productID
+ _objc_msgSend$removeAllOwningClients
+ _objc_msgSend$removeFromBus
+ _objc_msgSend$setEdidAttributes:
+ _objc_msgSend$setModelName:
+ _objc_msgSend$uuid
+ _objc_msgSend$week
+ _objc_msgSend$year
- -[NSUserDefaults(CEC) analyticsDelay]
- _CoreCECPhysicalAddressForPackedPhysicalAddress
- _CoreCECPhysicalAddressIsOnStreamPath
- _CoreCECPhysicalAddressIsValid
- _CoreCECPhysicalAddressString
- _PackedPhysicalAddressForCoreCECPhysicalAddress
- ___block_descriptor_56_e8_32o40b_e5_v8?0l
- _gDecoderContext
- _gDecoderInitOnce
- _kCECInterfacePropertyEDID
CStrings:
+ " %@"
+ " EDID: %@"
+ " PA: %s;"
+ " Route: %s;"
+ " pID: 0x%04lX;"
+ " vID: 0x%04lX;"
+ " year: %ld;"
+ "%@ %s ("
+ "%@ performRemoveFromBus:reply: called\n"
+ "-[CoreCECDevice removeFromBus]"
+ "-[CoreCECDeviceClient removeFromBus]"
+ "-[CoreRCDevice addOwningClient:]"
+ "-[CoreRCDevice removeAllOwningClients]"
+ "-[CoreRCDevice removeOwningClient:]"
+ "-[CoreRCXPCService connectionInvalidated:]_block_invoke"
+ "-[CoreRCXPCService(CEC) _performRemoveFromBus:reply:]"
+ "@\"CECEDIDAttributes\""
+ "@20@0:8S16"
+ "@24@0:8B16S20"
+ "@24@0:8q16"
+ "@44@0:8@16B24C28S32@36"
+ "@44@0:8@16B24C28S32Q36"
+ "@48@0:8C16S20@24@32Q40"
+ "@56@0:8@16C24S28@32@40Q48"
+ "Another device is already active source: %@, streamPath: %s\n"
+ "B24@0:8^S16"
+ "B32@0:8S16S20^@24"
+ "B32@0:8^B16^S24"
+ "B32@0:8^S16^Q24"
+ "B32@0:8^S16^S24"
+ "B36@0:8^@16^@24S32"
+ "B40@0:8^@16^@24S32C36"
+ "CECEDIDAttributes"
+ "Converting deprecated physical address: %lx"
+ "CoreCECBus removeDeviceWithType async operation failed %d\n"
+ "CoreCECDevice removeFromBus async operation failed %@\n"
+ "Ignored suspicious routing change %@, currentStreamPath=%s\n"
+ "Last known physical address: %s"
+ "No more owning clients, removing %@"
+ "Set stream path happened before adding the device, take active source now: %s"
+ "Storing physical address: %s"
+ "T@\"CECEDIDAttributes\",C,N,V_edidAttributes"
+ "T@\"NSMutableArray\",&,N,V_mappings"
+ "T@\"NSString\",C,N,V_modelName"
+ "T@\"NSString\",C,N,V_uuid"
+ "TS,N,V_address"
+ "TS,N,V_physicalAddress"
+ "TS,N,V_streamPath"
+ "TS,R,N,V_lastStreamPath"
+ "TS,R,N,V_physicalAddress"
+ "Tq,N,V_productID"
+ "Tq,N,V_vendorID"
+ "Tq,N,V_week"
+ "Tq,N,V_year"
+ "_address"
+ "_blockedMessages"
+ "_edidAttributes"
+ "_modelName"
+ "_performRemoveFromBus:reply:"
+ "_productID"
+ "_uuid"
+ "_week"
+ "_year"
+ "add owning client: %@  self:%@ %@"
+ "address"
+ "edidAttributes"
+ "initWithAttributes:"
+ "initWithInterface with physical address: %s"
+ "initWithModelName:"
+ "initWithVendorID:"
+ "kCECInterfacePropertyEDIDAttributes"
+ "modelName"
+ "performRemoveFromBus:reply:"
+ "previousCECPhysicalAddress"
+ "productID"
+ "remove all owning clients: %@  self:%@"
+ "remove owning client: %@  self:%@ %@"
+ "removeAllOwningClients"
+ "removeFromBus"
+ "removeFromBus %@"
+ "setAddress:"
+ "setBlockedMessages:"
+ "setEdidAttributes:"
+ "setModelName:"
+ "setProductID:"
+ "setUuid:"
+ "setWeek:"
+ "setYear:"
+ "uuid"
+ "v24@0:8B16S20"
+ "v28@0:8S16@?20"
+ "v28@0:8S16@?<v@?@\"CoreCECBus\"@\"NSError\">20"
+ "v40@0:8@\"CoreCECBus\"16B24S28@?<v@?@\"NSError\">32"
+ "v40@0:8@16B24S28@?32"
+ "v48@0:8@\"CoreCECDeviceBasicAttributes\"16@\"CoreCECBus\"24C32S36@?<v@?@\"CoreCECDevice\"@\"NSError\">40"
+ "v48@0:8@16@24C32S36@?40"
+ "week"
+ "year"
- " PA: %@;"
- " Route: %@;"
- "%@ %@ ("
- "-[NSDictionary(CoreCECInterfaceProperties) getLinkState:physicalAddress:]"
- "<invalid address: %08x>"
- "@28@0:8B16Q20"
- "@48@0:8@16B24C28Q32@40"
- "@48@0:8@16B24C28Q32Q40"
- "@52@0:8C16Q20@28@36Q44"
- "@60@0:8@16C24Q28@36@44Q52"
- "Another device is already active source: %@, streamPath: %@\n"
- "B32@0:8^B16^Q24"
- "B32@0:8^Q16^Q24"
- "B40@0:8Q16Q24^@32"
- "B40@0:8^@16^@24Q32"
- "B44@0:8^@16^@24Q32C40"
- "CoreCECBus removeDeviceWithType async operation failed\n"
- "Ignored suspicious routing change %@, currentStreamPath=%@\n"
- "Invalid Physical Address: %@\n"
- "Last known physical address: %@"
- "Set stream path happened before adding the device, take active source now: %@"
- "Storing physical address: %@"
- "T@\"NSMutableArray\",C,N,V_mappings"
- "TQ,N,V_physicalAddress"
- "TQ,N,V_streamPath"
- "TQ,R,N,V_lastStreamPath"
- "TQ,R,N,V_physicalAddress"
- "analyticsDelay"
- "initWithInterface with physical address: %@"
- "kCECInterfacePropertyEDID"
- "v28@0:8B16Q20"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"CoreCECBus\"@\"NSError\">24"
- "v44@0:8@\"CoreCECBus\"16B24Q28@?<v@?@\"NSError\">36"
- "v44@0:8@16B24Q28@?36"
- "v52@0:8@\"CoreCECDeviceBasicAttributes\"16@\"CoreCECBus\"24C32Q36@?<v@?@\"CoreCECDevice\"@\"NSError\">44"
- "v52@0:8@16@24C32Q36@?44"

```
