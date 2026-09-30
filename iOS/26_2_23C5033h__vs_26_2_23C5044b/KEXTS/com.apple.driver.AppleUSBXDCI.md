## com.apple.driver.AppleUSBXDCI

> `com.apple.driver.AppleUSBXDCI`

```diff

-847.60.10.0.0
-  __TEXT.__cstring: 0x57c5
-  __TEXT.__os_log: 0x27fd
+847.62.1.0.0
+  __TEXT.__cstring: 0x5869
+  __TEXT.__os_log: 0x284e
   __TEXT.__const: 0x34
-  __TEXT_EXEC.__text: 0x219c4
+  __TEXT_EXEC.__text: 0x21b80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

   __DATA_CONST.__const: 0x1108
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: EE51171C-3567-38F1-84FD-F1C49EEB932C
+  UUID: C21FA2A1-C3D7-3472-95B8-511D01BD4874
   Functions: 286
   Symbols:   0
-  CStrings:  663
+  CStrings:  666
 
Functions:
~ __ZN12AppleUSBXDCI16handleUSBSuspendEv : 1136 -> 1580
CStrings:
+ "%s@%s: %s::%s: Pending IO on ep 0x%02x, but interface does not want remote wake\n"
+ "AppleUSBXDCI::%s:Pending IO on ep 0x%02x, but interface does not want remote wake\n"

```
