## lockdownd

> `/usr/libexec/lockdownd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1378.40.2.0.0
-  __TEXT.__text: 0x912c4
+1378.40.3.0.0
+  __TEXT.__text: 0x912ec
   __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_stubs: 0x15c0
-  __TEXT.__objc_methlist: 0x180
-  __TEXT.__cstring: 0xee5e
+  __TEXT.__objc_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0x190
+  __TEXT.__cstring: 0xee5f
   __TEXT.__const: 0xe200
-  __TEXT.__gcc_except_tab: 0xaf0
-  __TEXT.__objc_methname: 0xf22
-  __TEXT.__oslogstring: 0x3f7
+  __TEXT.__gcc_except_tab: 0xaf8
+  __TEXT.__objc_methname: 0xf28
+  __TEXT.__oslogstring: 0x405
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methtype: 0x15a
   __TEXT.__services: 0x2d43
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xef8
   __DATA_CONST.__const: 0x7140
   __DATA_CONST.__cfstring: 0xdae0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__got: 0x430
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x330
-  __DATA.__objc_selrefs: 0x5a8
+  __DATA.__objc_selrefs: 0x5b0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x2358

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 882
+  Functions: 883
   Symbols:   642
-  CStrings:  2521
+  CStrings:  2522
 
CStrings:
+ "-[LockdownWiFiMonitor start]"
+ "Tried to start WiFi monitor with no interface; this is a no-op"
+ "start"
- "-[LockdownWiFiMonitor init]"
- "Failed to create initial state WiFiMonitor block"
```
