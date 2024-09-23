## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1525.200.51.0.0
-  __TEXT.__text: 0x3a6320
+1525.200.73.0.0
+  __TEXT.__text: 0x3aac2c
   __TEXT.__auth_stubs: 0x3e90
-  __TEXT.__objc_stubs: 0x31000
-  __TEXT.__objc_methlist: 0x1c43c
+  __TEXT.__objc_stubs: 0x310e0
+  __TEXT.__objc_methlist: 0x1c504
   __TEXT.__objc_classname: 0x2a96
-  __TEXT.__objc_methname: 0x579a6
-  __TEXT.__objc_methtype: 0xf0b7
-  __TEXT.__cstring: 0x1ee6d
-  __TEXT.__const: 0x8590
-  __TEXT.__oslogstring: 0x3e412
-  __TEXT.__gcc_except_tab: 0x26ac
+  __TEXT.__objc_methname: 0x57ba1
+  __TEXT.__objc_methtype: 0xf105
+  __TEXT.__cstring: 0x1f04d
+  __TEXT.__const: 0x85f0
+  __TEXT.__oslogstring: 0x3e882
+  __TEXT.__gcc_except_tab: 0x26bc
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x5f38
+  __TEXT.__swift5_typeref: 0x5f60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x6400
-  __TEXT.__swift5_builtin: 0x58c
-  __TEXT.__swift5_reflstr: 0x52e3
-  __TEXT.__swift5_fieldmd: 0x4664
-  __TEXT.__swift5_assocty: 0x6e0
+  __TEXT.__constg_swiftt: 0x64a4
+  __TEXT.__swift5_builtin: 0x578
+  __TEXT.__swift5_reflstr: 0x5403
+  __TEXT.__swift5_fieldmd: 0x46f8
+  __TEXT.__swift5_assocty: 0x6c8
   __TEXT.__swift5_proto: 0x604
   __TEXT.__swift5_types: 0x478
-  __TEXT.__swift5_capture: 0x2868
+  __TEXT.__swift5_capture: 0x288c
   __TEXT.__swift5_protos: 0x10c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xaeb0
-  __TEXT.__eh_frame: 0x4688
+  __TEXT.__unwind_info: 0xaf70
+  __TEXT.__eh_frame: 0x4760
   __DATA_CONST.__auth_got: 0x1f58
   __DATA_CONST.__got: 0x1e78
-  __DATA_CONST.__auth_ptr: 0x1020
-  __DATA_CONST.__const: 0x12df0
-  __DATA_CONST.__cfstring: 0x9f00
+  __DATA_CONST.__auth_ptr: 0x1008
+  __DATA_CONST.__const: 0x12fa8
+  __DATA_CONST.__cfstring: 0x9f40
   __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x998

   __DATA_CONST.__objc_intobj: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__linkguard: 0x16
-  __DATA.__objc_const: 0x3f088
-  __DATA.__objc_selrefs: 0xfeb8
-  __DATA.__objc_ivar: 0x1af4
-  __DATA.__objc_data: 0xb100
-  __DATA.__data: 0xc0a8
+  __DATA.__objc_const: 0x3f268
+  __DATA.__objc_selrefs: 0xff28
+  __DATA.__objc_ivar: 0x1b00
+  __DATA.__objc_data: 0xb170
+  __DATA.__data: 0xc0f8
   __DATA.__bss: 0x90d8
-  __DATA.__common: 0x5d0
+  __DATA.__common: 0x5e8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19681
-  Symbols:   2166
-  CStrings:  20879
+  Functions: 19770
+  Symbols:   2165
+  CStrings:  20926
 
Symbols:
- __linkguard_init
CStrings:
+ "recurring disclosure timer triggered"
+ "session:didReceiveUnderlyingLinksStatus:"
+ "handleCallUnderlyingLinksConnectionChangedWithNotification:"
+ "reportingController:pickedRoute:updatedByAnyTriggerForCall:"
+ "_isUnderlyingLinksConnected"
+ "CallRecordingRecurringDisclosureFinishedNotificationName"
+ " isUnderlyingLinksConnected=%!d(MISSING)"
+ "setIsUnderlyingLinksConnected:"
+ "recurringDisclosureCount"
+ "isAuxiliary"
+ "pickedRouteDidChangeHandler"
+ "isRedisclosing"
+ "sessionProvider:didReceiveUnderlyingLinksStatus:"
+ "recurring disclosure timer triggered, but we aren't tracking a recording session"
+ "groupSessionDidConnectUnderlyingLinks for session: %!@(MISSING)"
+ "underlyingLinksConnected"
+ "Scheduing recurring disclosure for %!s(MISSING) seconds from now with randomness %!s(MISSING)"
+ "recurring disclosure finished, but we aren't tracking a recording session"
+ "Notified that recurring disclosure finished"
+ "picked route: %!@(MISSING)"
+ "Received %!l(MISSING)d new voicemails since date %!s(MISSING): %!s(MISSING)"
+ "Asked to begin playing call recording recurring disclosure"
+ "Voicemail store changed. We were waiting for %!s(MISSING) and found %!s(MISSING)"
+ "Audio route update for %!s(MISSING): %!@(MISSING)"
+ "Setting underlying network link status to %!@(MISSING)"
+ "[CSDConversation] didReceiveUnderlyingLinksStatus: %!@(MISSING)"
+ "initWithUUID:state:callUUID:requestUUID:recordingStartedDate:recordingEndedDate:isRedisclosing:"
+ "recurring disclosure finished"
+ "v28@0:8@\"<CSDIDSGroupSessionProvider>\"16B24"
+ "Failed to transition to not playing recurring recording disclosure"
+ "groupSessionDidDisconnectUnderlyingLinks for session: %!@(MISSING)"
+ "/System/Library/PrivateFrameworks/TelephonyUtilities.framework/recurringDisclosureTwinkle.caf"
+ "v28@0:8@\"CSDIDSGroupSession\"16B24"
+ "CSDCallUnderlyingLinksConnectionChangedNotification"
+ "Setting up recurring disclosure"
+ "recurringDisclosureWorkItem"
+ "audioRoute"
+ "Asked to update %!l(MISSING)d voicemail notifications"
+ "isUnderlyingLinksConnected"
+ "recurringDisclosureFinishedNotification:"
+ "Recording not allowed because disclosure cannot be heard on the remote side."
+ "TB,N,V_isUnderlyingLinksConnected"
+ "Asked to play recurring recording disclosure"
+ "Failed to transition to playing recurring disclosure while recording"
+ "recurringDisclosureAudioPlayer"
+ "callToAudioRoutesTracker"
+ "setPickedRouteDidChangeHandler:"
+ "reportRouteWasPickedByAnyTrigger:"
- "Asked to end call recording start disclosure"
- "initWithUUID:state:callUUID:requestUUID:recordingStartedDate:recordingEndedDate:"

```
