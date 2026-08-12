## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`

```diff

-1616.100.2.2.1
-  __TEXT.__text: 0x510b90
-  __TEXT.__auth_stubs: 0x5a30
-  __TEXT.__objc_stubs: 0x3c920
-  __TEXT.__objc_methlist: 0x291c0
-  __TEXT.__objc_classname: 0x58c2
-  __TEXT.__objc_methname: 0x6e907
-  __TEXT.__cstring: 0x1b79c
-  __TEXT.__objc_methtype: 0x12d86
-  __TEXT.__const: 0xf438
-  __TEXT.__oslogstring: 0x51943
-  __TEXT.__gcc_except_tab: 0x2614
+1620.100.1.2.3
+  __TEXT.__text: 0x511ec0
+  __TEXT.__auth_stubs: 0x5a40
+  __TEXT.__objc_stubs: 0x3c9e0
+  __TEXT.__objc_methlist: 0x291f8
+  __TEXT.__objc_classname: 0x58d2
+  __TEXT.__objc_methname: 0x6ea97
+  __TEXT.__cstring: 0x1b8ac
+  __TEXT.__objc_methtype: 0x12da6
+  __TEXT.__const: 0xf568
+  __TEXT.__oslogstring: 0x51bf3
+  __TEXT.__gcc_except_tab: 0x2644
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x9118
+  __TEXT.__swift5_typeref: 0x9156
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x961c
-  __TEXT.__swift5_builtin: 0x6cc
-  __TEXT.__swift5_reflstr: 0x86b0
-  __TEXT.__swift5_fieldmd: 0x6c94
-  __TEXT.__swift5_assocty: 0x950
-  __TEXT.__swift5_proto: 0x90c
-  __TEXT.__swift5_types: 0x690
-  __TEXT.__swift5_capture: 0x954c
+  __TEXT.__constg_swiftt: 0x96a4
+  __TEXT.__swift5_builtin: 0x6e0
+  __TEXT.__swift5_reflstr: 0x8760
+  __TEXT.__swift5_fieldmd: 0x6d08
+  __TEXT.__swift5_assocty: 0x968
+  __TEXT.__swift5_proto: 0x914
+  __TEXT.__swift5_types: 0x69c
+  __TEXT.__swift5_capture: 0x9588
   __TEXT.__swift5_protos: 0x1a4
   __TEXT.__swift_as_entry: 0x290
   __TEXT.__swift_as_ret: 0x2e8
   __TEXT.__swift_as_cont: 0x5a8
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xeb80
+  __TEXT.__unwind_info: 0xeb98
   __TEXT.__eh_frame: 0xa728
-  __DATA_CONST.__const: 0x276f8
+  __DATA_CONST.__const: 0x27890
   __DATA_CONST.__cfstring: 0xbae0
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x140

   __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x2d28
+  __DATA_CONST.__auth_got: 0x2d30
   __DATA_CONST.__got: 0x2850
-  __DATA_CONST.__auth_ptr: 0x14a8
-  __DATA.__objc_const: 0x3f5a8
-  __DATA.__objc_selrefs: 0x13598
-  __DATA.__objc_ivar: 0x2004
-  __DATA.__objc_data: 0xe218
-  __DATA.__data: 0xffd8
-  __DATA.__bss: 0xdc70
+  __DATA_CONST.__auth_ptr: 0x14b8
+  __DATA.__objc_const: 0x3f640
+  __DATA.__objc_selrefs: 0x135c0
+  __DATA.__objc_ivar: 0x2008
+  __DATA.__objc_data: 0xe240
+  __DATA.__data: 0x10008
+  __DATA.__bss: 0xdd70
   __DATA.__common: 0xb40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28330
-  Symbols:   2934
-  CStrings:  24117
+  Functions: 28340
+  Symbols:   2935
+  CStrings:  24138
 
Symbols:
+ _TUShouldUseSuperboxTelephonyProvider
CStrings:
+ "-[CSDCallStateController pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:]"
+ "-[CSDCallStateController pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:]"
+ "Clearing out pickWhenAvailable route %@ because user is picking available route %@"
+ "Dispatching invokeAudioSessionActivationStateChangedHandler onto observer's queue with active: %d"
+ "HoldTimePredictionError"
+ "Ignoring superseded Siri voice change (generation %ld)"
+ "Not picking prematurely selected audio route because it's a Speaker route originally selected for voicemail"
+ "Not pushing uplinkMuted %d to conference for call %@ since call should not own the mute handler under session-based muting"
+ "Picking local route with identifier: %@ (routeSelectionProvenance: %ld)"
+ "Picking paired device with identifier %@ (routeSelectionProvenance: %ld)"
+ "Re-asserting secondary camera opt-in for participant %llu on remote enable"
+ "Route %@ did not become available in %@ seconds"
+ "Siri output voice changed; debouncing call screening regeneration"
+ "Stopping waiting for route %@ to become available"
+ "T@\"NSNotificationCenter\",R,N,V_notificationCenter"
+ "Thumper calling unsupported for sender identity %@ (labelID %@): CT isSupported=%d, IDS thumperServiceEnabledForLabel=%d"
+ "Thumper calling unsupported for sender identity %@: empty telephony subscription label identifier"
+ "Vv36@0:8@\"NSString\"16B24q28"
+ "Vv36@0:8@16B24q28"
+ "Will pick route %@ when it becomes available to pick"
+ "[WARN] initWithTUConversation: conversation %@ has no provider identifier; not stamping %@ into context"
+ "_notificationCenter"
+ "_shouldLaunchInCallApplicationForCall:"
+ "_shouldLaunchInCallApplicationForCall: %d"
+ "_startObservingNotifications"
+ "conversationManager:conversationWillBeRemoved:"
+ "deviceIsGreenTea"
+ "eligibleToEnable"
+ "holdTimePrediction"
+ "initWithQueue:assistantServicesObserver:chManager:featureFlags:deviceSupport:notificationCenter:"
+ "notifyDelegatesOfConversationThatWillBeRemoved:"
+ "pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:"
+ "pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:"
+ "pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:"
+ "pickWhenAvailableRoute"
+ "route: %@ (routeSelectionProvenance: %ld)"
+ "setEligibleToEnable:"
+ "voiceChangeGenerationDebouncer"
- "-[CSDCallStateController pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:]"
- "-[CSDCallStateController pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:]"
- "Clearing out pickWhenAvailable route identifier %@ because user is picking available route %@"
- "Not picking prematurely selected audio route because it's Speaker"
- "Picking local route with identifier: %@"
- "Picking paired device with identifier %@"
- "Route identifier %@ did not become available in %@ seconds"
- "Siri output voice changed and the call screening needs to be regenerated!"
- "Stopping waiting for route identifier %@ to become available"
- "Vv28@0:8@\"NSString\"16B24"
- "Will pick route identifier %@ when it becomes available to pick"
- "_shouldLaunchInCallApplicationForProviderOfCall:"
- "initWithQueue:assistantServicesObserver:chManager:featureFlags:deviceSupport:"
- "pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickWhenAvailableRouteIdentifier"
```
