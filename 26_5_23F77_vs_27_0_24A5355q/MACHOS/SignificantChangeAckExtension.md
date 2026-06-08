## SignificantChangeAckExtension

> `/System/Library/ExtensionKit/Extensions/SignificantChangeAckExtension.appex/SignificantChangeAckExtension`

```diff

-254.575.9.0.0
-  __TEXT.__text: 0x9744
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__const: 0x888
-  __TEXT.__constg_swiftt: 0x298
-  __TEXT.__swift5_typeref: 0x3e1
-  __TEXT.__swift5_fieldmd: 0x1b4
+279.3.1.2.0
+  __TEXT.__text: 0xa268
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x160
+  __TEXT.__const: 0x738
+  __TEXT.__constg_swiftt: 0x274
+  __TEXT.__swift5_typeref: 0x43d
+  __TEXT.__swift5_fieldmd: 0x180
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x38
-  __TEXT.__cstring: 0x247
-  __TEXT.__objc_methtype: 0x44
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__objc_classname: 0x31
-  __TEXT.__objc_methname: 0x1d5
-  __TEXT.__swift5_reflstr: 0x181
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__swift5_capture: 0xfc
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__cstring: 0x29e
+  __TEXT.__objc_methtype: 0x43
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__swift5_reflstr: 0x141
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__oslogstring: 0x3e9
   __TEXT.__swift5_assocty: 0x80
-  __TEXT.__oslogstring: 0x1c2
+  __TEXT.__swift5_capture: 0xac
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x390
-  __TEXT.__eh_frame: 0x720
-  __DATA_CONST.__auth_got: 0x598
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__auth_ptr: 0x278
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__objc_methname: 0xff
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__eh_frame: 0x710
+  __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xf0
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2b0
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x4e8
+  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_ptr: 0x268
+  __DATA.__objc_selrefs: 0x58
+  __DATA.__data: 0x288
+  __DATA.__common: 0x18
+  __DATA.__bss: 0x428
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 31C62BC1-DBFF-38A9-8A84-9EE17727905F
-  Functions: 254
+  UUID: 7ABFEF0E-7536-3B88-AE34-83902FEBF312
+  Functions: 214
   Symbols:   136
-  CStrings:  52
+  CStrings:  53
 
Symbols:
+ _objc_release
+ _objc_release_x25
+ _objc_retain_x25
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x24
+ _swift_retain_x9
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __Block_copy
- __Block_release
- __objc_empty_cache
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_release_x27
- _objc_release_x8
- _objc_retain_x27
- _swift_bridgeObjectRetain_n
- _swift_deallocClassInstance
- _swift_deletedMethodError
- _swift_getKeyPath
- _swift_retain_n
- _swift_updateClassMetadata2
CStrings:
+ "%s - called for %s"
+ "Failed to fetch age verification info."
+ "Failed to fetch region information: %@"
+ "Failed to get account info."
+ "SignificantChange context is nil, returning."
+ "SignificantChangeAckExtensionContext is nil, returning without initializing SignificantChangeSheet"
+ "SignificantChangeMetadata - appName: %s, regionID: %s, developerText: %s"
+ "Terminate called"
+ "XPC connection and sigchange context is available, creating client metadata and host context."
+ "XPC connection is nil, returning."
+ "com.apple.developer.declared-age-range"
+ "createMetadata(context:)"
- "Missing context from host."
- "_$observationRegistrar"
- "_TtC29SignificantChangeAckExtension11HostContext"
- "_developerString"
- "_hostAppName"
- "_hostBundleIdentifier"
- "iTunesMetadata"
- "id"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "localizedName"
- "storeItemIdentifier"

```
