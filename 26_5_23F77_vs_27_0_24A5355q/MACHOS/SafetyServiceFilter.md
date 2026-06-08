## SafetyServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter`

```diff

-152.0.2.0.0
-  __TEXT.__text: 0xc30
-  __TEXT.__auth_stubs: 0x230
+163.0.0.0.0
+  __TEXT.__text: 0xb28
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__gcc_except_tab: 0x18
   __TEXT.__oslogstring: 0x171
-  __TEXT.__cstring: 0xbe
+  __TEXT.__cstring: 0xc1
   __TEXT.__objc_methname: 0x33a
-  __TEXT.__objc_classname: 0x31
+  __TEXT.__objc_classname: 0x2e
   __TEXT.__objc_methtype: 0x349
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x308
   __DATA.__objc_selrefs: 0x158
   __DATA.__objc_ivar: 0x14

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEE852A8-689A-3E41-A8CF-AFBBB05159A0
+  UUID: B7F5909B-2844-36DC-A1E8-3F9599D705B3
   Functions: 18
   Symbols:   52
   CStrings:  121
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_b98 : 8 -> 656
~ sub_ba0 -> sub_e28 : 712 -> 8
~ sub_f4c -> sub_f14 : 200 -> 156
~ sub_1094 -> sub_1030 : 152 -> 148
~ sub_112c -> sub_10c4 : 264 -> 224
~ sub_1234 -> sub_11a4 : 484 -> 440
~ sub_1418 -> sub_135c : 260 -> 224
~ sub_151c -> sub_143c : 224 -> 184

```
