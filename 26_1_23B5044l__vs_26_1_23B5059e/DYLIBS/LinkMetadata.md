## LinkMetadata

> `/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata`

```diff

-300.1.7.0.0
-  __TEXT.__text: 0x10f378
+300.1.10.0.0
+  __TEXT.__text: 0x10f38c
   __TEXT.__auth_stubs: 0x2090
   __TEXT.__objc_methlist: 0x6be4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0xf860
+  __TEXT.__const: 0xf868
   __TEXT.__cstring: 0x9280
   __TEXT.__swift5_typeref: 0x44a8
   __TEXT.__constg_swiftt: 0x2954

   __TEXT.__swift5_fieldmd: 0x3ae4
   __TEXT.__swift5_assocty: 0x6a0
   __TEXT.__swift5_capture: 0x350
-  __TEXT.__oslogstring: 0xb33
+  __TEXT.__oslogstring: 0xc0b
   __TEXT.__swift5_proto: 0x1004
   __TEXT.__swift5_types: 0x44c
   __TEXT.__swift5_protos: 0x10

   __TEXT.__objc_methtype: 0x1a55
   __TEXT.__objc_stubs: 0x6bc0
   __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0xd48
+  __DATA_CONST.__const: 0xd50
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x80

   __AUTH_CONST.__objc_const: 0xca50
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH.__objc_data: 0xc10
-  __AUTH.__data: 0x638
+  __AUTH.__data: 0x528
   __DATA.__objc_ivar: 0x5f4
-  __DATA.__data: 0x2b38
-  __DATA.__bss: 0x145c8
+  __DATA.__data: 0x2a48
+  __DATA.__bss: 0x141a8
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x1ef0
-  __DATA_DIRTY.__data: 0x3290
-  __DATA_DIRTY.__bss: 0xc350
+  __DATA_DIRTY.__data: 0x3500
+  __DATA_DIRTY.__bss: 0xc750
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E307D995-9561-308F-9442-0376B9B42993
+  UUID: 93B933CB-36AE-3845-9C07-3287B8650CC7
   Functions: 7588
-  Symbols:   10958
-  CStrings:  4093
+  Symbols:   10960
+  CStrings:  4094
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_LinkMetadata
Functions:
~ sub_18eeee4c8 -> sub_18ef6e510 : 2348 -> 2364
~ sub_18eefa5b8 -> sub_18ef7a610 : 2224 -> 2228
CStrings:
+ "Failed to create framework record for: %{public}s"
+ "Failed to register daemon from: %{public}s"
+ "Found static metadata file at %{public}s for %{public}@"
+ "Importing the daemon record for %{public}s..."
+ "Importing the framework record for %{public}s..."
+ "Metadata for %{public}@ contains attribution bundle identifier but isn't entitled to do so"
+ "No static metadata directories found in %{public}s for %{public}@"
+ "Processing associated daemon records for %{public}s..."
+ "Processing associated standalone extension records for %{public}s..."
+ "Processing bundle metadata for %{public}s..."
+ "Processing embedded extension records for %{public}s..."
+ "The plist for %{public}s should contain MetadataAbsolutePaths"
+ "Unable to extract bundle metadata for %{public}s:\nempty extensionMetadata and daemonMetadata for URL %{public}s of %{public}@\""
+ "Undefined bundle identifier for %{public}@"
+ "→ Found standalone extension %{public}s attributed to %{public}s"
+ "→ Got a nil bundleIdentifier while enumerating standalone extensions attributed to %{public}s"
+ "→ No standalone extensions found for %{public}s"
- "Failed to create framework record for: %s"
- "Failed to register daemon from: %s"
- "Found static metadata file at %s for %@"
- "Importing the daemon record for %s..."
- "Importing the framework record for %s..."
- "Metadata for %@ contains attribution bundle identifier but isn't entitled to do so"
- "No static metadata directories found in %s for %@"
- "Processing associated daemon records for %s..."
- "Processing associated standalone extension records for %s..."
- "Processing bundle metadata for %s..."
- "Processing embedded extension records for %s..."
- "The plist for %s should contain MetadataAbsolutePaths"
- "Unable to extract bundle metadata for %s:\nempty extensionMetadata and daemonMetadata for URL %s of %@\""
- "→ Found standalone extension %s attributed to %s"
- "→ Got a nil bundleIdentifier while enumerating standalone extensions attributed to %s"
- "→ No standalone extensions found for %s"

```
