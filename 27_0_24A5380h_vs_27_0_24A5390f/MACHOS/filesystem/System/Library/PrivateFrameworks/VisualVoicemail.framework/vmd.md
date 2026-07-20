## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-954.0.0.0.0
-  __TEXT.__text: 0xbb3c8
-  __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_stubs: 0xe0e0
+956.0.0.0.0
+  __TEXT.__text: 0xc0fa4
+  __TEXT.__auth_stubs: 0x18a0
+  __TEXT.__objc_stubs: 0xe2a0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x7c24
-  __TEXT.__cstring: 0x47fa
-  __TEXT.__objc_classname: 0xe0a
-  __TEXT.__objc_methname: 0x12963
-  __TEXT.__objc_methtype: 0x34f4
+  __TEXT.__objc_methlist: 0x7e74
+  __TEXT.__cstring: 0x491a
+  __TEXT.__objc_classname: 0xe4a
+  __TEXT.__objc_methname: 0x12d7f
+  __TEXT.__objc_methtype: 0x35da
   __TEXT.__const: 0x522
-  __TEXT.__gcc_except_tab: 0xca98
-  __TEXT.__oslogstring: 0x16107
+  __TEXT.__gcc_except_tab: 0x10d1c
+  __TEXT.__oslogstring: 0x16337
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4028
+  __TEXT.__unwind_info: 0x49a0
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__const: 0x3400
-  __DATA_CONST.__cfstring: 0x5520
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__const: 0x34e0
+  __DATA_CONST.__cfstring: 0x5640
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0xc70
-  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__auth_got: 0xc68
+  __DATA_CONST.__got: 0x828
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA.__objc_const: 0x127b8
-  __DATA.__objc_selrefs: 0x4778
-  __DATA.__objc_ivar: 0x79c
-  __DATA.__objc_data: 0x1d20
+  __DATA.__objc_const: 0x12cf0
+  __DATA.__objc_selrefs: 0x4820
+  __DATA.__objc_ivar: 0x7d0
+  __DATA.__objc_data: 0x1e10
   __DATA.__data: 0x1220
-  __DATA.__bss: 0x620
+  __DATA.__bss: 0x640
   __DATA.__common: 0x4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3551
-  Symbols:   710
-  CStrings:  5832
+  Functions: 3605
+  Symbols:   709
+  CStrings:  5898
 
Symbols:
- ___memcpy_chk
CStrings:
+ "%s#E %s%sGet QuickSwitch mode failed for account UUID %@, could not find service"
+ "%s#E %s%sGet QuickSwitch parameters failed for account UUID %@, could not find subscription"
+ "%s#E Fetch failed, executing completion"
+ "%s#I %s Get QuickSwitch mode %s for accountUUID %@"
+ "%s#I %s%s%@ is notifying delegates about voicemail store changed"
+ "%s#I Fetch already in progress, %@ (pending: %lu)"
+ "%s#I Fetch failed, executing %lu pending completion(s)"
+ "%s#I Fetch succeeded, executing %lu pending completion(s)"
+ "%s#I Fetch succeeded, executing completion"
+ "%s#I Store saved but carrier services controller is not set, skipping"
+ "%s#I [%s] Get QuickSwitch parameters for accountUUID %@"
+ "@56@0:8@16@24@32@40@48"
+ "T@\"NSMutableArray\",&,N,V_pendingFetchCompletions"
+ "T@\"NSString\",C,N,V_accountID"
+ "T@\"NSString\",C,N,V_device"
+ "T@\"NSString\",C,N,V_mode"
+ "T@\"NSString\",R,C,N,V_accountID"
+ "T@\"NSString\",R,N,V_version"
+ "T@\"VMServiceNotificationObserver\",W,N,V_notificationObserver"
+ "TB,N,V_dataReceived"
+ "TB,N,V_roleManual"
+ "TB,N,V_twinManual"
+ "VMCarrierServicesController.mm"
+ "VMQuickSwitchCache"
+ "VMQuickSwitchParameters"
+ "VMSharedStore"
+ "VoicemailStore.mm"
+ "_accountID"
+ "_dataReceived"
+ "_device"
+ "_pendingFetchCompletions"
+ "_roleManual"
+ "_twinManual"
+ "dataReceived"
+ "deserializeFromPayload:"
+ "device"
+ "executePendingFetchCompletions:data:error:"
+ "getQuickSwitchDataCache:"
+ "getQuickSwitchDataCacheWithCompletion:"
+ "getQuickSwitchDataCacheWithReply:"
+ "getQuickSwitchModeParameterForAccountUUID:completion:"
+ "getQuickSwitchModeParameterForAccountUUID:reply:"
+ "getQuickSwitchParametersForAccountUUID:completion:"
+ "getQuickSwitchParametersForAccountUUID:reply:"
+ "getQuickSwitchRoleParameterForAccountUUID:completion:"
+ "getQuickSwitchTwinParameterForAccountUUID:completion:"
+ "handleVoicemailStoreChanged"
+ "handleVoicemailStoreChanged:"
+ "initWithStateRequestController:transcriptionService:telephonyClient:queue:voicemailStore:notificationObserver:"
+ "initWithTranscriptionService:queue:telephonyClient:voicemailStore:notificationObserver:"
+ "notificationObserver != nil"
+ "notifyVoicemailsUpdated:"
+ "notifyVoicemailsUpdated_sync:"
+ "pendingFetchCompletions"
+ "prepareVoicemailsWithCompletion:"
+ "queuing"
+ "roleManual"
+ "setAccountID:"
+ "setDataReceived:"
+ "setDevice:"
+ "setNotificationObserver:"
+ "setPendingFetchCompletions:"
+ "setRoleManual:"
+ "setTwinManual:"
+ "skipping"
+ "storeSaved"
+ "twinManual"
+ "v16@?0@\"NSOrderedSet\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@\"VMQuickSwitchParameters\"8"
+ "v20@?0@\"NSArray\"8B16"
+ "v20@?0@\"NSString\"8B16"
+ "v24@0:8@\"NSOrderedSet\"16"
+ "v24@0:8@?<v@?@\"NSArray\"B>16"
+ "v24@0:8@?<v@?B@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?BQ@\"NSError\">16"
+ "v28@?0B8@\"NSArray\"12@\"NSError\"20"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"VMQuickSwitchParameters\"@\"NSError\">24"
+ "v36@0:8B16@20@28"
+ "vm.shared.store"
+ "voicemailStore != nil"
- "%s#I %s%s%@ is notifying delegates about voicemail store saved"
- "%s#I Fetch already in progress, skipping"
- "@32@0:8@16^B24"
- "VMCarrierServicesController.m"
- "VoicemailStore.m"
- "getQuickSwitchRoleParameterForAccountUUID:isManual:"
- "getQuickSwitchTwinParameterForAccountUUID:isManual:"
- "handleVoicemailStoreSaved"
- "initWithStateRequestController:transcriptionService:telephonyClient:queue:"
- "initWithTranscriptionService:queue:telephonyClient:"
- "isDataAvailable"
- "isDeleted"
- "isTemporary"
- "notifyVoicemailStoreSaved"
- "notifyVoicemailStoreSaved_sync"
- "v24@0:8@?<v@?B@\"NSError\">16"
```
