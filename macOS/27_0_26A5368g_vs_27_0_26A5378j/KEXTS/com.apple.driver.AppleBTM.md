## com.apple.driver.AppleBTM

> `com.apple.driver.AppleBTM`

```diff

   __TEXT.__const: 0x5a0
-  __TEXT.__cstring: 0x416d
-  __TEXT.__os_log: 0x6c4
-  __TEXT_EXEC.__text: 0x1a014
+  __TEXT.__cstring: 0x40c5
+  __TEXT.__os_log: 0x6fb
+  __TEXT_EXEC.__text: 0x1a004
   __TEXT_EXEC.__auth_stubs: 0x3d0
   __DATA.__data: 0x177
   __DATA.__common: 0x448

   __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1101
-  Symbols:   1755
-  CStrings:  536
+  Functions: 1098
+  Symbols:   1754
+  CStrings:  535
 
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
Symbols:
+ __ZZN19AppleBTMAONPMUAgent14configSamplingE10SampleRateE11_os_log_fmt_1
+ __ZZN19AppleBTMAONPMUAgent14configSamplingE10SampleRateE11_os_log_fmt_2
+ __ZZN19AppleBTMAONPMUAgent17loadPMUFilterSpecEvE20kalloc_type_view_809
+ __ZZN19AppleBTMAONPMUAgent17loadPMUFilterSpecEvE20kalloc_type_view_847
- _ZN19AppleBTMAONPMUAgent14configSamplingE10SampleRate
- __ZZN19AppleBTMAONPMUAgent17loadPMUFilterSpecEvE20kalloc_type_view_807
- __ZZN19AppleBTMAONPMUAgent17loadPMUFilterSpecEvE20kalloc_type_view_845
CStrings:
+ "%s: _pmuDriver is NULL"
+ "%s: _pmuSecondaryDriver is NULL"
- "\"AppleBTM: %s:%u \" \"%s: _pmuDriver is NULL\" @%s:%d"
- "\"AppleBTM: %s:%u \" \"%s: _pmuSecondaryDriver is NULL\" @%s:%d"
- "IOReturn AppleBTMAONPMUAgent::configSampling(SampleRate)"

```
