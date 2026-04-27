## trustd

> `/usr/libexec/trustd`

```diff

-61901.120.60.0.0
-  __TEXT.__text: 0x69360
+61901.120.66.0.1
+  __TEXT.__text: 0x68534
   __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_stubs: 0x3200
   __TEXT.__objc_methlist: 0xd54
   __TEXT.__const: 0x5ab1
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__gcc_except_tab: 0xce0
-  __TEXT.__cstring: 0x7373
-  __TEXT.__oslogstring: 0x6787
+  __TEXT.__cstring: 0x735c
+  __TEXT.__oslogstring: 0x68b8
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x3062
+  __TEXT.__objc_methname: 0x3082
   __TEXT.__objc_methtype: 0xc75
-  __TEXT.__unwind_info: 0x1178
+  __TEXT.__unwind_info: 0x1148
   __DATA_CONST.__auth_got: 0x1228
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x4ea0
+  __DATA_CONST.__const: 0x4e38
   __DATA_CONST.__cfstring: 0x6840
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xe08
+  __DATA.__objc_selrefs: 0xe20
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x428
-  __DATA.__bss: 0x538
+  __DATA.__bss: 0x528
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D3F2FFB7-1E39-30B7-8CA9-DFCD3A4174FC
-  Functions: 1341
+  UUID: 69C238CC-59CA-328B-9467-0D8540BB8C04
+  Functions: 1325
   Symbols:   847
-  CStrings:  3229
+  CStrings:  3233
 
CStrings:
+ "allKeys"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/D93AE7DC-0DC2-4832-991B-73973CB4665B/TemporaryDirectory.sieAz1/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "minusSet:"
+ "policy_graph: anyPolicy in policy mapping at depth %d (cert %d), mapping %zu"
+ "policy_graph: empty graph and explicit_policy=0 at depth %d (cert %d)"
+ "policy_graph: failed to create mappings dictionary at depth %d (%zu mappings, limit %d)"
+ "policy_graph: failed to delete mapped policies at depth %d (cert %d)"
+ "policy_graph: failed to process policy mappings at depth %d (cert %d)"
+ "policy_graph: max nodes (%d) reached at depth %d"
+ "setWithArray:"
- "UsePolicyGraphVerifier"
- "com.apple.security.file./Library/Caches/com.apple.xbs/66E53E73-CC04-48CE-8389-7CCF296063B0/TemporaryDirectory.z7WZoN/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "policy mapping anyPolicy failure %u"
- "policy tree failure on cert %u"
- "policy tree failure on leaf"
- "policy: too many nodes"

```
