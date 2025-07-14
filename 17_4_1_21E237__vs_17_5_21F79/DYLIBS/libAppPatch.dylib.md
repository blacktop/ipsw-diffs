## libAppPatch.dylib

> `/usr/lib/libAppPatch.dylib`

```diff

-1270.102.7.0.0
-  __TEXT.__text: 0x13254
-  __TEXT.__auth_stubs: 0xd00
+1270.120.9.0.0
+  __TEXT.__text: 0x134dc
+  __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__cstring: 0x562a
+  __TEXT.__cstring: 0x568b
   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x23a
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__unwind_info: 0x31c
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x5a
   __TEXT.__objc_methname: 0x1654
   __TEXT.__objc_methtype: 0x3ed

   __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_classrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x3600
+  __AUTH_CONST.__cfstring: 0x3620
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x160
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65690434-1F86-3148-8C80-292F2EB83EAF
-  Functions: 205
-  Symbols:   886
-  CStrings:  1227
+  UUID: 64C40299-D300-35F0-A46C-685DED099DB2
+  Functions: 208
+  Symbols:   893
+  CStrings:  1230
 
Symbols:
+ _MILoadInfoPlistWithError
+ _MILoadRawInfoPlist
+ __CFBundleCopyInfoPlistURL
+ __CreateCFBundle
+ ___block_literal_global.105
- ___block_literal_global.121
CStrings:
+ "CFBundleGetInfoDictionary failed for bundle at %@"
+ "Error when introspecting %@"
+ "Expected Info.plist file at %@ but found something that was not a file."
+ "Failed to create CFBundle for %@"
+ "Failed to get Info.plist URL from %@; falling back to assumed path"
+ "MILoadInfoPlistWithError"
+ "_CreateCFBundle"
- "CFBundleGetInfoDictionary failed for bundle %@"
- "Error when introspecting %@ : %@"
- "Expected Info.plist file at %@ but found something else: %@"
- "Failed to create CFBundle from URL %@"
- "MILoadInfoPlist"

```
