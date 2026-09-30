## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

```diff

-200.1.0.0.0
-  __TEXT.__text: 0x404
-  __TEXT.__auth_stubs: 0x210
+200.2.0.0.0
+  __TEXT.__text: 0x62c
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x7a
-  __TEXT.__oslogstring: 0x16
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x8c
+  __TEXT.__oslogstring: 0xfe
   __TEXT.__objc_methname: 0x5a
   __TEXT.__unwind_info: 0x70
-  __DATA.__auth_got: 0x110
+  __DATA.__auth_got: 0x120
   __DATA.__got: 0x18
   __DATA.__const: 0x48
   __DATA.__cfstring: 0x40

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 7
-  Symbols:   44
-  CStrings:  13
+  Symbols:   46
+  CStrings:  20
 
Symbols:
+ __os_log_impl
+ _objc_release_x23
+ _strncmp
- _objc_release_x19
CStrings:
+ "%!{(MISSING)public}s reset on-disk tailspin configuration. Apple-Internal: %!{(MISSING)bool}d, Is Photos: %!{(MISSING)bool}d"
+ "Did"
+ "Didn't"
+ "Not Photos, no on-disk config"
+ "Photos"
+ "is Photos: %!{(MISSING)bool}d, is tailspin enabled: %!{(MISSING)bool}d"
+ "last build reset: %!{(MISSING)public}@, current build: %!{(MISSING)public}@"

```
