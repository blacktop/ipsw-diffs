## neagent

> `/usr/libexec/neagent`

```diff

-2205.40.9.0.0
-  __TEXT.__text: 0x151f0
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0x1008
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__objc_methname: 0x244e
-  __TEXT.__oslogstring: 0x2fdf
-  __TEXT.__cstring: 0x10c4
-  __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methtype: 0xd9f
-  __TEXT.__unwind_info: 0x370
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x500
+2205.40.18.0.0
+  __TEXT.__text: 0x15ce4
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x1030
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__objc_methname: 0x248e
+  __TEXT.__oslogstring: 0x31a3
+  __TEXT.__cstring: 0x10d0
+  __TEXT.__objc_classname: 0x32d
+  __TEXT.__objc_methtype: 0xdda
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x550
   __DATA_CONST.__cfstring: 0x460
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x1d28
-  __DATA.__objc_selrefs: 0xa48
-  __DATA.__objc_ivar: 0x138
-  __DATA.__objc_data: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA.__objc_const: 0x1e20
+  __DATA.__objc_selrefs: 0xa50
+  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x840
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCE23CF2-76E3-3FD3-B2F0-5106DDCFE3F8
-  Functions: 305
-  Symbols:   177
-  CStrings:  954
+  UUID: 005AF24B-14C9-3BB1-955F-AF22DB3FA9ED
+  Functions: 309
+  Symbols:   183
+  CStrings:  967
 
Symbols:
+ _OBJC_CLASS_$_NSSet
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_retain_x28
CStrings:
+ "%s: URLCHECK: FINAL RESULT: BATCH ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH BLOCKED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: BATCH BLOCKED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSSet\""
+ "NEAgentSession: failed to initialize the delegate, shouldDisable %d"
+ "NEPIRBatchGroup"
+ "_dispatchGroup"
+ "_pending_urls"
+ "_requestBatchGroups"
+ "initWithArray:"
+ "v16@?0B8B12"
+ "v24@0:8@?<v@?BB>16"
- "NEAgentSession: failed to initialize the delegate"

```
