## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.40.45.0.1
-  __TEXT.__text: 0x167ed0
-  __TEXT.__auth_stubs: 0x3d40
-  __TEXT.__objc_methlist: 0x4880
+61439.40.54.0.0
+  __TEXT.__text: 0x168cc8
+  __TEXT.__auth_stubs: 0x3d50
+  __TEXT.__objc_methlist: 0x48e8
   __TEXT.__const: 0x9b38
-  __TEXT.__cstring: 0x175df
-  __TEXT.__gcc_except_tab: 0x8c48
-  __TEXT.__oslogstring: 0xebd4
+  __TEXT.__cstring: 0x1768d
+  __TEXT.__gcc_except_tab: 0x8c90
+  __TEXT.__oslogstring: 0xece8
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5d18
-  __TEXT.__objc_classname: 0xa03
-  __TEXT.__objc_methname: 0xaa28
-  __TEXT.__objc_methtype: 0x32a1
-  __TEXT.__objc_stubs: 0x7ec0
+  __TEXT.__unwind_info: 0x5d40
+  __TEXT.__objc_classname: 0xa06
+  __TEXT.__objc_methname: 0xab10
+  __TEXT.__objc_methtype: 0x32f1
+  __TEXT.__objc_stubs: 0x7f20
   __DATA_CONST.__got: 0x700
-  __DATA_CONST.__const: 0x11b78
+  __DATA_CONST.__const: 0x11bf0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bc0
+  __DATA_CONST.__objc_selrefs: 0x2c00
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x1eb8
+  __AUTH_CONST.__auth_got: 0x1ec0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x4320
-  __AUTH_CONST.__cfstring: 0x14bc0
-  __AUTH_CONST.__objc_const: 0x9e50
+  __AUTH_CONST.__cfstring: 0x14d60
+  __AUTH_CONST.__objc_const: 0x9ed0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH.__objc_data: 0x19f0
   __AUTH.__data: 0xd10
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x48
-  __DATA.__objc_ivar: 0x518
+  __DATA.__objc_ivar: 0x51c
   __DATA.__data: 0x20c0
   __DATA.__bss: 0x9e8
   __DATA.__common: 0x18

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6582
-  Symbols:   9169
-  CStrings:  7822
+  Functions: 6594
+  Symbols:   9181
+  CStrings:  7852
 
Symbols:
+ _PBDataWriterWriteInt32Field
CStrings:
+ "hardfail"
+ "{?=\"repeatAfterSeconds\"b1\"eventClass\"b1}"
+ "SFA: underlyingErrors failed to encode %!{(MISSING)public}@ with failure: %!{(MISSING)public}@"
+ "Errors"
+ "setHasEventClass:"
+ "\x11\x13"
+ "Ti,N,V_eventClass"
+ "hasEventClass"
+ "clique-perform-ckserver-unreadable-data-removal"
+ "shouldRatelimit:rule:"
+ "setEventClass:"
+ "B32@0:8@\"SFAnalytics\"16@\"SFAnalyticsMatchingRule\"24"
+ "StringAsEventClass:"
+ "clique-perform-ckserver-unreadable-data-removal: unable to create otcontrol: %!@(MISSING)"
+ "eventType not a string"
+ "unknown eventclass: %!@(MISSING)"
+ "Note"
+ "clique-perform-ckserver-unreadable-data-removal: failed to remove data from ckserver: %!@(MISSING)"
+ "_eventClass"
+ "HardFailure"
+ "performCKServerUnreadableDataRemoval:error:"
+ "matchAttributes:eventClass:"
+ "note"
+ "Success"
+ "removed unreadable data from ckserver"
+ "eventClassAsString:"
+ "B32@0:8@16q24"
+ "softfail"
+ "SFA: underlyingErrors encoded to not json %!{(MISSING)public}@"
+ "SoftFailure"
+ "All"
+ "Rockwell"
+ "performCKServerUnreadableDataRemoval:reply:"
- "SFA: underlyingErrors failed to encode %!@(MISSING) with failure: %!@(MISSING)"
- "{?=\"repeatAfterSeconds\"b1}"
- "shouldRatelimit:"
- "matchAttributes:"

```
