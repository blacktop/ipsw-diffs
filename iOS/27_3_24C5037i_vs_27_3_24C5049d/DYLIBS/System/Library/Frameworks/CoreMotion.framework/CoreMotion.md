## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3188.0.7.0.1
-  __TEXT.__text: 0x3cdc34
-  __TEXT.__objc_methlist: 0xdc9c
-  __TEXT.__const: 0xcfa0
+3188.0.11.0.0
+  __TEXT.__text: 0x3ce638
+  __TEXT.__objc_methlist: 0xdd2c
+  __TEXT.__const: 0xcf70
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x30510
-  __TEXT.__cstring: 0x48621
+  __TEXT.__oslogstring: 0x3082a
+  __TEXT.__cstring: 0x48719
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
   __TEXT.__gcc_except_tab: 0xd8ec
-  __TEXT.__unwind_info: 0xd380
+  __TEXT.__unwind_info: 0xd3a0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3e18
+  __DATA_CONST.__const: 0x3e50
   __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5808
+  __DATA_CONST.__objc_selrefs: 0x5870
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x7e8
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x840
-  __AUTH_CONST.__const: 0x15bb0
-  __AUTH_CONST.__cfstring: 0x13e40
-  __AUTH_CONST.__objc_const: 0x1e360
+  __AUTH_CONST.__const: 0x15bd0
+  __AUTH_CONST.__cfstring: 0x13f40
+  __AUTH_CONST.__objc_const: 0x1e440
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x14c0
+  __AUTH_CONST.__auth_got: 0x14c8
   __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x220
   __DATA.__objc_ivar: 0x17e8
   __DATA.__data: 0xe20
   __DATA.__common: 0x138
-  __DATA_DIRTY.__objc_ivar: 0x1d0
+  __DATA_DIRTY.__objc_ivar: 0x1e8
   __DATA_DIRTY.__objc_data: 0x55a0
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x89

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12847
-  Symbols:   1822
-  CStrings:  11533
+  Functions: 12861
+  Symbols:   1830
+  CStrings:  11545
 
