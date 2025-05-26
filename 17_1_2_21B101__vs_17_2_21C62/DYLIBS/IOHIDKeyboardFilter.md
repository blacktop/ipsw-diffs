## IOHIDKeyboardFilter

> `/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter`

```diff

-2008.40.6.0.0
-  __TEXT.__text: 0x890c
-  __TEXT.__auth_stubs: 0x710
+2008.60.7.0.0
+  __TEXT.__text: 0x8a54
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_methlist: 0x94
   __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__cstring: 0x3ca
-  __TEXT.__oslogstring: 0x402
+  __TEXT.__gcc_except_tab: 0x570
+  __TEXT.__cstring: 0x3ff
+  __TEXT.__oslogstring: 0x45a
   __TEXT.__unwind_info: 0x3e0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x2e

   __DATA_CONST.__objc_const: 0xd0
   __DATA_CONST.__objc_selrefs: 0x98
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__const: 0x1a8
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x78
   __DATA.__got_weak: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 187
-  Symbols:   229
-  CStrings:  122
+  Functions: 188
+  Symbols:   231
+  CStrings:  124
 
Symbols:
+ _IOHIDEventSystemConnectionGetUUID
+ _IOHIDEventSystemConnectionHasEntitlement
CStrings:
+ "Insufficient permissions to remap alphanumeric keys or special characters for UUID: %@\n"
+ "com.apple.private.hid.client.alpha-numeric-remapping"

```
