## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-1444.5.3.0.0
-  __TEXT.__text: 0x23c058
+1444.5.4.0.0
+  __TEXT.__text: 0x23c17c
   __TEXT.__auth_stubs: 0x3c90
   __TEXT.__objc_methlist: 0xdb2c
   __TEXT.__const: 0xa40
   __TEXT.__cstring: 0x2fde5
-  __TEXT.__oslogstring: 0x1f241
-  __TEXT.__gcc_except_tab: 0x32b78
+  __TEXT.__oslogstring: 0x1f2fb
+  __TEXT.__gcc_except_tab: 0x32bb4
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
   __TEXT.__unwind_info: 0xd178

   - /usr/lib/system/libxpc.dylib
   Functions: 10359
   Symbols:   18170
-  CStrings:  12770
+  CStrings:  12772
 
Functions:
~ __ZL25_LSLaunchWithRunningboardP9LSContextP6FSNodejPvPK9__CFArrayPK6AEDescS9_P7NSArrayIP11LSSliceInfoEPK14__CFDictionaryjPK13audit_token_tPK15_LSOpen2OptionsP19ProcessSerialNumberPU15__autoreleasingP7NSError : 43816 -> 44108
CStrings:
+ "LAUNCH: Attempting to validate the bundle path, and failed to determine execPath %{private}s"
+ "LAUNCH: Attempting to validate the bundle path, and failed to determine nodePath %{private}s"
```
