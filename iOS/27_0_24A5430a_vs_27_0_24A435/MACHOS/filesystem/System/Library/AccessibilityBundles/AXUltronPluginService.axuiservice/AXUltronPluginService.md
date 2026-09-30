## AXUltronPluginService

> `/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

 3240.9.0.0.0
-  __TEXT.__text: 0x390c
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x42c
+  __TEXT.__text: 0x43dc
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x1d0
-  __TEXT.__objc_classname: 0x81
-  __TEXT.__objc_methname: 0xcaf
-  __TEXT.__objc_methtype: 0x3d9
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__objc_methname: 0x106e
+  __TEXT.__objc_methtype: 0x404
   __TEXT.__constg_swiftt: 0x88
   __TEXT.__swift5_typeref: 0x93
   __TEXT.__swift5_fieldmd: 0x10

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__oslogstring: 0x545
-  __TEXT.__cstring: 0xd3
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__oslogstring: 0x74a
+  __TEXT.__cstring: 0xef
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__eh_frame: 0x108
   __DATA_CONST.__const: 0x228
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA.__objc_const: 0x4a0
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_const: 0x568
+  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x160
-  __DATA.__data: 0x188
+  __DATA.__data: 0x1e8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 94
-  Symbols:   143
-  CStrings:  224
+  Functions: 108
+  Symbols:   161
+  CStrings:  275
 
Symbols:
+ _AXIDSServiceDeviceNRIdentifierKey
+ _AXIDSServiceDeviceNearbyStatusKey
+ _AXIDSServiceMessageKey
+ _AXSDSoundDetectionGenerateUserNotificationForDetectionTypeFromSource
+ _AXSDSoundDetectionMessageKeyConfidence
+ _AXSDSoundDetectionMessageKeyType
+ _NRDevicePropertyHWModelString
+ _OBJC_CLASS_$_AXIDSServices
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSUUID
+ ___NSArray0__struct
+ ___kCFBooleanTrue
+ _objc_alloc
+ _objc_opt_isKindOfClass
+ _objc_retain_x23
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "@\"NSMutableDictionary\""
+ "AXIDSServicesClient"
+ "IDS server connection interrupted — clearing stale wrist state"
+ "T@\"NSArray\",&,N,V_connectedDevices"
+ "T@\"NSMutableDictionary\",&,N,V_watchActiveWristState"
+ "TB,N,V_hasPendingWristStateRequest"
+ "UPDATING: _watchActiveWristState: %@, deviceID:%@"
+ "Watch SR: nearby supported watch found but wrist state unknown — requesting state, phone continues listening"
+ "WatchOS sound recognition forwarding changed"
+ "[%@]: Sound detection delegated to Watch — syncing all keys to companion"
+ "[%@]: Watch is actively listening — iPhone stopped with %lu enabled sounds synced"
+ "[%@]: iPhone should stop listening for watch forwarding."
+ "_connectedDevices"
+ "_hasConnectedWatchWithSoundRecognitionSupport"
+ "_hasPendingWristStateRequest"
+ "_requestWatchWristState"
+ "_shouldPhoneBeListening"
+ "_shouldStopSoundDetectionForWatchCoordination:"
+ "_watchActiveWristState"
+ "allowForwardingSoundRecognitionToSupportedWatch"
+ "boolValue"
+ "bridgeSettings"
+ "connectedDevices"
+ "connectedDevicesDidChange:"
+ "connectedDevicesDidChange: %@"
+ "deviceForBluetoothID:"
+ "dictionary"
+ "didReceiveIncomingData:"
+ "doubleValue"
+ "hasPendingWristStateRequest"
+ "hasPrefix:"
+ "initWithUUIDString:"
+ "lowercaseString"
+ "n237"
+ "n238"
+ "n240"
+ "objectForKeyedSubscript:"
+ "onWristState"
+ "overrideSupportWatchSoundRecognition"
+ "publishMessage:priority:requestingResponse:"
+ "registerForIncomingData:"
+ "removeAllObjects"
+ "serverConnectionWasInterrupted"
+ "setConnectedDevices:"
+ "setHasPendingWristStateRequest:"
+ "setObject:forKeyedSubscript:"
+ "setWatchActiveWristState:"
+ "syncAllKeysToCompanion"
+ "v24@0:8@\"NSArray\"16"
+ "valueForProperty:"
+ "watchActiveWristState"
```
