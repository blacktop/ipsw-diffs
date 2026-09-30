## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

```diff

-168.0.0.0.0
-  __TEXT.__text: 0x20500
+169.0.0.0.0
+  __TEXT.__text: 0x205fc
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__objc_methlist: 0x32e8
   __TEXT.__const: 0x350
   __TEXT.__cstring: 0x1a68
-  __TEXT.__oslogstring: 0x37f
+  __TEXT.__oslogstring: 0x3ca
   __TEXT.__gcc_except_tab: 0xb28
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF3EE66C-AFD6-397F-B6FF-404423EFA459
-  Functions: 971
-  Symbols:   3743
-  CStrings:  2209
+  UUID: 134D5C90-49EE-3DDA-A1BA-6A16B03EACBC
+  Functions: 972
+  Symbols:   3745
+  CStrings:  2210
 
Symbols:
+ -[RCPVirtualHIDService postHIDEvent:].cold.2
Functions:
~ -[RCPPlayer playEventStream:withOptions:] : 1464 -> 1468
~ -[RCPPlayer _cloneAndTransformHIDEvent:machTimeOffset:transform:] : 228 -> 232
~ -[RCPVirtualHIDService postHIDEvent:] : 300 -> 396
+ -[RCPVirtualHIDService postHIDEvent:].cold.2
CStrings:
+ "03:33:33"
+ "Event timestamp is significantly in the past: %llu vs %llu (diff: %llu ns)"
+ "Jul 22 2025"
- "07:02:47"
- "Jul  8 2025"

```
