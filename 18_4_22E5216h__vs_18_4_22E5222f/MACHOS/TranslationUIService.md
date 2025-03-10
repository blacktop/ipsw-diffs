## TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

```diff

-300.8.0.0.0
-  __TEXT.__text: 0x497fc
-  __TEXT.__auth_stubs: 0x2030
-  __TEXT.__objc_methlist: 0x43c
-  __TEXT.__const: 0x24e0
-  __TEXT.__constg_swiftt: 0xd64
-  __TEXT.__swift5_typeref: 0x5058
+300.11.0.0.0
+  __TEXT.__text: 0x4bfa4
+  __TEXT.__auth_stubs: 0x2170
+  __TEXT.__objc_methlist: 0x444
+  __TEXT.__const: 0x25b0
+  __TEXT.__constg_swiftt: 0xe68
+  __TEXT.__swift5_typeref: 0x517a
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xd5a
-  __TEXT.__swift5_fieldmd: 0xa38
-  __TEXT.__swift5_assocty: 0x2e0
-  __TEXT.__objc_methname: 0xd2a
-  __TEXT.__swift5_proto: 0xb0
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__cstring: 0x1028
+  __TEXT.__swift5_reflstr: 0xdba
+  __TEXT.__swift5_fieldmd: 0xa7c
+  __TEXT.__swift5_assocty: 0x2c8
+  __TEXT.__objc_methname: 0xdd7
+  __TEXT.__swift5_proto: 0xac
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__cstring: 0x10b8
   __TEXT.__objc_classname: 0xa8
   __TEXT.__objc_methtype: 0x1d8
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__oslogstring: 0xc89
-  __TEXT.__swift5_capture: 0x5d8
-  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__oslogstring: 0xdd9
+  __TEXT.__swift5_capture: 0x61c
+  __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0xe00
-  __TEXT.__eh_frame: 0xee8
-  __DATA_CONST.__auth_got: 0x1018
-  __DATA_CONST.__got: 0x728
-  __DATA_CONST.__auth_ptr: 0x940
-  __DATA_CONST.__const: 0x1488
+  __TEXT.__unwind_info: 0xeb8
+  __TEXT.__eh_frame: 0xff8
+  __DATA_CONST.__auth_got: 0x10b8
+  __DATA_CONST.__got: 0x760
+  __DATA_CONST.__auth_ptr: 0x950
+  __DATA_CONST.__const: 0x1508
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0xdd8
-  __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_data: 0x820
-  __DATA.__data: 0x22f8
-  __DATA.__bss: 0x18a0
-  __DATA.__common: 0x118
+  __DATA.__objc_const: 0xe98
+  __DATA.__objc_selrefs: 0x520
+  __DATA.__objc_data: 0x978
+  __DATA.__data: 0x2360
+  __DATA.__bss: 0x1860
+  __DATA.__common: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/Translation.framework/Translation

   - /System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1287
-  Symbols:   226
-  CStrings:  385
+  Functions: 1322
+  Symbols:   236
+  CStrings:  411
 
Symbols:
+ _OBJC_CLASS_$_NEPolicy
+ _OBJC_CLASS_$_NEPolicyCondition
+ _OBJC_CLASS_$_NEPolicyResult
+ _OBJC_CLASS_$_NEPolicySession
+ _OBJC_CLASS_$_NSRunLoop
+ _audit_token_to_pid
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_storeStrong
+ _swift_getObjCClassFromMetadata
CStrings:
+ "App record info plist: %s"
+ "Network restriction policy was not applied."
+ "Restricting network access for process %d"
+ "Unable to obtain an AppExtensionProcess"
+ "Will translate %ld characters, replacementAllowed: %{bool}d"
+ "_policySession"
+ "_serviceModel"
+ "_shouldDismiss"
+ "_shouldExpand"
+ "_subscriptions"
+ "_translation"
+ "addPolicy:"
+ "allInterfaces"
+ "apply"
+ "boolValue"
+ "call to restrict network accdess when a policy session already exists."
+ "com.apple.developer.translation-ui-provider.network-access"
+ "drop"
+ "effectivePID:"
+ "in _willAppearInRemoteViewController"
+ "in onChange of shouldExpand: %{bool}d"
+ "in onChange of translation: %ld"
+ "in rootView()"
+ "infoDictionary"
+ "initWithOrder:result:conditions:"
+ "mainRunLoop"
+ "objectForKey:ofClass:"
+ "removeAllPolicies"
+ "setPriority:"
- "Have source string (length: %ld)"
- "Request for string to translate was nil."
- "Will translate %ld characters"

```
