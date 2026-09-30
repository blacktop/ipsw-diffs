## SoftwareUpdateSettings

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings`

```diff

-399.80.2.0.0
-  __TEXT.__text: 0x1d7e8
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0xd5c
-  __TEXT.__cstring: 0x200a
+412.100.1.0.0
+  __TEXT.__text: 0x1e2a0
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x10e4
+  __TEXT.__cstring: 0x1dba
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__oslogstring: 0x5d4
+  __TEXT.__oslogstring: 0x784
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__const: 0x3e4
   __TEXT.__swift5_typeref: 0x15a

   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0x29d
-  __TEXT.__objc_methname: 0x4163
+  __TEXT.__objc_methname: 0x4173
   __TEXT.__objc_methtype: 0xef5
-  __TEXT.__objc_stubs: 0x2e60
-  __DATA_CONST.__got: 0x378
+  __TEXT.__objc_stubs: 0x2e80
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x888
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1000
+  __DATA_CONST.__objc_selrefs: 0x11d8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x518
   __AUTH_CONST.__auth_ptr: 0x108
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x3328
+  __AUTH_CONST.__cfstring: 0x1c80
+  __AUTH_CONST.__objc_const: 0x2c88
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 520
-  Symbols:   609
-  CStrings:  1171
+  Functions: 514
+  Symbols:   612
+  CStrings:  1163
 
Symbols:
+ _objc_release_x26
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _NSLog
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _objc_release_x27
CStrings:
+ "Localizable-AgeAttestation"
+ "NO"
+ "PallasOverrides"
+ "YES"
+ "[SU Terms] %s: Failed to mark terms as disagreed in iCloud with HTTP status %ld"
+ "[SU Terms] %s: Failed to mark terms as disagreed in iCloud with error %{public}@"
+ "[SU Terms] %s: Marked terms as disagreed in iCloud"
+ "[SU Terms] %s: Reporting TOS action: %{public}@"
+ "[SU Terms] %s: Terms QFA feature flag disabled. Not reporting terms '%{public}@' action."
+ "[SU Terms] %s: Terms user action reporter unavailable. Not reporting terms '%{public}@' action."
+ "[SU Terms] Adding headers: %{public}@"
+ "[SU Terms] Downloading URL configuration for combined terms"
+ "[SU Terms] Error loading RemoteUI terms: %{public}@"
+ "[SU Terms] Failed to mark terms as agreed in iCloud: %{public}@"
+ "[SU Terms] Loading combined terms from %{public}@"
+ "[SU Terms] No terms on update asset"
+ "[SU Terms] Not showing terms because accepted version %{public}@ >= asset version: %{public}@"
+ "[SU Terms] Response = %{public}@"
+ "[SU Terms] SLA version in combined terms: %{public}@"
+ "[SU Terms] Submitting event for T&C interaction: %{public}@"
+ "[SU Terms] Terms accepted: %{public}@, error: %{public}@"
+ "[SU Terms] Terms config response does not contain the generic terms url"
+ "[SU Terms] Update asset license agreement has version: %{public}@, length %llu"
+ "[SU Terms] Using terms from the update asset"
+ "[SU Terms] iCloud Terms Dismissed via server"
+ "[SU Terms] terms dict = %{public}@"
+ "termsDictionary"
- "%s: Failed to mark terms as disagreed in iCloud with HTTP status %ld"
- "%s: Failed to mark terms as disagreed in iCloud with error %@"
- "%s: Marked terms as disagreed in iCloud"
- "%s: Reporting TOS action: %@"
- "%s: Terms QFA feature flag disabled. Not reporting terms '%@' action."
- "%s: Terms user action reporter unavailable. Not reporting terms '%@' action."
- "Error loading RemoteUI terms: %@"
- "Failed to mark terms as agreed in iCloud: %@"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "NERP"
- "Not showing terms because accepted version %@ >= asset version: %@"
- "SLA version in combined terms: %@"
- "SU Terms: Adding headers: %@"
- "SU Terms: Downloading URL configuration for combined terms"
- "SU Terms: Loading combined terms from %@"
- "SU Terms: No terms on update asset"
- "SU Terms: Update asset license agreement has version: %@, length %llu"
- "SoftwareUpdateSettings"
- "Submitting event for T&C interaction: %@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Terms accepted: %@, error: %@"
- "Terms config response did not contain a terms URL: %@"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "YASE"
- "iCloud Terms Dismissed via server"
- "invalid Collection: less than 'count' elements in collection"
- "v20@?0B8@\"NSError\"12"

```
