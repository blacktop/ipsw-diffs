## com.apple.driver.AppleProxDriver

> `com.apple.driver.AppleProxDriver`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`

```diff

-58.0.0.0.0
+59.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x8ca
-  __TEXT.__os_log: 0x79f
-  __TEXT_EXEC.__text: 0xa650
+  __TEXT.__cstring: 0x8f1
+  __TEXT.__os_log: 0x7b8
+  __TEXT_EXEC.__text: 0xa818
   __TEXT_EXEC.__auth_stubs: 0x310
   __DATA.__data: 0xe0
   __DATA.__common: 0xd8

   __DATA_CONST.__const: 0x2138
   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x88
   Functions: 196
   Symbols:   0
-  CStrings:  165
+  CStrings:  168
 
Functions:
~ sub_fffffe0009470d5c -> sub_fffffe0009489ddc : 56 -> 60
~ sub_fffffe0009470d94 -> sub_fffffe0009489e18 : 56 -> 60
~ sub_fffffe0009470dcc -> sub_fffffe0009489e54 : 120 -> 160
~ sub_fffffe0009470e44 -> sub_fffffe0009489ef4 : 120 -> 160
~ sub_fffffe0009470f70 -> sub_fffffe000948a048 : 108 -> 112
~ sub_fffffe0009470ff0 -> sub_fffffe000948a0cc : 92 -> 96
~ sub_fffffe000947104c -> sub_fffffe000948a12c : 92 -> 96
~ sub_fffffe00094718e8 -> sub_fffffe000948a9cc : 628 -> 716
~ sub_fffffe00094762ac -> sub_fffffe000948f3e8 : 300 -> 580
~ sub_fffffe00094763d8 -> sub_fffffe000948f62c : 776 -> 764
CStrings:
+ "12111112122212121111111211111122111112121"
+ "AtlantisProcessingPlan"
+ "ProcessingPlan"
+ "Using processing plan %s"
- "1211111212221212111111121111112211111212"
```
