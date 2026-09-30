## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-446.0.0.0.0
-  __TEXT.__text: 0x7fc44
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x5480
+450.2.0.0.0
+  __TEXT.__text: 0x7f78c
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x54c0
   __TEXT.__const: 0x248
-  __TEXT.__gcc_except_tab: 0x284c
-  __TEXT.__cstring: 0xb501
-  __TEXT.__oslogstring: 0x1b92
-  __TEXT.__dlopen_cstrs: 0x4dc
-  __TEXT.__unwind_info: 0x1c00
-  __TEXT.__objc_classname: 0x5fa
-  __TEXT.__objc_methname: 0xf366
+  __TEXT.__gcc_except_tab: 0x26e0
+  __TEXT.__cstring: 0xb4e5
+  __TEXT.__oslogstring: 0x1c34
+  __TEXT.__dlopen_cstrs: 0x4db
+  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__objc_classname: 0x5fd
+  __TEXT.__objc_methname: 0xf40e
   __TEXT.__objc_methtype: 0x1b08
-  __TEXT.__objc_stubs: 0xb2c0
-  __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x2918
+  __TEXT.__objc_stubs: 0xb2a0
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x28b8
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_selrefs: 0x3670
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x6c0
-  __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x77e0
-  __AUTH_CONST.__objc_const: 0x9380
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x9e0
+  __AUTH_CONST.__cfstring: 0x7740
+  __AUTH_CONST.__objc_const: 0x93b0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x1450
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x6f0
+  __DATA.__objc_ivar: 0x6f4
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x2d8
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2554
-  Symbols:   3120
-  CStrings:  4380
+  Functions: 2560
+  Symbols:   3124
+  CStrings:  4385
 
Symbols:
+ _AXLogTemp
- _OBJC_CLASS_$_AVAudioPCMBuffer
- _VOTLogCommon
- _log2
CStrings:
+ "\x05\x11"
+ "\x1a"
+ "%!s(MISSING): session active: %!@(MISSING)"
+ "-[AXHeardController updateAnalytics]_block_invoke_2"
+ "-[HUAccessoryHearingSyncManager _sendIDSMessageIfNeededForListeningModes:addresses:force:]"
+ "-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]"
+ "-[HUAccessoryHearingSyncManager shouldUpdateWatchesWithListeningModes:]_block_invoke"
+ "-[HUComfortSoundsController _handleContinuitySessionCheck]"
+ "Changed listening mode %!@(MISSING), for device: %!@(MISSING)"
+ "Found identifiers for %!@(MISSING) = %!@(MISSING)"
+ "HUAccessoryHearingSyncManager Characteristic %!@(MISSING), addresses %!@(MISSING)"
+ "Headphone Selected %!d(MISSING), Listening modes sent to Watches: %!@(MISSING), new: %!@(MISSING)"
+ "Listening modes for Watch changed: %!d(MISSING)"
+ "Routes and isHeadphoneStreamSelected are updated, deviceListeningState: %!@(MISSING)"
+ "T@\"AXDispatchTimer\",&,N,V_messageTimer"
+ "TB,N,V_isHeadphoneStreamSelected"
+ "TB,N,V_isInContinuitySession"
+ "Updated listening modes for Watch: %!@(MISSING)"
+ "_handleContinuitySessionCheck"
+ "_isHeadphoneStreamSelected"
+ "_isInContinuitySession"
+ "_messageTimer"
+ "_sendIDSMessageIfNeededForListeningModes:addresses:force:"
+ "clearEngine"
+ "isHeadphoneStreamSelected"
+ "isInContinuitySession"
+ "messageTimer"
+ "paCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsync"
+ "routesDidChange isHeadphoneStreamSelected %!d(MISSING)"
+ "scheduleFile:atTime:completionCallbackType:completionHandler:"
+ "sendIDSMessageIfNeededForNewListeningModes:addresses:force:"
+ "sendListeningModesIDSMessageIfNeeded"
+ "setIsHeadphoneStreamSelected:"
+ "setIsInContinuitySession:"
+ "setMessageTimer:"
+ "shouldUpdateWatchesWithListeningModes:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement"
+ "v16@?0@\"BluetoothDevice\"8"
+ "v16@?0q8"
- "\x06"
- "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2"
- "-[HUAccessoryHearingSyncManager listeningModesChangedState:]"
- "-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke"
- "Error reading audio file into buffer: %!@(MISSING)"
- "Headphone Selected %!d(MISSING), Listening modes Watch saved: %!@(MISSING), new: %!@(MISSING)"
- "Listening modes added AccessoryChangeWatch"
- "Listening modes changed AccessoryChangeAll"
- "Listening modes no changes AccessoryChangeNone"
- "Listening modes persistent: %!@(MISSING) new: %!@(MISSING)"
- "Listening modes removed AccessoryChangeWatch"
- "Oneness active: %!@(MISSING)"
- "Set listening mode %!@(MISSING), for device: %!@(MISSING)"
- "Skipping tipi update. Address is nil %!@(MISSING) - %!@(MISSING)"
- "T@\"NSMutableDictionary\",&,N,V_tipiStateByIdentifier"
- "Tipi updated for %!@(MISSING) - %!@(MISSING)"
- "_handleOnenessCheck"
- "_tipiStateByIdentifier"
- "_watchListeningState"
- "checkIdentifier:forOwnershipWithCompletion:"
- "initWithPCMFormat:frameCapacity:"
- "listeningModesChangedState:"
- "paCurrentBluetoothDeviceSupportingTransparencyAccommodations"
- "readIntoBuffer:error:"
- "scheduleBuffer:atTime:options:completionHandler:"
- "setTipiChangedHandler:"
- "setTipiStateByIdentifier:"
- "setWatchListeningState:"
- "softlink:r:path:/System/Library/PrivateFrameworks//UserManagement.framework/UserManagement"
- "tipiDevices"
- "tipiState"
- "tipiStateByIdentifier"
- "v16@?0@\"CBDevice\"8"
- "watchListeningState"

```
