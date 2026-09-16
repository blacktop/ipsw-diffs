## AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-41.0.50.0.0
-  __TEXT.__text: 0x383b4
-  __TEXT.__auth_stubs: 0x2120
-  __TEXT.__objc_stubs: 0x860
-  __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0x20d8
-  __TEXT.__swift5_typeref: 0xbe5
-  __TEXT.__cstring: 0x9a1
+41.1.9.0.0
+  __TEXT.__text: 0x3a030
+  __TEXT.__auth_stubs: 0x2160
+  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methlist: 0x414
+  __TEXT.__const: 0x21f8
+  __TEXT.__swift5_typeref: 0xc01
+  __TEXT.__cstring: 0x9f1
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0x135f
-  __TEXT.__objc_methtype: 0xa9c
+  __TEXT.__objc_methname: 0x141d
+  __TEXT.__objc_methtype: 0xb6c
   __TEXT.__constg_swiftt: 0x3c0
   __TEXT.__swift5_reflstr: 0x292
   __TEXT.__swift5_fieldmd: 0x2ac
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x70
-  __TEXT.__swift5_capture: 0x68c
-  __TEXT.__oslogstring: 0xdf4
+  __TEXT.__swift5_capture: 0x69c
+  __TEXT.__oslogstring: 0xe24
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift5_acfuncs: 0x1b8
-  __TEXT.__swift_as_entry: 0x1fc
-  __TEXT.__swift_as_ret: 0x274
-  __TEXT.__swift_as_cont: 0x324
+  __TEXT.__swift5_acfuncs: 0x1cc
+  __TEXT.__swift_as_entry: 0x214
+  __TEXT.__swift_as_ret: 0x294
+  __TEXT.__swift_as_cont: 0x354
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x16f8
-  __TEXT.__eh_frame: 0x3f68
-  __DATA_CONST.__const: 0x15c0
+  __TEXT.__unwind_info: 0x1780
+  __TEXT.__eh_frame: 0x42f0
+  __DATA_CONST.__const: 0x15f0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x1098
-  __DATA_CONST.__got: 0x850
-  __DATA_CONST.__auth_ptr: 0x5f0
-  __DATA.__objc_const: 0x620
-  __DATA.__objc_selrefs: 0x438
+  __DATA_CONST.__auth_got: 0x10b8
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__auth_ptr: 0x618
+  __DATA.__objc_const: 0x630
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_data: 0x1b8
-  __DATA.__data: 0xb00
-  __DATA.__common: 0x1d8
+  __DATA.__data: 0xb30
+  __DATA.__common: 0x1f0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1397
-  Symbols:   216
-  CStrings:  354
+  Functions: 1449
+  Symbols:   221
+  CStrings:  365
 
Symbols:
+ _LNMetadataProviderErrorDomain
+ _OBJC_CLASS_$_LNAutoShortcut
+ _OBJC_CLASS_$_LNStaticDeferredLocalizedString
+ _OBJC_CLASS_$_NSError
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
CStrings:
+ "Failed to tear down ephemeral services: %@"
+ "RunnerServiceDispatcher.updateAppShortcutParameters"
+ "autoShortcuts(forBundleIdentifier:localeIdentifier:)"
+ "autoShortcutsForBundleIdentifier:localeIdentifier:completion:"
+ "basePhraseTemplate"
+ "basePhraseTemplates"
+ "code"
+ "domain"
+ "key"
+ "openApplicationAndFetchListenerEndpointWithLaunchApplicationRequest:reply:"
+ "openApplicationWithLaunchApplicationRequest:reply:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@0:8@\"LNDaemonLaunchApplicationRequest\"16@?<v@?@\"LNConnectionListenerEndpoint\"@\"NSError\">24"
+ "v32@0:8@\"LNDaemonLaunchApplicationRequest\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"LNAppEntityContext\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSArray\"16@\"LNAppEntityContext\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "autoShortcuts(forLocaleIdentifier:)"
- "autoShortcutsForLocaleIdentifier:completion:"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
```
