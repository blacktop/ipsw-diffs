## AdPlatformsCommon

> `/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon`

```diff

-556.0.83.0.0
-  __TEXT.__text: 0x4de48
+556.1.3.0.0
+  __TEXT.__text: 0x4de80
   __TEXT.__auth_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x25d4
   __TEXT.__const: 0x5230
-  __TEXT.__cstring: 0x4740
+  __TEXT.__cstring: 0x46f0
   __TEXT.__gcc_except_tab: 0x19c
   __TEXT.__oslogstring: 0x109b
   __TEXT.__constg_swiftt: 0x22e4

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1B2DF149-2D5C-35EC-BC96-698A39AD9258
+  UUID: 638001C1-7C90-32FA-9803-178689C7F868
   Functions: 2652
   Symbols:   339
   CStrings:  1982
Functions:
~ sub_1ba514760 -> sub_1bb7e1760 : 2564 -> 2616
~ sub_1ba523c64 -> sub_1bb7f0c98 : 1028 -> 1032
CStrings:
+ "SELECT rowid, value, expiration, type, timestamp, generation, name, processId, amsDSID, paStatus FROM Identifier WHERE name = ? AND type = ?"
- "SELECT i.rowid, i.value, i.expiration, i.type, i.timestamp, i.generation, i.name, i.processId, i.amsDSID, i.paStatus FROM Identifier AS i INNER JOIN IdentifierSource AS s ON i.rowid = s.identifierRowId WHERE i.name = ?"

```
