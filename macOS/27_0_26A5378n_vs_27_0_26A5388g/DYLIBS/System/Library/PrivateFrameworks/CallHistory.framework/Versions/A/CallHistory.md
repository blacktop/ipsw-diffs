## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
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

-145.100.7.0.0
-  __TEXT.__text: 0x1bd1a0
+147.100.5.0.0
+  __TEXT.__text: 0x1bd1e4
   __TEXT.__objc_methlist: 0x39e4
   __TEXT.__const: 0x1e6b0
   __TEXT.__cstring: 0x4266
-  __TEXT.__oslogstring: 0x63d9
+  __TEXT.__oslogstring: 0x6409
   __TEXT.__gcc_except_tab: 0x7dc
   __TEXT.__dlopen_cstrs: 0xe3
   __TEXT.__constg_swiftt: 0x114cc
Functions:
~ -[CallDBManagerClient createHelperConnection] : 768 -> 764
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:] : 680 -> 732
~ -[CHRecentCall description] : 2248 -> 2268
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:].cold.1 : 64 -> 116
~ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:].cold.4 : 116 -> 64
CStrings:
+ "147.100.5"
+ "147.100.5~64"
+ "Call History access requires data store access entitlement %@ or %@. This will be a hard error in the future."
+ "Client is missing the %@ and %@ entitlements (in future, one of these will be required)"
+ "createDatabase client (permanent:%{public}i) (syncHelperDidSucceed:%{public}i)"
- "145.100.7"
- "145.100.7~143"
- "Call History access requires data store access entitlement %@ or %@."
- "Not attempting to create helper connection because we're missing the %@ and %@ entitlements (one is required)"
- "createDatabase client (permanent:%{public}i)"
```
