## com.apple.driver.ApplePhoneBTM

> `com.apple.driver.ApplePhoneBTM`

```diff

-  __TEXT.__cstring: 0x425b
+  __TEXT.__cstring: 0x41b3
   __TEXT.__const: 0x5f0
-  __TEXT.__os_log: 0x6c4
-  __TEXT_EXEC.__text: 0x197d4
+  __TEXT.__os_log: 0x6fb
+  __TEXT_EXEC.__text: 0x197c4
   __TEXT_EXEC.__auth_stubs: 0x3d0
   __DATA.__data: 0x177
   __DATA.__common: 0x470

   __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1117
+  Functions: 1114
   Symbols:   0
-  CStrings:  544
+  CStrings:  543
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ "%s: _pmuDriver is NULL"
+ "%s: _pmuSecondaryDriver is NULL"
- "\"AppleBTM: %s:%u \" \"%s: _pmuDriver is NULL\" @%s:%d"
- "\"AppleBTM: %s:%u \" \"%s: _pmuSecondaryDriver is NULL\" @%s:%d"
- "IOReturn AppleBTMAONPMUAgent::configSampling(SampleRate)"

```
