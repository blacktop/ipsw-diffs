## neagent

> `/usr/libexec/neagent`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2365.40.3.0.2
-  __TEXT.__text: 0x1adac
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x2680
-  __TEXT.__objc_methlist: 0x1210
+2365.60.12.0.0
+  __TEXT.__text: 0x1b0e8
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x2760
+  __TEXT.__objc_methlist: 0x1228
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x6bc
-  __TEXT.__objc_methname: 0x2efa
-  __TEXT.__oslogstring: 0x3fbd
-  __TEXT.__cstring: 0x195d
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__objc_methname: 0x2f8d
+  __TEXT.__oslogstring: 0x4046
+  __TEXT.__cstring: 0x18fd
   __TEXT.__objc_classname: 0x354
   __TEXT.__objc_methtype: 0xef8
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x5e8
   __DATA_CONST.__const: 0x690
-  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x1f0
-  __DATA.__objc_const: 0x2208
-  __DATA.__objc_selrefs: 0xd68
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_const: 0x2250
+  __DATA.__objc_selrefs: 0xda0
+  __DATA.__objc_ivar: 0x180
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 362
-  Symbols:   220
-  CStrings:  1189
+  Functions: 365
+  Symbols:   218
+  CStrings:  1197
 
Symbols:
- _NEGetConsoleUserUID
- _getpwuid
CStrings:
+ "%@ extension [%@] exited during the update, notify that extension failed"
+ "%@ update for extension [%@] did not complete within %d seconds"
+ "_appsUpdateTimer"
+ "_providerActiveAtUpdateStart"
+ "appsUpdateEnding"
+ "appsUpdateStarted"
+ "pluginType"
+ "queue"
+ "sendFailedTimer"
+ "setAppsUpdateEnding:"
+ "setAppsUpdateStarted:"
+ "setSendFailedTimer:"
- "/Library/Managed Preferences"
- "com.apple.networkextension.urlfilter.plist"
- "dictionaryWithContentsOfFile:"
- "urlfilterProfileEnabled"
```
