## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

-527.400.0.0.0
-  __TEXT.__text: 0x26dddc
-  __TEXT.__auth_stubs: 0x2570
+529.2.0.0.0
+  __TEXT.__text: 0x264ab8
+  __TEXT.__auth_stubs: 0x2580
   __TEXT.__objc_stubs: 0x109a0
   __TEXT.__objc_methlist: 0x7b40
-  __TEXT.__const: 0x3730
-  __TEXT.__cstring: 0xd1dc
-  __TEXT.__oslogstring: 0x199ab
+  __TEXT.__const: 0x3460
+  __TEXT.__cstring: 0xd1ac
+  __TEXT.__oslogstring: 0x19b0b
   __TEXT.__gcc_except_tab: 0x2194
-  __TEXT.__objc_methname: 0x1a80f
+  __TEXT.__objc_methname: 0x1a82b
   __TEXT.__objc_classname: 0x1f8f
   __TEXT.__objc_methtype: 0x51fb
-  __TEXT.__constg_swiftt: 0x2654
-  __TEXT.__swift5_typeref: 0x23cc
-  __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x1c84
-  __TEXT.__swift5_fieldmd: 0x122c
-  __TEXT.__swift5_capture: 0x38fc
-  __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_proto: 0x28c
-  __TEXT.__swift5_types: 0x160
+  __TEXT.__constg_swiftt: 0x261c
+  __TEXT.__swift5_typeref: 0x2378
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_reflstr: 0x1ca4
+  __TEXT.__swift5_fieldmd: 0x121c
+  __TEXT.__swift5_capture: 0x3dc0
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__swift5_proto: 0x268
+  __TEXT.__swift5_types: 0x158
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__info_plist: 0x582
-  __TEXT.__unwind_info: 0x6e88
-  __TEXT.__eh_frame: 0xf730
-  __DATA_CONST.__auth_got: 0x12c8
-  __DATA_CONST.__got: 0x1228
-  __DATA_CONST.__auth_ptr: 0x790
-  __DATA_CONST.__const: 0xd3d0
+  __TEXT.__info_plist: 0x580
+  __TEXT.__unwind_info: 0x6ba0
+  __TEXT.__eh_frame: 0xe5e0
+  __DATA_CONST.__auth_got: 0x12d0
+  __DATA_CONST.__got: 0x1220
+  __DATA_CONST.__auth_ptr: 0x768
+  __DATA_CONST.__const: 0xdf90
   __DATA_CONST.__cfstring: 0x4a00
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x1fa50
-  __DATA.__objc_selrefs: 0x5040
+  __DATA.__objc_selrefs: 0x5048
   __DATA.__objc_ivar: 0x81c
   __DATA.__objc_data: 0x40d0
-  __DATA.__data: 0x79e0
-  __DATA.__bss: 0x4830
+  __DATA.__data: 0x7930
+  __DATA.__bss: 0x43b0
   __DATA.__common: 0x118
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7672
+  Functions: 7609
   Symbols:   1302
-  CStrings:  1434
+  CStrings:  1431
 
Symbols:
+ _$s15ScreenTimeSwift19STUserNotificationsV16NotificationTypeO10askRequestyAESS_SSSo8NSNumberCSgSStcAEmFWC
+ _$sSo9ACAccountC12FamilyCircleE7appleIDSSSgvg
- _$s15ScreenTimeSwift19STUserNotificationsV16NotificationTypeO10askRequestyAESS_SSSo8NSNumberCSStcAEmFWC
- _BGSystemTaskSchedulerErrorDomain
CStrings:
+ "_processIncomingV2(messageContent:messageContentType:destination:dataStore:familyCircle:)"
+ "_send(payload:toDestination:familyCircle:queueIdentifier:)"
+ "_sendAcknowledgementMessage(for:toIDSDestination:familyCircle:)"
+ "_sendCheckinResponseOnV2(using:to:familyCircle:)"
+ "_sendV2(message:destinations:familyCircle:)"
+ "_sendV2(messageData:options:destinations:familyCircle:)"
- "configurationChanges(for:dataStore:)"
- "createCheckinResponsePayload(forFamily:using:)"
- "processIncomingV2(messageContent:messageContentType:destination:)"
- "send(payload:toDestination:queueIdentifier:)"
- "sendAcknowledgementMessage(for:toIDSDestination:)"
- "sendCheckinResponseOnV2(using:to:)"
- "sendSettings(to:using:)"
- "sendV2(message:destinations:)"
- "sendV2(messageData:options:destinations:)"

```
