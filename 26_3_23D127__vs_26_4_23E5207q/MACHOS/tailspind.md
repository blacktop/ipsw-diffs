## tailspind

> `/usr/libexec/tailspind`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0xd368
-  __TEXT.__auth_stubs: 0xbc0
+250.0.0.0.0
+  __TEXT.__text: 0xd2ac
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0xfed
+  __TEXT.__cstring: 0x103b
   __TEXT.__objc_methname: 0xc42
-  __TEXT.__oslogstring: 0x259e
+  __TEXT.__oslogstring: 0x25eb
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x3a0
-  __DATA_CONST.__auth_got: 0x5f0
+  __TEXT.__unwind_info: 0x3b8
+  __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x408

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 92EA1305-47C5-3F56-A6FB-7AE4FF52F3C8
-  Functions: 243
-  Symbols:   242
-  CStrings:  483
+  UUID: 3424C168-5C88-3015-B2D5-712E8C460FDB
+  Functions: 248
+  Symbols:   238
+  CStrings:  485
 
Symbols:
+ ___strlcpy_chk
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x8
- _strncpy
CStrings:
+ "<background_tracing_available>"
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "hangtracerd"
+ "ktrace buffer starts after client's end timestamp. Requested: %llu, Actual: %llu, delta: %llu (%.3f secs)"
- "<foreground_tracing>"
- "ktrace buffer starts after client's end timestamp"

```
