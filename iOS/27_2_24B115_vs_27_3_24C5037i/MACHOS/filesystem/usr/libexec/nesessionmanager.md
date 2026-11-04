## nesessionmanager

> `/usr/libexec/nesessionmanager`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2365.40.3.0.2
-  __TEXT.__text: 0xb7378
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_stubs: 0x8c20
-  __TEXT.__objc_methlist: 0x3fe4
+2365.60.12.0.0
+  __TEXT.__text: 0xb7924
+  __TEXT.__auth_stubs: 0x1e20
+  __TEXT.__objc_stubs: 0x8ce0
+  __TEXT.__objc_methlist: 0x3ffc
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x23f4
-  __TEXT.__objc_methname: 0x9d7c
-  __TEXT.__oslogstring: 0x11b5b
-  __TEXT.__cstring: 0x5e08
+  __TEXT.__gcc_except_tab: 0x2414
+  __TEXT.__objc_methname: 0x9e7f
+  __TEXT.__oslogstring: 0x11be4
+  __TEXT.__cstring: 0x5da8
   __TEXT.__objc_classname: 0xbc4
   __TEXT.__objc_methtype: 0x22b4
-  __TEXT.__unwind_info: 0x1e48
+  __TEXT.__unwind_info: 0x1e58
   __DATA_CONST.__const: 0x1e88
-  __DATA_CONST.__cfstring: 0x2b20
+  __DATA_CONST.__cfstring: 0x2ac0
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0xf28
+  __DATA_CONST.__auth_got: 0xf20
   __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x8780
-  __DATA.__objc_selrefs: 0x26c8
-  __DATA.__objc_ivar: 0x7fc
+  __DATA.__objc_const: 0x8808
+  __DATA.__objc_selrefs: 0x26f8
+  __DATA.__objc_ivar: 0x80c
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0x1040
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1970
-  Symbols:   714
-  CStrings:  4369
+  Functions: 1974
+  Symbols:   713
+  CStrings:  4378
 
Symbols:
- _getpwuid
CStrings:
+ "%@ extension [%@] exited during the update, notify that extension failed"
+ "%@ update for extension [%@] did not complete within %d seconds"
+ "_appsUpdateTimer"
+ "_pluginPathRulesExpandedForUID"
+ "_providerActiveAtUpdateStart"
+ "_providerStartRetryPending"
+ "appsUpdateEnding"
+ "appsUpdateStarted"
+ "scopeSocketToInterfaceNameWithFlags:flags:"
+ "sendFailedTimer"
+ "setAppsUpdateEnding:"
+ "setAppsUpdateStarted:"
+ "setSendFailedTimer:"
+ "tunnelIPToInterfaceNameWithFlags:secondaryResultType:flags:"
- "/Library/Managed Preferences"
- "com.apple.networkextension.urlfilter.plist"
- "dictionaryWithContentsOfFile:"
- "stringByAppendingPathComponent:"
- "urlfilterProfileEnabled"
```
