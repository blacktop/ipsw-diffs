## managedappsd

> `/usr/libexec/managedappsd`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x818
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x42
-  __TEXT.__oslogstring: 0x8c
+105.0.0.0.0
+  __TEXT.__text: 0x119c
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_stubs: 0x60
+  __TEXT.__const: 0x52
+  __TEXT.__oslogstring: 0x63
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x66
-  __TEXT.__objc_methname: 0x13
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__swift5_typeref: 0xd
+  __TEXT.__cstring: 0x16
+  __TEXT.__objc_methname: 0x37
+  __TEXT.__unwind_info: 0x98
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x8
-  __DATA.__common: 0x30
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_selrefs: 0x18
+  __DATA.__data: 0x10
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore
   - /System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CAA1297B-94B1-3D05-BD9C-50AB6CC9F381
-  Functions: 6
-  Symbols:   44
-  CStrings:  10
+  UUID: CF7BF4C7-584E-39ED-A961-50E795BE19CF
+  Functions: 16
+  Symbols:   68
+  CStrings:  8
 
Symbols:
+ _$s20ManagedAppsInterface0aB19ServiceProcessLabelV4name5scopeSSAA0abD5ScopeO_tFZ
+ _$s20ManagedAppsInterface0aB19ServiceProcessLabelV5label5scopeSSAA0abD5ScopeO_tFZ
+ _$s2os6LoggerV20ManagedAppsInterfaceE07manageddB9ScopeNameSSvgZ
+ _$s2os6LoggerV20ManagedAppsInterfaceE07manageddB9ScopeNameSSvsZ
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS6appendyySSF
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSSN
+ _$sSa11descriptionSSvg
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$ss11CommandLineO9argumentsSaySSGvgZ
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss20__StaticArrayStorageCN
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss5UInt8VMn
+ _OBJC_CLASS_$_DMCSandboxUtilities
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ _malloc_size
+ _memcpy
+ _memmove
+ _swift_bridgeObjectRetain
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x23
+ _swift_retain_x23
+ _swift_unknownObjectRetain
- _$s20ManagedAppsInterface0aB15ServiceBundleIDV07managedB5AgentSSvgZ
- _$s20ManagedAppsInterface0aB15ServiceBundleIDV12managedappsdSSvgZ
- _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
- __set_user_dir_suffix
- _objc_release_x23
- _swift_retain
CStrings:
+ "%s running..."
+ "%s setup: services"
+ "===== %s's main... ====="
+ "===== launch args: %s ====="
+ "enterSandboxWithIdentifier:profile:"
- "===== managedappsd main... ====="
- "Fatal error"
- "_set_user_dir_suffix() failed!"
- "managedappsd running..."
- "managedappsd setup: sandbox"
- "managedappsd setup: services"
- "managedappsd/main.swift"

```
