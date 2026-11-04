## addressbooksyncd

> `/usr/libexec/addressbooksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-308.0.0.0.0
-  __TEXT.__text: 0x3b254
+309.0.0.0.0
+  __TEXT.__text: 0x3b3b4
   __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x7940
-  __TEXT.__objc_methlist: 0x4578
+  __TEXT.__objc_stubs: 0x7980
+  __TEXT.__objc_methlist: 0x4598
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x924
-  __TEXT.__objc_methname: 0x84b6
-  __TEXT.__cstring: 0x2dac
+  __TEXT.__objc_methname: 0x8512
+  __TEXT.__cstring: 0x2e43
   __TEXT.__objc_classname: 0x5fb
   __TEXT.__objc_methtype: 0x13f2
-  __TEXT.__oslogstring: 0x263e
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__oslogstring: 0x2670
+  __TEXT.__unwind_info: 0x1098
   __DATA_CONST.__const: 0xe98
-  __DATA_CONST.__cfstring: 0x3340
+  __DATA_CONST.__cfstring: 0x3360
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_nlcatlist: 0x8

   __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x6a0
   __DATA.__objc_const: 0x9520
-  __DATA.__objc_selrefs: 0x27c0
+  __DATA.__objc_selrefs: 0x27d0
   __DATA.__objc_ivar: 0x4e0
   __DATA.__objc_data: 0x1310
   __DATA.__data: 0x6f0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1627
+  Functions: 1631
   Symbols:   407
-  CStrings:  2704
+  CStrings:  2710
 
CStrings:
+ "%s: No Apple Account exists for user"
+ "%s: No CardDAV account exists for user"
+ "%s: Won't set primary iCloud CardDAV ID"
+ "+[ABSAccountsManager primaryiCloudCardDAVAccountIdentifier]"
+ "+[ABSAccountsManager setPrimaryiCloudCardDAVAccountIdentifier:]"
+ "== Started AddressBookSync-309"
+ "Forcing accounts sync via %@ override"
+ "_internal_shouldForceAccountsSync"
+ "internal_forceAccountsSync"
+ "retryPendingPrimaryiCloudCardDAVAccountIdentifierIfNeeded"
- "== Started AddressBookSync-308"
- "No Apple Account exists for user"
- "No CardDAV account exists for user"
- "Won't set primary iCloud CardDAV ID"
```
