## trustd

> `/usr/libexec/trustd`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x5e9a0
-  __TEXT.__auth_stubs: 0x23c0
+61901.0.9.0.1
+  __TEXT.__text: 0x5f978
+  __TEXT.__auth_stubs: 0x23e0
   __TEXT.__objc_stubs: 0x2d40
-  __TEXT.__objc_methlist: 0xbf4
-  __TEXT.__const: 0x5981
+  __TEXT.__objc_methlist: 0xc0c
+  __TEXT.__const: 0x59a1
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x66f9
-  __TEXT.__oslogstring: 0x584a
+  __TEXT.__cstring: 0x67c1
+  __TEXT.__oslogstring: 0x5a8e
   __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2cb2
+  __TEXT.__objc_methname: 0x2ccd
   __TEXT.__objc_methtype: 0xae6
-  __TEXT.__unwind_info: 0x1030
-  __DATA_CONST.__auth_got: 0x11f0
-  __DATA_CONST.__got: 0x788
+  __TEXT.__unwind_info: 0x1050
+  __DATA_CONST.__auth_got: 0x1200
+  __DATA_CONST.__got: 0x798
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4990
-  __DATA_CONST.__cfstring: 0x5d60
+  __DATA_CONST.__const: 0x4a38
+  __DATA_CONST.__cfstring: 0x5e40
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x3b0
-  __DATA.__bss: 0x4e0
+  __DATA.__bss: 0x500
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 448BF9BB-866D-3B25-A074-D85081D6E77D
-  Functions: 1243
-  Symbols:   829
-  CStrings:  2889
+  UUID: 122D41B6-9A64-3756-BB60-8C754D8CB0CF
+  Functions: 1254
+  Symbols:   833
+  CStrings:  2923
 
Symbols:
+ _CFDataGetBytes
+ _SecPolicyCheckCertURI
+ _kSecPolicyCheckRootMarkerOid
+ _kSecPolicyCheckURI
CStrings:
+ ";"
+ "AppAnchor|"
+ "AppleAnchor|"
+ "EXPLAIN QUERY PLAN "
+ "EXPLAIN QUERY PLAN for \"%s\":"
+ "EarlyAnchorExpiration"
+ "Failed to get query plan"
+ "Failed to show plan: %@"
+ "Malformed anchor record, cert hash not a string: %{public}@"
+ "Malformed anchor record, no cert for hash: %{public}@"
+ "Malformed anchor record, not a dictionary: %{public}@"
+ "Malformed anchor record, oids not an array: %{public}@"
+ "Malformed anchor record, type not a string: %{public}@"
+ "Malformed anchor records, not an array"
+ "SecDbVerboseDatabaseLogging"
+ "SystemAnchor|"
+ "Unable to finalize query: %d"
+ "Unable to prepare query: %d"
+ "UpdateTokenItemsForSystemKeychain"
+ "UserAnchor|"
+ "WARNING: Upcoming anchor expiration: %@. Evaluated by %@ against %@ using %@.\n%@"
+ "anchorCache"
+ "anchorRecordsPermitttedForPolicy:policyId:"
+ "com.apple."
+ "earlyExpiration"
+ "item"
+ "query plan: %s"
+ "unknown anchor type: %{public}@"
- "getBytes:range:"

```
