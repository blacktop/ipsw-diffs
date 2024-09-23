## profiled

> `/usr/libexec/profiled`

```diff

-2351.0.0.0.0
-  __TEXT.__text: 0x9d7e0
-  __TEXT.__auth_stubs: 0x20e0
+2352.1.1.0.0
+  __TEXT.__text: 0x9d844
+  __TEXT.__auth_stubs: 0x2100
   __TEXT.__objc_stubs: 0xfa20
   __TEXT.__objc_methlist: 0x4c8c
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x194c
-  __TEXT.__oslogstring: 0xcb03
+  __TEXT.__oslogstring: 0xcb12
   __TEXT.__cstring: 0x8b27
   __TEXT.__objc_methname: 0x1330c
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x1ff1
   __TEXT.__unwind_info: 0x16a0
-  __DATA_CONST.__auth_got: 0x1080
+  __DATA_CONST.__auth_got: 0x1090
   __DATA_CONST.__got: 0x1b80
   __DATA_CONST.__const: 0x1b38
   __DATA_CONST.__cfstring: 0x8300

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1921
-  Symbols:   1452
+  Symbols:   1454
   CStrings:  4883
 
Symbols:
+ _MCFixHostileSymlinks
+ _MCDestinationPathIsSafeFromSymlinkAttacks
CStrings:
+ "Destination path contains suspicious symlink: %!{(MISSING)public}@"
- "Setting AirPlay whitelist to %!l(MISSING)u devices."

```
