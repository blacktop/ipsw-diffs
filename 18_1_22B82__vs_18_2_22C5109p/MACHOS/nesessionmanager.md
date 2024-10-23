## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2063.42.2.0.0
-  __TEXT.__text: 0x94b98
-  __TEXT.__auth_stubs: 0x1a50
-  __TEXT.__objc_stubs: 0x7240
-  __TEXT.__objc_methlist: 0x287c
-  __TEXT.__const: 0x130
+2063.60.13.502.1
+  __TEXT.__text: 0x96b1c
+  __TEXT.__auth_stubs: 0x1ae0
+  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__objc_methlist: 0x28cc
+  __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x1bf4
-  __TEXT.__oslogstring: 0xb8c1
-  __TEXT.__objc_methname: 0x81a6
-  __TEXT.__cstring: 0x4090
-  __TEXT.__objc_classname: 0x900
-  __TEXT.__objc_methtype: 0x1b8d
-  __TEXT.__unwind_info: 0x12d0
-  __DATA_CONST.__auth_got: 0xd38
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x19b0
+  __TEXT.__oslogstring: 0xbca1
+  __TEXT.__objc_methname: 0x83ae
+  __TEXT.__cstring: 0x4192
+  __TEXT.__objc_classname: 0x909
+  __TEXT.__objc_methtype: 0x1d49
+  __TEXT.__unwind_info: 0x12f8
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x1a10
   __DATA_CONST.__cfstring: 0x2240
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x76c8
-  __DATA.__objc_selrefs: 0x1dd0
-  __DATA.__objc_ivar: 0x628
-  __DATA.__objc_data: 0x12c0
+  __DATA.__objc_const: 0x7818
+  __DATA.__objc_selrefs: 0x1e40
+  __DATA.__objc_ivar: 0x63c
+  __DATA.__objc_data: 0x1310
   __DATA.__data: 0xc18
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
+  - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1555
-  Symbols:   629
-  CStrings:  3406
+  Functions: 1566
+  Symbols:   639
+  CStrings:  3461
 
Symbols:
+ _OBJC_CLASS_$_NEVPNApp
+ _ne_tracker_validate_domain
+ _ne_trie_has_high_ascii
+ _ne_trie_init
+ _ne_trie_insert
+ _ne_trie_search
+ _objc_copyStruct
+ _uidna_close
+ _uidna_nameToASCII_UTF8
+ _uidna_openUTS46
CStrings:
+ "\x16"
+ "%!@(MISSING) perApp VPN domain %!s(MISSING) <%!d(MISSING)>"
+ "%!@(MISSING): %!s(MISSING) - Added domain trie - ID %!l(MISSING)u %!@(MISSING)"
+ "%!@(MISSING): %!s(MISSING) - Deleted domain trie - ID %!l(MISSING)u %!@(MISSING)"
+ "%!@(MISSING): %!s(MISSING) - Failed to add domain trie"
+ "%!@(MISSING): %!s(MISSING) - Failed to delete domain trie - ID %!l(MISSING)u"
+ "%!@(MISSING): %!s(MISSING) - deleting all IDs %!@(MISSING)"
+ "%!@(MISSING): %!s(MISSING) - failed to build domain trie"
+ "-[NESMPolicyMasterSession addDomainTrieWithData:matchSigningIdentifier:]"
+ "-[NESMPolicyMasterSession removeAllDomainTries]"
+ "-[NESMPolicyMasterSession removeDomainTrieWithID:ids:]"
+ "-[NESMPolicySession getDomainTrie:matchSigningIdentifier:appRules:masterSession:]"
+ "@48@0:8@16i24B28B32c36Q40"
+ "Added domain trie of length %!z(MISSING)u <id %!l(MISSING)u>"
+ "B28@0:8r*16i24"
+ "Failed to add domain trie: [%!d(MISSING)] %!s(MISSING)"
+ "Failed to puny-code domain"
+ "Failed to punycode label - uidna_nameToASCII_UTF8(%!s(MISSING)) failed errorCode %!d(MISSING)"
+ "Failed to punycode label - uidna_nameToASCII_UTF8(%!s(MISSING)) failed info.errors 0x%!X(MISSING)"
+ "NETrie"
+ "NETrie - No domain"
+ "NETrie - dealloc"
+ "NETrie - dealloc - free memory"
+ "NETrie - failed init"
+ "NETrie - failed insert for %!@(MISSING)"
+ "NETrie - high ASCII detected <%!@(MISSING)>"
+ "NETrie - high ASCII detected <%!s(MISSING)>"
+ "NETrie - initialized with %!d(MISSING) domains (Nodes used = %!d(MISSING), child maps used = %!d(MISSING), bytes used = %!d(MISSING), root = %!d(MISSING))"
+ "T{ne_trie=QQ^{ne_trie_node}^S*^vSSSSSSSQQQQBd},V_trie"
+ "_necpTrieIDs"
+ "_partialSearchAllowed"
+ "_partialSearchTerminator"
+ "_reverse"
+ "_trie"
+ "addDomainTrieWithData:"
+ "c"
+ "commonPrefixWithString:options:"
+ "compareAppRules:newAppRules:noExistingDomain:"
+ "domainFilter:"
+ "findRuleWithSameDomains:matchSigningIdentifier:startIndex:"
+ "initWithBytes:length:"
+ "initWithDomains:prefixCount:reverse:partialSearchAllowed:partialSearchTerminator:extra_bytes:"
+ "keyEnumerator"
+ "lowercaseString"
+ "perApp VPN domain - Derived %!l(MISSING)u unique prefixes, %!l(MISSING)u unique domains, %!l(MISSING)u reversed domains, %!l(MISSING)u total bytes"
+ "perApp VPN domain - puny-coded %!s(MISSING) -> %!s(MISSING)"
+ "perApp VPN domain - puny-coding %!s(MISSING) <%!d(MISSING)>"
+ "removeDomainTrieWithID:"
+ "search:length:"
+ "searchWithString:"
+ "setTrie:"
+ "trie"
+ "v128@0:8{ne_trie=QQ^{ne_trie_node}^S*^vSSSSSSSQQQQBd}16"
+ "{ne_trie=\"magic\"Q\"version\"Q\"nodes\"^{ne_trie_node}\"child_maps\"^S\"bytes\"*\"memory\"^v\"nodes_count\"S\"child_maps_count\"S\"bytes_count\"S\"nodes_free_next\"S\"child_maps_free_next\"S\"bytes_free_next\"S\"root\"S\"trie_memory_size\"Q\"nodes_mem_size\"Q\"child_maps_mem_size\"Q\"bytes_mem_size\"Q\"is_mmap\"B\"timestamp\"d}"
+ "{ne_trie=QQ^{ne_trie_node}^S*^vSSSSSSSQQQQBd}16@0:8"

```
