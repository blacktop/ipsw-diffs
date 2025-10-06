## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-173.2.0.0.0
-  __TEXT.__text: 0x6215c
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0x1260
+174.16.1.1.2
+  __TEXT.__text: 0x60528
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_stubs: 0x1680
   __TEXT.__init_offsets: 0x9c
-  __TEXT.__objc_methlist: 0x5b0
-  __TEXT.__const: 0x151c
-  __TEXT.__gcc_except_tab: 0x1618
-  __TEXT.__cstring: 0x3796
-  __TEXT.__oslogstring: 0xe68e
-  __TEXT.__objc_classname: 0xc6
-  __TEXT.__objc_methname: 0x20f6
-  __TEXT.__objc_methtype: 0x10cd
-  __TEXT.__unwind_info: 0x17c4
-  __TEXT.__eh_frame: 0x1dc
-  __DATA_CONST.__auth_got: 0x888
-  __DATA_CONST.__got: 0x198
+  __TEXT.__objc_methlist: 0x760
+  __TEXT.__const: 0x14fc
+  __TEXT.__gcc_except_tab: 0x1570
+  __TEXT.__cstring: 0x385c
+  __TEXT.__oslogstring: 0xeaa4
+  __TEXT.__objc_classname: 0xe6
+  __TEXT.__objc_methname: 0x284e
+  __TEXT.__objc_methtype: 0x1127
+  __TEXT.__unwind_info: 0x176c
+  __TEXT.__eh_frame: 0x1c8
+  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3bf0
-  __DATA_CONST.__cfstring: 0xb80
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x3690
+  __DATA_CONST.__cfstring: 0xd60
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x16f0
-  __DATA.__objc_selrefs: 0x5b8
-  __DATA.__objc_classrefs: 0xb0
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x84
-  __DATA.__objc_data: 0x1e0
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x1a00
+  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0xb08
   __DATA.__bss: 0xaa10
   __DATA.__common: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 23BB40B2-BC5C-34AA-8658-1F38B7D0384B
-  Functions: 2272
-  Symbols:   414
-  CStrings:  1962
+  UUID: B998E36F-EE20-35CE-8EE2-665DB83B64A4
+  Functions: 2218
+  Symbols:   430
+  CStrings:  2073
 
