## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-350.2.0.0.0
-  __TEXT.__text: 0x167918
+351.3.0.0.0
+  __TEXT.__text: 0x169e74
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__const: 0x7c78
-  __TEXT.__cstring: 0xbd82
+  __TEXT.__cstring: 0xbe9a
   __TEXT.__oslogstring: 0x610
-  __TEXT.__unwind_info: 0x1e34
+  __TEXT.__unwind_info: 0x1e48
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1ce0
   __AUTH_CONST.__const: 0x1118

   __DATA.__bss: 0x26f0
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x3808
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__bss: 0x2b8
   - /usr/lib/libSystem.B.dylib
-  UUID: 5E92BE51-9B6E-3F09-8288-DA19326CE217
-  Functions: 2515
+  UUID: 7C30DACD-316D-341E-98F0-DD42E019E9D1
+  Functions: 2530
   Symbols:   566
-  CStrings:  2223
+  CStrings:  2229
 
CStrings:
+ "ABMultivalue"
+ "ABMultivalueLabel"
+ "ABPersonLink"
+ "WHERE abp.StoreID IN  ( ? ) ORDER BY abp.PersonLink , abp.ROWID , abmv.property, abmv.UID"
+ "WITH preferredmatched(rowid ) as ( WITH matched(rowid, personlink) as ( SELECT rowid, personlink from ABPerson WHERE"
+ "ab_allowed_preferred_contact"

```
