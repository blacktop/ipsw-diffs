## tailspind

> `/usr/libexec/tailspind`

```diff

 218.2.0.0.0
-  __TEXT.__text: 0xd40c
+  __TEXT.__text: 0xd4f8
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_stubs: 0x900
   __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0xff6
+  __TEXT.__cstring: 0x1002
   __TEXT.__objc_methname: 0xbd2
-  __TEXT.__oslogstring: 0x256d
+  __TEXT.__oslogstring: 0x25ba
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: FC134EF0-2CB7-3B2D-971C-A1EF9548136D
-  Functions: 240
+  UUID: 16FDF223-F570-31F5-960E-E4D7C31108B1
+  Functions: 241
   Symbols:   242
-  CStrings:  474
+  CStrings:  476
 
Functions:
~ sub_100008a5c : 6040 -> 6156
+ sub_10000b8ac
+ sub_10000b8d4
- sub_10000b86c
- sub_10000b8b4
+ sub_10000dca4
CStrings:
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "hangtracerd"

```
