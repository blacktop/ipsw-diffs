## APConfigurationSystem

> `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem`

```diff

-556.0.60.0.0
-  __TEXT.__text: 0xda70
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0xc2c
-  __TEXT.__const: 0xe98
-  __TEXT.__cstring: 0xee7
-  __TEXT.__oslogstring: 0xa6d
+556.0.65.1.0
+  __TEXT.__text: 0xb75c
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0xc14
+  __TEXT.__const: 0xbb8
+  __TEXT.__cstring: 0xda7
+  __TEXT.__oslogstring: 0xa8d
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__swift5_typeref: 0x37c
-  __TEXT.__swift5_capture: 0x70
-  __TEXT.__constg_swiftt: 0x4f8
-  __TEXT.__swift5_reflstr: 0x2bf
-  __TEXT.__swift5_fieldmd: 0x3e8
-  __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x4b0
-  __TEXT.__eh_frame: 0x188
-  __TEXT.__objc_classname: 0x47d
-  __TEXT.__objc_methname: 0x1b9a
+  __TEXT.__swift5_typeref: 0x2c0
+  __TEXT.__swift5_fieldmd: 0x328
+  __TEXT.__constg_swiftt: 0x3dc
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_reflstr: 0x23f
+  __TEXT.__swift5_proto: 0x90
+  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__eh_frame: 0x108
+  __TEXT.__objc_classname: 0x49b
+  __TEXT.__objc_methname: 0x1b7c
   __TEXT.__objc_methtype: 0x387
-  __TEXT.__objc_stubs: 0x1520
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__objc_stubs: 0x1500
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x6f8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x520
-  __AUTH_CONST.__const: 0x7d0
-  __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x3310
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__const: 0x550
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x3270
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x1d8
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x190
   __DATA.__objc_ivar: 0x58
-  __DATA.__data: 0x3d8
-  __DATA.__bss: 0x1180
-  __DATA_DIRTY.__objc_data: 0xc68
-  __DATA_DIRTY.__data: 0x390
+  __DATA.__data: 0x368
+  __DATA.__bss: 0xd80
+  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__data: 0x2b0
   __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8CE6B5C5-AC87-33A0-B582-CFD44B8411EE
-  Functions: 469
-  Symbols:   278
-  CStrings:  729
+  UUID: C6CA107F-05E9-3CEB-B597-3A8CAFA8556D
+  Functions: 389
+  Symbols:   263
+  CStrings:  723
 
Symbols:
+ _OBJC_CLASS_$_APFeatureFlagsEnforcingConfig
+ _OBJC_METACLASS_$_APFeatureFlagsEnforcingConfig
- _OBJC_CLASS_$_APConfigurationSharedStorageUpdater
- _OBJC_METACLASS_$_APConfigurationSharedStorageUpdater
- __swiftEmptyDictionarySingleton
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _bzero
- _malloc_size
- _memmove
- _objc_allocWithZone
- _swift_bridgeObjectRetain
- _swift_bridgeObjectRetain_n
- _swift_deallocPartialClassInstance
- _swift_getObjectType
- _swift_isUniquelyReferenced_nonNull_native
- _swift_isaMask
CStrings:
+ "APFeatureFlagsEnforcingConfig"
+ "FeatureFlag/Enforcing"
+ "Using canned data: %@"
+ "configurationSystemPayloadOverride"
+ "delay"
+ "restartEnabled"
+ "retryTimeout"
- "APConfigurationSharedStorageUpdater"
- "APConfigurationSystem/ConfigurationSharedStorage.swift"
- "ConfigurationSharedStorageKey"
- "Failed to retrieve user defaults for Configuration System suite."
- "Fatal error"
- "_TtC21APConfigurationSystem38ConfigurationSharedStorageDataProvider"
- "com.apple.AdPlatforms"
- "dealloc"
- "dictionaryForKey:"
- "setObject:forKey:"
- "sharedStorage"
- "storage"
- "updateSharedStorage"

```
