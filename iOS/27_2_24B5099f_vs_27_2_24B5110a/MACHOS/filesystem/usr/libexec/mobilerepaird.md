## mobilerepaird

> `usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-1307.40.64.0.0
-  __TEXT.__text: 0x1f2ec
+1307.40.66.0.0
+  __TEXT.__text: 0x201cc
   __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x1a14
+  __TEXT.__objc_stubs: 0x3b40
+  __TEXT.__objc_methlist: 0x1a74
   __TEXT.__const: 0x172
-  __TEXT.__gcc_except_tab: 0xa08
-  __TEXT.__objc_methname: 0x463e
-  __TEXT.__cstring: 0x40d0
-  __TEXT.__oslogstring: 0x3461
-  __TEXT.__objc_classname: 0x59f
-  __TEXT.__objc_methtype: 0xe41
+  __TEXT.__gcc_except_tab: 0xa10
+  __TEXT.__objc_methname: 0x4781
+  __TEXT.__cstring: 0x444d
+  __TEXT.__oslogstring: 0x3626
+  __TEXT.__objc_classname: 0x5af
+  __TEXT.__objc_methtype: 0xe63
   __TEXT.__ustring: 0x12a
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__unwind_info: 0xa18
   __DATA_CONST.__const: 0xdb0
-  __DATA_CONST.__cfstring: 0x4060
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__cfstring: 0x41e0
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x4e8
-  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x3098
-  __DATA.__objc_selrefs: 0x11a0
+  __DATA.__objc_const: 0x3128
+  __DATA.__objc_selrefs: 0x11e0
   __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0xe70
+  __DATA.__objc_data: 0xec0
   __DATA.__data: 0x4c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 668
+  Functions: 685
   Symbols:   299
-  CStrings:  1664
+  CStrings:  1699
 
CStrings:
+ "+[MRFinishRepairAlert alertShownKeyForFollowUpClientID:]"
+ "+[MRFinishRepairAlert composedMessageWithFormat:finishRepairMessage:]"
+ "+[MRFinishRepairAlert shouldPresentAlertWithTitle:message:displayFollowup:alreadyShown:]"
+ "-[MRBaseComponentHandler popUpFinishRepairAlert]"
+ "-[MRBaseComponentHandler sendFinishRepairAlertShownAnalytics]_block_invoke"
+ "B40@0:8@16@24B32B36"
+ "B60@0:8@16@24@32@40B48Q52"
+ "CoreAnalyticsEvent: ModuleType(%@), EventType(FinishRepairAlertShown)"
+ "FINISH_LATER"
+ "FINISH_REPAIR_ALERT_MESSAGE"
+ "FINISH_REPAIR_ALERT_SHOWN"
+ "FINISH_REPAIR_NOTIFICATION_MESSAGE"
+ "FinishRepairAlertShown"
+ "MRFinishRepairAlert"
+ "No response for %@ notification, not acting on it ERROR:%d"
+ "Q24@0:8Q16"
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
+ "actionResponseForButtonStyle:"
+ "alertShownKeyForFollowUpClientID:"
+ "composedMessageWithFormat:finishRepairMessage:"
+ "partsAndServiceHistoryURL"
+ "popUpFinishRepairAlert"
+ "popUpNotificationNowWithMessage:title:openSensitiveURL:componentName:legacyPopup:buttonStyle:"
+ "sendFinishRepairAlertShownAnalytics"
+ "shouldPresentAlertWithTitle:message:displayFollowup:alreadyShown:"
+ "stringByReplacingOccurrencesOfString:withString:"
- "popUpNotificationNowWithMessage:title:openSensitiveURL:componentName:legacyPopup:"
- "v52@0:8@16@24@32@40B48"
```
