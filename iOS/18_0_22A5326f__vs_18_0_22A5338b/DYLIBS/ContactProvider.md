## ContactProvider

> `/System/Library/Frameworks/ContactProvider.framework/ContactProvider`

```diff

-24.0.0.0.0
-  __TEXT.__text: 0x279e4
-  __TEXT.__auth_stubs: 0xe40
+25.0.0.0.0
+  __TEXT.__text: 0x2786c
+  __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x1328
   __TEXT.__swift5_typeref: 0x772

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__cstring: 0xf01
-  __TEXT.__oslogstring: 0xb03
+  __TEXT.__cstring: 0xef1
+  __TEXT.__oslogstring: 0xbc3
   __TEXT.__swift5_capture: 0x1d4
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__unwind_info: 0xdd0
   __TEXT.__eh_frame: 0x1e28
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x7f0
+  __TEXT.__objc_methname: 0x7db
   __TEXT.__objc_methtype: 0x100
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__auth_ptr: 0x308
   __AUTH_CONST.__const: 0xdc0
   __AUTH_CONST.__objc_const: 0x1d68

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1084
-  Symbols:   212
-  CStrings:  300
+  Functions: 1082
+  Symbols:   213
+  CStrings:  299
 
Symbols:
+ _objc_release_x9
CStrings:
+ "Closing transaction - %!{(MISSING)public}s"
+ "ContactItemEnumerator.invalidate() error %!{(MISSING)public}@"
+ "ExtensionHost.handleInvalidate() error %!{(MISSING)public}@"
+ "ExtensionHost.handleInvalidate() for %!{(MISSING)public}s"
+ "ItemChangeSession ended, throwing error %!{(MISSING)public}@"
+ "ItemChangeSession.sync() error %!{(MISSING)public}@"
+ "ItemContentSession.enumerate() error %!{(MISSING)public}@"
+ "Opening transaction - %!{(MISSING)public}s"
+ "Synchronize reason: %!{(MISSING)public}s"
+ "The app invalidated the extension while it was enumerating content or changes."
+ "The extension can't run because the feature isn't available."
+ "The framework couldn't discover the app's extension."
+ "Transaction already closed - %!{(MISSING)public}s"
+ "Transaction left open - %!{(MISSING)public}s. Call complete() on this transaction!"
+ "didSave() - sleeping %!{(MISSING)public}u seconds for %!{(MISSING)public}ld items"
+ "fetchContacts() - failed to fetch: %!{(MISSING)public}@"
+ "finishEnumeratingChangesWithError() - failed to save: %!{(MISSING)public}@"
+ "finishEnumeratingContentWithError() - failed to save: %!{(MISSING)public}@"
+ "handleSynchronize - caught error %!{(MISSING)public}@"
+ "isResetRequested = %!{(MISSING)bool,public}d, isContentEnumerated = %!{(MISSING)bool,public}d, isMoreComing = %!{(MISSING)bool,public}d, itemOffset = %!{(MISSING)public}ld"
+ "resetProviderMetadata() - failed to save: %!{(MISSING)public}@"
+ "save() - did fail: %!{(MISSING)public}@"
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
- "didSave() - sleeping %!u(MISSING) seconds for %!l(MISSING)d items"
- "fetchContacts() - failed to fetch: %!@(MISSING)"
- "finishEnumeratingChangesWithError() - failed to save: %!@(MISSING)"
- "finishEnumeratingContentWithError() - failed to save: %!@(MISSING)"
- "handleSynchronize - caught error %!@(MISSING)"
- "isResetRequested = %!{(MISSING)bool}d, isContentEnumerated = %!{(MISSING)bool}d, isMoreComing = %!{(MISSING)bool}d, itemAnchor = %!l(MISSING)d, itemOffset = %!l(MISSING)d"
- "resetProviderMetadata() - failed to save: %!@(MISSING)"
- "save() - did fail: %!@(MISSING)"
- "setIsResetRequested:"
- "update contact items - failed contact diff: %!@(MISSING)"
- "update contact items - failed find update contact for identifier %!s(MISSING)"

```
