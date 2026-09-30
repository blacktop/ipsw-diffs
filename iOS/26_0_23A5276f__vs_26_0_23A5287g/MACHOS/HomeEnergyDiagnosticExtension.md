## HomeEnergyDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/HomeEnergyDiagnosticExtension`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0x458
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x180
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x97
-  __TEXT.__oslogstring: 0x64
+347.0.0.0.0
+  __TEXT.__text: 0x26a8
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x309
+  __TEXT.__oslogstring: 0x54
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x134
+  __TEXT.__objc_methname: 0xeb
   __TEXT.__objc_methtype: 0x32
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x8
-  __DATA_CONST.__cfstring: 0x60
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0x42
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb8
+  __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0x70
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_data: 0x100
+  __DATA.__data: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E79C55D3-639B-33C8-9EC1-C9F859FBA869
-  Functions: 5
-  Symbols:   38
-  CStrings:  31
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: 916126B1-F8CA-33FA-AB0A-5578FBAF1EE0
+  Functions: 23
+  Symbols:   61
+  CStrings:  39
 
Symbols:
+ _MobileGestalt_copy_buildVersion_obj
+ _MobileGestalt_copy_modelNumber_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_NSObject
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ _memcpy
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_errorRelease
+ _swift_getErrorValue
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_release
+ _swift_willThrow
- _objc_enumerationMutation
- _objc_release_x22
- _objc_release_x25
- _objc_release_x28
- _objc_retain_x25
- _objc_retain_x8
CStrings:
+ "Compression Failed"
+ "Compression complete. File at "
+ "TYP,PAT,LNK,DEV,DAT,UID,GID,MOD,FLG,MTM,BTM,CTM"
+ "Unable to find directory."
+ "compress(directoryURL:) could not create a file path to the archive at "
+ "compress(directoryURL:) could not create a file path to the following directory "
+ "compress(directoryURL:) could not create a key set"
+ "compress(directoryURL:) could not create compression stream for "
+ "compress(directoryURL:) could not create encoding stream for "
+ "compress(directoryURL:) could not write directory to the encoding stream"
+ "compress(directoryURL:) could not write to file located at "
+ "copyCoreDataStoresWithUrl:"
+ "dealloc"
+ "init"
+ "temporaryDirectory"
- "HomeEnergyDiagnosticsDump.plist"
- "LocalCache.store"
- "Unable to find contents in directory: %@."
- "containsString:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"

```
