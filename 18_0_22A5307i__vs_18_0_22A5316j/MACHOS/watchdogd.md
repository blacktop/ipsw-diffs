## watchdogd

> `/usr/libexec/watchdogd`

```diff

-274.0.1.0.0
-  __TEXT.__text: 0xa180
-  __TEXT.__auth_stubs: 0xf20
+274.0.3.0.0
+  __TEXT.__text: 0xa440
+  __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_stubs: 0xa40
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x40a4
-  __TEXT.__oslogstring: 0x1ad
+  __TEXT.__cstring: 0x40a8
+  __TEXT.__oslogstring: 0x280
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__objc_methname: 0x69f
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__auth_got: 0x7a0
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x318

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_selrefs: 0x290
   __DATA.__data: 0x8d50
-  __DATA.__bss: 0x6c8
+  __DATA.__bss: 0xae0
   __DATA.__common: 0x90
   __INFO_FILTER.__disable: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 162
-  Symbols:   304
-  CStrings:  563
+  Functions: 169
+  Symbols:   305
+  CStrings:  568
 
Symbols:
+ _os_parse_boot_arg_from_buffer_int
CStrings:
+ "watchdog opt-in service registration is not supported on VM"
+ "watchdog opt-in service registration is only supported on darwinOS variant"
+ "watchdog user space monitoring is disabled"
+ "wdt"
- "watchdog opt-in service registration is not supported on this OS"

```
