## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-758.100.41.0.0
-  __TEXT.__text: 0x3f730
-  __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x1a50
+758.100.43.0.0
+  __TEXT.__text: 0x3ff50
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_methlist: 0x1a58
   __TEXT.__const: 0x5e0
-  __TEXT.__oslogstring: 0x3419
-  __TEXT.__cstring: 0x91cc
+  __TEXT.__oslogstring: 0x347a
+  __TEXT.__cstring: 0x92d3
   __TEXT.__gcc_except_tab: 0x1208
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0xa90
+  __TEXT.__unwind_info: 0xa98
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x4cf6
-  __TEXT.__objc_methtype: 0xc67
-  __TEXT.__objc_stubs: 0x4580
+  __TEXT.__objc_methname: 0x4d4d
+  __TEXT.__objc_methtype: 0xc92
+  __TEXT.__objc_stubs: 0x45a0
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x11c0
+  __DATA_CONST.__const: 0x11d0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1510
+  __DATA_CONST.__objc_selrefs: 0x1518
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xc60
-  __AUTH_CONST.__auth_got: 0xa30
+  __AUTH_CONST.__auth_got: 0xa38
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0xa3e0
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0xa520
   __AUTH_CONST.__objc_const: 0x36a0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x4b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 965
-  Symbols:   1625
-  CStrings:  2979
+  Functions: 969
+  Symbols:   1631
+  CStrings:  2993
 
Symbols:
+ _kOSALogCleanupOptionFilterByHeaders
+ _kOSALogCleanupOptionFilterByLogAge
+ _xpc_dictionary_set_double
CStrings:
+ "\"\x12"
+ "Connection error to %s: %s"
+ "Error creating log at %s/%s while purging: %@"
+ "Error deleting non-retirable log at %s/%s while purging: %@"
+ "Error retiring %s/%s while purging logs"
+ "Invalid XPC response from %s"
+ "Log age filter incorrectly formatted"
+ "Log cleanup request failed. Error: %s"
+ "Log cleanup request successfully completed"
+ "Log header filter incorrectly formatted"
+ "Not purging %s/%s: log did not meet criteria"
+ "OSALogCleanup"
+ "Unexpected reply from %s"
+ "cleanupLogs:withFilters:error:"
+ "filterByHeaders"
+ "filterByLogAge"
+ "purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:"
+ "v40@0:8@16@24^@32"
+ "v48@0:8@16r*24B32B36@?40"
- "\x12\x12"
- "Error creating log at %s while purging: %@"
- "Error deleting non-retirable log at %s while purging: %@"
- "Error retiring %s while purging logs"
- "opt-changed"
- "purgeLogs:"

```
