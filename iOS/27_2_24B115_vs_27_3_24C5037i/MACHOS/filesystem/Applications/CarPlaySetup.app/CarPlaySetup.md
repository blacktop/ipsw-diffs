## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-807.4.1.0.0
-  __TEXT.__text: 0x7bd8
+808.6.0.0.0
+  __TEXT.__text: 0x84d0
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x1320
-  __TEXT.__objc_methlist: 0xc40
-  __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x2c8b
-  __TEXT.__cstring: 0x1e6
-  __TEXT.__oslogstring: 0xccc
+  __TEXT.__objc_stubs: 0x13c0
+  __TEXT.__objc_methlist: 0xcb0
+  __TEXT.__const: 0x70
+  __TEXT.__objc_methname: 0x2e1b
+  __TEXT.__cstring: 0x1ef
+  __TEXT.__oslogstring: 0xdf5
   __TEXT.__objc_classname: 0x1af
   __TEXT.__objc_methtype: 0x11b9
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__unwind_info: 0x338
-  __DATA_CONST.__const: 0x478
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x188
-  __DATA.__objc_const: 0x1888
-  __DATA.__objc_selrefs: 0x8d0
+  __DATA_CONST.__got: 0x198
+  __DATA.__objc_const: 0x18a8
+  __DATA.__objc_selrefs: 0x908
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 193
-  Symbols:   127
-  CStrings:  569
+  Functions: 204
+  Symbols:   129
+  CStrings:  583
 
Symbols:
+ _OBJC_CLASS_$_CARSetupVehicleHandlesMessagingViewController
+ _OBJC_CLASS_$_CARSetupVehicleMessageAIProcessingAlert
CStrings:
+ "_presentAlert:"
+ "alertWithResponseHandler:"
+ "initWithVehicleName:responseHandler:"
+ "onboarding prompt confirmed with response: %lu"
+ "present vehicle handles messaging prompt"
+ "present vehicle message processing prompt"
+ "presentVehicleHandlesMessagingPromptForVehicleName:responseHandler:"
+ "presentVehicleMessageAIProcessingPromptForVehicleName:responseHandler:"
+ "promptDirector:wantsToPresentVehicleHandlesMessagingPromptForVehicleName:responseHandler:"
+ "promptDirector:wantsToPresentVehicleMessageAIProcessingPromptForVehicleName:responseHandler:"
+ "v16@?0Q8"
+ "v48@0:8@\"NSString\"16Q24@\"NSArray\"32@?<v@?Q>40"
+ "v56@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24Q32@\"NSArray\"40@?<v@?Q>48"
+ "vehicle handles messaging prompt answered: %{public}@"
+ "vehicle handles messaging prompt received response: %{public}@"
+ "vehicle message processing prompt answered: %{public}@"
+ "vehicle message processing prompt received response: %{public}@"
- "onboarding prompt confirmed, proceeding to car key setup: %{public}@"
- "v48@0:8@\"NSString\"16Q24@\"NSArray\"32@?<v@?B>40"
- "v56@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24Q32@\"NSArray\"40@?<v@?B>48"
```
