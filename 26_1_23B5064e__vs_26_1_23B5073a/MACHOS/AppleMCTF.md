## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.97.1.0.0
-  __TEXT.__text: 0x76130
+905.5.1.0.0
+  __TEXT.__text: 0x76240
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x23831
-  __TEXT.__const: 0x1f1c8
+  __TEXT.__cstring: 0x238a5
+  __TEXT.__const: 0x1f3a8
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x610
   __DATA_CONST.__auth_got: 0x6b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24A451F1-4503-32FF-A731-EF6D0C1A5A0F
+  UUID: BDEE82F3-089B-355E-A8B6-7B8140063594
   Functions: 619
   Symbols:   354
-  CStrings:  2988
+  CStrings:  2991
 
Functions:
~ sub_28334 : 688 -> 952
~ sub_285e4 -> sub_286ec : 468 -> 516
~ sub_3b5d8 -> sub_3b710 : 116 -> 120
~ sub_3f644 -> sub_3f780 : 5400 -> 5472
~ sub_40b5c -> sub_40ce0 : 576 -> 452
~ sub_448f0 -> sub_449f8 : 144 -> 152
CStrings:
+ "%lld %d AVE %s: %s:%d Invalid bounds %d %d"
+ "%lld %d AVE %s: %s:%d Invalid bounds %d %d\n"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature\n"
+ "22:57:49"
+ "905.5.1"
+ "AVE_MCTF_SMap_Parse"
+ "Oct 16 2025"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
- "22:48:14"
- "904.97.1"
- "Oct  8 2025"

```
