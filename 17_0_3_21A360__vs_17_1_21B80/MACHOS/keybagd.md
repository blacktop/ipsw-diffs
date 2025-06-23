## keybagd

> `/usr/libexec/keybagd`

```diff

-619.2.1.0.0
-  __TEXT.__text: 0x1c724
-  __TEXT.__auth_stubs: 0x13a0
+621.40.2.0.0
+  __TEXT.__text: 0x1c7a8
+  __TEXT.__auth_stubs: 0x13c0
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x480
-  __TEXT.__cstring: 0x77df
+  __TEXT.__cstring: 0x77fb
   __TEXT.__const: 0xd1
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__objc_methname: 0x1731
+  __TEXT.__objc_methname: 0x173b
   __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methtype: 0x911
+  __TEXT.__objc_methtype: 0x917
   __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__oslogstring: 0x16a
   __TEXT.__unwind_info: 0x5f8
-  __DATA_CONST.__auth_got: 0x9e0
+  __DATA_CONST.__auth_got: 0x9f0
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0xe00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AA667DAA-5738-3937-9256-0ECD9B3AF679
+  UUID: 786D1E94-478F-3D69-8B97-E4A4E077F449
   Functions: 441
-  Symbols:   373
+  Symbols:   375
   CStrings:  1904
 
Symbols:
+ _objc_release_x24
+ _objc_retain_x24
CStrings:
+ "-[KBXPCService SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:]"
+ "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:"
+ "unlock(memento:%d, verify_only: %d) -> %d"
+ "v48@0:8@\"NSFileHandle\"16Q24B32B36@?<v@?i@\"NSError\">40"
+ "v48@0:8@16Q24B32B36@?40"
- "-[KBXPCService SeshatUnlockWithSecret:secretSize:withMemento:withReply:]"
- "SeshatUnlockWithSecret:secretSize:withMemento:withReply:"
- "unlock(memento:%d) -> %d"
- "v44@0:8@\"NSFileHandle\"16Q24B32@?<v@?i@\"NSError\">36"
- "v44@0:8@16Q24B32@?36"

```
