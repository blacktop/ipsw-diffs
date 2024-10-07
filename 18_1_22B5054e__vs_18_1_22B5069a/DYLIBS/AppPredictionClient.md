## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-583.0.1.0.0
-  __TEXT.__text: 0x175dd0
+584.0.0.0.0
+  __TEXT.__text: 0x1762b4
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x16048
+  __TEXT.__objc_methlist: 0x16050
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1a348
+  __TEXT.__cstring: 0x1a468
   __TEXT.__oslogstring: 0x16598
-  __TEXT.__gcc_except_tab: 0x21e4
+  __TEXT.__gcc_except_tab: 0x21f8
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x6040
+  __TEXT.__unwind_info: 0x6058
   __TEXT.__objc_classname: 0x3810
-  __TEXT.__objc_methname: 0x310bf
+  __TEXT.__objc_methname: 0x310e1
   __TEXT.__objc_methtype: 0x64dd
   __TEXT.__objc_stubs: 0x1b3a0
   __DATA_CONST.__got: 0x1678

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94c0
+  __DATA_CONST.__objc_selrefs: 0x94c8
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xb70
   __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x26e0
-  __AUTH_CONST.__cfstring: 0x141a0
+  __AUTH_CONST.__cfstring: 0x141c0
   __AUTH_CONST.__objc_const: 0x44da0
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x6a8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9997
-  Symbols:   12225
-  CStrings:  12681
+  Functions: 10001
+  Symbols:   12230
+  CStrings:  12683
 
CStrings:
+ "SELECT timestamp, score, duration, suggestionId, suggestionMappingReason FROM timelineDonations WHERE extensionBundleId = :extensionBundleId AND widgetKind = :widgetKind AND containerBundleIdentifier = :containerBundleIdentifier AND suggestionMappingReason IS NOT NULL ORDER BY timestamp"
+ "fetchAllTimelineEntriesForWidget:"

```
