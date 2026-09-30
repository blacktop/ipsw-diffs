## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-57.0.4.0.0
-  __TEXT.__text: 0x6544
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x340
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0x912
-  __TEXT.__oslogstring: 0x1870
-  __TEXT.__unwind_info: 0x360
+64.0.18.0.0
+  __TEXT.__text: 0x6950
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0x34c
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0xae8
+  __TEXT.__cstring: 0x984
+  __TEXT.__oslogstring: 0x1a8c
+  __TEXT.__unwind_info: 0x368
   __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methname: 0xbd2
+  __TEXT.__objc_methname: 0xbf8
   __TEXT.__objc_methtype: 0x108
-  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_stubs: 0xa80
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x370
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x2d8
   __DATA.__objc_ivar: 0x24
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9657A1A1-E03F-3C1D-B879-584D320CAB8A
-  Functions: 94
-  Symbols:   469
-  CStrings:  365
+  UUID: 80F4DE53-B9FF-3244-BF84-A76E71B52755
+  Functions: 95
+  Symbols:   476
+  CStrings:  381
 
Symbols:
+ -[SafetyAlerts onUserTappedOnUiWithInfo:]
+ _objc_msgSend$doubleValue
+ _objc_retain_x23
+ _objc_retain_x24
+ _xpc_dictionary_set_double
Functions:
~ -[SafetyAlerts getIsSafetyAlertsEnabledFromReply:] : 608 -> 604
~ -[SafetyAlerts onSignificantEventDetected:] : 308 -> 304
+ -[SafetyAlerts onUserTappedOnUiWithInfo:]
CStrings:
+ "UID"
+ "doubleValue"
+ "onUserTappedOnUiWithInfo:"
+ "saUiUserTap"
+ "snapshotSeconds"
+ "userSnapshotCompleteTsSeconds"
+ "userTappedSeconds"
+ "userTappedTsSeconds"
+ "userTappedUid"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,#warning,onUserTappedOnUiWithInfo,cantCreateMessage\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,#warning,onUserTappedOnUiWithInfo,emptyInfo\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,#warning,onUserTappedOnUiWithInfo,missingParams\", \"uid\":%{private, location:escape_only}@, \"userTappedTsSeconds\":%{private, location:escape_only}@, \"snapShotCompleteTsSeconds\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,onUserTappedOnUiWithInfo\", \"info\":%{private, location:escape_only}@}"

```
