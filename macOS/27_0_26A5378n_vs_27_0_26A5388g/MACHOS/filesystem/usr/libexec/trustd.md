## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x5dd38
-  __TEXT.__auth_stubs: 0x2340
-  __TEXT.__objc_stubs: 0x33a0
-  __TEXT.__objc_methlist: 0xe0c
+62460.0.55.0.1
+  __TEXT.__text: 0x5c448
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0xdf4
   __TEXT.__const: 0xbc60
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__objc_classname: 0x1ce
-  __TEXT.__objc_methname: 0x2ff5
-  __TEXT.__objc_methtype: 0xc79
+  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__objc_methname: 0x2f6a
+  __TEXT.__objc_methtype: 0xc5d
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__swift5_reflstr: 0x4
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xc0c
-  __TEXT.__cstring: 0x5988
-  __TEXT.__oslogstring: 0x5c91
-  __TEXT.__unwind_info: 0x1078
-  __DATA_CONST.__const: 0x47c8
-  __DATA_CONST.__cfstring: 0x5700
+  __TEXT.__gcc_except_tab: 0xbc0
+  __TEXT.__cstring: 0x5bee
+  __TEXT.__oslogstring: 0x5c4e
+  __TEXT.__unwind_info: 0x1040
+  __DATA_CONST.__const: 0x4308
+  __DATA_CONST.__cfstring: 0x5820
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11b0
-  __DATA_CONST.__got: 0x900
+  __DATA_CONST.__auth_got: 0x11a0
+  __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1758
-  __DATA.__objc_selrefs: 0xe68
+  __DATA.__objc_const: 0x1750
+  __DATA.__objc_selrefs: 0xe40
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
-  __DATA.__data: 0x488
+  __DATA.__data: 0x428
   __DATA.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1292
-  Symbols:   874
-  CStrings:  2156
+  Functions: 1263
+  Symbols:   869
+  CStrings:  2165
 
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
+ "com.apple.security.file./AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ilRCzf/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "doSQLite:"
+ "v16@?0^{__SecRevocationDb=BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
+ "v16@?0^{sqlite3=}8"
+ "validupdate: Failed to allocate revocation db cache"
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
- "com.apple.security.file./AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ih6abw/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "com.apple.trustdFileHelper"
- "failed to ceate %{public}@ connection"
- "failed to fix files; caught exception: %@"
- "failed to talk to %{public}@: %@"
- "fixFiles:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "setRemoteObjectInterface:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "trustdFileHelper"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "validupdate: Failed to create db at \"%@\""
```
