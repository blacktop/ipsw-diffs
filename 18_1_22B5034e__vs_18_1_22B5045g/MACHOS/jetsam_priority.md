## jetsam_priority

> `/usr/libexec/jetsam_priority`

```diff

-10725.0.0.0.0
-  __TEXT.__text: 0x8ec8
-  __TEXT.__auth_stubs: 0x4e0
+10725.40.2.0.0
+  __TEXT.__text: 0x9104
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xac8
-  __TEXT.__cstring: 0x116f
+  __TEXT.__gcc_except_tab: 0xb68
+  __TEXT.__cstring: 0x116e
   __TEXT.__objc_methname: 0x126
   __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 91
-  Symbols:   109
+  Symbols:   124
   CStrings:  179
 
Symbols:
+ _objc_release_x19
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retain_x8
+ _objc_release_x27
+ _optind
+ _objc_release_x8
+ _objc_release_x20
+ _objc_release_x9
+ _objc_release
+ _objc_release_x25
+ __DefaultRuneLocale
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
CStrings:
+ "   -z <optional PID>: Reset interval footprint for PID (or all). Requires development kernel.\n"
- "   -z (optional:) PID: Reset interval footprint for PID (or all). Requires development kernel.\n"

```
