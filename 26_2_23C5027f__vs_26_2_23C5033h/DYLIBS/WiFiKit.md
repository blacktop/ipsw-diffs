## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-1163.1.0.0.0
-  __TEXT.__text: 0x9be5c
+1163.3.0.0.0
+  __TEXT.__text: 0x9bd9c
   __TEXT.__auth_stubs: 0x1610
   __TEXT.__objc_methlist: 0x96d8
   __TEXT.__const: 0x283
-  __TEXT.__oslogstring: 0xb0f1
+  __TEXT.__oslogstring: 0xb0ae
   __TEXT.__cstring: 0xb599
   __TEXT.__gcc_except_tab: 0x2c74
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__unwind_info: 0x1ca0
   __TEXT.__objc_classname: 0xe54
-  __TEXT.__objc_methname: 0x1599e
+  __TEXT.__objc_methname: 0x159b2
   __TEXT.__objc_methtype: 0x2fd0
-  __TEXT.__objc_stubs: 0xe780
+  __TEXT.__objc_stubs: 0xe760
   __DATA_CONST.__got: 0xbf8
   __DATA_CONST.__const: 0x2638
   __DATA_CONST.__objc_classlist: 0x348

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8ED29805-47BC-3EAC-A9F7-79F5F2B78E25
+  UUID: 87F915B7-EF8F-3779-9156-5BD68D58CD39
   Functions: 3423
-  Symbols:   12071
-  CStrings:  7702
+  Symbols:   12070
+  CStrings:  7701
 
Symbols:
+ -[WFControlCenterStateMonitor performActionFrom:withCSLSConnectionState:completion:]
- -[WFControlCenterStateMonitor performActionFrom:withCompletion:]
- _objc_msgSend$setPresenter:
Functions:
~ -[WFControlCenterStateMonitor performActionFrom:withCompletion:] -> -[WFControlCenterStateMonitor performActionFrom:withCSLSConnectionState:completion:] : 208 -> 4
~ -[WFClient _unscheduleCallbacksWithManager:] : 160 -> 172
CStrings:
+ "performActionFrom:withCSLSConnectionState:completion:"
- "initializing WFControlCenterStateMonitor with presenter for alerts"
- "performActionFrom:withCompletion:"

```
