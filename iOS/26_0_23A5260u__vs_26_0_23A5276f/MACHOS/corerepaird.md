## corerepaird

> `/usr/libexec/corerepaird`

```diff

-921.0.34.0.0
-  __TEXT.__text: 0x133c
+921.0.65.0.0
+  __TEXT.__text: 0x134c
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x340
   __TEXT.__objc_methlist: 0x3a4
   __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0x1f3
+  __TEXT.__oslogstring: 0x1de
   __TEXT.__cstring: 0x1ea
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x743

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  UUID: D53EF887-8AA9-3BD2-838A-4C678F318313
+  UUID: 68C82DDF-036D-317B-B708-A4FB54D54B6E
   Functions: 39
   Symbols:   55
   CStrings:  188
Functions:
~ sub_100001b30 : 684 -> 700
CStrings:
+ "Received a connection on preflightControl!"
- "Received a connection on com.apple.corerepair.preflightControl!"

```
