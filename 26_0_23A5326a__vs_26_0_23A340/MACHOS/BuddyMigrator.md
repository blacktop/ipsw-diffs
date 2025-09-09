## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

 5374.106.0.0.0
-  __TEXT.__text: 0x15b70
+  __TEXT.__text: 0x15bb4
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_stubs: 0x1e40
   __TEXT.__objc_methlist: 0x1068

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 038BCDE9-476F-37D7-BA53-853A0526EEB6
+  UUID: E1C1733B-9274-3EA9-9097-DF7A6DE1B29B
   Functions: 536
   Symbols:   334
   CStrings:  937
Functions:
~ sub_2438 : 8780 -> 8764
~ sub_168ac -> sub_1689c : 204 -> 232
~ sub_16978 -> sub_16984 : 204 -> 232
~ sub_16cfc -> sub_16d24 : 220 -> 248
CStrings:
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"

```
