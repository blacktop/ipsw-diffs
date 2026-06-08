## libenergytrace.dylib

> `/usr/lib/libenergytrace.dylib`

```diff

 23.0.0.0.0
-  __TEXT.__text: 0x694
-  __TEXT.__auth_stubs: 0x70
+  __TEXT.__text: 0x5d8
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x19f
   __TEXT.__cstring: 0x57
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__got: 0x8
+  __TEXT.__unwind_info: 0x80
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x38
   __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__bss: 0x48
   - /usr/lib/libSystem.B.dylib
-  UUID: 75320403-56D3-31FE-BD5B-04B32719AC17
+  UUID: 3C822BE3-58EF-3680-9554-40A957348CC7
   Functions: 11
-  Symbols:   28
+  Symbols:   26
   CStrings:  12
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ __get_signpost_params.cold.1 -> _entr_act_modify : 20 -> 248
~ _entr_act_begin -> __get_signpost_params : 296 -> 160
~ __get_signpost_params -> _entr_act_begin : 160 -> 252
~ _entr_act_end : 296 -> 252
~ ____get_signpost_params_block_invoke -> __get_signpost_params.cold.1 : 124 -> 20
~ _entr_act_modify -> _entr_act_set : 292 -> 8
~ _entr_shouldtrace -> ____get_signpost_params_block_invoke : 116 -> 124
~ _entr_act_set -> _entr_shouldtrace : 8 -> 104
~ _entr_act_associate : 320 -> 276

```
