## Accessibility

> `/System/Library/Assistant/Plugins/Accessibility.assistantBundle/Accessibility`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x7d0
-  __TEXT.__auth_stubs: 0x100
+3191.19.0.0.0
+  __TEXT.__text: 0x810
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x18

   __TEXT.__objc_methtype: 0x1a5
   __TEXT.__oslogstring: 0x6f
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x38

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBBF3439-2D07-3534-8552-749C3D58A647
+  UUID: 9DAF31DE-01DE-3BE7-A18E-D46E5392D68D
   Functions: 16
-  Symbols:   62
+  Symbols:   60
   CStrings:  75
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
Functions:
~ sub_b28 : 176 -> 184
~ sub_be0 -> sub_be8 : 176 -> 184
~ sub_c98 -> sub_ca8 : 176 -> 184
~ sub_d50 -> sub_d68 : 180 -> 188
~ sub_e0c -> sub_e2c : 176 -> 184
~ _AXAssistantSendMissingSettingFailure : 144 -> 148
~ _AXAssistantCallCompletionWithSpeakThisError : 560 -> 564
~ sub_1184 -> sub_11b4 : 180 -> 188
~ sub_1240 -> sub_1278 : 176 -> 184

```
