## SMS

> `/System/Library/Messages/PlugIns/SMS.imservice/SMS`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1491.200.101.2.5
-  __TEXT.__text: 0x10a50
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x2b20
-  __TEXT.__objc_methlist: 0xdd4
+1491.300.43.0.0
+  __TEXT.__text: 0x10a88
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__objc_methlist: 0xdb4
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x1184
-  __TEXT.__cstring: 0x650
-  __TEXT.__objc_methname: 0x4932
+  __TEXT.__cstring: 0x64d
+  __TEXT.__objc_methname: 0x4923
   __TEXT.__oslogstring: 0x1e7b
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methtype: 0x1b2f
+  __TEXT.__objc_methtype: 0x1aeb
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0x7f
-  __TEXT.__constg_swiftt: 0xb8
+  __TEXT.__constg_swiftt: 0xd0
   __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5b8
-  __DATA_CONST.__const: 0x5c0
+  __TEXT.__unwind_info: 0x5c0
+  __DATA_CONST.__const: 0x5c8
   __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x1180
-  __DATA.__objc_selrefs: 0x1040
+  __DATA.__objc_const: 0x1178
+  __DATA.__objc_selrefs: 0x1038
   __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x3d0
+  __DATA.__objc_data: 0x3d8
   __DATA.__data: 0x418
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 223
+  Functions: 224
   Symbols:   307
-  CStrings:  1026
+  CStrings:  1022
 
Symbols:
+ _swift_isaMask
- _objc_retain_x3
CStrings:
+ "cleanupFailedBuildForParts:"
+ "didReceiveError:forMessageID:forceError:account:submitMetric:"
+ "didReceiveError:forMessageID:forceError:submitMetric:"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@?<v@?@\"IMMessageItem\"B@\"NSArray\">16"
+ "v28@?0@\"IMMessageItem\"8B16@\"NSArray\"20"
+ "v44@0:8I16@20B28@32B40"
- "cleanupFailedBuildWithError:forParts:"
- "didReceiveError:forMessageID:forceError:"
- "didReceiveError:forMessageID:forceError:account:"
- "maxChatParticipantsForContext:"
- "q24@0:8@\"IMServiceReachabilityContext\"16"
- "q24@0:8@16"
- "v24@0:8@?<v@?@\"IMMessageItem\"B@\"NSArray\"I>16"
- "v28@0:8I16@\"NSArray\"20"
- "v28@0:8I16@20"
- "v32@?0@\"IMMessageItem\"8B16@\"NSArray\"20I28"
- "v40@0:8I16@20B28@32"
```
