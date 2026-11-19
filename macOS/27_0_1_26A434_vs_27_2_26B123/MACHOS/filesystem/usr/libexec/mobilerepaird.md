## mobilerepaird

> `/usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-1307.1.2.0.0
-  __TEXT.__text: 0xaf24
+1307.40.66.0.0
+  __TEXT.__text: 0xc1c4
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x904
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__objc_methname: 0x1de6
-  __TEXT.__cstring: 0x1b02
-  __TEXT.__oslogstring: 0x76c
-  __TEXT.__objc_classname: 0x162
-  __TEXT.__objc_methtype: 0x364
-  __TEXT.__info_plist: 0x521
-  __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x1740
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__objc_stubs: 0x1ae0
+  __TEXT.__objc_methlist: 0x974
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x3b8
+  __TEXT.__objc_methname: 0x1f78
+  __TEXT.__cstring: 0x1f3c
+  __TEXT.__oslogstring: 0x931
+  __TEXT.__objc_classname: 0x176
+  __TEXT.__objc_methtype: 0x394
+  __TEXT.__info_plist: 0x523
+  __TEXT.__unwind_info: 0x2f8
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__cfstring: 0x1900
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x280
-  __DATA.__objc_const: 0x10d8
-  __DATA.__objc_selrefs: 0x818
+  __DATA_CONST.__got: 0x288
+  __DATA.__objc_const: 0x1168
+  __DATA.__objc_selrefs: 0x870
   __DATA.__objc_ivar: 0xb0
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x190
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 218
+  Functions: 238
   Symbols:   155
-  CStrings:  654
+  CStrings:  696
 
CStrings:
+ "+[MRFinishRepairAlert alertShownKeyForFollowUpClientID:]"
+ "+[MRFinishRepairAlert composedMessageWithFormat:finishRepairMessage:]"
+ "+[MRFinishRepairAlert shouldPresentAlertWithTitle:message:displayFollowup:alreadyShown:]"
+ "-[MRBaseComponentHandler popUpFinishRepairAlert]"
+ "-[MRBaseComponentHandler sendFinishRepairAlertShownAnalytics]_block_invoke"
+ "-[MRBaseComponentHandler sendFinishRepairNotificationShownAnalytics]_block_invoke"
+ "@32@0:8@16@24"
+ "B40@0:8@16@24B32B36"
+ "B60@0:8@16@24@32@40B48Q52"
+ "CoreAnalyticsEvent: ModuleType(%@), EventType(FinishRepairAlertShown)"
+ "CoreAnalyticsEvent: ModuleType(%@), EventType(FinishRepairNotificationShown)"
+ "FINISH_LATER"
+ "FINISH_REPAIR_ALERT_MESSAGE"
+ "FINISH_REPAIR_ALERT_SHOWN"
+ "FINISH_REPAIR_NOTIFICATION_MESSAGE"
+ "FinishRepairAlertShown"
+ "FinishRepairNotificationShown"
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
+ "componentsSeparatedByString:"
+ "composedMessageWithFormat:finishRepairMessage:"
+ "length"
+ "partsAndServiceHistoryURL"
+ "popUpFinishRepairAlert"
+ "popUpNotificationNowWithMessage:title:openSensitiveURL:componentName:legacyPopup:buttonStyle:"
+ "sendFinishRepairAlertShownAnalytics"
+ "sendFinishRepairNotificationShownAnalytics"
+ "shouldPresentAlertWithTitle:message:displayFollowup:alreadyShown:"
+ "stringByReplacingOccurrencesOfString:withString:"
- "popUpNotificationNowWithMessage:title:openSensitiveURL:componentName:legacyPopup:"
- "v52@0:8@16@24@32@40B48"
```