Symbols:
+ _CFPreferencesCopyAppValue
+ _CMMagicPoseEventDeviceOrientationKey
+ _CMMagicPoseEventHingeStateKey
+ _CMMagicPoseEventInnerDisplayOrientationKey
+ _CMMagicPoseEventOuterDisplayOrientationKey
+ _CMMagicPoseEventSendNotification
+ _CMMagicPoseEventStableOrientationStateKey
+ _CMMagicPoseEventTabletopPoseKey
CStrings:
+ "%@ deviceOrientation:%@ outerDisplayOrientation:%@ innerDisplayOrientation:%@ hingeState:%@ tabletopPose:%@ stableOrientationState:%@ timestamp: %f timestampContinuous: %f"
+ "%{public}f: Device Stationary?, %{public}s, Orientation, %{public}s, Proximity, %{public}s, AllowInPocket, %{public}s, State, %{public}s"
+ "%{public}f: monitorTime, %{public}f, bksMonitorTime, %{public}f, bksDelay, %{public}f, proxStatus, %{public}s"
+ "%{public}f: query response external=%{public}u (%{public}s), cbcount=%{public}lu"
+ "+[CMDeviceStateManager sharedManager]_block_invoke"
+ "+[CMMagicPoseEvent deviceOrientationForConfigType:deviceOrientation:hingeState:tabletopPose:]"
+ "+[CMMagicPoseManager computeMagicPoseEventForDeviceOrientation:outerDisplayOrientation:innerDisplayOrientation:angle:tabletopPose:timestamp:continuousTimestamp:]"
+ "+[CMWakeGestureManager toTabletopPose:]"
+ "-[CMDeviceStateManager dispatchDeviceStateEvent:error:onQueue:toHandler:]"
+ "-[CMDeviceStateManager onNotification:]"
+ "-[CMDeviceStateManager startUpdatesToQueue:withHandler:]"
+ "-[CMMagicPoseManager onMagicPoseStateData:]"
+ "-[CMMagicPoseManager onNotification:]_block_invoke"
+ "-[CMMagicPoseManager simulateMagicPoseEventWithOrientation:outerDisplayOrientation:innerDisplayOrientation:hingeState:tabletopPose:stableOrientationState:delaySecs:]"
+ "-[CMMagicPoseManager startUpdatesPrivateToQueue:withHandler:]"
+ "-[CMMagicPoseManager startUpdatesToQueue:withHandler:]_block_invoke"
+ "-[CMMagicPoseManager stopUpdatesPrivate]"
+ "-[CMMagicPoseManagerInternal feedMagicPoseEvent:outerDisplayOrientationType:innerDisplayOrientationType:hingeStateType:tabletopPoseType:stableOrientationStateType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]"
+ "-[CMMagicPoseManagerInternal sendMagicPoseEventToClientPrivate]"
+ "-[CMSuppressionManager feedMagicPoseEvent:facedown:timestamp:force:]_block_invoke"
+ "-[CMSuppressionManager handleMagicPoseEvent:]"
+ "-[CMSuppressionManager handleMagicPoseEvent:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Shared/Motion/MagicPose/CLSPUMagicPoseInterface.mm"
+ "CLMagicPoseNotifier"
+ "CLMagicPoseNotifier::CLMagicPoseNotifier()"
+ "CLMagicPoseNotifier::fLastEventFromVirtualDevice defaulted to: %s"
+ "CLMagicPoseNotifier::onIoHidEventPhysical fLastEventFromVirtualDevice set to false."
+ "CLMagicPoseNotifier::onIoHidEventVirtual fLastEventFromVirtualDevice set to true."
+ "CMMagicPoseEventDeviceOrientationKey"
+ "CMMagicPoseEventHingeStateKey"
+ "CMMagicPoseEventInnerDisplayOrientationKey"
+ "CMMagicPoseEventOuterDisplayOrientationKey"
+ "CMMagicPoseEventSendNotification"
+ "CMMagicPoseEventStableOrientationStateKey"
+ "CMMagicPoseEventTabletopPoseKey"
+ "CMMagicPoseManager error: %{public}@"
+ "CMMagicPoseReport::visit() type %{public}d failed."
+ "Device Stationary?, %{public}s, Orientation, %{public}s, Proximity, %{public}s, AllowInPocket, %{public}s"
+ "DeviceOrientation Ambiguous for HingeState Ambiguous, OpenAmbiguous & OpenTransitioning."
+ "DeviceOrientation=%{public}ld OuterDisplayOrientation=%{public}ld InnerDisplayOrientation=%{public}ld HingeState=%{public}ld TabletopPose=%{public}ld TimestampDeltaArrivalToNotified=%{public}f"
+ "Dropping event after teardown in onMagicPoseStateData:."
+ "Event created successfully. DeviceOrientation: %{public}@ OuterDisplayOrientation: %{public}@ InnerDisplayOrientation: %{public}@ HingeState: %{public}@ TabletopPose: %{public}@ timestamp: %{public}f, continuousTimestamp: %{public}f"
+ "Incoming magic mount state, mountStatus,%{public}u, tabletopPose,%{public}u, isAPAwake,%{public}u, isSimulated,%{public}u, timestampSecs,%{public}f"
+ "Incoming magic pose event, DeviceOrientation,%{public}@,HingeState,%{public}@,TabletopPose,%{public}@"
+ "Invalid DeviceOrientation input."
+ "Invalid deviceOrientationType, hingeStateType, tabletopPoseType combination."
+ "Invalid simulated hingeState value"
+ "Invalid simulated innerDisplayOrientation value"
+ "Invalid simulated orientation value"
+ "Invalid simulated outerDisplayOrientation value"
+ "Invalid simulated stableOrientationState value"
+ "Invalid simulated tabletopPose value"
+ "MagicPoseState CLMagicPoseNotifier::currentMagicPoseState()"
+ "Not available for continuity camera configuration, tabletopPose,%{public}u"
+ "Orientation=%{public}u OuterDisplayOrientation=%{public}u InnerDisplayOrientation=%{public}u HingeState=%{public}u TabletopPose=%{public}u StableOrientationState=%{public}u TimestampDeltaDetectedToArrival=%{public}f"
+ "Proximity detection mask: %{public}u, Tested bit: %{public}u, Last prox state: %{public}s"
+ "QueryRequest,%{public}f"
+ "Report,Type,%{public}u,Orientation,%{public}u,OuterDisplayOrientation,%{public}u,InnerDisplayOrientation,%{public}u,HingeState,%{public}u,TabletopPose,%{public}u,StableOrientationState,%{public}u,isSimulated,%{public}d,timestamp,%{public}lf,timestampContinuous,%{public}lf,now,%{public}lf"
+ "Report,mountStatus,%{public}u,tabletopPose,%{public}u,APAwake,%{public}u,isSimulated,%{public}u,timestamp,%{public}lf,now,%{public}lf"
+ "Sending DeviceState event to client: %{public}@,now,%{public}f"
+ "TempestMGFrontCameraOffsetOverride"
+ "Transition, From: %{public}s, To: %{public}s, %{public}s"
+ "[%{public}@] Incoming MagicPose Notification DeviceOrientation: %{public}ld  OuterDisplayOrientation: %{public}ld InnerDisplayOrientation: %{public}ld HingeState: %{public}f TabletopPose: %{public}d StableOrientationState: %{public}ld"
+ "[%{public}@] Incoming magicPose event, deviceOrientationType,%{public}u, outerDisplayOrientationType,%{public}u, innerDisplayOrientationType,%{public}u, hingeStateType,%{public}u, tabletopPoseType,%{public}u, stableOrientationStateType,%{public}u, isSimulated,%{public}u, timestampAbsoluteSecs,%{public}f, timestampContinuousSecs,%{public}f"
+ "[%{public}@] Invalid deviceOrientation value!"
+ "[%{public}@] Invalid hingeState value!"
+ "[%{public}@] Invalid innerDisplayOrientation value!"
+ "[%{public}@] Invalid outerDisplayOrientation value!"
+ "[%{public}@] Invalid stableOrientationState value!"
+ "[%{public}@] Sending MagicPose event to client: %{public}@,now,%{public}f"
+ "[%{public}@] Starting MagicPose updates without progress."
+ "[%{public}@] Stopping MagicPose updates"
+ "[%{public}ld] Incoming magic pose event, DeviceOrientation,%{public}@,HingeState,%{public}@,TabletopPose,%{public}@"
+ "[%{public}ld][%{public}@][%{public}ld] -> Feeding magic pose event: %{public}@ @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] -> Not feeding magic pose event: %{public}@ @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] Stopping suppression updates. Final states: MP: %{public}@ @ %{public}f, SPN: %{public}@ @ %{public}f, DP: %{public}@ @ %{public}f"
+ "[CLMagicPoseNotifier] Skipping open for physical HID device on VM/Simulator"
+ "[CLMagicPoseNotifier] copied event isn't DeviceState report,type,%{public}d,size,%{public}lu"
+ "[CLMagicPoseNotifier] copyEvent returned invalid event ref"
+ "[CLMagicPoseNotifier] currentMagicPoseState failed, openHidDevice failed"
+ "[CLMagicPoseNotifier] currentMagicPoseState: no HID device available"
+ "[CLSPUMagicPoseInterface] Service required"
+ "[CLSPUMagicPoseInterface] Simulate failed"
+ "[CLSPUMagicPoseInterface] Simulate,orientation,%{public}u,outerDisplayOrientation,%{public}u,innerDisplayOrientation,%{public}u,hingeState,%{public}u,tabletopPose,%{public}u,stableOrientationState,%{public}u,%{public}f"
+ "[CLSPUMagicPoseInterface] sendCommand skipped, no physical HID driver (VM/Simulator)"
+ "[CMMagicPoseEvent isValidDeviceOrientation:innerDisplayOrientation]"
+ "[CMMagicPoseEvent isValidDeviceOrientation:orientation]"
+ "[CMMagicPoseEvent isValidDeviceOrientation:outerDisplayOrientation]"
+ "[CMMagicPoseEvent isValidHingeState:hingeState]"
+ "[CMMagicPoseEvent isValidStableOrientationState:stableOrientationState]"
+ "[CMMagicPoseEvent isValidTabletopPose:tabletopPose]"
+ "bool CLSPUMagicPoseInterface::sendCommand(const void *, size_t)"
+ "static void CLMagicPoseNotifier::onIoHidEventPhysical(void *, void *, void *, IOHIDEventRef)"
+ "static void CLMagicPoseNotifier::onIoHidEventVirtual(void *, void *, void *, IOHIDEventRef)"
+ "v24@?0@\"CMMagicPoseEvent\"8@\"NSError\"16"
+ "virtual bool CLMagicPoseNotifier::openHidDevice()"
+ "virtual void CLMagicPoseNotifier::numberOfSpectatorsChanged(int, size_t)"
+ "virtual void CLMagicPoseNotifier::visitMagicPose(const CMMagicPoseReport::MagicPose *)"
+ "virtual void CLSPUMagicPoseInterface::visitPong(const CMMagicPoseReport::Pong *)"
+ "void CLSPUMagicPoseInterface::onIoHidEvent(IOHIDEventRef)"
+ "void CLSPUMagicPoseInterface::simulateMagicPoseEvent(uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, CFTimeInterval)_block_invoke"
+ "void CLSPUMagicPoseInterface::visitIoHidEvent(const uint8_t *, size_t, const CFTimeInterval, const CFTimeInterval)"
+ "{\"msg%{public}.0s\":\"Invalid simulated hingeState value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated innerDisplayOrientation value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated orientation value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated outerDisplayOrientation value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated stableOrientationState value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated tabletopPose value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"[CLSPUMagicPoseInterface] Service required\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "%@ deviceOrientation:%@ deviceOrientation0:%@ deviceOrientation1:%@ hingeState:%@ tabletopPose:%@ stableOrientationState:%@ timestamp: %f timestampContinuous: %f"
- "%f: Device Stationary?, %s, Orientation, %s, Proximity, %s, AllowInPocket, %s, State, %s"
- "%f: monitorTime, %f, bksMonitorTime, %f, bksDelay, %f, proxStatus, %s"
- "%f: query response external=%u (%s), cbcount=%lu"
- "+[CMDeviceStateManager computeDeviceStateEventForPropertyA:propertyA0:propertyA1:angle:propertyC:timestamp:continuousTimestamp:]"
- "+[CMMagicPoseManager sharedManager]_block_invoke"
- "+[CMWakeGestureManager toPropertyC:]"
- "-[CMDeviceStateManager onDeviceStateData:]"
- "-[CMDeviceStateManager onNotification:]_block_invoke"
- "-[CMDeviceStateManager startUpdatesPrivateToQueue:withHandler:]"
- "-[CMDeviceStateManager startUpdatesToQueue:withHandler:]_block_invoke"
- "-[CMDeviceStateManager stopUpdatesPrivate]"
- "-[CMDeviceStateManagerInternal feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]"
- "-[CMDeviceStateManagerInternal sendEventToClientPrivate]"
- "-[CMMagicPoseManager createMagicPoseEventFromDeviceStateEvent:]"
- "-[CMMagicPoseManager dispatchMagicPoseEvent:error:onQueue:toHandler:]"
- "-[CMMagicPoseManager startUpdatesToQueue:withHandler:]"
- "-[CMSuppressionManager feedDeviceStateEvent:facedown:timestamp:force:]_block_invoke"
- "-[CMSuppressionManager handleDeviceStateEvent:]"
- "-[CMSuppressionManager handleDeviceStateEvent:]_block_invoke"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Shared/Motion/DeviceState/CLSPUDeviceStateInterface.mm"
- "CLDeviceStateNotifier"
- "CLDeviceStateNotifier::CLDeviceStateNotifier()"
- "CLDeviceStateNotifier::fLastEventFromVirtualDevice defaulted to: %s"
- "CLDeviceStateNotifier::onIoHidEventPhysical fLastEventFromVirtualDevice set to false."
- "CLDeviceStateNotifier::onIoHidEventVirtual fLastEventFromVirtualDevice set to true."
- "CMDeviceStateManager error: %{public}@"
- "CMDeviceStateReport::visit() type %{public}d failed."
- "Device Stationary?, %s, Orientation, %s, Proximity, %s, AllowInPocket, %s"
- "DeviceState CLDeviceStateNotifier::currentDeviceState()"
- "Dropping event after teardown in onDeviceStateData:."
- "Event created successfully. PropertyA: %{public}@ PropertyA0: %{public}@ PropertyA1: %{public}@ PropertyB: %{public}@ PropertyC: %{public}@ timestamp: %{public}f, continuousTimestamp: %{public}f"
- "Incoming device state event, PropertyA,%{public}@,PropertyB,%{public}@,PropertyC,%{public}@"
- "Incoming magic mount state, mountStatus,%{public}u, propertyC,%{public}u, isAPAwake,%{public}u, isSimulated,%{public}u, timestampSecs,%{public}f"
- "Invalid device orientation value"
- "Invalid device orientation0 value"
- "Invalid device orientation1 value"
- "Invalid deviceStatePropertyAType, propertyBType, propertyCType combination."
- "Invalid hinge state value"
- "Invalid stable orientation state value"
- "Invalid tabletop pose value"
- "Not available for continuity camera configuration, propertyC,%{public}u"
- "PropertyA=%{public}ld PropertyA0=%{public}ld PropertyA1=%{public}ld PropertyB=%{public}ld PropertyC=%{public}ld TimestampDeltaArrivalToNotified=%{public}f"
- "PropertyA=%{public}u PropertyA0=%{public}u PropertyA1=%{public}u PropertyB=%{public}u PropertyC=%{public}u PropertyD=%{public}u TimestampDeltaDetectedToArrival=%{public}f"
- "Proximity detection mask: %u, Last prox state: %s"
- "QueryRequest,%f"
- "Report,Type,%{public}u,PropertyAType,%{public}u,PropertyA0Type,%{public}u,PropertyA1Type,%{public}u,PropertyBType,%{public}u,PropertyCType,%{public}u,PropertyDType,%{public}u,isSimulated,%{public}d,timestamp,%{public}lf,timestampContinuous,%{public}lf,now,%{public}lf"
- "Report,mountStatus,%{public}u,propertyC,%{public}u,APAwake,%{public}u,isSimulated,%{public}u,timestamp,%{public}lf,now,%{public}lf"
- "Sending MagicPose event to client: %{public}@,now,%{public}f"
- "Transition, From: %s, To: %s, %s"
- "[%{public}@] Incoming DeviceState Notification PropertyA: %{public}ld  PropertyA0: %{public}ld PropertyA1: %{public}ld PropertyB: %{public}f PropertyC: %{public}d PropertyD: %{public}ld"
- "[%{public}@] Incoming deviceState event, propertyAType,%{public}u, propertyA0Type,%{public}u, propertyA1Type,%{public}u, propertyBType,%{public}u, propertyCType,%{public}u, propertyDType,%{public}u, isSimulated,%{public}u, timestampAbsoluteSecs,%{public}f, timestampContinuousSecs,%{public}f"
- "[%{public}@] Invalid propertyA value!"
- "[%{public}@] Invalid propertyA0 value!"
- "[%{public}@] Invalid propertyA1 value!"
- "[%{public}@] Invalid propertyB value!"
- "[%{public}@] Invalid propertyD value!"
- "[%{public}@] Sending DeviceState event to client: %{public}@,now,%{public}f"
- "[%{public}@] Starting DeviceState updates without progress."
- "[%{public}@] Stopping DeviceState updates"
- "[%{public}ld] Incoming device state event, PropertyA,%{public}@,PropertyB,%{public}@,PropertyC,%{public}@"
- "[%{public}ld][%{public}@][%{public}ld] -> Feeding device state event: %{public}@ @ %{public}f"
- "[%{public}ld][%{public}@][%{public}ld] -> Not feeding device state event: %{public}@ @ %{public}f"
- "[%{public}ld][%{public}@][%{public}ld] Stopping suppression updates. Final states: DS: %{public}@ @ %{public}f, SPN: %{public}@ @ %{public}f, DP: %{public}@ @ %{public}f"
- "[CLDeviceStateNotifier] Skipping open for physical HID device on VM/Simulator"
- "[CLDeviceStateNotifier] copied event isn't DeviceState report,type,%{public}d,size,%{public}lu"
- "[CLDeviceStateNotifier] copyEvent returned invalid event ref"
- "[CLDeviceStateNotifier] currentDeviceState failed, openHidDevice failed"
- "[CLDeviceStateNotifier] currentDeviceState: no HID device available"
- "[CLSPUDeviceStateInterface] Service required"
- "[CLSPUDeviceStateInterface] Simulate failed"
- "[CLSPUDeviceStateInterface] Simulate,propertyA,%{public}u,propertyA0,%{public}u,propertyA1,%{public}u,propertyB,%{public}u,propertyC,%{public}u,propertyD,%{public}u,%{public}f"
- "[CLSPUDeviceStateInterface] sendCommand skipped, no physical HID driver (VM/Simulator)"
- "bool CLSPUDeviceStateInterface::sendCommand(const void *, size_t)"
- "hingeState >= kCMMagicPoseHingeStateType_Ambiguous && hingeState < kCMMagicPoseHingeStateType_Max"
- "orientation >= kCMMagicPoseDeviceOrientationType_Ambiguous && orientation < kCMMagicPoseDeviceOrientationType_Max"
- "orientation0 >= kCMMagicPoseDeviceOrientationType_Ambiguous && orientation0 < kCMMagicPoseDeviceOrientationType_Max"
- "orientation1 >= kCMMagicPoseDeviceOrientationType_Ambiguous && orientation1 < kCMMagicPoseDeviceOrientationType_Max"
- "stableOrientationState >= kCMMagicPoseStableOrientationStateType_Ambiguous && stableOrientationState < kCMMagicPoseStableOrientationStateType_Max"
- "static void CLDeviceStateNotifier::onIoHidEventPhysical(void *, void *, void *, IOHIDEventRef)"
- "static void CLDeviceStateNotifier::onIoHidEventVirtual(void *, void *, void *, IOHIDEventRef)"
- "tabletopPose >= kCMMagicPoseTabletopPoseType_Ambiguous && tabletopPose < kCMMagicPoseTabletopPoseType_Max"
- "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
- "virtual bool CLDeviceStateNotifier::openHidDevice()"
- "virtual void CLDeviceStateNotifier::numberOfSpectatorsChanged(int, size_t)"
- "virtual void CLDeviceStateNotifier::visitDeviceState(const CMDeviceStateReport::DeviceState *)"
- "virtual void CLSPUDeviceStateInterface::visitPong(const CMDeviceStateReport::Pong *)"
- "void CLSPUDeviceStateInterface::onIoHidEvent(IOHIDEventRef)"
- "void CLSPUDeviceStateInterface::simulateDeviceStateEvent(uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, CFTimeInterval)_block_invoke"
- "void CLSPUDeviceStateInterface::visitIoHidEvent(const uint8_t *, size_t, const CFTimeInterval, const CFTimeInterval)"
- "{\"msg%{public}.0s\":\"Invalid device orientation value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"Invalid device orientation0 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"Invalid device orientation1 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"Invalid hinge state value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"Invalid stable orientation state value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"Invalid tabletop pose value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"[CLSPUDeviceStateInterface] Service required\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
```
