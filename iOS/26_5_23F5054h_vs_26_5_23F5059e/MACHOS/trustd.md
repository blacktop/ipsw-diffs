## trustd

> `/usr/libexec/trustd`

```diff

-61901.120.56.0.1
-  __TEXT.__text: 0x6940c
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_stubs: 0x3160
+61901.120.60.0.0
+  __TEXT.__text: 0x69360
+  __TEXT.__auth_stubs: 0x2430
+  __TEXT.__objc_stubs: 0x31a0
   __TEXT.__objc_methlist: 0xd54
   __TEXT.__const: 0x5ab1
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__gcc_except_tab: 0xc20
-  __TEXT.__cstring: 0x7357
-  __TEXT.__oslogstring: 0x676b
+  __TEXT.__gcc_except_tab: 0xce0
+  __TEXT.__cstring: 0x7373
+  __TEXT.__oslogstring: 0x6787
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x3030
+  __TEXT.__objc_methname: 0x3062
   __TEXT.__objc_methtype: 0xc75
-  __TEXT.__unwind_info: 0x1170
-  __DATA_CONST.__auth_got: 0x1218
-  __DATA_CONST.__got: 0x7c8
+  __TEXT.__unwind_info: 0x1178
+  __DATA_CONST.__auth_got: 0x1228
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x4ea0
   __DATA_CONST.__cfstring: 0x6840

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_selrefs: 0xe08
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x428

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 28EAAF74-D560-3F8C-B4F0-03BFF73E273B
-  Functions: 1339
-  Symbols:   844
-  CStrings:  3225
+  UUID: D3F2FFB7-1E39-30B7-8CA9-DFCD3A4174FC
+  Functions: 1341
+  Symbols:   847
+  CStrings:  3229
 
Symbols:
+ _CFStringCreateWithBytesNoCopy
+ __CFCopySystemVersionDictionary
+ __kCFSystemVersionBuildVersionKey
CStrings:
+ "0123456789ABCDEF"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/66E53E73-CC04-48CE-8389-7CCF296063B0/TemporaryDirectory.z7WZoN/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "stringWithContentsOfFile:"
+ "trigger downgrade from gen8"
+ "valid-downgrade"
+ "writeToFile:atomically:"
- "%02X"
- "com.apple.security.file./Library/Caches/com.apple.xbs/7BD9B574-B86B-4AA5-8A5B-46D03238BB9C/TemporaryDirectory.iStmIC/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"

```
