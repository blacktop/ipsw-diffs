## watchdogd

> `/usr/libexec/watchdogd`

```diff

-274.40.3.0.0
-  __TEXT.__text: 0xa454
+274.40.4.0.0
+  __TEXT.__text: 0xa5a4
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_stubs: 0xa40
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x40a8
+  __TEXT.__cstring: 0x4187
   __TEXT.__oslogstring: 0x280
   __TEXT.__objc_classname: 0x1
   __TEXT.__gcc_except_tab: 0x5c

   __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__const: 0x760
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x318

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 169
+  Functions: 170
   Symbols:   305
-  CStrings:  568
+  CStrings:  573
 
CStrings:
+ "WindowServer"
+ "wdt_ext_ws_to"
+ "detected boot-arg (%!s(MISSING)) for WindowServer timeout override: %!l(MISSING)ld"
+ "%!s(MISSING) configured to timeout in %!l(MISSING)ld seconds (per %!s(MISSING) boot-arg)"
+ "Keep %!s(MISSING) default timeout cause %!l(MISSING)ld seconds (per %!s(MISSING) boot-arg) is too short"

```
