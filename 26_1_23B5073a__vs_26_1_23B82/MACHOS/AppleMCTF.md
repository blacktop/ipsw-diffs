## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-905.5.1.0.0
-  __TEXT.__text: 0x76240
+905.5.3.0.0
+  __TEXT.__text: 0x76268
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x238a5
+  __TEXT.__cstring: 0x2389b
   __TEXT.__const: 0x1f3a8
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x610

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BDEE82F3-089B-355E-A8B6-7B8140063594
+  UUID: 03CC5229-6212-3476-913E-DDBD021524F3
   Functions: 619
   Symbols:   354
   CStrings:  2991
Functions:
~ sub_3b710 : 120 -> 116
~ sub_3f780 -> sub_3f77c : 5472 -> 5400
~ sub_40ce0 -> sub_40c94 : 452 -> 576
~ sub_449f8 -> sub_44a28 : 152 -> 144
CStrings:
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
+ "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
+ "06:35:24"
+ "905.5.3"
+ "Oct 23 2025"
- "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature"
- "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature\n"
- "22:57:49"
- "905.5.1"
- "Oct 16 2025"

```
