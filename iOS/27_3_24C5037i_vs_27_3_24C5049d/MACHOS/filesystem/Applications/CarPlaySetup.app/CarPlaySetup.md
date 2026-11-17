## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-808.6.0.0.0
-  __TEXT.__text: 0x84d0
+808.9.1.0.0
+  __TEXT.__text: 0x8518
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x13c0
+  __TEXT.__objc_stubs: 0x13a0
   __TEXT.__objc_methlist: 0xcb0
   __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x2e1b
+  __TEXT.__objc_methname: 0x2e5f
   __TEXT.__cstring: 0x1ef
-  __TEXT.__oslogstring: 0xdf5
+  __TEXT.__oslogstring: 0xe0a
   __TEXT.__objc_classname: 0x1af
-  __TEXT.__objc_methtype: 0x11b9
+  __TEXT.__objc_methtype: 0x1218
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__unwind_info: 0x368
   __DATA_CONST.__const: 0x4a0

   - /usr/lib/libobjc.A.dylib
   Functions: 204
   Symbols:   129
-  CStrings:  583
+  CStrings:  585
 
Symbols:
+ _OBJC_CLASS_$_CARSetupMessageProcessingViewController
- _OBJC_CLASS_$_CARSetupVehicleMessageAIProcessingAlert
Functions:
~ sub_1000036f0 : 196 -> 204
~ sub_1000037b4 -> sub_1000037bc : 308 -> 324
~ sub_100007704 -> sub_10000771c : 220 -> 236
~ sub_100007894 -> sub_1000078bc : 188 -> 220
CStrings:
+ "initWithVehicleBrand:needsAIConsent:responseHandler:"
+ "initWithVehicleBrand:responseHandler:"
+ "present vehicle handles messaging with AI prompt"
+ "presentVehicleHandlesMessagingPromptForVehicleBrand:needsAIConsent:responseHandler:"
+ "presentVehicleHandlesMessagingWithAIPromptForVehicleBrand:responseHandler:"
+ "promptDirector:wantsToPresentVehicleHandlesMessagingPromptForVehicleBrand:needsAIConsent:responseHandler:"
+ "promptDirector:wantsToPresentVehicleHandlesMessagingWithAIPromptForVehicleBrand:responseHandler:"
+ "v36@0:8@\"NSString\"16B24@?<v@?B>28"
+ "v44@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24B32@?<v@?B>36"
+ "vehicle handles messaging with AI prompt answered: %{public}@"
+ "vehicle handles messaging with AI prompt received response: %{public}@"
- "alertWithResponseHandler:"
- "initWithVehicleName:responseHandler:"
- "present vehicle message processing prompt"
- "presentVehicleHandlesMessagingPromptForVehicleName:responseHandler:"
- "presentVehicleMessageAIProcessingPromptForVehicleName:responseHandler:"
- "promptDirector:wantsToPresentVehicleHandlesMessagingPromptForVehicleName:responseHandler:"
- "promptDirector:wantsToPresentVehicleMessageAIProcessingPromptForVehicleName:responseHandler:"
- "vehicle message processing prompt answered: %{public}@"
- "vehicle message processing prompt received response: %{public}@"
```
