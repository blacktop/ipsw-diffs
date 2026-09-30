## ContactProvider

> `/System/Library/Frameworks/ContactProvider.framework/ContactProvider`

```diff

-22.0.0.0.0
-  __TEXT.__text: 0x276f0
-  __TEXT.__auth_stubs: 0xe80
+25.0.0.0.0
+  __TEXT.__text: 0x2786c
+  __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x1298
-  __TEXT.__swift5_typeref: 0x774
-  __TEXT.__swift5_fieldmd: 0x780
-  __TEXT.__constg_swiftt: 0xf34
+  __TEXT.__const: 0x1328
+  __TEXT.__swift5_typeref: 0x772
+  __TEXT.__swift5_fieldmd: 0x7b0
+  __TEXT.__constg_swiftt: 0xf54
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x5e5
+  __TEXT.__swift5_reflstr: 0x6a1
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__cstring: 0xed0
+  __TEXT.__cstring: 0xef1
+  __TEXT.__oslogstring: 0xbc3
+  __TEXT.__swift5_capture: 0x1d4
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__swift5_capture: 0x204
-  __TEXT.__oslogstring: 0x973
-  __TEXT.__unwind_info: 0xd70
-  __TEXT.__eh_frame: 0x1bf8
+  __TEXT.__unwind_info: 0xdd0
+  __TEXT.__eh_frame: 0x1e28
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x7f0
+  __TEXT.__objc_methname: 0x7db
   __TEXT.__objc_methtype: 0x100
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x740
-  __AUTH_CONST.__auth_ptr: 0x308
-  __AUTH_CONST.__const: 0xe38
-  __AUTH_CONST.__objc_const: 0x1ce8
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__auth_ptr: 0x300
+  __AUTH_CONST.__const: 0xdc0
+  __AUTH_CONST.__objc_const: 0x1d68
   __AUTH.__objc_data: 0x1c8
-  __AUTH.__data: 0x1008
-  __DATA.__data: 0x9b0
+  __AUTH.__data: 0x1068
+  __DATA.__data: 0x9a0
   __DATA.__bss: 0x1230
   __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1085
-  Symbols:   206
-  CStrings:  288
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1082
+  Symbols:   213
+  CStrings:  299
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x9
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "Closing transaction - %!{(MISSING)public}s"
+ "ContactItemEnumerator.invalidate() error %!{(MISSING)public}@"
+ "ExtensionHost.handleInvalidate() error %!{(MISSING)public}@"
+ "ExtensionHost.handleInvalidate() for %!{(MISSING)public}s"
+ "ItemChangeSession ended, throwing error %!{(MISSING)public}@"
+ "ItemChangeSession.sync() did fail to save"
+ "ItemChangeSession.sync() did timeout"
+ "ItemChangeSession.sync() error %!{(MISSING)public}@"
+ "ItemChangeSession.sync() will retry enumerating the sync anchor"
+ "ItemContentSession.enumerate() did fail to save"
+ "ItemContentSession.enumerate() did timeout"
+ "ItemContentSession.enumerate() error %!{(MISSING)public}@"
+ "ItemContentSession.enumerate() will retry enumerating the page"
+ "Opening transaction - %!{(MISSING)public}s"
+ "Synchronize reason: %!{(MISSING)public}s"
+ "The app invalidated the extension while it was enumerating content or changes."
+ "The extension can't run because the feature isn't available."
+ "The framework couldn't discover the app's extension."
+ "Transaction already closed - %!{(MISSING)public}s"
+ "Transaction left open - %!{(MISSING)public}s. Call complete() on this transaction!"
+ "_TtC15ContactProvider17ItemChangeSession"
+ "_TtC15ContactProvider18ItemContentSession"
+ "didSave() - sleeping %!{(MISSING)public}u seconds for %!{(MISSING)public}ld items"
+ "fetchContacts() - failed to fetch: %!{(MISSING)public}@"
+ "finishEnumeratingChangesWithError() - failed to save: %!{(MISSING)public}@"
+ "finishEnumeratingContentWithError() - failed to save: %!{(MISSING)public}@"
+ "handleSynchronize - caught error %!{(MISSING)public}@"
+ "isResetRequested = %!{(MISSING)bool,public}d, isContentEnumerated = %!{(MISSING)bool,public}d, isMoreComing = %!{(MISSING)bool,public}d, itemOffset = %!{(MISSING)public}ld"
+ "maxPageRetries"
+ "maxSyncAnchorRetries"
+ "pageRetryCount"
+ "resetProviderMetadata() - failed to save: %!{(MISSING)public}@"
+ "save() - did fail: %!{(MISSING)public}@"
+ "save() - did save"
+ "syncAnchorRetryCount"
+ "update contact items - failed contact diff: %!{(MISSING)public}@"
+ "update contact items - failed find update contact for identifier %!{(MISSING)public}s"
- "Closing transaction - %!s(MISSING)"
- "ContactItemEnumerator.invalidate() error %!@(MISSING)"
- "ExtensionHost.handleInvalidate() error %!@(MISSING)"
- "ExtensionHost.handleInvalidate() for %!s(MISSING)"
- "ItemChangeSession ended, throwing error %!@(MISSING)"
- "ItemChangeSession.sync() error %!@(MISSING)"
- "ItemContentSession.enumerate() error %!@(MISSING)"
- "Opening transaction - %!s(MISSING)"
- "Synchronize reason: %!s(MISSING)"
- "The extension cannot run because the feature is not available."
- "The extension was invalidated by the app while it was enumerating content or changes."
- "The framework could not discover the app's extension."
- "Transaction already closed - %!s(MISSING)"
- "Transaction left open - %!s(MISSING). Call complete() on this transaction!"
- "_TtC15ContactProviderP33_925121AD3E2DFF4C85D5A6218F4F9B0517ItemChangeSession"
- "_TtC15ContactProviderP33_925121AD3E2DFF4C85D5A6218F4F9B0518ItemContentSession"
- "didSave() - sleeping %!u(MISSING) seconds for %!l(MISSING)d items"
- "failed to reset provider metadata"
- "handleSynchronize - caught error %!@(MISSING)"
- "isResetRequested = %!{(MISSING)bool}d, isContentEnumerated = %!{(MISSING)bool}d, isMoreComing = %!{(MISSING)bool}d, itemAnchor = %!l(MISSING)d, itemOffset = %!l(MISSING)d"
- "save request was executed successfully"
- "setIsResetRequested:"
- "update contact items - failed contact diff: %!@(MISSING)"
- "update contact items - failed find update contact for identifier %!s(MISSING)"
- "update contact items - failed to fetch contacts: %!@(MISSING)"
- "update contact items - failed to save: %!@(MISSING)"

```
