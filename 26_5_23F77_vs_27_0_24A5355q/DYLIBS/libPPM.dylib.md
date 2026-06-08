## libPPM.dylib

> `/usr/lib/libPPM.dylib`

```diff

-1035.100.47.0.0
-  __TEXT.__text: 0x11cc
-  __TEXT.__auth_stubs: 0x360
+1177.0.0.502.4
+  __TEXT.__text: 0x11b0
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x563
+  __TEXT.__cstring: 0x565
   __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x29
-  __TEXT.__objc_methname: 0x3d5
-  __TEXT.__objc_methtype: 0x19c
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x260
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0623A1D-3211-36DD-AD37-5CA6097F8CDD
+  UUID: D18B4F05-B86A-3721-8A00-785A8EAE9004
   Functions: 32
-  Symbols:   177
-  CStrings:  143
+  Symbols:   180
+  CStrings:  72
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[PPMClient initWithClientIdentifier:] : 108 -> 116
~ +[PPMClient sharedInstanceWithClientRepresentation:options:error:] : 200 -> 188
~ ___66+[PPMClient sharedInstanceWithClientRepresentation:options:error:]_block_invoke : 172 -> 168
~ -[PPMClient getClientNumber:] : 128 -> 124
~ _budgetNotificationCallback : 360 -> 344
~ -[PPMClient admissionCheckWithLevel:options:error:handler:] : 336 -> 332
~ -[PPMClient activityStoppedWithLevel:options:error:] : 208 -> 204
~ -[PPMClient activityStartedWithLevel:options:error:] : 208 -> 204
~ -[PPMClient pushTelemetryToPPM:error:] : 968 -> 980
CStrings:
- ".cxx_destruct"
- "@\"NSString\""
- "@\"PPMClientUserClientInterface\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24^@32"
- "B"
- "B16@0:8"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B32@0:8^@16@?24"
- "B32@0:8^{__CFDictionary=}16^@24"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24^@32@?40"
- "I"
- "I16@0:8"
- "PPMClient"
- "PPMClientUserClientInterface"
- "T@\"NSString\",&,Videntifier"
- "T@\"PPMClientUserClientInterface\",&,VuserClient"
- "TB,R,V_attribute"
- "TI,R,V_connect"
- "TI,Vconnect"
- "TI,Vversion"
- "_attribute"
- "_connect"
- "activityStartedWithLevel:options:error:"
- "activityStoppedWithLevel:options:error:"
- "admissionCheckOfValuePPM:clientNumber:level:result:"
- "admissionCheckWithLevel:options:error:handler:"
- "attribute"
- "connect"
- "dictionary"
- "endInteraction:"
- "getClientNumber:"
- "i24@0:8@16"
- "i24@0:8I16I20"
- "i24@0:8I16i20"
- "i28@0:8I16I20I24"
- "i28@0:8I16I20i24"
- "i28@0:8I16^{UserClientTelemetryDict=II[20[128c]][20i]}20"
- "i36@0:8I16I20i24^I28"
- "identifier"
- "init"
- "initWithClient:error:"
- "initWithClientIdentifier:"
- "initWithLongLong:"
- "intValue"
- "isEqualToString:"
- "openPPMUserClient:clientNumber:"
- "pushTelemetry:userDictRef:"
- "pushTelemetryToPPM:error:"
- "registerForNotificationsWithError:handler:"
- "setBudget:clientNumber:value:"
- "setConnect:"
- "setDebugFlag:value:"
- "setIdentifier:"
- "setObject:forKey:"
- "setUserClient:"
- "setVersion:"
- "setupIOKitUserClientWith:error:"
- "sharedInstanceWithClientRepresentation:error:"
- "sharedInstanceWithClientRepresentation:options:error:"
- "startActivity:clientNumber:level:"
- "stopActivity:clientNumber:level:"
- "userClient"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "version"

```
