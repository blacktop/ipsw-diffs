## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-1307.40.64.0.0
-  __TEXT.__text: 0x1e050
-  __TEXT.__objc_methlist: 0x174c
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x3e5a
-  __TEXT.__oslogstring: 0xda0
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__unwind_info: 0x6b8
+1307.40.66.0.0
+  __TEXT.__text: 0x1f3b4
+  __TEXT.__objc_methlist: 0x17c4
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x4240
+  __TEXT.__oslogstring: 0xf65
+  __TEXT.__gcc_except_tab: 0x3d8
+  __TEXT.__unwind_info: 0x6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x450
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdd0
+  __DATA_CONST.__objc_selrefs: 0xe28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x4ac0
-  __AUTH_CONST.__objc_const: 0x3ed8
+  __AUTH_CONST.__cfstring: 0x4cc0
+  __AUTH_CONST.__objc_const: 0x3f98
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x15c
+  __AUTH.__objc_data: 0x1950
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 520
+  Functions: 540
   Symbols:   255
-  CStrings:  739
+  CStrings:  767
 
CStrings:
+ "+[MRFinishRepairAlert alertShownKeyForFollowUpClientID:]"
+ "+[MRFinishRepairAlert composedMessageWithFormat:finishRepairMessage:]"
+ "+[MRFinishRepairAlert shouldPresentAlertWithTitle:message:displayFollowup:alreadyShown:]"
+ "-[MRBaseComponentHandler popUpFinishRepairAlert]"
+ "-[MRBaseComponentHandler sendFinishRepairAlertShownAnalytics]_block_invoke"
+ "CoreAnalyticsEvent: ModuleType(%@), EventType(FinishRepairAlertShown)"
+ "FINISH_CAMERA_CONTROL_REPAIR_TITLE"
+ "FINISH_CG_REPAIR_TITLE"
+ "FINISH_ECL_REPAIR_TITLE"
+ "FINISH_LATER"
+ "FINISH_REPAIR_ALERT_MESSAGE"
+ "FINISH_REPAIR_ALERT_SHOWN"
+ "FINISH_REPAIR_NOTIFICATION_MESSAGE"
+ "FINISH_VB_REPAIR_TITLE"
+ "FinishRepairAlertShown"
+ "No response for %@ notification, not acting on it ERROR:%d"
+ "[%s] Finish Repair alert already shown for this repair, skipping"
+ "[%s] Finish Repair alert never reached the screen, re-arming it"
+ "[%s] could not build the Finish Repair alert body, skipping"
+ "[%s] could not build the Finish Repair notification body, falling back to %@"
+ "[%s] follow-up UI disabled, skipping Finish Repair alert"
+ "[%s] message format unusable, falling back to the Finish Repair message: %{public}@"
+ "[%s] no Finish Repair message to build the body from"
+ "[%s] no Finish Repair title or message, skipping Finish Repair alert"
+ "[%s] no follow-up client ID, cannot track the Finish Repair alert"
+ "[%s] popups disabled, skipping Finish Repair alert"
+ "[%s] presenting Finish Repair alert outside the handler lock"
+ "[%s] presenting one-time Finish Repair alert"
```
