## gamesaved

> `/usr/libexec/gamesaved`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__DATA.__objc_selrefs`

```diff

-102.0.4.0.0
-  __TEXT.__text: 0x2e4b8
+102.1.2.0.0
+  __TEXT.__text: 0x2f604
   __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x360
-  __TEXT.__const: 0xfd8
-  __TEXT.__cstring: 0x57a
-  __TEXT.__oslogstring: 0xedd
+  __TEXT.__objc_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x390
+  __TEXT.__const: 0xff8
+  __TEXT.__cstring: 0x59a
+  __TEXT.__oslogstring: 0xf1d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0x2ba
-  __TEXT.__objc_methname: 0xf5d
-  __TEXT.__objc_methtype: 0x66b
-  __TEXT.__constg_swiftt: 0x830
-  __TEXT.__swift5_typeref: 0x716
-  __TEXT.__swift5_fieldmd: 0x46c
+  __TEXT.__objc_classname: 0x2ea
+  __TEXT.__objc_methname: 0xfad
+  __TEXT.__objc_methtype: 0x53b
+  __TEXT.__constg_swiftt: 0x864
+  __TEXT.__swift5_typeref: 0x7b8
+  __TEXT.__swift5_fieldmd: 0x47c
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x4f2
-  __TEXT.__swift5_capture: 0x340
+  __TEXT.__swift5_capture: 0x394
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__swift_as_entry: 0xa4
-  __TEXT.__swift_as_ret: 0xe0
-  __TEXT.__swift_as_cont: 0x248
-  __TEXT.__unwind_info: 0xc70
-  __TEXT.__eh_frame: 0x2138
-  __DATA_CONST.__const: 0xe40
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift_as_entry: 0xa8
+  __TEXT.__swift_as_ret: 0xe4
+  __TEXT.__swift_as_cont: 0x24c
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__eh_frame: 0x21d0
+  __DATA_CONST.__const: 0xfa8
+  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__auth_ptr: 0x220
-  __DATA.__objc_const: 0x1548
+  __DATA_CONST.__auth_ptr: 0x228
+  __DATA.__objc_const: 0x14d0
   __DATA.__objc_selrefs: 0x410
-  __DATA.__objc_data: 0x430
-  __DATA.__data: 0x1018
-  __DATA.__common: 0x78
+  __DATA.__objc_data: 0x4e0
+  __DATA.__data: 0x10a8
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 680
-  Symbols:   467
-  CStrings:  351
+  Functions: 712
+  Symbols:   470
+  CStrings:  354
 
Symbols:
+ _$s10ObjectiveC8SelectorVMn
+ _OBJC_CLASS_$_FPXPCAutomaticErrorProxy
+ _OBJC_METACLASS_$_FPXPCAutomaticErrorProxy
CStrings:
+ "@\"NSProgress\"24@0:8@?<v@?@\"NSError\">16"
+ "@24@0:8@?16"
+ "@24@0:8^{_NSZone=}16"
+ "@52@0:8@16@24@32@40i48"
+ "@60@0:8@16@24@32@40i48@?52"
+ "@68@0:8@16@24@32@40i48@?52@?60"
+ "@?<v@?@\"FPXPCAutomaticErrorProxy\"@\"<NSCopying>\">32@?0@\"FPXPCAutomaticErrorProxy\"8:16@\"<NSCopying>\"24"
+ "Error connecting to the iWork collaboration service"
+ "Error creating the iWork collaboration proxy"
+ "GSFileProvideriWorkCollaboration"
+ "NSCopying"
+ "_TtC9gamesaved19AutomaticErrorProxy"
+ "com.apple.iWorkCollaboration"
+ "copyWithZone:"
+ "fetchLatestRevision(over:)"
+ "fetchLatestRevisionWithCompletionHandler:"
+ "iWork Collaboration Proxy"
+ "initWithConnection:protocol:orError:name:requestPid:"
+ "initWithConnection:protocol:orError:name:requestPid:requestWillBegin:"
+ "initWithConnection:protocol:orError:name:requestPid:requestWillBegin:requestDidBegin:"
+ "sanitizeErrors"
+ "v24@?0@\"FPXPCAutomaticErrorProxy\"8@\"<NSCopying>\"16"
+ "v40@?0@\"FPXPCAutomaticErrorProxy\"8:16@\"<NSCopying>\"24@\"NSProgress\"32"
- "@\"NSProgress\"40@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">32"
- "@\"NSProgress\"48@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24Q32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
- "@40@0:8@16@24@?32"
- "@48@0:8@16@24Q32@?40"
- "Error connecting to DocServerlessInterface"
- "ICDFileProviderClientSideCollaborationProtocol"
- "calculateCollaborationVersionForContents:reply:"
- "com.apple.CloudDocs.private.ClientSideCollaboration"
- "extractEtagsFromBaseVersion:withReply:"
- "fetchLatestRevisionIntoURL:reply:"
- "fetchLatestRevisionWithReply:"
- "uploadContents:baseVersion:options:reply:"
- "uploadContents:baseVersion:reply:"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"ICDCollaborationVersion\"@\"NSFileProviderItemVersion\"@\"NSError\">16"
- "v32@0:8@\"NSFileProviderItemVersion\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"ICDCollaborationVersion\"@\"NSError\">24"
- "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"NSURL\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@?0@\"ICDCollaborationVersion\"8@\"NSFileProviderItemVersion\"16@\"NSError\"24"
```
