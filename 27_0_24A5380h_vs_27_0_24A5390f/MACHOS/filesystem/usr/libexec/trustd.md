## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x5a36c
-  __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x3340
-  __TEXT.__objc_methlist: 0xe0c
+62460.0.55.0.1
+  __TEXT.__text: 0x58e00
+  __TEXT.__auth_stubs: 0x2380
+  __TEXT.__objc_stubs: 0x32a0
+  __TEXT.__objc_methlist: 0xdf4
   __TEXT.__const: 0xbd90
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x2f93
-  __TEXT.__objc_methtype: 0xc79
+  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__objc_methname: 0x2f08
+  __TEXT.__objc_methtype: 0xc5d
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__swift5_reflstr: 0x4
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__cstring: 0x5d3f
-  __TEXT.__oslogstring: 0x5b59
-  __TEXT.__unwind_info: 0x1028
-  __DATA_CONST.__const: 0x41a0
-  __DATA_CONST.__cfstring: 0x5a40
+  __TEXT.__gcc_except_tab: 0xab8
+  __TEXT.__cstring: 0x5fa4
+  __TEXT.__oslogstring: 0x5b4b
+  __TEXT.__unwind_info: 0xff8
+  __DATA_CONST.__const: 0x3da0
+  __DATA_CONST.__cfstring: 0x5b80
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11e0
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__auth_got: 0x11d0
+  __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1758
-  __DATA.__objc_selrefs: 0xe50
+  __DATA.__objc_const: 0x1750
+  __DATA.__objc_selrefs: 0xe28
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
-  __DATA.__data: 0x458
+  __DATA.__data: 0x3f8
   __DATA.__bss: 0x520
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1220
-  Symbols:   886
-  CStrings:  2169
+  Functions: 1197
+  Symbols:   881
+  CStrings:  2179
 
Symbols:
+ _SecFixTrustdFilePermissions
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_EHTYPE_id
- _objc_begin_catch
- _objc_end_catch
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@: sqlite3 rc=%d: %s"
+ "(null)"
+ "B16@?0^{sqlite3=}8"
+ "ValidCacheFiles"
+ "_SecRevocationDbCertHashInGroup bind"
+ "_SecRevocationDbCertHashInGroup failed: rc=%d"
+ "_SecRevocationDbCertHashInGroup prepare"
+ "_SecRevocationDbCertHashInGroup step"
+ "_SecRevocationDbCopyDateConstraints bind"
+ "_SecRevocationDbCopyDateConstraints failed: rc=%d"
+ "_SecRevocationDbCopyDateConstraints prepare"
+ "_SecRevocationDbCopyDateConstraints step"
+ "_SecRevocationDbCopyUpdateSource failed: rc=%d"
+ "_SecRevocationDbGetGroupFormat bind"
+ "_SecRevocationDbGetGroupFormat prepare"
+ "_SecRevocationDbGetGroupFormat step"
+ "_SecRevocationDbGetLocalGeneration failed: rc=%d"
+ "_SecRevocationDbGetVersion failed: rc=%d"
+ "_SecRevocationDbGroupIdForIssuerHash bind"
+ "_SecRevocationDbGroupIdForIssuerHash failed: rc=%d"
+ "_SecRevocationDbGroupIdForIssuerHash prepare"
+ "_SecRevocationDbGroupIdForIssuerHash step"
+ "_SecRevocationDbReadSchemaVersionFromDb failed: rc=%d"
+ "_SecRevocationDbSerialInGroup bind"
+ "_SecRevocationDbSerialInGroup bind retry"
+ "_SecRevocationDbSerialInGroup failed: rc=%d"
+ "_SecRevocationDbSerialInGroup prepare"
+ "_SecRevocationDbSerialInGroup prepare retry"
+ "_SecRevocationDbSerialInGroup retry failed: rc=%d"
+ "_SecRevocationDbSerialInGroup step"
+ "_SecRevocationDbSerialInGroup step retry"
+ "doSQLite:"
+ "failed to stat valid db: %s"
+ "v16@?0^{__SecRevocationDb=BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
+ "v16@?0^{sqlite3=}8"
+ "validupdate: Failed to allocate revocation db cache"
+ "wrong owner for valid db"
- "%s"
- "%{public}@ failed to fix our files: %@"
- "B24@?0^{__SecRevocationDbConnection=^{__SecRevocationDb}^{__OpaqueSecDbConnection}qq}8^^{__CFError}16"
- "TrustdFileHelper_protocol"
- "_SecRevocationDbCertHashInGroup failed: %@"
- "_SecRevocationDbCopyDateConstraints failed: %@"
- "_SecRevocationDbCopyUpdateSource failed: %@"
- "_SecRevocationDbGetLocalGeneration failed: %@"
- "_SecRevocationDbGetVersion failed: %@"
- "_SecRevocationDbGroupIdForIssuerHash failed: %@"
- "_SecRevocationDbReadSchemaVersionFromDb failed: %@"
- "_SecRevocationDbSerialInGroup failed: %@"
- "com.apple.securityuploadd"
- "failed to ceate %{public}@ connection"
- "failed to fix files; caught exception: %@"
- "failed to talk to %{public}@: %@"
- "fixFiles:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "securityuploadd"
- "setRemoteObjectInterface:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "validupdate: Failed to create db at \"%@\""
```
