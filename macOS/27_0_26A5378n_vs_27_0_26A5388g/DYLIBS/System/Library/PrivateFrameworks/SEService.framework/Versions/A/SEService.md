## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-70.35.1.0.0
-  __TEXT.__text: 0xe9d18
-  __TEXT.__objc_methlist: 0x32b0
-  __TEXT.__const: 0x160a0
-  __TEXT.__cstring: 0x6a65
-  __TEXT.__oslogstring: 0x1d77
+70.37.0.0.0
+  __TEXT.__text: 0xea114
+  __TEXT.__objc_methlist: 0x32d8
+  __TEXT.__const: 0x160b0
+  __TEXT.__cstring: 0x6b35
+  __TEXT.__oslogstring: 0x1e17
   __TEXT.__gcc_except_tab: 0x107c
   __TEXT.__swift5_typeref: 0x3c98
   __TEXT.__constg_swiftt: 0x3304

   __TEXT.__swift_as_cont: 0x2f0
   __TEXT.__swift5_capture: 0xf8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x4548
+  __TEXT.__unwind_info: 0x4560
   __TEXT.__eh_frame: 0x5820
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcb0
+  __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15a0
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x9d28
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x6d08
+  __AUTH_CONST.__cfstring: 0x35e0
+  __AUTH_CONST.__objc_const: 0x6d10
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x48

   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/Versions/A/OctagonTrust

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6211
-  Symbols:   4491
-  CStrings:  1020
+  Functions: 6214
+  Symbols:   4503
+  CStrings:  1029
 
Symbols:
+ -[SEProxyWithManagerSession _checkPairing:]
+ -[SEProxyWithManagerSession validatePairing:callback:]
+ -[SEProxyWithRemoteTransceiver validatePairing:callback:]
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_SEService
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SEService
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SEService
+ _objc_msgSend$_checkPairing:
+ _objc_msgSend$deleteAllApplets:error:
+ _objc_msgSend$validateSEPairings:
CStrings:
+ "Failed pairing check 1"
+ "Failed to deleteAllApplets"
+ "Failed to recheck after deleteAll %d %@"
+ "Got ambiguous pairing result %d"
+ "Missing key and/or applet identifier"
+ "Missing key identifier"
+ "Pairing state (after) %{public}x / %{public}@"
+ "Pairing state (before) %{public}x / %{public}@"
+ "STSRemoteTransceiver doesn't support validatePairing"
+ "Validate pairing re-paired with result %{public}d / %{public}@"
- "Invalid reader ID"
```
