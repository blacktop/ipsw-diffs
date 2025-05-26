## seputil

> `/usr/libexec/seputil`

```diff

-774.60.2.0.0
-  __TEXT.__text: 0x164e0
+774.100.29.0.0
+  __TEXT.__text: 0x16818
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__cstring: 0x5621
+  __TEXT.__cstring: 0x5769
   __TEXT.__oslogstring: 0x93
   __TEXT.__const: 0xbe4
   __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x454
+  __TEXT.__unwind_info: 0x458
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x528
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xb28
+  __DATA.__data: 0xb48
   __DATA.__bss: 0x8b5
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 441
+  Functions: 443
   Symbols:   196
-  CStrings:  674
+  CStrings:  683
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
CStrings:
+ "\t\t                         'value' should be 'enable' or 'disable'.\n"
+ "\t\t%s --test-run test (run all tests in the category 'test')\n"
+ "\t\t%s --test-run test/pass (run the test 'pass' in the category 'test')\n"
+ "\t\t--tunable-check <value>  Enable or disable tunable check mode.\n"
+ "\t\tExamples:\n"
+ "\tDebugging and Diagnostic commands\n"
+ "\tSystem testing commands\n"
+ "\tUnit test commands\n"
+ "%s: Tunable mode must be 'enable' or 'disable'.\n"
+ "Failed to update tunable check mode. ret: 0x%x\n"
+ "disable"
+ "enable"
+ "tunable-check"
- "\t%s --test-run test (run all tests in the category 'test')\n"
- "\t%s --test-run test/pass (run the test 'pass' in the category 'test')\n"
- "\tExamples:\n"
- "\tTesting commands\n"

```
