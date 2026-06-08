## CTParserService

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService`

```diff

-13187.6.0.0.0
-  __TEXT.__text: 0x14490
+13466.3.0.0.0
+  __TEXT.__text: 0x14b88
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__init_offsets: 0x90
-  __TEXT.__gcc_except_tab: 0x1a00
-  __TEXT.__cstring: 0x378
-  __TEXT.__const: 0x2a26
-  __TEXT.__oslogstring: 0x1d6
-  __TEXT.__unwind_info: 0x1150
+  __TEXT.__gcc_except_tab: 0x1abc
+  __TEXT.__cstring: 0x5d5
+  __TEXT.__const: 0x2a46
+  __TEXT.__oslogstring: 0x1e2
+  __TEXT.__unwind_info: 0x11d8
+  __DATA_CONST.__const: 0x2568
   __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x2568
   __DATA.__data: 0x851
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 49A2B6EB-31A6-34C4-B4C3-BA0B8B6AD4B9
-  Functions: 787
+  UUID: 14355F25-2983-3B47-9260-70A539F2070D
+  Functions: 803
   Symbols:   339
-  CStrings:  79
+  CStrings:  81
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __Z15CSIboolAsStringb
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRG3ugAdEmQU2ZSB6VWnhsuR5MzSZe8tQB1XVQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CRG3ugAdEmQU2ZSB6VWnhsuR5MzSZe8tQB1XVQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "3GPP parsing OK: %{bool}d"
+ "3GPP2 parsing OK: %{bool}d"
- "3GPP parsing OK: %s"
- "3GPP2 parsing OK: %s"

```
