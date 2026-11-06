## BackgroundTaskManagement

> `/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement`

```diff

-371.0.0.0.0
-  __TEXT.__text: 0x1fec0
+371.1.4.0.0
+  __TEXT.__text: 0x1fff4
   __TEXT.__objc_methlist: 0x1994
   __TEXT.__const: 0xe8
   __TEXT.__oslogstring: 0x1ae5
-  __TEXT.__cstring: 0x1b51
-  __TEXT.__gcc_except_tab: 0xc1c
+  __TEXT.__cstring: 0x1b73
+  __TEXT.__gcc_except_tab: 0xc3c
   __TEXT.__unwind_info: 0xa78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__cfstring: 0x1480
   __AUTH_CONST.__objc_const: 0x2090
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 864
   Symbols:   1585
-  CStrings:  438
+  CStrings:  440
 
Functions:
~ _BTMItemTypeBaseDescription : 436 -> 472
~ _BTMItemIdentifierForURLAndType : 500 -> 532
~ _ValidateItemType : 144 -> 172
~ -[BTMItem setExecutablePathFromLauncherTargetWithConfig:] : 1556 -> 1584
~ _BTMItemTypeValidateRegistrationParameters : 400 -> 440
~ _ComposedItemIdentifier : 156 -> 160
~ _BTMItemIdentifierWithRegistrationInfo : 764 -> 804
~ -[BTMManager getItemWithIdentifier:uid:error:] : 644 -> 716
~ -[BTMManager fetchItemWithUUID:uid:error:] : 696 -> 724
CStrings:
+ "system xpcservice"
+ "user xpcservice"
```