Symbols:
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _kMXSessionAudioCategory_AudioVideo
+ _kMXSessionAudioCategory_PhoneCall
+ _kMXSessionAudioCategory_VoiceCommand
+ _kMXSession_RouteDescriptionKey_AVAudioRouteName
+ _kMXSession_RouteDescriptionKey_RouteUID
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_ActiveAudioCategory
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_AudioCategory
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_SequenceNumber
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_SilenceVolumeHUD
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_Volume
+ _kMXSystemControllerNotification_PickableRoutesDidChange
+ _kMXSystemControllerNotification_SystemVolumeDidChange
+ _kMXSystemControllerProperty_PickedRoute
+ _objc_release_x25
+ _objc_retain_x19
+ _objc_retain_x8
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "@\"NSNumber\""
+ "@24@0:8@16"
+ "@28@0:8I16@20"
+ "@?"
+ "BT Stats for metric '%@' sent to CoreAnalytics with result %u manualVolumeUpdate: %@"
+ "BTAudioAVNotificationMonitor: Add listener (kMXSystemControllerNotification_SystemVolumeDidChange)"
+ "BTAudioAVNotificationMonitor: _volumeAudioCategoryMap %@"
+ "BTAudioAVNotificationMonitor: adding sequence num: %@ sequeneArray %@"
+ "BTAudioAVNotificationMonitor: is sequenceNumber %@ in _sequenceArray %s"
+ "BTAudioAVNotificationMonitor: kMXSystemControllerNotification_PickableRoutesDidChange"
+ "BTAudioAVNotificationMonitor: kMXSystemControllerNotification_SystemVolumeDidChange : volume %@, audio category %@, sequenceNumber %@, isPersonalizedVolumeUpdate %@ activeAudioCategory: %@"
+ "BTAudioAVNotificationMonitor: returning as audioCategory is nil"
+ "BTAudioAVNotificationMonitor: sequenceArray contents %@"
+ "BTAudioAVNotificationMonitor:Av audio route name %@"
+ "BTAudioDetect Input avgPwr %fdB,intv %u/%u,processed %llu,delivered %llu,rate %f,encoded %zu"
+ "BTAudioDetect Output avgPwr %fdB,intv %u/%u,processed %llu,delivered %llu,rate %f,encoded %zu"
+ "BTAudioPersonalizedVolumeDevice"
+ "BTUnifiedAudioDevice::startManualVolumeUpdateTimer: reached the time limit"
+ "Bottom-Up"
+ "BundleID"
+ "Creating _btAudioDeviceDict entry for %@ Device ID %u: "
+ "CurrentAudioCategory"
+ "CurrentVolume"
+ "Dropping manual volume update as the support is not available on accessory for this software version"
+ "I24@0:8@16"
+ "Initializing Personalized Volume Device %@ "
+ "IsPersonalizedVolumeUpdate"
+ "ManualVolumeUpdate"
+ "NotifyManualVolumeChanged:shouldUpdateBuds:"
+ "PVRampEndAudioCategoryConfigChanged"
+ "PVRampEndInEarStatusChanged"
+ "PVRampEndRampAchieved"
+ "PersonalizedVolume"
+ "PersonalizedVolumeEnabled"
+ "Pickable routes for routeUid %@ _currentDeviceUID %@ _currentActiveVolumeAudioCategory %@ (current category is <%@>):"
+ "RampInProgress"
+ "ReasonForManualUpdate"
+ "Release Smart Route Manager Entry for %@ %d"
+ "Request to get the volume for wrong catetory: %@"
+ "Spatial Profile : HRTF no longer 'required in plugin: Trigger Release %d"
+ "T@\"NSNumber\",&,N,V_isPersonalizedVolumeUpdate"
+ "T@\"NSNumber\",&,N,V_processManualVolumeUpdates"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_manualVolumeUpdatesQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",N,V_avNotificationMonitorQueue"
+ "T@\"NSString\",&,N,V_currentActiveVolumeAudioCategory"
+ "T@\"NSString\",&,N,V_currentDeviceUID"
+ "T@\"NSString\",&,N,V_reasonForManualVolumeUpdate"
+ "T@\"NSString\",?,R,C"
+ "Top-Down"
+ "_avNotificationMonitorQueue"
+ "_bdAddr"
+ "_btAudioDeviceDict"
+ "_btPersonalizedVolumeDeviceMutex"
+ "_currentActiveVolumeAudioCategory"
+ "_currentDeviceUID"
+ "_deviceID"
+ "_getCurrentAudioCategoryFromString:"
+ "_getManualVolumeUpdateReasonFromString:"
+ "_isPersonalizedVolumeUpdate"
+ "_manualUpdateDispatchBlock"
+ "_manualVolumeUpdatesQueue"
+ "_personalizedVolumeEnabled"
+ "_processManualVolumeUpdates"
+ "_reasonForManualVolumeUpdate"
+ "_sendManualVolumeUpdate"
+ "_sequenceArray"
+ "_volumeAudioCategoryMap"
+ "avNotificationMonitorQueue"
+ "boolValue"
+ "choosePickableRoute"
+ "com.apple.BTAudioHALPlugin.BTAudioAVNotificationMonitor.ManaualVolumeUpdatesQueue"
+ "com.apple.Bluetooth.PersonalizedVolumeManualUpdateV2"
+ "componentsSeparatedByString:"
+ "currentActiveVolumeAudioCategory"
+ "currentDeviceUID"
+ "deviceUID is nil"
+ "firstObject"
+ "getCurrentPersonalizedVolumeDevice"
+ "getPersonalizedVolumeDevice:"
+ "getVolumeForCurrentAudioCategory:"
+ "initWithBluetoothInfo:deviceAddr:"
+ "initWithString:"
+ "intValue"
+ "isBluetoothRoute"
+ "isPersonalizedVolumeUpdate"
+ "isVolumeUpdateToAccessoryRequired:"
+ "manualVolumeUpdatesQueue"
+ "numberWithBool:"
+ "numberWithLongLong:"
+ "numberWithUnsignedChar:"
+ "objectForKeyedSubscript:"
+ "personalizedVolumeEnabled:"
+ "processManualVolumeUpdates"
+ "processManualVolumeUpdates:"
+ "reasonForManualVolumeUpdate"
+ "registerPersonalizedVolumeListener:deviceUID:"
+ "sendManualVolumeUpdate:"
+ "setAvNotificationMonitorQueue:"
+ "setCurrentActiveVolumeAudioCategory:"
+ "setCurrentDeviceUID:"
+ "setIsPersonalizedVolumeUpdate:"
+ "setManualVolumeUpdatesQueue:"
+ "setProcessManualVolumeUpdates:"
+ "setReasonForManualVolumeUpdate:"
+ "startManualVolumeUpdateTimer"
+ "unRegisterPersonalizedVolumeListener:deviceUID:"
+ "updateVolumeActiveAudioCategoryMap:audioCategory:"
+ "v20@0:8C16"
+ "v28@0:8C16@20"
+ "v28@0:8I16@20"
- "Constructor we got the nexus UUID"
- "Device sample rate changed %f -> %f [encoder = %d, decoder = %d]"
- "LC3"
- "LECA Device XPC connection for UID %@ connected to[ %d ] "
- "LECA: Codec Update completed Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
- "LECA: Direction %x Stream state output = %d input = %d"
- "LECA: Setting Supported Codecs"
- "LECA: UpdateSamplingRate minRate %f, maxRate %f"
- "LECA: Updating Codecs Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
- "Spatial Profile : HRTF no longer required in plugin: Trigger Release %d"
- "kBTAudioMsgPropertyChannelLayout"
- "kBTAudioMsgPropertyMaxChannels"
- "xpc_get_type(channelLayoutProp) == XPC_TYPE_INT64"
- "xpc_get_type(maxChannelsProp) == XPC_TYPE_INT64"
- "xpc_get_type(selectedCodecProp) == XPC_TYPE_INT64"

```
