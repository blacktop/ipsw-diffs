## ndp

> `/usr/sbin/ndp`

```diff

-741.100.2.0.0
-  __TEXT.__text: 0x3afc
+754.0.0.0.0
+  __TEXT.__text: 0x3c5c
   __TEXT.__auth_stubs: 0x310
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xbc9
+  __TEXT.__cstring: 0xbfb
   __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__const: 0x58
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x58
   __DATA.__data: 0x50
   __DATA.__bss: 0x25d4
   __DATA.__common: 0x298
   - /usr/lib/libSystem.B.dylib
-  UUID: 4FECA6C6-4825-301D-A6CD-32C13C9A0ECF
-  Functions: 24
-  Symbols:   99
-  CStrings:  201
+  UUID: 17E9C4F8-D54B-3095-88D5-E555911E5B10
+  Functions: 25
+  Symbols:   100
+  CStrings:  203
 
Symbols:
+ _rti_flush
CStrings:
+ "       ndp -Z interface"
+ "acndfIilprstA:HPRxwWzZ%:"
+ "ioctl(SIOCSRTIFLUSH_IN6)"
+ "ndp: cannot apply flag '%s' to all interfaces\n"
- "acndfIilprstA:HPRxwWz%:"
- "ndp: cannpt apply flag '%s' to all interfaces\n"

```
