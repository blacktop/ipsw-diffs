## authd

> `System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-61901.160.44.701.4
-  __TEXT.__text: 0x2d9fc
-  __TEXT.__auth_stubs: 0x14e0
+61901.160.44.702.5
+  __TEXT.__text: 0x2dde8
+  __TEXT.__auth_stubs: 0x14f0
   __TEXT.__objc_stubs: 0xd80
   __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0xb10
   __TEXT.__dlopen_cstrs: 0x2f6
-  __TEXT.__cstring: 0x3498
-  __TEXT.__gcc_except_tab: 0x10c0
-  __TEXT.__oslogstring: 0x54ac
+  __TEXT.__cstring: 0x3516
+  __TEXT.__gcc_except_tab: 0x10d8
+  __TEXT.__oslogstring: 0x55f0
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methname: 0xd4c
   __TEXT.__objc_methtype: 0x47f
   __TEXT.__unwind_info: 0x740
-  __DATA_CONST.__auth_got: 0xa80
-  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x2680
   __DATA_CONST.__cfstring: 0x1320

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 578
-  Symbols:   407
-  CStrings:  1245
+  Functions: 579
+  Symbols:   409
+  CStrings:  1253
 
Symbols:
+ __xpc_error_peer_code_signing_requirement
+ _xpc_connection_set_peer_code_signing_requirement
CStrings:
+ "agent: peer has to satisfy %{public}s"
+ "agent: the responder does not satisfy the required code identity"
+ "agent: unable to require the peer code identity %{public}s (%d)"
+ "com.apple.ahp"
+ "engine %llu: PAM service name contains invalid characters, ignoring it"
+ "engine %llu: client is not entitled to select the %{public}s PAM service, ignoring it"
+ "identifier \"com.apple.SecurityAgent\" and anchor apple"
+ "identifier \"com.apple.authorizationhost\" and anchor apple"
```
