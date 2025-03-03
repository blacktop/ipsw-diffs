## dhcp6d

> `/usr/libexec/dhcp6d`

```diff

-494.100.3.0.0
-  __TEXT.__text: 0x74c8
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x92c
+494.100.6.502.1
+  __TEXT.__text: 0x7748
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x9a2
   __TEXT.__oslogstring: 0x55b
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__cfstring: 0x6c0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  Functions: 97
-  Symbols:   127
-  CStrings:  183
+  Functions: 100
+  Symbols:   130
+  CStrings:  194
 
Symbols:
+ _SCPrint
+ ___stdoutp
+ _printf
CStrings:
+ " CLIENT_FQDN flags 0x%x"
+ " CLIENT_FQDN option is too short %d < %d\n"
+ " N"
+ " O"
+ " S"
+ " ["
+ " ]"
+ " domain-name %@"
+ " domain-name bad, raw bytes <"
+ ">"
+ "CLIENT_FQDN"
+ "LENGTH %d\n"
+ "name %@\n"
- "label length is 0\n"
- "name missing end label\n"

```
