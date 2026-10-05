## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-256.0.1.0.0
-  __TEXT.__text: 0x628e0
-  __TEXT.__objc_methlist: 0x1f2c
-  __TEXT.__const: 0x1250
-  __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__cstring: 0x2a8f
+258.0.0.0.0
+  __TEXT.__text: 0x62bbc
+  __TEXT.__objc_methlist: 0x1f44
+  __TEXT.__const: 0x1240
+  __TEXT.__gcc_except_tab: 0x6d0
+  __TEXT.__cstring: 0x2abf
   __TEXT.__ustring: 0x84
-  __TEXT.__oslogstring: 0x6cff
+  __TEXT.__oslogstring: 0x6d4f
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__swift5_typeref: 0xe18
   __TEXT.__swift5_reflstr: 0x31e

   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__unwind_info: 0x1a48
-  __TEXT.__eh_frame: 0x17e0
+  __TEXT.__unwind_info: 0x1a58
+  __TEXT.__eh_frame: 0x1808
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a70
+  __DATA_CONST.__objc_selrefs: 0x1a80
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2314
-  Symbols:   2086
-  CStrings:  833
+  Functions: 2316
+  Symbols:   2088
+  CStrings:  836
 
Symbols:
+ -[CCRapportManager _isFileTransferSessionPossibleWithPeer:error:]
+ -[CCRapportManager _peerHasIPLink:]
+ -[CCRapportManager _statusFlagsUnionForPeer:matchedDeviceCount:]
- -[CCRapportManager _isFileTransferSessionPossible:]
CStrings:
+ " no"
+ "%@ active device statusFlags: 0x%llx"
+ "%@ has%s IP link (%lu active device(s))"
+ "No transport available for a Rapport FileTransferSession"
- "WiFi is off"
```
