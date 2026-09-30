## tailspind

> `/usr/libexec/tailspind`

```diff

-238.0.0.0.0
+240.0.0.0.0
   __TEXT.__text: 0xd454
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_stubs: 0x960

   __TEXT.__const: 0x12c
   __TEXT.__cstring: 0xff9
   __TEXT.__objc_methname: 0xc42
-  __TEXT.__oslogstring: 0x25d3
+  __TEXT.__oslogstring: 0x25eb
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: E0419B5C-898F-38CF-AB1C-E3BD56DA0216
+  UUID: B8F9E934-225B-3C9F-929F-38D9FCCABFAF
   Functions: 244
   Symbols:   242
   CStrings:  485
CStrings:
+ "Updating trace buffer reset event name: %{public}s (was %{public}s)"
+ "tailspin CPUTrace config requested by client %{public}s [%d]"
- "Updating trace buffer reset event name: %s (was %s)"
- "tailspin CPUTrace config requested by client %s [%d]"

```
