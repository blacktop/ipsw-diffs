## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-145.100.7.2.1
-  __TEXT.__text: 0x1b8d28
+147.100.5.2.1
+  __TEXT.__text: 0x1b8d60
   __TEXT.__objc_methlist: 0x3b5c
-  __TEXT.__const: 0x1e7d0
+  __TEXT.__const: 0x1e7e0
   __TEXT.__cstring: 0x4274
-  __TEXT.__oslogstring: 0x6349
+  __TEXT.__oslogstring: 0x6379
   __TEXT.__gcc_except_tab: 0x7e8
   __TEXT.__dlopen_cstrs: 0x147
   __TEXT.__constg_swiftt: 0x11538
Functions:
~ -[CallDBManagerClient createHelperConnection] : 828 -> 824
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:] : 644 -> 692
~ -[CHRecentCall description] : 2124 -> 2140
~ +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:processHandle:error:] : 748 -> 744
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:].cold.1 : 60 -> 112
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:].cold.4 : 112 -> 60
CStrings:
+ "147.100.5.2.1"
+ "147.100.5.2.1~16"
+ "Call History access requires data store access entitlement %@ or %@. This will be a hard error in the future."
+ "Client is missing the %@ and %@ entitlements (in future, one of these will be required)"
+ "createDatabase client (permanent:%{public}i) (syncHelperDidSucceed:%{public}i)"
- "145.100.7.2.1"
- "145.100.7.2.1~3"
- "Call History access requires data store access entitlement %@ or %@."
- "Not attempting to create helper connection because we're missing the %@ and %@ entitlements (one is required)"
- "createDatabase client (permanent:%{public}i)"
```
