## AppleTracingSupportSymbolication

> `/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication`

```diff

-65.2.0.0.0
-  __TEXT.__text: 0x1adf4
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__const: 0x378
-  __TEXT.__gcc_except_tab: 0x1370
-  __TEXT.__cstring: 0x6ee
-  __TEXT.__oslogstring: 0x275
-  __TEXT.__unwind_info: 0xd28
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x548
-  __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__const: 0x260
-  __DATA.__bss: 0x88
+84.100.20.0.0
+  __TEXT.__text: 0x1aa64
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__const: 0x35c
+  __TEXT.__gcc_except_tab: 0x13e0
+  __TEXT.__cstring: 0x708
+  __TEXT.__oslogstring: 0x2a5
+  __TEXT.__unwind_info: 0xcd0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x568
+  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__const: 0x240
+  __DATA.__bss: 0x98
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 709
-  Symbols:   1037
-  CStrings:  68
+  Functions: 693
+  Symbols:   1031
+  CStrings:  71
 
Symbols:
+ __Z28should_prewarm_symbolicatorsv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _dispatch_once
+ _memcpy
+ _sysctlbyname
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
CStrings:
+ "Path not accessible for %s @ 0x%llx (pid=%d)\n%s"
+ "hw.memsize_physical"
+ "v8@?0"

```
