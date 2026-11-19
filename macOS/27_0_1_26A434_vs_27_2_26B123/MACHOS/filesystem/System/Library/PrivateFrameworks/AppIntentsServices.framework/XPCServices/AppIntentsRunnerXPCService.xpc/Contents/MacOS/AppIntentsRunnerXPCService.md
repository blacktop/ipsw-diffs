## AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/Contents/MacOS/AppIntentsRunnerXPCService`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_reflstr`
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
-  __TEXT.__text: 0x3a068
-  __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x424
-  __TEXT.__const: 0x20e8
-  __TEXT.__swift5_typeref: 0xbe5
-  __TEXT.__cstring: 0x9f1
+41.1.16.0.0
+  __TEXT.__text: 0x3a9d0
+  __TEXT.__auth_stubs: 0x1f60
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x43c
+  __TEXT.__const: 0x2202
+  __TEXT.__swift5_typeref: 0xc02
+  __TEXT.__cstring: 0xa6d
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0x1468
-  __TEXT.__objc_methtype: 0xb3c
+  __TEXT.__objc_methname: 0x14e6
+  __TEXT.__objc_methtype: 0xbfc
   __TEXT.__constg_swiftt: 0x3c0
   __TEXT.__swift5_reflstr: 0x292
   __TEXT.__swift5_fieldmd: 0x2ac
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x70
-  __TEXT.__swift5_capture: 0x70c
-  __TEXT.__oslogstring: 0xf14
+  __TEXT.__swift5_capture: 0x71c
+  __TEXT.__oslogstring: 0xf48
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift5_acfuncs: 0x1b8
-  __TEXT.__swift_as_entry: 0x1fc
-  __TEXT.__swift_as_ret: 0x274
-  __TEXT.__swift_as_cont: 0x324
+  __TEXT.__swift5_acfuncs: 0x1cc
+  __TEXT.__swift_as_entry: 0x214
+  __TEXT.__swift_as_ret: 0x298
+  __TEXT.__swift_as_cont: 0x35c
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__eh_frame: 0x3f50
-  __DATA_CONST.__const: 0x1700
+  __TEXT.__unwind_info: 0x1780
+  __TEXT.__eh_frame: 0x42c0
+  __DATA_CONST.__const: 0x1738
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0xf48
-  __DATA_CONST.__got: 0x870
-  __DATA_CONST.__auth_ptr: 0x5f0
-  __DATA.__objc_const: 0x638
-  __DATA.__objc_selrefs: 0x468
+  __DATA_CONST.__auth_got: 0xfb8
+  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__auth_ptr: 0x620
+  __DATA.__objc_const: 0x648
+  __DATA.__objc_selrefs: 0x480
   __DATA.__objc_data: 0x1b8
-  __DATA.__data: 0xb20
-  __DATA.__common: 0x1d8
+  __DATA.__data: 0xb08
+  __DATA.__common: 0x148
   __DATA.__bss: 0xb80
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/Versions/A/XPCDistributed
+  - /System/Library/PrivateFrameworks/_AppIntentsServices_AppIntents.framework/Versions/A/_AppIntentsServices_AppIntents
   - /System/Library/PrivateFrameworks/_AppIntentsServices_ToolKit.framework/Versions/A/_AppIntentsServices_ToolKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1429
-  Symbols:   171
-  CStrings:  370
+  Functions: 1465
+  Symbols:   175
+  CStrings:  378
 
Symbols:
+ _LNMetadataProviderErrorDomain
+ _OBJC_CLASS_$_LNAutoShortcut
+ _OBJC_CLASS_$_LNStaticDeferredLocalizedString
+ _OBJC_CLASS_$_NSError
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
- _OBJC_CLASS_$_LNConnectionPolicySignals
- _swift_conformsToProtocol2
CStrings:
+ "%sCannot cancel execution: executor is nil"
+ "%sReceived environmentForViewSnippet request"
+ "%sReceived preferredContentSizeForViewSnippet request"
+ "%sResponding to environment for view snippet | snippetEnvironment=%@"
+ "%sResponding to preferred content size for view snippet | size=%s"
+ "ClientSessionGracePeriod"
+ "ExecutionResultRetention"
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
- "Cannot cancel execution: executor is nil"
- "[%s] Received environmentForViewSnippet request"
- "[%s] Received preferredContentSizeForViewSnippet request"
- "[%s] Responding to environment for view snippet | snippetEnvironment=%@"
- "[%s] Responding to preferred content size for view snippet | size=%s"
- "autoShortcuts(forLocaleIdentifier:)"
- "autoShortcutsForLocaleIdentifier:completion:"
- "policyWithActionMetadata:"
- "policyWithActionMetadata:signals:"
- "policyWithEntityMetadata:"
- "runnerDispatcher"
- "setPreferredBundleIdentifier:"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
```
