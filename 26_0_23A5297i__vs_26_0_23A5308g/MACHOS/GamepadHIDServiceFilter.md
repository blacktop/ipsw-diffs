## GamepadHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter`

```diff

-13.0.36.0.0
-  __TEXT.__text: 0x36a4
-  __TEXT.__auth_stubs: 0x450
+13.0.39.0.0
+  __TEXT.__text: 0x36cc
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_stubs: 0x540
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x574
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__gcc_except_tab: 0x3d0
   __TEXT.__cstring: 0x17f
-  __TEXT.__oslogstring: 0x4db
+  __TEXT.__oslogstring: 0x4ee
   __TEXT.__objc_methname: 0xc0c
   __TEXT.__objc_classname: 0x280
   __TEXT.__objc_methtype: 0xbbc
   __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB06D5CF-64AA-357F-BEB7-A5326BE88307
-  Functions: 115
-  Symbols:   95
+  UUID: A5EFF2AB-F5C4-3443-9036-2A34A32EEE3C
+  Functions: 114
+  Symbols:   97
   CStrings:  281
 
Symbols:
+ _objc_release_x24
+ _objc_release_x25
CStrings:
+ "-> [%#x] Press sequence [%zu] handle event (down: %zd, max:%d) -> State:%d Count:%d Next:%f"
+ "-> [%#x] Press sequence [%zu] pass event (down: %u)\n%@"
- "-> [%#x] Press sequence [%zu] handle event (down: %zd) -> State:%d Count:%d Next:%f"
- "-> [%#x] Press sequence [%zu] pass event %@"

```
