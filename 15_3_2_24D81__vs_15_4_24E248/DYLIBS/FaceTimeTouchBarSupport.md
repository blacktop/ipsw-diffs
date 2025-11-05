## FaceTimeTouchBarSupport

> `/System/Library/PrivateFrameworks/FaceTimeTouchBarSupport.framework/Versions/A/FaceTimeTouchBarSupport`

```diff

-2975.400.141.0.0
-  __TEXT.__text: 0x11280
+2975.500.181.1.1
+  __TEXT.__text: 0x1119c
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0xcec
+  __TEXT.__objc_methlist: 0xfc4
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x13e4
   __TEXT.__oslogstring: 0x205
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x348
   __TEXT.__objc_classname: 0x158
-  __TEXT.__objc_methname: 0x3a98
-  __TEXT.__objc_methtype: 0x746
-  __TEXT.__objc_stubs: 0x3420
+  __TEXT.__objc_methname: 0x3b3c
+  __TEXT.__objc_methtype: 0x757
+  __TEXT.__objc_stubs: 0x3480
   __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf58
+  __DATA_CONST.__objc_selrefs: 0x1028
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x18e8
+  __AUTH_CONST.__objc_const: 0x13f8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D68971FB-86FE-35EB-A5EE-F79D8B523532
-  Functions: 311
-  Symbols:   1090
-  CStrings:  1144
+  UUID: B698F433-711D-35E3-AFA3-535B4F536F0A
+  Functions: 314
+  Symbols:   1101
+  CStrings:  1148
 
Symbols:
+ +[DFRController contactStore].cold.1
+ +[DFRController sharedInstance].cold.1
+ +[FTTelephonyCapabilityManager sharedInstance].cold.1
+ +[iMessageHelper sharedInstance].cold.1
+ -[DFRController updateControlsForAddPersonButton:]
+ -[DFRController updateControlsForAudioVideoHasOngoingCall:audioAndVideoButtonAvailable:]
+ -[DFRController updateControlsForInviteWithMessagesButton:]
+ -[DFRController updateControlsWithViewModel:hasOngoingCall:]
+ FaceTimeOSLog.cold.1
+ _objc_msgSend$updateControlsForAddPersonButton:
+ _objc_msgSend$updateControlsForAudioVideoHasOngoingCall:audioAndVideoButtonAvailable:
+ _objc_msgSend$updateControlsForInviteWithMessagesButton:
- -[DFRController updateControlsWithViewModel:]
CStrings:
+ "updateControlsForAddPersonButton:"
+ "updateControlsForAudioVideoHasOngoingCall:audioAndVideoButtonAvailable:"
+ "updateControlsForInviteWithMessagesButton:"
+ "updateControlsWithViewModel:hasOngoingCall:"
+ "v24@0:8B16B20"
+ "v28@0:8@\"DFRViewModel\"16B24"
- "updateControlsWithViewModel:"
- "v24@0:8@\"DFRViewModel\"16"

```
