## Accessibility

> `/System/Library/Assistant/Plugins/Accessibility.assistantBundle/Accessibility`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x810
-  __TEXT.__auth_stubs: 0xe0
+3229.1.6.0.0
+  __TEXT.__text: 0x7a4
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x18

   __TEXT.__objc_methtype: 0x1a5
   __TEXT.__oslogstring: 0x6f
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x7b0
   __DATA.__objc_selrefs: 0x120
   __DATA.__objc_data: 0x230

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81C76736-98C9-3A69-BA5E-8C261698502B
+  UUID: 819E77D5-CA76-30E4-B155-C719441FFCEB
   Functions: 16
   Symbols:   60
   CStrings:  75
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_b28 : 184 -> 176
~ sub_be8 -> sub_be0 : 184 -> 176
~ sub_ca8 -> sub_c98 : 184 -> 176
~ sub_d68 -> sub_d50 : 188 -> 180
~ sub_e2c -> sub_e0c : 184 -> 176
~ _AXAssistantSendMissingSettingFailure : 148 -> 144
~ _AXAssistantCallCompletionWithSpeakThisError : 564 -> 516
~ sub_11b4 -> sub_1158 : 188 -> 180
~ sub_1278 -> sub_1214 : 184 -> 176

```
