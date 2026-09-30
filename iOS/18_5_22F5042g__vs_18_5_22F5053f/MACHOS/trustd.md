## trustd

> `/usr/libexec/trustd`

```diff

-61439.120.15.0.0
-  __TEXT.__text: 0x5ea94
-  __TEXT.__auth_stubs: 0x23b0
+61439.120.22.0.0
+  __TEXT.__text: 0x5e948
+  __TEXT.__auth_stubs: 0x23c0
   __TEXT.__objc_stubs: 0x2d40
   __TEXT.__objc_methlist: 0xbf4
-  __TEXT.__const: 0x4771
+  __TEXT.__const: 0x5981
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x66ff
-  __TEXT.__oslogstring: 0x5879
+  __TEXT.__cstring: 0x66f9
+  __TEXT.__oslogstring: 0x584a
   __TEXT.__objc_classname: 0x194
   __TEXT.__objc_methname: 0x2cb2
   __TEXT.__objc_methtype: 0xae6
-  __TEXT.__unwind_info: 0x1038
-  __DATA_CONST.__auth_got: 0x11e8
+  __TEXT.__unwind_info: 0x1030
+  __DATA_CONST.__auth_got: 0x11f0
   __DATA_CONST.__got: 0x788
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4950
+  __DATA_CONST.__const: 0x4990
   __DATA_CONST.__cfstring: 0x5d60
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18

   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x3b0
-  __DATA.__bss: 0x4c8
+  __DATA.__bss: 0x4e0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1241
-  Symbols:   828
-  CStrings:  2152
+  Functions: 1243
+  Symbols:   829
+  CStrings:  2149
 
Symbols:
+ _SecCertificateCopyAppleExternalRoots
CStrings:
+ "OTATrust: failed to update from asset: %@"
+ "Using asset trust store %llu instead of system trust store %llu"
+ "Using supplementals asset v%llu instead of system v%llu"
+ "Using system trust store %llu instead of asset trust store %llu"
- "OTATrust: failed to update from asset after notification: %@"
- "OTATrust: failed to update from asset during periodic re-read: %@"
- "Using asset v%llu instead of system v%llu"
- "Using built-in constrained anchors"
- "Using built-in system anchors"
- "Using trust store version %llu from %s"
- "asset"

```
