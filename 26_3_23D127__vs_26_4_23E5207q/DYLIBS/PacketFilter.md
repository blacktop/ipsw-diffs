## PacketFilter

> `/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter`

```diff

-112.0.0.0.0
-  __TEXT.__text: 0x828c
+114.100.1.0.0
+  __TEXT.__text: 0x8264
   __TEXT.__auth_stubs: 0x580
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x233c

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
-  UUID: 3812D519-8430-3EB8-9F5C-F824EB254874
+  UUID: 51312C4B-18F2-3661-A7B3-A37F6C79BB0F
   Functions: 131
   Symbols:   513
   CStrings:  361
Functions:
~ ___PFUserCreate_block_invoke : 200 -> 192
~ _PFCheckRule : 1932 -> 1968
~ ___PFLogCheck : 392 -> 388
~ ___PFDummyNetConsistencyCheck : 348 -> 344
~ _PFCheckNATRule : 292 -> 288
~ ___PFRuleStrToNum : 316 -> 276
~ ___PFXPCResponseHandler : 380 -> 384
~ _PFManagerAddUser : 188 -> 164
~ _PFManagerRelease : 32 -> 36

```
