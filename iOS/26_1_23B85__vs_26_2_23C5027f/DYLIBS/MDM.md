## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-55.42.6.0.0
-  __TEXT.__text: 0x55c44
+55.60.5.0.0
+  __TEXT.__text: 0x55c8c
   __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_methlist: 0x4194
   __TEXT.__const: 0x1aa
   __TEXT.__gcc_except_tab: 0x1130
   __TEXT.__cstring: 0x55a2
-  __TEXT.__oslogstring: 0x6ccc
+  __TEXT.__oslogstring: 0x6cfb
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F54DE948-A195-3346-98B1-F06E629AD129
+  UUID: 2E358D64-E65A-33A5-97D3-CB244A44F706
   Functions: 1646
   Symbols:   6652
-  CStrings:  4264
+  CStrings:  4265
 
Functions:
~ -[MDMServerCore migrateMDMWithContext:completion:] : 244 -> 316
CStrings:
+ "Device is on seed build. Skip the random delay"

```
