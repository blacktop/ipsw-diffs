## com.apple.iokit.IOReportFamily

> `com.apple.iokit.IOReportFamily`

```diff

-  __TEXT.__cstring: 0x216
+  __TEXT.__cstring: 0x238
   __TEXT.__os_log: 0x4fc
-  __TEXT_EXEC.__text: 0x31f8
-  __TEXT_EXEC.__auth_stubs: 0x1f0
+  __TEXT_EXEC.__text: 0x31ec
+  __TEXT_EXEC.__auth_stubs: 0x210
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1518
   __DATA_CONST.__kalloc_type: 0x80
-  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__kalloc_var: 0xa0
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x58
   Functions: 69
-  Symbols:   470
-  CStrings:  42
+  Symbols:   474
+  CStrings:  44
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _IOFreeTypeVarImpl
+ _IOMallocTypeVarImpl
+ __ZZL18_disableReportCallPvS_E20kalloc_type_view_786
+ __ZZN18IOReportUserClient4stopEP9IOServiceE20kalloc_type_view_803
+ _thread_call_enter
- _thread_call_enter1
Functions:
~ __ZN18IOReportUserClient4stopEP9IOService : 264 -> 280
~ __ZL18_disableReportCallPvS_ : 192 -> 164
CStrings:
+ "111"
+ "site.DisableThreadCallContext"

```
