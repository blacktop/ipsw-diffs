## SystemMigrationNetwork

> `/System/Library/PrivateFrameworks/SystemMigrationNetwork.framework/Versions/A/SystemMigrationNetwork`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1421.0.0.0.0
-  __TEXT.__text: 0x3cdb0
-  __TEXT.__objc_methlist: 0x4570
+1426.0.0.0.0
+  __TEXT.__text: 0x3d1e4
+  __TEXT.__objc_methlist: 0x4578
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x9430
-  __TEXT.__gcc_except_tab: 0xe68
-  __TEXT.__ustring: 0x2cde
+  __TEXT.__cstring: 0x956f
+  __TEXT.__gcc_except_tab: 0xe84
+  __TEXT.__ustring: 0x2c4c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xdd8
+  __TEXT.__unwind_info: 0xdd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29b0
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xf0
-  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__got: 0x5b8
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x9540
+  __AUTH_CONST.__cfstring: 0x96a0
   __AUTH_CONST.__objc_const: 0x6878
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1531
-  Symbols:   4053
-  CStrings:  1253
+  Functions: 1533
+  Symbols:   4057
+  CStrings:  1264
 
Symbols:
+ -[SMNNetworkSession(ALConnectionDelegate) backfillHistoryRemoteAddressesForConnection:]
+ GCC_except_table215
+ ___87-[SMNNetworkSession(ALConnectionDelegate) backfillHistoryRemoteAddressesForConnection:]_block_invoke
+ ___NSArray0__struct
+ _objc_msgSend$backfillHistoryRemoteAddressesForConnection:
- GCC_except_table211
CStrings:
+ "/Data/Library/Caches"
+ "/Data/tmp"
+ "/Library/Caches"
+ "/Library/Containers/"
+ "/Library/Group Containers/"
+ "SMNWindowsSystemProfileAction"
+ "Skipping Group Container cache: %@"
+ "Skipping container cache/tmp: %@"
+ "Skipping dataless directory: %@"
+ "Skipping dataless file: %@"
+ "[SMNWirelessController] Attempting to start Soft-AP. SSID=%@, channel=%@"
+ "^\\/Library\\/Group Containers\\/[^\\/]+\\/Library\\/Caches\\/.*$"
+ "source will skip Group Container cache. path=%@"
+ "source will skip container cache/tmp. path=%@"
- "[SMNNetworkSession] ❌ Cannot promote connection with nil remoteAddresses"
- "[SMNWirelessController] Attempting to start Soft-AP. SSID=%@, password=%@, channel=%@"
- "^\\/Library\\/Group Containers\\/group\\.com\\.apple\\.CoreSpeech\\/Caches\\/.*$"
```
