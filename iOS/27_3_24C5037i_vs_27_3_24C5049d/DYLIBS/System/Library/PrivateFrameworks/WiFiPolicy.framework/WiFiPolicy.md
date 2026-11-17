## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1079.2.0.0.0
-  __TEXT.__text: 0xe0e38
+1079.4.0.0.0
+  __TEXT.__text: 0xe0ec8
   __TEXT.__objc_methlist: 0x13eb0
   __TEXT.__const: 0x888
-  __TEXT.__cstring: 0x25e6b
+  __TEXT.__cstring: 0x25e9b
   __TEXT.__oslogstring: 0x550e
   __TEXT.__gcc_except_tab: 0x190c
   __TEXT.__dlopen_cstrs: 0xa8

   __DATA_CONST.__objc_arraydata: 0x1550
   __DATA_CONST.__got: 0xbc0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x20ee0
+  __AUTH_CONST.__cfstring: 0x20f20
   __AUTH_CONST.__objc_const: 0x25c20
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1aa0

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 7246
   Symbols:   12042
-  CStrings:  5332
+  CStrings:  5334
 
Symbols:
+ -[WiFiUsageMonitor appendAppleMeshFieldsToDict:isMeshEligibleNetwork:]
- -[WiFiUsageMonitor appendAppleMeshFieldsToDict:]
Functions:
~ -[WiFiUsageMonitor submitLqmToCA:forInterface:] : 2008 -> 2036
~ -[WiFiUsageMonitor appendAppleMeshFieldsToDict:] -> -[WiFiUsageMonitor appendAppleMeshFieldsToDict:isMeshEligibleNetwork:] : 396 -> 512
CStrings:
+ "foundMeshCandidate"
+ "meshCandidateCount"
```
