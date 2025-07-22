## misd

> `/usr/libexec/misd`

```diff

-359.0.0.0.0
-  __TEXT.__text: 0x201a0
+360.0.0.0.0
+  __TEXT.__text: 0x201b4
   __TEXT.__auth_stubs: 0x11e0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xaee1
+  __TEXT.__cstring: 0xaf17
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x4c8
   __DATA_CONST.__auth_got: 0x8f8
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x9d8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B90BE323-69B8-344D-A879-55DBF8E56C0D
-  Functions: 427
+  UUID: BC5A431E-79EF-3B6C-84A2-9F7FDD34307A
+  Functions: 429
   Symbols:   380
-  CStrings:  1788
+  CStrings:  1790
 
CStrings:
+ "%s: %s err = %d"
+ "%s: CoreTelephony connection was lost"
+ "%s: encountered a connection error trying to activate tethering, tearing down phs service"
+ "FALSE"
+ "TRUE"
+ "doauth(%d), tethering %s supported, user %s authenticated"
+ "mis_pdp_ct_event_callback"
+ "set state: %s, pstate %s(%d)->%s(%d), state %s(%d)->%s(%d), reason %s(%d), airplane mode %s, cellular data plan %s, connection availability %s"
+ "setting netrb state to %d, reason %d from %d"
- "%s: %s"
- "%s: encountered a connection error trying to activate tethering, tearing down personal hotspot"
- "Setting netrb state to %d from %d"
- "Setting netrb state to %d, reason %d from %d"
- "doauth(%d) tethering %s supported, user %s authenticated"
- "mis_pdp_ct_event_cb"
- "set state: %s, pstate %s(%d)->%s(%d), state %s(%d)->%s(%d), reason %s(%d), airplane mode %s, cellular data plan %s"

```
