## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`

```diff

-1616.100.2.0.0
-  __TEXT.__text: 0x503ba8
-  __TEXT.__auth_stubs: 0x58c0
-  __TEXT.__objc_stubs: 0x3a6a0
-  __TEXT.__objc_methlist: 0x288c0
-  __TEXT.__objc_classname: 0x5169
-  __TEXT.__objc_methname: 0x6aac7
-  __TEXT.__cstring: 0x1bbd8
-  __TEXT.__objc_methtype: 0x12b6b
-  __TEXT.__const: 0xeab0
-  __TEXT.__oslogstring: 0x4e7eb
-  __TEXT.__gcc_except_tab: 0x20e0
+1620.100.1.1.22
+  __TEXT.__text: 0x50479c
+  __TEXT.__auth_stubs: 0x58d0
+  __TEXT.__objc_stubs: 0x3a740
+  __TEXT.__objc_methlist: 0x288f0
+  __TEXT.__objc_classname: 0x5159
+  __TEXT.__objc_methname: 0x6ad07
+  __TEXT.__cstring: 0x1bc78
+  __TEXT.__objc_methtype: 0x12b5b
+  __TEXT.__const: 0xebf0
+  __TEXT.__oslogstring: 0x4ea4b
+  __TEXT.__gcc_except_tab: 0x2110
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x864a
+  __TEXT.__swift5_typeref: 0x866e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x87dc
-  __TEXT.__swift5_builtin: 0x62c
-  __TEXT.__swift5_reflstr: 0x7560
-  __TEXT.__swift5_fieldmd: 0x6200
-  __TEXT.__swift5_assocty: 0x780
-  __TEXT.__swift5_proto: 0x8bc
-  __TEXT.__swift5_types: 0x5f8
+  __TEXT.__constg_swiftt: 0x8864
+  __TEXT.__swift5_builtin: 0x640
+  __TEXT.__swift5_reflstr: 0x7610
+  __TEXT.__swift5_fieldmd: 0x6274
+  __TEXT.__swift5_assocty: 0x798
+  __TEXT.__swift5_proto: 0x8c4
+  __TEXT.__swift5_types: 0x604
   __TEXT.__swift5_protos: 0x168
   __TEXT.__swift_as_entry: 0x328
   __TEXT.__swift_as_ret: 0x33c
   __TEXT.__swift_as_cont: 0x668
-  __TEXT.__swift5_capture: 0x86ec
+  __TEXT.__swift5_capture: 0x86f0
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__unwind_info: 0xe0e0
   __TEXT.__eh_frame: 0xac78
-  __DATA_CONST.__const: 0x24510
+  __DATA_CONST.__const: 0x24630
   __DATA_CONST.__cfstring: 0xbec0
   __DATA_CONST.__objc_classlist: 0xbc8
   __DATA_CONST.__objc_catlist: 0x140

   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x2c70
+  __DATA_CONST.__auth_got: 0x2c78
   __DATA_CONST.__got: 0x25b8
-  __DATA_CONST.__auth_ptr: 0x11a0
-  __DATA.__objc_const: 0x3c5a8
-  __DATA.__objc_selrefs: 0x12d68
-  __DATA.__objc_ivar: 0x1f08
-  __DATA.__objc_data: 0xd338
-  __DATA.__data: 0xebc8
-  __DATA.__bss: 0xe6dc
+  __DATA_CONST.__auth_ptr: 0x11b0
+  __DATA.__objc_const: 0x3c640
+  __DATA.__objc_selrefs: 0x12d90
+  __DATA.__objc_ivar: 0x1f0c
+  __DATA.__objc_data: 0xd360
+  __DATA.__data: 0xebb8
+  __DATA.__bss: 0xe7dc
   __DATA.__common: 0x9c9
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27139
-  Symbols:   2832
-  CStrings:  23487
+  Functions: 27148
+  Symbols:   2833
+  CStrings:  23506
 
Symbols:
+ _TUShouldUseSuperboxTelephonyProvider
CStrings:
+ "-[CSDCallStateController pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:]"
+ "-[CSDCallStateController pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:routeSelectionProvenance:]"
+ "Clearing out pickWhenAvailable route %@ because user is picking available route %@"
+ "Did not find relevant app running to host the call, terminating it: %@"
+ "HoldTimePredictionError"
+ "Not picking prematurely selected audio route because it's a Speaker route originally selected for voicemail"
+ "Not pushing uplinkMuted %d to conference for call %@ since call should not own the mute handler under session-based muting"
+ "Picking local route with identifier: %@ (routeSelectionProvenance: %ld)"
+ "Picking paired device with identifier %@ (routeSelectionProvenance: %ld)"
+ "Re-asserting secondary camera opt-in for participant %llu on remote enable"
+ "Route %@ did not become available in %@ seconds"
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
+ "initWithQueue:chManager:featureFlags:deviceSupport:notificationCenter:"
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
- "Stopping waiting for route identifier %@ to become available"
- "Vv28@0:8@\"NSString\"16B24"
- "Will pick route identifier %@ when it becomes available to pick"
- "[WARN] Did not find relevant app running to host the call: %@, Terminating it."
- "_shouldLaunchInCallApplicationForProviderOfCall:"
- "initWithQueue:chManager:featureFlags:deviceSupport:"
- "pickLocalRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickPairedHostDeviceRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickRouteWithUniqueIdentifier:shouldWaitUntilAvailable:"
- "pickWhenAvailableRouteIdentifier"
```
