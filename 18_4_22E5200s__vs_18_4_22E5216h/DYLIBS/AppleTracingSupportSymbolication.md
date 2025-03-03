## AppleTracingSupportSymbolication

> `/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication`

```diff

-84.100.16.0.0
-  __TEXT.__text: 0x1a524
-  __TEXT.__auth_stubs: 0x820
+84.100.20.0.0
+  __TEXT.__text: 0x1aa64
+  __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0x35c
-  __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x6ee
-  __TEXT.__oslogstring: 0x275
+  __TEXT.__gcc_except_tab: 0x13e0
+  __TEXT.__cstring: 0x708
+  __TEXT.__oslogstring: 0x2a5
   __TEXT.__unwind_info: 0xcd0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x548
-  __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__const: 0x220
-  __DATA.__bss: 0x88
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
-  Functions: 690
-  Symbols:   1023
-  CStrings:  68
+  Functions: 693
+  Symbols:   1031
+  CStrings:  71
 
Symbols:
+ __Z28should_prewarm_symbolicatorsv
+ __ZTISt9exception
+ _dispatch_once
+ _sysctlbyname
CStrings:
+ "Path not accessible for %s @ 0x%llx (pid=%d)\n%s"
+ "hw.memsize_physical"
+ "v8@?0"

```
