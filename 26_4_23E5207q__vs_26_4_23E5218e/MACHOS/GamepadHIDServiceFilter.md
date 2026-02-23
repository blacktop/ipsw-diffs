## GamepadHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter`

```diff

-13.4.8.0.0
+13.4.9.0.0
   __TEXT.__text: 0x2a00
   __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x428
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x394
-  __TEXT.__oslogstring: 0x4da
+  __TEXT.__oslogstring: 0x4fd
   __TEXT.__objc_methname: 0x800
   __TEXT.__cstring: 0x83
   __TEXT.__objc_classname: 0x96

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 623C7D84-9A6D-3A24-B477-98BA7E30D641
-  Functions: 68
+  UUID: 49198E46-FFCA-3CAE-894E-3BE8067047CA
+  Functions: 67
   Symbols:   86
   CStrings:  203
 
CStrings:
+ "-> [%#x] Press sequence [%zu] not passing event: Press count threshold (%u) not met by completed press count (%u)."
- "-> [%#x] Press sequence [%zu] not passing event: Press count threshold not met."

```
