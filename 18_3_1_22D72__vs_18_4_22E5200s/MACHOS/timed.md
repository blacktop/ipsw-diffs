## timed

> `/usr/libexec/timed`

```diff

-334.0.2.0.0
-  __TEXT.__text: 0x18ef8
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x2740
-  __TEXT.__objc_methlist: 0xc08
+334.0.4.0.0
+  __TEXT.__text: 0x186e8
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_methlist: 0xf04
   __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x2050
+  __TEXT.__objc_methname: 0x24ff
+  __TEXT.__cstring: 0x1f59
+  __TEXT.__objc_classname: 0x14a
+  __TEXT.__objc_methtype: 0x54f
   __TEXT.__oslogstring: 0x2ad6
-  __TEXT.__objc_methname: 0x24d0
-  __TEXT.__objc_classname: 0x13d
-  __TEXT.__objc_methtype: 0x53f
-  __TEXT.__gcc_except_tab: 0xd8
+  __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xdb0
-  __DATA_CONST.__cfstring: 0x2c00
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0xdb8
+  __DATA_CONST.__cfstring: 0x29c0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2510
-  __DATA.__objc_selrefs: 0xaa0
-  __DATA.__objc_ivar: 0x184
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0x2130
+  __DATA.__objc_selrefs: 0xb20
+  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x310
   __DATA.__bss: 0x140
   __DATA.__common: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 548
-  Symbols:   259
-  CStrings:  1326
+  Functions: 599
+  Symbols:   251
+  CStrings:  1313
 
Symbols:
+ _memcpy
- _CFUserNotificationCreate
- _CFUserNotificationReceiveResponse
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSURLComponents
- _OBJC_CLASS_$_NSURLQueryItem
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
CStrings:
+ "334.0.4"
+ "@\"TMTapToRadar\""
+ "TB,GhasAlertedForFutureTime"
+ "TMHasAlertedForFutureTime"
+ "TMTapToRadar"
+ "_ttrQueue"
+ "com.apple.timed.tapToRadarQ"
+ "hasAlertedForFutureTime"
+ "hasPrefix:"
+ "islandTTR"
+ "launchTTRwithContext:"
+ "radarHelper"
+ "setHasAlertedForFutureTime:"
+ "ttrPromptWithText:fields:"
- "1.0"
- "1332142"
- "334.0.2"
- "Classification"
- "ComponentID"
- "ComponentName"
- "ComponentVersion"
- "CoreTime | All"
- "Description"
- "Dismiss"
- "File a radar"
- "I Didn't Try"
- "Island"
- "Other Bug"
- "Reproducibility"
- "Title"
- "URL"
- "You have encountered a rare issue that is currently being investigated"
- "array"
- "defaultWorkspace"
- "initWithString:"
- "openURL:configuration:completionHandler:"
- "queryItemWithName:value:"
- "setQueryItems:"
- "tap-to-radar://new"
- "timed is islanded"
- "timed problem detected"

```
