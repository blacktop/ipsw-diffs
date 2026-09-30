## nanoprefsyncd

> `/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd`

```diff

-320.0.0.0.0
-  __TEXT.__text: 0x25a7c
+321.0.0.0.0
+  __TEXT.__text: 0x25bc4
   __TEXT.__auth_stubs: 0xa70
   __TEXT.__objc_stubs: 0x3580
   __TEXT.__objc_methlist: 0x207c
-  __TEXT.__cstring: 0x213b
+  __TEXT.__cstring: 0x2178
   __TEXT.__objc_methname: 0x5b5e
   __TEXT.__objc_classname: 0x2ec
   __TEXT.__objc_methtype: 0xfa9
   __TEXT.__const: 0xe0
-  __TEXT.__oslogstring: 0x37c0
+  __TEXT.__oslogstring: 0x37f7
   __TEXT.__gcc_except_tab: 0x6c8
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__unwind_info: 0x6a0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AA2C715D-1FCA-338C-8E32-38295BFC361A
+  UUID: 614E6CD8-E954-339A-8DDB-A64B2485746F
   Functions: 713
   Symbols:   327
-  CStrings:  1770
+  CStrings:  1772
 
Functions:
~ sub_100006fb4 : 628 -> 956
CStrings:
+ "%s: Doing a sync because of a build version change (KVO)"
+ "-[NPSServer observeValueForKeyPath:ofObject:change:context:]"
+ "Launching; \"NanoPreferencesSyncDaemon-321\" \"10\""
- "Launching; \"NanoPreferencesSyncDaemon-320\" \"1697\""

```
