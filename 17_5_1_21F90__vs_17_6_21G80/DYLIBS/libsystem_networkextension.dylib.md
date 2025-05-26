## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-1838.122.1.0.0
+1838.140.5.0.1
   __TEXT.__text: 0x15ca0
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x18f9
-  __TEXT.__oslogstring: 0x2c76
+  __TEXT.__oslogstring: 0x2d2d
   __TEXT.__unwind_info: 0x374
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0xc70

   - /usr/lib/system/libxpc.dylib
   Functions: 264
   Symbols:   651
-  CStrings:  525
+  CStrings:  526
 
CStrings:
+ "%s Set domain - is_tracker %d domain <%{private}s> owner <%{private}s>, tracker domain <%{private}s>"
+ "%s: found match for domain <%{private}s> (index %d) owner <%{private}s>"
+ "%s: lookup for <%{private}s> length %d"
+ "%s: marking socket attribution as user <non-app-initiated flag %d> with website context <%{private}s>"
+ "Could not set tracker domain attributes - domain <%{private}s>, owner <%{private}s>, tracker domain <%{private}s>"
+ "Failed to set domain(s) for socket - invalid domain syntax in <%{private}s>"
- "%s: found match for domain <%s> (index %d) owner <%s>"
- "%s: lookup for <%s> length %d"
- "%s: marking socket attribution as user <non-app-initiated flag %d> with website context %s"
- "Could not set tracker domain attributes - domain %s, owner %s, tracker domain %s"
- "Failed to set domain(s) for socket - invalid domain syntax in %s"

```
