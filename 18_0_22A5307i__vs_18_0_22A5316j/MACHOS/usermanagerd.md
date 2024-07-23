## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-412.0.0.0.0
-  __TEXT.__text: 0xacc74
+414.0.0.0.0
+  __TEXT.__text: 0xace44
   __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0x2220
   __TEXT.__objc_methlist: 0x1064
   __TEXT.__const: 0x10e4
-  __TEXT.__gcc_except_tab: 0xde8
+  __TEXT.__gcc_except_tab: 0xe40
   __TEXT.__cstring: 0x66fe
   __TEXT.__objc_classname: 0x39a
-  __TEXT.__objc_methname: 0x340a
-  __TEXT.__objc_methtype: 0x128a
-  __TEXT.__oslogstring: 0x1076d
+  __TEXT.__objc_methname: 0x346d
+  __TEXT.__objc_methtype: 0x12c2
+  __TEXT.__oslogstring: 0x10770
   __TEXT.__unwind_info: 0x12c0
   __DATA_CONST.__auth_got: 0xc38
   __DATA_CONST.__got: 0x1e0

   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x5600
-  __DATA.__objc_selrefs: 0xbd8
+  __DATA.__objc_selrefs: 0xbe8
   __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0xa00
   __DATA.__data: 0x11d0

   - /usr/lib/libsandbox.1.dylib
   Functions: 1530
   Symbols:   458
-  CStrings:  3178
+  CStrings:  3182
 
CStrings:
+ "In UMSyncServer: bundleIdentifiersForPersona entitlement failure:%!d(MISSING)"
+ "In UMSyncServer: entitlement OK, but invalid bundleArray"
+ "In UMSyncServer: entitlement OK, calling bundleIdentifiersForPersona for profileInfo:%!@(MISSING) for pid:%!d(MISSING) with asid:%!d(MISSING)"
+ "In UMSyncServer: setBundlesIdentifiers for profileInfo:%!@(MISSING) for pid:%!d(MISSING) with asid:%!d(MISSING)"
+ "Update BundleIDS Succcess, new bundles:%!@(MISSING)"
+ "bundleIdentifiersForPersona:completionHandler:"
+ "setBundlesIdentifiers:forPersona:completionHandler:"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "In UMSyncServer: entitlement OK, calling fetchBundleIdentifiersForPersona for profileInfo:%!@(MISSING) for pid:%!d(MISSING) with asid:%!d(MISSING)"
- "In UMSyncServer: entitlement OK, calling fetchMultiPersonaBundleIDsList for pid:%!d(MISSING) with asid:%!d(MISSING)"
- "In UMSyncServer: fetchBundleIdentifiersForPersona entitlement failure:%!d(MISSING)"
- "fetchMultiPersonaBundleIdentifiersforPid Entitlement Failure for pid:%!d(MISSING)"

```
