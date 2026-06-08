## TeaState

> `/System/Library/PrivateFrameworks/TeaState.framework/TeaState`

```diff

-1428.0.0.0.0
-  __TEXT.__text: 0x7ec80
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__const: 0x4c1c
-  __TEXT.__constg_swiftt: 0x2b9c
-  __TEXT.__swift5_typeref: 0x17fd
-  __TEXT.__swift5_reflstr: 0xc9b
-  __TEXT.__swift5_fieldmd: 0x17d4
+1463.0.0.0.0
+  __TEXT.__text: 0x85838
+  __TEXT.__const: 0x4cfc
+  __TEXT.__constg_swiftt: 0x2c78
+  __TEXT.__swift5_typeref: 0x183d
+  __TEXT.__swift5_reflstr: 0xd5b
+  __TEXT.__swift5_fieldmd: 0x18f8
   __TEXT.__swift5_assocty: 0x530
-  __TEXT.__swift5_capture: 0xaf4
-  __TEXT.__oslogstring: 0xd9e
+  __TEXT.__swift5_capture: 0xad0
+  __TEXT.__oslogstring: 0x102e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x30c
-  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift5_proto: 0x31c
+  __TEXT.__swift5_types: 0x1e4
   __TEXT.__swift_as_entry: 0xf4
   __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift5_protos: 0xc8
+  __TEXT.__swift_as_cont: 0x254
+  __TEXT.__swift5_protos: 0xcc
   __TEXT.__cstring: 0x60b
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1e48
-  __TEXT.__eh_frame: 0x4020
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x2ba
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x288
+  __TEXT.__unwind_info: 0x1ef0
+  __TEXT.__eh_frame: 0x3fa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x818
-  __AUTH_CONST.__const: 0x3bb0
-  __AUTH_CONST.__objc_const: 0xb90
+  __DATA_CONST.__objc_selrefs: 0x48
+  __DATA_CONST.__got: 0x2d0
+  __AUTH_CONST.__const: 0x3c88
+  __AUTH_CONST.__objc_const: 0xd48
+  __AUTH_CONST.__auth_got: 0x938
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x1148
-  __DATA.__data: 0x2718
+  __AUTH.__data: 0x1280
+  __DATA.__data: 0x28a0
   __DATA.__bss: 0x4fe0
-  __DATA.__common: 0x40
+  __DATA.__common: 0x71
   - /System/Library/Frameworks/Combine.framework/Combine
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88406DB1-9291-3B81-A59E-33D05F3C8032
-  Functions: 2322
-  Symbols:   159
-  CStrings:  130
+  UUID: 4E15614D-6037-30F3-92E4-4F94658DAEF9
+  Functions: 2361
+  Symbols:   186
+  CStrings:  89
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSUserDefaults
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_retain_x9
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x27
- _objc_retain_x20
- _swift_getOpaqueTypeMetadata2
- _swift_readAtKeyPath
- _swift_stdlib_isStackAllocationSafe
CStrings:
+ "(ValueReader in _D23218144BBD8F86575AD7D6956F47E7)"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "Dependency exists without value; returning default. Scope=%s, Key=%s"
+ "Dependency lookup in torn-down scope. Identifier=%s, RequestedScope=%s, DetachedScope=%s. Returning default value."
+ "Found dependency vertex without value; recording edge and using default. Scope=%s, Key=%s, Vertex=%s"
+ "Registering scope with parent that is not in the graph. Scope=%s, Parent=%s. This may indicate a detached scope."
+ "Skipping update of torn-down node (async). Node=%s"
+ "TeaStateLogEnable"
+ "XCODE_RUNNING_FOR_PREVIEWS"
+ "init DependencyGraph rootScope: %s"
- "**SF** init DependencyGraph rootScope: %s"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "_TtC8TeaState13RuleTaskQueue"
- "_TtC8TeaState13StorageHandle"
- "_TtC8TeaState15DependencyGraph"
- "_TtC8TeaState7Storage"
- "_TtC8TeaState9GraphDump"
- "callbacks"
- "commandActions"
- "commandHandlers"
- "continuation"
- "currentState"
- "currentThread"
- "currentlyUpdatingVertices"
- "dependencyContainer"
- "dependencyGraph"
- "description"
- "edges"
- "eventHandlers"
- "eventSubscriptions"
- "graph"
- "graphLock"
- "handler"
- "inflightExplicitUpdates"
- "init"
- "isMainThread"
- "lock"
- "pendingScopeDefinitions"
- "pendingScopeTeardowns"
- "pointee"
- "rootDependencyContainer"
- "rootScope"
- "ruleQueue"
- "ruleValue"
- "rulesPendingUpdate"
- "scope"
- "scopeParents"
- "scopeRuleSets"
- "scopeTags"
- "scopeVertices"
- "scopedDependencyContainers"
- "scopes"
- "storage"
- "subscope"
- "task"
- "truth"
- "unlock"
- "updateSignalHandler"
- "value"
- "vertexIdentifier"
- "vertices"

```
